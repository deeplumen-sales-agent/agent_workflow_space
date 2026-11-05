# Agent Workflow Space Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 建立一个 Git 管理的跨 AI 共享规则、工作流和长期记忆仓库。

**Architecture:** 以 `core/`、`workflows/`、`memory/` 和 `inbox/` 作为平台无关的正式来源，以根目录入口文件和 Cursor 规则作为适配层；脚本生成适配文件并执行无依赖校验。

**Tech Stack:** Markdown、Python 3 标准库、GitHub Actions。

**Spec:** `docs/superpowers/specs/2026-11-04-agent-workflow-space-design.md`

## Global Constraints

- 正式内容只在 `core/`、`workflows/` 和 `memory/` 维护。
- 候选记忆先进入 `inbox/`，确认后才进入正式记忆。
- 密钥、密码、生产连接串和未脱敏个人数据禁止进入 Git。
- 用户当前指令、平台安全约束和项目规则优先于共享规则。

---

### Task 1: 建立共享目录和规则

**Files:**
- Create: `core/working-principles.md`
- Create: `core/memory-policy.md`
- Create: `core/evidence-status.md`
- Create: `core/glossary.md`
- Create: `workflows/prd-writing/workflow.md`
- Create: `workflows/prd-writing/template.md`
- Create: `workflows/prd-writing/checklist.md`

- [ ] **Step 1:** 写入基础规则、记忆生命周期、证据状态和 PRD 工作流。
- [ ] **Step 2:** 检查每条规则都有明确范围和状态表达。

### Task 2: 建立记忆审核边界

**Files:**
- Create: `memory/README.md`
- Create: `memory/decisions/README.md`
- Create: `memory/projects/README.md`
- Create: `inbox/README.md`

- [ ] **Step 1:** 写入候选记忆的 front matter 和晋级规则。
- [ ] **Step 2:** 确认正式记忆与临时上下文分层。

### Task 3: 建立平台适配和自动校验

**Files:**
- Create: `adapters/README.md`
- Create: `scripts/build-adapters.py`
- Create: `scripts/validate.py`
- Create: `.github/workflows/validate.yml`
- Create: `.gitignore`

- [ ] **Step 1:** 编写无依赖的适配文件生成脚本。
- [ ] **Step 2:** 编写目录、敏感内容和生成标记校验脚本。
- [ ] **Step 3:** 配置 GitHub Actions 在 push 和 pull request 时运行校验。

### Task 4: 验证和提交

**Files:**
- Modify: `README.md`
- Create: `CONTRIBUTING.md`

- [ ] **Step 1:** 运行 `python scripts/build-adapters.py`。
- [ ] **Step 2:** 运行 `python scripts/validate.py`。
- [ ] **Step 3:** 检查 `git diff --check` 和生成文件内容。
- [ ] **Step 4:** 提交并推送到远端分支。
