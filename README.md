# the_pizza_journey

## What this repo is
The Pizza Journey is a family game project created by Sergio, Lucía, and Julia.
It is the shared workspace for planning, implementation, and kid-friendly creative direction, including characters, levels, quiz ideas, and gameplay polish.
The repo also keeps project-specific Codex skills locally so the workflow stays portable and easy to reuse.

## Key features / scope
- Build a family-friendly game with kid-driven ideas for characters, levels, and quizzes.
- Keep project planning and implementation artifacts in one place.
- Store project-specific Codex skills under `.codex/skills/` for repeatable workflows.
- Not yet a fully scaffolded runtime app in this repo root.

## Setup
This repo does not yet include a Python package or a frontend app scaffold at the root.

For Python work, use the standard `uv` workflow when Python tooling is added:

```bash
uv venv
uv sync
```

For project-specific skills, no install step is required beyond cloning the repo because local skill copies are stored in `.codex/skills/`.

## How to run
Current common workflows are documentation and skill maintenance.

```bash
# inspect local project skills
find .codex/skills -maxdepth 2 -type f | sort

# run the local sprite-plan helper script
python3 .codex/skills/kid-sketch-character-sprites/scripts/generate_sprite_plan.py \
  --character "luna-star" \
  --style "storybook cartoon platformer" \
  --view side \
  --size 1024x1024 \
  --action idle:4 \
  --action walk:6 \
  --action jump:3 \
  --format both
```

## Configuration
- No required environment variables are currently documented for the repo root.
- Local project skills are stored in `.codex/skills/`.
- Global Codex skills may also exist in the user profile, but project-specific skills should be copied into this repo to keep the workflow self-contained.

## Project structure
- `.codex/skills/`: local copies of project-specific Codex skills
- `docs/`: planning and project documentation
- `README.md`: project overview and workflow entry point
- `AGENTS.md`: repo-specific agent instructions

## Contributing / Development notes
- Keep new workflows documented in this README.
- When creating or updating a skill for this project, also keep a repo-local copy in `.codex/skills/<skill-name>/`.
- Avoid committing temporary caches or generated scratch files with the copied skills.
