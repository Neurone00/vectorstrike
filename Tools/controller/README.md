# STRIKE VECTOR phone controller

Static page + WebSocket relay. No build step.

```bash
cd Tools/controller && npm install && node server.js
```

The terminal prints the LAN URL and a QR code. Open it on the phone (Chrome), tap **Start**
(grants orientation on iOS, enters fullscreen), tap **Calibrate** while holding the phone in the
neutral position.

## Protocol

- Connect to `ws://<lan-ip>:8080` (plain) or `wss://<lan-ip>:8443` (with certs, see below); the game
  process on the Mac can use plain `ws://127.0.0.1:8081`. First message `{"role":"game"}` (or `{"role":"phone"}`).
- Phone -> all game clients, ~30 Hz, verbatim:
  `{t, steer:-1..1, throttle:0..1, abL, abR, boost, pulse, mode:"auto"|"manual", line:0|1|2}`
- Game -> all phones: anything you send (unused for now).
- Test listener: `node test_client.js` (PORT env to override) prints every message.

Steering: tilt (gamma in portrait, beta in landscape) minus the calibrated zero, 3° deadzone, full
lock at 30° (`DEADZONE`, `FULL_LOCK` at the top of `race.html`). Throttle keeps its value on release.
Airbrakes, Boost and Pulse are true while held.

## Android app (`android/`) — the way we ship it

Browsers gate motion sensors behind a secure context plus a permission that Chrome auto-denies on
self-signed origins and Brave's shields block outright, so the controller is a tiny native shell:
a fullscreen `WebView` showing the same `race.html` (copied into assets at build time) with tilt
coming from Android's `SensorManager` through `window.nativeTilt(gamma, beta)`. No browser, no
certificate, no permission prompt. Everything else (throttle, zones, WebSocket) is the web page.

Build (needs a JDK, Android command-line tools and the SDK packages below; one-time):

```bash
brew install gradle && brew install --cask android-commandlinetools
```

```bash
yes | sdkmanager --licenses >/dev/null && sdkmanager "platform-tools" "platforms;android-35" "build-tools;35.0.0"
```

```bash
cd Tools/controller/android && gradle assembleDebug
```

Auto-update (verified 2026-10-20, v0.3 → v0.4 on Android 10): on every launch the app reads the latest GitHub release of this repo; if its tag
`controller-vX.Y` is newer than the installed version it downloads the APK (system download
notification) and opens the installer, which asks for one confirmation. The first time, Android
asks to allow installs from "SV Controller". Publish a new version with `./android/release.sh X.Y
"notes"` (bumps versionCode, builds, creates the release); never reuse a version.

Install: download the APK from the GitHub release
https://github.com/Neurone00/vectorstrike/releases/latest on the phone and open it
(allow "install unknown apps" for the browser once). Alternatives: with the server running,
`http://<mac-ip>:8080/app.apk` serves the freshly built APK; or `adb install -r
app/build/outputs/apk/debug/app-debug.apk` over USB. New build → `gh release create controller-vX.Y <apk>`. In the app type the Mac's `ip:8080` in the field and tap Start;
the address is remembered. The server (`node server.js`) stays plain HTTP on 8080.

## Secure context (required for tilt on Android Chrome)

**Verified 2026-10-20, Chrome 155 / Android 10:**

- Plain `http://` LAN page: `deviceorientation` never fires (`orient:none`).
- Self-signed HTTPS (tap through the warning): page loads, but Chrome auto-denies the motion-sensor
  permission on any origin with a certificate error (`navigator.permissions` reports `denied`,
  `DeviceOrientationEvent.requestPermission()` returns `denied`). Still no tilt.
- So the origin must be *trusted* as secure. Two ways:

**A. Chrome flag, per phone, no certificates (what we use now).** On the phone open
`chrome://flags/#unsafely-treat-insecure-origin-as-secure`, enable it, enter
`http://192.168.1.55:8080` (the Mac's LAN IP), Relaunch. Then open the plain HTTP URL. Redo if the
Mac's IP changes.

**B. Trusted certificate.** `brew install mkcert && mkcert -install && mkcert <lan-ip>`, rename the
output to `key.pem` / `cert.pem` next to `server.js`, and install mkcert's root CA on the phone
(`mkcert -CAROOT`, copy `rootCA.pem`, Settings > Security > Install certificate > CA). The server
then serves HTTPS on **8443** automatically (8080 only redirects there) and the page uses `wss://`;
game clients connect to `wss://<lan-ip>:8443` and must skip certificate verification (see
`test_client.js`). Keep `.pem` files out of git. The self-signed pair from the failed attempt is
parked as `*.pem.off`.

The debug line on the page shows `perm:` (motion-sensor site permission), `secure:` and raw event
counts; the page also sends the same diagnostics to the server log once a second (`diag ...`).
