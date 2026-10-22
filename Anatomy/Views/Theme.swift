//
//  Theme.swift
//  Anatomy
//
//  The app's dark, premium look: colour tokens, type styles and the few
//  building blocks every screen is made of.
//

import SwiftUI

enum Theme {
    // MARK: Colours

    /// Deepest background, behind the 3D model and every screen.
    static let background = Color(hex: "0A0C11")
    /// Grouped surfaces (lists, sheets).
    static let surface = Color(hex: "11141B")
    /// Cards on top of a surface.
    static let card = Color(hex: "181C25")
    /// Pressed / elevated cards and inputs.
    static let elevated = Color(hex: "212633")
    static let stroke = Color.white.opacity(0.08)
    static let strokeStrong = Color.white.opacity(0.14)

    static let textPrimary = Color(hex: "F2F4F8")
    static let textSecondary = Color(hex: "A2AABA")
    static let textTertiary = Color(hex: "6A7283")

    /// Interactive accent (buttons, selection, links).
    static let accent = Color(hex: "3BB4FF")
    /// Premium highlights.
    static let gold = Color(hex: "E9B95C")
    static let success = Color(hex: "3DD68C")
    static let danger = Color(hex: "FF5D5D")
    static let clinical = Color(hex: "FF6FA5")

    static let goldGradient = LinearGradient(colors: [Color(hex: "F5D08A"), Color(hex: "D79A36")], startPoint: .topLeading, endPoint: .bottomTrailing)
    static let accentGradient = LinearGradient(colors: [Color(hex: "54C6FF"), Color(hex: "2F7BFF")], startPoint: .topLeading, endPoint: .bottomTrailing)

    // MARK: Type

    /// Latin terms are set in the serif italic of a printed atlas.
    static func latin(_ style: Font.TextStyle = .subheadline) -> Font {
        .system(style, design: .serif).italic()
    }

    /// Font of the name under a structure's title: the Latin face when the
    /// Latin name is the second one, plain text when it leads.
    static func secondName(_ style: Font.TextStyle = .subheadline, latinFirst: Bool) -> Font {
        latinFirst ? .system(style) : latin(style)
    }

    static func display(_ style: Font.TextStyle = .largeTitle) -> Font {
        .system(style, design: .default).weight(.bold)
    }

    /// Small capitals above sections.
    static let eyebrow = Font.system(.caption2, design: .default).weight(.bold)
}

// MARK: - Building blocks

/// A rounded card on the dark surface.
struct Card<Content: View>: View {
    var padding: CGFloat = 16
    var radius: CGFloat = 20
    @ViewBuilder var content: Content

    var body: some View {
        content
            .padding(padding)
            .frame(maxWidth: .infinity, alignment: .leading)
            .background(Theme.card, in: .rect(cornerRadius: radius))
            .overlay { RoundedRectangle(cornerRadius: radius).strokeBorder(Theme.stroke) }
    }
}

/// Caps label used above sections ("TEMEL BİLGİLER").
struct Eyebrow: View {
    let text: String
    var color: Color = Theme.textTertiary

    var body: some View {
        Text(text.uppercased(with: .current))
            .font(Theme.eyebrow)
            .tracking(1.1)
            .foregroundStyle(color)
    }
}

/// Section header with an optional trailing action.
struct SectionHeader: View {
    let title: String
    var subtitle: String?
    var action: (title: String, run: () -> Void)?

    var body: some View {
        HStack(alignment: .firstTextBaseline) {
            VStack(alignment: .leading, spacing: 2) {
                Text(title)
                    .font(.title3.weight(.bold))
                    .foregroundStyle(Theme.textPrimary)
                if let subtitle {
                    Text(subtitle)
                        .font(.footnote)
                        .foregroundStyle(Theme.textSecondary)
                }
            }
            Spacer()
            if let action {
                Button(action.title, action: action.run)
                    .font(.subheadline.weight(.semibold))
                    .foregroundStyle(Theme.accent)
            }
        }
    }
}

/// Full-width primary button.
struct PrimaryButtonStyle: ButtonStyle {
    var gradient: LinearGradient = Theme.accentGradient
    var foreground: Color = .white

    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .font(.headline)
            .foregroundStyle(foreground)
            .frame(maxWidth: .infinity)
            .padding(.vertical, 15)
            .background(gradient, in: .rect(cornerRadius: 16))
            .opacity(configuration.isPressed ? 0.85 : 1)
            .scaleEffect(configuration.isPressed ? 0.985 : 1)
            .animation(.snappy(duration: 0.15), value: configuration.isPressed)
    }
}

/// Secondary button on a card background.
struct SecondaryButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .font(.subheadline.weight(.semibold))
            .foregroundStyle(Theme.textPrimary)
            .frame(maxWidth: .infinity)
            .padding(.vertical, 13)
            .background(Theme.elevated, in: .rect(cornerRadius: 14))
            .overlay { RoundedRectangle(cornerRadius: 14).strokeBorder(Theme.stroke) }
            .opacity(configuration.isPressed ? 0.8 : 1)
    }
}

/// Plain press feedback for custom tappable cards.
struct PressableStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .scaleEffect(configuration.isPressed ? 0.98 : 1)
            .opacity(configuration.isPressed ? 0.9 : 1)
            .animation(.snappy(duration: 0.15), value: configuration.isPressed)
    }
}

/// Small gold "PREMIUM" pill.
struct PremiumBadge: View {
    var compact = false

    var body: some View {
        HStack(spacing: 3) {
            Image(systemName: "crown.fill")
            if !compact { Text("PREMIUM") }
        }
        .font(.system(size: compact ? 9 : 10, weight: .heavy))
        .tracking(0.6)
        .foregroundStyle(Color(hex: "2A1D05"))
        .padding(.horizontal, compact ? 5 : 7)
        .padding(.vertical, 3)
        .background(Theme.goldGradient, in: .capsule)
    }
}

/// A lock glyph shown on content the free tier cannot open.
struct LockBadge: View {
    var body: some View {
        Image(systemName: "lock.fill")
            .font(.system(size: 10, weight: .bold))
            .foregroundStyle(Color(hex: "2A1D05"))
            .frame(width: 20, height: 20)
            .background(Theme.goldGradient, in: .circle)
    }
}

extension View {
    /// The app-wide dark background.
    func themedBackground() -> some View {
        background(Theme.background.ignoresSafeArea())
    }
}
