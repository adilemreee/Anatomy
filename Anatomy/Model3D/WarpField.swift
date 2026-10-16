//
//  WarpField.swift
//  Anatomy
//
//  The female body is the male atlas moved by a smooth displacement field:
//  the difference between the female and the male skin, carried into the
//  body (tools/skin/warp_field.py). Bones, muscles, vessels, nerves and
//  organs follow it, so every layer lines up with the female skin.
//

import Foundation
import simd

nonisolated struct WarpField: Sendable {
    /// One regular grid of displacements, index (i * ny + j) * nz + k.
    struct Grid: Sendable {
        let origin: SIMD3<Float>
        let cell: Float
        let nx: Int, ny: Int, nz: Int
        let values: [SIMD3<Float>]

        var upper: SIMD3<Float> { origin + SIMD3(Float(nx - 1), Float(ny - 1), Float(nz - 1)) * cell }

        /// Trilinear displacement at `p` (clamped to the grid).
        func displacement(at p: SIMD3<Float>) -> SIMD3<Float> {
            let g = (p - origin) / cell
            let x = min(max(g.x, 0), Float(nx - 1) - 0.001)
            let y = min(max(g.y, 0), Float(ny - 1) - 0.001)
            let z = min(max(g.z, 0), Float(nz - 1) - 0.001)
            let i = Int(x), j = Int(y), k = Int(z)
            let fx = x - Float(i), fy = y - Float(j), fz = z - Float(k)
            func v(_ a: Int, _ b: Int, _ c: Int) -> SIMD3<Float> { values[(a * ny + b) * nz + c] }
            let c00 = v(i, j, k) * (1 - fx) + v(i + 1, j, k) * fx
            let c10 = v(i, j + 1, k) * (1 - fx) + v(i + 1, j + 1, k) * fx
            let c01 = v(i, j, k + 1) * (1 - fx) + v(i + 1, j, k + 1) * fx
            let c11 = v(i, j + 1, k + 1) * (1 - fx) + v(i + 1, j + 1, k + 1) * fx
            return (c00 * (1 - fy) + c10 * fy) * (1 - fz) + (c01 * (1 - fy) + c11 * fy) * fz
        }

        /// 1 well inside the grid, falling to 0 within `margin` of its faces.
        func weight(at p: SIMD3<Float>, margin: Float) -> Float {
            let a = (p - origin) / margin, b = (upper - p) / margin
            let m = simd_min(a, b)
            let t = min(max(min(m.x, min(m.y, m.z)), 0), 1)
            return t * t * (3 - 2 * t)
        }
    }

    /// The body-wide grid, then finer grids (hands, feet) blended in over it.
    let base: Grid
    let details: [Grid]

    /// Loads `warp-female.bin` ("WRP2": a grid count, then per grid origin
    /// f32×3, cell size f32, dims u32×3 and float16 xyz per cell), compressed
    /// like the mesh packs.
    static func loadFemale() -> WarpField? {
        guard let url = Bundle.main.url(forResource: "warp-female", withExtension: "bin"),
              let compressed = try? Data(contentsOf: url),
              let data = try? (compressed as NSData).decompressed(using: .zlib) as Data else { return nil }
        return data.withUnsafeBytes { raw -> WarpField? in
            guard raw.count > 8, raw[0] == 0x57, raw[1] == 0x52, raw[2] == 0x50, raw[3] == 0x32 else { return nil }
            func f(_ o: Int) -> Float { raw.loadUnaligned(fromByteOffset: o, as: Float.self) }
            func u(_ o: Int) -> Int { Int(raw.loadUnaligned(fromByteOffset: o, as: UInt32.self)) }
            let count = u(4)
            var cursor = 8
            var grids: [Grid] = []
            for _ in 0..<count {
                guard cursor + 28 <= raw.count else { return nil }
                let origin = SIMD3(f(cursor), f(cursor + 4), f(cursor + 8)), cell = f(cursor + 12)
                let nx = u(cursor + 16), ny = u(cursor + 20), nz = u(cursor + 24)
                cursor += 28
                let n = nx * ny * nz
                guard cursor + n * 6 <= raw.count else { return nil }
                var values = [SIMD3<Float>](repeating: .zero, count: n)
                for c in 0..<n {
                    let o = cursor + c * 6
                    values[c] = SIMD3(Float(raw.loadUnaligned(fromByteOffset: o, as: Float16.self)),
                                      Float(raw.loadUnaligned(fromByteOffset: o + 2, as: Float16.self)),
                                      Float(raw.loadUnaligned(fromByteOffset: o + 4, as: Float16.self)))
                }
                cursor += n * 6
                grids.append(Grid(origin: origin, cell: cell, nx: nx, ny: ny, nz: nz, values: values))
            }
            guard let base = grids.first else { return nil }
            return WarpField(base: base, details: Array(grids.dropFirst()))
        }
    }

    func displacement(at p: SIMD3<Float>) -> SIMD3<Float> {
        var d = base.displacement(at: p)
        for grid in details {
            let w = grid.weight(at: p, margin: 0.012)
            if w > 0 { d += (grid.displacement(at: p) - d) * w }
        }
        return d
    }
}

