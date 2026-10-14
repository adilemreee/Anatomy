//
//  SpecimenScene.swift
//  Anatomy
//
//  A structure on its own, on a dark stage, with Z-Anatomy's feature labels
//  (e.g. "Caput ossis femoris" on the femur). Only the requested parts are
//  uploaded, so it opens quickly next to the main atlas.
//

import RealityKit
import SwiftUI

/// Feature labels exported by tools/export_labels.py.
@MainActor
final class FeatureLibrary {
    static let shared = FeatureLibrary()

    nonisolated struct Feature: Hashable, Sendable {
        enum Kind: Hashable, Sendable {
            /// A Z-Anatomy feature label ("Head of femur").
            case feature
            /// One part of a structure made of several (a head of a muscle).
            case part
            /// Where a muscle arises / attaches; `name` is the bone.
            case origin, insertion
        }

        let name: String
        let anchor: SIMD3<Float>
        let tip: SIMD3<Float>
        var kind: Kind = .feature
        /// The part the feature lies on (set by the specimen scene).
        var part: PartRef?
    }

    private let byOwner: [String: [Feature]]

    private init() {
        struct File: Decodable {
            struct Label: Decodable {
                let name: String
                let owner: String
                let anchor: [Float]
                let tip: [Float]
            }
            let labels: [Label]
        }
        var map: [String: [Feature]] = [:]
        if let url = Bundle.main.url(forResource: "labels", withExtension: "json"),
           let data = try? Data(contentsOf: url),
           let file = try? JSONDecoder().decode(File.self, from: data) {
            for label in file.labels where label.anchor.count == 3 && label.tip.count == 3 {
                // "(Third trochanter)": Z-Anatomy brackets features that are not always present.
                var name = label.name.trimmingCharacters(in: .whitespaces)
                if name.hasPrefix("("), name.hasSuffix(")") { name = String(name.dropFirst().dropLast()) }
                let feature = Feature(name: name,
                                      anchor: SIMD3(label.anchor[0], label.anchor[1], label.anchor[2]),
                                      tip: SIMD3(label.tip[0], label.tip[1], label.tip[2]))
                map[label.owner, default: []].append(feature)
            }
        }
        byOwner = map
    }

    /// Labels for a part; parts that only have labels on the other side of the
    /// body get the mirrored set.
    func features(for part: PartInfo) -> [Feature] {
        if let own = byOwner[part.name] { return own }
        let mirrored: String
        if part.name.hasSuffix(".l") { mirrored = String(part.name.dropLast(2)) + ".r" }
        else if part.name.hasSuffix(".r") { mirrored = String(part.name.dropLast(2)) + ".l" }
        else { return [] }
        return (byOwner[mirrored] ?? []).map {
            Feature(name: $0.name, anchor: $0.anchor * SIMD3(-1, 1, 1), tip: $0.tip * SIMD3(-1, 1, 1), kind: $0.kind)
        }
    }

    func hasFeatures(_ part: PartInfo) -> Bool { !features(for: part).isEmpty }
}

@MainActor
@Observable
final class SpecimenScene: ViewportScene {
    /// A placed label: title, the pinned point and the box it is drawn in.
    nonisolated struct Label: Identifiable, Hashable, Sendable {
        let id: Int
        let name: String
        let title: String
        let subtitle: String?
        let anchor: CGPoint
        let box: CGRect
        let kind: FeatureLibrary.Feature.Kind

        /// Where the leader line meets the box: the middle of the side that
        /// faces the anchor.
        var attach: CGPoint {
            if anchor.x < box.minX || anchor.x > box.maxX {
                return CGPoint(x: anchor.x < box.minX ? box.minX : box.maxX,
                               y: min(max(anchor.y, box.minY + 10), box.maxY - 10))
            }
            return CGPoint(x: min(max(anchor.x, box.minX + 14), box.maxX - 14),
                           y: anchor.y < box.midY ? box.minY : box.maxY)
        }
    }

    private(set) var isReady = false
    private(set) var cameraVersion = 0
    private(set) var isCameraMoving = false
    private(set) var featureCount = 0
    private(set) var hasAttachments = false
    /// The feature whose region is coloured on the model.
    private(set) var highlightedFeature: Int?

    @ObservationIgnored let root = Entity()
    @ObservationIgnored private let camera = Entity()
    @ObservationIgnored private var features: [FeatureLibrary.Feature] = []
    @ObservationIgnored private var positions: [SIMD3<Float>] = []
    @ObservationIgnored private var indices: [UInt32] = []
    @ObservationIgnored private var tween: CameraTween?
    @ObservationIgnored private var yaw: Float = 0
    @ObservationIgnored private var pitch: Float = 0.08
    @ObservationIgnored private var distance: Float = 0.6
    @ObservationIgnored private var target = SIMD3<Float>(0, 1, 0)
    @ObservationIgnored private var home: (SIMD3<Float>, Float, Float) = (.zero, 0.6, 0)
    @ObservationIgnored private var homePitch: Float = 0.08
    /// Triangle ranges of the test mesh per part, with bounds, for culling rays.
    @ObservationIgnored private var partTriangles: [(range: Range<Int>, lo: SIMD3<Float>, hi: SIMD3<Float>)] = []
    /// Per entry of `partTriangles`: whether it is a muscle. Attachment pins
    /// lie under their muscle, so muscles do not hide them.
    @ObservationIgnored private var partIsMuscle: [Bool] = []
    @ObservationIgnored private let fieldOfView: Float = 32
    @ObservationIgnored private var bounds: (SIMD3<Float>, SIMD3<Float>) = (.zero, .zero)
    @ObservationIgnored private var ownerNames: Set<String> = []
    @ObservationIgnored private var aspect: Float = 0.46
    /// The drawn mesh, kept on the CPU to cut highlight patches from it.
    @ObservationIgnored private var displayVertices = Data()
    @ObservationIgnored private var displayIndices: [UInt32] = []
    /// Index range of every studied part inside `displayIndices`.
    @ObservationIgnored private var displayRanges: [PartRef: Range<Int>] = [:]
    @ObservationIgnored private var spot: ModelEntity?
    @ObservationIgnored private var spotTask: Task<Void, Never>?

