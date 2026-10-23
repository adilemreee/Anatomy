//
//  ReviewReminder.swift
//  Anatomy
//

import Foundation
import UserNotifications

/// The daily review reminder: at a time the user picks, how many flashcards
/// wait for review that day. A notification's text is fixed when it is
/// scheduled, so the next seven days are planned ahead with the count each
/// day will have, and planned again whenever the app goes to the background.
@MainActor
enum ReviewReminder {
    static let enabledKey = "reminder.enabled"
    /// Minutes after midnight.
    static let timeKey = "reminder.minutes"
    static let defaultMinutes = 20 * 60
    private static let prefix = "review."

    static var isEnabled: Bool { UserDefaults.standard.bool(forKey: enabledKey) }

    static var minutes: Int {
        UserDefaults.standard.object(forKey: timeKey) as? Int ?? defaultMinutes
    }

    /// Asks for permission; false when the user declined (now or before).
    static func requestPermission() async -> Bool {
        let center = UNUserNotificationCenter.current()
        let settings = await center.notificationSettings()
        switch settings.authorizationStatus {
        case .authorized, .provisional, .ephemeral: return true
        case .denied: return false
        default: return (try? await center.requestAuthorization(options: [.alert, .sound, .badge])) ?? false
        }
    }

    /// Replaces the planned reminders. `dueCards` counts the cards due by a
    /// date; a day that was already studied gets no reminder.
    static func schedule(studiedToday: Bool, dueCards: (Date) -> Int) {
        let center = UNUserNotificationCenter.current()
        let ids = (0..<7).map { "\(prefix)\($0)" }
        center.removePendingNotificationRequests(withIdentifiers: ids)
        guard isEnabled else { return }
        let calendar = Calendar.current
        let today = calendar.startOfDay(for: .now)
        for day in 0..<7 {
            guard let date = calendar.date(byAdding: .minute, value: minutes, to: calendar.date(byAdding: .day, value: day, to: today) ?? today),
                  date > .now, !(day == 0 && studiedToday) else { continue }
            let count = dueCards(date)
            let content = UNMutableNotificationContent()
            content.title = String(localized: "Tekrar zamanı")
            content.body = count > 0
                ? String(localized: "Bugün \(count) kartın seni bekliyor.")
                : String(localized: "Günlük hedefin için kısa bir tekrara ne dersin?")
            content.sound = .default
            let components = calendar.dateComponents([.year, .month, .day, .hour, .minute], from: date)
            let request = UNNotificationRequest(identifier: ids[day], content: content,
                                                trigger: UNCalendarNotificationTrigger(dateMatching: components, repeats: false))
            center.add(request)
        }
    }
}
