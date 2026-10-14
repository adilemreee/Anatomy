//
//  LibraryView.swift
//  Anatomy
//

import StoreKit
import SwiftUI

/// The Profile tab: Premium status, progress, favourites, history,
/// settings and credits.
struct LibraryView: View {
    @Environment(AppModel.self) private var app
    @Environment(\.openURL) private var openURL
    @State private var confirmReset = false
    @State private var manageSubscriptions = false
    @AppStorage("profile.level") private var level = "faculty"
    @AppStorage("study.dailyGoal") private var dailyGoal = 20
    @AppStorage("atlas.focusOnTap") private var focusOnTap = true
    @AppStorage("atlas.compact") private var compactAtlas = false

    var body: some View {
        @Bindable var app = app
        NavigationStack {
            List {
                Section {
                    premiumCard
                        .listRowInsets(EdgeInsets())
                        .listRowBackground(Color.clear)
                }

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
                                        .foregroundStyle(Theme.textSecondary)
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
                .listRowBackground(Theme.card)

                Section("Ayarlar") {
                    Picker(selection: $app.colorMode) {
                        ForEach(ColorMode.allCases) { Text($0.title).tag($0) }
                    } label: {
                        Label("Model renkleri", systemImage: "paintpalette")
                    }
                    Picker(selection: Binding(get: { app.sex }, set: { newValue in
                        if newValue == .female, !app.requirePremium(.femaleAnatomy) { return }
                        app.sex = newValue
                    })) {
                        ForEach(BodySex.allCases) { Text($0.title).tag($0) }
                    } label: {
                        Label("Üreme organları", systemImage: "figure.dress.line.vertical.figure")
                    }
                    Picker(selection: $level) {
                        Text("Tıp fakültesi").tag("faculty")
                        Text("TUS hazırlığı").tag("tus")
                        Text("Diş hekimliği").tag("dentistry")
                        Text("Diğer sağlık bölümleri").tag("health")
                    } label: {
                        Label("Çalışma düzeyi", systemImage: "graduationcap")
                    }
                    Stepper(value: $dailyGoal, in: 10...100, step: 10) {
                        Label("Günlük hedef: \(dailyGoal) soru", systemImage: "flag.checkered")
                    }
                    Toggle(isOn: $focusOnTap) {
                        Label("Seçilen yapıya yaklaş", systemImage: "scope")
                    }
                    .tint(Theme.accent)
                    Toggle(isOn: $compactAtlas) {
                        Label("Sade atlas görünümü", systemImage: "rectangle.compress.vertical")
                    }
                    .tint(Theme.accent)
                }
                .listRowBackground(Theme.card)

                Section("Favoriler") {
                    let favorites = app.study.favorites.compactMap(app.store.entry)
                    if favorites.isEmpty {
                        Label("Bir maddeyi yıldızlayarak buraya ekleyebilirsin.", systemImage: "star")
                            .foregroundStyle(Theme.textSecondary)
                    }
                    ForEach(favorites) { entry in
                        NavigationLink(value: entry) {
                            EntryRow(entry: entry, tint: app.store.system(entry.systemID)?.tint ?? Theme.accent, locked: !app.isFree(entry), chevron: false)
                        }
                    }
                    .onDelete { offsets in
                        for i in offsets { app.study.toggleFavorite(favorites[i].id) }
                    }
                }
                .listRowBackground(Theme.card)

                Section {
                    let recents = app.study.recents.compactMap(app.store.entry)
                    if recents.isEmpty {
                        Label("Henüz bir madde görüntülemedin.", systemImage: "clock")
                            .foregroundStyle(Theme.textSecondary)
                    }
                    ForEach(recents.prefix(10)) { entry in
                        NavigationLink(value: entry) {
                            EntryRow(entry: entry, tint: app.store.system(entry.systemID)?.tint ?? Theme.accent, locked: !app.isFree(entry), chevron: false)
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
                .listRowBackground(Theme.card)

                Section("Uygulama") {
                    NavigationLink {
                        AboutView()
                    } label: {
                        Label("Hakkında ve kaynaklar", systemImage: "info.circle")
                    }
                    Button {
                        Task { await app.purchases.restore() }
                    } label: {
                        Label("Satın alımları geri yükle", systemImage: "arrow.clockwise")
                    }
                    Button {
                        openURL(Legal.privacy)
                    } label: {
                        Label("Gizlilik politikası", systemImage: "hand.raised")
                    }
                    Button {
                        openURL(Legal.terms)
                    } label: {
                        Label("Kullanım koşulları", systemImage: "doc.text")
                    }
                    Button(role: .destructive) {
                        confirmReset = true
                    } label: {
                        Label("İlerlemeyi sıfırla", systemImage: "arrow.counterclockwise")
                    }
                }
                .listRowBackground(Theme.card)
            }
            .scrollContentBackground(.hidden)
            .themedBackground()
            .navigationTitle("Profil")
            .navigationDestination(for: BodySystem.self) { SystemDetailView(system: $0) }
            .navigationDestination(for: AtlasEntry.self) { EntryDetailView(entry: $0) }
            .confirmationDialog("Tüm test sonuçların ve serin silinecek.", isPresented: $confirmReset, titleVisibility: .visible) {
                Button("İlerlemeyi sıfırla", role: .destructive) { app.study.resetProgress() }
            }
            .manageSubscriptionsSheet(isPresented: $manageSubscriptions)
        }
    }

    @ViewBuilder
    private var premiumCard: some View {
        if app.isPremium {
            HStack(spacing: 14) {
                Image(systemName: "crown.fill")
                    .font(.title2)
                    .foregroundStyle(Theme.goldGradient)
                    .frame(width: 48, height: 48)
                    .background(Theme.gold.opacity(0.14), in: .circle)
                VStack(alignment: .leading, spacing: 2) {
                    Text("Premium aktif").font(.headline).foregroundStyle(Theme.textPrimary)
                    Text(app.purchases.activePlan.map { "\($0.title) plan" } ?? "Tüm içerik açık")
                        .font(.caption)
                        .foregroundStyle(Theme.textSecondary)
                }
                Spacer()
                if app.purchases.activePlan == .monthly || app.purchases.activePlan == .yearly {
                    Button("Yönet") { manageSubscriptions = true }
                        .font(.subheadline.weight(.semibold))
                        .foregroundStyle(Theme.gold)
                }
            }
            .padding(16)
            .background(Theme.card, in: .rect(cornerRadius: 20))
            .overlay { RoundedRectangle(cornerRadius: 20).strokeBorder(Theme.gold.opacity(0.4)) }
        } else {
            Button {
                app.requirePremium(.general)
            } label: {
                VStack(alignment: .leading, spacing: 10) {
                    PremiumBadge()
                    Text("Tüm sistemleri, inceleme modunu ve soru bankasını aç")
                        .font(.title3.weight(.bold))
                        .foregroundStyle(Color(hex: "2A1D05"))
                        .multilineTextAlignment(.leading)
                    HStack {
                        Text(app.purchases.trialText(.yearly).map { "\($0) dene" } ?? "Premium'a geç")
                            .font(.subheadline.weight(.semibold))
                        Image(systemName: "arrow.right")
                    }
                    .foregroundStyle(Color(hex: "2A1D05"))
                }
                .padding(18)
                .frame(maxWidth: .infinity, alignment: .leading)
                .background(Theme.goldGradient, in: .rect(cornerRadius: 22))
            }
            .buttonStyle(PressableStyle())
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
                        .foregroundStyle(Theme.textSecondary)
                }
                .padding(.vertical, 4)
            }

            Section("3D modeller") {
                credit("Z-Anatomy",
                       "3D modeller ve İngilizce kaynak metinler Z-Anatomy projesinden alınmıştır (Creative Commons Atıf-AynıLisanslaPaylaş 4.0, CC BY-SA 4.0). Modeller bu uygulama için sadeleştirilmiş, yeniden renklendirilmiş ve sistemlere ayrılmıştır; değiştirilmiş modeller de aynı lisansla sunulur.",
                       "github.com/Z-Anatomy", "https://github.com/Z-Anatomy/Models-of-human-anatomy")
                credit("BodyParts3D",
                       "Z-Anatomy modelleri BodyParts3D veritabanından türetilmiştir. Karaciğer, mide, bağırsaklar, akciğer lobları, böbrekler ve diğer organlar ile inceleme modundaki yüksek ayrıntılı modeller BodyParts3D 3.0 verisinden hazırlanıp atlasa hizalanmıştır. BodyParts3D, © The Database Center for Life Science (DBCLS), Creative Commons Atıf-AynıLisanslaPaylaş 2.1 Japonya (CC BY-SA 2.1 JP).",
                       "dbarchive.biosciencedbc.jp/en/bodyparts3d", "https://dbarchive.biosciencedbc.jp/en/bodyparts3d/")
                credit("Human Reference Atlas (HuBMAP)",
                       "Rahim, yumurtalıklar, fallop tüpleri, kadın mesanesi ve meme bezi Human Reference Atlas 3D referans organlarından (Visible Human Female, NIH) alınmış ve atlasa hizalanmıştır. Creative Commons Atıf 4.0 (CC BY 4.0).",
                       "humanatlas.io", "https://humanatlas.io/3d-reference-library")
                credit("meshoptimizer",
                       "Modellerin uzaklığa göre sadeleştirilmiş detay seviyeleri meshoptimizer ile üretilmiştir. © Arseny Kapoulkine, MIT lisansı.",
                       "github.com/zeux/meshoptimizer", "https://github.com/zeux/meshoptimizer")
            }
            .listRowBackground(Theme.card)

            Section("Terminoloji ve metinler") {
                Text("Latince terimler Terminologia Anatomica 2 (FIPAT) listesine dayanır; terimlerin kendisi kamu malıdır. İngilizce kaynak metinler Wikipedia tabanlıdır (CC BY-SA). Türkçe maddeler, parça açıklamaları ve sorular bu uygulama için özgün olarak hazırlanmıştır.")
                    .font(.subheadline)
            }
            .listRowBackground(Theme.card)

            Section("Uyarı") {
                Text("Bu uygulama eğitim amaçlıdır; tıbbi tanı veya tedavi için kullanılmamalıdır. Klinik kararlar için güncel kaynaklara ve uzman görüşüne başvurun.")
                    .font(.subheadline)
                    .foregroundStyle(Theme.textSecondary)
            }
            .listRowBackground(Theme.card)
        }
        .scrollContentBackground(.hidden)
        .themedBackground()
        .navigationTitle("Hakkında")
        .navigationBarTitleDisplayMode(.inline)
    }

    private func credit(_ title: String, _ text: String, _ linkTitle: String, _ url: String) -> some View {
        VStack(alignment: .leading, spacing: 6) {
            Text(title)
                .font(.headline)
            Text(text)
                .font(.subheadline)
                .foregroundStyle(Theme.textSecondary)
            Link(linkTitle, destination: URL(string: url)!)
                .font(.subheadline)
        }
        .padding(.vertical, 4)
    }

    private var partCount: Int {
        app.scene.manifests.values.reduce(0) { $0 + $1.count }
    }
}
