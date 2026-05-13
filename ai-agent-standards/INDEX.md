# INDEX — AI Agent Coding Standards

**Find the file you need in this framework.**

---

## 🎯 By Role

### New Engineers

| File | Purpose | Priority |
|------|---------|----------|
| [`../karpathy/principles.md`](../karpathy/principles.md) | **4 Karpathy Principles (source of truth)** | ⭐⭐⭐ |
| [`../karpathy/examples.md`](../karpathy/examples.md) | **Anti-patterns & correct approaches** | ⭐⭐⭐ |
| [`onboarding/quick-reference.md`](onboarding/quick-reference.md) | 1-page cheat sheet (printable) | ⭐⭐⭐ |
| [`onboarding/karpathy-principles-guide.md`](onboarding/karpathy-principles-guide.md) | Detailed training (20-30 min) | ⭐⭐⭐ |
| [`onboarding/think-before-coding-worksheet.md`](onboarding/think-before-coding-worksheet.md) | Interactive exercise (30 min) | ⭐⭐ |
| [`onboarding/first-task-walkthrough.md`](onboarding/first-task-walkthrough.md) | Step-by-step first task guide | ⭐⭐⭐ |
| [`onboarding/common-mistakes.md`](onboarding/common-mistakes.md) | Common mistakes & how to avoid | ⭐⭐ |
| [`prompts/PROMPT-TEMPLATE.md`](prompts/PROMPT-TEMPLATE.md) | Standard prompt template | ⭐⭐ |

### Code Reviewer / QA

| File | Purpose | Priority |
|------|---------|----------|
| [`principles/karpathy-framework.md`](principles/karpathy-framework.md) | Reviewer checklist for 4 principles | ⭐⭐⭐ |
| [`quality-control/code-review-checklist.md`](quality-control/code-review-checklist.md) | Checklist with Karpathy validation | ⭐⭐⭐ |
| [`quality-control/audit-ai-code-full.md`](quality-control/audit-ai-code-full.md) | Detailed audit checklist | ⭐⭐⭐ |
| [`quality-control/hallucination-detection.md`](quality-control/hallucination-detection.md) | Detecting AI hallucinations | ⭐⭐ |
| [`reference/error-reference-complete.md`](reference/error-reference-complete.md) | Common AI error table | ⭐⭐ |

### Senior Engineer / Tech Lead

| File | Purpose | Priority |
|------|---------|----------|
| [`principles/karpathy-framework.md`](principles/karpathy-framework.md) | Master reference for all principles | ⭐⭐⭐ |
| [`reference/sync-karpathy-across-tools.md`](reference/sync-karpathy-across-tools.md) | Keeping Cursor/Claude/Copilot in sync | ⭐⭐⭐ |
| [`quality-control/`](quality-control/) | Full quality control pipeline | ⭐⭐⭐ |
| [`risk-management/escalation-workflow.md`](risk-management/escalation-workflow.md) | Handling uncooperative AI | ⭐⭐⭐ |
| [`risk-management/security-constraints.md`](risk-management/security-constraints.md) | Non-negotiable constraints | ⭐⭐⭐ |
| [`prompts/sample-use-cases/`](prompts/sample-use-cases/) | Prompt examples by use case | ⭐⭐⭐ |
| [`metrics/kpi-definitions.md`](metrics/kpi-definitions.md) | Detailed KPI definitions | ⭐⭐ |

### Manager / Product Owner

| File | Purpose | Priority |
|------|---------|----------|
| [`principles/karpathy-framework.md`](principles/karpathy-framework.md) | Understand core behavioral principles | ⭐⭐⭐ |
| [`reference/methodology-for-management.md`](reference/methodology-for-management.md) | Methodology explanation | ⭐⭐⭐ |
| [`metrics/kpi-definitions.md`](metrics/kpi-definitions.md) | Metrics & ROI tracking | ⭐⭐⭐ |
| [`metrics/sample-weekly-report.md`](metrics/sample-weekly-report.md) | Sample report | ⭐⭐ |
| [`risk-management/cost-control-policy.md`](risk-management/cost-control-policy.md) | AI cost control | ⭐⭐ |

---

## 📁 By Directory

### 📂 `karpathy/` — Karpathy Principles (Source of Truth)

> **Location:** `../karpathy/` (at repo root, not inside this folder)

| File | Content |
|------|---------|
| [`../karpathy/principles.md`](../karpathy/principles.md) | **SOURCE OF TRUTH**: 4 Principles — Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution |
| [`../karpathy/examples.md`](../karpathy/examples.md) | Real-world anti-patterns and correct approaches for each principle |

---

### 📂 `principles/` — Detailed Framework

