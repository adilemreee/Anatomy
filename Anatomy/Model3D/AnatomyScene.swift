//
//  AnatomyScene.swift
//  Anatomy
//
//  Owns the RealityKit content for the 3D atlas: one LowLevelMesh per body
//  system, per-part visibility / ghosting / selection, an orbit camera and CPU
//  ray picking against the decoded geometry.
//

import Metal
import RealityKit
import SwiftUI
import UIKit

/// Identifies one 3D part inside a system pack.
nonisolated struct PartRef: Hashable, Sendable {
    let system: String
    let index: Int
}

/// A toggleable 3D layer (one Z-Anatomy system collection).
nonisolated struct ModelLayer: Identifiable, Hashable, Sendable {
    let id: String
    let title: String
    let icon: String
    /// Fallback colour for parts without their own material colour.
    let color: String
    let roughness: Float
    let defaultOn: Bool

    var tint: Color { Color(hex: color) }

    static let all: [ModelLayer] = [
        ModelLayer(id: "skeletal", title: "İskelet", icon: "figure.stand", color: "e9dfca", roughness: 0.7, defaultOn: true),
        ModelLayer(id: "joints", title: "Eklemler ve Bağlar", icon: "figure.flexibility", color: "c9d6dc", roughness: 0.5, defaultOn: false),
        ModelLayer(id: "muscular", title: "Kaslar", icon: "figure.strengthtraining.traditional", color: "b8473f", roughness: 0.55, defaultOn: true),
        ModelLayer(id: "insertions", title: "Kas Yapışma Yerleri", icon: "pin.fill", color: "d0453b", roughness: 0.5, defaultOn: false),
        ModelLayer(id: "cardiovascular", title: "Kalp ve Damarlar", icon: "heart.fill", color: "c4302b", roughness: 0.45, defaultOn: false),
        ModelLayer(id: "lymphoid", title: "Lenfoid Organlar", icon: "shield.lefthalf.filled", color: "8fb46a", roughness: 0.45, defaultOn: false),
        ModelLayer(id: "nervous", title: "Sinir Sistemi ve Duyular", icon: "brain.head.profile.fill", color: "e8c34a", roughness: 0.45, defaultOn: false),
        ModelLayer(id: "visceral", title: "İç Organlar", icon: "lungs.fill", color: "d98b7c", roughness: 0.48, defaultOn: false),
        ModelLayer(id: "regions", title: "Deri ve Bölgeler", icon: "hand.raised.fill", color: "e8c2a8", roughness: 0.6, defaultOn: false),
    ]

    static func layer(_ id: String) -> ModelLayer? { all.first { $0.id == id } }
}

@MainActor
@Observable
final class AnatomyScene {
    // MARK: Observable state

    private(set) var enabledLayers: Set<String>
    private(set) var ghostedLayers: Set<String> = []
    private(set) var loadingLayers: Set<String> = []
    /// Layers whose geometry is on screen.
    private(set) var loadedLayers: Set<String> = []
    private(set) var failedLayers: [String: String] = [:]
    /// The part that was tapped.
    private(set) var selection: PartRef?
    /// Everything drawn as selected: the tapped part plus the other parts of
    /// the same structure on the same side (e.g. both heads of biceps).
    private(set) var selectedGroup: Set<PartRef> = []
    private(set) var hiddenParts: Set<PartRef> = []
    private(set) var isolation: Set<PartRef>?
    private(set) var highlighted: Set<PartRef> = []
    var showCoverings = false { didSet { refreshAll() } }
    var xray = false { didSet { refreshAll() } }
    var colorMode: ColorMode = .realistic { didSet { if colorMode != oldValue { recolorAll() } } }
    /// Bumped whenever the camera comes to rest (after a gesture or animation).
    private(set) var cameraVersion = 0
    var isCameraMoving = false
    /// Bumped whenever the set of drawn parts changes.
    private(set) var visibilityVersion = 0

    /// Resolves the parts that belong to the same structure as a tapped part.
    @ObservationIgnored var groupResolver: ((PartRef) -> Set<PartRef>)?

