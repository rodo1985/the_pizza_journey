---
name: tpj-character-pack-implementer
description: Implement the PAR-01 Character Pack workstream for The Pizza Journey. Use when Codex is working in this repo and needs to build or extend the starter character roster, character selection flow, placeholder character visuals, or other work defined by docs/plans/PAR-01.md and docs/plans/project-plan.md.
---

# TPJ Character Pack Implementer

## Quick Start

- Read `docs/plans/project-plan.md` and `docs/plans/PAR-01.md` before making changes.
- Inspect the current character data, selection UI, save state, and placeholder art flow.
- Confirm the dependency from `PAR-01.md` is already satisfied. If it is not, stop and report the blocker.

## Workflow

1. Review the current implementation and identify the existing character data model.
2. Keep the work data-driven. Prefer editing character definitions and selection rendering over adding character-specific branching to scene logic.
3. Implement only the PAR-01 scope:
   - add or refine three starter characters
   - give each one a distinct placeholder identity
   - keep selection persistence working
   - keep names and visuals easy to replace later
4. Update tests and docs for any behavior or data-model changes.
5. Run the relevant validation commands and report what changed, what was tested, and any remaining risks.

## Implementation Boundaries

- Prefer likely ownership areas such as character config, character selection UI, and placeholder presentation.
- Avoid changing unrelated level, quiz, boss, or touch-control systems except for narrow integration fixes.
- Do not add unique character abilities unless the PAR file or current branch explicitly requires them.

## Done Criteria

- Three starter characters exist in a data-driven format.
- Character selection clearly shows the three options.
- The selected character carries into gameplay correctly.
- The work remains easy to extend later with better art or unique abilities.
