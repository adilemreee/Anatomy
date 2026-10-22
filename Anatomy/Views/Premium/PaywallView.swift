//
//  PaywallView.swift
//  Anatomy
//

import StoreKit
import SwiftUI

/// The Premium offer: what it unlocks, the three plans and the legal links
/// App Review asks for.
struct PaywallView: View {
    @Environment(AppModel.self) private var app
    @Environment(\.dismiss) private var dismiss
    @Environment(\.openURL) private var openURL
    let context: PaywallContext
    @State private var plan: PurchaseStore.Plan = .yearly
    @State private var working = false

    private var purchases: PurchaseStore { app.purchases }

    var body: some View {
        ZStack(alignment: .top) {
            Theme.background.ignoresSafeArea()
            header
            ScrollView {
                VStack(alignment: .leading, spacing: 22) {
                    Spacer().frame(height: 190)
                    titleBlock
                    benefits
                    plans
                    if let error = purchases.lastError {
                        Text(error)
                            .font(.footnote)
                            .foregroundStyle(Theme.danger)
                    }
                    legal
                }
                .padding(.horizontal, 20)
                .padding(.bottom, 140)
            }
            .scrollIndicators(.hidden)
        }
        .safeAreaInset(edge: .bottom) { purchaseBar }
        .overlay(alignment: .topTrailing) {
            Button {
                dismiss()
            } label: {
                Image(systemName: "xmark")
                    .font(.subheadline.weight(.bold))
                    .foregroundStyle(Theme.textSecondary)
                    .frame(width: 36, height: 36)
                    .background(Color.white.opacity(0.08), in: .circle)
            }
            .padding(16)
            .accessibilityLabel("Kapat")
        }
        .task { await purchases.loadProducts() }
        .onChange(of: purchases.isPremium) { _, premium in
            if premium { dismiss() }
        }
        .preferredColorScheme(.dark)
    }

    // MARK: Header

    /// The figure starts below the status bar and Dynamic Island and fades
    /// in from the dark background at the top and into it at the bottom.
    private var header: some View {
        Color.clear
            .frame(height: 250)
            .overlay(alignment: .top) {
                if let image = UIImage(named: "card-muscular") {
                    Image(uiImage: image).resizable().scaledToFill()
                        .frame(height: 250, alignment: .top)
                } else {
                    Theme.accentGradient
                }
            }
            .clipped()
            .mask {
                LinearGradient(stops: [.init(color: .clear, location: 0), .init(color: .black, location: 0.16),
                                       .init(color: .black, location: 0.55), .init(color: .clear, location: 1)],
                               startPoint: .top, endPoint: .bottom)
            }
            .padding(.top, 8)
    }

    private var titleBlock: some View {
        VStack(alignment: .leading, spacing: 8) {
            PremiumBadge()
            Text(context.feature == .general ? String(localized: "Anatomiyi en iyi hâliyle öğren") : context.feature.title)
                .font(.system(.largeTitle, weight: .bold))
                .foregroundStyle(Theme.textPrimary)
                .fixedSize(horizontal: false, vertical: true)
            Text("Kemikler, eklemler ve kaslar için 280'i aşkın ayrıntılı madde, yaklaşık 500 işaretli kemik oluşumu, 380'i aşkın özgün TUS ve komite sorusu ve 3.000'e yakın bilgi kartı, tek bir uygulamada.")
                .font(.body)
                .foregroundStyle(Theme.textSecondary)
        }
    }

    private var benefits: some View {
        VStack(alignment: .leading, spacing: 14) {
            benefit("figure.strengthtraining.traditional", String(localized: "Kas-iskelet sistemi, en ince ayrıntısıyla"), String(localized: "Bütün kemikler, eklemler ve bağlar, 200'ü aşkın kas ve yapışma yerleri; kadın ve erkek anatomisi"))
            benefit("cube.transparent", String(localized: "İnceleme modu"), String(localized: "Her yapıyı tek başına, işaretli oluşumlarıyla incele; kasların origo ve insersiyosunu gör"))
            benefit("text.book.closed", String(localized: "Ayrıntılı Türkçe maddeler"), String(localized: "Latince terimler, kanlanma, sinir, klinik bilgi ve her maddede TUS notları"))
            benefit("checkmark.seal", String(localized: "Sınırsız soru bankası"), String(localized: "Açıklamalı özgün sorular, klinik vakalar, kas–sinir ve kemik oluşumu soruları, süreli denemeler ve istatistikler"))
            benefit("rectangle.on.rectangle.angled", String(localized: "Aralıklı tekrar kartları"), String(localized: "Yapı, Latince ad, origo–insersiyo–sinir, kemik oluşumu, TUS ve klinik desteleri"))
        }
    }

    private func benefit(_ icon: String, _ title: String, _ detail: String) -> some View {
        HStack(alignment: .top, spacing: 14) {
            Image(systemName: icon)
                .font(.system(size: 17, weight: .semibold))
                .foregroundStyle(Theme.gold)
                .frame(width: 36, height: 36)
                .background(Theme.gold.opacity(0.12), in: .rect(cornerRadius: 10))
            VStack(alignment: .leading, spacing: 2) {
                Text(title).font(.subheadline.weight(.semibold)).foregroundStyle(Theme.textPrimary)
                Text(detail).font(.footnote).foregroundStyle(Theme.textSecondary).fixedSize(horizontal: false, vertical: true)
            }
        }
    }

