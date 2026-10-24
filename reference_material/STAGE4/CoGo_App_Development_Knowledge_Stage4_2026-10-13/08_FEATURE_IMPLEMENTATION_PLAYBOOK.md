# Feature Implementation Playbook for Android Apps Built in CoGo

This is a decision framework for implementing app features; it is not a substitute for inspecting the user's template or current Android platform documentation.

## Architecture by project size

- **Tiny single-screen app:** one Activity/Composable may be enough; avoid needless layers.
- **Multiple screens or nontrivial state:** separate UI, state/business logic, and data access; use ViewModel/repository patterns where appropriate.
- **Persistent structured data:** choose Room/SQLite or another fit-for-purpose store; don't use preferences as a relational database.
- **Small key-value settings:** DataStore or SharedPreferences depending on project stack and needs.
- **Remote data:** repository/API layer, asynchronous calls, loading/error/empty states, timeouts, and lifecycle-aware cancellation.

Avoid adding an architecture framework just because it is popular. Every dependency creates compatibility, download, size, and maintenance costs on a phone-first/offline workflow.

## Feature checklist

### UI and navigation
- Define screens and navigation states before code.
- Keep UI responsive; do not block the main thread with file, database, or network operations.
- Provide loading/empty/error/success states.
- Handle Back and process recreation intentionally.

### Local data
- Decide whether data must survive app restarts, device restarts, or uninstall/reinstall.
- Choose a storage type that matches the data and access pattern.
- Add migration strategy if schema changes are expected.
- Test empty database, malformed old data, and repeated saves.

### Network/API
- Declare `android.permission.INTERNET` in the manifest when the app performs network requests.
- If the app needs to check connection state, assess whether `ACCESS_NETWORK_STATE` is needed; don't add it by habit.
- Use HTTPS; avoid enabling cleartext traffic as a generic fix.
- Parse server errors and timeouts; never assume a request succeeded because no exception was shown.
- Do not embed privileged secrets in an APK. Anything shipped in client code can be extracted.
- For offline-first apps, define cache behavior and how users see stale/offline data.

### Files, photos, and media
- Use modern Android system pickers/Storage Access Framework when users select files where suitable.
- Storage behavior depends on Android version and the API being used. Avoid asking for broad storage permissions without a clear need.
- Test cancel, denied access, missing file, and large-file cases.

### Permissions
- Add a permission only when the feature actually needs it.
- Declare it in the manifest and request runtime permission when Android requires it.
- Explain the purpose in user-facing UI; handle denial gracefully.
- Test granted, denied, and “don't ask again”/settings recovery where applicable.

### Background work
- Use appropriate Android scheduling APIs for deferrable work rather than indefinite background services.
- Android versions and vendor battery policies affect background behavior. Test on target devices.
- For long-running foreground work, follow current notification/foreground-service requirements.

### Notifications
- Check Android notification permission requirements on target versions.
- Create notification channels on Android versions that require them.
- Handle tap actions and pending intents safely.

### Security
- Validate untrusted input; avoid path traversal and unsafe deserialization.
- Keep authentication/session data out of logs.
- Use HTTPS and platform cryptographic APIs; don't invent crypto.
- Use Android Keystore for app-held cryptographic keys when appropriate.
- Keep signing keystores and credentials backed up securely and never commit them.

## Dependency addition protocol

1. Determine whether the feature can be built using Android SDK APIs already available.
2. If a library is justified, verify its official coordinate, current version, minSdk, Kotlin/AGP compatibility, license, transitive dependencies, and whether it can be downloaded/cached in CoGo.
3. Inspect whether the project uses a version catalog.
4. Add one dependency at a time, sync, and build.
5. If offline, confirm artifact availability instead of promising automatic resolution.

## Testing ladder

1. Compile/build.
2. Manual happy path.
3. Empty/error/permission-denied cases.
4. Persistence across restart if relevant.
5. Network-offline and slow response if relevant.
6. Small/large screen and target Android versions.
7. Debug vs release behavior.
