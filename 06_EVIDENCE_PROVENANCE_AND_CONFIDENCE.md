# Evidence, provenance and confidence rules

## Evidence classes
- `official_current`: current official CoGo help/release note observed on the snapshot date.
- `official_versioned`: official source pinned to a numbered release/tag.
- `official_test_definition`: checked-in test/QA scenario. Proves a test is defined, not that it was executed during this research.
- `source_stage`: moving development branch; may contain unreleased behavior.
- `android_platform`: general Android/Gradle/Kotlin behavior, versioned where necessary.
- `derived_guidance`: practical synthesis from documented behavior; validate against the user's actual project.
- `reference_code_unverified`: code authored for a package but not built/tested on device.
- `device_verified`: only after a named CoGo version/device built, installed, launched and passed the recorded tests.

## Non-negotiable honesty rules
1. Never describe a source-reviewed test as a test that ran.
2. Never describe a code sample as CoGo-verified without build/test evidence.
3. Never say an APK was generated unless the artifact or Build Output exists.
4. Never infer current behavior from the `stage` branch without labeling it.
5. Do not treat all facts from old compatibility pages as current after a toolchain migration.
6. Preserve negative results and unresolved errors; they are valuable evidence.
7. When a claim is version-sensitive, store the version and date.
8. When official sources conflict or have different update cadence, state the conflict and prefer the source appropriate to the claim.

## Provenance minimum for every record
`canonical_id`, topic, statement, source stage/record IDs, source URLs, version scope, evidence class, verification status, confidence, date reviewed, caveat, and original record payload.

## Confidence meaning
- **High:** explicit, current first-party source or direct reproducible evidence.
- **Medium:** derived synthesis or a source whose version/coverage is limited.
- **Low:** hypothesis, incomplete evidence, or an unconfirmed workaround.
Confidence does not equal test execution. A high-confidence statement can still be source-reviewed only.