extension MeshPack {
    /// This pack moved by `warp`; parts for which `keep` is true (already
    /// modelled in the female shape) stay where they are. Normals follow the
    /// local deformation, part bounds are recomputed.
    nonisolated func warped(by warp: WarpField, keep: (PartInfo) -> Bool) -> MeshPack {
        var copy = self
        let e: Float = 0.004
        let moving = parts.indices.filter { !keep(parts[$0]) && ranges[$0].vertexCount > 0 }
        // Blocks of vertices, spread over all cores.
        var blocks: [Swift.Range<Int>] = []
        for p in moving {
            let r = ranges[p]
            var start = r.vertexStart
            let end = r.vertexStart + r.vertexCount
            while start < end {
                blocks.append(start..<min(start + 8192, end))
                start += 8192
            }
        }
        positions.withUnsafeBufferPointer { srcPositions in
            normals.withUnsafeBufferPointer { srcNormals in
                copy.positions.withUnsafeMutableBufferPointer { dstPositions in
                    copy.normals.withUnsafeMutableBufferPointer { dstNormals in
                        // Every block writes its own vertices only.
                        let buffers = WarpBuffers(sp: srcPositions.baseAddress!, sn: srcNormals.baseAddress!,
                                                  dp: dstPositions.baseAddress!, dn: dstNormals.baseAddress!)
                        DispatchQueue.concurrentPerform(iterations: blocks.count) { b in
                            let sp = buffers.sp, sn = buffers.sn, dp = buffers.dp, dn = buffers.dn
                            for v in blocks[b] {
                                let x = sp[v]
                                let d = warp.displacement(at: x)
                                // Jacobian of the displacement by forward differences; the
                                // normal goes through the inverse transpose (to first order).
                                let dx = (warp.displacement(at: x + SIMD3(e, 0, 0)) - d) / e
                                let dy = (warp.displacement(at: x + SIMD3(0, e, 0)) - d) / e
                                let dz = (warp.displacement(at: x + SIMD3(0, 0, e)) - d) / e
                                let n = sn[v]
                                let jtn = SIMD3(simd_dot(dx, n), simd_dot(dy, n), simd_dot(dz, n))
                                dp[v] = x + d
                                dn[v] = simd_normalize(n - jtn)
                            }
                        }
                    }
                }
            }
        }
        for p in moving {
            let r = ranges[p]
            var lo = SIMD3<Float>(repeating: .greatestFiniteMagnitude), hi = -lo
            for v in r.vertexStart..<r.vertexStart + r.vertexCount {
                lo = simd_min(lo, copy.positions[v]); hi = simd_max(hi, copy.positions[v])
            }
            copy.parts[p].bounds = [lo.x, lo.y, lo.z, hi.x, hi.y, hi.z]
        }
        return copy
    }
}

/// The source and destination arrays of a warp, shared by its parallel blocks.
private nonisolated struct WarpBuffers: @unchecked Sendable {
    let sp: UnsafePointer<SIMD3<Float>>, sn: UnsafePointer<SIMD3<Float>>
    let dp: UnsafeMutablePointer<SIMD3<Float>>, dn: UnsafeMutablePointer<SIMD3<Float>>
}

/// Extra per-vertex moves for the female body (tools/skin/female_fix.py):
/// the few vertices that the warp leaves outside her skin or just under it.
nonisolated struct FemaleFix: Sendable {
    /// system -> (vertex index in the pack, move)
    let moves: [String: [(Int, SIMD3<Float>)]]

    static func load() -> FemaleFix? {
        guard let url = Bundle.main.url(forResource: "female-fix", withExtension: "bin"),
              let compressed = try? Data(contentsOf: url),
              let data = try? (compressed as NSData).decompressed(using: .zlib) as Data else { return nil }
        return data.withUnsafeBytes { raw -> FemaleFix? in
            guard raw.count > 8, raw[0] == 0x46, raw[1] == 0x46, raw[2] == 0x58, raw[3] == 0x31 else { return nil }
            var cursor = 4
            func u32() -> Int { defer { cursor += 4 }; return Int(raw.loadUnaligned(fromByteOffset: cursor, as: UInt32.self)) }
            let systems = u32()
            var moves: [String: [(Int, SIMD3<Float>)]] = [:]
            for _ in 0..<systems {
                guard cursor < raw.count else { return nil }
                let length = Int(raw[cursor]); cursor += 1
                guard cursor + length + 4 <= raw.count,
                      let name = String(bytes: UnsafeRawBufferPointer(rebasing: raw[cursor..<cursor + length]), encoding: .utf8) else { return nil }
                cursor += length
                let count = u32()
                guard cursor + count * 10 <= raw.count else { return nil }
                var list: [(Int, SIMD3<Float>)] = []
                list.reserveCapacity(count)
                for _ in 0..<count {
                    let index = Int(raw.loadUnaligned(fromByteOffset: cursor, as: UInt32.self))
                    let move = SIMD3(Float(raw.loadUnaligned(fromByteOffset: cursor + 4, as: Float16.self)),
                                     Float(raw.loadUnaligned(fromByteOffset: cursor + 6, as: Float16.self)),
                                     Float(raw.loadUnaligned(fromByteOffset: cursor + 8, as: Float16.self)))
                    list.append((index, move))
                    cursor += 10
                }
                moves[name] = list
            }
            return FemaleFix(moves: moves)
        }
    }
}

extension MeshPack {
    /// Adds the female per-vertex moves of this pack's system.
    nonisolated func fixed(by fix: FemaleFix?) -> MeshPack {
        guard let list = fix?.moves[system], !list.isEmpty else { return self }
        var copy = self
        for (index, move) in list where copy.positions.indices.contains(index) {
            copy.positions[index] += move
        }
        return copy
    }
}
