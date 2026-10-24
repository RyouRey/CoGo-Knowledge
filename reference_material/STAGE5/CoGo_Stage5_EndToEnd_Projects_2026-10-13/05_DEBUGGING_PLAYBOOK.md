# Debugging playbook for CoGo app projects

## First principle
Diagnose from the earliest specific error in Build Output. The last line `BUILD FAILED` usually summarizes failure, not its cause.

| Symptom | Likely class of cause | Evidence to inspect | Safe next step |
|---|---|---|---|
| Gradle sync fails before Kotlin/Java compile | plugin/dependency/repository/toolchain resolution | first `Could not resolve`, plugin not found, or version error | compare generated build files with current CoGo template; check connectivity/cache only if relevant |
| Old project fails after CoGo upgrade | toolchain migration | AGP/Gradle/Kotlin mismatch; project created on 26.37 or earlier | backup, follow official migration guide, change only required config |
| `Unresolved reference: R` | resource merge/compile, namespace, XML error, wrong import | earlier resource errors; package/namespace; generated R import | fix earliest XML/resource or namespace error, then rebuild |
| `Unresolved reference: ...` for a View ID | ID mismatch or wrong layout | XML `android:id` vs `findViewById`/binding | align IDs and ensure correct layout is loaded |
| `Unresolved reference: androidx.compose...` | project not Compose-enabled or dependencies absent | template family and generated Gradle setup | recreate/use Compose template; don't paste random dependencies as first fix |
| `package ... does not exist` / package mismatch | source package differs from actual app package or import | first line of source and actual folder/package | update package declaration and imports consistently |
| `Manifest merger failed` | component/permission/SDK/attribute conflict | full merger error, manifest files, library manifests | fix the named conflict; do not delete manifest entries blindly |
| App builds but crashes on launch | runtime exception, missing resource, manifest/config | Logcat stack trace, first `Caused by` | find app's first relevant stack frame; reproduce with minimal steps |
| Button appears but does nothing | listener not wired, view ID mismatch, overlay/disabled state | click handler, view ID, runtime log | add a visible temporary result and test one event |
| App installs but can't launch | no launchable Activity, manifest issue, install failure | manifest and install output | ensure launchable Activity exists and is declared |
| Quick Build fails but Gradle works | edit not supported by Quick Build or experimental path issue | Quick Build status/output and same change under Gradle | use normal Gradle for the correctness baseline; record the edit type |
| APK not found | wrong variant/task/output path | complete build output and `build/outputs` tree | inspect actual generated path; don't assume debug/release or module |
| Dependency resolution fails offline | dependency not cached/available | exact coordinate and repository error | prefer bundled/template dependencies or restore network; don't invent mirrors |

## Triage order
1. Capture the full first error and 30–50 lines around it.
2. Identify whether failure occurred during sync, resource processing, Kotlin/Java compile, dexing, packaging, install, or runtime.
3. Confirm CoGo version and project age.
4. Compare current files against the template-generated baseline.
5. Change one root cause at a time.
6. Rebuild and check whether the first error moved.
7. If runtime-only, capture Logcat and reproduce from a clean launch.
8. Save the fix and its environment as a knowledge record.

## Avoid
- Replacing the whole Gradle file as a first reaction.
- Adding several dependencies before understanding the missing symbol.
- Deleting `AndroidManifest.xml` entries because an error mentions the manifest.
- Treating every Quick Build fallback as a defect.
- Claiming a fix is confirmed without rerunning the failing test.
