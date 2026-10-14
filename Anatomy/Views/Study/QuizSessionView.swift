//
//  QuizSessionView.swift
//  Anatomy
//
//  A practice test (answer shown at once, with explanation) or a timed exam
//  (answers can be changed, results at the end), followed by the results.
//

import SwiftUI

struct QuizSessionView: View {
    @Environment(AppModel.self) private var app
    @Environment(\.dismiss) private var dismiss
    let session: QuizSession
    @State private var scene: AnatomyScene?
    @State private var showEntry: AtlasEntry?
    @State private var showNavigator = false
    @State private var confirmFinish = false
    @State private var confirmClose = false
    @State private var feedback = 0
    @State private var lastCorrect = false

    var body: some View {
        NavigationStack {
            Group {
                if session.isFinished {
                    QuizResultView(session: session, scene: $scene) { dismiss() }
                } else if let question = session.current {
                    questionPage(question)
                        .id(session.index)
                        .transition(.asymmetric(insertion: .move(edge: .trailing).combined(with: .opacity),
                                                removal: .move(edge: .leading).combined(with: .opacity)))
                }
            }
            .animation(.snappy(duration: 0.3), value: session.index)
            .animation(.snappy, value: session.isFinished)
            .themedBackground()
            .navigationBarTitleDisplayMode(.inline)
            .toolbar { toolbar }
            .sheet(item: $showEntry) { entry in
                NavigationStack {
                    EntryDetailView(entry: entry)
                        .navigationDestination(for: AtlasEntry.self) { EntryDetailView(entry: $0) }
                        .toolbar {
                            ToolbarItem(placement: .confirmationAction) {
                                Button("Kapat") { showEntry = nil }
                            }
                        }
                }
                .appOverlays()
                .preferredColorScheme(.dark)
            }
            .sheet(isPresented: $showNavigator) {
                QuestionNavigator(session: session) { i in
                    session.index = i
                    showNavigator = false
                }
                .presentationDetents([.medium, .large])
                .presentationBackground(Theme.surface)
            }
            .confirmationDialog("Sınavı bitirmek istiyor musun?", isPresented: $confirmFinish, titleVisibility: .visible) {
                Button("Bitir ve sonucu gör") { finish() }
            } message: {
                Text(session.blankCount > 0 ? "\(session.blankCount) soru boş." : "Tüm soruları cevapladın.")
            }
            .confirmationDialog("Sınavdan çıkılsın mı?", isPresented: $confirmClose, titleVisibility: .visible) {
                Button("Bitir ve sonucu gör") { finish() }
                Button("Kaydetmeden çık", role: .destructive) { dismiss() }
            }
        }
        .appOverlays(active: showEntry == nil && !showNavigator)
        .sensoryFeedback(trigger: feedback) { _, _ in lastCorrect ? .success : .error }
        .task(id: session.id) { await runClock() }
        .preferredColorScheme(.dark)
    }

    // MARK: Toolbar

    @ToolbarContentBuilder
    private var toolbar: some ToolbarContent {
        ToolbarItem(placement: .cancellationAction) {
            Button {
                if session.isExam, !session.isFinished { confirmClose = true } else { dismiss() }
            } label: {
                Image(systemName: "xmark")
            }
            .accessibilityLabel("Kapat")
        }
        ToolbarItem(placement: .principal) {
            if session.isFinished {
                Text(session.config.title).font(.headline)
            } else {
                VStack(spacing: 4) {
                    HStack(spacing: 8) {
                        Text("\(session.index + 1)/\(session.questions.count)")
                            .font(.subheadline.weight(.semibold).monospacedDigit())
                        if session.config.timeLimit != nil {
                            TimelineView(.periodic(from: .now, by: 1)) { context in
                                let left = session.remaining(at: context.date) ?? 0
                                HStack(spacing: 3) {
                                    Image(systemName: "timer")
                                    Text(Self.clock(left))
                                }
                                .font(.subheadline.weight(.semibold).monospacedDigit())
                                .foregroundStyle(left < 120 ? Theme.danger : Theme.textSecondary)
                            }
                        }
                    }
                    ProgressBar(value: Double(session.isExam ? session.answeredCount : session.index + (session.isRevealed(session.index) ? 1 : 0)) / Double(max(session.questions.count, 1)))
                        .frame(width: 150, height: 4)
                }
            }
        }
        ToolbarItemGroup(placement: .primaryAction) {
            if !session.isFinished, let q = session.current {
                let saved = app.study.isBookmarked(q.id)
                Button {
                    app.study.toggleBookmark(q.id)
                } label: {
                    Image(systemName: saved ? "bookmark.fill" : "bookmark")
                        .foregroundStyle(saved ? Theme.gold : Theme.textPrimary)
                }
                .accessibilityLabel(saved ? "İşareti kaldır" : "Soruyu işaretle")
                if session.isExam {
                    Button("Bitir") { confirmFinish = true }
                        .fontWeight(.semibold)
                }
            }
        }
    }

