# 7. Testing, CI, Security and Reliability

## 7.1 Testing architecture
The repository includes shared testing modules:
- `testing:android`
- `testing:common`
- `testing:lsp`
- `testing:tooling`
- `testing:unit`

Use the closest test layer to the behavior being changed. The names indicate organization, but exact fixtures and commands must be read from each module's Gradle file and test sources.

## 7.2 Suggested test matrix
| Change | Minimum test focus |
|---|---|
| ViewModel/state | state transitions, effects, errors, cancellation |
| Repository/data source | success, empty data, persistence, IO failure |
| Gradle tooling | request formation, task execution, event delivery, process failure |
| LSP/editor | protocol, indexing, document sync, edit ranges, regression tests |
| Plugin API | binary compatibility, metadata validation, lifecycle, service availability |
| Plugin runtime | install/activate/deactivate/uninstall and permission failure |
| AI backend | missing credentials/model, offline, malformed response, cancellation |
| AI tools | invalid arguments, permission denial, traversal attempts, timeout |
| Native/ABI code | v7 and v8 variants where applicable, load failure and packaging |
| Deep links | malformed URI, wrong project, traversal/symlink, lifecycle races |
| Packaging | APK install, native library extraction, release artifact smoke test |

## 7.3 Repository workflow
Repository instructions describe `stage` as the integration branch and `main` as release-oriented. Feature work normally branches from `stage` and opens a PR to `stage`. Official/public release and publishing workflows are automated through GitHub Actions. Verify current contributor docs before using commands or making a release.

## 7.4 Coverage pitfalls
The repository's app Gradle file documents JaCoCo path issues:
- Android test execution data may live under `outputs/unit_test_code_coverage/<variant>UnitTest/`, not the default `build/jacoco/`.
- `:app` may run ASM transforms, meaning measured bytecode is not necessarily the raw Kotlin classes directory.
- A wrong path can silently skip coverage or create false “uncovered” classes.

General lesson: inspect generated report inputs and verify that class files match the execution data; do not trust a percentage without validating the report configuration.

## 7.5 Security threat model
An IDE is a high-capability app because it handles project files, executes build tools, loads plugins, invokes terminal commands, installs APKs and may send context to AI services. Relevant trust boundaries include:
- project import and archive extraction;
- deep links and file paths;
- plugin artifact installation/classloading;
- Gradle scripts and third-party build plugins;
- local web server or IPC endpoints;
- privileged debugging/bootstrap code;
- native libraries and downloaded models;
- AI tool invocation and prompt context;
- logs/crash reports and secret redaction;
- signing keys, credentials and Git tokens.

## 7.6 Concrete security lessons
- Deep-link file paths must be constrained to the intended project directory, including symlink resolution.
- Plugin-shared interfaces must use host-defined API types to avoid classloader type confusion.
- AI-generated tool arguments are untrusted; validate schema, permissions and paths.
- Do not include secrets in prompts, crash reports or logs.
- Avoid arbitrary shell execution from model output.
- Treat downloaded dependencies and build scripts as executable supply-chain inputs.
- Record artifact provenance and verify signatures/hashes where available.
- Keep least privilege and explicit user confirmation for destructive/external operations.

## 7.7 Reliability and resource constraints
Mobile builds are affected by RAM, storage, thermal throttling, background execution policies, ABI-specific native libraries and large model/toolchain assets. Reproducible bug reports must include device/runtime context, not just source code.

## 7.8 Security review workflow
1. Identify entry points and trust boundaries.
2. Trace input from source to sensitive sink.
3. Check validation, canonicalization, permissions and error paths.
4. Inspect tests for adversarial inputs.
5. Review logs for secret leakage.
6. Check dependency versions and provenance.
7. Verify the fix on target Android/ABI variants.
8. Follow the official security policy for responsible disclosure; do not publish exploit details before coordination.
