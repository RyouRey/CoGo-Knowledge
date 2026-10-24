# 9. Research Backlog and Confidence

## 9.1 What this stage verified
- Official product page and release notes show a version difference during the research window: product page crawled as 26.39, while release notes/GitHub Releases showed 26.40.
- The `stage` branch contains architecture, plugin authoring and plugin API changelog documentation.
- `settings.gradle.kts` includes the main module list and composite-build setup.
- `gradle/libs.versions.toml` contains a source-visible dependency version catalog.
- `ARCHITECTURE.md` gives detailed design information including UDF, module families, build tooling, deep links/path traversal protection and resource constraints.
- `PLUGIN_API_CHANGELOG.md` records version-mapped plugin capabilities and unreleased entries.

## 9.2 High-confidence claims
- CoGo is a mobile-first Android IDE maintained by App Dev for All.
- It is the maintained successor to AndroidIDE.
- It runs a real Gradle build on-device via a tooling API in a separate process.
- The codebase is in migration: legacy View/LiveData/EventBus areas coexist with newer UDF/Compose areas.
- The plugin artifact is `.cgp` and the API has lifecycle, metadata, services and extension contracts.
- Gemini and llama.cpp are distinct AI integration paths.
- ABI flavors and composite build substitution materially affect repository build commands and dependency choices.

## 9.3 Medium-confidence analysis
- The suggested troubleshooting decision tree is a practical synthesis, not a guaranteed exact internal runtime sequence.
- The recommended AI agent tool policy is security guidance, not a claim that all controls are implemented in CoGo.
- The module responsibility summaries are based on architecture docs, Gradle settings and names; some require class-by-class tracing for precision.

## 9.4 Needs verification before production use
- Exact call chain for every user-project Gradle task.
- Full AI prompt assembly, file-selection rules, backend fallback and telemetry behavior.
- Exact on-device debugger privilege/bootstrap model.
- All plugin permissions, loader behavior and failure recovery.
- Current complete AGP/Gradle/Kotlin support matrix.
- Exact state of features mentioned in `stage` for release 26.40.
- Full private asset provenance and checksums.
- Current CI workflows and required status checks.
- Whether every module listed in settings is shipped/used in the same way in each build variant.

## 9.5 Next deep-dive tasks
1. Pin release `26.40` and its commit SHA.
2. Compare tag `26.40` with `stage`.
3. Trace a build action from UI → ViewModel/event → tooling API request → subprocess → event consumer.
4. Trace plugin install → metadata validation → classloader → initialize/activate → service registration → deactivate/dispose.
5. Trace AI prompt assembly → backend → tool registry → argument validation → result display.
6. Map tests to the above call chains.
7. Generate a full module graph from Gradle settings and project dependencies.
8. Inventory workflows and release automation.
9. Add source-file and line-level citations to each dataset record.
10. Re-run the evaluation set against any AI/RAG implementation.

## 9.6 Research integrity statement
This pack is a structured, source-aware research aid, not official CoGo documentation, not a full source audit and not a security certification. Public repository access does not guarantee that every build asset is public or included. Revalidate version-specific claims before using this pack to make release or compatibility decisions.
