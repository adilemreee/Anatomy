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

    /// Realistic tissue colours or Z-Anatomy's teaching colours; remembered.
    var colorMode: ColorMode {
        get { scene.colorMode }
        set {
            scene.colorMode = newValue
            UserDefaults.standard.set(newValue.rawValue, forKey: "colorMode")
        }
    }
    /// Shown full screen over everything.
    var specimen: SpecimenRequest?
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
        // -AtlasColors educational, otherwise the last choice.
        if let mode = (defaults.string(forKey: "AtlasColors") ?? defaults.string(forKey: "colorMode")).flatMap(ColorMode.init(rawValue:)) {
            scene.colorMode = mode
        }
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
        // Tapping one head of a muscle selects the whole muscle on that side.
        scene.groupResolver = { [weak self] ref in
            guard let self, let info = self.scene.info(ref),
                  let entry = self.store.entry(for: info), self.store.isExact(entry, for: info) else { return [ref] }
            let group = self.scene.refs(matching: entry.models).filter {
                $0.system == ref.system && self.scene.info($0)?.side == info.side
            }
            return group.count <= 6 ? Set(group) : [ref]
        }
        // -AtlasInspect "Sacrum" opens the specimen viewer on launch.
        if let name = defaults.string(forKey: "AtlasInspect") {
            if let entry = store.entries.first(where: { $0.models.contains(name) }) {
                inspect(entry)
            } else {
                let refs = scene.refs(matching: [name])
                if !refs.isEmpty {
                    specimen = specimenRequest(for: refs, title: name, subtitle: name, entryID: nil)
                }
            }
        }
        // -AtlasReveal "Popliteus muscle" finds a structure in the atlas.
        if let name = defaults.string(forKey: "AtlasReveal") {
            let refs = scene.refs(matching: [name])
            Task { await scene.reveal(refs) }
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

    /// Opens the specimen viewer for an entry's parts (one side only).
    func inspect(_ entry: AtlasEntry) {
        var refs = scene.refs(matching: entry.models)
        guard !refs.isEmpty else { return }
        // Bilateral structures: keep the right side, like an atlas plate.
        if refs.contains(where: { scene.info($0)?.side == "r" }) {
            refs = refs.filter { scene.info($0)?.side != "l" }
        }
        // Very large groups would be unreadable on their own.
        if refs.count > 40 { refs = Array(refs.prefix(40)) }
        specimen = specimenRequest(for: refs, title: entry.tr, subtitle: entry.la, entryID: entry.id)
    }

    /// The specimen for `refs`. Muscles come with their attachment patches
    /// (origins red, insertions blue) and the bones they attach to.
    func specimenRequest(for refs: [PartRef], title: String, subtitle: String, entryID: String?) -> SpecimenRequest {
        let muscles = refs.filter { $0.system == "muscular" }.compactMap { scene.info($0) }
        guard !muscles.isEmpty else { return SpecimenRequest(refs: refs, title: title, subtitle: subtitle, entryID: entryID) }
        var names = Set<String>()
        for muscle in muscles {
            names.insert(muscle.base.lowercased())
            if let parent = muscle.path.last { names.insert(parent.lowercased()) }
        }
        let sides = Set(muscles.compactMap(\.side))
        var attachments: [PartRef] = []
        var bones: [PartRef] = []
        var seen = Set<PartRef>()
        for (i, patch) in (scene.manifests["insertions"] ?? []).enumerated()
        where names.contains(patch.base.lowercased()) && (sides.isEmpty || patch.side.map(sides.contains) ?? true) {
            guard let bone = patch.path.last?.lowercased() else { continue }
            // The bone the patch lies on; a few patches in the source are
            // tagged with the wrong side and are left out.
            let carriers = scene.refs(matching: [bone]).filter { ref in
                guard ref.system == "skeletal", let info = scene.info(ref), info.base.lowercased() == bone,
                      info.side == nil || info.side == patch.side else { return false }
                let b = info.bounds, c = patch.center, m: Float = 0.015
                return c.x > b[0] - m && c.x < b[3] + m && c.y > b[1] - m && c.y < b[4] + m && c.z > b[2] - m && c.z < b[5] + m
            }
            guard !carriers.isEmpty else { continue }
            attachments.append(PartRef(system: "insertions", index: i))
            for ref in carriers where seen.insert(ref).inserted { bones.append(ref) }
        }
        return SpecimenRequest(refs: refs + attachments, context: Array(bones.prefix(14)),
                               title: title, subtitle: subtitle, entryID: entryID)
    }

    func hasModel(_ entry: AtlasEntry) -> Bool {
        !entry.models.isEmpty && !scene.refs(matching: entry.models).isEmpty
    }
}