| File | Content |
|------|---------|
| [`principles/karpathy-framework.md`](principles/karpathy-framework.md) | **MASTER REFERENCE**: 4 Principles with detailed explanation, integration with framework, reviewer checklist |

**Quick Learning Path:**
1. Read [`karpathy/principles.md`](../karpathy/principles.md) — 5 min
2. Read [`onboarding/karpathy-principles-guide.md`](onboarding/karpathy-principles-guide.md) — 20 min
3. Complete [`onboarding/think-before-coding-worksheet.md`](onboarding/think-before-coding-worksheet.md) — 30 min
4. Apply using [`quality-control/code-review-checklist.md`](quality-control/code-review-checklist.md)

---

### 📂 `prompts/` — Prompt Template Library

| File | Content |
|------|---------|
| [`prompts/README.md`](prompts/README.md) | Library usage guide |
| [`prompts/HEADER-TEMPLATE.yaml`](prompts/HEADER-TEMPLATE.yaml) | Standard YAML header for prompts |
| [`prompts/PROMPT-TEMPLATE.md`](prompts/PROMPT-TEMPLATE.md) | Prompt template (Context → Task → Constraints → Output) |
| [`prompts/claude-system-instructions.md`](prompts/claude-system-instructions.md) | System prompt for Claude with Karpathy principles |
| **Use Cases:** | |
| [`create-api-with-rate-limiting.md`](prompts/sample-use-cases/create-api-with-rate-limiting.md) | API endpoint + auth + rate limiting |
| [`refactor-cache-strategy.md`](prompts/sample-use-cases/refactor-cache-strategy.md) | Cache optimization & performance |
| [`generate-unit-tests.md`](prompts/sample-use-cases/generate-unit-tests.md) | Auto-generate unit tests |
| [`security-audit.md`](prompts/sample-use-cases/security-audit.md) | Security vulnerability check |
| [`database-migration.md`](prompts/sample-use-cases/database-migration.md) | Safe schema migration |
| [`indexed-by-category.md`](prompts/indexed-by-category.md) | Categorized prompt index |

---

### 📂 `templates/` — Reusable Templates

| File | Purpose |
|------|---------|
| [`templates/README.md`](templates/README.md) | Template guide |
| [`templates/project-cursorrules-template`](templates/project-cursorrules-template) | `.cursorrules` template for new projects |
| [`templates/project-structure-template.md`](templates/project-structure-template.md) | Optimal project structure suggestions |
| [`templates/task-description-template.md`](templates/task-description-template.md) | Task template for Jira/Trello |

---

### 📂 `quality-control/` — Quality Control Pipeline

| File | Content |
|------|---------|
| [`quality-control/README.md`](quality-control/README.md) | Pipeline overview |
| [`quality-control/code-review-checklist.md`](quality-control/code-review-checklist.md) | **Checklist with Karpathy validation [REQUIRED]** |
| [`quality-control/self-check-report-template.md`](quality-control/self-check-report-template.md) | Self-check report template with principle verification |
| [`quality-control/audit-ai-code-full.md`](quality-control/audit-ai-code-full.md) | Detailed audit checklist |
| [`quality-control/hallucination-detection.md`](quality-control/hallucination-detection.md) | Detecting & handling hallucinations |
| [`quality-control/ci-cd-gates.md`](quality-control/ci-cd-gates.md) | CI/CD integration rules |

---

### 📂 `risk-management/` — Risk Management

| File | Content |
|------|---------|
| [`risk-management/README.md`](risk-management/README.md) | Risk management overview |
| [`risk-management/security-constraints.md`](risk-management/security-constraints.md) | Non-negotiable constraints |
| [`risk-management/ai-failure-log-template.md`](risk-management/ai-failure-log-template.md) | AI failure log template |
| [`risk-management/escalation-workflow.md`](risk-management/escalation-workflow.md) | Escalation when AI won't cooperate |
| [`risk-management/cost-control-policy.md`](risk-management/cost-control-policy.md) | API cost control policy |
| [`risk-management/incident-response-plan.md`](risk-management/incident-response-plan.md) | Incident response plan |
| [`risk-management/mitigation-strategies.md`](risk-management/mitigation-strategies.md) | Risk mitigation strategies |

---

### 📂 `metrics/` — KPI Tracking & Performance

| File | Content |
|------|---------|
| [`metrics/README.md`](metrics/README.md) | Metrics setup guide |
| [`metrics/kpi-definitions.md`](metrics/kpi-definitions.md) | Detailed KPI definitions |
| [`metrics/tracking-template.csv`](metrics/tracking-template.csv) | CSV template for AI-assisted task logging |
| [`metrics/sample-weekly-report.md`](metrics/sample-weekly-report.md) | Sample weekly report |
| [`metrics/dashboard-guide.md`](metrics/dashboard-guide.md) | Dashboard setup guide |
| [`metrics/analysis-queries.sql`](metrics/analysis-queries.sql) | Sample SQL queries for metrics |

