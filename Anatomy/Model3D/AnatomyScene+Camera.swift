//
//  AnatomyScene+Camera.swift
//  Anatomy
//

import RealityKit
import SwiftUI

extension AnatomyScene {
    func orbit(by delta: CGSize) {
        tween?.cancel()
        yaw -= Float(delta.width) * 0.008
        pitch = min(max(pitch + Float(delta.height) * 0.006, -1.45), 1.45)
        applyCamera()
    }

    func zoom(by factor: CGFloat) {
        tween?.cancel()
        distance = min(max(distance / Float(factor), 0.1), 5)
        applyCamera()
    }

    func pan(by delta: CGSize, viewHeight: CGFloat) {
        tween?.cancel()
        let worldPerPoint = 2 * distance * tan(fieldOfView * .pi / 360) / Float(max(viewHeight, 1))
        let m = camera.transformMatrix(relativeTo: nil)
        let right = SIMD3(m.columns.0.x, m.columns.0.y, m.columns.0.z)
        let up = SIMD3(m.columns.1.x, m.columns.1.y, m.columns.1.z)
        target -= right * Float(delta.width) * worldPerPoint
        target += up * Float(delta.height) * worldPerPoint
        target = simd_clamp(target, SIMD3(-1.2, -0.4, -1.2), SIMD3(1.2, 2.3, 1.2))
        applyCamera()
    }

    func setCamera(target newTarget: SIMD3<Float>, distance newDistance: Float, yaw newYaw: Float, pitch newPitch: Float = 0.05) {
        tween?.cancel()
        target = newTarget
        distance = newDistance
        yaw = newYaw
        pitch = newPitch
        applyCamera()
    }

    func resetCamera() {
        animateCamera(target: Self.homeTarget, distance: Self.homeDistance, yaw: 0, pitch: 0.05)
    }

    func rotate(toYaw newYaw: Float) {
        animateCamera(target: target, distance: distance, yaw: newYaw, pitch: 0.05)
    }

    /// Moves the camera so that `refs` fill the view.
    func frame(_ refs: [PartRef], margin: Float = 1.15) {
        var lo = SIMD3<Float>(repeating: .greatestFiniteMagnitude)
        var hi = -lo
        for ref in refs {
            guard let info = info(ref) else { continue }
            let b = info.bounds
            lo = simd_min(lo, SIMD3(b[0], b[1], b[2]))
            hi = simd_max(hi, SIMD3(b[3], b[4], b[5]))
        }
        guard lo.x <= hi.x else { return }
        let center = (lo + hi) / 2
        let radius = max(simd_length(hi - lo) / 2, 0.03)
        let fit = radius / sin(fieldOfView * .pi / 360) * margin
        // Look at the part from the side it faces most.
        var newYaw = yaw
        if abs(center.x) > 0.12, abs(center.x) > abs(center.z) * 1.5, radius < 0.25 {
            newYaw = center.x > 0 ? .pi / 3 : -.pi / 3
        } else if center.z < -0.06, radius < 0.25 {
            newYaw = .pi
        } else if abs(remainder(yaw, 2 * .pi)) > .pi / 2 && center.z > 0.02 {
            newYaw = 0
        }
        animateCamera(target: center, distance: min(max(fit, 0.16), 3.3), yaw: newYaw, pitch: 0.08)
    }

    func animateCamera(target newTarget: SIMD3<Float>, distance newDistance: Float, yaw newYaw: Float, pitch newPitch: Float) {
        tween?.cancel()
        let start = (target, distance, yaw, pitch)
        // Take the short way round.
        var endYaw = newYaw
        while endYaw - start.2 > .pi { endYaw -= 2 * .pi }
        while start.2 - endYaw > .pi { endYaw += 2 * .pi }
        tween = Task { [weak self] in
            let steps = 40
            for step in 1...steps {
                guard let self, !Task.isCancelled else { return }
                let t = Float(step) / Float(steps)
                let e = t < 0.5 ? 4 * t * t * t : 1 - pow(-2 * t + 2, 3) / 2
                self.target = start.0 + (newTarget - start.0) * e
                self.distance = start.1 + (newDistance - start.1) * e
                self.yaw = start.2 + (endYaw - start.2) * e
                self.pitch = start.3 + (newPitch - start.3) * e
                self.applyCamera()
                try? await Task.sleep(for: .milliseconds(11))
            }
            self?.cameraDidSettle()
        }
    }

    func beginCameraInteraction() {
        tween?.cancel()
        if !isCameraMoving { isCameraMoving = true }
    }

    func applyCamera() {
        let offset = SIMD3<Float>(
            sin(yaw) * cos(pitch),
            sin(pitch),
            cos(yaw) * cos(pitch)
        ) * distance
        camera.look(at: target, from: target + offset, relativeTo: nil)
    }

    /// Projects a model-space point into view coordinates (nil if behind the camera).
    func project(_ p: SIMD3<Float>, in size: CGSize) -> CGPoint? {
        let inverse = camera.transformMatrix(relativeTo: nil).inverse
        let c = inverse * SIMD4(p, 1)
        guard c.z < -0.01 else { return nil }
        let t = tan(fieldOfView * .pi / 360)
        let aspect = Float(size.width / size.height)
        let nx = c.x / (-c.z * t * aspect)
        let ny = c.y / (-c.z * t)
        return CGPoint(x: CGFloat((nx + 1) / 2) * size.width, y: CGFloat((1 - ny) / 2) * size.height)
    }
}
