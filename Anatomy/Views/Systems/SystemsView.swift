//
//  SystemsView.swift
//  Anatomy
//

import SwiftUI

/// Explore the written atlas: the structure of the day, body systems and
/// body regions.
struct SystemsView: View {
    @Environment(AppModel.self) private var app

    private let columns = [GridItem(.flexible(), spacing: 12), GridItem(.flexible(), spacing: 12)]

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 28) {
                    if let entry = entryOfTheDay {
                        NavigationLink(value: entry) {
                            DailyCard(entry: entry, system: app.store.system(entry.systemID))
                        }
                        .buttonStyle(PressableStyle())
                    }

                    VStack(alignment: .leading, spacing: 14) {
                        SectionHeader(title: "Sistemler", subtitle: "\(app.store.entries.count) ayrıntılı madde, \(totalParts) üç boyutlu yapı")
                        LazyVGrid(columns: columns, spacing: 12) {
                            ForEach(app.store.systems) { system in
                                NavigationLink(value: system) {
                                    SystemCard(system: system, count: app.store.entries(in: system.id).count,
                                               locked: !Access.canOpen(systemID: system.id, premium: app.isPremium))
                                }
                                .buttonStyle(PressableStyle())
                            }
                        }
                    }

                    VStack(alignment: .leading, spacing: 14) {
                        SectionHeader(title: "Bölgelere göre")
                        LazyVGrid(columns: columns, spacing: 10) {
                            ForEach(BodyRegion.allCases) { region in
                                let count = app.store.entries.filter { $0.region == region }.count
                                if count > 0 {
                                    NavigationLink(value: region) {
                                        RegionTile(region: region, count: count)
                                    }
                                    .buttonStyle(PressableStyle())
                                }
                            }
                        }
                    }
                }
                .padding(.horizontal, 16)
                .padding(.bottom, 32)
            }
            .themedBackground()
            .navigationTitle("Keşfet")
            .navigationDestination(for: BodySystem.self) { SystemDetailView(system: $0) }
            .navigationDestination(for: BodyRegion.self) { RegionDetailView(region: $0) }
            .navigationDestination(for: AtlasEntry.self) { EntryDetailView(entry: $0) }
        }
    }

    private var totalParts: Int {
        app.scene.manifests.values.reduce(0) { $0 + $1.count }
    }

    /// A different structure every day, the same for the whole day; free
    /// users get one from the free system.
    private var entryOfTheDay: AtlasEntry? {
        let entries = app.isPremium ? app.store.entries : app.store.entries.filter(app.isFree)
        guard !entries.isEmpty else { return nil }
        let day = Calendar.current.ordinality(of: .day, in: .era, for: .now) ?? 0
        return entries[(day &* 7919) % entries.count]
    }
}

private struct DailyCard: View {
    let entry: AtlasEntry
    let system: BodySystem?

    var body: some View {
        let tint = system?.tint ?? Theme.accent
        ZStack(alignment: .bottomLeading) {
            Color.clear
                .frame(height: 200)
                .overlay {
                    if let id = system?.id, let image = UIImage(named: "card-\(id)") {
                        Image(uiImage: image).resizable().scaledToFill()
                    } else {
                        LinearGradient(colors: [tint.opacity(0.5), tint.opacity(0.1)], startPoint: .topLeading, endPoint: .bottomTrailing)
                    }
                }
                .overlay {
                    LinearGradient(colors: [.clear, .black.opacity(0.55), .black.opacity(0.92)], startPoint: .top, endPoint: .bottom)
                }
                .clipped()
            VStack(alignment: .leading, spacing: 5) {
                Eyebrow(text: "Günün yapısı", color: tint)
                Text(entry.tr)
                    .font(.title2.weight(.bold))
                    .foregroundStyle(.white)
                Text(entry.la)
                    .font(Theme.latin(.subheadline))
                    .foregroundStyle(.white.opacity(0.75))
                Text(entry.summary)
                    .font(.footnote)
                    .foregroundStyle(.white.opacity(0.75))
                    .lineLimit(2)
                    .multilineTextAlignment(.leading)
                    .padding(.top, 2)
            }
            .padding(18)
        }
        .clipShape(.rect(cornerRadius: 24))
        .overlay { RoundedRectangle(cornerRadius: 24).strokeBorder(Theme.stroke) }
    }
}

