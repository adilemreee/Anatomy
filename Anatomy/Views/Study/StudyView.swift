//
//  StudyView.swift
//  Anatomy
//

import SwiftUI

/// The Study tab: today's goal, quick start, the question bank by system,
/// timed exams, practice modes, review and statistics.
struct StudyView: View {
    @Environment(AppModel.self) private var app
    @AppStorage("study.dailyGoal") private var dailyGoal = 20
    @AppStorage("study.scope") private var scopeID = ""
    @State private var path = NavigationPath()

    var body: some View {
        NavigationStack(path: $path) {
            ScrollView {
                VStack(alignment: .leading, spacing: 28) {
                    todayCard
                    quickStart
                    bankSection
                    examSection
                    practiceSection
                    reviewSection
                    statsTeaser
                }
                .padding(.horizontal, 16)
                .padding(.top, 4)
                .padding(.bottom, 32)
            }
            .scrollIndicators(.hidden)
            .themedBackground()
            .navigationTitle("Çalış")
            .navigationDestination(for: BodySystem.self) { SystemQuizView(system: $0) }
            .navigationDestination(for: StudyRoute.self) { route in
                switch route {
                case .statistics: StatsView()
                case .exams: ExamListView()
                case .flashcards: FlashcardSetupView()
                }
            }
            .onAppear {
                // -StudyRoute flashcards opens a study screen on launch (screenshots, testing).
                if path.isEmpty, UserDefaults.standard.string(forKey: "StudyRoute") == "flashcards" {
                    path.append(StudyRoute.flashcards)
                }
            }
        }
    }

    /// The system the quick start and practice modes use; nil for all.
    private var scope: BodySystem? {
        scopeID.isEmpty ? nil : app.store.system(scopeID)
    }

    private var scopeSystems: Set<String>? {
        scope.map { [$0.id] }
    }

    // MARK: Today

    private var todayCard: some View {
        let today = app.study.answeredToday
        let progress = min(1, Double(today) / Double(max(dailyGoal, 1)))
        return HStack(spacing: 18) {
            ZStack {
                ProgressRing(value: progress, color: progress >= 1 ? Theme.success : Theme.accent, lineWidth: 7)
                VStack(spacing: 0) {
                    Text("\(today)")
                        .font(.title2.weight(.bold))
                        .foregroundStyle(Theme.textPrimary)
                        .contentTransition(.numericText())
                    Text("/\(dailyGoal)")
                        .font(.caption2.weight(.semibold))
                        .foregroundStyle(Theme.textTertiary)
                }
            }
            .frame(width: 74, height: 74)

            VStack(alignment: .leading, spacing: 8) {
                Text(progress >= 1 ? String(localized: "Günlük hedef tamam!") : String(localized: "Bugünkü hedefin"))
                    .font(.headline)
                    .foregroundStyle(Theme.textPrimary)
                HStack(spacing: 14) {
                    stat(icon: "flame.fill", color: .orange, value: "\(app.study.streak)",
                         label: app.study.streak == 1 ? String(localized: LocalizedStringResource("streak.oneDay", defaultValue: "gün seri")) : String(localized: "gün seri"))
                    stat(icon: "target", color: Theme.success,
                         value: app.study.answered == 0 ? "–" : (app.study.accuracy).formatted(.percent.precision(.fractionLength(0))), label: String(localized: "doğruluk"))
                }
                if let left = app.freeQuestionsLeft {
                    Button {
                        app.requirePremium(.questions)
                    } label: {
                        HStack(spacing: 6) {
                            PremiumBadge(compact: true)
                            Text(left > 0 ? String(localized: "Bugün \(left) ücretsiz soru kaldı") : String(localized: "Ücretsiz sorular bitti"))
                                .font(.caption.weight(.semibold))
                                .foregroundStyle(Theme.gold)
                        }
                    }
                    .buttonStyle(.plain)
                }
            }
            Spacer(minLength: 0)
        }
        .padding(18)
        .background(Theme.card, in: .rect(cornerRadius: 24))
        .overlay { RoundedRectangle(cornerRadius: 24).strokeBorder(Theme.stroke) }
    }

    private func stat(icon: String, color: Color, value: String, label: String) -> some View {
        HStack(spacing: 5) {
            Image(systemName: icon)
                .font(.caption)
                .foregroundStyle(color)
            Text(value)
                .font(.subheadline.weight(.bold))
                .foregroundStyle(Theme.textPrimary)
            Text(label)
                .font(.caption)
                .foregroundStyle(Theme.textSecondary)
        }
    }

