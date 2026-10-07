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

    private var scene: AnatomyScene { app.scene }

    var body: some View {
        ZStack {
            backdrop
            // Only keep the 3D view alive while the tab is on screen so
            // RealityKit stops rendering in the background.
            if app.tab == .atlas {
                AnatomyViewport(scene: scene) { ref in
                    withAnimation(.snappy) { scene.select(ref) }
                    tapCount += 1
                }
                .ignoresSafeArea()
            }

            VStack(spacing: 12) {
                topBar
                if scene.isIsolating || !scene.hiddenParts.isEmpty || !scene.highlighted.isEmpty {
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

            if !scene.loadingLayers.isEmpty {
                loadingBadge
            }
        }
        .sensoryFeedback(.selection, trigger: tapCount)
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
                    GlassIconButton(systemImage: "scope", label: "Görünümü sıfırla") {
                        scene.resetCamera()
                    }
                }
            }
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
            Text(scene.isIsolating ? "İzole görünüm" : (scene.highlighted.isEmpty ? "\(scene.hiddenParts.count) parça gizli" : "\(scene.highlighted.count) parça vurgulandı"))
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

    private var loadingBadge: some View {
        HStack(spacing: 8) {
            ProgressView()
            Text("Model yükleniyor…")
                .font(.footnote.weight(.medium))
        }
        .padding(.horizontal, 14)
        .padding(.vertical, 10)
        .glassEffect(.regular, in: .capsule)
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

        VStack(alignment: .leading, spacing: 12) {
            HStack(alignment: .top, spacing: 12) {
                if let layer {
                    SystemBadge(icon: layer.icon, color: layer.tint, size: 38)
                }
                VStack(alignment: .leading, spacing: 3) {
                    Text(title(entry: exact ? entry : nil, latin: latin))
                        .font(.headline)
                        .lineLimit(2)
                    if let subtitle = subtitle(entry: exact ? entry : nil, latin: latin) {
                        Text(subtitle)
                            .font(.subheadline)
                            .foregroundStyle(.secondary)
                            .lineLimit(2)
                    }
                    if let entry, !exact {
                        Text("Bağlı yapı: \(entry.tr)")
                            .font(.caption)
                            .foregroundStyle(.tint)
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

            HStack(spacing: 8) {
                actionButton("Bilgi", systemImage: "info.circle", prominent: true, action: onInfo)
                actionButton("Odakla", systemImage: "scope") { app.scene.frame([ref]) }
                actionButton("İzole", systemImage: "viewfinder") {
                    app.scene.isolate([ref])
                    app.scene.frame([ref])
                }
                actionButton("Gizle", systemImage: "eye.slash") {
                    withAnimation(.snappy) { app.scene.hide(ref) }
                }
            }
        }
        .padding(16)
        .glassEffect(.regular, in: .rect(cornerRadius: 26))
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
            .background(prominent ? AnyShapeStyle(Color.accentColor) : AnyShapeStyle(.quaternary), in: .rect(cornerRadius: 14))
        }
        .buttonStyle(.plain)
    }
}
