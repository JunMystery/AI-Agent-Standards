# AI Agent Coding Standards

**Version:** 1.3.0 | **Release:** 2026-05-13 | **Language:** English

A **zero-config, drop-in framework** that makes AI coding agents (Claude, Gemini, Copilot, Cursor, Windsurf) follow disciplined coding practices based on the **Karpathy Principles**. Includes CI/CD quality gates, PR audit checklists, and multi-agent orchestration support.

> **Core philosophy:** AI is a tool, not a decision-maker. Engineers retain authority over architecture, security, and production decisions.

---

## 🚀 Quick Start

### 1. Install (1 step)

Copy this repo's contents into your project root. See [INSTALL.md](./INSTALL.md) for details.

### 2. Verify

Ask your AI agent:

> **"What coding standards are you following?"**

Expected response:

> ✅ **AI-Agent-Coding Standards v1.3** with Karpathy Principles active.

### 3. Use Skills

See [SKILL-REFERENCE.md](./SKILL-REFERENCE.md) — quick lookup for which files to `@reference` based on your task type.

---

## 🎯 The 4 Karpathy Principles

The behavioral foundation for all AI-assisted coding, derived from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876):

| # | Principle | Core Rule | Prevents |
|---|-----------|-----------|----------|
| 1 | **Think Before Coding** | Surface assumptions, present alternatives, ask when confused | Coding the wrong solution |
| 2 | **Simplicity First** | Minimum code, no speculative features | Over-engineering, bloat |
| 3 | **Surgical Changes** | Touch only what you must, match existing style | Scope creep, drive-by refactors |
| 4 | **Goal-Driven Execution** | Define verifiable success criteria | Ambiguous outcomes, wasted iterations |

**Learn more:**
- [karpathy/principles.md](./karpathy/principles.md) — Source of truth (5 min read)
- [karpathy/examples.md](./karpathy/examples.md) — Anti-patterns & correct approaches (10 min read)

---

## 🤖 AI Tool Support Matrix

| Tool | Instruction File | Auto-detected? |
|------|-----------------|----------------|
| **Claude Code** | [`CLAUDE.md`](./CLAUDE.md) | ✅ |
| **Gemini Code Assist / CLI** | [`GEMINI.md`](./GEMINI.md) | ✅ |
| **GitHub Copilot** | [`COPILOT.md`](./COPILOT.md) | ✅ |
| **VS Code Copilot** | [`.instructions.md`](./.instructions.md) | ✅ |
| **Cursor** | [`.cursor/rules/karpathy-guidelines.mdc`](./.cursor/rules/karpathy-guidelines.mdc) | ✅ |
| **Windsurf** | [`.cursorrules`](./.cursorrules) | ✅ |

Each file contains the 4 Karpathy Principles, role definitions, and a **verification prompt** so you can confirm the agent loaded the correct skills.

---

## 📁 Repository Structure

```
AI-Agent-Coding/
│
│ ── AUTO-DISCOVERY FILES (AI agents read these) ──
├── CLAUDE.md                    → Claude Code
├── GEMINI.md                    → Gemini Code Assist
├── COPILOT.md                   → GitHub Copilot
├── .instructions.md             → VS Code Copilot
├── .cursor/rules/               → Cursor
├── .cursorrules                 → Cursor/Windsurf fallback
│
│ ── KARPATHY PRINCIPLES (source of truth) ──
├── karpathy/
│   ├── principles.md            → The 4 principles
│   └── examples.md              → Anti-patterns & correct approaches
│
│ ── FRAMEWORK DOCUMENTATION ──
├── ai-agent-standards/
│   ├── INDEX.md                 → Complete file index
│   ├── CHANGELOG.md             → Version history
│   ├── onboarding/              → Training & quick reference
│   ├── prompts/                 → Prompt templates & 7 sample use cases
│   ├── quality-control/         → Review checklists, audit (11 sections)
│   ├── risk-management/         → 12 security constraints (v2.0)
│   ├── reference/               → Glossary, error reference
│   └── multi-agent/             → 4 Agents: Coder, Test, Reviewer, Docs
│
│ ── CI/CD AUTOMATION ──
├── .github/
│   ├── pull_request_template.md → Systematic Audit Checklist for PRs
│   └── workflows/
│       └── ai-code-audit.yml    → SAST quality gate (SonarCloud + 12-constraint scan)
│
│ ── AUTOMATION SCRIPTS ──
├── scripts/
│   └── security-audit.sh        → Local security scan (all 12 constraints)
│
│ ── ROOT FILES ──
├── SKILL-REFERENCE.md           → Quick lookup: which files to @reference
├── SKILL-REFERENCE_VI.md        → Same, Vietnamese with explanations
├── INSTALL.md                   → Installation guide (1 step)
├── README.md                    → This file
└── Development_doc_VI.md        → Original methodology (Vietnamese)
```

