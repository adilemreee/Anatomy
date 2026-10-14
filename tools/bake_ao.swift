// Bakes per-vertex ambient occlusion into the mesh packs.
//
//   swiftc -O tools/bake_ao.swift -o /tmp/bake_ao
//   /tmp/bake_ao Anatomy/Resources/Models/mesh-*.bin
//
// Reads an "ANT1" pack (see tools/export_zanatomy.py), casts cosine weighted
// hemisphere rays from every vertex against all triangles of the same system
// and rewrites the file as "ANT2": identical layout plus, after each part's
// indices, one byte of occlusion per vertex (255 = fully open).
// Occlusion is computed per system so it stays correct whichever layers are
// shown together in the app.

import Foundation
import simd

// MARK: - Raw deflate (Compression framework)

func inflate(_ data: Data) -> Data {
    (try? (data as NSData).decompressed(using: .zlib) as Data) ?? Data()
}

func deflate(_ data: Data) -> Data {
    (try! (data as NSData).compressed(using: .zlib)) as Data
}

// MARK: - Pack

struct Part {
    var vertexCount: Int
    var indexCount: Int
    var positionBytes: Data
    var normalBytes: Data
    var indexBytes: Data
}

func readPack(_ raw: Data) -> (lo: SIMD3<Float>, hi: SIMD3<Float>, parts: [Part], header: Data) {
    precondition(raw.prefix(4) == Data("ANT1".utf8), "expected an ANT1 pack")
    func u32(_ o: Int) -> Int { Int(raw.withUnsafeBytes { $0.loadUnaligned(fromByteOffset: o, as: UInt32.self) }) }
    func f32(_ o: Int) -> Float { raw.withUnsafeBytes { $0.loadUnaligned(fromByteOffset: o, as: Float.self) } }
    let count = u32(4)
    let lo = SIMD3(f32(8), f32(12), f32(16))
    let hi = SIMD3(f32(20), f32(24), f32(28))
    var cursor = 32
    var sizes: [(Int, Int)] = []
    for _ in 0..<count {
        sizes.append((u32(cursor), u32(cursor + 4)))
        cursor += 8
    }
    let header = raw.subdata(in: 4..<cursor)
    var parts: [Part] = []
    for (v, i) in sizes {
        let wide = v > 65535
        let p = raw.subdata(in: cursor..<cursor + v * 6); cursor += v * 6
        let n = raw.subdata(in: cursor..<cursor + v * 3); cursor += v * 3
        let ib = raw.subdata(in: cursor..<cursor + i * (wide ? 4 : 2)); cursor += i * (wide ? 4 : 2)
        parts.append(Part(vertexCount: v, indexCount: i, positionBytes: p, normalBytes: n, indexBytes: ib))
    }
    return (lo, hi, parts, header)
}

// MARK: - BVH

struct Triangle {
    var a: SIMD3<Float>, e1: SIMD3<Float>, e2: SIMD3<Float>
    /// 0 for both sexes, 1 male, 2 female (see `sexCodes`).
    var sex: UInt8 = 0
}

struct Node {
    var lo: SIMD3<Float>
    var hi: SIMD3<Float>
    var left: Int32   // child indices, -1 for leaves
    var right: Int32
    var start: Int32  // first triangle (leaf)
    var count: Int32  // triangle count (leaf)
}

final class BVH {
    var nodes: [Node] = []
    var tris: [Triangle]

    init(_ input: [Triangle]) {
        var tris = input
        var centroids = tris.map { $0.a + ($0.e1 + $0.e2) / 3 }
        nodes.reserveCapacity(tris.count / 2)
        func bounds(_ r: Range<Int>) -> (SIMD3<Float>, SIMD3<Float>) {
            var lo = SIMD3<Float>(repeating: .infinity), hi = -lo
            for i in r {
                let t = tris[i]
                for p in [t.a, t.a + t.e1, t.a + t.e2] { lo = simd_min(lo, p); hi = simd_max(hi, p) }
            }
            return (lo, hi)
        }
        func build(_ r: Range<Int>) -> Int {
            let (lo, hi) = bounds(r)
            let index = nodes.count
            nodes.append(Node(lo: lo, hi: hi, left: -1, right: -1, start: Int32(r.lowerBound), count: Int32(r.count)))
            if r.count <= 6 { return index }
            // split the longest centroid axis at its midpoint
            var clo = SIMD3<Float>(repeating: .infinity), chi = -clo
            for i in r { clo = simd_min(clo, centroids[i]); chi = simd_max(chi, centroids[i]) }
            let ext = chi - clo
            let axis = ext.x > ext.y ? (ext.x > ext.z ? 0 : 2) : (ext.y > ext.z ? 1 : 2)
            let mid = (clo[axis] + chi[axis]) / 2
            var i = r.lowerBound, j = r.upperBound - 1
            while i <= j {
                if centroids[i][axis] < mid { i += 1 } else {
                    tris.swapAt(i, j); centroids.swapAt(i, j); j -= 1
                }
            }
            var split = i
            if split == r.lowerBound || split == r.upperBound { split = (r.lowerBound + r.upperBound) / 2 }
            let left = build(r.lowerBound..<split)
            let right = build(split..<r.upperBound)
            nodes[index].left = Int32(left)
            nodes[index].right = Int32(right)
            nodes[index].count = 0
            return index
        }
        self.tris = tris
        _ = build(0..<tris.count)
        self.tris = tris
    }

