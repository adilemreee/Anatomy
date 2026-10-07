//
//  MeshPack.swift
//  Anatomy
//
//  Reads the per-system geometry packs produced by tools/export_zanatomy.py.
//

import Foundation
import simd

/// Metadata for one 3D part, read from `mesh-<system>.json`.
nonisolated struct PartInfo: Decodable, Hashable, Sendable {
    /// Full Z-Anatomy object name, e.g. "Femur.l".
    let name: String
    /// Name without the side suffix, e.g. "Femur".
    let base: String
    /// Ancestor groups from the outermost to the direct parent.
    let path: [String]
    /// minX, minY, minZ, maxX, maxY, maxZ in model space.
    let bounds: [Float]
    let tris: Int
    let side: String?
    /// "origin" / "insertion" for muscle attachment patches.
    let kind: String?
    let color: String?
    let fascia: Bool?

    var center: SIMD3<Float> {
        SIMD3((bounds[0] + bounds[3]) / 2, (bounds[1] + bounds[4]) / 2, (bounds[2] + bounds[5]) / 2)
    }

    var extent: SIMD3<Float> {
        SIMD3(bounds[3] - bounds[0], bounds[4] - bounds[1], bounds[5] - bounds[2])
    }

    var sideTitle: String? {
        switch side {
        case "l": "Sol"
        case "r": "Sağ"
        default: nil
        }
    }

    var isFascia: Bool { fascia ?? false }
}

nonisolated struct PackManifest: Decodable, Sendable {
    let system: String
    let parts: [PartInfo]
}

/// Decoded geometry for one system: every part's vertices and triangles laid
/// out back to back so they can be uploaded into a single `LowLevelMesh`.
nonisolated struct MeshPack: Sendable {
    struct Range: Sendable {
        let vertexStart: Int
        let vertexCount: Int
        let indexStart: Int
        let indexCount: Int
    }

    let system: String
    let parts: [PartInfo]
    let ranges: [Range]
    let positions: [SIMD3<Float>]
    let normals: [SIMD3<Float>]
    /// Global vertex indices (already offset by each part's `vertexStart`).
    let indices: [UInt32]

    enum LoadError: Error {
        case missingResource(String)
        case corrupt(String)
    }

    static func manifest(for system: String) throws -> PackManifest {
        guard let url = Bundle.main.url(forResource: "mesh-\(system)", withExtension: "json") else {
            throw LoadError.missingResource("mesh-\(system).json")
        }
        return try JSONDecoder().decode(PackManifest.self, from: Data(contentsOf: url))
    }

    static func load(system: String) throws -> MeshPack {
        let manifest = try manifest(for: system)
        guard let url = Bundle.main.url(forResource: "mesh-\(system)", withExtension: "bin") else {
            throw LoadError.missingResource("mesh-\(system).bin")
        }
        let compressed = try Data(contentsOf: url)
        let data = try (compressed as NSData).decompressed(using: .zlib) as Data
        return try data.withUnsafeBytes { raw in
            try parse(raw, manifest: manifest)
        }
    }

    private static func parse(_ raw: UnsafeRawBufferPointer, manifest: PackManifest) throws -> MeshPack {
        var cursor = 0
        func read<T>(_: T.Type) throws -> T {
            let size = MemoryLayout<T>.size
            guard cursor + size <= raw.count else { throw LoadError.corrupt("unexpected end of data") }
            defer { cursor += size }
            return raw.loadUnaligned(fromByteOffset: cursor, as: T.self)
        }

        guard raw.count > 8, raw[0] == 0x41, raw[1] == 0x4E, raw[2] == 0x54, raw[3] == 0x31 else {
            throw LoadError.corrupt("bad magic")
        }
        cursor = 4
        let partCount = Int(try read(UInt32.self))
        guard partCount == manifest.parts.count else {
            throw LoadError.corrupt("part count \(partCount) does not match manifest \(manifest.parts.count)")
        }
        let lo = SIMD3<Float>(try read(Float.self), try read(Float.self), try read(Float.self))
        let hi = SIMD3<Float>(try read(Float.self), try read(Float.self), try read(Float.self))
        let scale = (hi - lo) / 65535

        var counts: [(Int, Int)] = []
        counts.reserveCapacity(partCount)
        var totalVertices = 0
        var totalIndices = 0
        for _ in 0..<partCount {
            let v = Int(try read(UInt32.self))
            let i = Int(try read(UInt32.self))
            counts.append((v, i))
            totalVertices += v
            totalIndices += i
        }

        var positions = [SIMD3<Float>]()
        var normals = [SIMD3<Float>]()
        var indices = [UInt32]()
        var ranges = [Range]()
        positions.reserveCapacity(totalVertices)
        normals.reserveCapacity(totalVertices)
        indices.reserveCapacity(totalIndices)
        ranges.reserveCapacity(partCount)

        for (vertexCount, indexCount) in counts {
            let vertexStart = positions.count
            let indexStart = indices.count
            let wide = vertexCount > 65535
            let needed = vertexCount * 9 + indexCount * (wide ? 4 : 2)
            guard cursor + needed <= raw.count else { throw LoadError.corrupt("truncated part") }

            for v in 0..<vertexCount {
                let o = cursor + v * 6
                let x = Float(raw.loadUnaligned(fromByteOffset: o, as: UInt16.self))
                let y = Float(raw.loadUnaligned(fromByteOffset: o + 2, as: UInt16.self))
                let z = Float(raw.loadUnaligned(fromByteOffset: o + 4, as: UInt16.self))
                positions.append(lo + SIMD3(x, y, z) * scale)
            }
            cursor += vertexCount * 6

            for v in 0..<vertexCount {
                let o = cursor + v * 3
                let n = SIMD3<Float>(
                    Float(Int8(bitPattern: raw[o])),
                    Float(Int8(bitPattern: raw[o + 1])),
                    Float(Int8(bitPattern: raw[o + 2]))
                )
                let length = simd_length(n)
                normals.append(length > 0 ? n / length : SIMD3(0, 1, 0))
            }
            cursor += vertexCount * 3

            let base = UInt32(vertexStart)
            if wide {
                for i in 0..<indexCount {
                    indices.append(base + raw.loadUnaligned(fromByteOffset: cursor + i * 4, as: UInt32.self))
                }
                cursor += indexCount * 4
            } else {
                for i in 0..<indexCount {
                    indices.append(base + UInt32(raw.loadUnaligned(fromByteOffset: cursor + i * 2, as: UInt16.self)))
                }
                cursor += indexCount * 2
            }
            ranges.append(Range(vertexStart: vertexStart, vertexCount: vertexCount, indexStart: indexStart, indexCount: indexCount))
        }

        return MeshPack(
            system: manifest.system,
            parts: manifest.parts,
            ranges: ranges,
            positions: positions,
            normals: normals,
            indices: indices
        )
    }
}
