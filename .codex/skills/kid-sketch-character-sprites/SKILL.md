---
name: kid-sketch-character-sprites
description: Turn a child's hand-drawn character sketch into a game-ready character art package with consistent movement variations, transparent PNG frames, and a reusable sprite plan. Use when Codex is given a kid-made drawing, scanned sketch, photo of paper art, or rough concept and needs to preserve the child's idea while cleaning it up into a playable 2D character for games, animation tests, sprite sheets, or motion-frame exports.
---

# Kid Sketch Character Sprites

Use this skill to transform a child's drawing into a clean, consistent character design and a PNG sprite set for game movement.
Preserve the child's intent first. Improve readability, silhouette, and production consistency without sanding off the personality that makes the drawing theirs.

## Inputs

- Accept a sketch as an attached image, screenshot, scan, or local image path.
- Accept optional notes about:
  - character name
  - age or personality
  - game genre
  - target style such as soft cartoon, storybook, retro platformer, or mobile game mascot
  - required actions such as idle, walk, run, jump, attack, hurt, celebrate
  - target canvas size such as `512x512` or `1024x1024`
- If the user does not provide these details, infer a gentle cartoon style that stays close to the drawing and default to a basic platformer action set.

## Required Workflow

1. Inspect the sketch carefully.
   - Identify the shapes the child clearly intended: head shape, hair, face, clothes, props, shoes, cape, tail, wings, or unusual features.
   - Separate intentional design choices from accidental wobble caused by hand drawing.
   - Preserve the emotional identity of the drawing even when cleaning proportions.
2. Build a character identity summary before generating art.
   - Write a short description of the character's silhouette, colors, attitude, and standout details.
   - Call out what must remain unchanged across all frames.
   - If the sketch is ambiguous in a way that changes the design materially, ask one brief clarification question. Otherwise proceed.
3. Define the sprite pack.
   - Start with `idle`, `walk`, `jump`, and `celebrate` unless the user requests a different set.
   - Add left or right facing rules, frame counts, and whether the pack should feel side-view, top-down, or three-quarter.
   - Keep one stable canvas size, character scale, and ground alignment for all frames.
4. Create a production-ready prompt pack and sprite plan.
   - Use `scripts/generate_sprite_plan.py` to create a JSON or Markdown manifest for actions, frame counts, naming, and export rules.
   - If needed, read [references/prompt-patterns.md](./references/prompt-patterns.md) for prompt structure and [references/sprite-guidelines.md](./references/sprite-guidelines.md) for consistency rules.
5. Generate the character art.
   - If an image-generation or art-export tool is available in the current session, use it to produce transparent PNG frames.
   - Keep the face, costume, body proportions, and key accessories consistent from frame to frame.
   - Favor clean cartoon readability over painterly detail so the frames remain usable in a game.
6. Validate the output set.
   - Check that the character keeps the same identity in every frame.
   - Check that feet placement, scale, eye line, and prop placement do not drift unnecessarily.
   - Check that every PNG has a transparent background and a predictable name.

## Non-Negotiable Art Rules

- Preserve the child's original idea. Do not redesign the character into a generic hero unless the user explicitly asks for reinterpretation.
- Keep the style family consistent across all movement states.
- Use transparent backgrounds for final PNG outputs.
- Use the same canvas size for the whole set.
- Keep the character centered consistently so game import is easier.
- Prefer bold silhouettes, simple color blocking, and readable expressions.
- Avoid extra background elements, shadows outside the character footprint, or perspective shifts that break animation continuity.

## Default Deliverables

Produce these artifacts unless the user asks for something narrower:

- A short character summary
- A sprite plan listing actions, frame counts, and naming
- A base style prompt describing the cleaned-up cartoon look
- One prompt per action if image generation is needed
- Transparent PNG files for each frame, or a clearly labeled blocker if PNG export is not available in the session

## Naming and Export Rules

- Use lowercase kebab-case names.
- Name files like `character-name_action_0001.png`.
- Keep frame numbering zero-padded to four digits.
- Keep all frames in one folder per character unless the user asks for per-action folders.
- If both sprite sheets and individual frames are produced, keep both and name the sheet `character-name_spritesheet.png`.

## Using the Helper Script

Run the helper script to create a reusable plan before generating images:

```bash
python3 scripts/generate_sprite_plan.py \
  --character "luna-star" \
  --style "bright cartoon platformer" \
  --view side \
  --size 1024x1024 \
  --action idle:4 \
  --action walk:6 \
  --action jump:3 \
  --action celebrate:5 \
  --format both
```

Use the generated plan to keep prompts, filenames, and frame counts aligned.

## Delivery Requirements

- Mention what details came directly from the child's drawing.
- Mention any tasteful cleanup choices you made, and why.
- List the exported actions and frame counts.
- If you could not generate PNGs in-session, say so plainly and provide the finished prompt pack plus sprite manifest so the user can generate the art in the next tool or workflow.