    /// True if the ray hits any triangle closer than `maxT`. Genital organs
    /// of the other sex are never shown together with `sex` (0 for packs
    /// without any), so they let the light through.
    func occluded(_ o: SIMD3<Float>, _ d: SIMD3<Float>, _ maxT: Float, sex: UInt8) -> Bool {
        let inv = SIMD3<Float>(1 / d.x, 1 / d.y, 1 / d.z)
        return withUnsafeTemporaryAllocation(of: Int32.self, capacity: 64) { stack in
        var sp = 1
        stack[0] = 0
        return nodes.withUnsafeBufferPointer { nodes in
            tris.withUnsafeBufferPointer { tris in
                while sp > 0 {
                    sp -= 1
                    let n = nodes[Int(stack[sp])]
                    let t0 = (n.lo - o) * inv, t1 = (n.hi - o) * inv
                    let tmin = simd_reduce_max(simd_min(t0, t1)), tmax = simd_reduce_min(simd_max(t0, t1))
                    if tmax < max(tmin, 0) || tmin > maxT { continue }
                    if n.left < 0 {
                        for k in Int(n.start)..<Int(n.start + n.count) {
                            let t = tris[k]
                            if t.sex != 0, t.sex != sex { continue }
                            let p = simd_cross(d, t.e2)
                            let det = simd_dot(t.e1, p)
                            if abs(det) < 1e-12 { continue }
                            let invDet = 1 / det
                            let s = o - t.a
                            let u = simd_dot(s, p) * invDet
                            if u < 0 || u > 1 { continue }
                            let q = simd_cross(s, t.e1)
                            let v = simd_dot(d, q) * invDet
                            if v < 0 || u + v > 1 { continue }
                            let h = simd_dot(t.e2, q) * invDet
                            if h > 1e-4 && h < maxT { return true }
                        }
                    } else if sp + 2 < stack.count {
                        stack[sp] = n.left; sp += 1
                        stack[sp] = n.right; sp += 1
                    }
                }
                return false
            }
        }
        }
    }
}

// MARK: - Main

let rayCount = 28
let radius: Float = 0.035

func manifestParts(_ url: URL) -> [[String: Any]] {
    guard let data = try? Data(contentsOf: url),
          let json = try? JSONSerialization.jsonObject(with: data) as? [String: Any] else { return [] }
    return json["parts"] as? [[String: Any]] ?? []
}

/// Sheets that the app hides by default (fasciae, pleura, peritoneum,
/// meninges, "covering" parts) must not darken the organs they wrap.
func coveringFlags(manifest url: URL) -> [Bool] {
    let words = ["pleura", "omentum", "mesocolon", "meso-appendix", "dura", "falx", "tentorium", "arachnoid", "pia mater"]
    return manifestParts(url).map { part in
        if part["fascia"] as? Bool == true || part["covering"] as? Bool == true { return true }
        let base = (part["base"] as? String ?? "").lowercased()
        if words.contains(where: { base.contains($0) }) { return true }
        let path = part["path"] as? [String] ?? []
        return path.contains("Meninges") || path.contains("Peritoneal structures")
    }
}

/// 1 for "sex": "m", 2 for "f", 0 otherwise.
func sexCodes(manifest url: URL) -> [UInt8] {
    manifestParts(url).map { part in
        switch part["sex"] as? String {
        case "m": 1
        case "f": 2
        default: 0
        }
    }
}

// Fixed cosine-weighted hemisphere directions (z-up), rotated per vertex.
var hemisphere: [SIMD3<Float>] = []
for k in 0..<rayCount {
    let u = (Float(k) + 0.5) / Float(rayCount)
    let phi = Float(k) * 2.399963 // golden angle
    let r = sqrt(u)
    hemisphere.append(SIMD3(r * cos(phi), r * sin(phi), sqrt(max(0, 1 - u))))
}

