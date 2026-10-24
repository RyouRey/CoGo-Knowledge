# Rebuild scope

This edition was rebuilt from the uploaded `CoGo_Knowledge_Base.zip` specifically as a maintainable GitHub repository. It is not packaged around the assumption that it will be uploaded as one source file to a ChatGPT Project.

## Preserved

- Original Stage 7 synthesis documents and the 184-record master JSONL dataset.
- The five earlier Stage 1–5 ZIP archives.
- Extracted Stage 1–5 research material, evidence notes, sample project source files, and stage datasets.
- Historical Stage 7 QA report and package manifest, unchanged, so their scope and original file checksums remain meaningful.

## Added

- Repository-level README, contributor guide, changelog, and license/attribution note.
- Documentation for repository layout, dataset schema, maintenance, known gaps, and this rebuild scope.
- Standard-library-only validators, unit tests, and GitHub Actions quality checks.
- A separate `repository_manifest.json` covering the repository-focused edition.

## Intentionally not done

- No research claim was silently rewritten or marked newly verified.
- No source snapshot date was advanced just because the repository packaging changed.
- The JSONL's historical evidence/confidence labels were not auto-normalized; they are surfaced as warnings until an explicit, provenance-preserving schema migration is designed.
- No license was selected on the repository owner's behalf.
- The remote GitHub repository has not been changed by generating this downloadable package.

The result improves repository usability and repeatable quality checks without pretending to complete the outstanding content-validation and device-testing work.
