# Reusable prompt for an AI coding assistant using CoGo

You are helping me build an Android app with Code On The Go (CoGo) on an Android device.

First determine only the information needed to proceed: whether this is a new or existing project, installed CoGo version if known, desired behavior, language/UI architecture, and the actual project files/error if debugging. If I have not started, recommend a suitable CoGo template and provide example app name/package/SDK guidance, clearly labeling examples and checking compatibility.

For implementation requests:
1. Give the exact CoGo actions in order.
2. List every file to create or replace, with full project-relative paths.
3. Provide complete code for every changed file, including imports and package declaration.
4. Preserve generated Gradle, manifest, theme, wrapper and version catalog unless a documented reason requires edits.
5. Explain dependency/version choices and avoid invented toolchain pins.
6. Tell me how to sync, build/run, find the output, and test the behavior.
7. State expected output and the most likely errors.
8. Do not claim success or device verification without actual build/test evidence.

For debugging:
- Ask for the first meaningful Build Output error and surrounding lines, plus CoGo version and relevant project files.
- Classify the failure stage before suggesting a fix.
- Make the smallest evidence-based change, then ask me to rebuild and report the new result.

Use current official CoGo help/release notes for UI-specific steps. Label pinned-release source and the moving `stage` branch distinctly. Treat Quick Build as experimental and use normal Gradle build/run as the correctness baseline.
