//
//  Diagnostics.swift
//  Anatomy
//

import Foundation
import MetricKit

/// Crash, hang and performance reports from MetricKit. iOS hands them to the
/// app about once a day (diagnostics right after a crash or hang, on the next
/// launch); they are kept on the device, the latest 20, and the user can send
/// them from the Profile tab. The same reports reach Xcode's Organizer for
/// users who share analytics with developers. The signposts time the atlas
/// and specimen loads, which then show up in the metric reports.
final class Diagnostics: NSObject, MXMetricManagerSubscriber {
    static let shared = Diagnostics()
    nonisolated static let log = MXMetricManager.makeLogHandle(category: "Atlas")
    private static let limit = 20

    func start() {
        MXMetricManager.shared.add(self)
    }

    nonisolated func didReceive(_ payloads: [MXMetricPayload]) {
        for payload in payloads { Self.save(payload.jsonRepresentation(), kind: "metrics", at: payload.timeStampEnd) }
    }

    nonisolated func didReceive(_ payloads: [MXDiagnosticPayload]) {
        for payload in payloads { Self.save(payload.jsonRepresentation(), kind: "diagnostics", at: payload.timeStampEnd) }
    }

    /// The saved reports, newest first.
    nonisolated static var reports: [URL] {
        let files = (try? FileManager.default.contentsOfDirectory(at: folder, includingPropertiesForKeys: nil)) ?? []
        return files.filter { $0.pathExtension == "json" }.sorted { $0.lastPathComponent > $1.lastPathComponent }
    }

    nonisolated private static var folder: URL {
        URL.applicationSupportDirectory.appending(path: "Diagnostics", directoryHint: .isDirectory)
    }

    nonisolated private static func save(_ data: Data, kind: String, at date: Date) {
        let manager = FileManager.default
        try? manager.createDirectory(at: folder, withIntermediateDirectories: true)
        let stamp = date.formatted(.iso8601.year().month().day().time(includingFractionalSeconds: false)).replacingOccurrences(of: ":", with: "")
        try? data.write(to: folder.appending(path: "\(stamp)-\(kind).json"), options: .atomic)
        for old in reports.dropFirst(limit) { try? manager.removeItem(at: old) }
    }
}
