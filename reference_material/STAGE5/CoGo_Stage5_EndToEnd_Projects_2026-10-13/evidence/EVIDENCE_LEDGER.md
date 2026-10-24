# Evidence ledger

| Claim | Evidence class | Source | Status |
|---|---|---|---|
| CoGo 26.41 release notes dated 2026-10-06 | official_release_doc | https://appdevforall.org/code-on-the-go-release-notes-26-41/ | source reviewed |
| Projects made in 26.37 or earlier may fail on 26.38+ unless migrated | official_release_doc | same 26.41 notes | source reviewed |
| Quick Build is experimental and needs eligible app, launchable Activity, one process, debug variant | official_release_doc | same 26.41 notes | source reviewed |
| CoGo repository includes E2E tests creating No Activity, Empty Activity, Basic Activity | official_test_definition | https://github.com/appdevforall/CodeOnTheGo/blob/stage/app/src/androidTest/kotlin/com/itsaky/androidide/EndToEndTest.kt | source reviewed; not executed here |
| Quick Build manual QA covers code edit, syntax error, resource edit, fallback | official_test_definition | https://github.com/appdevforall/CodeOnTheGo/blob/stage/quickbuild/docs/manual-qa.md | source reviewed; not executed here |
| P1 Kotlin/XML converter compiles and behaves correctly | reasoned_reference_code | project files in this package | NOT DEVICE VERIFIED |
| P2 Java/XML notes compiles and behaves correctly | reasoned_reference_code | project files in this package | NOT DEVICE VERIFIED |
| P3 Compose counter compiles and behaves correctly | reasoned_reference_code | project files in this package | NOT DEVICE VERIFIED |
| Final APK produced by this research | none | none | NOT PRODUCED |
