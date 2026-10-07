//
//  QuizEngine.swift
//  Anatomy
//

import Foundation

/// One multiple-choice question generated from the atlas content.
nonisolated struct QuizQuestion: Identifiable, Hashable, Sendable {
    enum Kind: Hashable, Sendable {
        case latinName, turkishName, description, fact(String), model
    }

    let id = UUID()
    let kind: Kind
    let prompt: String
    /// Extra context shown under the prompt (e.g. a masked description).
    let detail: String?
    let options: [String]
    let answer: Int
    let entryID: String
    /// Model names to highlight for 3D questions.
    let models: [String]
}

/// The kinds of study sessions offered on the Study tab.
nonisolated enum QuizMode: String, CaseIterable, Identifiable, Sendable {
    case mixed, terms, facts, model, weak

    var id: String { rawValue }

    var title: String {
        switch self {
        case .mixed: "Karma test"
        case .terms: "Latince terimler"
        case .facts: "Ayrıntı soruları"
        case .model: "3D tanıma"
        case .weak: "Zayıf konularım"
        }
    }

    var subtitle: String {
        switch self {
        case .mixed: "Her türden 10 soru"
        case .terms: "Türkçe ⇄ Latince eşleştirme"
        case .facts: "Origo, insersiyo, sinir, dallar…"
        case .model: "3D modelde işaretli yapıyı bul"
        case .weak: "En az bildiğin yapılar"
        }
    }

    var icon: String {
        switch self {
        case .mixed: "shuffle"
        case .terms: "character.book.closed"
        case .facts: "list.bullet.clipboard"
        case .model: "cube.transparent"
        case .weak: "target"
        }
    }
}

@MainActor
enum QuizEngine {
    /// Fact labels that make good questions, in order of preference.
    static let factLabels = ["İnnervasyon", "Origo", "İnsersiyo", "Fonksiyon", "Köken", "Dalları", "Beslediği alan",
                             "Eklemleştiği kemikler", "Eklem tipi", "Konum", "Hormon", "Çıkış / köken", "Motor (efferent)"]

    static func questions(mode: QuizMode, system: String?, count: Int = 10, store: AtlasStore, study: StudyStore, hasModel: (AtlasEntry) -> Bool) -> [QuizQuestion] {
        var pool = store.entries.filter { system == nil || $0.systemID == system }
        guard pool.count >= 4 else { return [] }
        if mode == .weak {
            pool.sort { study.score($0.id).mastery < study.score($1.id).mastery }
            pool = Array(pool.prefix(max(12, count * 2))).shuffled()
        } else {
            // Prefer less practised entries but keep variety.
            pool.shuffle()
            pool.sort { study.score($0.id).seen < study.score($1.id).seen }
            pool = Array(pool.prefix(max(count * 3, 30))).shuffled()
        }

        var out: [QuizQuestion] = []
        var used = Set<String>()
        for entry in pool where out.count < count {
            guard !used.contains(entry.id) else { continue }
            let kinds: [QuizQuestion.Kind]
            switch mode {
            case .terms: kinds = [.latinName, .turkishName].shuffled()
            case .facts: kinds = factKinds(for: entry).shuffled()
            case .model: kinds = hasModel(entry) ? [.model] : []
            case .mixed, .weak:
                var k: [QuizQuestion.Kind] = [.latinName, .turkishName, .description]
                k += factKinds(for: entry).prefix(2)
                if hasModel(entry) { k.append(.model) }
                kinds = k.shuffled()
            }
            for kind in kinds {
                if let q = make(kind, entry: entry, store: store) {
                    out.append(q)
                    used.insert(entry.id)
                    break
                }
            }
        }
        return out
    }

    private static func factKinds(for entry: AtlasEntry) -> [QuizQuestion.Kind] {
        factLabels.filter { label in entry.facts.contains { $0.label == label } }.map { .fact($0) }
    }

    /// Up to three distractor entries: same group first, then same system.
    private static func distractors(for entry: AtlasEntry, store: AtlasStore, where accept: (AtlasEntry) -> Bool) -> [AtlasEntry] {
        let sameSystem = store.entries(in: entry.systemID).filter { $0.id != entry.id && accept($0) }
        var picks = sameSystem.filter { $0.group == entry.group }.shuffled()
        picks += sameSystem.filter { $0.group != entry.group }.shuffled()
        if picks.count < 3 {
            picks += store.entries.filter { $0.systemID != entry.systemID && accept($0) }.shuffled()
        }
        return Array(picks.prefix(3))
    }

    private static func make(_ kind: QuizQuestion.Kind, entry: AtlasEntry, store: AtlasStore) -> QuizQuestion? {
        switch kind {
        case .latinName:
            let others = distractors(for: entry, store: store) { $0.la != entry.la }
            return build(kind, prompt: "‘\(entry.tr)’ yapısının Latince adı hangisidir?", detail: nil,
                         answer: entry.la, others: others.map(\.la), entry: entry)
        case .turkishName:
            let others = distractors(for: entry, store: store) { $0.tr != entry.tr }
            return build(kind, prompt: "‘\(entry.la)’ hangi yapıdır?", detail: nil,
                         answer: entry.tr, others: others.map(\.tr), entry: entry)
        case .description:
            let others = distractors(for: entry, store: store) { $0.tr != entry.tr }
            return build(kind, prompt: "Tanımı verilen yapı hangisidir?", detail: masked(entry.summary, entry: entry),
                         answer: entry.tr, others: others.map(\.tr), entry: entry)
        case .fact(let label):
            guard let value = entry.facts.first(where: { $0.label == label })?.value else { return nil }
            let others = distractors(for: entry, store: store) { other in
                guard let v = other.facts.first(where: { $0.label == label })?.value else { return false }
                return v != value
            }.compactMap { $0.facts.first(where: { $0.label == label })?.value }
            guard others.count == 3 else { return nil }
            return build(kind, prompt: "‘\(entry.tr)’ – \(label.lowercased(with: Locale(identifier: "tr_TR"))) nedir?", detail: nil,
                         answer: value, others: others, entry: entry)
        case .model:
            let others = distractors(for: entry, store: store) { !$0.models.isEmpty && $0.tr != entry.tr }
            return build(kind, prompt: "Modelde işaretlenen yapı hangisidir?", detail: nil,
                         answer: entry.tr, others: others.map(\.tr), entry: entry, models: entry.models)
        }
    }

    private static func build(_ kind: QuizQuestion.Kind, prompt: String, detail: String?, answer: String, others: [String], entry: AtlasEntry, models: [String] = []) -> QuizQuestion? {
        let unique = Array(NSOrderedSet(array: others.filter { $0 != answer })).compactMap { $0 as? String }
        guard unique.count >= 3 else { return nil }
        var options = Array(unique.prefix(3)) + [answer]
        options.shuffle()
        guard let index = options.firstIndex(of: answer) else { return nil }
        return QuizQuestion(kind: kind, prompt: prompt, detail: detail, options: options, answer: index, entryID: entry.id, models: models)
    }

    /// Hides the entry's own names inside its description.
    private static func masked(_ text: String, entry: AtlasEntry) -> String {
        var out = text
        var names = [entry.tr, entry.la, entry.en] + entry.aliases
        names += entry.tr.split(separator: " ").map(String.init).filter { $0.count > 4 }
        for name in names.sorted(by: { $0.count > $1.count }) where name.count > 2 {
            out = out.replacingOccurrences(of: name, with: "▢▢▢", options: [.caseInsensitive, .diacriticInsensitive])
        }
        return out
    }
}
