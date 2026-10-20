# STRIKE VECTOR — Shared project memory

Updated: 2026-10-20, Europe/Rome.

## Broader concept

A multiplayer science-fiction anti-gravity racing RPG combining fast accessible competition with combat, power-ups, abilities and tactical decisions. The world takes its hardware and setting seriously even when races become chaotic.

Reference intent: Wipeout's racing identity and anti-gravity speed; XCOM: Enemy Unknown/XCOM 2's strong shapes and tactical clarity; Mass Effect's orbital scale and cinematic science fiction. These are influences, not designs to reproduce. Mario Kart informs accessible multiplayer fun, **not visual style**.

The proposed interaction model uses a shared main display and individual phones, with gyro steering and touch actions. Tactical slow motion is part of the concept to investigate. Exact rules, synchronization, combat balance, control implementation and networking remain Claude/user work.

## Responsibility split — explicit user direction

**ChatGPT: art direction and visual assets. Claude: mechanics, code and engine.**

ChatGPT is the ongoing art partner: coherent visual identity, concepts, asset designs, materials, visual UI, VFX treatments, production art specifications and visual review. It should not focus too much on mechanics. Claude implements the game and translates art specifications into working engine content. Visual artifacts may require technical integration; the appearance is ChatGPT's responsibility, implementation Claude's.

## Decisions and their status

| Decision | Status |
|---|---|
| Less realistic, more gritty spacepunk | Explicit user direction |
| Graffiti accents | Explicit user direction |
| “.5 cel shading” | Explicit request; interpreted as a hybrid of broad cel shadow bands and soft shading, exact look still needs in-engine review |
| Kestrel image `SV_CON_001_Kestrel_APPROVED_BASE_v002.png` | User explicitly said “i love this!” |
| More emissive light parts and light trails “ash shaders” | Explicit request; interpreted as shader-driven emission/trails, not ash particles |
| Last four current visuals: emissive Kestrel v004, Anchor Ring context v002, track kit v002, tactical study v001 | User approved their look and feel on 2026-10-19; not geometry or working engine implementation |
| One vehicle and one track for the proof of concept | Explicit user scope |
| All assets necessary for that proof of concept | Explicit user scope; supporting assets rather than new vehicle/track content |
| Kestrel name, Anchor Ring setting name, numeric dimensions and budgets | ChatGPT proposals; not separately approved requirements |
| Extra vehicle instances visible in environment concept | Context art only; do not infer alternate vehicle assets or implemented multiplayer |
| Phone control model and tactical pulse | Broader concept from brief; mechanics not finalized |

The clean realistic v001 direction is superseded. Do not use its material treatment to guide production. The approved gritty image is the form and finish anchor; later graffiti, half-cel and emission requests must remain part of the direction.

## Current milestone

One Kestrel vehicle design, one compact orbital industrial race circuit, and enough supporting visuals to build and evaluate them: modular road/curve/barrier/support/gate art, shared materials, markings/graffiti, background planet/station treatment, engine/trail effects and the minimum interface appearance needed by the implementation.

Supporting-asset candidates are a production checklist, not permission to design a whole game. Avoid new factions, characters, vehicle classes, tracks or large weapon/ability libraries. Ask Claude which interface states need visual assets; ChatGPT then designs their appearance.

## Truth and source order

1. Latest explicit user instruction.
2. This shared memory and the current approved visual reference.
3. Current art direction and handoff documents.
4. Other concept images, interpreted as studies.
5. Original source brief where not superseded.

Written dimensions/material definitions override visual ambiguities in generated views; unresolved conflicts need a recorded decision, not silent guessing. Generated views are not orthographic engineering references.

## Continuation protocol

Read `CLAUDE.md` and the relevant handoff before work. Preserve approved files. Add numbered versions for iterations. Record significant new approvals, changes, delivered files and verification results here. Keep implementation status factual: proposed, generated concept, implemented, and verified are different states.

Historical first-art-session status: no 3D/engine implementation had then been verified. See the later 2026-10-20 implementation and art updates below for current status.

## Modeling handoff update — 2026-10-19

The user approved the last four current visuals for look and feel and asked how to model them in 3D. See `Art/StrikeVector/production/MODELING_WORKFLOW.md`. Preserve the approved style; resolve generated-view inconsistencies through a single consistent blockout. No 3D models have yet been produced or verified.

## Planning session — 2026-10-19 (Claude + user)

Full roadmap: Claude's plan file; summary here is the source of truth for mechanics decisions. Where this conflicts with the "Decisions" table above, this section wins.

### Design pillar

**A racing game that also feels like a MOBA and an RTS.** The craft is a unit: the player plans its routes, issues commands (abilities, targets, line switches) and manages a resource (charge), and may take direct control for moments that need micro. Operators are MOBA-style roles with ability kits; planned racing lines are the "lanes". Direct arcade steering is one tool, not the whole game.

### Decisions (explicit user choices)