    // MARK: Quick start

    private var quickStart: some View {
        VStack(alignment: .leading, spacing: 16) {
            HStack {
                Eyebrow(text: String(localized: "Hızlı başla"), color: .white.opacity(0.75))
                Spacer()
                scopeMenu
            }
            VStack(alignment: .leading, spacing: 6) {
                Text(String(localized: "Karma test"))
                    .font(.title.weight(.bold))
                    .foregroundStyle(.white)
                Text("Soru bankası, klinik vakalar ve atlas sorularından sana göre seçilmiş 10 soru. Her cevabın açıklaması anında.")
                    .font(.subheadline)
                    .foregroundStyle(.white.opacity(0.85))
                    .fixedSize(horizontal: false, vertical: true)
            }
            Button {
                app.startQuiz(QuizConfig(title: String(localized: "Karma test"), source: .mixed, systems: scopeSystems, count: 10))
            } label: {
                Label("Başla", systemImage: "play.fill")
            }
            .buttonStyle(PrimaryButtonStyle(gradient: LinearGradient(colors: [.white, .white], startPoint: .top, endPoint: .bottom),
                                            foreground: Color(hex: "1B3FA8")))
        }
        .padding(20)
        .background {
            ZStack(alignment: .topTrailing) {
                LinearGradient(colors: [Color(hex: "2F6BFF"), Color(hex: "6A4CFF")], startPoint: .topLeading, endPoint: .bottomTrailing)
                Image(systemName: "brain.head.profile")
                    .font(.system(size: 150, weight: .thin))
                    .foregroundStyle(.white.opacity(0.08))
                    .offset(x: 30, y: -10)
            }
        }
        .clipShape(.rect(cornerRadius: 26))
    }

    private var scopeMenu: some View {
        Menu {
            Button {
                scopeID = ""
            } label: {
                Label("Tüm sistemler", systemImage: scope == nil ? "checkmark" : "square.grid.2x2")
            }
            Divider()
            ForEach(app.store.systems) { system in
                Button {
                    if Access.canOpen(systemID: system.id, premium: app.isPremium) {
                        scopeID = system.id
                    } else {
                        app.requirePremium(.system(system.tr))
                    }
                } label: {
                    Label(system.tr, systemImage: scope?.id == system.id ? "checkmark" : system.icon)
                }
            }
        } label: {
            HStack(spacing: 4) {
                Text(scope?.tr ?? String(localized: "Tüm sistemler"))
                Image(systemName: "chevron.down")
                    .font(.caption2.weight(.bold))
            }
            .font(.caption.weight(.semibold))
            .foregroundStyle(.white)
            .padding(.horizontal, 10)
            .padding(.vertical, 6)
            .background(.white.opacity(0.18), in: .capsule)
        }
    }

    // MARK: Question bank

    private var bankSection: some View {
        VStack(alignment: .leading, spacing: 12) {
            SectionHeader(title: String(localized: "Soru bankası"),
                          subtitle: app.bank.isLoaded ? String(localized: "\(app.bank.questions.count) özgün soru · açıklamalı cevaplar") : String(localized: "Yükleniyor…"))
            VStack(spacing: 0) {
                ForEach(Array(app.store.systems.enumerated()), id: \.element.id) { i, system in
                    NavigationLink(value: system) {
                        BankSystemRow(system: system, locked: !Access.canOpen(systemID: system.id, premium: app.isPremium))
                    }
                    .buttonStyle(.plain)
                    if i < app.store.systems.count - 1 {
                        Divider().overlay(Theme.stroke).padding(.leading, 62)
                    }
                }
            }
            .background(Theme.card, in: .rect(cornerRadius: 20))
            .overlay { RoundedRectangle(cornerRadius: 20).strokeBorder(Theme.stroke) }
        }
    }

    // MARK: Exams