---

### 📂 `onboarding/` — Training & Guides

| File | Content |
|------|---------|
| [`onboarding/README.md`](onboarding/README.md) | Onboarding program overview |
| [`onboarding/quick-reference.md`](onboarding/quick-reference.md) | **1-page cheat sheet (printable)** ⭐ |
| [`onboarding/first-task-walkthrough.md`](onboarding/first-task-walkthrough.md) | Detailed first task walkthrough |
| [`onboarding/common-mistakes.md`](onboarding/common-mistakes.md) | Common mistakes & how to avoid |

---

### 📂 `multi-agent/` — Multi-Agent Framework (P2 Placeholder)

| File | Content |
|------|---------|
| [`multi-agent/README.md`](multi-agent/README.md) | Overview (P2) |
| [`multi-agent/roadmap.md`](multi-agent/roadmap.md) | Development roadmap |
| [`multi-agent/orchestration-design.md`](multi-agent/orchestration-design.md) | Preliminary orchestration design |

---

### 📂 `reference/` — Reference Documentation

| File | Content |
|------|---------|
| [`reference/README.md`](reference/README.md) | Reference directory guide |
| [`reference/error-reference-complete.md`](reference/error-reference-complete.md) | Common AI error table |
| [`reference/use-case-cookbook.md`](reference/use-case-cookbook.md) | Detailed use case examples |
| [`reference/methodology-for-management.md`](reference/methodology-for-management.md) | Methodology for managers |
| [`reference/glossary.md`](reference/glossary.md) | Terms & definitions |
| [`reference/external-links.md`](reference/external-links.md) | External documentation links |
| [`reference/sync-karpathy-across-tools.md`](reference/sync-karpathy-across-tools.md) | Keeping principles synced across AI tools |

---

## 🔗 Root Level Files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Claude Code auto-discovery instructions |
| `GEMINI.md` | Gemini Code Assist auto-discovery instructions |
| `COPILOT.md` | GitHub Copilot custom instructions |
| `.instructions.md` | VS Code Copilot system instructions |
| `.cursor/rules/karpathy-guidelines.mdc` | Cursor auto-discovery rules |
| `.cursorrules` | Cursor/Windsurf fallback rules |
| `INSTALL.md` | 1-step installation guide |
| `README.md` | Main readme & quick-start |
| `INDEX.md` | **This file** — master index |
| `CHANGELOG.md` | Version history & updates |
| `.gitignore` | Exclude sensitive files |

---

## 🎯 Quick Navigation

### "I want to..."

| Need | Go to |
|------|-------|
| Get started quickly | [`../README.md`](../README.md) + [`onboarding/quick-reference.md`](onboarding/quick-reference.md) |
| Review AI code | [`quality-control/code-review-checklist.md`](quality-control/code-review-checklist.md) |
| Write prompts | [`prompts/PROMPT-TEMPLATE.md`](prompts/PROMPT-TEMPLATE.md) + [`prompts/sample-use-cases/`](prompts/sample-use-cases/) |
| Handle AI errors | [`risk-management/escalation-workflow.md`](risk-management/escalation-workflow.md) |
| Track metrics | [`metrics/tracking-template.csv`](metrics/tracking-template.csv) |
| Report to management | [`metrics/sample-weekly-report.md`](metrics/sample-weekly-report.md) |
| Find error solutions | [`reference/error-reference-complete.md`](reference/error-reference-complete.md) |
| Understand methodology | [`reference/methodology-for-management.md`](reference/methodology-for-management.md) |
| Verify AI loaded skills | Ask: "What coding standards are you following?" or `/standards` |

---

## 📊 File Statistics

| Type | Count |
|------|-------|
| Main directories | 9 (including karpathy/) |
| Guide files (README) | 9 |
| Sample prompts | 5 |
| Checklists & templates | 8+ |
| Reference documents | 7 |
| AI auto-discovery files | 6 |
| **Total** | **45+** |

---

## ✅ Setup Validation Checklist

When setting up a new project:
- [ ] All directories copied to project root
- [ ] `.cursorrules` updated for your tech stack
- [ ] `.gitignore` excludes secrets
- [ ] `README.md` & `INDEX.md` accessible
- [ ] Team reviewed `onboarding/quick-reference.md`
- [ ] Verification prompt tested: `/standards` returns expected response
- [ ] Metrics tracking set up

---

## 🔄 Version Info

- **Framework Version:** 1.1.0
- **Last Updated:** 2026-05-13
- **Status:** ✓ Production Ready

---

**Looking for something? Use Ctrl+F or browse the tables above.**

**New here? Start with [`karpathy/principles.md`](../karpathy/principles.md) 👉**
