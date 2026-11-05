# 记忆政策

## 记忆层级

1. **临时上下文**：当前对话中的推理、草稿和工具输出，只属于当前任务。
2. **候选记忆**：写入 `inbox/`，有来源但尚未确认。
3. **正式记忆**：写入 `memory/`，经过人工确认，可被其他 agent 默认读取。
4. **废弃记忆**：保留原文件并标记 `deprecated`，说明替代内容和日期。

## 晋级条件

一条内容进入正式记忆前，必须能回答：

- 它描述的事实或决策是什么？
- 来源是什么，观察时间是什么？
- 适用范围是什么？
- 当前状态是什么？
- 如果它失效，替代内容在哪里？

## Front matter

正式记忆和候选记忆使用以下字段：

```yaml
status: candidate | confirmed | pending_confirmation | deprecated
source: 来源文件、任务或会议
updated: YYYY-MM-DD
scope: global | project:<name> | workflow:<name>
confidence: high | medium | low
```

没有这些字段的内容只能作为说明文档，不能自动作为长期记忆。
