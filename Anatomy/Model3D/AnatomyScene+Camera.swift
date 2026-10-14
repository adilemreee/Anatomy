//
//  AnatomyScene+Camera.swift
//  Anatomy
//

import QuartzCore
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
    /// Centre and camera distance that fit `refs` on screen.
    func framing(_ refs: [PartRef], margin: Float = 1.15) -> (SIMD3<Float>?, Float) {
        var lo = SIMD3<Float>(repeating: .greatestFiniteMagnitude)
        var hi = -lo
        for ref in refs {
            guard let info = info(ref) else { continue }
            let b = info.bounds
            lo = simd_min(lo, SIMD3(b[0], b[1], b[2]))
            hi = simd_max(hi, SIMD3(b[3], b[4], b[5]))
        }
        guard lo.x <= hi.x else { return (nil, distance) }
        let radius = max(simd_length(hi - lo) / 2, 0.03)
        let halfV = fieldOfView * .pi / 360
        let halfH = atan(tan(halfV) * min(viewAspect, 1))
        let fit = radius / sin(min(halfV, halfH)) * margin
        return ((lo + hi) / 2, min(max(fit, 0.16), 3.3))
    }

    /// A gentle move towards a tapped part: it comes towards the middle,
    /// a little above it (the selection card covers the bottom), and the
    /// camera moves closer, at most halving the distance per tap and never
    /// zooming out.
    func focus(on refs: [PartRef]) {
        let (center, fit) = framing(refs, margin: 2.4)
        guard let center else { return }
        let newDistance = max(min(distance, max(fit, distance * 0.5)), 0.3)
        let halfHeight = newDistance * tan(fieldOfView * .pi / 360)
        let m = camera.transformMatrix(relativeTo: nil)
        let up = simd_normalize(SIMD3(m.columns.1.x, m.columns.1.y, m.columns.1.z))
        let newTarget = center - up * halfHeight * 0.2
        guard simd_distance(newTarget, target) > 0.01 || newDistance < distance * 0.97 else { return }
        animateCamera(target: newTarget, distance: newDistance, yaw: yaw, pitch: pitch)
    }

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
        if !isCameraMoving { isCameraMoving = true }
        tween = CameraTween(duration: 0.55) { [weak self] e in
            guard let self else { return }
            self.target = start.0 + (newTarget - start.0) * e
            self.distance = start.1 + (newDistance - start.1) * e
            self.yaw = start.2 + (endYaw - start.2) * e
            self.pitch = start.3 + (newPitch - start.3) * e
            self.applyCamera()
        } completion: { [weak self] in
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
        updateDetail()
    }

    // MARK: Level of detail

    /// Picks each part's level of detail from how big its simplification
    /// error would be on screen: at most a pixel at rest, a little more while
    /// the camera moves. Throttled while moving; forced when it settles.
    func updateDetail(force: Bool = false) {
        let now = CACurrentMediaTime()
        guard force || now - lastDetailUpdate > 0.12 else { return }
        lastDetailUpdate = now
        let eye = camera.position(relativeTo: nil)
        let view = camera.transformMatrix(relativeTo: nil).inverse
        let tanV = tan(fieldOfView * .pi / 360)
        // A little wider than the screen so parts swinging into view while
        // the camera moves are already refined.
        let tanH = tanV * max(viewAspect, 0.2) * 1.15
        let tanVM = tanV * 1.15
        let slackH = (1 + tanH * tanH).squareRoot(), slackV = (1 + tanVM * tanVM).squareRoot()
        let pixelsPerMetreAtOne = viewPixelHeight / (2 * tanV)
        let tolerance: Float = isCameraMoving ? 3.5 : 1.6
        for (id, system) in systems where enabledLayers.contains(id) {
            let pack = system.pack
            guard pack.levelCount > 1 else { continue }
            var levels = partLevels[id] ?? Array(repeating: 0, count: pack.parts.count)
            var changed = false
            let coarsest = pack.levelCount - 1
            for i in pack.parts.indices {
                let r = system.radii[i]
                // Off screen: keep the cheapest level.
                let c = view * SIMD4(system.centers[i], 1)
                let depth = -c.z
                let offScreen = depth < -r || abs(c.x) > depth * tanH + r * slackH || abs(c.y) > depth * tanVM + r * slackV
                var level = 0
                if offScreen {
                    level = coarsest
                } else {
                    let scale = pixelsPerMetreAtOne / max(simd_distance(system.centers[i], eye) - r, 0.02)
                    for l in Swift.stride(from: coarsest, through: 1, by: -1) where pack.error(of: i, level: l) * scale <= tolerance {
                        level = l
                        break
                    }
                }
                if levels[i] != UInt8(level) {
                    levels[i] = UInt8(level)
                    changed = true
                }
            }
            if changed {
                partLevels[id] = levels
                refresh(id, visibilityChanged: false)
            }
        }
        if Self.logsDetail { print("LOD", drawnTriangleSummary()) }
    }

    /// -AtlasDebugLOD YES prints the drawn triangle count after every update.
    private static let logsDetail = UserDefaults.standard.bool(forKey: "AtlasDebugLOD")

    /// Triangles currently drawn per enabled system, for debugging.
    func drawnTriangleSummary() -> String {
        var total = 0
        var parts: [String] = []
        for (id, system) in systems.sorted(by: { $0.key < $1.key }) where enabledLayers.contains(id) {
            let count = system.mesh.parts.reduce(0) { $0 + $1.indexCount / 3 }
            total += count
            parts.append("\(id) \(count)")
        }
        return "\(total) [\(parts.joined(separator: ", "))]"
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
