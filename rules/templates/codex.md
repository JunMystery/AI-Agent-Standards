# AGENTS.md

Behavioral guidelines for OpenAI Codex in this project, including the Codex VS Code extension. These reduce common LLM coding mistakes and enforce controlled AI-assisted development.

{{generated_notice}}

**Framework:** AI-Coding-Standards v2.6.1 with 6 Core Principles
**Governance:** Controlled AI-Assisted Development (vibe-proof approach)

---

## Core Operating Rules

- Follow the 6 Core Principles in [karpathy/principles.md](karpathy/principles.md).
- Read [PROJECT-STANDARDS.md](PROJECT-STANDARDS.md) first when it exists and has project-specific rules.
- Keep changes surgical: do not refactor, reformat, or rename unrelated code.
- Prefer existing project patterns, helpers, test tools, and design systems before adding new structure.
- Define success criteria for non-trivial work, then verify with the smallest relevant checks.
- Preserve user changes in the worktree. Never revert or overwrite unrelated edits unless explicitly asked.

{{task_references}}

## Codex Verification

{{verification}}
