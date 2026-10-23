//
//  AppModel.swift
//  Anatomy
//

import Observation
import SwiftUI
import UserNotifications

/// Top-level app state shared through the environment.
@MainActor
@Observable
final class AppModel {
    enum Tab: String, Hashable {
        case atlas, systems, study, library, search
    }

    var tab: Tab = .atlas

    /// Realistic tissue colours or Z-Anatomy's teaching colours; remembered.
    var colorMode: ColorMode {
        get { scene.colorMode }
        set {
            scene.colorMode = newValue
            UserDefaults.standard.set(newValue.rawValue, forKey: "colorMode")
        }
    }

    /// Which genital organs the atlas shows; remembered.
    var sex: BodySex {
        get { scene.sex }
        set {
            scene.sex = newValue
            UserDefaults.standard.set(newValue.rawValue, forKey: "bodySex")
        }
    }

    /// Shown full screen over everything.
    var specimen: SpecimenRequest?
    /// The Premium offer, with what the user just tried to open.
    var paywall: PaywallContext?
    /// The running test or exam, shown full screen.
    var quiz: QuizSession?
    var flashcards: FlashcardDeck?
    /// A short message shown as an alert (e.g. no questions for a filter).
    var notice: String?
    /// The launch animation has finished (the onboarding waits for it).
    var launchFinished = UserDefaults.standard.bool(forKey: "SkipSplash") || UserDefaults.standard.bool(forKey: "AtlasNoChrome")
    /// The app's screens are built (behind the launch animation, once its
    /// figure is on screen: building the 3D atlas holds up the main thread).
    var interfaceMounted = UserDefaults.standard.bool(forKey: "SkipSplash") || UserDefaults.standard.bool(forKey: "AtlasNoChrome")
    let store: AtlasStore
    let study: StudyStore
    let bank = QuestionBank()
    let scene: AnatomyScene
    let purchases: PurchaseStore

    var isPremium: Bool { purchases.isPremium }

    /// Opens the paywall unless Premium is active; returns whether the
    /// feature may be used.
    @discardableResult
    func requirePremium(_ feature: PremiumFeature) -> Bool {
        if purchases.isPremium { return true }
        paywall = PaywallContext(feature: feature)
        return false
    }

    /// Whether a 3D part can be studied without Premium (the skeleton).
    func isFree(_ ref: PartRef) -> Bool {
        isPremium || ref.system == Access.freeLayer
    }

    func isFree(_ entry: AtlasEntry) -> Bool {
        Access.canOpen(systemID: entry.systemID, premium: isPremium)
    }

    /// Systems the user can study.
    var openSystems: Set<String> {
        Set(store.systems.map(\.id).filter { Access.canOpen(systemID: $0, premium: isPremium) })
    }

    /// Questions a free user can still answer today; nil with Premium.
    var freeQuestionsLeft: Int? {
        isPremium ? nil : max(0, Access.freeDailyQuestions - study.answeredToday)
    }

    /// Starts a test, applying the free tier limits.
    func startQuiz(_ config: QuizConfig) {
        var config = config
        if !isPremium {
            if config.isExam {
                requirePremium(.exam)
                return
            }
            // Muscle–nerve questions need the muscular system.
            if config.source == .innervation, !openSystems.contains("muscular") {
                requirePremium(.system(store.system("muscular")?.tr ?? String(localized: "Kas Sistemi")))
                return
            }
            let allowed = (config.systems ?? Set(store.systems.map(\.id))).intersection(openSystems)
            guard !allowed.isEmpty else {
                let name = config.systems?.first.flatMap(store.system)?.tr ?? String(localized: "Bu sistem")
                requirePremium(.system(name))
                return
            }
            guard let left = freeQuestionsLeft, left > 0 else {
                requirePremium(.questions)
                return
            }
            config.systems = allowed
            config.count = min(config.count, left)
        }
        let questions = QuizEngine.questions(for: config, store: store, bank: bank, study: study, hasModel: hasModel)
        guard !questions.isEmpty else {
            notice = switch config.source {
            case .wrongs: String(localized: "Yanlış yaptığın soru yok. Harika!")
            case .bookmarks: String(localized: "Henüz soru işaretlemedin. Soru ekranındaki yer imi düğmesiyle kaydedebilirsin.")
            default: String(localized: "Bu seçim için soru bulunamadı.")
            }
            return
        }
        quiz = QuizSession(config: config, questions: questions)
    }

