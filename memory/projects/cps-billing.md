---
status: confirmed
source: CPS/AP billing research and production read-only audit working rules through 2026-10-23
updated: 2026-11-04
scope: project:cps-billing
confidence: high
---

# CPS / AP 计费与对账记忆

## 业务链路拆分

订单事实、归因、资格、hold/release、ledger、provider acceptance、invoice/payment、refund/adjustment 必须分开记录。一个阶段的证据不能自动替代另一个阶段的证据。

## 结论口径

- HTTP 202、usage matching、代码测试通过或数据字段存在，都不能直接证明提供方已经收款、发票已支付或商家账务已结清。
- 退款和调整需要保留原订单、原归因、原计费记录、调整原因和最终账务状态。
- 费率、计佣基数、账期、豁免和 provider 规则属于时间敏感配置，写入正式记忆前必须标注来源和验证日期。
- 生产只读核查可以证明观察到的事实，不能替代业务签字或外部提供方确认。

## 数据边界

CPS 相关表、事件、快照、工作项和对账结果应按用途区分。集成测试必须使用隔离测试库，不得把带写入的测试套件指向生产。
