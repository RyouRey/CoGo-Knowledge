# Build, Run, Quick Build and APK

## Standard Gradle build/run
Use this as the correctness baseline:
1. Wait for project sync.
2. Choose the debug variant.
3. Run the normal Build/Run action or the appropriate task offered by the project.
4. Read Build Output and wait for completion.
5. Install and launch the produced app.
6. Exercise the feature, not just the splash screen.
7. When preparing distribution, use the release flow and signing guidance appropriate to the project.

Task names can vary with the project and CoGo version. Common Gradle task names such as `assembleDebug` and `installDebug` are conventions, not a promise that every template/version exposes the exact same UI entry. Prefer tasks actually listed by CoGo.

## Quick Build (CoGo 26.41 experimental feature)
The official 26.41 release notes describe Quick Build as an experimental fast iteration path. Requirements include:
- Experimental features enabled and CoGo restarted.
- An Android application with a launchable Activity.
- Single-process app (extra processes are unsupported).
- Debug variant selected; release variant must be changed to debug.
- Additional memory/storage is needed because compiler tools remain loaded between edits.
- Library and plugin projects are not eligible.

Workflow described by release notes:
1. Create/open eligible app.
2. First Quick Build provisions a proxy app and can take about as long as a normal first build.
3. Install/launch the proxy app; if a normal app with the same app ID is installed, heed the replacement confirmation.
4. Save compatible edits to trigger live reload.
5. Use Quick Build to restart with changes when appropriate.

## Crucial limitation
Quick Build is for iteration, not the artifact you should treat as the final shipping build. The development-branch design note explicitly says deployable/installable output still comes from the normal Gradle pipeline; Quick Build's live-reload pipeline is intentionally narrower and can fall back to Gradle. This source-stage detail must be version-checked before applying to future releases.

## APK location
Do not guess a single absolute path. Output location can vary by variant, module, template, and build configuration. Inspect Build Output for the generated APK path or use the project's file tree to locate the `build/outputs/apk/` directory. Confirm the APK's timestamp and variant before sharing it.
