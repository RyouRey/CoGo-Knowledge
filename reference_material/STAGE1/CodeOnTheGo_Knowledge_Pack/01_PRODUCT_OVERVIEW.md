# 1. Product Overview

## 1.1 What it is
Code On The Go (CoGo) is a mobile-first Android IDE intended to let people create, edit, build, and deploy real Android applications directly on Android phones and tablets. The official positioning emphasizes development without a conventional computer and with an offline-capable workflow. It is maintained by App Dev for All and succeeds AndroidIDE, which was archived in 2024.

CoGo is not merely a syntax-highlighting text editor. Its scope includes an on-device toolchain, Gradle-based Android project builds, language tooling, terminal, project management, UI-design helpers, debugging support, Git integration, and an extensible plugin system.

## 1.2 Product goals
- Lower the hardware and connectivity barrier to Android development.
- Bring a substantial Android development workflow onto a mobile device.
- Support Kotlin and Java projects.
- Allow capabilities to be extended by optional plugins/add-ons.
- Offer workflows such as converting a photographed hand-drawn layout into Android XML through Sketch to UI.
- Support on-device debugging rather than requiring a separate workstation in every case.

These are product goals, not a promise that every desktop Android Studio feature or every Android Gradle Plugin (AGP) combination is supported.

## 1.3 Main capabilities documented by the project
- Editing Android project files and source code.
- Building Android projects using a real Gradle build executed on-device through a tooling layer.
- Deploying/installing built apps on the device.
- Java and Kotlin development support, plus XML and other language tooling.
- Embedded terminal based on Termux components.
- Project/file navigation and editor facilities.
- UI design tooling: layout editor, XML inflation/rendering components, vector tools, and Compose preview support.
- Plugin/add-on support, including third-party capabilities such as Android NDK support.
- Git operations through JGit and project cloning from the app.
- AI-related functionality: Gemini through Google's GenAI SDK and a local llama.cpp integration. Availability and behavior depend on configuration, model assets, network access, device resources, and release.
- Sketch to UI plugin: photo of a hand-drawn UI layout → usable Android XML layout.
- On-device debugger stack described by the official site.

## 1.4 Who benefits
- Learners who only have an Android phone or tablet.
- Developers who need to make small changes while away from a desktop.
- People in low-connectivity environments, after required assets and dependencies are available.
- Plugin authors who want to add features to the IDE.
- Researchers exploring mobile-first build systems and local development environments.

## 1.5 What it is not
- Not an Android emulator running a desktop IDE.
- Not automatically equivalent to Android Studio in breadth, polish, or compatibility.
- Not guaranteed to build arbitrary projects: AGP, Gradle, Java/Kotlin versions, native libraries, memory, disk, and Android restrictions matter.
- Not fully offline for cloud-backed features or initial asset/dependency acquisition.
- Not a guarantee that projects created by older releases remain buildable without migration. The official product page warns that releases 26.38+ include a breaking core-toolchain upgrade for projects created with 26.37 or earlier.

## 1.6 Compatibility snapshot (as surfaced in official materials)
- CoGo's own minimum Android OS: Android 9 according to the official device-compatibility discussion.
- Supported CPU ABIs: `armeabi-v7a` (32-bit ARM) and `arm64-v8a` (64-bit ARM).
- Approximate storage: 3.5 GB minimum, including roughly 2 GB for assets and about 1 GB additional build headroom.
- Approximate free RAM: 1.5 GB minimum; 4 GB free RAM recommended.
- Bundled JDK: 21.
- Bundled Kotlin: 1.9.2.
- The official page states that AGP 8.11.0 is shipped by default and can use up to Java 17 language syntax in the documented setup.
- Device, release, and project configuration can change actual compatibility. Verify the current official page before relying on these values.

## 1.7 Project and organization
- Main repository: `appdevforall/CodeOnTheGo`.
- Organization: `appdevforall`.
- Add-ons repository: `appdevforall/addons`.
- The codebase namespace remains `com.itsaky.androidide`, reflecting its AndroidIDE lineage.
- Repository is GPL-3.0-or-later according to its README/license summary. This applies to the repository's covered code; third-party assets and dependencies can have their own licenses.
- The organization describes its mission as building free, open-source app development tools that work without a traditional computer or Internet access.

## 1.8 Product-level strengths and trade-offs
**Strengths**
- Portability: editing and building can happen on the same Android device.
- Offline-first core workflow once assets/dependencies are provisioned.
- Open-source implementation that can be inspected and extended.
- Optional plugins reduce the need to ship every possible feature in the base app.
- Native toolchain and Gradle integration make it more capable than a simple editor.

**Trade-offs**
- Mobile RAM, thermal limits, storage, screen size, and background-process policies constrain builds.
- The app has a large multi-module codebase and vendored/forked components, so contributors face a learning curve.
- Toolchain upgrades can break older projects and require migration.
- Some features depend on cloud services, downloads, external repositories, or device-specific capabilities.
- Compatibility must be checked against exact CoGo release and project build configuration.

## 1.9 Practical interpretation
The best mental model is: **a mobile IDE plus an embedded Android build environment, with a plugin layer and optional cloud/local AI features**. When diagnosing a problem, first identify whether it belongs to the IDE, project Gradle configuration, bundled toolchain/assets, plugin, device resource limits, or external service.
