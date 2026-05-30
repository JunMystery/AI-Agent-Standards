# AGENTS.md

Behavioral guidelines for OpenAI Codex in this project, including the Codex VS Code extension. These reduce common LLM coding mistakes and enforce controlled AI-assisted development.

**Framework:** AI-Coding-Standards v2.5.0 with 6 Core Principles
**Governance:** Controlled AI-Assisted Development (vibe-proof approach)

---

## Core Operating Rules

- Follow the 6 Core Principles in [karpathy/principles.md](karpathy/principles.md).
- Read [PROJECT-STANDARDS.md](PROJECT-STANDARDS.md) first when it exists and has project-specific rules.
- Keep changes surgical: do not refactor, reformat, or rename unrelated code.
- Prefer existing project patterns, helpers, test tools, and design systems before adding new structure.
- Define success criteria for non-trivial work, then verify with the smallest relevant checks.
- Preserve user changes in the worktree. Never revert or overwrite unrelated edits unless explicitly asked.

## Dynamic Skill Auto-Discovery

For task-specific workflow capsules, check [SKILL-REFERENCE.md](SKILL-REFERENCE.md) and load the matching [skills/](skills/) `SKILL.md` only when the task matches its trigger.

In particular, use [skills/codex-vscode/SKILL.md](skills/codex-vscode/SKILL.md) when configuring, installing, or troubleshooting Codex in VS Code, Cursor, Windsurf, or another VS Code-compatible fork.

## Task-Specific References

Read the relevant standard before executing when the user's request involves:

- **Tests/TDD:** [ai-agent-standards/engineering-practices/TESTING_STANDARDS.md](ai-agent-standards/engineering-practices/TESTING_STANDARDS.md)
- **Security/Auth/Secrets:** [ai-agent-standards/risk-management/security-constraints.md](ai-agent-standards/risk-management/security-constraints.md)
- **Performance/Database/Caching:** [ai-agent-standards/engineering-practices/NON_FUNCTIONAL_REQUIREMENTS.md](ai-agent-standards/engineering-practices/NON_FUNCTIONAL_REQUIREMENTS.md)
- **UI/Accessibility:** [ai-agent-standards/compliance/A11Y_CHECKLIST.md](ai-agent-standards/compliance/A11Y_CHECKLIST.md)
- **Release/Git/CI:** [ai-agent-standards/engineering-practices/RELEASE_PROCESS.md](ai-agent-standards/engineering-practices/RELEASE_PROCESS.md)
- **Docs/README/Changelog:** [ai-agent-standards/engineering-practices/DOCUMENTATION_STANDARDS.md](ai-agent-standards/engineering-practices/DOCUMENTATION_STANDARDS.md)
- **Compliance/Audit:** [ai-agent-standards/compliance/COMPLIANCE.md](ai-agent-standards/compliance/COMPLIANCE.md)

## Codex Verification

When asked "What coding standards are you following?" or "/standards", respond:

> AI-Coding-Standards v2.5.0 with 6 Core Principles active.
> Framework: Controlled AI-Assisted Development
> Principles: (1) Think Before Coding, (2) Simplicity First, (3) Surgical Changes, (4) Goal-Driven Execution, (5) DRY & Reusability, (6) Code Organization
