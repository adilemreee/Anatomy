//
//  FlashcardsView.swift
//  Anatomy
//

import SwiftUI

/// A spaced repetition deck: due cards first, then new ones.
@MainActor
@Observable
final class FlashcardDeck: Identifiable {
    let id = UUID()
    private(set) var cards: [AtlasEntry]
    var index = 0
    private(set) var reviewed = 0
    private(set) var remembered = 0

    init(entries: [AtlasEntry], study: StudyStore, limit: Int = 25) {
        let due = entries.filter { study.isDue($0.id) }
            .sorted { (study.card($0.id)?.due ?? .distantPast) < (study.card($1.id)?.due ?? .distantPast) }
        let new = entries.filter { study.card($0.id) == nil }.shuffled()
            .sorted { study.score($0.id).mastery < study.score($1.id).mastery }
        cards = Array((due + new).prefix(limit))
        if cards.isEmpty {
            // Everything is scheduled for later: practise the earliest ones.
            cards = Array(entries.sorted { (study.card($0.id)?.due ?? .distantPast) < (study.card($1.id)?.due ?? .distantPast) }.prefix(limit))
        }
    }

    var current: AtlasEntry? { cards.indices.contains(index) ? cards[index] : nil }

    func grade(_ grade: StudyStore.CardGrade, study: StudyStore) {
        guard let entry = current else { return }
        study.grade(card: entry.id, grade)
        reviewed += 1
        if grade != .again { remembered += 1 }
        // Forgotten cards come back at the end of this session.
        if grade == .again { cards.append(entry) }
        index += 1
    }
}

struct FlashcardsView: View {
    @Environment(AppModel.self) private var app
    @Environment(\.dismiss) private var dismiss
    let deck: FlashcardDeck
    @State private var flipped = false