    @ObservationIgnored let library = PackLibrary.shared
    /// Manifests for every layer, loaded eagerly so search works before the
    /// geometry is on screen.
    @ObservationIgnored let manifests: [String: [PartInfo]]
    /// Lowercased part names and group names -> parts.
    @ObservationIgnored private let nameIndex: [String: [PartRef]]
    /// Per-part `isCovering`, precomputed because it is checked on every refresh.
    @ObservationIgnored private let coverings: [String: [Bool]]

    // MARK: RealityKit

    @ObservationIgnored let root = Entity()
    @ObservationIgnored let camera = Entity()
    @ObservationIgnored private let modelRoot = Entity()
    @ObservationIgnored private var iblEntity: Entity?
    @ObservationIgnored private var shadow: Entity?
    @ObservationIgnored var systems: [String: LoadedSystem] = [:]
    @ObservationIgnored var tween: Task<Void, Never>?
    @ObservationIgnored private var materials: [any RealityKit.Material] = []
    @ObservationIgnored private var materialsIsolated = false

    // Orbit camera parameters.
    @ObservationIgnored var yaw: Float = 0
    @ObservationIgnored var pitch: Float = 0.05
    @ObservationIgnored var distance: Float = 3.3
    @ObservationIgnored var target = SIMD3<Float>(0, 0.88, 0)
    @ObservationIgnored let fieldOfView: Float = 38

    static let homeTarget = SIMD3<Float>(0, 0.88, 0)
    static let homeDistance: Float = 3.3

    struct LoadedSystem {
        let pack: MeshPack
        let mesh: LowLevelMesh
        let entity: ModelEntity
        let bounds: [BoundingBox]
    }

    init(initialLayers: Set<String>? = nil) {
        enabledLayers = initialLayers ?? Set(ModelLayer.all.filter(\.defaultOn).map(\.id))
        var manifests: [String: [PartInfo]] = [:]
        for layer in ModelLayer.all {
            manifests[layer.id] = PackLibrary.shared.parts(layer.id)
        }
        self.manifests = manifests
        var index: [String: [PartRef]] = [:]
        for layer in ModelLayer.all {
            for (i, part) in (manifests[layer.id] ?? []).enumerated() {
                let ref = PartRef(system: layer.id, index: i)
                index[part.base.lowercased(), default: []].append(ref)
                for group in Set(part.path) where group.lowercased() != part.base.lowercased() {
                    index[group.lowercased(), default: []].append(ref)
                }
            }
        }
        nameIndex = index
        coverings = manifests.mapValues { $0.map(\.isCovering) }

        camera.components.set(PerspectiveCameraComponent(near: 0.01, far: 50, fieldOfViewInDegrees: fieldOfView, fieldOfViewOrientation: .vertical))
        for light in AnatomyMaterials.cameraLights() {
            camera.addChild(light)
        }
        root.addChild(camera)
        root.addChild(modelRoot)
        setupEnvironment()
        applyCamera()
    }

    // MARK: Layers

    func isEnabled(_ layer: String) -> Bool { enabledLayers.contains(layer) }
    func isGhosted(_ layer: String) -> Bool { ghostedLayers.contains(layer) }
    func isLoaded(_ layer: String) -> Bool { systems[layer] != nil }
    func materialNames(_ layer: String) -> [String] { library.materials(layer) }

    func setLayer(_ layer: String, enabled: Bool) {
        if enabled {
            enabledLayers.insert(layer)
        } else {
            enabledLayers.remove(layer)
            if selection?.system == layer { select(nil) }
        }
        if enabled, systems[layer] == nil {
            Task { await load(layer) }
        } else {
            refresh(layer)
        }
    }

    func setLayer(_ layer: String, ghosted: Bool) {
        if ghosted { ghostedLayers.insert(layer) } else { ghostedLayers.remove(layer) }
        refresh(layer)
    }

