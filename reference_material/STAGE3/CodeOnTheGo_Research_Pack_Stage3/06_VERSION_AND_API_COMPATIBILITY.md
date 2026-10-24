# 6. Version and API Compatibility Notes

## 6.1 Release pin
This stage uses tag `26.40` → commit `2b0b6cdd10fb9af948aa989b46e07054f65f292b`.

Release endpoint:
https://api.github.com/repos/appdevforall/CodeOnTheGo/releases/tags/26.40

The release was published on 2026-09-29. The release body lists Kotlin snippets, a flattened dependency graph, embedding capability in plugin API, project-creation Git initialization, template tooltips and Kotlin debugger improvements.

## 6.2 On-device plugin build versions
The pinned `docs/PLUGIN_AUTHORING.md` distinguishes repository/online plugin build versions from on-device offline versions. It documents on-device pins of AGP `9.3.1`, Kotlin `2.3.21`, and Gradle `9.6.1` for that snapshot. It also explains that AGP 9 compiles Kotlin itself and does not accept the old `org.jetbrains.kotlin.android` plugin in the same manner; the authoring instructions instead pin the Kotlin Gradle plugin on the root buildscript classpath.

Do not reuse these numbers for arbitrary projects or future CoGo releases without rechecking the authoritative constants and guide.

## 6.3 Plugin API changelog caveat
The changelog's headings use API capability release-week labels (e.g. `YY.WW`), which are not necessarily identical to the app's marketing/release version labels. Interpret entries by reading their text and compatibility floor, not by assuming a numeric label always means the same versioning scheme.

The pinned changelog describes an embedding capability with:
- `EmbeddingBackend extends LlmBackend`;
- `embed(List<String>)` returning a future with one vector per input;
- `getEmbeddingDimensions()`;
- `getEmbeddingModelId()`;
- whole-batch success/failure semantics;
- non-blocking, concurrency-safe expectations.

Because this is API-contract material, plugins using that capability should check the changelog and the exact API types at the target release before compiling.

Pinned changelog:
https://github.com/appdevforall/CodeOnTheGo/blob/26.40/docs/PLUGIN_API_CHANGELOG.md

## 6.4 Do not conflate these facts
- `26.40` release commit is pinned.
- `stage` can contain unreleased APIs.
- App build dependencies and on-device user-project build dependencies are different concerns.
- Plugin API version compatibility and Android SDK min/target SDK are different concerns.
- The existence of an API class does not prove a specific plugin has permission to use it.
- The existence of a test does not prove it ran in this research session.
