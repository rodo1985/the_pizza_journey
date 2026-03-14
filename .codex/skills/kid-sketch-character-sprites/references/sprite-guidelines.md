# Sprite Guidelines

Use this reference when turning a child-made sketch into a stable game character set.

## Goal

Keep the drawing recognizable while making it clean enough for animation and game export.

## What To Preserve

- Core silhouette
- Hair shape and any unusual spikes, curls, or hats
- Face mood
- Clothing layers and costume gimmicks
- Signature accessories such as swords, capes, backpacks, crowns, or animal ears
- Color intent, even if the original coloring is rough

## What To Clean Up

- Accidental asymmetry that is not part of the concept
- Wobbly line thickness caused by the photo or scan
- Tangents that make arms, legs, or props hard to read
- Inconsistent limb lengths between frames
- Tiny details that will disappear at gameplay scale

## Animation Consistency Rules

- Keep the same head-to-body ratio in every frame.
- Keep eye placement stable unless the expression changes on purpose.
- Keep props attached in a repeatable place.
- Keep the feet touching an implied ground line for idle and walk cycles.
- Keep the torso mass stable during simple motion cycles.
- Exaggerate poses slightly for readability, but do not mutate the character.

## Recommended Starter Action Set

- `idle:4`
- `walk:6`
- `jump:3`
- `celebrate:5`

Use this as the default when the user wants a basic playable character and has not specified actions.

## Export Checklist

- Transparent background
- Stable canvas size
- Stable character scale
- Clear file naming
- One orientation rule for the whole set
- No background shadows or stray paint outside the character
