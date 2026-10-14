//
//  AnatomyMaterials.swift
//  Anatomy
//
//  The four material states every part can be drawn with, the studio
//  lighting rig and the soft contact shadow under the figure.
//

import Metal
import RealityKit
import UIKit

@MainActor
enum AnatomyMaterials {
    /// Order matches `LowLevelMesh.Part.materialIndex`.
    enum Slot: Int, CaseIterable {
        case solid = 0, ghost, selected, highlighted
    }

    private static let library: MTLLibrary? = MTLCreateSystemDefaultDevice()?.makeDefaultLibrary()

    /// Materials for one entity. `occlusion` lowers the baked crease shading,
    /// which is useful when deep structures are shown on their own.
    /// RealityKit only allows this on the main thread.
    static func make(occlusion: Float = 1, rim: Float = 0.35, detail: TextureResource?, skin: TextureResource? = nil) -> [any RealityKit.Material] {
        guard let library else { return fallback() }
        do {
            let shader = CustomMaterial.SurfaceShader(named: "anatomySurface", in: library)
            func material(_ values: SIMD4<Float>) throws -> CustomMaterial {
                var m = try CustomMaterial(surfaceShader: shader, lightingModel: .clearcoat)
                m.custom.value = values
                if let detail { m.custom.texture = .init(detail) }
                // Skin texture atlas, sampled where a vertex has texture coordinates.
                if let skin { m.baseColor = .init(tint: .white, texture: .init(skin)) }
                return m
            }
            var solid = try material(SIMD4(0, occlusion, rim, 0))
            solid.faceCulling = .none

            var ghost = try material(SIMD4(1, occlusion * 0.5, 0, 0))
            ghost.blending = .transparent(opacity: .init(floatLiteral: 1))
            ghost.writesDepth = false
            ghost.faceCulling = .back

            var selected = try material(SIMD4(2, min(occlusion, 0.5), 0, 0))
            selected.faceCulling = .none

            var highlighted = try material(SIMD4(3, min(occlusion, 0.5), 0, 0))
            highlighted.faceCulling = .none
            return [solid, ghost, selected, highlighted]
        } catch {
            return fallback()
        }
    }

    /// Plain materials in case custom shaders are unavailable.
    private static func fallback() -> [any RealityKit.Material] {
        func pbr(_ color: UIColor, opacity: Float = 1) -> PhysicallyBasedMaterial {
            var m = PhysicallyBasedMaterial()
            m.baseColor = .init(tint: color)
            m.roughness = .init(floatLiteral: 0.55)
            m.faceCulling = .none
            if opacity < 1 {
                m.blending = .transparent(opacity: .init(floatLiteral: opacity))
                m.writesDepth = false
            }
            return m
        }
        return [pbr(UIColor(white: 0.85, alpha: 1)), pbr(UIColor(white: 0.85, alpha: 1), opacity: 0.12),
                pbr(UIColor(red: 0.16, green: 0.62, blue: 1, alpha: 1)), pbr(UIColor(red: 1, green: 0.72, blue: 0.15, alpha: 1))]
    }

    // MARK: Lighting

    /// Key, fill and rim lights that travel with the camera so the figure is
    /// always nicely lit from the viewer's side.
    static func cameraLights() -> [Entity] {
        let key = DirectionalLight()
        key.light.intensity = 1500
        key.light.color = UIColor(red: 1, green: 0.97, blue: 0.93, alpha: 1)
        // From the upper left of the viewer for readable relief.
        key.orientation = simd_quatf(angle: .pi / 4.5, axis: [0, 1, 0]) * simd_quatf(angle: -.pi / 5, axis: [1, 0, 0])

        let rim = DirectionalLight()
        rim.light.intensity = 700
        rim.light.color = UIColor(red: 0.85, green: 0.92, blue: 1, alpha: 1)
        // Points back towards the camera from behind the figure.
        rim.orientation = simd_quatf(angle: .pi * 0.9, axis: [0, 1, 0]) * simd_quatf(angle: -.pi / 9, axis: [1, 0, 0])

        // A soft fill from the lower right so surfaces turned away from the
        // key (the underside of the liver) keep their form and colour.
        let fill = DirectionalLight()
        fill.light.intensity = 650
        fill.light.color = UIColor(red: 1, green: 0.95, blue: 0.9, alpha: 1)
        fill.orientation = simd_quatf(angle: -.pi / 3.2, axis: [0, 1, 0]) * simd_quatf(angle: .pi / 7, axis: [1, 0, 0])
        return [key, rim, fill]
    }

    /// A soft studio environment for image based lighting.
    static func environment() async -> EnvironmentResource? {
        guard let image = environmentImage() else { return nil }
        let options = EnvironmentResource.CreateOptions(samplingQuality: .normal, specularCubeDimension: 128)
        return try? await EnvironmentResource(equirectangular: image, options: options)
    }

