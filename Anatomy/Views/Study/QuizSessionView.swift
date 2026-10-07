//
//  QuizSessionView.swift
//  Anatomy
//

import SwiftUI

struct QuizSessionView: View {
    @Environment(AppModel.self) private var app
    @Environment(\.dismiss) private var dismiss
    @State var session: QuizSession
    @State private var scene: AnatomyScene?
    @State private var showEntry: AtlasEntry?

    var body: some View {
        NavigationStack {
            Group {
                if let question = session.current {
                    questionView(question)
                        .id(question.id)
                        .transition(.asymmetric(insertion: .move(edge: .trailing).combined(with: .opacity), removal: .move(edge: .leading).combined(with: .opacity)))
                } else {
                    resultView
                }
            }
            .animation(.snappy, value: session.index)
            .atlasBackground()
            .navigationTitle(session.mode.title)
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Kapat") { dismiss() }
                }
                ToolbarItem(placement: .principal) {
                    if !session.isFinished {
                        ProgressView(value: Double(session.index), total: Double(session.questions.count))
                            .frame(width: 140)
                    }
                }
            }
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
            }
        }
        .sensoryFeedback(trigger: session.chosen) { _, chosen in
            guard let chosen, let q = session.current else { return nil }
            return chosen == q.answer ? .success : .error
        }
    }

    // MARK: Question

    private func questionView(_ q: QuizQuestion) -> some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 18) {
                Text("Soru \(session.index + 1) / \(session.questions.count)")
                    .font(.footnote.weight(.semibold))
                    .foregroundStyle(.secondary)

                if !q.models.isEmpty {
                    modelPreview(for: q)
                }

                Text(q.prompt)
                    .font(.title3.weight(.semibold))
                    .fixedSize(horizontal: false, vertical: true)

                if let detail = q.detail {
                    Text(detail)
                        .font(.body)
                        .foregroundStyle(.secondary)
                        .padding(14)
                        .frame(maxWidth: .infinity, alignment: .leading)
                        .background(Color(.secondarySystemGroupedBackground), in: .rect(cornerRadius: 16))
                }

                VStack(spacing: 10) {
                    ForEach(Array(q.options.enumerated()), id: \.offset) { index, option in
                        OptionButton(text: option, state: optionState(index, q)) {
                            choose(index, q)
                        }
                        .disabled(session.chosen != nil)
                    }
                }

                if session.chosen != nil, let entry = app.store.entry(q.entryID) {
                    feedback(entry: entry, correct: session.chosen == q.answer)
                }
            }
            .padding(16)
        }
        .safeAreaInset(edge: .bottom) {
            if session.chosen != nil {
                Button {
                    session.chosen = nil
                    session.index += 1
                } label: {
                    Text(session.index + 1 < session.questions.count ? "Sonraki soru" : "Sonucu gör")
                        .font(.headline)
                        .frame(maxWidth: .infinity)
                        .padding(.vertical, 6)
                }
                .buttonStyle(.glassProminent)
                .controlSize(.large)
                .padding(.horizontal, 16)
                .padding(.bottom, 8)
            }
        }
    }

    private func modelPreview(for q: QuizQuestion) -> some View {
        ZStack {
            RoundedRectangle(cornerRadius: 22)
                .fill(LinearGradient(colors: [Color(hex: "eef1f6"), Color(hex: "d6dce6")], startPoint: .top, endPoint: .bottom))
            if let scene {
                AnatomyViewport(scene: scene)
                    .clipShape(.rect(cornerRadius: 22))
                if !scene.loadingLayers.isEmpty {
                    ProgressView()
                }
            }
        }
        .frame(height: 300)
        .task(id: q.id) {
            let scene = self.scene ?? AnatomyScene(initialLayers: [])
            self.scene = scene
            let refs = scene.refs(matching: q.models)
            let systems = Set(refs.map(\.system))
            for layer in ModelLayer.all where !systems.contains(layer.id) {
                scene.setLayer(layer.id, enabled: false)
            }
            scene.showAll()
            await scene.reveal(refs, margin: 2.6)
        }
    }

    private func feedback(entry: AtlasEntry, correct: Bool) -> some View {
        VStack(alignment: .leading, spacing: 10) {
            Label(correct ? "Doğru!" : "Yanlış", systemImage: correct ? "checkmark.circle.fill" : "xmark.circle.fill")
                .font(.headline)
                .foregroundStyle(correct ? .green : .red)
            Text("\(entry.tr) – \(entry.la)")
                .font(.subheadline.weight(.semibold))
            Text(entry.summary)
                .font(.subheadline)
                .foregroundStyle(.secondary)
                .lineLimit(4)
            Button("Maddeyi aç") { showEntry = entry }
                .font(.subheadline.weight(.semibold))
        }
        .padding(16)
        .frame(maxWidth: .infinity, alignment: .leading)
        .background((correct ? Color.green : Color.red).opacity(0.1), in: .rect(cornerRadius: 18))
        .transition(.opacity.combined(with: .scale(scale: 0.97)))
    }

    private func optionState(_ index: Int, _ q: QuizQuestion) -> OptionButton.State {
        guard let chosen = session.chosen else { return .idle }
        if index == q.answer { return .correct }
        if index == chosen { return .wrong }
        return .dimmed
    }

    private func choose(_ index: Int, _ q: QuizQuestion) {
        withAnimation(.snappy) {
            session.chosen = index
        }
        let correct = index == q.answer
        if correct { session.correctCount += 1 }
        app.study.record(q.entryID, correct: correct)
    }

    // MARK: Result

    private var resultView: some View {
        let total = session.questions.count
        let ratio = total == 0 ? 0 : Double(session.correctCount) / Double(total)
        return VStack(spacing: 20) {
            Spacer()
            ZStack {
                ProgressRing(value: ratio, color: ratio >= 0.7 ? .green : (ratio >= 0.4 ? .orange : .red), lineWidth: 12)
                    .frame(width: 160, height: 160)
                VStack(spacing: 2) {
                    Text("\(session.correctCount)/\(total)")
                        .font(.largeTitle.weight(.bold))
                    Text("doğru").foregroundStyle(.secondary)
                }
            }
            Text(ratio >= 0.8 ? "Harika iş!" : (ratio >= 0.5 ? "İyi gidiyorsun" : "Biraz daha tekrar"))
                .font(.title2.weight(.bold))
            Text("Yanlış yaptığın yapılar ‘Zayıf konularım’ testinde daha sık karşına çıkacak.")
                .font(.subheadline)
                .foregroundStyle(.secondary)
                .multilineTextAlignment(.center)
                .padding(.horizontal, 32)
            Spacer()
            Button {
                dismiss()
            } label: {
                Text("Bitir")
                    .font(.headline)
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, 6)
            }
            .buttonStyle(.glassProminent)
            .controlSize(.large)
            .padding(.horizontal, 16)
            .padding(.bottom, 16)
        }
    }
}

