# Evidence and version policy

## Why this matters
CoGo is an evolving mobile IDE. A code sample can be valid Android code yet fail in a particular project because the generated template, package name, SDK configuration, AGP/Kotlin version, dependencies, or device architecture differs.

## Version baseline (snapshot: 2026-10-13)
- User-facing release documentation: CoGo 26.41, dated 2026-10-06.
- Public numbered GitHub release visible in the repository release listing: 26.40, dated 2026-09-29.
- The repository `stage` branch contains newer work including Quick Build internals. Treat it as development-branch evidence, not an automatic guarantee about every installed release.
- CoGo release notes warn that projects created with 26.37 or earlier may fail on 26.38+ unless migrated.
- CoGo documentation says it bundles JDK 21 and documents supported AGP range; use the current compatibility page rather than inventing toolchain pins.

## Evidence labels
1. `official_release_doc`: a published CoGo release note/help page.
2. `source_at_release`: code from a pinned, published source tag.
3. `source_stage`: current development branch; useful for understanding implementation but not a release guarantee.
4. `official_test_definition`: a checked-in automated test or manual QA scenario. It proves that a test is defined, not that this research run executed it.
5. `reasoned_reference_code`: code authored for this package and reviewed for consistency, but not built in CoGo in this run.
6. `device_verified`: only allowed after the exact project has been built, installed, launched, and tested on a documented device/version. Requires evidence log and reproducible steps.

## Never upgrade evidence without proof
Do not call a sample “tested”, “build-verified”, or “works on CoGo 26.41” unless the test actually happened on that environment. Record failures as useful evidence too.

## Version-sensitive instructions
- Start from a template created by the installed CoGo version.
- Keep generated Gradle wrapper/build files unless there is evidence that they must change.
- Use the template's existing package and namespace, or explicitly update all package declarations and references consistently.
- Do not copy an old internet example's Gradle versions into a new project.
- For older projects, back up before migration and follow the official migration guide matching the installed CoGo version.
- Treat Quick Build as an optional experimental edit loop with eligibility restrictions; use normal Gradle build/run as the authoritative baseline.
