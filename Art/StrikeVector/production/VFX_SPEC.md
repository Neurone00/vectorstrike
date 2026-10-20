# Kestrel emission and trails — art specification

User request: make the existing light parts more emissive and leave light trails as shaders. ChatGPT specifies appearance; Claude owns shader/trail implementation and performance decisions.

## Emission

Existing cyan front apertures and rear engine apertures glow. Preserve their positions and dark surrounding housings. Color target: mint cyan `#79DDD0`, tending toward pale mint-white in the brightest cores, with a saturated mint middle and tight soft halo. Only a little spill reaches nearby metal. Bone armor and graffiti remain non-emissive.

HDR emission and bloom settings depend on renderer, exposure and tone mapping. Do not treat a fixed intensity value as portable. Match the concept at the chosen exposure; do not clip away aperture shape. Demonstrate emission both with and without bloom so the underlying light-region design can be reviewed.

## Trails

Two rear trail attachment points, aligned with the engine outlets. Front running lights do not generate propulsion ribbons. Taper width and opacity toward the tail. Use a pale core, mint surround, slight segmented painterly edge and a few fading square sparks. No thick smoke, fire plume or pervasive particle cloud.

Desired behavior: tail follows prior craft motion rather than rotating as a rigid beam; no trail jumps on reset/teleport; stable appearance as frame rate changes. Trail lifetime/distance is an implementation tuning parameter. Start visually short enough that adjacent racers and track boundaries remain readable. Avoid assigning a mandatory length before speed/camera tests.

Tactical presentation reduces trail prominence quickly so brackets and projected paths remain clear. Exact state timing, time-scale handling and transition triggers belong to Claude. Avoid writing mechanics based solely on this art note.

## Acceptance captures for art review

Neutral background close-up, gameplay distance, accelerating straight, broad turn, stopped/reset craft and proposed tactical state. Include a bright planet backdrop and dark station background. Confirm rear-only origins, stable taper, no opaque rectangular billboard edges, no oversized bloom, and no ribbons hiding targets.

This is a visual target and review checklist, **not an implemented shader or verified effect**.
