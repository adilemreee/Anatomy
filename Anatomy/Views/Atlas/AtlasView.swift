//
//  AtlasView.swift
//  Anatomy
//

import SwiftUI

/// The 3D atlas: the whole-body model with floating controls.
struct AtlasView: View {
    @Environment(AppModel.self) private var app
    @Environment(\.colorScheme) private var colorScheme
    @State private var showLayers = false
    @State private var showParts = false
    @State private var detail: PartRef?
    @State private var tapCount = 0
    @AppStorage("atlas.labels") private var showLabels = false
    @State private var labels: [AnatomyScene.ScreenLabel] = []
    @State private var viewSize: CGSize = .zero

    private var scene: AnatomyScene { app.scene }

    /// Nothing is on screen yet and something is still coming.
    private var isFirstLoad: Bool {
        scene.loadedLayers.isEmpty && scene.failedLayers.isEmpty && !scene.enabledLayers.isEmpty
    }

    var body: some View {
        ZStack {
            backdrop
            AnatomyViewport(scene: scene, onTap: { ref in
                withAnimation(.snappy) { scene.select(ref) }
                tapCount += 1
            }, onSizeChange: {
                viewSize = $0
                if $0.height > 0 { scene.viewAspect = Float($0.width / $0.height) }
            }) {
                if showLabels, !scene.isCameraMoving {
                    labelLayer
                        .transition(.opacity)
                }
            }
            .ignoresSafeArea()
            .opacity(isFirstLoad ? 0 : 1)
            .animation(.easeOut(duration: 0.6), value: isFirstLoad)

            if isFirstLoad {
                FirstLoadView()
                    .transition(.opacity.combined(with: .scale(scale: 0.96)))
            }

            if !app.hidesChrome {
            VStack(spacing: 12) {
                topBar
                if !isFirstLoad, let layer = scene.loadingLayers.compactMap(ModelLayer.layer).first {
                    loadingBadge(layer)
                        .frame(maxWidth: .infinity, alignment: .leading)
                        .transition(.move(edge: .top).combined(with: .opacity))
                }
                if scene.isIsolating || !scene.hiddenParts.isEmpty || !scene.highlighted.isEmpty || !scene.fadedParts.isEmpty {
                    restoreBanner
                        .transition(.move(edge: .top).combined(with: .opacity))
                }
                Spacer()
                if let ref = scene.selection, let info = scene.info(ref) {
                    SelectionCard(ref: ref, info: info) {
                        detail = ref
                    }
                    .transition(.move(edge: .bottom).combined(with: .opacity))
                } else {
                    viewPresets
                }
            }
            .padding(.horizontal, 16)
            .padding(.bottom, 8)
            }
        }
        .animation(.snappy, value: scene.loadingLayers)
        .toolbarVisibility(app.hidesChrome ? .hidden : .automatic, for: .tabBar)
        .sensoryFeedback(.selection, trigger: tapCount)
        .task(id: LabelKey(camera: scene.cameraVersion, visibility: scene.visibilityVersion, enabled: showLabels, size: viewSize)) {
            guard showLabels else {
                labels = []
                return
            }
            try? await Task.sleep(for: .milliseconds(150))
            guard !Task.isCancelled else { return }
            let store = app.store
            let result = await scene.labels(in: viewSize) { store.displayName(for: $0) }
            guard !Task.isCancelled else { return }
            withAnimation(.easeOut(duration: 0.2)) { labels = result }
        }
        .animation(.snappy, value: scene.selection)
        .animation(.snappy, value: scene.isIsolating)
        .task {
            await scene.loadEnabledLayers()
            await app.store.loadGlossary()
        }
        .sheet(isPresented: $showLayers) {
            LayersSheet()
                .presentationDetents([.medium, .large])
                .presentationBackgroundInteraction(.enabled(upThrough: .medium))
        }
        .sheet(isPresented: $showParts) {
            PartsBrowser()
                .presentationDetents([.medium, .large])
        }
        .sheet(item: $detail) { ref in
            NavigationStack {
                PartDetailView(ref: ref)
            }
            .presentationDetents([.large])
        }
    }

