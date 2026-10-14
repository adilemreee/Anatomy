//
//  RootView.swift
//  Anatomy
//

import SwiftUI

struct RootView: View {
    @Environment(AppModel.self) private var app
    @AppStorage("onboarding.done") private var onboardingDone = false
    /// -OpenEntry hepar shows an entry page on launch (screenshots, testing).
    @State private var launchEntry: AtlasEntry?

    var body: some View {
        @Bindable var app = app
        TabView(selection: $app.tab) {
            Tab("Atlas", systemImage: "figure.arms.open", value: AppModel.Tab.atlas) {
                AtlasView()
            }
            Tab("Keşfet", systemImage: "square.grid.2x2.fill", value: AppModel.Tab.systems) {
                SystemsView()
            }
            Tab("Çalış", systemImage: "graduationcap.fill", value: AppModel.Tab.study) {
                StudyView()
            }
            Tab("Profil", systemImage: "person.crop.circle.fill", value: AppModel.Tab.library) {
                LibraryView()
            }
            Tab("Ara", systemImage: "magnifyingglass", value: AppModel.Tab.search, role: .search) {
                SearchView()
            }
        }
        .tabViewStyle(.sidebarAdaptable)
        .tint(Theme.accent)
        .preferredColorScheme(.dark)
        // Inspection and the paywall open over whatever modal is in front.
        .appOverlays(active: app.quiz == nil && app.flashcards == nil)
        .fullScreenCover(item: $app.quiz) { session in
            QuizSessionView(session: session)
        }
        .fullScreenCover(item: $app.flashcards) { deck in
            FlashcardsView(deck: deck)
        }
        .alert(app.notice ?? "", isPresented: Binding(get: { app.notice != nil }, set: { if !$0 { app.notice = nil } })) {
            Button("Tamam", role: .cancel) {}
        }
        .fullScreenCover(isPresented: Binding(get: { !onboardingDone && !app.hidesChrome && !UserDefaults.standard.bool(forKey: "SkipOnboarding") },
                                              set: { if !$0 { onboardingDone = true } })) {
            OnboardingView { onboardingDone = true }
        }
        .task {
            await app.store.loadGlossary()
            if let id = UserDefaults.standard.string(forKey: "OpenEntry") { launchEntry = app.store.entry(id) }
            // -ShowPaywall YES opens the Premium offer (screenshots, testing).
            if UserDefaults.standard.bool(forKey: "ShowPaywall") { app.paywall = PaywallContext(feature: .general) }
        }
        .sheet(item: $launchEntry) { entry in
            NavigationStack {
                EntryDetailView(entry: entry)
                    .navigationDestination(for: AtlasEntry.self) { EntryDetailView(entry: $0) }
            }
            .appOverlays()
        }
        .task {
            await app.bank.load(systems: app.store.systems.map(\.id))
            // -StartQuiz mixed|bank|clinical|… or -StartQuiz exam (screenshots, testing)
            if let start = UserDefaults.standard.string(forKey: "StartQuiz") {
                if start == "exam" {
                    app.startQuiz(ExamPreset.all[0].config)
                } else if start == "cards" {
                    app.startFlashcards(systems: nil)
                } else if let source = QuizSource(rawValue: start) {
                    app.startQuiz(QuizConfig(title: source.title, source: source, count: 10))
                }
            }
        }
    }
}

/// Presents the specimen viewer and the paywall. Every modal screen that can
/// lead to them hosts this too; only the frontmost host is `active`.
private struct AppOverlays: ViewModifier {
    @Environment(AppModel.self) private var app
    let active: Bool
    /// False inside the specimen viewer itself.
    let specimen: Bool

    func body(content: Content) -> some View {
        content
            .fullScreenCover(item: Binding(get: { active && specimen ? app.specimen : nil }, set: { app.specimen = $0 })) { request in
                SpecimenView(request: request)
            }
            .fullScreenCover(item: Binding(get: { active ? app.paywall : nil }, set: { app.paywall = $0 })) { context in
                PaywallView(context: context)
            }
    }
}

extension View {
    func appOverlays(active: Bool = true, specimen: Bool = true) -> some View {
        modifier(AppOverlays(active: active, specimen: specimen))
    }
}
