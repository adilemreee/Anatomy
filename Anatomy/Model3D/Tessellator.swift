//
//  Tessellator.swift
//  Anatomy
//
//  Smooth subdivision for the specimen viewer. Z-Anatomy's meshes are light
//  (a femur has under 4 000 triangles), which shows as facets and polygonal
//  outlines when one structure fills the screen. Each level splits every
//  triangle in four and lifts the new edge points onto the curved
//  point-normal triangle through the corners (Vlachos et al., "Curved PN
//  Triangles", 2001). Edge points depend only on the edge's two vertices, so
//  neighbouring triangles stay watertight.
//

import Foundation
import simd

nonisolated enum Tessellator {
    /// Subdivides `levels` times, stopping early once `maxTriangles` would be exceeded.
    static func smooth(vertices: Data, indices: [UInt32], maxTriangles: Int, levels: Int = 2) -> (Data, [UInt32]) {
        var data = vertices, idx = indices
        for _ in 0..<levels where (idx.count / 3) * 4 <= maxTriangles {
            (data, idx) = subdivide(vertices: data, indices: idx)
        }
        return (data, idx)
    }

    /// One level of PN-triangle subdivision on `VertexBuilder` vertex data.
    static func subdivide(vertices: Data, indices: [UInt32]) -> (Data, [UInt32]) {
        let stride = VertexBuilder.stride
        let vertexCount = vertices.count / stride
        // Every new vertex sits on an edge; a closed mesh has 1.5 edges per triangle.
        var out = [UInt8](repeating: 0, count: (vertexCount + indices.count) * stride)
        var next = vertexCount
        var edges = [UInt64: UInt32](minimumCapacity: indices.count / 2 + 16)
        var newIndices = [UInt32]()
        newIndices.reserveCapacity(indices.count * 4)

        vertices.withUnsafeBytes { src in
            out.withUnsafeMutableBytes { dst in
                guard let s = src.baseAddress, let d = dst.baseAddress else { return }
                d.copyMemory(from: s, byteCount: vertices.count)

                func vec(_ i: Int, _ offset: Int) -> SIMD3<Float> {
                    let p = d + i * stride + offset
                    return SIMD3(p.loadUnaligned(as: Float.self), (p + 4).loadUnaligned(as: Float.self), (p + 8).loadUnaligned(as: Float.self))
                }
                func store(_ v: SIMD3<Float>, _ i: Int, _ offset: Int) {
                    let p = d + i * stride + offset
                    p.storeBytes(of: v.x, as: Float.self)
                    (p + 4).storeBytes(of: v.y, as: Float.self)
                    (p + 8).storeBytes(of: v.z, as: Float.self)
                }

                func midpoint(_ a: UInt32, _ b: UInt32) -> UInt32 {
                    let key = a < b ? UInt64(a) << 32 | UInt64(b) : UInt64(b) << 32 | UInt64(a)
                    if let m = edges[key] { return m }
                    let ia = Int(a), ib = Int(b), m = next
                    next += 1

                    // Every attribute starts as the average of the two ends …
                    let pa = d + ia * stride, pb = d + ib * stride, pm = d + m * stride
                    for offset in Swift.stride(from: 24, to: stride, by: 4) where offset != 36 {
                        let v = ((pa + offset).loadUnaligned(as: Float.self) + (pb + offset).loadUnaligned(as: Float.self)) * 0.5
                        (pm + offset).storeBytes(of: v, as: Float.self)
                    }
                    for k in 36..<40 {
                        (pm + k).storeBytes(of: UInt8((UInt16(pa.load(fromByteOffset: k, as: UInt8.self)) + UInt16(pb.load(fromByteOffset: k, as: UInt8.self)) + 1) / 2), as: UInt8.self)
                    }

                    // … then position and normal come from the curved patch.
                    let p0 = vec(ia, 0), p1 = vec(ib, 0)
                    let n0 = simd_normalize(vec(ia, 12)), n1 = simd_normalize(vec(ib, 12))
                    let e = p1 - p0
                    let b210 = (2 * p0 + p1 - simd_dot(e, n0) * n0) / 3
                    let b120 = (2 * p1 + p0 + simd_dot(e, n1) * n1) / 3
                    let position = (p0 + p1) / 8 + (b210 + b120) * (3.0 / 8.0)
                    let len2 = simd_length_squared(e)
                    var n110 = n0 + n1
                    if len2 > 1e-14 { n110 -= 2 * simd_dot(e, n0 + n1) / len2 * e }
                    var normal = n0 + n1 + (simd_length_squared(n110) > 1e-12 ? simd_normalize(n110) : .zero)
                    normal = simd_length_squared(normal) > 1e-12 ? simd_normalize(normal) : n0
                    var tangent = vec(m, 24)
                    tangent -= simd_dot(tangent, normal) * normal
                    tangent = simd_length_squared(tangent) > 1e-12 ? simd_normalize(tangent) : vec(ia, 24)
                    store(position, m, 0)
                    store(normal, m, 12)
                    store(tangent, m, 24)

                    edges[key] = UInt32(m)
                    return UInt32(m)
                }

                var t = 0
                while t + 2 < indices.count {
                    let a = indices[t], b = indices[t + 1], c = indices[t + 2]
                    t += 3
                    let ab = midpoint(a, b), bc = midpoint(b, c), ca = midpoint(c, a)
                    newIndices.append(contentsOf: [a, ab, ca, ab, b, bc, ca, bc, c, ab, bc, ca])
                }
            }
        }
        return (Data(out.prefix(next * stride)), newIndices)
    }
}
