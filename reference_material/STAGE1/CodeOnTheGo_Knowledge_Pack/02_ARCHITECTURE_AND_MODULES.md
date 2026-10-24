# 2. Architecture and Module Map

## 2.1 Architecture in one view
The project is a large layered Android application. Its architecture document explicitly notes that the app is mid-migration: much of the UI remains Android Views/Fragments, while newer features follow a more consistent Unidirectional Data Flow (UDF) architecture and new UI is expected to use Jetpack Compose.

Typical newer feature flow:

`UI → ViewModel → Repository → Data source`

- UI renders state and sends user intents/events.
- ViewModel owns screen state and launches work in `viewModelScope`.
- Repository hides data-source details and threading/IO from UI logic.
- Data sources include Room/SQLite, files/preferences, the on-device Gradle tooling API, and external/local clients.
- `StateFlow` carries durable screen state upward.
- `SharedFlow` is used for one-shot UI effects such as navigation, dialogs, or toasts.
- Koin supplies dependencies through modules such as `coreModule`, `pluginModule`, and `templateModule`.

Older areas may use `LiveData` and GreenRobot EventBus directly. EventBus is a cross-subsystem side channel for events such as build/install lifecycle and editor signals; the architecture notes caution against using it as a replacement for a ViewModel's local state.

## 2.2 Important architectural reality
Do not assume the entire repository follows one uniform pattern. The architecture document says the app is predominantly View-based today and is in migration. For a new feature, follow the current local conventions and architecture guidance instead of copying an older screen blindly.

## 2.3 Main module families
The repository is layer-and-subsystem oriented rather than purely feature-by-feature. The architecture document describes roughly 80 Gradle modules plus three included composite builds. Module counts can change.

| Area | Representative modules | Responsibility |
|---|---|---|
| Application integration | `app` | Activities, fragments, services, dependency injection, agent, web server and integration |
| Build engine | `subprojects:tooling-api*`, `gradle-plugin*`, `subprojects:projects`, `subprojects:builder-model-impl` | Runs real Gradle builds out-of-process and streams events/results |
| Language tooling | `lsp:*`, `lexers`, `editor*`, `editor-treesitter` | Language servers, indexing, syntax highlighting, code editing, document outline/refactoring |
| UI design tooling | `layouteditor`, `uidesigner`, `xml-inflater`, `vectormaster`, `compose-preview` | Visual/layout and vector tools; preview support |
| Terminal | `termux:termux-app`, `termux-shared`, `termux-view`, `termux-emulator` | Embedded terminal and shell experience |
| Plugin system | `plugin-api`, `plugin-api:plugin-builder`, `plugin-manager` | Public extension contract, build tooling and plugin management |
| On-device AI | `llama-api`, `llama-impl` | llama.cpp integration and per-ABI native packaging |
| Cross-cutting infrastructure | `common`, `common-ui`, `common-compose`, `eventbus*`, `logger`, `resources`, `preferences`, `shared` | Shared utilities, events, themes, logging and preferences |
| Testing | `testing:android`, `testing:unit`, `testing:lsp`, `testing:tooling`, `testing:common` | Shared test support split by subsystem |

The exact module list should be checked in `settings.gradle.kts` and the current repository tree.

## 2.4 Dependency rules
The architecture notes document these constraints:
- `app` depends inward on libraries; libraries must not depend on `app`.
- Use the existing vendored/forked dependencies supplied through composite builds rather than adding duplicate Maven coordinates.
- Android module configuration is centralized in `composite-builds/build-logic`.
- ABI flavors are centrally configured for Android modules.
- Repository declarations are centralized in settings, with `RepositoriesMode.FAIL_ON_PROJECT_REPOS`.
- Check `gradle/libs.versions.toml` before adding a dependency.

These rules matter because apparently small Gradle changes can affect dozens of modules or conflict with the repository's dependency substitution.

## 2.5 Build-system architecture
CoGo executes a real Gradle build for the user's Android project. The build engine is separated from the UI process through a tooling API and streams progress/events back to the IDE. This separation helps isolate the long-running build process and allows the UI to report progress.

Conceptual flow:
1. User opens a project.
2. IDE identifies project and module structure.
3. Gradle sync/configuration runs using the project's wrapper/configuration and the on-device environment.
4. The user invokes a Gradle task.
5. The tooling layer executes the build in a separate process.
6. Build output and lifecycle events return to the IDE.
7. User inspects errors/logs and iterates.
8. A successful build produces an APK/AAB or other configured artifact; install/deploy depends on task and project settings.

Exact task names depend on project configuration. For CoGo itself, ABI flavors mean tasks include variants such as `assembleV8Debug` and `assembleV7Release`, rather than a generic flavorless `assembleDebug`.

## 2.6 Persistence and data sources
Documented examples include:
- Room for queryable relational data such as recent projects.
- SQLite for some local content, including documentation storage.
- Filesystem and preferences/DataStore for local configuration.
- External clients such as Gemini SDK and JGit.
- Local llama.cpp inference.
- Tooling API for builds.

Repositories should mediate these sources in newer features so UI code is not tied to storage or networking details.

## 2.7 UI migration
- Existing UI: Activities, Fragments, Views, RecyclerView and Material Components.
- New UI: Jetpack Compose, with UDF/ViewModel/StateFlow retained.
- A production example mentioned by the architecture document is the Manager screen with Plugins/Templates tabs, `Scaffold`, `TabRow`, and `HorizontalPager`.
- Compose preview is for previewing the user's Compose code; do not confuse it with CoGo's own UI being entirely Compose.

## 2.8 Repository exploration order
Recommended source-reading order:
1. `README.md` — purpose, installation, contribution and license.
2. `ARCHITECTURE.md` — current system boundaries and conventions.
3. `CLAUDE.md` / agent instructions — repository-specific development commands and branch model.
4. `settings.gradle.kts` — module graph.
5. Root `build.gradle.kts`, `gradle/libs.versions.toml`, `composite-builds/build-logic`.
6. `app/` integration layer.
7. One subsystem end-to-end, e.g. plugin manager or a language service.
8. Relevant tests under `testing/`.
9. Git history/issues/PRs for the specific behavior.

## 2.9 Security-relevant architecture example
The architecture notes describe deep links that can request a project/file/line/column. File paths are user-controllable URL content, so the implementation uses a path-traversal/symlink guard rather than naïve path joining. This is a useful example of security-sensitive boundary validation inside an IDE: project paths and imported content must not be trusted just because they arrive through an internal-looking URL.
