//
//  FlashcardsView.swift
//  Anatomy
//

import SwiftUI

/// A shuffled deck of entries, least known first.
@MainActor
@Observable
final class FlashcardDeck: Identifiable {
    let id = UUID()
    let cards: [AtlasEntry]
    var index = 0
    var known = 0

    init(entries: [AtlasEntry], study: StudyStore, limit: Int = 20) {
        cards = Array(entries.shuffled().sorted { study.score($0.id).mastery < study.score($1.id).mastery }.prefix(limit))
    }

    var current: AtlasEntry? { cards.indices.contains(index) ? cards[index] : nil }
}

struct FlashcardsView: View {
    @Environment(AppModel.self) private var app
    @Environment(\.dismiss) private var dismiss
    @State var deck: FlashcardDeck
    @State private var flipped = false

    var body: some View {
        NavigationStack {
            VStack(spacing: 20) {
                if let entry = deck.current {
                    Text("\(deck.index + 1) / \(deck.cards.count)")
                        .font(.footnote.weight(.semibold))
                        .foregroundStyle(.secondary)
                    card(entry)
                        .id(entry.id)
                        .transition(.asymmetric(insertion: .move(edge: .trailing).combined(with: .opacity), removal: .move(edge: .leading).combined(with: .opacity)))
                    HStack(spacing: 12) {
                        Button {
                            answer(entry, known: false)
                        } label: {
                            Label("Tekrar et", systemImage: "arrow.counterclockwise")
                                .frame(maxWidth: .infinity)
                        }
                        .buttonStyle(.glass)
                        .tint(.orange)
                        Button {
                            answer(entry, known: true)
                        } label: {
                            Label("Biliyorum", systemImage: "checkmark")
                                .frame(maxWidth: .infinity)
                        }
                        .buttonStyle(.glassProminent)
                        .tint(.green)
                    }
                    .controlSize(.large)
                } else {
                    Spacer()
                    Image(systemName: "checkmark.seal.fill")
                        .font(.system(size: 64))
                        .foregroundStyle(.green)
                    Text("Deste bitti!")
                        .font(.title.weight(.bold))
                    Text("\(deck.cards.count) karttan \(deck.known) tanesini bildin.")
                        .foregroundStyle(.secondary)
                    Spacer()
                    Button("Kapat") { dismiss() }
                        .buttonStyle(.glassProminent)
                        .controlSize(.large)
                }
            }
            .padding(16)
            .animation(.snappy, value: deck.index)
            .atlasBackground()
            .navigationTitle("Bilgi kartları")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Kapat") { dismiss() }
                }
            }
        }
    }

    private func card(_ entry: AtlasEntry) -> some View {
        let system = app.store.system(entry.systemID)
        let tint = system?.tint ?? .accentColor
        return ZStack {
            // Front
            VStack(spacing: 16) {
                if let system {
                    SystemBadge(icon: system.icon, color: tint, size: 56)
                }
                Text(entry.tr)
                    .font(.largeTitle.weight(.bold))
                    .multilineTextAlignment(.center)
                Text(entry.region.title)
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
                Spacer().frame(height: 12)
                Label("Çevirmek için dokun", systemImage: "hand.tap")
                    .font(.footnote)
                    .foregroundStyle(.tertiary)
            }
            .padding(24)
            .frame(maxWidth: .infinity, maxHeight: .infinity)
            .opacity(flipped ? 0 : 1)

            // Back
            ScrollView {
                VStack(alignment: .leading, spacing: 12) {
                    Text(entry.la)
                        .font(.title2.weight(.bold).italic())
                        .foregroundStyle(tint)
                    Text(entry.en)
                        .font(.subheadline)
                        .foregroundStyle(.secondary)
                    Text(entry.summary)
                        .font(.body)
                    if !entry.facts.isEmpty {
                        FactTable(facts: Array(entry.facts.prefix(4)), tint: tint)
                    }
                }
                .padding(24)
            }
            .rotation3DEffect(.degrees(180), axis: (x: 0, y: 1, z: 0))
            .opacity(flipped ? 1 : 0)
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .background(Color(.secondarySystemGroupedBackground), in: .rect(cornerRadius: 28))
        .overlay {
            RoundedRectangle(cornerRadius: 28).strokeBorder(tint.opacity(0.35), lineWidth: 1.5)
        }
        .rotation3DEffect(.degrees(flipped ? 180 : 0), axis: (x: 0, y: 1, z: 0))
        .onTapGesture {
            withAnimation(.spring(duration: 0.45)) { flipped.toggle() }
        }
    }

    private func answer(_ entry: AtlasEntry, known: Bool) {
        app.study.record(entry.id, correct: known)
        if known { deck.known += 1 }
        flipped = false
        deck.index += 1
    }
}
