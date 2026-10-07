//
//  AnatomyViewport.swift
//  Anatomy
//

import RealityKit
import SwiftUI
import UIKit

/// The interactive 3D view: one finger orbits, two fingers pan, pinch zooms
/// and a tap picks the part under the finger.
struct AnatomyViewport: View {
    let scene: AnatomyScene
    var onTap: (PartRef?) -> Void = { _ in }

    var body: some View {
        GeometryReader { proxy in
            RealityView { content in
                content.add(scene.root)
            }
            .gesture(PanRecognizer(touches: 1...1) { delta in
                scene.orbit(by: delta)
            })
            .gesture(PanRecognizer(touches: 2...2) { delta in
                scene.pan(by: delta, viewHeight: proxy.size.height)
            })
            .gesture(PinchRecognizer { factor in
                scene.zoom(by: factor)
            })
            .gesture(TapRecognizer { point in
                onTap(scene.pick(at: point, in: proxy.size))
            })
        }
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
        guard recognizer.state == .changed else { return }
        let t = recognizer.translation(in: recognizer.view)
        recognizer.setTranslation(.zero, in: recognizer.view)
        onChange(CGSize(width: t.x, height: t.y))
    }
}

private struct PinchRecognizer: UIGestureRecognizerRepresentable {
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
