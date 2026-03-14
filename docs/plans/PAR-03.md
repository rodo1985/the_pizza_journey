# PAR-03 Quiz Content

## Purpose

Expand the educational quiz system with more pizza-related questions, clearer rewards, and content that stays separate from gameplay code.

## Scope

- Add a larger multiple-choice question bank.
- Group quiz questions by level theme or ingredient.
- Tune score and reward values for correct answers.
- Keep question wording simple and child-friendly.

## Dependencies

- `FND-05` must be complete because the quiz modal, pause flow, and reward hooks need to exist first.

## Inputs And Interfaces Touched

- `QuizQuestion`
- quiz data files
- reward configuration
- quiz result text and feedback

## Deliverables

- Expanded quiz question bank
- Level-linked quiz sets
- Reward tuning notes
- Review guidance for family-friendly wording

## Acceptance Checklist

- Questions load from data instead of being hard-coded in scene logic.
- Multiple questions can be assigned to a level without changing runtime code.
- Correct and incorrect outcomes are clear to children.
- Rewards remain balanced and do not overpower the core platforming loop.

## Out Of Scope

- Free-text answer input
- Full localization system
- Voice narration
- Networked content delivery

## Suggested Branch Name

`codex/quiz-content`