    /// A dark photo studio: dim ceiling and walls, one soft key box above the
    /// camera, two narrow strips at the sides for gentle edge highlights.
    /// Wet tissue reflects this, so it must not be bright overall or every
    /// organ looks like plastic.
    private static func environmentImage() -> CGImage? {
        let width = 256, height = 128
        let format = UIGraphicsImageRendererFormat()
        format.scale = 1
        let image = UIGraphicsImageRenderer(size: CGSize(width: width, height: height), format: format).image { ctx in
            let cg = ctx.cgContext
            let colors = [
                UIColor(red: 0.42, green: 0.44, blue: 0.48, alpha: 1).cgColor,
                UIColor(red: 0.30, green: 0.31, blue: 0.34, alpha: 1).cgColor,
                UIColor(red: 0.22, green: 0.21, blue: 0.21, alpha: 1).cgColor,
                UIColor(red: 0.15, green: 0.14, blue: 0.14, alpha: 1).cgColor,
            ]
            let gradient = CGGradient(colorsSpace: CGColorSpaceCreateDeviceRGB(), colors: colors as CFArray, locations: [0, 0.42, 0.55, 1])!
            cg.drawLinearGradient(gradient, start: .zero, end: CGPoint(x: 0, y: height), options: [])
            // Soft key box in front and above (the +Z direction is the middle column).
            let key = CGGradient(colorsSpace: CGColorSpaceCreateDeviceRGB(),
                                 colors: [UIColor(white: 1, alpha: 0.55).cgColor, UIColor(white: 1, alpha: 0).cgColor] as CFArray,
                                 locations: [0, 1])!
            cg.drawRadialGradient(key, startCenter: CGPoint(x: width / 2 - 18, y: 26), startRadius: 0,
                                  endCenter: CGPoint(x: width / 2 - 18, y: 26), endRadius: 30, options: [])
            cg.setFillColor(UIColor(white: 1, alpha: 0.18).cgColor)
            cg.fill(CGRect(x: width / 4 - 5, y: 26, width: 10, height: 40))
            cg.fill(CGRect(x: 3 * width / 4 - 5, y: 26, width: 10, height: 40))
        }
        return image.cgImage
    }

    // MARK: Contact shadow

    /// A blurred disc on the floor that grounds the standing figure.
    static func contactShadow() async -> Entity? {
        let size = 256
        let format = UIGraphicsImageRendererFormat()
        format.scale = 1
        format.opaque = false
        let image = UIGraphicsImageRenderer(size: CGSize(width: size, height: size), format: format).image { ctx in
            let colors = [UIColor(white: 0, alpha: 0.38).cgColor, UIColor(white: 0, alpha: 0.12).cgColor, UIColor(white: 0, alpha: 0).cgColor]
            let gradient = CGGradient(colorsSpace: CGColorSpaceCreateDeviceRGB(), colors: colors as CFArray, locations: [0, 0.45, 1])!
            let c = CGPoint(x: size / 2, y: size / 2)
            ctx.cgContext.drawRadialGradient(gradient, startCenter: c, startRadius: 0, endCenter: c, endRadius: CGFloat(size) / 2, options: [])
        }
        guard let cg = image.cgImage,
              let texture = try? await TextureResource(image: cg, options: .init(semantic: .color)) else { return nil }
        var material = UnlitMaterial()
        material.color = .init(tint: .white, texture: .init(texture))
        material.blending = .transparent(opacity: .init(floatLiteral: 1))
        material.writesDepth = false
        let entity = ModelEntity(mesh: .generatePlane(width: 0.95, depth: 0.55), materials: [material])
        entity.position = [0, -0.004, 0.0]
        entity.name = "contact-shadow"
        return entity
    }
}

extension AnatomyMaterials {
    private static var cache: [SIMD2<Float>: [any RealityKit.Material]] = [:]
    private static var spotMaterial: (any RealityKit.Material)?
    private static var skinLoad: Task<TextureResource?, Never>?

    /// The MakeHuman skin atlas (male left half, female right half), in sRGB
    /// with a full mip chain. Loaded once.
    static func skinTexture() async -> TextureResource? {
        if let skinLoad { return await skinLoad.value }
        let task = Task<TextureResource?, Never> {
            guard let url = Bundle.main.url(forResource: "skin-atlas", withExtension: "jpg") else { return nil }
            return try? await TextureResource(contentsOf: url, options: .init(semantic: .color, mipmapsMode: .allocateAndGenerateAll))
        }
        skinLoad = task
        return await task.value
    }

    /// See-through glowing material for highlight patches in the specimen
    /// viewer; the vertex colour's alpha fades the patch out at its edge.
    static func spot() async -> any RealityKit.Material {
        if let spotMaterial { return spotMaterial }
        let detail = await DetailTexture.resource()
        var material: any RealityKit.Material = UnlitMaterial(color: UIColor(red: 0.1, green: 0.62, blue: 1, alpha: 0.6))
        if let library {
            let shader = CustomMaterial.SurfaceShader(named: "anatomySurface", in: library)
            if var m = try? CustomMaterial(surfaceShader: shader, lightingModel: .clearcoat) {
                m.custom.value = SIMD4(4, 0, 0, 0)
                if let detail { m.custom.texture = .init(detail) }
                m.blending = .transparent(opacity: .init(floatLiteral: 1))
                m.writesDepth = false
                // Some high-detail meshes wind the other way round.
                m.faceCulling = .none
                material = m
            }
        }
        spotMaterial = material
        return material
    }

    /// Shared material sets. Compiling the surface shader blocks the main
    /// thread for over a second the first time, so callers await this after
    /// the first frame instead of building materials while views appear.
    static func shared(occlusion: Float = 1, rim: Float = 0.35) async -> [any RealityKit.Material] {
        let key = SIMD2(occlusion, rim)
        if let cached = cache[key] { return cached }
        let detail = await DetailTexture.resource()
        let skin = await skinTexture()
        if let cached = cache[key] { return cached }
        let materials = make(occlusion: occlusion, rim: rim, detail: detail, skin: skin)
        cache[key] = materials
        return materials
    }
}
