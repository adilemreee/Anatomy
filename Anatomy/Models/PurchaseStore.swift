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
            case .yearly: "Yıllık"
            case .monthly: "Aylık"
            case .lifetime: "Ömür boyu"
            }
        }
    }

    private(set) var products: [Plan: Product] = [:]
    private(set) var isPremium = false
    private(set) var activePlan: Plan?
    private(set) var isLoading = false
    private(set) var lastError: String?

    @ObservationIgnored private var updates: Task<Void, Never>?
    /// -PremiumUnlocked YES for screenshots and testing.
    @ObservationIgnored private let forcedUnlock = UserDefaults.standard.bool(forKey: "PremiumUnlocked")

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
            lastError = "Ürünler yüklenemedi. İnternet bağlantını kontrol et."
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

    /// Buys `plan`; returns whether Premium is active afterwards.
    @discardableResult
    func purchase(_ plan: Plan) async -> Bool {
        guard let product = products[plan] else {
            lastError = "Bu plan şu anda kullanılamıyor."
            return false
        }
        lastError = nil
        do {
            switch try await product.purchase() {
            case .success(let verification):
                if case .verified(let transaction) = verification {
                    await transaction.finish()
                }
                await refreshEntitlements()
            case .pending:
                lastError = "Satın alma onay bekliyor."
            case .userCancelled:
                break
            @unknown default:
                break
            }
        } catch {
            lastError = "Satın alma tamamlanamadı."
        }
        return isPremium
    }

    func restore() async {
        lastError = nil
        do {
            try await AppStore.sync()
            await refreshEntitlements()
            if !isPremium { lastError = "Geri yüklenecek bir satın alma bulunamadı." }
        } catch {
            lastError = "Satın almalar geri yüklenemedi."
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

    func trialText(_ plan: Plan) -> String? {
        guard let offer = products[plan]?.subscription?.introductoryOffer, offer.paymentMode == .freeTrial else { return nil }
        let period = offer.period
        let unit: String
        switch period.unit {
        case .day: unit = "gün"
        case .week: unit = "hafta"
        case .month: unit = "ay"
        case .year: unit = "yıl"
        @unknown default: unit = "gün"
        }
        return "\(period.value) \(unit) ücretsiz"
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
