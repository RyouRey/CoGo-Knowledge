# 1. Pinned Source Index

## 1.1 Release identity
- Tag: `26.40`
- Commit: `2b0b6cdd10fb9af948aa989b46e07054f65f292b`
- Release page: https://github.com/appdevforall/CodeOnTheGo/releases/tag/26.40
- Published: 2026-09-29
- Release notes include Kotlin snippets, a flattened dependency graph, plugin embedding capability, project-creation Git initialization, template tooltips, and Kotlin breakpoint/stepping work.

## 1.2 Files directly inspected
| Source file | Purpose | Blob SHA | Selected anchors |
|---|---|---|---|
| `ARCHITECTURE.md` | Architecture constraints and end-to-end flows | `8706f7553ea4b43bff78bf224feb4ba2668fdeb8` | Overview; Core Architecture; deep-link flow |
| `settings.gradle.kts` | Modules, composite builds, repository policy | `3d781b0f9eccf511303bbe7047cdb38435fe4676` | `dependencyResolutionManagement`; `include` |
| `gradle/libs.versions.toml` | Dependency/version catalog | `a0d5ac5e88444344f0481490f5a74fda55a65e28` | `[versions]`; `[libraries]` |
| `app/src/main/java/com/itsaky/androidide/models/DeepLinkRequest.kt` | URL parser/writer | `53d312cf2024b066d4e2431b905e82867ec6c746` | `MAX_LINK_PATH_LENGTH` L84; `parse` L155; `buildUrl` L305 |
| `app/src/main/java/com/itsaky/androidide/activities/DeepLinkActivity.kt` | Exported App Link trampoline | `b5ead707b035cb8204cbd12f2c63edfa2eddf0e1` | `onCreate` L49; readiness gate L62; parse call L82 |
| `app/src/test/java/com/itsaky/androidide/models/DeepLinkRequestTest.kt` | Parser regression tests | `af7ec4db8f3f83bebcaa7062fed18a33593de177` | project-only L31; reserved keyword L86; ambiguous file L156 |
| `common/src/test/java/com/itsaky/androidide/utils/PathTraversalTest.kt` | Contained-path regression tests | `1d33d6fae5a3fa566138fa0623d0a07b14088857` | `..` rejection L48; NUL L89; symlink escape L151 |
| `plugin-api/src/main/kotlin/com/itsaky/androidide/plugins/IPlugin.kt` | Public plugin lifecycle and metadata model | `c54581cc1f6f777ce9ecc137dea3517dcccd17ef` | `IPlugin`; `PluginMetadata`; `PluginPermission` |
| `plugin-manager/src/main/kotlin/com/itsaky/androidide/plugins/manager/loaders/PluginLoader.kt` | Plugin resources/classes/native libs | `7db58f76cfe33b67c69bf99f4eda7402d2471a91` | resources L34; classloader L94; native extraction L150 |
| `plugin-manager/src/main/kotlin/com/itsaky/androidide/plugins/manager/core/PluginManager.kt` | Plugin discovery/loading/activation | `bcd2d84d6603a7a907fd05d996600b944296b77f` | `loadPlugins` L379; loader call L606; activation L706 |
| `app/src/main/java/com/itsaky/androidide/services/builder/GradleBuildService.kt` | Build service/tooling API bridge | `121356f0cc5a4772acade7944cf3bbbba6542ef5` | class L104; task classification L186; build ID L197; `onCreate` L258 |
| `docs/PLUGIN_API_CHANGELOG.md` | Plugin API capability/version map | `9b79639203ce8d566c51d799be740d1b6aea6475` | compatibility guidance; 26.40 embedding capability |
| `docs/PLUGIN_AUTHORING.md` | Plugin build and metadata contract | `4a2bbeca71fb9575fce2a14b989ae3428f11d771` | `.cgp`; build plugins; metadata table |

## 1.3 Canonical pinned links
- Deep-link parser: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/app/src/main/java/com/itsaky/androidide/models/DeepLinkRequest.kt
- Deep-link entry activity: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/app/src/main/java/com/itsaky/androidide/activities/DeepLinkActivity.kt
- Deep-link tests: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/app/src/test/java/com/itsaky/androidide/models/DeepLinkRequestTest.kt
- Path traversal tests: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/common/src/test/java/com/itsaky/androidide/utils/PathTraversalTest.kt
- Plugin interface: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/plugin-api/src/main/kotlin/com/itsaky/androidide/plugins/IPlugin.kt
- Plugin loader: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/plugin-manager/src/main/kotlin/com/itsaky/androidide/plugins/manager/loaders/PluginLoader.kt
- Plugin manager: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/plugin-manager/src/main/kotlin/com/itsaky/androidide/plugins/manager/core/PluginManager.kt
- Gradle build service: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/app/src/main/java/com/itsaky/androidide/services/builder/GradleBuildService.kt
- Plugin API changelog: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/docs/PLUGIN_API_CHANGELOG.md
- Plugin authoring: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/docs/PLUGIN_AUTHORING.md
