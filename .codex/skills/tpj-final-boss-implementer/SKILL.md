---
name: tpj-final-boss-implementer
description: Implement the PAR-05 Boss Battle workstream for The Pizza Journey. Use when Codex is working in this repo and needs to add the final boss encounter, final-level retry rules, or other work defined by docs/plans/PAR-05.md and docs/plans/project-plan.md.
---

# TPJ Final Boss Implementer

## Quick Start

- Read `docs/plans/project-plan.md` and `docs/plans/PAR-05.md` before editing.
- Inspect the current enemy, combat, level-flow, and retry systems.
- Confirm the gameplay foundation and level pipeline dependencies are already in place. If not, stop and report the blocker.

## Workflow

1. Review the current combat loop and final-level flow.
2. Reuse the existing gameplay systems where possible. Extend enemy or encounter patterns before inventing a separate boss framework.
3. Implement only the PAR-05 scope:
   - build the boss encounter
   - wire final-level-specific retry behavior
   - connect boss defeat to the celebration route
   - keep the difficulty readable and child-friendly
4. Update tests and docs for new encounter rules.
5. Validate the final-level retry flow and report what changed plus any balancing risks.

## Implementation Boundaries

- Prefer ownership over boss behavior, final-level rules, and victory handoff logic.
- Avoid broad rewrites to unrelated mid-game levels, quiz content, or touch-control systems.
- Keep the special-case logic contained so level 6 does not make the rest of the level pipeline harder to maintain.

## Done Criteria

- The boss battle fits into the existing gameplay architecture.
- Losing in level 6 restarts only level 6.
- Boss defeat flows cleanly into the endgame celebration.
- The solution stays readable and avoids spreading special-case logic across the whole codebase.
