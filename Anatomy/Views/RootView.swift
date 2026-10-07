//
//  RootView.swift
//  Anatomy
//

import SwiftUI

struct RootView: View {
    @Environment(AppModel.self) private var app

    var body: some View {
        @Bindable var app = app
        TabView(selection: $app.tab) {
            Tab("Atlas", systemImage: "figure.arms.open", value: AppModel.Tab.atlas) {
                AtlasView()
            }
            Tab("Sistemler", systemImage: "square.grid.2x2.fill", value: AppModel.Tab.systems) {
                SystemsView()
            }
            Tab("Çalış", systemImage: "brain", value: AppModel.Tab.study) {
                StudyView()
            }
            Tab("Kitaplığım", systemImage: "books.vertical.fill", value: AppModel.Tab.library) {
                LibraryView()
            }
            Tab(value: AppModel.Tab.search, role: .search) {
                SearchView()
            }
        }
        .tabViewStyle(.sidebarAdaptable)
    }
}