    static func clock(_ seconds: TimeInterval) -> String {
        let s = Int(seconds.rounded(.up))
        return s >= 3600 ? String(format: "%d:%02d:%02d", s / 3600, s / 60 % 60, s % 60) : String(format: "%02d:%02d", s / 60, s % 60)
    }

    // MARK: Question

    private func questionPage(_ q: QuizQuestion) -> some View {
        let i = session.index
        return ScrollView {
            QuestionContent(question: q, number: i + 1, chosen: session.answer(at: i),
                            revealed: session.isRevealed(i), exam: session.isExam, scene: $scene,
                            onChoose: { choose($0) }, onOpenEntry: { showEntry = $0 })
                .padding(16)
                .padding(.bottom, 90)
        }
        .scrollIndicators(.hidden)
        .safeAreaInset(edge: .bottom) { bottomBar }
    }

    @ViewBuilder
    private var bottomBar: some View {
        if session.isExam {
            HStack(spacing: 10) {
                Button {
                    session.index -= 1
                } label: {
                    Image(systemName: "chevron.left")
                        .frame(width: 22)
                }
                .buttonStyle(SecondaryButtonStyle())
                .frame(width: 64)
                .disabled(session.index == 0)

                Button {
                    showNavigator = true
                } label: {
                    Label(session.isFlagged(session.index) ? "İşaretli" : "Sorular", systemImage: session.isFlagged(session.index) ? "flag.fill" : "square.grid.3x3")
                }
                .buttonStyle(SecondaryButtonStyle())

                Button {
                    session.toggleFlag()
                } label: {
                    Image(systemName: session.isFlagged(session.index) ? "flag.slash" : "flag")
                        .frame(width: 22)
                }
                .buttonStyle(SecondaryButtonStyle())
                .frame(width: 64)

                Button {
                    if session.index + 1 < session.questions.count {
                        session.index += 1
                    } else {
                        confirmFinish = true
                    }
                } label: {
                    Image(systemName: session.index + 1 < session.questions.count ? "chevron.right" : "checkmark")
                        .frame(width: 22)
                }
                .buttonStyle(PrimaryButtonStyle())
                .frame(width: 64)
            }
            .padding(.horizontal, 16)
            .padding(.vertical, 10)
            .background(.ultraThinMaterial)
        } else if session.isRevealed(session.index) {
            Button {
                if session.index + 1 < session.questions.count {
                    session.index += 1
                } else {
                    finish()
                }
            } label: {
                Text(session.index + 1 < session.questions.count ? "Sonraki soru" : "Sonucu gör")
            }
            .buttonStyle(PrimaryButtonStyle())
            .padding(.horizontal, 16)
            .padding(.vertical, 10)
            .background(.ultraThinMaterial)
            .transition(.move(edge: .bottom).combined(with: .opacity))
        }
    }

    private func choose(_ option: Int) {
        guard let q = session.current else { return }
        if session.isExam {
            if session.answer(at: session.index) == option {
                session.clearAnswer()
            } else {
                session.choose(option)
            }
            return
        }
        guard !session.isRevealed(session.index) else { return }
        let correct = withAnimation(.snappy) { session.choose(option) }
        app.study.record(question: q.id, system: q.systemID, entries: q.entryIDs, correct: correct)
        lastCorrect = correct
        feedback += 1
    }

