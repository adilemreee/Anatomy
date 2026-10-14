//
//  PackLibrary.swift
//  Anatomy
//
//  Shared cache of part manifests and decoded mesh packs, plus the vertex
//  buffer builder used by the atlas and the small structure previews.
//

import Foundation
import simd

/// Decodes each system's geometry once and shares it between scenes.
@MainActor
final class PackLibrary {
    static let shared = PackLibrary()

    let manifests: [String: PackManifest]
    private var packs: [String: MeshPack] = [:]
    private var loading: [String: Task<MeshPack, Error>] = [:]

    private init() {
        var manifests: [String: PackManifest] = [:]
        for layer in ModelLayer.all {
            if let manifest = try? MeshPack.manifest(for: layer.id) {
                manifests[layer.id] = manifest
            }
        }
        self.manifests = manifests
    }

    func parts(_ system: String) -> [PartInfo] { manifests[system]?.parts ?? [] }
    func materials(_ system: String) -> [String] { manifests[system]?.materials ?? [] }

    func cachedPack(_ system: String) -> MeshPack? { packs[system] }

    func pack(_ system: String) async throws -> MeshPack {
        if let pack = packs[system] { return pack }
        if let task = loading[system] { return try await task.value }
        guard let manifest = manifests[system] else { throw MeshPack.LoadError.missingResource(system) }
        let task = Task.detached(priority: .userInitiated) {
            try MeshPack.load(system: system, manifest: manifest)
        }
        loading[system] = task
        defer { loading[system] = nil }
        let pack = try await task.value
        packs[system] = pack
        return pack
    }
}

