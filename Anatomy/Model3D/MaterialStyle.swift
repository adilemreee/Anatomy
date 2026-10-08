//
//  MaterialStyle.swift
//  Anatomy
//
//  Maps Z-Anatomy material names (kept per triangle run by the exporter) to
//  the colour, fibre and wetness values the surface shader uses.
//

import Foundation
import simd
import SwiftUI

/// How parts are coloured.
nonisolated enum ColorMode: String, CaseIterable, Identifiable, Sendable {
    /// Natural tissue colours.
    case realistic
    /// Z-Anatomy's teaching colours: muscles by action, bones one by one,
    /// brain lobes, nerve groups.
    case educational

    var id: String { rawValue }

    var title: String {
        switch self {
        case .realistic: "Gerçekçi"
        case .educational: "Öğretici"
        }
    }
}

nonisolated struct SurfaceStyle: Sendable {
    /// sRGB colour, 0…1.
    var color: SIMD3<Float>
    /// 0 = smooth, 1 = muscle belly fibres.
    var fibre: Float
    /// 0 = dry and matte, 1 = wet and glossy.
    var wetness: Float
    /// How much per-part brightness variation to apply.
    var variation: Float = 0
    /// Shader pattern: 0 plain, 1 muscle fibres, 2 bone, 3 organ.
    var pattern: Float = 0
}