    init() {
        camera.components.set(PerspectiveCameraComponent(near: 0.005, far: 20, fieldOfViewInDegrees: fieldOfView, fieldOfViewOrientation: .vertical))
        for light in AnatomyMaterials.cameraLights() { camera.addChild(light) }
        root.addChild(camera)
    }

    /// Loads `refs` (framed and labelled) and `context` (shown around them).
    func load(refs: [PartRef], context: [PartRef] = [], mode: ColorMode) async {
        let library = PackLibrary.shared
        let focus = Set(refs)
        let all = refs + context.filter { !focus.contains($0) }
        var vertexData = Data()
        var drawIndices: [UInt32] = []
        var allIndices: [UInt32] = []
        var allPositions: [SIMD3<Float>] = []
        var allNormals: [SIMD3<Float>] = []
        var lo = SIMD3<Float>(repeating: .greatestFiniteMagnitude), hi = -lo
        var collected: [FeatureLibrary.Feature] = []
        var structures: [(name: String, span: Range<Int>, ref: PartRef)] = []
        var attachments: [(bone: String, origin: Bool, span: Range<Int>)] = []

        for system in Set(all.map(\.system)).sorted() {
            guard let pack = try? await library.pack(system) else { continue }
            let partIndices = all.filter { $0.system == system }.map(\.index).sorted()
            // Drawn from the high-detail mesh where there is one (BodyParts3D),
            // otherwise from the atlas pack.
            let drawn = await Task.detached(priority: .userInitiated) { () -> (Data, [UInt32], [Int: Range<Int>]) in
                var data = Data(), idx: [UInt32] = [], plain: [Int] = [], ranges: [Int: Range<Int>] = [:]
                func add(_ output: VertexBuilder.Output) -> Int {
                    let base = UInt32(data.count / VertexBuilder.stride)
                    let start = idx.count
                    data.append(output.vertices)
                    idx.append(contentsOf: output.indices.map { $0 + base })
                    return start
                }
                for p in partIndices {
                    if let detail = DetailLibrary.shared.pack(system: system, index: p) {
                        let start = add(VertexBuilder.build(pack: detail, parts: [0], mode: mode))
                        ranges[p] = start..<idx.count
                    } else {
                        plain.append(p)
                    }
                }
                if !plain.isEmpty {
                    let output = VertexBuilder.build(pack: pack, parts: plain, mode: mode)
                    let start = add(output)
                    for (k, p) in plain.enumerated() where output.ranges.indices.contains(k) {
                        let r = output.ranges[k]
                        ranges[p] = start + r.start..<start + r.start + r.count
                    }
                }
                return (data, idx, ranges)
            }.value
            let drawBase = UInt32(vertexData.count / VertexBuilder.stride)
            let indexBase = drawIndices.count
            vertexData.append(drawn.0)
            drawIndices.append(contentsOf: drawn.1.map { $0 + drawBase })
            for (p, r) in drawn.2 where focus.contains(PartRef(system: system, index: p)) {
                displayRanges[PartRef(system: system, index: p)] = indexBase + r.lowerBound..<indexBase + r.upperBound
            }
            // Picking, label visibility and pins use the lighter atlas mesh.
            for p in partIndices {
                let r = pack.ranges[p]
                let span = allPositions.count..<allPositions.count + r.vertexCount
                let shift = Int64(span.lowerBound) - Int64(r.vertexStart)
                let triangleStart = allIndices.count
                allIndices.append(contentsOf: pack.indices[r.indexStart..<r.indexStart + r.indexCount].map { UInt32(Int64($0) + shift) })
                let pb = pack.parts[p].bounds
                partTriangles.append((triangleStart..<allIndices.count, SIMD3(pb[0], pb[1], pb[2]) - 0.001, SIMD3(pb[3], pb[4], pb[5]) + 0.001))
                partIsMuscle.append(system == "muscular")
                allPositions.append(contentsOf: pack.positions[r.vertexStart..<r.vertexStart + r.vertexCount])
                allNormals.append(contentsOf: pack.normals[r.vertexStart..<r.vertexStart + r.vertexCount])
                guard focus.contains(PartRef(system: system, index: p)) else { continue }
                let info = pack.parts[p]
                let b = info.bounds
                lo = simd_min(lo, SIMD3(b[0], b[1], b[2]))
                hi = simd_max(hi, SIMD3(b[3], b[4], b[5]))
                if system == "insertions" {
                    let material = info.dominantMaterial.flatMap { pack.materials.indices.contains($0) ? pack.materials[$0] : nil } ?? ""
                    attachments.append((info.path.last ?? info.base, MaterialStyles.isOrigin(info, material: material), span))
                } else {
                    let ref = PartRef(system: system, index: p)
                    collected += FeatureLibrary.shared.features(for: info).map { feature in
                        var feature = feature
                        feature.part = ref
                        return feature
                    }
                    ownerNames.insert(info.base.lowercased())
                    structures.append((Self.plainName(info.base), span, ref))
                }
            }
        }
        guard !drawIndices.isEmpty, !allIndices.isEmpty else { return }
        // Shown right away as is; the smoothly subdivided version replaces it
        // once it has been built in the background.
        let box = BoundingBox(min: lo, max: hi)
        guard let resource = try? await Self.meshResource(vertices: vertexData, indices: drawIndices, bounds: box) else { return }
        let entity = ModelEntity(mesh: resource, materials: await AnatomyMaterials.shared(occlusion: 0.28, rim: 0.7))
        root.addChild(entity)
        positions = allPositions
        indices = allIndices
        displayVertices = vertexData
        displayIndices = drawIndices

        bounds = (lo, hi)
        let center = (lo + hi) / 2
        let fit = fitDistance()
        // Open on the view that shows most of the structure: candidates around
        // it, level and from above, scored by the visible surface facing the
        // camera. Side structures start turned a little towards their own
        // side; the anatomical front view wins when views are about as good.
        let sideYaw: Float = center.x > 0.1 ? 0.6 : (center.x < -0.1 ? -0.6 : 0)
        var candidates: [(yaw: Float, pitch: Float, bias: Float)] = [(sideYaw, 0.08, 1.15), (.pi - sideYaw, 0.08, 1)]
        for k in 0..<8 {
            candidates.append((Float(k) * .pi / 4, 0.08, 1))
            candidates.append((Float(k) * .pi / 4, 0.7, 0.95))
        }
        candidates.append((sideYaw, 1.3, 0.92))
        let samples = structures.flatMap { s in stride(from: s.span.lowerBound, to: s.span.upperBound, by: max(s.span.count / max(140 / max(structures.count, 1), 1), 1)) }
        let pts = allPositions, nrm = allNormals, idx = allIndices, boxes = partTriangles
        let view = await Task.detached(priority: .userInitiated) { () -> (yaw: Float, pitch: Float) in
            var best: (score: Float, yaw: Float, pitch: Float) = (-1, sideYaw, 0.08)
            for c in candidates {
                let eye = center + SIMD3(sin(c.yaw) * cos(c.pitch), sin(c.pitch), cos(c.yaw) * cos(c.pitch)) * fit
                var score: Float = 0
                for i in samples {
                    let toV = pts[i] - eye, d = simd_length(toV), dir = toV / d
                    let facing = simd_dot(nrm[i], -dir)
                    guard facing > 0.05 else { continue }
                    if Self.blocked(eye, dir, before: d - 0.003, parts: boxes, positions: pts, indices: idx) { continue }
                    score += facing
                }
                score *= c.bias
                if score > best.score { best = (score, c.yaw, c.pitch) }
            }
            return (best.yaw, best.pitch)
        }.value
        let startYaw = view.yaw
        pitch = view.pitch

        // Labels for the heads of a muscle and for where it attaches, pinned
        // on a point that can be seen from the opening view. Every
        // attachment patch gets a pin; the labels keep one per bone.
        let facing = SIMD3<Float>(sin(startYaw) * cos(pitch), sin(pitch), cos(startYaw) * cos(pitch))
        let eye = center + facing * fit
        let muscles = partIsMuscle
        let heads = (2...10).contains(structures.count) ? structures : []
        let headSpans = heads.map(\.span), patchSpans = attachments.map(\.span)
        let pins = await Task.detached(priority: .userInitiated) { () -> (parts: [(SIMD3<Float>, SIMD3<Float>)], attachments: [(SIMD3<Float>, SIMD3<Float>)]) in
            let bones = boxes.enumerated().filter { !muscles[$0.offset] }.map(\.element)
            let parts = headSpans.map { Self.visiblePoint(positions: pts, normals: nrm, span: $0, facing: facing, eye: eye,
                                                           occluders: boxes, indices: idx) }
            let patches = patchSpans.map { Self.visiblePoint(positions: pts, normals: nrm, span: $0, facing: facing, eye: eye,
                                                            occluders: bones, indices: idx) }
            return (parts, patches)
        }.value
        for (s, (p, n)) in zip(heads, pins.parts) {
            collected.append(.init(name: s.name, anchor: p, tip: p + n * 0.03, kind: .part, part: s.ref))
        }
        for (a, (p, n)) in zip(attachments, pins.attachments) {
            collected.append(.init(name: a.bone, anchor: p, tip: p + n * 0.03, kind: a.origin ? .origin : .insertion))
        }
        features = collected
        featureCount = collected.count
        hasAttachments = !attachments.isEmpty
        home = (center, fit, startYaw)
        homePitch = view.pitch
        target = center
        distance = fit
        yaw = startYaw
        applyCamera()
        isReady = true
        cameraDidSettle()

        if let environment = await AnatomyMaterials.environment() {
            let ibl = Entity()
            ibl.components.set(ImageBasedLightComponent(source: .single(environment), intensityExponent: 0.25))
            root.addChild(ibl)
            entity.components.set(ImageBasedLightReceiverComponent(imageBasedLight: ibl))
        }

        // Light meshes get two levels of curved subdivision, dense ones one;
        // the total stays within what an older phone draws smoothly.
        let triangles = drawIndices.count / 3
        let levels = triangles > 90_000 ? 1 : 2
        let source = (vertexData, drawIndices)
        let (smoothVertices, smoothIndices) = await Task.detached(priority: .userInitiated) {
            Tessellator.smooth(vertices: source.0, indices: source.1, maxTriangles: 420_000, levels: levels)
        }.value
        guard !Task.isCancelled, smoothIndices.count > drawIndices.count,
              let smooth = try? await Self.meshResource(vertices: smoothVertices, indices: smoothIndices, bounds: box) else { return }
        entity.model?.mesh = smooth
        // Every triangle became `factor` consecutive ones: scale the ranges.
        let factor = smoothIndices.count / drawIndices.count
        displayRanges = displayRanges.mapValues { $0.lowerBound * factor..<$0.upperBound * factor }
        displayVertices = smoothVertices
        displayIndices = smoothIndices
        if let feature = highlightedFeature { highlight(feature: feature) }
    }

