//
//  FlashcardSetupView.swift
//  Anatomy
//

import SwiftUI

/// Chooses a flashcard deck: every kind together or one kind, for all
/// systems, one system or one of its headings.
struct FlashcardSetupView: View {
    @Environment(AppModel.self) private var app
    @AppStorage("cards.system") private var systemID = ""
    @State private var group: String?

    private var system: BodySystem? { systemID.isEmpty ? nil : app.store.system(systemID) }

    private var scope: Set<String> {
        system.map { [$0.id] } ?? Set(app.store.systems.map(\.id))
    }

    var body: some View {
        let library = app.flashcardLibrary
        let open = scope.intersection(app.openSystems)
        let all = library.cards(kinds: Set(Flashcard.Kind.allCases), systems: open, group: group)
        ScrollView {
            VStack(alignment: .leading, spacing: 24) {
                mixedCard(cards: all)
                scopePicker
                VStack(alignment: .leading, spacing: 12) {
                    SectionHeader(title: String(localized: "Desteler"), subtitle: String(localized: "Her kart kendi tekrar takvimiyle ilerler"))
                    VStack(spacing: 0) {
                        let kinds = Flashcard.Kind.allCases.filter { kind in all.contains { $0.kind == kind } }
                        ForEach(Array(kinds.enumerated()), id: \.element) { i, kind in
                            DeckRow(kind: kind, cards: all.filter { $0.kind == kind }) {
                                start(kinds: [kind], title: kind.title)
                            }
                            if i < kinds.count - 1 {
                                Divider().overlay(Theme.stroke).padding(.leading, 62)
                            }
                        }
                    }
                    .background(Theme.card, in: .rect(cornerRadius: 20))
                    .overlay { RoundedRectangle(cornerRadius: 20).strokeBorder(Theme.stroke) }
                }
                if !app.isPremium {
                    Button {
                        app.requirePremium(.flashcards)
                    } label: {
                        HStack(spacing: 8) {
                            PremiumBadge(compact: true)
                            Text("Eklem ve kas kartları Premium'da")
                                .font(.footnote.weight(.semibold))
                                .foregroundStyle(Theme.gold)
                        }
                    }
                    .buttonStyle(.plain)
                }
            }
            .padding(16)
            .padding(.bottom, 24)
        }
        .themedBackground()
        .navigationTitle("Bilgi kartları")
        .navigationBarTitleDisplayMode(.inline)
    }

    private func start(kinds: Set<Flashcard.Kind>, title: String) {
        let name = [system?.tr, group].compactMap(\.self).joined(separator: " · ")
        app.startFlashcards(kinds: kinds, systems: scope, group: group, title: name.isEmpty ? title : "\(title) · \(name)")
    }

    private func mixedCard(cards: [Flashcard]) -> some View {
        let due = cards.count { app.study.isDue($0.id) }
        let new = cards.count { app.study.card($0.id) == nil }
        return VStack(alignment: .leading, spacing: 14) {
            Eyebrow(text: String(localized: "Aralıklı tekrar"), color: .white.opacity(0.75))
            VStack(alignment: .leading, spacing: 6) {
                Text(due > 0 ? String(localized: "\(due) kart seni bekliyor") : (new > 0 ? String(localized: "Yeni kartlarla başla") : String(localized: "Bugünkü tekrarların tamam")))
                    .font(.title2.weight(.bold))
                    .foregroundStyle(.white)
                Text("\(cards.count) kart · \(new) yeni. Hatırlayamadığın kartlar daha sık, bildiklerin daha seyrek gelir.")
                    .font(.subheadline)
                    .foregroundStyle(.white.opacity(0.85))
                    .fixedSize(horizontal: false, vertical: true)
            }
            Button {
                start(kinds: Set(Flashcard.Kind.allCases), title: String(localized: "Karışık tekrar"))
            } label: {
                Label("Karışık tekrar", systemImage: "play.fill")
            }
            .buttonStyle(PrimaryButtonStyle(gradient: LinearGradient(colors: [.white, .white], startPoint: .top, endPoint: .bottom),
                                            foreground: Color(hex: "4A2A99")))
        }
        .padding(20)
        .background {
            ZStack(alignment: .topTrailing) {
                LinearGradient(colors: [Color(hex: "8B5CF6"), Color(hex: "4F46E5")], startPoint: .topLeading, endPoint: .bottomTrailing)
                Image(systemName: "rectangle.on.rectangle.angled")
                    .font(.system(size: 130, weight: .thin))
                    .foregroundStyle(.white.opacity(0.08))
                    .offset(x: 24, y: -6)
            }
        }
        .clipShape(.rect(cornerRadius: 26))
    }

