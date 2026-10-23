//
//  StudyStore.swift
//  Anatomy
//

import Foundation
import Observation

/// Favourites, history, question statistics, wrong answers, exam results and
/// flashcard schedules, persisted in UserDefaults.
@MainActor
@Observable
final class StudyStore {
    nonisolated struct Score: Codable, Hashable, Sendable {
        var seen = 0
        var correct = 0
        var lastSeen: Date?

        /// 0…1, how well the item is known.
        var mastery: Double {
            guard seen > 0 else { return 0 }
            let ratio = Double(correct) / Double(seen)
            return ratio * min(1, Double(seen) / 3)
        }
    }

    nonisolated struct Tally: Codable, Hashable, Sendable {
        var answered = 0
        var correct = 0

        var accuracy: Double { answered == 0 ? 0 : Double(correct) / Double(answered) }
    }

    /// One finished timed exam.
    nonisolated struct ExamRecord: Codable, Hashable, Sendable, Identifiable {
        var id = UUID()
        var date: Date
        var title: String
        var total: Int
        var correct: Int
        var wrong: Int
        var seconds: Int

        /// TUS style net: four wrong answers cancel one right answer.
        var net: Double { Double(correct) - Double(wrong) / 4 }
    }

    /// Spaced repetition state of one flashcard.
    nonisolated struct Card: Codable, Hashable, Sendable {
        /// Leitner box, 0 = new or forgotten.
        var box = 0
        var due: Date = .distantPast
        var reviews = 0
    }

    nonisolated enum CardGrade: Sendable {
        case again, hard, good, easy
    }

    private struct Snapshot: Codable {
        var favorites: [String] = []
        var recents: [String] = []
        var scores: [String: Score] = [:]
        var studyDays: [String] = []
        var answered = 0
        var correct = 0
        var questionScores: [String: Score] = [:]
        var wrongs: [String] = []
        var bookmarks: [String] = []
        var daily: [String: Tally] = [:]
        var systems: [String: Tally] = [:]
        var exams: [ExamRecord] = []
        var cards: [String: Card] = [:]

        init() {}

        init(from decoder: any Decoder) throws {
            let c = try decoder.container(keyedBy: CodingKeys.self)
            favorites = try c.decodeIfPresent([String].self, forKey: .favorites) ?? []
            recents = try c.decodeIfPresent([String].self, forKey: .recents) ?? []
            scores = try c.decodeIfPresent([String: Score].self, forKey: .scores) ?? [:]
            studyDays = try c.decodeIfPresent([String].self, forKey: .studyDays) ?? []
            answered = try c.decodeIfPresent(Int.self, forKey: .answered) ?? 0
            correct = try c.decodeIfPresent(Int.self, forKey: .correct) ?? 0
            questionScores = try c.decodeIfPresent([String: Score].self, forKey: .questionScores) ?? [:]
            wrongs = try c.decodeIfPresent([String].self, forKey: .wrongs) ?? []
            bookmarks = try c.decodeIfPresent([String].self, forKey: .bookmarks) ?? []
            daily = try c.decodeIfPresent([String: Tally].self, forKey: .daily) ?? [:]
            systems = try c.decodeIfPresent([String: Tally].self, forKey: .systems) ?? [:]
            exams = try c.decodeIfPresent([ExamRecord].self, forKey: .exams) ?? []
            cards = try c.decodeIfPresent([String: Card].self, forKey: .cards) ?? [:]
        }
    }

    private(set) var favorites: [String] = []
    private(set) var recents: [String] = []
    /// Per atlas entry.
    private(set) var scores: [String: Score] = [:]
    private(set) var studyDays: Set<String> = []
    private(set) var answered = 0
    private(set) var correct = 0
    /// Per question key (bank id or generated key).
    private(set) var questionScores: [String: Score] = [:]
    /// Questions answered wrong and not yet answered right again, newest first.
    private(set) var wrongs: [String] = []
    private(set) var bookmarks: [String] = []
    /// Answers per day ("y-m-d").
    private(set) var daily: [String: Tally] = [:]
    /// Answers per body system.
    private(set) var systems: [String: Tally] = [:]
    private(set) var exams: [ExamRecord] = []
    private(set) var cards: [String: Card] = [:]

