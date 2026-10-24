# 6. Editor, LSP, UI Design and Debugging

## 6.1 Editor stack
Architecture documentation identifies Sora-based editor modules, language servers under `lsp:*`, lexers, indexing and Tree-sitter support. The editor subsystem is separate from language-specific intelligence, even where the UI presents the features together.

Source families:
- `editor`, `editor-api`: editor surface and contracts.
- `editor-treesitter`, `lexers`: parsing/highlighting support.
- `lsp:api`, `lsp:external`, `lsp:models`: shared protocol/contracts/models.
- `lsp:java`, `lsp:kotlin`, `lsp:xml`: language-specific tooling.
- `lsp:indexing`, `lsp:jvm-symbol-index`, `lsp:jvm-symbol-models`: indexing and symbol information.
- `lsp:refactor-core`, `lsp:ui`: shared refactoring logic and UI.
- `treeview`: tree-oriented UI/helper component.

## 6.2 LSP investigation model
For an editor-intelligence issue, distinguish:
1. Syntax highlighting/lexer failure.
2. Parser/tree-sitter failure.
3. Project indexing or symbol graph failure.
4. Language server startup/communication failure.
5. Semantic analysis or dependency classpath failure.
6. Refactoring edit-range or document synchronization failure.
7. UI rendering or stale state.

A visual symptom such as “red underline missing” does not identify the layer. Search tests and logs for the earliest failing subsystem.

## 6.3 Refactoring separation
Architecture documentation says `lsp:refactor-core` stores language-agnostic edit primitives such as offset spans, block geometry, rewrite composition and name primitives. Java/Kotlin modules can share this logic, while `lsp:ui` holds shared Compose sheets. The design keeps generic text-edit mechanics separate from language-specific parsing/semantics.

## 6.4 UI design tools
Documented modules:
- `uidesigner`
- `xml-inflater`
- `vectormaster`
- `compose-preview`
- `templates-api` and `templates-impl`

Interpretation:
- Layout editing is distinct from runtime rendering.
- XML inflation/preview is distinct from Android's final on-device resource/runtime behavior.
- Vector drawable editing is distinct from general image editing.
- Compose preview targets the user's Compose UI; it does not imply that CoGo's whole own interface is Compose.
- Sketch to UI is described as an add-on workflow converting a photo of a hand-drawn interface into Android XML.

## 6.5 Terminal
Termux-related modules provide the embedded terminal environment. Android is not a general desktop Linux distribution: CPU ABI, app sandbox, executable permissions, storage access, available binaries and Android process restrictions all matter. Do not promise arbitrary desktop Linux package compatibility.

## 6.6 Debugging
The product page advertises on-device debugging. Architecture material also lists privileged-service/Shizuku-related modules, but a full description of exact debugger privilege mechanics requires implementation-level inspection. Do not infer the precise security model solely from module names.

When investigating a debug issue, classify it:
- compile/sync failure;
- debugger attach/start failure;
- breakpoint binding/location failure;
- stepping/variable evaluation failure;
- app runtime exception;
- native crash;
- install/signature/ABI failure.

The 26.40 release notes list work on Kotlin breakpoints, resolving breakpoint locations, stepping and variables. Confirm whether the relevant feature is present in the installed release.

## 6.7 Debug report checklist
- CoGo version and release channel.
- Android version, device ABI and free RAM.
- User project build configuration.
- Exact reproduction steps.
- Whether the issue occurs in Java, Kotlin, XML or Compose.
- Complete relevant logs and stack trace.
- Expected and actual behavior.
- Whether it began after an IDE/toolchain upgrade.
- Minimal project or sanitized source excerpt.
