# Version compatibility and migration

## Snapshot facts and source conflicts
- Official CoGo release notes identify version **26.41**, updated 2026-10-06, as the user-facing release in this research snapshot.
- The public GitHub releases page visible during the same snapshot showed **26.40** as the latest numbered public tag (released 2026-09-29).
- Therefore, 26.41 release-note claims should be cited as user-facing documentation, while source-level claims should name a pinned tag such as `26.40` or explicitly say they come from the moving `stage` branch.
- The repository `stage` branch is not a synonym for a released build and may contain unreleased features/API changes.

## Toolchain transition
Release 26.38 upgraded CoGo's core toolchain. The published updated-stack guide identifies Kotlin 2.3.21, AGP 9.3.1, Gradle 9.6.1 and Android Build Tools 36.0.0 for updated templates. Official 26.41 notes warn that projects created with 26.37 or earlier may fail until migrated.

## Safe migration workflow
1. Identify CoGo version and approximate project creation version.
2. Back up/copy the project before changing build files.
3. Try a normal build and capture the first specific error.
4. Read the official migration guide linked from the release notes.
5. Inspect the actual root build file, app-module build file, `gradle-wrapper.properties`, and optional `gradle/libs.versions.toml`.
6. Follow the migration case that matches the actual project. Do not blindly paste all version numbers into every file.
7. Sync, build, install, launch and run feature tests.
8. Keep the backup until the migrated project is confirmed.

## Compatibility matrix
| Situation | Guidance | Evidence status |
|---|---|---|
| New project created in current CoGo | Keep generated toolchain and template setup | official guidance |
| Project created in 26.37 or earlier, now opened in 26.38+ | Back up and follow current migration guide | official warning |
| Tutorial shows older Kotlin/AGP/Gradle | Do not copy pins automatically; inspect the project | derived safety rule |
| Compose code in Views-only project | Use a Compose template or fully configure compatibility with current docs | derived guidance |
| Offline dependency error | Determine whether the artifact is cached/available; offline-capable IDE does not imply all dependencies are cached | derived guidance |
| Plugin project | Separate build/API compatibility contract; do not apply ordinary app advice blindly | source-specific |

## Important stale-source trap
The June 2026 compatibility discussion still mentions older default stack values such as Kotlin 1.9.2 and AGP 8.11.0. That source predates the 26.38 toolchain transition. It must not be the sole authority for a project using the newer toolchain. Always prefer the current release/migration docs and actual project files.