    @ObservationIgnored private let defaults: UserDefaults
    @ObservationIgnored private let key = "study.v1"

    init(defaults: UserDefaults = .standard) {
        self.defaults = defaults
        if let data = defaults.data(forKey: key), let snapshot = try? JSONDecoder().decode(Snapshot.self, from: data) {
            favorites = snapshot.favorites
            recents = snapshot.recents
            scores = snapshot.scores
            studyDays = Set(snapshot.studyDays)
            answered = snapshot.answered
            correct = snapshot.correct
            questionScores = snapshot.questionScores
            wrongs = snapshot.wrongs
            bookmarks = snapshot.bookmarks
            daily = snapshot.daily
            systems = snapshot.systems
            exams = snapshot.exams
            cards = snapshot.cards
        }
    }

    private func save() {
        var snapshot = Snapshot()
        snapshot.favorites = favorites
        snapshot.recents = recents
        snapshot.scores = scores
        snapshot.studyDays = Array(studyDays)
        snapshot.answered = answered
        snapshot.correct = correct
        snapshot.questionScores = questionScores
        snapshot.wrongs = wrongs
        snapshot.bookmarks = bookmarks
        snapshot.daily = daily
        snapshot.systems = systems
        snapshot.exams = exams
        snapshot.cards = cards
        if let data = try? JSONEncoder().encode(snapshot) {
            defaults.set(data, forKey: key)
        }
    }

    // MARK: Favourites & history

    func isFavorite(_ id: String) -> Bool { favorites.contains(id) }

    func toggleFavorite(_ id: String) {
        if let i = favorites.firstIndex(of: id) {
            favorites.remove(at: i)
        } else {
            favorites.insert(id, at: 0)
        }
        save()
    }

    func markViewed(_ id: String) {
        recents.removeAll { $0 == id }
        recents.insert(id, at: 0)
        if recents.count > 40 { recents.removeLast(recents.count - 40) }
        save()
    }

    func clearRecents() {
        recents.removeAll()
        save()
    }

    // MARK: Questions

    /// Records one answered question. `entries` are the atlas entries it was
    /// about; their mastery moves with it.
    func record(question key: String, system: String, entries: [String], correct isCorrect: Bool) {
        var score = questionScores[key] ?? Score()
        score.seen += 1
        if isCorrect { score.correct += 1 }
        score.lastSeen = .now
        questionScores[key] = score

        for id in Set(entries) {
            var s = scores[id] ?? Score()
            s.seen += 1
            if isCorrect { s.correct += 1 }
            s.lastSeen = .now
            scores[id] = s
        }

        wrongs.removeAll { $0 == key }
        if !isCorrect {
            wrongs.insert(key, at: 0)
            if wrongs.count > 500 { wrongs.removeLast(wrongs.count - 500) }
        }

        answered += 1
        if isCorrect { correct += 1 }
        let day = Self.dayKey(.now)
        studyDays.insert(day)
        daily[day, default: Tally()].answered += 1
        if isCorrect { daily[day, default: Tally()].correct += 1 }
        systems[system, default: Tally()].answered += 1
        if isCorrect { systems[system, default: Tally()].correct += 1 }
        save()
    }

    func score(_ id: String) -> Score { scores[id] ?? Score() }

    func questionScore(_ key: String) -> Score { questionScores[key] ?? Score() }

    func mastery(of ids: [String]) -> Double {
        guard !ids.isEmpty else { return 0 }
        return ids.map { score($0).mastery }.reduce(0, +) / Double(ids.count)
    }

    func isBookmarked(_ key: String) -> Bool { bookmarks.contains(key) }

    func toggleBookmark(_ key: String) {
        if let i = bookmarks.firstIndex(of: key) {
            bookmarks.remove(at: i)
        } else {
            bookmarks.insert(key, at: 0)
        }
        save()
    }

    func clearWrongs() {
        wrongs.removeAll()
        save()
    }

    func addExam(_ record: ExamRecord) {
        exams.insert(record, at: 0)
        if exams.count > 100 { exams.removeLast(exams.count - 100) }
        save()
    }

