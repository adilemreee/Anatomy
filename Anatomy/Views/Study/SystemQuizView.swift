//
//  SystemQuizView.swift
//  Anatomy
//

import SwiftUI

/// The question bank of one body system: settings and topic tests.
struct SystemQuizView: View {
    @Environment(AppModel.self) private var app
    let system: BodySystem
    @AppStorage("quiz.count") private var count = 20
    @State private var level: QuestionLevel?
    @State private var clinicalOnly = false

    var body: some View {
        let questions = app.bank.questions(in: system.id)
        let locked = !Access.canOpen(systemID: system.id, premium: app.isPremium)
        ScrollView {
            VStack(alignment: .leading, spacing: 24) {
                header(questions: questions)
                settings
                Button {
                    start(group: nil)
                } label: {
                    Label(locked ? "Premium ile aç" : "Tüm konulardan \(count) soru", systemImage: locked ? "lock.open.fill" : "play.fill")
                }
                .buttonStyle(locked ? PrimaryButtonStyle(gradient: Theme.goldGradient, foreground: Color(hex: "2A1D05"))
                                    : PrimaryButtonStyle())

                VStack(alignment: .leading, spacing: 12) {
                    SectionHeader(title: "Konular", subtitle: "Bir konuya dokunarak o konunun testini başlat")
                    VStack(spacing: 0) {
                        let groups = system.groups
                        ForEach(Array(groups.enumerated()), id: \.element) { i, group in
                            let inGroup = questions.filter { $0.group == group }
                            topicRow(group: group, questions: inGroup, locked: locked)
                            if i < groups.count - 1 {
                                Divider().overlay(Theme.stroke).padding(.leading, 16)
                            }
                        }
                    }
                    .background(Theme.card, in: .rect(cornerRadius: 20))
                    .overlay { RoundedRectangle(cornerRadius: 20).strokeBorder(Theme.stroke) }
                }

                VStack(alignment: .leading, spacing: 12) {
                    SectionHeader(title: "Atlastan sorular", subtitle: "Maddelerden otomatik üretilen sorular")
                    LazyVGrid(columns: [GridItem(.flexible(), spacing: 12), GridItem(.flexible(), spacing: 12)], spacing: 12) {
                        ForEach([QuizSource.terms, .facts, .model, .weak], id: \.self) { source in
                            Button {
                                app.startQuiz(QuizConfig(title: "\(system.tr) · \(source.title)", source: source,
                                                         systems: [system.id], count: 10))
                            } label: {
                                HStack(spacing: 10) {
                                    Image(systemName: source.icon)
                                        .foregroundStyle(Color(hex: source.tint))
                                    Text(source.title)
                                        .font(.subheadline.weight(.semibold))
                                        .foregroundStyle(Theme.textPrimary)
                                        .lineLimit(1)
                                        .minimumScaleFactor(0.85)
                                    Spacer(minLength: 0)
                                }
                                .padding(14)
                                .background(Theme.card, in: .rect(cornerRadius: 16))
                                .overlay { RoundedRectangle(cornerRadius: 16).strokeBorder(Theme.stroke) }
                            }
                            .buttonStyle(PressableStyle())
                        }
                    }
                }
            }
            .padding(16)
            .padding(.bottom, 24)
        }
        .themedBackground()
        .navigationTitle(system.tr)
        .navigationBarTitleDisplayMode(.inline)
    }

