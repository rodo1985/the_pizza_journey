---
name: tpj-mobile-touch-implementer
description: Implement the PAR-04 Mobile Touch Support workstream for The Pizza Journey. Use when Codex is working in this repo and needs to add or refine touch controls, responsive gameplay overlays, mobile layout behavior, or other work defined by docs/plans/PAR-04.md and docs/plans/project-plan.md.
---

# TPJ Mobile Touch Implementer

## Quick Start

- Read `docs/plans/project-plan.md` and `docs/plans/PAR-04.md` first.
- Inspect the current input abstraction, HUD overlay, and mobile layout assumptions before editing.
- Confirm the shared input contracts and overlay shell already exist. If not, stop and report the blocker.

## Workflow

1. Review the keyboard input path and find the normalized player-intent contract.
2. Reuse the same gameplay intent model for touch input. Do not fork the gameplay logic into separate keyboard and touch code paths.
3. Implement only the PAR-04 scope:
   - add on-screen touch controls
   - route them through the touch input adapter
   - keep HUD and controls readable on mobile
   - preserve gameplay visibility
4. Update tests and docs for any input-contract or layout changes.
5. Validate in the available browser workflow and report supported behavior plus known gaps.

## Implementation Boundaries

- Prefer ownership over touch input adapters, HUD overlays, and responsive styles.
- Avoid rewriting core player movement or combat logic unless the existing abstraction is truly missing a shared hook.
- Keep the design landscape-first unless the repo requirements change.

## Done Criteria

- Touch controls feed the same intent structure as keyboard input.
- Mobile controls are usable without hiding critical gameplay information.
- HUD and controls remain readable on small screens.
- The implementation stays isolated enough that the gameplay core does not become mobile-specific.
