//
//  SpecimenView.swift
//  Anatomy
//

import SwiftUI

/// What to show in the specimen viewer.
struct SpecimenRequest: Identifiable, Hashable {
    let id = UUID()
    /// What is studied (framed and labelled), including attachment patches.
    let refs: [PartRef]
    /// Shown around it for orientation, e.g. the bones a muscle attaches to.
    var context: [PartRef] = []
    let title: String
    let subtitle: String
    let entryID: String?
}

/// Full-screen viewer for one structure with its labelled features.
struct SpecimenView: View {
    @Environment(AppModel.self) private var app
    @Environment(\.dismiss) private var dismiss
    let request: SpecimenRequest
    @State private var scene = SpecimenScene()
    @State private var labels: [SpecimenScene.Label] = []
    @State private var size: CGSize = .zero
    @State private var showLabels = true
    @State private var focused: Int?
    @State private var showEntry = false
    @State private var showFeatures = false
    @State private var headerBottom: CGFloat = 170
    @State private var controlsTop: CGFloat = 760

    var body: some View {
        ZStack {
            RadialGradient(colors: [Color(hex: "262c38"), Color(hex: "0c0e13")], center: .init(x: 0.5, y: 0.42), startRadius: 30, endRadius: 650)
                .ignoresSafeArea()

            AnatomyViewport(scene: scene, onTap: { _ in }, onSizeChange: {
                size = $0
                scene.setViewSize($0)
            }) {
                if showLabels, scene.isReady, !scene.isCameraMoving {
                    labelLayer.transition(.opacity)
                }
            }
            .ignoresSafeArea()
            .opacity(scene.isReady ? 1 : 0)

            if !scene.isReady {
                ProgressView().tint(.white).controlSize(.large)
            }

            VStack {
                header
                    .onGeometryChange(for: CGFloat.self) { $0.frame(in: .global).maxY } action: { headerBottom = $0 }
                Spacer()
                if let focused, scene.allFeatures.indices.contains(focused) {
                    let feature = scene.allFeatures[focused]
                    let names = names(for: feature)
                    FeatureCard(title: names.title, subtitle: names.subtitle, kind: feature.kind,
                                turkish: app.store.partTerm(feature.name)?.d, definition: app.store.term(feature.name)?.def,
                                zoom: { scene.focus(feature: focused) },
                                close: { withAnimation(.snappy) { self.focused = nil } })
                        .id(focused)
                        .transition(.move(edge: .bottom).combined(with: .opacity))
                        .padding(.bottom, 10)
                }
                controls
                    .onGeometryChange(for: CGFloat.self) { $0.frame(in: .global).minY } action: { controlsTop = $0 }
            }
            .padding(.horizontal, 16)
            .padding(.bottom, 8)
        }
        .environment(\.colorScheme, .dark)
        .statusBarHidden(false)
        .task {
            await app.store.loadGlossary()
            await scene.load(refs: request.refs, context: request.context, mode: app.scene.colorMode)
        }
        .task(id: LabelKey(version: scene.cameraVersion, show: showLabels, size: size, top: headerBottom, bottom: controlsTop)) {
            guard showLabels, scene.isReady else { labels = []; return }
            try? await Task.sleep(for: .milliseconds(120))
            guard !Task.isCancelled else { return }
            let store = app.store
            let result = await scene.labels(in: size, top: headerBottom + 10, bottom: controlsTop - 12,
                                            names: { store.featureNames($0) },
                                            priority: { store.landmark($0)?.rank ?? 0 })
            guard !Task.isCancelled else { return }
            withAnimation(.easeOut(duration: 0.25)) { labels = result }
        }
        // The tapped feature's region glows on the model.
        .onChange(of: focused) { _, feature in scene.highlight(feature: feature) }
        // A tap on the model picks the nearest visible feature; empty space clears.
        .onChange(of: scene.tapVersion) {
            withAnimation(.snappy) { focused = scene.tappedFeature }
        }
        .sheet(isPresented: $showFeatures) {
            FeatureList(features: scene.allFeatures, names: names(for:), selected: focused) { index in
                showFeatures = false
                withAnimation(.snappy) { focused = index }
                scene.focus(feature: index)
            }
            .presentationDetents([.medium, .large])
            .presentationBackground(Theme.surface)
            .preferredColorScheme(.dark)
        }
        .sheet(isPresented: $showEntry) {
            if let id = request.entryID, let entry = app.store.entry(id) {
                NavigationStack {
                    EntryDetailView(entry: entry)
                        .navigationDestination(for: AtlasEntry.self) { EntryDetailView(entry: $0) }
                        .toolbar {
                            ToolbarItem(placement: .confirmationAction) { Button("Kapat") { showEntry = false } }
                        }
                }
                .appOverlays(specimen: false)
                .preferredColorScheme(.dark)
            }
        }
    }

