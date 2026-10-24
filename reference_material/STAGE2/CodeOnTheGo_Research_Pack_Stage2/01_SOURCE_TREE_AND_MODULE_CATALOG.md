# 1. Source Tree and Module Catalog

## 1.1 Repository identity
Main repository: `appdevforall/CodeOnTheGo`  
Main branch model described in repository instructions: `main` is release-oriented; `stage` is the protected integration/development branch; feature branches generally branch from `stage` and target `stage`.

The code still uses the namespace `com.itsaky.androidide`, reflecting its AndroidIDE lineage. Root Gradle configuration still names the root project `AndroidIDE`; do not interpret that as evidence that the current product is still the archived AndroidIDE app.

## 1.2 Root-level navigation
| Path | Why it matters | Evidence class |
|---|---|---|
| `README.md` | Project identity, install instructions, acknowledgements, license | Directly documented |
| `ARCHITECTURE.md` | Current architecture, module groups, constraints, build rules | Directly documented |
| `CLAUDE.md` | Repository-specific agent instructions and branch/build conventions | Directly documented |
| `AGENTS.md` | Agent-oriented repository rules; inspect before automated edits | Source-indexed |
| `CONTRIBUTING.md` | Contributor expectations and PR process | Directly documented |
| `SECURITY.md` | Vulnerability reporting and security policy | Directly documented |
| `settings.gradle.kts` | Included Gradle modules, composite builds, repository policy and dependency substitution | Source-inspected |
| `build.gradle.kts` | Root build logic, asset provisioning and shared tasks | Source-indexed |
| `gradle/libs.versions.toml` | Version catalog for dependencies and plugins | Source-inspected |
| `composite-builds/build-logic/` | Shared Android module configuration and build conventions | Directly documented |
| `composite-builds/build-deps/` | Vendored/forked build-time dependencies substituted into the build | Directly documented |
| `composite-builds/build-deps-common/` | Shared forked build dependency projects | Directly documented |
| `app/` | Application integration layer | Directly documented |
| `plugin-api/` | Public plugin contract and plugin builder | Directly documented |
| `plugin-manager/` | Plugin discovery/management/runtime integration | Directly documented |
| `lsp/` | Language server and refactoring subsystem | Directly documented |
| `editor/`, `editor-api/`, `editor-treesitter/`, `lexers/` | Code editing, language adapters, highlighting and tree-sitter support | Directly documented |
| `termux/` | Embedded terminal components | Directly documented |
| `quickbuild/` | Experimental quick-build subsystem | Directly documented |
| `subprojects/tooling-api*` | On-device Gradle tooling/process/event integration | Directly documented |
| `llama-api/`, `llama-impl/` | On-device llama.cpp integration | Directly documented |
| `testing/` | Shared test harnesses by subsystem | Directly documented |
| `apk-viewer-plugin/` | In-tree example cited by plugin authoring documentation | Directly documented |

## 1.3 Module families from `settings.gradle.kts` and architecture docs
The architecture describes approximately 80 Gradle modules plus three included composite builds. The count is approximate and can change.

### Application and shared infrastructure
- `:app`
- `:common`
- `:common-compose`
- `:common-ui`
- `:shared`
- `:resources`
- `:preferences`
- `:logger`
- `:build-info`
- `:actions`
- `:annotations`
- `:annotation-processors`
- `:annotation-processors-ksp`
- `:idetooltips`
- `:floating-window`
- `:lookup`
- `:logsender`, `:logsender-sample`

**Interpretation:** these provide the host app, shared UI/utilities, configuration, logging, build metadata, actions, generated code, and cross-module helpers. Confirm exact responsibilities in each module's README/build file/source before editing.

### Editor and language tooling
- `:editor`
- `:editor-api`
- `:editor-treesitter`
- `:lexers`
- `:lsp:api`
- `:lsp:external`
- `:lsp:models`
- `:lsp:indexing`
- `:lsp:java`
- `:lsp:jvm-symbol-index`
- `:lsp:jvm-symbol-models`
- `:lsp:kotlin`
- `:lsp:refactor-core`
- `:lsp:ui`
- `:lsp:xml`
- `:treeview`