    var answeredToday: Int { daily[Self.dayKey(.now)]?.answered ?? 0 }

    /// The last `days` days, oldest first.
    func activity(days: Int) -> [(date: Date, tally: Tally)] {
        let calendar = Calendar.current
        let today = calendar.startOfDay(for: .now)
        return (0..<days).reversed().compactMap { offset in
            guard let date = calendar.date(byAdding: .day, value: -offset, to: today) else { return nil }
            return (date, daily[Self.dayKey(date)] ?? Tally())
        }
    }

    /// Consecutive days (ending today or yesterday) with at least one answer.
    var streak: Int {
        var day = Date.now
        var count = 0
        if !studyDays.contains(Self.dayKey(day)) {
            day = Calendar.current.date(byAdding: .day, value: -1, to: day) ?? day
        }
        while studyDays.contains(Self.dayKey(day)) {
            count += 1
            day = Calendar.current.date(byAdding: .day, value: -1, to: day) ?? day
        }
        return count
    }

    var accuracy: Double {
        answered == 0 ? 0 : Double(correct) / Double(answered)
    }

    // MARK: Flashcards

    /// Days until the next review for each Leitner box.
    private static let intervals: [Double] = [0, 1, 3, 7, 16, 35, 80]

    func card(_ id: String) -> Card? { cards[id] }

    func isDue(_ id: String, at date: Date = .now) -> Bool {
        guard let card = cards[id] else { return false }
        return card.due <= date
    }

    /// Whether something was studied today (a question or a card).
    var studiedToday: Bool { studyDays.contains(Self.dayKey(.now)) }

    /// Grades a flashcard; the structure it is about (`entry`) gains or
    /// loses mastery with it.
    func grade(card id: String, entry: String? = nil, _ grade: CardGrade) {
        var card = cards[id] ?? Card()
        switch grade {
        case .again: card.box = 0
        case .hard: card.box = max(1, card.box)
        case .good: card.box = min(card.box + 1, Self.intervals.count - 1)
        case .easy: card.box = min(card.box + 2, Self.intervals.count - 1)
        }
        card.reviews += 1
        let days = grade == .again ? 0 : (grade == .hard ? max(1, Self.intervals[card.box] / 2) : Self.intervals[card.box])
        // Forgotten cards come back in ten minutes, within the same session.
        card.due = grade == .again ? Date.now.addingTimeInterval(600) : Calendar.current.date(byAdding: .hour, value: Int(days * 24), to: .now) ?? .now
        cards[id] = card

        let scoreID = entry ?? id
        var s = scores[scoreID] ?? Score()
        s.seen += 1
        if grade != .again { s.correct += 1 }
        s.lastSeen = .now
        scores[scoreID] = s
        studyDays.insert(Self.dayKey(.now))
        save()
    }

    /// When a card graded now would come back, for the button captions.
    func nextInterval(card id: String, _ grade: CardGrade) -> String {
        let box = cards[id]?.box ?? 0
        switch grade {
        case .again: return String(localized: "10 dk")
        case .hard: return Self.format(days: max(1, Self.intervals[max(1, box)] / 2))
        case .good: return Self.format(days: Self.intervals[min(box + 1, Self.intervals.count - 1)])
        case .easy: return Self.format(days: Self.intervals[min(box + 2, Self.intervals.count - 1)])
        }
    }

    private static func format(days: Double) -> String {
        days < 30 ? String(localized: "\(Int(days)) g") : String(localized: "\(Int((days / 30).rounded())) ay")
    }

    func resetProgress() {
        scores.removeAll()
        studyDays.removeAll()
        answered = 0
        correct = 0
        questionScores.removeAll()
        wrongs.removeAll()
        daily.removeAll()
        systems.removeAll()
        exams.removeAll()
        cards.removeAll()
        save()
    }

    static func dayKey(_ date: Date) -> String {
        let c = Calendar.current.dateComponents([.year, .month, .day], from: date)
        return "\(c.year ?? 0)-\(c.month ?? 0)-\(c.day ?? 0)"
    }
}