    private var examSection: some View {
        VStack(alignment: .leading, spacing: 12) {
            SectionHeader(title: String(localized: "Deneme sınavları"), subtitle: String(localized: "Süreli, TUS formatında; sonuçlar sınav sonunda"))
            ScrollView(.horizontal) {
                HStack(spacing: 12) {
                    ForEach(ExamPreset.all) { preset in
                        ExamCard(preset: preset, locked: !app.isPremium) {
                            app.startQuiz(preset.config)
                        }
                    }
                }
                .padding(.horizontal, 16)
            }
            .scrollIndicators(.hidden)
            .padding(.horizontal, -16)
            if !app.study.exams.isEmpty {
                NavigationLink(value: StudyRoute.exams) {
                    HStack {
                        Image(systemName: "clock.arrow.circlepath")
                            .foregroundStyle(Theme.accent)
                        Text("Sınav geçmişi (\(app.study.exams.count))")
                            .font(.subheadline.weight(.semibold))
                            .foregroundStyle(Theme.textPrimary)
                        Spacer()
                        Image(systemName: "chevron.right")
                            .font(.footnote.weight(.semibold))
                            .foregroundStyle(Theme.textTertiary)
                    }
                    .padding(14)
                    .background(Theme.card, in: .rect(cornerRadius: 16))
                }
                .buttonStyle(.plain)
            }
        }
    }

    // MARK: Practice

    private var practiceSection: some View {
        VStack(alignment: .leading, spacing: 12) {
            SectionHeader(title: String(localized: "Pratik"), subtitle: scope.map { String(localized: "\($0.tr) için") } ?? String(localized: "Tüm sistemlerden"))
            LazyVGrid(columns: [GridItem(.flexible(), spacing: 12), GridItem(.flexible(), spacing: 12)], spacing: 12) {
                ForEach([QuizSource.clinical, .innervation, .landmarks, .facts, .terms, .model, .weak, .bank], id: \.self) { source in
                    ModeTile(source: source) {
                        app.startQuiz(QuizConfig(title: source.title, source: source, systems: scopeSystems, count: 10))
                    }
                }
            }
        }
    }

    // MARK: Review

    private var reviewSection: some View {
        let due = dueCards
        return VStack(alignment: .leading, spacing: 12) {
            SectionHeader(title: String(localized: "Tekrar"))
            VStack(spacing: 0) {
                ReviewRow(source: .wrongs, count: app.study.wrongs.count) {
                    app.startQuiz(QuizConfig(title: QuizSource.wrongs.title, source: .wrongs, count: 20, preferNew: false))
                }
                Divider().overlay(Theme.stroke).padding(.leading, 62)
                ReviewRow(source: .bookmarks, count: app.study.bookmarks.count) {
                    app.startQuiz(QuizConfig(title: QuizSource.bookmarks.title, source: .bookmarks, count: 30, preferNew: false))
                }
                Divider().overlay(Theme.stroke).padding(.leading, 62)
                NavigationLink(value: StudyRoute.flashcards) {
                    HStack(spacing: 14) {
                        SystemBadge(icon: "rectangle.on.rectangle.angled.fill", color: Color(hex: "B07CFF"), size: 40)
                        VStack(alignment: .leading, spacing: 2) {
                            Text("Bilgi kartları")
                                .font(.headline)
                                .foregroundStyle(Theme.textPrimary)
                            Text(due > 0 ? String(localized: "\(due) kartın tekrar zamanı geldi") : String(localized: "6 deste · aralıklı tekrar ile kalıcı öğren"))
                                .font(.subheadline)
                                .foregroundStyle(Theme.textSecondary)
                        }
                        Spacer()
                        if due > 0 {
                            CountPill(count: due, color: Color(hex: "B07CFF"))
                        }
                        Image(systemName: "chevron.right")
                            .font(.footnote.weight(.semibold))
                            .foregroundStyle(Theme.textTertiary)
                    }
                    .padding(14)
                    .contentShape(.rect)
                }
                .buttonStyle(.plain)
            }
            .background(Theme.card, in: .rect(cornerRadius: 20))
            .overlay { RoundedRectangle(cornerRadius: 20).strokeBorder(Theme.stroke) }
        }
    }

    private var dueCards: Int {
        app.dueCards(systems: scopeSystems)
    }

    // MARK: Statistics

    private var statsTeaser: some View {
        NavigationLink(value: StudyRoute.statistics) {
            VStack(alignment: .leading, spacing: 14) {
                HStack {
                    Label("İstatistikler", systemImage: "chart.bar.xaxis")
                        .font(.headline)
                        .foregroundStyle(Theme.textPrimary)
                    Spacer()
                    if !app.isPremium { PremiumBadge() }
                    Image(systemName: "chevron.right")
                        .font(.footnote.weight(.semibold))
                        .foregroundStyle(Theme.textTertiary)
                }
                ActivityBars(days: app.study.activity(days: 14), goal: dailyGoal)
                    .frame(height: 64)
                Text("Son 14 gün · toplam \(app.study.answered) soru")
                    .font(.caption)
                    .foregroundStyle(Theme.textSecondary)
            }
            .padding(16)
            .background(Theme.card, in: .rect(cornerRadius: 20))
            .overlay { RoundedRectangle(cornerRadius: 20).strokeBorder(Theme.stroke) }
        }
        .buttonStyle(PressableStyle())
    }
}

