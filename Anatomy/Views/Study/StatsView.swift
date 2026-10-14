//
//  StatsView.swift
//  Anatomy
//

import Charts
import SwiftUI

/// Detailed statistics (Premium): activity, accuracy by system, exam history.
struct StatsView: View {
    @Environment(AppModel.self) private var app
    @AppStorage("study.dailyGoal") private var dailyGoal = 20

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 22) {
                overview
                if app.isPremium {
                    details
                } else {
                    ZStack {
                        details
                            .blur(radius: 8)
                            .allowsHitTesting(false)
                            .accessibilityHidden(true)
                        VStack(spacing: 12) {
                            LockBadge()
                                .scaleEffect(1.6)
                                .padding(.bottom, 4)
                            Text("Ayrıntılı istatistikler Premium'da")
                                .font(.headline)
                                .foregroundStyle(Theme.textPrimary)
                            Text("Sistem bazında başarı, 30 günlük grafik, sınav geçmişi ve zayıf konular.")
                                .font(.subheadline)
                                .foregroundStyle(Theme.textSecondary)
                                .multilineTextAlignment(.center)
                            Button {
                                app.requirePremium(.statistics)
                            } label: {
                                Label("Premium ile aç", systemImage: "lock.open.fill")
                            }
                            .buttonStyle(PrimaryButtonStyle(gradient: Theme.goldGradient, foreground: Color(hex: "2A1D05")))
                            .frame(maxWidth: 260)
                        }
                        .padding(24)
                        .background(Theme.surface.opacity(0.92), in: .rect(cornerRadius: 24))
                        .padding(.horizontal, 8)
                    }
                }
            }
            .padding(16)
            .padding(.bottom, 24)
        }
        .scrollIndicators(.hidden)
        .themedBackground()
        .navigationTitle("İstatistikler")
        .navigationBarTitleDisplayMode(.inline)
    }

    private var overview: some View {
        let study = app.study
        let solvedBank = app.bank.questions.filter { study.questionScore($0.id).seen > 0 }.count
        return LazyVGrid(columns: [GridItem(.flexible(), spacing: 12), GridItem(.flexible(), spacing: 12)], spacing: 12) {
            tile("\(study.answered)", "Cevaplanan soru", "checkmark.circle.fill", Theme.accent)
            tile(study.answered == 0 ? "–" : "%\(Int(study.accuracy * 100))", "Genel doğruluk", "target", Theme.success)
            tile("\(study.streak)", "Günlük seri", "flame.fill", .orange)
            tile("\(solvedBank)/\(app.bank.questions.count)", "Bankadan çözülen", "books.vertical.fill", Color(hex: "B07CFF"))
        }
    }

    private var details: some View {
        VStack(alignment: .leading, spacing: 22) {
            Card {
                VStack(alignment: .leading, spacing: 12) {
                    Eyebrow(text: "Son 30 gün")
                    let days = app.study.activity(days: 30)
                    Chart {
                        ForEach(Array(days.enumerated()), id: \.offset) { _, day in
                            BarMark(x: .value("Gün", day.date, unit: .day), y: .value("Doğru", day.tally.correct))
                                .foregroundStyle(Theme.success)
                            BarMark(x: .value("Gün", day.date, unit: .day), y: .value("Yanlış", day.tally.answered - day.tally.correct))
                                .foregroundStyle(Theme.danger.opacity(0.75))
                        }
                        RuleMark(y: .value("Hedef", dailyGoal))
                            .lineStyle(StrokeStyle(lineWidth: 1, dash: [4, 4]))
                            .foregroundStyle(Theme.textTertiary)
                    }
                    .chartXAxis {
                        AxisMarks(values: .stride(by: .day, count: 7)) { _ in
                            AxisValueLabel(format: .dateTime.day().month(.abbreviated), centered: false)
                                .foregroundStyle(Theme.textTertiary)
                        }
                    }
                    .chartYAxis {
                        AxisMarks { _ in
                            AxisGridLine().foregroundStyle(Theme.stroke)
                            AxisValueLabel().foregroundStyle(Theme.textTertiary)
                        }
                    }
                    .frame(height: 170)
                    HStack(spacing: 14) {
                        legend(Theme.success, "Doğru")
                        legend(Theme.danger.opacity(0.75), "Yanlış")
                        legend(Theme.textTertiary, "Günlük hedef")
                    }
                    .font(.caption)
                }
            }

            Card {
                VStack(alignment: .leading, spacing: 14) {
                    Eyebrow(text: "Sistemlere göre başarı")
                    ForEach(app.store.systems) { system in
                        let tally = app.study.systems[system.id] ?? StudyStore.Tally()
                        VStack(alignment: .leading, spacing: 6) {
                            HStack {
                                Image(systemName: system.icon)
                                    .foregroundStyle(system.tint)
                                    .frame(width: 20)
                                Text(system.tr)
                                    .font(.subheadline)
                                    .foregroundStyle(Theme.textPrimary)
                                Spacer()
                                Text(tally.answered == 0 ? "–" : "%\(Int(tally.accuracy * 100)) · \(tally.answered) soru")
                                    .font(.caption.monospacedDigit())
                                    .foregroundStyle(Theme.textSecondary)
                            }
                            ProgressBar(value: tally.accuracy, color: system.tint)
                                .frame(height: 5)
                                .opacity(tally.answered == 0 ? 0.4 : 1)
                        }
                    }
                }
            }

            let weak = weakEntries
            if !weak.isEmpty {
                Card {
                    VStack(alignment: .leading, spacing: 12) {
                        Eyebrow(text: "En zayıf yapıların")
                        ForEach(weak) { entry in
                            let score = app.study.score(entry.id)
                            HStack {
                                VStack(alignment: .leading, spacing: 2) {
                                    Text(entry.tr)
                                        .font(.subheadline.weight(.medium))
                                        .foregroundStyle(Theme.textPrimary)
                                    Text(entry.la)
                                        .font(Theme.latin(.caption))
                                        .foregroundStyle(Theme.textSecondary)
                                }
                                Spacer()
                                Text("\(score.correct)/\(score.seen)")
                                    .font(.caption.weight(.semibold).monospacedDigit())
                                    .foregroundStyle(Theme.danger)
                            }
                        }
                        Button {
                            app.startQuiz(QuizConfig(title: QuizSource.weak.title, source: .weak, count: 10))
                        } label: {
                            Label("Zayıf konularımı çalış", systemImage: "scope")
                        }
                        .buttonStyle(SecondaryButtonStyle())
                    }
                }
            }

            if !app.study.exams.isEmpty {
                Card {
                    VStack(alignment: .leading, spacing: 12) {
                        Eyebrow(text: "Deneme netleri")
                        let exams = Array(app.study.exams.prefix(12).reversed())
                        Chart {
                            ForEach(Array(exams.enumerated()), id: \.offset) { i, exam in
                                LineMark(x: .value("Sınav", i + 1), y: .value("Başarı", Double(exam.correct) / Double(max(exam.total, 1)) * 100))
                                    .foregroundStyle(Theme.accent)
                                PointMark(x: .value("Sınav", i + 1), y: .value("Başarı", Double(exam.correct) / Double(max(exam.total, 1)) * 100))
                                    .foregroundStyle(Theme.accent)
                            }
                        }
                        .chartYScale(domain: 0...100)
                        .chartXAxis(.hidden)
                        .chartYAxis {
                            AxisMarks(values: [0, 50, 100]) { value in
                                AxisGridLine().foregroundStyle(Theme.stroke)
                                AxisValueLabel { Text("%\(value.as(Int.self) ?? 0)") }.foregroundStyle(Theme.textTertiary)
                            }
                        }
                        .frame(height: 130)
                        NavigationLink(value: StudyRoute.exams) {
                            Text("Tüm sınavlar")
                                .font(.subheadline.weight(.semibold))
                                .foregroundStyle(Theme.accent)
                        }
                    }
                }
            }
        }
    }

    private var weakEntries: [AtlasEntry] {
        app.store.entries
            .filter { app.study.score($0.id).seen >= 2 }
            .sorted { app.study.score($0.id).mastery < app.study.score($1.id).mastery }
            .filter { app.study.score($0.id).mastery < 0.6 }
            .prefix(6)
            .map { $0 }
    }

    private func tile(_ value: String, _ label: String, _ icon: String, _ color: Color) -> some View {
        VStack(alignment: .leading, spacing: 6) {
            Image(systemName: icon)
                .foregroundStyle(color)
            Text(value)
                .font(.title2.weight(.bold).monospacedDigit())
                .foregroundStyle(Theme.textPrimary)
                .lineLimit(1)
                .minimumScaleFactor(0.7)
            Text(label)
                .font(.caption)
                .foregroundStyle(Theme.textSecondary)
        }
        .frame(maxWidth: .infinity, alignment: .leading)
        .padding(14)
        .background(Theme.card, in: .rect(cornerRadius: 18))
        .overlay { RoundedRectangle(cornerRadius: 18).strokeBorder(Theme.stroke) }
    }

    private func legend(_ color: Color, _ text: String) -> some View {
        HStack(spacing: 5) {
            RoundedRectangle(cornerRadius: 2).fill(color).frame(width: 10, height: 10)
            Text(text).foregroundStyle(Theme.textSecondary)
        }
    }
}

