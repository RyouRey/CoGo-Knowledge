# CoGo App Development Knowledge — Stage 5
Snapshot: 2026-10-13
Goal: build an evidence-led knowledge base for helping people create Android apps with Code On The Go (CoGo) on an Android device.

## Scope
This stage focuses on user app development, not modifying CoGo itself. It includes three small end-to-end project blueprints:
1. Kotlin + XML: centimetre/inch converter.
2. Java + XML: in-memory quick notes.
3. Kotlin + Jetpack Compose: counter.

Each blueprint includes full source files for the files the user is instructed to add/replace, file placement, assumptions, manual test cases, and failure diagnosis. The user's project template remains the authority for Gradle files, package name, SDK values, themes, and generated resources.

## Important evidence status
- Official CoGo release notes say 26.41 was updated on 2026-10-06 and document Quick Build requirements and migration warnings.
- CoGo's public repository release list showed 26.40 as the latest numbered release available at the research snapshot. The public `stage` branch contains newer development work and must not be treated as identical to release 26.41.
- The repository includes end-to-end tests for project creation and template setup, plus Quick Build manual QA scenarios. These are source/documentation evidence, not proof that this researcher executed the test suite on a phone.
- **The three example apps in this package have not been built or installed by this research run.** They are internally reviewed reference implementations and testable blueprints, not claimed device-verified APKs.
- No APK is included because no real CoGo build was executed.

## How to use
1. Read `01_EVIDENCE_AND_VERSION_POLICY.md`.
2. Follow `02_GENERAL_CO_GO_WORKFLOW.md` and choose a project blueprint.
3. Create the project in CoGo using a matching template. Do not overwrite generated Gradle files with generic snippets.
4. Apply only the listed source/resource file changes.
5. Run Gradle sync and a normal debug build/run first.
6. Record exact app version, device, project template, Gradle/AGP/Kotlin versions, task used, build output, install/launch result, and tests in `tests/05_EVIDENCE_CAPTURE_TEMPLATE.md`.
7. Only after recording successful real-device results may a record be upgraded to `device_verified`.

## Package contents
- `01_EVIDENCE_AND_VERSION_POLICY.md` — evidence hierarchy and version scope.
- `02_GENERAL_CO_GO_WORKFLOW.md` — end-to-end workflow and what to capture.
- `03_PROJECT_BLUEPRINTS.md` — comparison of the three sample projects.
- `04_BUILD_RUN_QUICKBUILD_AND_APK.md` — distinguishes standard Gradle build from experimental Quick Build.
- `05_DEBUGGING_PLAYBOOK.md` — error triage.
- `06_TOOLCHAIN_MIGRATION.md` — old project migration cautions.
- `07_AI_ASSISTANT_PROTOCOL.md` — expected behavior for an AI coding helper.
- `08_MANUAL_TEST_MATRIX.md` — repeatable tests.
- `09_SOURCE_MANIFEST.md` — sources and limitations.
- `10_STAGE6_BACKLOG.md` — next research stage before final Stage 7.
- `11_IMPLEMENTATION_KNOWLEDGE_DATASET.jsonl` — structured knowledge records.
- `projects/` — full source examples and individual READMEs.
- `evidence/` — evidence ledger and source claims.
- `tests/` — test matrix and capture template.

## Success criterion
A person using CoGo should be able to follow a blueprint without guessing where code goes, get clear guidance for the next action, and know what evidence is needed when a build fails. This package does not promise that all templates, versions, devices, or dependencies behave identically.
