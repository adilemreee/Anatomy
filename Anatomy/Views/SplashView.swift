//
//  SplashView.swift
//  Anatomy
//

import SwiftUI
import UIKit

/// The launch animation: the figure rises out of the dark as a skin
/// silhouette, a scan line sweeps across its right half and reveals the
/// muscles and bones under the skin, the name fades in; when the atlas has
/// loaded it opens onto the app.
///
/// Building the 3D atlas behind it holds up the main thread for a few
/// hundred milliseconds at a time, so the animation is made of Core
/// Animation layers: the render server plays them on its own and they stay
/// smooth while the app is busy. The app starts building its screens as
/// soon as the animation is running.
struct SplashView: View {
    /// Whether what the splash waits for (the first 3D layers) is ready.
    let isReady: () -> Bool
    /// Called once the animation runs: the app builds its screens then.
    let onFigureShown: () -> Void
    let onFinish: () -> Void

    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    var body: some View {
        SplashAnimation(reduceMotion: reduceMotion, isReady: isReady, onStarted: onFigureShown, onFinish: onFinish)
            .ignoresSafeArea()
            .accessibilityElement(children: .ignore)
            .accessibilityLabel("Anatomi Atlası yükleniyor")
    }
}

private struct SplashAnimation: UIViewRepresentable {
    let reduceMotion: Bool
    let isReady: () -> Bool
    let onStarted: () -> Void
    let onFinish: () -> Void

    func makeUIView(context: Context) -> SplashLayerView {
        SplashLayerView(reduceMotion: reduceMotion, isReady: isReady, onStarted: onStarted, onFinish: onFinish)
    }

    func updateUIView(_ view: SplashLayerView, context: Context) {}
}

private final class SplashLayerView: UIView {
    /// Seconds of animation before the splash may leave, its exit, and the
    /// longest it waits for the atlas.
    private static let minimum = 2.5, exit = 0.45, longest = 7.0

    private let reduceMotion: Bool
    private let isReady: () -> Bool
    private let onStarted: () -> Void
    private let onFinish: () -> Void

    private let content = CALayer()
    private let glow = CAGradientLayer()
    private let figure = CALayer()
    private let skinHolder = CALayer()
    private let skin = CALayer()
    private let skinMask = CALayer()
    private let skinMaskLeft = CALayer()
    private let skinMaskRight = CALayer()
    private let anatomy = CALayer()
    private let anatomyMask = CALayer()
    private let scanGlow = CAGradientLayer()
    private let scan = CAGradientLayer()
    private let titles = CALayer()
    private let title = CATextLayer()
    private let subtitle = CATextLayer()
    private var started = false

    private static let skinImage = UIImage(named: "SplashSkin")
    private static let anatomyImage = UIImage(named: "SplashAnatomy")
    private static let aspect: CGFloat = {
        guard let image = skinImage, image.size.height > 0 else { return 0.4 }
        return image.size.width / image.size.height
    }()

    init(reduceMotion: Bool, isReady: @escaping () -> Bool, onStarted: @escaping () -> Void, onFinish: @escaping () -> Void) {
        self.reduceMotion = reduceMotion
        self.isReady = isReady
        self.onStarted = onStarted
        self.onFinish = onFinish
        super.init(frame: .zero)
        backgroundColor = UIColor(Theme.background)
        isUserInteractionEnabled = true
        buildLayers()
    }

    required init?(coder: NSCoder) { fatalError("init(coder:) has not been implemented") }