**Interpretation:** separate editor widgets/contracts, syntax/language services, indexing, refactoring primitives, UI for refactoring and tree navigation. A module name does not prove every LSP capability is implemented to desktop-IDE parity.

### UI design and project templates
- `:uidesigner`
- `:xml-inflater`
- `:vectormaster`
- `:compose-preview`
- `:templates-api`
- `:templates-impl`

**Interpretation:** UI layout/vector/preview capabilities and project/template creation contracts. Sketch to UI is presented as an add-on feature, not simply another name for the XML inflater.

### Build system and project models
- `:gradle-plugin`
- `:gradle-plugin-config`
- `:subprojects:tooling-api`
- `:subprojects:tooling-api-events`
- `:subprojects:tooling-api-impl`
- `:subprojects:tooling-api-model`
- `:subprojects:projects`
- `:subprojects:project-models`
- `:subprojects:builder-model-impl`
- `:subprojects:aapt2-proto`
- `:subprojects:aaptcompiler`
- `:subprojects:framework-stubs`
- `:subprojects:xml-dom`
- `:subprojects:xml-utils`
- `:subprojects:javac-services`
- `:subprojects:kotlin-analysis-api`

**Interpretation:** build invocation/event bridge, project/build models, resource compilation support, framework/API stubs and compiler/language infrastructure. Trace call sites before asserting the exact boundary of each module.

### Plugin system
- `:plugin-api`
- `:plugin-api:plugin-builder`
- `:plugin-manager`

**Interpretation:** compile-time extension contract, artifact packaging and runtime management. The plugin API is a public boundary; app-private classes should not be treated as stable extension points.

### Terminal, AI, Git and experimental features
- `:termux:termux-app`
- `:termux:termux-emulator`
- `:termux:termux-shared`
- `:termux:termux-view`
- `:llama-api`, `:llama-impl` (architecture docs)
- `:git-core`
- `:profiler`
- `:quickbuild:core`
- `:quickbuild:daemon`
- `:quickbuild:protocol`
- `:quickbuild:runtime`

**Interpretation:** terminal integration, local inference, Git, profiling and an explicitly experimental quick-build family. Verify whether each is enabled/used in a particular release.

### Testing
- `:testing:android`
- `:testing:common`
- `:testing:lsp`
- `:testing:tooling`
- `:testing:unit`

**Interpretation:** shared test fixtures/harnesses grouped by the layer under test.

## 1.4 Composite builds and dependency substitution
`settings.gradle.kts` includes:
- `composite-builds/build-logic`
- `plugin-api/plugin-builder`
- `composite-builds/build-deps`
- `composite-builds/build-deps-common`

The settings file substitutes selected Maven coordinates under `com.itsaky.androidide.build:*` with local projects in the composite builds. Examples include `javac`, `jdt`, `layoutlib-api`, `treeview`, `javapoet`, `appintro`, and related components.

**Contributor rule:** do not add a new external Maven dependency for a component already supplied through a composite-build substitution. Check settings and the version catalog first.

## 1.5 ABI flavor convention
Architecture documentation states Android modules are configured centrally with:
- `v7` → `armeabi-v7a`
- `v8` → `arm64-v8a`

The plugin API module is excluded from the standard ABI flavors. Tasks may therefore be `assembleV8Debug` or `assembleV7Release`, not a flavorless `assembleDebug`.

## 1.6 Practical source-navigation recipe
For a bug or feature:
1. Search the UI action/label or error string.
2. Find the Activity/Fragment/Compose screen and ViewModel.
3. Follow repository calls into the data source or service.
4. Follow events/interfaces to the subsystem that performs work.
5. Read tests for the intended behavior and edge cases.
6. Inspect the Gradle file for dependencies, flavors, packaging and test setup.
7. Inspect release notes/PR history for when the behavior changed.
8. Record exact branch, commit SHA and source URL in your research notes.
