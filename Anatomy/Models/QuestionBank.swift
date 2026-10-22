//
//  QuestionBank.swift
//  Anatomy
//
//  The written question bank (questions-<system>.json, authored in
//  tools/content/questions): original basic, faculty and TUS level questions
//  with five options and explained answers.
//

import Foundation
import Observation

/// How hard a question is meant to be.
nonisolated enum QuestionLevel: String, Codable, CaseIterable, Identifiable, Sendable {
    /// Basic: names, positions and the main facts every student should know.
    case basic
    /// Committee / faculty exam level.
    case faculty
    /// TUS level: details, clinical reasoning, exceptions.
    case tus

    var id: String { rawValue }

    var title: String {
        switch self {
        case .basic: String(localized: "Temel")
        case .faculty: String(localized: "Fakülte")
        case .tus: String(localized: "TUS")
        }
    }
}

/// One written question.
nonisolated struct BankQuestion: Identifiable, Hashable, Sendable, Decodable {
    let id: String
    /// Group heading of the system the question belongs to.
    let group: String
    let level: QuestionLevel
    /// A clinical vignette rather than a plain knowledge question.
    let clinical: Bool
    let stem: String
    let options: [String]
    let answer: Int
    let explanation: String
    /// Why each option is right or wrong; empty strings where nothing is said.
    let notes: [String]
    /// Atlas entries the question is about.
    let entries: [String]
    /// 3D model names to show with the question.
    let models: [String]
    var systemID: String = ""

    private enum CodingKeys: String, CodingKey {
        case id, group, level, clinical, stem, options, answer, explanation, notes, entries, models
    }

    init(from decoder: any Decoder) throws {
        let c = try decoder.container(keyedBy: CodingKeys.self)
        id = try c.decode(String.self, forKey: .id)
        group = try c.decode(String.self, forKey: .group)
        level = try c.decodeIfPresent(QuestionLevel.self, forKey: .level) ?? .faculty
        clinical = try c.decodeIfPresent(Bool.self, forKey: .clinical) ?? false
        stem = try c.decode(String.self, forKey: .stem)
        options = try c.decode([String].self, forKey: .options)
        answer = try c.decode(Int.self, forKey: .answer)
        explanation = try c.decode(String.self, forKey: .explanation)
        notes = try c.decodeIfPresent([String].self, forKey: .notes) ?? []
        entries = try c.decodeIfPresent([String].self, forKey: .entries) ?? []
        models = try c.decodeIfPresent([String].self, forKey: .models) ?? []
    }
}

private nonisolated struct QuestionFile: Decodable, Sendable {
    let system: String
    let questions: [BankQuestion]
}

@MainActor
@Observable
final class QuestionBank {
    private(set) var questions: [BankQuestion] = []
    private(set) var isLoaded = false

    private var byID: [String: BankQuestion] = [:]
    private var bySystem: [String: [BankQuestion]] = [:]

    /// Decodes every question file off the main thread.
    func load(systems: [String]) async {
        guard !isLoaded else { return }
        let loaded = await Task.detached(priority: .userInitiated) { () -> [BankQuestion] in
            var out: [BankQuestion] = []
            let decoder = JSONDecoder()
            for system in systems {
                guard let url = AppLanguage.url(for: "questions-\(system)"),
                      let data = try? Data(contentsOf: url) else { continue }
                do {
                    let file = try decoder.decode(QuestionFile.self, from: data)
                    out += file.questions.map { q in
                        var q = q
                        q.systemID = file.system
                        return q
                    }
                } catch {
                    print("questions-\(system).json: \(error)")
                }
            }
            return out
        }.value
        questions = loaded
        byID = Dictionary(loaded.map { ($0.id, $0) }, uniquingKeysWith: { a, _ in a })
        bySystem = Dictionary(grouping: loaded, by: \.systemID)
        isLoaded = true
    }

    func question(_ id: String) -> BankQuestion? { byID[id] }

    func questions(in system: String) -> [BankQuestion] { bySystem[system] ?? [] }

    func questions(in system: String, group: String) -> [BankQuestion] {
        questions(in: system).filter { $0.group == group }
    }

    func count(in system: String) -> Int { bySystem[system]?.count ?? 0 }
}
