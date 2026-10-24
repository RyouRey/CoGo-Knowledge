# Next Research Backlog — Practical Validation

## Priority 1: Run a real CoGo project matrix

Use a physical Android device and record:

- CoGo release (currently 26.41 in this snapshot), app architecture (32/64-bit), Android version, device RAM/storage available.
- New Project screen fields, template names, default values, and exact generated files.
- Build untouched templates: Java/XML, Kotlin/XML if available, Compose/Kotlin.
- Sync behavior with and without network, including one dependency not already cached.
- Build Output, task names exposed by the task browser, exact APK path/name, install and launch result.
- Release variant and signing behavior, with credentials redacted.
- Quick Build enabled/disabled and conditions where it is unavailable.

## Priority 2: Build a known-good example corpus

For each app type, retain full source tree, toolchain, build logs, and acceptance results:

1. Single-screen counter/form (no third-party libraries).
2. Multi-screen navigation app.
3. Local persistence app.
4. REST/HTTPS app with loading/error/offline state.
5. File/photo picker app using modern system picker.
6. Notification/background-work sample.
7. Compose sample with preview.
8. Existing project migration from 26.37 to 26.41.
9. Release-signed APK sample.

Do not claim these are tested until the artifacts and logs exist.

## Priority 3: Expand error signature dataset

Collect anonymized, redacted examples of:

- AGP/Kotlin migration failures.
- Offline dependency resolution.
- Namespace/manifest/resource failures.
- Duplicate/transitive dependency errors.
- Java/Kotlin compile failures.
- Runtime crashes and install/signature errors.
- Device-specific memory/storage/build failures.

Each record should include CoGo version, AGP/Gradle/Kotlin versions, task, first error, diagnosis, fix, verification status, and source URL.

## Priority 4: Knowledge base quality

- Keep a canonical record per fact with provenance and last-verified date.
- Separate CoGo-specific UI instructions from Android platform knowledge.
- Version-gate migration advice and UI labels.
- Add negative examples (“do not do this”) for common AI hallucinations.
- Measure whether an AI response contains exact paths, complete files, valid DSL, and honest test status.

## Out of scope unless user explicitly changes the goal

- Modifying CoGo's own source code.
- Deep internal call-chain mapping of plugin classloaders/deep links.
- IDE plugin authoring as a primary track. Plugins/add-ons may be discussed when needed to enhance the user's application-development workflow, but they are not the main target.
