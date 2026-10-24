# Sync, Build, Run Tasks, Quick Build, and APK Output

## Sync vs build

CoGo Help says project sync aligns the IDE's project model with Gradle. It saves unsaved changes, refreshes project structure/libraries/build settings, and reports details in Build Output. Run **Sync project** after changing dependencies, Gradle build files, or project settings.

A successful sync does not prove source code compiles; it only establishes that the project configuration/model was refreshed successfully.

## Run Gradle tasks from the UI

Official Help documents this flow:

1. Open the project slider.
2. Tap **Run tasks**.
3. Search/browse the task list.
4. Tap task names to select one or more.
5. Tap the green Run button.
6. Confirm selected tasks and run; results appear in Build Output.

Use task names that actually appear in the current project's task list. Do not assume a task exists in every module or build setup.

## Common task intentions

| Goal | Typical task name | Notes |
|---|---|---|
| Compile/build debug app | `assembleDebug` or the IDE's Build/Quick Run action | Prefer CoGo UI's documented Build/Quick Run for beginners |
| Build release variant | `assembleRelease` | Release signing/configuration must be valid |
| Run unit tests | `testDebugUnitTest` or variant-specific test task | Exact task depends on project/plugins/variants |
| Clean generated outputs | `clean` | Use when stale generated output is suspected; not a first fix for every error |
| Inspect dependencies | `dependencies` or variant-specific dependency task | Useful for conflicts; exact configurations vary |
| Inspect Java toolchains | module-specific `javaToolchains` task where available | Availability depends on Gradle/AGP/project |

Do not tell users to run all tasks. Choose the narrowest task that proves the next hypothesis. A normal app development loop usually needs Build/Quick Run, not every lint/test/release task on every edit.

## Build and launch using CoGo UI

CoGo Help documents:

1. Tap the **Build** button; monitor Build Output.
2. If successful, choose install.
3. Choose launch when prompted.
4. Android may show an installation/security prompt; follow device prompts carefully.
5. If already installed, use the project's **Launch app** option or the app drawer.

Current versions also have Quick Run (green triangle) and Quick Build; labels/placement can vary by release and preferences.

## Quick Build (CoGo 26.41 release notes)

Quick Build is experimental and requires enabling experimental features and restarting CoGo. It is intended for a launchable Android app with a single process, debug variant selected, and enough memory/storage. It does not support library/plugin projects or multi-process apps. The first Quick Build creates a proxy app and may take about as long as a normal first build; subsequent saved edits can be compiled and pushed into the running app quickly. Apps with background services may restart fully. Use normal Build/Quick Run for final verification and whenever Quick Build constraints don't fit.

## Find the APK

CoGo Help documents this conventional path:

`CodeOnTheGoProjects/<AppName>/app/build/outputs/apk/<debug-or-release>/app`

The actual artifact often has `.apk` extension and may be named differently depending on variant/build configuration. Open the project tree/files or use Build Output to locate the exact file. Do not invent a sandbox path or promise a filename that has not been checked.

## What success means

A successful build only proves the configured variant compiled and packaged. For a usable app, also verify:

- APK exists and can be installed.
- Launch Activity opens.
- Main screen renders without crash.
- The requested interaction works.
- Permissions/network/storage behavior works on the target Android version.
- Data persists or reloads as expected.
- A release build is signed with the intended key if distribution is planned.

## Troubleshooting sequence

1. Find the first meaningful error above the final failure summary.
2. If it is a configuration/dependency error, inspect Gradle DSL, repository access, versions, and offline state.
3. If it is a source error, use file/line and compiler message.
4. If it is a resource/manifest error, inspect resource naming and XML.
5. If build passes but install fails, inspect Android install/signature/API/device error.
6. If install passes but app crashes, inspect app logs/stack trace and runtime behavior.
7. Rebuild the narrowest target; avoid changing unrelated settings.
