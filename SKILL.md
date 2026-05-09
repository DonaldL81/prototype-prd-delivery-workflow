---
name: prototype-prd-delivery-workflow
description: "Use when building product prototypes, frontend prototype pages, or PRD-driven demos from product-manager requirements. This skill enforces a disciplined workflow: clarify business and system context, confirm tech stack and development standards, plan before coding, confirm each page before implementation, keep previewable deliverables, continuously update page specs, decision logs, and PRD, distinguish demo logic from real product logic, and optionally write screens to Figma."
---

# Prototype PRD Delivery Workflow

## Overview

Use this skill to run a product prototype project as a controlled mini delivery process instead of ad hoc page building. It keeps the project flow, page specs, decisions, issues, demo logic, and PRD continuously synchronized.

## When To Use

Use this skill when the user asks to:

- Build a product prototype, frontend demo, or previewable page set.
- Convert product-manager requirements into pages plus PRD.
- Work page by page with confirmation before development.
- Avoid messy development and define a workflow first.
- Keep `docs/PRD.md` updated throughout development.
- Separate prototype demo behavior from real product logic.
- Produce `dist/`, a single-file HTML preview, project docs, and optional Figma output.

## Non-Negotiables

1. Do not start page development before project framework, tech stack, development standards, and development plan are confirmed.
2. Treat `docs/PRD.md` as a living document. Create its skeleton early and update it after each confirmed page.
3. For every page, ask whether reference materials exist before designing or coding.
4. Keep real product logic separate from demo logic such as hardcoded login, mock data, fake API responses, or fixed redirects.
5. Every confirmed decision, page spec, issue, solution, and PRD-worthy logic must be written to project documents, not only kept in chat.
6. Before final delivery, build `dist/`, generate a single-file HTML preview when feasible, check PRD coverage, and ask whether Figma output is needed.

## Project Documents

Default project files:

- `AGENTS.md`: project entry rules and recovery rules.
- `docs/00_workflow.md`: detailed workflow.
- `docs/project-brief.md`: project context, current phase, tech stack, standards, plan, delivery requirements.
- `docs/page-specs.md`: per-page fields, operations, interactions, API/backend logic, states, PRD write status.
- `docs/decision-log.md`: decisions, reference analysis, demo logic, issues, solutions, lessons learned.
- `docs/PRD.md`: living product requirements document.

If these files do not exist, initialize them before development. Use `scripts/init_project_docs.py` or copy the templates from `assets/templates/`.

## Workflow

1. Read `AGENTS.md` and `docs/00_workflow.md` if present. If missing, initialize them.
2. Gather requirement summary, requirement background, business background, business process, data interaction flow, frontend function framework, roles, modules, data sources, backend/API assumptions, and constraints.
3. Produce and confirm the project framework in `docs/project-brief.md`.
4. Confirm tech stack, run/build commands, delivery format, directory structure, mock rules, naming/style standards, responsive rules, and demo-logic labeling.
5. Create or update `docs/PRD.md` skeleton and the PRD pending-write list.
6. Produce the development plan and wait for user confirmation.
7. For each page:
   - Ask whether there are references: screenshots, prototype HTML, online system screenshots, competitor screenshots, Figma links, existing code, API docs, or field tables.
   - Analyze references before page confirmation.
   - Output a page confirmation card.
   - Wait for user confirmation.
   - Implement the page and provide preview.
   - Update `docs/page-specs.md`, `docs/decision-log.md`, and `docs/PRD.md`.
8. When issues are resolved, immediately record the problem, solution, PRD impact, and lesson learned in `docs/decision-log.md`.
9. Before delivery, run the delivery checklist, build outputs, ask whether Figma write-in is needed, and finalize `docs/PRD.md`.

## Page Confirmation Card

Use this structure before developing each page:

```text
页面名称：
页面目标：
用户角色：
页面入口：
页面字段：
页面操作：
交互逻辑：
接口逻辑：
后端逻辑：
数据来源：
权限规则：
加载状态：
空状态：
异常状态：
正式开发逻辑：
原型演示逻辑：
验收标准：
PRD 写入状态：
对应 PRD 章节：
待确认问题：
```

## Recovery Rule

If context is long, compressed, interrupted, or the current phase is unclear:

1. Stop development.
2. Read `AGENTS.md`.
3. Read the execution card in `docs/00_workflow.md`.
4. Read existing `docs/project-brief.md`, `docs/page-specs.md`, `docs/decision-log.md`, and `docs/PRD.md`.
5. Output: current phase, completed items, next step, pending confirmations.

## Complete Reference

For detailed rules, read `references/workflow.md`.
