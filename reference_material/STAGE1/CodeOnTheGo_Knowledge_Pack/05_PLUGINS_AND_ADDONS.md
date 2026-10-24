# 5. Plugins and Add-ons

## 5.1 Why plugins exist
CoGo's plugin system allows optional capabilities to be installed separately instead of bundling every feature into the base IDE. The organization maintains a public add-ons repository. The core repo includes `plugin-api`, `plugin-api:plugin-builder`, and `plugin-manager`.

The plugin authoring guide describes a plugin as a standalone Android module that builds to a `.cgp` file, which is a renamed APK. The closest in-tree example noted by the guide is `apk-viewer-plugin/`.

## 5.2 Plugin project structure
A documented recommended shape is:
```text
my-plugin/
├── build.gradle.kts
├── proguard-rules.pro
├── settings.gradle.kts
└── src/main/
    ├── AndroidManifest.xml
    └── assets/
        ├── icon_day.png
        └── icon_night.png
```
Real plugins will add Kotlin/Java source, resources and any required assets. Use the current authoring guide and sample plugin rather than treating this abbreviated tree as a complete template.

## 5.3 Manifest metadata and compatibility
Plugin metadata is part of the `AndroidManifest.xml` contract. The API changelog documents:
- `plugin.min_ide_version`
- `plugin.max_ide_version`
- `plugin.sidebar_items`
- plugin metadata and lifecycle contracts
- version mapping using `YY.WW` format, e.g. `26.30` means ISO year 2026, week 30.

The changelog says the minimum version is enforced at install time today, while maximum is parsed but advisory. Always verify current behavior before relying on that detail.

A plugin should set `plugin.min_ide_version` to the earliest CoGo release that contains every capability it uses. Read the API changelog for breaking entries at or below the target compatibility floor.

## 5.4 Lifecycle and services
The documented plugin foundation includes:
- `IPlugin` lifecycle methods: `initialize`, `activate`, `deactivate`, `dispose`.
- `PluginContext`, `ServiceRegistry`, `ResourceManager`, `PluginLogger`, `PluginMetadata`, `PluginPermission`.
- Extension points such as `UIExtension`, `EditorExtension`, `EditorTabExtension`, `ProjectExtension`, and `DocumentationExtension`.
- Core services including `IdeProjectService`, `IdeEditorService`, `IdeUIService`, `IdeBuildService`, `IdeFileService`, `IdeEditorTabService`, and `IdeTooltipService`.

The API changelog describes later additions such as cross-plugin services/lifecycle observation, inline editor suggestions, dynamic toolbar icons, module-specific build context, project-search providers and plugin-contributed AI agent tools.

## 5.5 Plugin API compatibility lessons
- Treat the public API as a versioned contract, not as an implementation detail.
- Use the official `plugin-api` dependency and builder plugin rather than copying internal host classes into a plugin.
- Avoid duplicating types that must cross plugin classloader boundaries. The changelog specifically notes that host-defined types are needed for shared contracts because plugins have their own classloaders.
- Check API changelog and compatibility metadata before adopting recent APIs.
- Rebuild and test against the actual target CoGo version.
- Handle missing optional services and permission failures.
- Avoid depending on private app implementation classes when a public API exists.

## 5.6 Build basics
The changelog documents on-device Maven resolution for plugin API and builder artifacts, with example coordinates:
```kotlin
dependencies {
    compileOnly("com.itsaky.androidide:plugin-api:1.0.0")
}

plugins {
    id("com.itsaky.androidide.plugins.build") version "1.0.0"
}
```
This example is version-specific; confirm current documentation and repository configuration before copying it.

The add-ons repository describes standalone plugin projects, each building a `.cgp` via `assemblePlugin`, and a publishing workflow that builds against the core repository's `plugin-api-latest` release and publishes a catalog.

## 5.7 Plugin security and reliability checklist
- Request only permissions needed by the feature.
- Validate all external/user-controlled file paths and input.
- Avoid executing untrusted downloaded code or shell commands.
- Avoid hard-coded secrets in source or build configuration.
- Fail gracefully if a service is unavailable.
- Ensure lifecycle cleanup removes listeners, callbacks and registered services.
- Avoid blocking the UI thread.
- Check plugin compatibility before using recent APIs.
- Include build provenance and version information where supported.
- Test install, activation, deactivation, update and uninstall paths.

## 5.8 Plugin API evolution snapshot
The public changelog is a living history. Examples visible in the researched source include:
- Foundation around release 26.02.
- API-stability baseline and module-specific context/task execution in 26.28.
- Cross-plugin services and inline editor suggestions in 26.29.
- Project-search providers in 26.30.
- Maven-coordinate support for API/builder on-device in 26.31.
- Plugin-contributed agent tools in 26.33.
- Build provenance metadata in 26.37.
- Embedding backend capability in 26.40.
- An unreleased 26.41 entry in the inspected branch.

This is a snapshot, not a compatibility promise. The release branch and `stage` may differ.