nonisolated enum MaterialStyles {
    // MARK: Lookup

    static func style(material: String, part: PartInfo, layer: String, mode: ColorMode) -> SurfaceStyle {
        var style = realistic(material: material, part: part, layer: layer)
        style.pattern = pattern(material: material, layer: layer, style: style)
        if mode == .educational, let hex = educationalColor(material: material, layer: layer) {
            style.color = teaching(rgb(hex))
            style.variation = 0
        }
        return style
    }

    /// Z-Anatomy's palette is fully saturated; pull it slightly towards grey
    /// and down in brightness so it reads like a printed atlas.
    private static func teaching(_ c: SIMD3<Float>) -> SIMD3<Float> {
        let luma = simd_dot(c, SIMD3(0.299, 0.587, 0.114))
        return simd_mix(SIMD3(repeating: luma), c, SIMD3(repeating: 0.8)) * 0.9 + 0.03
    }

    /// A representative swatch for lists and labels.
    static func swatch(for part: PartInfo, layer: String, materials: [String], mode: ColorMode = .realistic) -> Color {
        let material = part.dominantMaterial.flatMap { materials.indices.contains($0) ? materials[$0] : nil } ?? ""
        let c = style(material: material, part: part, layer: layer, mode: mode).color
        return Color(red: Double(c.x), green: Double(c.y), blue: Double(c.z))
    }

    private static func pattern(material m: String, layer: String, style: SurfaceStyle) -> Float {
        if style.fibre > 0.01 { return 1 }
        if m.hasPrefix("Bone") || m.hasPrefix("Suture") || (layer == "skeletal" && m == "Default") { return 2 }
        switch layer {
        case "visceral", "lymphoid", "cardiovascular": return 3
        case "nervous": return m.hasPrefix("Nerve") ? 0 : 3
        default: return 0
        }
    }

    // MARK: Muscle attachments

    /// Patches where Z-Anatomy's ".o"/".e" name suffix is right and the
    /// material is not; elsewhere the material wins (e.g. the sternocostal
    /// head of pectoralis major arises from the sternum).
    private static let suffixIsRight: Set<String> = ["Long head of triceps brachii", "Deep head of flexor pollicis brevis"]

    /// Muscles whose attachments Z-Anatomy has the wrong way round, checked
    /// against the origo/insersiyo of the atlas entries (the trapezius arises
    /// from the occipital bone, the serratus anterior inserts on the scapula).
    private static let reversedMuscles: Set<String> = [
        "Descending part of trapezius muscle", "Transverse part of trapezius muscle", "Ascending part of trapezius muscle",
        "Longus capitis muscle", "Rectus anterior capitis muscle", "Rectus lateralis capitis muscle",
        "Obliquus superior capitis muscle", "Rectus posterior major capitis muscle", "Rectus posterior minor capitis muscle",
        "Pectoralis minor muscle", "Serratus anterior muscle",
    ]

    /// Single patches with the wrong kind, keyed "muscle|bone".
    private static let correctedPatches: [String: Bool] = [
        "Latissimus dorsi muscle|Scapula": true,
        "External abdominal oblique muscle|Hip bone": false,
    ]

    /// Whether an attachment patch is an origin (red) rather than an insertion (blue).
    static func isOrigin(_ part: PartInfo, material: String) -> Bool {
        if let fixed = correctedPatches["\(part.base)|\(part.path.last ?? "")"] { return fixed }
        let fromData: Bool
        if suffixIsRight.contains(part.base) || !(material.hasPrefix("Origin") || material.hasPrefix("Muscular origin") || material.hasPrefix("End-")) {
            fromData = part.kind != "insertion"
        } else {
            fromData = !material.hasPrefix("End-")
        }
        return reversedMuscles.contains(part.base) ? !fromData : fromData
    }

    // MARK: Educational colours

    private static let zanatomyColors: [String: String] = {
        guard let url = Bundle.main.url(forResource: "material-colors", withExtension: "json"),
              let data = try? Data(contentsOf: url),
              let map = try? JSONDecoder().decode([String: String].self, from: data) else { return [:] }
        return map
    }()

    private static func educationalColor(material: String, layer: String) -> String? {
        // Keep connective tissue natural so the colour-coded tissue stands out.
        let keep = ["Tendon", "Fascia", "Ligament", "Cartilage", "Bursa", "Articular capsule", "Teeth", "Teeth-roots", "Dentine", "Default"]
        if keep.contains(material) { return nil }
        if layer == "cardiovascular" || layer == "regions" || layer == "visceral" { return nil }
        return zanatomyColors[material]
    }

    /// Teaching legend for the muscle action colours.
    static let muscleLegend: [(material: String, title: String)] = [
        ("Flexion", "Fleksiyon (bükme)"),
        ("Extension", "Ekstansiyon (açma)"),
        ("Abductor", "Abdüksiyon (uzaklaştırma)"),
        ("Adductor", "Addüksiyon (yaklaştırma)"),
        ("External rotation", "Dış rotasyon"),
        ("Internal rotator", "İç rotasyon"),
        ("Levator", "Kaldırıcı (elevasyon)"),
        ("Depressor", "İndirici (depresyon)"),
        ("Flexion fingers", "Parmak fleksörleri"),
        ("Extensor extremities", "Parmak ekstansörleri"),
        ("Flexion hand/foot", "El / ayak fleksörleri"),
        ("Extension hand/foot", "El / ayak ekstansörleri"),
        ("Biarticular", "İki eklemli kaslar"),
        ("Orbicularis/Constrictor", "Halka / büzücü kaslar"),
        ("Masticator", "Çiğneme kasları"),
        ("Ingestion", "Yutma"),
        ("Phonation", "Ses oluşumu"),
        ("Superficial", "Yüzeyel kaslar"),
        ("Diaphragm", "Diyafram"),
    ]

    static let brainLegend: [(material: String, title: String)] = [
        ("Frontal lobe", "Alın lobu"),
        ("Parietal lobe", "Yan kafa lobu"),
        ("Temporal lobe", "Şakak lobu"),
        ("Occipital lobe", "Art kafa lobu"),
        ("Insula", "İnsula"),
        ("Limbic lobe", "Limbik lob"),
        ("Cerebellum", "Beyincik"),
    ]

    static func legendColor(_ material: String) -> Color {
        let c = teaching(rgb(zanatomyColors[material] ?? "999999"))
        return Color(red: Double(c.x), green: Double(c.y), blue: Double(c.z))
    }

    // MARK: Realistic colours

    private static func realistic(material m: String, part: PartInfo, layer: String) -> SurfaceStyle {
        let name = part.base.lowercased()
        func named(_ words: String...) -> Bool { words.contains { name.contains($0) } }

        switch m {
        case "Tendon": return SurfaceStyle(color: rgb("e6dcc8"), fibre: 0.3, wetness: 0.8, variation: 0.03)
        case "Fascia": return SurfaceStyle(color: rgb("cdd6dc"), fibre: 0, wetness: 0.8)
        case "Bursa": return SurfaceStyle(color: rgb("a7cde0"), fibre: 0, wetness: 0.9)
        case "Ligament", "Origin-Ligament": return SurfaceStyle(color: rgb("ddd8c9"), fibre: 0.3, wetness: 0.75, variation: 0.03)
        case "Articular capsule": return SurfaceStyle(color: rgb("d3cbbf"), fibre: 0.15, wetness: 0.7)
        case "Cartilage": return SurfaceStyle(color: rgb("bed4dc"), fibre: 0, wetness: 0.65, variation: 0.02)
        case "Fat": return SurfaceStyle(color: rgb("ead27e"), fibre: 0, wetness: 0.6)
        case "Teeth": return SurfaceStyle(color: rgb("f3efe6"), fibre: 0, wetness: 0.85)
        case "Teeth-roots", "Dentine": return SurfaceStyle(color: rgb("ddd0b2"), fibre: 0, wetness: 0.4)
        case "Artery": return SurfaceStyle(color: rgb("c22b27"), fibre: 0, wetness: 0.75)
        case "Vein": return SurfaceStyle(color: rgb("3a5cb4"), fibre: 0, wetness: 0.75)
        case "Pulmonary artery": return SurfaceStyle(color: rgb("4b68cc"), fibre: 0, wetness: 0.75)
        case "Pulmonary vein": return SurfaceStyle(color: rgb("c43a3a"), fibre: 0, wetness: 0.75)
        case "LCR": return SurfaceStyle(color: rgb("9ec9de"), fibre: 0, wetness: 0.9)
        case "Cornea": return SurfaceStyle(color: rgb("e3edf2"), fibre: 0, wetness: 1)
        case "Eye": return SurfaceStyle(color: rgb("f2efe8"), fibre: 0, wetness: 0.9)
        case "Iris": return SurfaceStyle(color: rgb("5b7c9c"), fibre: 0, wetness: 0.8)
        case "Nail": return SurfaceStyle(color: rgb("eed8cd"), fibre: 0, wetness: 0.8)
        case "Black": return SurfaceStyle(color: rgb("3b2d26"), fibre: 0, wetness: 0.3)
        case "Gallbladder": return SurfaceStyle(color: rgb("5f8d3d"), fibre: 0, wetness: 0.9)
        case "Ductus": return SurfaceStyle(color: rgb("7fa45a"), fibre: 0, wetness: 0.8)
        default: break
        }
        if m.hasPrefix("Origin") || m.hasPrefix("Muscular origin") || m.hasPrefix("End-") {
            return SurfaceStyle(color: rgb(isOrigin(part, material: m) ? "d4473d" : "3c78d3"), fibre: 0, wetness: 0.5)
        }
        if m.hasPrefix("Bone") { return SurfaceStyle(color: rgb("ece3cf"), fibre: 0, wetness: 0.3, variation: 0.03) }
        if m.hasPrefix("Suture") { return SurfaceStyle(color: rgb("bba98a"), fibre: 0, wetness: 0.15) }
        if m.hasPrefix("Lymph") { return SurfaceStyle(color: rgb("86bc62"), fibre: 0, wetness: 0.7, variation: 0.05) }
        if m.hasPrefix("Nerve") { return SurfaceStyle(color: rgb("ecd27c"), fibre: 0.25, wetness: 0.55, variation: 0.03) }
        if m.hasPrefix("Skin") { return SurfaceStyle(color: m == "Skin-in" ? rgb("d9a98d") : rgb("e5bc9f"), fibre: 0, wetness: 0.35, variation: 0.02) }
        if m.hasPrefix("Lung") { return SurfaceStyle(color: rgb("e2a29d"), fibre: 0, wetness: 0.85, variation: 0.04) }
        if m.hasPrefix("Bronchi") { return SurfaceStyle(color: rgb("dfe5e7"), fibre: 0.1, wetness: 0.7, variation: 0.02) }

        switch layer {
        case "muscular":
            // Every action group is a muscle belly.
            return SurfaceStyle(color: rgb("9c302b"), fibre: 1, wetness: 0.45, variation: 0.08)
        case "cardiovascular":
            // The heart wall uses Z-Anatomy's muscle material.
            return SurfaceStyle(color: rgb("a32f2c"), fibre: 0.55, wetness: 0.8, variation: 0.04)
        case "nervous":
            switch m {
            case "White matter": return SurfaceStyle(color: rgb("efe5d6"), fibre: 0, wetness: 0.5)
            case "Brain-Inner": return SurfaceStyle(color: rgb("e9d0bb"), fibre: 0, wetness: 0.55)
            case "Cerebellum": return SurfaceStyle(color: rgb("c78f84"), fibre: 0, wetness: 0.65)
            case "Interlobar sulci": return SurfaceStyle(color: rgb("b98276"), fibre: 0, wetness: 0.6)
            case "Nucleus", "Nucleus (afferent fibers)", "Nucleus (efferent fibers)": return SurfaceStyle(color: rgb("b08d7b"), fibre: 0, wetness: 0.55)
            case "Mucosa": return SurfaceStyle(color: rgb("cf7f83"), fibre: 0, wetness: 0.9)
            case "Gland": return SurfaceStyle(color: rgb("d69878"), fibre: 0, wetness: 0.8)
            case "Orbicularis/Constrictor", "Levator", "Depressor", "Superficial": return SurfaceStyle(color: rgb("a8332d"), fibre: 1, wetness: 0.7, variation: 0.06)
            default: return SurfaceStyle(color: rgb("dcac9e"), fibre: 0, wetness: 0.65, variation: 0.03)
            }
        case "visceral":
            if named("liver", "segment of liver") { return SurfaceStyle(color: rgb("8e3a2e"), fibre: 0, wetness: 0.95, variation: 0.03) }
            if named("kidney", "renal") { return SurfaceStyle(color: rgb("8b3b33"), fibre: 0, wetness: 0.9) }
            if named("spleen") { return SurfaceStyle(color: rgb("7c2e38"), fibre: 0, wetness: 0.9) }
            if named("pancrea") { return SurfaceStyle(color: rgb("e2b37a"), fibre: 0, wetness: 0.8) }
            if named("stomach") { return SurfaceStyle(color: rgb("d78878"), fibre: 0, wetness: 0.9) }
            if named("colon", "caecum", "appendix", "rectum", "taenia") { return SurfaceStyle(color: rgb("c78a6d"), fibre: 0, wetness: 0.9, variation: 0.03) }
            if named("duodenum", "jejunum", "ileum") { return SurfaceStyle(color: rgb("e09d8b"), fibre: 0, wetness: 0.95) }
            if named("thyroid") { return SurfaceStyle(color: rgb("a8483f"), fibre: 0, wetness: 0.85) }
            if named("suprarenal", "parathyroid") { return SurfaceStyle(color: rgb("d8a24c"), fibre: 0, wetness: 0.8) }
            if named("bladder", "ureter", "urethra") { return SurfaceStyle(color: rgb("e1bd7a"), fibre: 0, wetness: 0.85) }
            if named("testis", "epididymis", "deferens", "seminal", "ejaculatory") { return SurfaceStyle(color: rgb("dfb4a2"), fibre: 0, wetness: 0.85) }
            if named("prostate") { return SurfaceStyle(color: rgb("c78a7b"), fibre: 0, wetness: 0.8) }
            if named("penis", "glans", "corpus") { return SurfaceStyle(color: rgb("d29d8f"), fibre: 0, wetness: 0.8) }
            if named("tongue", "palate", "uvula") { return SurfaceStyle(color: rgb("c9625b"), fibre: 0.4, wetness: 0.95) }
            if named("trachea", "bronch") { return SurfaceStyle(color: rgb("dfe5e7"), fibre: 0.1, wetness: 0.7) }
            if named("parotid", "submandibular", "sublingual", "hypophysis", "pineal") { return SurfaceStyle(color: rgb("d9a77a"), fibre: 0, wetness: 0.8) }
            if named("omentum", "mesocolon", "peritone") { return SurfaceStyle(color: rgb("ecd79a"), fibre: 0, wetness: 0.85) }
            if named("pleura") { return SurfaceStyle(color: rgb("d3e2ea"), fibre: 0, wetness: 0.95) }
            if m == "Mucosa" || m == "Mucosa of stomach" { return SurfaceStyle(color: rgb("cf7f7c"), fibre: 0, wetness: 0.95) }
            if m == "Intestine" { return SurfaceStyle(color: rgb("df9c89"), fibre: 0, wetness: 0.95) }
            if m == "Gland" { return SurfaceStyle(color: rgb("d69a72"), fibre: 0, wetness: 0.85) }
            return SurfaceStyle(color: rgb("d38b7c"), fibre: 0, wetness: 0.9, variation: 0.03)
        case "lymphoid":
            if named("spleen") || m.hasPrefix("Organ") { return SurfaceStyle(color: rgb("7c2e38"), fibre: 0, wetness: 0.9) }
            if named("thymus") || m == "Gland" { return SurfaceStyle(color: rgb("d8b29a"), fibre: 0, wetness: 0.8) }
            return SurfaceStyle(color: rgb("86bc62"), fibre: 0, wetness: 0.7, variation: 0.05)
        case "skeletal":
            return SurfaceStyle(color: rgb("ece3cf"), fibre: 0, wetness: 0.3, variation: 0.03)
        case "joints":
            return SurfaceStyle(color: rgb("ddd8c9"), fibre: 0.25, wetness: 0.7)
        case "regions":
            return SurfaceStyle(color: rgb("e5bc9f"), fibre: 0, wetness: 0.35)
        default:
            return SurfaceStyle(color: rgb("cfc5bd"), fibre: 0, wetness: 0.5)
        }
    }

    static func rgb(_ hex: String) -> SIMD3<Float> {
        var value: UInt64 = 0
        Scanner(string: hex).scanHexInt64(&value)
        return SIMD3(Float((value >> 16) & 0xFF), Float((value >> 8) & 0xFF), Float(value & 0xFF)) / 255
    }
}
