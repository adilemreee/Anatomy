//
//  PremiumFeature.swift
//  Anatomy
//

import Foundation

/// What a locked tap was trying to open; the paywall leads with it.
enum PremiumFeature: Hashable {
    case system(String)
    case structure(String)
    case inspection
    case questions
    case exam
    case statistics
    case flashcards
    case femaleAnatomy
    case general

    var title: String {
        switch self {
        case .system(let name): String(localized: "\(name) Premium'da")
        case .structure(let name): String(localized: "\(name) Premium'da")
        case .inspection: String(localized: "İnceleme modu Premium'da")
        case .questions: String(localized: "Günlük ücretsiz sorularını bitirdin")
        case .exam: String(localized: "Deneme sınavları Premium'da")
        case .statistics: String(localized: "Ayrıntılı istatistikler Premium'da")
        case .flashcards: String(localized: "Tüm bilgi kartları Premium'da")
        case .femaleAnatomy: String(localized: "Kadın anatomisi Premium'da")
        case .general: String(localized: "Anatomi Atlası Premium")
        }
    }
}

struct PaywallContext: Identifiable, Hashable {
    let id = UUID()
    let feature: PremiumFeature
}
