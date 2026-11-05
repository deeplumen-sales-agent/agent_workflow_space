# Agent 适配层

不同 AI 平台的入口文件语法和自动加载位置不同。正式内容只在 `core/`、`workflows/`、`memory/` 和 `runbooks/` 维护；运行 `python scripts/build-adapters.py` 生成根目录入口文件。

当前生成入口：

- `AGENTS.md`：Codex 和支持 AGENTS 约定的 agent。
- `CLAUDE.md`：Claude Code。
- `GEMINI.md`：Gemini CLI。
- `.cursor/rules/00-shared-agent-workflow.mdc`：Cursor。

如果某个平台有额外的项目级规则，应在适配文件中引用共享内容，而不是复制后各自修改。
