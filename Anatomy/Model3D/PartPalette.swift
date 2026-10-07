//
//  PartPalette.swift
//  Anatomy
//
//  Z-Anatomy keeps its colours in shader node graphs, so the export has no
//  usable per-part colour. The atlas colours parts by system, hierarchy and
//  name instead, following common anatomical illustration conventions.
//

import Foundation

nonisolated enum PartPalette {
    static func color(for part: PartInfo, layer: String) -> String {
        let name = part.base.lowercased()
        let path = part.path.map { $0.lowercased() }
        func inPath(_ words: String...) -> Bool {
            path.contains { p in words.contains { p.contains($0) } }
        }
        func named(_ words: String...) -> Bool {
            words.contains { name.contains($0) }
        }

        switch layer {
        case "skeletal":
            if named("tooth", "teeth", "incisor", "canine", "molar", "premolar") || inPath("teeth") { return "f3efe4" }
            if named("cartilage") || inPath("cartilage") { return "b7cdd6" }
            return "e7dbc1"

        case "joints":
            if named("disc", "nucleus pulposus", "symphysis", "meniscus", "labrum", "cartilage") { return "a9c6d3" }
            if named("capsule", "membrane") { return "cfc6b3" }
            return "d8cfb6"

        case "muscular":
            if named("bursa") || inPath("bursae") { return "b9d3e2" }
            if named("sheath") || inPath("tendon sheath") { return "c6d6e2" }
            if named("tendon", "aponeurosis", "linea alba", "retinacul", "ligament", "arch", "band", "tract") { return "e3d8bf" }
            if part.isFascia || named("fascia", "septum") { return "d8cdbd" }
            return "b4433b"

        case "insertions":
            return part.kind == "origin" ? "d9473f" : "3d78d6"

        case "cardiovascular":
            if inPath("valvular complex") || named("leaflet", "cusp", "valve") { return "e8d1bd" }
            if named("papillary") { return "a63a3a" }
            if inPath("heart") && !inPath("arteries of heart", "cardiac veins") || named("atrium", "ventricle") { return "a9393a" }
            if inPath("pulmonary arteries") || named("pulmonary trunk", "pulmonary artery") { return "4a6fc7" }
            if inPath("pulmonary veins") || named("pulmonary vein") { return "c8352f" }
            if inPath("vein", "venous", "sinus", "vena cava") || named("vein", "vena", "sinus", "plexus") { return "3e62b9" }
            return "c8302c"

        case "nervous":
            if inPath("eye") {
                if named("lens") { return "e9f0f3" }
                if named("iris") { return "6b8fb0" }
                if named("muscle") { return "b4433b" }
                if named("retina", "choroid") { return "c56a5c" }
                return "efe9dc"
            }
            if inPath("ear") { return "e3cfa9" }
            if inPath("meninges") || named("dura", "arachnoid", "pia mater") { return "cdb7d3" }
            if inPath("spinal cord") && !inPath("spinal nerves") { return "e8d3a2" }
            if inPath("brain") {
                if named("ventricle", "aqueduct", "choroid") { return "8ab4d8" }
                if named("cerebell") || inPath("cerebellum") { return "d8a59d" }
                if inPath("brainstem", "brain stem", "midbrain", "pons", "medulla") { return "e2c09f" }
                return "e0b9ae"
            }
            if named("ganglion", "ganglia") || inPath("ganglia") { return "d9a33a" }
            return "e9c13b"

        case "visceral":
            if named("lobe of", "lung") && !named("bronch") { return "e39b98" }
            if named("bronch", "trachea") { return "d9e2e7" }
            if named("pleura") { return "cfe0ea" }
            if named("liver", "segment of liver") { return "8f3a2d" }
            if named("gallbladder", "bile duct") { return "5d8d3e" }
            if named("pancrea") { return "e3b577" }
            if named("stomach") { return "d98a7b" }
            if named("duodenum", "jejunum", "ileum") { return "e2a08e" }
            if named("colon", "caecum", "cecum", "appendix", "taenia", "rectum") { return "c98a6c" }
            if named("omentum", "mesocolon", "meso-") { return "ecd89a" }
            if named("kidney", "renal") { return "8b3a33" }
            if named("ureter", "bladder", "urethra") { return "e2bf78" }
            if named("thyroid") { return "a8473e" }
            if named("parathyroid", "suprarenal", "adrenal") { return "d9a24a" }
            if named("hypophysis", "pineal") { return "d39a7c" }
            if named("testis", "epididymis", "ductus deferens", "ejaculatory", "seminal") { return "dfb3a1" }
            if named("prostate") { return "c7897a" }
            if named("penis", "glans", "corpus") { return "d39d8e" }
            if named("parotid", "submandibular", "sublingual") { return "dab27c" }
            if named("tongue", "uvula", "palate") { return "c9625b" }
            if named("gingiva") { return "d9827b" }
            if named("pharynx", "oesophagus", "epiglottis", "mucosa") { return "d18780" }
            return "d98b7c"

        case "lymphoid":
            if named("spleen") { return "7d2f3b" }
            if named("thymus") { return "d8b8a1" }
            if named("tonsil") { return "c97a70" }
            return "86bb63"

        case "regions":
            if named("hair", "eyebrow", "eyelash") { return "4b3a31" }
            if named("nail") { return "ecd5ca" }
            return "e7c2a6"

        default:
            return "cccccc"
        }
    }
}
