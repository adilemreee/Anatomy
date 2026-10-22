//
//  FlashcardsView.swift
//  Anatomy
//

import SwiftUI

struct FlashcardsView: View {
    @Environment(AppModel.self) private var app
    @Environment(\.dismiss) private var dismiss
    let deck: FlashcardDeck
    @State private var flipped = false

    var body: some View {
        NavigationStack {
            VStack(spacing: 18) {
                if let card = deck.current {
                    ProgressBar(value: Double(deck.index) / Double(max(deck.cards.count, 1)))
                        .frame(height: 4)
                    cardView(card)
                        .id("\(deck.index)-\(card.id)")
                        .transition(.asymmetric(insertion: .move(edge: .trailing).combined(with: .opacity),
                                                removal: .move(edge: .leading).combined(with: .opacity)))
                    if flipped {
                        gradeButtons(card)
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
            .navigationTitle(deck.current == nil ? deck.title : String(localized: "Kart \(min(deck.index + 1, deck.cards.count))/\(deck.cards.count)"))
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

    private func gradeButtons(_ card: Flashcard) -> some View {
        HStack(spacing: 8) {
            // "Tekrar" alone is the Review section title; the grade means "again".
            gradeButton(LocalizedStringResource("flashcard.again", defaultValue: "Tekrar"), .again, Theme.danger, card)
            gradeButton("Zor", .hard, .orange, card)
            gradeButton("İyi", .good, Theme.success, card)
            gradeButton("Kolay", .easy, Theme.accent, card)
        }
    }

    private func gradeButton(_ title: LocalizedStringResource, _ grade: StudyStore.CardGrade, _ color: Color, _ card: Flashcard) -> some View {
        Button {
            flipped = false
            deck.grade(grade, study: app.study)
        } label: {
            VStack(spacing: 3) {
                Text(title)
                    .font(.subheadline.weight(.bold))
                    .lineLimit(1)
                    .minimumScaleFactor(0.75)
                Text(app.study.nextInterval(card: card.id, grade))
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

    private func cardView(_ card: Flashcard) -> some View {
        let entry = app.store.entry(card.entryID)
        let tint = Color(hex: card.kind.tint)
        return ZStack {
            front(card, tint: tint)
                .padding(24)
                .frame(maxWidth: .infinity, maxHeight: .infinity)
                .opacity(flipped ? 0 : 1)

            ScrollView {
                Group {
                    if card.kind == .overview, let entry {
                        overviewBack(entry, tint: app.store.system(entry.systemID)?.tint ?? tint)
                    } else {
                        back(card, tint: tint)
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

    private func front(_ card: Flashcard, tint: Color) -> some View {
        let long = card.prompt.count > 60
        return VStack(spacing: 16) {
            Label(card.kind.title, systemImage: card.kind.icon)
                .font(.caption.weight(.bold))
                .foregroundStyle(tint)
            if !card.eyebrow.isEmpty {
                Text(card.eyebrow)
                    .font(.subheadline)
                    .foregroundStyle(Theme.textSecondary)
                    .multilineTextAlignment(.center)
                    .lineLimit(2)
            }
            Text(card.prompt)
                .font(long ? .title3.weight(.semibold) : .largeTitle.weight(.bold))
                .foregroundStyle(Theme.textPrimary)
                .multilineTextAlignment(.center)
                .minimumScaleFactor(0.6)
            Text(card.ask)
                .font(.subheadline.weight(.semibold))
                .foregroundStyle(tint)
                .padding(.horizontal, 14)
                .padding(.vertical, 7)
                .background(tint.opacity(0.14), in: .capsule)
                .multilineTextAlignment(.center)
        }
    }

    private func back(_ card: Flashcard, tint: Color) -> some View {
        VStack(alignment: .leading, spacing: 12) {
            Text([.tus, .clinical, .facts].contains(card.kind) ? card.ask : "\(card.prompt) · \(card.ask)")
                .font(.subheadline.weight(.semibold))
                .foregroundStyle(Theme.textSecondary)
                .fixedSize(horizontal: false, vertical: true)
            Text(card.answer)
                .font(card.answer.count > 80 ? .title3.weight(.semibold) : .title2.weight(.bold))
                .foregroundStyle(tint)
                .fixedSize(horizontal: false, vertical: true)
            if let detail = card.answerDetail {
                Text(detail)
                    .font(.subheadline)
                    .foregroundStyle(Theme.textPrimary)
                    .fixedSize(horizontal: false, vertical: true)
                    .padding(12)
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .background(tint.opacity(0.08), in: .rect(cornerRadius: 12))
            }
            if card.kind == .facts, let entry = app.store.entry(card.entryID) {
                Text(app.store.fullName(entry))
                    .font(.footnote)
                    .foregroundStyle(Theme.textTertiary)
            }
        }
        .frame(maxWidth: .infinity, alignment: .leading)
    }

    private func overviewBack(_ entry: AtlasEntry, tint: Color) -> some View {
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
    }
}
