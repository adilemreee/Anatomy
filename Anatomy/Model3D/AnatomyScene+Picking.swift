//
//  AnatomyScene+Picking.swift
//  Anatomy
//
//  CPU ray picking against the decoded geometry and on-screen labels.
//

import RealityKit
import SwiftUI

extension AnatomyScene {
    // MARK: Labels

    /// A name pinned on screen next to a visible part.
    nonisolated struct ScreenLabel: Identifiable, Hashable, Sendable {
        let ref: PartRef
        /// The pinned surface point.
        let anchor: CGPoint
        /// The text pill, in a column beside the body.
        let box: CGRect
        let text: String
        var id: PartRef { ref }
        var center: CGPoint { CGPoint(x: box.midX, y: box.midY) }
        /// Where the leader line meets the pill: the side facing the anchor.
        var attach: CGPoint { CGPoint(x: anchor.x < box.midX ? box.minX : box.maxX, y: box.midY) }
    }

    /// Everything picking needs, copied off the scene so rays can be cast on
    /// a background thread while the user keeps interacting.
    nonisolated struct PickSnapshot: Sendable {
        nonisolated struct System: Sendable {
            let id: String
            let pack: MeshPack
            let lo: [SIMD3<Float>]
            let hi: [SIMD3<Float>]
            /// Per part: 0 hidden, 1 drawn solid, 2 see-through.
            let state: [UInt8]
        }

        let systems: [System]
        let camera: simd_float4x4
        let fieldOfView: Float

        func ray(at point: CGPoint, in size: CGSize) -> (SIMD3<Float>, SIMD3<Float>) {
            let aspect = Float(size.width / size.height)
            let t = tan(fieldOfView * .pi / 360)
            let x = (2 * Float(point.x / size.width) - 1) * t * aspect
            let y = (1 - 2 * Float(point.y / size.height)) * t
            let local = simd_normalize(SIMD3<Float>(x, y, -1))
            let dir4 = camera * SIMD4(local, 0)
            return (SIMD3(camera.columns.3.x, camera.columns.3.y, camera.columns.3.z), simd_normalize(SIMD3(dir4.x, dir4.y, dir4.z)))
        }

        func project(_ p: SIMD3<Float>, in size: CGSize) -> CGPoint? {
            let c = camera.inverse * SIMD4(p, 1)
            guard c.z < -0.01 else { return nil }
            let t = tan(fieldOfView * .pi / 360)
            let aspect = Float(size.width / size.height)
            return CGPoint(x: CGFloat((c.x / (-c.z * t * aspect) + 1) / 2) * size.width,
                           y: CGFloat((1 - c.y / (-c.z * t)) / 2) * size.height)
        }

        /// The frontmost drawn part along the ray; see-through parts only win
        /// when nothing solid is hit.
        func pick(_ origin: SIMD3<Float>, _ direction: SIMD3<Float>) -> PartRef? {
            var candidates: [(system: Int, part: Int, entry: Float, ghost: Bool)] = []
            for (s, system) in systems.enumerated() {
                for i in system.state.indices where system.state[i] != 0 {
                    if let entry = AnatomyScene.rayBox(origin, direction, lo: system.lo[i], hi: system.hi[i]) {
                        candidates.append((s, i, entry, system.state[i] == 2))
                    }
                }
            }
            candidates.sort { $0.entry < $1.entry }
            var best: (Float, PartRef)?
            var bestGhost: (Float, PartRef)?
            for c in candidates {
                // Sorted by box entry: nothing after this can be closer than a solid hit.
                if let solid = best, c.entry >= solid.0 { break }
                let limit = c.ghost ? (bestGhost?.0 ?? .infinity) : (best?.0 ?? .infinity)
                if c.entry >= limit { continue }
                let system = systems[c.system]
                if let hit = AnatomyScene.rayMesh(origin, direction, pack: system.pack, part: c.part, limit: limit) {
                    let ref = PartRef(system: system.id, index: c.part)
                    if c.ghost { bestGhost = (hit, ref) } else { best = (hit, ref) }
                }
            }
            return best?.1 ?? bestGhost?.1
        }
    }