    private func finish() {
        guard !session.isFinished else { return }
        if session.isExam {
            for (i, q) in session.questions.enumerated() {
                guard let correct = session.isCorrect(i) else { continue }
                app.study.record(question: q.id, system: q.systemID, entries: q.entryIDs, correct: correct)
            }
            app.study.addExam(StudyStore.ExamRecord(date: .now, title: session.config.title, total: session.questions.count,
                                                    correct: session.correctCount, wrong: session.wrongCount,
                                                    seconds: Int(session.elapsed)))
        }
        session.finish()
    }

    private func runClock() async {
        guard session.config.timeLimit != nil else { return }
        while !session.isFinished {
            try? await Task.sleep(for: .seconds(1))
            if Task.isCancelled { return }
            if (session.remaining(at: .now) ?? 1) <= 0 {
                finish()
            }
        }
    }
}

// MARK: - Question content

/// The question, its options and, once revealed, the explanation. Used while
/// answering and when reviewing results.
struct QuestionContent: View {
    @Environment(AppModel.self) private var app
    let question: QuizQuestion
    let number: Int
    let chosen: Int?
    let revealed: Bool
    var exam = false
    @Binding var scene: AnatomyScene?
    var onChoose: ((Int) -> Void)?
    var onOpenEntry: (AtlasEntry) -> Void

    var body: some View {
        let system = app.store.system(question.systemID)
        let tint = system?.tint ?? Theme.accent
        VStack(alignment: .leading, spacing: 18) {
            HStack(spacing: 6) {
                if let system {
                    TagView(text: system.tr, color: tint, systemImage: system.icon)
                }
                TagView(text: question.kindTitle, color: question.clinical ? Theme.clinical : Theme.textSecondary,
                        systemImage: question.clinical ? "stethoscope" : nil)
                if question.level == .tus {
                    Text("TUS")
                        .font(.caption2.weight(.heavy))
                        .foregroundStyle(Theme.gold)
                        .padding(.horizontal, 7)
                        .padding(.vertical, 4)
                        .background(Theme.gold.opacity(0.15), in: .capsule)
                }
            }

            if !question.models.isEmpty {
                QuizModelPreview(models: question.models, scene: $scene)
            }

            VStack(alignment: .leading, spacing: 10) {
                Text("Soru \(number)")
                    .font(.caption.weight(.bold))
                    .foregroundStyle(Theme.textTertiary)
                Text(question.prompt)
                    .font(.system(size: 18, weight: .semibold))
                    .foregroundStyle(Theme.textPrimary)
                    .lineSpacing(3)
                    .fixedSize(horizontal: false, vertical: true)
            }

            if let detail = question.detail {
                Text(detail)
                    .font(.subheadline)
                    .foregroundStyle(Theme.textSecondary)
                    .lineSpacing(2)
                    .fixedSize(horizontal: false, vertical: true)
                    .padding(14)
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .background(Theme.elevated, in: .rect(cornerRadius: 14))
            }

            VStack(spacing: 10) {
                ForEach(Array(question.options.enumerated()), id: \.offset) { i, option in
                    OptionButton(letter: Self.letter(i), text: option, state: state(i)) {
                        onChoose?(i)
                    }
                    .disabled(onChoose == nil || (revealed && !exam))
                }
            }

            if revealed {
                explanation
                    .transition(.opacity.combined(with: .move(edge: .bottom)))
            }
        }
    }

    static func letter(_ i: Int) -> String {
        ["A", "B", "C", "D", "E", "F"][min(i, 5)]
    }

    private func state(_ i: Int) -> OptionButton.Style {
        if revealed {
            if i == question.answer { return .correct }
            if i == chosen { return .wrong }
            return .dimmed
        }
        return i == chosen ? .selected : .idle
    }

