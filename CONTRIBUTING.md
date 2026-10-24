# Contributing

Thanks for helping improve CoGo-Knowledge. The primary goal is to make the information more traceable, accurate, and useful—not merely to increase the number of notes.

## Before changing a technical claim

1. Identify the exact claim and the user workflow it affects.
2. Prefer current official help/release notes for user-facing behavior.
3. Prefer a pinned tag or commit for source-code implementation claims. Label moving branches such as `stage` as development evidence.
4. Record the source URL, access/review date, CoGo version or commit scope, verification status, confidence, and caveats.
5. If no source supports the claim, mark it as inference or an unverified workaround rather than stating it as fact.

## Evidence discipline

- Do not turn a test definition into a claim that the test ran.
- Do not label sample code as device-verified without a reproducible build/install/run record.
- Preserve negative results and unresolved errors.
- Keep historical snapshots identifiable; update claims and dates only when the source was actually rechecked.
- Do not delete old stage archives just because newer synthesis documents exist.

## Dataset changes

The master dataset is newline-delimited JSON (one complete JSON object per line). Avoid pretty-printing the whole file into a single JSON array. Preserve `canonical_id`, lineage fields, and `original_record` unless a documented migration explains the change.

When editing data, run:

```bash
python -m unittest discover -s tests -v
python scripts/validate_repository.py
```

Current legacy inconsistencies are documented in `docs/DATASET_SCHEMA.md`. Do not silently change a label's meaning as a side effect of a formatting cleanup. If normalizing schema fields, document the mapping, preserve old values for provenance, and include tests.

## Documentation changes

- Keep relative links valid.
- Use dated, version-scoped claims for details likely to change.
- Separate source facts, derived guidance, reference code, and verified execution.
- Update `CHANGELOG.md` for meaningful corpus or repository changes.
- Regenerate `repository_manifest.json` when adding, removing, or editing files.

## Pull request checklist

- [ ] The reason for the change is clear.
- [ ] Sources and version scope are recorded for new technical claims.
- [ ] Verification status is accurately represented.
- [ ] Local links/paths remain valid.
- [ ] Unit tests and repository validation pass.
- [ ] The repository manifest and changelog are updated where appropriate.
