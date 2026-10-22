//
//  EntryDetailView.swift
//  Anatomy
//

import SwiftUI

/// Full page for one written atlas entry.
struct EntryDetailView: View {
    @Environment(AppModel.self) private var app
    let entry: AtlasEntry

    var body: some View {
        ScrollView {
            EntryContent(entry: entry)
                .padding(.horizontal, 16)
                .padding(.bottom, 32)
                .readableWidth()
        }
        .themedBackground()
        .navigationTitle(app.store.title(entry))
        .navigationBarTitleDisplayMode(.inline)
        .toolbar {
            ToolbarItem(placement: .topBarTrailing) {
                FavoriteButton(id: entry.id)
            }
        }
        .onAppear { app.study.markViewed(entry.id) }
    }
}

struct FavoriteButton: View {
    @Environment(AppModel.self) private var app
    let id: String

    var body: some View {
        let on = app.study.isFavorite(id)
        Button {
            app.study.toggleFavorite(id)
        } label: {
            Image(systemName: on ? "star.fill" : "star")
                .foregroundStyle(on ? Theme.gold : Theme.textPrimary)
        }
        .sensoryFeedback(.impact(weight: .light), trigger: on)
        .accessibilityLabel(on ? String(localized: "Favorilerden çıkar") : String(localized: "Favorilere ekle"))
    }
}

/// The body of an entry page; also used inside the 3D part sheet.
struct EntryContent: View {
    @Environment(AppModel.self) private var app
    let entry: AtlasEntry
    var showsModelButton = true

    var body: some View {
        let system = app.store.system(entry.systemID)
        let tint = system?.tint ?? Theme.accent
        let locked = !app.isFree(entry)
        VStack(alignment: .leading, spacing: 16) {
            header(system: system, tint: tint)

            if showsModelButton, app.hasModel(entry), !locked {
                HStack(spacing: 10) {
                    Button {
                        app.inspect(entry)
                    } label: {
                        Label("3D İncele", systemImage: "cube.transparent")
                    }
                    .buttonStyle(PrimaryButtonStyle())
                    Button {
                        app.showInAtlas(entry)
                    } label: {
                        Label("Atlasta göster", systemImage: "figure.arms.open")
                    }
                    .buttonStyle(SecondaryButtonStyle())
                }
            }

            Card {
                Text(entry.summary)
                    .font(.body)
                    .foregroundStyle(Theme.textPrimary)
                    .fixedSize(horizontal: false, vertical: true)
            }

            if locked {
                LockedEntryCard(entry: entry, system: system)
            } else {
                details(tint: tint)
            }
        }
    }

    @ViewBuilder
    private func details(tint: Color) -> some View {
        if !entry.facts.isEmpty {
            InfoCard(title: String(localized: "Temel bilgiler"), icon: "list.bullet.rectangle", tint: tint) {
                FactTable(facts: entry.facts, tint: tint)
            }
        }

        ForEach(entry.sections, id: \.title) { section in
            InfoCard(title: section.title, icon: "text.alignleft", tint: tint) {
                Text(section.body)
                    .font(.subheadline)
                    .foregroundStyle(Theme.textPrimary)
                    .fixedSize(horizontal: false, vertical: true)
            }
        }

        if !entry.tus.isEmpty {
            InfoCard(title: String(localized: "TUS notları"), icon: "target", tint: Theme.gold) {
                BulletList(items: entry.tus, color: Theme.gold)
            }
        }

        if !entry.clinical.isEmpty {
            InfoCard(title: String(localized: "Klinik bilgi"), icon: "stethoscope", tint: Theme.clinical) {
                BulletList(items: entry.clinical, color: Theme.clinical)
            }
        }

        let related = app.store.related(of: entry)
        if !related.isEmpty {
            InfoCard(title: String(localized: "İlişkili yapılar"), icon: "point.3.connected.trianglepath.dotted", tint: tint) {
                FlowLayout(spacing: 8) {
                    ForEach(related) { other in
                        NavigationLink(value: other) {
                            Text(app.store.title(other))
                                .font(.subheadline.weight(.medium))
                                .padding(.horizontal, 12)
                                .padding(.vertical, 7)
                                .background(tint.opacity(0.14), in: .capsule)
                                .foregroundStyle(tint)
                        }
                        .buttonStyle(.plain)
                    }
                }
            }
        }

        // Not offered from inside a running test or the specimen viewer.
        if app.quiz == nil, app.specimen == nil {
            Button {
                app.startQuiz(QuizConfig(title: app.store.title(entry), source: .bank, systems: [entry.systemID], count: 8,
                                         preferNew: false, entries: [entry.id]))
            } label: {
                HStack(spacing: 12) {
                    Image(systemName: "checklist")
                        .font(.title3)
                        .foregroundStyle(Theme.accent)
                        .frame(width: 40, height: 40)
                        .background(Theme.accent.opacity(0.14), in: .rect(cornerRadius: 12))
                    VStack(alignment: .leading, spacing: 2) {
                        Text("Bu konudan soru çöz")
                            .font(.headline)
                            .foregroundStyle(Theme.textPrimary)
                        Text(questionCountText)
                            .font(.caption)
                            .foregroundStyle(Theme.textSecondary)
                    }
                    Spacer()
                    Image(systemName: "chevron.right")
                        .font(.footnote.weight(.semibold))
                        .foregroundStyle(Theme.textTertiary)
                }
                .padding(14)
                .background(Theme.card, in: .rect(cornerRadius: 20))
                .overlay { RoundedRectangle(cornerRadius: 20).strokeBorder(Theme.stroke) }
            }
            .buttonStyle(PressableStyle())
        }

        if let reference = referenceText {
            ReferenceTextCard(text: reference)
        }
    }

