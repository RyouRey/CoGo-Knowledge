# 6. AI, Git, Offline Operation and Security

## 6.1 AI integration: two different execution models
The architecture document identifies two AI paths:
1. **Gemini** through Google's GenAI SDK — a remote/cloud-backed integration that normally requires network access and valid service configuration.
2. **llama.cpp** through `llama-api` and `llama-impl` — an on-device/native integration that can support local inference when compatible model assets are present and the device has sufficient resources.

Do not collapse these into a single “AI works offline” claim. Cloud AI and local AI have different privacy, latency, connectivity, hardware and model-availability properties.

## 6.2 AI agent architecture
The repository has an agent-related subsystem, and the plugin API changelog describes plugin-contributed agent tools. The host provides a registry contract so plugins can register/unregister tool sources during activation/deactivation. This design avoids relying on a duplicated type from another plugin classloader.

For AI agent feature development, investigate:
- agent UI/state;
- repository/client abstraction;
- prompt/context construction;
- tool registry and invocation contract;
- permissions and tool validation;
- error/cancellation behavior;
- model/backend selection;
- tests for missing models, network failures, malformed output and tool failures.

Do not infer that a feature is implemented solely from the presence of a module or API symbol. Trace the actual runtime call path.

## 6.3 Embeddings and retrieval
The API changelog describes an embedding capability interface introduced in 26.40. It addresses batch embedding, embedding dimensions and model identity. These are important retrieval-system design details:
- Batch requests reduce per-item overhead when indexing many chunks.
- Dimensions help validate vector shape.
- Model identity matters because vectors produced by different models may not be comparable even if dimensions match.
- Existing vectors may need invalidation/reindexing if the embedding model changes.

For AI knowledge systems, retain source provenance, model identifier, chunking strategy and indexing version alongside embeddings.

## 6.4 Git
The architecture identifies JGit as the Git client and the support page mentions cloning a Git repository from the main menu as a feature added in response to user requests. Git remote operations require network access; local repository operations may work offline after cloning.

A practical Git workflow:
- Clone when connected.
- Commit locally after each coherent change.
- Keep a clean baseline before toolchain migration.
- Use branches for experiments.
- Record CoGo version and build configuration with issue reports.
- Do not put access tokens or credentials in commits.

## 6.5 Offline operation boundaries
Offline-capable operations can include editing, browsing local files, and building projects whose toolchain/assets/dependencies are already present. Potentially online operations include:
- first-run downloads and asset installation;
- fetching uncached Maven/Gradle dependencies;
- Gemini/cloud AI;
- Git clone/push/pull against remotes;
- release updates and plugin catalog downloads;
- fetching external documentation or other remote resources.

The exact offline boundary depends on what has already been provisioned and on project configuration.

## 6.6 Security boundaries to examine
An IDE executes build tools and compiles user code, so security review should pay attention to:
- plugin installation and code loading;
- shell/process execution;
- build scripts and Gradle plugins;
- external project imports;
- deep links and file path handling;
- permissions and privileged debugging/bootstrap paths;
- local web server interfaces;
- AI tool calls and prompt-injected project content;
- secrets in logs or AI context;
- model files and native libraries.

The architecture's deep-link implementation uses a traversal/symlink guard for a user-controlled path, illustrating the importance of validating paths at trust boundaries.

## 6.7 AI-specific safety and privacy recommendations
For a local AI workflow:
- Explain which data stays on-device and which is sent to a remote provider.
- Make cloud/local backend selection visible.
- Avoid including secrets, signing keys, keystores, tokens or private source files in prompts by default.
- Treat project files, comments and documentation as untrusted content; they may contain instructions intended to manipulate the agent.
- Restrict tool permissions and validate paths/arguments.
- Ask for confirmation before destructive edits, deletion, external publication or signing/releasing artifacts.
- Keep an audit trail of tool calls and file modifications.
- Never assume generated code is secure or correct without tests and review.

## 6.8 AI training/knowledge ingestion
If using this pack to build an AI retrieval corpus:
- Keep source URLs and retrieval dates.
- Separate confirmed facts from hypotheses and recommendations.
- Chunk by meaningful sections, not arbitrary token lengths alone.
- Preserve headings, code identifiers and version numbers.
- Store `source_url`, `retrieved_at`, `branch_or_release`, `confidence`, and `last_verified` metadata.
- Re-crawl living docs and release notes before answering version-sensitive questions.
- Respect the license for source code and third-party documentation; do not treat public availability as permission to remove attribution or license terms.
