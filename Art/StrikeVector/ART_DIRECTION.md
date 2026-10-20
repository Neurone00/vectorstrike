# STRIKE VECTOR — Art direction v0.2

Status: working direction reflecting user feedback, 2026-10-19. Focus: art, not gameplay-system design.

## Visual promise

**Salvage-built orbital racers with military weight, garage individuality and bright energy exhaust.** Strong, simple silhouettes do most of the work. The finish is stylized, gritty and tactile; the world is serious without needing photographic realism.

Primary reference: [user-approved Kestrel](concepts/SV_CON_001_Kestrel_APPROVED_BASE_v002.png). The emission revision illustrates the requested brighter apertures/trails. Keep the approved silhouette and paint distribution as the anchor.

## Shape and finish

- Broad forked nose, visible central negative space, recessed dark canopy, rear crossbeam and paired squared engine housings define Kestrel.
- Chunky bevelled planes, clipped corners, strong structural frame. Few major forms before secondary detail.
- Structural symmetry supports reusable modeling. Asymmetric repair plates, paint and graffiti supply individuality.
- Worn paint is authored in broad chips and stains. Concentrate grime at seams, welds and exhausts; avoid uniform noise.
- A small number of thick hoses, readable fasteners and reinforcement plates communicate repairability. Avoid tiny greebles.
- Graffiti belongs on selected armor and trackside panels. Original abstract crew tags, rough stencils and tallies; no copied franchise marks.
- Graffiti must not obscure race numbers, hazards, targeting information or the vehicle's defining gap.

## Palette — proposed production targets

| Role | HEX | Use |
|---|---|---|
| Charcoal | `#252C30` | Structural frame, recesses, deck |
| Dirty bone | `#B8B09A` | Large painted armor and barrier panels |
| Faded mustard | `#C18A32` | Racing bands, gate, hazard accents |
| Oxide red | `#9F4938` | Salvage patches, repairs, heat-stained parts |
| Mint cyan | `#79DDD0` | Energy apertures and engine trails |
| Acid lime | `#C9D657` | Sparse graffiti accent, non-emissive |

These are authored swatch targets, not pixel samples from the painting. Lit images will differ. Preserve the dirty bone/mustard/graphite balance. Reserve the strongest brightness for energy and essential interface feedback.

## Hybrid “.5 cel” treatment

Interpretation: halfway between graphic cel shading and soft stylized shading. Two broad shadow families, softened boundaries, restrained variation inside lit planes and selective dark edge accents. Matte painted finish, simplified specular shapes and no photographic microdetail. Keep wear readable without making every edge black. The exact shader blend is an artistic target, not a prescribed engine algorithm or literal measured 50% property.

## Material library — appearance targets for Claude

| Material | Appearance | Implementation starting point, provisional |
|---|---|---|
| Painted armor | Matte worn bone/mustard/oxide | Roughness 0.65–0.85; paint metallic 0 |
| Bare frame | Dark satin steel | Roughness 0.45–0.65; exposed metal metallic 1 |
| Rubber/hose | Nearly black, broad highlights | Roughness 0.8; metallic 0 |
| Canopy | Opaque smoked graphic glass for PoC | Roughness 0.2–0.35; avoid transparency dependency |
| Energy | Bright mint with pale core | Separate emissive region; see VFX specification |
| Graffiti/markings | Matte ink, limited overspray | Shared atlas/decal workflow decided by Claude |

PBR parameters are art-oriented starting values; Claude should adapt to the chosen shader and renderer. Avoid separate full texture sets for every small part. Prefer a shared palette and one small wear/marking library. Painted metal should not be uniformly metallic just because the substrate is steel.

## World and lighting

Anchor Ring is a repurposed orbital industrial installation: dark modular deck, patched barriers, a blunt start/finish structure, exposed underside ribs, distant huge station forms and a planet backdrop. Reuse vehicle materials and clipped planar construction. Keep repair debris and visual clutter outside the route.

Warm directional key and cool planet fill support graphic light/shadow separation. Keep sufficient fill to read the charcoal frame. Distinguish foreground racer, road, distant architecture and sky by value. Static signage and graffiti are mostly non-emissive; avoid turning the scene into neon cyberpunk.

## Emission, trails and tactical appearance

Only the light apertures and trails emit; bone armor stays matte. Use pale cores, mint outer light and tight controlled bloom. Do not erase the dark engine housings with bloom. Rear exhaust outlets emit trails; front lights do not create forward thrust ribbons.

Trail direction follows motion history, fades and tapers, with a few small dying particles. Keep long ribbons behind the racer. In tactical presentation shorten/dim the trail and reduce secondary motion clutter so targets remain clear. Exact timing is Claude's implementation decision, reviewed against the artwork.

Tactical mode is the same world and camera language, with restrained brackets, labels and projected paths. Avoid an unrelated blue holographic world filter. Pair color with shape and text. Limit stacked overlays and preserve the route and vehicle silhouettes.

## Interfaces

ChatGPT supplies the visual language and requested UI assets, not control logic. Use a rugged handheld instrument appearance: charcoal panels, dirty bone type, mustard emphasis, cyan active feedback and clipped corners. Essential text stays crisp; distressed texture belongs on framing, not small text. Keep graffiti away from critical labels. Phone layouts should use large separated touch regions and stay legible while tilted; exact controls and required states are defined with Claude/user.

## Belongs / does not belong

Belongs: a broad patched hull with one crew tag, two bright engine slots, dark exposed frame and purposeful paint wear. A repeated road/barrier kit with one memorable orbital landmark.

Does not belong: a pristine white showroom racer, needle-shaped spaceship, realistic tank, tiny mechanical detailing everywhere, saturated neon on every seam, comic fantasy kart or arbitrary decorative graffiti covering the entire scene.

## Visual acceptance

The silhouette must read without textures. At normal gameplay distance the forked hull and paired engines remain distinct. Graffiti reads as accent, emission as energy, and hazard markings as navigation. Racing and tactical frames must visibly belong to the same scene. Final art requires in-engine visual review; concept images alone do not prove performance, readability or asset readiness.