    private var questionCountText: String {
        let written = app.bank.questions.filter { $0.entries.contains(entry.id) }.count
        return written > 0 ? String(localized: "\(written) soru bankası sorusu ve atlas soruları") : String(localized: "Bu yapı ve ilişkili yapılar hakkında sorular")
    }

    private var referenceText: String? {
        for name in entry.models + [entry.en] {
            if let def = app.store.term(name)?.def { return def }
        }
        return nil
    }

    private func header(system: BodySystem?, tint: Color) -> some View {
        VStack(alignment: .leading, spacing: 8) {
            HStack(spacing: 6) {
                if let system {
                    TagView(text: system.tr, color: tint, systemImage: system.icon)
                }
                TagView(text: entry.region.title, color: Theme.textSecondary, systemImage: entry.region.icon)
            }
            Text(app.store.title(entry))
                .font(.system(.largeTitle, weight: .bold))
                .foregroundStyle(Theme.textPrimary)
                .fixedSize(horizontal: false, vertical: true)
            if !app.store.subtitle(entry).isEmpty {
                Text(app.store.subtitle(entry))
                    .font(Theme.secondName(.title3, latinFirst: app.store.latinFirst))
                    .foregroundStyle(tint)
            }
            if entry.en != entry.la, entry.en != entry.tr {
                Text(entry.en)
                    .font(.subheadline)
                    .foregroundStyle(Theme.textTertiary)
            }
        }
        .padding(.top, 8)
    }
}

/// A content card with an icon title.
struct InfoCard<Content: View>: View {
    let title: String
    let icon: String
    var tint: Color = Theme.accent
    @ViewBuilder var content: Content

    var body: some View {
        Card {
            VStack(alignment: .leading, spacing: 12) {
                Label {
                    Text(title).font(.headline).foregroundStyle(Theme.textPrimary)
                } icon: {
                    Image(systemName: icon).foregroundStyle(tint)
                }
                content
            }
        }
    }
}

struct BulletList: View {
    let items: [String]
    var color: Color = Theme.accent

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            ForEach(items, id: \.self) { item in
                HStack(alignment: .firstTextBaseline, spacing: 10) {
                    Circle().fill(color).frame(width: 6, height: 6)
                    Text(item)
                        .font(.subheadline)
                        .foregroundStyle(Theme.textPrimary)
                        .fixedSize(horizontal: false, vertical: true)
                }
            }
        }
    }
}

/// What a free user sees instead of the details.
private struct LockedEntryCard: View {
    @Environment(AppModel.self) private var app
    let entry: AtlasEntry
    let system: BodySystem?