    private func buildLayers() {
        let accent = UIColor(Theme.accent)
        layer.addSublayer(content)

        glow.type = .radial
        glow.colors = [UIColor(Color(hex: "1E4FD8")).withAlphaComponent(0.42).cgColor, UIColor.clear.cgColor]
        content.addSublayer(glow)

        // The skin, hidden over the revealed band right of the midline.
        skin.contents = Self.skinImage?.cgImage
        skin.contentsGravity = .resize
        skinMaskLeft.backgroundColor = UIColor.black.cgColor
        skinMaskRight.backgroundColor = UIColor.black.cgColor
        skinMask.addSublayer(skinMaskLeft)
        skinMask.addSublayer(skinMaskRight)
        skin.mask = skinMask
        skinHolder.addSublayer(skin)
        skinHolder.shadowColor = accent.cgColor
        skinHolder.shadowOpacity = 0.35
        skinHolder.shadowRadius = 24
        skinHolder.shadowOffset = .zero
        figure.addSublayer(skinHolder)

        // The muscles and bones, shown up to the scan line.
        anatomy.contents = Self.anatomyImage?.cgImage
        anatomy.contentsGravity = .resize
        anatomyMask.backgroundColor = UIColor.black.cgColor
        anatomy.mask = anatomyMask
        figure.addSublayer(anatomy)

        // The scan line at the edge of the reveal, with a wide and a tight glow.
        for (line, radius, strength) in [(scanGlow, CGFloat(24), Float(0.6)), (scan, 10, 1)] {
            line.colors = [UIColor.clear, accent.withAlphaComponent(0.9), .white, accent.withAlphaComponent(0.9), .clear].map(\.cgColor)
            line.startPoint = CGPoint(x: 0.5, y: 0)
            line.endPoint = CGPoint(x: 0.5, y: 1)
            line.shadowColor = accent.cgColor
            line.shadowRadius = radius
            line.shadowOpacity = strength
            line.shadowOffset = .zero
            line.opacity = 0
            figure.addSublayer(line)
        }
        content.addSublayer(figure)

        title.string = NSAttributedString(string: String(localized: "Anatomi Atlası"), attributes: [
            .font: UIFont.systemFont(ofSize: 30, weight: .bold).rounded,
            .foregroundColor: UIColor(Theme.textPrimary),
            .kern: 0.4,
        ])
        subtitle.string = NSAttributedString(string: String(localized: "3B KAS-İSKELET ANATOMİSİ"), attributes: [
            .font: UIFont.systemFont(ofSize: 11, weight: .semibold),
            .foregroundColor: accent.withAlphaComponent(0.9),
            .kern: 3,
        ])
        for text in [title, subtitle] {
            text.alignmentMode = .center
            text.truncationMode = .end
            titles.addSublayer(text)
        }
        content.addSublayer(titles)
    }

    override func layoutSubviews() {
        super.layoutSubviews()
        guard bounds.width > 0, bounds.height > 0 else { return }
        CATransaction.begin()
        CATransaction.setDisableActions(true)
        let size = bounds.size
        content.frame = bounds
        glow.frame = bounds
        glow.startPoint = CGPoint(x: 0.5, y: 0.42)
        glow.endPoint = CGPoint(x: 0.5 + size.height * 0.55 / size.width, y: 0.42 + 0.55)

        let height = min(size.height * 0.56, 560), width = height * Self.aspect
        let titleHeight = ceil(UIFont.systemFont(ofSize: 30, weight: .bold).rounded.lineHeight)
        let subtitleHeight = ceil(UIFont.systemFont(ofSize: 11, weight: .semibold).lineHeight)
        let stack = height + 34 + titleHeight + 8 + subtitleHeight
        let top = (size.height - stack) / 2 - size.height * 0.02
        figure.frame = CGRect(x: (size.width - width) / 2, y: top, width: width, height: height)
        for layer in [skinHolder, skin, skinMask, anatomy] { layer.frame = figure.bounds }
        // Fully revealed: the animations start from the closed state.
        let half = width / 2
        skinMaskLeft.frame = CGRect(x: 0, y: 0, width: half, height: height)
        skinMaskRight.frame = CGRect(x: width, y: 0, width: half, height: height)
        anatomyMask.frame = CGRect(x: 0, y: 0, width: width, height: height)
        for line in [scanGlow, scan] {
            line.frame = CGRect(x: width - 1.25, y: -height * 0.02, width: 2.5, height: height * 1.04)
        }
        titles.frame = CGRect(x: 16, y: top + height + 34, width: size.width - 32, height: titleHeight + 8 + subtitleHeight)
        title.frame = CGRect(x: 0, y: 0, width: titles.bounds.width, height: titleHeight)
        subtitle.frame = CGRect(x: 0, y: titleHeight + 8, width: titles.bounds.width, height: subtitleHeight)
        for text in [title, subtitle] { text.contentsScale = traitCollection.displayScale }
        CATransaction.commit()

        if !started {
            started = true
            start()
        }
    }

    // MARK: Animation

