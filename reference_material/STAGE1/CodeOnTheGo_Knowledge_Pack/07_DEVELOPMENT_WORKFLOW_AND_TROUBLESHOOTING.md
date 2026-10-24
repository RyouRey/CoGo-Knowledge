# 7. Development Workflow and Troubleshooting

## 7.1 Workflow for using CoGo to build an Android app
1. Install CoGo from the official site and allow setup to finish.
2. Ensure sufficient free storage and RAM.
3. Create or open a project using a template compatible with the installed CoGo toolchain.
4. Record application ID/package name, language, minimum SDK, AGP, Gradle wrapper and Kotlin plugin versions.
5. Add/edit source files, resources, manifest and Gradle configuration.
6. Run project sync/configuration.
7. Build the appropriate debug variant.
8. Read the first meaningful error if the build fails; distinguish sync, dependency, compilation, packaging and install errors.
9. Install/run the generated APK and check runtime behavior.
10. Capture logs and reproduce the issue with minimal changes.
11. Commit a working state before attempting a major upgrade or migration.

## 7.2 Workflow for contributing to CoGo itself
Follow repository-specific instructions first. The inspected `CLAUDE.md` documents a branch model:
- `main` is the release branch and receives merges from `stage`.
- `stage` is the protected integration/default branch.
- Feature work branches from `stage` and opens a PR to `stage`.
- Official/public actions such as releases and external publishing run in GitHub Actions, not as ad hoc local commands.

Always check the current contribution guide and automation before making changes; these instructions may evolve.

## 7.3 Choosing the right subsystem
| Symptom / feature | First places to inspect |
|---|---|
| Screen state or navigation | UI screen, ViewModel, UI state/effect/event types |
| Data persistence | Repository, Room DAO/database, preferences or SQLite source |
| Gradle sync/build progress | `tooling-api`, build integration, event types, logs |
| Syntax highlighting or editor behavior | `editor*`, `lexers`, `editor-treesitter` |
| Java/Kotlin language intelligence | relevant `lsp:*` module and tests |
| XML preview/layout | `xml-inflater`, `layouteditor`, `uidesigner` |
| Compose preview | `compose-preview` and its integration |
| Plugin fails to load | plugin manifest metadata, plugin manager, public API version |
| AI agent/tool failure | agent repository/backend, tool registry, permissions, cancellation |
| Local inference failure | `llama-api`, `llama-impl`, ABI/model assets/device resources |
| Git behavior | JGit integration and repository state |
| Release APK size/packaging | root/app Gradle scripts, native library settings, CI post-processing |

## 7.4 Troubleshooting matrix
### Project will not sync
- Check wrapper and AGP compatibility.
- Check repository/dependency resolution.
- Check missing SDK components.
- Verify Java/Kotlin plugin configuration.
- Look for migration instructions if created on a pre-26.38 CoGo toolchain.

### Build fails offline
- Determine whether a dependency or Gradle distribution is uncached.
- Reconnect to fetch required artifacts, or provision them before going offline.
- Avoid repeatedly changing source code when the error is clearly a missing artifact.

### Build process is killed
- Free storage and RAM.
- Close heavy apps and reduce concurrent work.
- Try a smaller project or a lower-memory build configuration if appropriate.
- Capture whether the OS killed the process or Gradle reported an exception.

### APK builds but will not install
- Check ABI support.
- Check min SDK and device Android version.
- Check signing/version conflicts with an already installed package.
- Read Package Manager install errors.

### App installs but crashes
- Determine whether CoGo or the generated app crashed.
- Capture the full exception/native crash.
- Check permissions, initialization, resource lookup and lifecycle.
- Reproduce after a clean build if stale artifacts are suspected.

### Plugin does not install/load
- Verify `.cgp` packaging and manifest metadata.
- Verify `plugin.min_ide_version` and required API capability.
- Check required permissions and activation lifecycle.
- Compare the plugin's build API with the installed CoGo release.

### Local AI does not respond
- Verify the selected backend and model availability.
- Check ABI and native library availability.
- Check free RAM, storage and model size.
- Distinguish model loading from inference failure.
- Test cloud AI separately only if network/service configuration is available.

## 7.5 Good bug report template
Include:
- CoGo version/release and install source.
- Device model, Android version, CPU ABI.
- Project source or minimal reproducer (remove secrets).
- AGP, Gradle wrapper, Kotlin and Java settings.
- Exact steps to reproduce.
- Expected versus actual behavior.
- Full relevant error/stack trace/logcat excerpt.
- Whether network access changes the outcome.
- Whether the issue started after an update/migration.
- A minimal diff or test case if contributing a fix.

## 7.6 Contributor quality checklist
- Read `ARCHITECTURE.md` and local agent/contributor instructions.
- Search for an existing implementation before adding dependencies.
- Follow module dependency direction and centralized build logic.
- Use UDF/Compose for new UI unless the subsystem guidance says otherwise.
- Keep blocking IO off the main thread.
- Add tests at the correct subsystem level.
- Validate both relevant ABI variants where applicable.
- Check permissions, file paths, error handling and lifecycle cleanup.
- Avoid modifying vendored/generated assets without understanding their source of truth.
- Verify the actual release workflow, not only a local debug build.