    private var header: some View {
        HStack(alignment: .top) {
            VStack(alignment: .leading, spacing: 3) {
                Text("İNCELEME")
                    .font(.caption2.weight(.bold))
                    .tracking(1.2)
                    .foregroundStyle(.cyan)
                Text(request.title)
                    .font(.title2.weight(.bold))
                    .foregroundStyle(.white)
                if !request.subtitle.isEmpty {
                    Text(request.subtitle)
                        .font(app.store.latinFirst ? .subheadline : .subheadline.italic())
                        .foregroundStyle(.white.opacity(0.7))
                }
                if scene.hasAttachments {
                    HStack(spacing: 12) {
                        legendDot(.origin, String(localized: "Başlangıç yeri"))
                        legendDot(.insertion, String(localized: "Tutunma yeri"))
                    }
                    .padding(.top, 4)
                } else if scene.featureCount > 0 {
                    Text("\(scene.featureCount) işaretli oluşum · bir etikete dokun")
                        .font(.caption)
                        .foregroundStyle(.white.opacity(0.5))
                        .padding(.top, 2)
                }
            }
            Spacer()
            Button {
                dismiss()
            } label: {
                Image(systemName: "xmark")
                    .font(.headline)
                    .frame(width: 44, height: 44)
            }
            .buttonStyle(.plain)
            .glassEffect(.regular.interactive(), in: .circle)
            .accessibilityLabel("Kapat")
        }
        .padding(.top, 8)
    }

    /// Turkish name and Latin subtitle of a feature, as on its label.
    private func names(for feature: FeatureLibrary.Feature) -> (title: String, subtitle: String?) {
        let store = app.store
        let name = store.featureNames(feature.name)
        let title = name.tr ?? name.la ?? feature.name
        switch feature.kind {
        case .origin, .insertion:
            let role = feature.kind == .origin ? String(localized: "Başlangıç yeri") : String(localized: "Tutunma yeri")
            return (title, feature.bone.map { "\(role) · \(store.featureNames($0).tr ?? $0)" } ?? role)
        case .feature, .part: return (title, LabelLayout.subtitle(name.la, under: title))
        }
    }

    private func legendDot(_ kind: FeatureLibrary.Feature.Kind, _ title: String) -> some View {
        HStack(spacing: 5) {
            Circle().fill(Self.color(for: kind)).frame(width: 8, height: 8)
            Text(title)
                .font(.caption)
                .foregroundStyle(.white.opacity(0.7))
        }
    }

    static func color(for kind: FeatureLibrary.Feature.Kind) -> Color {
        switch kind {
        case .origin: Color(hex: "e8564b")
        case .insertion: Color(hex: "4f8ff0")
        case .feature, .part: .white
        }
    }

    private var controls: some View {
        GlassEffectContainer(spacing: 10) {
            // Four views and three buttons share the row; longer view names
            // (German, French) take a smaller font or a row of their own.
            ViewThatFits(in: .horizontal) {
                HStack(spacing: 10) {
                    turnButtons(.subheadline, padding: 11)
                    iconButtons
                }
                HStack(spacing: 10) {
                    turnButtons(.footnote, padding: 7)
                    iconButtons
                }
                VStack(spacing: 10) {
                    turnButtons(.subheadline, padding: 11)
                    HStack(spacing: 10) { iconButtons }
                }
            }
        }
    }

    @ViewBuilder private var iconButtons: some View {
        GlassIconButton(systemImage: "tag", isOn: showLabels, label: String(localized: "Etiketler")) {
            withAnimation(.snappy) { showLabels.toggle() }
        }
        if scene.featureCount > 0 {
            GlassIconButton(systemImage: "list.bullet", label: String(localized: "Oluşumlar")) { showFeatures = true }
        }
        if request.entryID != nil {
            GlassIconButton(systemImage: "book", label: String(localized: "Madde")) { showEntry = true }
        }
    }

    private func turnButtons(_ font: Font, padding: CGFloat) -> some View {
        HStack(spacing: 2) {
            // Views, not sides: "Sağ"/"Sol" alone name a body side.
            turnButton(LocalizedStringResource("view.front", defaultValue: "Ön"), 0, font, padding)
            turnButton(LocalizedStringResource("view.left", defaultValue: "Sol"), .pi / 2, font, padding)
            turnButton(LocalizedStringResource("view.back", defaultValue: "Arka"), .pi, font, padding)
            turnButton(LocalizedStringResource("view.right", defaultValue: "Sağ"), -.pi / 2, font, padding)
        }
        .padding(4)
        .glassEffect(.regular, in: .capsule)
    }

