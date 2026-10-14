//
//  QuizEngine.swift
//  Anatomy
//
//  Builds study sessions from the written question bank and from questions
//  generated out of the atlas entries (names, facts, descriptions, 3D).
//

import Foundation

/// One multiple-choice question as shown in a session.
nonisolated struct QuizQuestion: Identifiable, Hashable, Sendable {
    /// Stable key: the bank id, or "g|kind|…|entry" for generated questions,
    /// so wrong answers and bookmarks can be asked again later.
    let id: String
    let systemID: String
    let group: String
    let level: QuestionLevel
    let clinical: Bool
    let isGenerated: Bool
    let prompt: String
    /// Extra context under the prompt (a masked description, facts).
    let detail: String?
    let options: [String]
    let answer: Int
    let explanation: String?
    /// Why each option is right or wrong; may be empty.
    let notes: [String]
    let entryIDs: [String]
    /// Model names to show in 3D.
    let models: [String]

    var kindTitle: String {
        if !isGenerated { return clinical ? "Klinik vaka" : "Soru bankası" }
        if id.hasPrefix("g|model") { return "3D tanıma" }
        if id.hasPrefix("g|la") || id.hasPrefix("g|tr") { return "Terminoloji" }
        if id.hasPrefix("g|desc") { return "Tanım" }
        return "Ayrıntı"
    }
}

/// What a session draws its questions from.
nonisolated enum QuizSource: String, Hashable, Sendable, CaseIterable, Identifiable {
    /// Written and generated questions together.
    case mixed
    /// Written questions only.
    case bank
    /// Written clinical vignettes.
    case clinical
    /// Turkish ⇄ Latin names.
    case terms
    /// Origins, insertions, nerves, branches…
    case facts
    /// Name the highlighted 3D structure.
    case model
    /// The least known structures.
    case weak
    case wrongs
    case bookmarks

    var id: String { rawValue }

    var title: String {
        switch self {
        case .mixed: "Karma test"
        case .bank: "Soru bankası"
        case .clinical: "Klinik vakalar"
        case .terms: "Latince terimler"
        case .facts: "Ayrıntı soruları"
        case .model: "3D tanıma"
        case .weak: "Zayıf konularım"
        case .wrongs: "Yanlışlarım"
        case .bookmarks: "İşaretlediklerim"
        }
    }

    var subtitle: String {
        switch self {
        case .mixed: "Soru bankası ve atlas sorularından karışık"
        case .bank: "Açıklamalı özgün sorular"
        case .clinical: "Vaka temelli, TUS tarzı sorular"
        case .terms: "Türkçe ⇄ Latince eşleştirme"
        case .facts: "Origo, insersiyo, sinir, dallar…"
        case .model: "Modelde işaretli yapıyı bul"
        case .weak: "En az bildiğin yapılar"
        case .wrongs: "Yanlış yaptığın soruları tekrar çöz"
        case .bookmarks: "Kaydettiğin sorular"
        }
    }

    var icon: String {
        switch self {
        case .mixed: "shuffle"
        case .bank: "books.vertical.fill"
        case .clinical: "stethoscope"
        case .terms: "character.book.closed.fill"
        case .facts: "list.bullet.clipboard.fill"
        case .model: "cube.transparent.fill"
        case .weak: "scope"
        case .wrongs: "xmark.circle.fill"
        case .bookmarks: "bookmark.fill"
        }
    }

    var tint: String {
        switch self {
        case .mixed: "7C83FF"
        case .bank: "3BB4FF"
        case .clinical: "FF6FA5"
        case .terms: "34D3C2"
        case .facts: "F59E5B"
        case .model: "5C9DFF"
        case .weak: "FF7A59"
        case .wrongs: "FF5D5D"
        case .bookmarks: "E9B95C"
        }
    }
}

/// Everything needed to start a session.
nonisolated struct QuizConfig: Hashable, Sendable {
    var title: String
    var source: QuizSource = .mixed
    /// Systems to draw from; nil means every system the user can open.
    var systems: Set<String>?
    var group: String?
    var level: QuestionLevel?
    var count = 10
    /// Exam mode: answers are revealed only at the end.
    var isExam = false
    var timeLimit: TimeInterval?
    /// Prefer questions never answered before.
    var preferNew = true
    /// Only questions about these atlas entries (an entry's own test).
    var entries: Set<String>?
}

@MainActor
enum QuizEngine {
    // MARK: Sessions

