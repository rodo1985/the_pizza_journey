# The Pizza Journey Project Plan

Current status: planning complete, foundation implementation not started in this branch yet.

## Project Summary

The Pizza Journey is a family-friendly 2D side-scrolling platform game built as a web app for desktop and mobile browsers. The player chooses a cartoon character, travels through pizza-themed levels, collects ingredients, defeats friendly-scary spider enemies, answers simple pizza quiz questions, and completes the final pizza.

This plan focuses on a clean technical foundation first. The first delivery milestone is a playable vertical slice that proves movement, combat, quiz flow, progression, and child-friendly usability before the full six-level game is built.

## A. Architecture Decision

### Why Phaser 3 + TypeScript + Vite is a good fit

- Phaser 3 is a strong choice for a 2D platformer because it already provides scenes, arcade physics, camera support, collision handling, sprite animation hooks, and browser-friendly performance.
- TypeScript helps the project stay understandable as the number of level configs, character definitions, quiz questions, and game-state transitions grows.
- Vite gives fast startup, quick hot reload, simple static builds, and a good path toward later Progressive Web App support.
- React should wrap the game shell because menus, overlays, quiz dialogs, and future mobile touch controls are easier to maintain in standard UI code than inside the game canvas.

### Major technical components

- React app shell for menus, HUD overlays, quiz modal, and screen flow.
- Phaser runtime for side-scrolling gameplay, collisions, enemies, checkpoints, and camera movement.
- Shared session store for score, lives, selected character, ingredient progress, quiz state, and level results.
- Config-driven content layer for characters, levels, quiz questions, and future balancing.
- Local storage persistence for simple progression and settings.

### Maintainability structure

- Keep gameplay systems, UI systems, and content data in separate folders.
- Use reusable scene and object classes instead of one-off level scripts.
- Prefer data-driven level and quiz definitions over hard-coded level logic.
- Design the input layer behind an interface so keyboard is first and touch can be added later without rewriting gameplay code.
- Keep placeholder assets simple and easy to replace by using generated shapes and named asset keys.

## B. System Design

### Scenes

- `BootScene`
  - Sets up basic Phaser configuration and placeholder textures.
- `PreloadScene`
  - Loads future assets and establishes a clean loading step, even if the first version uses mostly generated placeholders.
- `LevelScene`
  - Runs the platform gameplay for any level using a `LevelDefinition`.

### Reusable game objects and classes

- `Player`
  - Handles movement, jumping, attacking, damage, respawn, and checkpoint use.
- `SpiderEnemy`
  - Handles simple patrol behavior, player collision, and defeat when hit by the hammer.
- `HammerHitbox`
  - Short-lived attack area created by the player controller.
- `IngredientCollectible`
  - Gives score and marks the level ingredient as collected.
- `QuizTrigger`
  - Pauses gameplay and opens a quiz event the first time the player reaches it.
- `CheckpointFlag`
  - Stores the latest safe respawn point in the current run.
- `GameSessionStore`
  - Shared state layer between React and Phaser.
- `LocalStorageSaveRepository`
  - Saves lightweight progression and settings between sessions.
- `KeyboardController`
  - Produces normalized player input from the keyboard.
- `TouchController`
  - Planned input adapter for future on-screen controls.

### State management

- Use a framework-neutral `GameSessionStore` as the single source of truth for:
  - current screen
  - selected character
  - current level id
  - score
  - lives or health
  - collected ingredient state
  - quiz modal state
  - win and lose outcomes
- React subscribes to state changes for the screen flow and HUD.
- Phaser reads and updates the same store during gameplay.

### Input handling

- Define an `InputController` interface that returns normalized player intent.
- The first implementation is keyboard-only.
- Future touch buttons should feed the same intent structure.
- Recommended MVP controls:
  - move left: `ArrowLeft` or `A`
  - move right: `ArrowRight` or `D`
  - jump: `ArrowUp`, `W`, or `Space`
  - hammer attack: `J` or `X`

### Level configuration

- Store level data in TypeScript configuration files.
- Each `LevelDefinition` should describe:
  - world size
  - theme colors
  - platform positions
  - holes and hazards
  - player spawn point
  - checkpoint position
  - spider spawn data
  - ingredient placement
  - quiz trigger positions
  - finish zone
- Start with simple rectangle-based geometry instead of tilemaps to keep the first version approachable.

### Quiz system

- Use multiple-choice questions in the MVP because they are easier for children and better for future touch input.
- A quiz trigger pauses gameplay and opens a React modal.
- Correct answers give bonus score and may optionally heal one health point later.
- Quiz data should be stored separately from level logic so Lucía can help extend it safely.

### UI and HUD

- React-based overlays should show:
  - current score
  - lives or health
  - selected character
  - ingredient collected state
  - quiz prompts and results
- UI should use large text, strong contrast, and simple language.

### Save and progression strategy

- Save lightweight progression in local storage:
  - selected character
  - highest unlocked level
  - basic settings
  - cumulative score
- Keep checkpoint respawn state session-only.
- For the full game, losing in level 6 should restart only level 6.

