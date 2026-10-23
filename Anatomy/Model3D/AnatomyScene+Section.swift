//
//  AnatomyScene+Section.swift
//  Anatomy
//
//  Section view: a plane cuts the body and everything on one side of it is
//  left out, so a horizontal, sagittal or coronal section shows the way it
//  does on a CT or MRI slice. The shader does the cutting (the plane travels
//  in the material constants, see AnatomyMaterials.sectioned); picking and
//  labels skip what was cut away.
//

import RealityKit
import SwiftUI

/// A cutting plane across one of the body's axes.
nonisolated struct SectionPlane: Hashable, Sendable {
    enum Axis: Int, CaseIterable, Identifiable, Sendable {
        /// Left from right (the x axis).
        case sagittal = 0
        /// Head from feet (the y axis): an axial slice.
        case horizontal = 1
        /// Front from back (the z axis).
        case coronal = 2

        var id: Int { rawValue }

        /// In the order the picker lists them.
        static let ordered: [Axis] = [.horizontal, .sagittal, .coronal]

        var title: String {
            switch self {
            case .horizontal: String(localized: "Yatay")
            case .sagittal: String(localized: "Sagital")
            case .coronal: String(localized: "Koronal")
            }
        }

        /// The value the shader reads from the metallic scale.
        var code: Float { [0.2, 0.5, 0.8][rawValue] }
    }

    var axis: Axis
    /// Where the plane crosses the axis, in metres.
    var offset: Float
    /// Keeps what lies below the offset (the right side, the feet, the back)
    /// rather than above it.
    var keepBelow = true

    func keeps(_ p: SIMD3<Float>) -> Bool {
        keepBelow ? p[axis.rawValue] <= offset : p[axis.rawValue] >= offset
    }

    /// Whether anything inside the box is kept.
    func keeps(lo: SIMD3<Float>, hi: SIMD3<Float>) -> Bool {
        keepBelow ? lo[axis.rawValue] <= offset : hi[axis.rawValue] >= offset
    }
}

extension AnatomyScene {
    /// The body's extent along an axis (the parts of the layers on show),
    /// for the slider.
    func sectionRange(_ axis: SectionPlane.Axis) -> ClosedRange<Float> {
        var lo = Float.greatestFiniteMagnitude, hi = -Float.greatestFiniteMagnitude
        for (id, system) in systems where enabledLayers.contains(id) {
            for box in system.bounds {
                lo = min(lo, box.min[axis.rawValue])
                hi = max(hi, box.max[axis.rawValue])
            }
        }
        return lo < hi ? lo...hi : -1...1
    }

    /// Turns the camera to the cut face: an axial slice close up from above
    /// (or below), a sagittal or coronal one from the side it was cut on,
    /// head to hips (the most there is to see; the rest is a pan away).
    /// `covered` is the share of the view's bottom that controls cover; the
    /// slice sits above them.
    func faceSection(_ plane: SectionPlane, covered: Float = 0.4) {
        let trunk = sectionRange(.horizontal).upperBound - 0.32
        let center: SIMD3<Float>, newDistance: Float, newYaw: Float, newPitch: Float
        switch plane.axis {
        case .horizontal:
            center = SIMD3(0, plane.offset, 0)
            newDistance = 1.0
            newYaw = 0
            newPitch = plane.keepBelow ? 1.1 : -1.1
        case .sagittal:
            center = SIMD3(plane.offset, trunk, 0)
            newDistance = 2.1
            newYaw = plane.keepBelow ? .pi / 2 : -.pi / 2
            newPitch = 0.05
        case .coronal:
            center = SIMD3(0, trunk, plane.offset)
            newDistance = 2.1
            newYaw = plane.keepBelow ? 0 : .pi
            newPitch = 0.05
        }
        let up = SIMD3(-sin(newPitch) * sin(newYaw), cos(newPitch), -sin(newPitch) * cos(newYaw))
        let lift = newDistance * tan(fieldOfView * .pi / 360) * covered
        animateCamera(target: center - up * lift, distance: newDistance, yaw: newYaw, pitch: newPitch)
    }

    /// Moves the camera with an axial plane being slid up or down.
    func followSection(by delta: Float) {
        tween?.cancel()
        target.y += delta
        applyCamera()
    }
}
