# Blueprint file map

## P1 Kotlin/XML
| File | Action | Purpose |
|---|---|---|
| `app/src/main/java/<actual-package>/MainActivity.kt` | replace | validates input and computes inches |
| `app/src/main/res/layout/activity_main.xml` | replace | input, button, result |
| Gradle files | keep generated | preserve template-specific toolchain/dependencies |
| Manifest/theme | keep generated | Activity launch setup comes from template |

## P2 Java/XML
| File | Action | Purpose |
|---|---|---|
| `app/src/main/java/<actual-package>/MainActivity.java` | replace | input validation and note append |
| `app/src/main/res/layout/activity_main.xml` | replace | input, add button, status, scrollable notes |
| Gradle files | keep generated | no new dependency required |
| Manifest/theme | keep generated | preserve template defaults |

## P3 Compose
| File | Action | Purpose |
|---|---|---|
| `app/src/main/java/<actual-package>/MainActivity.kt` | replace | Compose Activity and counter state |
| Compose template Gradle files | keep generated | provides Compose compiler and UI dependencies |
| XML layout | do not add | UI is composed in Kotlin |
| Manifest/theme | keep generated | preserve template defaults |

## Package name warning
The source examples use `com.example...` package declarations. If the actual generated package differs, replace the declaration with the exact package and place the file in the corresponding package folder. A path can be moved by the IDE or file tree; the declaration and namespace must remain consistent.
