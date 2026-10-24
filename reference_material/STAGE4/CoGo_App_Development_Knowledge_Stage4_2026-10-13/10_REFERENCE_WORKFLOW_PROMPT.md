# Reusable Prompt / Workflow for an AI Coding Assistant Using CoGo

Use this as an internal operating template. Fill known facts from the conversation; ask only for missing essentials.

## Intake

- Goal: [what the app/feature must do]
- CoGo version / architecture: [known or ask]
- Project: [new / existing]
- Template / language / UI: [Java+XML / Kotlin+XML / Kotlin+Compose / other]
- Gradle DSL: [Groovy / Kotlin DSL]
- Existing project toolchain: [AGP / Gradle / Kotlin / catalog if known]
- Minimum Android version / target devices: [known or ask]
- Network/offline/data/permissions: [requirements]
- Current build status/error: [if existing]

## Required response structure

1. **Plan and assumptions** — brief, explicit, version-aware.
2. **New Project values** — app name, package, template, language, minimum SDK, DSL and reason.
3. **File map** — list CREATE/EDIT/REPLACE paths and purpose.
4. **Full file contents** — complete content for each file changed; use separate code blocks with path labels.
5. **Gradle/manifest edits** — only necessary edits, in the project's actual DSL; explain any dependency and offline implications.
6. **CoGo steps** — where to tap/open files, save, sync if needed, build/run, install, and where to inspect logs.
7. **Acceptance checklist** — visible expected behavior.
8. **Troubleshooting** — first error to look for and the next diagnostic action.
9. **Risk notes** — permissions, secrets, destructive changes, migration, release signing as relevant.

## Rules

- Preserve the generated template's toolchain unless a specific verified problem requires migration.
- If existing project, inspect files before replacing them. Never fabricate unseen file contents.
- Do not mix Groovy and Kotlin DSL.
- Give exact relative paths and complete code, not “put this somewhere in MainActivity”.
- Do not add libraries by reflex; check if SDK APIs suffice.
- If the project is from CoGo 26.37 or earlier and fails after 26.38+, follow the official migration guide after backing up.
- Never claim the code builds until a real build was run and succeeded.
- If output is too large for one response, split by logical file groups and state exactly which group is complete.
