//
//  AppModel.swift
//  Anatomy
//

import Observation
import SwiftUI

/// Top-level app state shared through the environment.
@MainActor
@Observable
final class AppModel {
    enum Tab: Hashable {
        case atlas, systems, study, library, search
    }

    var tab: Tab = .atlas
    let store: AtlasStore
    let study: StudyStore
    let scene: AnatomyScene

    init() {
        store = AtlasStore()
        study = StudyStore()
        // Launch arguments for screenshots and testing, e.g.
        // -AtlasLayers skeletal,visceral -AtlasGhost skeletal
        let defaults = UserDefaults.standard
        let layers = defaults.string(forKey: "AtlasLayers").map { Set($0.split(separator: ",").map(String.init)) }
        scene = AnatomyScene(initialLayers: layers)
        for layer in (defaults.string(forKey: "AtlasGhost") ?? "").split(separator: ",") {
            scene.setLayer(String(layer), ghosted: true)
        }
        // -AtlasHideSide muscular:r hides one side of a layer (used for the icon).
        if let spec = defaults.string(forKey: "AtlasHideSide")?.split(separator: ":"), spec.count == 2 {
            let layer = String(spec[0]), side = String(spec[1])
            for (i, part) in (scene.manifests[layer] ?? []).enumerated() where part.side == side {
                scene.hide(PartRef(system: layer, index: i))
            }
        }
        // -AtlasCamera "x,y,z,distance,yaw"
        if let values = defaults.string(forKey: "AtlasCamera")?.split(separator: ",").compactMap({ Float($0) }), values.count == 5 {
            scene.setCamera(target: SIMD3(values[0], values[1], values[2]), distance: values[3], yaw: values[4])
        }
    }

    /// Hides the floating controls (for screenshots).
    var hidesChrome: Bool { UserDefaults.standard.bool(forKey: "AtlasNoChrome") }

    /// Switches to the 3D atlas and frames the parts that show `entry`.
    func showInAtlas(_ entry: AtlasEntry, isolate: Bool = false) {
        let refs = scene.refs(matching: entry.models)
        guard !refs.isEmpty else { return }
        tab = .atlas
        Task { await scene.reveal(refs, isolate: isolate) }
    }

    func showInAtlas(_ refs: [PartRef], isolate: Bool = false) {
        guard !refs.isEmpty else { return }
        tab = .atlas
        Task { await scene.reveal(refs, isolate: isolate) }
    }

    func hasModel(_ entry: AtlasEntry) -> Bool {
        !entry.models.isEmpty && !scene.refs(matching: entry.models).isEmpty
    }
}
