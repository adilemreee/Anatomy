//
//  AnatomyViewport.swift
//  Anatomy
//

import RealityKit
import SwiftUI
import UIKit

/// What the interactive viewport needs from a scene.
@MainActor
protocol ViewportScene: AnyObject {
    var root: Entity { get }
    var camera: Entity { get }
    /// Asked after every change: the view only draws when something moved.
    var renderSchedule: RenderSchedule { get }
    func orbit(by delta: CGSize)
    func zoom(by factor: CGFloat)
    func pan(by delta: CGSize, viewHeight: CGFloat)
    func beginCameraInteraction()
    func cameraDidSettle()
    func pick(at point: CGPoint, in size: CGSize) async -> PartRef?
}

extension AnatomyScene: ViewportScene {}

/// The interactive 3D view: one finger orbits, two fingers pan, pinch zooms
/// and a tap picks the part under the finger.
struct AnatomyViewport<Scene: ViewportScene, Overlay: View>: View {
    let scene: Scene
    var onTap: (PartRef?) -> Void = { _ in }
    var onSizeChange: (CGSize) -> Void = { _ in }
    /// Drawn in the same coordinate space as the 3D view (e.g. labels).
    @ViewBuilder var overlay: () -> Overlay

    var body: some View {
        GeometryReader { proxy in
            ZStack(alignment: .topLeading) {
                RealityCanvasView(root: scene.root, camera: scene.camera, schedule: scene.renderSchedule)
                .gesture(PanRecognizer(touches: 1...1, scene: scene) { delta in
                    scene.orbit(by: delta)
                })
                .gesture(PanRecognizer(touches: 2...2, scene: scene) { delta in
                    scene.pan(by: delta, viewHeight: proxy.size.height)
                })
                .gesture(PinchRecognizer(scene: scene) { factor in
                    scene.zoom(by: factor)
                })
                .gesture(TapRecognizer { point in
                    let size = proxy.size
                    Task { onTap(await scene.pick(at: point, in: size)) }
                })
                overlay()
            }
            .onAppear { onSizeChange(proxy.size) }
            .onChange(of: proxy.size) { _, size in onSizeChange(size) }
        }
    }
}

extension AnatomyViewport where Overlay == EmptyView {
    init(scene: Scene, onTap: @escaping (PartRef?) -> Void = { _ in }) {
        self.init(scene: scene, onTap: onTap, onSizeChange: { _ in }, overlay: { EmptyView() })
    }
}

/// Lets all of our recognizers run together (pinch + two finger pan).
final class SimultaneousGestureDelegate: NSObject, UIGestureRecognizerDelegate {
    func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldRecognizeSimultaneouslyWith other: UIGestureRecognizer) -> Bool {
        true
    }
}

private struct PanRecognizer: UIGestureRecognizerRepresentable {
    let touches: ClosedRange<Int>
    let scene: any ViewportScene
    let onChange: (CGSize) -> Void

    func makeCoordinator(converter: CoordinateSpaceConverter) -> SimultaneousGestureDelegate {
        SimultaneousGestureDelegate()
    }

    func makeUIGestureRecognizer(context: Context) -> UIPanGestureRecognizer {
        let recognizer = UIPanGestureRecognizer()
        recognizer.minimumNumberOfTouches = touches.lowerBound
        recognizer.maximumNumberOfTouches = touches.upperBound
        recognizer.delegate = context.coordinator
        return recognizer
    }

    func handleUIGestureRecognizerAction(_ recognizer: UIPanGestureRecognizer, context: Context) {
        switch recognizer.state {
        case .began: scene.beginCameraInteraction()
        case .ended, .cancelled, .failed: scene.cameraDidSettle()
        default: break
        }
        guard recognizer.state == .changed else { return }
        let t = recognizer.translation(in: recognizer.view)
        recognizer.setTranslation(.zero, in: recognizer.view)
        onChange(CGSize(width: t.x, height: t.y))
    }
}

private struct PinchRecognizer: UIGestureRecognizerRepresentable {
    let scene: any ViewportScene
    let onChange: (CGFloat) -> Void

    func makeCoordinator(converter: CoordinateSpaceConverter) -> SimultaneousGestureDelegate {
        SimultaneousGestureDelegate()
    }

    func makeUIGestureRecognizer(context: Context) -> UIPinchGestureRecognizer {
        let recognizer = UIPinchGestureRecognizer()
        recognizer.delegate = context.coordinator
        return recognizer
    }

    func handleUIGestureRecognizerAction(_ recognizer: UIPinchGestureRecognizer, context: Context) {
        switch recognizer.state {
        case .began: scene.beginCameraInteraction()
        case .ended, .cancelled, .failed: scene.cameraDidSettle()
        default: break
        }
        guard recognizer.state == .changed else { return }
        onChange(recognizer.scale)
        recognizer.scale = 1
    }
}

private struct TapRecognizer: UIGestureRecognizerRepresentable {
    let onTap: (CGPoint) -> Void

    func makeCoordinator(converter: CoordinateSpaceConverter) -> SimultaneousGestureDelegate {
        SimultaneousGestureDelegate()
    }

    func makeUIGestureRecognizer(context: Context) -> UITapGestureRecognizer {
        let recognizer = UITapGestureRecognizer()
        recognizer.delegate = context.coordinator
        return recognizer
    }

    func handleUIGestureRecognizerAction(_ recognizer: UITapGestureRecognizer, context: Context) {
        guard recognizer.state == .ended else { return }
        onTap(context.converter.localLocation)
    }
}