    var body: some View {
        VStack(alignment: .leading, spacing: 14) {
            VStack(alignment: .leading, spacing: 8) {
                ForEach(entry.facts.prefix(3), id: \.label) { fact in
                    VStack(alignment: .leading, spacing: 3) {
                        Text(fact.title.uppercased(with: .current))
                            .font(Theme.eyebrow)
                            .foregroundStyle(Theme.textTertiary)
                        Text(fact.value)
                            .font(.subheadline)
                            .foregroundStyle(Theme.textPrimary)
                            .lineLimit(2)
                    }
                }
            }
            .blur(radius: 6)
            .allowsHitTesting(false)
            .accessibilityHidden(true)

            VStack(alignment: .leading, spacing: 6) {
                HStack(spacing: 8) {
                    LockBadge()
                    Text("Bu maddenin tamamı Premium'da")
                        .font(.headline)
                        .foregroundStyle(Theme.textPrimary)
                }
                Text("\(entry.facts.count) temel bilgi, \(entry.sections.count + entry.clinical.count + entry.tus.count) klinik ve sınav notu, 3D inceleme ve bu konudaki sorular.")
                    .font(.footnote)
                    .foregroundStyle(Theme.textSecondary)
            }
            Button {
                app.requirePremium(.system(system?.tr ?? entry.tr))
            } label: {
                Label("Premium ile aç", systemImage: "lock.open.fill")
            }
            .buttonStyle(PrimaryButtonStyle(gradient: Theme.goldGradient, foreground: Color(hex: "2A1D05")))
        }
        .padding(16)
        .background(Theme.card, in: .rect(cornerRadius: 20))
        .overlay { RoundedRectangle(cornerRadius: 20).strokeBorder(Theme.gold.opacity(0.35)) }
    }
}

/// English reference text from Z-Anatomy (Wikipedia derived), collapsed by default.
struct ReferenceTextCard: View {
    let text: String
    @State private var expanded = false

    var body: some View {
        Card {
            DisclosureGroup(isExpanded: $expanded) {
                VStack(alignment: .leading, spacing: 10) {
                    ForEach(Array(text.components(separatedBy: "\n\n").enumerated()), id: \.offset) { _, paragraph in
                        if paragraph.hasPrefix("## ") {
                            Text(paragraph.dropFirst(3))
                                .font(.subheadline.weight(.semibold))
                                .foregroundStyle(Theme.textPrimary)
                                .padding(.top, 4)
                        } else {
                            Text(paragraph)
                                .font(.subheadline)
                                .foregroundStyle(Theme.textSecondary)
                                .fixedSize(horizontal: false, vertical: true)
                        }
                    }
                    Text("Kaynak: Z-Anatomy (Wikipedia tabanlı), CC BY-SA 4.0")
                        .font(.caption2)
                        .foregroundStyle(Theme.textTertiary)
                }
                .padding(.top, 8)
            } label: {
                Label("İngilizce kaynak metin", systemImage: "book.closed")
                    .font(.headline)
                    .foregroundStyle(Theme.textPrimary)
            }
            .tint(Theme.textSecondary)
        }
    }
}

/// Wraps its children onto multiple lines.
struct FlowLayout: Layout {
    var spacing: CGFloat = 8

    func sizeThatFits(proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) -> CGSize {
        let width = proposal.width ?? .infinity
        var x: CGFloat = 0, y: CGFloat = 0, rowHeight: CGFloat = 0, maxX: CGFloat = 0
        for view in subviews {
            let size = view.sizeThatFits(.unspecified)
            if x > 0, x + size.width > width {
                x = 0
                y += rowHeight + spacing
                rowHeight = 0
            }
            x += size.width + spacing
            maxX = max(maxX, x - spacing)
            rowHeight = max(rowHeight, size.height)
        }
        return CGSize(width: min(maxX, width), height: y + rowHeight)
    }

    func placeSubviews(in bounds: CGRect, proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) {
        var x = bounds.minX, y = bounds.minY, rowHeight: CGFloat = 0
        for view in subviews {
            let size = view.sizeThatFits(.unspecified)
            if x > bounds.minX, x + size.width > bounds.maxX {
                x = bounds.minX
                y += rowHeight + spacing
                rowHeight = 0
            }
            view.place(at: CGPoint(x: x, y: y), proposal: ProposedViewSize(size))
            x += size.width + spacing
            rowHeight = max(rowHeight, size.height)
        }
    }
}