    static func questions(for config: QuizConfig, store: AtlasStore, bank: QuestionBank, study: StudyStore,
                          hasModel: (AtlasEntry) -> Bool) -> [QuizQuestion] {
        let inScope: (String, String) -> Bool = { system, group in
            (config.systems?.contains(system) ?? true) && (config.group == nil || config.group == group)
        }
        if let entries = config.entries {
            return entryQuestions(entries, config: config, store: store, bank: bank, study: study, hasModel: hasModel)
        }
        switch config.source {
        case .wrongs, .bookmarks:
            let keys = config.source == .wrongs ? study.wrongs : study.bookmarks
            let questions = keys.compactMap { question(forKey: $0, store: store, bank: bank) }
                .filter { inScope($0.systemID, $0.group) }
            return Array(questions.prefix(config.count))
        case .bank, .clinical:
            let written = bankQuestions(config: config, bank: bank, study: study, inScope: inScope)
            var out = Array(written.prefix(config.count))
            // Topics with few written questions are topped up from the atlas.
            if config.source == .bank, !config.isExam, out.count < config.count {
                out += generated(config: config, count: config.count - out.count, store: store, study: study,
                                 hasModel: hasModel, inScope: inScope, exclude: [])
            }
            return out
        case .mixed:
            let written = bankQuestions(config: config, bank: bank, study: study, inScope: inScope)
            // About two thirds written questions when there are enough of them.
            let target = written.isEmpty ? 0 : min(written.count, Int((Double(config.count) * 0.65).rounded()))
            var out = Array(written.prefix(target))
            out += generated(config: config, count: config.count - out.count, store: store, study: study,
                             hasModel: hasModel, inScope: inScope, exclude: Set(out.flatMap(\.entryIDs)))
            if out.count < config.count {
                out += written.dropFirst(target).prefix(config.count - out.count)
            }
            return out.shuffled()
        case .terms, .facts, .model, .weak:
            return generated(config: config, count: config.count, store: store, study: study,
                             hasModel: hasModel, inScope: inScope, exclude: [])
        }
    }

    /// Written questions in scope: never answered first, then the ones
    /// answered wrong, then the rest; shuffled within each tier.
    private static func bankQuestions(config: QuizConfig, bank: QuestionBank, study: StudyStore,
                                      inScope: (String, String) -> Bool) -> [QuizQuestion] {
        var pool = bank.questions.filter { q in
            inScope(q.systemID, q.group)
                && (config.level == nil || q.level == config.level)
                && (config.source != .clinical || q.clinical)
        }
        // The level chosen in the profile comes first more often (TUS
        // preparation leans on TUS questions), without excluding the other.
        let preferred = QuestionLevel(rawValue: UserDefaults.standard.string(forKey: "profile.level") ?? "")
        var order: [String: Double] = [:]
        for q in pool {
            order[q.id] = Double.random(in: 0..<1) - (config.level == nil && q.level == preferred ? 0.35 : 0)
        }
        func tier(_ q: BankQuestion) -> Int {
            guard config.preferNew else { return 0 }
            let s = study.questionScore(q.id)
            if s.seen == 0 { return 0 }
            return s.correct < s.seen ? 1 : 2
        }
        pool.sort { tier($0) != tier($1) ? tier($0) < tier($1) : order[$0.id, default: 0] < order[$1.id, default: 0] }
        return pool.map(make)
    }

    /// Written questions linked to the entries, then generated ones about
    /// them and their related structures.
    private static func entryQuestions(_ ids: Set<String>, config: QuizConfig, store: AtlasStore, bank: QuestionBank,
                                       study: StudyStore, hasModel: (AtlasEntry) -> Bool) -> [QuizQuestion] {
        var out = bank.questions.filter { !ids.isDisjoint(with: $0.entries) }.shuffled().map(make)
        out = Array(out.prefix(config.count))
        var used = Set(out.map(\.id))
        let entries = ids.compactMap(store.entry)
        let related = entries.flatMap { store.related(of: $0) }.filter { !ids.contains($0.id) }
        for entry in entries + related.shuffled() where out.count < config.count {
            var kinds: [Kind] = [.latinName, .turkishName, .description] + factKinds(for: entry) + reverseKinds(for: entry)
            if hasModel(entry) { kinds.append(.model) }
            // Several questions about the entry itself, one about each related structure.
            let limit = ids.contains(entry.id) ? 4 : 1
            var added = 0
            for kind in kinds.shuffled() where added < limit && out.count < config.count {
                if let q = make(kind, entry: entry, store: store), used.insert(q.id).inserted {
                    out.append(q)
                    added += 1
                }
            }
        }
        return out
    }