/// Interleaved vertex data in the layout the surface shader expects.
nonisolated enum VertexBuilder {
    /// 36 bytes per vertex:
    ///  0 position   float3
    /// 12 normal     char4 normalised (xyz)
    /// 16 tangent    char4 normalised (xyz, the fibre direction on the surface)
    /// 20 color      uchar4 normalised (linear rgb, a = baked occlusion)
    /// 24 uv1        uchar4 normalised (fibre strength, wetness, tissue / 255, -)
    /// 28 uv2        char4 normalised (the part's fibre axis xyz, surface pattern / 4)
    /// 32 uv0        ushort2 normalised (skin texture coordinates, 0 = none)
    static let stride = 36

    enum Offset {
        static let position = 0, normal = 12, tangent = 16, color = 20, uv1 = 24, uv2 = 28, uv0 = 32
    }

    struct Output: Sendable {
        var vertices: Data
        var indices: [UInt32]
        /// Index range of each requested part inside `indices`.
        var ranges: [(start: Int, count: Int)]
        var bounds: [(SIMD3<Float>, SIMD3<Float>)]
    }

    /// Builds vertex data for `parts` (all parts when nil). When a subset is
    /// requested the vertices are compacted and the indices rebased; the full
    /// build also carries the simplified levels after the full-detail indices.
    static func build(pack: MeshPack, parts subset: [Int]? = nil, mode: ColorMode) -> Output {
        let partIndices = subset ?? Array(pack.parts.indices)
        let compact = subset != nil
        let vertexTotal = compact ? partIndices.reduce(0) { $0 + pack.ranges[$1].vertexCount } : pack.positions.count
        var data = Data(count: vertexTotal * stride)
        var indices: [UInt32] = compact ? [] : pack.indices + pack.lodIndices
        if compact { indices.reserveCapacity(partIndices.reduce(0) { $0 + pack.ranges[$1].indexCount }) }
        var ranges: [(Int, Int)] = []
        var bounds: [(SIMD3<Float>, SIMD3<Float>)] = []
        let textured = mode == .realistic && pack.uvs.count == pack.positions.count

        data.withUnsafeMutableBytes { raw in
            var outVertex = 0
            for p in partIndices {
                let part = pack.parts[p]
                let range = pack.ranges[p]
                let styles = styles(for: part, pack: pack, mode: mode)
                // Per-vertex style index, written by every triangle of each run.
                var styleOf = [UInt8](repeating: UInt8(styles.dominant), count: range.vertexCount)
                var tri = range.indexStart
                for (s, run) in styles.runs.enumerated() {
                    for _ in 0..<run {
                        for k in 0..<3 {
                            styleOf[Int(pack.indices[tri + k]) - range.vertexStart] = UInt8(s)
                        }
                        tri += 3
                    }
                }
                let axis = styles.needsAxis ? principalAxis(pack: pack, range: range) : nil
                let variation = partVariation(part.name)

                var lo = SIMD3<Float>(repeating: .greatestFiniteMagnitude), hi = -lo
                for v in 0..<range.vertexCount {
                    let src = range.vertexStart + v
                    let position = pack.positions[src]
                    let normal = pack.normals[src]
                    lo = simd_min(lo, position); hi = simd_max(hi, position)
                    let style = styles.list[Int(styleOf[v])]
                    // Pattern and tissue share one signed byte: pattern * 16 + tissue.
                    let surfaceCode = (style.pattern * 16 + style.tissue) / 127
                    var tangent = SIMD3<Float>(1, 0, 0)
                    if let axis {
                        let t = axis - normal * simd_dot(axis, normal)
                        let len = simd_length(t)
                        tangent = len > 1e-4 ? t / len : perpendicular(normal)
                    } else {
                        tangent = perpendicular(normal)
                    }
                    var color = style.color * (1 + (variation - 0.5) * 2 * style.variation)
                    color = simd_clamp(color, .zero, SIMD3(repeating: 1))
                    let linear = SIMD3<Float>(pow(color.x, 2.2), pow(color.y, 2.2), pow(color.z, 2.2))

                    let o = ((compact ? outVertex : range.vertexStart) + v) * stride
                    raw.storeBytes(of: position.x, toByteOffset: o, as: Float.self)
                    raw.storeBytes(of: position.y, toByteOffset: o + 4, as: Float.self)
                    raw.storeBytes(of: position.z, toByteOffset: o + 8, as: Float.self)
                    storeSigned(normal, 0, raw, o + Offset.normal)
                    storeSigned(tangent, 0, raw, o + Offset.tangent)
                    storeUnsigned(SIMD4(linear, 0), raw, o + Offset.color)
                    raw.storeBytes(of: pack.occlusion[src], toByteOffset: o + Offset.color + 3, as: UInt8.self)
                    storeUnsigned(SIMD4(style.fibre, style.wetness, 0, 0), raw, o + Offset.uv1)
                    storeSigned(axis ?? tangent, surfaceCode, raw, o + Offset.uv2)
                    // The skin texture is the realistic look; teaching colours keep the regions apart.
                    raw.storeBytes(of: textured ? pack.uvs[src] : 0, toByteOffset: o + Offset.uv0, as: UInt32.self)
                }
                bounds.append((lo, hi))

                if compact {
                    let start = indices.count
                    let rebase = Int64(outVertex) - Int64(range.vertexStart)
                    for i in range.indexStart..<range.indexStart + range.indexCount {
                        indices.append(UInt32(Int64(pack.indices[i]) + rebase))
                    }
                    ranges.append((start, range.indexCount))
                    outVertex += range.vertexCount
                } else {
                    ranges.append((range.indexStart, range.indexCount))
                }
            }
        }
        return Output(vertices: data, indices: indices, ranges: ranges, bounds: bounds)
    }

    // MARK: Packed attributes

    static func storeSigned(_ v: SIMD3<Float>, _ w: Float, _ raw: UnsafeMutableRawBufferPointer, _ offset: Int) {
        storeSigned(v, w, raw.baseAddress!, offset)
    }

    static func storeUnsigned(_ v: SIMD4<Float>, _ raw: UnsafeMutableRawBufferPointer, _ offset: Int) {
        storeUnsigned(v, raw.baseAddress!, offset)
    }

    /// Four signed normalised bytes (-1…1).
    static func storeSigned(_ v: SIMD3<Float>, _ w: Float, _ p: UnsafeMutableRawPointer, _ offset: Int) {
        let q = simd_clamp(SIMD4(v, w) * 127, SIMD4(repeating: -127), SIMD4(repeating: 127)).rounded(.toNearestOrAwayFromZero)
        p.storeBytes(of: SIMD4<Int8>(Int8(q.x), Int8(q.y), Int8(q.z), Int8(q.w)), toByteOffset: offset, as: SIMD4<Int8>.self)
    }

    /// Four unsigned normalised bytes (0…1).
    static func storeUnsigned(_ v: SIMD4<Float>, _ p: UnsafeMutableRawPointer, _ offset: Int) {
        let q = simd_clamp(v * 255, SIMD4(repeating: 0), SIMD4(repeating: 255)).rounded(.toNearestOrAwayFromZero)
        p.storeBytes(of: SIMD4<UInt8>(UInt8(q.x), UInt8(q.y), UInt8(q.z), UInt8(q.w)), toByteOffset: offset, as: SIMD4<UInt8>.self)
    }

    static func loadSigned(_ p: UnsafeRawPointer, _ offset: Int) -> SIMD4<Float> {
        let b = p.loadUnaligned(fromByteOffset: offset, as: SIMD4<Int8>.self)
        return SIMD4(Float(b.x), Float(b.y), Float(b.z), Float(b.w)) / 127
    }

    static func loadUnsigned(_ p: UnsafeRawPointer, _ offset: Int) -> SIMD4<Float> {
        let b = p.loadUnaligned(fromByteOffset: offset, as: SIMD4<UInt8>.self)
        return SIMD4(Float(b.x), Float(b.y), Float(b.z), Float(b.w)) / 255
    }

    static func loadPosition(_ p: UnsafeRawPointer, _ offset: Int) -> SIMD3<Float> {
        SIMD3(p.loadUnaligned(fromByteOffset: offset, as: Float.self),
              p.loadUnaligned(fromByteOffset: offset + 4, as: Float.self),
              p.loadUnaligned(fromByteOffset: offset + 8, as: Float.self))
    }

    static func storePosition(_ v: SIMD3<Float>, _ p: UnsafeMutableRawPointer, _ offset: Int) {
        p.storeBytes(of: v.x, toByteOffset: offset, as: Float.self)
        p.storeBytes(of: v.y, toByteOffset: offset + 4, as: Float.self)
        p.storeBytes(of: v.z, toByteOffset: offset + 8, as: Float.self)
    }

    private struct PartStyles {
        var list: [SurfaceStyle]
        /// Triangle count of each run, in order.
        var runs: [Int]
        var dominant: Int
        var needsAxis: Bool
    }

    private static func styles(for part: PartInfo, pack: MeshPack, mode: ColorMode) -> PartStyles {
        let seg = part.seg ?? [[0, part.tris]]
        var list: [SurfaceStyle] = []
        var runs: [Int] = []
        var dominant = 0
        var best = -1
        for (i, run) in seg.enumerated() where run.count == 2 {
            let material = pack.materials.indices.contains(run[0]) ? pack.materials[run[0]] : ""
            list.append(MaterialStyles.style(material: material, part: part, layer: pack.system, mode: mode))
            runs.append(run[1])
            if run[1] > best { best = run[1]; dominant = i }
        }
        if list.isEmpty {
            list = [MaterialStyles.style(material: "", part: part, layer: pack.system, mode: mode)]
            runs = [part.tris]
        }
        return PartStyles(list: list, runs: runs, dominant: dominant, needsAxis: list.contains { $0.fibre > 0.01 })
    }

    /// Longest direction of the part (power iteration on the covariance).
    private static func principalAxis(pack: MeshPack, range: MeshPack.Range) -> SIMD3<Float> {
        let step = max(1, range.vertexCount / 1500)
        var mean = SIMD3<Float>.zero
        var n: Float = 0
        var v = range.vertexStart
        while v < range.vertexStart + range.vertexCount {
            mean += pack.positions[v]; n += 1; v += step
        }
        mean /= max(n, 1)
        var c = simd_float3x3(0)
        v = range.vertexStart
        while v < range.vertexStart + range.vertexCount {
            let d = pack.positions[v] - mean
            c += simd_float3x3(columns: (d * d.x, d * d.y, d * d.z))
            v += step
        }
        var axis = SIMD3<Float>(0.3, 1, 0.2)
        for _ in 0..<12 {
            let next = c * axis
            let len = simd_length(next)
            if len < 1e-12 { break }
            axis = next / len
        }
        return simd_normalize(axis)
    }

    private static func perpendicular(_ n: SIMD3<Float>) -> SIMD3<Float> {
        let a: SIMD3<Float> = abs(n.y) < 0.9 ? SIMD3(0, 1, 0) : SIMD3(1, 0, 0)
        return simd_normalize(simd_cross(a, n))
    }

    /// Stable 0…1 value per part for subtle colour variation.
    private static func partVariation(_ name: String) -> Float {
        var hash: UInt32 = 2166136261
        for byte in name.utf8 { hash = (hash ^ UInt32(byte)) &* 16777619 }
        return Float(hash % 1000) / 999
    }
}

extension SIMD4 where Scalar == Float {
    nonisolated var xyz: SIMD3<Float> { SIMD3(x, y, z) }
}
