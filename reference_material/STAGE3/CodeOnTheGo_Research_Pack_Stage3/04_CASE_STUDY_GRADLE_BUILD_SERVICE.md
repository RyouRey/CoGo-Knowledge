# 4. Case Study — Gradle Build Service

## 4.1 Source-level anchors
The app-side service is:
`app/src/main/java/com/itsaky/androidide/services/builder/GradleBuildService.kt`

At the inspected release tag:
- class declaration is around line 104;
- `getBuildType(tasks)` is around line 186;
- `nextBuildId(runType)` is around line 197;
- `onCreate()` begins around line 258.

The service implements the app's `BuildService`, `IToolingApiClient`, and `ToolingServerRunner.Observer` contracts. It holds references to a tooling client/runner and a tooling server, and uses a coroutine scope named `GradleBuildService`.

Pinned source:
https://github.com/appdevforall/CodeOnTheGo/blob/26.40/app/src/main/java/com/itsaky/androidide/services/builder/GradleBuildService.kt

## 4.2 Observed behavior in the inspected section
- It tracks the Gradle daemon PID separately from a listener because the daemon can outlive an individual build and UI/activity recreation can miss the original notification.
- It exposes tooling-server PID from the runner when the server is started.
- It checks for the project's Gradle wrapper files (`gradlew`, `gradle-wrapper.jar`, `gradle-wrapper.properties`) before treating the wrapper as available.
- It creates build IDs with a session UUID and incrementing counter, along with the run type.
- It wraps build listener callbacks so UI-facing listener methods are dispatched on the UI thread.
- It is a foreground Android service with notification handling.

These are directly observed implementation facts from the inspected source, not a full trace of every build entry point.

## 4.3 Architecture context
The architecture doc states that CoGo executes a real Gradle build in a separate process via its tooling API and streams events back. Relevant adjacent areas include:
- `subprojects:tooling-api*`;
- `gradle-plugin*`;
- `subprojects:projects`;
- builder/project model modules;
- event models and app-side event consumers.

Pinned architecture:
https://github.com/appdevforall/CodeOnTheGo/blob/26.40/ARCHITECTURE.md

## 4.4 Debugging a build problem
Collect:
1. selected tasks and run type;
2. project root and wrapper presence;
3. Gradle distribution, Java/JDK and Android SDK availability;
4. tooling-server startup/exit state;
5. first exception and full cause chain;
6. build ID/session ID;
7. output/event sequence and whether terminal events arrive;
8. cancellation/timeout state;
9. device ABI, memory, storage and app version.

Then classify the failure:
- service start/binding;
- tooling server startup;
- wrapper/configuration;
- dependency resolution;
- compilation/resource packaging;
- progress/event delivery;
- cancellation/cleanup;
- result/UI rendering.

## 4.5 Proposed build-service tests (not claimed to exist)
- daemon starts once, outlives one build, and remains visible after listener recreation;
- server exits with no build in flight and frees the build slot;
- server exits during an active build and emits a terminal failure;
- two overlapping build requests are serialized or explicitly refused;
- cancellation produces exactly one terminal result;
- task failure includes the first causal error and does not appear as success;
- UI callbacks are always dispatched on the expected thread;
- missing wrapper files fail before task execution with a useful message;
- build IDs are unique across a service session;
- listener is null and no callback wrapper is created;
- process dies before a final result is delivered;
- malformed/late progress event does not crash the UI.

## 4.6 Key caution
A source trace is not the same as executing tests. This pack inspected source and tests but does not claim to have run Gradle, unit tests, instrumentation tests or a device build.
