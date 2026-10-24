# 3. Build Pipeline and Toolchain

## 3.1 Two distinct builds
A key distinction:
- **Building CoGo itself:** the repository build compiles the IDE and its modules, including ABI-specific variants and asset packaging.
- **Building a user's Android project inside CoGo:** the installed IDE runs a real Gradle build through its on-device tooling API in a separate process.

These workflows share concepts but differ in root project, task names, SDK configuration, dependency provisioning and output artifacts.

## 3.2 User-project build flow (conceptual)
```text
Open/create project
  → locate Gradle wrapper and settings
  → provision/select local SDK/toolchain
  → configure/sync Gradle project
  → choose task/variant
  → launch tooling API build in separate process
  → stream progress/results/events to IDE
  → compile Kotlin/Java and resources
  → dex/package/sign according to project config
  → APK/AAB artifact
  → install/run/debug
```
This is a conceptual flow derived from the architecture. The exact call chain, task model and event classes must be traced in source for a specific version.

## 3.3 Tooling API responsibility
The architecture assigns `subprojects:tooling-api*`, related Gradle plugin modules, project models and builder model implementation to the build engine. It runs a real Gradle build out-of-process and streams events back to the IDE.

For a build-progress bug, investigate:
- the UI action that initiates the task;
- task/variant selection;
- request model and execution API;
- process launch/environment;
- event model and event transport;
- event consumers and UI state;
- process cleanup/cancellation;
- error propagation and log capture.

## 3.4 CoGo repository build rules
`settings.gradle.kts`:
- enables type-safe project accessors;
- includes composite build logic and plugin builder;
- includes composite build dependencies;
- substitutes selected `com.itsaky.androidide.build:*` coordinates with local projects;
- centralizes dependency repositories and sets `FAIL_ON_PROJECT_REPOS`;
- includes the large module list.

Architecture docs say module configuration is centralized in `composite-builds/build-logic`. Each Android module except `:plugin-api` receives `v7` and `v8` ABI flavors. Therefore, CoGo build tasks can be ABI-specific (`assembleV8Debug`, `assembleV7Release`).

## 3.5 Toolchain facts in the inspected branch
Architecture documentation states the CoGo app build uses:
- `COMPILE_SDK=36`
- `MIN_SDK=28`
- `TARGET_SDK=28`
- generated apps can use a separate minimum SDK floor stated as 16.

The documented reason for CoGo's target SDK 28 is that newer target levels enforce W^X restrictions that conflict with an IDE's need to execute code/toolchain components from app-writable files. This is a CoGo-specific architectural constraint, not advice to set target SDK 28 in ordinary apps.

The version catalog in `stage` lists, among other values:
- AGP version alias `8.8.2`;
- Kotlin `2.3.0`;
- Koin Android `4.1.1`;
- Room `2.8.4`;
- Tree-sitter `4.3.2`;
- Sora editor `0.23.6`;
- JDK/source compatibility settings should be confirmed in the relevant module/build logic.

These repository versions differ in some respects from the previous package's older compatibility snapshot. Always distinguish the IDE's build configuration from its bundled user-project toolchain.

## 3.6 APK packaging and native libraries
The app build script contains packaging configuration for duplicate resources and native libraries. The inspected comments explain:
- debug variants can use uncompressed native libraries loaded from the APK;
- release/instrumentation bundled-asset variants override packaging to compress and extract native libraries at install time;
- post-build recompression must preserve intended native-library behavior.

A packaging change can affect both APK size and runtime loading. Validate the artifact after packaging/recompression, not only the Gradle task's exit code.

## 3.7 External assets and reproducibility
Architecture and repository instructions say large assets such as SDK/bootstrap archives, Gradle distributions, API jars, documentation databases and local Maven archives may be ignored by Git and fetched/reconstructed through build/release tasks. A local cached asset may be stale relative to the source of truth.

Before treating an on-disk binary/database as authoritative:
1. Check `git ls-files <path>`.
2. Check `git check-ignore -v <path>`.
3. Search build scripts for asset provisioning and source URL.
4. Record source/version/hash if available.
5. Do not infer that a clean Git checkout contains every required binary.

## 3.8 Common failure taxonomy
| Stage | Typical signal | First investigation |
|---|---|---|
| Gradle startup | wrapper/distribution cannot start | distribution availability, JDK, permissions |
| Project configuration | plugin/DSL exception | AGP/Gradle compatibility and build scripts |
| Dependency resolution | missing artifact or repository error | coordinates, repositories, cache/network |
| Source compilation | Kotlin/Java errors | compiler version, source and dependency API |
| Resource compilation | AAPT/resource errors | manifest, resource names, SDK components |
| DEX/package | duplicate classes, desugaring or packaging errors | dependency graph, packaging config, ABI |
| Install | package manager error | min SDK, ABI, signature/version conflict |
| Runtime | exception/native crash | logcat, permissions, initialization, native library |
| OS termination | process killed/no final Gradle exception | memory, storage, thermal/background limits |

## 3.9 Build-troubleshooting protocol
- Save the first causal error and full relevant stack trace.
- Record CoGo version, Android version, ABI, AGP, Gradle wrapper, Kotlin plugin and Java settings.
- Identify the failing phase before changing configuration.
- Check the 26.38+ migration boundary for projects created on 26.37 or earlier.
- Check free storage and available RAM.
- Determine whether a dependency is missing locally before concluding that source code is broken.
- Change one variable at a time and rebuild the same variant.
- Preserve the before/after configuration and logs.
