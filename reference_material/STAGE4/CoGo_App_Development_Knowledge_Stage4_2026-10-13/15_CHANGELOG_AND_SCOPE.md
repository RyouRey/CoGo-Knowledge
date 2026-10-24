# Changelog and Scope Correction

## Stage 4 — 2026-10-13

### Goal corrected

The target is documentation and machine-readable knowledge for **creating and developing Android applications using CoGo as an Android IDE**. The target is not documentation for modifying CoGo's own source code.

### Reprioritized content

- Project creation and template selection.
- Name/package/language/minimum SDK/Gradle DSL decisions.
- File placement and project structure.
- Build toolchain and CoGo 26.38+ migration compatibility.
- Sync, task selection, build/run, Quick Build, APK output.
- XML/View UI vs Compose.
- Evidence-first debugging, dependency/permission practices, release signing.
- AI response protocol, acceptance matrix, and operational JSONL dataset.

### Carried forward from Stage 3

Stage 3 pinned source at tag 26.40 for internal implementation case studies. That research remains archival context, but its deep-link/plugin-loader/Gradle service call chains are not the priority for the user's intended knowledge base. Stage 4 uses official user-facing CoGo documentation and current release notes as primary sources.

### Version note

At snapshot date 2026-10-13, the official dated release notes identify 26.41 (released 2026-10-06) as current. The source repository tag used in earlier work is 26.40. Operational guidance cites 26.41 docs where relevant; source code references from 26.40 must not be treated as proof of every 26.41 UI detail.
