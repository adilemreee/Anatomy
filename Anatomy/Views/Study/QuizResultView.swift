//
//  QuizResultView.swift
//  Anatomy
//

import SwiftUI

/// Score, TUS net, per-system breakdown and a review of every question.
struct QuizResultView: View {
    @Environment(AppModel.self) private var app
    let session: QuizSession
    @Binding var scene: AnatomyScene?
    let close: () -> Void
    @State private var filter: Filter = .all

    enum Filter: String, CaseIterable, Identifiable {
        case all, wrong, blank, correct
        var id: String { rawValue }
        var title: String {
            switch self {
            case .all: String(localized: "Tümü")
            case .wrong: String(localized: "Yanlış")
            case .blank: String(localized: "Boş")
            case .correct: String(localized: "Doğru")
            }
        }
    }

    var body: some View {
        let total = session.questions.count
        let ratio = total == 0 ? 0 : Double(session.correctCount) / Double(total)
        ScrollView {
            VStack(spacing: 22) {
                VStack(spacing: 14) {
                    ZStack {
                        ProgressRing(value: ratio, color: color(for: ratio), lineWidth: 12)
                            .frame(width: 150, height: 150)
                        VStack(spacing: 0) {
                            Text(ratio.formatted(.percent.precision(.fractionLength(0))))
                                .font(.system(size: 40, weight: .bold, design: .rounded))
                                .foregroundStyle(Theme.textPrimary)
                            Text("başarı")
                                .font(.subheadline)
                                .foregroundStyle(Theme.textSecondary)
                        }
                    }
                    Text(headline(ratio))
                        .font(.title2.weight(.bold))
                        .foregroundStyle(Theme.textPrimary)
                    Text("\(total) soru · \(session.isExam ? String(localized: "deneme sınavı") : String(localized: "pratik"))")
                        .font(.subheadline)
                        .foregroundStyle(Theme.textSecondary)
                }
                .padding(.top, 8)

                HStack(spacing: 10) {
                    tile("\(session.correctCount)", String(localized: "Doğru"), Theme.success)
                    tile("\(session.wrongCount)", String(localized: "Yanlış"), Theme.danger)
                    tile("\(session.blankCount)", String(localized: "Boş"), Theme.textSecondary)
                    tile(String(format: "%.2f", session.net), String(localized: "Net"), Theme.accent)
                }

                HStack {
                    Label(QuizSessionView.clock(session.elapsed), systemImage: "clock")
                    Spacer()
                    Text("Soru başına \(Int(session.elapsed / Double(max(total, 1)))) sn")
                }
                .font(.footnote.weight(.medium))
                .foregroundStyle(Theme.textSecondary)
                .padding(.horizontal, 4)

                if session.bySystem.count > 1 {
                    Card {
                        VStack(alignment: .leading, spacing: 12) {
                            Eyebrow(text: String(localized: "Sistemlere göre"))
                            ForEach(session.bySystem, id: \.system) { row in
                                let system = app.store.system(row.system)
                                HStack(spacing: 10) {
                                    Image(systemName: system?.icon ?? "circle")
                                        .foregroundStyle(system?.tint ?? Theme.accent)
                                        .frame(width: 20)
                                    Text(system?.tr ?? row.system)
                                        .font(.subheadline)
                                        .foregroundStyle(Theme.textPrimary)
                                    Spacer()
                                    Text("\(row.correct)/\(row.total)")
                                        .font(.subheadline.weight(.semibold).monospacedDigit())
                                        .foregroundStyle(Theme.textSecondary)
                                }
                                ProgressBar(value: Double(row.correct) / Double(max(row.total, 1)), color: system?.tint ?? Theme.accent)
                                    .frame(height: 4)
                            }
                        }
                    }
                }

                VStack(alignment: .leading, spacing: 12) {
                    SectionHeader(title: String(localized: "Soruları incele"))
                    Picker("Filtre", selection: $filter) {
                        ForEach(Filter.allCases) { Text($0.title).tag($0) }
                    }
                    .pickerStyle(.segmented)
                    VStack(spacing: 8) {
                        ForEach(indices, id: \.self) { i in
                            NavigationLink {
                                ReviewPager(session: session, indices: indices, start: i, scene: $scene)
                            } label: {
                                reviewRow(i)
                            }
                            .buttonStyle(.plain)
                        }
                        if indices.isEmpty {
                            Text("Bu filtrede soru yok.")
                                .font(.subheadline)
                                .foregroundStyle(Theme.textSecondary)
                                .padding(.vertical, 12)
                        }
                    }
                }
            }
            .padding(16)
            .padding(.bottom, 100)
        }
        .scrollIndicators(.hidden)
        .safeAreaInset(edge: .bottom) {
            VStack(spacing: 10) {
                let wrong = session.questions.indices.filter { session.isCorrect($0) != true }
                if !wrong.isEmpty {
                    Button {
                        app.startQuiz(title: String(localized: "Yanlış ve boşlar"), questions: wrong.map { session.questions[$0] })
                    } label: {
                        Label("Yanlış ve boşları tekrar çöz (\(wrong.count))", systemImage: "arrow.counterclockwise")
                    }
                    .buttonStyle(PrimaryButtonStyle())
                }
                Button("Bitir", action: close)
                    .buttonStyle(SecondaryButtonStyle())
            }
            .padding(.horizontal, 16)
            .padding(.vertical, 10)
            .background(.ultraThinMaterial)
        }
    }

