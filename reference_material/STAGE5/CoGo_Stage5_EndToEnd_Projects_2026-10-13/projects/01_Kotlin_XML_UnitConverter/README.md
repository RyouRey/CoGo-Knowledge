# P1 — Kotlin/XML Unit Converter

## Goal
Convert centimetres to inches using a minimal XML View UI and Kotlin Activity.

## Create in CoGo
- Project name: `UnitConverter`
- Example package: `com.example.unitconverter`
- Choose a Kotlin template that uses XML Views (not Compose).
- Keep the generated Gradle files, manifest, theme and wrapper.

## Replace/add these files
1. Replace the generated Activity file with `MainActivity.kt`, adapting its package declaration to the package actually generated in your project.
2. Replace `app/src/main/res/layout/activity_main.xml` with the layout below.
3. Optional: if your template uses `strings.xml` for all labels, move hardcoded labels into resources later; this minimal blueprint intentionally keeps the number of touched files small.

## Build and test
- Wait for Gradle sync.
- Run normal debug build/run.
- Test 100 cm -> 39.37 inches; 2.54 cm -> 1.00 inch; empty and invalid input must not crash.

## Evidence status
Reference implementation; not built or installed by this research run.