    /// Restarts with a fixed list of questions (e.g. the wrong ones of a test).
    func startQuiz(title: String, questions: [QuizQuestion]) {
        guard !questions.isEmpty else { return }
        var list = questions
        if let left = freeQuestionsLeft {
            guard left > 0 else {
                // Called from inside a finished test: close it first.
                quiz = nil
                Task {
                    try? await Task.sleep(for: .milliseconds(600))
                    requirePremium(.questions)
                }
                return
            }
            list = Array(list.prefix(left))
        }
        quiz = QuizSession(config: QuizConfig(title: title, source: .bank, count: list.count), questions: list)
    }

    /// Every flashcard the atlas makes (built on first use).
    @ObservationIgnored private(set) lazy var flashcardLibrary = FlashcardLibrary(store: store)

    /// Opens a flashcard deck; free users get the skeletal system.
    func startFlashcards(kinds: Set<Flashcard.Kind> = Set(Flashcard.Kind.allCases), systems: Set<String>?,
                         group: String? = nil, title: String = String(localized: "Bilgi kartları")) {
        var scope = systems ?? Set(store.systems.map(\.id))
        if !isPremium {
            scope.formIntersection(openSystems)
            if scope.isEmpty {
                requirePremium(.flashcards)
                return
            }
        }
        let cards = flashcardLibrary.cards(kinds: kinds, systems: scope, group: group)
        guard !cards.isEmpty else {
            notice = String(localized: "Bu seçim için kart bulunamadı.")
            return
        }
        flashcards = FlashcardDeck(title: title, cards: cards, study: study)
    }

    /// Cards whose review is due (now, or by `date`), in the systems the user can study.
    func dueCards(kinds: Set<Flashcard.Kind> = Set(Flashcard.Kind.allCases), systems: Set<String>? = nil,
                  group: String? = nil, at date: Date = .now) -> Int {
        let scope = (systems ?? Set(store.systems.map(\.id))).intersection(openSystems)
        return flashcardLibrary.cards(kinds: kinds, systems: scope, group: group).count { study.isDue($0.id, at: date) }
    }

    /// Plans the daily review reminders for the coming week (see ReviewReminder).
    func scheduleReminders() {
        ReviewReminder.schedule(studiedToday: study.studiedToday) { [weak self] date in
            self?.dueCards(at: date) ?? 0
        }
    }

    /// Opens the Study tab when a review reminder is tapped.
    @ObservationIgnored private let notifications = NotificationRouter()

