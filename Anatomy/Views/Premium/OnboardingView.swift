//
//  OnboardingView.swift
//  Anatomy
//

import SwiftUI

/// First launch: three pages about the app, the user's level, then the
/// Premium offer.
struct OnboardingView: View {
    @Environment(AppModel.self) private var app
    let finish: () -> Void
    @State private var page = 0
    @AppStorage("profile.level") private var level = ""

    private let pages: [(image: String, icon: String, title: String, text: String)] = [
        ("card-muscular", "figure.arms.open", String(localized: "Türkçe 3D kas-iskelet atlası"),
         String(localized: "Kemikleri, eklemleri ve kasları döndür, yakınlaştır, katman katman aç.")),
        ("card-skeletal", "cube.transparent", String(localized: "Her yapıyı tek başına incele"),
         String(localized: "İnceleme modunda Latince oluşumları, kasların başlangıç ve tutunma yerlerini işaretli gör.")),
        ("card-articular", "checkmark.seal.fill", String(localized: "Sınava hazırlan"),
         String(localized: "TUS ve komite düzeyinde özgün sorular, açıklamalı cevaplar, deneme sınavları ve aralıklı tekrar.")),
    ]

    var body: some View {
        ZStack {
            Theme.background.ignoresSafeArea()
            if page < pages.count {
                featurePage(pages[page])
                    .id(page)
                    .transition(.asymmetric(insertion: .move(edge: .trailing).combined(with: .opacity), removal: .move(edge: .leading).combined(with: .opacity)))
            } else {
                levelPage
                    .transition(.move(edge: .trailing).combined(with: .opacity))
            }
        }
        .animation(.snappy, value: page)
        .safeAreaInset(edge: .bottom) {
            VStack(spacing: 14) {
                HStack(spacing: 6) {
                    ForEach(0...pages.count, id: \.self) { i in
                        Capsule()
                            .fill(i == page ? Theme.accent : Color.white.opacity(0.18))
                            .frame(width: i == page ? 22 : 7, height: 7)
                    }
                }
                Button(page < pages.count ? String(localized: "Devam") : String(localized: "Başla")) {
                    if page < pages.count {
                        page += 1
                    } else {
                        finish()
                        if !app.isPremium {
                            Task {
                                try? await Task.sleep(for: .milliseconds(450))
                                app.requirePremium(.general)
                            }
                        }
                    }
                }
                .buttonStyle(PrimaryButtonStyle())
                .disabled(page == pages.count && level.isEmpty)
                .opacity(page == pages.count && level.isEmpty ? 0.5 : 1)
            }
            .padding(.horizontal, 24)
            .padding(.bottom, 8)
        }
        .preferredColorScheme(.dark)
    }

    private func featurePage(_ p: (image: String, icon: String, title: String, text: String)) -> some View {
        VStack(spacing: 0) {
            // Below the status bar and Dynamic Island, fading in at the top
            // and out into the background at the bottom.
            Color.clear
                .frame(height: 400)
                .overlay(alignment: .top) {
                    if let image = UIImage(named: p.image) {
                        Image(uiImage: image)
                            .resizable()
                            .scaledToFill()
                            .frame(height: 400, alignment: .top)
                    } else {
                        Theme.accentGradient
                    }
                }
                .clipped()
                .mask {
                    LinearGradient(stops: [.init(color: .clear, location: 0), .init(color: .black, location: 0.1),
                                           .init(color: .black, location: 0.5), .init(color: .clear, location: 1)],
                                   startPoint: .top, endPoint: .bottom)
                }
                .padding(.top, 4)
            VStack(alignment: .leading, spacing: 12) {
                Image(systemName: p.icon)
                    .font(.system(size: 26, weight: .semibold))
                    .foregroundStyle(Theme.accent)
                Text(p.title)
                    .font(.system(.largeTitle, weight: .bold))
                    .foregroundStyle(Theme.textPrimary)
                    .fixedSize(horizontal: false, vertical: true)
                Text(p.text)
                    .font(.body)
                    .foregroundStyle(Theme.textSecondary)
                    .fixedSize(horizontal: false, vertical: true)
            }
            .padding(.horizontal, 24)
            .frame(maxWidth: .infinity, alignment: .leading)
            Spacer()
        }
    }

    private var levelPage: some View {
        VStack(alignment: .leading, spacing: 18) {
            Spacer().frame(height: 40)
            Text("Ne için çalışıyorsun?")
                .font(.system(.largeTitle, weight: .bold))
                .foregroundStyle(Theme.textPrimary)
            Text("Soruları ve önerileri buna göre ayarlarız. Sonra Profil'den değiştirebilirsin.")
                .font(.body)
                .foregroundStyle(Theme.textSecondary)
            VStack(spacing: 10) {
                option("faculty", String(localized: "Tıp fakültesi (Dönem 1–3)"), String(localized: "Komite ve final sınavları"), "building.columns.fill")
                option("tus", String(localized: "TUS hazırlığı"), String(localized: "Klinik vakalar ve zor sorular ağırlıkta"), "target")
                option("dentistry", String(localized: "Diş hekimliği"), String(localized: "Baş-boyun ağırlıklı"), "mouth.fill")
                option("health", String(localized: "Diğer sağlık bölümleri"), String(localized: "Fizyoterapi, hemşirelik, ebelik…"), "cross.case.fill")
            }
            Spacer()
        }
        .padding(.horizontal, 24)
    }

    private func option(_ id: String, _ title: String, _ detail: String, _ icon: String) -> some View {
        Button {
            withAnimation(.snappy) { level = id }
        } label: {
            HStack(spacing: 14) {
                Image(systemName: icon)
                    .font(.title3)
                    .foregroundStyle(level == id ? Theme.accent : Theme.textSecondary)
                    .frame(width: 30)
                VStack(alignment: .leading, spacing: 2) {
                    Text(title).font(.headline).foregroundStyle(Theme.textPrimary)
                    Text(detail).font(.caption).foregroundStyle(Theme.textSecondary)
                }
                Spacer()
                Image(systemName: level == id ? "checkmark.circle.fill" : "circle")
                    .foregroundStyle(level == id ? Theme.accent : Theme.textTertiary)
            }
            .padding(16)
            .background(level == id ? Theme.accent.opacity(0.1) : Theme.card, in: .rect(cornerRadius: 18))
            .overlay { RoundedRectangle(cornerRadius: 18).strokeBorder(level == id ? Theme.accent : Theme.stroke) }
        }
        .buttonStyle(PressableStyle())
    }
}
