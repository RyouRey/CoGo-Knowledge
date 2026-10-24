# Knowledge-base QA checklist

Before adding a new record:
- [ ] Does the claim answer a user-app development question rather than CoGo source modification?
- [ ] Is the CoGo version scope explicit?
- [ ] Is the source an official release/help doc, pinned source, development branch, or a hypothesis?
- [ ] Are UI actions exact enough for a phone user to follow?
- [ ] Are paths rooted from the project tree and conditional on the chosen template?
- [ ] Is full code provided where required?
- [ ] Are generated Gradle versions preserved unless evidence requires a change?
- [ ] Does the record include expected output and a way to test it?
- [ ] Are likely errors and smallest safe fixes included?
- [ ] Does the record avoid claiming a build was verified without logs?
- [ ] Are source URLs and review date included?
- [ ] Are duplicate or contradictory instructions reconciled?

## Evidence upgrade checklist
A record can become `device_verified` only when:
- [ ] The exact app version and device are recorded.
- [ ] The source tree or changed files are archived.
- [ ] A normal debug build succeeds and its output is captured.
- [ ] The app installs and launches.
- [ ] Feature-specific tests pass.
- [ ] Failures are recorded rather than omitted.
- [ ] A second person can repeat the steps from the captured instructions.
