//
//  CameraTween.swift
//  Anatomy
//
//  Camera moves driven by the display refresh instead of a sleeping task, so
//  they stay smooth at 60 and 120 Hz and never drift from the frame clock.
//

import QuartzCore

@MainActor
final class CameraTween: NSObject {
    private var link: CADisplayLink?
    private var startTime: CFTimeInterval?
    private let duration: CFTimeInterval
    private let step: (Float) -> Void
    private let completion: () -> Void

    /// `step` receives the eased progress (0…1) on every frame.
    init(duration: CFTimeInterval = 0.5, step: @escaping (Float) -> Void, completion: @escaping () -> Void) {
        self.duration = duration
        self.step = step
        self.completion = completion
        super.init()
        let link = CADisplayLink(target: self, selector: #selector(tick(_:)))
        link.preferredFrameRateRange = CAFrameRateRange(minimum: 60, maximum: 120, preferred: 120)
        link.add(to: .main, forMode: .common)
        self.link = link
    }

    @objc private func tick(_ link: CADisplayLink) {
        let now = link.targetTimestamp
        let start = startTime ?? link.timestamp
        startTime = start
        let t = Float(min(max((now - start) / duration, 0), 1))
        // Ease in and out (cubic).
        let e = t < 0.5 ? 4 * t * t * t : 1 - pow(-2 * t + 2, 3) / 2
        step(e)
        if t >= 1 {
            stop()
            completion()
        }
    }

    /// Stops without calling the completion.
    func cancel() { stop() }

    private func stop() {
        link?.invalidate()
        link = nil
    }
}
