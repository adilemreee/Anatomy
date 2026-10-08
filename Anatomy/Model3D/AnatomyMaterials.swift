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
    static func make(occlusion: Float = 1, rim: Float = 0.35) -> [any RealityKit.Material] {
        guard let library else { return fallback() }
        do {
            let shader = CustomMaterial.SurfaceShader(named: "anatomySurface", in: library)
            var solid = try CustomMaterial(surfaceShader: shader, lightingModel: .lit)
            solid.custom.value = SIMD4(0, occlusion, rim, 0)
            solid.faceCulling = .none

            var ghost = try CustomMaterial(surfaceShader: shader, lightingModel: .lit)
            ghost.custom.value = SIMD4(1, occlusion * 0.5, 0, 0)
            ghost.blending = .transparent(opacity: .init(floatLiteral: 1))
            ghost.writesDepth = false
            ghost.faceCulling = .back

            var selected = try CustomMaterial(surfaceShader: shader, lightingModel: .lit)
            selected.custom.value = SIMD4(2, min(occlusion, 0.5), 0, 0)
            selected.faceCulling = .none

            var highlighted = try CustomMaterial(surfaceShader: shader, lightingModel: .lit)
            highlighted.custom.value = SIMD4(3, min(occlusion, 0.5), 0, 0)
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
        return [key, rim]
    }

    /// A soft studio environment for image based lighting.
    static func environment() async -> EnvironmentResource? {
        guard let image = environmentImage() else { return nil }
        let options = EnvironmentResource.CreateOptions(samplingQuality: .normal, specularCubeDimension: 128)
        return try? await EnvironmentResource(equirectangular: image, options: options)
    }

    private static func environmentImage() -> CGImage? {
        let width = 256, height = 128
        let format = UIGraphicsImageRendererFormat()
        format.scale = 1
        let image = UIGraphicsImageRenderer(size: CGSize(width: width, height: height), format: format).image { ctx in
            let cg = ctx.cgContext
            let colors = [
                UIColor(red: 0.96, green: 0.97, blue: 1.0, alpha: 1).cgColor,
                UIColor(red: 0.80, green: 0.82, blue: 0.86, alpha: 1).cgColor,
                UIColor(red: 0.46, green: 0.43, blue: 0.41, alpha: 1).cgColor,
                UIColor(red: 0.16, green: 0.15, blue: 0.15, alpha: 1).cgColor,
            ]
            let gradient = CGGradient(colorsSpace: CGColorSpaceCreateDeviceRGB(), colors: colors as CFArray, locations: [0, 0.45, 0.56, 1])!
            cg.drawLinearGradient(gradient, start: .zero, end: CGPoint(x: 0, y: height), options: [])
            // Large soft boxes: front key, side strips for specular highlights.
            cg.setFillColor(UIColor(white: 1, alpha: 0.75).cgColor)
            cg.fillEllipse(in: CGRect(x: width / 2 - 34, y: 14, width: 68, height: 34))
            cg.setFillColor(UIColor(white: 1, alpha: 0.45).cgColor)
            cg.fill(CGRect(x: width / 4 - 8, y: 20, width: 16, height: 46))
            cg.fill(CGRect(x: 3 * width / 4 - 8, y: 20, width: 16, height: 46))
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
