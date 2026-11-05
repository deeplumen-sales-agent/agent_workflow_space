# Agent Workflow Space 设计

## 目标

建立一个由 Git 管理的共享仓库，让不同 AI agent 读取同一套基础规则、工作流和已确认记忆，同时保留各平台入口差异和候选记忆审核边界。

## 架构

- `core/` 是共享规则的唯一来源。
- `workflows/` 保存可复用的、与平台无关的工作方法和模板。
- `memory/` 保存已确认的长期信息；`inbox/` 保存待确认候选。
- `adapters/` 和根目录生成文件把共享内容映射到不同 AI 的加载入口。
- Git 分支和 GitHub Actions 提供变更记录与基础校验。

## 数据流

```text
agent 输出候选内容 → inbox/ → 人工确认与去重 → memory/ 或 workflows/ → 生成 adapters → 各 agent 读取
```

正式内容不会从多个 agent 自动双向覆盖。冲突保留证据并标记 `pending_confirmation`。

## 边界

- 当前会话上下文、平台隐藏记忆、权限和工具状态不进入共享仓库。
- 密钥、密码、生产连接串和未脱敏个人数据禁止进入 Git。
- 用户当前指令、平台安全约束和项目规则优先于共享规则。

## 验证

- `scripts/validate.py` 检查必需目录、生成标记、敏感内容和占位词。
- GitHub Actions 在 push 和 pull request 时运行同一校验。
