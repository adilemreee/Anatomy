//
//  PurchaseStore.swift
//  Anatomy
//
//  Premium through StoreKit 2: a monthly and a yearly subscription (one
//  group, the yearly plan with a free trial) and a one-time lifetime unlock.
//  Products are defined in App Store Connect with the identifiers below;
//  Anatomy/Products.storekit mirrors them for local testing.
//

import Foundation
import Observation
import StoreKit

@MainActor
@Observable
final class PurchaseStore {
    enum Plan: String, CaseIterable, Identifiable {
        case yearly = "com.adilemre.anatomi.premium.yearly"
        case monthly = "com.adilemre.anatomi.premium.monthly"
        case lifetime = "com.adilemre.anatomi.premium.lifetime"

        var id: String { rawValue }

        var title: String {
            switch self {
            case .yearly: String(localized: "Yıllık")
            case .monthly: String(localized: "Aylık")
            case .lifetime: String(localized: "Ömür boyu")
            }
        }
    }

    private(set) var products: [Plan: Product] = [:]
    private(set) var isPremium = false
    private(set) var activePlan: Plan?
    private(set) var isLoading = false
    private(set) var lastError: String?
    /// Win-back offers (set up in App Store Connect) the App Store makes to
    /// this former subscriber, by plan: bought with the offer price.
    private(set) var winBackOffers: [Plan: Product.SubscriptionOffer] = [:]

    @ObservationIgnored private var updates: Task<Void, Never>?
    #if DEBUG
    /// -PremiumUnlocked YES for screenshots and testing (debug builds only: in
    /// a release build a defaults key must never unlock Premium).
    @ObservationIgnored private let forcedUnlock = UserDefaults.standard.bool(forKey: "PremiumUnlocked")
    #else
    @ObservationIgnored private let forcedUnlock = false
    #endif

    init() {
        isPremium = forcedUnlock
        updates = Task { [weak self] in
            for await result in Transaction.updates {
                if case .verified(let transaction) = result {
                    await transaction.finish()
                }
                await self?.refreshEntitlements()
            }
        }
        Task {
            await loadProducts()
            await refreshEntitlements()
            await refreshWinBackOffers()
        }
    }

    func loadProducts() async {
        guard products.isEmpty else { return }
        isLoading = true
        defer { isLoading = false }
        do {
            let list = try await Product.products(for: Plan.allCases.map(\.rawValue))
            var map: [Plan: Product] = [:]
            for product in list {
                if let plan = Plan(rawValue: product.id) { map[plan] = product }
            }
            products = map
        } catch {
            lastError = String(localized: "Ürünler yüklenemedi. İnternet bağlantını kontrol et.")
        }
    }

    func refreshEntitlements() async {
        var plan: Plan?
        for await result in Transaction.currentEntitlements {
            guard case .verified(let transaction) = result, transaction.revocationDate == nil,
                  let p = Plan(rawValue: transaction.productID) else { continue }
            if let expiry = transaction.expirationDate, expiry < .now { continue }
            // Lifetime wins over a subscription.
            if plan != .lifetime { plan = p }
        }
        activePlan = plan
        isPremium = forcedUnlock || plan != nil
    }

    /// The win-back offers this user is eligible for: only someone whose
    /// subscription lapsed gets them.
    func refreshWinBackOffers() async {
        var offers: [Plan: Product.SubscriptionOffer] = [:]
        if !isPremium {
            for plan in [Plan.yearly, .monthly] {
                guard let subscription = products[plan]?.subscription, !subscription.winBackOffers.isEmpty,
                      let statuses = try? await subscription.status else { continue }
                var eligible = Set<String>()
                for status in statuses {
                    if case .verified(let info) = status.renewalInfo { eligible.formUnion(info.eligibleWinBackOfferIDs) }
                }
                if let offer = subscription.winBackOffers.first(where: { $0.id.map(eligible.contains) ?? false }) {
                    offers[plan] = offer
                }
            }
        }
        winBackOffers = offers
    }

