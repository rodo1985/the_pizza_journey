#!/usr/bin/env python3
"""Generate a reusable sprite plan for a character animation set.

This helper creates a JSON and/or Markdown manifest that defines the
character name, style, canvas size, action list, frame counts, and expected
file names for a sprite pack. The output is intended to keep image generation
and export workflows consistent across actions.

Example:
    python3 generate_sprite_plan.py \
        --character "luna-star" \
        --style "bright cartoon platformer" \
        --view side \
        --size 1024x1024 \
        --action idle:4 \
        --action walk:6 \
        --action jump:3 \
        --format both
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class ActionPlan:
    """Describe one animation action and its output frame names.

    Args:
        name: Canonical action name such as ``idle`` or ``walk``.
        frames: Number of frames to export for the action.
        files: Ordered PNG file names for the action.
    """

    name: str
    frames: int
    files: list[str]


@dataclass(frozen=True)
class SpritePlan:
    """Describe the full character sprite package.

    Args:
        character: Normalized character identifier used in filenames.
        style: Target art direction for the sprite set.
        view: Camera view such as ``side`` or ``top-down``.
        size: Output canvas size in ``WIDTHxHEIGHT`` format.
        actions: Ordered list of action plans.
        naming_pattern: Filename pattern for generated PNG frames.
    """

    character: str
    style: str
    view: str
    size: str
    actions: list[ActionPlan]
    naming_pattern: str


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for sprite plan generation.

    Returns:
        argparse.Namespace: Parsed arguments ready for validation.
    """

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--character",
        required=True,
        help="Character name used in output filenames, preferably kebab-case.",
    )
    parser.add_argument(
        "--style",
        required=True,
        help="Short art direction, for example 'storybook cartoon platformer'.",
    )
    parser.add_argument(
        "--view",
        default="side",
        help="Camera view such as side, top-down, or three-quarter.",
    )
    parser.add_argument(
        "--size",
        default="1024x1024",
        help="Canvas size in WIDTHxHEIGHT format.",
    )
    parser.add_argument(
        "--action",
        action="append",
        default=[],
        help="Action definition in the format name:frames. Repeat for multiple actions.",
    )
    parser.add_argument(
        "--format",
        choices=("json", "markdown", "both"),
        default="both",
        help="Output format to write.",
    )
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Directory where manifest files will be written.",
    )
    return parser.parse_args()


def validate_size(size: str) -> str:
    """Validate the output canvas size.

    Args:
        size: Candidate size string in ``WIDTHxHEIGHT`` format.

    Returns:
        str: The validated size string.

    Raises:
        ValueError: If the size is not in the expected format.
    """

    width, separator, height = size.partition("x")
    if separator != "x" or not width.isdigit() or not height.isdigit():
        raise ValueError("Size must use WIDTHxHEIGHT format, for example 1024x1024.")
    return size


def normalize_name(name: str) -> str:
    """Normalize a character or action name to lowercase kebab-case.

    Args:
        name: Raw user-provided identifier.

    Returns:
        str: Identifier normalized for filenames.
    """

    cleaned = name.strip().lower().replace("_", "-").replace(" ", "-")
    while "--" in cleaned:
        cleaned = cleaned.replace("--", "-")
    return cleaned


def parse_actions(raw_actions: list[str], character: str) -> list[ActionPlan]:
    """Parse action specifications into structured action plans.

    Args:
        raw_actions: Action definitions such as ``["idle:4", "walk:6"]``.
        character: Normalized character identifier used in filenames.

    Returns:
        list[ActionPlan]: Parsed actions with generated filenames.

    Raises:
        ValueError: If an action definition does not follow ``name:frames``.
    """

    if not raw_actions:
        raw_actions = ["idle:4", "walk:6", "jump:3", "celebrate:5"]

    plans: list[ActionPlan] = []
    for raw_action in raw_actions:
        name, separator, frame_text = raw_action.partition(":")
        if separator != ":" or not frame_text.isdigit():
            raise ValueError(
                f"Invalid action '{raw_action}'. Use the format name:frames, for example walk:6."
            )

        action_name = normalize_name(name)
        frames = int(frame_text)
        files = [
            f"{character}_{action_name}_{index:04d}.png"
            for index in range(1, frames + 1)
        ]
        plans.append(ActionPlan(name=action_name, frames=frames, files=files))
    return plans


def build_plan(args: argparse.Namespace) -> SpritePlan:
    """Build the complete sprite plan from parsed arguments.

    Args:
        args: Parsed command-line arguments.

    Returns:
        SpritePlan: Structured plan ready for export.
    """

    character = normalize_name(args.character)
    size = validate_size(args.size)
    actions = parse_actions(args.action, character)
    return SpritePlan(
        character=character,
        style=args.style.strip(),
        view=normalize_name(args.view),
        size=size,
        actions=actions,
        naming_pattern=f"{character}_<action>_0001.png",
    )


def write_json(plan: SpritePlan, output_dir: Path) -> Path:
    """Write the sprite plan as JSON.

    Args:
        plan: Sprite plan to export.
        output_dir: Directory where the file should be written.

    Returns:
        Path: Path to the written JSON file.
    """

    destination = output_dir / f"{plan.character}-sprite-plan.json"
    payload = asdict(plan)
    destination.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return destination


def write_markdown(plan: SpritePlan, output_dir: Path) -> Path:
    """Write the sprite plan as a human-readable Markdown file.

    Args:
        plan: Sprite plan to export.
        output_dir: Directory where the file should be written.

    Returns:
        Path: Path to the written Markdown file.
    """

    destination = output_dir / f"{plan.character}-sprite-plan.md"
    lines = [
        f"# {plan.character} sprite plan",
        "",
        f"- Style: `{plan.style}`",
        f"- View: `{plan.view}`",
        f"- Canvas: `{plan.size}`",
        f"- Naming: `{plan.naming_pattern}`",
        "",
        "## Actions",
        "",
    ]

    for action in plan.actions:
        lines.append(f"### {action.name}")
        lines.append("")
        lines.append(f"- Frames: `{action.frames}`")
        lines.append("- Files:")
        for file_name in action.files:
            lines.append(f"  - `{file_name}`")
        lines.append("")

    destination.write_text("\n".join(lines), encoding="utf-8")
    return destination


def main() -> int:
    """Run the CLI and write the requested sprite plan files.

    Returns:
        int: Process exit code. Returns ``0`` on success.

    Raises:
        ValueError: If input validation fails.
    """

    args = parse_args()
    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    plan = build_plan(args)
    written_files: list[Path] = []

    if args.format in {"json", "both"}:
        written_files.append(write_json(plan, output_dir))
    if args.format in {"markdown", "both"}:
        written_files.append(write_markdown(plan, output_dir))

    for path in written_files:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
