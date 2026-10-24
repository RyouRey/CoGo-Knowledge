# Source Register and Provenance

**Research date:** 2026-10-13. Links checked during this stage. This register distinguishes current user-facing guidance from pinned source-code context.

## Primary CoGo user documentation

1. **Create a new project** — https://appdevforall.org/codeonthego/help/project-create-new.html  
   Covers New Project flow, app name/package, location, language, minimum SDK, `.kts` choice, template descriptions, and project initialization.
2. **Work with projects and files** — https://appdevforall.org/codeonthego/help/project-top.html  
   General file/project structure context.
3. **Build your app** — https://appdevforall.org/codeonthego/help/build-top.html  
   Sync, run Gradle tasks, Build/install/launch, APK path.
4. **Write and edit code** — https://appdevforall.org/codeonthego/help/editor-top.html  
   Code editor and source-file workflow.
5. **Create UI with XML** — https://appdevforall.org/codeonthego/help/layout-top.html  
   XML resources and layout editor.
6. **Create UI with Jetpack Compose** — https://appdevforall.org/codeonthego/help/layout-jpc-top.html  
   XML vs Compose, Compose template, enabling Compose in Kotlin project, preview.
7. **Gradle** — https://appdevforall.org/codeonthego/help/gradle-top.html  
   Gradle task categories.
8. **Terminal** — https://appdevforall.org/codeonthego/help/terminal-top.html  
   Terminal usage, package installation, local Git.
9. **Create a keystore for release builds** — https://appdevforall.org/codeonthego/help/build-keystore.html  
   Signing key and release build workflow.
10. **Tutorial: Build a weight converter app** — https://appdevforall.org/codeonthego/help/tutorials.html  
    Official end-to-end sample tutorial entry point.
11. **Help index** — https://appdevforall.org/codeonthego/help/index.html  
    Index of Quick start, projects, editor, XML, Compose, build, debug, keystore, Git, plugins, Gradle, Java/Kotlin references.
13. **Weight converter tutorial** — https://appdevforall.org/codeonthego/help/tutorials.html  
    An official Java/Empty Activity workflow that names the setup values and the `MainActivity.java` and `activity_main.xml` paths.

## Current product/release sources

13. **CoGo release notes 26.41 (2026-10-06)** — https://appdevforall.org/code-on-the-go-release-notes-26-41/  
    Current release in snapshot; Quick Build constraints and behavior; other release features.
14. **Modernizing the build stack (release 26.38)** — https://appdevforall.org/modernizing-the-build-stack-benefits-and-breaking-changes/  
    Toolchain values and migration context: Kotlin 2.3.21, AGP 9.3.1, Gradle 9.6.1, Build Tools 36.0.0; version catalogs optional.
15. **Official migration guide** — https://github.com/appdevforall/CodeOnTheGo/wiki/IMPORTANT:-Fix-project-breaking-changes-after-the-Gradle-AGP-Kotlin-toolchain-upgrade  
    Case A/B migration depending on whether `gradle/libs.versions.toml` exists; specific Gradle file edits and known error signatures.
16. **CoGo device compatibility** — https://github.com/appdevforall/CodeOnTheGo/discussions/1394  
    Device compatibility discussion updated 2026-06-15. Some compatibility details are superseded by later toolchain releases, so prefer current official release pages for current values.
17. **CoGo repository README at pinned tag 26.40** — https://github.com/appdevforall/CodeOnTheGo/blob/26.40/README.md  
    Product identity and official links. Repository source snapshot used for continuity with Stage 3; not a complete guide to user workflow.
18. **CoGo version catalog at tag 26.40** — https://github.com/appdevforall/CodeOnTheGo/blob/26.40/gradle/libs.versions.toml  
    Source-level version reference for the IDE itself; not the authoritative source for every user project's template version.

## Evidence details

- The official project-creation help page says app name updates the package field automatically, asks for language and minimum SDK, and offers `.kts` as an option. It lists No Activity, Empty Activity, Basic Activity, Navigation Drawer, Bottom Navigation, Tabbed, Legacy (No AndroidX), and Compose templates.
- Official build help documents project sync, task selection, build/install/launch, and a conventional APK output directory.
- The Compose help page says CoGo supports XML/View System and Compose, with Compose Kotlin-only.
- Release 26.41 notes say Quick Build is experimental and requires a launchable Activity, single process, debug variant, and more memory/storage than a normal build.
- The 26.38 stack update is a breaking change for older projects. New templates generated after the upgrade should not need manual migration.

## Limitations

- The research did not install CoGo or run a sample app on a physical device.
- User-facing help pages may have UI text or details updated after this snapshot.
- The pinned repository tag is 26.40 while the current release notes observed are 26.41; the difference is intentional and documented.
- The online search result for current CoGo landing page had a stale summary for 26.39 even though the 26.41 release notes were published later. This package therefore treats the dated 26.41 release-notes page as the current release source in this snapshot.
- General Android implementation recommendations are derived guidance and must be checked against the actual target SDK, library versions, and app requirements.
