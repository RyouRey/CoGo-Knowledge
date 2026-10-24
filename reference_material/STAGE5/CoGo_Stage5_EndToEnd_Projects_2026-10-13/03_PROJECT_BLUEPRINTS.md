# Project blueprints

| ID | Project | Template family | Learning goals | Persistence |
|---|---|---|---|---|
| P1 | Unit Converter | Kotlin + XML/View | input validation, event handler, text output | none |
| P2 | Quick Notes | Java + XML/View | multiple UI controls, list rendering, empty input | memory only; resets after process death |
| P3 | Compose Counter | Kotlin + Jetpack Compose | composable UI, state, click actions | none |

## Rules for applying any blueprint
- Create the project in CoGo first.
- Use the exact package that the generated project has. Replace the example `com.example...` package in code if necessary.
- Only replace files explicitly listed for that blueprint. Keep generated manifest, Gradle files, theme resources and wrapper.
- If a resource ID in the generated template differs, either change the XML and code together or use the blueprint's matching pair.
- A Compose project must come from a Compose-enabled template; pasting Compose imports into a Views-only project does not install Compose dependencies.
- These examples are designed to be small enough to diagnose on a phone. They are not production-ready architecture examples.
