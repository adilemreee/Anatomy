//
//  PartsBrowser.swift
//  Anatomy
//

import SwiftUI

/// Browses every 3D part by the model's own hierarchy, with search.
struct PartsBrowser: View {
    @Environment(AppModel.self) private var app
    @Environment(\.dismiss) private var dismiss
    @State private var query = ""
    @State private var layerID = "skeletal"

    var body: some View {
        NavigationStack {
            Group {
                if query.isEmpty {
                    tree
                } else {
                    results
                }
            }
            .scrollContentBackground(.hidden)
            .background(Theme.surface.ignoresSafeArea())
            .navigationTitle("3D Parçalar")
            .navigationBarTitleDisplayMode(.inline)
            .searchable(text: $query, placement: .navigationBarDrawer(displayMode: .always), prompt: "Parça ara (Latince, İngilizce, Türkçe)")
            .toolbar {
                ToolbarItem(placement: .confirmationAction) {
                    Button("Bitti") { dismiss() }
                }
            }
        }
    }

    private var tree: some View {
        List {
            Section {
                Picker("Katman", selection: $layerID) {
                    ForEach(ModelLayer.all) { layer in
                        Label(layer.title, systemImage: layer.icon).tag(layer.id)
                    }
                }
            }
            let root = PartTree.build(parts: app.scene.manifests[layerID] ?? [], sex: app.sex)
            ForEach(root.children) { node in
                NodeView(node: node, layerID: layerID, onPick: pick)
            }
            if !root.parts.isEmpty {
                ForEach(root.parts, id: \.self) { index in
                    PartRow(ref: PartRef(system: layerID, index: index), onPick: pick)
                }
            }
        }
    }

    private var results: some View {
        let matches = search(query)
        return List {
            if matches.isEmpty {
                ContentUnavailableView.search(text: query)
            }
            ForEach(matches, id: \.self) { ref in
                PartRow(ref: ref, showsLayer: true, onPick: pick)
            }
        }
    }

    private func search(_ text: String) -> [PartRef] {
        let q = SearchText.fold(text)
        guard q.count >= 2 else { return [] }
        let store = app.store
        var out: [PartRef] = []
        for layer in ModelLayer.all {
            for (i, part) in (app.scene.manifests[layer.id] ?? []).enumerated() where part.shows(for: app.sex) {
                let names = [part.base, store.latinName(for: part) ?? "", store.displayName(for: part)]
                if names.contains(where: { SearchText.fold($0).contains(q) }) {
                    out.append(PartRef(system: layer.id, index: i))
                    if out.count >= 200 { return out }
                }
            }
        }
        return out
    }

    private func pick(_ refs: [PartRef]) {
        dismiss()
        Task { await app.scene.reveal(refs) }
    }
}

/// The part hierarchy of one layer, built from each part's ancestor path.
final class PartTree: Identifiable {
    let id: String
    let name: String
    var children: [PartTree] = []
    var parts: [Int] = []

    init(id: String, name: String) {
        self.id = id
        self.name = name
    }

    /// All part indices below this node.
    var allParts: [Int] { parts + children.flatMap(\.allParts) }

    @MainActor private static var cache: [Int: PartTree] = [:]

    /// The tree of `parts`, without the other sex's genital organs.
    @MainActor static func build(parts: [PartInfo], sex: BodySex) -> PartTree {
        let key = (parts.count ^ (parts.first?.name.hashValue ?? 0)) &* 2 + (sex == .female ? 1 : 0)
        if let tree = cache[key] { return tree }
        let root = PartTree(id: "root", name: "")
        var lookup: [String: PartTree] = ["": root]
        for (index, part) in parts.enumerated() where part.shows(for: sex) {
            // The first path element is the system itself; skip it.
            let path = Array(part.path.dropFirst())
            var node = root
            var key = ""
            for name in path {
                key += "/" + name
                if let next = lookup[key] {
                    node = next
                } else {
                    let next = PartTree(id: key, name: name)
                    node.children.append(next)
                    lookup[key] = next
                    node = next
                }
            }
            node.parts.append(index)
        }
        cache[key] = root
        return root
    }
}

private struct NodeView: View {
    @Environment(AppModel.self) private var app
    let node: PartTree
    let layerID: String
    let onPick: ([PartRef]) -> Void

    var body: some View {
        DisclosureGroup {
            ForEach(node.children) { child in
                NodeView(node: child, layerID: layerID, onPick: onPick)
            }
            ForEach(node.parts, id: \.self) { index in
                PartRow(ref: PartRef(system: layerID, index: index), onPick: onPick)
            }
        } label: {
            HStack {
                let latin = app.store.latinName(node.name)
                VStack(alignment: .leading, spacing: 2) {
                    Text(app.store.groupName(node.name))
                        .font(.subheadline.weight(.semibold))
                    if let latin {
                        Text(latin)
                            .font(.caption.italic())
                            .foregroundStyle(.secondary)
                    }
                }
                Spacer()
                Button {
                    onPick(node.allParts.map { PartRef(system: layerID, index: $0) })
                } label: {
                    Image(systemName: "scope")
                }
                .buttonStyle(.borderless)
                .accessibilityLabel("Grubu 3D'de göster")
            }
        }
    }
}

private struct PartRow: View {
    @Environment(AppModel.self) private var app
    let ref: PartRef
    var showsLayer = false
    let onPick: ([PartRef]) -> Void

    var body: some View {
        if let info = app.scene.info(ref) {
            let store = app.store
            let entry = store.entry(for: info)
            let exact = entry.map { store.isExact($0, for: info) } ?? false
            Button {
                onPick([ref])
            } label: {
                HStack(spacing: 10) {
                    Circle()
                        .fill(MaterialStyles.swatch(for: info, layer: ref.system, materials: app.scene.materialNames(ref.system), mode: app.scene.colorMode))
                        .frame(width: 10, height: 10)
                    VStack(alignment: .leading, spacing: 2) {
                        HStack(spacing: 4) {
                            Text(store.displayName(for: info))
                                .foregroundStyle(.primary)
                            if let side = info.sideTitle {
                                Text(side).foregroundStyle(.secondary)
                            }
                        }
                        .font(.subheadline)
                        Text(showsLayer ? "\(ModelLayer.layer(ref.system)?.title ?? "") · \(store.latinName(for: info) ?? info.base)" : (store.latinName(for: info) ?? info.base))
                            .font(.caption)
                            .foregroundStyle(.secondary)
                            .lineLimit(1)
                    }
                    Spacer()
                    if app.scene.hiddenParts.contains(ref) {
                        Image(systemName: "eye.slash").foregroundStyle(.secondary)
                    }
                }
            }
            .swipeActions {
                if app.scene.hiddenParts.contains(ref) {
                    Button("Göster") { app.scene.unhide(ref) }
                } else {
                    Button("Gizle") { app.scene.hide(ref) }.tint(.gray)
                }
            }
        }
    }
}
