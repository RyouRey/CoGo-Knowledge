# Source manifest and research anchors

Research snapshot: 2026-10-13.

## Official CoGo documentation
1. Release 26.41 notes (published 2026-10-06): https://appdevforall.org/code-on-the-go-release-notes-26-41/
   - Evidence: current release snapshot, migration warning, experimental Quick Build requirements and flow.
2. CoGo download/compatibility page: https://appdevforall.org/code-on-the-go/
   - Evidence: general supported device/toolchain notes; check page freshness because its captured text may lag a newer release.
3. Quick Build development design note (branch `stage`): https://github.com/appdevforall/CodeOnTheGo/blob/stage/docs/adr/0016-quick-build-compiles-outside-gradle.md
   - Evidence: Quick Build pipeline boundaries and tradeoffs; development-branch evidence only.
4. Quick Build manual QA (branch `stage`): https://github.com/appdevforall/CodeOnTheGo/blob/stage/quickbuild/docs/manual-qa.md
   - Evidence: manual test procedures for basic app edits, resource changes, syntax errors, and fallback behavior; does not prove the tests were run by this research.
5. End-to-end template creation test (branch `stage`): https://github.com/appdevforall/CodeOnTheGo/blob/stage/app/src/androidTest/kotlin/com/itsaky/androidide/EndToEndTest.kt
   - Evidence: test code exercises onboarding and creation of No Activity, Empty Activity, and Basic Activity templates.
6. Java/XML sample project source (branch `stage`): https://github.com/appdevforall/CodeOnTheGo/blob/stage/testing/resources/sample-project/app/src/main/java/com/itsaky/androidide/template/Java/kts/MainActivity.java
   - Evidence: Java Activity and generated view-binding pattern in an internal sample fixture.
7. Java/XML sample layout: https://github.com/appdevforall/CodeOnTheGo/blob/stage/testing/resources/sample-project/app/src/main/res/layout/activity_main.xml
8. Kotlin debugger fixture setup: https://github.com/appdevforall/CodeOnTheGo/blob/stage/testing/resources/kotlin-debug-fixture/README.md
9. Release listing: https://github.com/appdevforall/CodeOnTheGo/releases
   - Evidence: numbered public release listing visible during this snapshot.

## Source pin policy
- Use release notes for user-facing behavior and version warnings.
- Use pinned release tags for stable source claims whenever possible.
- Use `stage` only to understand newer implementation/testing, and label it as such.
- When source branch and release notes differ, do not silently combine them into one guaranteed behavior.
- Re-check these links before Stage 6/7 because CoGo changes regularly.

## Limits
This research run did not clone/build CoGo, did not run the repository's Android tests, did not create APKs, and did not test the three blueprint projects on a physical phone. The sample code is a reference implementation awaiting device verification.