    init() {
        store = AtlasStore()
        study = StudyStore()
        purchases = PurchaseStore()
        // Launch arguments for screenshots and testing, e.g.
        // -AtlasLayers skeletal,visceral -AtlasGhost skeletal
        let defaults = UserDefaults.standard
        let layers = defaults.string(forKey: "AtlasLayers").map { Set($0.split(separator: ",").map(String.init)) }
        scene = AnatomyScene(initialLayers: layers)
        Diagnostics.shared.start()
        notifications.open = { [weak self] in self?.tab = .study }
        UNUserNotificationCenter.current().delegate = notifications
        // -AppTab study opens another tab (screenshots).
        if let tab = defaults.string(forKey: "AppTab").flatMap(Tab.init(rawValue:)) {
            self.tab = tab
        }
        // -AtlasSex female, otherwise the last choice.
        if let sex = (defaults.string(forKey: "AtlasSex") ?? defaults.string(forKey: "bodySex")).flatMap(BodySex.init(rawValue:)) {
            scene.sex = sex
        }
        // -AtlasColors educational, otherwise the last choice.
        if let mode = (defaults.string(forKey: "AtlasColors") ?? defaults.string(forKey: "colorMode")).flatMap(ColorMode.init(rawValue:)) {
            scene.colorMode = mode
        }
        for layer in (defaults.string(forKey: "AtlasGhost") ?? "").split(separator: ",") {
            scene.setLayer(String(layer), ghosted: true)
        }
        // -AtlasHideSide muscular:r hides one side of a layer (used for the icon).
        if let spec = defaults.string(forKey: "AtlasHideSide")?.split(separator: ":"), spec.count == 2 {
            let layer = String(spec[0]), side = String(spec[1])
            for (i, part) in (scene.manifests[layer] ?? []).enumerated() where part.side == side {
                scene.hide(PartRef(system: layer, index: i))
            }
        }
        // Tapping one head of a muscle selects the whole muscle on that side.
        scene.groupResolver = { [weak self] ref in
            guard let self, let info = self.scene.info(ref),
                  let entry = self.store.entry(for: info), self.store.isExact(entry, for: info) else { return [ref] }
            let group = self.scene.refs(matching: entry.models).filter {
                $0.system == ref.system && self.scene.info($0)?.side == info.side
            }
            return group.count <= 6 ? Set(group) : [ref]
        }
        // -AtlasInspect "Sacrum" opens the specimen viewer on launch.
        if let name = defaults.string(forKey: "AtlasInspect") {
            if let entry = store.entries.first(where: { $0.models.contains(name) }) {
                inspect(entry)
            } else {
                let refs = scene.refs(matching: [name])
                if !refs.isEmpty {
                    specimen = specimenRequest(for: refs, title: name, subtitle: name, entryID: nil)
                }
            }
        }
        // -AtlasReveal "Popliteus muscle" finds a structure in the atlas.
        if let name = defaults.string(forKey: "AtlasReveal") {
            let refs = scene.refs(matching: [name])
            Task { await scene.reveal(refs) }
        }
        // -AtlasSection "horizontal,1.3[,above]" opens a section view.
        if let spec = defaults.string(forKey: "AtlasSection")?.split(separator: ","), spec.count >= 2,
           let axis = ["sagittal", "horizontal", "coronal"].firstIndex(of: String(spec[0])).flatMap(SectionPlane.Axis.init(rawValue:)),
           let offset = Float(spec[1]) {
            scene.section = SectionPlane(axis: axis, offset: offset, keepBelow: spec.count < 3)
        }
        // -AtlasCamera "x,y,z,distance,yaw[,pitch]"
        if let values = defaults.string(forKey: "AtlasCamera")?.split(separator: ",").compactMap({ Float($0) }), values.count >= 5 {
            scene.setCamera(target: SIMD3(values[0], values[1], values[2]), distance: values[3], yaw: values[4],
                            pitch: values.count > 5 ? values[5] : 0.05)
        }
    }

    /// Whether the layers shown at launch have loaded (the launch animation
    /// waits for them).
    var atlasReady: Bool {
        scene.loadingLayers.isEmpty && scene.enabledLayers.allSatisfy(scene.isLoaded)
    }

    /// Hides the floating controls (for screenshots).
    var hidesChrome: Bool { UserDefaults.standard.bool(forKey: "AtlasNoChrome") }

    /// Switches to the 3D atlas and frames the parts that show `entry`.
    func showInAtlas(_ entry: AtlasEntry, isolate: Bool = false) {
        showInAtlas(scene.refs(matching: entry.models), isolate: isolate)
    }

    func showInAtlas(_ refs: [PartRef], isolate: Bool = false) {
        let refs = scene.matchingSex(refs)
        guard !refs.isEmpty else { return }
        // Female organs need Premium, like the switch in the layers sheet.
        if refs.allSatisfy({ scene.sex(of: $0) == .female }), sex != .female {
            guard requirePremium(.femaleAnatomy) else { return }
            sex = .female
        } else if refs.allSatisfy({ scene.sex(of: $0) == .male }), sex != .male {
            sex = .male
        }
        tab = .atlas
        Task { await scene.reveal(refs, isolate: isolate) }
    }

    /// Opens the specimen viewer for an entry's parts (one side only).
    func inspect(_ entry: AtlasEntry) {
        var refs = scene.matchingSex(scene.refs(matching: entry.models))
        guard !refs.isEmpty else { return }
        // Bilateral structures: keep the right side, like an atlas plate.
        if refs.contains(where: { scene.info($0)?.side == "r" }) {
            refs = refs.filter { scene.info($0)?.side != "l" }
        }
        // Very large groups would be unreadable on their own.
        if refs.count > 40 { refs = Array(refs.prefix(40)) }
        specimen = specimenRequest(for: refs, title: store.title(entry), subtitle: store.subtitle(entry), entryID: entry.id)
    }

