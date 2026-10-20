# STRIKE VECTOR — Start here

Read `PROJECT_MEMORY.md`, then `Art/StrikeVector/handoff/CHATGPT_TO_CLAUDE.md` before implementation.

## Ownership

- **ChatGPT owns art direction and visual assets.** This includes visual research, concept art, the visual bible, vehicle/environment design, materials, UI appearance, VFX appearance, asset specifications, and visual consistency reviews.
- **Claude owns mechanics, code, tools, and engine implementation.** This includes gameplay systems, controls, networking, camera behavior, physics, performance, importing assets, and implementing shaders/VFX from ChatGPT's visual specifications.
- ChatGPT should focus on art, not spend substantial effort designing mechanics. Mechanics discussions belong with Claude and the user. Request visual constraints from ChatGPT where implementation needs them.
- Technical asset generation, Blender scripts, exports and Unity integration belong with Claude under this division. ChatGPT supplies the artistic specification and reviews the resulting visuals.
- Neither assistant should silently change the other's agreed direction. Record proposals and dependencies in the exchange memory.

## Project and current milestone

STRIKE VECTOR is a multiplayer sci-fi anti-gravity racing RPG: arcade racing, weapons and power-ups, plus tactical/RPG decisions. A shared main screen shows racing; each player's smartphone supplies gyroscope steering and touch actions. Synchronized tactical slow-motion pulses are an idea to explore, not an implemented or locked mechanic.

The current proof of concept has **one vehicle design and one track**, with the supporting assets necessary to demonstrate them. This is a milestone within the broader game, not a replacement for its vision. Do not expand into more vehicle classes, additional tracks, or a complete RPG without user direction.

## Current art direction

**Gritty stylized spacepunk, graffiti accents, hybrid “.5 cel shading,” bright cyan emission and light trails.** Serious world; playful, chaotic competition. Chunky readable forms, salvaged industrial construction, worn bone/mustard/oxide-red paint over graphite. Avoid photorealism, pristine military showroom styling, generic neon cyberpunk, and Mario Kart-like visuals.

The user explicitly liked `Art/StrikeVector/concepts/SV_CON_001_Kestrel_APPROVED_BASE_v002.png`. Preserve that vehicle's identity. They then requested stronger emission from the cyan lights and shader-driven light trails. The user subsequently approved the look and feel of the emission revision v004, Anchor Ring context v002, track kit v002 and tactical study v001. Approval covers appearance, not precise geometry or implementation. See `Art/StrikeVector/production/MODELING_WORKFLOW.md` for the next production sequence.

The source brief is `Art/StrikeVector/reference/USER_BRIEF.txt`. Later explicit user decisions in `PROJECT_MEMORY.md` take precedence over conflicting details in that brief.

## State and next work

Current state (2026-10-20): an engineering Unity project, generated circuit, five-box craft, controller/relay and recorded driving captures exist. Production Kestrel/track models, matching materials, shaders and trails are still missing. ChatGPT inspected source/settings/captures but did not rerun the engine. See `Art/StrikeVector/reviews/ART_AUDIT_2026-10-20.md` and the new `Art/StrikeVector/handoff/ART_DELIVERY_2026-10-20.md` for delivered modeling references and art assets. Generated concept paintings remain appearance references, not model files.

The engine-side sequence was agreed on 2026-10-19; see the planning section at the end of `PROJECT_MEMORY.md` (Unity 6 + URP, spline-constrained movement with player-drawn lines, Android web controller, single player vs AI). Keep art choices aligned with ChatGPT's direction. Use `Art/StrikeVector/handoff/CLAUDE_TO_CHATGPT.md` to record implemented visual results, actual import settings, screenshots, limitations, and art requests.
