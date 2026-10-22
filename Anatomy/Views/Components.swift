//
//  Components.swift
//  Anatomy
//

import SwiftUI

/// A round floating control used on top of the 3D view.
struct GlassIconButton: View {
    let systemImage: String
    var isOn = false
    let label: String
    let action: () -> Void

    var body: some View {
        Button(action: action) {
            Image(systemName: systemImage)
                .font(.system(size: 17, weight: .semibold))
                .frame(width: 44, height: 44)
                .foregroundStyle(isOn ? Color.white : Color.primary)
        }
        .buttonStyle(.plain)
        .glassEffect(isOn ? .regular.tint(.accentColor).interactive() : .regular.interactive(), in: .circle)
        .accessibilityLabel(label)
    }
}

/// Small capsule label, e.g. a system name.
struct TagView: View {
    let text: String
    var color: Color = .secondary
    var systemImage: String?

    var body: some View {
        HStack(spacing: 4) {
            if let systemImage {
                Image(systemName: systemImage).font(.caption2.weight(.semibold))
            }
            Text(text).font(.caption.weight(.semibold))
        }
        .padding(.horizontal, 8)
        .padding(.vertical, 4)
        .foregroundStyle(color)
        .background(color.opacity(0.14), in: .capsule)
    }
}

/// Rounded inset block used for content sections.
struct ContentCard<Content: View>: View {
    var title: String?
    var systemImage: String?
    var tint: Color = .accentColor
    @ViewBuilder var content: Content

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            if let title {
                Label {
                    Text(title).font(.headline)
                } icon: {
                    if let systemImage {
                        Image(systemName: systemImage).foregroundStyle(tint)
                    }
                }
            }
            content
        }
        .frame(maxWidth: .infinity, alignment: .leading)
        .padding(16)
        .background(Theme.card, in: .rect(cornerRadius: 18))
        .overlay { RoundedRectangle(cornerRadius: 18).strokeBorder(Theme.stroke) }
    }
}

/// The label/value table for origin, insertion, innervation …
struct FactTable: View {
    let facts: [AtlasEntry.Fact]
    var tint: Color = .accentColor

    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            ForEach(Array(facts.enumerated()), id: \.offset) { index, fact in
                VStack(alignment: .leading, spacing: 3) {
                    Text(fact.title.uppercased(with: .current))
                        .font(.caption2.weight(.bold))
                        .tracking(0.6)
                        .foregroundStyle(tint)
                    Text(fact.value)
                        .font(.subheadline)
                        .foregroundStyle(Theme.textPrimary)
                        .fixedSize(horizontal: false, vertical: true)
                }
                .frame(maxWidth: .infinity, alignment: .leading)
                .padding(.vertical, 10)
                if index < facts.count - 1 {
                    Divider().overlay(Theme.stroke)
                }
            }
        }
    }
}

/// Round icon in a system's colour.
struct SystemBadge: View {
    let icon: String
    let color: Color
    var size: CGFloat = 40

    var body: some View {
        Image(systemName: icon)
            .font(.system(size: size * 0.45, weight: .semibold))
            .foregroundStyle(.white)
            .frame(width: size, height: size)
            .background(
                LinearGradient(colors: [color, color.opacity(0.72)], startPoint: .topLeading, endPoint: .bottomTrailing),
                in: .rect(cornerRadius: size * 0.3)
            )
    }
}

/// A thin progress ring.
struct ProgressRing: View {
    let value: Double
    var color: Color = .accentColor
    var lineWidth: CGFloat = 5

    var body: some View {
        ZStack {
            Circle().stroke(color.opacity(0.18), lineWidth: lineWidth)
            Circle()
                .trim(from: 0, to: max(0.001, min(1, value)))
                .stroke(color, style: StrokeStyle(lineWidth: lineWidth, lineCap: .round))
                .rotationEffect(.degrees(-90))
        }
    }
}

extension View {
    /// Applies the app-wide grouped background.
    func atlasBackground() -> some View {
        background(Theme.background.ignoresSafeArea())
            .scrollContentBackground(.hidden)
    }

    /// Caps the content's width on wide windows (iPad, the inner display of
    /// iPhone Duo) and centres it, so lines and rows stay easy to read;
    /// narrow windows are unaffected.
    func readableWidth(_ maxWidth: CGFloat = 720) -> some View {
        frame(maxWidth: maxWidth)
            .frame(maxWidth: .infinity)
    }
}

/// Widths for `readableWidth`: reading pages and the dashboard-like tabs.
enum ReadableWidth {
    static let text: CGFloat = 720
    static let dashboard: CGFloat = 1000
}
