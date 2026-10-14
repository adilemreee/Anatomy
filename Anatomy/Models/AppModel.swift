//
//  AppModel.swift
//  Anatomy
//

import Observation
import SwiftUI

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
            let allowed = (config.systems ?? Set(store.systems.map(\.id))).intersection(openSystems)
            guard !allowed.isEmpty else {
                let name = config.systems?.first.flatMap(store.system)?.tr ?? "Bu sistem"
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
            case .wrongs: "Yanlış yaptığın soru yok. Harika!"
            case .bookmarks: "Henüz soru işaretlemedin. Soru ekranındaki yer imi düğmesiyle kaydedebilirsin."
            default: "Bu seçim için soru bulunamadı."
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

    /// Opens a flashcard deck; free users get the skeletal system.
    func startFlashcards(systems: Set<String>?) {
        var scope = systems ?? Set(store.systems.map(\.id))
        if !isPremium {
            scope.formIntersection(openSystems)
            if scope.isEmpty {
                requirePremium(.flashcards)
                return
            }
        }
        let entries = store.entries.filter { scope.contains($0.systemID) }
        flashcards = FlashcardDeck(entries: entries, study: study)
    }

    init() {
        store = AtlasStore()
        study = StudyStore()
        purchases = PurchaseStore()
        // Launch arguments for screenshots and testing, e.g.
        // -AtlasLayers skeletal,visceral -AtlasGhost skeletal
        let defaults = UserDefaults.standard
        let layers = defaults.string(forKey: "AtlasLayers").map { Set($0.split(separator: ",").map(String.init)) }
        scene = AnatomyScene(initialLayers: layers)
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
        // -AtlasCamera "x,y,z,distance,yaw[,pitch]"
        if let values = defaults.string(forKey: "AtlasCamera")?.split(separator: ",").compactMap({ Float($0) }), values.count >= 5 {
            scene.setCamera(target: SIMD3(values[0], values[1], values[2]), distance: values[3], yaw: values[4],
                            pitch: values.count > 5 ? values[5] : 0.05)
        }
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
        specimen = specimenRequest(for: refs, title: entry.tr, subtitle: entry.la, entryID: entry.id)
    }

    /// The specimen for `refs`. Muscles come with their attachment patches
    /// (origins red, insertions blue) and the bones they attach to.
    func specimenRequest(for refs: [PartRef], title: String, subtitle: String, entryID: String?) -> SpecimenRequest {
        let muscles = refs.filter { $0.system == "muscular" }.compactMap { scene.info($0) }
        guard !muscles.isEmpty else { return SpecimenRequest(refs: refs, title: title, subtitle: subtitle, entryID: entryID) }
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

    func hasModel(_ entry: AtlasEntry) -> Bool {
        !entry.models.isEmpty && !scene.refs(matching: entry.models).isEmpty
    }
}
