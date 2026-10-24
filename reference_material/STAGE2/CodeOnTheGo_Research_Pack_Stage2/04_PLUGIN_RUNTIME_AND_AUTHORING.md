# 4. Plugin Runtime and Authoring

## 4.1 Plugin packaging model
The official authoring guide describes a plugin as a standalone Android module that builds to a `.cgp` artifact, a renamed APK. The in-tree `apk-viewer-plugin/` is identified as the closest example. A typical project contains Gradle configuration, an Android manifest, Kotlin/Java code, resources and theme-aware icon assets.

The public add-ons repository has a distinct repository-level workflow; some of its plugins refer to built `plugin-api.jar` and `gradle-plugin.jar` under a shared `libs/` folder. Do not assume a copied plugin subdirectory is self-contained unless its build setup explicitly is.

## 4.2 Public API components
The plugin API changelog documents the foundational contract:
- `IPlugin`: `initialize`, `activate`, `deactivate`, `dispose`;
- `PluginContext`;
- `ServiceRegistry`;
- `ResourceManager`;
- `PluginLogger`;
- `PluginMetadata`;
- `PluginPermission`;
- extension interfaces such as `UIExtension`, `EditorExtension`, `EditorTabExtension`, `ProjectExtension`, `DocumentationExtension`;
- host services such as `IdeProjectService`, `IdeEditorService`, `IdeUIService`, `IdeBuildService`, `IdeFileService`, `IdeEditorTabService`, `IdeTooltipService`.

The exact public API must be read from `plugin-api` and the ABI dump for the target version, not inferred only from this list.

## 4.3 Lifecycle semantics (design interpretation)
- **initialize:** receive host context and set up non-active plugin state.
- **activate:** register active services, listeners and extension contributions.
- **deactivate:** unregister or stop active contributions and release active resources.
- **dispose:** final cleanup when the plugin is being torn down.

These descriptions are a practical mental model; consult actual interface KDoc and runtime implementation for precise ordering, threading and failure behavior.

## 4.4 Version compatibility
Plugin metadata includes `plugin.min_ide_version` and `plugin.max_ide_version`. The changelog documents a `YY.WW` format (`26.30` means ISO year 2026, week 30). In the documented snapshot, minimum version is enforced during installation while maximum is parsed but advisory.

Compatibility workflow:
1. List every API capability the plugin uses.
2. Find the earliest release week for each capability in the API changelog.
3. Set minimum version to the highest required floor.
4. Read all breaking entries at or below that floor.
5. Compile against the intended plugin API/builder.
6. Install and test on the actual target CoGo version.
7. Test missing service/permission/error cases.
8. Recompile when binary-incompatible API changes are documented.

## 4.5 Maven coordinates and builder
The authoring guide documents:
```kotlin
dependencies {
    compileOnly("com.itsaky.androidide:plugin-api:1.0.0")
}
```
and a builder plugin:
```kotlin
plugins {
    id("com.itsaky.androidide.plugins.build")
}
```
The guide also shows `pluginBuilder { pluginName = "my-plugin"; pluginVersion = "1.0.0" }`. Exact plugin versions and Gradle plugin setup depend on the current authoring guide and the environment. Do not blindly combine examples from different release generations.

## 4.6 API evolution examples
The public changelog includes:
- foundation and extension points (26.02 genesis);
- API-stability baseline and ABI dump (26.28);
- cross-plugin services, lifecycle observation, inline editor suggestions and dynamic toolbar icons (26.29);
- project-search providers (26.30);
- on-device Maven-coordinate resolution for API/builder (26.31);
- plugin-contributed AI agent tools (26.33);
- build provenance metadata in `.cgp` (26.37);
- embedding backend capability (26.40);
- unreleased 26.41 entries on the inspected `stage` branch.

A release-week label is not proof that a capability is in every build based on `stage`; confirm release tags.

## 4.7 Classloader and shared-contract hazard
The changelog explicitly explains why plugin-shared contracts must be defined by the host. Each `.cgp` can be loaded in its own classloader with the host as parent. If each plugin bundles its own copy of a shared interface/class, the code can compile yet fail at runtime with type incompatibility or `ClassCastException`.

General rule: use the host-provided public API type for contracts that cross plugin boundaries; avoid shading/duplicating those contract classes into plugin artifacts.

## 4.8 Agent tool extension
The changelog describes a host-owned registry for plugin-contributed agent tools. A plugin registers a tool source on activation and unregisters it on deactivation. A tool specification describes the operation and invocation receives a structured request; the outcome returns a result. Exact schemas must be fetched from the API source for the target version.

Security implications:
- validate arguments on the host side;
- check permissions;
- constrain filesystem paths;
- do not execute arbitrary model-generated shell text;
- require confirmation for destructive or externally visible actions;
- surface failures to the user;
- unregister tools on deactivation.

## 4.9 Plugin security/reliability checklist
- Declare only necessary permissions.
- Validate every path, URI, package name and external input.
- Keep secrets out of source, manifests and logs.
- Do not assume activation succeeded merely because installation succeeded.
- Avoid blocking the UI thread.
- Unregister listeners/services during deactivation.
- Handle missing optional host services.
- Test upgrade/downgrade and uninstall/reinstall behavior.
- Track source commit/build timestamp when the builder supports provenance.
- Keep plugin minimum IDE version aligned with used API capabilities.
