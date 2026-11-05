# 记忆收件箱

这是各 agent 提交候选长期记忆的地方。文件名使用 `YYYY-MM-DD-agent-topic.md`，内容至少包含：

```yaml
status: candidate
source: 来源文件、任务或会议
updated: YYYY-MM-DD
scope: global | project:<name> | workflow:<name>
confidence: high | medium | low
```

候选内容必须说明事实、来源、适用范围和可能的冲突。确认后移动到 `memory/`，没有确认的内容不能作为共享规则使用。
