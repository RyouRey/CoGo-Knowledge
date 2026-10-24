# Knowledge Base Regression and Generated-App Acceptance Matrix

This matrix is for evaluating whether the AI knowledge base helps users develop apps in CoGo reliably.

## Knowledge retrieval tests

| ID | Prompt/test | Expected behavior |
|---|---|---|
| K01 | “I’m creating my first app. Which template?” | Recommends based on UI/language requirements; explains trade-offs |
| K02 | “Can I use Java with Compose?” | Clearly says official CoGo help describes Compose as Kotlin-only; offers XML/View approach for Java |
| K03 | “Which minSdk should I choose?” | Asks target-device requirement; distinguishes minSdk/targetSdk/compileSdk |
| K04 | Existing project has `build.gradle`, not `.kts` | Uses Groovy DSL syntax |
| K05 | Existing project uses `gradle/libs.versions.toml` | Preserves catalog and edits aliases coherently |
| K06 | User has CoGo 26.41 and fresh template | Keeps generated new-stack versions; avoids needless migration |
| K07 | Project built with 26.37 fails on 26.41 | Requests backup, checks catalog/no-catalog case, links official migration guide |
| K08 | User asks for exact file placement | Provides relative paths and complete file plan |
| K09 | User requests dependency while offline | Verifies cache/availability; doesn't promise download |
| K10 | Build output says Kotlin plugin no longer required | Checks AGP/new-stack context before recommending removal |
| K11 | User wants to distribute app | Covers release variant, signing key, backup, and testing |
| K12 | User shares logs containing secrets | Warns to redact secrets and avoids repeating them |
| K13 | “Build succeeded, is app finished?” | Distinguishes packaging success from runtime/feature acceptance |
| K14 | “Fix it” with no logs/files | Requests exact error/file/version instead of inventing root cause |

## Generated app acceptance

- [ ] App name and application ID are distinct and valid.
- [ ] Template/language/UI architecture match the user's request.
- [ ] Existing generated build files preserved unless change is justified.
- [ ] Every code block names its exact file path.
- [ ] File contents are complete and mutually consistent.
- [ ] Manifest, package, namespace, and resource IDs align.
- [ ] Dependencies are compatible with the project's actual toolchain.
- [ ] Sync is requested when build configuration/dependencies change.
- [ ] Build/run instructions use CoGo UI or verified task names.
- [ ] First meaningful error is used for diagnosis.
- [ ] Happy path and failure/empty/permission cases are tested.
- [ ] Network, storage, and permissions follow least-privilege design.
- [ ] APK path is confirmed from output rather than guessed.
- [ ] Release signing credentials are kept private and backed up.
- [ ] The answer does not claim unperformed tests passed.

## Hands-on validation matrix for next stage

| Scenario | Evidence to collect |
|---|---|
| Fresh Kotlin/XML project | CoGo version, template, generated tree, first build output, APK path |
| Fresh Java/XML project | Same plus exact generated DSL/source files |
| Fresh Compose project | Generated plugins/dependencies, preview behavior, build output |
| Existing pre-26.38 project | Backup, before/after build output, migration case, actual result |
| Offline dependency miss | Exact resolution error and whether enabling online resolution fixes it |
| Runtime crash | Stack trace and reproducible steps |
| Release APK | Selected variant, signing config path (redacted), artifact and install result |
| Quick Build | Experimental flag, process/variant requirements, first and subsequent build behavior |
