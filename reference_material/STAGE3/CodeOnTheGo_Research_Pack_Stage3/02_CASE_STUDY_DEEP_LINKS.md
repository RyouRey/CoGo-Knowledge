# 2. Case Study — Deep Links and Path Safety

## 2.1 Trace map
```text
External HTTPS App Link
  → Android manifest intent-filter
  → DeepLinkActivity.onCreate
      → setup/readiness gate
      → DeepLinkRequest.parse(Uri)
  → project/editor routing
  → pending file request carried through activity intents
  → project/file resolution after project is available
  → contained-path validation
  → editor navigation
```

This is a system-level map, not a claim that every arrow is implemented in one class. The architecture document names the relevant activity/model/editor paths; follow the exact hand-off at the pinned tag when debugging a specific case.

## 2.2 Entry gate
`DeepLinkActivity.kt`:
- `onCreate` begins at approximately line 49.
- It checks `isIdeSetupComplete()` at approximately line 62 before parsing the URI.
- It parses with `DeepLinkRequest.parse(intent?.data)` at approximately line 82.

Why it matters:
- A link must not bypass onboarding, required toolchain setup, storage checks or device-compatibility gates.
- The code comments explain that links received before setup are dropped rather than held through potentially long onboarding.
- The activity is an exported App Links entry point, so malformed explicit intents are part of the threat model even when verified HTTPS App Links are configured.

Source: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/app/src/main/java/com/itsaky/androidide/activities/DeepLinkActivity.kt

## 2.3 Parser contract
`DeepLinkRequest.kt`:
- `MAX_LINK_PATH_LENGTH = 512` at approximately line 84. The KDoc explains the value is constrained by Binder/Parcelable transaction budget, not just filesystem path length.
- `parse` starts at approximately line 155.
- `buildUrl` starts at approximately line 305.
- The parser keeps line and column as raw strings in `PendingFileRequest`, preserving the difference between a missing segment and a present-but-invalid number.
- The accepted form is `https://appdevforall.org/device/open/project/{projectName}[/file/{filename}[/line/{n}[/column/{n}]]]`, with `www` accepted as well.
- Trailing line/column metadata is peeled from the end so a project or file path segment named `line` or `column` is less likely to be misinterpreted.
- The URL writer parses its own generated output back and checks that the parsed request matches the intended values; ambiguous links can be rejected instead of silently changing meaning.

Source: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/app/src/main/java/com/itsaky/androidide/models/DeepLinkRequest.kt

## 2.4 Regression tests already present
`DeepLinkRequestTest.kt` includes tests for:
- project-only URL;
- project plus file;
- project, file and line;
- project, file, line and column;
- multi-segment paths;
- project name equal to `line`;
- project name equal to `file`;
- a real path segment named `line` before a trailing line pair;
- ambiguous `file/line/Main.kt` shape, where no actual file remains after peeling the suffix.

Selected anchors:
- project-only: around line 31;
- reserved keyword: around line 86;
- ambiguous file case: around line 156.

Source: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/app/src/test/java/com/itsaky/androidide/models/DeepLinkRequestTest.kt

## 2.5 Contained path tests
`PathTraversalTest.kt` directly tests:
- relative in-project path acceptance;
- `..` traversal rejection;
- empty path rejection;
- paths that normalize to the project root;
- encoded slash/traversal after URI decoding;
- leading slash and backslash rejection;
- embedded NUL handling;
- ordinary filenames containing `..` (e.g. `notes..txt`) remaining valid;
- normalized redundant separators;
- symlink inside the project pointing outside the project being rejected.

Selected anchors:
- literal `..`: around line 48;
- NUL character: around line 89;
- symlink escape: around line 151.

Source: https://github.com/appdevforall/CodeOnTheGo/blob/26.40/common/src/test/java/com/itsaky/androidide/utils/PathTraversalTest.kt

## 2.6 Security invariants
1. Validate the parsed scheme, host and path shape.
2. Do not treat intent-filter matching as sufficient validation for explicit intents.
3. Bound path/request length before carrying data through Android intents/Parcel.
4. Preserve absent vs malformed line/column metadata.
5. Resolve paths against the intended project root; do not use a raw string join as the only check.
6. Reject parent traversal and symlink escape.
7. Reject a file request that resolves to no meaningful file target.
8. Ensure generated links round-trip to the same request.
9. Confirm project identity before navigating into a running editor.
10. Test activity/task/lifecycle race scenarios separately from parser correctness.

## 2.7 Proposed additional tests (not claimed to exist)
- Unicode normalization differences between a requested project name and filesystem directory.
- A symbolic link whose target is replaced between validation and open (TOCTOU exploration).
- Very long URL at exactly 511, 512 and 513 characters.
- Explicit intent with a valid-looking URI but a wrong calling context.
- Invalid line values: zero, negative, overflow, non-numeric, dangling `/line`.
- Invalid column with a valid line.
- Multiple overlapping deep-link requests while a close-confirmation dialog is open.
- A cold project open where Gradle sync fails after a file request is queued.
- `buildUrl`/`parse` property-based round-trip tests over reserved path segments.
