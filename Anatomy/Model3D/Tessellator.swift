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
                typealias O = VertexBuilder.Offset

                func unit(_ v: SIMD3<Float>, _ fallback: SIMD3<Float>) -> SIMD3<Float> {
                    simd_length_squared(v) > 1e-12 ? simd_normalize(v) : fallback
                }

                func midpoint(_ a: UInt32, _ b: UInt32) -> UInt32 {
                    let key = a < b ? UInt64(a) << 32 | UInt64(b) : UInt64(b) << 32 | UInt64(a)
                    if let m = edges[key] { return m }
                    let ia = Int(a), ib = Int(b), m = next
                    next += 1
                    let pa = ia * stride, pb = ib * stride, pm = m * stride

                    // Colour, occlusion, fibre and wetness are averaged; the
                    // tissue kind, fibre axis and pattern are per part.
                    let ca = VertexBuilder.loadUnsigned(d, pa + O.color), cb = VertexBuilder.loadUnsigned(d, pb + O.color)
                    VertexBuilder.storeUnsigned((ca + cb) * 0.5, d, pm + O.color)
                    let ua = VertexBuilder.loadUnsigned(d, pa + O.uv1), ub = VertexBuilder.loadUnsigned(d, pb + O.uv1)
                    let um = (ua + ub) * 0.5
                    VertexBuilder.storeUnsigned(SIMD4(um.x, um.y, ua.z, ua.w), d, pm + O.uv1)
                    (d + pm + O.uv2).copyMemory(from: d + pa + O.uv2, byteCount: 4)
                    // Texture coordinates are interpolated where both ends have them.
                    let ta0 = d.loadUnaligned(fromByteOffset: pa + O.uv0, as: SIMD2<UInt16>.self)
                    let tb0 = d.loadUnaligned(fromByteOffset: pb + O.uv0, as: SIMD2<UInt16>.self)
                    var tm0 = SIMD2<UInt16>(0, 0)
                    if ta0 != .zero, tb0 != .zero {
                        tm0 = SIMD2(UInt16((UInt32(ta0.x) + UInt32(tb0.x)) / 2), UInt16((UInt32(ta0.y) + UInt32(tb0.y)) / 2))
                    }
                    d.storeBytes(of: tm0, toByteOffset: pm + O.uv0, as: SIMD2<UInt16>.self)

                    // Position and normal come from the curved patch.
                    let p0 = VertexBuilder.loadPosition(d, pa), p1 = VertexBuilder.loadPosition(d, pb)
                    let n0 = unit(VertexBuilder.loadSigned(d, pa + O.normal).xyz, SIMD3(0, 1, 0))
                    let n1 = unit(VertexBuilder.loadSigned(d, pb + O.normal).xyz, n0)
                    let e = p1 - p0
                    let b210 = (2 * p0 + p1 - simd_dot(e, n0) * n0) / 3
                    let b120 = (2 * p1 + p0 + simd_dot(e, n1) * n1) / 3
                    let position = (p0 + p1) / 8 + (b210 + b120) * (3.0 / 8.0)
                    let len2 = simd_length_squared(e)
                    var n110 = n0 + n1
                    if len2 > 1e-14 { n110 -= 2 * simd_dot(e, n0 + n1) / len2 * e }
                    let bend: SIMD3<Float> = unit(n110, .zero)
                    let normal = unit(n0 + n1 + bend, n0)
                    let ta = VertexBuilder.loadSigned(d, pa + O.tangent).xyz, tb = VertexBuilder.loadSigned(d, pb + O.tangent).xyz
                    var tangent = ta + tb
                    tangent -= simd_dot(tangent, normal) * normal
                    tangent = unit(tangent, ta)
                    VertexBuilder.storePosition(position, d, pm)
                    VertexBuilder.storeSigned(normal, 0, d, pm + O.normal)
                    VertexBuilder.storeSigned(tangent, 0, d, pm + O.tangent)

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