    private func header(questions: [BankQuestion]) -> some View {
        let solved = questions.filter { app.study.questionScore($0.id).seen > 0 }
        let right = solved.filter { let s = app.study.questionScore($0.id); return s.correct > 0 && s.correct == s.seen }.count
        let clinical = questions.filter(\.clinical).count
        let tus = questions.filter { $0.level == .tus }.count
        return VStack(alignment: .leading, spacing: 16) {
            HStack(spacing: 14) {
                SystemBadge(icon: system.icon, color: system.tint, size: 54)
                VStack(alignment: .leading, spacing: 3) {
                    Text(system.tr)
                        .font(.title2.weight(.bold))
                        .foregroundStyle(Theme.textPrimary)
                    Text(system.la)
                        .font(Theme.latin(.subheadline))
                        .foregroundStyle(system.tint)
                }
            }
            HStack(spacing: 10) {
                metric("\(questions.count)", "soru")
                metric("\(clinical)", "klinik vaka")
                metric("\(tus)", "TUS düzeyi")
                metric(solved.isEmpty ? "–" : "%\(Int(Double(right) / Double(solved.count) * 100))", "başarı")
            }
            ProgressBar(value: questions.isEmpty ? 0 : Double(solved.count) / Double(questions.count), color: system.tint)
                .frame(height: 6)
            Text("\(solved.count) / \(questions.count) soru çözüldü")
                .font(.caption)
                .foregroundStyle(Theme.textSecondary)
        }
        .padding(18)
        .background(Theme.card, in: .rect(cornerRadius: 24))
        .overlay { RoundedRectangle(cornerRadius: 24).strokeBorder(Theme.stroke) }
    }

    private func metric(_ value: String, _ label: String) -> some View {
        VStack(alignment: .leading, spacing: 2) {
            Text(value)
                .font(.headline.monospacedDigit())
                .foregroundStyle(Theme.textPrimary)
            Text(label)
                .font(.caption2)
                .foregroundStyle(Theme.textSecondary)
                .lineLimit(1)
                .minimumScaleFactor(0.8)
        }
        .frame(maxWidth: .infinity, alignment: .leading)
    }

    private var settings: some View {
        VStack(alignment: .leading, spacing: 14) {
            VStack(alignment: .leading, spacing: 8) {
                Eyebrow(text: "Düzey")
                Picker("Düzey", selection: $level) {
                    Text("Tümü").tag(QuestionLevel?.none)
                    Text("Fakülte").tag(QuestionLevel?.some(.faculty))
                    Text("TUS").tag(QuestionLevel?.some(.tus))
                }
                .pickerStyle(.segmented)
            }
            VStack(alignment: .leading, spacing: 8) {
                Eyebrow(text: "Soru sayısı")
                Picker("Soru sayısı", selection: $count) {
                    ForEach([10, 20, 40, 60], id: \.self) { Text("\($0)").tag($0) }
                }
                .pickerStyle(.segmented)
            }
            Toggle(isOn: $clinicalOnly) {
                Label("Yalnızca klinik vakalar", systemImage: "stethoscope")
                    .font(.subheadline.weight(.medium))
                    .foregroundStyle(Theme.textPrimary)
            }
            .tint(Theme.clinical)
        }
        .padding(16)
        .background(Theme.card, in: .rect(cornerRadius: 20))
        .overlay { RoundedRectangle(cornerRadius: 20).strokeBorder(Theme.stroke) }
    }

    private func topicRow(group: String, questions: [BankQuestion], locked: Bool) -> some View {
        let solved = questions.filter { app.study.questionScore($0.id).seen > 0 }.count
        return Button {
            start(group: group)
        } label: {
            HStack(spacing: 12) {
                VStack(alignment: .leading, spacing: 6) {
                    Text(group)
                        .font(.subheadline.weight(.semibold))
                        .foregroundStyle(Theme.textPrimary)
                        .multilineTextAlignment(.leading)
                    ProgressBar(value: questions.isEmpty ? 0 : Double(solved) / Double(questions.count), color: system.tint)
                        .frame(height: 4)
                }
                Text("\(solved)/\(questions.count)")
                    .font(.caption.monospacedDigit())
                    .foregroundStyle(Theme.textSecondary)
                    .frame(minWidth: 46, alignment: .trailing)
                Image(systemName: locked ? "lock.fill" : "play.circle.fill")
                    .font(.title3)
                    .foregroundStyle(locked ? Theme.gold : system.tint)
            }
            .padding(.horizontal, 16)
            .padding(.vertical, 13)
            .contentShape(.rect)
        }
        .buttonStyle(.plain)
    }

    private func start(group: String?) {
        let title = group ?? system.tr
        app.startQuiz(QuizConfig(title: title, source: clinicalOnly ? .clinical : .bank, systems: [system.id],
                                 group: group, level: level, count: count))
    }
}
