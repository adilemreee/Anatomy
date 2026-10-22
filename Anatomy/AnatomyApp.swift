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
        }
    }
}
