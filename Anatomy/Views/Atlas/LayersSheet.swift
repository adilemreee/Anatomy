//
//  LayersSheet.swift
//  Anatomy
//

import SwiftUI

/// Turns body-system layers on/off and makes them see-through.
struct LayersSheet: View {
    @Environment(AppModel.self) private var app
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        @Bindable var scene = app.scene
        @Bindable var app = app
        NavigationStack {
            List {
                Section {
                    ForEach(ModelLayer.all) { layer in
                        LayerRow(layer: layer)
                    }
                } header: {
                    Text("Sistemler")
                } footer: {
                    Text("Saydam yaptığın katmanın içinden alttaki yapılara dokunabilirsin.")
                }
                .listRowBackground(Theme.card)

                Section {
                    Picker("Üreme organları", selection: Binding(get: { app.sex }, set: { newValue in
                        if newValue == .female, !app.requirePremium(.femaleAnatomy) { return }
                        app.sex = newValue
                    })) {
                        ForEach(BodySex.allCases) { Text($0.title).tag($0) }
                    }
                    .pickerStyle(.segmented)
                } header: {
                    Text("Anatomi")
                } footer: {
                    Text("Kadın görünümünde rahim, yumurtalıklar ve fallop tüpleri gösterilir; iskelet ve diğer sistemler aynı kalır.")
                }
                .listRowBackground(Theme.card)

                Section {
                    Picker("Renkler", selection: $app.colorMode) {
                        ForEach(ColorMode.allCases) { Text($0.title).tag($0) }
                    }
                    .pickerStyle(.segmented)
                    .listRowSeparator(.hidden)
                    if app.colorMode == .educational {
                        ColorLegend(title: "Kaslar: hareketine göre", items: MaterialStyles.muscleLegend)
                        ColorLegend(title: "Beyin: loblar", items: MaterialStyles.brainLegend)
                    }
                } header: {
                    Text("Renkler")
                } footer: {
                    Text(app.colorMode == .realistic
                         ? "Dokular kadavradaki gerçek renklerine yakın gösterilir."
                         : "Kaslar yaptıkları harekete, kemikler ve beyin lobları tek tek ayırt edilecek şekilde renklendirilir.")
                }
                .listRowBackground(Theme.card)

                Section("Görünüm") {
                    Toggle(isOn: $scene.xray) {
                        Label("Röntgen görünümü", systemImage: "circle.lefthalf.filled")
                    }
                    Toggle(isOn: $scene.showCoverings) {
                        Label {
                            VStack(alignment: .leading, spacing: 2) {
                                Text("Örtü dokularını göster")
                                Text("Fasyalar, plevra, periton ve beyin zarları")
                                    .font(.caption)
                                    .foregroundStyle(.secondary)
                            }
                        } icon: {
                            Image(systemName: "square.stack.3d.down.forward")
                        }
                    }
                    Button {
                        scene.showAll()
                        scene.highlight([])
                    } label: {
                        Label("Gizlenen tüm parçaları göster", systemImage: "eye")
                    }
                    .disabled(scene.hiddenParts.isEmpty && !scene.isIsolating && scene.highlighted.isEmpty)
                }
                .listRowBackground(Theme.card)

                Section("Hazır görünümler") {
                    preset("Sadece iskelet", icon: "figure.stand", layers: ["skeletal"])
                    preset("Kaslar ve iskelet", icon: "figure.strengthtraining.traditional", layers: ["skeletal", "muscular"])
                    preset("İç organlar", icon: "lungs.fill", layers: ["skeletal", "visceral"], ghost: ["skeletal"])
                    preset("Dolaşım sistemi", icon: "heart.fill", layers: ["skeletal", "cardiovascular"], ghost: ["skeletal"])
                    preset("Sinir sistemi", icon: "brain.head.profile.fill", layers: ["skeletal", "nervous"], ghost: ["skeletal"])
                    preset("Eklemler ve bağlar", icon: "figure.flexibility", layers: ["skeletal", "joints"])
                    preset("Kas yapışma yerleri", icon: "pin.fill", layers: ["skeletal", "insertions"])
                }
                .listRowBackground(Theme.card)
            }
            .scrollContentBackground(.hidden)
            .background(Theme.surface.ignoresSafeArea())
            .navigationTitle("Katmanlar")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .confirmationAction) {
                    Button("Bitti") { dismiss() }
                }
            }
        }
    }

    private func preset(_ title: String, icon: String, layers: Set<String>, ghost: Set<String> = []) -> some View {
        Button {
            let scene = app.scene
            for layer in ModelLayer.all {
                scene.setLayer(layer.id, ghosted: ghost.contains(layer.id))
                scene.setLayer(layer.id, enabled: layers.contains(layer.id))
            }
            scene.xray = false
        } label: {
            Label(title, systemImage: icon)
        }
    }
}

private struct LayerRow: View {
    @Environment(AppModel.self) private var app
    let layer: ModelLayer

    var body: some View {
        let scene = app.scene
        let on = scene.isEnabled(layer.id)
        HStack(spacing: 12) {
            SystemBadge(icon: layer.icon, color: layer.tint, size: 34)
            VStack(alignment: .leading, spacing: 2) {
                Text(layer.title)
                    .font(.body.weight(.medium))
                Group {
                    if scene.loadingLayers.contains(layer.id) {
                        Text("Yükleniyor…")
                    } else if let error = scene.failedLayers[layer.id] {
                        Text("Yüklenemedi: \(error)").foregroundStyle(.red)
                    } else {
                        Text("\(scene.manifests[layer.id]?.count ?? 0) parça")
                    }
                }
                .font(.caption)
                .foregroundStyle(.secondary)
            }
            Spacer()
            if on {
                Button {
                    scene.setLayer(layer.id, ghosted: !scene.isGhosted(layer.id))
                } label: {
                    Image(systemName: scene.isGhosted(layer.id) ? "circle.dashed" : "circle.fill")
                        .font(.title3)
                        .foregroundStyle(layer.tint)
                }
                .buttonStyle(.borderless)
                .accessibilityLabel(scene.isGhosted(layer.id) ? "Opak yap" : "Saydam yap")
            }
            Toggle("", isOn: Binding(
                get: { scene.isEnabled(layer.id) },
                set: { scene.setLayer(layer.id, enabled: $0) }
            ))
            .labelsHidden()
        }
    }
}

/// Colour key for the teaching colours.
private struct ColorLegend: View {
    let title: String
    let items: [(material: String, title: String)]
    @State private var expanded = false

    var body: some View {
        DisclosureGroup(isExpanded: $expanded) {
            LazyVGrid(columns: [GridItem(.adaptive(minimum: 150), alignment: .leading)], alignment: .leading, spacing: 8) {
                ForEach(items, id: \.material) { item in
                    HStack(spacing: 8) {
                        RoundedRectangle(cornerRadius: 4)
                            .fill(MaterialStyles.legendColor(item.material))
                            .frame(width: 16, height: 16)
                            .overlay { RoundedRectangle(cornerRadius: 4).strokeBorder(.black.opacity(0.12)) }
                        Text(item.title)
                            .font(.footnote)
                            .lineLimit(1)
                            .minimumScaleFactor(0.8)
                    }
                }
            }
            .padding(.vertical, 4)
        } label: {
            Text(title).font(.subheadline.weight(.medium))
        }
    }
}
