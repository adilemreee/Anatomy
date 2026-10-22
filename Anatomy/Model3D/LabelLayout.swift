//
//  LabelLayout.swift
//  Anatomy
//
//  Callout labels laid out like the plates of a printed atlas: two columns
//  beside the model, each label level with its point where it can be, no
//  overlaps, and leader lines that do not cross within a column.
//

import CoreGraphics
import UIKit

nonisolated enum LabelLayout {
    /// One label to place, in priority order.
    struct Item {
        let anchor: CGPoint
        let size: CGSize
    }

    /// The horizontal extent of the model on screen, row by row.
    struct Silhouette {
        let originY: CGFloat
        let bin: CGFloat
        var minX: [CGFloat]
        var maxX: [CGFloat]

        /// Rows `points` cover, `bin` points tall.
        init(points: [CGPoint], in bounds: CGRect, bin: CGFloat = 6) {
            originY = bounds.minY
            self.bin = bin
            let rows = max(Int((bounds.height / bin).rounded(.up)), 1)
            minX = Array(repeating: .infinity, count: rows)
            maxX = Array(repeating: -.infinity, count: rows)
            for p in points where p.y >= bounds.minY && p.y < bounds.maxY {
                let row = min(Int((p.y - bounds.minY) / bin), rows - 1)
                minX[row] = min(minX[row], p.x)
                maxX[row] = max(maxX[row], p.x)
            }
        }

        /// The model's extent between two heights; nil where it is absent.
        func span(from y0: CGFloat, to y1: CGFloat) -> (min: CGFloat, max: CGFloat)? {
            let a = max(Int((y0 - originY) / bin), 0), b = min(Int((y1 - originY) / bin), minX.count - 1)
            guard a <= b else { return nil }
            var lo = CGFloat.infinity, hi = -CGFloat.infinity
            for row in a...b {
                lo = min(lo, minX[row])
                hi = max(hi, maxX[row])
            }
            return lo.isFinite ? (lo, hi) : nil
        }

        /// The model's overall extent.
        var extent: (min: CGFloat, max: CGFloat)? {
            let lo = minX.min() ?? .infinity, hi = maxX.max() ?? -.infinity
            return lo.isFinite ? (lo, hi) : nil
        }
    }

    /// Free width on each side of the model inside `safe`.
    static func room(_ silhouette: Silhouette, in safe: CGRect, gap: CGFloat) -> (left: CGFloat, right: CGFloat) {
        guard let extent = silhouette.span(from: safe.minY, to: safe.maxY) else { return (safe.width / 2, safe.width / 2) }
        return (max(extent.min - gap - safe.minX, 0), max(safe.maxX - extent.max - gap, 0))
    }

    /// Boxes for `items` (nil for those left out for lack of room). Earlier
    /// items win when a column is full. Labels go on the side of the model
    /// their point is on, hug the model's outline where there is room and
    /// sit at the edge of `safe` where there is not.
    static func place(_ items: [Item], silhouette: Silhouette, in safe: CGRect, avoiding: [CGRect] = [],
                      gap: CGFloat = 12, spacing: CGFloat = 6) -> [CGRect?] {
        guard !items.isEmpty, safe.height > 40 else { return items.map { _ in nil } }
        let extent = silhouette.span(from: safe.minY, to: safe.maxY)
        let middle = extent.map { ($0.min + $0.max) / 2 } ?? safe.midX

        // Fill the two columns in priority order.
        var columns: [[Int]] = [[], []]
        var used: [CGFloat] = [0, 0]
        for (i, item) in items.enumerated() {
            let preferred = item.anchor.x < middle ? 0 : 1
            for side in [preferred, 1 - preferred] {
                let need = item.size.height + (columns[side].isEmpty ? 0 : spacing)
                // The other side only for points near the middle, so lines
                // do not cross the whole model.
                if side != preferred, abs(item.anchor.x - middle) > safe.width * 0.12 { break }
                if used[side] + need <= safe.height {
                    columns[side].append(i)
                    used[side] += need
                    break
                }
            }
        }

        // A label pushed far from its point gets a long slanting line that
        // crosses others: the least important of those makes room instead.
        let maxShift = max(safe.height * 0.15, 70)
        var out = [CGRect?](repeating: nil, count: items.count)
        for side in 0..<2 {
            var column = columns[side].sorted { items[$0].anchor.y < items[$1].anchor.y }
            var mids = stack(column, items, in: safe, spacing: spacing)
            while let worst = column.indices.filter({ abs(mids[$0] - items[column[$0]].anchor.y) > maxShift })
                .max(by: { column[$0] < column[$1] }) {
                column.remove(at: worst)
                mids = stack(column, items, in: safe, spacing: spacing)
            }
            for (k, i) in column.enumerated() {
                let size = items[i].size
                let top = mids[k] - size.height / 2
                // Beside the model's outline at this height, else at the edge.
                let span = silhouette.span(from: top - spacing, to: top + size.height + spacing)
                var x: CGFloat
                if side == 0 {
                    let edge = min(span?.min ?? items[i].anchor.x, items[i].anchor.x) - gap
                    x = max(safe.minX, edge - size.width)
                } else {
                    let edge = max(span?.max ?? items[i].anchor.x, items[i].anchor.x) + gap
                    x = min(safe.maxX - size.width, edge)
                }
                var box = CGRect(x: x, y: top, width: size.width, height: size.height)
                // Step out of the way of buttons over the view, still on
                // the point's own side.
                if let blocker = avoiding.first(where: { $0.intersects(box) }) {
                    box.origin.x = side == 0 ? blocker.maxX + 4 : blocker.minX - size.width - 4
                    let fits = side == 0 ? box.maxX <= items[i].anchor.x - 6 : box.minX >= items[i].anchor.x + 6
                    guard fits, safe.contains(box), !avoiding.contains(where: { $0.intersects(box) }) else { continue }
                }
                out[i] = box
            }
        }
        return out
    }

    /// Boxes for `items` right beside their own points, for when the model
    /// fills the screen and there is no room next to it: on the outer side
    /// of each point, else a little above or below, else on the inner side.
    /// Boxes never overlap each other, `avoiding` or another item's point;
    /// earlier items win.
    static func placeNear(_ items: [Item], middle: CGFloat, in safe: CGRect, avoiding: [CGRect] = [],
                          gap: CGFloat = 9) -> [CGRect?] {
        var out = [CGRect?](repeating: nil, count: items.count)
        var taken: [CGRect] = []
        for (i, item) in items.enumerated() {
            let p = item.anchor, w = item.size.width, h = item.size.height
            let outer: CGFloat = p.x < middle ? -1 : 1
            let steps: [CGFloat] = [0, -1, 1, -2, 2]
            var candidates: [CGRect] = []
            for direction in [outer, -outer] {
                let x = direction < 0 ? p.x - gap - w : p.x + gap
                for s in steps {
                    candidates.append(CGRect(x: x, y: p.y - h / 2 + s * (h + 5), width: w, height: h))
                }
            }
            let others = items.indices.filter { $0 != i }.map { items[$0].anchor }
            for box in candidates where safe.contains(box) {
                let padded = box.insetBy(dx: -3, dy: -3)
                guard !taken.contains(where: { $0.intersects(padded) }),
                      !avoiding.contains(where: { $0.intersects(box) }),
                      !others.contains(where: { padded.contains($0) }) else { continue }
                out[i] = box
                taken.append(box)
                break
            }
        }
        return out
    }

    /// Vertical centres for a column sorted top to bottom: as close to each
    /// point's height as the labels above and below allow.
    private static func stack(_ column: [Int], _ items: [Item], in safe: CGRect, spacing: CGFloat) -> [CGFloat] {
        var mids = column.map { min(max(items[$0].anchor.y, safe.minY + items[$0].size.height / 2),
                                     safe.maxY - items[$0].size.height / 2) }
        guard column.count > 1 else { return mids }
        for k in 1..<column.count {
            let least = mids[k - 1] + (items[column[k - 1]].size.height + items[column[k]].size.height) / 2 + spacing
            mids[k] = max(mids[k], least)
        }
        let overflow = mids[column.count - 1] + items[column[column.count - 1]].size.height / 2 - safe.maxY
        if overflow > 0 { mids[column.count - 1] -= overflow }
        for k in stride(from: column.count - 2, through: 0, by: -1) {
            let most = mids[k + 1] - (items[column[k + 1]].size.height + items[column[k]].size.height) / 2 - spacing
            mids[k] = min(mids[k], most)
        }
        return mids
    }

    // MARK: Text

    /// Size of a label box for a title (up to `titleLines` lines) and an
    /// optional one-line subtitle, no wider than `maxWidth`.
    static func size(title: String, subtitle: String?, maxWidth: CGFloat, titleLines: Int = 2,
                     titleFont: UIFont, subtitleFont: UIFont, padding: CGSize) -> CGSize {
        let inner = max(maxWidth - padding.width * 2, 20)
        let titleRect = (title as NSString).boundingRect(with: CGSize(width: inner, height: .greatestFiniteMagnitude),
                                                         options: [.usesLineFragmentOrigin], attributes: [.font: titleFont], context: nil)
        let oneLine = (title as NSString).size(withAttributes: [.font: titleFont]).width
        var width = min(oneLine, inner)
        var height = min(ceil(titleRect.height), ceil(titleFont.lineHeight) * CGFloat(titleLines))
        if let subtitle {
            width = max(width, min((subtitle as NSString).size(withAttributes: [.font: subtitleFont]).width, inner))
            height += ceil(subtitleFont.lineHeight) + 1
        }
        return CGSize(width: ceil(width) + padding.width * 2, height: height + padding.height * 2)
    }

    /// The Latin subtitle unless it only repeats the title
    /// ("Condylus medialis femoris" under "Condylus medialis ossis femoris").
    static func subtitle(_ latin: String?, under title: String) -> String? {
        guard let latin, !latin.isEmpty else { return nil }
        let a = words(title), b = words(latin)
        if a == b || title.localizedCaseInsensitiveContains(latin) || latin.localizedCaseInsensitiveContains(title) { return nil }
        if a.count >= 2, b.count >= 2, a.prefix(2) == b.prefix(2) { return nil }
        return latin
    }

    private static func words(_ s: String) -> [String] {
        s.lowercased().split { !$0.isLetter }.map(String.init).filter { !["os", "ossis", "musculi", "musculus", "m", "mm"].contains($0) }
    }
}
