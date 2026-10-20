# STRIKE VECTOR — Unity project

Status 2026-10-20: compiles on Unity 6000.6.6f1; `StrikeVector → Build Race Scene` and `Build Mac App` both run in batch mode. Driving around the generated loop verified from the player log and screenshots.

## First run

1. Unity Hub with Unity **6000.6.6f1** (installed 2026-10-20; Mac Build Support is included on macOS).
2. Hub → Add → select this `Game/` folder.
3. Packages resolve on open. The project is on the built-in render pipeline for now; URP comes with the art pass.
4. Menu **StrikeVector → Build Race Scene**. It creates `Assets/SV/Scenes/Race.unity`: generated track ribbon, placeholder Kestrel (five boxes), chase camera, HUD, input stack.
5. Press Play. Keyboard: arrows/WASD, Q/E airbrakes, Shift boost, Space pulse.
6. Phone: install `Tools/controller/android/app/build/outputs/apk/debug/app-debug.apk` on the Android phone (copy it over and open it). Run `Tools/demo.sh` on the Mac (starts the relay and the app), type the Mac's IP with `:8080` in the phone app, tap Start, Calibrate, tilt. The game reads `ws://127.0.0.1:8081` and switches to the phone while it streams, back to keyboard when it stops. Browser pages are not used on Android: Chrome and Brave block the gyroscope on self-signed origins (see `Tools/controller/README.md`).
7. **StrikeVector → Build Mac App** writes `Game/Builds/StrikeVector.app`.

## What is where

| File | Role |
|---|---|
| `Scripts/TrackSpline.cs` | Closed Catmull-Rom centerline, arc-length sampling, generated deck + walls. Default ~1.4 km loop until the circuit layout reference exists |
| `Scripts/CraftMover.cs` | Craft state `(s, lateral, speed)`; tilt → lateral rate, slider → target speed, airbrakes, boost, wall scrape, lap count |
| `Scripts/RaceInput.cs` | The input struct and provider interface |
| `Scripts/KeyboardInput.cs`, `PhoneInput.cs`, `InputRouter.cs` | Keyboard fallback, WebSocket phone reader (`ClientWebSocket`, no package), auto-switch |
| `Scripts/ChaseCamera.cs`, `RaceHud.cs` | Follow camera with speed FOV; OnGUI debug HUD |
| `Scripts/Telemetry.cs` | Logs craft state every 2 s; with `-sv-shots` on the command line also saves screenshots to the persistent data folder |
| `Scripts/Editor/SVSetup.cs` | Scene builder and Mac build menu items |

Not here yet: planned racing lines / auto mode, AI rivals, damage, charge, pulse, abilities, art. See the planning section at the end of `../PROJECT_MEMORY.md`.