    /// A copy of what is drawn, for picking off the main thread.
    func pickSnapshot() -> PickSnapshot {
        var out: [PickSnapshot.System] = []
        for layer in ModelLayer.all {
            guard enabledLayers.contains(layer.id), let system = systems[layer.id] else { continue }
            var states = [UInt8](repeating: 0, count: system.pack.parts.count)
            for i in states.indices {
                switch state(of: PartRef(system: layer.id, index: i)) {
                case .hidden: states[i] = 0
                case .ghost: states[i] = 2
                case .solid, .selected, .highlighted: states[i] = 1
                }
            }
            out.append(.init(id: layer.id, pack: system.pack, lo: system.bounds.map(\.min), hi: system.bounds.map(\.max), state: states))
        }
        return PickSnapshot(systems: out, camera: camera.transformMatrix(relativeTo: nil), fieldOfView: fieldOfView)
    }

    /// Picks the largest parts on screen that are actually visible at their
    /// pin and lays out their names: in two columns beside the body when
    /// there is room next to it, otherwise right beside each pin (see
    /// LabelLayout). Labels stay between `top` and `bottom` and off the
    /// `avoiding` rectangles (buttons over the view). All the geometry work
    /// happens off the main thread.
    func labels(in size: CGSize, top: CGFloat = 120, bottom: CGFloat? = nil, avoiding: [CGRect] = [],
                name: (PartInfo) -> String, limit: Int = 16) async -> [ScreenLabel] {
        guard size.width > 0 else { return [] }
        let snapshot = pickSnapshot()
        // Names are resolved up front (the store lives on the main actor).
        var names: [PartRef: String] = [:]
        for system in snapshot.systems {
            for i in system.state.indices where system.state[i] == 1 {
                names[PartRef(system: system.id, index: i)] = name(system.pack.parts[i])
            }
        }
        let resolved = names
        let font = UIFont.systemFont(ofSize: UIFont.preferredFont(forTextStyle: .caption2).pointSize, weight: .semibold)
        let safe = CGRect(x: 8, y: top, width: size.width - 16, height: max((bottom ?? size.height - 150) - top, 0))
        return await Task.detached(priority: .userInitiated) { () -> [ScreenLabel] in
            let t = tan(snapshot.fieldOfView * .pi / 360)
            let eye = SIMD3(snapshot.camera.columns.3.x, snapshot.camera.columns.3.y, snapshot.camera.columns.3.z)

            // The body's outline on screen, from a sample of what is drawn.
            var drawn: [(MeshPack, Int)] = []
            var total = 0
            for system in snapshot.systems {
                for i in system.state.indices where system.state[i] != 0 {
                    drawn.append((system.pack, i))
                    total += system.pack.ranges[i].vertexCount
                }
            }
            let step = max(total / 40_000, 1)
            var points: [CGPoint] = []
            points.reserveCapacity(total / step + drawn.count)
            for (pack, i) in drawn {
                let r = pack.ranges[i]
                var v = r.vertexStart
                while v < r.vertexStart + r.vertexCount {
                    if let p = snapshot.project(pack.positions[v], in: size) { points.append(p) }
                    v += step
                }
            }
            let silhouette = LabelLayout.Silhouette(points: points, in: CGRect(origin: .zero, size: size))
            let middle = silhouette.extent.map { ($0.min + $0.max) / 2 } ?? size.width / 2

            var candidates: [(ref: PartRef, point: CGPoint, size: CGFloat, base: String)] = []
            for system in snapshot.systems {
                for (i, info) in system.pack.parts.enumerated() where system.state[i] == 1 {
                    let depth = max(simd_distance(info.center, eye), 0.01)
                    let screen = CGFloat(simd_length(info.extent) / 2 / (depth * t)) * size.height / 2
                    guard screen > 18 else { continue }
                    // Anchor on the camera-facing surface rather than the box
                    // centre, which is often buried inside the body.
                    let anchor = AnatomyScene.surfaceAnchor(pack: system.pack, part: i, camera: eye) ?? info.center
                    guard let point = snapshot.project(anchor, in: size), safe.insetBy(dx: 22, dy: 0).contains(point),
                          !avoiding.contains(where: { $0.insetBy(dx: -6, dy: -6).contains(point) }) else { continue }
                    candidates.append((PartRef(system: system.id, index: i), point, screen, info.base))
                }
            }
            candidates.sort { $0.size > $1.size }
            let bases = Dictionary(uniqueKeysWithValues: snapshot.systems.map { ($0.id, $0.pack.parts.map(\.base)) })

            // The biggest parts that are really what we see at their pin,
            // pins kept a little apart. A name shared by the left and right
            // part goes on the side with fewer labels so far.
            var byName: [String: [Int]] = [:]
            var order: [String] = []
            for (k, c) in candidates.prefix(160).enumerated() {
                guard let text = resolved[c.ref] else { continue }
                if byName[text] == nil { order.append(text) }
                byName[text, default: []].append(k)
            }
            var chosen: [(ref: PartRef, point: CGPoint, text: String)] = []
            var perSide = [0, 0]
            let spread = min(size.width, size.height) * 0.04
            for text in order {
                guard chosen.count < limit + limit / 2, !Task.isCancelled else { break }
                let instances = (byName[text] ?? []).map { candidates[$0] }.sorted {
                    perSide[$0.point.x < middle ? 0 : 1] < perSide[$1.point.x < middle ? 0 : 1]
                }
                for c in instances {
                    guard chosen.allSatisfy({ hypot($0.point.x - c.point.x, $0.point.y - c.point.y) >= spread }) else { continue }
                    let (o, d) = snapshot.ray(at: c.point, in: size)
                    guard let hit = snapshot.pick(o, d), hit == c.ref || bases[hit.system]?[hit.index] == c.base else { continue }
                    chosen.append((c.ref, c.point, text))
                    perSide[c.point.x < middle ? 0 : 1] += 1
                    break
                }
            }

            let items = chosen.map { c in
                LabelLayout.Item(anchor: c.point,
                                 size: CGSize(width: ceil((c.text as NSString).size(withAttributes: [.font: font]).width) + 16, height: 22))
            }
            // Columns when the pills fit beside the body, else next to the pins.
            let room = LabelLayout.room(silhouette, in: safe, gap: 10)
            let typical = items.map(\.size.width).sorted().dropFirst(items.count / 2).first ?? 0
            let boxes = min(room.left, room.right) >= typical
                ? LabelLayout.place(items, silhouette: silhouette, in: safe, avoiding: avoiding, gap: 10, spacing: 5)
                : LabelLayout.placeNear(items, middle: middle, in: safe, avoiding: avoiding)
            var out: [ScreenLabel] = []
            for (c, box) in zip(chosen, boxes) {
                guard let box, out.count < limit else { continue }
                out.append(ScreenLabel(ref: c.ref, anchor: c.point, box: box, text: c.text))
            }
            return out
        }.value
    }

