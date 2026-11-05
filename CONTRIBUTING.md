# 贡献规则

## 修改正式规则或工作流

1. 从 `main` 创建分支。
2. 只修改对应的 `core/`、`workflows/` 或 `memory/` 文件。
3. 运行 `python scripts/build-adapters.py` 和 `python scripts/validate.py`。
4. 检查生成的适配文件是否只反映正式内容。
5. 提交时写清楚变化、原因、来源和验证结果。

## 提交候选记忆

候选记忆放入 `inbox/`，文件名使用 `YYYY-MM-DD-agent-topic.md`。每条候选记忆都要写明来源、范围、状态和置信度。未经人工确认的内容只能作为候选，不能直接成为共享规则。

## 记忆晋级

确认后将内容移动到 `memory/decisions/` 或 `memory/projects/`，保留来源和确认日期；失效内容标记为 `deprecated`，不要直接删除历史记录。
