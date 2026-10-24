# 8. AI Retrieval Schema and Evaluation

## 8.1 Recommended use
The JSONL dataset is a starter corpus for retrieval, not a fine-tuning dataset guaranteed to improve model behavior. For a robust CoGo assistant, combine:
- source-grounded documentation chunks;
- exact source-file snippets at a pinned commit;
- release notes;
- tests and examples;
- carefully labeled troubleshooting cases;
- API compatibility history.

## 8.2 Recommended chunk schema
Each JSONL record should include:
- `id`: stable unique identifier;
- `topic`: broad subsystem;
- `question`: optional retrieval-style query;
- `fact` or `content`: concise answer/context;
- `source_url`: canonical source;
- `source_ref`: branch/tag/commit;
- `source_file`: repository path when applicable;
- `source_sha`: blob SHA when available;
- `retrieved_at`: ISO date;
- `evidence_class`: documented/source-indexed/analysis/needs-verification;
- `confidence`: high/medium/low;
- `version_scope`: release or branch scope;
- `keywords`: search aliases;
- `caveat`: what must not be inferred.

## 8.3 Version-aware retrieval
Do not merge `stage` and release-tag facts into a single unqualified answer. Add metadata filters:
- `source_ref = 26.40` for release 26.40;
- `source_ref = stage` for current development docs;
- `version_scope = historical` for old release behavior;
- `evidence_class = analysis` when an item is advice rather than a source assertion.

If the question asks “in the latest release,” prefer release notes and tag-specific source. If it asks “in the current repository,” use `stage` but label unreleased capabilities.

## 8.4 Retrieval chunking
- Split at headings and keep the heading path with every chunk.
- Keep code examples intact.
- Keep version numbers and API names with the paragraphs that explain them.
- Avoid huge chunks spanning unrelated modules.
- Avoid one-line chunks that lose important qualifiers.
- Keep source URL and branch metadata outside the text body as structured fields.

## 8.5 Evaluation question set
Build a regression set such as:
1. What does CoGo do, and what is not guaranteed by “offline-capable”?
2. Which module family should be inspected for build-progress events?
3. Why does `assembleV8Debug` appear instead of `assembleDebug` in the CoGo repo?
4. What is the difference between the IDE's own SDK config and the minimum SDK for apps built with it?
5. How should a plugin choose `plugin.min_ide_version`?
6. Why can duplicating a plugin API interface cause a runtime class-cast failure?
7. What is the difference between Gemini and llama.cpp integration?
8. Which path guard is documented for deep links?
9. What evidence is needed to claim a feature is in release 26.40?
10. How should a build error be classified before changing versions?

## 8.6 Quality metrics
- **Citation accuracy:** does the answer link to the source that supports it?
- **Version accuracy:** is release vs stage correctly distinguished?
- **Abstention quality:** does the system say “not verified” when source tracing is incomplete?
- **Module routing:** does it point to the correct subsystem?
- **Causal diagnosis:** does it classify failure phase before recommending changes?
- **Security behavior:** does it reject prompt injection and validate tool paths?
- **Freshness:** are release-sensitive facts periodically refreshed?
- **Consistency:** do generated answers preserve caveats and avoid contradicting source docs?

## 8.7 Dataset maintenance
When refreshing:
1. pin a release tag and capture its commit SHA;
2. fetch relevant docs and source files;
3. diff docs/API ABI dumps/release notes;
4. update facts and mark removed/changed claims;
5. rerun evaluation questions;
6. regenerate embeddings if chunk content or model changes;
7. preserve old snapshots for historical questions;
8. record date, branch/tag and file SHA in the manifest.
