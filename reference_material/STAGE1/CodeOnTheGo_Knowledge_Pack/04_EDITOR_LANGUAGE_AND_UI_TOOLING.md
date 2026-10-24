# 4. Editor, Language Tooling, UI Tools and Debugging

## 4.1 Code editor and language support
The architecture lists Sora-based editor modules, language-server modules (`lsp:*`), lexers, indexing, and Tree-sitter-based editor support. These subsystems underpin editing experiences such as syntax highlighting, language intelligence, project indexing, outlines and refactoring.

Representative areas:
- `editor*` and `editor-treesitter`: editor surface and syntax/document tooling.
- `lexers`: lexical/syntax support.
- `lsp:api`, `lsp:java`, `lsp:kotlin`, `lsp:xml`, `lsp:indexing`, `lsp:refactor-core`, `lsp:ui`: language-specific and shared language features.
- `editor/.../language/outline`: tree-sitter-backed document outline rendered by app UI.

Do not assume all language-server capabilities match desktop IDEs. Check the actual implementation, tests and current release for the feature under investigation.

## 4.2 Refactoring design
The architecture notes identify a shared, language-agnostic `lsp:refactor-core` for offset spans, block geometry, rewrite composition and name primitives, used by Java and Kotlin refactoring implementations. Shared UI for refactoring sheets is placed in `lsp:ui`.

This illustrates a sound design principle: keep syntax/language-specific parsing and semantics in language modules, while sharing edit geometry and UI patterns when possible.

## 4.3 UI and layout design tools
Documented UI-design modules include:
- `layouteditor`
- `uidesigner`
- `xml-inflater`
- `vectormaster`
- `compose-preview`

These are distinct tools with different jobs:
- A layout editor offers visual interaction with layout structures.
- XML inflation/rendering supports displaying Android XML layouts in a preview context.
- Vector tooling assists with vector drawable workflows.
- Compose preview supports previewing the user's Jetpack Compose UI code.
- Sketch to UI is an add-on workflow that converts a photographed hand-drawn interface sketch into Android XML.

For a specific UI rendering discrepancy, determine whether the issue is in source XML/Compose, the preview/inflater implementation, Android resource resolution, or runtime behavior on the device.

## 4.4 Terminal
CoGo embeds Termux-related modules (`termux-app`, `termux-shared`, `termux-view`, `termux-emulator`). This provides a shell/terminal capability as part of the mobile development environment.

A terminal is useful for project inspection and build/debug commands, but do not assume every desktop Linux binary or arbitrary package can run on Android. Android's sandbox, CPU ABI, executable permissions, storage paths and bundled environment matter.

## 4.5 On-device debugger
The official product page describes an on-device debugger that bootstraps privileged access and avoids the need for additional hardware. The public landing-page summary does not expose all implementation details, so the precise privilege model, supported Android versions and limitations should be verified in the dedicated debugger documentation and source code before making low-level claims.

For debugging an app, separate these layers:
1. **Compile-time** — syntax/type/resource errors.
2. **Gradle/configuration** — plugin, dependency, variant and task errors.
3. **Install-time** — package/signature/version/permission or ABI issues.
4. **Startup/runtime** — crash, exception, native crash, permission or lifecycle issue.
5. **Functional behavior** — app launches but logic or UI is wrong.

## 4.6 Log and error handling workflow
- Preserve the full stack trace and the first causal exception.
- Identify the process and package that crashed: CoGo itself or the user's app.
- Distinguish Java/Kotlin exceptions from native crashes and build failures.
- Reproduce with the smallest project or smallest change possible.
- Include device Android version, ABI, CoGo version and project toolchain.
- For a regression, compare the last known good release/commit with the failing one.

## 4.7 UI architecture in CoGo itself
New CoGo UI follows Compose + UDF, while legacy Views remain. When adding a new screen, the intended pattern is generally:
- immutable/sealed UI state;
- ViewModel owns state and work;
- sealed UI events/intents for user actions;
- separate effects flow for one-off events;
- repository abstraction for data access;
- dependency injection through Koin;
- lifecycle-aware collection in the UI.

Follow the exact package conventions and tests for the subsystem. A migration-in-progress repository can have valid local exceptions.