    private var backdrop: some View {
        let colors: [Color] = colorScheme == .dark
            ? [Color(hex: "1d2330"), Color(hex: "0b0d12")]
            : [Color(hex: "f4f6fa"), Color(hex: "d9dee8")]
        return RadialGradient(colors: colors, center: .init(x: 0.5, y: 0.4), startRadius: 40, endRadius: 700)
            .ignoresSafeArea()
    }

    private var topBar: some View {
        HStack(alignment: .top) {
            VStack(alignment: .leading, spacing: 2) {
                Text("Anatomi Atlası")
                    .font(.title2.weight(.bold))
                Text(layerSummary)
                    .font(.caption)
                    .foregroundStyle(.secondary)
                    .lineLimit(1)
            }
            .padding(.top, 4)
            Spacer()
            GlassEffectContainer(spacing: 10) {
                VStack(spacing: 10) {
                    GlassIconButton(systemImage: "square.3.layers.3d", label: "Katmanlar") { showLayers = true }
                    GlassIconButton(systemImage: "list.bullet.indent", label: "Parça listesi") { showParts = true }
                    GlassIconButton(systemImage: "circle.lefthalf.filled", isOn: scene.xray, label: "Röntgen görünümü") {
                        scene.xray.toggle()
                    }
                    GlassIconButton(systemImage: "tag", isOn: showLabels, label: "Etiketler") {
                        withAnimation(.snappy) { showLabels.toggle() }
                    }
                    GlassIconButton(systemImage: "scope", label: "Görünümü sıfırla") {
                        scene.resetCamera()
                    }
                }
            }
        }
    }

    private var labelLayer: some View {
        ZStack(alignment: .topLeading) {
            ForEach(labels) { label in
                let color = scene.info(label.ref).map { MaterialStyles.swatch(for: $0, layer: label.ref.system, materials: scene.materialNames(label.ref.system), mode: scene.colorMode) } ?? .accentColor
                Path { path in
                    path.move(to: label.anchor)
                    path.addLine(to: CGPoint(x: label.center.x < label.anchor.x ? label.center.x + 4 : label.center.x - 4, y: label.center.y))
                }
                .stroke(.white.opacity(0.85), lineWidth: 1)
                Circle()
                    .fill(color)
                    .stroke(.white, lineWidth: 1.5)
                    .frame(width: 8, height: 8)
                    .position(label.anchor)
                Button {
                    withAnimation(.snappy) { scene.select(label.ref) }
                    tapCount += 1
                } label: {
                    Text(label.text)
                        .font(.caption2.weight(.semibold))
                        .lineLimit(1)
                        .fixedSize()
                        .padding(.horizontal, 8)
                        .padding(.vertical, 4)
                        .glassEffect(.regular, in: .capsule)
                }
                .buttonStyle(.plain)
                .position(label.center)
            }
        }
        .frame(width: viewSize.width, height: viewSize.height, alignment: .topLeading)
    }

    private struct LabelKey: Hashable {
        let camera: Int
        let visibility: Int
        let enabled: Bool
        let size: CGSize

        static func == (a: LabelKey, b: LabelKey) -> Bool {
            a.camera == b.camera && a.visibility == b.visibility && a.enabled == b.enabled && a.size == b.size
        }

        func hash(into hasher: inout Hasher) {
            hasher.combine(camera)
            hasher.combine(visibility)
            hasher.combine(enabled)
            hasher.combine(size.width)
            hasher.combine(size.height)
        }
    }

    private var layerSummary: String {
        let names = ModelLayer.all.filter { scene.isEnabled($0.id) }.map(\.title)
        return names.isEmpty ? "Katman seçilmedi" : names.joined(separator: " · ")
    }

