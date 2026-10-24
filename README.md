# CoGo-Knowledge

A version-controlled research and engineering knowledge base about **Code On The Go (CoGo)**, with practical references for Android project creation, toolchain compatibility, build/debug workflows, architecture, plugins, evidence tracking, and example app blueprints.

> **Research snapshot:** 2026-10-13. This repository is an independent research synthesis, not official CoGo documentation and not a complete audit of CoGo's source code.

## What this repository is for

- Preserve source-backed notes about CoGo and its development workflow.
- Make implementation guidance traceable to sources, versions, and confidence levels.
- Keep historical research stages and reference examples available for review.
- Provide repeatable repository-quality checks for the knowledge corpus.
- Record limitations instead of presenting untested code as verified.

This repository is maintained as a public knowledge project. It is **not** a CoGo application, a runnable RAG engine, or a claim that the sample projects have been built successfully.

## Start here

| Need | File |
|---|---|
| High-level scope and snapshot status | [`00_FINAL_README.md`](00_FINAL_README.md) |
| Navigate the knowledge base | [`01_MASTER_INDEX.md`](01_MASTER_INDEX.md) |
| Understand the recommended development workflow | [`02_AI_ASSISTANT_OPERATIONAL_PLAYBOOK.md`](02_AI_ASSISTANT_OPERATIONAL_PLAYBOOK.md) |
| Choose project/template and language | [`03_PROJECT_CREATION_DECISION_TREE.md`](03_PROJECT_CREATION_DECISION_TREE.md) |
| Review version/toolchain caveats | [`04_VERSION_COMPATIBILITY_AND_MIGRATION.md`](04_VERSION_COMPATIBILITY_AND_MIGRATION.md) |
| Build, debug, and release | [`05_BUILD_DEBUG_AND_RELEASE_PLAYBOOK.md`](05_BUILD_DEBUG_AND_RELEASE_PLAYBOOK.md) |
| Interpret evidence and confidence | [`06_EVIDENCE_PROVENANCE_AND_CONFIDENCE.md`](06_EVIDENCE_PROVENANCE_AND_CONFIDENCE.md) |
| Check accepted tests and known gaps | [`07_ACCEPTANCE_TESTS_AND_KNOWN_GAPS.md`](07_ACCEPTANCE_TESTS_AND_KNOWN_GAPS.md) |
| Browse source references | [`09_SOURCE_REGISTER.md`](09_SOURCE_REGISTER.md) |
| Inspect the machine-readable corpus | [`11_MASTER_KNOWLEDGE_DATASET.jsonl`](11_MASTER_KNOWLEDGE_DATASET.jsonl) |
| Review the original Stage 7 inventory | [`13_FINAL_PACKAGE_MANIFEST.json`](13_FINAL_PACKAGE_MANIFEST.json) |
| Understand the repository structure | [`docs/REPOSITORY_LAYOUT.md`](docs/REPOSITORY_LAYOUT.md) |
| See what changed in this rebuild | [`docs/REBUILD_SCOPE.md`](docs/REBUILD_SCOPE.md) |
| Maintain and validate the repository | [`docs/MAINTENANCE.md`](docs/MAINTENANCE.md) |
| Understand the current dataset schema and known inconsistencies | [`docs/DATASET_SCHEMA.md`](docs/DATASET_SCHEMA.md) |
| Review limitations and outstanding issues | [`docs/KNOWN_ISSUES.md`](docs/KNOWN_ISSUES.md) |

## Repository layout

- Root numbered Markdown files are the Stage 7 synthesis documents retained with their original names to preserve the original package's references.
- `11_MASTER_KNOWLEDGE_DATASET.jsonl` is the combined 184-record dataset.
- `12_DATASET_QA_REPORT.json` and `13_FINAL_PACKAGE_MANIFEST.json` are **historical Stage 7 artifacts**. They describe the research package as of the snapshot, not every maintenance file subsequently added to the Git repository.
- `prior_stages/` preserves the earlier Stage 1–5 archives.
- `reference_material/` contains the extracted prior-stage documentation, datasets, evidence notes, and sample-project source files.
- `scripts/` contains standard-library-only validation tools.
- `tests/` contains unit tests for the validation tools.
- `.github/workflows/` runs validation in GitHub Actions.

See [`docs/REPOSITORY_LAYOUT.md`](docs/REPOSITORY_LAYOUT.md) for the full map.

## Validate locally

Requirements: Python 3.10 or later. No third-party Python packages are required.

```bash
python -m unittest discover -s tests -v
python scripts/validate_repository.py
```

The validator checks JSONL/JSON syntax, essential dataset fields, duplicate canonical IDs, the original Stage 7 manifest's file sizes and SHA-256 hashes, and integrity of the preserved stage ZIP archives. It also reports metadata-quality warnings such as non-standard legacy labels and `local:` source references. Those warnings are intentionally not treated as proof that a knowledge claim is false.

To rebuild the repository inventory after changing files:

```bash
python scripts/update_repository_manifest.py
```

## Evidence and limitations

- CoGo behavior and compatibility can change; review version-sensitive sources before applying old guidance.
- A checked-in test definition does not prove that the test was executed.
- The Stage 5 sample blueprints were not built, installed, or run on a physical device in the recorded Stage 7 research run.
- No APK artifacts were produced by that research run.
- The data contains mixed legacy `evidence_class` and `confidence` values; see [`docs/DATASET_SCHEMA.md`](docs/DATASET_SCHEMA.md). Validation reports this rather than silently rewriting source records.
- The source snapshot recorded a difference between the official 26.41 release notes and the 26.40 numbered GitHub tag. That is historical context and must be rechecked before describing the latest release.

## Sources and attribution

The corpus includes links to official CoGo/App Dev for All materials, source repositories, help pages, and selected project references. Each individual claim should be evaluated against its linked source and version scope. See [`09_SOURCE_REGISTER.md`](09_SOURCE_REGISTER.md).

No license file is included in this package. Do not infer a reuse license solely from the repository being public; see [`docs/LICENSE_AND_ATTRIBUTION.md`](docs/LICENSE_AND_ATTRIBUTION.md).

## Status

The research synthesis snapshot is preserved; repository maintainability has been improved with navigation, contributor guidance, schema notes, scripted quality checks, and CI. These repository improvements do **not** mean the underlying CoGo claims or sample applications have been newly device-verified.