    private static func meshResource(vertices: Data, indices: [UInt32], bounds: BoundingBox) async throws -> MeshResource {
        let mesh = try AnatomyScene.makeMesh(vertexCount: vertices.count / VertexBuilder.stride, indexCount: indices.count)
        AnatomyScene.upload(VertexBuilder.Output(vertices: vertices, indices: indices, ranges: [], bounds: []), into: mesh)
        mesh.parts.replaceAll([LowLevelMesh.Part(indexCount: indices.count, topology: .triangle, materialIndex: 0, bounds: bounds)])
        return try await MeshResource(from: mesh)
    }

    // MARK: Highlight

    /// Feature names, kinds and owners for the list of features.
    var allFeatures: [FeatureLibrary.Feature] { features }

    /// Colours the region of a feature on the model: a soft patch around
    /// the point for features and attachments, the whole part for the parts
    /// of a structure (a head of a muscle, a liver segment). nil clears it.
    func highlight(feature index: Int?) {
        highlightedFeature = index
        spotTask?.cancel()
        guard let index, features.indices.contains(index), !displayIndices.isEmpty else {
            spot?.removeFromParent()
            spot = nil
            return
        }
        let feature = features[index]
        let all = Array(displayRanges.values)
        let own = feature.part.flatMap { displayRanges[$0] }.map { [$0] }
        let ranges: [Range<Int>]
        let radius: Float
        switch feature.kind {
        case .part:
            ranges = own ?? all
            radius = .infinity
        case .feature:
            ranges = own ?? all
            radius = spotRadius(for: index)
        case .origin, .insertion:
            // Only the attachment patches, not the muscle lying over them.
            let patches = displayRanges.filter { $0.key.system == "insertions" }.map(\.value)
            ranges = patches.isEmpty ? all : patches
            radius = spotRadius(for: index) * 1.6
        }
        let vertices = displayVertices, indices = displayIndices, center = feature.anchor
        let lift = max(simd_length(bounds.1 - bounds.0) * 0.0012, 0.00004)
        spotTask = Task { [weak self] in
            let patch = await Task.detached(priority: .userInitiated) {
                Self.spotMesh(vertices: vertices, indices: indices, ranges: ranges, center: center, radius: radius, lift: lift)
            }.value
            guard let self, !Task.isCancelled, self.highlightedFeature == index, let patch,
                  let resource = try? await Self.meshResource(vertices: patch.vertices, indices: patch.indices,
                                                              bounds: BoundingBox(min: patch.lo, max: patch.hi)) else { return }
            let material = await AnatomyMaterials.spot()
            guard !Task.isCancelled, self.highlightedFeature == index else { return }
            let entity = ModelEntity(mesh: resource, materials: [material])
            self.spot?.removeFromParent()
            self.root.addChild(entity)
            self.spot = entity
        }
    }

