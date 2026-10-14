//
//  AtlasStore.swift
//  Anatomy
//

import Foundation
import Observation

/// Latin name and reference text for a Z-Anatomy term, keyed by its English name.
nonisolated struct GlossaryTerm: Decodable, Sendable {
    let la: String?
    let def: String?
}

/// Turkish name, corrected Latin name and short Turkish description of a 3D
/// part or model group (terms.json, tools/content/terms).
nonisolated struct PartTerm: Decodable, Sendable {
    let tr: String
    let la: String?
    let d: String?
}

/// Read-only access to the written atlas content and the 3D glossary.
@MainActor
@Observable
final class AtlasStore {
    let systems: [BodySystem]
    let entries: [AtlasEntry]
    /// Turkish dictionary of every part and group, keyed by lowercased English name.
    let terms: [String: PartTerm]
    private(set) var glossary: [String: GlossaryTerm] = [:]

    @ObservationIgnored private let byID: [String: AtlasEntry]
    @ObservationIgnored private let byModel: [String: String]
    @ObservationIgnored private let searchIndex: [(entry: AtlasEntry, haystack: String)]

    init() {
        let decoder = JSONDecoder()
        var systems: [BodySystem] = []
        if let url = Bundle.main.url(forResource: "atlas-systems", withExtension: "json"),
           let data = try? Data(contentsOf: url) {
            do {
                systems = try decoder.decode([BodySystem].self, from: data)
            } catch {
                assertionFailure("atlas-systems.json: \(error)")
            }
        }
        self.systems = systems

        var entries: [AtlasEntry] = []
        for system in systems {
            guard let url = Bundle.main.url(forResource: "atlas-\(system.id)", withExtension: "json"),
                  let data = try? Data(contentsOf: url) else { continue }
            do {
                let file = try decoder.decode(EntryFile.self, from: data)
                entries += file.entries.map { entry in
                    var entry = entry
                    entry.systemID = system.id
                    return entry
                }
            } catch {
                assertionFailure("atlas-\(system.id).json: \(error)")
            }
        }
        self.entries = entries

        if let url = Bundle.main.url(forResource: "terms", withExtension: "json"),
           let data = try? Data(contentsOf: url),
           let map = try? decoder.decode([String: PartTerm].self, from: data) {
            terms = map
        } else {
            terms = [:]
        }

        var byID: [String: AtlasEntry] = [:]
        var byModel: [String: String] = [:]
        for entry in entries {
            byID[entry.id] = entry
            for model in entry.models where byModel[model.lowercased()] == nil {
                byModel[model.lowercased()] = entry.id
            }
        }
        self.byID = byID
        self.byModel = byModel
        searchIndex = entries.map { entry in
            let text = ([entry.tr, entry.la, entry.en, entry.group] + entry.aliases).joined(separator: " ")
            return (entry, SearchText.fold(text))
        }
    }

    private struct EntryFile: Decodable {
        let entries: [AtlasEntry]
    }

    func loadGlossary() async {
        guard glossary.isEmpty else { return }
        let terms = await Task.detached(priority: .utility) { () -> [String: GlossaryTerm] in
            guard let url = Bundle.main.url(forResource: "glossary", withExtension: "json"),
                  let data = try? Data(contentsOf: url) else { return [:] }
            return (try? JSONDecoder().decode([String: GlossaryTerm].self, from: data)) ?? [:]
        }.value
        glossary = terms
    }

    // MARK: Lookup

    func entry(_ id: String) -> AtlasEntry? { byID[id] }

    func system(_ id: String) -> BodySystem? { systems.first { $0.id == id } }

    func entries(in systemID: String) -> [AtlasEntry] {
        entries.filter { $0.systemID == systemID }
    }

    /// Entries of a system grouped in the order the system declares.
    func groups(in system: BodySystem) -> [(title: String, entries: [AtlasEntry])] {
        let list = entries(in: system.id)
        var order = system.groups
        for entry in list where !order.contains(entry.group) { order.append(entry.group) }
        return order.compactMap { group in
            let items = list.filter { $0.group == group }
            return items.isEmpty ? nil : (group, items)
        }
    }

    /// The written entry describing a 3D part: the part itself, or the closest
    /// ancestor group that has an entry.
    func entry(for part: PartInfo) -> AtlasEntry? {
        if let id = byModel[part.base.lowercased()] { return byID[id] }
        for ancestor in part.path.reversed() {
            if let id = byModel[ancestor.lowercased()] { return byID[id] }
        }
        return nil
    }

    /// Whether `part` is described by `entry` exactly (not through an ancestor).
    func isExact(_ entry: AtlasEntry, for part: PartInfo) -> Bool {
        byModel[part.base.lowercased()] == entry.id
    }

    func term(_ englishName: String) -> GlossaryTerm? {
        glossary[englishName.lowercased()]
    }

    /// The Turkish dictionary entry for a part or group name.
    func partTerm(_ englishName: String) -> PartTerm? {
        terms[englishName.lowercased()]
    }

    func latinName(for part: PartInfo) -> String? {
        latinName(part.base) ?? entry(for: part).flatMap { isExact($0, for: part) ? $0.la : nil }
    }

    /// Latin name of a part or group: the corrected dictionary form first,
    /// then Terminologia Anatomica via the glossary.
    func latinName(_ englishName: String) -> String? {
        partTerm(englishName)?.la ?? term(englishName)?.la
    }

    /// Best display name for a 3D part: its own Turkish name, then the
    /// written entry that describes exactly this part, then Latin.
    func displayName(for part: PartInfo) -> String {
        if let tr = partTerm(part.base)?.tr { return tr }
        if let entry = entry(for: part), isExact(entry, for: part) { return entry.tr }
        return term(part.base)?.la ?? part.base
    }

    /// Turkish name of a model group (a folder in the parts browser).
    func groupName(_ englishName: String) -> String {
        partTerm(englishName)?.tr ?? term(englishName)?.la ?? englishName
    }

    /// Short Turkish description of a part or group.
    func partDescription(_ englishName: String) -> String? {
        partTerm(englishName)?.d
    }

    func related(of entry: AtlasEntry) -> [AtlasEntry] {
        entry.related.compactMap { byID[$0] }
    }

    // MARK: Search

    func search(_ query: String, limit: Int = 60) -> [AtlasEntry] {
        let q = SearchText.fold(query)
        guard !q.isEmpty else { return [] }
        let words = q.split(separator: " ").map(String.init)
        var scored: [(Int, AtlasEntry)] = []
        for (entry, hay) in searchIndex where words.allSatisfy({ hay.contains($0) }) {
            var score = 0
            let names = [entry.tr, entry.la, entry.en].map(SearchText.fold)
            if names.contains(q) { score += 100 }
            if names.contains(where: { $0.hasPrefix(q) }) { score += 40 }
            score -= hay.count / 40
            scored.append((score, entry))
        }
        return scored.sorted { $0.0 > $1.0 }.prefix(limit).map(\.1)
    }
}

enum SearchText {
    /// Lowercases and removes Turkish / Latin diacritics so "kalp", "KALP" and
    /// "kalp" match, as do "ş" and "s", "ı" and "i".
    nonisolated static func fold(_ text: String) -> String {
        text
            .folding(options: [.caseInsensitive, .diacriticInsensitive], locale: Locale(identifier: "en_US"))
            .replacingOccurrences(of: "ı", with: "i")
            .lowercased()
            .trimmingCharacters(in: .whitespacesAndNewlines)
    }
}
