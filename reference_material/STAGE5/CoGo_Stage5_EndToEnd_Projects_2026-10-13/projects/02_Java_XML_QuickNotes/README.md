# P2 — Java/XML Quick Notes (in-memory demo)

## Goal
Practice Java, XML Views, click listeners, input validation and rendering multiple notes.

## Create in CoGo
- Project name: `QuickNotes`
- Example package: `com.example.quicknotes`
- Choose a Java template that uses XML Views.
- Keep generated Gradle files, manifest, theme and wrapper.

## Replace/add these files
1. Replace the generated Activity with `MainActivity.java`, adapting package declaration.
2. Replace `app/src/main/res/layout/activity_main.xml` with the provided layout.
3. The note list is memory-only; data is expected to reset after process death. This is deliberate so the first project has no extra database dependencies.

## Build and test
- Normal debug build/run.
- Add two notes, try empty input, verify the list scrolls.
- Force-stop and relaunch: notes reset, which is expected for this demo.

## Evidence status
Reference implementation; not built or installed by this research run.