    /// Loads every enabled layer that is not on screen yet.
    func loadEnabledLayers() async {
        let pending = ModelLayer.all.filter { enabledLayers.contains($0.id) && systems[$0.id] == nil }
        // Decode all packs in the background while the shader compiles on the
        // main thread; the layers still appear in order.
        for layer in pending {
            Task { _ = try? await library.pack(layer.id) }
        }
        if materials.isEmpty {
            materials = await AnatomyMaterials.shared()
        }
        for layer in pending {
            await load(layer.id)
        }
        // Warm up the other sets so isolating and inspecting open smoothly.
        _ = await AnatomyMaterials.shared(occlusion: 0.45)
        _ = await AnatomyMaterials.shared(occlusion: 0.55, rim: 0.7)
    }

    func ensureLoaded(_ layer: String) async {
        if systems[layer] == nil { await load(layer) }
    }

    private func load(_ layerID: String) async {
        guard systems[layerID] == nil, !loadingLayers.contains(layerID), ModelLayer.layer(layerID) != nil else { return }
        loadingLayers.insert(layerID)
        defer { loadingLayers.remove(layerID) }
        do {
            let pack = try await library.pack(layerID)
            let mode = colorMode
            let vertices = await Task.detached(priority: .userInitiated) {
                VertexBuilder.build(pack: pack, mode: mode)
            }.value
            if materials.isEmpty {
                materials = await AnatomyMaterials.shared(occlusion: materialsIsolated ? 0.45 : 1)
            }
            guard systems[layerID] == nil else { return }
            let loaded = try build(pack: pack, vertices: vertices)
            systems[layerID] = loaded
            loadedLayers.insert(layerID)
            modelRoot.addChild(loaded.entity)
            failedLayers[layerID] = nil
            refresh(layerID)
        } catch {
            failedLayers[layerID] = String(describing: error)
        }
    }

    private func build(pack: MeshPack, vertices: VertexBuilder.Output) throws -> LoadedSystem {
        let mesh = try Self.makeMesh(vertexCount: pack.positions.count, indexCount: vertices.indices.count)
        Self.upload(vertices, into: mesh)
        var bounds: [BoundingBox] = []
        bounds.reserveCapacity(pack.parts.count)
        for part in pack.parts {
            let b = part.bounds
            bounds.append(BoundingBox(min: SIMD3(b[0], b[1], b[2]), max: SIMD3(b[3], b[4], b[5])))
        }
        let entity = ModelEntity()
        entity.name = pack.system
        let loaded = LoadedSystem(pack: pack, mesh: mesh, entity: entity, bounds: bounds)
        mesh.parts.replaceAll(parts(for: loaded))
        let resource = try MeshResource(from: mesh)
        entity.components.set(ModelComponent(mesh: resource, materials: materials))
        if let iblEntity {
            entity.components.set(ImageBasedLightReceiverComponent(imageBasedLight: iblEntity))
        }
        return loaded
    }

    static func makeMesh(vertexCount: Int, indexCount: Int) throws -> LowLevelMesh {
        var descriptor = LowLevelMesh.Descriptor()
        descriptor.vertexCapacity = vertexCount
        descriptor.indexCapacity = indexCount
        descriptor.indexType = .uint32
        descriptor.vertexAttributes = [
            .init(semantic: .position, format: .float3, layoutIndex: 0, offset: 0),
            .init(semantic: .normal, format: .float3, layoutIndex: 0, offset: 12),
            .init(semantic: .tangent, format: .float3, layoutIndex: 0, offset: 24),
            .init(semantic: .color, format: .uchar4Normalized, layoutIndex: 0, offset: 36),
            .init(semantic: .uv1, format: .float2, layoutIndex: 0, offset: 40),
            .init(semantic: .uv2, format: .float4, layoutIndex: 0, offset: 48),
        ]
        descriptor.vertexLayouts = [.init(bufferIndex: 0, bufferStride: VertexBuilder.stride)]
        return try LowLevelMesh(descriptor: descriptor)
    }

