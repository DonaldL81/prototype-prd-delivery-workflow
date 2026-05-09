#!/usr/bin/env python3
"""Initialize product prototype workflow docs in a project.

Usage:
  python init_project_docs.py --project C:\\path\\to\\project
  python init_project_docs.py --project . --overwrite
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


WORKFLOW_TARGET = Path("docs") / "00_workflow.md"


def copy_template_tree(src: Path, dst: Path, overwrite: bool) -> list[str]:
    """Copy project document templates, excluding docs/00_workflow.md.

    The workflow file has a single source of truth at references/workflow.md.
    It is copied separately so the skill does not maintain two workflow copies.
    """

    copied: list[str] = []

    # Walk every file in assets/templates and preserve its relative path.
    for item in src.rglob("*"):
        if item.is_dir():
            continue

        rel = item.relative_to(src)

        # Skip workflow template copies. docs/00_workflow.md is generated from
        # references/workflow.md later in this script.
        if rel == WORKFLOW_TARGET:
            continue

        target = dst / rel
        target.parent.mkdir(parents=True, exist_ok=True)

        # Preserve existing project docs unless the caller explicitly asks to
        # overwrite them.
        if target.exists() and not overwrite:
            continue

        shutil.copy2(item, target)
        copied.append(str(rel))

    return copied


def copy_workflow_reference(skill_dir: Path, project_dir: Path, overwrite: bool) -> str | None:
    """Copy references/workflow.md to project docs/00_workflow.md.

    This keeps references/workflow.md as the only maintained full workflow
    source while still giving each initialized project its own workflow file.
    """

    workflow_src = skill_dir / "references" / "workflow.md"
    workflow_dst = project_dir / WORKFLOW_TARGET

    if not workflow_src.exists():
        raise SystemExit(f"Workflow reference not found: {workflow_src}")

    workflow_dst.parent.mkdir(parents=True, exist_ok=True)

    # Do not replace a project's workflow unless --overwrite is provided.
    if workflow_dst.exists() and not overwrite:
        return None

    shutil.copy2(workflow_src, workflow_dst)
    return str(WORKFLOW_TARGET)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", default=".", help="Target project directory")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    # Resolve the skill layout from the script location:
    # skill/
    #   scripts/init_project_docs.py
    #   assets/templates/
    #   references/workflow.md
    script_dir = Path(__file__).resolve().parent
    skill_dir = script_dir.parent
    template_dir = skill_dir / "assets" / "templates"
    project_dir = Path(args.project).resolve()

    if not template_dir.exists():
        raise SystemExit(f"Template directory not found: {template_dir}")

    # Ensure the target project directory exists before copying files into it.
    project_dir.mkdir(parents=True, exist_ok=True)

    # Copy reusable project templates such as AGENTS.md, project-brief.md,
    # page-specs.md, decision-log.md, and PRD.md.
    copied = copy_template_tree(template_dir, project_dir, args.overwrite)

    # Generate docs/00_workflow.md from the single workflow source.
    workflow_rel = copy_workflow_reference(skill_dir, project_dir, args.overwrite)
    if workflow_rel:
        copied.append(workflow_rel)

    print(f"Project: {project_dir}")
    if copied:
        print("Created/updated:")
        for rel in copied:
            print(f"- {rel}")
    else:
        print("No files copied. Existing files were preserved. Use --overwrite to replace them.")


if __name__ == "__main__":
    main()