    var body: some View {
        NavigationStack {
            VStack(spacing: 18) {
                if let entry = deck.current {
                    ProgressBar(value: Double(deck.index) / Double(max(deck.cards.count, 1)))
                        .frame(height: 4)
                    card(entry)
                        .id("\(deck.index)-\(entry.id)")
                        .transition(.asymmetric(insertion: .move(edge: .trailing).combined(with: .opacity),
                                                removal: .move(edge: .leading).combined(with: .opacity)))
                    if flipped {
                        gradeButtons(entry)
                            .transition(.move(edge: .bottom).combined(with: .opacity))
                    } else {
                        Button {
                            withAnimation(.spring(duration: 0.45)) { flipped = true }
                        } label: {
                            Label("Cevabı göster", systemImage: "arrow.trianglehead.2.clockwise.rotate.90")
                        }
                        .buttonStyle(PrimaryButtonStyle())
                    }
                } else {
                    finished
                }
            }
            .padding(16)
            .animation(.snappy, value: deck.index)
            .animation(.snappy, value: flipped)
            .themedBackground()
            .navigationTitle(deck.current == nil ? "Bilgi kartları" : "Kart \(min(deck.index + 1, deck.cards.count))/\(deck.cards.count)")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button {
                        dismiss()
                    } label: {
                        Image(systemName: "xmark")
                    }
                    .accessibilityLabel("Kapat")
                }
            }
        }
        .preferredColorScheme(.dark)
    }

    private var finished: some View {
        VStack(spacing: 16) {
            Spacer()
            Image(systemName: "checkmark.seal.fill")
                .font(.system(size: 64))
                .foregroundStyle(Theme.success)
            Text("Bugünlük bu kadar!")
                .font(.title.weight(.bold))
                .foregroundStyle(Theme.textPrimary)
            Text("\(deck.reviewed) tekrar, \(deck.remembered) hatırlandı. Kartlar unutma eğrine göre yeniden planlandı.")
                .font(.subheadline)
                .foregroundStyle(Theme.textSecondary)
                .multilineTextAlignment(.center)
                .padding(.horizontal, 24)
            Spacer()
            Button("Kapat") { dismiss() }
                .buttonStyle(PrimaryButtonStyle())
        }
    }

    private func gradeButtons(_ entry: AtlasEntry) -> some View {
        HStack(spacing: 8) {
            gradeButton("Tekrar", .again, Theme.danger, entry)
            gradeButton("Zor", .hard, .orange, entry)
            gradeButton("İyi", .good, Theme.success, entry)
            gradeButton("Kolay", .easy, Theme.accent, entry)
        }
    }

    private func gradeButton(_ title: String, _ grade: StudyStore.CardGrade, _ color: Color, _ entry: AtlasEntry) -> some View {
        Button {
            flipped = false
            deck.grade(grade, study: app.study)
        } label: {
            VStack(spacing: 3) {
                Text(title)
                    .font(.subheadline.weight(.bold))
                Text(app.study.nextInterval(card: entry.id, grade))
                    .font(.caption2.weight(.medium))
                    .opacity(0.8)
            }
            .foregroundStyle(color)
            .frame(maxWidth: .infinity)
            .padding(.vertical, 11)
            .background(color.opacity(0.15), in: .rect(cornerRadius: 14))
            .overlay { RoundedRectangle(cornerRadius: 14).strokeBorder(color.opacity(0.35)) }
        }
        .buttonStyle(PressableStyle())
    }

    private func card(_ entry: AtlasEntry) -> some View {
        let system = app.store.system(entry.systemID)
        let tint = system?.tint ?? Theme.accent
        return ZStack {
            // Front
            VStack(spacing: 16) {
                if let system {
                    SystemBadge(icon: system.icon, color: tint, size: 56)
                }
                Text(entry.tr)
                    .font(.largeTitle.weight(.bold))
                    .foregroundStyle(Theme.textPrimary)
                    .multilineTextAlignment(.center)
                Text("\(entry.group) · \(entry.region.title)")
                    .font(.subheadline)
                    .foregroundStyle(Theme.textSecondary)
                    .multilineTextAlignment(.center)
                Spacer().frame(height: 8)
                Text("Latince adı, tanımı ve temel bilgileri hatırla")
                    .font(.footnote)
                    .foregroundStyle(Theme.textTertiary)
            }
            .padding(24)
            .frame(maxWidth: .infinity, maxHeight: .infinity)
            .opacity(flipped ? 0 : 1)

            // Back
            ScrollView {
                VStack(alignment: .leading, spacing: 12) {
                    Text(entry.tr)
                        .font(.headline)
                        .foregroundStyle(Theme.textSecondary)
                    Text(entry.la)
                        .font(Theme.latin(.title2).weight(.semibold))
                        .foregroundStyle(tint)
                    Text(entry.summary)
                        .font(.subheadline)
                        .foregroundStyle(Theme.textPrimary)
                        .fixedSize(horizontal: false, vertical: true)
                    if !entry.facts.isEmpty {
                        FactTable(facts: Array(entry.facts.prefix(5)), tint: tint)
                    }
                    if let point = entry.tus.first {
                        HStack(alignment: .firstTextBaseline, spacing: 8) {
                            Image(systemName: "target")
                                .foregroundStyle(Theme.gold)
                            Text(point)
                                .font(.footnote)
                                .foregroundStyle(Theme.textPrimary)
                                .fixedSize(horizontal: false, vertical: true)
                        }
                        .padding(12)
                        .background(Theme.gold.opacity(0.1), in: .rect(cornerRadius: 12))
                    }
                }
                .padding(22)
            }
            .scrollIndicators(.hidden)
            .rotation3DEffect(.degrees(180), axis: (x: 0, y: 1, z: 0))
            .opacity(flipped ? 1 : 0)
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .background(Theme.card, in: .rect(cornerRadius: 28))
        .overlay {
            RoundedRectangle(cornerRadius: 28).strokeBorder(tint.opacity(0.35), lineWidth: 1.5)
        }
        .rotation3DEffect(.degrees(flipped ? 180 : 0), axis: (x: 0, y: 1, z: 0))
        .onTapGesture {
            withAnimation(.spring(duration: 0.45)) { flipped.toggle() }
        }
    }
}
