# Code On The Go (CoGo) — Knowledge Pack

**Version of this research:** 2026-10-13  
**Purpose:** Human-readable technical documentation and an AI-ingestion starter corpus.  
**Primary sources:** official product page, public GitHub repository, architecture notes, plugin authoring guide, plugin API changelog, and App Dev for All organization page.

## Contents
1. `01_PRODUCT_OVERVIEW.md` — purpose, users, features, constraints, ecosystem.
2. `02_ARCHITECTURE_AND_MODULES.md` — architecture, module families, state and build flow.
3. `03_BUILD_TOOLCHAIN_AND_COMPATIBILITY.md` — Gradle, SDK/JDK/Kotlin, ABIs, storage/RAM, migration.
4. `04_EDITOR_LANGUAGE_AND_UI_TOOLING.md` — editor, language services, UI design tools, debugging.
5. `05_PLUGINS_AND_ADDONS.md` — plugin architecture, lifecycle, metadata, compatibility and development.
6. `06_AI_GIT_OFFLINE_AND_SECURITY.md` — AI backends, Git, offline model, security considerations.
7. `07_DEVELOPMENT_WORKFLOW_AND_TROUBLESHOOTING.md` — practical workflow for contributors and users.
8. `08_REPOSITORY_MAP_AND_RESEARCH_NOTES.md` — repository map, evidence quality, gaps and next steps.
9. `09_AI_KNOWLEDGE_DATASET.jsonl` — short, standalone facts in JSON Lines format.
10. `SOURCES.md` — source links and scope notes.

## How to use this pack
- Read the index first, then the product and architecture documents.
- Treat the repository's current `stage` branch as a moving target, not as a fixed release snapshot.
- Before implementing or debugging a specific feature, reopen the linked source files and check the branch/release in use.
- The JSONL file is an initial retrieval/finetuning-style knowledge set, not a substitute for the full docs or source code.
- Keep provenance: each record/document links back to official sources where possible.

## Research limitations
This is a source-based analysis of publicly available material, not a line-by-line audit of every file in a repository containing thousands of commits and many modules. It does not claim to enumerate every class, API, issue, pull request, or historical change. Some large runtime assets live outside the public source repository and are fetched separately. Product pages and `stage` documentation can change after this research date.

## Important distinction
“Offline-capable” means the core local editing/build workflow is designed to work without a continuous Internet connection once required assets and dependencies are present. It does **not** mean every feature is offline: cloud AI, downloading dependencies/assets, Git remotes, updates, plugin catalog access, and some setup operations need connectivity.
