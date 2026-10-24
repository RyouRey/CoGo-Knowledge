# Stage 6 backlog — expand, troubleshoot, and validate

Stage 6 is the final hardening stage before Stage 7 synthesis. Keep the user goal focused on building apps with CoGo.

## Priority 1 — real device verification
- Obtain a device with a named CoGo release installed.
- Record Android version, CPU architecture, available RAM/storage, CoGo version.
- Build and run each of the three example projects from the generated template baseline.
- Save exact project trees, generated Gradle files, Build Output, install/run outcomes, and test results.
- Change evidence status only after real execution.

## Priority 2 — compatibility matrix
- Compare Java/XML, Kotlin/XML, and Compose templates on the same CoGo version.
- Check 32-bit vs 64-bit only when devices/builds are available.
- Test a project created before 26.38 with the official migration guide; never infer migration steps from the warning alone.
- Capture which edits are eligible for Quick Build and which fall back to Gradle.

## Priority 3 — error corpus
Create minimal reproducible examples for:
- invalid package name;
- missing resource ID;
- malformed XML;
- missing Compose dependency/template;
- unresolved library/dependency;
- AGP/Gradle mismatch;
- manifest merge error;
- runtime crash;
- install permission or app-ID replacement issue;
- low storage/memory failure.
For each, store the original error, root cause, minimal fix, retest output, and scope.

## Priority 4 — expand app types
- persistent notes using Room or SQLite only after dependency/template compatibility is confirmed;
- network API example with timeout/error/loading states;
- local data/file access and permission flow;
- multi-screen navigation;
- app signing/release artifact;
- accessibility and small-screen UI checks.

## Exit criteria for Stage 6
- Every source-derived claim has a version and source.
- Every tested blueprint has evidence logs or explicitly remains unverified.
- No generic Gradle pins are recommended without checking the project.
- Error records include root cause and a successful retest or a clear unresolved status.
- Dataset schema validates and duplicate/conflicting records are reviewed.
