//
//  AnatomyApp.swift
//  Anatomy
//
//  Created by adil emre  on 7.10.2026.
//

import SwiftUI

@main
struct AnatomyApp: App {
    @State private var app = AppModel()

    var body: some Scene {
        WindowGroup {
            ZStack {
                if app.interfaceMounted {
                    RootView()
                }
                if !app.launchFinished {
                    SplashView(isReady: { app.interfaceMounted && app.atlasReady },
                               onFigureShown: { app.interfaceMounted = true },
                               onFinish: { app.launchFinished = true })
                        .zIndex(1)
                }
            }
            .environment(app)
            .preferredColorScheme(.dark)
            #if DEBUG
            // -ForceLandscape YES turns the window sideways (short-height layout checks).
            .onAppear {
                let scene = UIApplication.shared.connectedScenes.compactMap { $0 as? UIWindowScene }.first
                if UserDefaults.standard.bool(forKey: "ForceLandscape") {
                    scene?.requestGeometryUpdate(.iOS(interfaceOrientations: .landscapeRight))
                }
                // -WindowSize 466x678 shrinks the window below the status bar of an
                // iPad, with the size classes of that width (iPhone Duo screenshots).
                let size = (UserDefaults.standard.string(forKey: "WindowSize") ?? "").split(separator: "x").compactMap { Double($0) }
                if size.count == 2, let window = scene?.keyWindow {
                    window.frame = CGRect(x: 0, y: window.safeAreaInsets.top, width: size[0], height: size[1])
                    window.traitOverrides.horizontalSizeClass = size[0] < 600 ? .compact : .regular
                }
            }
            #endif
        }
    }
}
