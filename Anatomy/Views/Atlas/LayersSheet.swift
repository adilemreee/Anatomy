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

                Section("Hazır görünümler") {
                    preset("Sadece iskelet", icon: "figure.stand", layers: ["skeletal"])
                    preset("Kaslar ve iskelet", icon: "figure.strengthtraining.traditional", layers: ["skeletal", "muscular"])
                    preset("İç organlar", icon: "lungs.fill", layers: ["skeletal", "visceral"], ghost: ["skeletal"])
                    preset("Dolaşım sistemi", icon: "heart.fill", layers: ["skeletal", "cardiovascular"], ghost: ["skeletal"])
                    preset("Sinir sistemi", icon: "brain.head.profile.fill", layers: ["skeletal", "nervous"], ghost: ["skeletal"])
                    preset("Eklemler ve bağlar", icon: "figure.flexibility", layers: ["skeletal", "joints"])
                    preset("Kas yapışma yerleri", icon: "pin.fill", layers: ["skeletal", "insertions"])
                }
            }
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
