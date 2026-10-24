# Project Creation and Template Decision Guide

## Official CoGo flow

CoGo Help (`Create a new project`) documents this flow:

1. Main menu → **Create project**.
2. Select a template.
3. Enter **App name**. The package name is automatically updated based on the app name.
4. Keep the default save location or select another using **Save location**.
5. Choose **Java** or **Kotlin**.
6. Choose **Minimum SDK** (the oldest Android version to support).
7. Optionally select **Use Kotlin Script (.kts) for Gradle build files**.
8. Tap **Create project** and wait for **Project initialized**.
9. Open the Project menu / swipe from the left to inspect the generated file tree.

The exact screen can change between CoGo releases. Use the installed app's labels and current help if they differ.

## Naming

- **App name**: human-facing display/project name. Use readable words; CoGo permits letters, digits (not as first character), and underscores per the help page.
- **Package/application ID**: use a stable reverse-domain style such as `id.example.myapp`. Keep it lowercase, avoid spaces/hyphens, and treat it as an identity rather than a display label.
- Changing the package/namespace later can require edits in source declarations, manifest, Gradle `namespace`, and possibly application ID. Do not rename it casually after publishing.
- App name and package name are not interchangeable.

## Template selection

| Template | Choose when | Cautions |
|---|---|---|
| **No Activity** | Experienced user wants full control and understands manifest/Activity setup | Not a beginner default; must create the launchable Activity and supporting configuration manually |
| **Empty Activity** | Simple conventional app, beginner, XML/View-based work | Official help describes a simple `MainActivity` with no navigation/interaction elements |
| **Basic Activity** | Need a starter screen with floating action button | Remove/replace sample behavior deliberately |
| **Navigation Drawer Activity** | App has several major sections and a side drawer is appropriate | More scaffold than a one-screen utility needs |
| **Bottom Navigation Activity** | Three or more peer sections that should remain quickly accessible | Don't choose just for decoration; plan each destination |
| **Tabbed Activity** | Closely related content pages where tabs are natural | Check generated scaffold before assuming implementation details |
| **Legacy Activity (No AndroidX)** | Only when compatibility with old Support Library is an explicit requirement | Official help warns this is outdated; avoid for new projects by default |
| **Compose Activity** | Kotlin-first app using Jetpack Compose UI in Kotlin code | Kotlin only; confirm generated Compose setup and preview/build support in installed CoGo version |

## Practical defaults (recommendations, not CoGo-enforced rules)

For a first conventional app with a few screens or forms, use **Empty Activity** and choose Kotlin or Java according to the user's existing skills. For a Kotlin UI intended to use Compose, choose **Compose Activity** rather than trying to bolt Compose onto an unrelated template. For a beginner who explicitly wants Java and XML, use an XML/View-based template and retain the generated project structure.

### Language choice

- **Java + XML**: good for users who know Java, conventional View-based UI, and broad existing examples.
- **Kotlin + XML**: combines Kotlin language with traditional XML layouts; useful if user wants Kotlin but not Compose.
- **Kotlin + Compose**: declarative UI in Kotlin; avoid mixing in XML layouts unless there is a specific reason.

Do not assume every CoGo template supports every language combination. The UI and generated files are the source of truth.

## Minimum SDK decision

Minimum SDK is a product/support decision, not a magic value.

1. Ask which oldest Android version/device the app must support.
2. Pick the corresponding API level using current Android platform references.
3. Prefer the template's offered/default value unless a compatibility requirement changes it.
4. Check library minimum SDK requirements before adding dependencies.
5. Distinguish `minSdk` (oldest supported runtime), `targetSdk` (behavior/policy target), and `compileSdk` (API surface used to compile).

Do not choose the highest available minimum SDK merely to avoid compatibility work. Do not promise compatibility with devices below `minSdk`.

## Gradle DSL choice

- If user is new and the chosen template defaults to Kotlin DSL, keeping `.kts` is fine.
- If continuing an existing project, follow its existing DSL.
- Kotlin DSL uses `implementation("group:artifact:version")`, `id("plugin.id")`, and `isMinifyEnabled = true` style.
- Groovy DSL uses `implementation 'group:artifact:version'`, `id 'plugin.id'`, and `minifyEnabled true` style.
- Never copy a whole build snippet without checking which DSL and AGP generation the project uses.

## Post-creation checkpoint

Before writing feature code, confirm:

- CoGo shows **Project initialized**.
- The project tree contains the expected `app` module and generated files.
- The launch Activity exists for an app template.
- The app builds once without changes, if practical. This baseline isolates template/toolchain issues from later code errors.
- Save a backup or Git commit before significant work.
