# PAR-02 Level Pipeline

## Purpose

Scale the foundation from one playable sample level into a reusable level-definition pipeline for levels 2 through 5.

## Scope

- Define reusable patterns for platforms, hazards, enemy spawns, checkpoints, and ingredient placement.
- Add level configuration files for Cheese Hills, Mushroom Forest, Olive Bridge, and Pepperoni Cave.
- Keep level logic generic so `LevelScene` can load each level from data.
- Document theme progression and difficulty ramp expectations.

## Dependencies

- `FND-04` must be complete because the first playable level establishes the base `LevelDefinition` format.

## Inputs And Interfaces Touched

- `LevelDefinition`
- enemy and hazard spawn configuration
- ingredient placement rules
- level theme metadata

## Deliverables

- Level config structure that supports levels 2 to 5
- Four additional level data files
- Reusable placement and balancing patterns
- Notes for future level-6 integration

## Acceptance Checklist

- Levels 2 to 5 can be represented with the same scene logic as level 1.
- Level data remains readable for beginner contributors.
- No level-specific hacks are required in `LevelScene` for normal progression.
- Ingredient placement and checkpoint rules are consistent across levels.

## Out Of Scope

- Final boss encounter
- Tilemap editor tooling
- Procedural generation
- Final art polish

## Suggested Branch Name

`codex/level-pipeline`