### Mobile support approach

- Build the layout as mobile-friendly from the start.
- Use Phaser scale settings that adapt to screen size.
- Keep input handling abstract so touch can be added without rewriting `Player`.
- Design HUD layout with future touch buttons in mind.
- Stay browser-first and avoid native-only assumptions.

## C. MVP Definition

The smallest playable version that proves the game works should include:

- a title screen
- a character selection screen with 3 placeholder character choices
- one playable character controller
- one level: Tomato Field
- one spider enemy
- one tomato ingredient collectible
- one quiz interaction
- one checkpoint
- one win condition
- one lose and retry loop
- placeholder visuals made from simple shapes and colors

### MVP success criteria

- A child can start the game without confusion.
- The player can choose a character and start the level.
- The player can move, jump, attack, collect the ingredient, answer a quiz, and finish the level.
- The player can lose and retry without breaking the flow.
- The codebase is simple enough for future contributors to extend with more levels and content.

## D. Team Structure

### 1. Tech and Design Lead

- Responsibilities:
  - own architecture decisions
  - keep the repo understandable
  - review pull requests
  - coordinate integration and deployment
  - maintain the roadmap
- Outputs:
  - architecture docs
  - merge decisions
  - release checklists
- Dependencies:
  - none
- Start:
  - immediately

### 2. Gameplay Engineer

- Responsibilities:
  - player movement
  - physics
  - combat
  - enemy behavior
  - checkpoints
  - level gameplay rules
- Outputs:
  - playable Phaser systems
- Dependencies:
  - project scaffold and shared state contracts
- Start:
  - during foundation phase

### 3. UI and App Engineer

- Responsibilities:
  - title screen
  - character selection screen
  - HUD
  - quiz modal
  - win and lose screens
  - save and progression bridge
- Outputs:
  - React shell and overlays
- Dependencies:
  - session store contracts
- Start:
  - during foundation phase

### 4. Content Designer

- Responsibilities:
  - level themes
  - character definitions
  - quiz questions
  - reward tuning
  - child-friendly wording
- Outputs:
  - content configuration files
  - balance notes
- Dependencies:
  - stable config formats
- Start:
  - after foundation contracts are in place

### 5. QA and Release Owner

- Responsibilities:
  - run smoke tests
  - validate child-friendly clarity
  - confirm builds and deployment steps
  - keep README and docs accurate
- Outputs:
  - QA checklist
  - release notes
  - verification reports
- Dependencies:
  - runnable build
- Start:
  - late foundation onward

## E. Task Breakdown

### 1. Foundation Phase

| Task ID | Title | Purpose | Dependencies | Deliverables |
| --- | --- | --- | --- | --- |
| FND-01 | Repo Scaffold | Create the React + Vite + TypeScript app, add Phaser, testing tools, base configs, and repo docs | None | Runnable app shell, package config, root docs |
| FND-02 | Core Architecture | Add Phaser bootstrap, scene registration, shared constants, and placeholder texture generation | FND-01 | Clean game bootstrap and typed structure |
| FND-03 | Session And Input | Implement shared state, local persistence, and keyboard input abstraction | FND-02 | Game session store and input contracts |
| FND-04 | Vertical Slice Gameplay | Build one sample level with player, spider, ingredient, checkpoint, hazards, and win or lose rules | FND-03 | Playable Tomato Field slice |
| FND-05 | UI Flow And Quiz | Build title screen, character select, HUD, quiz modal, game over, and victory screens | FND-03, FND-04 | Complete first playable loop |
| FND-06 | Docs And Validation | Add README, architecture docs, tests, and smoke-check instructions | FND-05 | Beginner-friendly documentation and validated prototype |

### 2. Parallel Development Phase

| Task ID | Title | Purpose | Dependencies | Deliverables |
| --- | --- | --- | --- | --- |
| PAR-01 | Character Pack | Expand the starter roster and make character selection content-driven | FND-05 | Three distinct starter characters |
| PAR-02 | Level Pipeline | Add reusable level definitions for levels 2 to 5 | FND-04 | Additional level configs and content rules |
| PAR-03 | Quiz Content | Expand educational questions and reward tuning | FND-05 | Larger quiz bank and tuning notes |
| PAR-04 | Mobile Touch Support | Add touch controls using the existing input abstraction | FND-03, FND-05 | Touch input and mobile-friendly controls |
| PAR-05 | Boss Battle | Build the final boss and level-6-specific retry rules | FND-04, PAR-02 | Final boss encounter and retry flow |
| PAR-06 | Polish And QA | Improve feel, readability, audio hooks, and child-friendly clarity | FND-05 | Polish backlog, fixes, and QA improvements |

### 3. Integration And Polish Phase

| Task ID | Title | Purpose | Dependencies | Deliverables |
| --- | --- | --- | --- | --- |
| INT-01 | Multi-Level Progression | Connect all levels, unlock flow, and final pizza assembly | PAR-01, PAR-02, PAR-03, PAR-05 | Complete six-level progression |
| INT-02 | Deployment And PWA Prep | Prepare static deployment, manifest polish, and future offline support | FND-06 | Browser deployment setup and PWA-ready structure |
| INT-03 | Family QA Pass | Run family playtests, fix confusion points, and finalize docs | INT-01, INT-02 | Release-ready prototype |

