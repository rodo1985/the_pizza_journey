---
name: tpj-level-pipeline-implementer
description: Implement the PAR-02 Level Pipeline workstream for The Pizza Journey. Use when Codex is working in this repo and needs to add or refactor level definitions, reusable placement rules, world progression content, or other work defined by docs/plans/PAR-02.md and docs/plans/project-plan.md.
---

# TPJ Level Pipeline Implementer

## Quick Start

- Read `docs/plans/project-plan.md` and `docs/plans/PAR-02.md` first.
- Inspect the current `LevelDefinition` shape, level-loading flow, and any sample level content before editing.
- Confirm the dependency from `PAR-02.md` is satisfied. If the level pipeline contract is missing, stop and report the blocker.

## Workflow

1. Identify the current shared level schema and the level-loading path.
2. Keep the solution generic. Extend the level definition format instead of adding level-specific logic branches where possible.
3. Implement only the PAR-02 scope:
   - add or refine reusable level-definition patterns
   - create level data for levels 2 to 5
   - keep them loadable by the same scene logic
   - document the intended difficulty ramp and theming
4. Update tests and docs for any level-contract changes.
5. Run validation and report the added level coverage plus any follow-up risks.

## Implementation Boundaries

- Prefer ownership over level data files, level schema types, and lightweight scene integration.
- Avoid changing quiz, boss, or touch-control behavior except where shared interfaces require a narrow update.
- Do not introduce a tilemap toolchain unless the repo already moved in that direction and the change is necessary for PAR-02.

## Done Criteria

- Levels 2 to 5 can be expressed through shared level data.
- The level scene stays generic and readable.
- Additional level content can be added without rewriting the scene architecture.
- Docs and tests explain the level schema clearly enough for a new contributor.