    static func upload(_ vertices: VertexBuilder.Output, into mesh: LowLevelMesh) {
        mesh.withUnsafeMutableBytes(bufferIndex: 0) { raw in
            vertices.vertices.withUnsafeBytes { src in
                guard let base = src.baseAddress, let dst = raw.baseAddress else { return }
                dst.copyMemory(from: base, byteCount: min(src.count, raw.count))
            }
        }
        mesh.withUnsafeMutableIndices { raw in
            let out = raw.bindMemory(to: UInt32.self)
            vertices.indices.withUnsafeBufferPointer { src in
                guard let base = src.baseAddress, let dst = out.baseAddress else { return }
                dst.update(from: base, count: min(src.count, out.count))
            }
        }
    }

    /// Rewrites vertex colours after a colour mode change.
    private func recolorAll() {
        let mode = colorMode
        for (id, system) in systems {
            let pack = system.pack
            Task {
                let vertices = await Task.detached(priority: .userInitiated) {
                    VertexBuilder.build(pack: pack, mode: mode)
                }.value
                guard colorMode == mode, let current = systems[id] else { return }
                current.mesh.withUnsafeMutableBytes(bufferIndex: 0) { raw in
                    vertices.vertices.withUnsafeBytes { src in
                        guard let base = src.baseAddress, let dst = raw.baseAddress else { return }
                        dst.copyMemory(from: base, byteCount: min(src.count, raw.count))
                    }
                }
            }
        }
    }

    private func setupEnvironment() {
        Task { [weak self] in
            guard let environment = await AnatomyMaterials.environment(), let self else { return }
            let ibl = Entity()
            ibl.components.set(ImageBasedLightComponent(source: .single(environment), intensityExponent: -0.45))
            self.root.addChild(ibl)
            self.iblEntity = ibl
            for system in self.systems.values {
                system.entity.components.set(ImageBasedLightReceiverComponent(imageBasedLight: ibl))
            }
            if let shadow = await AnatomyMaterials.contactShadow() {
                self.shadow = shadow
                self.modelRoot.addChild(shadow)
            }
        }
    }

    // MARK: Part state

    enum PartState { case hidden, solid, ghost, selected, highlighted }

    func state(of ref: PartRef) -> PartState {
        guard enabledLayers.contains(ref.system) else { return .hidden }
        if hiddenParts.contains(ref) { return .hidden }
        if let isolation, !isolation.contains(ref) { return .hidden }
        let selected = selectedGroup.contains(ref)
        if !showCoverings, coverings[ref.system]?[ref.index] == true, !selected, !highlighted.contains(ref) { return .hidden }
        if selected { return .selected }
        if highlighted.contains(ref) { return .highlighted }
        if xray { return .ghost }
        if ghostedLayers.contains(ref.system) { return .ghost }
        return .solid
    }

    /// Builds the draw list for a system. Neighbouring parts in the same state
    /// are contiguous in the index buffer, so they collapse into one draw call;
    /// colours live in the vertices and picking works on the CPU copy.
    private func parts(for system: LoadedSystem) -> [LowLevelMesh.Part] {
        let id = system.pack.system
        var out: [LowLevelMesh.Part] = []
        var runStart = 0
        var runCount = 0
        var runMaterial = -1
        var runBounds = BoundingBox()

        func flush() {
            guard runCount > 0 else { return }
            out.append(LowLevelMesh.Part(
                indexOffset: runStart * MemoryLayout<UInt32>.size,
                indexCount: runCount,
                topology: .triangle,
                materialIndex: runMaterial,
                bounds: runBounds
            ))
            runCount = 0
            runMaterial = -1
        }

        for (i, range) in system.pack.ranges.enumerated() {
            let material: Int
            switch state(of: PartRef(system: id, index: i)) {
            case .hidden:
                flush()
                continue
            case .solid: material = AnatomyMaterials.Slot.solid.rawValue
            case .ghost: material = AnatomyMaterials.Slot.ghost.rawValue
            case .selected: material = AnatomyMaterials.Slot.selected.rawValue
            case .highlighted: material = AnatomyMaterials.Slot.highlighted.rawValue
            }
            if material == runMaterial, range.indexStart == runStart + runCount {
                runCount += range.indexCount
                runBounds = runBounds.union(system.bounds[i])
            } else {
                flush()
                runStart = range.indexStart
                runCount = range.indexCount
                runMaterial = material
                runBounds = system.bounds[i]
            }
        }
        flush()
        return out
    }

