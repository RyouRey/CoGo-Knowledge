# UI Architecture: XML/View System vs Jetpack Compose

CoGo's official help supports two UI approaches:

- **XML/View System:** layout lives in XML resources; app behavior is wired in Java or Kotlin.
- **Jetpack Compose:** UI is written in Kotlin using composable functions; Kotlin only.

## Choose based on project context

| Need | Recommended approach | Reason |
|---|---|---|
| Existing project already uses XML layouts | Continue XML/View System | Avoid a large UI migration |
| User wants Java | XML/View System | Compose is Kotlin-only |
| User is learning conventional Android file placement | XML/View System | Separates UI layout from behavior and exposes resource/manifest concepts |
| New Kotlin-first UI with state-driven screens | Compose template | Declarative UI and state-driven updates |
| User asks to match a generated Compose template | Keep Compose | Preserve its plugin/compiler/dependency setup |
| Mixed UI requested | Clarify why; add interop only deliberately | Mixed architectures add complexity |

## XML/View workflow

1. Inspect the generated Activity and layout file.
2. Place layout in `app/src/main/res/layout/`.
3. Define stable IDs for interactive controls.
4. Load/bind the layout using the template's existing pattern (for example `setContentView` and `findViewById`, ViewBinding, or another scaffold already generated).
5. Put user-visible text in string resources where practical.
6. Wire events and state in Activity/Fragment/ViewModel as appropriate.
7. Build, launch, and test orientation/small-screen behavior.

Do not assume the template uses ViewBinding. Inspect its Gradle file and generated code first.

## Compose workflow

1. Start with CoGo's Compose Activity template when creating a new Compose project.
2. Inspect the generated `MainActivity` and existing `@Composable` entry function.
3. Keep the generated Compose dependencies/compiler setup intact.
4. Model changing UI with state rather than manually mutating view widgets.
5. Split large screens into small composables; keep business logic out of composable rendering where feasible.
6. Use CoGo's Compose preview if available in the installed release/project; otherwise build and run.
7. Validate actual runtime UI. A preview is helpful but does not replace end-to-end testing.

## Enabling Compose in an existing Kotlin project

Official CoGo help shows `android { buildFeatures { compose = true } }` for Kotlin DSL and `compose true` for Groovy DSL. This is only one part of Compose configuration; compiler/plugin/dependency requirements depend on the AGP/Kotlin stack. Do not paste the switch alone into an arbitrary old project and promise it is sufficient. Prefer the current CoGo Compose template and preserve its generated versions.

## UI acceptance checks

- Controls are reachable and labeled.
- Long text and narrow screen widths do not overflow.
- Touch targets are usable.
- Loading, empty, success, and error states are visible.
- Back navigation behaves correctly.
- State survives configuration changes or process recreation where required.
- Accessibility: content descriptions for meaningful images/icons, adequate contrast, and sensible semantics.
