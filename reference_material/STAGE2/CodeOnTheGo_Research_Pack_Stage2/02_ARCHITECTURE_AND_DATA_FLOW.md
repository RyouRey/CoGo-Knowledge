# 2. Architecture and Data Flow

## 2.1 High-level model
CoGo is a layered, subsystem-oriented Android application. `app` is the integration point; most other Gradle modules are libraries composed by the app. The architecture document describes the project as predominantly Android Views/Fragments today, while newer feature surfaces use UDF with ViewModel, StateFlow, repositories and Koin. New UI is intended to use Jetpack Compose.

## 2.2 UDF flow for newer features
```text
User action / UI intent
        ↓
Activity / Fragment / Compose UI
        ↓
ViewModel (viewModelScope)
        ↓
Repository
        ↓
Data source / service
        ↓
Result/state
        ↑
StateFlow for durable UI state
SharedFlow for one-shot UI effects
```

- **UI:** renders state and emits intents/events; it should not own business logic or blocking I/O.
- **ViewModel:** coordinates the screen, exposes immutable state and launches asynchronous work.
- **Repository:** hides data-source details and threading from UI/ViewModel.
- **Data source:** Room/DAO, SQLite, filesystem/preferences, build tooling, external AI client, local model runtime, or Git implementation.
- **StateFlow:** appropriate for current screen state that subscribers need to render.
- **SharedFlow:** used for transient effects such as navigation, toast/snackbar or dialog requests.
- **Koin:** dependency injection, including modules such as `coreModule`, `pluginModule`, and `templateModule`.

## 2.3 Legacy side channels
Older UI paths may use LiveData and GreenRobot EventBus. The architecture explicitly treats EventBus as a cross-subsystem integration side-channel for signals such as build progress, installation results and editor events. It should not replace local ViewModel state within a single screen.

When debugging event-driven behavior, identify:
- event class and producer;
- event bus registration/subscription;
- thread mode;
- event lifecycle and unregister behavior;
- consumers that transform it into screen state.

## 2.4 Data-source examples
Architecture documentation names:
- `RecentProjectRoomDatabase` and its DAO for recent-project data;
- `DocumentationContentSource` using `SQLiteOpenHelper` for documentation storage;
- filesystem/preferences;
- tooling API for on-device Gradle;
- `GeminiRepository` for Gemini-related work;
- `PluginRepository` and `TemplateRepository`;
- `BreakpointRepository`;
- llama.cpp integration;
- JGit.

These are source-navigation anchors. To assert exact schema or runtime behavior, inspect the actual class and its tests at a pinned commit.

## 2.5 Deep links as an example of multi-layer control flow
The architecture document gives a detailed example for project/file links:
1. `DeepLinkActivity` is a UI-less trampoline for the official `device/open/project/...` link form.
2. It parses the URL into a request containing project identity and optional file/line/column.
3. It checks whether an editor is already active and routes to the main/editor activity.
4. `EditorHandlerActivity` handles the request differently if the same project is open, another project is open, or no project is open.
5. For a different project, the existing close-confirmation flow is respected.
6. Pending navigation may be handed off from `onDestroy()` to avoid races with `singleTask` activity delivery.
7. When a project is opened cold, file navigation waits until project sync succeeds.
8. The file path is checked by `PathTraversal.resolveWithinDirectory`, which guards against traversal and symlink escape.
9. The URL writer validates its own output by parsing it back, preventing ambiguous path segments from being misinterpreted as line/column metadata.

This example is valuable because it shows Android lifecycle, asynchronous Gradle sync, navigation, user confirmation and filesystem trust boundaries interacting in one feature.

## 2.6 Architecture boundaries and dependency direction
- `app` depends inward on libraries; libraries must not depend on `app`.
- Vendored/forked dependencies are substituted through composite builds rather than imported ad hoc.
- Android module configuration is centralized in `composite-builds/build-logic`.
- Repository declarations are centralized in `settings.gradle.kts`, using `RepositoriesMode.FAIL_ON_PROJECT_REPOS`.
- The version catalog is the first place to check before adding dependencies.
- `common-compose` is intended as a leaf shared UI/theming layer, allowing modules to opt in without forcing Compose dependencies on unrelated modules.

## 2.7 Design guidance for a new feature
1. Define the feature's data/state model before its UI.
2. Use immutable/sealed UI state, UI events and UI effects where consistent with the subsystem.
3. Put asynchronous work in `viewModelScope` and use IO dispatchers for blocking I/O.
4. Put data access behind a repository when it is non-trivial or has multiple backends.
5. Inject dependencies through Koin following nearby patterns.
6. Collect state lifecycle-aware.
7. Use Compose for new UI unless the local subsystem has a documented reason not to.
8. Keep EventBus for cross-module events rather than screen-local state.
9. Add tests for state transitions, cancellation, errors and lifecycle.
10. Validate accessibility, configuration changes and resource constraints on a real device.

## 2.8 Anti-patterns
- View/UI performs network, filesystem or Gradle work directly.
- Mutable state is exposed to UI without a stable contract.
- EventBus is used for every local button click.
- A library module imports `app` classes.
- New dependencies duplicate already-substituted composite-build projects.
- File paths from deep links, plugins or AI tools are trusted without canonical/path containment checks.
- Code is copied from a legacy screen without checking whether the feature is being migrated to UDF.
