# PAR-04 Mobile Touch Support

## Purpose

Add mobile touch controls using the shared input abstraction so the game becomes playable on phones and tablets without rewriting core gameplay systems.

## Scope

- Implement on-screen movement, jump, and hammer buttons.
- Map touch input into the same normalized player-intent interface used by keyboard controls.
- Adjust HUD layout and screen spacing for small screens.
- Validate that mobile controls do not block essential gameplay visibility.

## Dependencies

- `FND-03` must be complete because the input abstraction must already exist.
- `FND-05` must be complete because React overlays and HUD layout are part of the touch-control solution.

## Inputs And Interfaces Touched

- `InputController`
- `TouchController`
- React HUD and control overlay
- responsive layout styles

## Deliverables

- Touch control overlay
- Touch input mapping
- Mobile layout adjustments
- Basic mobile usability notes

## Acceptance Checklist

- The player can move, jump, and attack using touch controls.
- Touch controls feed the same gameplay logic as keyboard input.
- Core HUD information stays visible on mobile.
- The layout remains usable in common landscape mobile sizes.

## Out Of Scope

- Gesture-heavy controls
- Native app wrappers
- Controller support
- Full mobile-device performance optimization

## Suggested Branch Name

`codex/mobile-touch`