enum StudyRoute: Hashable {
    case statistics, exams, flashcards
}

// MARK: - Exams

/// A ready-made timed exam.
struct ExamPreset: Identifiable {
    let id: String
    let title: String
    let subtitle: String
    let count: Int
    let minutes: Int
    let level: QuestionLevel?
    let colors: [Color]

    var config: QuizConfig {
        QuizConfig(title: title, source: .bank, level: level, count: count, isExam: true,
                   timeLimit: TimeInterval(minutes * 60), preferNew: true)
    }

    static let all: [ExamPreset] = [
        ExamPreset(id: "mini", title: String(localized: "Mini deneme"), subtitle: String(localized: "Tüm sistemler"), count: 20, minutes: 25, level: nil,
                   colors: [Color(hex: "1F8F7A"), Color(hex: "155E75")]),
        ExamPreset(id: "basic", title: String(localized: "Temel tekrar"), subtitle: String(localized: "Temel düzey sorular"), count: 30, minutes: 30, level: .basic,
                   colors: [Color(hex: "2E8B57"), Color(hex: "1B5E3B")]),
        ExamPreset(id: "tus", title: String(localized: "TUS anatomi denemesi"), subtitle: String(localized: "Yalnızca TUS düzeyi"), count: 40, minutes: 50, level: .tus,
                   colors: [Color(hex: "B4527A"), Color(hex: "6D2A8C")]),
        ExamPreset(id: "faculty", title: String(localized: "Komite denemesi"), subtitle: String(localized: "Fakülte düzeyi"), count: 50, minutes: 60, level: .faculty,
                   colors: [Color(hex: "C27A1E"), Color(hex: "8A3B12")]),
        ExamPreset(id: "marathon", title: String(localized: "Maraton"), subtitle: String(localized: "Tüm bankadan karışık"), count: 100, minutes: 120, level: nil,
                   colors: [Color(hex: "3A4BC2"), Color(hex: "1D2470")]),
    ]
}

private struct ExamCard: View {
    let preset: ExamPreset
    let locked: Bool
    let action: () -> Void

    var body: some View {
        Button(action: action) {
            VStack(alignment: .leading, spacing: 10) {
                HStack {
                    Image(systemName: "timer")
                        .font(.title3)
                    Spacer()
                    if locked { LockBadge() }
                }
                Spacer(minLength: 0)
                Text(preset.title)
                    .font(.headline)
                    .multilineTextAlignment(.leading)
                    .fixedSize(horizontal: false, vertical: true)
                Text("\(preset.count) soru · \(preset.minutes) dk")
                    .font(.subheadline.weight(.semibold))
                    .opacity(0.9)
                Text(preset.subtitle)
                    .font(.caption)
                    .opacity(0.75)
            }
            .foregroundStyle(.white)
            .padding(16)
            .frame(width: 170, height: 170, alignment: .leading)
            .background(LinearGradient(colors: preset.colors, startPoint: .topLeading, endPoint: .bottomTrailing),
                        in: .rect(cornerRadius: 22))
        }
        .buttonStyle(PressableStyle())
    }
}

// MARK: - Rows and tiles

private struct BankSystemRow: View {
    @Environment(AppModel.self) private var app
    let system: BodySystem
    let locked: Bool

    var body: some View {
        let questions = app.bank.questions(in: system.id)
        let solved = questions.filter { app.study.questionScore($0.id).seen > 0 }.count
        HStack(spacing: 14) {
            SystemBadge(icon: system.icon, color: system.tint, size: 40)
            VStack(alignment: .leading, spacing: 5) {
                HStack(spacing: 6) {
                    Text(system.tr)
                        .font(.subheadline.weight(.semibold))
                        .foregroundStyle(Theme.textPrimary)
                    if locked { LockBadge() }
                }
                ProgressBar(value: questions.isEmpty ? 0 : Double(solved) / Double(questions.count), color: system.tint)
                    .frame(height: 4)
            }
            Text("\(solved)/\(questions.count)")
                .font(.caption.monospacedDigit())
                .foregroundStyle(Theme.textSecondary)
                .frame(minWidth: 52, alignment: .trailing)
            Image(systemName: "chevron.right")
                .font(.footnote.weight(.semibold))
                .foregroundStyle(Theme.textTertiary)
        }
        .padding(.horizontal, 14)
        .padding(.vertical, 12)
        .contentShape(.rect)
    }
}

