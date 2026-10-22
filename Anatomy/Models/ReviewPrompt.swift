//
//  ReviewPrompt.swift
//  Anatomy
//

import Foundation

/// When to ask for an App Store rating: right after a test that went well,
/// once someone has solved enough questions to judge the app, and at most
/// once per app version. The system shows the prompt at most three times a
/// year on top of this.
enum ReviewPrompt {
    private static let key = "review.askedVersion"

    private static var version: String {
        Bundle.main.infoDictionary?["CFBundleShortVersionString"] as? String ?? ""
    }

    static func shouldAsk(score: Double, questions: Int, answeredInTotal: Int) -> Bool {
        score >= 0.7 && questions >= 5 && answeredInTotal >= 40
            && UserDefaults.standard.string(forKey: key) != version
    }

    static func markAsked() {
        UserDefaults.standard.set(version, forKey: key)
    }
}
