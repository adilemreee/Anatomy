//
//  AtlasView.swift
//  Anatomy
//

import SwiftUI

/// The 3D atlas: the whole body on a dark stage, a rail of body systems on
/// the left, a search field on top and a tool bar (or the selected
/// structure) at the bottom.
struct AtlasView: View {
    @Environment(AppModel.self) private var app
    @Environment(\.displayScale) private var displayScale
    @State private var showLayers = false
    @State private var showSearch = false
    @State private var detail: PartRef?
    @State private var tapCount = 0
    @AppStorage("atlas.labels") private var showLabels = false
    @AppStorage("atlas.gestureHintSeen") private var gestureHintSeen = false
    /// Search and the system rail folded away so the model gets the screen.
    @AppStorage("atlas.compact") private var compact = false
    @AppStorage("atlas.focusOnTap") private var focusOnTap = true
    @State private var labels: [AnatomyScene.ScreenLabel] = []
    @State private var viewSize: CGSize = .zero
    /// Free band for labels between the top controls and the toolbar, and
    /// the system rail on the left that labels keep clear of.
    @State private var chromeTop: CGFloat = 120
    @State private var chromeBottom: CGFloat = 0
    @State private var railFrame: CGRect = .zero
    @State private var toast: String?

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
                if ref != nil {
                    tapCount += 1
                    // Move towards the structure so it stands out.
                    if focusOnTap { scene.focus(on: Array(scene.selectedGroup)) }
                }
                gestureHintSeen = true
            }, onSizeChange: {
                viewSize = $0
                scene.setViewport(size: $0, scale: displayScale)
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
                chrome
            }

            if !gestureHintSeen, !isFirstLoad, !app.hidesChrome, !UserDefaults.standard.bool(forKey: "AtlasNoHint") {
                GestureHint { withAnimation(.easeOut) { gestureHintSeen = true } }
                    .transition(.opacity)
            }
        }
        .animation(.snappy, value: scene.loadingLayers)
        .animation(.snappy, value: scene.selection)
        .animation(.snappy, value: scene.isIsolating)
        .toolbarVisibility(app.hidesChrome ? .hidden : .automatic, for: .tabBar)
        .sensoryFeedback(.selection, trigger: tapCount)
        .task(id: LabelKey(camera: scene.cameraVersion, visibility: scene.visibilityVersion, enabled: showLabels, size: viewSize,
                           frame: [chromeTop, chromeBottom, railFrame.minX, railFrame.minY, railFrame.maxX, railFrame.maxY].map { $0.rounded() })) {
            guard showLabels else {
                labels = []
                return
            }
            try? await Task.sleep(for: .milliseconds(150))
            guard !Task.isCancelled else { return }
            let store = app.store
            let premium = app.isPremium
            let bottom = chromeBottom > chromeTop + 200 ? chromeBottom - 8 : viewSize.height - 150
            let result = await scene.labels(in: viewSize, top: chromeTop + 8, bottom: bottom,
                                            avoiding: railFrame.isEmpty ? [] : [railFrame.insetBy(dx: -4, dy: -4)]) {
                store.title(for: $0)
            }
                .filter { premium || $0.ref.system == Access.freeLayer }
            guard !Task.isCancelled else { return }
            withAnimation(.easeOut(duration: 0.2)) { labels = result }
        }
        .task {
            await scene.loadEnabledLayers()
            await app.store.loadGlossary()
        }
        .sheet(isPresented: $showLayers) {
            LayersSheet()
                .appOverlays()
                .presentationDetents([.medium, .large])
                .presentationBackgroundInteraction(.enabled(upThrough: .medium))
        }
        .sheet(isPresented: $showSearch) {
            PartsBrowser()
                .appOverlays()
                .presentationDetents([.large])
        }
        .sheet(item: $detail) { ref in
            NavigationStack {
                PartDetailView(ref: ref)
            }
            .appOverlays()
            .presentationDetents([.medium, .large])
            .presentationBackgroundInteraction(.enabled(upThrough: .medium))
        }
    }

    private var chrome: some View {
        VStack(spacing: 10) {
            topBar
                .onGeometryChange(for: CGFloat.self) { $0.frame(in: .global).maxY } action: { chromeTop = $0 }
            if !isFirstLoad, let layer = scene.loadingLayers.compactMap(ModelLayer.layer).first {
                loadingBadge(layer)
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
                toolBar
                    .onGeometryChange(for: CGFloat.self) { $0.frame(in: .global).minY } action: { chromeBottom = $0 }
                    .transition(.move(edge: .bottom).combined(with: .opacity))
            }
        }
        .padding(.horizontal, 16)
        .padding(.bottom, 8)
        .overlay(alignment: .leading) {
            if scene.selection == nil {
                Group {
                    if compact {
                        CollapsedRail { withAnimation(.snappy) { compact = false } }
                    } else {
                        SystemRail(announce: { message in showToast(message) },
                                   collapse: { withAnimation(.snappy) { compact = true } })
                    }
                }
                .padding(.leading, 12)
                .onGeometryChange(for: CGRect.self) { $0.frame(in: .global) } action: { railFrame = $0 }
                .onDisappear { railFrame = .zero }
                .transition(.move(edge: .leading).combined(with: .opacity))
            }
        }
        .animation(.snappy, value: compact)
        .overlay(alignment: .center) {
            if let toast {
                Text(toast)
                    .font(.subheadline.weight(.semibold))
                    .padding(.horizontal, 16)
                    .padding(.vertical, 10)
                    .glassEffect(.regular, in: .capsule)
                    .transition(.opacity.combined(with: .scale(scale: 0.9)))
                    .allowsHitTesting(false)
            }
        }
    }

    private func showToast(_ text: String) {
        withAnimation(.snappy) { toast = text }
        Task {
            try? await Task.sleep(for: .seconds(1.3))
            if toast == text { withAnimation(.easeOut) { toast = nil } }
        }
    }

    private var backdrop: some View {
        ZStack {
            Theme.background
            RadialGradient(colors: [Color(hex: "283041").opacity(0.95), .clear], center: .init(x: 0.5, y: 0.38), startRadius: 20, endRadius: 520)
        }
        .ignoresSafeArea()
    }

    // MARK: Top

    private var topBar: some View {
        HStack(spacing: 10) {
            if compact {
                Button {
                    showSearch = true
                } label: {
                    Image(systemName: "magnifyingglass")
                        .font(.system(size: 17, weight: .semibold))
                        .foregroundStyle(Theme.textPrimary)
                        .frame(width: 46, height: 46)
                }
                .buttonStyle(.plain)
                .glassEffect(.regular.interactive(), in: .circle)
                .accessibilityLabel("Yapı ara")
                Spacer()
            } else {
                Button {
                    showSearch = true
                } label: {
                    HStack(spacing: 10) {
                        Image(systemName: "magnifyingglass")
                            .font(.body.weight(.semibold))
                            .foregroundStyle(Theme.textSecondary)
                        Text("Yapı ara: femur, deltoid, diz eklemi…")
                            .font(.subheadline)
                            .foregroundStyle(Theme.textSecondary)
                            .lineLimit(1)
                        Spacer(minLength: 0)
                    }
                    .padding(.horizontal, 16)
                    .frame(height: 46)
                    .contentShape(.capsule)
                }
                .buttonStyle(.plain)
                .glassEffect(.regular.interactive(), in: .capsule)
                .accessibilityLabel("Yapı ara")
            }

            if !app.isPremium {
                Button {
                    app.requirePremium(.general)
                } label: {
                    Image(systemName: "crown.fill")
                        .font(.system(size: 17, weight: .bold))
                        .foregroundStyle(Theme.goldGradient)
                        .frame(width: 46, height: 46)
                }
                .buttonStyle(.plain)
                .glassEffect(.regular.interactive(), in: .circle)
                .accessibilityLabel("Premium")
            }
        }
        .padding(.top, 6)
    }

    // MARK: Bottom tools

    private var toolBar: some View {
        GlassEffectContainer(spacing: 8) {
            HStack(spacing: compact ? 0 : 2) {
                ToolButton(title: String(localized: "Sıfırla"), systemImage: "arrow.counterclockwise", compact: compact) {
                    withAnimation(.snappy) {
                        scene.showAll()
                        scene.highlight([])
                        scene.select(nil)
                    }
                    scene.resetCamera()
                }
                Menu {
                    Button("Önden", systemImage: "person") { scene.rotate(toYaw: 0) }
                    Button("Arkadan", systemImage: "person.fill") { scene.rotate(toYaw: .pi) }
                    Button("Soldan", systemImage: "arrow.left") { scene.rotate(toYaw: .pi / 2) }
                    Button("Sağdan", systemImage: "arrow.right") { scene.rotate(toYaw: -.pi / 2) }
                } label: {
                    ToolLabel(title: String(localized: "Bakış"), systemImage: "rotate.3d", compact: compact)
                }
                .buttonStyle(.plain)
                ToolButton(title: String(localized: "Etiketler"), systemImage: "tag", isOn: showLabels, compact: compact) {
                    withAnimation(.snappy) { showLabels.toggle() }
                }
                ToolButton(title: String(localized: "Röntgen"), systemImage: "circle.lefthalf.filled", isOn: scene.xray, compact: compact) {
                    scene.xray.toggle()
                }
                Menu {
                    Picker("Model", selection: Binding(get: { app.sex }, set: { newValue in
                        if newValue == .female, !app.requirePremium(.femaleAnatomy) { return }
                        app.sex = newValue
                    })) {
                        Label("Erkek modeli", systemImage: "figure.stand").tag(BodySex.male)
                        Label("Kadın modeli", systemImage: "figure.stand.dress").tag(BodySex.female)
                    }
                } label: {
                    ToolLabel(title: app.sex.title, systemImage: app.sex == .female ? "figure.stand.dress" : "figure.stand", compact: compact)
                }
                .buttonStyle(.plain)
                .accessibilityLabel("Model: \(app.sex.title)")
                ToolButton(title: String(localized: "Katmanlar"), systemImage: "slider.horizontal.3", compact: compact) {
                    showLayers = true
                }
            }
            .padding(5)
            .glassEffect(.regular, in: .capsule)
        }
    }

    // MARK: Labels

    private var labelLayer: some View {
        ZStack(alignment: .topLeading) {
            ForEach(labels) { label in
                let color = scene.info(label.ref).map { MaterialStyles.swatch(for: $0, layer: label.ref.system, materials: scene.materialNames(label.ref.system), mode: scene.colorMode) } ?? .accentColor
                Path { path in
                    // A short level stub out of the pill, then on to the pin.
                    let attach = label.attach
                    path.move(to: attach)
                    path.addLine(to: CGPoint(x: attach.x + (attach.x == label.box.minX ? -7 : 7), y: attach.y))
                    path.addLine(to: label.anchor)
                }
                .stroke(.white.opacity(0.75), lineWidth: 1)
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
                        .foregroundStyle(.white)
                        .lineLimit(1)
                        .minimumScaleFactor(0.8)
                        .frame(width: label.box.width, height: label.box.height)
                        .background(Color.black.opacity(0.55), in: .capsule)
                        .overlay { Capsule().strokeBorder(Color.white.opacity(0.14)) }
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

        let frame: [CGFloat]

        static func == (a: LabelKey, b: LabelKey) -> Bool {
            a.camera == b.camera && a.visibility == b.visibility && a.enabled == b.enabled && a.size == b.size && a.frame == b.frame
        }

        func hash(into hasher: inout Hasher) {
            hasher.combine(camera)
            hasher.combine(visibility)
            hasher.combine(enabled)
            hasher.combine(size.width)
            hasher.combine(size.height)
            hasher.combine(frame)
        }
    }

    // MARK: Status

    private var restoreBanner: some View {
        HStack(spacing: 10) {
            Image(systemName: scene.isIsolating ? "viewfinder" : "eye.slash")
                .foregroundStyle(Theme.accent)
            Text(restoreTitle)
                .font(.subheadline.weight(.medium))
                .lineLimit(1)
                .minimumScaleFactor(0.8)
            Spacer()
            Button("Tümünü göster") {
                withAnimation(.snappy) {
                    scene.showAll()
                    scene.highlight([])
                }
            }
            .font(.subheadline.weight(.semibold))
            .foregroundStyle(Theme.accent)
        }
        .padding(.horizontal, 16)
        .padding(.vertical, 10)
        .glassEffect(.regular, in: .capsule)
    }

    private var restoreTitle: String {
        if scene.isIsolating { return String(localized: "Yalnız seçilen yapı") }
        var parts: [String] = []
        // Short enough to fit next to "Tümünü göster" on the smallest phones.
        if !scene.highlighted.isEmpty { parts.append(String(localized: "\(scene.highlighted.count) yapı vurgulu")) }
        if !scene.fadedParts.isEmpty { parts.append(String(localized: "önü saydam")) }
        if !scene.hiddenParts.isEmpty { parts.append(String(localized: "\(scene.hiddenParts.count) gizli")) }
        return parts.isEmpty ? String(localized: "Değiştirilmiş görünüm") : parts.joined(separator: " · ")
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
        .frame(maxWidth: .infinity, alignment: .leading)
    }
}

// MARK: - Tool bar buttons

private struct ToolLabel: View {
    let title: String
    let systemImage: String
    var isOn = false
    /// Icons only, in a slimmer bar.
    var compact = false

    var body: some View {
        VStack(spacing: 3) {
            Image(systemName: systemImage)
                .font(.system(size: 17, weight: .semibold))
            if !compact {
                Text(title)
                    .font(.system(size: 10, weight: .semibold))
                    .lineLimit(1)
                    .minimumScaleFactor(0.6)
            }
        }
        .foregroundStyle(isOn ? Theme.accent : Theme.textPrimary)
        .frame(width: compact ? 46 : 57, height: compact ? 40 : 50)
        .background(isOn ? Theme.accent.opacity(0.16) : .clear, in: .capsule)
        .contentShape(.capsule)
    }
}

private struct ToolButton: View {
    let title: String
    let systemImage: String
    var isOn = false
    var compact = false
    let action: () -> Void

    var body: some View {
        Button(action: action) {
            ToolLabel(title: title, systemImage: systemImage, isOn: isOn, compact: compact)
        }
        .buttonStyle(.plain)
        .accessibilityLabel(title)
    }
}

// MARK: - System rail

/// One button per body system along the left edge. Tap shows or hides the
/// system, long press makes it see-through.
private struct SystemRail: View {
    @Environment(AppModel.self) private var app
    let announce: (String) -> Void
    let collapse: () -> Void

    private static let order = ["skeletal", "joints", "muscular", "cardiovascular", "nervous", "visceral", "lymphoid", "regions"]

    var body: some View {
        let scene = app.scene
        VStack(spacing: 6) {
            ForEach(Self.order.compactMap(ModelLayer.layer)) { layer in
                let on = scene.isEnabled(layer.id)
                let ghost = scene.isGhosted(layer.id)
                Button {
                    let enable = !on
                    scene.setLayer(layer.id, enabled: enable)
                    announce(enable ? String(localized: "\(layer.title) açıldı") : String(localized: "\(layer.title) kapandı"))
                } label: {
                    ZStack(alignment: .topTrailing) {
                        Image(systemName: layer.icon)
                            .font(.system(size: 16, weight: .semibold))
                            .foregroundStyle(on ? Color.white : Theme.textTertiary)
                            .frame(width: 42, height: 42)
                            .background {
                                Circle()
                                    .fill(on ? AnyShapeStyle(layer.tint.gradient) : AnyShapeStyle(Color.white.opacity(0.06)))
                                    .opacity(ghost ? 0.45 : 1)
                            }
                            .overlay {
                                if ghost {
                                    Circle().strokeBorder(layer.tint, style: StrokeStyle(lineWidth: 1.5, dash: [3, 3]))
                                }
                            }
                        if scene.loadingLayers.contains(layer.id) {
                            ProgressView().controlSize(.mini).tint(.white).offset(x: 2, y: -2)
                        }
                    }
                    .overlay(alignment: .bottom) {
                        if layer.isBeta {
                            BetaBadge(compact: true).offset(y: 4)
                        }
                    }
                }
                .buttonStyle(.plain)
                .simultaneousGesture(LongPressGesture(minimumDuration: 0.45).onEnded { _ in
                    guard on else { return }
                    scene.setLayer(layer.id, ghosted: !ghost)
                    announce(ghost ? String(localized: "\(layer.title) opak") : String(localized: "\(layer.title) saydam"))
                })
                .accessibilityLabel(layer.isBeta ? "\(layer.title), beta" : layer.title)
                .accessibilityValue(on ? (ghost ? String(localized: "Saydam") : String(localized: "Açık")) : String(localized: "Kapalı"))
                .accessibilityHint("Uzun basarak saydam yapabilirsin")
            }
            Button(action: collapse) {
                Image(systemName: "chevron.left")
                    .font(.system(size: 13, weight: .bold))
                    .foregroundStyle(Theme.textSecondary)
                    .frame(width: 42, height: 30)
                    .contentShape(.rect)
            }
            .buttonStyle(.plain)
            .accessibilityLabel("Menüyü daralt")
        }
        .padding(6)
        .glassEffect(.regular, in: .capsule)
        .sensoryFeedback(.selection, trigger: scene.enabledLayers)
    }
}

/// The folded system rail: one button that shows how many systems are on.
private struct CollapsedRail: View {
    @Environment(AppModel.self) private var app
    let expand: () -> Void

    var body: some View {
        let count = app.scene.enabledLayers.count
        Button(action: expand) {
            ZStack(alignment: .topTrailing) {
                Image(systemName: "square.3.layers.3d")
                    .font(.system(size: 17, weight: .semibold))
                    .foregroundStyle(Theme.textPrimary)
                    .frame(width: 46, height: 46)
                Text("\(count)")
                    .font(.system(size: 10, weight: .heavy).monospacedDigit())
                    .foregroundStyle(.white)
                    .frame(minWidth: 16, minHeight: 16)
                    .background(Theme.accent, in: .circle)
                    .offset(x: 3, y: -3)
            }
        }
        .buttonStyle(.plain)
        .glassEffect(.regular.interactive(), in: .circle)
        .accessibilityLabel("Sistemleri göster")
        .accessibilityValue("\(count) sistem açık")
    }
}

// MARK: - First load and gesture hint

/// Shown until the first layer of the model is on screen.
private struct FirstLoadView: View {
    var body: some View {
        VStack(spacing: 18) {
            Image(systemName: "figure.stand")
                .font(.system(size: 54, weight: .light))
                .foregroundStyle(Theme.accent)
                .symbolEffect(.breathe.pulse, options: .repeating)
                .frame(width: 112, height: 112)
                .glassEffect(.regular, in: .circle)
            VStack(spacing: 6) {
                Text("3B model hazırlanıyor")
                    .font(.headline)
                Text("Binlerce anatomik yapı yükleniyor")
                    .font(.footnote)
                    .foregroundStyle(Theme.textSecondary)
                    .multilineTextAlignment(.center)
            }
            ProgressView()
        }
        .padding(32)
        .accessibilityElement(children: .combine)
    }
}

/// One-time explanation of the gestures.
private struct GestureHint: View {
    let dismiss: () -> Void

    var body: some View {
        VStack(spacing: 18) {
            Text("Modeli keşfet")
                .font(.title3.weight(.bold))
            VStack(alignment: .leading, spacing: 14) {
                hint("hand.draw", String(localized: "Tek parmakla kaydır"), String(localized: "Modeli döndür"))
                hint("hand.pinch", String(localized: "İki parmakla sıkıştır"), String(localized: "Yakınlaştır, uzaklaştır"))
                hint("arrow.up.and.down.and.arrow.left.and.right", String(localized: "İki parmakla sürükle"), String(localized: "Görüntüyü kaydır"))
                hint("hand.tap", String(localized: "Bir yapıya dokun"), String(localized: "Adını ve bilgisini gör"))
                hint("square.3.layers.3d", String(localized: "Soldaki düğmeler"), String(localized: "Sistemleri aç, kapa; uzun bas: saydam"))
            }
            Button("Başla", action: dismiss)
                .buttonStyle(PrimaryButtonStyle())
        }
        .padding(24)
        .frame(maxWidth: 360)
        .background(Theme.surface.opacity(0.96), in: .rect(cornerRadius: 28))
        .overlay { RoundedRectangle(cornerRadius: 28).strokeBorder(Theme.stroke) }
        .padding(24)
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .background(Color.black.opacity(0.35).ignoresSafeArea().onTapGesture(perform: dismiss))
    }

    private func hint(_ icon: String, _ title: String, _ detail: String) -> some View {
        HStack(spacing: 14) {
            Image(systemName: icon)
                .font(.title3)
                .foregroundStyle(Theme.accent)
                .frame(width: 32)
            VStack(alignment: .leading, spacing: 1) {
                Text(title).font(.subheadline.weight(.semibold))
                Text(detail).font(.caption).foregroundStyle(Theme.textSecondary)
            }
        }
    }
}

extension PartRef: Identifiable {
    var id: String { "\(system)#\(index)" }
}

// MARK: - Selection card

/// Bottom card describing the selected part.
private struct SelectionCard: View {
    @Environment(AppModel.self) private var app
    let ref: PartRef
    let info: PartInfo
    let onInfo: () -> Void

    var body: some View {
        let store = app.store
        let layer = ModelLayer.layer(ref.system)
        let locked = !app.isFree(ref)
        let side = info.sideTitle.map { " (\($0))" } ?? ""
        let group = app.scene.selectedGroup
        let levels = self.levels
        let current = levels.firstIndex { $0.refs == group } ?? 0
        let level = levels.indices.contains(current) ? levels[current] : nil
        let wholeGroup = current > 0

        VStack(alignment: .leading, spacing: 12) {
            HStack(alignment: .top, spacing: 12) {
                if let layer {
                    SystemBadge(icon: layer.icon, color: layer.tint, size: 40)
                }
                VStack(alignment: .leading, spacing: 3) {
                    Text(wholeGroup ? (level?.title ?? "") : store.title(for: info) + side)
                        .font(.headline)
                        .foregroundStyle(Theme.textPrimary)
                        .lineLimit(2)
                    let second = wholeGroup ? (level?.subtitle ?? "") : subtitle
                    if !second.isEmpty {
                        Text(second)
                            .font(info.kind == nil ? Theme.secondName(latinFirst: store.latinFirst) : Theme.latin(.subheadline))
                            .foregroundStyle(Theme.textSecondary)
                            .lineLimit(1)
                    }
                    if group.count > 1 {
                        Text(wholeGroup ? String(localized: "\(group.count) parça birlikte seçili") : String(localized: "\(group.count) bölümüyle birlikte seçildi"))
                            .font(.caption)
                            .foregroundStyle(Theme.textTertiary)
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

            if levels.count > 1 {
                // The tapped part or, wider, the structure it belongs to (the
                // frontal bone, the bones of the cranium, the cranium…), on as
                // many lines as needed: every level in sight.
                HStack(spacing: 0) {
                    FlowLayout(spacing: 6) {
                        ForEach(Array(levels.enumerated()), id: \.offset) { index, option in
                            Button {
                                withAnimation(.snappy) { app.scene.selectGroup(option.refs, anchor: ref) }
                            } label: {
                                Text(index == 0 ? option.title : "\(option.title) · \(option.refs.count)")
                                    .font(.caption.weight(.semibold))
                                    .lineLimit(1)
                                    .padding(.horizontal, 11)
                                    .padding(.vertical, 6)
                                    .foregroundStyle(index == current ? Color.white : Theme.textPrimary)
                                    .background(index == current ? AnyShapeStyle(Theme.accentGradient) : AnyShapeStyle(Theme.elevated), in: .capsule)
                            }
                            .buttonStyle(.plain)
                        }
                    }
                    Spacer(minLength: 0)
                }
                .accessibilityLabel("Seçim düzeyi")
            }

            if locked {
                Button {
                    app.requirePremium(.structure(store.displayName(for: info)))
                } label: {
                    HStack(spacing: 10) {
                        LockBadge()
                        VStack(alignment: .leading, spacing: 1) {
                            Text("Bu yapının bilgisi Premium'da")
                                .font(.subheadline.weight(.semibold))
                                .foregroundStyle(Theme.textPrimary)
                            Text("Ücretsiz sürümde iskelet sistemi açık.")
                                .font(.caption)
                                .foregroundStyle(Theme.textSecondary)
                        }
                        Spacer()
                        Image(systemName: "chevron.right").foregroundStyle(Theme.textTertiary)
                    }
                    .padding(12)
                    .background(Theme.gold.opacity(0.1), in: .rect(cornerRadius: 14))
                    .overlay { RoundedRectangle(cornerRadius: 14).strokeBorder(Theme.gold.opacity(0.35)) }
                }
                .buttonStyle(PressableStyle())
            } else if wholeGroup {
                if let text = level?.name.flatMap(store.partDescription) {
                    Text(text)
                        .font(.footnote)
                        .foregroundStyle(Theme.textSecondary)
                        .lineLimit(3)
                        .fixedSize(horizontal: false, vertical: true)
                }
            } else if let summary {
                Text(summary)
                    .font(.footnote)
                    .foregroundStyle(Theme.textSecondary)
                    .lineLimit(3)
                    .fixedSize(horizontal: false, vertical: true)
            }

            HStack(spacing: 8) {
                actionButton("İncele", systemImage: "cube.transparent", prominent: true) {
                    guard app.isFree(ref) || app.requirePremium(.inspection) else { return }
                    let refs = Array(group.isEmpty ? [ref] : group)
                    let entry = wholeGroup ? nil : store.entry(for: info)
                    app.specimen = app.specimenRequest(
                        for: refs,
                        title: wholeGroup ? (level?.title ?? "") : store.title(for: info),
                        subtitle: wholeGroup ? (level?.subtitle ?? "") : store.subtitle(for: info),
                        entryID: entry?.id
                    )
                }
                actionButton("Bilgi", systemImage: "info.circle") {
                    guard app.isFree(ref) || app.requirePremium(.structure(store.displayName(for: info))) else { return }
                    onInfo()
                }
                actionButton("Yalnız", systemImage: "viewfinder") {
                    let refs = group.isEmpty ? [ref] : group
                    app.scene.isolate(refs)
                    app.scene.frame(Array(refs))
                }
                actionButton("Saydam", systemImage: "circle.dashed") {
                    withAnimation(.snappy) { app.scene.toggleFade(group.isEmpty ? [ref] : group) }
                }
                actionButton("Gizle", systemImage: "eye.slash") {
                    withAnimation(.snappy) { app.scene.hide(ref) }
                }
            }
        }
        .padding(16)
        .background(Theme.surface.opacity(0.94), in: .rect(cornerRadius: 26))
        .overlay { RoundedRectangle(cornerRadius: 26).strokeBorder(Theme.stroke) }
        .shadow(color: .black.opacity(0.35), radius: 24, y: 10)
    }

    /// Selection levels: the tapped part (with its own sections), then the
    /// groups it belongs to, nearest first (same side, this body's sex).
    private struct Level {
        let title: String
        /// The other name: the Latin one, or the language's own when Latin leads.
        let subtitle: String
        var name: String? = nil
        let refs: Set<PartRef>
    }

    /// Wider structures that are not one group of the model hierarchy: the
    /// whole skull is the cranium with the bones outside it (mandible, hyoid).
    private static let combined: [String: (groups: [String], title: String, latin: String)] = [
        "Cranium": (["Cranium", "Extracranial bones of head"], String(localized: "Kafatası ve alt çene"), "Ossa capitis"),
    ]

    private var levels: [Level] {
        let scene = app.scene
        let store = app.store
        var base = scene.groupResolver?(ref) ?? [ref]
        base.insert(ref)
        var out = [Level(title: store.title(for: info), subtitle: store.subtitle(for: info), refs: base)]
        var lastCount = base.count
        for name in info.path.dropFirst().reversed() {
            let refs = Set(scene.matchingSex(scene.refs(matching: [name])).filter { other in
                guard other.system == ref.system, let otherInfo = scene.info(other) else { return false }
                return info.side == nil || otherInfo.side == nil || otherInfo.side == info.side
            })
            guard refs.count > lastCount, refs.count <= 150 else { continue }
            out.append(Level(title: store.title(ofGroup: name), subtitle: store.subtitle(ofGroup: name), name: name, refs: refs.union([ref])))
            lastCount = refs.count
            if out.count == 3 { break }
        }
        for name in info.path {
            guard let wider = Self.combined[name] else { continue }
            let refs = Set(scene.matchingSex(scene.refs(matching: wider.groups)).filter { $0.system == ref.system })
            if refs.count > lastCount {
                out.append(store.latinFirst ? Level(title: wider.latin, subtitle: wider.title, refs: refs.union([ref]))
                                            : Level(title: wider.title, subtitle: wider.latin, refs: refs.union([ref])))
            }
        }
        return out
    }

    private var subtitle: String {
        if let kind = info.kind { return kind == "origin" ? String(localized: "Kasın başlangıç yeri (origo)") : String(localized: "Kasın tutunma yeri (insersiyo)") }
        return app.store.subtitle(for: info)
    }

    private var summary: String? {
        if let d = app.store.partDescription(info.base) { return d }
        if let entry = app.store.entry(for: info), app.store.isExact(entry, for: info) { return entry.summary }
        return app.store.partDescription(info.path.last ?? "")
    }

    private func actionButton(_ title: LocalizedStringKey, systemImage: String, prominent: Bool = false, action: @escaping () -> Void) -> some View {
        Button(action: action) {
            VStack(spacing: 4) {
                Image(systemName: systemImage)
                    .font(.system(size: 16, weight: .semibold))
                Text(title)
                    .font(.caption2.weight(.semibold))
                    // German labels ("Ausblenden") are wider than the button.
                    .lineLimit(1)
                    .minimumScaleFactor(0.7)
            }
            .frame(maxWidth: .infinity)
            .padding(.horizontal, 2)
            .padding(.vertical, 9)
            .foregroundStyle(prominent ? Color.white : Theme.textPrimary)
            .background(prominent ? AnyShapeStyle(Theme.accentGradient) : AnyShapeStyle(Theme.elevated), in: .rect(cornerRadius: 14))
        }
        .buttonStyle(PressableStyle())
    }
}
