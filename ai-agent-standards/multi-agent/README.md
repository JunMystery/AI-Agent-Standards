# Multi-Agent Framework

**Status:** ✅ Implemented (v1.3.0)  
**Framework:** AI-Agent-Coding Standards v1.3 with Karpathy Principles

---

## Architecture

4 specialized agents with strict role isolation. Human engineer retains final authority.

```
Coder Agent → Test Agent → Reviewer Agent → Human Engineer
                                                   ↓
                                         Documentation Agent
```

---

## Agents

| Agent | File | Scope | Forbidden |
|-------|------|-------|-----------|
| **Coder** | [coder-agent.md](./coder-agent.md) | Write implementation code | DB schemas, env vars, architecture decisions |
| **Test** | [test-agent.md](./test-agent.md) | Write tests independently | Modify production code |
| **Reviewer** | [reviewer-agent.md](./reviewer-agent.md) | Security audit & optimize | Add new features, change business logic |
| **Documentation** | [documentation-agent.md](./documentation-agent.md) | API docs, READMEs, changelogs | Modify source code or tests |

---

## How to Use

### Single-Agent (default)
No setup needed. Your AI agent loads rules from the root instruction file (`CLAUDE.md`, `GEMINI.md`, etc.) automatically.

### Multi-Agent
Assign the appropriate file as system instructions for each agent in your orchestration tool:

```
Agent A → load coder-agent.md as system prompt
Agent B → load test-agent.md as system prompt
Agent C → load reviewer-agent.md as system prompt
Agent D → load documentation-agent.md as system prompt
```

Works with: Claude API, OpenAI API, LangChain, CrewAI, or any tool that accepts custom system prompts.

---

## Key Rules (All Agents)

1. **Human engineer has final authority** — no agent can override
2. **Karpathy Principles enforced** — Think, Simplicity, Surgical, Goal-Driven
3. **12 security constraints active** — see [security-constraints.md](../risk-management/security-constraints.md)
4. **Self-Check report required** — every agent output includes verification

---

## Reference

- [SKILL-REFERENCE.md](../../SKILL-REFERENCE.md) — Quick lookup for all skills
- [security-constraints.md](../risk-management/security-constraints.md) — 12 non-negotiable security rules
- [karpathy/principles.md](../../karpathy/principles.md) — The 4 principles
