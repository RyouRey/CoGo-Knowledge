# Android Project File Map for CoGo

This is a conventional Android project map, not a guarantee that every template has every file. CoGo templates and the user's existing project take precedence.

## Common paths and responsibilities

| Path | Role | Change it when |
|---|---|---|
| `settings.gradle` / `settings.gradle.kts` | Project name, included modules, plugin/dependency repositories in some setups | Adding modules or changing centralized repository configuration |
| `build.gradle` / `build.gradle.kts` at root | Shared plugins, buildscript classpath, root configuration | Toolchain/plugin changes or shared configuration |
| `gradle/libs.versions.toml` | Optional version catalog | Project already uses aliases such as `libs.plugins...` / `libs.androidx...` |
| `gradle/wrapper/gradle-wrapper.properties` | Gradle distribution URL/version | Only when migration/compatibility requires it; avoid arbitrary changes |
| `gradle.properties` | Gradle/Android build flags | Memory, AndroidX, or feature-specific build configuration |
| `local.properties` | Local machine/IDE-specific properties; sometimes signing properties in documented setup | Only when required; do not commit secrets or machine-specific paths |
| `app/build.gradle` / `app/build.gradle.kts` | App module plugins, namespace, SDK levels, dependencies, build types, compile options | Most app-specific Gradle changes |
| `app/src/main/AndroidManifest.xml` | App components, intent filters, app-level permissions, metadata | Permissions, Activities/services/providers, deep links, app configuration |
| `app/src/main/java/<package>/...` | Java/Kotlin source in many templates; directory may also be named `kotlin` | Activities, fragments, ViewModels, repositories, helpers |
| `app/src/main/res/layout/*.xml` | XML View layouts | Screen layout for XML/View-based UI |
| `app/src/main/res/values/strings.xml` | User-visible strings | Add/edit text and localization resources |
| `app/src/main/res/values/colors.xml` | Color resources in templates that use them | Centralize colors if the project follows this pattern |
| `app/src/main/res/values/themes.xml` / `styles.xml` | Theme/style resources | Theme, typography, window styling |
| `app/src/main/res/drawable/` | Vector drawables, shape drawables, images | Icons and drawable resources |
| `app/src/main/res/mipmap-*/` | Launcher icons | App icon assets |
| `app/src/test/` | Local unit tests | Logic tests not requiring a device UI |
| `app/src/androidTest/` | Instrumented tests | Tests that need Android runtime/device |
| `app/build/outputs/apk/debug/` | Common debug APK output path | Locate debug APK after successful build |
| `app/build/outputs/apk/release/` | Common release APK output path | Locate release APK after successful release build |

CoGo Help documents APKs under `CodeOnTheGoProjects > AppName > app > build > outputs > apk > debug or release > app`. Actual filename and variant subdirectory may differ; inspect the output panel/build result rather than assuming one exact filename.

## Placement rules

- **Java/Kotlin code** belongs in the source set and package path that matches its `package` declaration. Don't put a Java class in `res/`.
- **XML layouts** belong under `app/src/main/res/layout/`; resource filenames should be lowercase with underscores.
- **Strings/colors/themes** belong in the appropriate `res/values/` XML resource files when the project uses resource-based UI.
- **Images/vector drawables** belong in `res/drawable/` or launcher assets in `res/mipmap-*` as appropriate.
- **Manifest declarations** belong in `AndroidManifest.xml`, but don't add permissions/components without checking whether they already exist.
- **Gradle dependency declarations** belong in the app module's build file unless the project uses a version catalog or central convention. If a catalog is used, update the catalog and module declaration consistently.
- **Compose UI** is normally Kotlin source (`@Composable` functions); do not create XML layouts just because an XML template normally uses them.

## Minimal file plan format for AI responses

For a feature, give a table with `Action`, `Path`, `Purpose`, and `Why`. Mark each path as `CREATE`, `REPLACE`, or `EDIT`. Explicitly list files that must **not** be changed. For a full replacement, provide the entire final file. For an edit, provide an unambiguous insertion point or the complete final file when that is safer.

## Example: a small XML screen

- `EDIT app/src/main/java/id/example/myapp/MainActivity.java` — bind controls and handle clicks.
- `EDIT app/src/main/res/layout/activity_main.xml` — declare controls and constraints/layout.
- `EDIT app/src/main/res/values/strings.xml` — add labels if strings resources are used.
- `EDIT app/src/main/AndroidManifest.xml` only if an activity/permission declaration is genuinely needed.
- `EDIT app/build.gradle` only if a new dependency or build setting is needed.

This is an illustrative plan. Inspect the actual template first; it may use different activity names, package paths, binding strategy, or DSL.
