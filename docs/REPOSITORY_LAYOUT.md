# Repository layout

The repository keeps the original Stage 7 filenames at the root to avoid breaking the relative references used by earlier notes. Repository-maintenance files are additive.

```text
CoGo-Knowledge/
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── 00_FINAL_README.md
├── 01_MASTER_INDEX.md
├── 02_AI_ASSISTANT_OPERATIONAL_PLAYBOOK.md
├── 03_PROJECT_CREATION_DECISION_TREE.md
├── 04_VERSION_COMPATIBILITY_AND_MIGRATION.md
├── 05_BUILD_DEBUG_AND_RELEASE_PLAYBOOK.md
├── 06_EVIDENCE_PROVENANCE_AND_CONFIDENCE.md
├── 07_ACCEPTANCE_TESTS_AND_KNOWN_GAPS.md
├── 08_FINAL_AI_PROMPT_TEMPLATE.md
├── 09_SOURCE_REGISTER.md
├── 11_MASTER_KNOWLEDGE_DATASET.jsonl
├── 12_DATASET_QA_REPORT.json
├── 13_FINAL_PACKAGE_MANIFEST.json
├── repository_manifest.json
├── prior_stages/                 # Original Stage 1–5 ZIP files
├── reference_material/           # Extracted Stage 1–5 docs, data and examples
├── docs/                         # Repository-maintenance documentation
├── scripts/                      # Validation and manifest utilities
├── tests/                        # Unit tests for validation utilities
└── .github/workflows/             # Automated quality checks
```

## Two manifests, two purposes

- `13_FINAL_PACKAGE_MANIFEST.json` describes the original Stage 7 research package and its historical file hashes. It must not be rewritten just to include new repository-maintenance files.
- `repository_manifest.json` inventories the current repository edition, including maintenance files, with sizes and SHA-256 hashes.

The ZIP archives in `prior_stages/` and the extracted copies under `reference_material/` intentionally overlap: one preserves the original handoff artifact, while the other allows individual files to be reviewed without extracting archives manually.