/// Every finished exam.
struct ExamListView: View {
    @Environment(AppModel.self) private var app

    var body: some View {
        List {
            ForEach(app.study.exams) { exam in
                HStack(spacing: 14) {
                    let ratio = Double(exam.correct) / Double(max(exam.total, 1))
                    ZStack {
                        ProgressRing(value: ratio, color: ratio >= 0.7 ? Theme.success : (ratio >= 0.45 ? .orange : Theme.danger), lineWidth: 4)
                        Text("\(Int(ratio * 100))")
                            .font(.caption.weight(.bold))
                    }
                    .frame(width: 40, height: 40)
                    VStack(alignment: .leading, spacing: 3) {
                        Text(exam.title)
                            .font(.subheadline.weight(.semibold))
                        Text(exam.date.formatted(date: .abbreviated, time: .shortened))
                            .font(.caption)
                            .foregroundStyle(Theme.textSecondary)
                    }
                    Spacer()
                    VStack(alignment: .trailing, spacing: 3) {
                        Text(String(format: "%.2f net", exam.net))
                            .font(.subheadline.weight(.bold).monospacedDigit())
                        Text("\(exam.correct)D · \(exam.wrong)Y · \(exam.total - exam.correct - exam.wrong)B")
                            .font(.caption.monospacedDigit())
                            .foregroundStyle(Theme.textSecondary)
                    }
                }
                .listRowBackground(Theme.card)
            }
        }
        .scrollContentBackground(.hidden)
        .themedBackground()
        .navigationTitle("Sınav geçmişi")
        .navigationBarTitleDisplayMode(.inline)
    }
}
