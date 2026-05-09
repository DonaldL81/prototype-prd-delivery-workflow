# Prototype PRD Delivery Workflow

这是一个 Codex Skill，用于把产品原型开发变成一套受控、可追踪、PRD 驱动的交付流程。

它会约束 Codex 不要一上来就直接写页面，而是先完成需求澄清、项目框架确认、技术栈与开发规范确认、逐页确认、持续更新文档、生成可预览交付物，并在需要时写入 Figma。

## 适用场景

当你希望 Codex 执行以下工作时，可以使用这个 Skill：

- 根据产品需求构建产品原型或前端 Demo。
- 在编码前先确认项目范围、技术栈、开发规范和开发计划。
- 每个页面开发前先询问并分析参考资料。
- 每个页面开发前输出页面开发确认卡。
- 在开发过程中持续维护 `docs/PRD.md`、`docs/page-specs.md` 和 `docs/decision-log.md`。
- 区分原型演示逻辑和真实产品逻辑。
- 准备可预览交付物，例如 `dist/` 和单文件 HTML。

## 仓库结构

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

## 安装方式

把本仓库文件夹复制到你的 Codex skills 目录中，例如：

```text
~/.codex/skills/prototype-prd-delivery-workflow
```

Windows 通常是：

```text
C:\Users\<你的用户名>\.codex\skills\prototype-prd-delivery-workflow
```

复制完成后，重启或重新加载 Codex，让 Codex 发现这个 Skill。

## 使用方式

可以在提示词中显式要求 Codex 使用这个 Skill：

```text
Use $prototype-prd-delivery-workflow to initialize docs, confirm planning, and keep PRD updated.
```

也可以用中文描述你的工作方式，例如：

```text
帮我按 PRD 驱动流程开发一个产品原型，先不要直接写页面，先确认项目框架、技术栈和开发计划。
```

## 初始化项目文档

Skill 中包含一个初始化脚本，可以在目标项目中创建默认流程文档：

```bash
python scripts/init_project_docs.py --project /path/to/project
```

如果要覆盖已有生成文档：

```bash
python scripts/init_project_docs.py --project /path/to/project --overwrite
```

脚本会创建或更新以下文件：

- `AGENTS.md`
- `docs/00_workflow.md`
- `docs/project-brief.md`
- `docs/page-specs.md`
- `docs/decision-log.md`
- `docs/PRD.md`

## 文件说明

- `SKILL.md`：Skill 的触发描述和核心执行规则。
- `agents/openai.yaml`：Codex UI 中展示用的 Skill 元信息。
- `references/workflow.md`：完整的详细工作流规范。
- `assets/templates/`：初始化项目时使用的文档模板。
- `scripts/init_project_docs.py`：将模板复制到目标项目的初始化脚本；默认保留已有文件，除非使用 `--overwrite`。

## 工作流核心原则

1. 不直接开发：项目框架、技术栈、开发规范和开发计划确认前，不进入页面编码。
2. 逐页确认：每个页面都要先确认字段、操作、交互、接口、后端逻辑、数据来源和验收标准。
3. 参考资料先解析：有截图、原型、Figma、接口文档或竞品资料时，先解析再开发。
4. 过程持续沉淀：页面规格、决策记录和 PRD 必须边开发边更新。
5. 演示逻辑与正式逻辑分离：Mock、写死数据、固定跳转等只作为原型演示逻辑记录。
6. 交付前检查：构建产物、单文件 HTML、PRD 覆盖、演示逻辑剥离和 Figma 需求都要检查。
