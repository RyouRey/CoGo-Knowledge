# 8. Repository Map and Research Notes

## 8.1 Organization repositories observed
The App Dev for All GitHub organization lists `CodeOnTheGo` as the main IDE repository and `addons` as the repository for add-ons. It also hosts other projects, including Knowledge to Go and documentation/tooling-related repositories. Do not assume every repository in the organization is a runtime dependency of CoGo.

## 8.2 Key files in the main repository
- `README.md`: product summary, installation, AndroidIDE lineage, acknowledgements and license.
- `ARCHITECTURE.md`: architecture as implemented today, module map, dependency rules, toolchain details and asset provenance.
- `CLAUDE.md`: branch model and repository-specific operating rules for contributors/agents.
- `CONTRIBUTING.md`: contribution process.
- `SECURITY.md`: security reporting and policies.
- `E2E_TESTING_REPORT.md`: end-to-end testing information.
- `settings.gradle.kts`: module inclusion and composite builds.
- Root `build.gradle.kts`: top-level build and asset wiring.
- `gradle/libs.versions.toml`: dependency/version catalog.
- `composite-builds/build-logic`: centralized build conventions.
- `app/`: main app integration layer.
- `plugin-api/`, `plugin-manager/`: extension contract and runtime management.
- `apk-viewer-plugin/`: in-tree plugin example identified by authoring docs.
- `llama-api/`, `llama-impl/`: local inference integration.
- `lsp/`, `editor*`, `lexers/`: language/editor subsystems.
- `termux/`: terminal components.
- `testing/`: subsystem testing harnesses.

## 8.3 Important adjacent repositories and asset sources
The architecture notes state that large assets are not all stored in the main public repository. They are ignored by Git and fetched/reconstructed as part of build/release workflows.
- `appdevforall/dev-assets` is described as a private asset store for per-ABI Android SDK/bootstrap, Gradle distribution/API jars, local Maven repository archive, templates and documentation database copies.
- `appdevforall/OfflineDocumentationTools` is public and manages the documentation database schema and ingestion/build tooling.
- `appdevforall/addons` contains plugins and templates; the publishing workflow builds plugins and publishes the add-on catalog.

This is important for reproducibility: a checkout's Git history may not contain every binary asset required to build the full app.

## 8.4 License and attribution
The main repository identifies GPL-3.0-or-later. The README also lists third-party documentation and books under their own licenses, including CC BY 4.0 material and other license terms. Check each dependency and asset's license separately. This research pack summarizes public facts and links to sources; it does not copy the repository's source tree or redistribute its binary assets.

## 8.5 Evidence confidence
**High confidence (directly documented):**
- Product positioning and major features.
- AndroidIDE successor relationship.
- Layered architecture, module families and key build constraints.
- Plugin API contract concepts and changelog examples.
- Compatibility figures explicitly listed by official product/support pages.

**Medium confidence (interpretation based on documented architecture):**
- Suggested diagnostic decision trees and subsystem triage.
- Generalized build flow and recommendations for contributors.
- Security and AI data-handling recommendations.

**Requires additional source tracing before asserting:**
- Exact behavior of every feature in every release.
- Full list of supported AGP/Gradle/Kotlin combinations.
- Exact on-device debugger privilege implementation.
- All plugin permissions and every extension point.
- All classes, APIs, tests, open issues and pull-request status.
- Exact AI prompt construction, telemetry/data retention, and model behavior.
- Full contents of private asset repositories.

## 8.6 Research method and limitations
This analysis uses public official pages and selected repository documentation, including `ARCHITECTURE.md`, `PLUGIN_AUTHORING.md`, `PLUGIN_API_CHANGELOG.md`, and `CLAUDE.md`. The repository is large and active, with thousands of commits. A genuinely exhaustive analysis would require checking out a pinned commit and systematically indexing every source file, test, workflow, issue and release note.

The `stage` branch is a development/integration branch, not necessarily identical to the latest public release. Version numbers and API features in `stage` may be unreleased. The product site showed release 26.39 as current in the researched snapshot, while the plugin API changelog included a later unreleased 26.41 section. This difference is expected for a moving development branch.

## 8.7 Recommended next-stage deep dive
To expand this pack into a source-audited engineering manual:
1. Pin the exact release tag or commit.
2. Clone the main repository and add-ons repository.
3. Generate a module dependency graph from Gradle settings.
4. Inventory source packages/classes and public APIs.
5. Map build lifecycle from UI action to tooling process and event consumers.
6. Trace plugin installation, validation, class loading and lifecycle.
7. Trace AI prompt/context, backend selection and tool invocation.
8. Inventory tests and CI workflows.
9. Link issues/PRs to relevant source modules.
10. Regenerate the knowledge dataset with source file/line references and commit hashes.
