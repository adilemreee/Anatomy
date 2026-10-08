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

    @ObservationIgnored let root = Entity()
    @ObservationIgnored private let camera = Entity()
    @ObservationIgnored private var features: [FeatureLibrary.Feature] = []
    @ObservationIgnored private var positions: [SIMD3<Float>] = []
    @ObservationIgnored private var indices: [UInt32] = []
    @ObservationIgnored private var tween: Task<Void, Never>?
    @ObservationIgnored private var yaw: Float = 0
    @ObservationIgnored private var pitch: Float = 0.08
    @ObservationIgnored private var distance: Float = 0.6
    @ObservationIgnored private var target = SIMD3<Float>(0, 1, 0)
    @ObservationIgnored private var home: (SIMD3<Float>, Float, Float) = (.zero, 0.6, 0)
    @ObservationIgnored private let fieldOfView: Float = 32
    @ObservationIgnored private var bounds: (SIMD3<Float>, SIMD3<Float>) = (.zero, .zero)
    @ObservationIgnored private var ownerNames: Set<String> = []
    @ObservationIgnored private var aspect: Float = 0.46

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
        var structures: [(name: String, span: Range<Int>)] = []
        var attachments: [(bone: String, origin: Bool, span: Range<Int>)] = []

        for system in Set(all.map(\.system)).sorted() {
            guard let pack = try? await library.pack(system) else { continue }
            let partIndices = all.filter { $0.system == system }.map(\.index).sorted()
            // Drawn from the high-detail mesh where there is one (BodyParts3D),
            // otherwise from the atlas pack.
            let drawn = await Task.detached(priority: .userInitiated) { () -> (Data, [UInt32]) in
                var data = Data(), idx: [UInt32] = [], plain: [Int] = []
                func add(_ output: VertexBuilder.Output) {
                    let base = UInt32(data.count / VertexBuilder.stride)
                    data.append(output.vertices)
                    idx.append(contentsOf: output.indices.map { $0 + base })
                }
                for p in partIndices {
                    if let detail = DetailLibrary.shared.pack(system: system, index: p) {
                        add(VertexBuilder.build(pack: detail, parts: [0], mode: mode))
                    } else {
                        plain.append(p)
                    }
                }
                if !plain.isEmpty { add(VertexBuilder.build(pack: pack, parts: plain, mode: mode)) }
                return (data, idx)
            }.value
            let drawBase = UInt32(vertexData.count / VertexBuilder.stride)
            vertexData.append(drawn.0)
            drawIndices.append(contentsOf: drawn.1.map { $0 + drawBase })
            // Picking, label visibility and pins use the lighter atlas mesh.
            for p in partIndices {
                let r = pack.ranges[p]
                let span = allPositions.count..<allPositions.count + r.vertexCount
                let shift = Int64(span.lowerBound) - Int64(r.vertexStart)
                allIndices.append(contentsOf: pack.indices[r.indexStart..<r.indexStart + r.indexCount].map { UInt32(Int64($0) + shift) })
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
                    collected += FeatureLibrary.shared.features(for: info)
                    ownerNames.insert(info.base.lowercased())
                    structures.append((Self.plainName(info.base), span))
                }
            }
        }
        guard !drawIndices.isEmpty, !allIndices.isEmpty else { return }
        // Drawn smoothly subdivided.
        let source = (vertexData, drawIndices)
        let (smoothVertices, smoothIndices) = await Task.detached(priority: .userInitiated) {
            Tessellator.smooth(vertices: source.0, indices: source.1, maxTriangles: 800_000)
        }.value
        guard let mesh = try? AnatomyScene.makeMesh(vertexCount: smoothVertices.count / VertexBuilder.stride, indexCount: smoothIndices.count) else { return }
        AnatomyScene.upload(VertexBuilder.Output(vertices: smoothVertices, indices: smoothIndices, ranges: [], bounds: []), into: mesh)
        mesh.parts.replaceAll([LowLevelMesh.Part(indexCount: smoothIndices.count, topology: .triangle, materialIndex: 0,
                                                 bounds: BoundingBox(min: lo, max: hi))])
        guard let resource = try? await MeshResource(from: mesh) else { return }
        let entity = ModelEntity(mesh: resource, materials: await AnatomyMaterials.shared(occlusion: 0.55, rim: 0.7))
        root.addChild(entity)
        positions = allPositions
        indices = allIndices

        bounds = (lo, hi)
        let center = (lo + hi) / 2
        let fit = fitDistance()
        // Side structures are best seen turned a little towards their own
        // side. With bones around it, a muscle opens from whichever of front
        // and back shows more of it (the gluteus and trapezius from behind).
        var startYaw: Float = center.x > 0.1 ? 0.6 : (center.x < -0.1 ? -0.6 : 0)
        if !context.isEmpty {
            let sides = (startYaw, Float.pi - startYaw)
            let samples = structures.flatMap { s in stride(from: s.span.lowerBound, to: s.span.upperBound, by: max(s.span.count / 60, 1)) }
            let pitch = self.pitch
            let pts = allPositions, nrm = allNormals, idx = allIndices
            let counts = await Task.detached(priority: .userInitiated) { () -> (Int, Int) in
                func visible(_ yaw: Float) -> Int {
                    let eye = center + SIMD3(sin(yaw) * cos(pitch), sin(pitch), cos(yaw) * cos(pitch)) * fit
                    var count = 0
                    for i in samples {
                        let toV = pts[i] - eye, d = simd_length(toV)
                        guard simd_dot(nrm[i], -toV / d) > 0.1 else { continue }
                        if let hit = Self.firstHit(eye, toV / d, positions: pts, indices: idx), hit < d - 0.003 { continue }
                        count += 1
                    }
                    return count
                }
                return (visible(sides.0), visible(sides.1))
            }.value
            if Float(counts.1) > Float(counts.0) * 1.15 { startYaw = sides.1 }
        }

        // Labels for the heads of a muscle and for where it attaches, pinned
        // on the side that faces the opening view.
        let facing = SIMD3<Float>(sin(startYaw) * cos(pitch), sin(pitch), cos(startYaw) * cos(pitch))
        func pin(_ span: Range<Int>) -> (SIMD3<Float>, SIMD3<Float>) {
            Self.surfacePoint(positions: allPositions, normals: allNormals, span: span, facing: facing)
        }
        if (2...10).contains(structures.count) {
            for s in structures {
                let (p, n) = pin(s.span)
                collected.append(.init(name: s.name, anchor: p, tip: p + n * 0.03, kind: .part))
            }
        }
        var pinned = Set<String>()
        for a in attachments where pinned.insert("\(a.bone)|\(a.origin)").inserted {
            let (p, n) = pin(a.span)
            collected.append(.init(name: a.bone, anchor: p, tip: p + n * 0.03, kind: a.origin ? .origin : .insertion))
        }
        features = collected
        featureCount = collected.count
        hasAttachments = !attachments.isEmpty
        home = (center, fit, startYaw)
        target = center
        distance = fit
        yaw = startYaw
        applyCamera()
        isReady = true
        cameraDidSettle()

        if let environment = await AnatomyMaterials.environment() {
            let ibl = Entity()
            ibl.components.set(ImageBasedLightComponent(source: .single(environment), intensityExponent: -0.6))
            root.addChild(ibl)
            entity.components.set(ImageBasedLightReceiverComponent(imageBasedLight: ibl))
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
        return max(radius / sin(halfV) * 1.2, radius / sin(halfH) * 0.84)
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
        tween = Task { [weak self] in
            for step in 1...36 {
                guard let self, !Task.isCancelled else { return }
                let t = Float(step) / 36
                let e = t < 0.5 ? 4 * t * t * t : 1 - pow(-2 * t + 2, 3) / 2
                self.target = start.0 + (self.home.0 - start.0) * e
                self.distance = start.1 + (self.home.1 - start.1) * e
                self.yaw = start.2 + (end - start.2) * e
                self.pitch = start.3 + (0.08 - start.3) * e
                self.applyCamera()
                try? await Task.sleep(for: .milliseconds(11))
            }
            self?.cameraDidSettle()
        }
    }

    private func applyCamera() {
        let offset = SIMD3<Float>(sin(yaw) * cos(pitch), sin(pitch), cos(yaw) * cos(pitch)) * distance
        camera.look(at: target, from: target + offset, relativeTo: nil)
    }

    func pick(at point: CGPoint, in size: CGSize) async -> PartRef? { nil }

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
    func labels(in size: CGSize, top: CGFloat, bottom: CGFloat, latin: (String) -> String?) async -> [Label] {
        guard size.width > 0, bottom - top > 120, !features.isEmpty else { return [] }
        let safe = CGRect(x: 8, y: top, width: size.width - 16, height: bottom - top)
        let eye = camera.position(relativeTo: nil)
        let positions = self.positions, indices = self.indices
        let candidates: [(Int, FeatureLibrary.Feature, CGPoint)] = features.enumerated().compactMap { i, f in
            guard f.kind != .feature || !ownerNames.contains(f.name.lowercased()),
                  let p = project(f.anchor, in: size), safe.insetBy(dx: 12, dy: 0).contains(p) else { return nil }
            return (i, f, p)
        }
        let open = await Task.detached(priority: .userInitiated) { () -> [Bool] in
            candidates.map { _, f, _ in
                let toAnchor = f.anchor - eye
                let d = simd_length(toAnchor)
                guard let hit = Self.firstHit(eye, toAnchor / d, positions: positions, indices: indices) else { return true }
                // Attachments often sit just under the edge of their tendon.
                return hit > d - (f.kind == .origin || f.kind == .insertion ? 0.012 : 0.004)
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
            let title = latin(f.name) ?? f.name
            let subtitle: String?
            switch f.kind {
            case .origin: subtitle = "Başlangıç yeri"
            case .insertion: subtitle = "Tutunma yeri"
            case .feature, .part: subtitle = title.caseInsensitiveCompare(f.name) == .orderedSame ? nil : f.name
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

    nonisolated private static func firstHit(_ o: SIMD3<Float>, _ d: SIMD3<Float>, positions: [SIMD3<Float>], indices: [UInt32]) -> Float? {
        var best = Float.infinity
        var i = 0
        while i + 2 < indices.count {
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
