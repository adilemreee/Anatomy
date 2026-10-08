//
//  LibraryView.swift
//  Anatomy
//

import SwiftUI

/// Favourites, history, progress per system and credits.
struct LibraryView: View {
    @Environment(AppModel.self) private var app
    @State private var confirmReset = false

    var body: some View {
        NavigationStack {
            List {
                Section("İlerleme") {
                    ForEach(app.store.systems) { system in
                        let ids = app.store.entries(in: system.id).map(\.id)
                        let mastery = app.study.mastery(of: ids)
                        let seen = ids.filter { app.study.score($0).seen > 0 }.count
                        NavigationLink(value: system) {
                            HStack(spacing: 12) {
                                SystemBadge(icon: system.icon, color: system.tint, size: 32)
                                VStack(alignment: .leading, spacing: 2) {
                                    Text(system.tr).font(.subheadline.weight(.medium))
                                    Text("\(seen)/\(ids.count) yapı çalışıldı")
                                        .font(.caption)
                                        .foregroundStyle(.secondary)
                                }
                                Spacer()
                                ZStack {
                                    ProgressRing(value: mastery, color: system.tint, lineWidth: 4)
                                    Text("\(Int(mastery * 100))")
                                        .font(.caption2.weight(.bold))
                                }
                                .frame(width: 34, height: 34)
                            }
                        }
                    }
                }

                Section("Favoriler") {
                    let favorites = app.study.favorites.compactMap(app.store.entry)
                    if favorites.isEmpty {
                        Label("Bir maddeyi yıldızlayarak buraya ekleyebilirsin.", systemImage: "star")
                            .foregroundStyle(.secondary)
                    }
                    ForEach(favorites) { entry in
                        NavigationLink(value: entry) {
                            EntryRow(entry: entry, tint: app.store.system(entry.systemID)?.tint ?? .accentColor)
                        }
                    }
                    .onDelete { offsets in
                        for i in offsets { app.study.toggleFavorite(favorites[i].id) }
                    }
                }

                Section {
                    let recents = app.study.recents.compactMap(app.store.entry)
                    if recents.isEmpty {
                        Label("Henüz bir madde görüntülemedin.", systemImage: "clock")
                            .foregroundStyle(.secondary)
                    }
                    ForEach(recents.prefix(15)) { entry in
                        NavigationLink(value: entry) {
                            EntryRow(entry: entry, tint: app.store.system(entry.systemID)?.tint ?? .accentColor)
                        }
                    }
                } header: {
                    HStack {
                        Text("Son bakılanlar")
                        Spacer()
                        if !app.study.recents.isEmpty {
                            Button("Temizle") { app.study.clearRecents() }
                                .font(.caption)
                        }
                    }
                }

                Section {
                    NavigationLink {
                        AboutView()
                    } label: {
                        Label("Hakkında ve kaynaklar", systemImage: "info.circle")
                    }
                    Button(role: .destructive) {
                        confirmReset = true
                    } label: {
                        Label("İlerlemeyi sıfırla", systemImage: "arrow.counterclockwise")
                    }
                }
            }
            .navigationTitle("Kitaplığım")
            .navigationDestination(for: BodySystem.self) { SystemDetailView(system: $0) }
            .navigationDestination(for: AtlasEntry.self) { EntryDetailView(entry: $0) }
            .confirmationDialog("Tüm test sonuçların ve serin silinecek.", isPresented: $confirmReset, titleVisibility: .visible) {
                Button("İlerlemeyi sıfırla", role: .destructive) { app.study.resetProgress() }
            }
        }
    }
}

struct AboutView: View {
    @Environment(AppModel.self) private var app

    var body: some View {
        List {
            Section {
                VStack(alignment: .leading, spacing: 8) {
                    Text("Anatomi Atlası")
                        .font(.title2.weight(.bold))
                    Text("Etkileşimli 3D insan anatomisi atlası: \(app.store.entries.count) Türkçe madde, \(partCount) üç boyutlu yapı.")
                        .foregroundStyle(.secondary)
                }
                .padding(.vertical, 4)
            }

            Section("3D modeller") {
                VStack(alignment: .leading, spacing: 6) {
                    Text("Z-Anatomy")
                        .font(.headline)
                    Text("3D modeller ve İngilizce kaynak metinler Z-Anatomy projesinden alınmıştır (Creative Commons Atıf-AynıLisanslaPaylaş 4.0, CC BY-SA 4.0). Modeller bu uygulama için sadeleştirilmiş, yeniden renklendirilmiş ve sistemlere ayrılmıştır; değiştirilmiş modeller de aynı lisansla sunulur.")
                        .font(.subheadline)
                    Link("github.com/Z-Anatomy", destination: URL(string: "https://github.com/Z-Anatomy/Models-of-human-anatomy")!)
                        .font(.subheadline)
                }
                VStack(alignment: .leading, spacing: 6) {
                    Text("BodyParts3D")
                        .font(.headline)
                    Text("Z-Anatomy modelleri BodyParts3D veritabanından türetilmiştir. İnceleme modundaki yüksek ayrıntılı kemik ve organ modelleri BodyParts3D 3.0 (%95 seti) verisinden hazırlanmış, Z-Anatomy modeline hizalanmıştır. BodyParts3D, © The Database Center for Life Science (DBCLS), Creative Commons Atıf-AynıLisanslaPaylaş 2.1 Japonya (CC BY-SA 2.1 JP).")
                        .font(.subheadline)
                    Link("dbarchive.biosciencedbc.jp/en/bodyparts3d", destination: URL(string: "https://dbarchive.biosciencedbc.jp/en/bodyparts3d/")!)
                        .font(.subheadline)
                }
            }

            Section("Terminoloji ve metinler") {
                Text("Latince terimler Terminologia Anatomica 2 (FIPAT) listesine dayanır. İngilizce kaynak metinler Wikipedia tabanlıdır (CC BY-SA). Türkçe içerik bu uygulama için hazırlanmıştır.")
                    .font(.subheadline)
            }

            Section("Uyarı") {
                Text("Bu uygulama eğitim amaçlıdır; tıbbi tanı veya tedavi için kullanılmamalıdır. Klinik kararlar için güncel kaynaklara ve uzman görüşüne başvurun.")
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
            }
        }
        .navigationTitle("Hakkında")
        .navigationBarTitleDisplayMode(.inline)
    }

    private var partCount: Int {
        app.scene.manifests.values.reduce(0) { $0 + $1.count }
    }
}
