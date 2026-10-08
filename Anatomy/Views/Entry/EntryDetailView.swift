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
        }
        .atlasBackground()
        .navigationTitle(entry.tr)
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
                .foregroundStyle(on ? .yellow : .primary)
        }
        .sensoryFeedback(.impact(weight: .light), trigger: on)
        .accessibilityLabel(on ? "Favorilerden çıkar" : "Favorilere ekle")
    }
}

/// The body of an entry page; also used inside the 3D part sheet.
struct EntryContent: View {
    @Environment(AppModel.self) private var app
    let entry: AtlasEntry
    var showsModelButton = true

    var body: some View {
        let system = app.store.system(entry.systemID)
        let tint = system?.tint ?? .accentColor
        VStack(alignment: .leading, spacing: 16) {
            header(system: system, tint: tint)

            if showsModelButton, app.hasModel(entry) {
                HStack(spacing: 10) {
                    Button {
                        app.inspect(entry)
                    } label: {
                        Label("3D İncele", systemImage: "cube.transparent")
                            .frame(maxWidth: .infinity)
                    }
                    .buttonStyle(.glassProminent)
                    Button {
                        app.showInAtlas(entry)
                    } label: {
                        Label("Atlasta göster", systemImage: "figure.arms.open")
                            .frame(maxWidth: .infinity)
                    }
                    .buttonStyle(.glass)
                }
                .controlSize(.large)
            }

            ContentCard {
                Text(entry.summary)
                    .font(.body)
                    .fixedSize(horizontal: false, vertical: true)
            }

            if !entry.facts.isEmpty {
                ContentCard(title: "Temel bilgiler", systemImage: "list.bullet.rectangle", tint: tint) {
                    FactTable(facts: entry.facts, tint: tint)
                }
            }

            ForEach(entry.sections, id: \.title) { section in
                ContentCard(title: section.title, systemImage: "text.alignleft", tint: tint) {
                    Text(section.body)
                        .fixedSize(horizontal: false, vertical: true)
                }
            }

            if !entry.clinical.isEmpty {
                ContentCard(title: "Klinik bilgi", systemImage: "stethoscope", tint: .pink) {
                    VStack(alignment: .leading, spacing: 10) {
                        ForEach(entry.clinical, id: \.self) { note in
                            HStack(alignment: .firstTextBaseline, spacing: 8) {
                                Circle().fill(.pink).frame(width: 6, height: 6)
                                Text(note).fixedSize(horizontal: false, vertical: true)
                            }
                        }
                    }
                }
            }

            let related = app.store.related(of: entry)
            if !related.isEmpty {
                ContentCard(title: "İlişkili yapılar", systemImage: "point.3.connected.trianglepath.dotted", tint: tint) {
                    FlowLayout(spacing: 8) {
                        ForEach(related) { other in
                            NavigationLink(value: other) {
                                Text(other.tr)
                                    .font(.subheadline.weight(.medium))
                                    .padding(.horizontal, 12)
                                    .padding(.vertical, 7)
                                    .background(tint.opacity(0.12), in: .capsule)
                                    .foregroundStyle(tint)
                            }
                            .buttonStyle(.plain)
                        }
                    }
                }
            }

            if let reference = referenceText {
                ReferenceTextCard(text: reference)
            }
        }
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
                TagView(text: entry.region.title, color: .secondary, systemImage: entry.region.icon)
            }
            Text(entry.tr)
                .font(.largeTitle.weight(.bold))
                .fixedSize(horizontal: false, vertical: true)
            Text(entry.la)
                .font(.title3.italic())
                .foregroundStyle(tint)
            if entry.en != entry.la {
                Text(entry.en)
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
            }
        }
        .padding(.top, 8)
    }
}

/// English reference text from Z-Anatomy (Wikipedia derived), collapsed by default.
struct ReferenceTextCard: View {
    let text: String
    @State private var expanded = false

    var body: some View {
        ContentCard {
            DisclosureGroup(isExpanded: $expanded) {
                VStack(alignment: .leading, spacing: 10) {
                    ForEach(Array(text.components(separatedBy: "\n\n").enumerated()), id: \.offset) { _, paragraph in
                        if paragraph.hasPrefix("## ") {
                            Text(paragraph.dropFirst(3))
                                .font(.subheadline.weight(.semibold))
                                .padding(.top, 4)
                        } else {
                            Text(paragraph)
                                .font(.subheadline)
                                .foregroundStyle(.secondary)
                                .fixedSize(horizontal: false, vertical: true)
                        }
                    }
                    Text("Kaynak: Z-Anatomy (Wikipedia tabanlı), CC BY-SA 4.0")
                        .font(.caption2)
                        .foregroundStyle(.tertiary)
                }
                .padding(.top, 8)
            } label: {
                Label("İngilizce kaynak metin", systemImage: "book.closed")
                    .font(.headline)
            }
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