private struct ModeTile: View {
    let source: QuizSource
    let action: () -> Void

    var body: some View {
        let tint = Color(hex: source.tint)
        Button(action: action) {
            VStack(alignment: .leading, spacing: 10) {
                Image(systemName: source.icon)
                    .font(.title3)
                    .foregroundStyle(tint)
                    .frame(width: 40, height: 40)
                    .background(tint.opacity(0.15), in: .rect(cornerRadius: 12))
                Text(source.title)
                    .font(.subheadline.weight(.semibold))
                    .foregroundStyle(Theme.textPrimary)
                Text(source.subtitle)
                    .font(.caption)
                    .foregroundStyle(Theme.textSecondary)
                    .lineLimit(2, reservesSpace: true)
                    .multilineTextAlignment(.leading)
            }
            .padding(14)
            .frame(maxWidth: .infinity, alignment: .leading)
            .background(Theme.card, in: .rect(cornerRadius: 20))
            .overlay { RoundedRectangle(cornerRadius: 20).strokeBorder(Theme.stroke) }
        }
        .buttonStyle(PressableStyle())
    }
}

private struct ReviewRow: View {
    let source: QuizSource
    let count: Int
    let action: () -> Void

    var body: some View {
        let tint = Color(hex: source.tint)
        Button(action: action) {
            HStack(spacing: 14) {
                SystemBadge(icon: source.icon, color: tint, size: 40)
                VStack(alignment: .leading, spacing: 2) {
                    Text(source.title)
                        .font(.headline)
                        .foregroundStyle(Theme.textPrimary)
                    Text(source.subtitle)
                        .font(.subheadline)
                        .foregroundStyle(Theme.textSecondary)
                }
                Spacer()
                if count > 0 {
                    CountPill(count: count, color: tint)
                }
                Image(systemName: "chevron.right")
                    .font(.footnote.weight(.semibold))
                    .foregroundStyle(Theme.textTertiary)
            }
            .padding(14)
            .contentShape(.rect)
        }
        .buttonStyle(.plain)
    }
}

struct CountPill: View {
    let count: Int
    let color: Color

    var body: some View {
        Text("\(count)")
            .font(.caption.weight(.bold).monospacedDigit())
            .foregroundStyle(color)
            .padding(.horizontal, 8)
            .padding(.vertical, 3)
            .background(color.opacity(0.16), in: .capsule)
    }
}

struct ProgressBar: View {
    let value: Double
    var color: Color = Theme.accent

    var body: some View {
        GeometryReader { geo in
            ZStack(alignment: .leading) {
                Capsule().fill(Color.white.opacity(0.08))
                Capsule().fill(color)
                    .frame(width: max(value > 0 ? 4 : 0, geo.size.width * min(1, value)))
            }
        }
    }
}

/// Answers per day as small bars, the goal as a dashed line.
struct ActivityBars: View {
    let days: [(date: Date, tally: StudyStore.Tally)]
    let goal: Int

    var body: some View {
        let peak = max(goal, days.map(\.tally.answered).max() ?? 0, 1)
        GeometryReader { geo in
            let gap: CGFloat = 4
            let width = (geo.size.width - gap * CGFloat(days.count - 1)) / CGFloat(max(days.count, 1))
            ZStack(alignment: .bottomLeading) {
                Path { p in
                    let y = geo.size.height * (1 - CGFloat(goal) / CGFloat(peak))
                    p.move(to: CGPoint(x: 0, y: y))
                    p.addLine(to: CGPoint(x: geo.size.width, y: y))
                }
                .stroke(Theme.textTertiary.opacity(0.6), style: StrokeStyle(lineWidth: 1, dash: [3, 3]))
                HStack(alignment: .bottom, spacing: gap) {
                    ForEach(Array(days.enumerated()), id: \.offset) { i, day in
                        let h = geo.size.height * CGFloat(day.tally.answered) / CGFloat(peak)
                        RoundedRectangle(cornerRadius: 3)
                            .fill(day.tally.answered >= goal ? Theme.success : (i == days.count - 1 ? Theme.accent : Theme.accent.opacity(0.55)))
                            .frame(width: width, height: max(3, h))
                            .opacity(day.tally.answered == 0 ? 0.25 : 1)
                    }
                }
            }
        }
    }
}
