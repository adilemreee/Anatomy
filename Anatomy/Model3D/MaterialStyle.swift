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
        case .realistic: String(localized: "Gerçekçi")
        case .educational: String(localized: "Öğretici")
        }
    }
}

/// Organ surfaces the shader imitates; raw values match `Tissue` in AnatomyShaders.metal.
nonisolated enum Tissue: Float, Sendable {
    case generic = 0, liver, lung, kidney, spleen, stomach, intestine, gland, heart, vessel, brain, hollow, fat, cartilage, nerve, skin
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
    /// Organ surface the shader imitates (see `Tissue`).
    var tissue: Float = 0

    func tissue(_ t: Tissue) -> SurfaceStyle {
        var copy = self
        copy.tissue = t.rawValue
        return copy
    }
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
        if m == "Scalp" || m == "Scalp edge" { return 4 }
        if m == "Pubic hair" { return 4 }
        if m == "Scrotal skin" { return 5 }
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
        ("Flexion", String(localized: "Fleksiyon (bükme)")),
        ("Extension", String(localized: "Ekstansiyon (açma)")),
        ("Abductor", String(localized: "Abdüksiyon (uzaklaştırma)")),
        ("Adductor", String(localized: "Addüksiyon (yaklaştırma)")),
        ("External rotation", String(localized: "Dış rotasyon")),
        ("Internal rotator", String(localized: "İç rotasyon")),
        ("Levator", String(localized: "Kaldırıcı (elevasyon)")),
        ("Depressor", String(localized: "İndirici (depresyon)")),
        ("Flexion fingers", String(localized: "Parmak fleksörleri")),
        ("Extensor extremities", String(localized: "Parmak ekstansörleri")),
        ("Flexion hand/foot", String(localized: "El / ayak fleksörleri")),
        ("Extension hand/foot", String(localized: "El / ayak ekstansörleri")),
        ("Biarticular", String(localized: "İki eklemli kaslar")),
        ("Orbicularis/Constrictor", String(localized: "Halka / büzücü kaslar")),
        ("Masticator", String(localized: "Çiğneme kasları")),
        ("Ingestion", "Yutma"),
        ("Phonation", String(localized: "Ses oluşumu")),
        ("Superficial", String(localized: "Yüzeyel kaslar")),
        ("Diaphragm", "Diyafram"),
    ]

    static let brainLegend: [(material: String, title: String)] = [
        ("Frontal lobe", String(localized: "Alın lobu")),
        ("Parietal lobe", "Yan kafa lobu"),
        ("Temporal lobe", String(localized: "Şakak lobu")),
        ("Occipital lobe", "Art kafa lobu"),
        ("Insula", String(localized: "İnsula")),
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
        case "Bursa": return SurfaceStyle(color: rgb("a7cde0"), fibre: 0, wetness: 0.9).tissue(.hollow)
        case "Ligament", "Origin-Ligament": return SurfaceStyle(color: rgb("ddd8c9"), fibre: 0.3, wetness: 0.75, variation: 0.03)
        case "Articular capsule": return SurfaceStyle(color: rgb("d3cbbf"), fibre: 0.15, wetness: 0.7)
        case "Cartilage": return SurfaceStyle(color: rgb("bed4dc"), fibre: 0, wetness: 0.65, variation: 0.02).tissue(.cartilage)
        case "Fat": return SurfaceStyle(color: rgb("ead27e"), fibre: 0, wetness: 0.6).tissue(.fat)
        case "Teeth": return SurfaceStyle(color: rgb("f3efe6"), fibre: 0, wetness: 0.85)
        case "Teeth-roots", "Dentine": return SurfaceStyle(color: rgb("ddd0b2"), fibre: 0, wetness: 0.4)
        case "Artery": return SurfaceStyle(color: rgb("b8302b"), fibre: 0, wetness: 0.75).tissue(.vessel)
        case "Vein": return SurfaceStyle(color: rgb("3d5aa8"), fibre: 0, wetness: 0.75).tissue(.vessel)
        case "Pulmonary artery": return SurfaceStyle(color: rgb("4b68cc"), fibre: 0, wetness: 0.75).tissue(.vessel)
        case "Pulmonary vein": return SurfaceStyle(color: rgb("c43a3a"), fibre: 0, wetness: 0.75).tissue(.vessel)
        case "LCR": return SurfaceStyle(color: rgb("9ec9de"), fibre: 0, wetness: 0.9).tissue(.hollow)
        case "Cornea": return SurfaceStyle(color: rgb("e3edf2"), fibre: 0, wetness: 1).tissue(.hollow)
        case "Eye": return SurfaceStyle(color: rgb("f2efe8"), fibre: 0, wetness: 0.9).tissue(.hollow)
        case "Iris": return SurfaceStyle(color: rgb("5b7c9c"), fibre: 0, wetness: 0.8)
        case "Nail": return SurfaceStyle(color: rgb("eed8cd"), fibre: 0, wetness: 0.8)
        case "Black": return SurfaceStyle(color: rgb("3b2d26"), fibre: 0, wetness: 0.3)
        case "Gallbladder": return SurfaceStyle(color: rgb("4f7f38"), fibre: 0, wetness: 0.9).tissue(.hollow)
        case "Ductus": return SurfaceStyle(color: rgb("7fa45a"), fibre: 0, wetness: 0.8).tissue(.hollow)
        case "Pericardium": return SurfaceStyle(color: rgb("d8cbb8"), fibre: 0.12, wetness: 0.95, variation: 0.02)
        case "Areola": return SurfaceStyle(color: rgb("a8634f"), fibre: 0, wetness: 0.45, variation: 0.02).tissue(.skin)
        case "Areola rim": return SurfaceStyle(color: rgb("bd8470"), fibre: 0, wetness: 0.42, variation: 0.02).tissue(.skin)
        case "Lips": return SurfaceStyle(color: rgb("c4847c"), fibre: 0, wetness: 0.62, variation: 0.02).tissue(.skin)
        case "Lip border": return SurfaceStyle(color: rgb("cc9585"), fibre: 0, wetness: 0.5, variation: 0.02).tissue(.skin)
        case "Scalp": return SurfaceStyle(color: rgb("d8a78e"), fibre: 0, wetness: 0.34, variation: 0.02).tissue(.skin)
        case "Scalp edge": return SurfaceStyle(color: rgb("d8a78e"), fibre: 0, wetness: 0.16, variation: 0.02).tissue(.skin)
        case "Eyebrow": return SurfaceStyle(color: rgb("2e2018"), fibre: 0, wetness: 0.35)
        case "Brow skin": return SurfaceStyle(color: rgb("b98a74"), fibre: 0, wetness: 0.34, variation: 0.02).tissue(.skin)
        case "Eyelash": return SurfaceStyle(color: rgb("1d1612"), fibre: 0, wetness: 0.4)
        case "Scrotal skin": return SurfaceStyle(color: rgb("c08f7b"), fibre: 0, wetness: 0.4, variation: 0.03).tissue(.skin)
        case "Penile skin": return SurfaceStyle(color: rgb("cc9a84"), fibre: 0, wetness: 0.38, variation: 0.02).tissue(.skin)
        case "Pubic hair": return SurfaceStyle(color: rgb("d0a088"), fibre: 0, wetness: 0.3, variation: 0.02).tissue(.skin)
        case "Mammary lobule": return SurfaceStyle(color: rgb("c4737a"), fibre: 0, wetness: 0.85, variation: 0.05).tissue(.gland)
        case "Lactiferous duct": return SurfaceStyle(color: rgb("e6d9c6"), fibre: 0, wetness: 0.8, variation: 0.02).tissue(.hollow)
        case "Breast fat": return SurfaceStyle(color: rgb("e3b04e"), fibre: 0, wetness: 0.75, variation: 0.03).tissue(.fat)
        case "Sclera": return SurfaceStyle(color: rgb("eeeae2"), fibre: 0, wetness: 1).tissue(.hollow)
        case "Eye iris": return SurfaceStyle(color: rgb("6a4a2e"), fibre: 0, wetness: 1).tissue(.hollow)
        case "Pupil": return SurfaceStyle(color: rgb("0d0b0a"), fibre: 0, wetness: 1)
        case "Mouth": return SurfaceStyle(color: rgb("4a1d1c"), fibre: 0, wetness: 0.9).tissue(.skin)   // no blue rim between the lips
        case "Vulva mucosa": return SurfaceStyle(color: rgb("d89d98"), fibre: 0, wetness: 0.95, variation: 0.02).tissue(.skin)
        case "Glans": return SurfaceStyle(color: rgb("c08a80"), fibre: 0, wetness: 0.6, variation: 0.02).tissue(.skin)
        case "Labia": return SurfaceStyle(color: rgb("c99883"), fibre: 0, wetness: 0.4, variation: 0.02).tissue(.skin)
        case "Labia minora": return SurfaceStyle(color: rgb("b5786f"), fibre: 0, wetness: 0.8, variation: 0.03).tissue(.skin)
        case "Vaginal orifice": return SurfaceStyle(color: rgb("94474a"), fibre: 0, wetness: 0.9).tissue(.hollow)
        case "Scrotum": return SurfaceStyle(color: rgb("bf8a78"), fibre: 0, wetness: 0.4, variation: 0.03).tissue(.skin)
        default: break
        }
        if m.hasPrefix("Origin") || m.hasPrefix("Muscular origin") || m.hasPrefix("End-") {
            return SurfaceStyle(color: rgb(isOrigin(part, material: m) ? "d4473d" : "3c78d3"), fibre: 0, wetness: 0.5)
        }
        if m.hasPrefix("Bone") { return SurfaceStyle(color: rgb("ece3cf"), fibre: 0, wetness: 0.3, variation: 0.03) }
        if m.hasPrefix("Suture") { return SurfaceStyle(color: rgb("bba98a"), fibre: 0, wetness: 0.15) }
        if m.hasPrefix("Lymph") { return SurfaceStyle(color: rgb("86bc62"), fibre: 0, wetness: 0.7, variation: 0.05).tissue(.gland) }
        if m.hasPrefix("Nerve") { return SurfaceStyle(color: rgb("ecd27c"), fibre: 0, wetness: 0.55, variation: 0.03).tissue(.nerve) }
        if m.hasPrefix("Skin") { return SurfaceStyle(color: m == "Skin-in" ? rgb("c99780") : rgb("d8a78e"), fibre: 0, wetness: 0.35, variation: 0.02).tissue(.skin) }
        if m.hasPrefix("Lung") { return SurfaceStyle(color: rgb("d99a94"), fibre: 0, wetness: 0.85, variation: 0.04).tissue(.lung) }
        if m.hasPrefix("Bronchi") { return SurfaceStyle(color: rgb("dfe5e7"), fibre: 0, wetness: 0.7, variation: 0.02).tissue(.cartilage) }

        switch layer {
        case "muscular":
            // Every action group is a muscle belly.
            return SurfaceStyle(color: rgb("9c302b"), fibre: 1, wetness: 0.45, variation: 0.08)
        case "cardiovascular":
            // The heart wall uses Z-Anatomy's muscle material.
            return SurfaceStyle(color: rgb("9c2f2a"), fibre: 0.55, wetness: 0.8, variation: 0.04).tissue(.heart)
        case "nervous":
            switch m {
            case "White matter": return SurfaceStyle(color: rgb("efe5d6"), fibre: 0, wetness: 0.5).tissue(.brain)
            case "Brain-Inner": return SurfaceStyle(color: rgb("e9d0bb"), fibre: 0, wetness: 0.55).tissue(.brain)
            case "Cerebellum": return SurfaceStyle(color: rgb("c78f84"), fibre: 0, wetness: 0.65).tissue(.brain)
            case "Interlobar sulci": return SurfaceStyle(color: rgb("b98276"), fibre: 0, wetness: 0.6).tissue(.brain)
            case "Nucleus", "Nucleus (afferent fibers)", "Nucleus (efferent fibers)": return SurfaceStyle(color: rgb("b08d7b"), fibre: 0, wetness: 0.55)
            case "Mucosa": return SurfaceStyle(color: rgb("cf7f83"), fibre: 0, wetness: 0.9).tissue(.hollow)
            case "Gland": return SurfaceStyle(color: rgb("d69878"), fibre: 0, wetness: 0.8).tissue(.gland)
            case "Orbicularis/Constrictor", "Levator", "Depressor", "Superficial": return SurfaceStyle(color: rgb("a8332d"), fibre: 1, wetness: 0.7, variation: 0.06)
            default: return SurfaceStyle(color: rgb("dcac9e"), fibre: 0, wetness: 0.65, variation: 0.03).tissue(.brain)
            }
        case "visceral":
            if named("liver", "segment of liver") { return SurfaceStyle(color: rgb("7e3328"), fibre: 0, wetness: 0.95, variation: 0.03).tissue(.liver) }
            if named("kidney", "renal") { return SurfaceStyle(color: rgb("843a31"), fibre: 0, wetness: 0.9).tissue(.kidney) }
            if named("spleen") { return SurfaceStyle(color: rgb("6f2a36"), fibre: 0, wetness: 0.9).tissue(.spleen) }
            if named("pancrea") { return SurfaceStyle(color: rgb("e0b07c"), fibre: 0, wetness: 0.8).tissue(.gland) }
            if named("stomach") { return SurfaceStyle(color: rgb("d78878"), fibre: 0, wetness: 0.9).tissue(.stomach) }
            if named("colon", "caecum", "appendix", "rectum", "taenia", "anal canal") { return SurfaceStyle(color: rgb("c98a6e"), fibre: 0, wetness: 0.9, variation: 0.03).tissue(.intestine) }
            if named("duodenum", "jejunum", "ileum") { return SurfaceStyle(color: rgb("df9a88"), fibre: 0, wetness: 0.95).tissue(.intestine) }
            if named("oesophagus", "esophagus", "pharynx") { return SurfaceStyle(color: rgb("cd8478"), fibre: 0, wetness: 0.9).tissue(.stomach) }
            if named("thyroid") { return SurfaceStyle(color: rgb("a4473f"), fibre: 0, wetness: 0.85).tissue(.gland) }
            if named("suprarenal", "parathyroid") { return SurfaceStyle(color: rgb("d6a04e"), fibre: 0, wetness: 0.8).tissue(.gland) }
            if named("bladder", "ureter", "urethra") { return SurfaceStyle(color: rgb("deb87c"), fibre: 0, wetness: 0.85).tissue(.hollow) }
            if named("testis", "epididymis", "deferens", "seminal", "ejaculatory") { return SurfaceStyle(color: rgb("dfb4a2"), fibre: 0, wetness: 0.85).tissue(.hollow) }
            if named("areola", "nipple") { return SurfaceStyle(color: rgb("b77565"), fibre: 0, wetness: 0.45, variation: 0.03).tissue(.skin) }
            if named("mammary", "lactiferous") { return SurfaceStyle(color: rgb("e9c3ad"), fibre: 0, wetness: 0.75, variation: 0.04).tissue(.gland) }
            if named("ovary", "uterus", "uterine", "vagina", "fallopian") { return SurfaceStyle(color: rgb("d9a093"), fibre: 0, wetness: 0.85).tissue(.hollow) }
            if named("prostate") { return SurfaceStyle(color: rgb("c78a7b"), fibre: 0, wetness: 0.8).tissue(.gland) }
            if named("penis", "glans", "corpus") { return SurfaceStyle(color: rgb("d29d8f"), fibre: 0, wetness: 0.8).tissue(.hollow) }
            if named("tongue", "palate", "uvula") { return SurfaceStyle(color: rgb("c9625b"), fibre: 0.4, wetness: 0.95) }
            if named("gingiva") { return SurfaceStyle(color: rgb("d4787a"), fibre: 0, wetness: 0.95).tissue(.hollow) }
            if named("trachea", "bronch", "larynx", "cartilage", "epiglottis") { return SurfaceStyle(color: rgb("dfe5e7"), fibre: 0, wetness: 0.7).tissue(.cartilage) }
            if named("parotid", "submandibular", "sublingual", "hypophysis", "pineal") { return SurfaceStyle(color: rgb("d9a77a"), fibre: 0, wetness: 0.8).tissue(.gland) }
            if named("omentum", "mesocolon", "peritone", "mesentery") { return SurfaceStyle(color: rgb("e8d290"), fibre: 0, wetness: 0.85).tissue(.fat) }
            if named("pleura") { return SurfaceStyle(color: rgb("d3e2ea"), fibre: 0, wetness: 0.95).tissue(.hollow) }
            if named("lung") { return SurfaceStyle(color: rgb("d99a94"), fibre: 0, wetness: 0.85, variation: 0.04).tissue(.lung) }
            if m == "Mucosa" || m == "Mucosa of stomach" { return SurfaceStyle(color: rgb("cf7f7c"), fibre: 0, wetness: 0.95).tissue(.hollow) }
            if m == "Intestine" { return SurfaceStyle(color: rgb("df9c89"), fibre: 0, wetness: 0.95).tissue(.intestine) }
            if m == "Gland" { return SurfaceStyle(color: rgb("d69a72"), fibre: 0, wetness: 0.85).tissue(.gland) }
            return SurfaceStyle(color: rgb("d38b7c"), fibre: 0, wetness: 0.9, variation: 0.03)
        case "lymphoid":
            if named("spleen") || m.hasPrefix("Organ") { return SurfaceStyle(color: rgb("6f2a36"), fibre: 0, wetness: 0.9).tissue(.spleen) }
            if named("thymus") || m == "Gland" { return SurfaceStyle(color: rgb("d8b29a"), fibre: 0, wetness: 0.8).tissue(.gland) }
            return SurfaceStyle(color: rgb("86bc62"), fibre: 0, wetness: 0.7, variation: 0.05).tissue(.gland)
        case "skeletal":
            return SurfaceStyle(color: rgb("ece3cf"), fibre: 0, wetness: 0.3, variation: 0.03)
        case "joints":
            return SurfaceStyle(color: rgb("ddd8c9"), fibre: 0.25, wetness: 0.7)
        case "regions":
            return SurfaceStyle(color: rgb("e5bc9f"), fibre: 0, wetness: 0.35).tissue(.skin)
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
