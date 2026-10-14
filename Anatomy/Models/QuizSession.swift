//
//  QuizSession.swift
//  Anatomy
//

import Foundation
import Observation

/// A running practice test or timed exam.
@MainActor
@Observable
final class QuizSession: Identifiable {
    let id = UUID()
    let config: QuizConfig
    let questions: [QuizQuestion]
    var index = 0
    /// The chosen option of every question, nil while unanswered.
    private(set) var answers: [Int?]
    /// Practice mode: questions whose answer has been shown.
    private(set) var revealed: Set<Int> = []
    private(set) var flagged: Set<Int> = []
    let startedAt = Date.now
    private(set) var finishedAt: Date?

    init(config: QuizConfig, questions: [QuizQuestion]) {
        self.config = config
        self.questions = questions
        answers = Array(repeating: nil, count: questions.count)
    }

    var isExam: Bool { config.isExam }
    var isFinished: Bool { finishedAt != nil }
    var current: QuizQuestion? { questions.indices.contains(index) ? questions[index] : nil }

    func answer(at i: Int) -> Int? { answers.indices.contains(i) ? answers[i] : nil }
    func isRevealed(_ i: Int) -> Bool { revealed.contains(i) }
    func isFlagged(_ i: Int) -> Bool { flagged.contains(i) }

    /// Practice: locks the answer and reveals it. Exam: (re)selects.
    /// Returns whether the choice was correct.
    @discardableResult
    func choose(_ option: Int) -> Bool {
        guard let q = current, !isFinished else { return false }
        if !isExam {
            guard answers[index] == nil else { return answers[index] == q.answer }
            revealed.insert(index)
        }
        answers[index] = option
        return option == q.answer
    }

    func clearAnswer() {
        guard isExam, !isFinished, answers.indices.contains(index) else { return }
        answers[index] = nil
    }

    func toggleFlag() {
        if flagged.contains(index) { flagged.remove(index) } else { flagged.insert(index) }
    }

    func finish() {
        guard finishedAt == nil else { return }
        finishedAt = .now
    }

    // MARK: Results

    var correctCount: Int { zip(answers, questions).filter { $0.0 == $0.1.answer }.count }
    var wrongCount: Int { zip(answers, questions).filter { $0.0 != nil && $0.0 != $0.1.answer }.count }
    var blankCount: Int { answers.filter { $0 == nil }.count }
    var answeredCount: Int { answers.count - blankCount }
    var net: Double { Double(correctCount) - Double(wrongCount) / 4 }

    var elapsed: TimeInterval { (finishedAt ?? .now).timeIntervalSince(startedAt) }

    func remaining(at date: Date) -> TimeInterval? {
        config.timeLimit.map { max(0, $0 - date.timeIntervalSince(startedAt)) }
    }

    func isCorrect(_ i: Int) -> Bool? {
        guard let a = answer(at: i) else { return nil }
        return a == questions[i].answer
    }

    /// Correct / answered per system, for the result breakdown.
    var bySystem: [(system: String, correct: Int, total: Int)] {
        var order: [String] = []
        var tally: [String: (Int, Int)] = [:]
        for (i, q) in questions.enumerated() {
            if tally[q.systemID] == nil { order.append(q.systemID) }
            var t = tally[q.systemID] ?? (0, 0)
            t.1 += 1
            if isCorrect(i) == true { t.0 += 1 }
            tally[q.systemID] = t
        }
        return order.map { ($0, tally[$0]!.0, tally[$0]!.1) }
    }
}
