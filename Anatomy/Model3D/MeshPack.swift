//
//  MeshPack.swift
//  Anatomy
//
//  Reads the per-system geometry packs produced by tools/export_zanatomy.py
//  (and tools/bake_ao.swift).
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
    /// Triangle runs per material: [[materialIndex, triangleCount], ...].
    let seg: [[Int]]?

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

    /// Sheets that wrap other structures (fasciae, pleura, peritoneal folds,
    /// meninges). They are hidden by default so the organs inside are visible.
    var isCovering: Bool {
        if isFascia { return true }
        let name = base.lowercased()
        let words = ["pleura", "omentum", "mesocolon", "meso-appendix", "dura", "falx", "tentorium", "arachnoid", "pia mater"]
        if words.contains(where: { name.contains($0) }) { return true }
        return path.contains { $0 == "Meninges" || $0 == "Peritoneal structures" }
    }

    /// Material index covering most of the part's triangles.
    var dominantMaterial: Int? {
        seg?.max { $0[1] < $1[1] }?.first
    }
}

nonisolated struct PackManifest: Decodable, Sendable {
    let system: String
    let materials: [String]?
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
    let materials: [String]
    let parts: [PartInfo]
    let ranges: [Range]
    let positions: [SIMD3<Float>]
    let normals: [SIMD3<Float>]
    /// Baked ambient occlusion per vertex (255 = open).
    let occlusion: [UInt8]
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

    static func load(system: String, manifest: PackManifest) throws -> MeshPack {
        guard let url = Bundle.main.url(forResource: "mesh-\(system)", withExtension: "bin") else {
            throw LoadError.missingResource("mesh-\(system).bin")
        }
        let compressed = try Data(contentsOf: url)
        let data = try (compressed as NSData).decompressed(using: .zlib) as Data
        return try decode(data, manifest: manifest)
    }

    /// Parses an inflated "ANT1"/"ANT2" pack.
    static func decode(_ data: Data, manifest: PackManifest) throws -> MeshPack {
        try data.withUnsafeBytes { raw in
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

        guard raw.count > 8, raw[0] == 0x41, raw[1] == 0x4E, raw[2] == 0x54, raw[3] == 0x31 || raw[3] == 0x32 else {
            throw LoadError.corrupt("bad magic")
        }
        let hasOcclusion = raw[3] == 0x32
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
        var occlusion = [UInt8]()
        var indices = [UInt32]()
        var ranges = [Range]()
        positions.reserveCapacity(totalVertices)
        normals.reserveCapacity(totalVertices)
        occlusion.reserveCapacity(totalVertices)
        indices.reserveCapacity(totalIndices)
        ranges.reserveCapacity(partCount)

        for (vertexCount, indexCount) in counts {
            let vertexStart = positions.count
            let indexStart = indices.count
            let wide = vertexCount > 65535
            let needed = vertexCount * (hasOcclusion ? 10 : 9) + indexCount * (wide ? 4 : 2)
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

            if hasOcclusion {
                occlusion.append(contentsOf: UnsafeRawBufferPointer(rebasing: raw[cursor..<cursor + vertexCount]))
                cursor += vertexCount
            } else {
                occlusion.append(contentsOf: repeatElement(255, count: vertexCount))
            }
            ranges.append(Range(vertexStart: vertexStart, vertexCount: vertexCount, indexStart: indexStart, indexCount: indexCount))
        }

        return MeshPack(
            system: manifest.system,
            materials: manifest.materials ?? [],
            parts: manifest.parts,
            ranges: ranges,
            positions: positions,
            normals: normals,
            occlusion: occlusion,
            indices: indices
        )
    }
}

/// High-detail replacements for single parts (tools/build_hd.py), used by the
/// specimen viewer. Each part is compressed on its own ("ANH1", see
/// tools/pack_hd.py) so opening a femur inflates only the femur.
nonisolated final class DetailLibrary: @unchecked Sendable {
    static let shared = DetailLibrary()

    private struct System {
        let file: Data
        let materials: [String]
        /// LOD part index -> (high-detail part info, offset, length)
        let parts: [Int: (PartInfo, Int, Int)]
    }

    private let lock = NSLock()
    private var systems: [String: System?] = [:]

    /// The high-detail mesh standing in for part `index` of `system`, if any.
    func pack(system: String, index: Int) -> MeshPack? {
        guard let sys = load(system), let (info, offset, length) = sys.parts[index] else { return nil }
        let slice = sys.file.subdata(in: offset..<offset + length)
        guard let data = try? (slice as NSData).decompressed(using: .zlib) as Data else { return nil }
        return try? MeshPack.decode(data, manifest: PackManifest(system: system, materials: sys.materials, parts: [info]))
    }

    func hasDetail(system: String, index: Int) -> Bool {
        load(system)?.parts[index] != nil
    }

    private func load(_ system: String) -> System? {
        lock.lock()
        defer { lock.unlock() }
        if let cached = systems[system] { return cached }
        var result: System?
        if let bin = Bundle.main.url(forResource: "hd-\(system)", withExtension: "bin"),
           let json = Bundle.main.url(forResource: "hd-\(system)", withExtension: "json"),
           let file = try? Data(contentsOf: bin, options: .alwaysMapped),
           let manifestData = try? Data(contentsOf: json),
           let manifest = try? JSONDecoder().decode(PackManifest.self, from: manifestData),
           let links = try? JSONDecoder().decode(Links.self, from: manifestData),
           file.count > 8, file.prefix(4) == Data("ANH1".utf8) {
            let count = Int(file.withUnsafeBytes { $0.loadUnaligned(fromByteOffset: 4, as: UInt32.self) })
            var parts: [Int: (PartInfo, Int, Int)] = [:]
            if count == manifest.parts.count, count == links.parts.count, file.count >= 8 + count * 8 {
                file.withUnsafeBytes { raw in
                    for k in 0..<count {
                        let offset = Int(raw.loadUnaligned(fromByteOffset: 8 + k * 8, as: UInt32.self))
                        let length = Int(raw.loadUnaligned(fromByteOffset: 12 + k * 8, as: UInt32.self))
                        guard offset + length <= file.count else { continue }
                        parts[links.parts[k].lod] = (manifest.parts[k], offset, length)
                    }
                }
            }
            result = System(file: file, materials: manifest.materials ?? [], parts: parts)
        }
        systems[system] = .some(result)
        return result
    }

    private struct Links: Decodable {
        struct Link: Decodable { let lod: Int }
        let parts: [Link]
    }
}