    private var restoreBanner: some View {
        HStack(spacing: 10) {
            Image(systemName: scene.isIsolating ? "viewfinder" : "eye.slash")
                .foregroundStyle(.tint)
            Text(restoreTitle)
                .font(.subheadline.weight(.medium))
            Spacer()
            Button("Tümünü göster") {
                withAnimation(.snappy) {
                    scene.showAll()
                    scene.highlight([])
                }
            }
            .font(.subheadline.weight(.semibold))
        }
        .padding(.horizontal, 16)
        .padding(.vertical, 10)
        .glassEffect(.regular, in: .capsule)
    }

    private var viewPresets: some View {
        GlassEffectContainer {
            HStack(spacing: 4) {
                presetButton("Ön", yaw: 0)
                presetButton("Sol", yaw: .pi / 2)
                presetButton("Arka", yaw: .pi)
                presetButton("Sağ", yaw: -.pi / 2)
            }
            .padding(4)
            .glassEffect(.regular, in: .capsule)
        }
    }

    private func presetButton(_ title: String, yaw: Float) -> some View {
        Button {
            scene.rotate(toYaw: yaw)
        } label: {
            Text(title)
                .font(.subheadline.weight(.semibold))
                .padding(.horizontal, 14)
                .padding(.vertical, 9)
                .contentShape(.capsule)
        }
        .buttonStyle(.plain)
    }

    private var restoreTitle: String {
        if scene.isIsolating { return "İzole görünüm" }
        var parts: [String] = []
        if !scene.highlighted.isEmpty { parts.append("\(scene.highlighted.count) parça vurgulandı") }
        if !scene.fadedParts.isEmpty { parts.append("üstündekiler saydam") }
        if !scene.hiddenParts.isEmpty { parts.append("\(scene.hiddenParts.count) parça gizli") }
        return parts.isEmpty ? "Değiştirilmiş görünüm" : parts.joined(separator: " · ")
    }

    private func loadingBadge(_ layer: ModelLayer) -> some View {
        HStack(spacing: 8) {
            ProgressView()
                .controlSize(.small)
            Text("\(layer.title) yükleniyor…")
                .font(.caption.weight(.medium))
        }
        .padding(.horizontal, 12)
        .padding(.vertical, 8)
        .glassEffect(.regular, in: .capsule)
    }
}

/// Shown until the first layer of the model is on screen.
private struct FirstLoadView: View {
    var body: some View {
        VStack(spacing: 18) {
            Image(systemName: "figure.stand")
                .font(.system(size: 54, weight: .light))
                .foregroundStyle(.tint)
                .symbolEffect(.breathe.pulse, options: .repeating)
                .frame(width: 112, height: 112)
                .glassEffect(.regular, in: .circle)
            VStack(spacing: 6) {
                Text("3B model hazırlanıyor")
                    .font(.headline)
                Text("Z-Anatomy modelinin binlerce parçası yükleniyor")
                    .font(.footnote)
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
            }
            ProgressView()
        }
        .padding(32)
        .accessibilityElement(children: .combine)
    }
}

extension PartRef: Identifiable {
    var id: String { "\(system)#\(index)" }
}

/// Bottom card describing the selected part.
private struct SelectionCard: View {
    @Environment(AppModel.self) private var app
    let ref: PartRef
    let info: PartInfo
    let onInfo: () -> Void