    // MARK: Plans

    private var plans: some View {
        VStack(spacing: 10) {
            ForEach(PurchaseStore.Plan.allCases) { option in
                PlanRow(plan: option, selected: plan == option, purchases: purchases) {
                    withAnimation(.snappy) { plan = option }
                }
            }
        }
    }

    private var purchaseBar: some View {
        VStack(spacing: 8) {
            Button {
                working = true
                Task {
                    await purchases.purchase(plan)
                    working = false
                }
            } label: {
                HStack {
                    if working { ProgressView().tint(.black) }
                    Text(ctaTitle)
                }
            }
            .buttonStyle(PrimaryButtonStyle(gradient: Theme.goldGradient, foreground: Color(hex: "2A1D05")))
            .disabled(working || purchases.products[plan] == nil)
            Text(footnote)
                .font(.caption2)
                .foregroundStyle(Theme.textTertiary)
                .multilineTextAlignment(.center)
        }
        .padding(.horizontal, 20)
        .padding(.top, 12)
        .padding(.bottom, 6)
        .background(Theme.background.opacity(0.96))
    }

    private var ctaTitle: String {
        if let trial = purchases.trialText(plan) { return String(localized: "\(trial) dene") }
        return plan == .lifetime ? String(localized: "Bir kez öde, hep kullan") : String(localized: "Premium'a geç")
    }

    private var footnote: String {
        switch plan {
        case .lifetime:
            return String(localized: "Tek seferlik ödeme. Abonelik değildir.")
        case .yearly:
            if let trial = purchases.trialText(plan) {
                return String(localized: "\(trial), sonra yılda bir \(purchases.price(.yearly)) ücretlendirilir. İstediğin zaman App Store ayarlarından iptal edebilirsin.")
            }
            return String(localized: "Yılda bir \(purchases.price(.yearly)) ücretlendirilir. İstediğin zaman App Store ayarlarından iptal edebilirsin.")
        case .monthly:
            return String(localized: "Ayda bir \(purchases.price(.monthly)) ücretlendirilir. İstediğin zaman App Store ayarlarından iptal edebilirsin.")
        }
    }

    private var legal: some View {
        HStack(spacing: 18) {
            Button("Satın alımları geri yükle") {
                Task { await purchases.restore() }
            }
            Button("Kullanım Koşulları") { openURL(Legal.terms) }
            Button("Gizlilik") { openURL(Legal.privacy) }
        }
        .font(.caption.weight(.medium))
        .foregroundStyle(Theme.textSecondary)
        .frame(maxWidth: .infinity)
        .padding(.top, 4)
    }
}

private struct PlanRow: View {
    let plan: PurchaseStore.Plan
    let selected: Bool
    let purchases: PurchaseStore
    let select: () -> Void

    var body: some View {
        Button(action: select) {
            HStack(spacing: 14) {
                Image(systemName: selected ? "checkmark.circle.fill" : "circle")
                    .font(.title3)
                    .foregroundStyle(selected ? Theme.gold : Theme.textTertiary)
                VStack(alignment: .leading, spacing: 3) {
                    HStack(spacing: 6) {
                        Text(plan.title).font(.headline).foregroundStyle(Theme.textPrimary)
                        if plan == .yearly, let saving = purchases.yearlySavings {
                            Text("\((Double(saving) / 100).formatted(.percent.precision(.fractionLength(0)))) tasarruf")
                                .font(.caption2.weight(.heavy))
                                .foregroundStyle(Color(hex: "2A1D05"))
                                .padding(.horizontal, 6).padding(.vertical, 2)
                                .background(Theme.goldGradient, in: .capsule)
                        }
                    }
                    Text(detail).font(.caption).foregroundStyle(Theme.textSecondary)
                }
                Spacer()
                VStack(alignment: .trailing, spacing: 2) {
                    Text(purchases.price(plan)).font(.headline).foregroundStyle(Theme.textPrimary)
                    if let monthly = purchases.monthlyEquivalent(of: plan) {
                        Text("aylık \(monthly)").font(.caption2).foregroundStyle(Theme.textTertiary)
                    }
                }
            }
            .padding(16)
            .background(selected ? Theme.gold.opacity(0.08) : Theme.card, in: .rect(cornerRadius: 18))
            .overlay {
                RoundedRectangle(cornerRadius: 18).strokeBorder(selected ? Theme.gold : Theme.stroke, lineWidth: selected ? 1.5 : 1)
            }
        }
        .buttonStyle(PressableStyle())
    }

    private var detail: String {
        switch plan {
        case .yearly: purchases.trialText(plan).map { String(localized: "\($0), sonra yıllık") } ?? String(localized: "Yılda bir ödeme")
        case .monthly: String(localized: "Her ay yenilenir")
        case .lifetime: String(localized: "Tek seferlik ödeme, abonelik yok")
        }
    }
}

/// Links required next to subscriptions (the pages are docs/ in this repo,
/// served at anatomi.adilemree.xyz). The terms include Apple's standard EULA.
enum Legal {
    static let terms = URL(string: "https://anatomi.adilemree.xyz/terms")!
    static let privacy = URL(string: "https://anatomi.adilemree.xyz/privacy")!
    static let support = URL(string: "https://anatomi.adilemree.xyz/destek")!
}