    private func turnButton(_ title: LocalizedStringResource, _ yaw: Float, _ font: Font, _ padding: CGFloat) -> some View {
        Button {
            scene.turn(to: yaw)
        } label: {
            Text(title)
                .font(font.weight(.semibold))
                .lineLimit(1)
                .fixedSize()
                .padding(.horizontal, padding)
                .padding(.vertical, 9)
                .contentShape(.capsule)
        }
        .buttonStyle(.plain)
    }

    private var labelLayer: some View {
        ZStack(alignment: .topLeading) {
            ForEach(labels) { label in
                let isFocused = focused == label.id
                let dimmed = focused != nil && !isFocused
                Path { path in
                    // A short level stub out of the box, then on to the point.
                    let attach = label.attach
                    path.move(to: attach)
                    if attach.x == label.box.minX || attach.x == label.box.maxX {
                        path.addLine(to: CGPoint(x: attach.x + (attach.x == label.box.minX ? -8 : 8), y: attach.y))
                    }
                    path.addLine(to: label.anchor)
                }
                .stroke(Color.white.opacity(isFocused ? 0.95 : (dimmed ? 0.25 : 0.6)), lineWidth: isFocused ? 1.4 : 0.8)
                Circle()
                    .fill(isFocused ? Color.cyan : Self.color(for: label.kind))
                    .frame(width: isFocused ? 8 : 6, height: isFocused ? 8 : 6)
                    .overlay { Circle().stroke(Color.black.opacity(0.35), lineWidth: 0.5) }
                    .position(label.anchor)
                Button {
                    withAnimation(.snappy) { focused = isFocused ? nil : label.id }
                    // Turn so the coloured region faces the viewer.
                    if !isFocused { scene.focus(feature: label.id, zoom: false) }
                } label: {
                    VStack(alignment: .leading, spacing: 1) {
                        Text(label.title)
                            .font(.caption.weight(.semibold))
                            .foregroundStyle(.white)
                            .lineLimit(3)
                            .minimumScaleFactor(0.85)
                        if let subtitle = label.subtitle {
                            Text(subtitle)
                                .font(app.store.latinFirst ? .caption2 : .caption2.italic())
                                .foregroundStyle(.white.opacity(0.62))
                                .lineLimit(1)
                                .minimumScaleFactor(0.7)
                        }
                    }
                    .padding(.horizontal, 9)
                    .frame(width: label.box.width, height: label.box.height, alignment: .leading)
                    .background(Color.black.opacity(isFocused ? 0.62 : 0.42), in: .rect(cornerRadius: 7))
                    .overlay(alignment: .leading) {
                        if label.kind == .origin || label.kind == .insertion {
                            UnevenRoundedRectangle(topLeadingRadius: 7, bottomLeadingRadius: 7)
                                .fill(Self.color(for: label.kind))
                                .frame(width: 3)
                        }
                    }
                    .overlay {
                        RoundedRectangle(cornerRadius: 7).strokeBorder(isFocused ? Color.cyan : Color.white.opacity(0.14), lineWidth: 1)
                    }
                }
                .buttonStyle(.plain)
                .opacity(dimmed ? 0.45 : 1)
                .position(x: label.box.midX, y: label.box.midY)
                .accessibilityLabel(label.subtitle.map { "\(label.title), \($0)" } ?? label.title)
            }
        }
        .frame(width: size.width, height: size.height, alignment: .topLeading)
    }

    private struct LabelKey: Hashable {
        let version: Int
        let show: Bool
        let width: CGFloat
        let height: CGFloat
        let top: CGFloat
        let bottom: CGFloat

        init(version: Int, show: Bool, size: CGSize, top: CGFloat, bottom: CGFloat) {
            self.version = version
            self.show = show
            width = size.width
            height = size.height
            self.top = top.rounded()
            self.bottom = bottom.rounded()
        }
    }
}

