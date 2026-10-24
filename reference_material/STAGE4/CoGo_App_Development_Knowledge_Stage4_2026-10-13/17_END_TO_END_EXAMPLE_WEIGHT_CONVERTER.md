# End-to-End CoGo Example: Weight Converter (Official Tutorial Blueprint)

**Source:** https://appdevforall.org/codeonthego/help/tutorials.html  
**Purpose:** Use a small, known-scope app to teach the AI how to translate a request into project choices, exact file edits, build/run steps, and acceptance tests. This is a workflow blueprint based on official CoGo help, not a claim that this package itself ran the tutorial.

## User-visible requirement

Build a one-screen Android app that converts kilograms to pounds or pounds to kilograms. The user enters a decimal quantity, selects the input unit, and sees the converted quantity/unit update whenever the input or unit selection changes.

## Official tutorial project setup

The CoGo tutorial uses:

- Template: **Empty Activity**
- App name: `WeightConverter`
- Language: **Java**
- Minimum SDK: tutorial uses API 21 (Android 5.0 / Lollipop) as its default example
- Two primary files to edit: `MainActivity.java` and `activity_main.xml`

The API 21 value belongs to this tutorial's historical example; do not treat it as the recommended minimum for every new app. In a new project, select minSdk based on target devices and current CoGo/template support.

## File placement

The tutorial's documented paths are:

- Java activity: `app/src/main/java/com/example/weightconverter/MainActivity.java`
- Layout: `app/src/main/res/layout/activity_main.xml`

The path depends on the package name chosen. If the user changes the package/app setup, inspect the generated package path and update code package declarations accordingly.

## UI plan

The official tutorial describes three Views in the XML layout:

1. `EditText` with ID `inputQuantity`, configured for decimal numeric input.
2. `Spinner` with ID `inputUnits`, populated with `kg` and `lbs` choices.
3. `TextView` with ID `convertedMeasurement`, showing the converted value and output unit.

The tutorial uses a ConstraintLayout and percentage widths as one possible layout. An AI should inspect the generated project's available dependencies and layout structure before assuming ConstraintLayout is configured.

## Behavior plan

- Populate the unit dropdown with `kg` and `lbs`.
- Attach a text-change listener to the quantity field.
- Attach a selection listener to the dropdown.
- Both listeners call one shared `updateConversionResult()` method.
- Parse decimal input safely; handle blank/invalid input without crashing.
- Convert using a documented factor such as `1 kg = 2.20462 lbs` (and reciprocal conversion), and format the result consistently.
- Set an initial valid result when the Activity opens.

For an AI-generated implementation, favor robust blank-input handling over copying any incomplete code excerpt from a page extraction. Verify all imports and listeners are present in the final complete file.

## Build/run sequence in CoGo

1. Create the project and wait for `Project initialized`.
2. Open the Project menu/file tree.
3. Navigate to `app/src/main/java/.../MainActivity.java` and replace/edit the generated Activity as directed.
4. Navigate to `app/src/main/res/layout/activity_main.xml` and replace/edit the generated layout as directed.
5. Save both files.
6. Tap Build/Quick Run and inspect Build Output.
7. Install and launch the app when prompted.
8. If the layout builds, test interaction logic; a layout-only build is not proof the conversion works.

## Acceptance tests

- [ ] App launches and shows the quantity field, unit dropdown, and result.
- [ ] Initial state has a valid default quantity/unit/result.
- [ ] Entering `1` with kg selected shows approximately `2.20462 lbs` (rounding may vary).
- [ ] Selecting lbs for `1` shows approximately `0.45359 kg`.
- [ ] Editing the quantity updates the result without a separate button.
- [ ] Switching the unit updates the output unit and conversion.
- [ ] Empty input does not crash.
- [ ] Invalid/partial decimal input does not crash while the user is typing.
- [ ] Rotation/relaunch behavior is acceptable for the stated requirements.
- [ ] Build Output has no unresolved compile/resource errors.

## Why this example matters for the knowledge base

This tutorial is useful as a procedural pattern: a clear app specification → project configuration → exact file paths → UI resources → event logic → build/run → acceptance checks. Future sample apps should follow the same shape, and should add toolchain/version metadata plus build evidence when actually tested.