    private var indices: [Int] {
        session.questions.indices.filter { i in
            switch filter {
            case .all: true
            case .wrong: session.isCorrect(i) == false
            case .blank: session.isCorrect(i) == nil
            case .correct: session.isCorrect(i) == true
            }
        }
    }

    private func reviewRow(_ i: Int) -> some View {
        let q = session.questions[i]
        let result = session.isCorrect(i)
        return HStack(alignment: .top, spacing: 12) {
            Image(systemName: result == true ? "checkmark.circle.fill" : (result == false ? "xmark.circle.fill" : "minus.circle.fill"))
                .font(.title3)
                .foregroundStyle(result == true ? Theme.success : (result == false ? Theme.danger : Theme.textTertiary))
            VStack(alignment: .leading, spacing: 4) {
                Text("Soru \(i + 1) · \(q.kindTitle)")
                    .font(.caption.weight(.semibold))
                    .foregroundStyle(Theme.textTertiary)
                Text(q.prompt)
                    .font(.subheadline)
                    .foregroundStyle(Theme.textPrimary)
                    .lineLimit(2)
                    .multilineTextAlignment(.leading)
            }
            Spacer(minLength: 0)
            Image(systemName: "chevron.right")
                .font(.footnote.weight(.semibold))
                .foregroundStyle(Theme.textTertiary)
                .padding(.top, 4)
        }
        .padding(14)
        .background(Theme.card, in: .rect(cornerRadius: 16))
        .overlay { RoundedRectangle(cornerRadius: 16).strokeBorder(Theme.stroke) }
    }

    private func tile(_ value: String, _ label: String, _ color: Color) -> some View {
        VStack(spacing: 4) {
            Text(value)
                .font(.title3.weight(.bold).monospacedDigit())
                .foregroundStyle(color)
                .lineLimit(1)
                .minimumScaleFactor(0.7)
            Text(label)
                .font(.caption)
                .foregroundStyle(Theme.textSecondary)
        }
        .frame(maxWidth: .infinity)
        .padding(.vertical, 12)
        .background(Theme.card, in: .rect(cornerRadius: 16))
        .overlay { RoundedRectangle(cornerRadius: 16).strokeBorder(Theme.stroke) }
    }

    private func color(for ratio: Double) -> Color {
        ratio >= 0.7 ? Theme.success : (ratio >= 0.45 ? .orange : Theme.danger)
    }

    private func headline(_ ratio: Double) -> String {
        switch ratio {
        case 0.9...: String(localized: "Mükemmel!")
        case 0.7..<0.9: String(localized: "Çok iyi")
        case 0.5..<0.7: String(localized: "İyi gidiyorsun")
        default: String(localized: "Tekrar zamanı")
        }
    }
}

/// Swipe through the answered questions with their explanations.
private struct ReviewPager: View {
    @Environment(AppModel.self) private var app
    let session: QuizSession
    let indices: [Int]
    @State var start: Int
    @Binding var scene: AnatomyScene?
    @State private var showEntry: AtlasEntry?

    var body: some View {
        TabView(selection: $start) {
            ForEach(indices, id: \.self) { i in
                ScrollView {
                    QuestionContent(question: session.questions[i], number: i + 1, chosen: session.answer(at: i),
                                    revealed: true, scene: $scene, onChoose: nil, onOpenEntry: { showEntry = $0 })
                        .padding(16)
                        .padding(.bottom, 40)
                }
                .scrollIndicators(.hidden)
                .tag(i)
            }
        }
        .tabViewStyle(.page(indexDisplayMode: .never))
        .themedBackground()
        .navigationTitle("Soru \(start + 1)")
        .navigationBarTitleDisplayMode(.inline)
        .toolbar {
            ToolbarItem(placement: .primaryAction) {
                let key = session.questions[start].id
                let saved = app.study.isBookmarked(key)
                Button {
                    app.study.toggleBookmark(key)
                } label: {
                    Image(systemName: saved ? "bookmark.fill" : "bookmark")
                        .foregroundStyle(saved ? Theme.gold : Theme.textPrimary)
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
            .appOverlays()
            .preferredColorScheme(.dark)
        }
    }
}
