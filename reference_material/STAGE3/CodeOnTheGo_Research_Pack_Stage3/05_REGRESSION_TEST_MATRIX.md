# 5. Regression Test Matrix

## 5.1 Existing test evidence
| Area | Existing test source | Examples observed |
|---|---|---|
| Deep-link parser | `app/src/test/java/com/itsaky/androidide/models/DeepLinkRequestTest.kt` | project-only; line/column; multi-segment file path; reserved keywords; ambiguous file request |
| Path containment | `common/src/test/java/com/itsaky/androidide/utils/PathTraversalTest.kt` | `..`; empty path; NUL; absolute path; backslash; symlink escape; ordinary filename with `..` |
| Gradle build service | service and neighboring tests are present in the repository history/search results; exact test files must be confirmed at the pinned tag before relying on them | build slot, server exit, event delivery should be traced in tag-specific tests |
| Plugin runtime | `plugin-manager` source and API docs inspected; a complete test inventory has not been completed | add lifecycle/load failure cases after locating tag-specific tests |

## 5.2 Priority labels
- **P0:** security boundary, data loss, build cancellation/result correctness.
- **P1:** plugin lifecycle, compatibility, project-open routing.
- **P2:** UI presentation, diagnostics, observability.

## 5.3 Suggested minimum CI matrix
| Change | Required validation |
|---|---|
| Deep-link parser/writer | unit tests + round-trip tests + manifest prefix test |
| Path resolution | traversal, symlink, NUL, absolute path, normalization tests |
| Activity routing | Robolectric/instrumentation lifecycle and task-stack tests |
| Plugin loader | corrupt artifact, classloader contract, native extraction tests |
| Plugin lifecycle | initialize/activate/deactivate/dispose and rollback tests |
| Build service | unit tests for slots, server lifecycle, terminal results and cancellation |
| Build tooling | integration test using a tiny Android project and local/cached dependencies |
| Native/ABI changes | v7 and v8 build/install smoke tests where supported |
| Release packaging | inspect actual APK and test install/launch |

## 5.4 Research-quality checklist
Before asserting “tested”:
- cite the test file and exact test method;
- verify the test exists at the pinned release tag;
- describe what assertion it makes;
- state whether the test was merely inspected or actually executed;
- do not extrapolate one passing unit test into a system-wide guarantee.
