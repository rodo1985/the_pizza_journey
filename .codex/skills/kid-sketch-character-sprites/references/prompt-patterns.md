# Prompt Patterns

Use these patterns when the session has an image-generation tool or when Codex needs to hand off precise prompts to another art workflow.

## Base Character Prompt

Use this structure:

```text
Turn this child's hand-drawn sketch into a polished 2D cartoon game character.
Preserve the original silhouette, personality, clothing idea, and standout accessories from the drawing.
Clean up proportions only enough for animation readability.
Style: [STYLE].
View: [VIEW].
Render as a clean production-ready character on a transparent background.
Keep the design consistent and suitable for a sprite animation set.
```

## Action Frame Prompt

Use this structure:

```text
Using the same character design established from the child's sketch, create the [ACTION] frame [FRAME_NUMBER] of [TOTAL_FRAMES].
Keep face, costume, colors, proportions, and accessories consistent.
Use a transparent background.
Maintain the same camera angle, scale, and ground alignment.
Pose intent: [POSE_DESCRIPTION].
Style: clean cartoon game sprite, readable silhouette, no background, no extra objects.
```

## Pose Description Hints

- `idle`: breathing, blinking, gentle sway
- `walk`: alternating legs, opposite arm swing, forward energy
- `run`: larger stride, stronger lean, more dynamic arm swing
- `jump`: crouch, lift-off, airborne
- `celebrate`: raised arms, bounce, smile, proud stance
- `hurt`: recoil, defensive pose, brief expression change

## Consistency Reminder

Repeat these constraints in prompts when the model starts drifting:

- same character
- same outfit
- same colors
- same proportions
- same accessories
- same art style
- transparent background
- centered character