    // MARK: Written questions

    static func make(_ q: BankQuestion) -> QuizQuestion {
        QuizQuestion(id: q.id, systemID: q.systemID, group: q.group, level: q.level, clinical: q.clinical,
                     isGenerated: false, prompt: q.stem, detail: nil, options: q.options, answer: q.answer,
                     explanation: q.explanation, notes: q.notes, entryIDs: q.entries, models: q.models)
    }

    /// Rebuilds a question from its key (wrong answers, bookmarks).
    static func question(forKey key: String, store: AtlasStore, bank: QuestionBank) -> QuizQuestion? {
        guard key.hasPrefix("g|") else { return bank.question(key).map(make) }
        let parts = key.split(separator: "|", omittingEmptySubsequences: false).map(String.init)
        guard parts.count >= 3, let entry = store.entry(parts[parts.count - 1]) else { return nil }
        let kind: Kind
        switch parts[1] {
        case "la": kind = .latinName
        case "tr": kind = .turkishName
        case "desc": kind = .description
        case "model": kind = .model
        case "fact" where parts.count == 4: kind = .fact(parts[2])
        case "rev" where parts.count == 4: kind = .reverse(parts[2].components(separatedBy: "+"))
        default: return nil
        }
        return make(kind, entry: entry, store: store)
    }

    // MARK: Generated questions

    private enum Kind: Hashable {
        case latinName, turkishName, description, model
        case fact(String)
        /// Identify the structure from one or two of its facts.
        case reverse([String])

        var key: String {
            switch self {
            case .latinName: "la"
            case .turkishName: "tr"
            case .description: "desc"
            case .model: "model"
            case .fact(let label): "fact|\(label)"
            case .reverse(let labels): "rev|\(labels.joined(separator: "+"))"
            }
        }
    }

    /// Fact labels that make good questions, with how to ask about them.
    private static let factPrompts: [String: (String) -> String] = [
        "İnnervasyon": { "‘\($0)’ hangi sinir tarafından innerve edilir?" },
        "Origo": { "‘\($0)’ için origo (başlangıç yeri) hangisidir?" },
        "İnsersiyo": { "‘\($0)’ için insersiyo (sonlanma yeri) hangisidir?" },
        "Fonksiyon": { "‘\($0)’ için temel fonksiyon hangisidir?" },
        "Kanlanma": { "‘\($0)’ için kanlanma hangisinde doğru verilmiştir?" },
        "Dalları": { "‘\($0)’ için dallar hangisinde doğru verilmiştir?" },
        "Beslediği alan": { "‘\($0)’ hangi bölgeyi besler?" },
        "Eklem tipi": { "‘\($0)’ hangi tip eklemdir?" },
        "Kemik tipi": { "‘\($0)’ hangi kemik tipindedir?" },
        "Motor (efferent)": { "‘\($0)’ için motor dağılım hangisidir?" },
        "Duyusal (afferent)": { "‘\($0)’ için duyusal alan hangisidir?" },
        "Çıkış / köken": { "‘\($0)’ nereden çıkar?" },
        "Köken": { "‘\($0)’ nereden köken alır?" },
        "Eklemleri": { "‘\($0)’ hangi kemiklerle eklem yapar?" },
        "Eklemleştiği kemikler": { "‘\($0)’ için eklemleşen kemikler hangileridir?" },
        "Bölümleri": { "‘\($0)’ için bölümler hangisinde doğru verilmiştir?" },
        "Önemli oluşumlar": { "Aşağıdakilerden hangisi ‘\($0)’ üzerindeki önemli oluşumlardır?" },
        "Seyir": { "‘\($0)’ için seyir hangisinde doğru tanımlanmıştır?" },
        "Konum": { "‘\($0)’ nerede bulunur?" },
        "Hormon": { "‘\($0)’ hangi hormon(lar)ı salgılar?" },
        "Bağlar": { "‘\($0)’ için güçlendirici bağlar hangisinde verilmiştir?" },
    ]

    /// Fact pairs that identify a structure well, by kind of structure.
    private static let reverseSets: [[String]] = [
        ["Origo", "İnsersiyo"], ["İnsersiyo", "İnnervasyon"], ["Origo", "Fonksiyon"],
        ["Motor (efferent)", "Duyusal (afferent)"], ["Köken", "Motor (efferent)"],
        ["Çıkış / köken", "Beslediği alan"], ["Çıkış / köken", "Dalları"], ["Eklem tipi", "Eklemleştiği kemikler"],
    ]

