//
//  Flashcards.swift
//  Anatomy
//
//  Flashcards made from the atlas: one overview card per structure plus a
//  card for its Latin name, each of its facts, each bone landmark and each
//  exam or clinical note. Every card has its own spaced repetition schedule.
//

import Foundation
import Observation

nonisolated struct Flashcard: Identifiable, Hashable, Sendable {
    nonisolated enum Kind: String, CaseIterable, Identifiable, Hashable, Sendable {
        case overview, latin, facts, landmarks, tus, clinical

        var id: String { rawValue }

        var title: String {
            switch self {
            case .overview: String(localized: "Yapı kartları")
            case .latin: String(localized: "Latince adlar")
            case .facts: String(localized: "Ayrıntılar")
            case .landmarks: String(localized: "Kemik oluşumları")
            case .tus: String(localized: "TUS bilgileri")
            case .clinical: String(localized: "Klinik bilgiler")
            }
        }

        var subtitle: String {
            switch self {
            case .overview: String(localized: "Yapının tanımı ve temel bilgileri")
            case .latin: String(localized: "Türkçe adından Latince adına")
            case .facts: String(localized: "Origo, insersiyo, sinir, eklem tipi…")
            case .landmarks: String(localized: "Çıkıntı, oluk ve deliklerin kemiği")
            case .tus: String(localized: "Sınavlarda sorulan noktalar")
            case .clinical: String(localized: "Klinik tablodan yapıya")
            }
        }

        var icon: String {
            switch self {
            case .overview: "rectangle.on.rectangle.angled.fill"
            case .latin: "character.book.closed.fill"
            case .facts: "list.bullet.clipboard.fill"
            case .landmarks: "mappin.and.ellipse"
            case .tus: "target"
            case .clinical: "stethoscope"
            }
        }

        var tint: String {
            switch self {
            case .overview: "B07CFF"
            case .latin: "34D3C2"
            case .facts: "F59E5B"
            case .landmarks: "A98BFF"
            case .tus: "E9B95C"
            case .clinical: "FF6FA5"
            }
        }
    }

    /// Schedule key. Overview cards use the entry id, as before.
    let id: String
    let kind: Kind
    let entryID: String
    let systemID: String
    let group: String
    /// Small caption above the prompt.
    let eyebrow: String
    let prompt: String
    /// What to recall, shown in a capsule under the prompt.
    let ask: String
    let answer: String
    let answerDetail: String?
}

/// Every card the atlas makes, built once.
@MainActor
final class FlashcardLibrary {
    let cards: [Flashcard]
    private let byID: [String: Flashcard]

    init(store: AtlasStore) {
        var cards: [Flashcard] = []
        for entry in store.entries {
            func card(_ id: String, _ kind: Flashcard.Kind, eyebrow: String, prompt: String, ask: String,
                      answer: String, detail: String? = nil) -> Flashcard {
                Flashcard(id: id, kind: kind, entryID: entry.id, systemID: entry.systemID, group: entry.group,
                          eyebrow: eyebrow, prompt: prompt, ask: ask, answer: answer, answerDetail: detail)
            }
            cards.append(card(entry.id, .overview, eyebrow: "\(entry.group) · \(entry.region.title)", prompt: entry.tr,
                              ask: String(localized: "Latince adı, tanımı ve temel bilgileri"), answer: entry.la, detail: entry.summary))
            cards.append(card("la|\(entry.id)", .latin, eyebrow: entry.group, prompt: entry.tr, ask: String(localized: "Latince adı"),
                              answer: entry.la, detail: entry.en.isEmpty || AppLanguage.current == "en" ? nil : String(localized: "İngilizce: \(entry.en)")))
            for fact in entry.facts where fact.value.count < 400 {
                cards.append(card("f|\(fact.label)|\(entry.id)", .facts, eyebrow: entry.la, prompt: entry.tr,
                                  ask: Self.question(for: fact), answer: fact.value))
            }
            for (i, note) in entry.tus.enumerated() where note.count >= 40 {
                cards.append(card("tn|\(i)|\(entry.id)", .tus, eyebrow: entry.group,
                                  prompt: QuizEngine.masked(note, entry: entry), ask: String(localized: "Hangi yapı?"),
                                  answer: "\(entry.tr) (\(entry.la))", detail: note))
            }
            for (i, note) in entry.clinical.enumerated() where note.count >= 40 {
                cards.append(card("cn|\(i)|\(entry.id)", .clinical, eyebrow: entry.group,
                                  prompt: QuizEngine.masked(note, entry: entry), ask: String(localized: "Hangi yapı?"),
                                  answer: "\(entry.tr) (\(entry.la))", detail: note))
            }
        }
        for mark in store.landmarks {
            guard let bone = store.entry(mark.entry) else { continue }
            cards.append(Flashcard(id: "lm|\(mark.name)", kind: .landmarks, entryID: bone.id, systemID: bone.systemID,
                                   group: bone.group, eyebrow: "", prompt: mark.title,
                                   ask: String(localized: "Hangi kemikte, ne işe yarar?"), answer: bone.tr,
                                   answerDetail: mark.d.isEmpty ? nil : mark.d))
        }
        self.cards = cards
        byID = Dictionary(cards.map { ($0.id, $0) }, uniquingKeysWith: { first, _ in first })
    }