private struct SystemCard: View {
    let system: BodySystem
    let count: Int
    let locked: Bool

    var body: some View {
        // A render of the system's own 3D model (Assets: card-<id>).
        let image = UIImage(named: "card-\(system.id)")
        ZStack(alignment: .bottomLeading) {
            Color.clear
                .frame(height: 168)
                .overlay {
                    if let image {
                        Image(uiImage: image).resizable().scaledToFill()
                    } else {
                        LinearGradient(colors: [system.tint.opacity(0.35), system.tint.opacity(0.08)], startPoint: .topLeading, endPoint: .bottomTrailing)
                    }
                }
                .overlay {
                    LinearGradient(colors: [.clear, .black.opacity(0.4), .black.opacity(0.88)], startPoint: .top, endPoint: .bottom)
                }
                .clipped()
            VStack(alignment: .leading, spacing: 3) {
                Text(system.tr)
                    .font(.headline)
                    .foregroundStyle(.white)
                    .lineLimit(2)
                    .multilineTextAlignment(.leading)
                Text("\(count) madde")
                    .font(.caption)
                    .foregroundStyle(.white.opacity(0.7))
            }
            .padding(12)
        }
        .overlay(alignment: .topLeading) {
            SystemBadge(icon: system.icon, color: system.tint, size: 32)
                .padding(10)
        }
        .overlay(alignment: .topTrailing) {
            if locked { LockBadge().padding(10) }
        }
        .clipShape(.rect(cornerRadius: 20))
        .overlay { RoundedRectangle(cornerRadius: 20).strokeBorder(Theme.stroke) }
    }
}

private struct RegionTile: View {
    let region: BodyRegion
    let count: Int

    var body: some View {
        HStack(spacing: 12) {
            Image(systemName: region.icon)
                .font(.title3)
                .foregroundStyle(Theme.accent)
                .frame(width: 30)
            VStack(alignment: .leading, spacing: 2) {
                Text(region.title)
                    .font(.subheadline.weight(.semibold))
                    .foregroundStyle(Theme.textPrimary)
                    .lineLimit(1)
                    .minimumScaleFactor(0.85)
                Text("\(count) yapı")
                    .font(.caption)
                    .foregroundStyle(Theme.textSecondary)
            }
            Spacer(minLength: 0)
        }
        .padding(14)
        .background(Theme.card, in: .rect(cornerRadius: 16))
        .overlay { RoundedRectangle(cornerRadius: 16).strokeBorder(Theme.stroke) }
    }
}

/// Entries grouped under small headings, on cards.
private struct EntryGroupCard: View {
    let title: String
    let tint: Color
    let entries: [AtlasEntry]
    let locked: Bool

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            Eyebrow(text: title, color: tint)
                .padding(.horizontal, 4)
            VStack(spacing: 0) {
                ForEach(Array(entries.enumerated()), id: \.element.id) { index, entry in
                    NavigationLink(value: entry) {
                        EntryRow(entry: entry, tint: tint, locked: locked)
                            .padding(.horizontal, 14)
                            .padding(.vertical, 11)
                            .contentShape(.rect)
                    }
                    .buttonStyle(.plain)
                    if index < entries.count - 1 {
                        Divider().overlay(Theme.stroke).padding(.leading, 14)
                    }
                }
            }
            .background(Theme.card, in: .rect(cornerRadius: 18))
            .overlay { RoundedRectangle(cornerRadius: 18).strokeBorder(Theme.stroke) }
        }
    }
}

struct SystemDetailView: View {
    @Environment(AppModel.self) private var app
    let system: BodySystem

    var body: some View {
        let locked = !Access.canOpen(systemID: system.id, premium: app.isPremium)
        ScrollView {
            VStack(alignment: .leading, spacing: 20) {
                header(locked: locked)
                ForEach(app.store.groups(in: system), id: \.title) { group in
                    EntryGroupCard(title: group.title, tint: system.tint, entries: group.entries, locked: locked)
                }
            }
            .padding(.horizontal, 16)
            .padding(.bottom, 32)
        }
        .themedBackground()
        .navigationTitle(system.tr)
        .navigationBarTitleDisplayMode(.inline)
    }