    private static let easeOut = CAMediaTimingFunction(controlPoints: 0.215, 0.61, 0.355, 1)
    private static let easeInOut = CAMediaTimingFunction(controlPoints: 0.645, 0.045, 0.355, 1)
    private static let easeIn = CAMediaTimingFunction(controlPoints: 0.55, 0.085, 0.68, 0.53)

    private func start() {
        let width = figure.bounds.width, half = width / 2
        if !reduceMotion {
            let t0 = CACurrentMediaTime() + 0.05
            animate(content: glow, "opacity", from: 0, to: 1, at: t0, 0.7)
            animate(content: figure, "opacity", from: 0, to: 1, at: t0, 0.7)
            animate(content: figure, "transform", from: CATransform3DConcat(CATransform3DMakeScale(0.94, 0.94, 1), CATransform3DMakeTranslation(0, 14, 0)),
                    to: CATransform3DIdentity, at: t0, 0.7)
            // The reveal: the skin opens and the anatomy follows the scan line.
            animate(content: skinMaskRight, "position.x", from: half + half / 2, to: width + half / 2, at: t0 + 0.45, 1.15, Self.easeInOut)
            animate(content: anatomyMask, "position.x", from: half - width / 2, to: width / 2, at: t0 + 0.45, 1.15, Self.easeInOut)
            for line in [scanGlow, scan] {
                animate(content: line, "position.x", from: half, to: width, at: t0 + 0.45, 1.15, Self.easeInOut)
                let fade = CAKeyframeAnimation(keyPath: "opacity")
                fade.values = [0, 1, 1, 0]
                fade.keyTimes = [0, 0.2 / 1.45, 1.1 / 1.45, 1].map { NSNumber(value: $0) }
                fade.timingFunctions = [Self.easeOut, CAMediaTimingFunction(name: .linear), Self.easeOut]
                fade.beginTime = t0 + 0.45
                fade.duration = 1.45
                fade.fillMode = .both
                line.add(fade, forKey: "fade")
            }
            animate(content: titles, "opacity", from: 0, to: 1, at: t0 + 1.0, 0.7)
            animate(content: titles, "transform", from: CATransform3DMakeTranslation(0, 10, 0), to: CATransform3DIdentity, at: t0 + 1.0, 0.7)
        }

        // Let the first frames reach the screen, then build the app behind.
        let launched = Date()
        Task { @MainActor [weak self] in
            try? await Task.sleep(for: .milliseconds(150))
            self?.onStarted()
            try? await Task.sleep(for: .seconds(self?.reduceMotion == true ? 0.6 : Self.minimum))
            while let self, !self.isReady(), Date().timeIntervalSince(launched) < Self.longest {
                try? await Task.sleep(for: .milliseconds(100))
            }
            self?.leave()
        }
    }

    private func leave() {
        CATransaction.begin()
        CATransaction.setCompletionBlock { [onFinish] in onFinish() }
        content.opacity = 0
        content.transform = CATransform3DMakeScale(1.08, 1.08, 1)
        animate(content: content, "opacity", from: 1, to: 0, at: CACurrentMediaTime(), Self.exit, Self.easeIn)
        animate(content: content, "transform", from: CATransform3DIdentity, to: CATransform3DMakeScale(1.08, 1.08, 1),
                at: CACurrentMediaTime(), Self.exit, Self.easeIn)
        backgroundColor = .clear
        let fade = CABasicAnimation(keyPath: "backgroundColor")
        fade.fromValue = UIColor(Theme.background).cgColor
        fade.toValue = UIColor.clear.cgColor
        fade.duration = Self.exit
        fade.timingFunction = Self.easeIn
        layer.add(fade, forKey: "fade")
        CATransaction.commit()
    }

    private func animate(content layer: CALayer, _ keyPath: String, from: Any, to: Any, at begin: CFTimeInterval,
                         _ duration: CFTimeInterval, _ timing: CAMediaTimingFunction = SplashLayerView.easeOut) {
        let animation = CABasicAnimation(keyPath: keyPath)
        animation.fromValue = from
        animation.toValue = to
        animation.beginTime = begin
        animation.duration = duration
        animation.timingFunction = timing
        animation.fillMode = .backwards
        layer.add(animation, forKey: keyPath)
    }
}

private extension UIFont {
    var rounded: UIFont {
        fontDescriptor.withDesign(.rounded).map { UIFont(descriptor: $0, size: pointSize) } ?? self
    }
}
