---
status: confirmed
source: merchant-facing AI Sales Commission rules and production read-only validation through 2026-10-26
updated: 2026-11-04
scope: project:ai-sales-commission
confidence: medium
---

# AI Sales Commission 记忆

## 文档口径

- 商家-facing 说明需要分别解释费用、COD、shipping protection、账单周期和退款影响。
- 费率、最低收费、资格条件、账单日期和退款计算不能从旧文档或代码快照直接推断为当前生产规则。
- 生产只读核验、代码实现、商家规则、账单生成和实际付款是不同证据层。

## 维护规则

任何数字费率、币种、账期、退款扣除或生产激活状态进入正式记忆前，都必须补充当前来源、验证时间和适用店铺范围。没有这些信息时使用 `pending_confirmation` 或 `unverified`。
