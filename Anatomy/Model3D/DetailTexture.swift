//
//  DetailTexture.swift
//  Anatomy
//
//  The tiling detail texture behind every surface (see AnatomyShaders.metal):
//    r  broad mottling (fbm of value noise)
//    g  fine isotropic grain (muscle fascicles, bone pores, specks)
//    b  cell borders (lobules of lung, liver, glands and fat)
//  Generated once at launch instead of evaluating noise per pixel, which
//  kept the GPU of older phones busy on every frame.
//

import CoreGraphics
import Foundation
import RealityKit

nonisolated enum DetailTexture {
    static let size = 512

    /// RGBX bytes of the tile; every channel wraps around seamlessly.
    static func pixels() -> [UInt8] {
        let n = size
        var out = [UInt8](repeating: 255, count: n * n * 4)
        let borderPeriod = 10
        let cellPoints = cellCentres(period: borderPeriod, seed: 0x5bd1e995)
        out.withUnsafeMutableBufferPointer { buffer in
            for y in 0..<n {
                let v = (Float(y) + 0.5) / Float(n)
                for x in 0..<n {
                    let u = (Float(x) + 0.5) / Float(n)
                    let mottle = 0.5 * noise(u, v, period: 4, seed: 11) + 0.25 * noise(u, v, period: 8, seed: 23)
                        + 0.15 * noise(u, v, period: 16, seed: 37) + 0.1 * noise(u, v, period: 32, seed: 41)
                    let grain = 0.65 * noise(u, v, period: 32, seed: 53) + 0.35 * noise(u, v, period: 96, seed: 67)
                    let border = cellBorder(u, v, period: borderPeriod, points: cellPoints)
                    let o = (y * n + x) * 4
                    buffer[o] = byte(stretch(mottle, 0.5, 1.7))
                    buffer[o + 1] = byte(stretch(grain, 0.5, 1.9))
                    buffer[o + 2] = byte(border)
                }
            }
        }
        return out
    }

    @MainActor private static var cached: TextureResource?

    /// The texture with a full mip chain, in linear (raw) colour space.
    @MainActor static func resource() async -> TextureResource? {
        if let cached { return cached }
        let bytes = await Task.detached(priority: .userInitiated) { pixels() }.value
        guard let provider = CGDataProvider(data: Data(bytes) as CFData),
              let image = CGImage(width: size, height: size, bitsPerComponent: 8, bitsPerPixel: 32, bytesPerRow: size * 4,
                                  space: CGColorSpaceCreateDeviceRGB(),
                                  bitmapInfo: CGBitmapInfo(rawValue: CGImageAlphaInfo.noneSkipLast.rawValue),
                                  provider: provider, decode: nil, shouldInterpolate: true, intent: .defaultIntent) else { return nil }
        let texture = try? await TextureResource(image: image, options: .init(semantic: .raw, mipmapsMode: .allocateAndGenerateAll))
        cached = texture
        return texture
    }

    // MARK: Noise

    private static func byte(_ v: Float) -> UInt8 { UInt8(max(0, min(255, (v * 255).rounded()))) }

    /// Spreads values around `mid` so the shader gets usable contrast.
    private static func stretch(_ v: Float, _ mid: Float, _ gain: Float) -> Float {
        max(0, min(1, (v - mid) * gain + 0.5))
    }

    private static func hash(_ x: Int, _ y: Int, _ seed: UInt32) -> UInt32 {
        var h = UInt32(truncatingIfNeeded: x &* 374_761_393 &+ y &* 668_265_263) ^ seed &* 2_654_435_761
        h = (h ^ (h >> 13)) &* 1_274_126_177
        return h ^ (h >> 16)
    }

    private static func unit(_ h: UInt32) -> Float { Float(h & 0xFFFF) / 65535 }

    /// Periodic value noise on a `period` × `period` lattice over the tile.
    private static func noise(_ u: Float, _ v: Float, period: Int, seed: UInt32) -> Float {
        let x = u * Float(period), y = v * Float(period)
        let xf = x.rounded(.down), yf = y.rounded(.down)
        let xi = Int(xf), yi = Int(yf)
        let fx = x - xf, fy = y - yf
        let sx = fx * fx * (3 - 2 * fx), sy = fy * fy * (3 - 2 * fy)
        func at(_ i: Int, _ j: Int) -> Float {
            unit(hash((i % period + period) % period, (j % period + period) % period, seed))
        }
        let a = at(xi, yi), b = at(xi + 1, yi), c = at(xi, yi + 1), d = at(xi + 1, yi + 1)
        return (a + (b - a) * sx) + ((c + (d - c) * sx) - (a + (b - a) * sx)) * sy
    }

    /// One jittered point per cell of a periodic grid.
    private static func cellCentres(period: Int, seed: UInt32) -> [SIMD2<Float>] {
        (0..<period * period).map { k in
            let i = k % period, j = k / period
            let h = hash(i, j, seed)
            return SIMD2(Float(i) + 0.15 + 0.7 * unit(h), Float(j) + 0.15 + 0.7 * unit(h >> 7 ^ h << 9))
        }
    }

    /// 1 on the borders between Voronoi cells, falling to 0 inside them.
    private static func cellBorder(_ u: Float, _ v: Float, period: Int, points: [SIMD2<Float>]) -> Float {
        let p = SIMD2(u * Float(period), v * Float(period))
        let ci = Int(p.x.rounded(.down)), cj = Int(p.y.rounded(.down))
        var f1: Float = .greatestFiniteMagnitude, f2: Float = .greatestFiniteMagnitude
        for dj in -1...1 {
            for di in -1...1 {
                let i = ci + di, j = cj + dj
                let wi = (i % period + period) % period, wj = (j % period + period) % period
                // The point of the wrapped cell, moved next to the pixel.
                let q = points[wj * period + wi] + SIMD2(Float(i - wi), Float(j - wj))
                let d = simd_distance(p, q)
                if d < f1 { f2 = f1; f1 = d } else if d < f2 { f2 = d }
            }
        }
        let gap = f2 - f1
        let t = min(max(gap / 0.22, 0), 1)
        return 1 - t * t
    }
}
