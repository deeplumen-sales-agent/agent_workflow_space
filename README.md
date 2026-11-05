# Agent Workflow Space

这是 Deeplumen 各 AI agent 共用的规则、工作流和长期记忆仓库。

仓库采用“正式内容单一来源 + 各 AI 入口适配 + 候选记忆收件箱”的方式：

```text
各 AI 产生候选记忆 → inbox/ → 人工确认 → memory/ 或 workflows/ → 生成各 AI 入口文件
```

## 目录

- `core/`：所有 agent 都应遵守的基础规则、记忆政策和状态词表。
- `workflows/`：可复用的工作流和模板，例如 `workflows/prd-writing/`。
- `memory/`：已经确认的长期记忆、项目背景和决策记录。
- `inbox/`：各 agent 提交的候选记忆，未经确认不得视为正式规则。
- `runbooks/`：脱敏后的生产只读连接、核查和操作手册。
- `adapters/`：各 AI 平台的适配说明和生成结果说明。
- `scripts/`：生成适配文件和执行仓库校验的脚本。
- `docs/superpowers/`：本仓库的设计和实施记录。

## 快速开始

在仓库根目录执行：

```bash
python scripts/build-adapters.py  # Windows 也可以使用：py -3 scripts/build-adapters.py
python scripts/validate.py        # Windows 也可以使用：py -3 scripts/validate.py
```

`build-adapters.py` 会生成根目录的 `AGENTS.md`、`CLAUDE.md`、`GEMINI.md` 和 Cursor 规则文件。生成文件包含来源标记，不应手工编辑；正式内容应修改 `core/`、`workflows/` 或 `memory/`。

## Git 约定

- `main` 只接收已确认的规则、工作流和记忆。
- 新工作流使用 `feat/<name>` 分支；新记忆使用 `memory/<name>` 分支。
- 候选记忆先提交到 `inbox/`，确认后再移动到正式目录，并在提交说明中注明来源。
- 不把 API key、密码、生产连接串、客户个人数据或其他秘密写入仓库。
- 生产连接手册只保存流程、变量名、验证查询和安全边界；真实值留在受控秘密管理器中。
- 如果两个来源冲突，保留冲突记录并标记为 `pending_confirmation`，不要静默覆盖。

## 优先级

当前用户指令和平台安全约束优先于项目规则；项目规则优先于本仓库的共享规则；本仓库共享规则优先于 agent 的临时推断。
