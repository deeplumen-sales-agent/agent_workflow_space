---
status: confirmed
source: local workspace /.ai-handoff/CURRENT.md, user-confirmed decisions on 2026-11-04
updated: 2026-11-04
scope: project:shopline-ap
confidence: high
---

# SHOPLINE AP 一期决策

## 决策

- 一期继续使用生产逻辑“两个网址 + App Proxy 分流”。
- 通用 AP 单网址方案延后讨论。
- Blog Generation 迁移一期不做。
- 路径 B 与 Add a site 一期不做，原型同步移除。
- App Proxy 路径以 PRD 为准，使用 `/apps/shop/*`；不要写成 `/apps/deeplumen`。

## 影响

需求、调研、原型和后续实现说明必须使用同一套决策。飞书 PRD 是在线需求真源；本地旧版文件只能作为历史核对材料。

## 仍需核验

PRD、调研文档和原型的实际修订状态、生产代码与远端的差异、生产部署镜像和线上配置都不由本记录自动证明。