    var body: some View {
        let store = app.store
        let layer = ModelLayer.layer(ref.system)
        let entry = store.entry(for: info)
        let exact = entry.map { store.isExact($0, for: info) } ?? false
        let latin = store.latinName(for: info)
        let group = app.scene.selectedGroup

        VStack(alignment: .leading, spacing: 12) {
            HStack(alignment: .top, spacing: 12) {
                if let layer {
                    SystemBadge(icon: layer.icon, color: layer.tint, size: 40)
                }
                VStack(alignment: .leading, spacing: 3) {
                    Text(title(entry: exact ? entry : nil, latin: latin))
                        .font(.headline)
                        .lineLimit(2)
                    if let subtitle = subtitle(entry: exact ? entry : nil, latin: latin) {
                        Text(subtitle)
                            .font(.subheadline.italic())
                            .foregroundStyle(.secondary)
                            .lineLimit(1)
                    }
                    if let entry, !exact {
                        Text("Bağlı yapı: \(entry.tr)")
                            .font(.caption.weight(.medium))
                            .foregroundStyle(.tint)
                    } else if group.count > 1 {
                        Text("\(group.count) bölümüyle birlikte seçildi")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                    }
                }
                Spacer(minLength: 0)
                Button {
                    withAnimation(.snappy) { app.scene.select(nil) }
                } label: {
                    Image(systemName: "xmark")
                        .font(.footnote.weight(.bold))
                        .frame(width: 30, height: 30)
                }
                .buttonStyle(.plain)
                .glassEffect(.regular.interactive(), in: .circle)
                .accessibilityLabel("Seçimi kaldır")
            }

            if let summary = summary(entry: entry, exact: exact) {
                Text(summary)
                    .font(.footnote)
                    .foregroundStyle(.secondary)
                    .lineLimit(3)
                    .fixedSize(horizontal: false, vertical: true)
            }

            HStack(spacing: 8) {
                actionButton("İncele", systemImage: "cube.transparent", prominent: true) {
                    let refs = Array(group.isEmpty ? [ref] : group)
                    app.specimen = app.specimenRequest(
                        for: refs,
                        title: title(entry: exact ? entry : nil, latin: latin),
                        subtitle: (exact ? entry?.la : nil) ?? latin ?? info.base,
                        entryID: entry?.id
                    )
                }
                actionButton("Bilgi", systemImage: "info.circle", action: onInfo)
                actionButton("İzole", systemImage: "viewfinder") {
                    let refs = group.isEmpty ? [ref] : group
                    app.scene.isolate(refs)
                    app.scene.frame(Array(refs))
                }
                actionButton("Gizle", systemImage: "eye.slash") {
                    withAnimation(.snappy) { app.scene.hide(ref) }
                }
            }
        }
        .padding(16)
        .glassEffect(.regular, in: .rect(cornerRadius: 26))
    }

    private func summary(entry: AtlasEntry?, exact: Bool) -> String? {
        if let entry, exact { return entry.summary }
        if let def = app.store.term(info.base)?.def {
            return def.components(separatedBy: "\n\n").first
        }
        return entry?.summary
    }

    private func title(entry: AtlasEntry?, latin: String?) -> String {
        let side = info.sideTitle.map { " (\($0))" } ?? ""
        if let entry { return entry.tr + side }
        return (latin ?? info.base) + side
    }

    private func subtitle(entry: AtlasEntry?, latin: String?) -> String? {
        if let entry { return entry.la == entry.tr ? entry.en : entry.la }
        if let latin, latin.lowercased() != info.base.lowercased() { return info.base }
        if let kind = info.kind { return kind == "origin" ? "Kasın başlangıç yeri (origo)" : "Kasın yapışma yeri (insersiyo)" }
        return info.path.last
    }

    private func actionButton(_ title: String, systemImage: String, prominent: Bool = false, action: @escaping () -> Void) -> some View {
        Button(action: action) {
            VStack(spacing: 4) {
                Image(systemName: systemImage)
                    .font(.system(size: 16, weight: .semibold))
                Text(title)
                    .font(.caption2.weight(.semibold))
            }
            .frame(maxWidth: .infinity)
            .padding(.vertical, 8)
            .foregroundStyle(prominent ? Color.white : Color.primary)
            .background(prominent ? AnyShapeStyle(Color.accentColor.gradient) : AnyShapeStyle(.quaternary), in: .rect(cornerRadius: 14))
        }
        .buttonStyle(.plain)
    }
}
