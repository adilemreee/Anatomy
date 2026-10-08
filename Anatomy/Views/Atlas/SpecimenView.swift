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
                if showLabels, !scene.isCameraMoving {
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
                if let label = labels.first(where: { $0.id == focused }) {
                    FeatureCard(label: label, definition: app.store.term(label.name)?.def) {
                        withAnimation(.snappy) { focused = nil }
                    }
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
            let result = await scene.labels(in: size, top: headerBottom + 10, bottom: controlsTop - 12) { store.term($0)?.la }
            guard !Task.isCancelled else { return }
            withAnimation(.easeOut(duration: 0.25)) {
                labels = result
                if let focused, !result.contains(where: { $0.id == focused }) { self.focused = nil }
            }
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
                .environment(\.colorScheme, .light)
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
                Text(request.subtitle)
                    .font(.subheadline.italic())
                    .foregroundStyle(.white.opacity(0.7))
                if scene.hasAttachments {
                    HStack(spacing: 12) {
                        legendDot(.origin, "Başlangıç yeri")
                        legendDot(.insertion, "Tutunma yeri")
                    }
                    .padding(.top, 4)
                } else if scene.featureCount > 0 {
                    Text("\(scene.featureCount) işaretli oluşum")
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
            HStack(spacing: 10) {
                HStack(spacing: 2) {
                    turnButton("Ön", 0)
                    turnButton("Sol", .pi / 2)
                    turnButton("Arka", .pi)
                    turnButton("Sağ", -.pi / 2)
                }
                .padding(4)
                .glassEffect(.regular, in: .capsule)
                GlassIconButton(systemImage: "tag", isOn: showLabels, label: "Etiketler") {
                    withAnimation(.snappy) { showLabels.toggle() }
                }
                if request.entryID != nil {
                    GlassIconButton(systemImage: "book", label: "Madde") { showEntry = true }
                }
            }
        }
    }

    private func turnButton(_ title: String, _ yaw: Float) -> some View {
        Button {
            scene.turn(to: yaw)
        } label: {
            Text(title)
                .font(.subheadline.weight(.semibold))
                .padding(.horizontal, 11)
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
                    path.move(to: label.attach)
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
                } label: {
                    VStack(alignment: .leading, spacing: 1) {
                        Text(label.title)
                            .font(.caption.weight(.semibold))
                            .foregroundStyle(.white)
                            .lineLimit(2)
                            .minimumScaleFactor(0.75)
                        if let subtitle = label.subtitle {
                            Text(subtitle)
                                .font(.caption2.italic())
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

/// Details for the focused feature label.
private struct FeatureCard: View {
    let label: SpecimenScene.Label
    let definition: String?
    let close: () -> Void

    var body: some View {
        VStack(alignment: .leading, spacing: 6) {
            HStack(alignment: .firstTextBaseline) {
                VStack(alignment: .leading, spacing: 2) {
                    Text(label.title)
                        .font(.headline)
                    if let subtitle = label.subtitle {
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
            if let text = summary {
                Text(text)
                    .font(.footnote)
                    .foregroundStyle(.secondary)
                    .lineLimit(5)
                    .fixedSize(horizontal: false, vertical: true)
                Text("Kaynak: Z-Anatomy (Wikipedia tabanlı), CC BY-SA 4.0")
                    .font(.caption2)
                    .foregroundStyle(.tertiary)
            }
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
