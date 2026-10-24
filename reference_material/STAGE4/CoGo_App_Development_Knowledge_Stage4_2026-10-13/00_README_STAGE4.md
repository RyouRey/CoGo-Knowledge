# CoGo App Development Knowledge Base — Stage 4

**Snapshot:** 2026-10-13  
**Product:** Code on the Go (CoGo), Android IDE  
**Research focus:** help an AI guide users to create, build, debug, and ship Android apps *using CoGo*. This is not a guide to modifying CoGo's own source code.

## Purpose

Turn CoGo's official user documentation, current release notes, and versioned source anchors into operational knowledge that can answer practical questions such as:

- Which project template should I choose?
- What should the app name, package name, language, and minimum SDK be?
- Which files should I create/edit, and where do they belong?
- Can you give me the complete code for every required file?
- Which Gradle settings and dependencies are compatible with my CoGo version?
- Which build task should I run, and how do I interpret its output?
- How do I fix an error based on evidence rather than guesswork?
- Where is the APK, and how do I sign and distribute it safely?

## Important scope correction

Stages 2 and 3 researched CoGo implementation details. Some of that material can help establish capabilities and constraints, but it is not the primary objective. The useful target is **application development with CoGo as the tool**. Deep internal code paths, plugin class loading, deep-link parser internals, and IDE modification are explicitly out of scope unless they explain a user-facing development workflow.

## Evidence policy

Each knowledge item should be classified as one of:

- **Official-current:** current CoGo help/release page observed on 2026-10-13.
- **Official-versioned:** repository/source at pinned tag `26.40`, useful for exact reproducibility but not proof of every feature in `26.41`.
- **Android-platform:** Android/Kotlin/Gradle platform concepts that are not CoGo-specific.
- **Derived guidance:** practical synthesis of documented behavior; must be verified against the user's actual project when version/template matters.
- **Unverified:** needs hands-on confirmation or a current official source before presenting as fact.

Never present a generic Android Studio workflow as if the exact UI labels exist in CoGo. Prefer CoGo's in-app Help, long-press tooltips, and official CoGo help pages for exact controls.

## Current product baseline

- Official release notes identify CoGo **26.41**, updated 2026-10-06, as the latest release observed in this research snapshot.
- Release 26.38 introduced a major toolchain transition. Projects created on 26.37 or earlier may need migration; projects created by the updated templates need no migration changes.
- The new-stack guide identifies Kotlin 2.3.21, Gradle 9.6.1, AGP 9.3.1, and Build Tools 36.0.0 as the standard stack for updated templates.
- Treat exact version advice as versioned. Always inspect the actual project's top-level `build.gradle(.kts)`, module build file, `gradle-wrapper.properties`, optional `gradle/libs.versions.toml`, and CoGo release before prescribing changes.

## Included files

1. `01_AI_ASSISTANT_PROTOCOL.md` — how an AI should help safely and precisely.
2. `02_PROJECT_CREATION_DECISION_GUIDE.md` — project setup and template selection.
3. `03_ANDROID_PROJECT_FILE_MAP.md` — file placement and responsibility.
4. `04_BUILD_TOOLCHAIN_COMPATIBILITY.md` — versions, sync, offline constraints, migration warning.
5. `05_BUILD_RUN_TASKS_APK.md` — sync, tasks, Quick Run, Quick Build, APK paths.
6. `06_UI_XML_VS_COMPOSE.md` — UI architecture decision and workflow.
7. `07_DEBUGGING_AND_ERROR_TRIAGE.md` — evidence-first debugging.
8. `08_FEATURE_IMPLEMENTATION_PLAYBOOK.md` — storage, network, permissions, architecture, tests.
9. `09_RELEASE_SIGNING_AND_DELIVERY.md` — signing, release builds, backups, delivery.
10. `10_REFERENCE_WORKFLOW_PROMPT.md` — reusable intake and response template for an AI.
11. `11_REGRESSION_AND_ACCEPTANCE_MATRIX.md` — checks for the knowledge base and generated projects.
12. `12_SOURCE_REGISTER.md` — sources, date, limitations, and source-use notes.
13. `13_IMPLEMENTATION_KNOWLEDGE_DATASET.jsonl` — machine-readable operational facts and procedures.
14. `14_RESEARCH_BACKLOG.md` — what needs further hands-on validation.
15. `15_CHANGELOG_AND_SCOPE.md` — why the research direction changed.
16. `17_END_TO_END_EXAMPLE_WEIGHT_CONVERTER.md` — end-to-end example blueprint based on official CoGo tutorial.
17. `16_PACKAGE_MANIFEST.json` — file hashes and package metadata.

## Validation limits

This package is a researched documentation artifact. No app was built, installed, or tested on a physical device as part of this stage. It does not claim that all generated code or every task has been experimentally validated in CoGo. The next stage should validate representative projects on an actual CoGo installation, with screenshots/logs and exact version metadata.
