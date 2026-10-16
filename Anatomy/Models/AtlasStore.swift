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
        let q = SearchQuery(query)
        guard !q.isEmpty else { return [] }
        let words = q.forms[0].split(separator: " ")
        var scored: [(Int, AtlasEntry)] = []
        for (entry, hay) in searchIndex {
            var score = q.score([entry.tr, entry.la, entry.en] + entry.aliases)
            if score == 0 {
                // Words found anywhere in the entry (its group, its aliases).
                guard words.allSatisfy({ hay.contains($0) }) || q.score(folded: hay) > 0 else { continue }
                score = 5
            }
            scored.append((score - hay.count / 40, entry))
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

    /// Lowercased with the diacritics kept ("diş", not "dış").
    nonisolated static func typed(_ text: String) -> String {
        text.lowercased(with: Locale(identifier: "tr_TR")).trimmingCharacters(in: .whitespacesAndNewlines)
    }
}

/// A search query matched the way people type Turkish: diacritics are
/// optional, word endings are ignored ("bilek" finds "el bileği", "lenf
/// düğümü" finds "lenf düğümleri") and a few everyday words find the terms
/// the names use ("atardamar" finds the arteries).
nonisolated struct SearchQuery: Sendable {
    /// The folded query, then its everyday-word replacements.
    let forms: [String]
    /// Per form, per word: the beginnings a word of the name may have.
    private let stems: [[Beginning]]
    /// As typed: "diş" ranks the teeth over "dış karotis".
    private let typed: String
    /// Whether the query has Turkish letters, which then count.
    private let marked: Bool

    /// Everyday words (folded) and the word the names use instead.
    private static let everyday: [(String, String)] = [
        ("atardamarlar", "arter"), ("atardamar", "arter"), ("toplardamarlar", "ven"), ("toplardamar", "ven"),
        ("apandis", "apendiks"), ("legen kemigi", "kalca kemigi"), ("legen", "pelvis"), ("pazi", "biseps"),
        ("incik", "kaval"), ("nefes borusu", "soluk borusu"), ("koltuk alti", "aksiller"),
        ("omurilik sogani", "medulla oblongata"), ("dol yatagi", "rahim"), ("goz bebegi", "pupilla"),
        ("bademcik", "tonsil"), ("husye", "testis"), ("yumurtalik", "over"),
    ]

    init(_ text: String) {
        let folded = SearchText.fold(text)
        var forms = [folded]
        for (word, term) in Self.everyday where (" " + folded + " ").contains(" " + word + " ") {
            let form = (" " + folded + " ").replacingOccurrences(of: " " + word + " ", with: " " + term + " ")
                .trimmingCharacters(in: .whitespaces)
            if !forms.contains(form) { forms.append(form) }
        }
        self.forms = forms
        stems = forms.map { $0.split(separator: " ").map { Self.beginning(of: String($0)) } }
        typed = SearchText.typed(text)
        marked = typed != folded
    }

    var isEmpty: Bool { forms[0].isEmpty }
    var count: Int { forms[0].count }

    /// How well `names` (Turkish, Latin, English…) match, 0 when they do not.
    func score(_ names: [String]) -> Int {
        score(folded: names.map(SearchText.fold), typed: names.map(SearchText.typed))
    }

    /// The same for names already folded and lowercased (search indexes).
    func score(folded: [String], typed names: [String]) -> Int {
        var best = 0
        for (name, typedName) in zip(folded, names) where !name.isEmpty {
            var s = score(folded: name)
            if s > 0 {
                if typedName.contains(typed) { s += 15 } else if marked { s /= 2 }
            }
            best = max(best, s)
        }
        return best
    }

    /// The score against an already folded name.
    func score(folded name: String) -> Int {
        var best = 0
        for (k, form) in forms.enumerated() {
            var s = 0
            if name == form {
                s = 100
            } else if let fit = Self.fit(form, in: name), k == 0 || fit > 10 {
                s = fit
            } else if Self.wordsBegin(stems[k], in: name) {
                s = 20
            }
            if s > 0 { best = max(best, s - (k == 0 ? 0 : 5)) }
        }
        return best
    }

    /// 60 at the start of the name (70 as whole words), 50 whole words
    /// elsewhere, 30 at a word start, 10 inside a word.
    private static func fit(_ form: String, in name: String) -> Int? {
        var best: Int?
        var searchRange = name.startIndex..<name.endIndex
        while let r = name.range(of: form, range: searchRange) {
            let starts = r.lowerBound == name.startIndex || !name[name.index(before: r.lowerBound)].isLetter
            let ends = r.upperBound == name.endIndex || !name[r.upperBound].isLetter
            let s = r.lowerBound == name.startIndex ? (ends ? 70 : 60) : (starts ? (ends ? 50 : 30) : 10)
            best = max(best ?? 0, s)
            searchRange = name.index(after: r.lowerBound)..<name.endIndex
        }
        return best
    }

    /// Whether every query word begins some word of the name, endings aside.
    private static func wordsBegin(_ words: [Beginning], in name: String) -> Bool {
        guard !words.isEmpty else { return false }
        let nameWords = name.split { !$0.isLetter && !$0.isNumber }
        return words.allSatisfy { begin in
            nameWords.contains { word in
                // Short words whole: "el" is not "elmacık".
                begin.stem.count <= 2 ? word == begin.stem : word.hasPrefix(begin.stem)
                    || begin.softened.map { word.hasPrefix($0) && Self.vowelEndings.contains(String(word.dropFirst($0.count))) } ?? false
            }
        }
    }

    /// A query word without its Turkish ending (plural, possessive, case),
    /// and with its last consonant softened before a vowel ending (kemik /
    /// kemiği, kalp / kalbi, not kalbur).
    private struct Beginning: Sendable {
        let stem: String
        let softened: String?
    }

    private static let vowelEndings: Set<String> = ["", "i", "in", "inin", "ini", "ine", "e", "a", "u", "un", "unun", "unu", "una"]

    private static func beginning(of word: String) -> Beginning {
        var stem = word
        for ending in ["lerinin", "larinin", "lerin", "larin", "leri", "lari", "ler", "lar", "nin", "nun", "in", "un", "si", "su", "i", "u"]
        where stem.hasSuffix(ending) && stem.count - ending.count >= 3 {
            stem.removeLast(ending.count)
            break
        }
        let soft: [Character: Character] = ["k": "g", "g": "k", "p": "b", "b": "p", "t": "d", "d": "t"]
        let softened = stem.last.flatMap { soft[$0] }.map { String(stem.dropLast()) + String($0) }
        return Beginning(stem: stem, softened: softened)
    }
}
