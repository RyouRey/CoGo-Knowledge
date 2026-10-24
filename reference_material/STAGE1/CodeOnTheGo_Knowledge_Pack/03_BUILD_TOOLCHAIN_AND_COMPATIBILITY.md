# 3. Build Toolchain and Compatibility

## 3.1 Toolchain overview
CoGo bundles an Android development environment that includes JDK 21 and Kotlin 1.9.2, and runs Gradle builds on-device. Projects still define their own Gradle wrapper, Android Gradle Plugin (AGP), SDK levels, Java/Kotlin language options, plugins and dependencies. Therefore, the IDE's bundled tools and a project's declared build stack must be compatible.

## 3.2 Current documented compatibility snapshot
The official product page and compatibility discussion surfaced these values:
- Android OS minimum: Android 9.
- CPU: 32-bit ARM (`armeabi-v7a`) and 64-bit ARM (`arm64-v8a`).
- Approximate storage: 3.5 GB minimum.
- Approximate free RAM: 1.5 GB minimum; 4 GB free RAM recommended.
- JDK shipped: 21.
- Kotlin shipped: 1.9.2.
- AGP 8.11.0 is documented as the default shipped project setup; in that setup Java syntax can be configured up to Java 17.
- Device-compatibility discussion lists a supported AGP range at the time it was written; check the live compatibility page before selecting a version.

“Free RAM” means RAM available to apps at runtime, not the device's advertised total RAM. Storage estimates include downloaded/installed assets and build workspace headroom, and are approximate.

## 3.3 CoGo's own SDK configuration versus apps it builds
The architecture notes state that CoGo itself uses:
- `COMPILE_SDK=36`
- `MIN_SDK=28`
- `TARGET_SDK=28`
- `MIN_SDK_FOR_APPS_BUILT_WITH_COGO=16` as the floor for generated apps, distinct from CoGo's own minimum.

These are repository architecture facts from the inspected branch, not universal settings users should copy into every app.

The repository deliberately pins its own target SDK to 28 because higher target levels enforce W^X (write XOR execute) restrictions that block executing code from app-writable files. That conflicts with an IDE's need to execute bundled/installed toolchain components and user build tools. This is a product-specific constraint and should not be copied blindly into ordinary consumer apps.

## 3.4 ABI variants
The repository centralizes `v7` and `v8` product flavors:
- `v7` → `armeabi-v7a`
- `v8` → `arm64-v8a`

For CoGo's own build, tasks may look like:
- `assembleV7Debug`
- `assembleV8Debug`
- `assembleV7Release`
- `assembleV8Release`

There is intentionally no flavorless `assembleDebug` for modules covered by the ABI flavor setup. The plugin API module is an exception to the flavor rule.

## 3.5 Why builds fail
Common compatibility classes:
1. **Gradle/AGP mismatch** — the wrapper and AGP version are incompatible.
2. **Java version mismatch** — source/target compatibility or Gradle runtime requirements differ.
3. **Kotlin/AGP mismatch** — Kotlin Gradle plugin and AGP constraints conflict.
4. **Missing SDK/platform/build tools** — the project requests components not present locally.
5. **Dependency resolution** — artifact not cached and no network, repository unavailable, or coordinates invalid.
6. **Native ABI mismatch** — dependency contains only an ABI not supported by the device/build variant.
7. **Insufficient memory/storage** — daemon crashes, process killed, disk-full errors or long GC pauses.
8. **Toolchain migration** — old project assumptions no longer match new CoGo core stack.
9. **Plugin compatibility** — plugin was built against a newer/older API contract.
10. **Configuration/plugin errors** — syntax or configuration errors in Gradle files.

## 3.6 Breaking toolchain migration
The official page warns that release 26.38 and later upgraded the core development stack, and projects created with 26.37 or earlier may fail to build until migrated. This affects both 32-bit and 64-bit devices. The proper response is to follow the official migration guide and release notes for the exact version, not to randomly downgrade Gradle or change AGP until the error disappears.

Suggested migration checklist:
- Record the current CoGo version and device ABI.
- Back up the project and version-control state.
- Read the release notes and migration guide for the upgrade boundary.
- Identify the project Gradle wrapper, AGP, Kotlin plugin and Java configuration.
- Apply the documented migration steps.
- Sync/configure first; do not immediately change unrelated dependencies.
- Run a clean build for the correct variant.
- Install and smoke-test the resulting APK.
- Keep the build log and changes if reporting a regression.

## 3.7 Offline behavior and dependency caching
A local build can be offline only if required SDK components, Gradle distribution, Maven artifacts, plugin artifacts and other assets are already available locally. First-time setup and uncached dependencies can require network access. Large CoGo assets are documented as external to the main repository and downloaded/reconstructed during build/release workflows.

Do not equate “offline-capable IDE” with “every arbitrary project builds offline.” A project that introduces a dependency not in cache generally needs connectivity or a previously provisioned artifact.

## 3.8 Native assets and APK size
The architecture notes describe per-ABI native assets, including llama.cpp integration, and a specific packaging optimization for native `.so` libraries. `android:extractNativeLibs="true"` is required for some executable native components to be materialized in the app's native library directory. The post-build APK recompression step must preserve the intended compression behavior; an incorrect no-compress list can undo size savings.

This is a useful contributor lesson: APK packaging settings may affect runtime execution and size, not just cosmetic archive details. Validate release and CI packaging, not only a local debug build.

## 3.9 Diagnostic sequence for build errors
1. Capture the complete first error, not just the final “build failed.”
2. Identify whether the failure occurs during Gradle startup, project sync, dependency resolution, compilation, dexing, packaging or install.
3. Record CoGo version, Android version, ABI, AGP, Gradle wrapper, Kotlin plugin and Java configuration.
4. Determine whether the project is old enough to cross the 26.38 migration boundary.
5. Check disk space and available RAM.
6. Retry with network if the error indicates an uncached dependency; otherwise don't assume network will fix it.
7. Change one variable at a time.
8. Rebuild the same variant and preserve before/after logs.
