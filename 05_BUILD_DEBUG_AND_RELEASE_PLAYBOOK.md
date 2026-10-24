# Build, debug, Quick Build and release playbook

## Build baseline
1. Wait for project initialization and Gradle sync.
2. Build/run the unchanged starter project before feature work.
3. Use the task picker in CoGo when a specific Gradle task is needed: open the project slider, choose Run tasks, search/select the exact task, run it, and inspect Build Output. Exact UI labels may vary by version.
4. Prefer the actual task list and variant/module names from the project. Android Gradle tasks may be variant-specific.
5. Inspect the generated APK path in Build Output/project tree. The common `build/outputs/apk/debug` and `release` locations are conventions, not a guarantee of one universal path.

## Failure-stage triage
| Stage | First evidence to inspect | Typical causes |
|---|---|---|
| Project initialization / Gradle sync | first configuration/plugin/repository error | invalid build config, unsupported plugin, offline uncached dependency |
| Resource processing | XML/resource merger error | malformed XML, duplicate/missing resource, invalid reference |
| Java/Kotlin compilation | first source error and line | syntax, imports, package mismatch, unsupported API/language version |
| Dex/package | dex/manifest/packaging exception | duplicate classes, minification/packaging conflict, unsupported bytecode |
| Install | install output and OS message | signature conflict, app ID replacement, insufficient storage, permission |
| Launch/runtime | Logcat exception chain | missing Activity, null view, missing resource, runtime logic error |
| Feature behavior | reproduction steps and state | listener not wired, lifecycle/persistence assumption, wrong calculation |

Always preserve the first causal error, not just the final `BUILD FAILED` summary. Capture enough surrounding lines to include task name and nested `Caused by`.

## Quick Build — CoGo 26.41
The 26.41 release notes describe Quick Build as experimental. The documented requirements include:
- enable experimental features and restart CoGo;
- project must produce an Android app with a launchable Activity;
- app must run in one process;
- debug variant must be selected;
- library and plugin projects are not eligible;
- extra memory/storage is needed because compiler tools remain loaded.

The first provisioning may take about as long as the first normal build. Subsequent compatible saves may reload faster. Unsupported edits can fail or fall back to Gradle, so record the exact edit and status. Use normal Gradle for the correctness baseline and final shipping APK.

## Test and artifact checklist
- [ ] Sync completed
- [ ] Debug build completed
- [ ] App installed
- [ ] App launched
- [ ] Feature behavior tested
- [ ] Invalid/empty inputs tested
- [ ] Force-stop/relaunch tested where relevant
- [ ] Logcat checked if runtime failure
- [ ] Release build performed separately if shipping
- [ ] APK path, timestamp, variant and size recorded
- [ ] Signing key/credentials handled securely
- [ ] Tested artifact corresponds to the file being distributed

## APK and signing
Do not guess the APK path or claim one exists without evidence. Confirm it from Build Output or the project file tree. For release builds, protect the signing key and passwords; do not place secrets in source control or chat. A successful debug build does not prove a release build is signed correctly.
