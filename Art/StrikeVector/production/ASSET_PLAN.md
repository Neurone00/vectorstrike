# Proof-of-concept art asset plan

One vehicle design, one track. All values below are **proposed starting specifications**, not measured properties of the concept images or locked platform budgets. ChatGPT owns appearance; Claude builds/imports technical assets.

## Priorities

| Priority / ID | Asset | Art deliverable / implementation intent |
|---|---|---|
| P0 / VEH_001 | Kestrel vehicle | Approved hero reference; one chassis with separate emission regions |
| P0 / TRK_001 | Straight deck | Reusable road segment |
| P0 / TRK_002 | Broad curve | Same cross-section and materials as straight |
| P0 / TRK_003 | Barrier | Repeated side protection, repaired paint variants via shared markings |
| P0 / TRK_004 | Support | Simple reusable underside silhouette |
| P0 / TRK_005 | Start/finish gate | One landmark built from the same industrial language |
| P0 / MAT_001 | Shared materials | Painted armor, frame, rubber, canopy, energy and ink |
| P0 / GFX_001 | Markings/graffiti | Original crew tag, tallies, race number and directional/hazard marks |
| P0 / VFX_001 | Engine emission and trail | Appearance reference and technical art specification |
| P1 / ENV_001 | Backdrop | One planet treatment and a small set of distant station silhouettes |
| P1 / UI_001 | Essential interface appearance | Racing/tactical/phone visuals only for states Claude confirms necessary |
| P1 / VFX_002 | Tactical visual state | Brackets, path and restrained pulse treatment; no new mechanic specified |

No alternate vehicle classes, pickups, character set, large weapon library or second circuit in this milestone. UI and VFX are supporting art, not additional game-content scope.

## Vehicle proposal

- Bounding envelope: 5.6m length × 3.2m width × 1.35m body height, excluding trails; neutral hover clearance about 0.45m.
- Model groups: paired front armor prongs; central canopy/body; rear crossbeam; paired engine pods; two hoses; small reusable repair/fastener set.
- Identity must survive a solid-black silhouette and a neutral gray material pass.
- Initial triangle ceiling: roughly 12k–18k for the visible vehicle; LOD targets only after camera/platform review. Do not spend the budget automatically.
- Use shared painted materials and masking for color/wear; separate energy material/region. Avoid one material slot per plate.
- Proposed origin: vehicle root under chassis center at neutral hover reference; clearly named rear trail attachment points and separate front light attachments. Claude chooses conversion/export conventions and records them.

## Track proposal

- Drivable width 16m; road excludes barrier thickness. Repeated straight length 8m. Barrier height about 1.2m, thickness about 0.6m.
- Broad curve proposal: 64m centerline radius; 30° arc per module, repeated and rotated for bends. Straight/curve endpoints share identical cross-section and deck elevation.
- A simple closed test circuit is sufficient. Exact loop layout, speed suitability and race rules are Claude/user decisions. Visual reference favors broad orbital bends, one strong straight view and one start/finish landmark.
- Gate clear opening: 16m wide and 6m high. Supports and signage remain outside the drivable envelope.
- Barrier proposal: 4m repeat. Straight deck target ≤2k triangles, curve ≤4k, barrier ≤500, support ≤1k, gate ≤3k. These are provisional ceilings, not measured performance promises.
- At matching joints: no gaps, steps, z-fighting or sudden material discontinuities. Keep deck and barrier as separate reusable groups where practical.
- Reuse patch plates/decals rather than modeling unique damage into every module.

## Asset conventions

Suggested IDs: `SV_VEH_Kestrel`, `SV_TRK_Straight_08`, `SV_TRK_Curve_R64_A30`, `SV_TRK_Barrier_04`, `SV_TRK_Support`, `SV_TRK_StartFinish`, `SV_MAT_*`, `SV_GFX_*`, `SV_VFX_*`.

Use meters; record source and engine axis conventions, origin, scale and export settings explicitly. Do not assume Blender-to-engine axis handling. Version art non-destructively. GLB/FBX/native files are future implementation deliverables, not current assets.

## Review gates

1. Approved silhouette reproduced in neutral lighting.
2. One straight/curve junction fits at correct scale.
3. Shared half-cel materials, paint wear and graffiti read at gameplay distance.
4. Engine lights retain their frames; trails stay behind the craft and do not obscure navigation.
5. Whole track and necessary interface states reviewed in engine, with actual budgets/performance recorded by Claude.

## 2026-10-20 update

Claude/user planning permits Stock/Hauler/Strip variants on the same Kestrel chassis; these do not authorize unrelated vehicle designs. The current engineering route is 1366.07m and has variable curvature. REF_01/05/06 construction references and REF_08/10 art assets now exist; see `../handoff/ART_DELIVERY_2026-10-20.md`. Fixed-radius library pieces must not be assumed to tile every bend of that existing route.