## F. Parallelization Plan

After the foundation is merged, these workstreams can run safely in parallel:

- Core gameplay and content expansion
  - character pack
  - level pipeline
  - boss battle
- UI and player-facing flow
  - menu polish
  - quiz presentation
  - win and lose feedback improvements
- Content data
  - quiz bank creation
  - level theming notes
  - reward tuning
- Mobile support
  - touch controls
  - responsive layout adjustments
- QA and polish
  - readability checks
  - child playtesting
  - animation and audio hooks

See the `PAR-XX.md` files in this folder for the workstream-specific briefs.

## G. Git And Worktree Strategy

### Branch strategy

- Keep `main` stable and always runnable.
- Build the foundation on:
  - `codex/foundation-phaser-react-vite`
- After foundation is merged, branch from updated `main` for each workstream:
  - `codex/character-pack`
  - `codex/level-pipeline`
  - `codex/quiz-content`
  - `codex/mobile-touch`
  - `codex/final-boss`
  - `codex/polish-qa`

### Worktree setup

Use separate worktrees so work can progress without branch switching:

- `../tpj-foundation`
- `../tpj-characters`
- `../tpj-levels`
- `../tpj-quiz`
- `../tpj-mobile`
- `../tpj-boss`
- `../tpj-polish`

### Merge guidance

- Keep each branch focused on one workstream.
- Rebase regularly on `main`.
- Merge foundation first.
- Use a temporary integration branch only if two workstreams need combined testing before they are safe to merge into `main`.

## H. Initial File And Folder Structure

```text
the_pizza_journey/
├─ README.md
├─ docs/
│  ├─ architecture.md
│  └─ plans/
│     ├─ project-plan.md
│     ├─ PAR-01.md
│     ├─ PAR-02.md
│     ├─ PAR-03.md
│     ├─ PAR-04.md
│     ├─ PAR-05.md
│     └─ PAR-06.md
├─ public/
│  ├─ manifest.webmanifest
│  └─ icons/
├─ src/
│  ├─ main.tsx
│  ├─ App.tsx
│  ├─ app/
│  │  ├─ GameShell.tsx
│  │  └─ routes.ts
│  ├─ game/
│  │  ├─ bootstrap/createGame.ts
│  │  ├─ config/gameConfig.ts
│  │  ├─ scenes/BootScene.ts
│  │  ├─ scenes/PreloadScene.ts
│  │  ├─ scenes/LevelScene.ts
│  │  ├─ objects/Player.ts
│  │  ├─ objects/SpiderEnemy.ts
│  │  ├─ objects/HammerHitbox.ts
│  │  ├─ objects/IngredientCollectible.ts
│  │  ├─ objects/QuizTrigger.ts
│  │  ├─ objects/CheckpointFlag.ts
│  │  ├─ input/InputController.ts
│  │  ├─ input/KeyboardController.ts
│  │  ├─ input/TouchController.ts
│  │  ├─ state/GameSessionStore.ts
│  │  ├─ state/LocalStorageSaveRepository.ts
│  │  ├─ data/characters.ts
│  │  ├─ data/levels/level1.tomato-field.ts
│  │  ├─ data/quizzes/level1.ts
│  │  ├─ ui/HudOverlay.tsx
│  │  ├─ ui/QuizModal.tsx
│  │  └─ utils/placeholderTextures.ts
│  └─ styles/
│     └─ app.css
├─ tests/
│  ├─ gameSessionStore.test.ts
│  └─ levelDefinition.test.ts
├─ index.html
├─ package.json
├─ tsconfig.json
├─ vite.config.ts
├─ vitest.config.ts
└─ pyproject.toml
```

## I. Foundation Implementation Scope

When foundation work starts, the first implementation branch should deliver:

- npm-based React + Vite + TypeScript scaffold
- Phaser wired into the React shell
- `BootScene`, `PreloadScene`, and `LevelScene`
- keyboard input controller
- one sample Tomato Field level
- one spider enemy
- one ingredient collectible
- one quiz trigger
- one checkpoint
- minimal HUD
- title screen
- character selection shell
- runnable prototype with placeholder graphics

### Foundation implementation rules

- Keep the code simple and beginner-friendly.
- Use comments for non-obvious logic and design decisions.
- Add docstrings or JSDoc for every function, method, and class.
- Prefer configuration over hard-coded level logic.
- Use placeholder visuals that are easy to replace later.
- Keep child-friendly difficulty and readability in mind.

### Completion status markers

- `Foundation complete`
  - Use this only after the scaffold, gameplay slice, UI flow, and docs are implemented and runnable.
- `Ready for parallel workstreams`
  - Use this only after foundation is merged and the shared contracts are stable enough for parallel branches.

At the time of writing this plan, neither marker should be claimed yet.
