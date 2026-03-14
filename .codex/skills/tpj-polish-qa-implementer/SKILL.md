---
name: tpj-polish-qa-implementer
description: Implement the PAR-06 Polish And QA workstream for The Pizza Journey. Use when Codex is working in this repo and needs to improve feel, readability, child-friendly usability, QA coverage, or other work defined by docs/plans/PAR-06.md and docs/plans/project-plan.md.
---

# TPJ Polish And QA Implementer

## Quick Start

- Read `docs/plans/project-plan.md` and `docs/plans/PAR-06.md` first.
- Inspect the current gameplay flow, HUD, feedback hooks, test setup, and any existing QA notes.
- Confirm the full first-playable loop already exists. If not, stop and report the missing dependency.

## Workflow

1. Review the current first-playable experience end to end.
2. Focus on clarity, feel, and confidence-building improvements before cosmetic extras.
3. Implement only the PAR-06 scope:
   - improve readability and feedback
   - refine difficulty and child-friendly clarity
   - add or refine audio and animation hooks when appropriate
   - strengthen QA notes and validation coverage
4. Update tests and docs when behavior or expectations change.
5. Report the polish wins, QA gaps addressed, and any remaining usability risks.

## Implementation Boundaries

- Prefer small, focused improvements over broad rewrites.
- Touch gameplay systems only when the polish task directly requires it.
- Do not add major new feature scope under the label of polish.

## Done Criteria

- The game feels clearer and more welcoming to a child.
- Feedback for success, failure, and quiz outcomes is easier to understand.
- QA notes or tests cover the polished behavior.
- The branch improves quality without destabilizing the architecture.