    /// The front-facing vertex closest to the centroid of the part's
    /// camera-facing surface.
    nonisolated static func surfaceAnchor(pack: MeshPack, part: Int, camera: SIMD3<Float>) -> SIMD3<Float>? {
        let range = pack.ranges[part]
        let step = max(1, range.vertexCount / 60)
        var sum = SIMD3<Float>.zero
        var count: Float = 0
        var facing: [SIMD3<Float>] = []
        var v = range.vertexStart
        let end = range.vertexStart + range.vertexCount
        while v < end {
            let p = pack.positions[v]
            if simd_dot(pack.normals[v], camera - p) > 0 {
                sum += p
                count += 1
                facing.append(p)
            }
            v += step
        }
        guard count > 0 else { return nil }
        let centroid = sum / count
        return facing.min { simd_distance_squared($0, centroid) < simd_distance_squared($1, centroid) }
    }

    // MARK: Picking

    /// Returns the frontmost pickable part under `point` (in view coordinates).
    /// Boxes are tested here; triangles are tested off the main thread, nearest
    /// box first, stopping as soon as no closer hit is possible.
    func pick(at point: CGPoint, in size: CGSize) async -> PartRef? {
        guard size.width > 0, size.height > 0 else { return nil }
        let snapshot = pickSnapshot()
        return await Task.detached(priority: .userInitiated) {
            let (origin, direction) = snapshot.ray(at: point, in: size)
            return snapshot.pick(origin, direction)
        }.value
    }

