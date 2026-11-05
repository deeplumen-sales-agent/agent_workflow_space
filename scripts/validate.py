#!/usr/bin/env python3
"""Run dependency-free repository checks."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "CONTRIBUTING.md",
    "core/working-principles.md",
    "core/memory-policy.md",
    "core/evidence-status.md",
    "workflows/prd-writing/workflow.md",
    "workflows/prd-writing/template.md",
    "workflows/prd-writing/checklist.md",
    "memory/README.md",
    "memory/decisions/README.md",
    "memory/projects/README.md",
    "inbox/README.md",
    "runbooks/production/database-readonly.md",
    "workflows/production-readonly-audit/workflow.md",
    "workflows/agent-handoff/workflow.md",
    "memory/projects/agentic-commerce-ap.md",
    "memory/projects/shopline-ap.md",
    "memory/projects/cps-billing.md",
    "memory/projects/ai-sales-commission.md",
    "memory/projects/ac-radar.md",
    "memory/projects/wuxian-as-cooperation.md",
    "memory/decisions/2026-11-04-shopline-ap-phase-one.md",
    "scripts/build-adapters.py",
    "scripts/validate.py",
    ".github/workflows/validate.yml",
]
GENERATED = [
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    ".cursor/rules/00-shared-agent-workflow.mdc",
]
SENSITIVE = [
    re.compile(r"gh[pousr]_[A-Za-z0-9_\-]{20,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"postgres(?:ql)?://[^<\s]+:[^<\s]+@"),
    re.compile(r"-----BEGIN (?:RSA|OPENSSH|EC|DSA|PRIVATE) KEY-----"),
]
PLACEHOLDER = re.compile(r"\b(?:TODO|TBD)\b")


def text_files():
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() in {".md", ".py", ".yml", ".yaml", ".mdc", ".txt"}:
            yield path


def main() -> int:
    errors = []

    for relative in REQUIRED + GENERATED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    for relative in GENERATED:
        path = ROOT / relative
        if path.is_file() and "GENERATED FILE" not in path.read_text(encoding="utf-8"):
            errors.append(f"generated marker missing: {relative}")

    for path in text_files():
        content = path.read_text(encoding="utf-8")
        for pattern in SENSITIVE:
            if pattern.search(content):
                errors.append(f"possible secret in: {path.relative_to(ROOT)}")
        if PLACEHOLDER.search(content) and path.name not in {"validate.py"}:
            errors.append(f"placeholder word found in: {path.relative_to(ROOT)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