    /// Buys `plan`; returns whether Premium is active afterwards.
    @discardableResult
    func purchase(_ plan: Plan) async -> Bool {
        guard let product = products[plan] else {
            lastError = String(localized: "Bu plan şu anda kullanılamıyor.")
            return false
        }
        lastError = nil
        do {
            let options: Set<Product.PurchaseOption> = winBackOffers[plan].map { [.winBackOffer($0)] } ?? []
            switch try await product.purchase(options: options) {
            case .success(let verification):
                if case .verified(let transaction) = verification {
                    await transaction.finish()
                }
                await refreshEntitlements()
            case .pending:
                lastError = String(localized: "Satın alma onay bekliyor.")
            case .userCancelled:
                break
            @unknown default:
                break
            }
        } catch {
            lastError = String(localized: "Satın alma tamamlanamadı.")
        }
        return isPremium
    }

    func restore() async {
        lastError = nil
        do {
            try await AppStore.sync()
            await refreshEntitlements()
            if !isPremium { lastError = String(localized: "Geri yüklenecek bir satın alma bulunamadı.") }
        } catch {
            lastError = String(localized: "Satın almalar geri yüklenemedi.")
        }
    }

    // MARK: Display helpers

    func price(_ plan: Plan) -> String {
        products[plan]?.displayPrice ?? "–"
    }

    /// "Aylık ₺42" for the yearly plan, for comparison.
    func monthlyEquivalent(of plan: Plan) -> String? {
        guard plan == .yearly, let product = products[plan] else { return nil }
        let monthly = product.price / 12
        return monthly.formatted(product.priceFormatStyle)
    }

    /// Savings of the yearly plan over twelve monthly payments, in percent.
    var yearlySavings: Int? {
        guard let y = products[.yearly]?.price, let m = products[.monthly]?.price, m > 0 else { return nil }
        let ratio = (y as NSDecimalNumber).doubleValue / ((m as NSDecimalNumber).doubleValue * 12)
        let saving = Int(((1 - ratio) * 100).rounded())
        return saving > 0 ? saving : nil
    }

    /// "3 ay boyunca ₺99,99/ay" for a win-back offer.
    func winBackText(_ plan: Plan) -> String? {
        guard let offer = winBackOffers[plan] else { return nil }
        let price = offer.displayPrice
        let unit = offer.period.unit
        let count = offer.period.value * max(offer.periodCount, 1)
        switch offer.paymentMode {
        case .freeTrial:
            return Self.free(count, unit)
        case .payUpFront:
            return String(localized: "\(Self.duration(count, unit)) için \(price)")
        default:
            return String(localized: "\(Self.duration(count, unit)) boyunca dönem başına \(price)")
        }
    }

    private static func duration(_ count: Int, _ unit: Product.SubscriptionPeriod.Unit) -> String {
        switch unit {
        // Identifier keys: "%lld ay" is already the compact review interval.
        case .week: String(localized: "duration.week", defaultValue: "\(count) hafta")
        case .month: String(localized: "duration.month", defaultValue: "\(count) ay")
        case .year: String(localized: "duration.year", defaultValue: "\(count) yıl")
        default: String(localized: "duration.day", defaultValue: "\(count) gün")
        }
    }

    func trialText(_ plan: Plan) -> String? {
        guard let offer = products[plan]?.subscription?.introductoryOffer, offer.paymentMode == .freeTrial else { return nil }
        return Self.free(offer.period.value, offer.period.unit)
    }

    private static func free(_ count: Int, _ unit: Product.SubscriptionPeriod.Unit) -> String {
        switch unit {
        case .week: String(localized: "\(count) hafta ücretsiz")
        case .month: String(localized: "\(count) ay ücretsiz")
        case .year: String(localized: "\(count) yıl ücretsiz")
        default: String(localized: "\(count) gün ücretsiz")
        }
    }
}

/// What the free tier may open. Everything else asks for Premium.
@MainActor
enum Access {
    /// The only 3D layer and written system open without Premium.
    static let freeLayer = "skeletal"
    static let freeSystem = "skeletal"
    /// Questions a free user can answer per day.
    static let freeDailyQuestions = 10

    static func canOpen(layer: String, premium: Bool) -> Bool {
        premium || layer == freeLayer
    }

    static func canOpen(systemID: String, premium: Bool) -> Bool {
        premium || systemID == freeSystem
    }
}
