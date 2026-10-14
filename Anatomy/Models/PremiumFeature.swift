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
        case .system(let name): "\(name) Premium'da"
        case .structure(let name): "\(name) Premium'da"
        case .inspection: "İnceleme modu Premium'da"
        case .questions: "Günlük ücretsiz sorularını bitirdin"
        case .exam: "Deneme sınavları Premium'da"
        case .statistics: "Ayrıntılı istatistikler Premium'da"
        case .flashcards: "Tüm bilgi kartları Premium'da"
        case .femaleAnatomy: "Kadın anatomisi Premium'da"
        case .general: "Anatomi Atlası Premium"
        }
    }
}

struct PaywallContext: Identifiable, Hashable {
    let id = UUID()
    let feature: PremiumFeature
}
