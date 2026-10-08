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
        /// Centre of the text pill, beside the anchor.
        let center: CGPoint
        let text: String
        var id: PartRef { ref }
    }

    /// Picks the largest parts on screen that are actually visible at their
    /// centre and lays out non-overlapping labels for them.
    func labels(in size: CGSize, name: (PartInfo) -> String, limit: Int = 16) async -> [ScreenLabel] {
        guard size.width > 0 else { return [] }
        let t = tan(fieldOfView * .pi / 360)
        let cameraPosition = camera.position(relativeTo: nil)
        var candidates: [(ref: PartRef, point: CGPoint, size: CGFloat, info: PartInfo)] = []
        for (id, system) in systems where enabledLayers.contains(id) {
            for (i, info) in system.pack.parts.enumerated() {
                let ref = PartRef(system: id, index: i)
                let st = state(of: ref)
                guard st == .solid || st == .selected || st == .highlighted else { continue }
                let depth = max(simd_distance(info.center, cameraPosition), 0.01)
                let radius = simd_length(info.extent) / 2
                let screen = CGFloat(radius / (depth * t)) * size.height / 2
                guard screen > 18 else { continue }
                // Anchor on the camera-facing surface rather than the box centre,
                // which is often buried inside the body.
                let anchor = Self.surfaceAnchor(pack: system.pack, part: i, camera: cameraPosition) ?? info.center
                guard let point = project(anchor, in: size),
                      point.x > 30, point.x < size.width - 30, point.y > 120, point.y < size.height - 150 else { continue }
                candidates.append((ref, point, screen, info))
            }
        }
        candidates.sort { $0.size > $1.size }

        var out: [ScreenLabel] = []
        var taken: [CGRect] = []
        var names = Set<String>()
        for c in candidates.prefix(140) {
            guard out.count < limit else { break }
            let text = name(c.info)
            guard !names.contains(text) else { continue }
            // Is the part really what we see at its centre?
            guard let hit = await pick(at: c.point, in: size), hit == c.ref || manifests[hit.system]?[hit.index].base == c.info.base else { continue }
            // The pill grows away from the body's midline so the anchor stays visible.
            let width = CGFloat(text.count) * 6.3 + 22
            let leftSide = c.point.x < size.width / 2
            var x = leftSide ? c.point.x - width - 6 : c.point.x + 6
            x = min(max(x, 8), size.width - width - 8)
            let rect = CGRect(x: x, y: c.point.y - 12, width: width, height: 24)
            guard !taken.contains(where: { $0.insetBy(dx: -3, dy: -3).intersects(rect) }) else { continue }
            taken.append(rect)
            names.insert(text)
            out.append(ScreenLabel(ref: c.ref, anchor: c.point, center: CGPoint(x: rect.midX, y: rect.midY), text: text))
        }
        return out
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

    nonisolated static func rayBox(_ o: SIMD3<Float>, _ d: SIMD3<Float>, _ box: BoundingBox) -> Float? {
        let inv = SIMD3<Float>(1 / d.x, 1 / d.y, 1 / d.z)
        let t0 = (box.min - o) * inv
        let t1 = (box.max - o) * inv
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