    /// Half the distance to the nearest other feature on the same part,
    /// within sensible bounds for the size of the structure.
    private func spotRadius(for index: Int) -> Float {
        let feature = features[index]
        let size = max(simd_length(bounds.1 - bounds.0), 0.005)
        var nearest = Float.infinity
        for (i, other) in features.enumerated() where i != index && other.part == feature.part && other.kind == .feature {
            nearest = min(nearest, simd_distance(other.anchor, feature.anchor))
        }
        let guess = nearest.isFinite ? nearest * 0.6 : size * 0.08
        return min(max(guess, size * 0.03), size * 0.14)
    }

    /// The triangles of `ranges` near `center`, lifted a little off the
    /// surface, coloured with fading opacity towards the edge.
    nonisolated private static func spotMesh(vertices: Data, indices: [UInt32], ranges: [Range<Int>], center: SIMD3<Float>,
                                             radius: Float, lift: Float) -> (vertices: Data, indices: [UInt32], lo: SIMD3<Float>, hi: SIMD3<Float>)? {
        let stride = VertexBuilder.stride
        typealias O = VertexBuilder.Offset
        var remap: [UInt32: UInt32] = [:]
        var out = Data()
        var outIndices: [UInt32] = []
        var lo = SIMD3<Float>(repeating: .greatestFiniteMagnitude), hi = -lo
        vertices.withUnsafeBytes { raw in
            guard let base = raw.baseAddress else { return }
            func position(_ v: UInt32) -> SIMD3<Float> { VertexBuilder.loadPosition(base, Int(v) * stride) }
            for range in ranges {
                var t = range.lowerBound
                while t + 2 < range.upperBound, t + 2 < indices.count {
                    let tri = (indices[t], indices[t + 1], indices[t + 2])
                    t += 3
                    if radius.isFinite {
                        let d = min(simd_distance(position(tri.0), center), simd_distance(position(tri.1), center), simd_distance(position(tri.2), center))
                        if d > radius { continue }
                    }
                    for v in [tri.0, tri.1, tri.2] {
                        if let m = remap[v] {
                            outIndices.append(m)
                            continue
                        }
                        let m = UInt32(out.count / stride)
                        remap[v] = m
                        var bytes = [UInt8](repeating: 0, count: stride)
                        bytes.withUnsafeMutableBytes { dst in
                            guard let d = dst.baseAddress else { return }
                            d.copyMemory(from: base + Int(v) * stride, byteCount: stride)
                            let normal = VertexBuilder.loadSigned(d, O.normal)
                            let p = VertexBuilder.loadPosition(d, 0) + SIMD3(normal.x, normal.y, normal.z) * lift
                            VertexBuilder.storePosition(p, d, 0)
                            let distance = simd_distance(p, center)
                            var strength: Float = 1
                            if radius.isFinite {
                                let x = min(max((distance - radius * 0.45) / (radius * 0.55), 0), 1)
                                strength = 1 - x * x * (3 - 2 * x)
                            }
                            VertexBuilder.storeUnsigned(SIMD4(0.08, 0.62, 1, strength), d, O.color)
                            lo = simd_min(lo, p)
                            hi = simd_max(hi, p)
                        }
                        out.append(contentsOf: bytes)
                        outIndices.append(m)
                    }
                }
            }
        }
        return outIndices.isEmpty ? nil : (out, outIndices, lo, hi)
    }

