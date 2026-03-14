# PAR-01 Character Pack

## Purpose

Expand the starter roster into three visually distinct placeholder characters while keeping character selection fully data-driven and easy to replace later.

## Scope

- Add or refine three placeholder character definitions.
- Give each character a distinct color palette and simple visual identity.
- Keep gameplay behavior compatible with the same base controller.
- Improve the character selection screen so the choices feel clear and fun for children.

## Dependencies

- `FND-05` must be complete because the character select flow and core session state need to exist first.

## Inputs And Interfaces Touched

- `CharacterDefinition`
- character selection UI
- placeholder art generation or asset references
- saved selected-character state

## Deliverables

- Three distinct starter characters
- Data-driven character configuration
- Updated character select presentation
- Easy-to-replace placeholder visuals and naming

## Acceptance Checklist

- Three characters appear in the select screen.
- The selected character persists into gameplay.
- Character data can be edited without changing scene logic.
- Placeholder names and visuals remain safe to replace later.

## Out Of Scope

- Unique abilities per character
- Premium art pipeline
- Unlock systems
- Voice lines or complex animations

## Suggested Branch Name

`codex/character-pack`