private struct OptionButton: View {
    enum State { case idle, correct, wrong, dimmed }

    let text: String
    let state: State
    let action: () -> Void

    var body: some View {
        Button(action: action) {
            HStack(alignment: .top, spacing: 12) {
                Text(text)
                    .font(.body.weight(.medium))
                    .multilineTextAlignment(.leading)
                    .fixedSize(horizontal: false, vertical: true)
                Spacer(minLength: 0)
                switch state {
                case .correct: Image(systemName: "checkmark.circle.fill").foregroundStyle(.green)
                case .wrong: Image(systemName: "xmark.circle.fill").foregroundStyle(.red)
                default: EmptyView()
                }
            }
            .padding(16)
            .frame(maxWidth: .infinity, alignment: .leading)
            .background(background, in: .rect(cornerRadius: 16))
            .overlay {
                RoundedRectangle(cornerRadius: 16)
                    .strokeBorder(border, lineWidth: 2)
            }
            .opacity(state == .dimmed ? 0.55 : 1)
        }
        .buttonStyle(.plain)
    }

    private var background: Color {
        switch state {
        case .correct: .green.opacity(0.14)
        case .wrong: .red.opacity(0.14)
        default: Color(.secondarySystemGroupedBackground)
        }
    }

    private var border: Color {
        switch state {
        case .correct: .green
        case .wrong: .red
        default: .clear
        }
    }
}