    private static func generated(config: QuizConfig, count: Int, store: AtlasStore, study: StudyStore,
                                  hasModel: (AtlasEntry) -> Bool, inScope: (String, String) -> Bool,
                                  exclude: Set<String>) -> [QuizQuestion] {
        guard count > 0 else { return [] }
        var pool = store.entries.filter { inScope($0.systemID, $0.group) && !exclude.contains($0.id) }
        guard !pool.isEmpty else { return [] }
        if config.source == .weak {
            pool.shuffle()
            pool.sort { study.score($0.id).mastery < study.score($1.id).mastery }
            pool = Array(pool.prefix(max(12, count * 2))).shuffled()
        } else {
            // Prefer less practised entries but keep variety.
            pool.shuffle()
            pool.sort { study.score($0.id).seen < study.score($1.id).seen }
            pool = Array(pool.prefix(max(count * 3, 30))).shuffled()
        }

        var out: [QuizQuestion] = []
        for entry in pool where out.count < count {
            let kinds: [Kind]
            switch config.source {
            case .terms: kinds = [.latinName, .turkishName].shuffled()
            case .facts: kinds = (factKinds(for: entry) + reverseKinds(for: entry)).shuffled()
            case .model: kinds = hasModel(entry) ? [.model] : []
            default:
                var k: [Kind] = [.latinName, .turkishName, .description]
                k += factKinds(for: entry).shuffled().prefix(2)
                k += reverseKinds(for: entry).prefix(1)
                if hasModel(entry) { k.append(.model) }
                kinds = k.shuffled()
            }
            for kind in kinds {
                if let q = make(kind, entry: entry, store: store) {
                    out.append(q)
                    break
                }
            }
        }
        return out
    }

    private static func factKinds(for entry: AtlasEntry) -> [Kind] {
        entry.facts.map(\.label).filter { factPrompts[$0] != nil }.map { .fact($0) }
    }

    private static func reverseKinds(for entry: AtlasEntry) -> [Kind] {
        let labels = Set(entry.facts.map(\.label))
        return reverseSets.filter { $0.allSatisfy(labels.contains) }.map { .reverse($0) }
    }

    /// Distractor entries: same group first, then same system, then any.
    private static func distractors(for entry: AtlasEntry, store: AtlasStore, count: Int = 4,
                                    where accept: (AtlasEntry) -> Bool) -> [AtlasEntry] {
        let sameSystem = store.entries(in: entry.systemID).filter { $0.id != entry.id && accept($0) }
        var picks = sameSystem.filter { $0.group == entry.group }.shuffled()
        picks += sameSystem.filter { $0.group != entry.group }.shuffled()
        if picks.count < count {
            picks += store.entries.filter { $0.systemID != entry.systemID && accept($0) }.shuffled()
        }
        return Array(picks.prefix(count))
    }