    private var scopePicker: some View {
        VStack(alignment: .leading, spacing: 10) {
            ScrollView(.horizontal) {
                HStack(spacing: 8) {
                    chip(String(localized: "Tümü"), icon: "square.grid.2x2", selected: system == nil, locked: false) {
                        systemID = ""
                        group = nil
                    }
                    ForEach(app.store.systems) { item in
                        let locked = !Access.canOpen(systemID: item.id, premium: app.isPremium)
                        chip(item.tr, icon: item.icon, selected: system?.id == item.id, locked: locked) {
                            if locked {
                                app.requirePremium(.system(item.tr))
                            } else {
                                systemID = item.id
                                group = nil
                            }
                        }
                    }
                }
                .padding(.horizontal, 16)
            }
            .scrollIndicators(.hidden)
            .padding(.horizontal, -16)
            if let system {
                Menu {
                    Button {
                        group = nil
                    } label: {
                        Label("Tüm konular", systemImage: group == nil ? "checkmark" : "list.bullet")
                    }
                    Divider()
                    ForEach(system.groups, id: \.self) { item in
                        Button {
                            group = item
                        } label: {
                            if group == item { Label(item, systemImage: "checkmark") } else { Text(item) }
                        }
                    }
                } label: {
                    HStack(spacing: 6) {
                        Image(systemName: "line.3.horizontal.decrease.circle")
                        Text(group ?? String(localized: "Tüm konular"))
                            .lineLimit(1)
                        Image(systemName: "chevron.down")
                            .font(.caption2.weight(.bold))
                    }
                    .font(.subheadline.weight(.semibold))
                    .foregroundStyle(Theme.textPrimary)
                    .padding(.horizontal, 14)
                    .padding(.vertical, 9)
                    .background(Theme.card, in: .capsule)
                    .overlay { Capsule().strokeBorder(Theme.stroke) }
                }
            }
        }
    }

    private func chip(_ title: String, icon: String, selected: Bool, locked: Bool, action: @escaping () -> Void) -> some View {
        Button(action: action) {
            HStack(spacing: 6) {
                Image(systemName: locked ? "lock.fill" : icon)
                    .font(.caption)
                Text(title)
                    .font(.subheadline.weight(.semibold))
            }
            .foregroundStyle(selected ? .white : Theme.textPrimary)
            .padding(.horizontal, 14)
            .padding(.vertical, 9)
            .background(selected ? AnyShapeStyle(Theme.accent) : AnyShapeStyle(Theme.card), in: .capsule)
            .overlay { Capsule().strokeBorder(selected ? .clear : Theme.stroke) }
        }
        .buttonStyle(PressableStyle())
    }
}

private struct DeckRow: View {
    @Environment(AppModel.self) private var app
    let kind: Flashcard.Kind
    let cards: [Flashcard]
    let action: () -> Void

    var body: some View {
        let tint = Color(hex: kind.tint)
        let due = cards.count { app.study.isDue($0.id) }
        let learned = cards.count { (app.study.card($0.id)?.box ?? 0) >= 3 }
        Button(action: action) {
            HStack(spacing: 14) {
                SystemBadge(icon: kind.icon, color: tint, size: 40)
                VStack(alignment: .leading, spacing: 5) {
                    Text(kind.title)
                        .font(.headline)
                        .foregroundStyle(Theme.textPrimary)
                    Text(kind.subtitle)
                        .font(.caption)
                        .foregroundStyle(Theme.textSecondary)
                        .lineLimit(1)
                    HStack(spacing: 8) {
                        ProgressBar(value: cards.isEmpty ? 0 : Double(learned) / Double(cards.count), color: tint)
                            .frame(height: 4)
                        Text("\(learned)/\(cards.count)")
                            .font(.caption2.monospacedDigit())
                            .foregroundStyle(Theme.textTertiary)
                    }
                }
                if due > 0 {
                    CountPill(count: due, color: tint)
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