    /// The view (eight directions around the body, level or from above) from
    /// which most of `refs` can be seen, testing sample points against
    /// everything drawn, with the fraction that is visible and the parts
    /// covering the rest. Views where little has to be faded win over views
    /// where the structure faces away. The camera stays outside the body: for
    /// deep structures the distance grows past the outermost surface.
    func viewpoint(for refs: [PartRef], target: SIMD3<Float>, distance: Float)
        async -> (yaw: Float, pitch: Float, distance: Float, visible: Float, blockers: Set<PartRef>)? {
        var samples: [(SIMD3<Float>, SIMD3<Float>)] = []
        // The biggest parts make the outside of a structure (the chambers of
        // the heart, not the valves inside them).
        let sized = refs.sorted {
            (systems[$0.system]?.pack.ranges[$0.index].vertexCount ?? 0) > (systems[$1.system]?.pack.ranges[$1.index].vertexCount ?? 0)
        }
        for ref in sized.prefix(8) {
            guard let system = systems[ref.system] else { continue }
            let r = system.pack.ranges[ref.index]
            let step = max(r.vertexCount / max(160 / min(refs.count, 8), 1), 1)
            for v in Swift.stride(from: r.vertexStart, to: r.vertexStart + r.vertexCount, by: step) {
                samples.append((system.pack.positions[v], system.pack.normals[v]))
            }
        }
        guard !samples.isEmpty else { return nil }
        var occluders: [(PartRef, BoundingBox)] = []
        var packs: [String: MeshPack] = [:]
        for (id, system) in systems where enabledLayers.contains(id) {
            packs[id] = system.pack
            for i in system.pack.parts.indices {
                let ref = PartRef(system: id, index: i)
                let s = state(of: ref)
                if s == .hidden || s == .ghost { continue }
                occluders.append((ref, system.bounds[i]))
            }
        }
        let targets = Set(refs)
        return await Task.detached(priority: .userInitiated) { () -> (yaw: Float, pitch: Float, distance: Float, visible: Float, blockers: Set<PartRef>) in
            struct View { var k: Int; var yaw, pitch, distance, thickness, visible, facing, score: Float; var eye: SIMD3<Float> }
            var views: [View] = []
            for pitch in [Float(0.08), 0.65] {
                for k in 0..<8 {
                    let yaw = Float(k) * .pi / 4
                    let direction = SIMD3(sin(yaw) * cos(pitch), sin(pitch), cos(yaw) * cos(pitch))
                    // The outermost surface along the view, seen from far away.
                    let far: Float = 2.5
                    let outside = target + direction * far
                    var nearestFromOutside = far
                    for (ref, box) in occluders where !targets.contains(ref) {
                        guard let entry = Self.rayBox(outside, -direction, box), entry < nearestFromOutside,
                              let pack = packs[ref.system],
                              let hit = Self.rayMesh(outside, -direction, pack: pack, part: ref.index, limit: nearestFromOutside) else { continue }
                        nearestFromOutside = hit
                    }
                    let viewDistance = max(distance, far - nearestFromOutside + 0.04)
                    let eye = target + direction * viewDistance
                    var visible: Float = 0, facing: Float = 0, covered: Float = 0
                    var blockers: Set<PartRef> = []
                    for (p, n) in samples {
                        let toPoint = p - eye
                        let d = simd_length(toPoint)
                        let dir = toPoint / d
                        guard simd_dot(n, -dir) > 0.05 else { continue }
                        facing += 1
                        // The nearest part in front of the point, other than the target itself.
                        var nearest: (Float, PartRef)?
                        var blockedBySelf = false
                        for (ref, box) in occluders {
                            let limit = min(d - 0.004, nearest?.0 ?? .infinity)
                            guard let entry = Self.rayBox(eye, dir, box), entry < limit,
                                  let pack = packs[ref.system],
                                  let hit = Self.rayMesh(eye, dir, pack: pack, part: ref.index, limit: limit) else { continue }
                            if targets.contains(ref) { blockedBySelf = true } else { nearest = (hit, ref) }
                        }
                        if let (_, ref) = nearest {
                            blockers.insert(ref)
                            covered += 1
                        } else if !blockedBySelf {
                            visible += 1
                        }
                    }
                    // Prefer the front, then level views, when views are about as good.
                    let bias: Float = (k == 0 ? 1.08 : (k == 4 ? 0.97 : 1)) * (pitch > 0.3 ? 0.92 : 1)
                    let score = (visible + covered * 0.4) * bias - Float(blockers.count) * 0.6
                    views.append(View(k: k, yaw: yaw, pitch: pitch, distance: viewDistance, thickness: far - nearestFromOutside,
                                      visible: visible, facing: max(facing, 1), score: score, eye: eye))
                }
            }
            var best = views.max { $0.score < $1.score }!
            // Hidden from every side (the heart in the chest): the textbook view,
            // from the side with the least in front of it and the front when
            // that is about as thin (never through the arm from the side).
            if views.allSatisfy({ $0.visible / $0.facing < 0.2 }) {
                let thinnest = views.map(\.thickness).min() ?? 0
                func deep(_ v: View) -> Float {
                    let bias: Float = v.k == 0 ? 1 : (v.k == 1 || v.k == 7 ? 0.5 : (v.k == 4 ? 0.3 : 0))
                    return bias - (v.pitch > 0.3 ? 0.5 : 0) - (v.thickness - thinnest) / 0.03
                }
                best = views.max { deep($0) < deep($1) }!
            }
            // Everything between the camera and the structure, not only the
            // outermost layer: under the pectoral muscle come the ribs and the sternum.
            var counts: [PartRef: Int] = [:]
            for (p, n) in samples {
                let toPoint = p - best.eye
                let d = simd_length(toPoint)
                let dir = toPoint / d
                guard simd_dot(n, -dir) > 0.05 else { continue }
                for (ref, box) in occluders where !targets.contains(ref) {
                    guard let entry = Self.rayBox(best.eye, dir, box), entry < d - 0.004,
                          let pack = packs[ref.system],
                          Self.rayMesh(best.eye, dir, pack: pack, part: ref.index, limit: d - 0.004) != nil else { continue }
                    counts[ref, default: 0] += 1
                }
            }
            let minimum = max(1, Int(best.facing * 0.015))
            let covering = Set(counts.filter { $0.value >= minimum }.map(\.key))
            return (best.yaw, best.pitch, best.distance, best.visible / best.facing, covering)
        }.value
    }

    nonisolated static func rayBox(_ o: SIMD3<Float>, _ d: SIMD3<Float>, _ box: BoundingBox) -> Float? {
        rayBox(o, d, lo: box.min, hi: box.max)
    }

    nonisolated static func rayBox(_ o: SIMD3<Float>, _ d: SIMD3<Float>, lo: SIMD3<Float>, hi: SIMD3<Float>) -> Float? {
        let inv = SIMD3<Float>(1 / d.x, 1 / d.y, 1 / d.z)
        let t0 = (lo - o) * inv
        let t1 = (hi - o) * inv
        let tmin = simd_reduce_max(simd_min(t0, t1))
        let tmax = simd_reduce_min(simd_max(t0, t1))
        guard tmax >= max(tmin, 0) else { return nil }
        return max(tmin, 0)
    }

    nonisolated static func rayMesh(_ o: SIMD3<Float>, _ d: SIMD3<Float>, pack: MeshPack, part: Int, limit: Float) -> Float? {
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
}
