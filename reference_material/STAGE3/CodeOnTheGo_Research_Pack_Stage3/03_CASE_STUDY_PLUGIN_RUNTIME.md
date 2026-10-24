# 3. Case Study — Plugin Runtime

## 3.1 Main contracts
The public interface in `plugin-api/.../IPlugin.kt` declares:
```kotlin
interface IPlugin {
    fun initialize(context: PluginContext): Boolean
    fun activate(): Boolean
    fun deactivate(): Boolean
    fun dispose()
}
```
The same file declares `PluginMetadata`, including identity/version, minimum IDE version, permissions, dependencies, theme icon paths, and optional VCS/build provenance. `PluginPermission` includes filesystem, network, system-command, IDE-settings, project-structure, native-code and IDE-environment permissions.

Pinned source:
https://github.com/appdevforall/CodeOnTheGo/blob/26.40/plugin-api/src/main/kotlin/com/itsaky/androidide/plugins/IPlugin.kt

## 3.2 Loader behavior
`PluginLoader.kt` provides several distinct responsibilities:
- `loadPluginResources()` starts around line 34; it reads package metadata from the APK and tries `PackageManager` resources, with a manual `AssetManager` fallback if needed.
- `loadPluginClasses()` starts around line 94; it creates a `DexClassLoader` using the plugin APK path, an optimized dex cache directory, optional native library path and a caller-supplied parent classloader.
- `extractNativeLibs()` starts around line 150; it extracts `.so` entries under the device's first supported ABI from the plugin archive into an app-private directory, checking normalized output paths remain under the target directory.

Pinned source:
https://github.com/appdevforall/CodeOnTheGo/blob/26.40/plugin-manager/src/main/kotlin/com/itsaky/androidide/plugins/manager/loaders/PluginLoader.kt

## 3.3 Plugin manager behavior
The inspected `PluginManager.kt`:
- stores loaded plugin instances and plugin state in concurrent maps;
- has a plugin registry, plugin security manager, shared service registry and lifecycle dispatcher;
- creates the plugin directory under app-private files;
- performs loading work in an IO coroutine in `loadPlugins()` (around line 379);
- creates a classloader via `pluginLoader.loadPluginClasses(...)` (around line 606);
- instantiates the declared plugin main class as `IPlugin`;
- calls `activate()` in the load path (around line 706).

The complete sequence includes more logic than these anchors show. Before changing lifecycle behavior, inspect the entire method and all error/cleanup paths.

Pinned source:
https://github.com/appdevforall/CodeOnTheGo/blob/26.40/plugin-manager/src/main/kotlin/com/itsaky/androidide/plugins/manager/core/PluginManager.kt

## 3.4 Lifecycle and failure questions to trace next
- Does a failed `initialize()` prevent `activate()`?
- What happens when `activate()` returns false?
- Are extension registrations rolled back after an exception?
- Does `deactivate()` always run before `dispose()`?
- Are callbacks/services removed when a plugin crashes?
- Are native libraries deleted on uninstall?
- Are dependency plugins loaded in a deterministic order?
- Are plugin metadata compatibility checks performed before class loading?
- How are permissions checked at service invocation time versus installation time?
- Is a failed plugin quarantined, retried or automatically reloaded?

Do not infer answers solely from interface names. Trace all branches and tests at the pinned tag.

## 3.5 Classloader implications
`DexClassLoader` receives a parent classloader supplied by the host. The plugin API changelog warns that a plugin should not bundle duplicate copies of host-shared contract classes. A class with the same binary name loaded by a different classloader can be a different runtime type.

Practical consequences:
- plugin implementation classes can be loaded from the plugin artifact;
- API interfaces that cross the host/plugin boundary should resolve to host-provided definitions;
- avoid shading or repackaging the public plugin API into `.cgp`;
- test a real built `.cgp` on the target IDE, not just compilation against stubs.

## 3.6 Proposed plugin regression tests (not claimed to exist)
- corrupt/non-APK `.cgp`;
- missing `plugin.main_class`;
- main class not implementing `IPlugin`;
- constructor exception;
- `initialize()` returns false or throws;
- `activate()` returns false or throws;
- permission denied at each service boundary;
- dependency cycle/missing dependency;
- repeated activate/deactivate without duplicate callbacks;
- plugin unload while an asynchronous tool call is running;
- native library entry with unexpected path segments;
- same API class accidentally bundled into plugin APK;
- provenance absent vs present;
- update plugin while old classloader is still referenced.