---

## 📋 Key Files by Role

### For New Engineers
| File | Purpose | Time |
|------|---------|------|
| [karpathy/principles.md](./karpathy/principles.md) | Core principles | 5 min |
| [karpathy/examples.md](./karpathy/examples.md) | Learn by example | 10 min |
| [ai-agent-standards/onboarding/quick-reference.md](./ai-agent-standards/onboarding/quick-reference.md) | Cheat sheet | 5 min |
| [ai-agent-standards/onboarding/first-task-walkthrough.md](./ai-agent-standards/onboarding/first-task-walkthrough.md) | Guided first task | 15 min |

### For Code Reviewers
| File | Purpose |
|------|---------|
| [ai-agent-standards/quality-control/code-review-checklist.md](./ai-agent-standards/quality-control/code-review-checklist.md) | Review checklist with Karpathy validation |
| [ai-agent-standards/quality-control/audit-ai-code-full.md](./ai-agent-standards/quality-control/audit-ai-code-full.md) | Full audit checklist |

### For Prompt Engineering
| File | Purpose |
|------|---------|
| [ai-agent-standards/prompts/PROMPT-TEMPLATE.md](./ai-agent-standards/prompts/PROMPT-TEMPLATE.md) | Standard prompt structure |
| [ai-agent-standards/prompts/sample-use-cases/](./ai-agent-standards/prompts/sample-use-cases/) | Real-world prompt examples |

### For Security & Risk
| File | Purpose |
|------|---------|
| [risk-management/security-constraints.md](./ai-agent-standards/risk-management/security-constraints.md) | 6 non-negotiable security rules |
| [risk-management/escalation-workflow.md](./ai-agent-standards/risk-management/escalation-workflow.md) | When & how to escalate AI failures |
| [.github/pull_request_template.md](./.github/pull_request_template.md) | PR audit checklist (Zero-Trust, Two-Pair Eyes) |
| [.github/workflows/ai-code-audit.yml](./.github/workflows/ai-code-audit.yml) | Automated SAST quality gate |

### For Multi-Agent Setup
| File | Purpose |
|------|---------|
| [multi-agent/coder-agent.md](./ai-agent-standards/multi-agent/coder-agent.md) | Coder Agent — implementation only, no DB/env changes |
| [multi-agent/test-agent.md](./ai-agent-standards/multi-agent/test-agent.md) | Test Agent — writes tests independently, no production code changes |
| [multi-agent/reviewer-agent.md](./ai-agent-standards/multi-agent/reviewer-agent.md) | Reviewer Agent — security audit & optimization, no new features |
| [multi-agent/documentation-agent.md](./ai-agent-standards/multi-agent/documentation-agent.md) | Documentation Agent — API docs, READMEs, changelogs |

---

## 🔄 The 7-Step Pipeline

```
1. ANALYZE & DECOMPOSE
   ✓ Apply Principle #1 (Think Before Coding)
   ↓
2. DATA DESIGN (Engineer decides)
   ↓
3. ENFORCE ARCHITECTURE CONSTRAINTS
   ↓
4. BOTTOM-UP DEVELOPMENT (Core → Services → UI)
   ✓ Apply Principle #2 (Simplicity), #3 (Surgical)
   ↓
5. QUALITY CONTROL PIPELINE
   - AI Generate → Self-Check → Self-Fix → Output
   ✓ All 4 Principles verified in Self-Check Report
   ↓
6. HUMAN GATE — Engineer Review 👤
   ✓ Apply Principle #4 (Goal-Driven Execution)
   [APPROVE] → Merge + Checkpoint Backup
   [REJECT] → Iterate
   ↓
7. AUTO-DOCUMENT (API specs, README updates)
```


## 📝 Attribution

- **Methodology:** JunMystery — [Development_doc_VI.md](./Development_doc_VI.md)
- **Karpathy Principles:** Based on [Andrej Karpathy's post](https://x.com/karpathy/status/2015883857489522876), adapted from [andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) by [@forrestchang](https://github.com/forrestchang) (MIT License)
- **Status:** ✓ Open framework — use & extend freely

---

## Full Index

👉 [ai-agent-standards/INDEX.md](./ai-agent-standards/INDEX.md) — Complete file-by-file reference
