# Approved concepts → 3D production

2026-10-19. The user approved the look and feel of the last four current visuals: Kestrel emission v004, Anchor Ring context v002, track kit v002 and tactical study v001. Exact dimensions, hidden surfaces, topology and engine implementation remain unresolved production details.

## Ownership

ChatGPT owns artistic design, visual assets, material/marking art and appearance review. Claude owns executable Blender/tooling scripts, exports, engine integration and shaders. Claude should implement the art rather than invent a replacement aesthetic. No detailed gameplay design is required for this modeling step.

## 1. Establish one coherent model

Use Blender as the proposed editable source. Work in meters. Start with one vehicle and a short track section, not the entire circuit.

Generated pictures cannot supply reliable topology or mutually exact views. Build one internally consistent blockout and review it from front, rear, side, top and the gameplay camera. Do not try to satisfy contradictory perspective details in different pictures. Keep the approved silhouette and visual hierarchy as the authority; document any resolution of ambiguities.

Kestrel starting envelope: 5.6m × 3.2m × 1.35m body, provisional. Block out the two thick nose prongs, central slot, recessed canopy, rear crossbeam and paired engine pods using simple beveled meshes. Add broad repair plates and two hoses only after the primary proportions work. Mirror structural parts, then vary paint and repairs asymmetrically. The central slot must be genuine geometry; it defines the silhouette.

Review deliverable: editable source plus neutral-gray and silhouette captures, before detailed textures. Include a three-quarter view matching the hero image and the intended chase-camera view. ChatGPT checks proportion and identity.

## 2. Build the smallest useful track kit

Model a straight deck, a broad curve, barrier, underside support and start/finish gate. Reuse the same material family and clipped chunky construction. Existing proposed sizes/budgets are in `ASSET_PLAN.md`.

Begin with one straight/curve join and a barrier, so scale and seams can be checked beside Kestrel. Keep a continuous drivable surface. A curve needs its own curved barrier treatment or suitably short fitted repeats; do not force a long straight barrier across the bend. Reuse repair plates and graffiti through shared art, not unique high-detail damage geometry.

After the section is approved, assemble one simple closed circuit. Distant ring structures can use a few repeated low-detail silhouettes; a planet backdrop needs no terrain model. Spend geometry where it affects the visible silhouette.

## 3. Separate geometry from surface art

| Feature | Production treatment |
|---|---|
| Forked hull, engine frames, canopy, large patch plates | Actual geometry |
| Bevels and large silhouette dents | Geometry where visible |
| Thick exposed hoses | Simple low-sided curved geometry |
| Worn paint, grime, small seams and scratches | Shared texture/mask treatment |
| Crew graffiti, number 01, arrows, tallies | Authored marking atlas/decals or UV artwork |
| Bright cyan aperture | Small visible surface with separate emission control |
| Light trails and sparks | Engine effect, not permanent modeled ribbons |
| Tactical brackets, target labels and paths | Engine overlays/effects, not a second environment model |

Generated paintings are reference images, not directly usable albedo maps: their lighting and shadows must not be projected indiscriminately onto the model. ChatGPT supplies deliberately authored paint/graffiti designs as needed. Claude establishes the UV/import workflow.

## 4. Match the finish early

Use the small shared library in `../ART_DIRECTION.md`. Match the worn bone/mustard/oxide paint, graphite structure and sparse acid-lime graffiti before extra detailing. Painterly wear should work at gameplay distance, rather than rely on tiny scratches.

Half-cel shading is a renderer treatment: broad softened light/shadow bands, restrained highlights and selective edge accents. It is not extra mesh complexity. Make one material/lighting test on Kestrel and a barrier before shading the complete circuit.

Implement mint-white light cores with controlled cyan bloom and rear-only trailing ribbons using `VFX_SPEC.md`. Preserve the engine frames and readability. Racing and tactical views use the same models; only lighting emphasis, trail prominence and overlays change.

## 5. Package and verify

Preserve an editable `.blend` source. Export a practical interchange format that Claude tests with the selected Unity version/render pipeline; choose FBX or GLB based on actual importer support, not assumption. Record axis conversion, applied scale, pivots, material mapping and normal handling.

Keep collision geometry simple and separate from visible detail. Name rear trail sockets explicitly. Check transforms, normals, material slots, seams, UVs and gameplay-camera readability after import. Record actual triangle counts and performance instead of declaring provisional budgets achieved.

First requested output from Claude: **one gray Kestrel blockout, one straight/curve track sample and matching review captures**. Then ChatGPT reviews the silhouette and scale; material/graffiti/emission work follows. Do not detail the whole circuit before the first section looks right.

No models, scripts or working shaders were created as part of this document. This is the production handoff for making them.
