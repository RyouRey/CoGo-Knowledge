# Repository maintenance

## Routine review

The corpus is a dated research snapshot, so check both content and evidence when maintaining it:

1. Review version-sensitive claims in official CoGo help/release notes.
2. Review source-code claims against a numbered tag/commit where reproducibility matters.
3. Keep development branch observations clearly marked as moving-branch evidence.
4. Recheck Android/Gradle/Kotlin/toolchain constraints that can change independently of CoGo.
5. Record device/build verification only when a reproducible run was actually performed.
6. Update `CHANGELOG.md` and `repository_manifest.json` after changes.

## Local quality checks

```bash
python -m unittest discover -s tests -v
python scripts/validate_repository.py
```

The validator has three classes of results:

- **Errors:** malformed JSON, missing required fields, duplicate canonical IDs, archive corruption, or mismatch with the historical Stage 7 manifest.
- **Warnings:** legacy metadata vocabulary, `local:` source references, and other known consistency issues.
- **Information:** record counts, manifest checks, and archive checks that passed.

Warnings do not imply that a claim is false. They identify work requiring evidence-aware cleanup.

## Update the repository inventory

```bash
python scripts/update_repository_manifest.py
```

Review the diff before committing it. The inventory excludes itself to avoid a self-referential hash. Keep `13_FINAL_PACKAGE_MANIFEST.json` unchanged unless intentionally issuing a new version of the original Stage 7 research package.

## Device-validation records

To mark an app or a claim as device-verified, keep a reproducible evidence record containing CoGo version/build, device model, Android version, template, actual generated Gradle/AGP/Kotlin versions, complete Build Output, APK details if generated, install/launch outcome, feature-specific tests, and relevant Logcat output. A code review or syntax check is not a substitute for such a record.
