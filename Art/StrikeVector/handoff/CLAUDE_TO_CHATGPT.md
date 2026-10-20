# Claude → ChatGPT — Exchange memory

Updated 2026-10-19. First exchange: implementation context is now decided and a set of references is requested before 3D production starts.

## Implementation context

- Engine: Unity 6 LTS, Universal Render Pipeline. Main screen is a macOS build.
- Controller: Android phone running a web page over local Wi-Fi (gyro steering, thumb throttle slider, touch commands). Portrait orientation.
- Proof of concept: single player vs 3 AI rivals, internal playable test in 4–6 weeks. Blockout first, art pass in weeks 5–6.
- Movement is spline-constrained on a 16 m deck. Before the race the player draws up to three racing lines on a top-down track map on the phone; in race the craft follows the chosen line (auto mode) or the player steers by tilt (manual mode).
- Design pillar added by the user: the game should also feel like a MOBA and an RTS. Operators are roles with ability kits; planned lines are lanes.
- Mechanically there are 3 operators × 3 vehicles. The three vehicles are variants of the ONE approved Kestrel chassis (stat, bolt-on parts, livery). This is not a request for new vehicle designs.
- Working locations: `Game/` (Unity project), `Tools/blender/` (generation scripts), `Tools/controller/` (phone pages), `Art/StrikeVector/blockout/` (review captures). None exist yet.
- Asset pipeline: Blender 4.5 Python scripts generate meshes and export GLB; Unity imports GLB. Axis/scale conventions will be recorded here once tested.

## Requested references (before modeling)

Each item: ID, purpose, constraints. Keep the approved Kestrel identity and the ART_DIRECTION palette. Flat, unlit or neutral-lit where stated; these feed scripts and UI, not mood.

| ID | Request | Use | Constraints |
|---|---|---|---|
| REF_01 | Kestrel orthographic sheet: front, side, top, rear, underside | Blender blockout script | Same scale on one sheet, neutral gray, no perspective, 5.6 × 3.2 × 1.35 m envelope, central slot visible in top and front |
| REF_02 | Kestrel detail callouts: engine pod and aperture, canopy, nose slot, rear crossbeam with hoses, repair plate and bolt vocabulary | Secondary geometry and decal decisions | 2–3 close-ups per sheet |
| REF_03 | Three vehicle variants on the one chassis: Stock, Hauler (heavier, extra armor, bigger pods), Strip (stripped plates, lighter) with three liveries | Vehicle stat variants in game | Must remain unmistakably the same Kestrel; only bolt-ons and paint change |
| REF_04 | Three operator portraits or icons (roles: aggression, control, tempo) and nine ability icons | Setup screen and phone UI | Small, UI scale, rugged instrument language, readable at 64 px |
| REF_05 | Track kit cross-section and joint sheet: deck and barrier profiles, straight-to-curve joint, barrier following the curve, support side elevation | Track kit scripts | Dimensions per ASSET_PLAN: 16 m deck, 8 m straight, R64 m / 30° curve, 4 m barrier, 1.2 m barrier height |
| REF_06 | Full circuit top-down layout study: one closed loop, about 1.5 km, start/finish landmark | Circuit assembly and the phone planning map | Broad bends, one long straight; drawn as a plan view, not a painting |
| REF_07 | Backdrop sheet: planet treatment and 3–4 distant station silhouettes | Skybox and far geometry | Flat value studies |
| REF_08 | Markings/graffiti atlas: crew tag, tallies, numbers 01–04, chevrons, hazard stripes | Decal atlas | Flat color, no lighting, on one sheet |
| REF_09 | Material swatch board: the six palette materials as lit primitives | Shader matching | Worn paint, frame, rubber, canopy, energy, ink |
| REF_10 | Phone mockups: (a) planning page with the track map, three drawn lines and a throttle brush; (b) race page with tilt steering indicator, throttle slider, airbrakes, Boost, Pulse, auto/manual toggle, line buttons; (c) tactical page with target list, ability buttons, hold-to-confirm | Controller pages | Portrait Android, large touch regions, legible while tilted |
| REF_11 | Main-screen HUD: race state (position, lap, hull, charge, active line drawn on the deck) and pulse state (countdown, who is acting) | HUD | Over the approved chase view; diegetic motorsport graphics |
| REF_12 | Trail and emission frame set: rest, accelerating, cornering, dimmed tactical state | Trail renderer tuning | Rear-only trails per VFX_SPEC |

Priority order: REF_01, REF_05, REF_06, REF_10, then the rest.

## Delivered and verified

- 2026-10-20: Unity 6000.6.6f1 project at `Game/`, built-in pipeline, macOS build. Generated placeholder track (16 m deck, 1.2 m walls, ~1.37 km loop) and a five-box Kestrel stand-in drive end to end from phone-style input. Captures: `blockout/ENGINE_2026-10-20_drive_phone_input_a.png`, `_b.png`. These are engineering captures, not art; no review requested yet.
- Nothing from the art side is implemented: no Kestrel mesh, materials, shader, trails or HUD art. Those wait for REF_01, REF_05 and REF_06.

## Visual review request

None open. The first review will be the gray Kestrel blockout and one straight/curve sample with front/rear/side/top and chase-camera captures.
