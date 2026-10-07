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
                                ContentCard(title: "Bağlı olduğu yapı", systemImage: "arrow.turn.up.right", tint: layer?.tint ?? .accentColor) {
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
            .atlasBackground()
            .navigationTitle(exact ? entry!.tr : (store.latinName(for: info) ?? info.base))
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
            Text(latin ?? info.base)
                .font(.largeTitle.weight(.bold))
                .fixedSize(horizontal: false, vertical: true)
            if let latin, latin.lowercased() != info.base.lowercased() {
                Text(info.base)
                    .font(.title3)
                    .foregroundStyle(.secondary)
            }
            if let kind = info.kind {
                Text(kind == "origin" ? "Kasın başlangıç (origo) alanı" : "Kasın yapışma (insersiyo) alanı")
                    .font(.subheadline.weight(.medium))
                    .foregroundStyle(kind == "origin" ? .red : .blue)
            }
        }
        .padding(.top, 8)
    }

    private func partCard(info: PartInfo, layer: ModelLayer?) -> some View {
        ContentCard(title: "3D model", systemImage: "cube", tint: layer?.tint ?? .accentColor) {
            VStack(alignment: .leading, spacing: 10) {
                if let side = info.sideTitle {
                    LabeledContent("Taraf", value: side)
                }
                LabeledContent("Model adı", value: info.name)
                if !info.path.isEmpty {
                    VStack(alignment: .leading, spacing: 4) {
                        Text("Hiyerarşi")
                            .font(.subheadline)
                        Text(info.path.map { app.store.term($0)?.la ?? $0 }.joined(separator: "  ›  "))
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
