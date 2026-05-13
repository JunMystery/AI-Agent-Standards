# CHANGELOG — AI Agent Coding Standards

Track versions and updates for the AI Agent Coding Standards framework.

## [1.2.0] - 2026-05-13

### Added (P0 — Prompt Engineering Cookbook)
- **`prompts/sample-use-cases/rag-implementation-cookbook.md`** — RAG pipeline prompt for safe medical data retrieval (PROMPT-006)
- **RAG / AI Pipeline** category in `prompts/indexed-by-category.md`

### Added (P0 — Systematic Code Audit)
- **`.github/pull_request_template.md`** — PR audit checklist with Zero-Trust, Simplicity, Two-Pair Eyes sections
- **`.github/workflows/ai-code-audit.yml`** — Automated SAST quality gate (SonarCloud + dependency scan)
- **Section 10: RAG Pipeline Audit** in `audit-ai-code-full.md` (retrieval quality, source grounding, fallback)
- **Section 11: AI Output Safety Audit** in `audit-ai-code-full.md` (hallucination prevention, domain safety)

### Added (P2 — Multi-Agent Orchestration)
- **`multi-agent/coder-agent.md`** — Coder Agent system instructions (implementation only, no DB/env changes)
- **`multi-agent/reviewer-agent.md`** — Reviewer Agent system instructions (audit & optimize, no new features)

### Changed
- **`README.md`** — Updated to v1.2.0 with CI/CD, multi-agent, and expanded key files sections
- **`Development_doc_VI.md`** — Roadmap updated with P0/P2 completion status and deliverable links

---

## [1.1.0] - 2026-05-13

### Added
- **Karpathy Skills Integration:** Merged content from [andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) into the core framework
- **`karpathy/` module:** Single source of truth for the 4 Karpathy Principles
  - `karpathy/principles.md` — The 4 principles (source of truth)
  - `karpathy/examples.md` — Real-world anti-patterns and correct approaches
- **Auto-discovery instruction files** for all major AI tools:
  - `CLAUDE.md` — Claude Code
  - `GEMINI.md` — Gemini Code Assist / CLI
  - `COPILOT.md` — GitHub Copilot
  - `.instructions.md` — VS Code Copilot (rewritten in English)
  - `.cursor/rules/karpathy-guidelines.mdc` — Cursor
  - `.cursorrules` — Cursor/Windsurf fallback
- **Verification Prompt:** Each instruction file includes a verification block — users can ask `/standards` to confirm the AI loaded the correct skills
- **`INSTALL.md`** — 1-step installation guide with verification instructions
- **Root `.gitignore`** — Moved from `.ai-agent-standards/`

### Changed
- **Renamed `.ai-agent-standards/` → `ai-agent-standards/`** — Removed dot prefix for visibility across all OS/tools
- **`README.md`** — Rewritten in English with AI Tool Support Matrix and simplified Quick Start
- **All instruction files** — Converted to 100% English

### Removed
- **`andrej-karpathy-skills/`** — Deleted after content was integrated into the main framework
- **`.ai-agent-standards/.cursor/`** — Moved to root `.cursor/`
- **`.ai-agent-standards/.cursorrules`** — Merged into root `.cursorrules`
- **`.ai-agent-standards/.gitignore`** — Moved to root `.gitignore`

---

## [1.0.0] - 2026-05-12

### Added
- **Initial Release:** Complete framework built from the original methodology document
- **8 functional domains:**
  - `prompts/` — Standard prompt template library
  - `quality-control/` — Quality control pipeline
  - `risk-management/` — Risk management & escalation
  - `metrics/` — KPI tracking & performance
  - `onboarding/` — Training & onboarding materials
  - `multi-agent/` — Placeholder for P2 roadmap
  - `reference/` — Reference documentation & error tables
  - `templates/` — Reusable templates for new projects

- **Core Files:**
  - `.cursorrules` — Default Cursor/Windsurf rules
  - `README.md` — Quick-start guide
  - `INDEX.md` — Master file index
  - `CHANGELOG.md` — This file

- **Sample Prompts (5 use cases):**
  - API with rate limiting
  - Cache strategy refactor
  - Unit test generation
  - Security audit
  - Database migration

---

## Update Log

| Version | Date | Changes | Status |
|---------|------|---------|--------|
| 1.2.0 | 2026-05-13 | P0 Cookbook + Audit, CI/CD pipeline, Multi-Agent orchestration | ✓ Released |
| 1.1.0 | 2026-05-13 | Karpathy Skills Integration, English conversion, auto-discovery files | ✓ Released |
| 1.0.0 | 2026-05-12 | Initial release | ✓ Released |

---

## How to Update

When making changes:
1. Add a new entry at the top (after the CHANGELOG header)
2. Specify: Version, Date, Changes, Status
3. Commit to Git alongside source code changes
4. Update version in `README.md` for official releases

**Version Format:** Major.Minor.Patch (e.g., 1.0.0 → 1.0.1 → 1.1.0 → 2.0.0)
