---
status: confirmed
source: 2026-11-04 user-confirmed SHOPLINE phase-one decisions in local handoff
updated: 2026-11-04
scope: project:shopline-ap
confidence: high
---

# SHOPLINE 通用 AP 一期记忆

## 已确认决策

1. 一期维持生产逻辑“两个网址 + App Proxy 分流”；通用 AP 单网址方案后续再议。
2. Blog Generation（Generation 迁移）一期不做。
3. 路径 B 与 Add a site 一期不做，原型同步去掉。
4. 代理路径以 PRD 为准：`/apps/shop/*`，不是 `/apps/deeplumen`。

## 交接边界

- 飞书 PRD 是当前在线需求真源；本地旧版 Markdown 只能作为核对材料。
- 生产代码落后远端的提交数、生产部署镜像、生产配置和线上覆盖量必须重新核验，不能由本文件推断。
- 这份记忆记录的是用户确认的产品决策，不代表修订后的 PRD、调研文档或原型已经全部完成。
