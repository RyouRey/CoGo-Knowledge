# Toolchain migration policy

## Official warning
CoGo release notes for 26.38 and later warn that projects created with 26.37 or earlier may fail to build until migrated. Release 26.41 repeats this warning. The release notes describe an upgrade of the development stack and link to a migration guide.

## Safe migration sequence
1. Record installed CoGo version and project creation/last-known-good version.
2. Duplicate or back up the entire project before changing build configuration.
3. Read the migration guide linked from the official release notes for the exact target release.
4. Compare root and app Gradle files, wrapper version, AGP/Kotlin declarations, and version catalog if present.
5. Apply only the migration guide's required changes; don't paste version pins from plugin-authoring docs into an ordinary application.
6. Sync and build the debug variant.
7. Install/launch and test the app.
8. Keep the backup until the new build and app behavior are confirmed.

## Do not conflate projects
- Ordinary Android app project: follows its generated template and the current CoGo app toolchain.
- CoGo plugin project: has its own plugin API/build-plugin compatibility contract and is outside the main goal of this knowledge base.
- Library project: may not produce an installable app and does not satisfy Quick Build eligibility.
- Legacy project: may need migration even when the same source files compile fine in a new project.

## Unknowns
This package summarizes the official migration warning, but does not attempt to reproduce every migration step because the authoritative linked guide is the version-sensitive source of truth. When producing user-specific migration instructions, fetch and cite the current official guide instead of relying on this summary alone.