    /// The specimen for `refs`. Muscles come with their attachment patches
    /// (origins red, insertions blue) and the bones they attach to.
    func specimenRequest(for refs: [PartRef], title: String, subtitle: String, entryID: String?) -> SpecimenRequest {
        let muscles = refs.filter { $0.system == "muscular" }.compactMap { scene.info($0) }
        guard !muscles.isEmpty else {
            return SpecimenRequest(refs: refs, faded: bones(around: refs.filter { $0.system == "joints" }),
                                   title: title, subtitle: subtitle, entryID: entryID)
        }
        var names = Set<String>()
        for muscle in muscles {
            names.insert(muscle.base.lowercased())
            if let parent = muscle.path.last { names.insert(parent.lowercased()) }
        }
        let sides = Set(muscles.compactMap(\.side))
        var attachments: [PartRef] = []
        var bones: [PartRef] = []
        var seen = Set<PartRef>()
        for (i, patch) in (scene.manifests["insertions"] ?? []).enumerated()
        where names.contains(patch.base.lowercased()) && (sides.isEmpty || patch.side.map(sides.contains) ?? true) {
            guard let bone = patch.path.last?.lowercased() else { continue }
            // The bone the patch lies on; a few patches in the source are
            // tagged with the wrong side and are left out.
            let carriers = scene.refs(matching: [bone]).filter { ref in
                guard ref.system == "skeletal", let info = scene.info(ref), info.base.lowercased() == bone,
                      info.side == nil || info.side == patch.side else { return false }
                let b = info.bounds, c = patch.center, m: Float = 0.015
                return c.x > b[0] - m && c.x < b[3] + m && c.y > b[1] - m && c.y < b[4] + m && c.z > b[2] - m && c.z < b[5] + m
            }
            guard !carriers.isEmpty else { continue }
            attachments.append(PartRef(system: "insertions", index: i))
            for ref in carriers where seen.insert(ref).inserted { bones.append(ref) }
        }
        return SpecimenRequest(refs: refs + attachments, context: Array(bones.prefix(14)),
                               title: title, subtitle: subtitle, entryID: entryID)
    }

    /// The bones a set of ligaments, capsules and cartilages touch: the
    /// largest overlaps first (the femur and hip bone for the hip capsule
    /// before a sesamoid nearby).
    private func bones(around refs: [PartRef]) -> [PartRef] {
        let boxes = refs.compactMap { scene.info($0)?.bounds }
        guard !boxes.isEmpty else { return [] }
        let m: Float = 0.006
        var touching: [(ref: PartRef, overlap: Float)] = []
        for (i, bone) in (scene.manifests["skeletal"] ?? []).enumerated() {
            let b = bone.bounds
            var overlap: Float = 0
            for a in boxes {
                let dx = min(a[3], b[3]) - max(a[0], b[0]) + 2 * m
                let dy = min(a[4], b[4]) - max(a[1], b[1]) + 2 * m
                let dz = min(a[5], b[5]) - max(a[2], b[2]) + 2 * m
                if dx > 0, dy > 0, dz > 0 { overlap += dx * dy * dz }
            }
            if overlap > 0 { touching.append((PartRef(system: "skeletal", index: i), overlap)) }
        }
        return Array(scene.matchingSex(touching.sorted { $0.overlap > $1.overlap }.map(\.ref)).prefix(16))
    }

    func hasModel(_ entry: AtlasEntry) -> Bool {
        !entry.models.isEmpty && !scene.refs(matching: entry.models).isEmpty
    }
}

/// Receives taps on the review reminders.
private final class NotificationRouter: NSObject, UNUserNotificationCenterDelegate {
    @MainActor var open: (() -> Void)?

    nonisolated func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse) async {
        await MainActor.run { open?() }
    }

    /// No banner while the app is in front: the Study tab shows the count.
    nonisolated func userNotificationCenter(_ center: UNUserNotificationCenter, willPresent notification: UNNotification) async
        -> UNNotificationPresentationOptions {
        []
    }
}
