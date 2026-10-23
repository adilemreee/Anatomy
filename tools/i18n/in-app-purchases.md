# In-App Purchases (App Store Connect)

Localizations of the Premium products, to enter in App Store Connect
(Monetization > In-App Purchases / Subscriptions > product > Localization).
Limits: display name 30 characters, description 45. The same texts are in
`Anatomy/Products.storekit` for local StoreKit testing.

## Subscription group "Premium" (Subscription Group Display Name)

| Language | Display name |
|---|---|
| Turkish | Anatomi Atlası Premium |
| English (U.S. / U.K.) | Anatomy Atlas Premium |
| French (France / Canada) | Atlas Anatomie Premium |
| German | Anatomie Atlas Premium |
| Spanish (Spain / Mexico) | Atlas Anatomía Premium |

## com.adilemre.anatomi.premium.yearly

| Language | Display name | Description |
|---|---|---|
| Turkish | Premium – Yıllık | Tüm sistemler, inceleme modu ve soru bankası. |
| English | Premium – Yearly | All systems, inspection mode and questions. |
| French | Premium – Annuel | Tous les systèmes, mode examen et questions. |
| German | Premium – Jährlich | Alle Systeme, Präparatmodus und Fragenbank. |
| Spanish | Premium – Anual | Todos los sistemas, modo examen y preguntas. |

## com.adilemre.anatomi.premium.monthly

| Language | Display name | Description |
|---|---|---|
| Turkish | Premium – Aylık | Tüm sistemler, inceleme modu ve soru bankası. |
| English | Premium – Monthly | All systems, inspection mode and questions. |
| French | Premium – Mensuel | Tous les systèmes, mode examen et questions. |
| German | Premium – Monatlich | Alle Systeme, Präparatmodus und Fragenbank. |
| Spanish | Premium – Mensual | Todos los sistemas, modo examen y preguntas. |

## com.adilemre.anatomi.premium.lifetime

| Language | Display name | Description |
|---|---|---|
| Turkish | Premium – Ömür boyu | Tüm Premium özellikler, tek seferlik ödeme. |
| English | Premium – Lifetime | All Premium features, one-time payment. |
| French | Premium – À vie | Tout Premium, en un seul paiement. |
| German | Premium – Lebenslang | Alle Premium-Funktionen, einmalige Zahlung. |
| Spanish | Premium – De por vida | Todo Premium con un único pago. |

## Win-back offers (subscriptions)

The app reads win-back offers from StoreKit (`Product.SubscriptionInfo.winBackOffers`,
`RenewalInfo.eligibleWinBackOfferIDs`) and passes the offer with the purchase, so
nothing else is needed in the code. When a lapsed subscriber opens the Premium
screen, the plan with an offer is selected, its row shows "Just for you: …" and the
button reads "Redeem offer". The App Store can also show the offer on its own
(product page, Search, Games, and a system sheet in the app).

To create one: App Store Connect > the app > Monetization > Subscriptions >
group "Premium" > the yearly or monthly subscription > Subscription Prices >
Win-Back Offers > Create Win-Back Offer.

- Reference name, e.g. `winback-yearly-2026`; offer ID, e.g. `winback.yearly.50` (it cannot be changed later)
- Type: pay up front (e.g. 1 year at half price), pay as you go (e.g. 3 months at a lower price) or free trial
- Eligibility: paid for at least 2 months, lapsed for 1–6 months, and do not show again for 6 months
- Countries and prices, then start (and optionally end) dates
- Priority: "Normal"; mark it "Promote" only if the App Store should show it outside the app

To test, use a Sandbox account whose subscription has expired, or add a win-back offer to
`Anatomy/Products.storekit` in Xcode (Editor > Add Win-Back Offer) and expire the
subscription in the transaction manager.
