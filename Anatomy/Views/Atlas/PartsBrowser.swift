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
        let q = SearchQuery(query)
        let index = PartSearchIndex.shared(scene: app.scene, store: app.store)
        let groups = index.groups(matching: q, sex: app.sex)
        let matches = index.parts(matching: q, sex: app.sex)
        // Whole structures first ("kalp" finds the heart, not only its
        // chambers), unless a single part matches better ("böbrek").
        let partsFirst = (matches.first?.score ?? 0) > (groups.first?.score ?? 0)
        return List {
            if matches.isEmpty && groups.isEmpty {
                ContentUnavailableView.search(text: query)
            }
            if partsFirst {
                partSection(matches, titled: !groups.isEmpty)
            }
            if !groups.isEmpty {
                Section("Bütün yapılar") {
                    ForEach(groups) { group in
                        GroupRow(group: group, otherSex: group.sex.map { $0 != app.sex } ?? false, onPick: pick)
                    }
                }
            }
            if !partsFirst {
                partSection(matches, titled: !groups.isEmpty)
            }
        }
    }

    @ViewBuilder
    private func partSection(_ matches: [PartSearchIndex.Match], titled: Bool) -> some View {
        if !matches.isEmpty {
            Section(titled ? String(localized: "Parçalar") : "") {
                ForEach(matches, id: \.ref) { match in
                    PartRow(ref: match.ref, showsLayer: true, onPick: pick)
                }
            }
        }
    }

    private func pick(_ refs: [PartRef]) {
        dismiss()
        // Through the app: the other sex's organs switch the body (Premium
        // for the female one).
        app.showInAtlas(refs)
    }
}

/// Folded names of every part and model group, built once, so search keeps
/// up with typing.
@MainActor
final class PartSearchIndex {
    struct Match {
        let ref: PartRef
        let score: Int
    }

    private struct Part {
        let ref: PartRef
        let folded: [String]
        let typed: [String]
        let sex: BodySex?
        let order: Int
    }

    private struct Group {
        let layer: String
        let name: String
        let title: String
        let latin: String
        let folded: [String]
        let typed: [String]
        var refs: [PartRef] = []
        var sexes: [BodySex?] = []
    }

    private let partEntries: [Part]
    private let groupEntries: [Group]
    private static var cached: (key: Int, index: PartSearchIndex)?

    static func shared(scene: AnatomyScene, store: AtlasStore) -> PartSearchIndex {
        // The Latin glossary arrives after launch: rebuild once it has.
        let key = scene.manifests.values.reduce(0) { $0 + $1.count } &* 31 &+ store.glossary.count
        if let cached, cached.key == key { return cached.index }
        let index = PartSearchIndex(scene: scene, store: store)
        cached = (key, index)
        return index
    }

    private init(scene: AnatomyScene, store: AtlasStore) {
        var parts: [Part] = []
        var groups: [String: Group] = [:]
        var order: [String] = []
        for layer in ModelLayer.all {
            for (i, info) in (scene.manifests[layer.id] ?? []).enumerated() {
                let ref = PartRef(system: layer.id, index: i)
                let sex = info.sex.flatMap(BodySex.init(code:))
                let names = [store.displayName(for: info), store.latinName(for: info) ?? "", info.base]
                parts.append(Part(ref: ref, folded: names.map(SearchText.fold), typed: names.map(SearchText.typed),
                                  sex: sex, order: layer.id == "insertions" ? 1 : 0))
                // Attachment patches repeat the bones' groups.
                guard layer.id != "insertions" else { continue }
                // The first path element is the system itself.
                for name in info.path.dropFirst() {
                    let key = layer.id + "/" + name
                    if groups[key] == nil {
                        let title = store.groupName(name)
                        let latin = store.latinName(name) ?? ""
                        let names = [title, latin, name]
                        groups[key] = Group(layer: layer.id, name: name, title: title, latin: latin,
                                            folded: names.map(SearchText.fold), typed: names.map(SearchText.typed))
                        order.append(key)
                    }
                    groups[key]!.refs.append(ref)
                    groups[key]!.sexes.append(sex)
                }
            }
        }
        partEntries = parts
        groupEntries = order.compactMap { groups[$0] }
    }