for path in CommandLine.arguments.dropFirst() {
    let url = URL(fileURLWithPath: path)
    let raw = inflate(try! Data(contentsOf: url))
    guard raw.prefix(4) == Data("ANT1".utf8) else {
        print("skip \(url.lastPathComponent) (not ANT1)")
        continue
    }
    let start = Date()
    let pack = readPack(raw)
    let scale = (pack.hi - pack.lo) / 65535
    let coverings = coveringFlags(manifest: url.deletingPathExtension().appendingPathExtension("json"))
    let sexes = sexCodes(manifest: url.deletingPathExtension().appendingPathExtension("json"))
    var vertexSex: [UInt8] = []

    var positions: [SIMD3<Float>] = []
    var normals: [SIMD3<Float>] = []
    var triangles: [Triangle] = []
    var bases: [Int] = []
    for (partIndex, part) in pack.parts.enumerated() {
        let base = positions.count
        let occludes = !(partIndex < coverings.count && coverings[partIndex])
        let sex = partIndex < sexes.count ? sexes[partIndex] : 0
        vertexSex.append(contentsOf: repeatElement(sex, count: part.vertexCount))
        bases.append(base)
        part.positionBytes.withUnsafeBytes { b in
            for v in 0..<part.vertexCount {
                let x = Float(b.loadUnaligned(fromByteOffset: v * 6, as: UInt16.self))
                let y = Float(b.loadUnaligned(fromByteOffset: v * 6 + 2, as: UInt16.self))
                let z = Float(b.loadUnaligned(fromByteOffset: v * 6 + 4, as: UInt16.self))
                positions.append(pack.lo + SIMD3(x, y, z) * scale)
            }
        }
        part.normalBytes.withUnsafeBytes { b in
            for v in 0..<part.vertexCount {
                let n = SIMD3<Float>(Float(Int8(bitPattern: b[v * 3])), Float(Int8(bitPattern: b[v * 3 + 1])), Float(Int8(bitPattern: b[v * 3 + 2])))
                normals.append(simd_length(n) > 0 ? simd_normalize(n) : SIMD3(0, 1, 0))
            }
        }
        let wide = part.vertexCount > 65535
        part.indexBytes.withUnsafeBytes { b in
            var i = 0
            while i < part.indexCount {
                func idx(_ k: Int) -> Int { wide ? Int(b.loadUnaligned(fromByteOffset: k * 4, as: UInt32.self)) : Int(b.loadUnaligned(fromByteOffset: k * 2, as: UInt16.self)) }
                if occludes {
                    let a = positions[base + idx(i)], bb = positions[base + idx(i + 1)], c = positions[base + idx(i + 2)]
                    triangles.append(Triangle(a: a, e1: bb - a, e2: c - a, sex: sex))
                }
                i += 3
            }
        }
    }

    let bvh = BVH(triangles)
    let mixed = Set(sexes).count > 1
    var ao = [UInt8](repeating: 255, count: positions.count)
    let chunk = 4096
    let chunks = (positions.count + chunk - 1) / chunk
    ao.withUnsafeMutableBufferPointer { out in
        let outPtr = out
        DispatchQueue.concurrentPerform(iterations: chunks) { c in
            for v in c * chunk..<min(positions.count, (c + 1) * chunk) {
                let n = normals[v]
                // orthonormal basis around the normal
                let t = abs(n.x) > 0.9 ? simd_normalize(simd_cross(n, SIMD3(0, 1, 0))) : simd_normalize(simd_cross(n, SIMD3(1, 0, 0)))
                let b = simd_cross(n, t)
                let o = positions[v] + n * 0.0006
                // Parts shared by both sexes: the mean of the male and the
                // female scene.
                let scenes: [UInt8] = vertexSex[v] != 0 || !mixed ? [vertexSex[v]] : [1, 2]
                var hits = 0
                for sex in scenes {
                    for h in hemisphere {
                        let d = t * h.x + b * h.y + n * h.z
                        if bvh.occluded(o, d, radius, sex: sex) { hits += 1 }
                    }
                }
                let open = 1 - Float(hits) / Float(rayCount * scenes.count)
                outPtr[v] = UInt8(max(0, min(255, (open * 255).rounded())))
            }
        }
    }

    var out = Data("ANT2".utf8)
    out.append(pack.header)
    for (i, part) in pack.parts.enumerated() {
        out.append(part.positionBytes)
        out.append(part.normalBytes)
        out.append(part.indexBytes)
        out.append(contentsOf: ao[bases[i]..<bases[i] + part.vertexCount])
    }
    try! deflate(out).write(to: url)
    let mean = ao.reduce(0) { $0 + Int($1) } / max(ao.count, 1)
    print(String(format: "%@: %d vertices, %d triangles, mean openness %d, %.1fs",
                 url.lastPathComponent, positions.count, triangles.count, mean, Date().timeIntervalSince(start)))
}
