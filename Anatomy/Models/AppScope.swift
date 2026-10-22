//
//  AppScope.swift
//  Anatomy
//

import Foundation

/// What this edition of the app covers: the musculoskeletal system (bones,
/// joints and ligaments, muscles and their attachments) and the heart and
/// vessels.
///
/// The other systems (organs, nerves, senses, skin…) stay in the
/// code and in the bundle, switched off here: add their ids back to bring
/// them back in the atlas, the reading pages, the questions and the cards.
nonisolated enum AppScope {
    /// Written systems (atlas-<id>.json, questions-<id>.json).
    static let systems: Set<String> = ["skeletal", "articular", "muscular", "cardiovascular"]
    /// 3D layers (mesh-<id>.bin).
    static let layers: Set<String> = ["skeletal", "joints", "muscular", "insertions", "cardiovascular"]

    static func includes(system id: String) -> Bool { systems.contains(id) }
    static func includes(layer id: String) -> Bool { layers.contains(id) }
}
