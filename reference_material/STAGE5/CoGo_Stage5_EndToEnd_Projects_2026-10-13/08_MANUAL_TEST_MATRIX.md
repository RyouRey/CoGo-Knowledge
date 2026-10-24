# Manual end-to-end test matrix

Status at creation: test plan authored; no CoGo device execution performed by this research run.

## Common project creation/build tests
| ID | Test | Expected result | Evidence to capture |
|---|---|---|---|
| C01 | Create project from correct template | project opens and sync completes | CoGo version, template, screenshot/tree |
| C02 | Inspect generated package | package is valid and consistent with source paths | package declaration and app config |
| C03 | Build unchanged project | normal debug build succeeds | full Build Output |
| C04 | Install and launch unchanged project | launchable Activity opens | install output and app screen |
| C05 | Make one harmless source change | build/run reflects change | diff, build output, visible result |
| C06 | Introduce a deliberate syntax error | compiler identifies source/line; app not silently treated as updated | error lines and recovery build |
| C07 | Fix error and rebuild | normal build succeeds again | new build output |
| C08 | Relaunch app after force-stop | app launches without stale state/crash | steps and Logcat if failure |

## P1 — Kotlin/XML Unit Converter
| ID | Test | Expected result |
|---|---|---|
| P1-01 | Launch without input | result prompts user to enter a number |
| P1-02 | Enter `100`, tap Convert | displays `100.00 cm = 39.37 in` |
| P1-03 | Enter `2.54`, tap Convert | displays approximately `2.54 cm = 1.00 in` |
| P1-04 | Empty input | no crash; validation message |
| P1-05 | Alphabetic input or malformed decimal | no crash; validation message |
| P1-06 | Rotate/recreate activity | app remains usable; no persistence is promised |

## P2 — Java/XML Quick Notes
| ID | Test | Expected result |
|---|---|---|
| P2-01 | Launch with no notes | empty-state text visible |
| P2-02 | Add `Buy rice` | note appears in list |
| P2-03 | Add a second note | both notes remain visible in current process |
| P2-04 | Submit whitespace-only note | validation shown; blank note not added |
| P2-05 | Submit after adding note | input clears |
| P2-06 | Force-stop/relaunch | notes reset; this is expected for this in-memory demo |

## P3 — Compose Counter
| ID | Test | Expected result |
|---|---|---|
| P3-01 | Launch | title and counter value 0 visible |
| P3-02 | Tap `+1` once | value becomes 1 |
| P3-03 | Tap `+1` repeatedly | value increments on each tap |
| P3-04 | Tap Reset | value returns to 0 |
| P3-05 | Recreate process | persistence is not promised; counter may reset |

## Quick Build (optional, experimental)
| ID | Test | Expected result |
|---|---|---|
| QB01 | Confirm app meets official requirements | launchable app, one process, debug variant |
| QB02 | Enable experimental flag and restart CoGo | feature becomes available |
| QB03 | First provisioning | proxy app build/install/launch completes or reports explicit failure |
| QB04 | Compatible source edit/save | app updates or CoGo visibly falls back to normal build |
| QB05 | Deliberate compile error | no new broken code is silently deployed; useful error shown |
| QB06 | Unsupported edit/dependency path | fallback/error is explicit; normal Gradle remains available |
| QB07 | Compare final artifact | use normal Gradle build for the deliverable APK |

## Acceptance
A blueprint is `device_verified` only when all required tests pass on a named device and CoGo version, or failures are documented with reproducible evidence and the claim is narrowed accordingly.