    /// Turns the camera towards a feature so its coloured region faces the
    /// viewer; `zoom` also comes much closer.
    func focus(feature index: Int, zoom: Bool = true) {
        guard features.indices.contains(index) else { return }
        let feature = features[index]
        let center = (bounds.0 + bounds.1) / 2
        var outward = feature.tip - feature.anchor
        if simd_length(outward) < 1e-5 { outward = feature.anchor - center }
        outward = simd_normalize(simd_normalize(outward) * 0.7 + simd_normalize(feature.anchor - center + 1e-5) * 0.3)
        let newYaw = atan2(outward.x, outward.z)
        let newPitch = min(max(asin(min(max(outward.y, -1), 1)), -1.2), 1.2)
        let newTarget = center + (feature.anchor - center) * (zoom ? 0.75 : 0.35)
        let newDistance = zoom ? home.1 * (feature.kind == .part ? 0.8 : 0.55) : min(distance, home.1)
        animate(target: newTarget, distance: newDistance, yaw: newYaw, pitch: newPitch)
    }

    private func animate(target newTarget: SIMD3<Float>, distance newDistance: Float, yaw newYaw: Float, pitch newPitch: Float) {
        tween?.cancel()
        isCameraMoving = true
        let start = (target, distance, yaw, pitch)
        var end = newYaw
        while end - start.2 > .pi { end -= 2 * .pi }
        while start.2 - end > .pi { end += 2 * .pi }
        tween = CameraTween(duration: 0.55) { [weak self] e in
            guard let self else { return }
            self.target = start.0 + (newTarget - start.0) * e
            self.distance = start.1 + (newDistance - start.1) * e
            self.yaw = start.2 + (end - start.2) * e
            self.pitch = start.3 + (newPitch - start.3) * e
            self.applyCamera()
        } completion: { [weak self] in
            self?.cameraDidSettle()
        }
    }

    // MARK: Camera

    /// Updates the framing for a new viewport size.
    func setViewSize(_ size: CGSize) {
        guard size.width > 0, size.height > 0 else { return }
        let newAspect = Float(size.width / size.height)
        guard abs(newAspect - aspect) > 0.01 else { return }
        aspect = newAspect
        guard isReady else { return }
        let fit = fitDistance()
        let wasHome = abs(distance - home.1) < 0.0001
        home.1 = fit
        if wasHome {
            distance = fit
            applyCamera()
            cameraDidSettle()
        }
    }

    /// Distance at which the bounding sphere fits the view, leaving room for
    /// the header and controls vertically and the labels horizontally.
    private func fitDistance() -> Float {
        let radius = max(simd_length(bounds.1 - bounds.0) / 2, 0.01)
        let halfV = fieldOfView * .pi / 360
        let halfH = atan(tan(halfV) * aspect)
        return max(radius / sin(halfV) * 1.2, radius / sin(halfH) * 1.0)
    }

    func orbit(by delta: CGSize) {
        yaw -= Float(delta.width) * 0.009
        pitch = min(max(pitch + Float(delta.height) * 0.007, -1.5), 1.5)
        applyCamera()
    }

    func zoom(by factor: CGFloat) {
        distance = min(max(distance / Float(factor), home.1 * 0.25), home.1 * 3)
        applyCamera()
    }

