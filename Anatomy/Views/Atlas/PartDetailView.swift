//
//  PartDetailView.swift
//  Anatomy
//

import SwiftUI

/// Information about one tapped 3D part.
struct PartDetailView: View {
    @Environment(AppModel.self) private var app
    @Environment(\.dismiss) private var dismiss
    let ref: PartRef

    var body: some View {
        let store = app.store
        if let info = app.scene.info(ref) {
            let entry = store.entry(for: info)
            let exact = entry.map { store.isExact($0, for: info) } ?? false
            let layer = ModelLayer.layer(ref.system)
            ScrollView {
                VStack(alignment: .leading, spacing: 16) {
                    if let entry, exact {
                        EntryContent(entry: entry, showsModelButton: false)
                        partCard(info: info, layer: layer)
                    } else {
                        header(info: info, layer: layer)
                        if let entry {
                            NavigationLink(value: entry) {
                                ContentCard(title: String(localized: "Bağlı olduğu yapı"), systemImage: "arrow.turn.up.right", tint: layer?.tint ?? .accentColor) {
                                    HStack {
                                        VStack(alignment: .leading, spacing: 2) {
                                            Text(entry.tr).font(.title3.weight(.semibold))
                                            Text(entry.la).font(.subheadline.italic()).foregroundStyle(.secondary)
                                            Text(entry.summary)
                                                .font(.subheadline)
                                                .foregroundStyle(.secondary)
                                                .lineLimit(3)
                                                .padding(.top, 4)
                                        }
                                        Spacer()
                                        Image(systemName: "chevron.right").foregroundStyle(.tertiary)
                                    }
                                }
                            }
                            .buttonStyle(.plain)
                        }
                        partCard(info: info, layer: layer)
                        if let def = store.term(info.base)?.def {
                            ReferenceTextCard(text: def)
                        }
                    }
                }
                .padding(.horizontal, 16)
                .padding(.bottom, 32)
            }
            .themedBackground()
            .navigationTitle(store.displayName(for: info))
            .navigationBarTitleDisplayMode(.inline)
            .navigationDestination(for: AtlasEntry.self) { EntryDetailView(entry: $0) }
            .toolbar {
                ToolbarItem(placement: .confirmationAction) {
                    Button("Kapat") { dismiss() }
                }
                if let entry {
                    ToolbarItem(placement: .topBarLeading) {
                        FavoriteButton(id: entry.id)
                    }
                }
            }
            .onAppear {
                if let entry { app.study.markViewed(entry.id) }
            }
        }
    }

    private func header(info: PartInfo, layer: ModelLayer?) -> some View {
        let latin = app.store.latinName(for: info)
        return VStack(alignment: .leading, spacing: 8) {
            if let layer {
                TagView(text: layer.title, color: layer.tint, systemImage: layer.icon)
            }
            Text(app.store.displayName(for: info) + (info.sideTitle.map { " (\($0))" } ?? ""))
                .font(.system(.largeTitle, weight: .bold))
                .foregroundStyle(Theme.textPrimary)
                .fixedSize(horizontal: false, vertical: true)
            if let latin {
                Text(latin)
                    .font(Theme.latin(.title3))
                    .foregroundStyle(layer?.tint ?? Theme.accent)
            }
            Text(info.base)
                .font(.subheadline)
                .foregroundStyle(Theme.textTertiary)
            if let d = app.store.partDescription(info.base) {
                Card {
                    Text(d)
                        .font(.body)
                        .foregroundStyle(Theme.textPrimary)
                        .fixedSize(horizontal: false, vertical: true)
                }
                .padding(.top, 6)
            }
            if let kind = info.kind {
                Text(kind == "origin" ? String(localized: "Kasın başlangıç (origo) alanı") : String(localized: "Kasın yapışma (insersiyo) alanı"))
                    .font(.subheadline.weight(.medium))
                    .foregroundStyle(kind == "origin" ? .red : .blue)
            }
        }
        .padding(.top, 8)
    }

    private func partCard(info: PartInfo, layer: ModelLayer?) -> some View {
        ContentCard(title: String(localized: "3D model"), systemImage: "cube", tint: layer?.tint ?? .accentColor) {
            VStack(alignment: .leading, spacing: 10) {
                if let side = info.sideTitle {
                    LabeledContent("Taraf", value: side)
                }
                LabeledContent("Model adı", value: info.name)
                if !info.path.isEmpty {
                    VStack(alignment: .leading, spacing: 4) {
                        Text("Hiyerarşi")
                            .font(.subheadline)
                        Text(info.path.map { app.store.groupName($0) }.joined(separator: "  ›  "))
                            .font(.caption)
                            .foregroundStyle(.secondary)
                    }
                }
                LabeledContent("Boyut", value: dimensions(info))
            }
            .font(.subheadline)
        }
    }

    private func dimensions(_ info: PartInfo) -> String {
        let e = info.extent * 100
        let largest = max(e.x, e.y, e.z)
        return largest >= 1 ? String(format: "≈ %.1f cm", largest) : String(format: "≈ %.0f mm", largest * 10)
    }
}