| Area | Decision |
|---|---|
| Engine | Unity 6 LTS + URP; macOS build on the user's M3 Max |
| Proof of concept | Internal playable test in 4–6 weeks. Single player vs 3 AI rivals. Multiplayer later |
| Input | Android phone from day one via a web page on local Wi-Fi: gyro steering, thumb throttle slider, touch commands. No native app. Keyboard only as dev fallback |
| Movement | Spline-constrained motion on the track, not free hover physics. **Auto mode**: craft follows a player-drawn racing line at its planned throttle. **Manual mode**: tilt steers lateral position, slider sets throttle. Player toggles at any time |
| Planning | Pre-race the player draws up to 3 full-lap lines (multiple splines) on the phone's top-down track view with throttle per segment. In race: tap to switch the active line |
| Camera | Chase cam on the player only; rivals need not stay in frame |
| Pulse | Player-triggered, global slow-motion. Triggering costs charge; everyone with enough charge (AI too) may act during it |
| Damage | Hull points + short speed penalty on hit; zero hull = respawn behind, no elimination |
| Roster | 3 operators × 3 vehicles. Art stays ONE Kestrel chassis: vehicles are stat + livery/bolt-on variants (Stock / Hauler / Strip). Operator and vehicle combination changes play |
| Feedback loops | Charge economy (in-race actions fill a meter), situational modifiers, operator–vehicle synergies. No between-race progression in the PoC |
| Art pipeline | Reproducible Blender 4.5 Python scripts → GLB → Unity. ChatGPT supplies additional references first; request list in `Art/StrikeVector/handoff/CLAUDE_TO_CHATGPT.md` |
| Workspace | git + LFS initialised in this folder on 2026-10-19 |

### Proposals (Claude, not yet user-approved)

Operators Breaker / Warden / Scout with three abilities and a passive each; vehicles Stock / Hauler / Strip with tags balanced / heavy / light; starting costs and modifiers live in Unity data assets. First circuit ~1.5 km, 3 laps.

### Status — 2026-10-20

- `Tools/controller/`: Node relay + Android race page written and relay-tested on the Mac (a synthetic phone message reaches a game client). Not yet tested on a real phone; whether Android Chrome allows the gyroscope over plain HTTP is unknown, see its README.
- `Game/`: Unity 6000.6.6f1 project, built-in render pipeline for now. Compiles; `StrikeVector → Build Race Scene` and `Build Mac App` run in batch mode and produce `Game/Builds/StrikeVector.app`. **Verified 2026-10-20**: with the relay running and a synthetic phone stream (tilt + full throttle + boost), the player log shows the game switching from keyboard to phone input, steering across the 16 m deck, reaching 94.5 m/s on boost and completing laps of the 1366 m generated loop; captures in `Art/StrikeVector/blockout/ENGINE_2026-10-20_*.png`. Placeholder craft is five boxes; track is a generated ribbon with walls.
- Controller: **user decision 2026-10-20 (in the controller session): ship a small Android APK, not a browser page.** Real-phone tests showed Chrome and Brave block the gyroscope on plain HTTP and on self-signed HTTPS, and the user does not want to force a browser. The APK is a WebView around the same `race.html` with tilt from Android's SensorManager; debug build at `Tools/controller/android/app/build/outputs/apk/debug/app-debug.apk`. The relay stays plain HTTP on 8080 for phones (8443 only if certs are added) and plain `ws://127.0.0.1:8081` for the game, because Unity's TLS stack rejects self-signed certificates. `Tools/demo.sh` starts relay + app.
- Not yet done: a real phone driving the game end to end with the APK (the Unity side was verified with a synthetic phone stream over the same relay and protocol), planned lines/auto mode, AI, damage, charge, pulse, abilities, art. Blender blockout scripts wait for ChatGPT's REF_01/REF_05/REF_06.

## Art audit and production delivery — 2026-10-20 (ChatGPT)

Inspected current source, serialized route, settings and an engine capture. Engineering blockout exists; art is still missing. ChatGPT did not rerun the engine or verify real-phone end-to-end play. Current project uses built-in rendering while the agreed plan names URP; Claude should resolve this before shader matching.

Delivered editable SVG + PNG references REF_01 (five-view Kestrel construction), REF_05 (track cross-section/joints/support), REF_06 (map of the actual 1366.07m circuit), REF_08 (original markings), REF_10 (portrait phone state studies). Also delivered transparent 2048×1024 decal atlas, eight individual 512×512 graphics, per-cell UV metadata, individual phone screen studies and actual circuit coordinates. See `Art/StrikeVector/handoff/ART_DELIVERY_2026-10-20.md`.

All new construction details and layouts are proposals, not user-approved changes. Existing concept approval remains in force. No mechanics, controller or engine files changed. Next Claude output requested in the workspace: gray Kestrel and a straight/curve art sample for ChatGPT review. Remaining refs: 02/03/04/07/09/11/12. Current baseline map is a reference to the existing route, not a claim that the earlier proposed 1.5km long-straight circuit was built.