    func pan(by delta: CGSize, viewHeight: CGFloat) {
        let worldPerPoint = 2 * distance * tan(fieldOfView * .pi / 360) / Float(max(viewHeight, 1))
        let m = camera.transformMatrix(relativeTo: nil)
        target -= SIMD3(m.columns.0.x, m.columns.0.y, m.columns.0.z) * Float(delta.width) * worldPerPoint
        target += SIMD3(m.columns.1.x, m.columns.1.y, m.columns.1.z) * Float(delta.height) * worldPerPoint
        applyCamera()
    }

    func beginCameraInteraction() {
        tween?.cancel()
        isCameraMoving = true
    }

    func cameraDidSettle() {
        isCameraMoving = false
        cameraVersion += 1
    }

    /// Turns to a preset view of the body (0 front, .pi/2 from the left, .pi back).
    func turn(to newYaw: Float) {
        tween?.cancel()
        isCameraMoving = true
        let start = (target, distance, yaw, pitch)
        var end = newYaw
        while end - start.2 > .pi { end -= 2 * .pi }
        while start.2 - end > .pi { end += 2 * .pi }
        tween = CameraTween(duration: 0.5) { [weak self] e in
            guard let self else { return }
            self.target = start.0 + (self.home.0 - start.0) * e
            self.distance = start.1 + (self.home.1 - start.1) * e
            self.yaw = start.2 + (end - start.2) * e
            self.pitch = start.3 + (0.08 - start.3) * e
            self.applyCamera()
        } completion: { [weak self] in
            self?.cameraDidSettle()
        }
    }

    private func applyCamera() {
        let offset = SIMD3<Float>(sin(yaw) * cos(pitch), sin(pitch), cos(yaw) * cos(pitch)) * distance
        camera.look(at: target, from: target + offset, relativeTo: nil)
    }

    /// The feature nearest a tap on the model (nil for empty space), and a
    /// counter so the view notices repeated taps.
    private(set) var tappedFeature: Int?
    private(set) var tapVersion = 0

    /// Taps select the nearest visible feature pin instead of a part.
    func pick(at point: CGPoint, in size: CGSize) async -> PartRef? {
        let eye = camera.position(relativeTo: nil)
        let candidates = features.enumerated().compactMap { i, f -> (Int, CGFloat, SIMD3<Float>)? in
            guard let p = project(f.anchor, in: size) else { return nil }
            let d = hypot(p.x - point.x, p.y - point.y)
            return d < 48 ? (i, d, f.anchor) : nil
        }.sorted { $0.1 < $1.1 }.prefix(4)
        let positions = self.positions, indices = self.indices, boxes = partTriangles
        let hit = await Task.detached(priority: .userInitiated) { () -> Int? in
            for (i, _, anchor) in candidates {
                let toAnchor = anchor - eye
                let d = simd_length(toAnchor)
                if !Self.blocked(eye, toAnchor / d, before: d - 0.006, parts: boxes, positions: positions, indices: indices) { return i }
            }
            return nil
        }.value
        tappedFeature = hit
        tapVersion += 1
        return nil
    }

    // MARK: Labels

    private func project(_ p: SIMD3<Float>, in size: CGSize) -> CGPoint? {
        let c = camera.transformMatrix(relativeTo: nil).inverse * SIMD4(p, 1)
        guard c.z < -0.001 else { return nil }
        let t = tan(fieldOfView * .pi / 360)
        let nx = c.x / (-c.z * t * Float(size.width / size.height))
        let ny = c.y / (-c.z * t)
        return CGPoint(x: CGFloat((nx + 1) / 2) * size.width, y: CGFloat((1 - ny) / 2) * size.height)
    }

