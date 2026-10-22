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
    var level: QuestionLevel
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
        if !isGenerated { return clinical ? String(localized: "Klinik vaka") : String(localized: "Soru bankası") }
        if id.hasPrefix("g|model") { return String(localized: "3D tanıma") }
        if id.hasPrefix("g|lm") { return String(localized: "Kemik oluşumu") }
        if id.hasPrefix("g|nx") || id.hasPrefix("g|nm") { return String(localized: "İnnervasyon") }
        if id.hasPrefix("g|gx") { return String(localized: "Gruplar") }
        if id.hasPrefix("g|tn") { return String(localized: "TUS bilgisi") }
        if id.hasPrefix("g|cn") { return String(localized: "Klinik bilgi") }
        if id.hasPrefix("g|la") || id.hasPrefix("g|tr") { return String(localized: "Terminoloji") }
        if id.hasPrefix("g|desc") { return String(localized: "Tanım") }
        return String(localized: "Ayrıntı")
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
    /// Processes, surfaces and foramina of the bones.
    case landmarks
    /// Which muscle is supplied by which nerve.
    case innervation
    /// The least known structures.
    case weak
    case wrongs
    case bookmarks

    var id: String { rawValue }

    var title: String {
        switch self {
        case .mixed: String(localized: "Karma test")
        case .bank: String(localized: "Soru bankası")
        case .clinical: String(localized: "Klinik vakalar")
        case .terms: String(localized: "Latince terimler")
        case .facts: String(localized: "Ayrıntı soruları")
        case .model: String(localized: "3D tanıma")
        case .landmarks: String(localized: "Kemik oluşumları")
        case .innervation: String(localized: "Kas ve sinirleri")
        case .weak: String(localized: "Zayıf konularım")
        case .wrongs: String(localized: "Yanlışlarım")
        case .bookmarks: String(localized: "İşaretlediklerim")
        }
    }

    var subtitle: String {
        switch self {
        case .mixed: String(localized: "Soru bankası ve atlas sorularından karışık")
        case .bank: String(localized: "Açıklamalı özgün sorular")
        case .clinical: String(localized: "Vaka temelli, TUS tarzı sorular")
        case .terms: String(localized: "Türkçe ⇄ Latince eşleştirme")
        case .facts: String(localized: "Origo, insersiyo, sinir, dallar…")
        case .model: String(localized: "Modelde işaretli yapıyı bul")
        case .landmarks: String(localized: "Çıkıntı, oluk ve deliklerin kemiği")
        case .innervation: String(localized: "Hangi kas hangi sinirle?")
        case .weak: String(localized: "En az bildiğin yapılar")
        case .wrongs: String(localized: "Yanlış yaptığın soruları tekrar çöz")
        case .bookmarks: String(localized: "Kaydettiğin sorular")
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
        case .landmarks: "mappin.and.ellipse"
        case .innervation: "bolt.horizontal.fill"
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
        case .landmarks: "A98BFF"
        case .innervation: "F2C94C"
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
        case .terms, .facts, .model, .weak, .landmarks, .innervation:
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
            kinds += nerveKinds(for: entry, store: store).shuffled().prefix(2)
            kinds += landmarkKinds(for: entry, store: store).shuffled().prefix(2)
            kinds += noteKinds(for: entry) + groupKinds(for: entry, store: store).shuffled().prefix(1)
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
        switch (parts[1], parts.count == 4 ? parts[2] : nil) {
        case ("la", nil): kind = .latinName
        case ("tr", nil): kind = .turkishName
        case ("desc", nil): kind = .description
        case ("model", nil): kind = .model
        case ("fact", let label?): kind = .fact(label)
        case ("rev", let labels?): kind = .reverse(labels.components(separatedBy: "+"))
        case ("lm", let name?): kind = .landmark(name)
        case ("lmon", let name?): kind = .landmarkOn(name)
        case ("nx", let family?): kind = .nerveExcept(family)
        case ("nm", let family?): kind = .nerveMember(family)
        case ("gx", let parent?): kind = .groupExcept(parent)
        case ("tn", let raw?):
            guard let i = Int(raw) else { return nil }
            kind = .tusNote(i)
        case ("cn", let raw?):
            guard let i = Int(raw) else { return nil }
            kind = .clinicalNote(i)
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
        /// Which bone a landmark lies on (the entry is the bone).
        case landmark(String)
        /// Which landmark lies on the bone (the entry is the bone).
        case landmarkOn(String)
        /// The one muscle a nerve does not supply (the entry is that muscle).
        case nerveExcept(String)
        /// The one muscle a nerve supplies (the entry is that muscle).
        case nerveMember(String)
        /// The one structure outside a group entry (the entry is that structure).
        case groupExcept(String)
        /// Identify the structure from one of its exam notes or clinical notes.
        case tusNote(Int)
        case clinicalNote(Int)

        var key: String {
            switch self {
            case .latinName: "la"
            case .turkishName: "tr"
            case .description: "desc"
            case .model: "model"
            case .fact(let label): "fact|\(label)"
            case .reverse(let labels): "rev|\(labels.joined(separator: "+"))"
            case .landmark(let name): "lm|\(name)"
            case .landmarkOn(let name): "lmon|\(name)"
            case .nerveExcept(let family): "nx|\(family)"
            case .nerveMember(let family): "nm|\(family)"
            case .groupExcept(let parent): "gx|\(parent)"
            case .tusNote(let i): "tn|\(i)"
            case .clinicalNote(let i): "cn|\(i)"
            }
        }

        /// Naming and recognising a structure is basic; its details are
        /// faculty level; exam notes are TUS level.
        var level: QuestionLevel {
            switch self {
            case .latinName, .turkishName, .description, .model, .landmark, .landmarkOn: .basic
            case .tusNote: .tus
            default: .faculty
            }
        }
    }

    /// Fact labels that make good questions, with how to ask about them.
    private static let factPrompts: [String: (String) -> String] = [
        "İnnervasyon": { String(localized: "‘\($0)’ hangi sinir tarafından innerve edilir?") },
        "Origo": { String(localized: "‘\($0)’ için origo (başlangıç yeri) hangisidir?") },
        "İnsersiyo": { String(localized: "‘\($0)’ için insersiyo (sonlanma yeri) hangisidir?") },
        "Fonksiyon": { String(localized: "‘\($0)’ için temel fonksiyon hangisidir?") },
        "Kanlanma": { String(localized: "‘\($0)’ için kanlanma hangisinde doğru verilmiştir?") },
        "Dalları": { String(localized: "‘\($0)’ için dallar hangisinde doğru verilmiştir?") },
        "Beslediği alan": { String(localized: "‘\($0)’ hangi bölgeyi besler?") },
        "Eklem tipi": { String(localized: "‘\($0)’ hangi tip eklemdir?") },
        "Kemik tipi": { String(localized: "‘\($0)’ hangi kemik tipindedir?") },
        "Motor (efferent)": { String(localized: "‘\($0)’ için motor dağılım hangisidir?") },
        "Duyusal (afferent)": { String(localized: "‘\($0)’ için duyusal alan hangisidir?") },
        "Çıkış / köken": { String(localized: "‘\($0)’ nereden çıkar?") },
        "Köken": { String(localized: "‘\($0)’ nereden köken alır?") },
        "Eklemleri": { String(localized: "‘\($0)’ hangi kemiklerle eklem yapar?") },
        "Eklemleştiği kemikler": { String(localized: "‘\($0)’ için eklemleşen kemikler hangileridir?") },
        "Bölümleri": { String(localized: "‘\($0)’ için bölümler hangisinde doğru verilmiştir?") },
        "Önemli oluşumlar": { String(localized: "Aşağıdakilerden hangisi ‘\($0)’ üzerindeki önemli oluşumlardır?") },
        "Seyir": { String(localized: "‘\($0)’ için seyir hangisinde doğru tanımlanmıştır?") },
        "Konum": { String(localized: "‘\($0)’ nerede bulunur?") },
        "Hormon": { String(localized: "‘\($0)’ hangi hormon(lar)ı salgılar?") },
        "Bağlar": { String(localized: "‘\($0)’ için güçlendirici bağlar hangisinde verilmiştir?") },
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
        switch config.source {
        case .landmarks: pool = pool.filter { !store.landmarks(of: $0.id).isEmpty }
        case .innervation: pool = pool.filter { $0.facts.contains { $0.label == "İnnervasyon" } }
        default: break
        }
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
            case .facts:
                kinds = (factKinds(for: entry) + reverseKinds(for: entry) + noteKinds(for: entry)
                         + nerveKinds(for: entry, store: store).shuffled().prefix(2)
                         + groupKinds(for: entry, store: store).shuffled().prefix(1)).shuffled()
            case .model: kinds = hasModel(entry) ? [.model] : []
            case .landmarks: kinds = landmarkKinds(for: entry, store: store).shuffled()
            case .innervation:
                kinds = (nerveKinds(for: entry, store: store) + [.fact("İnnervasyon")]).shuffled()
            default:
                var k: [Kind] = [.latinName, .turkishName, .description]
                k += factKinds(for: entry).shuffled().prefix(2)
                k += reverseKinds(for: entry).prefix(1)
                k += nerveKinds(for: entry, store: store).shuffled().prefix(1)
                k += landmarkKinds(for: entry, store: store).shuffled().prefix(1)
                k += noteKinds(for: entry).shuffled().prefix(1)
                k += groupKinds(for: entry, store: store).shuffled().prefix(1)
                if hasModel(entry) { k.append(.model) }
                kinds = k.shuffled()
            }
            for kind in kinds where config.level == nil || kind.level == config.level {
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

    private static func landmarkKinds(for entry: AtlasEntry, store: AtlasStore) -> [Kind] {
        store.landmarks(of: entry.id).filter { !$0.shared }.flatMap { [Kind.landmark($0.name), .landmarkOn($0.name)] }
    }

    private static func noteKinds(for entry: AtlasEntry) -> [Kind] {
        entry.tus.indices.filter { entry.tus[$0].count >= 40 }.map { .tusNote($0) }
            + entry.clinical.indices.filter { entry.clinical[$0].count >= 40 }.map { .clinicalNote($0) }
    }

    // MARK: Nerves

    /// A nerve and the words that name it (or its branches) in an
    /// "İnnervasyon" fact.
    private struct NerveFamily {
        let title: String
        let patterns: [String]
    }

    /// Nerves that supply enough muscles for "which one is (not) supplied"
    /// questions. Branches count as the nerve (the plantar nerves as the
    /// tibial nerve, the posterior interosseous nerve as the radial nerve).
    private static let nerveFamilies: [NerveFamily] = [
        NerveFamily(title: "N. facialis (VII)", patterns: ["facialis"]),
        NerveFamily(title: "N. mandibularis (V3)", patterns: ["mandibularis", "v3"]),
        NerveFamily(title: "N. oculomotorius (III)", patterns: ["oculomotorius"]),
        NerveFamily(title: "N. vagus (X) ve dalları", patterns: ["vagus", "(x)", "laryngeus", "plexus pharyngeus"]),
        NerveFamily(title: "Ansa cervicalis", patterns: ["ansa cervicalis"]),
        NerveFamily(title: "N. suboccipitalis", patterns: ["suboccipitalis"]),
        NerveFamily(title: "Spinal sinirlerin arka dalları", patterns: ["arka dal", "rami posteriores", "rr. posteriores", "suboccipitalis"]),
        NerveFamily(title: "Nn. intercostales", patterns: ["intercostales", "interkostal"]),
        NerveFamily(title: "N. dorsalis scapulae", patterns: ["dorsalis scapulae"]),
        NerveFamily(title: "N. axillaris", patterns: ["axillaris"]),
        NerveFamily(title: "N. musculocutaneus", patterns: ["musculocutaneus"]),
        NerveFamily(title: "N. radialis ve dalları", patterns: ["radialis", "interosseus posterior"]),
        NerveFamily(title: "N. medianus ve dalları", patterns: ["medianus", "interosseus anterior"]),
        NerveFamily(title: "N. ulnaris", patterns: ["ulnaris"]),
        NerveFamily(title: "N. gluteus superior", patterns: ["gluteus superior"]),
        NerveFamily(title: "N. femoralis", patterns: ["femoralis"]),
        NerveFamily(title: "N. obturatorius", patterns: ["obturatorius"]),
        NerveFamily(title: "N. ischiadicus ve dalları", patterns: ["ischiadicus", "n. tibialis", "fibularis", "plantaris"]),
        NerveFamily(title: "N. tibialis ve dalları", patterns: ["n. tibialis", "plantaris medialis", "plantaris lateralis"]),
        NerveFamily(title: "N. fibularis profundus", patterns: ["fibularis profundus"]),
        NerveFamily(title: "N. plantaris medialis", patterns: ["plantaris medialis"]),
        NerveFamily(title: "N. plantaris lateralis", patterns: ["plantaris lateralis"]),
        NerveFamily(title: "N. pudendus", patterns: ["pudendus", "rectalis inferior"]),
    ]

    private enum Supply { case member, outsider, unclear }

    /// Which muscles each nerve family supplies, built once.
    private struct NerveIndex {
        var supply: [String: [String: Supply]] = [:]
        var members: [String: [String]] = [:]
        var regions: [String: Set<BodyRegion>] = [:]
    }

    private static var nerveIndexCache: NerveIndex?

    private static func nerveIndex(_ store: AtlasStore) -> NerveIndex {
        if let cached = nerveIndexCache { return cached }
        var index = NerveIndex()
        // Single muscles only: a group entry ("Mm. rhomboidei") would repeat its own parts.
        let muscles = store.entries.filter { $0.systemID == "muscular" && childIDs(of: $0, store: store).count < 2 }
        for family in nerveFamilies {
            let patterns = family.patterns.map(fold)
            var supply: [String: Supply] = [:]
            for muscle in muscles {
                guard let value = store.canonicalFact("İnnervasyon", of: muscle) else { continue }
                let first = primaryClause(value), all = fold(value)
                if patterns.contains(where: first.contains) {
                    supply[muscle.id] = .member
                } else {
                    supply[muscle.id] = patterns.contains(where: all.contains) ? .unclear : .outsider
                }
            }
            let members = muscles.filter { supply[$0.id] == .member }
            index.supply[family.title] = supply
            index.members[family.title] = members.map(\.id)
            index.regions[family.title] = Set(members.map(\.region))
        }
        nerveIndexCache = index
        return index
    }

    /// The innervation as shown, in the app's language.
    private static func innervation(of entry: AtlasEntry) -> String? {
        entry.facts.first { $0.label == "İnnervasyon" }?.value
    }

    /// A nerve family's name in the app's language; the key is the Turkish
    /// name kept in question keys. Latin names read the same everywhere.
    static func familyTitle(_ key: String) -> String {
        switch key {
        case "N. vagus (X) ve dalları": String(localized: "N. vagus (X) ve dalları")
        case "Spinal sinirlerin arka dalları": String(localized: "Spinal sinirlerin arka dalları")
        case "N. radialis ve dalları": String(localized: "N. radialis ve dalları")
        case "N. medianus ve dalları": String(localized: "N. medianus ve dalları")
        case "N. ischiadicus ve dalları": String(localized: "N. ischiadicus ve dalları")
        case "N. tibialis ve dalları": String(localized: "N. tibialis ve dalları")
        default: key
        }
    }

    /// The nerve named first: up to the first ";", ":" or "," outside brackets
    /// ("N. femoralis (L2–L3), bazen n. obturatorius…" → "n. femoralis (l2–l3)").
    private static func primaryClause(_ value: String) -> String {
        var depth = 0
        var out = ""
        for ch in value {
            if ch == "(" { depth += 1 } else if ch == ")" { depth = max(0, depth - 1) }
            if depth == 0, ";:,".contains(ch) { break }
            out.append(ch)
        }
        return fold(out)
    }

    private static func nerveKinds(for entry: AtlasEntry, store: AtlasStore) -> [Kind] {
        guard entry.systemID == "muscular" else { return [] }
        let index = nerveIndex(store)
        return nerveFamilies.compactMap { family in
            guard (index.members[family.title]?.count ?? 0) >= 3 else { return nil }
            switch index.supply[family.title]?[entry.id] {
            case .member: return .nerveMember(family.title)
            case .outsider where index.regions[family.title]?.contains(entry.region) == true: return .nerveExcept(family.title)
            default: return nil
            }
        }
    }

    // MARK: Groups

    /// The parts of a group entry: entries that name it as their parent or
    /// that list only some of its 3D models (a carpal bone of the carpus).
    private static func children(of parent: AtlasEntry, store: AtlasStore) -> [AtlasEntry] {
        let models = Set(parent.models.map { $0.lowercased() })
        return store.entries(in: parent.systemID).filter { child in
            guard child.id != parent.id else { return false }
            if child.parent == parent.id { return true }
            let own = Set(child.models.map { $0.lowercased() })
            return !own.isEmpty && own.count < models.count && own.isSubset(of: models)
        }
    }

    private static var childrenCache: [String: [String]] = [:]

    private static func childIDs(of parent: AtlasEntry, store: AtlasStore) -> [String] {
        if let cached = childrenCache[parent.id] { return cached }
        let ids = children(of: parent, store: store).map(\.id)
        childrenCache[parent.id] = ids
        return ids
    }

    /// Group entries of the same heading that the entry is not part of.
    private static func groupKinds(for entry: AtlasEntry, store: AtlasStore) -> [Kind] {
        let mine = Set(entry.models.map { $0.lowercased() })
        return store.entries(in: entry.systemID).compactMap { parent in
            guard parent.id != entry.id, parent.group == entry.group else { return nil }
            let kids = childIDs(of: parent, store: store)
            guard kids.count >= 4, !kids.contains(entry.id),
                  mine.isDisjoint(with: parent.models.map { $0.lowercased() }),
                  !childIDs(of: entry, store: store).contains(where: kids.contains) else { return nil }
            return .groupExcept(parent.id)
        }
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
        var question = compose(kind, entry: entry, store: store)
        question?.level = kind.level
        return question
    }

    private static func compose(_ kind: Kind, entry: AtlasEntry, store: AtlasStore) -> QuizQuestion? {
        let key = "g|\(kind.key)|\(entry.id)"
        // Structures are named as the app shows them: Latin first when chosen.
        func named(_ e: AtlasEntry) -> String { store.title(e) }
        let about = "\(store.fullName(entry)): \(firstSentence(entry.summary))"
        switch kind {
        case .latinName:
            let others = distractors(for: entry, store: store) { !similar($0.la, entry.la) && $0.tr != entry.tr }
            return build(key, entry: entry, prompt: String(localized: "‘\(entry.tr)’ için Latince ad hangisidir?"), detail: nil,
                         answer: entry.la, others: others.map { ($0.la, "\($0.la) → \($0.tr)") }, explanation: about)
        case .turkishName:
            let others = distractors(for: entry, store: store) { $0.tr != entry.tr && !similar($0.la, entry.la) }
            return build(key, entry: entry, prompt: String(localized: "‘\(entry.la)’ hangi yapıdır?"), detail: nil,
                         answer: entry.tr, others: others.map { ($0.tr, "\($0.tr) = \($0.la)") }, explanation: about)
        case .description:
            let others = distractors(for: entry, store: store) { $0.tr != entry.tr }
            return build(key, entry: entry, prompt: String(localized: "Tanımı verilen yapı hangisidir?"), detail: masked(entry.summary, entry: entry),
                         answer: named(entry), others: others.map { (named($0), "\(named($0)): \(firstSentence($0.summary))") },
                         explanation: about)
        case .fact(let label):
            guard let value = entry.facts.first(where: { $0.label == label })?.value,
                  let prompt = factPrompts[label]?(named(entry)) else { return nil }
            let others = distractors(for: entry, store: store) { other in
                guard let v = other.facts.first(where: { $0.label == label })?.value else { return false }
                return !similar(v, value)
            }.compactMap { other in
                other.facts.first(where: { $0.label == label }).map { ($0.value, String(localized: "\(named(other)) – \($0.title.lowercased(with: .current)) bilgisidir.")) }
            }
            guard others.count >= 3 else { return nil }
            var explanation = "\(named(entry)) – \(entry.facts.first { $0.label == label }?.title ?? label): \(value)."
            let extra = entry.facts.filter { $0.label != label && factPrompts[$0.label] != nil }.prefix(2)
            for fact in extra { explanation += "\n\(fact.title): \(fact.value)." }
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
            let detail = facts.map { "\($0.title): \($0.value)" }.joined(separator: "\n")
            return build(key, entry: entry, prompt: String(localized: "Özellikleri verilen yapı hangisidir?"), detail: detail, answer: named(entry),
                         others: others.map { other in
                             let first = labels.first.flatMap { l in other.facts.first { $0.label == l } }
                             return (named(other), first.map { "\(named(other)) – \($0.title): \($0.value)" } ?? named(other))
                         },
                         explanation: about)
        case .model:
            let others = distractors(for: entry, store: store) { !$0.models.isEmpty && $0.tr != entry.tr }
            return build(key, entry: entry, prompt: String(localized: "Modelde işaretlenen yapı hangisidir?"), detail: nil,
                         answer: named(entry), others: others.map { (named($0), store.fullName($0)) }, explanation: about,
                         models: entry.models)
        case .landmark(let name):
            guard let mark = store.landmark(name), mark.entry == entry.id, !names(entry, in: mark.title) else { return nil }
            let mine = Set(entry.models.map { $0.lowercased() })
            let others = distractors(for: entry, store: store) { other in
                other.tr != entry.tr && !store.landmarks(of: other.id).isEmpty
                    && mine.isDisjoint(with: other.models.map { $0.lowercased() })
            }
            return build(key, entry: entry, prompt: String(localized: "‘\(mark.title)’ hangi kemik üzerinde bulunur?"), detail: nil,
                         answer: named(entry),
                         others: others.map { other in
                             let example = store.landmarks(of: other.id).filter { !names(other, in: $0.title) }.randomElement()
                             return (named(other), example.map { String(localized: "\(named(other)) üzerinde değildir; o kemikte ör. ‘\($0.tr)’ bulunur.") }
                                 ?? String(localized: "\(named(other)) üzerinde değildir."))
                         },
                         explanation: "\(mark.title) – \(named(entry)). \(mark.d)")
        case .landmarkOn(let name):
            guard let mark = store.landmark(name), mark.entry == entry.id, !names(entry, in: mark.title) else { return nil }
            let own = store.landmarks(of: entry.id).map { plain($0.tr) }
            let mine = Set(entry.models.map { $0.lowercased() })
            let bones = distractors(for: entry, store: store, count: 10) { other in
                !store.landmarks(of: other.id).isEmpty && mine.isDisjoint(with: other.models.map { $0.lowercased() })
            }
            // One landmark from each other bone, none that names a bone.
            let others: [(String, String)] = bones.compactMap { bone in
                store.landmarks(of: bone.id).filter { !$0.shared }.shuffled().first { other in
                    // "Temporal çizgi" is not wrong for a bone with "Üst temporal çizgi".
                    let name = plain(other.tr)
                    return !own.contains { $0.contains(name) || name.contains($0) }
                        && !names(entry, in: other.title) && !names(bone, in: other.title)
                }.map { ($0.title, String(localized: "\($0.tr) \(named(bone)) üzerindedir.")) }
            }
            return build(key, entry: entry, prompt: String(localized: "Aşağıdakilerden hangisi ‘\(named(entry))’ üzerinde bulunur?"), detail: nil,
                         answer: mark.title, others: others, explanation: "\(mark.title): \(mark.d)")
        case .nerveExcept(let family):
            let index = nerveIndex(store)
            guard index.supply[family]?[entry.id] == .outsider, let value = innervation(of: entry) else { return nil }
            let members = (index.members[family] ?? []).compactMap(store.entry).filter { $0.la != entry.la }.shuffled()
            let others = members.sorted { ($0.region == entry.region ? 0 : 1) < ($1.region == entry.region ? 0 : 1) }
            return build(key, entry: entry, prompt: String(localized: "Aşağıdaki kaslardan hangisi ‘\(Self.familyTitle(family))’ tarafından innerve EDİLMEZ?"),
                         detail: nil, answer: entry.la,
                         others: others.map { ($0.la, "\($0.tr): \(innervation(of: $0) ?? "")") },
                         explanation: String(localized: "\(entry.la) (\(entry.tr)) – innervasyon: \(value). Diğer seçeneklerdeki kasların hepsi \(Self.familyTitle(family)) ile innerve edilir."))
        case .nerveMember(let family):
            let index = nerveIndex(store)
            guard index.supply[family]?[entry.id] == .member, let value = innervation(of: entry) else { return nil }
            let regions = index.regions[family] ?? []
            func rank(_ e: AtlasEntry) -> Int { e.region == entry.region ? 0 : (regions.contains(e.region) ? 1 : 2) }
            let others = store.entries(in: "muscular")
                .filter { index.supply[family]?[$0.id] == .outsider && $0.la != entry.la }
                .shuffled().sorted { rank($0) < rank($1) }
            return build(key, entry: entry, prompt: String(localized: "Aşağıdaki kaslardan hangisi ‘\(Self.familyTitle(family))’ tarafından innerve edilir?"),
                         detail: nil, answer: entry.la,
                         others: others.map { ($0.la, "\($0.tr): \(innervation(of: $0) ?? "")") },
                         explanation: String(localized: "\(entry.la) (\(entry.tr)) – innervasyon: \(value)."))
        case .groupExcept(let parentID):
            guard let parent = store.entry(parentID) else { return nil }
            let kids = childIDs(of: parent, store: store).compactMap(store.entry)
            guard kids.count >= 3, !kids.contains(where: { $0.id == entry.id }) else { return nil }
            let latin = entry.systemID == "muscular"
            func label(_ e: AtlasEntry) -> String { latin ? e.la : named(e) }
            let list = kids.map(label).joined(separator: ", ")
            return build(key, entry: entry, prompt: String(localized: "Aşağıdakilerden hangisi ‘\(parent.tr)’ (\(parent.la)) kapsamında yer almaz?"),
                         detail: nil, answer: label(entry),
                         others: kids.shuffled().map { (label($0), String(localized: "\($0.tr), \(parent.tr) kapsamındadır.")) },
                         explanation: String(localized: "\(parent.tr): \(list). \(label(entry)) bu gruba ait değildir – \(firstSentence(entry.summary))"))
        case .tusNote(let i), .clinicalNote(let i):
            let isTus = if case .tusNote = kind { true } else { false }
            let notes = isTus ? entry.tus : entry.clinical
            guard notes.indices.contains(i) else { return nil }
            let note = notes[i]
            let others = distractors(for: entry, store: store) { $0.tr != entry.tr && !mentions(note, $0) }
            return build(key, entry: entry,
                         prompt: isTus ? String(localized: "Aşağıdaki bilgi hangi yapıyla ilgilidir?") : String(localized: "Aşağıdaki klinik bilgi hangi yapıyla ilgilidir?"),
                         detail: masked(note, entry: entry), answer: named(entry),
                         others: others.map { (named($0), "\(named($0)): \(firstSentence($0.summary))") },
                         explanation: "\(store.fullName(entry)): \(note)")
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
        return head.folding(options: [.caseInsensitive, .diacriticInsensitive], locale: nil)
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

    /// Case and accent insensitive form for matching Latin and Turkish words.
    private static func fold(_ s: String) -> String {
        s.folding(options: [.caseInsensitive, .diacriticInsensitive], locale: nil)
    }

    /// A name without its bracketed part ("Dış topuk (lateral malleol)" → "dis topuk").
    private static func plain(_ s: String) -> String {
        fold(s.split(separator: "(").first.map(String.init) ?? s).trimmingCharacters(in: .whitespaces)
    }

    private static func words(_ s: String) -> [String] {
        fold(s).split { !$0.isLetter }.map(String.init)
    }

    /// Words too common to tell structures apart.
    private static let commonWords: Set<String> = [
        "musculus", "muscle", "musculi", "ossis", "major", "minor", "longus", "brevis", "superior", "inferior",
        "anterior", "posterior", "medialis", "lateralis", "profundus", "superficialis", "externus", "internus",
        "magnus", "articulatio", "ligamentum", "digitorum", "pollicis", "hallucis", "capitis", "colli", "thoracis",
        "lumborum", "transversus", "obliquus", "rectus", "minimi", "digiti", "manus", "pedis", "carpi", "extensor",
        "flexor", "abductor", "adductor", "kemigi", "kemikleri", "kaslar", "kaslari", "eklemi", "buyuk", "kucuk",
        "vertebra", "vertebrae", "bones", "joint", "omurlar", "omurlari",
        "muscle", "muscles", "joints", "ligament", "ligaments", "articulation", "muskel", "muskeln", "knochen",
        "gelenk", "musculo", "musculos", "hueso", "huesos", "articulacion", "grand", "petit", "großer", "kleiner",
        "mayor", "menor", "deep", "superficial", "profond", "profundo",
    ]

    /// Whether the text names another structure (so it cannot be a wrong
    /// option for a question built on that text).
    private static func mentions(_ text: String, _ other: AtlasEntry) -> Bool {
        let haystack = fold(text)
        return ([other.la, other.tr] + other.aliases).flatMap(words)
            .filter { $0.count >= 5 && !commonWords.contains($0) }
            .contains { haystack.contains($0) }
    }

    /// Whether a landmark's name gives its bone away ("Femur başı").
    private static func names(_ bone: AtlasEntry, in text: String) -> Bool {
        let found = words(text)
        let stems = ([bone.tr, bone.la, bone.en] + bone.aliases).flatMap(words)
            .filter { $0.count >= 4 && !commonWords.contains($0) && $0 != "kemik" && $0 != "bone" }
            .map { String($0.prefix($0.count <= 5 ? 3 : 4)) }
        return stems.contains { stem in found.contains { $0.hasPrefix(stem) } }
    }

    /// Hides the entry's own names inside its description.
    static func masked(_ text: String, entry: AtlasEntry) -> String {
        var out = text
        var names = [entry.tr, entry.la, entry.en] + entry.aliases
        names += entry.tr.split(separator: " ").map(String.init)
            .filter { $0.count > 4 && !maskKeep.contains($0.lowercased(with: .current)) }
        for name in names.sorted(by: { $0.count > $1.count }) where name.count > 2 {
            // Whole words only: "kosta" stays inside "interkostal".
            let pattern = "(?<!\\p{L})" + NSRegularExpression.escapedPattern(for: name)
            guard let regex = try? NSRegularExpression(pattern: pattern, options: [.caseInsensitive]) else { continue }
            out = regex.stringByReplacingMatches(in: out, range: NSRange(out.startIndex..., in: out), withTemplate: "▢▢▢")
        }
        return out
    }

    /// Words of Turkish names too general to hide ("Derin parmak fleksörü"
    /// keeps "parmak" readable in its notes).
    private static let maskKeep: Set<String> = [
        "parmak", "parmağı", "başparmak", "kemiği", "kemikleri", "kemikçikleri", "kasları", "eklemi", "eklemleri",
        "bağları", "büyük", "küçük", "derin", "yüzeyel", "fleksörü", "ekstansörü", "abdüktörü", "addüktörü",
        "omurları", "omuru", "dışarı", "içeri",
        "muscle", "muscles", "bone", "bones", "joint", "joints", "ligament", "finger", "thumb", "major", "minor",
        "longus", "brevis", "deep", "superficial", "muscles", "muscle", "grand", "petit", "profond", "doigt",
        "articulation", "muskel", "knochen", "gelenk", "großer", "kleiner", "finger", "tiefer", "músculo",
        "hueso", "articulación", "mayor", "menor", "dedo", "profundo",
    ]
}