    private var explanation: some View {
        let correct = chosen == question.answer
        let color = chosen == nil ? Theme.textSecondary : (correct ? Theme.success : Theme.danger)
        let entries = question.entryIDs.compactMap(app.store.entry)
        let notes = question.notes.enumerated().filter { !$0.element.isEmpty }
        return VStack(alignment: .leading, spacing: 14) {
            HStack(spacing: 8) {
                Image(systemName: chosen == nil ? "minus.circle.fill" : (correct ? "checkmark.circle.fill" : "xmark.circle.fill"))
                Text(chosen == nil ? "Boş bırakıldı" : (correct ? "Doğru cevap" : "Yanlış cevap"))
                Spacer()
                Text("Cevap: \(Self.letter(question.answer))")
                    .font(.subheadline.weight(.bold))
                    .padding(.horizontal, 10)
                    .padding(.vertical, 4)
                    .background(Theme.success.opacity(0.16), in: .capsule)
                    .foregroundStyle(Theme.success)
            }
            .font(.headline)
            .foregroundStyle(color)

            if let text = question.explanation {
                Text(text)
                    .font(.subheadline)
                    .foregroundStyle(Theme.textPrimary)
                    .lineSpacing(3)
                    .fixedSize(horizontal: false, vertical: true)
            }

            if !notes.isEmpty {
                VStack(alignment: .leading, spacing: 10) {
                    Eyebrow(text: "Seçenekler")
                    ForEach(notes, id: \.offset) { i, note in
                        HStack(alignment: .firstTextBaseline, spacing: 10) {
                            Text(Self.letter(i))
                                .font(.caption.weight(.heavy))
                                .foregroundStyle(i == question.answer ? Theme.success : Theme.textTertiary)
                                .frame(width: 16)
                            Text(note)
                                .font(.footnote)
                                .foregroundStyle(Theme.textSecondary)
                                .fixedSize(horizontal: false, vertical: true)
                        }
                    }
                }
                .padding(.top, 2)
            }

            if !entries.isEmpty {
                VStack(alignment: .leading, spacing: 8) {
                    Eyebrow(text: "Konuyu çalış")
                    FlowLayout(spacing: 8) {
                        ForEach(entries) { entry in
                            Button {
                                onOpenEntry(entry)
                            } label: {
                                HStack(spacing: 5) {
                                    Text(entry.tr)
                                    Image(systemName: "arrow.up.right")
                                        .font(.caption2.weight(.bold))
                                }
                                .font(.footnote.weight(.semibold))
                                .padding(.horizontal, 11)
                                .padding(.vertical, 7)
                                .background(Theme.accent.opacity(0.14), in: .capsule)
                                .foregroundStyle(Theme.accent)
                            }
                            .buttonStyle(.plain)
                        }
                    }
                }
            }
        }
        .padding(16)
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(Theme.card, in: .rect(cornerRadius: 20))
        .overlay { RoundedRectangle(cornerRadius: 20).strokeBorder(color.opacity(0.45), lineWidth: 1) }
    }
}

struct OptionButton: View {
    enum Style { case idle, selected, correct, wrong, dimmed }

    let letter: String
    let text: String
    let state: Style
    let action: () -> Void

    var body: some View {
        Button(action: action) {
            HStack(alignment: .center, spacing: 12) {
                Text(letter)
                    .font(.subheadline.weight(.bold))
                    .foregroundStyle(letterForeground)
                    .frame(width: 30, height: 30)
                    .background(letterBackground, in: .circle)
                Text(text)
                    .font(.body)
                    .foregroundStyle(Theme.textPrimary)
                    .multilineTextAlignment(.leading)
                    .fixedSize(horizontal: false, vertical: true)
                Spacer(minLength: 0)
                switch state {
                case .correct: Image(systemName: "checkmark.circle.fill").foregroundStyle(Theme.success)
                case .wrong: Image(systemName: "xmark.circle.fill").foregroundStyle(Theme.danger)
                default: EmptyView()
                }
            }
            .padding(.horizontal, 14)
            .padding(.vertical, 12)
            .frame(maxWidth: .infinity, alignment: .leading)
            .background(background, in: .rect(cornerRadius: 16))
            .overlay {
                RoundedRectangle(cornerRadius: 16)
                    .strokeBorder(border, lineWidth: state == .idle || state == .dimmed ? 1 : 1.5)
            }
            .opacity(state == .dimmed ? 0.5 : 1)
            .contentShape(.rect)
        }
        .buttonStyle(PressableStyle())
    }

