# Prototype PRD Delivery Workflow

A Codex skill for running product prototype work as a disciplined PRD-driven delivery process.

This skill helps Codex avoid jumping directly into page coding. It guides the workflow through requirement clarification, project framework confirmation, tech stack and standards confirmation, page-by-page approval, continuous documentation updates, previewable delivery, and optional Figma output.

## What It Does

Use this skill when you want Codex to:

- Build product prototypes or frontend demos from product requirements.
- Confirm project scope, tech stack, standards, and development plan before coding.
- Ask for reference materials before each page implementation.
- Produce page confirmation cards before development.
- Keep `docs/PRD.md`, `docs/page-specs.md`, and `docs/decision-log.md` updated throughout the project.
- Separate prototype demo logic from real product logic.
- Prepare previewable delivery artifacts such as `dist/` and single-file HTML output.

## Repository Structure

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── templates/
│       ├── AGENTS.md
│       └── docs/
│           ├── PRD.md
│           ├── decision-log.md
│           ├── page-specs.md
│           └── project-brief.md
├── references/
│   └── workflow.md
└── scripts/
    └── init_project_docs.py
```

## Install

Copy this folder into your Codex skills directory, for example:

```text
~/.codex/skills/prototype-prd-delivery-workflow
```

On Windows, that is typically:

```text
C:\Users\<you>\.codex\skills\prototype-prd-delivery-workflow
```

Then restart or reload Codex so the skill can be discovered.

## Usage

Ask Codex to use the skill explicitly:

```text
Use $prototype-prd-delivery-workflow to initialize docs, confirm planning, and keep PRD updated.
```

Or ask for a PRD-driven prototype workflow, for example:

```text
帮我按 PRD 驱动流程开发一个产品原型，先不要直接写页面，先确认项目框架、技术栈和开发计划。
```

## Initialize Project Docs

The skill includes a helper script for creating the default workflow documents in a project:

```bash
python scripts/init_project_docs.py --project /path/to/project
```

To overwrite existing generated docs:

```bash
python scripts/init_project_docs.py --project /path/to/project --overwrite
```

This creates or updates:

- `AGENTS.md`
- `docs/00_workflow.md`
- `docs/project-brief.md`
- `docs/page-specs.md`
- `docs/decision-log.md`
- `docs/PRD.md`

## Notes

- `SKILL.md` contains the concise trigger and execution instructions.
- `references/workflow.md` contains the full detailed workflow rules.
- `assets/templates/` contains reusable project document templates.
- `scripts/init_project_docs.py` copies templates into a target project while preserving existing files unless `--overwrite` is used.