    /// Visible features as floating labels. Each label starts out in the
    /// direction of Z-Anatomy's own leader line and is then pushed apart from
    /// the others and from every pinned point.
    /// `top` and `bottom` are the free band between the header and the controls.
    func labels(in size: CGSize, top: CGFloat, bottom: CGFloat, names: (String) -> (tr: String?, la: String?)) async -> [Label] {
        guard size.width > 0, bottom - top > 120, !features.isEmpty else { return [] }
        let safe = CGRect(x: 8, y: top, width: size.width - 16, height: bottom - top)
        let eye = camera.position(relativeTo: nil)
        let positions = self.positions, indices = self.indices, boxes = partTriangles
        let bones = partTriangles.enumerated().filter { !partIsMuscle[$0.offset] }.map(\.element)
        let candidates: [(Int, FeatureLibrary.Feature, CGPoint)] = features.enumerated().compactMap { i, f in
            guard f.kind != .feature || !ownerNames.contains(f.name.lowercased()),
                  let p = project(f.anchor, in: size), safe.insetBy(dx: 12, dy: 0).contains(p) else { return nil }
            return (i, f, p)
        }
        let open = await Task.detached(priority: .userInitiated) { () -> [Bool] in
            candidates.map { _, f, _ in
                let toAnchor = f.anchor - eye
                let d = simd_length(toAnchor)
                // Attachments lie under their own muscle: only bones hide them.
                let attachment = f.kind == .origin || f.kind == .insertion
                return !Self.blocked(eye, toAnchor / d, before: d - (attachment ? 0.006 : 0.004),
                                     parts: attachment ? bones : boxes, positions: positions, indices: indices)
            }
        }.value
        var visible = candidates.enumerated().filter { open[$0.offset] }.map(\.element)

        // Prefer features near the middle, but keep the pins spread out.
        let center = project((bounds.0 + bounds.1) / 2, in: size) ?? CGPoint(x: size.width / 2, y: size.height / 2)
        func rank(_ f: FeatureLibrary.Feature) -> Int { f.kind == .feature ? 1 : 0 }
        visible.sort {
            rank($0.1) != rank($1.1) ? rank($0.1) < rank($1.1)
                : hypot($0.2.x - center.x, $0.2.y - center.y) < hypot($1.2.x - center.x, $1.2.y - center.y)
        }
        let limit = min(max(Int(size.width * size.height / 34_000), 6), 14)
        let spacing = min(size.width, size.height) * 0.07
        var seen = Set<String>()
        var chosen: [(Int, FeatureLibrary.Feature, CGPoint)] = []
        for c in visible where chosen.count < limit {
            guard seen.insert("\(c.1.name.lowercased())|\(c.1.kind)").inserted,
                  chosen.allSatisfy({ hypot($0.2.x - c.2.x, $0.2.y - c.2.y) >= spacing }) else { continue }
            chosen.append(c)
        }

        // Size each box for its text and place it along the leader direction.
        var placed: [(id: Int, feature: FeatureLibrary.Feature, title: String, subtitle: String?, anchor: CGPoint, box: CGRect)] = []
        for (i, f, p) in chosen {
            // Turkish name first, Latin below it.
            let name = names(f.name)
            let title = name.tr ?? name.la ?? f.name
            let subtitle: String?
            switch f.kind {
            case .origin: subtitle = "Başlangıç yeri"
            case .insertion: subtitle = "Tutunma yeri"
            case .feature, .part: subtitle = name.la.flatMap { $0.caseInsensitiveCompare(title) == .orderedSame ? nil : $0 }
            }
            let titleWidth = CGFloat(title.count) * 6.5
            let width = min(max(max(titleWidth, CGFloat(subtitle?.count ?? 0) * 5.4) + 18, 78), 170)
            let lines: CGFloat = titleWidth > width - 18 ? 2 : 1
            let height = lines * 15 + (subtitle == nil ? 0 : 13) + 12
            var outward = CGVector(dx: p.x - center.x, dy: p.y - center.y)
            if hypot(outward.dx, outward.dy) < 1 { outward = CGVector(dx: p.x < size.width / 2 ? -1 : 1, dy: 0) }
            outward = Self.normalized(outward)
            var dir = outward
            if let q = project(f.tip, in: size), hypot(q.x - p.x, q.y - p.y) > 3 {
                let leader = Self.normalized(CGVector(dx: q.x - p.x, dy: q.y - p.y))
                dir = Self.normalized(CGVector(dx: leader.dx * 0.55 + outward.dx * 0.45, dy: leader.dy * 0.55 + outward.dy * 0.45))
            }
            let reach = 30 + abs(dir.dx) * width / 2 + abs(dir.dy) * height / 2
            let mid = CGPoint(x: p.x + dir.dx * reach, y: p.y + dir.dy * reach)
            let box = Self.clamp(CGRect(x: mid.x - width / 2, y: mid.y - height / 2, width: width, height: height), to: safe)
            placed.append((i, f, title, subtitle, p, box))
        }

        // Relax: separate overlapping boxes and keep boxes off the pins.
        let anchors = placed.map(\.anchor)
        for _ in 0..<120 {
            var moved = false
            for a in placed.indices {
                for b in placed.indices where b > a {
                    let ra = placed[a].box.insetBy(dx: -4, dy: -3), rb = placed[b].box.insetBy(dx: -4, dy: -3)
                    let overlap = ra.intersection(rb)
                    guard !overlap.isNull, overlap.width > 0.5, overlap.height > 0.5 else { continue }
                    moved = true
                    if overlap.width < overlap.height * 1.6 {
                        let sign: CGFloat = ra.midX < rb.midX ? -1 : 1
                        placed[a].box.origin.x += sign * overlap.width / 2
                        placed[b].box.origin.x -= sign * overlap.width / 2
                    } else {
                        let sign: CGFloat = ra.midY <= rb.midY ? -1 : 1
                        placed[a].box.origin.y += sign * overlap.height / 2
                        placed[b].box.origin.y -= sign * overlap.height / 2
                    }
                }
                for anchor in anchors {
                    let r = placed[a].box.insetBy(dx: -7, dy: -7)
                    guard r.contains(anchor) else { continue }
                    moved = true
                    let dx = anchor.x < r.midX ? r.maxX - anchor.x : r.minX - anchor.x
                    let dy = anchor.y < r.midY ? r.maxY - anchor.y : r.minY - anchor.y
                    if abs(dy) < abs(dx) { placed[a].box.origin.y -= dy * 0.5 } else { placed[a].box.origin.x -= dx * 0.5 }
                }
                placed[a].box = Self.clamp(placed[a].box, to: safe)
            }
            if !moved { break }
        }

        // Drop whatever still collides; earlier labels have priority.
        var out: [Label] = []
        for item in placed {
            let r = item.box.insetBy(dx: -2, dy: -2)
            guard !out.contains(where: { $0.box.intersects(r) }),
                  !anchors.contains(where: { $0 != item.anchor && item.box.insetBy(dx: -3, dy: -3).contains($0) }) else { continue }
            out.append(Label(id: item.id, name: item.feature.name, title: item.title, subtitle: item.subtitle,
                             anchor: item.anchor, box: item.box, kind: item.feature.kind))
        }
        return out
    }

