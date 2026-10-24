# Master index and navigation

## Main workflow references
| User need | Start with |
|---|---|
| Create a new project and choose a template | `03_PROJECT_CREATION_DECISION_TREE.md` |
| Choose Java, Kotlin/XML, or Compose | `03_PROJECT_CREATION_DECISION_TREE.md` |
| Know where files go | Stage 4 `03_ANDROID_PROJECT_FILE_MAP.md`; Stage 5 `tests/06_BLUEPRINT_FILE_MAP.md` |
| Request complete code for each file | `02_AI_ASSISTANT_OPERATIONAL_PLAYBOOK.md` |
| Add a dependency or change Gradle | `04_VERSION_COMPATIBILITY_AND_MIGRATION.md` and the actual project files |
| Build, run a task, find an APK | `05_BUILD_DEBUG_AND_RELEASE_PLAYBOOK.md` |
| Diagnose sync/build/runtime failures | `05_BUILD_DEBUG_AND_RELEASE_PLAYBOOK.md` |
| Quick Build vs normal build | Stage 5 `04_BUILD_RUN_QUICKBUILD_AND_APK.md` and official release notes |
| Release signing and delivery | Stage 4 `09_RELEASE_SIGNING_AND_DELIVERY.md` |
| Add storage/network/permissions | Stage 4 `08_FEATURE_IMPLEMENTATION_PLAYBOOK.md` |
| Understand CoGo internals, plugins, AI backends | Stage 1–3 source/research archives; treat development branch as moving |
| Retrieve machine-readable facts | `11_MASTER_KNOWLEDGE_DATASET.jsonl` |

## Stage map
- **Stage 1 — Product and repository baseline:** identity, features, constraints, architecture overview, initial knowledge dataset.
- **Stage 2 — Source-level architecture deep dive:** modules, build pipeline, plugin/AI/editor architecture, tests/security, retrieval schema.
- **Stage 3 — Implementation tracing:** deep links, plugin lifecycle, GradleBuildService, regression matrix, version/API compatibility.
- **Stage 4 — Operational app-development knowledge:** project creation, file map, toolchain, build/tasks/APK, UI architecture, debugging, feature recipes, release signing, AI workflow.
- **Stage 5 — End-to-end project blueprints:** Kotlin/XML converter, Java/XML notes, Compose counter, test matrices and evidence capture.
- **Stage 6 — Planned hardening:** intended to perform physical-device validation and expand reproducible error cases. It was not completed as a separate executed research package before the final-stage request.
- **Stage 7 — Final synthesis:** this package, its normalized dataset, source provenance, and acceptance criteria.

## Recommended retrieval strategy
1. Retrieve by the user's goal and current project state, not just by keyword.
2. Prefer current official CoGo help for UI labels and release-specific behavior.
3. Prefer pinned source for implementation claims; label `stage` as development-branch evidence.
4. If a user shares a project or log, treat that as the primary evidence for their specific case.
5. When evidence is insufficient, ask for the smallest missing artifact: exact CoGo version, project template/build files, first meaningful error, or Logcat stack trace.
