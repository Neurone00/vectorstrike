# Kestrel — reference-led modeling plan v002

2026-10-20. Supersedes the rejected REF_01 construction proposal and the assumption that its proportions were suitable for modeling.

## Authority and accuracy

Primary form authority: `concepts/SV_CON_001_Kestrel_APPROVED_BASE_v002.png`. Secondary finish authority: `concepts/SV_CON_001_Kestrel_Emission_v004.png`. The approved gameplay image informs the rear, but discrepancies between generated images are expected.

The user rejected the later vector reference/marking/UI pack as uninteresting and inaccurate. Its files are historical proposals, not production authority. The user now explicitly requests an accurate plan and authorizes starting an actual 3D model. This authorizes ChatGPT's art-side model generation; Claude retains gameplay and engine ownership.

A single perspective image does not establish exact real dimensions, underside, wall thickness or hidden attachments. We can reproduce visible shape relationships and test them with renders. We cannot claim a measured reconstruction. 5.6m length is a working scale convention only; width and height must be judged by projected appearance, not used to force the rejected block proportions.

## Observed forms to reproduce

| Region | Visible evidence | Modeling treatment |
|---|---|---|
| Main silhouette | Two long thick armor bodies, broad rear pods, low central cockpit | Profiled meshes with changing width/height along length; preserve the central negative space |
| Nose | Dark inset cavity under a thick sloping armored brow; clipped lower corners | Actual aperture frame and recessed backing, not a light rectangle pasted onto a solid box |
| Top armor | Forward slope, broad planar tops, chamfered outer sides, sparse major seams | Separate fitted armor sections over a dark structural body |
| Shoulders | Elevated bone plates flank the cockpit and step down toward the rear | Angled shoulder pieces with readable gaps; avoid straight parallel sticks |
| Cockpit | Smoked sloping windshield, tapered upper enclosure and thick dark frames | Faceted canopy, separate window faces and slim framing |
| Inner slot | Dark inner walls and exposed ribbed structure, clear space forward of cockpit | Real opening with restrained inner-wall details |
| Rear crossbeam | Wide dark transverse structure joining two engines | Low bridge with large panels and visible underside separation |
| Engine pods | Large clipped-square housings, deep dark throats, bright bracket-like strips | Multi-ring frame, cavity, a few large louvers, separate emissive geometry |
| Hoses | Two thick corrugated black hoses sweep backward into oxide sleeves | Curves/tubes with repeated rib collars; readable at medium distance |
| Surface character | Bone and mustard paint, selected oxide repairs, chunky chips and grime | Broad color blocking first; controlled wear second; no uniformly noisy surface |

## Explicitly inferred areas

- Underside hover pads and structural keel: simple plausible proposal; keep hidden details sparse.
- Rear exit internals: use the approved chase view as support, with the same frame vocabulary as the hero view.
- Engine attachment and canopy internals: shallow closed volumes for the first model, no interior design commitment.
- Panel boundaries obscured by perspective: resolve with few large plates; no invented dense greebles.

## Work sequence and acceptance

1. Build editable volumetric primary forms directly in Blender. Compare a front three-quarter render to the approved hero before adding surface clutter.
2. Add actual cavity depth, angular canopy, engine frames, hoses and a small number of repair plates. Check front, side, top, rear and underside from this same model.
3. Apply the approved color hierarchy and restrained emission. Model preview materials are not a validated Unity shader. Avoid letting bloom hide geometric errors.
4. Render front and rear three-quarter views plus a neutral multi-view sheet. Review visible mismatch honestly; record unresolved differences.
5. Export GLB, re-import it into a fresh Blender scene and verify mesh presence, dimensions, materials and triangles. Preserve the editable `.blend` and reproducible construction source. Engine import/performance testing remains with Claude.

## Review priorities

Highest: broad chunky silhouette; depth/length of the central slot; thick sloping nose armor; recessed canopy; paired engine scale and crossbeam. Next: hose arcs, frame depths, repair rhythm and mustard bands. Last: graffiti, small scratches, bolts, sparks and cinematic trail presentation.

No claim of final accuracy, production readiness or user approval until the resulting model has been reviewed. A rendered image of the actual model is required; another generated illustration does not verify geometry.