/// Details for the focused feature: names, description and a button that
/// turns the camera to it.
private struct FeatureCard: View {
    let title: String
    let subtitle: String?
    let kind: FeatureLibrary.Feature.Kind
    /// Short Turkish description from the dictionary, when there is one.
    let turkish: String?
    let definition: String?
    let zoom: () -> Void
    let close: () -> Void

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            HStack(alignment: .top, spacing: 10) {
                Circle()
                    .fill(kind == .origin ? Color(hex: "e8564b") : (kind == .insertion ? Color(hex: "4f8ff0") : Color(hex: "1a9eff")))
                    .frame(width: 10, height: 10)
                    .padding(.top, 6)
                VStack(alignment: .leading, spacing: 2) {
                    Text(title)
                        .font(.headline)
                        .fixedSize(horizontal: false, vertical: true)
                    if let subtitle {
                        Text(subtitle)
                            .font(.subheadline.italic())
                            .foregroundStyle(.secondary)
                    }
                }
                Spacer()
                Button(action: close) {
                    Image(systemName: "xmark.circle.fill")
                        .font(.title3)
                        .symbolRenderingMode(.hierarchical)
                }
                .buttonStyle(.plain)
                .accessibilityLabel("Kapat")
            }
            if let turkish, !turkish.isEmpty {
                Text(turkish)
                    .font(.footnote)
                    .foregroundStyle(.secondary)
                    .fixedSize(horizontal: false, vertical: true)
            } else if let text = summary {
                Text(text)
                    .font(.footnote)
                    .foregroundStyle(.secondary)
                    .lineLimit(4)
                    .fixedSize(horizontal: false, vertical: true)
                Text("Kaynak: Z-Anatomy (Wikipedia tabanlı), CC BY-SA 4.0")
                    .font(.caption2)
                    .foregroundStyle(.tertiary)
            }
            Button(action: zoom) {
                Label("Yakınlaş", systemImage: "scope")
                    .font(.subheadline.weight(.semibold))
                    .padding(.horizontal, 14)
                    .padding(.vertical, 8)
                    .background(Color(hex: "1a9eff").opacity(0.22), in: .capsule)
                    .foregroundStyle(Color(hex: "7cc8ff"))
            }
            .buttonStyle(.plain)
        }
        .padding(14)
        .frame(maxWidth: 560, alignment: .leading)
        .glassEffect(.regular, in: .rect(cornerRadius: 20))
    }

    /// The first plain paragraph of the reference text.
    private var summary: String? {
        definition?.components(separatedBy: "\n\n").first { !$0.hasPrefix("## ") && $0.count > 20 }
    }
}

/// Every labelled feature of the specimen, searchable; picking one turns
/// the camera to it and colours its region.
private struct FeatureList: View {
    let features: [FeatureLibrary.Feature]
    let names: (FeatureLibrary.Feature) -> (title: String, subtitle: String?)
    let selected: Int?
    let pick: (Int) -> Void
    @State private var query = ""

    var body: some View {
        NavigationStack {
            List {
                ForEach(rows, id: \.index) { row in
                    Button {
                        pick(row.index)
                    } label: {
                        HStack(spacing: 12) {
                            Circle()
                                .fill(SpecimenView.color(for: row.kind) == .white ? Color(hex: "1a9eff") : SpecimenView.color(for: row.kind))
                                .frame(width: 8, height: 8)
                            VStack(alignment: .leading, spacing: 2) {
                                Text(row.title)
                                    .font(.subheadline.weight(.medium))
                                    .foregroundStyle(Theme.textPrimary)
                                if let subtitle = row.subtitle {
                                    Text(subtitle)
                                        .font(Theme.latin(.caption))
                                        .foregroundStyle(Theme.textSecondary)
                                }
                            }
                            Spacer()
                            if row.index == selected {
                                Image(systemName: "checkmark")
                                    .foregroundStyle(Theme.accent)
                            }
                        }
                        .contentShape(.rect)
                    }
                    .buttonStyle(.plain)
                    .listRowBackground(Theme.card)
                }
            }
            .scrollContentBackground(.hidden)
            .searchable(text: $query, placement: .navigationBarDrawer(displayMode: .always), prompt: "Oluşum ara")
            .navigationTitle("Oluşumlar (\(features.count))")
            .navigationBarTitleDisplayMode(.inline)
        }
    }

    private var rows: [(index: Int, title: String, subtitle: String?, kind: FeatureLibrary.Feature.Kind)] {
        let all = features.enumerated().map { i, f in
            let n = names(f)
            return (index: i, title: n.title, subtitle: n.subtitle, kind: f.kind)
        }
        // A muscle can attach to one bone at several patches: list it once.
        var seen = Set<String>()
        let unique = all.filter { seen.insert("\($0.title)|\($0.subtitle ?? "")").inserted }
        let q = query.trimmingCharacters(in: .whitespaces)
        let filtered = q.isEmpty ? unique : unique.filter {
            $0.title.localizedStandardContains(q) || ($0.subtitle?.localizedStandardContains(q) ?? false)
        }
        return filtered.sorted { $0.title.localizedStandardCompare($1.title) == .orderedAscending }
    }
}