    /// "(Abdominal part of pectoralis major muscle)" → without the brackets.
    nonisolated private static func plainName(_ name: String) -> String {
        name.hasPrefix("(") && name.hasSuffix(")") ? String(name.dropFirst().dropLast()) : name
    }

    /// The vertex nearest the middle of a part among those facing the viewer.
    nonisolated private static func surfacePoint(positions: [SIMD3<Float>], normals: [SIMD3<Float>], span: Range<Int>,
                                                 facing: SIMD3<Float>) -> (SIMD3<Float>, SIMD3<Float>) {
        guard !span.isEmpty else { return (.zero, facing) }
        var sum = SIMD3<Float>.zero
        for i in span { sum += positions[i] }
        let middle = sum / Float(span.count)
        var best = span.lowerBound, bestScore = Float.infinity
        for i in span {
            let d = simd_length_squared(positions[i] - middle)
            let score = simd_dot(normals[i], facing) > 0.25 ? d : d + 1
            if score < bestScore { best = i; bestScore = score }
        }
        return (positions[best], normals[best])
    }

    /// A vertex of `span` that faces the viewer and is not hidden behind any
    /// of `occluders`, as near the middle of the part as possible; the plain
    /// surface point when none is visible.
    nonisolated private static func visiblePoint(positions: [SIMD3<Float>], normals: [SIMD3<Float>], span: Range<Int>,
                                                 facing: SIMD3<Float>, eye: SIMD3<Float>,
                                                 occluders: [(range: Range<Int>, lo: SIMD3<Float>, hi: SIMD3<Float>)],
                                                 indices: [UInt32]) -> (SIMD3<Float>, SIMD3<Float>) {
        guard !span.isEmpty else { return (.zero, facing) }
        var sum = SIMD3<Float>.zero
        for i in span { sum += positions[i] }
        let middle = sum / Float(span.count)
        let candidates = span.filter { simd_dot(normals[$0], facing) > 0.2 }
            .sorted { simd_length_squared(positions[$0] - middle) < simd_length_squared(positions[$1] - middle) }
        // Test the nearest few, then a spread of the rest.
        let step = max(candidates.count / 40, 1)
        let tested = Array(candidates.prefix(12)) + Swift.stride(from: 12, to: candidates.count, by: step).map { candidates[$0] }
        for i in tested {
            let toPoint = positions[i] - eye
            let d = simd_length(toPoint)
            if !blocked(eye, toPoint / d, before: d - 0.003, parts: occluders, positions: positions, indices: indices) {
                return (positions[i], normals[i])
            }
        }
        return surfacePoint(positions: positions, normals: normals, span: span, facing: facing)
    }

    nonisolated private static func normalized(_ v: CGVector) -> CGVector {
        let l = max(hypot(v.dx, v.dy), 0.0001)
        return CGVector(dx: v.dx / l, dy: v.dy / l)
    }

    nonisolated private static func clamp(_ r: CGRect, to safe: CGRect) -> CGRect {
        var r = r
        r.origin.x = min(max(r.minX, safe.minX), safe.maxX - r.width)
        r.origin.y = min(max(r.minY, safe.minY), safe.maxY - r.height)
        return r
    }

    /// Whether anything is hit along the ray before `limit`, skipping parts
    /// whose bounds the ray misses.
    nonisolated private static func blocked(_ o: SIMD3<Float>, _ d: SIMD3<Float>, before limit: Float,
                                            parts: [(range: Range<Int>, lo: SIMD3<Float>, hi: SIMD3<Float>)],
                                            positions: [SIMD3<Float>], indices: [UInt32]) -> Bool {
        let inv = SIMD3<Float>(1 / d.x, 1 / d.y, 1 / d.z)
        for part in parts {
            let t0 = (part.lo - o) * inv, t1 = (part.hi - o) * inv
            let near = simd_reduce_max(simd_min(t0, t1)), far = simd_reduce_min(simd_max(t0, t1))
            guard far >= max(near, 0), near < limit else { continue }
            if let hit = firstHit(o, d, positions: positions, indices: indices, range: part.range), hit < limit { return true }
        }
        return false
    }

    nonisolated private static func firstHit(_ o: SIMD3<Float>, _ d: SIMD3<Float>, positions: [SIMD3<Float>], indices: [UInt32],
                                             range: Range<Int>? = nil) -> Float? {
        var best = Float.infinity
        var i = range?.lowerBound ?? 0
        let end = range?.upperBound ?? indices.count
        while i + 2 < end {
            let a = positions[Int(indices[i])], b = positions[Int(indices[i + 1])], c = positions[Int(indices[i + 2])]
            i += 3
            let e1 = b - a, e2 = c - a
            let p = simd_cross(d, e2)
            let det = simd_dot(e1, p)
            if abs(det) < 1e-12 { continue }
            let inv = 1 / det
            let s = o - a
            let u = simd_dot(s, p) * inv
            if u < 0 || u > 1 { continue }
            let q = simd_cross(s, e1)
            let v = simd_dot(d, q) * inv
            if v < 0 || u + v > 1 { continue }
            let t = simd_dot(e2, q) * inv
            if t > 0.0005 && t < best { best = t }
        }
        return best.isFinite ? best : nil
    }
}
