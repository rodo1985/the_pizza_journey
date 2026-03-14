# PAR-05 Boss Battle

## Purpose

Build the Final Pizza Castle boss encounter and the rule that losing in level 6 restarts only level 6.

## Scope

- Define the boss behavior loop and child-friendly difficulty target.
- Implement the boss encounter using the existing gameplay systems wherever possible.
- Add final-level-specific retry handling.
- Connect the boss defeat to the completed pizza celebration flow.

## Dependencies

- `FND-04` must be complete because the core gameplay loop and combat systems must exist first.
- `PAR-02` must be complete because the level pipeline should already support normal level loading before the special final level is added.

## Inputs And Interfaces Touched

- enemy and combat systems
- final-level progression rules
- level completion flow
- retry and respawn rules

## Deliverables

- Boss prototype
- Level 6 rules
- Restart-level-6-only behavior
- Connection to the final victory sequence

## Acceptance Checklist

- The boss fight can be completed within the existing game flow.
- Losing in level 6 restarts only level 6.
- The boss logic is readable and avoids unnecessary one-off hacks.
- The final victory route leads cleanly into the completed pizza celebration.

## Out Of Scope

- Cinematic cutscenes
- Complex multi-phase animation polish
- Extra-final secret bosses
- Online leaderboards

## Suggested Branch Name

`codex/final-boss`
