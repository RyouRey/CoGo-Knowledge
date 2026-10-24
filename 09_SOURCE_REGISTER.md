# Source register

Research snapshot: 2026-10-13. Recheck version-sensitive pages before relying on this corpus later.

## Current user-facing sources
1. CoGo 26.41 release notes (2026-10-06): https://appdevforall.org/code-on-the-go-release-notes-26-41/
2. CoGo product/download/compatibility page: https://appdevforall.org/code-on-the-go/
3. CoGo help index: https://appdevforall.org/codeonthego/help/index.html
4. New-project help: https://appdevforall.org/codeonthego/help/project-create-new.html
5. Build help: https://appdevforall.org/codeonthego/help/build-top.html
6. Layout/Compose help: https://appdevforall.org/codeonthego/help/layout-jpc-top.html
7. Official toolchain migration guide: https://github.com/appdevforall/CodeOnTheGo/wiki/IMPORTANT:-Fix-project-breaking-changes-after-the-Gradle-AGP-Kotlin-toolchain-upgrade
8. Toolchain modernization overview: https://appdevforall.org/modernizing-the-build-stack-benefits-and-breaking-changes/

## Repository sources
9. Main repository and releases: https://github.com/appdevforall/CodeOnTheGo
10. Public releases page: https://github.com/appdevforall/CodeOnTheGo/releases
11. Architecture (`stage`): https://github.com/appdevforall/CodeOnTheGo/blob/stage/ARCHITECTURE.md
12. E2E test (`stage`): https://github.com/appdevforall/CodeOnTheGo/blob/stage/app/src/androidTest/kotlin/com/itsaky/androidide/EndToEndTest.kt
13. Quick Build manual QA (`stage`): https://github.com/appdevforall/CodeOnTheGo/blob/stage/quickbuild/docs/manual-qa.md
14. Quick Build design note (`stage`): https://github.com/appdevforall/CodeOnTheGo/blob/stage/docs/adr/0016-quick-build-compiles-outside-gradle.md
15. Plugin authoring/API docs (`stage`): https://github.com/appdevforall/CodeOnTheGo/blob/stage/docs/PLUGIN_AUTHORING.md and https://github.com/appdevforall/CodeOnTheGo/blob/stage/docs/PLUGIN_API_CHANGELOG.md
16. Device compatibility discussion (2026-06-15): https://github.com/appdevforall/CodeOnTheGo/discussions/1394

## How to resolve source precedence
- Use official release notes/help for user-visible current behavior.
- Use a numbered release tag for source-code behavior when reproducibility matters.
- Use `stage` for development insight only, with a branch label.
- Use the user's actual project/build files for their local configuration.
- Use a physical-device log/test result for a device-specific claim.
- If older compatibility material conflicts with newer release notes, prefer newer release documentation and record the discrepancy.
