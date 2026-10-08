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
    /// position f3 | normal f3 | tangent f3 | color rgba8 (a = occlusion) | uv1 f2 | uv2 f4 (fibre axis, pattern)
    static let stride = 64

    struct Output: Sendable {
        var vertices: Data
        var indices: [UInt32]
        /// Index range of each requested part inside `indices`.
        var ranges: [(start: Int, count: Int)]
        var bounds: [(SIMD3<Float>, SIMD3<Float>)]
    }

    /// Builds vertex data for `parts` (all parts when nil). When a subset is
    /// requested the vertices are compacted and the indices rebased.
    static func build(pack: MeshPack, parts subset: [Int]? = nil, mode: ColorMode) -> Output {
        let partIndices = subset ?? Array(pack.parts.indices)
        let compact = subset != nil
        let vertexTotal = compact ? partIndices.reduce(0) { $0 + pack.ranges[$1].vertexCount } : pack.positions.count
        var data = Data(count: vertexTotal * stride)
        var indices: [UInt32] = compact ? [] : pack.indices
        if compact { indices.reserveCapacity(partIndices.reduce(0) { $0 + pack.ranges[$1].indexCount }) }
        var ranges: [(Int, Int)] = []
        var bounds: [(SIMD3<Float>, SIMD3<Float>)] = []

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
                    raw.storeBytes(of: normal.x, toByteOffset: o + 12, as: Float.self)
                    raw.storeBytes(of: normal.y, toByteOffset: o + 16, as: Float.self)
                    raw.storeBytes(of: normal.z, toByteOffset: o + 20, as: Float.self)
                    raw.storeBytes(of: tangent.x, toByteOffset: o + 24, as: Float.self)
                    raw.storeBytes(of: tangent.y, toByteOffset: o + 28, as: Float.self)
                    raw.storeBytes(of: tangent.z, toByteOffset: o + 32, as: Float.self)
                    raw.storeBytes(of: UInt8((linear.x * 255).rounded()), toByteOffset: o + 36, as: UInt8.self)
                    raw.storeBytes(of: UInt8((linear.y * 255).rounded()), toByteOffset: o + 37, as: UInt8.self)
                    raw.storeBytes(of: UInt8((linear.z * 255).rounded()), toByteOffset: o + 38, as: UInt8.self)
                    raw.storeBytes(of: pack.occlusion[src], toByteOffset: o + 39, as: UInt8.self)
                    raw.storeBytes(of: style.fibre, toByteOffset: o + 40, as: Float.self)
                    raw.storeBytes(of: style.wetness, toByteOffset: o + 44, as: Float.self)
                    let fibreAxis = axis ?? tangent
                    raw.storeBytes(of: fibreAxis.x, toByteOffset: o + 48, as: Float.self)
                    raw.storeBytes(of: fibreAxis.y, toByteOffset: o + 52, as: Float.self)
                    raw.storeBytes(of: fibreAxis.z, toByteOffset: o + 56, as: Float.self)
                    raw.storeBytes(of: style.pattern, toByteOffset: o + 60, as: Float.self)
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
