---
name: tpj-quiz-content-implementer
description: Implement the PAR-03 Quiz Content workstream for The Pizza Journey. Use when Codex is working in this repo and needs to expand or refine pizza-question content, quiz reward tuning, quiz data organization, or other work defined by docs/plans/PAR-03.md and docs/plans/project-plan.md.
---

# TPJ Quiz Content Implementer

## Quick Start

- Read `docs/plans/project-plan.md` and `docs/plans/PAR-03.md` before editing.
- Inspect the current quiz question model, quiz modal flow, and reward hooks.
- Confirm the quiz runtime already exists. If the dependency from `PAR-03.md` is missing, stop and report the blocker.

## Workflow

1. Review the current quiz data structure and how quiz events are triggered.
2. Keep content separate from scene logic. Prefer adding or editing quiz data files and lightweight configuration over embedding content in runtime code.
3. Implement only the PAR-03 scope:
   - expand the multiple-choice question bank
   - organize content by level or ingredient
   - tune rewards and feedback text
   - keep wording child-friendly and easy to maintain
4. Update tests and docs for any quiz data or reward-contract changes.
5. Run validation and report content coverage, reward tuning decisions, and remaining risks.

## Implementation Boundaries

- Prefer ownership over quiz data files, reward configuration, and display text.
- Avoid refactoring unrelated platforming systems except for narrow integration changes required by reward hooks.
- Do not switch the interaction model away from multiple choice unless the project plan changes.

## Done Criteria

- Quiz questions live in data, not scene code.
- Content can scale per level or ingredient without changing the runtime flow.
- Rewards stay understandable and balanced.
- The wording remains simple, friendly, and easy for the family to review.
