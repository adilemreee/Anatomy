//
//  StudyView.swift
//  Anatomy
//

import SwiftUI

/// The Study tab: progress summary, quiz modes and flashcards.
struct StudyView: View {
    @Environment(AppModel.self) private var app
    @State private var system: String?
    @State private var session: QuizSession?
    @State private var flashcards: FlashcardDeck?

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 24) {
                    statsHeader
                    systemPicker
                    VStack(alignment: .leading, spacing: 12) {
                        Text("Testler")
                            .font(.title3.weight(.bold))
                        ForEach(QuizMode.allCases) { mode in
                            Button {
                                start(mode)
                            } label: {
                                ModeRow(mode: mode)
                            }
                            .buttonStyle(.plain)
                        }
                    }
                    VStack(alignment: .leading, spacing: 12) {
                        Text("Kartlar")
                            .font(.title3.weight(.bold))
                        Button {
                            let entries = app.store.entries.filter { system == nil || $0.systemID == system }
                            flashcards = FlashcardDeck(entries: entries, study: app.study)
                        } label: {
                            ModeRow(title: "Bilgi kartları", subtitle: "Çevir, hatırla, işaretle", icon: "rectangle.on.rectangle.angled", tint: .orange)
                        }
                        .buttonStyle(.plain)
                    }
                }
                .padding(16)
            }
            .atlasBackground()
            .navigationTitle("Çalış")
            .fullScreenCover(item: $session) { session in
                QuizSessionView(session: session)
            }
            .fullScreenCover(item: $flashcards) { deck in
                FlashcardsView(deck: deck)
            }
        }
    }

    private var statsHeader: some View {
        let study = app.study
        return HStack(spacing: 12) {
            StatTile(value: "\(study.streak)", label: "Günlük seri", icon: "flame.fill", tint: .orange)
            StatTile(value: "\(study.answered)", label: "Cevaplanan", icon: "checkmark.circle.fill", tint: .blue)
            StatTile(value: study.answered == 0 ? "–" : "%\(Int(study.accuracy * 100))", label: "Doğruluk", icon: "target", tint: .green)
        }
    }

    private var systemPicker: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            HStack(spacing: 8) {
                chip(title: "Tüm sistemler", icon: "square.grid.2x2", tint: .accentColor, selected: system == nil) { system = nil }
                ForEach(app.store.systems) { s in
                    chip(title: s.tr, icon: s.icon, tint: s.tint, selected: system == s.id) { system = s.id }
                }
            }
            .padding(.horizontal, 16)
        }
        .padding(.horizontal, -16)
    }

    private func chip(title: String, icon: String, tint: Color, selected: Bool, action: @escaping () -> Void) -> some View {
        Button(action: action) {
            Label(title, systemImage: icon)
                .font(.subheadline.weight(.semibold))
                .padding(.horizontal, 14)
                .padding(.vertical, 9)
                .foregroundStyle(selected ? Color.white : tint)
                .background(selected ? AnyShapeStyle(tint) : AnyShapeStyle(tint.opacity(0.12)), in: .capsule)
        }
        .buttonStyle(.plain)
    }

    private func start(_ mode: QuizMode) {
        let questions = QuizEngine.questions(mode: mode, system: system, store: app.store, study: app.study, hasModel: app.hasModel)
        guard !questions.isEmpty else { return }
        session = QuizSession(mode: mode, questions: questions)
    }
}

private struct StatTile: View {
    let value: String
    let label: String
    let icon: String
    let tint: Color

    var body: some View {
        VStack(alignment: .leading, spacing: 6) {
            Image(systemName: icon)
                .foregroundStyle(tint)
            Text(value)
                .font(.title2.weight(.bold))
                .contentTransition(.numericText())
            Text(label)
                .font(.caption)
                .foregroundStyle(.secondary)
        }
        .frame(maxWidth: .infinity, alignment: .leading)
        .padding(14)
        .background(Color(.secondarySystemGroupedBackground), in: .rect(cornerRadius: 18))
    }
}

private struct ModeRow: View {
    var title: String
    var subtitle: String
    var icon: String
    var tint: Color

    init(mode: QuizMode) {
        title = mode.title
        subtitle = mode.subtitle
        icon = mode.icon
        tint = switch mode {
        case .mixed: .indigo
        case .terms: .teal
        case .facts: .pink
        case .model: .blue
        case .weak: .red
        }
    }

    init(title: String, subtitle: String, icon: String, tint: Color) {
        self.title = title
        self.subtitle = subtitle
        self.icon = icon
        self.tint = tint
    }

    var body: some View {
        HStack(spacing: 14) {
            SystemBadge(icon: icon, color: tint, size: 44)
            VStack(alignment: .leading, spacing: 2) {
                Text(title).font(.headline).foregroundStyle(.primary)
                Text(subtitle).font(.subheadline).foregroundStyle(.secondary)
            }
            Spacer()
            Image(systemName: "chevron.right")
                .font(.footnote.weight(.semibold))
                .foregroundStyle(.tertiary)
        }
        .padding(14)
        .background(Color(.secondarySystemGroupedBackground), in: .rect(cornerRadius: 18))
    }
}

/// A running quiz.
@MainActor
@Observable
final class QuizSession: Identifiable {
    let id = UUID()
    let mode: QuizMode
    let questions: [QuizQuestion]
    var index = 0
    var chosen: Int?
    var correctCount = 0

    init(mode: QuizMode, questions: [QuizQuestion]) {
        self.mode = mode
        self.questions = questions
    }

    var current: QuizQuestion? { questions.indices.contains(index) ? questions[index] : nil }
    var isFinished: Bool { index >= questions.count }
}
