# Subject recipes

Portrait faces stay in [portrait-rules.md](portrait-rules.md). Use this file when kind is pet, food, kitchen-object, architecture, or a group that is mostly a room of objects.

Load the matching section **before** the inventory card.

## pet

- Species silhouette first (cat loaf, dog sit, rabbit huddle).
- Eyes: two ovals + iris. No wet-eye shine stacks.
- Fur = 3–8 **white** clumps with a black outline. Never strand hair. Never fill the body black, even if the photo is a black cat or black dog.
- Dark pets stay colorable: body, ears, tail, and legs are empty white interiors.
- Collar / tag / bow as 1–2 closed loops. Tag lettering omitted.
- Whiskers: at most 3 closed-looking lines per side at advanced; omit on simple. Do not hatch a whisker pad.
- Nose / mouth as small closed shapes, not a filled muzzle mask.
- Background: one floor plane + optional cushion. No carpet weave.

## dark-object (black clothes, black hair, dark furniture, night sky)

- A dark thing in the photo is still a **white pocket** on the plate. Only the outline is black.
- Black hair = 4–8 white clumps, never a filled helmet.
- Black shirt / trousers / sofa / cabinet = one or two closed slabs, white inside.
- Night sky or dark wall = empty page or one light horizon band, not a painted black field.
- Shadows are omitted. Do not invent a gray or black puddle under the subject.

## food

- Plate / bowl first as an ellipse, food as large closed mounds.
- A cake is tiers + 3–6 candle sticks, not icing lace.
- Steam / shine omitted (not colorable).
- Cut fruit shows 3–6 segments max.
- Brand wrappers → plain bag/box rectangles, no logo lettering.
- Do not draw every crumb.

## kitchen-object (counters, tools, groceries)

- Named appliances as rectangles with one handle/door seam: hood, fridge, sink, faucet.
- Bowls = ellipse + rim. Contents = 3–8 pieces, not a pile of 40.
- Knife = blade rectangle + handle. Do not draw serrations.
- Cutting board = one rounded rectangle. Wood grain **forbidden** (one slab).
- Bottles = cylinder + cap. Labels omitted.
- Knit mitt / dish towel = one garment shape, no stitch grid.
- Use `--kind group` or `--kind object` in QC (looser speckle than portrait) only if the script accepts `--kind`. Otherwise default QC.

## architecture

- Building = big masses: roof, wall, 3–8 window rectangles, door.
- No brick hatch, no roof-tile lace, no balcony rail as 40 sticks (use a slab + 3 posts).
- Temple / shrine: roof silhouette + 1–2 columns + stairs as 3 bands.
- Interior room: floor plane, back wall, 2–4 furniture blocks.
- Sky / ground stay empty white bands.
- People in an architecture photo follow portrait/group recipes at reduced face budget.

## Shared texture law

Knit, wood, brick, grass, fur, water sparkle → **one closed mass**. If a line would speckle QC, omit it. Dark photo regions still stay white inside the mass.
