//
//  RealityCanvas.swift
//  Anatomy
//
//  Draws a scene with RealityRenderer only when something has changed. A
//  RealityView draws every frame, even when nothing moves, which keeps the
//  GPU busy, warms the phone and drains the battery while someone reads a
//  label. Here the scenes say when they change (RenderSchedule) and the view
//  draws for as long as that needs, then stops.
//

import Metal
import QuartzCore
import RealityKit
import SwiftUI
import UIKit

/// When a scene needs frames: the scene asks after every change, for a
/// short while (GPU uploads and settling) or longer for an animation such
/// as the pulse of a selection.
@MainActor
final class RenderSchedule {
    private(set) var activeUntil: CFTimeInterval = 0
    fileprivate var wake: (() -> Void)?

    func setNeedsDisplay(for seconds: CFTimeInterval = 0.4) {
        activeUntil = max(activeUntil, CACurrentMediaTime() + seconds)
        wake?()
    }

    var isActive: Bool { CACurrentMediaTime() < activeUntil }
}

struct RealityCanvasView: UIViewRepresentable {
    let root: Entity
    let camera: Entity
    let schedule: RenderSchedule

    func makeUIView(context: Context) -> RealityCanvas {
        RealityCanvas(root: root, camera: camera, schedule: schedule)
    }

    func updateUIView(_ view: RealityCanvas, context: Context) {}

    static func dismantleUIView(_ view: RealityCanvas, coordinator: ()) {
        view.detach()
    }
}

final class RealityCanvas: UIView {
    override class var layerClass: AnyClass { CAMetalLayer.self }

    private var metalLayer: CAMetalLayer { layer as! CAMetalLayer }
    private let schedule: RenderSchedule
    private let renderer: RealityRenderer?
    private let queue: MTLCommandQueue?
    private let presented: MTLSharedEvent?
    private var frameNumber = UInt64(0)
    private var link: CADisplayLink?
    private var lastTime: CFTimeInterval?
    /// A frame is owed even if the schedule has run out (a new size, back on screen).
    private var needsFrame = true

    init(root: Entity, camera: Entity, schedule: RenderSchedule) {
        self.schedule = schedule
        let device = MTLCreateSystemDefaultDevice()
        queue = device?.makeCommandQueue()
        presented = device?.makeSharedEvent()
        let renderer = try? RealityRenderer()
        renderer?.entities.append(contentsOf: [root])
        renderer?.activeCamera = camera
        renderer?.cameraSettings.colorBackground = .color(UIColor.clear.cgColor)
        renderer?.cameraSettings.antialiasing = .multisample4X
        self.renderer = renderer
        super.init(frame: .zero)
        isOpaque = false
        backgroundColor = .clear
        metalLayer.device = device
        metalLayer.pixelFormat = .bgra8Unorm_srgb
        metalLayer.framebufferOnly = false
        metalLayer.isOpaque = false
        schedule.wake = { [weak self] in self?.wake() }
        NotificationCenter.default.addObserver(self, selector: #selector(becameActive),
                                               name: UIApplication.didBecomeActiveNotification, object: nil)
    }

    required init?(coder: NSCoder) { fatalError("init(coder:) has not been implemented") }

    /// Lets go of the scene so another view can show it.
    func detach() {
        link?.invalidate()
        link = nil
        schedule.wake = nil
        renderer?.entities.removeAll()
    }

    override func layoutSubviews() {
        super.layoutSubviews()
        let scale = traitCollection.displayScale
        let size = CGSize(width: (bounds.width * scale).rounded(), height: (bounds.height * scale).rounded())
        guard size.width > 0, size.height > 0 else { return }
        metalLayer.contentsScale = scale
        if metalLayer.drawableSize != size {
            metalLayer.drawableSize = size
            wake()
        }
    }

    override func didMoveToWindow() {
        super.didMoveToWindow()
        if window != nil {
            schedule.wake = { [weak self] in self?.wake() }
            wake()
        } else {
            link?.isPaused = true
        }
    }

    @objc private func becameActive() { wake() }

    private func wake() {
        needsFrame = true
        guard window != nil else { return }
        if let link {
            link.isPaused = false
        } else {
            let link = CADisplayLink(target: self, selector: #selector(tick(_:)))
            link.add(to: .main, forMode: .common)
            self.link = link
        }
    }

    @objc private func tick(_ link: CADisplayLink) {
        guard needsFrame || schedule.isActive, window != nil else {
            // Nothing changes: no more frames until the scene asks.
            link.isPaused = true
            lastTime = nil
            return
        }
        guard let renderer, let queue, let presented, metalLayer.drawableSize.width > 0,
              let drawable = metalLayer.nextDrawable() else { return }
        needsFrame = false
        let now = link.targetTimestamp
        let delta = lastTime.map { min(max(now - $0, 0), 1.0 / 15) } ?? 1.0 / 60
        lastTime = now
        frameNumber += 1
        do {
            let output = try RealityRenderer.CameraOutput(.singleProjection(colorTexture: drawable.texture))
            try renderer.updateAndRender(deltaTime: delta, cameraOutput: output,
                                         actionsAfterRender: [.signal(presented, value: frameNumber)])
        } catch {
            return
        }
        // Shown once the GPU has drawn it.
        guard let buffer = queue.makeCommandBuffer() else { return }
        buffer.encodeWaitForEvent(presented, value: frameNumber)
        buffer.present(drawable)
        buffer.commit()
    }
}
