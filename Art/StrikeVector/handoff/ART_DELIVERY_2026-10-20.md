# ChatGPT → Claude — Art delivery 2026-10-20

Ownership unchanged: ChatGPT handles art direction and visual assets. Claude handles code, mechanics, modeling tooling and engine integration. Existing approved concepts remain the look-and-feel authority.

## Delivered references

Each sheet has both a `.png` preview and an editable `.svg` under `production/references/`.

| Request | File stem | Use / limitation |
|---|---|---|
| REF_01 | `REF_01_Kestrel_Construction_v001` | Front, rear, side, top, underside at 80px/m, all derived from the same simplified construction. Proposed geometry, not a final model or newly approved design. Body 5.6 × 3.2 × 1.35m; axes X right / Y forward / Z up. |
| REF_05 | `REF_05_Track_Profiles_v001` | 16m clear deck, 1.2m barriers; proposed 0.6m barrier thickness and 0.45m deck thickness. Straight/curve tangent, barrier fitting and support study. R64/30° is a library example. |
| REF_06 | `REF_06_CurrentCircuit_Plan_v001` | Map of the actual Race.unity route, not a replacement. Corresponding `_Data_v001.json` includes source control points and sampled XZ coordinates. 1366.07m centerline. |
| REF_08 | `REF_08_Markings_Preview_v001` | Readable presentation only. Use the transparent art files described below for decals. |
| REF_10 | `REF_10_Phone_Layouts_v001` | Static plan/race/pulse design studies at 390 × 844 logical pixels. Separate screen SVG/PNG exports under `assets/ui/`. No controller code changes. |

REF_06 and REF_10 reflect the existing baseline rather than inventing a new circuit. The example colored lines in the planning study show visual treatment only; they are not valid authored racing splines. A1–A3 and displayed values are illustrative placeholders, not defined abilities or mechanics.

## Usable graphics

`assets/decals/SV_GFX_Markings_Atlas_v001.png`: 2048 × 1024 RGBA, transparent background, unlit flat colors. Eight 512px cells: original acid-lime crew arrow, bone tallies, numbers 01–04, mustard chevrons, mustard/graphite hazard patch. All have clear cell padding. The matching JSON records cell pixels and bottom-left UV bounds; editable SVG included.

Individual 512 × 512 PNG/SVG graphics are supplied alongside the atlas. PNG files resolve the font appearance; editable number SVGs use Arial Bold and need that font or conversion to outlines if your tool lacks it. This atlas is clean base ink; gritty wear should be applied selectively through the material/paint mask so it fits each surface. Do not repeat the same damaged chip pattern everywhere. No lighting is baked into the art.

`assets/ui/SV_UI_{Plan,Race,Pulse}_Study_v001.{png,svg}` are complete flat screen studies, not button sprite sheets or working layouts. Implement text, touch zones and dynamic values natively. Confirm safe areas and ergonomics on the actual phone before treating them as final UI.

## Requested next output from Claude

A gray Kestrel blockout and one road/barrier/curve sample. Show front/rear/side/top and the actual chase camera, with scale and actual triangle/material counts. Preserve the approved hero identity; use REF_01 to resolve the initial geometric construction, and flag conflicts for art review.

Confirm built-in versus URP before shader look matching. The current project is built-in although the agreed plan names URP. Do not treat the flat artwork as a tested shader implementation.

## Outstanding requests

REF_02 detail callouts, REF_03 chassis variants/liveries, REF_04 role/ability icons, REF_07 backdrop values, REF_09 lit materials, REF_11 HUD and REF_12 VFX frame set remain open. REF_01/05 are ready to inform a first blockout but require review of the model before finalization. REF_06 is a delivered current-layout reference, not an approved new long-straight layout.

No new images here have user approval yet. They implement the existing visual direction as reviewable production proposals.
