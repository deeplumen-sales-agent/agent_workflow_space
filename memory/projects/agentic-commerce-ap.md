---
status: confirmed
source: local workspace research and product decisions through 2026-10-26
updated: 2026-11-04
scope: project:agentic-commerce-ap
confidence: high
---

# Agentic Commerce / AP 项目记忆

## 稳定原则

- AP（Agentic Page）是面向 AI 入口的内容和页面适配能力，页面来源、输入契约、生成内容、发布状态和访问入口需要分别建模。
- 业务结论必须回到商品、集合、文章、首页等 SourceObject 的事实；没有来源的属性不能由模型补全。
- ProductVariant 属于 Product 的变体范围；Article 需要同时保留 Blog Collection 和 Article identity。
- App Proxy 是 SHOPLINE 一期支持的 AP 入口；原生 `/products/...` 接管不是自动成立的能力。
- 原生平台 sitemap 与 App Proxy AP sitemap 可以并存；robots/llms 根路径接管需要单独验证。
- CDN 已有的格式和尺寸收益不能直接算作 DeepLumen 的新增收益；批量图片替换需要稳定身份和恢复证据。

## 研究和需求边界

- Product、Collection、Article、Homepage 是通用 AP 重点对象。
- `SourceObject → SourceContract → InputContract` 是需求和实现之间的主要抽象链。
- Blog Generation 与已有 Blog Article → AP 是两条独立流程；SHOPLINE P0 选择已有 Blog Collection，不自动创建。
- 商家访谈中的兴趣、愿意测试、愿意付费和已同意行动必须分开记录，不能直接升级为产品决策。

## 时间敏感项

SHOPLINE 一期的具体路径、范围和原型状态以最新决策记录为准；本文件只保存稳定边界，不代表线上所有页面或配置已启用。
