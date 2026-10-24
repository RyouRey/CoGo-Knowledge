# Acceptance tests and known gaps

## What was checked for Stage 7
- [x] Five prior stage packages found and preserved.
- [x] Source JSONL files parsed successfully.
- [x] Original records normalized into a shared master schema while preserving each original record.
- [x] Exact duplicates merged while retaining source lineage.
- [x] Master JSONL parsed successfully.
- [x] Final ZIP archive integrity checked.
- [x] Version conflict between official 26.41 release notes and public 26.40 tag documented.
- [x] Source-review status kept separate from device verification.

## What was not checked
- [ ] No Stage 5 sample app was built in CoGo during this research run.
- [ ] No APK was generated or installed by this research run.
- [ ] No CoGo repository unit/E2E tests were executed by this research run.
- [ ] No physical-device test matrix was completed.
- [ ] No exhaustive audit of all CoGo source files or all Android device/toolchain combinations was performed.

## Why Stage 6 is marked incomplete
Stage 6 was planned as the hands-on validation/hardening stage, but the user explicitly requested the final Stage 7 before a separate Stage 6 execution package was produced. This Stage 7 package completes the synthesis and structural QA, but does not retroactively claim device validation. The missing hands-on tests remain visible as unresolved gaps.

## Final acceptance criteria for a future update
A future revision may mark a project `device_verified` only after a reproducible record includes:
- CoGo version/build;
- device model and Android version;
- project template and package;
- actual generated Gradle/AGP/Kotlin versions;
- complete Build Output;
- APK path/variant/timestamp if produced;
- install and launch result;
- feature-specific test results;
- Logcat excerpt for failures;
- a second person can follow the steps.

## Final verdict
**Stage 7 synthesis: complete. Physical-device validation: incomplete.** These are separate statuses and must not be conflated.