    private static func make(_ kind: Kind, entry: AtlasEntry, store: AtlasStore) -> QuizQuestion? {
        let key = "g|\(kind.key)|\(entry.id)"
        let about = "\(entry.tr) (\(entry.la)): \(firstSentence(entry.summary))"
        switch kind {
        case .latinName:
            let others = distractors(for: entry, store: store) { !similar($0.la, entry.la) && $0.tr != entry.tr }
            return build(key, entry: entry, prompt: "‘\(entry.tr)’ için Latince ad hangisidir?", detail: nil,
                         answer: entry.la, others: others.map { ($0.la, "\($0.la) → \($0.tr)") }, explanation: about)
        case .turkishName:
            let others = distractors(for: entry, store: store) { $0.tr != entry.tr && !similar($0.la, entry.la) }
            return build(key, entry: entry, prompt: "‘\(entry.la)’ hangi yapıdır?", detail: nil,
                         answer: entry.tr, others: others.map { ($0.tr, "\($0.tr) = \($0.la)") }, explanation: about)
        case .description:
            let others = distractors(for: entry, store: store) { $0.tr != entry.tr }
            return build(key, entry: entry, prompt: "Tanımı verilen yapı hangisidir?", detail: masked(entry.summary, entry: entry),
                         answer: entry.tr, others: others.map { ($0.tr, "\($0.tr): \(firstSentence($0.summary))") },
                         explanation: about)
        case .fact(let label):
            guard let value = entry.facts.first(where: { $0.label == label })?.value,
                  let prompt = factPrompts[label]?(entry.tr) else { return nil }
            let others = distractors(for: entry, store: store) { other in
                guard let v = other.facts.first(where: { $0.label == label })?.value else { return false }
                return !similar(v, value)
            }.compactMap { other in
                other.facts.first(where: { $0.label == label }).map { ($0.value, "\(other.tr) – \(label.lowercased(with: .tr)) bilgisidir.") }
            }
            guard others.count >= 3 else { return nil }
            var explanation = "\(entry.tr) – \(label): \(value)."
            let extra = entry.facts.filter { $0.label != label && factPrompts[$0.label] != nil }.prefix(2)
            for fact in extra { explanation += "\n\(fact.label): \(fact.value)." }
            return build(key, entry: entry, prompt: prompt, detail: nil, answer: value, others: others, explanation: explanation)
        case .reverse(let labels):
            let facts = labels.compactMap { label in entry.facts.first { $0.label == label } }
            guard facts.count == labels.count else { return nil }
            let others = distractors(for: entry, store: store) { other in
                // Every distractor must differ in at least one of the facts.
                labels.contains { label in
                    guard let v = other.facts.first(where: { $0.label == label })?.value,
                          let mine = entry.facts.first(where: { $0.label == label })?.value else { return true }
                    return !similar(v, mine)
                } && other.tr != entry.tr
            }
            let detail = facts.map { "\($0.label): \($0.value)" }.joined(separator: "\n")
            return build(key, entry: entry, prompt: "Özellikleri verilen yapı hangisidir?", detail: detail, answer: entry.tr,
                         others: others.map { other in
                             let first = labels.first.flatMap { l in other.facts.first { $0.label == l } }
                             return (other.tr, first.map { "\(other.tr) – \($0.label): \($0.value)" } ?? other.tr)
                         },
                         explanation: about)
        case .model:
            let others = distractors(for: entry, store: store) { !$0.models.isEmpty && $0.tr != entry.tr }
            return build(key, entry: entry, prompt: "Modelde işaretlenen yapı hangisidir?", detail: nil,
                         answer: entry.tr, others: others.map { ($0.tr, "\($0.tr) = \($0.la)") }, explanation: about,
                         models: entry.models)
        }
    }

    private static func build(_ key: String, entry: AtlasEntry, prompt: String, detail: String?, answer: String,
                              others: [(String, String)], explanation: String, models: [String] = []) -> QuizQuestion? {
        var seen = Set([answer.lowercased()])
        let unique = others.filter { seen.insert($0.0.lowercased()).inserted }
        guard unique.count >= 3 else { return nil }
        var options = Array(unique.prefix(4)).map { (text: $0.0, note: $0.1) } + [(text: answer, note: "")]
        options.shuffle()
        guard let index = options.firstIndex(where: { $0.text == answer }) else { return nil }
        return QuizQuestion(id: key, systemID: entry.systemID, group: entry.group, level: .faculty, clinical: false,
                            isGenerated: true, prompt: prompt, detail: detail, options: options.map(\.text), answer: index,
                            explanation: explanation, notes: options.map(\.note), entryIDs: [entry.id], models: models)
    }

    // MARK: Text helpers

    /// Two values count as the same answer when one contains the start of the
    /// other (“N. femoralis” and “N. femoralis (L2–L4)”).
    private static func similar(_ a: String, _ b: String) -> Bool {
        let x = core(a), y = core(b)
        return x == y || (!x.isEmpty && !y.isEmpty && (x.hasPrefix(y) || y.hasPrefix(x)))
    }

    private static func core(_ s: String) -> String {
        let head = s.split(whereSeparator: { "(,;–".contains($0) }).first.map(String.init) ?? s
        return head.folding(options: [.caseInsensitive, .diacriticInsensitive], locale: .tr)
            .trimmingCharacters(in: .whitespacesAndNewlines.union(.punctuationCharacters))
    }

    static func firstSentence(_ text: String) -> String {
        // Skip abbreviations like "m." or "a." so Latin terms are not cut.
        var index = text.startIndex
        while let dot = text[index...].firstIndex(of: ".") {
            let after = text.index(after: dot)
            let wordStart = text[..<dot].lastIndex(of: " ").map { text.index(after: $0) } ?? text.startIndex
            let word = text[wordStart..<dot]
            if after == text.endIndex { return text }
            if text[after] == " ", word.count > 3 { return String(text[...dot]) }
            index = after
        }
        return text
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

private extension Locale {
    static let tr = Locale(identifier: "tr_TR")
}
