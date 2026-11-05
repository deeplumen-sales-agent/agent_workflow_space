# Agent 交接工作流

## 目标

让另一个 agent 在没有完整聊天历史的情况下，能够安全地继续工作。

## 交接内容

交接文件至少包含：

```text
# Current Task
owner:
updated_at:
status:

## Goal

## Last Completed

## In Progress

## Next

## Decisions

## Changed Files

## Verification

## Risks
```

## 写作规则

- `Last Completed` 只写有证据的完成动作。
- `In Progress` 和 `Next` 要区分当前正在做什么与下一步计划。
- `Decisions` 写明日期、确认人或来源；没有确认的内容标记 `pending_confirmation`。
- `Verification` 区分代码测试、只读观察、业务确认和未执行项目。
- `Risks` 写时间敏感、权限缺口、生产配置、外部系统和数据准确性风险。
- 不把交接文件当作秘密存储，也不粘贴密码、Token、连接串或未脱敏个人数据。