    private func refresh(_ layer: String) {
        visibilityVersion &+= 1
        guard let system = systems[layer] else { return }
        system.mesh.parts.replaceAll(parts(for: system))
        system.entity.isEnabled = enabledLayers.contains(layer)
    }

    func refreshAll() {
        // Deep structures look too dark with full crease shading when isolated.
        let isolated = isolation != nil
        if isolated != materialsIsolated {
            materialsIsolated = isolated
            Task {
                let set = await AnatomyMaterials.shared(occlusion: isolated ? 0.45 : 1)
                guard materialsIsolated == isolated else { return }
                materials = set
                for system in systems.values {
                    system.entity.model?.materials = set
                }
            }
        }
        for layer in systems.keys { refresh(layer) }
    }

    // MARK: Selection & visibility

    func select(_ ref: PartRef?) {
        let touched = Set(selectedGroup.map(\.system)).union(ref.map { [$0.system] } ?? [])
        selection = ref
        if let ref {
            var group = groupResolver?(ref) ?? [ref]
            group.insert(ref)
            selectedGroup = group
        } else {
            selectedGroup = []
        }
        for system in touched { refresh(system) }
    }

    func hide(_ ref: PartRef) {
        let group = selectedGroup.contains(ref) ? selectedGroup : [ref]
        hiddenParts.formUnion(group)
        if let selection, group.contains(selection) { select(nil) }
        for system in Set(group.map(\.system)) { refresh(system) }
    }

    func unhide(_ ref: PartRef) {
        hiddenParts.remove(ref)
        refresh(ref.system)
    }

    func isolate(_ refs: Set<PartRef>) {
        isolation = refs
        for system in Set(refs.map(\.system)) where !enabledLayers.contains(system) {
            setLayer(system, enabled: true)
        }
        refreshAll()
    }

    var isIsolating: Bool { isolation != nil }

    func showAll() {
        hiddenParts.removeAll()
        isolation = nil
        refreshAll()
    }

    func highlight(_ refs: Set<PartRef>) {
        let systemsTouched = Set(highlighted.map(\.system)).union(refs.map(\.system))
        highlighted = refs
        for system in systemsTouched { refresh(system) }
    }

    func info(_ ref: PartRef) -> PartInfo? {
        guard let parts = manifests[ref.system], parts.indices.contains(ref.index) else { return nil }
        return parts[ref.index]
    }

    /// Every part whose base name, or one of whose ancestor groups, matches one
    /// of `names` (case-insensitive).
    /// Muscle attachment patches share names with their muscles; they are only
    /// returned when asked for explicitly.
    func refs(matching names: [String], includeInsertions: Bool = false) -> [PartRef] {
        var seen = Set<PartRef>()
        var out: [PartRef] = []
        for name in names {
            for ref in nameIndex[name.lowercased()] ?? []
            where (includeInsertions || ref.system != "insertions") && seen.insert(ref).inserted {
                out.append(ref)
            }
        }
        return out
    }

    func cameraDidSettle() {
        isCameraMoving = false
        cameraVersion += 1
    }

    /// Shows `refs` on screen: enables their layers, highlights and frames them.
    func reveal(_ refs: [PartRef], isolate: Bool = false, margin: Float = 1.15) async {
        guard !refs.isEmpty else { return }
        for system in Set(refs.map(\.system)) {
            if !enabledLayers.contains(system) { enabledLayers.insert(system) }
            await ensureLoaded(system)
            refresh(system)
        }
        if isolate {
            self.isolate(Set(refs))
        }
        if refs.count == 1 {
            select(refs[0])
            highlight([])
        } else {
            select(nil)
            highlight(Set(refs))
        }
        frame(refs, margin: margin)
    }

}