    private func header(locked: Bool) -> some View {
        VStack(alignment: .leading, spacing: 14) {
            HStack(spacing: 14) {
                SystemBadge(icon: system.icon, color: system.tint, size: 56)
                VStack(alignment: .leading, spacing: 2) {
                    Text(system.tr).font(.title2.weight(.bold)).foregroundStyle(Theme.textPrimary)
                    Text(system.la).font(Theme.latin(.subheadline)).foregroundStyle(system.tint)
                }
            }
            Text(system.intro)
                .font(.subheadline)
                .foregroundStyle(Theme.textSecondary)
                .fixedSize(horizontal: false, vertical: true)
            if locked {
                Button {
                    app.requirePremium(.system(system.tr))
                } label: {
                    Label("Bu sistemi Premium ile aç", systemImage: "lock.open.fill")
                }
                .buttonStyle(PrimaryButtonStyle(gradient: Theme.goldGradient, foreground: Color(hex: "2A1D05")))
            } else if let layer = system.layer, ModelLayer.layer(layer) != nil {
                Button {
                    showLayer(layer)
                } label: {
                    Label("Sistemi 3D'de göster", systemImage: "cube.transparent")
                }
                .buttonStyle(PrimaryButtonStyle())
            }
            let ids = app.store.entries(in: system.id).map(\.id)
            let mastery = app.study.mastery(of: ids)
            if mastery > 0 {
                HStack {
                    ProgressRing(value: mastery, color: system.tint, lineWidth: 4)
                        .frame(width: 22, height: 22)
                    Text("Ustalık %\(Int(mastery * 100))")
                        .font(.caption.weight(.medium))
                        .foregroundStyle(Theme.textSecondary)
                }
            }
        }
        .padding(.top, 8)
    }

    private func showLayer(_ layer: String) {
        let scene = app.scene
        for other in ModelLayer.all {
            let on = other.id == layer || (other.id == "skeletal" && layer != "skeletal" && layer != "regions")
            scene.setLayer(other.id, ghosted: other.id == "skeletal" && layer != "skeletal" && layer != "joints" && layer != "insertions")
            scene.setLayer(other.id, enabled: on)
        }
        scene.showAll()
        scene.highlight([])
        scene.select(nil)
        scene.resetCamera()
        app.tab = .atlas
    }
}

struct RegionDetailView: View {
    @Environment(AppModel.self) private var app
    let region: BodyRegion

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 20) {
                ForEach(app.store.systems) { system in
                    let items = app.store.entries(in: system.id).filter { $0.region == region }
                    if !items.isEmpty {
                        EntryGroupCard(title: system.tr, tint: system.tint, entries: items,
                                       locked: !Access.canOpen(systemID: system.id, premium: app.isPremium))
                    }
                }
            }
            .padding(.horizontal, 16)
            .padding(.vertical, 12)
        }
        .themedBackground()
        .navigationTitle(region.title)
    }
}

struct EntryRow: View {
    @Environment(AppModel.self) private var app
    let entry: AtlasEntry
    var tint: Color = Theme.accent
    var locked = false
    /// Lists draw their own disclosure indicator.
    var chevron = true

    var body: some View {
        HStack(spacing: 12) {
            VStack(alignment: .leading, spacing: 2) {
                Text(entry.tr)
                    .font(.body.weight(.medium))
                    .foregroundStyle(Theme.textPrimary)
                Text(entry.la)
                    .font(Theme.latin(.subheadline))
                    .foregroundStyle(Theme.textSecondary)
            }
            Spacer()
            if locked {
                Image(systemName: "lock.fill")
                    .font(.caption)
                    .foregroundStyle(Theme.gold)
            } else {
                if app.study.isFavorite(entry.id) {
                    Image(systemName: "star.fill")
                        .font(.caption)
                        .foregroundStyle(Theme.gold)
                }
                let mastery = app.study.score(entry.id).mastery
                if mastery > 0 {
                    ProgressRing(value: mastery, color: tint, lineWidth: 3)
                        .frame(width: 16, height: 16)
                }
            }
            if chevron {
                Image(systemName: "chevron.right")
                    .font(.caption.weight(.semibold))
                    .foregroundStyle(Theme.textTertiary)
            }
        }
    }
}
