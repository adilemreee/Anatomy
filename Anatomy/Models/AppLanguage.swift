//
//  AppLanguage.swift
//  Anatomy
//

import Foundation

/// The language the app's content is shown in.
///
/// The interface follows iOS (Localizable.xcstrings). Written content is
/// authored in Turkish (atlas-*.json, questions-*.json, terms.json…) and
/// translated into files with a language suffix (atlas-muscular.en.json),
/// built by tools/i18n. Any other device language gets English.
nonisolated enum AppLanguage {
    static let supported = ["tr", "en", "fr", "de", "es"]

    /// The language iOS picked for this launch among the app's localizations.
    static let current: String = {
        let preferred = Bundle.main.preferredLocalizations.first ?? "en"
        let code = Locale(identifier: preferred).language.languageCode?.identifier ?? preferred
        return supported.contains(code) ? code : "en"
    }()

    static var isTurkish: Bool { current == "tr" }

    static var locale: Locale { Locale(identifier: current) }

    /// The bundled JSON resource for `name` in the current language, falling
    /// back to the Turkish original when there is no translation.
    static func url(for name: String) -> URL? {
        if current != "tr", let url = Bundle.main.url(forResource: "\(name).\(current)", withExtension: "json") {
            return url
        }
        return Bundle.main.url(forResource: name, withExtension: "json")
    }
}