    /// Parts matching `query`, best first: this body's parts before the other
    /// sex's, the attachment patches last.
    func parts(matching query: SearchQuery, sex: BodySex) -> [Match] {
        guard query.count >= 2 else { return [] }
        var found: [(match: Match, rank: (Int, Int))] = []
        for part in partEntries {
            let score = query.score(folded: part.folded, typed: part.typed)
            guard score > 0 else { continue }
            let other = part.sex.map { $0 != sex } ?? false
            found.append((Match(ref: part.ref, score: score), ((other ? 2 : 0) + part.order, -score)))
        }
        return found.sorted { $0.rank < $1.rank }.prefix(200).map(\.match)
    }

    /// Groups matching `query` with more than one part in this body (or only
    /// in the other sex's), best first, each set of parts once.
    func groups(matching query: SearchQuery, sex: BodySex) -> [PartGroup] {
        guard query.count >= 2 else { return [] }
        var out: [PartGroup] = []
        var seen: Set<Set<PartRef>> = []
        var scored: [(Group, Int)] = []
        for group in groupEntries {
            let score = query.score(folded: group.folded, typed: group.typed)
            if score > 0 { scored.append((group, score)) }
        }
        scored.sort { ($0.1, $0.0.refs.count) > ($1.1, $1.0.refs.count) }
        for (group, score) in scored {
            let pairs = zip(group.refs, group.sexes)
            var refs = pairs.filter { $0.1 == nil || $0.1 == sex }.map(\.0)
            var groupSex: BodySex?
            if refs.count <= 1 {
                refs = pairs.filter { $0.1 != nil && $0.1 != sex }.map(\.0)
                groupSex = sex == .male ? .female : .male
            }
            guard refs.count > 1, seen.insert(Set(refs)).inserted else { continue }
            out.append(PartGroup(id: group.layer + "/" + group.name, layer: group.layer, name: group.name, title: group.title,
                                 latin: group.latin, score: score, refs: refs, sex: groupSex))
            if out.count == 12 { break }
        }
        return out
    }
}

/// A group of the model hierarchy found by name.
struct PartGroup: Identifiable {
    let id: String
    let layer: String
    let name: String
    let title: String
    let latin: String
    let score: Int
    var refs: [PartRef]
    /// Set when the group is only in the other sex's body.
    var sex: BodySex? = nil
}

private struct GroupRow: View {
    let group: PartGroup
    var otherSex = false
    let onPick: ([PartRef]) -> Void

    var body: some View {
        Button {
            onPick(group.refs)
        } label: {
            HStack(spacing: 10) {
                if let layer = ModelLayer.layer(group.layer) {
                    SystemBadge(icon: layer.icon, color: layer.tint, size: 28)
                }
                VStack(alignment: .leading, spacing: 2) {
                    Text(group.title)
                        .font(.subheadline.weight(.semibold))
                        .foregroundStyle(.primary)
                    Text("\(ModelLayer.layer(group.layer)?.title ?? "") · " + String(localized: "\(group.refs.count) parça") + (otherSex ? " · \(group.sex?.title ?? "")" : ""))
                        .font(.caption)
                        .foregroundStyle(.secondary)
                        .lineLimit(1)
                }
                Spacer()
                Image(systemName: "scope").foregroundStyle(.tint)
            }
        }
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
                            if let sex = app.scene.sex(of: ref), sex != app.sex {
                                Text(sex.title)
                                    .font(.caption2.weight(.semibold))
                                    .foregroundStyle(.secondary)
                                    .padding(.horizontal, 6)
                                    .padding(.vertical, 1)
                                    .background(Theme.elevated, in: .capsule)
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
