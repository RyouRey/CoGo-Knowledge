# Code On The Go — Research Pack Stage 3
## Implementation Trace & Regression Tests

**Snapshot:** 2026-10-13  
**Pinned release tag:** `26.40`  
**Release commit:** `2b0b6cdd10fb9af948aa989b46e07054f65f292b`  
**Repository:** https://github.com/appdevforall/CodeOnTheGo

## Goal
Stage 3 moves from subsystem maps to implementation traces grounded in files, methods, blob SHAs and selected regression tests. It is not a full repository audit; it provides reproducible starting points for further class-by-class work.

## Core distinction
- `26.40` is the pinned release snapshot used for implementation claims.
- `stage` is a moving development branch and must not be silently mixed into release claims.
- Analysis and suggested tests are labeled separately from directly observed code/test facts.

## Included
1. `01_PINNED_SOURCE_INDEX.md` — pinned source paths, blob SHAs and method anchors.
2. `02_CASE_STUDY_DEEP_LINKS.md` — URL parsing, lifecycle routing, path safety and regression tests.
3. `03_CASE_STUDY_PLUGIN_RUNTIME.md` — `.cgp` loader, classloader, plugin manager and lifecycle.
4. `04_CASE_STUDY_GRADLE_BUILD_SERVICE.md` — service boundary, event delivery and build-debugging trace.
5. `05_REGRESSION_TEST_MATRIX.md` — existing regression evidence and proposed missing tests.
6. `06_VERSION_AND_API_COMPATIBILITY.md` — release pin, API caveats and version-sensitive findings.
7. `07_NEXT_RESEARCH_BACKLOG.md` — precise continuation plan.
8. `08_IMPLEMENTATION_DATASET.jsonl` — retrieval-ready source-level records.
9. `09_SOURCE_MANIFEST.json` — snapshot and provenance metadata.
10. `SOURCES.md` — canonical links.

## How to use
- Human reader: read files 01–07 in order.
- RAG: chunk by heading; retain `source_ref`, `source_file`, `source_sha`, `line_anchor` and `evidence_class`.
- Coding agent: open the exact pinned URL before suggesting edits; inspect neighboring implementation and tests before making a change.
- Release-sensitive answer: cite tag `26.40`, not `stage`.

## Evidence labels
- `direct_source`: code or documentation inspected at tag `26.40`.
- `direct_test`: test code inspected at tag `26.40`.
- `analysis`: reasoned interpretation of code structure.
- `proposed_test`: recommended test, not claimed to exist.
- `needs_trace`: requires additional source or runtime investigation.

## Important limits
- No claim that the whole repository has been compiled or test suites executed during this research.
- No claim of a formal security audit.
- Source line anchors refer to the inspected file at the pinned tag; always verify if files are later edited.
- Tests prove only the behavior asserted by those tests, not total correctness.
