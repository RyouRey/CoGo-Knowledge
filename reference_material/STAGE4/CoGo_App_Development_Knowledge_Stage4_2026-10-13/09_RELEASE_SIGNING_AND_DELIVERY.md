# Release Build, Signing, Backup, and Delivery

## Debug vs release

- **Debug build:** fast development/testing; typically signed with a debug key. Do not use it as a substitute for a production release workflow.
- **Release build:** distribution-oriented variant; must use the intended signing identity and be tested separately.
- **APK:** installable package. **AAB:** publishing format used by Google Play; creation and delivery steps differ. Verify which artifact the user actually needs.

## CoGo-specific facts

CoGo Help documents a keystore workflow and says a default keystore may be created during installation and project files may include `release.keystore` and `release.properties`. The same help page recommends creating a unique keystore for an app intended for distribution rather than relying on the default installer-provided key. Exact template behavior may differ by version.

The help page also describes a Keystore Generator plugin and a release build flow: select the Release build variant, apply, then build. Use the installed app's current UI and current documentation.

## Signing safety checklist

- Create/choose the app's long-term signing key before public distribution.
- Record alias and passwords in a secure password manager.
- Back up the keystore in at least one secure location separate from the phone.
- Never send the keystore/passwords in chat or commit them to a public Git repository.
- Do not overwrite or lose the key used to sign a published app; update installs generally require a compatible signing identity.
- Avoid placing real secrets directly into source-controlled `build.gradle` files. Prefer a local, ignored properties file or secure mechanism consistent with the project.
- Before release, check app ID/package, version code/name, permissions, min/target SDK, release optimization, and license/privacy obligations.

## Release acceptance

1. Select Release variant using CoGo's build-variant UI.
2. Build release; inspect logs.
3. Locate the actual artifact path shown by CoGo.
4. Install on a test device or clean test profile where feasible.
5. Verify launch, core flows, data, network, and permissions.
6. Check that release-only optimization did not break reflection/serialization/resources.
7. Confirm signing key identity and store credentials safely.
8. Archive the exact APK/AAB, source revision, toolchain versions, and build notes.

## Distribution constraints

A signed APK can be shared for sideloading, but Android may show installation warnings and the recipient must permit installs from the relevant source. Publishing to a store involves separate developer account, target API, privacy, policy, and artifact requirements that should be checked against the current store rules. Don't promise store acceptance solely because a release APK builds.
