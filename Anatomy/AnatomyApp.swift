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
            RootView()
                .environment(app)
        }
    }
}
