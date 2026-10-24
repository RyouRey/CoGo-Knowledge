# Sources — Stage 3

## Release pin
- Release: https://github.com/appdevforall/CodeOnTheGo/releases/tag/26.40
- Tag reference API: https://api.github.com/repos/appdevforall/CodeOnTheGo/git/ref/tags/26.40
- Commit: `2b0b6cdd10fb9af948aa989b46e07054f65f292b`

## Implementation
- Architecture: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/ARCHITECTURE.md
- Settings: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/settings.gradle.kts
- Version catalog: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/gradle/libs.versions.toml
- Deep-link model: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/app/src/main/java/com/itsaky/androidide/models/DeepLinkRequest.kt
- Deep-link entry activity: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/app/src/main/java/com/itsaky/androidide/activities/DeepLinkActivity.kt
- Deep-link parser tests: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/app/src/test/java/com/itsaky/androidide/models/DeepLinkRequestTest.kt
- Path traversal tests: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/common/src/test/java/com/itsaky/androidide/utils/PathTraversalTest.kt
- Plugin lifecycle API: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/plugin-api/src/main/kotlin/com/itsaky/androidide/plugins/IPlugin.kt
- Plugin loader: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/plugin-manager/src/main/kotlin/com/itsaky/androidide/plugins/manager/loaders/PluginLoader.kt
- Plugin manager: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/plugin-manager/src/main/kotlin/com/itsaky/androidide/plugins/manager/core/PluginManager.kt
- Gradle build service: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/app/src/main/java/com/itsaky/androidide/services/builder/GradleBuildService.kt
- Plugin API changelog: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/docs/PLUGIN_API_CHANGELOG.md
- Plugin authoring guide: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/docs/PLUGIN_AUTHORING.md

## Research status
Source files and selected tests were inspected at the release tag. The pack does not claim that tests were executed, that the repository was compiled, or that the review constitutes a formal security audit.
