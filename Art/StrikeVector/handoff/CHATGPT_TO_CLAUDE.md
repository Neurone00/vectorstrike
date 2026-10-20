# ChatGPT → Claude — Project and art handoff

Read the root `CLAUDE.md` and `PROJECT_MEMORY.md` first.

## What you are building

A proof of concept inside a broader multiplayer anti-gravity racing RPG. The long-term identity is fast accessible sci-fi competition with tactical/RPG combat, a shared main screen and personal phone controllers. Do not reduce the project vision to a vehicle render or an ordinary racing demo; equally, do not implement the whole envisioned game as this milestone.

Current art scope: **one vehicle design, one track and their necessary supporting assets**. Additional instances of the same chassis can reuse the asset if your gameplay tests need them; this is not a request for alternate vehicle art.

## Collaboration boundary

**ChatGPT handles art direction and visual assets. Claude handles mechanics, code and engine implementation.**

ChatGPT should not own detailed mechanics design. Tell ChatGPT which visual states/assets you need, with constraints and screenshots. ChatGPT provides the art, specifications and visual feedback. You implement mechanics, Blender/tooling code where needed, scene assembly, asset import, shaders, trail rendering, optimization and validation. Do not ask ChatGPT to choose gameplay algorithms simply because it authored the art.

## Art decisions to preserve

- Less realistic; gritty spacepunk.
- Graffiti accents with readable markings and restrained coverage.
- Hybrid “.5 cel shading”: broad graphic shadows plus some soft light and painterly wear.
- User-approved Kestrel base: `../concepts/SV_CON_001_Kestrel_APPROVED_BASE_v002.png`.
- Stronger cyan light emission and light trails requested after that approval.
- Keep the chunky split nose, dark canopy, rear crossbeam, twin square engines, thick service hoses, dirty bone/mustard/oxide repairs and graphite structure.
- Keep bright energy restricted to light apertures/trails; do not turn pale hull panels into glowing surfaces.

## Inputs and their limits

`../ART_DIRECTION.md` is the current visual guide. `../production/ASSET_PLAN.md` contains proposed dimensions and a prioritized list. `../production/VFX_SPEC.md` defines intended emission and trail appearance. `../reference/USER_BRIEF.txt` preserves the original concept.

Concept images are appearance references, not ready-to-import models or verified texture maps. Generated multi-view geometry may disagree. Use the approved hero view for identity; use recorded numeric specs for dimensions. Propose a resolution when they conflict. Do not claim a working shader, GLB or model exists unless you actually produce and test it.

Some context images were generated before scope was narrowed. Rival craft, distant structures and illustrative UI do not establish extra content or locked mechanics. Files under `concepts/superseded/` are historical studies, not current visual authority.

## Suggested implementation exchange

Return a neutral-lit blockout of Kestrel and a short track section before expensive detail work. Include front/rear/side views, scale, actual triangle/material counts and gameplay-camera screenshots. Then request ChatGPT's art review. Engine/render pipeline and target hardware have not been specified; establish those with the user before treating numerical budgets as requirements.

Visual art requests should say: asset ID, intended use, camera/distance, dimensions, file-format needs, material/shader constraints, visual states and relevant screenshots. Keep technical constraints concise and leave artistic choices to ChatGPT.

## Current implementation status

No verified model, Blender script, shader, engine scene, functioning phone controller or playable gameplay. Only concepts and documentation have been created. The last four current studies are now approved for look and feel: emission Kestrel v004, Anchor Ring context v002, track kit v002 and tactical study v001. They remain concept references, not verified production models. See `../production/MODELING_WORKFLOW.md`.

## Current-date addendum — 2026-10-20

The earlier no-engine status above describes the initial art handoff. Engineering implementation now exists; see PROJECT_MEMORY.md for Claude's verified runs. For this delivery, read `ART_DELIVERY_2026-10-20.md`: REF_01/05/06 construction references and REF_08/10 graphics/layout studies are supplied. The current renderer is built-in; URP remains the agreed target in planning notes. New art proposals have not received user approval.