    private var background: Color {
        switch state {
        case .correct: Theme.success.opacity(0.13)
        case .wrong: Theme.danger.opacity(0.13)
        case .selected: Theme.accent.opacity(0.14)
        default: Theme.card
        }
    }

    private var border: Color {
        switch state {
        case .correct: Theme.success
        case .wrong: Theme.danger
        case .selected: Theme.accent
        default: Theme.stroke
        }
    }

    private var letterBackground: Color {
        switch state {
        case .correct: Theme.success
        case .wrong: Theme.danger
        case .selected: Theme.accent
        default: Theme.elevated
        }
    }

    private var letterForeground: Color {
        switch state {
        case .correct, .wrong, .selected: .white
        default: Theme.textSecondary
        }
    }
}

/// A small 3D view framing the structures a question is about.
struct QuizModelPreview: View {
    let models: [String]
    @Binding var scene: AnatomyScene?

    var body: some View {
        ZStack {
            RoundedRectangle(cornerRadius: 22)
                .fill(LinearGradient(colors: [Color(hex: "1A1F2A"), Color(hex: "0C0E13")], startPoint: .top, endPoint: .bottom))
            if let scene {
                AnatomyViewport(scene: scene)
                    .clipShape(.rect(cornerRadius: 22))
                if !scene.loadingLayers.isEmpty {
                    ProgressView()
                }
            }
        }
        .overlay { RoundedRectangle(cornerRadius: 22).strokeBorder(Theme.stroke) }
        .frame(height: 280)
        .task(id: models) {
            let scene = self.scene ?? AnatomyScene(initialLayers: [])
            self.scene = scene
            let refs = scene.refs(matching: models)
            let systems = Set(refs.map(\.system))
            for layer in ModelLayer.all where !systems.contains(layer.id) {
                scene.setLayer(layer.id, enabled: false)
            }
            scene.showAll()
            await scene.reveal(refs, margin: 2.6)
        }
    }
}

/// Grid of question numbers for jumping around an exam.
private struct QuestionNavigator: View {
    let session: QuizSession
    let jump: (Int) -> Void

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 16) {
                    HStack(spacing: 16) {
                        legend(Theme.accent, "Cevaplandı (\(session.answeredCount))")
                        legend(Theme.elevated, "Boş (\(session.blankCount))")
                        legend(.orange, "İşaretli (\(session.flagged.count))")
                    }
                    .font(.caption)
                    LazyVGrid(columns: Array(repeating: GridItem(.flexible(), spacing: 10), count: 6), spacing: 10) {
                        ForEach(session.questions.indices, id: \.self) { i in
                            Button {
                                jump(i)
                            } label: {
                                Text("\(i + 1)")
                                    .font(.subheadline.weight(.semibold).monospacedDigit())
                                    .foregroundStyle(session.answer(at: i) != nil ? .white : Theme.textSecondary)
                                    .frame(maxWidth: .infinity, minHeight: 42)
                                    .background(session.answer(at: i) != nil ? Theme.accent : Theme.elevated, in: .rect(cornerRadius: 10))
                                    .overlay(alignment: .topTrailing) {
                                        if session.isFlagged(i) {
                                            Circle().fill(.orange).frame(width: 8, height: 8).padding(4)
                                        }
                                    }
                                    .overlay {
                                        if i == session.index {
                                            RoundedRectangle(cornerRadius: 10).strokeBorder(.white, lineWidth: 2)
                                        }
                                    }
                            }
                            .buttonStyle(.plain)
                        }
                    }
                }
                .padding(16)
            }
            .navigationTitle("Sorular")
            .navigationBarTitleDisplayMode(.inline)
        }
        .preferredColorScheme(.dark)
    }

    private func legend(_ color: Color, _ text: String) -> some View {
        HStack(spacing: 5) {
            RoundedRectangle(cornerRadius: 3).fill(color).frame(width: 12, height: 12)
            Text(text).foregroundStyle(Theme.textSecondary)
        }
    }
}
