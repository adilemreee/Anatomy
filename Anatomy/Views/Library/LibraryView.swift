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
    @AppStorage(ReviewReminder.enabledKey) private var reminder = false
    @AppStorage(ReviewReminder.timeKey) private var reminderMinutes = ReviewReminder.defaultMinutes
    @State private var notificationsDenied = false

    /// The reminder time as today's date at that time, for the picker.
    private var reminderTime: Date {
        Calendar.current.date(byAdding: .minute, value: reminderMinutes, to: Calendar.current.startOfDay(for: .now)) ?? .now
    }

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
                        Label("Model", systemImage: "figure.dress.line.vertical.figure")
                    }
                    Toggle(isOn: Binding(get: { app.store.latinFirst }, set: { app.store.latinFirst = $0 })) {
                        Label("Latince adlar önde", systemImage: "character.book.closed")
                    }
                    .tint(Theme.accent)
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
                    Toggle(isOn: Binding(get: { reminder }, set: { on in
                        guard on else {
                            reminder = false
                            app.scheduleReminders()
                            return
                        }
                        Task {
                            if await ReviewReminder.requestPermission() {
                                reminder = true
                                app.scheduleReminders()
                            } else {
                                notificationsDenied = true
                            }
                        }
                    })) {
                        Label("Günlük tekrar hatırlatması", systemImage: "bell.badge")
                    }
                    .tint(Theme.accent)
                    if reminder {
                        DatePicker(selection: Binding(get: { reminderTime }, set: { date in
                            let parts = Calendar.current.dateComponents([.hour, .minute], from: date)
                            reminderMinutes = (parts.hour ?? 20) * 60 + (parts.minute ?? 0)
                            app.scheduleReminders()
                        }), displayedComponents: .hourAndMinute) {
                            Label("Hatırlatma saati", systemImage: "clock")
                        }
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

                .alert("Bildirimler kapalı", isPresented: $notificationsDenied) {
                    Button("Ayarları aç") {
                        if let url = URL(string: UIApplication.openNotificationSettingsURLString) { openURL(url) }
                    }
                    Button("Vazgeç", role: .cancel) {}
                } message: {
                    Text("Hatırlatma gönderebilmemiz için Ayarlar'dan Anatomi Atlası'nın bildirimlerine izin ver.")
                }

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
                    if let review = Legal.review {
                        Button {
                            openURL(review)
                        } label: {
                            Label("Uygulamayı puanla", systemImage: "star.bubble")
                        }
                    }
                    Button {
                        openURL(Legal.support)
                    } label: {
                        Label("Destek", systemImage: "questionmark.circle")
                    }
                    // Crash and performance reports MetricKit gave the app, if any.
                    let reports = Diagnostics.reports
                    if !reports.isEmpty {
                        ShareLink(items: reports, subject: Text("Anatomi Atlası tanılama raporları"),
                                  message: Text("Alıcı: destek@adilemree.xyz")) {
                            Label("Tanılama raporlarını gönder", systemImage: "stethoscope")
                        }
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

    /// Corner radius of an inset-grouped list section.
    private static let sectionRadius: CGFloat = 26

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
                    Text(app.purchases.activePlan.map { String(localized: "\($0.title) plan") } ?? String(localized: "Tüm içerik açık"))
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
            // The list clips its sections to its own corner radius; the card
            // uses the same one so the gold border is not cut at the corners.
            .background(Theme.card, in: .rect(cornerRadius: Self.sectionRadius, style: .continuous))
            .overlay {
                RoundedRectangle(cornerRadius: Self.sectionRadius, style: .continuous)
                    .strokeBorder(Theme.gold.opacity(0.4))
            }
        } else {
            Button {
                app.requirePremium(.general)
            } label: {
                VStack(alignment: .leading, spacing: 10) {
                    PremiumBadge()
                    Text("Eklemleri, kasları, inceleme modunu ve soru bankasını aç")
                        .font(.title3.weight(.bold))
                        .foregroundStyle(Color(hex: "2A1D05"))
                        .multilineTextAlignment(.leading)
                    HStack {
                        Text(app.purchases.trialText(.yearly).map { String(localized: "\($0) dene") } ?? String(localized: "Premium'a geç"))
                            .font(.subheadline.weight(.semibold))
                        Image(systemName: "arrow.right")
                    }
                    .foregroundStyle(Color(hex: "2A1D05"))
                }
                .padding(18)
                .frame(maxWidth: .infinity, alignment: .leading)
                .background(Theme.goldGradient, in: .rect(cornerRadius: Self.sectionRadius, style: .continuous))
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
                    Text("Etkileşimli 3D kas-iskelet atlası: \(app.store.entries.count) ayrıntılı madde, \(partCount) üç boyutlu yapı.")
                        .foregroundStyle(Theme.textSecondary)
                }
                .padding(.vertical, 4)
            }

            Section("3D modeller") {
                credit("Z-Anatomy",
                       String(localized: "3D modeller ve İngilizce kaynak metinler Z-Anatomy projesinden alınmıştır (Creative Commons Atıf-AynıLisanslaPaylaş 4.0, CC BY-SA 4.0). Modeller bu uygulama için sadeleştirilmiş, yeniden renklendirilmiş ve sistemlere ayrılmıştır; değiştirilmiş modeller de aynı lisansla sunulur."),
                       "github.com/Z-Anatomy", "https://github.com/Z-Anatomy/Models-of-human-anatomy")
                credit("BodyParts3D",
                       String(localized: "Z-Anatomy modelleri BodyParts3D veritabanından türetilmiştir. Deri, karaciğer, mide, bağırsaklar, akciğer lobları, böbrekler ve diğer organlar ile yüksek ayrıntılı kemikler BodyParts3D 3.0 verisinden hazırlanıp atlasa hizalanmıştır. BodyParts3D, © The Database Center for Life Science (DBCLS), Creative Commons Atıf-AynıLisanslaPaylaş 2.1 Japonya (CC BY-SA 2.1 JP)."),
                       "dbarchive.biosciencedbc.jp/en/bodyparts3d", "https://dbarchive.biosciencedbc.jp/en/bodyparts3d/")
                credit("Human Reference Atlas (HuBMAP)",
                       String(localized: "Rahim, yumurtalıklar, fallop tüpleri, kadın mesanesi ve meme bezi Human Reference Atlas 3D referans organlarından (Visible Human Female, NIH) alınmış ve atlasa hizalanmıştır. Creative Commons Atıf 4.0 (CC BY 4.0)."),
                       "humanatlas.io", "https://humanatlas.io/3d-reference-library")
                credit("MakeHuman",
                       String(localized: "Kadın modelinin beden biçimi (göğüs ve kasık dahil) MakeHuman'ın CC0 (kamu malı) taban modelinden alınmıştır; iskelet, kas, organlar ve deri bu biçime göre şekillendirilir."),
                       "makehumancommunity.org", "https://www.makehumancommunity.org")
                credit("meshoptimizer",
                       String(localized: "Modellerin uzaklığa göre sadeleştirilmiş detay seviyeleri meshoptimizer ile üretilmiştir. © Arseny Kapoulkine, MIT lisansı."),
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
