# 7. Next Research Backlog

## Completed in this stage
- Pin the release tag and commit.
- Capture source file blob SHAs for deep links, plugin runtime, Gradle build service, architecture and key tests.
- Identify implementation anchors and selected line numbers.
- Compare implementation structure with documented architecture.
- Separate directly observed facts from proposed tests.

## Next high-value steps
1. Fetch the full `DeepLinkRequest` parser/writer and map every branch to the exact test method.
2. Fetch the actual contained-path resolver implementation, not just its tests, and verify lexical/canonical/symlink checks.
3. Trace deep-link request hand-off across `DeepLinkActivity`, `MainActivity`, editor activities and project sync.
4. Trace `PluginManager` from installed file discovery through metadata parsing, permission validation, class loading, `initialize`, `activate`, registration, deactivation and disposal.
5. Inspect `PluginSecurityManager` and every sensitive service implementation to map permission enforcement to actual operations.
6. Inventory plugin runtime tests at tag `26.40`; identify untested error/rollback paths.
7. Trace `GradleBuildService` from the public build request to server start, request payload, event callback, terminal result and cleanup.
8. Inspect tooling API server-side counterpart and event/result types.
9. Map the 26.40 Kotlin debugger release-note items to their implementation files and tests.
10. Generate a machine-readable module dependency graph from Gradle project dependencies.
11. Run only feasible targeted tests in a reproducible checkout and record exact command, environment and outcome.
12. Repeat for next release tag and produce a tag-to-tag implementation delta.

## Definition of done for a true code trace
A case study is complete only when it has:
- pinned source commit;
- exact entry point and call chain;
- data/control-flow description;
- error and cancellation branches;
- test methods linked to each invariant;
- explicit unverified areas;
- no claim of test execution unless actually executed.