    func card(_ id: String) -> Flashcard? { byID[id] }

    func cards(kinds: Set<Flashcard.Kind>, systems: Set<String>, group: String? = nil) -> [Flashcard] {
        cards.filter { kinds.contains($0.kind) && systems.contains($0.systemID) && (group == nil || $0.group == group) }
    }

    /// What a fact card asks, from the fact's label.
    private static func question(for fact: AtlasEntry.Fact) -> String {
        switch fact.label {
        case "Origo": String(localized: "Origosu (başlangıcı)")
        case "İnsersiyo": String(localized: "İnsersiyosu (sonlanması)")
        case "İnnervasyon": String(localized: "Hangi sinirle innerve edilir?")
        case "Kanlanma": String(localized: "Kanlanması")
        case "Fonksiyon", "İşlev", "İşlevi": String(localized: "Fonksiyonu")
        case "Eklem tipi": String(localized: "Eklem tipi")
        case "Kemik tipi": String(localized: "Kemik tipi")
        case "Eklemleri", "Eklemleştiği kemikler": String(localized: "Eklem yaptığı kemikler")
        case "Bağlar": String(localized: "Bağları")
        case "Hareketler", "Hareket": String(localized: "Hareketleri")
        case "Önemli oluşumlar": String(localized: "Önemli oluşumları")
        case "Bölümleri": String(localized: "Bölümleri")
        default: fact.title
        }
    }
}

/// A spaced repetition session: due cards first, then new ones.
@MainActor
@Observable
final class FlashcardDeck: Identifiable {
    let id = UUID()
    let title: String
    private(set) var cards: [Flashcard]
    var index = 0
    private(set) var reviewed = 0
    private(set) var remembered = 0

    init(title: String, cards all: [Flashcard], study: StudyStore, limit: Int = 25) {
        self.title = title
        let due = all.filter { study.isDue($0.id) }
            .sorted { (study.card($0.id)?.due ?? .distantPast) < (study.card($1.id)?.due ?? .distantPast) }
        // New cards: the least known structures first, mixed within that.
        let new = all.filter { study.card($0.id) == nil }.shuffled()
            .sorted { study.score($0.entryID).mastery < study.score($1.entryID).mastery }
        cards = Array((due + new).prefix(limit))
        if cards.isEmpty {
            // Everything is scheduled for later: practise the earliest ones.
            cards = Array(all.sorted { (study.card($0.id)?.due ?? .distantPast) < (study.card($1.id)?.due ?? .distantPast) }.prefix(limit))
        }
    }

    var current: Flashcard? { cards.indices.contains(index) ? cards[index] : nil }

    func grade(_ grade: StudyStore.CardGrade, study: StudyStore) {
        guard let card = current else { return }
        study.grade(card: card.id, entry: card.entryID, grade)
        reviewed += 1
        if grade != .again { remembered += 1 }
        // Forgotten cards come back at the end of this session.
        if grade == .again { cards.append(card) }
        index += 1
    }
}
