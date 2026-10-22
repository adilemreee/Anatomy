//
//  SplashView.swift
//  Anatomy
//

import SwiftUI

/// The launch animation: the figure rises out of the dark as a skin
/// silhouette, a scan line sweeps across its right half and reveals the
/// muscles and bones under the skin, the name fades in; when the atlas has
/// loaded it opens onto the app.
///
/// The animation runs on its own clock that only advances while frames are
/// drawn: while the 3D atlas is being built behind it the main thread can
/// stall, and the animation then pauses instead of skipping ahead.
struct SplashView: View {
    /// Whether what the splash waits for (the first 3D layers) is ready.
    let isReady: () -> Bool
    /// Called once the figure is on screen: the app builds its screens then.
    let onFigureShown: () -> Void
    let onFinish: () -> Void

    @Environment(\.accessibilityReduceMotion) private var reduceMotion
    @State private var clock = Clock()

    /// Seconds of animation before the splash may leave, and its exit.
    private static let minimum = 2.5, exit = 0.45, longest = 7.0

    var body: some View {
        TimelineView(.animation) { context in
            let t = clock.tick(context.date, ready: isReady(), minimum: reduceMotion ? 0.6 : Self.minimum,
                               longest: Self.longest)
            frame(t: reduceMotion ? max(t, 2.4) : t, leave: clock.leaveProgress(exit: Self.exit))
        }
        .onChange(of: clock.figureShown) { _, shown in
            if shown { onFigureShown() }
        }
        .onChange(of: clock.finished) { _, done in
            if done { onFinish() }
        }
        .accessibilityElement(children: .ignore)
        .accessibilityLabel("Anatomi Atlası yükleniyor")
    }

    private func frame(t: Double, leave: Double) -> some View {
        let figureIn = ease(t / 0.7)
        let reveal = easeInOut((t - 0.45) / 1.15)
        let scan = min(ease((t - 0.45) / 0.2), 1 - ease((t - 1.55) / 0.35))
        let titleIn = ease((t - 1.0) / 0.7)
        return GeometryReader { geo in
            let height = min(geo.size.height * 0.56, 560)
            let width = height * Self.aspect
            ZStack {
                Theme.background.ignoresSafeArea()
                RadialGradient(colors: [Color(hex: "1E4FD8").opacity(0.42 * figureIn), .clear],
                               center: .init(x: 0.5, y: 0.42), startRadius: 10, endRadius: geo.size.height * 0.55)
                    .ignoresSafeArea()
                VStack(spacing: 34) {
                    figure(width: width, height: height, reveal: reveal, scan: scan)
                        .scaleEffect(0.94 + 0.06 * figureIn)
                        .opacity(figureIn)
                        .offset(y: 14 * (1 - figureIn))
                    VStack(spacing: 8) {
                        Text("Anatomi Atlası")
                            .font(.system(size: 30, weight: .bold, design: .rounded))
                            .foregroundStyle(Theme.textPrimary)
                            .tracking(0.4 + 3.6 * (1 - titleIn))
                        Text("3B KAS-İSKELET ANATOMİSİ")
                            .font(.system(size: 11, weight: .semibold))
                            .tracking(3)
                            .foregroundStyle(Theme.accent.opacity(0.9))
                    }
                    .opacity(titleIn)
                    .offset(y: 10 * (1 - titleIn))
                }
                .offset(y: -geo.size.height * 0.02)
            }
            .scaleEffect(1 + 0.08 * leave)
            .opacity(1 - leave)
        }
    }

    private static let aspect: CGFloat = {
        guard let image = UIImage(named: "SplashSkin"), image.size.height > 0 else { return 0.4 }
        return image.size.width / image.size.height
    }()

    /// The skin silhouette, with the muscles shown on the right half up to
    /// the scan line.
    private func figure(width: CGFloat, height: CGFloat, reveal: Double, scan: Double) -> some View {
        let half = width / 2
        let edge = half + half * reveal
        return ZStack(alignment: .leading) {
            Image("SplashSkin")
                .resizable()
                .frame(width: width, height: height)
                .mask(alignment: .leading) {
                    // everything but the revealed band right of the midline
                    HStack(spacing: 0) {
                        Rectangle().frame(width: half)
                        Color.clear.frame(width: edge - half)
                        Rectangle()
                    }
                }
                .shadow(color: Theme.accent.opacity(0.35), radius: 24)
            Image("SplashAnatomy")
                .resizable()
                .frame(width: width, height: height)
                .mask(alignment: .leading) {
                    Rectangle().frame(width: edge)
                }
            // the scan line at the edge of the reveal
            LinearGradient(colors: [.clear, Theme.accent.opacity(0.9), .white, Theme.accent.opacity(0.9), .clear],
                           startPoint: .top, endPoint: .bottom)
                .frame(width: 2.5, height: height * 1.04)
                .shadow(color: Theme.accent, radius: 10)
                .shadow(color: Theme.accent.opacity(0.6), radius: 24)
                .offset(x: edge - 1.25)
                .opacity(scan)
        }
        .frame(width: width, height: height)
    }

    private func ease(_ x: Double) -> Double {
        let t = min(max(x, 0), 1)
        return 1 - pow(1 - t, 3)
    }

    private func easeInOut(_ x: Double) -> Double {
        let t = min(max(x, 0), 1)
        return t < 0.5 ? 4 * t * t * t : 1 - pow(-2 * t + 2, 3) / 2
    }

    /// Animation time that advances by at most a frame's worth per drawn
    /// frame, and the exit once the atlas is ready.
    @Observable
    final class Clock {
        private(set) var finished = false
        private(set) var figureShown = false
        @ObservationIgnored private var last: Date?
        @ObservationIgnored private var time = 0.0
        @ObservationIgnored private var started: Date?
        @ObservationIgnored private var leaving: Double?

        func tick(_ now: Date, ready: Bool, minimum: Double, longest: Double) -> Double {
            if started == nil { started = now }
            if let last { time += min(max(now.timeIntervalSince(last), 0), 1.0 / 30) }
            last = now
            if time > 0.75, !figureShown {
                DispatchQueue.main.async { self.figureShown = true }
            }
            let waitedTooLong = now.timeIntervalSince(started ?? now) > longest
            if leaving == nil, time >= minimum, ready || waitedTooLong {
                leaving = time
            }
            return time
        }

        func leaveProgress(exit: Double) -> Double {
            guard let leaving else { return 0 }
            let p = min((time - leaving) / exit, 1)
            if p >= 1, !finished {
                DispatchQueue.main.async { self.finished = true }
            }
            return p * p
        }
    }
}
