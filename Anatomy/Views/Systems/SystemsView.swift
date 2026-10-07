//
//  SystemsView.swift
//  Anatomy
//

import SwiftUI

/// Browse the written atlas by body system or by region.
struct SystemsView: View {
    @Environment(AppModel.self) private var app

    private let columns = [GridItem(.adaptive(minimum: 160), spacing: 12)]

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 24) {
                    LazyVGrid(columns: columns, spacing: 12) {
                        ForEach(app.store.systems) { system in
                            NavigationLink(value: system) {
                                SystemCard(system: system, count: app.store.entries(in: system.id).count)
                            }
                            .buttonStyle(.plain)
                        }
                    }

                    VStack(alignment: .leading, spacing: 12) {
                        Text("Bölgelere göre")
                            .font(.title2.weight(.bold))
                        LazyVGrid(columns: columns, spacing: 12) {
                            ForEach(BodyRegion.allCases) { region in
                                let count = app.store.entries.filter { $0.region == region }.count
                                if count > 0 {
                                    NavigationLink(value: region) {
                                        HStack(spacing: 12) {
                                            Image(systemName: region.icon)
                                                .font(.title3)
                                                .foregroundStyle(.tint)
                                                .frame(width: 32)
                                            VStack(alignment: .leading, spacing: 2) {
                                                Text(region.title)
                                                    .font(.subheadline.weight(.semibold))
                                                    .foregroundStyle(.primary)
                                                Text("\(count) yapı")
                                                    .font(.caption)
                                                    .foregroundStyle(.secondary)
                                            }
                                            Spacer(minLength: 0)
                                        }
                                        .padding(14)
                                        .background(Color(.secondarySystemGroupedBackground), in: .rect(cornerRadius: 16))
                                    }
                                    .buttonStyle(.plain)
                                }
                            }
                        }
                    }
                }
                .padding(16)
            }
            .atlasBackground()
            .navigationTitle("Sistemler")
            .navigationDestination(for: BodySystem.self) { SystemDetailView(system: $0) }
            .navigationDestination(for: BodyRegion.self) { RegionDetailView(region: $0) }
            .navigationDestination(for: AtlasEntry.self) { EntryDetailView(entry: $0) }
        }
    }
}

private struct SystemCard: View {
    let system: BodySystem
    let count: Int

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            SystemBadge(icon: system.icon, color: system.tint, size: 44)
            Spacer(minLength: 0)
            Text(system.tr)
                .font(.headline)
                .foregroundStyle(.primary)
                .lineLimit(2)
                .multilineTextAlignment(.leading)
            Text("\(count) yapı")
                .font(.caption)
                .foregroundStyle(.secondary)
        }
        .frame(maxWidth: .infinity, minHeight: 112, alignment: .leading)
        .padding(14)
        .background(
            LinearGradient(colors: [system.tint.opacity(0.18), system.tint.opacity(0.05)], startPoint: .topLeading, endPoint: .bottomTrailing),
            in: .rect(cornerRadius: 20)
        )
        .background(Color(.secondarySystemGroupedBackground), in: .rect(cornerRadius: 20))
    }
}

struct SystemDetailView: View {
    @Environment(AppModel.self) private var app
    let system: BodySystem

    var body: some View {
        List {
            Section {
                VStack(alignment: .leading, spacing: 12) {
                    HStack(spacing: 14) {
                        SystemBadge(icon: system.icon, color: system.tint, size: 56)
                        VStack(alignment: .leading, spacing: 2) {
                            Text(system.tr).font(.title2.weight(.bold))
                            Text(system.la).font(.subheadline.italic()).foregroundStyle(system.tint)
                        }
                    }
                    Text(system.intro)
                        .font(.subheadline)
                        .fixedSize(horizontal: false, vertical: true)
                    if let layer = system.layer, ModelLayer.layer(layer) != nil {
                        Button {
                            showLayer(layer)
                        } label: {
                            Label("Sistemi 3D'de göster", systemImage: "cube.transparent")
                                .frame(maxWidth: .infinity)
                        }
                        .buttonStyle(.glassProminent)
                        .controlSize(.large)
                    }
                    let ids = app.store.entries(in: system.id).map(\.id)
                    let mastery = app.study.mastery(of: ids)
                    if mastery > 0 {
                        HStack {
                            ProgressRing(value: mastery, color: system.tint, lineWidth: 4)
                                .frame(width: 22, height: 22)
                            Text("Ustalık %\(Int(mastery * 100))")
                                .font(.caption.weight(.medium))
                                .foregroundStyle(.secondary)
                        }
                    }
                }
                .padding(.vertical, 6)
            }

            ForEach(app.store.groups(in: system), id: \.title) { group in
                Section(group.title) {
                    ForEach(group.entries) { entry in
                        NavigationLink(value: entry) {
                            EntryRow(entry: entry, tint: system.tint)
                        }
                    }
                }
            }
        }
        .navigationTitle(system.tr)
        .navigationBarTitleDisplayMode(.inline)
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
        List {
            ForEach(app.store.systems) { system in
                let items = app.store.entries(in: system.id).filter { $0.region == region }
                if !items.isEmpty {
                    Section(system.tr) {
                        ForEach(items) { entry in
                            NavigationLink(value: entry) {
                                EntryRow(entry: entry, tint: system.tint)
                            }
                        }
                    }
                }
            }
        }
        .navigationTitle(region.title)
    }
}

struct EntryRow: View {
    @Environment(AppModel.self) private var app
    let entry: AtlasEntry
    var tint: Color = .accentColor

    var body: some View {
        HStack(spacing: 12) {
            VStack(alignment: .leading, spacing: 2) {
                Text(entry.tr)
                    .font(.body.weight(.medium))
                Text(entry.la)
                    .font(.subheadline.italic())
                    .foregroundStyle(.secondary)
            }
            Spacer()
            if app.study.isFavorite(entry.id) {
                Image(systemName: "star.fill")
                    .font(.caption)
                    .foregroundStyle(.yellow)
            }
            let mastery = app.study.score(entry.id).mastery
            if mastery > 0 {
                ProgressRing(value: mastery, color: tint, lineWidth: 3)
                    .frame(width: 16, height: 16)
            }
        }
    }
}
