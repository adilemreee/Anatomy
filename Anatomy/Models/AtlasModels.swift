//
//  AtlasModels.swift
//  Anatomy
//

import SwiftUI

/// One anatomical structure in the atlas (a bone, muscle, organ, vessel, nerve…).
nonisolated struct AtlasEntry: Identifiable, Hashable, Sendable, Decodable {
    let id: String
    /// Turkish name.
    let tr: String
    /// Latin name (Terminologia Anatomica).
    let la: String
    /// English name.
    let en: String
    /// Group heading inside the system, e.g. "Üst ekstremite kemikleri".
    let group: String
    let region: BodyRegion
    let summary: String
    let facts: [Fact]
    let sections: [InfoSection]
    let clinical: [String]
    /// High-yield points that exams ask about.
    let tus: [String]
    let related: [String]
    let aliases: [String]
    /// Names of the 3D model objects that show this structure.
    let models: [String]
    /// The group entry this structure is part of (a muscle of a muscle group).
    let parent: String?
    /// Filled in by the store from the file the entry came from.
    var systemID: String = ""

    nonisolated struct Fact: Hashable, Sendable {
        /// The Turkish label, the same in every language: question logic
        /// keys on it ("İnnervasyon").
        let label: String
        let value: String
        /// The label shown, in the app's language.
        var title: String

        init(label: String, value: String, title: String? = nil) {
            self.label = label
            self.value = value
            self.title = title ?? label
        }
    }

    nonisolated struct InfoSection: Hashable, Sendable {
        let title: String
        let body: String
    }

    private enum CodingKeys: String, CodingKey {
        case id, tr, la, en, group, region, summary, facts, sections, clinical, tus, related, aliases, models, parent
    }

    init(from decoder: any Decoder) throws {
        let c = try decoder.container(keyedBy: CodingKeys.self)
        id = try c.decode(String.self, forKey: .id)
        tr = try c.decode(String.self, forKey: .tr)
        la = try c.decode(String.self, forKey: .la)
        en = try c.decode(String.self, forKey: .en)
        group = try c.decode(String.self, forKey: .group)
        region = try c.decodeIfPresent(BodyRegion.self, forKey: .region) ?? .general
        summary = try c.decode(String.self, forKey: .summary)
        let rawFacts = try c.decodeIfPresent([[String]].self, forKey: .facts) ?? []
        // [label, value] in Turkish; translations add the shown label: [label, value, title].
        facts = rawFacts.compactMap { $0.count >= 2 ? Fact(label: $0[0], value: $0[1], title: $0.count > 2 ? $0[2] : nil) : nil }
        let rawSections = try c.decodeIfPresent([[String]].self, forKey: .sections) ?? []
        sections = rawSections.compactMap { $0.count == 2 ? InfoSection(title: $0[0], body: $0[1]) : nil }
        clinical = try c.decodeIfPresent([String].self, forKey: .clinical) ?? []
        tus = try c.decodeIfPresent([String].self, forKey: .tus) ?? []
        related = try c.decodeIfPresent([String].self, forKey: .related) ?? []
        aliases = try c.decodeIfPresent([String].self, forKey: .aliases) ?? []
        models = try c.decodeIfPresent([String].self, forKey: .models) ?? []
        parent = try c.decodeIfPresent(String.self, forKey: .parent)
    }

    /// The value of the first fact whose label matches one of `labels`.
    func fact(_ labels: String...) -> String? {
        facts.first { fact in labels.contains { fact.label.localizedCaseInsensitiveContains($0) } }?.value
    }
}

/// A body system such as the skeletal or nervous system.
nonisolated struct BodySystem: Identifiable, Hashable, Sendable, Decodable {
    let id: String
    let tr: String
    let la: String
    let en: String
    let icon: String
    let color: String
    let summary: String
    let intro: String
    let groups: [String]
    /// Which 3D layer shows this system.
    let layer: String?

    var tint: Color { Color(hex: color) }
}

nonisolated enum BodyRegion: String, CaseIterable, Identifiable, Hashable, Sendable, Codable {
    case head, neck, thorax, abdomen, pelvis, back, upperLimb, lowerLimb, general

    var id: String { rawValue }

    var title: String {
        switch self {
        case .head: String(localized: "Baş")
        case .neck: String(localized: "Boyun")
        case .thorax: String(localized: "Göğüs (Toraks)")
        case .abdomen: String(localized: "Karın (Abdomen)")
        case .pelvis: String(localized: "Pelvis ve Perine")
        case .back: String(localized: "Sırt")
        case .upperLimb: String(localized: "Üst Ekstremite")
        case .lowerLimb: String(localized: "Alt Ekstremite")
        case .general: String(localized: "Genel / Tüm Vücut")
        }
    }

    var icon: String {
        switch self {
        case .head: "brain.head.profile"
        case .neck: "person.bust"
        case .thorax: "lungs"
        case .abdomen: "circle.grid.cross"
        case .pelvis: "figure.dress.line.vertical.figure"
        case .back: "figure.stand"
        case .upperLimb: "hand.raised"
        case .lowerLimb: "figure.walk"
        case .general: "figure.arms.open"
        }
    }
}

extension Color {
    nonisolated init(hex: String) {
        var value: UInt64 = 0
        Scanner(string: hex.trimmingCharacters(in: CharacterSet(charactersIn: "#"))).scanHexInt64(&value)
        self.init(
            red: Double((value >> 16) & 0xFF) / 255,
            green: Double((value >> 8) & 0xFF) / 255,
            blue: Double(value & 0xFF) / 255
        )
    }
}
