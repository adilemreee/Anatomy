//
//  SearchView.swift
//  Anatomy
//

import SwiftUI

/// Searches the written entries and every 3D part (Turkish, Latin, English).
struct SearchView: View {
    @Environment(AppModel.self) private var app
    @State private var query = ""
    @State private var parts: [PartRef] = []

    var body: some View {
        NavigationStack {
            List {
                if query.isEmpty {
                    suggestions
                } else {
                    let entries = app.store.search(query)
                    if entries.isEmpty && parts.isEmpty {
                        ContentUnavailableView.search(text: query)
                    }
                    if !entries.isEmpty {
                        Section("Atlas maddeleri") {
                            ForEach(entries) { entry in
                                NavigationLink(value: entry) {
                                    EntryRow(entry: entry, tint: app.store.system(entry.systemID)?.tint ?? Theme.accent, locked: !app.isFree(entry), chevron: false)
                                }
                            }
                        }
                        .listRowBackground(Theme.card)
                    }
                    if !parts.isEmpty {
                        Section("3D model parçaları") {
                            ForEach(parts) { ref in
                                PartResultRow(ref: ref)
                            }
                        }
                        .listRowBackground(Theme.card)
                    }
                }
            }
            .scrollContentBackground(.hidden)
            .themedBackground()
            .navigationTitle("Ara")
            .searchable(text: $query, prompt: "Kemik, kas, eklem, bağ…")
            .navigationDestination(for: AtlasEntry.self) { EntryDetailView(entry: $0) }
            .task(id: query) {
                try? await Task.sleep(for: .milliseconds(180))
                guard !Task.isCancelled else { return }
                parts = searchParts(query)
            }
        }
    }

    @ViewBuilder
    private var suggestions: some View {
        let recents = app.study.recents.compactMap(app.store.entry)
        if !recents.isEmpty {
            Section("Son bakılanlar") {
                ForEach(recents.prefix(8)) { entry in
                    NavigationLink(value: entry) {
                        EntryRow(entry: entry, tint: app.store.system(entry.systemID)?.tint ?? Theme.accent, locked: !app.isFree(entry), chevron: false)
                    }
                }
            }
            .listRowBackground(Theme.card)
        }
        Section("Örnek aramalar") {
            ForEach(["Femur", "Deltoid", "Biceps", String(localized: "Diz eklemi"), "Scapula", String(localized: "Menisküs"), "Psoas", "Atlas"], id: \.self) { sample in
                Button {
                    query = sample
                } label: {
                    Label(sample, systemImage: "magnifyingglass")
                }
            }
        }
        .listRowBackground(Theme.card)
    }

    private func searchParts(_ text: String) -> [PartRef] {
        let q = SearchText.fold(text)
        guard q.count >= 2 else { return [] }
        let store = app.store
        var seen = Set<String>()
        var out: [PartRef] = []
        for layer in ModelLayer.all {
            for (i, part) in (app.scene.manifests[layer.id] ?? []).enumerated() {
                let latin = store.latinName(for: part) ?? ""
                let turkish = store.displayName(for: part)
                guard SearchText.fold(part.base).contains(q) || SearchText.fold(latin).contains(q) || SearchText.fold(turkish).contains(q) else { continue }
                // One row per structure; left/right share a row.
                guard seen.insert(layer.id + part.base).inserted else { continue }
                out.append(PartRef(system: layer.id, index: i))
                if out.count >= 80 { return out }
            }
        }
        return out
    }
}

private struct PartResultRow: View {
    @Environment(AppModel.self) private var app
    let ref: PartRef

    var body: some View {
        if let info = app.scene.info(ref) {
            let layer = ModelLayer.layer(ref.system)
            Button {
                let refs = app.scene.manifests[ref.system]?.indices
                    .filter { app.scene.manifests[ref.system]?[$0].base == info.base }
                    .map { PartRef(system: ref.system, index: $0) } ?? [ref]
                app.showInAtlas(refs)
            } label: {
                HStack(spacing: 12) {
                    if let layer {
                        SystemBadge(icon: layer.icon, color: layer.tint, size: 30)
                    }
                    VStack(alignment: .leading, spacing: 2) {
                        Text(app.store.displayName(for: info))
                            .foregroundStyle(.primary)
                        Text(app.store.latinName(for: info) ?? info.base)
                            .font(.caption.italic())
                            .foregroundStyle(.secondary)
                    }
                    Spacer()
                    Image(systemName: "cube.transparent")
                        .foregroundStyle(.tint)
                }
            }
        }
    }
}
