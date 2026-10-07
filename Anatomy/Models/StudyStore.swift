//
//  StudyStore.swift
//  Anatomy
//

import Foundation
import Observation

/// Favourites, history and quiz progress, persisted in UserDefaults.
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

    private struct Snapshot: Codable {
        var favorites: [String] = []
        var recents: [String] = []
        var scores: [String: Score] = [:]
        var studyDays: [String] = []
        var answered = 0
        var correct = 0
    }

    private(set) var favorites: [String] = []
    private(set) var recents: [String] = []
    private(set) var scores: [String: Score] = [:]
    private(set) var studyDays: Set<String> = []
    private(set) var answered = 0
    private(set) var correct = 0

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
        }
    }

    private func save() {
        let snapshot = Snapshot(favorites: favorites, recents: recents, scores: scores,
                                studyDays: Array(studyDays), answered: answered, correct: correct)
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

    // MARK: Quiz

    func record(_ id: String, correct isCorrect: Bool) {
        var score = scores[id] ?? Score()
        score.seen += 1
        if isCorrect { score.correct += 1 }
        score.lastSeen = .now
        scores[id] = score
        answered += 1
        if isCorrect { correct += 1 }
        studyDays.insert(Self.dayKey(.now))
        save()
    }

    func score(_ id: String) -> Score { scores[id] ?? Score() }

    func mastery(of ids: [String]) -> Double {
        guard !ids.isEmpty else { return 0 }
        return ids.map { score($0).mastery }.reduce(0, +) / Double(ids.count)
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

    func resetProgress() {
        scores.removeAll()
        studyDays.removeAll()
        answered = 0
        correct = 0
        save()
    }

    private static func dayKey(_ date: Date) -> String {
        let c = Calendar.current.dateComponents([.year, .month, .day], from: date)
        return "\(c.year ?? 0)-\(c.month ?? 0)-\(c.day ?? 0)"
    }
}
