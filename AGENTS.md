# AGENTS.md

## Purpose
This repo contains the local project context for The Pizza Journey. Prefer simple, readable changes and keep repo-specific workflows documented so another contributor or agent can continue the work without guesswork.

## Local Skill Copy Rule
- When creating a new Codex skill for this project, always keep a local copy inside `.codex/skills/<skill-name>/`.
- If the skill is also created or updated in the global skills directory, copy the same final files into this repo so the project remains self-contained.
- Copy the full skill package when present:
  - `SKILL.md`
  - `agents/openai.yaml`
  - `scripts/`
  - `references/`
  - `assets/`
- Do not copy transient artifacts such as `__pycache__/`, temporary exports, or generated test files.
- When a local skill copy is added or updated, update `README.md` so the local skill workflow stays discoverable.

## Documentation Expectations
- Keep `README.md` accurate whenever project workflows change.
- Document important repo folders when they become part of the normal workflow.
- Prefer exact file paths and runnable commands over vague instructions.

## Skill Conventions
- Keep skill names lowercase and hyphenated.
- Make skill descriptions explicit about when the skill should be used.
- Prefer small helper scripts and focused references over long, bloated `SKILL.md` files.
