# Evidence-First Debugging and Error Triage

## Four different failure classes

1. **IDE/project setup:** project initialization, sync, missing SDK/tooling, unsupported plugin/version.
2. **Compile/configuration:** Kotlin/Java compile errors, Gradle DSL errors, dependency resolution, resource linking.
3. **Install/launch:** APK install/signature/API mismatch, missing launcher Activity, manifest declarations.
4. **Runtime/behavior:** crash, incorrect output, network failure, persistence bug, UI/state issue.

Identify the class before editing files.

## Ask the user for useful evidence

- CoGo version and architecture (32-bit/64-bit if known).
- Android version/device model if install/runtime-specific.
- The exact task/action that failed (Sync, Build, Quick Run, install, launch).
- Full first error and surrounding 20–50 log lines where possible.
- The relevant build file and source file, including exact paths.
- Whether a newly generated untouched template builds.
- Whether the project predates CoGo 26.38.

CoGo's 26.39 release notes say build errors/warnings in the log panel are clickable, taking the user to the line. The UI also supports searching/filtering/sharing logs in recent versions; controls may vary by release.

## Diagnostic matrix

| Symptom | First checks | Avoid |
|---|---|---|
| Sync fails resolving plugin/dependency | Network/offline flag, repository, exact coordinates/version, cache, DSL | Randomly changing AGP/Kotlin and all dependencies |
| Error mentions `org.jetbrains.kotlin.android plugin is no longer required` | Is project on AGP 9.3.1 new stack? Follow CoGo migration guide and remove obsolete Kotlin plugin line if applicable | Removing Kotlin plugin from an unrelated older stack |
| Error mentions `Using kotlinOptions is an error` | Inspect Kotlin target block and whether new-stack migration applies | Copying new syntax into an older project without checking |
| `InternalProblems` or related AGP config failures after CoGo upgrade | Compare project to migration guide; confirm AGP version | Editing source code; the issue may be build configuration |
| Cannot find symbol / unresolved reference | Exact package/import, dependency, spelling, source set, generated code, version API | Adding a dependency before verifying whether the type is in project or SDK |
| Resource not found / `R` issue | XML filename/ID, resource folder, XML syntax, package/namespace, failed resource task earlier in log | Manually editing generated `R` files |
| Manifest merger conflict | Existing manifest, duplicate declarations, `minSdk`, library manifest requirements | Blindly adding `tools:replace` without understanding conflict |
| Duplicate class | Dependency tree, transitive versions, duplicate local JAR/AAR | Excluding arbitrary libraries until it builds |
| `minSdk` mismatch | Compare library minSdk with app minSdk; decide product support policy | Raising minSdk without telling user older devices will be excluded |
| Build succeeds but app crashes immediately | Runtime stack trace, manifest launcher, initialization, null/state/data issues | Treating build success as app correctness |
| App can't access network | Manifest INTERNET permission, cleartext/network security policy, URL/TLS, connectivity, server response | Assuming INTERNET permission alone solves every network issue |
| Install/update says incompatible or signature mismatch | Device API, ABI, application ID, signing key, existing install | Uninstalling blindly if local app data matters |
| Works in debug but not release | R8/minification, release-only config, signing, missing keep rules, variant resources | Disabling all optimization without identifying root cause |
| Slow or out-of-memory build | Available RAM/storage, number of workers, project size, concurrent apps, daemon/build cache | Assuming a clean build fixes memory pressure |

## Root-cause loop

1. State the hypothesis in one sentence.
2. Identify the smallest check that can confirm/refute it.
3. Change one relevant thing.
4. Re-run the same failing action.
5. Compare the first error and resulting behavior.
6. If the hypothesis was wrong, revert or adjust before making another change.
7. Record the fix with the CoGo version, toolchain, exact error signature, and verified result.

## Security and data care

Before asking for logs, remind users to redact passwords, API keys, access tokens, signing credentials, private URLs, personal data, and proprietary source they cannot share. Don't recommend putting secrets in the manifest or hardcoding them into a public repository.
