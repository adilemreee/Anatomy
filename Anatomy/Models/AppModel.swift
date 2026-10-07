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
    let store = AtlasStore()
    let study = StudyStore()
    let scene = AnatomyScene()

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
