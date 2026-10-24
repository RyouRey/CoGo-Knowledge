# Master dataset schema

## File format

`11_MASTER_KNOWLEDGE_DATASET.jsonl` is UTF-8 JSON Lines. Each line is one independent JSON object. The Stage 7 snapshot contains 184 records with IDs from `CGO-FINAL-0001` through `CGO-FINAL-0184`.

## Core fields

| Field | Meaning |
|---|---|
| `canonical_id` | Stable ID assigned to the combined record. |
| `origin_stage` | Stage from which the record originated (`STAGE1`–`STAGE5`). |
| `origin_record_id` | Original record ID in the source-stage dataset. |
| `topic` | Topic label. Labels are not yet fully canonicalized. |
| `question` | Optional retrieval question. |
| `statement` | Main knowledge statement. |
| `procedure` | Optional steps/procedure. |
| `expected_result` | Optional expected outcome. |
| `failure_modes` | Optional failure modes. |
| `cogo_version_scope` | Version scope or caveat. |
| `evidence_class` | Legacy evidence/source label. Values are currently mixed and are not yet fully constrained to the taxonomy in `06_EVIDENCE_PROVENANCE_AND_CONFIDENCE.md`. |
| `verification_status` | Indicates whether a claim is documented, source-reviewed, recommended, or independently/device verified. |
| `confidence` | Legacy confidence/source-status value. Current records include `high`, `medium`, `official-current`, and `derived-guidance`. |
| `source_urls` | Source links; some values are `local:` pointers to files in the historical Stage 5 tree rather than web URLs. |
| `retrieved_at` | Date associated with the source record in the snapshot. |
| `caveat` | Optional limitations. |
| `original_record` | Preserved source-stage record payload. |
| `origin_records` | Lineage of contributing source records. |

## Current consistency issues

The data is syntactically valid, but its metadata schema is not yet fully normalized:

- `evidence_class` contains 21 distinct labels in the uploaded snapshot, including `directly_documented`, `derived_or_unspecified`, `reasoned_reference_code`, `official_release_doc`, and `architecture_doc`. The evidence-policy document instead defines a smaller high-level taxonomy such as `official_current`, `official_versioned`, `derived_guidance`, `reference_code_unverified`, and `device_verified`.
- `confidence` includes `official-current` and `derived-guidance` alongside the expected `high` and `medium` values. These two legacy labels describe source/evidence type more than confidence.
- `source_urls` contains `local:` pointers for Stage 5 examples and notes. They should be resolved against the archive tree, not treated as clickable external links.
- Topic naming mixes separators and granularity, e.g. `quick_build` / `quick-build`, `project_creation` / `project-creation`, and generic labels such as `p1` / `p2` / `p3`.

The validator reports these issues as warnings. It does not rewrite source data automatically, because a safe normalization requires an explicit mapping and preservation of every original value.

## Recommended future schema migration

A future migration should be versioned and tested, preferably with explicit fields for:

- `evidence_class` (controlled enum);
- `source_type` (original/source-system classification);
- `confidence` (`high`, `medium`, `low` only);
- `verification_status` (controlled enum);
- `source_urls` and `local_paths` as separate fields;
- normalized topic plus `topic_original` where a historical label changes.

Every mapping should be reproducible and should retain the raw source-stage payload. Do not claim the migration is complete until all records pass the schema validator and documented review.
