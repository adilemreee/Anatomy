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
    private(set) var failedLayers: [String: String] = [:]
    private(set) var selection: PartRef?
    private(set) var hiddenParts: Set<PartRef> = []
    private(set) var isolation: Set<PartRef>?
    private(set) var highlighted: Set<PartRef> = []
    var showFascia = false { didSet { refreshAll() } }
    var xray = false { didSet { refreshAll() } }

    /// Manifests for every layer, loaded eagerly so search works before the
    /// geometry is on screen.
    @ObservationIgnored let manifests: [String: [PartInfo]]
    /// Lowercased part names and group names -> parts.
    @ObservationIgnored private let nameIndex: [String: [PartRef]]

    // MARK: RealityKit

    @ObservationIgnored let root = Entity()
    @ObservationIgnored private let camera = Entity()
    @ObservationIgnored private let modelRoot = Entity()
    @ObservationIgnored private var iblEntity: Entity?
    @ObservationIgnored private var systems: [String: LoadedSystem] = [:]
    @ObservationIgnored private var tween: Task<Void, Never>?

    // Orbit camera parameters.
    @ObservationIgnored private(set) var yaw: Float = 0
    @ObservationIgnored private(set) var pitch: Float = 0.05
    @ObservationIgnored private(set) var distance: Float = 3.3
    @ObservationIgnored private(set) var target = SIMD3<Float>(0, 0.88, 0)
    @ObservationIgnored let fieldOfView: Float = 38

    static let homeTarget = SIMD3<Float>(0, 0.88, 0)
    static let homeDistance: Float = 3.3

    private struct LoadedSystem {
        let pack: MeshPack
        let mesh: LowLevelMesh
        let entity: ModelEntity
        /// Palette slot of every part.
        let colorSlot: [Int]
        let paletteCount: Int
        let bounds: [BoundingBox]
    }

    init(initialLayers: Set<String>? = nil) {
        enabledLayers = initialLayers ?? Set(ModelLayer.all.filter(\.defaultOn).map(\.id))
        var manifests: [String: [PartInfo]] = [:]
        for layer in ModelLayer.all {
            manifests[layer.id] = (try? MeshPack.manifest(for: layer.id))?.parts ?? []
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

        let cameraComponent = PerspectiveCameraComponent(near: 0.01, far: 50, fieldOfViewInDegrees: fieldOfView, fieldOfViewOrientation: .vertical)
        camera.components.set(cameraComponent)
        let key = DirectionalLight()
        key.light.intensity = 900
        key.light.color = .white
        key.orientation = simd_quatf(angle: -.pi / 9, axis: [1, 0, 0]) * simd_quatf(angle: .pi / 10, axis: [0, 1, 0])
        camera.addChild(key)
        root.addChild(camera)
        root.addChild(modelRoot)
        setupLighting()
        applyCamera()
    }

    // MARK: Layers

    func isEnabled(_ layer: String) -> Bool { enabledLayers.contains(layer) }
    func isGhosted(_ layer: String) -> Bool { ghostedLayers.contains(layer) }
    func isLoaded(_ layer: String) -> Bool { systems[layer] != nil }

    func setLayer(_ layer: String, enabled: Bool) {
        if enabled {
            enabledLayers.insert(layer)
        } else {
            enabledLayers.remove(layer)
            if selection?.system == layer { selection = nil }
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
        for layer in ModelLayer.all where enabledLayers.contains(layer.id) && systems[layer.id] == nil {
            await load(layer.id)
        }
    }

    func ensureLoaded(_ layer: String) async {
        if systems[layer] == nil { await load(layer) }
    }

    private func load(_ layerID: String) async {
        guard systems[layerID] == nil, !loadingLayers.contains(layerID), let layer = ModelLayer.layer(layerID) else { return }
        loadingLayers.insert(layerID)
        defer { loadingLayers.remove(layerID) }
        do {
            let pack = try await Task.detached(priority: .userInitiated) {
                try MeshPack.load(system: layerID)
            }.value
            let loaded = try build(pack: pack, layer: layer)
            systems[layerID] = loaded
            modelRoot.addChild(loaded.entity)
            failedLayers[layerID] = nil
            refresh(layerID)
        } catch {
            failedLayers[layerID] = String(describing: error)
        }
    }

    private func build(pack: MeshPack, layer: ModelLayer) throws -> LoadedSystem {
        let vertexCount = pack.positions.count
        let stride = MemoryLayout<Float>.size * 6
        var descriptor = LowLevelMesh.Descriptor()
        descriptor.vertexCapacity = vertexCount
        descriptor.indexCapacity = pack.indices.count
        descriptor.indexType = .uint32
        descriptor.vertexAttributes = [
            .init(semantic: .position, format: .float3, layoutIndex: 0, offset: 0),
            .init(semantic: .normal, format: .float3, layoutIndex: 0, offset: MemoryLayout<Float>.size * 3),
        ]
        descriptor.vertexLayouts = [.init(bufferIndex: 0, bufferStride: stride)]
        let mesh = try LowLevelMesh(descriptor: descriptor)

        mesh.withUnsafeMutableBytes(bufferIndex: 0) { raw in
            let out = raw.bindMemory(to: Float.self)
            for i in 0..<vertexCount {
                let p = pack.positions[i]
                let n = pack.normals[i]
                let o = i * 6
                out[o] = p.x; out[o + 1] = p.y; out[o + 2] = p.z
                out[o + 3] = n.x; out[o + 4] = n.y; out[o + 5] = n.z
            }
        }
        mesh.withUnsafeMutableIndices { raw in
            let out = raw.bindMemory(to: UInt32.self)
            pack.indices.withUnsafeBufferPointer { src in
                guard let base = src.baseAddress, let dst = out.baseAddress else { return }
                dst.update(from: base, count: src.count)
            }
        }

        // Palette: one solid + one ghost material per distinct colour, then the
        // selection and the "highlighted" (search/quiz) materials.
        var palette: [String] = []
        var slotOf: [String: Int] = [:]
        var colorSlot: [Int] = []
        colorSlot.reserveCapacity(pack.parts.count)
        for part in pack.parts {
            let hex = Self.displayColor(for: part, layer: layer)
            if let slot = slotOf[hex] {
                colorSlot.append(slot)
            } else {
                slotOf[hex] = palette.count
                colorSlot.append(palette.count)
                palette.append(hex)
            }
        }
        var materials: [any RealityKit.Material] = palette.map { Self.solidMaterial(hex: $0, roughness: layer.roughness) }
        materials += palette.map { Self.ghostMaterial(hex: $0) }
        materials.append(Self.selectionMaterial())
        materials.append(Self.highlightMaterial())

        var bounds: [BoundingBox] = []
        bounds.reserveCapacity(pack.parts.count)
        for part in pack.parts {
            let b = part.bounds
            bounds.append(BoundingBox(min: SIMD3(b[0], b[1], b[2]), max: SIMD3(b[3], b[4], b[5])))
        }

        let entity = ModelEntity()
        entity.name = layer.id
        let loaded = LoadedSystem(pack: pack, mesh: mesh, entity: entity, colorSlot: colorSlot, paletteCount: palette.count, bounds: bounds)
        mesh.parts.replaceAll(parts(for: loaded))
        let resource = try MeshResource(from: mesh)
        entity.components.set(ModelComponent(mesh: resource, materials: materials))
        if let iblEntity {
            entity.components.set(ImageBasedLightReceiverComponent(imageBasedLight: iblEntity))
        }
        return loaded
    }

    private static func displayColor(for part: PartInfo, layer: ModelLayer) -> String {
        PartPalette.color(for: part, layer: layer.id)
    }

    // MARK: Part state

    enum PartState { case hidden, solid, ghost, selected, highlighted }

    func state(of ref: PartRef) -> PartState {
        guard enabledLayers.contains(ref.system) else { return .hidden }
        if hiddenParts.contains(ref) { return .hidden }
        if let isolation, !isolation.contains(ref) { return .hidden }
        if !showFascia, manifests[ref.system]?[ref.index].isFascia == true, selection != ref { return .hidden }
        if selection == ref { return .selected }
        if highlighted.contains(ref) { return .highlighted }
        if xray { return .ghost }
        if ghostedLayers.contains(ref.system) { return .ghost }
        return .solid
    }

    /// Builds the draw list for a system. Neighbouring parts that share a
    /// material are contiguous in the index buffer, so they are merged into a
    /// single draw call; picking works on the CPU copy and is unaffected.
    private func parts(for system: LoadedSystem) -> [LowLevelMesh.Part] {
        let id = system.pack.system
        let k = system.paletteCount
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
            case .solid: material = system.colorSlot[i]
            case .ghost: material = k + system.colorSlot[i]
            case .selected: material = 2 * k
            case .highlighted: material = 2 * k + 1
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
        guard let system = systems[layer] else { return }
        system.mesh.parts.replaceAll(parts(for: system))
        system.entity.isEnabled = enabledLayers.contains(layer)
    }

    private func refreshAll() {
        for layer in systems.keys { refresh(layer) }
    }

    // MARK: Selection & visibility

    func select(_ ref: PartRef?) {
        let old = selection
        selection = ref
        if let old { refresh(old.system) }
        if let ref, ref.system != old?.system { refresh(ref.system) }
    }

    func hide(_ ref: PartRef) {
        hiddenParts.insert(ref)
        if selection == ref { selection = nil }
        refresh(ref.system)
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

    // MARK: Camera

    func orbit(by delta: CGSize) {
        tween?.cancel()
        yaw -= Float(delta.width) * 0.008
        pitch = min(max(pitch + Float(delta.height) * 0.006, -1.45), 1.45)
        applyCamera()
    }

    func zoom(by factor: CGFloat) {
        tween?.cancel()
        distance = min(max(distance / Float(factor), 0.12), 5)
        applyCamera()
    }

    func pan(by delta: CGSize, viewHeight: CGFloat) {
        tween?.cancel()
        let worldPerPoint = 2 * distance * tan(fieldOfView * .pi / 360) / Float(max(viewHeight, 1))
        let m = camera.transformMatrix(relativeTo: nil)
        let right = SIMD3(m.columns.0.x, m.columns.0.y, m.columns.0.z)
        let up = SIMD3(m.columns.1.x, m.columns.1.y, m.columns.1.z)
        target -= right * Float(delta.width) * worldPerPoint
        target += up * Float(delta.height) * worldPerPoint
        target = simd_clamp(target, SIMD3(-1.2, -0.4, -1.2), SIMD3(1.2, 2.3, 1.2))
        applyCamera()
    }

    func resetCamera() {
        animateCamera(target: Self.homeTarget, distance: Self.homeDistance, yaw: 0, pitch: 0.05)
    }

    func rotate(toYaw newYaw: Float) {
        animateCamera(target: target, distance: distance, yaw: newYaw, pitch: 0.05)
    }

    /// Moves the camera so that `refs` fill the view.
    func frame(_ refs: [PartRef], margin: Float = 1.15) {
        var lo = SIMD3<Float>(repeating: .greatestFiniteMagnitude)
        var hi = -lo
        for ref in refs {
            guard let info = info(ref) else { continue }
            let b = info.bounds
            lo = simd_min(lo, SIMD3(b[0], b[1], b[2]))
            hi = simd_max(hi, SIMD3(b[3], b[4], b[5]))
        }
        guard lo.x <= hi.x else { return }
        let center = (lo + hi) / 2
        let radius = max(simd_length(hi - lo) / 2, 0.03)
        let fit = radius / sin(fieldOfView * .pi / 360) * margin
        // Look at the part from the side it faces most.
        var newYaw = yaw
        if abs(center.x) > 0.12, abs(center.x) > abs(center.z) * 1.5, radius < 0.25 {
            newYaw = center.x > 0 ? .pi / 3 : -.pi / 3
        } else if center.z < -0.06, radius < 0.25 {
            newYaw = .pi
        } else if abs(remainder(yaw, 2 * .pi)) > .pi / 2 && center.z > 0.02 {
            newYaw = 0
        }
        animateCamera(target: center, distance: min(max(fit, 0.18), 3.2), yaw: newYaw, pitch: 0.08)
    }

    private func animateCamera(target newTarget: SIMD3<Float>, distance newDistance: Float, yaw newYaw: Float, pitch newPitch: Float) {
        tween?.cancel()
        let start = (target, distance, yaw, pitch)
        // Take the short way round.
        var endYaw = newYaw
        while endYaw - start.2 > .pi { endYaw -= 2 * .pi }
        while start.2 - endYaw > .pi { endYaw += 2 * .pi }
        tween = Task { [weak self] in
            let steps = 36
            for step in 1...steps {
                guard let self, !Task.isCancelled else { return }
                let t = Float(step) / Float(steps)
                let e = t < 0.5 ? 4 * t * t * t : 1 - pow(-2 * t + 2, 3) / 2
                self.target = start.0 + (newTarget - start.0) * e
                self.distance = start.1 + (newDistance - start.1) * e
                self.yaw = start.2 + (endYaw - start.2) * e
                self.pitch = start.3 + (newPitch - start.3) * e
                self.applyCamera()
                try? await Task.sleep(for: .milliseconds(12))
            }
        }
    }

    private func applyCamera() {
        let offset = SIMD3<Float>(
            sin(yaw) * cos(pitch),
            sin(pitch),
            cos(yaw) * cos(pitch)
        ) * distance
        camera.look(at: target, from: target + offset, relativeTo: nil)
    }

    // MARK: Picking

    /// Returns the frontmost pickable part under `point` (in view coordinates).
    /// Boxes are tested here; triangles are tested off the main thread, nearest
    /// box first, stopping as soon as no closer hit is possible.
    func pick(at point: CGPoint, in size: CGSize) async -> PartRef? {
        guard size.width > 0, size.height > 0 else { return nil }
        let aspect = Float(size.width / size.height)
        let t = tan(fieldOfView * .pi / 360)
        let x = (2 * Float(point.x / size.width) - 1) * t * aspect
        let y = (1 - 2 * Float(point.y / size.height)) * t
        let m = camera.transformMatrix(relativeTo: nil)
        let local = simd_normalize(SIMD3<Float>(x, y, -1))
        let dir4 = m * SIMD4(local, 0)
        let direction = simd_normalize(SIMD3(dir4.x, dir4.y, dir4.z))
        let origin = SIMD3(m.columns.3.x, m.columns.3.y, m.columns.3.z)

        struct Candidate: Sendable {
            let ref: PartRef
            let entry: Float
            let ghost: Bool
        }
        var candidates: [Candidate] = []
        var packs: [String: MeshPack] = [:]
        for (id, system) in systems where enabledLayers.contains(id) {
            packs[id] = system.pack
            for i in system.pack.parts.indices {
                let ref = PartRef(system: id, index: i)
                let state = state(of: ref)
                if state == .hidden { continue }
                if let entry = Self.rayBox(origin, direction, system.bounds[i]) {
                    candidates.append(Candidate(ref: ref, entry: entry, ghost: state == .ghost))
                }
            }
        }
        guard !candidates.isEmpty else { return nil }
        candidates.sort { $0.entry < $1.entry }

        return await Task.detached(priority: .userInitiated) {
            // Ghosted parts are see-through, so they only win when nothing solid is hit.
            var best: (Float, PartRef)?
            var bestGhost: (Float, PartRef)?
            for c in candidates {
                // Sorted by box entry: nothing after this can be closer than a solid hit.
                if let solid = best, c.entry >= solid.0 { break }
                let limit = c.ghost ? (bestGhost?.0 ?? .infinity) : (best?.0 ?? .infinity)
                if c.entry >= limit { continue }
                guard let pack = packs[c.ref.system] else { continue }
                if let hit = Self.rayMesh(origin, direction, pack: pack, part: c.ref.index, limit: limit) {
                    if c.ghost { bestGhost = (hit, c.ref) } else { best = (hit, c.ref) }
                }
            }
            return best?.1 ?? bestGhost?.1
        }.value
    }

    nonisolated private static func rayBox(_ o: SIMD3<Float>, _ d: SIMD3<Float>, _ box: BoundingBox) -> Float? {
        let inv = SIMD3<Float>(1 / d.x, 1 / d.y, 1 / d.z)
        let t0 = (box.min - o) * inv
        let t1 = (box.max - o) * inv
        let tmin = simd_reduce_max(simd_min(t0, t1))
        let tmax = simd_reduce_min(simd_max(t0, t1))
        guard tmax >= max(tmin, 0) else { return nil }
        return max(tmin, 0)
    }

    nonisolated private static func rayMesh(_ o: SIMD3<Float>, _ d: SIMD3<Float>, pack: MeshPack, part: Int, limit: Float) -> Float? {
        let range = pack.ranges[part]
        var best = limit
        var found = false
        pack.positions.withUnsafeBufferPointer { pos in
            pack.indices.withUnsafeBufferPointer { idx in
                var i = range.indexStart
                let end = range.indexStart + range.indexCount
                while i < end {
                    let a = pos[Int(idx[i])], b = pos[Int(idx[i + 1])], c = pos[Int(idx[i + 2])]
                    i += 3
                    let e1 = b - a, e2 = c - a
                    let p = simd_cross(d, e2)
                    let det = simd_dot(e1, p)
                    if abs(det) < 1e-12 { continue }
                    let invDet = 1 / det
                    let s = o - a
                    let u = simd_dot(s, p) * invDet
                    if u < 0 || u > 1 { continue }
                    let q = simd_cross(s, e1)
                    let v = simd_dot(d, q) * invDet
                    if v < 0 || u + v > 1 { continue }
                    let t = simd_dot(e2, q) * invDet
                    if t > 0.0005 && t < best {
                        best = t
                        found = true
                    }
                }
            }
        }
        return found ? best : nil
    }

    // MARK: Materials & lighting

    private static func solidMaterial(hex: String, roughness: Float) -> PhysicallyBasedMaterial {
        var m = PhysicallyBasedMaterial()
        m.baseColor = .init(tint: UIColor(Color(hex: hex)))
        m.roughness = .init(floatLiteral: roughness)
        m.metallic = .init(floatLiteral: 0)
        m.specular = .init(floatLiteral: 0.22)
        m.clearcoat = .init(floatLiteral: roughness < 0.5 ? 0.08 : 0)
        m.faceCulling = .none
        return m
    }

    private static func ghostMaterial(hex: String) -> PhysicallyBasedMaterial {
        var m = PhysicallyBasedMaterial()
        m.baseColor = .init(tint: UIColor(Color(hex: hex)))
        m.roughness = .init(floatLiteral: 0.5)
        m.metallic = .init(floatLiteral: 0)
        m.blending = .transparent(opacity: .init(floatLiteral: 0.13))
        m.writesDepth = false
        m.faceCulling = .back
        return m
    }

    private static func selectionMaterial() -> PhysicallyBasedMaterial {
        var m = PhysicallyBasedMaterial()
        m.baseColor = .init(tint: UIColor(red: 0.16, green: 0.72, blue: 1, alpha: 1))
        m.emissiveColor = .init(color: UIColor(red: 0.05, green: 0.42, blue: 0.75, alpha: 1))
        m.emissiveIntensity = 0.7
        m.roughness = .init(floatLiteral: 0.35)
        m.metallic = .init(floatLiteral: 0)
        m.faceCulling = .none
        return m
    }

    private static func highlightMaterial() -> PhysicallyBasedMaterial {
        var m = PhysicallyBasedMaterial()
        m.baseColor = .init(tint: UIColor(red: 1, green: 0.78, blue: 0.18, alpha: 1))
        m.emissiveColor = .init(color: UIColor(red: 0.7, green: 0.45, blue: 0.0, alpha: 1))
        m.emissiveIntensity = 0.6
        m.roughness = .init(floatLiteral: 0.4)
        m.metallic = .init(floatLiteral: 0)
        m.faceCulling = .none
        return m
    }

    private func setupLighting() {
        Task { [weak self] in
            guard let image = Self.environmentImage() else { return }
            let options = EnvironmentResource.CreateOptions(samplingQuality: .fast, specularCubeDimension: 64)
            guard let environment = try? await EnvironmentResource(equirectangular: image, options: options),
                  let self else { return }
            let ibl = Entity()
            ibl.components.set(ImageBasedLightComponent(source: .single(environment), intensityExponent: -0.4))
            self.root.addChild(ibl)
            self.iblEntity = ibl
            for system in self.systems.values {
                system.entity.components.set(ImageBasedLightReceiverComponent(imageBasedLight: ibl))
            }
        }
    }

    /// A soft studio gradient used as image based lighting.
    private static func environmentImage() -> CGImage? {
        let width = 128, height = 64
        let renderer = UIGraphicsImageRenderer(size: CGSize(width: width, height: height), format: {
            let f = UIGraphicsImageRendererFormat()
            f.scale = 1
            return f
        }())
        let image = renderer.image { ctx in
            let colors = [
                UIColor(white: 1.0, alpha: 1).cgColor,
                UIColor(white: 0.86, alpha: 1).cgColor,
                UIColor(red: 0.55, green: 0.52, blue: 0.5, alpha: 1).cgColor,
                UIColor(white: 0.22, alpha: 1).cgColor,
            ]
            let gradient = CGGradient(colorsSpace: CGColorSpaceCreateDeviceRGB(), colors: colors as CFArray, locations: [0, 0.42, 0.55, 1])!
            ctx.cgContext.drawLinearGradient(gradient, start: .zero, end: CGPoint(x: 0, y: height), options: [])
            // A brighter key area in front of the body.
            ctx.cgContext.setFillColor(UIColor(white: 1, alpha: 0.6).cgColor)
            ctx.cgContext.fillEllipse(in: CGRect(x: width / 2 - 18, y: 8, width: 36, height: 22))
        }
        return image.cgImage
    }
}
