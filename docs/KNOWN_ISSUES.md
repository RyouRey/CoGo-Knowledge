# Known issues and validation boundaries

This page describes known gaps in the uploaded Stage 7 snapshot; it does not imply that the associated claims are necessarily incorrect.

## Dataset and metadata

- The master JSONL is syntactically valid and contains 184 records, but `evidence_class` and `confidence` mix multiple vocabularies. See `DATASET_SCHEMA.md`.
- There are 15 `local:` source pointers in the master dataset. These need local path resolution when reading the source archive.
- Topic labels are not fully normalized.
- The `retrieved_at` values are all tied to the 2026-10-13 snapshot; they should not be mistaken for an ongoing freshness guarantee.

## Verification coverage

- The Stage 7 QA report records zero JSONL parse errors and zero exact duplicates merged.
- 131 records were marked `not_independently_verified` in the uploaded snapshot. This describes the evidence level; it is not a verdict that those claims are false.
- No Stage 5 sample app was built, installed, or run on a physical device during the recorded research run.
- No APK artifact was created in that run.
- The planned Stage 6 hardening stage was not delivered as a separately executed research package.
- The work does not claim to audit every CoGo source file or every device/toolchain combination.
- The research snapshot records a difference between official 26.41 release notes and the public 26.40 numbered release tag. Recheck live sources before using this as current release status.

## Repository engineering

- The original Stage 7 manifest inventories the original research package, not subsequently added maintenance files. `repository_manifest.json` is the inventory for this repository edition.
- The repository has no included license file. Do not infer an explicit reuse license from public visibility.
