# Skill Reference — Quick Lookup

**Which files to reference for each type of task.**

Copy the `@file` references into your prompt to activate the relevant skills.

---

## Everyday Coding (no extra reference needed)

Your AI agent **already loaded** the 4 Karpathy Principles from the root instruction file (`CLAUDE.md`, `GEMINI.md`, etc.). Just describe your task normally.

---

## By Task Type

### Security-Sensitive Code
> Auth, payments, encryption, user data, API keys

```
@ai-agent-standards/risk-management/security-constraints.md
```

### RAG / AI Pipeline
> Vector DB retrieval, LLM generation, embeddings

```
@ai-agent-standards/prompts/sample-use-cases/rag-implementation-cookbook.md
```

### Writing a Complex Prompt
> Multi-step tasks, strict constraints, specific output format

```
@ai-agent-standards/prompts/PROMPT-TEMPLATE.md
```

### Code Review / Audit
> Reviewing AI-generated code before merge

```
@ai-agent-standards/quality-control/audit-ai-code-full.md
@ai-agent-standards/quality-control/code-review-checklist.md
```

### Detecting Hallucinations
> AI imports fake libraries, calls non-existent APIs

```
@ai-agent-standards/quality-control/hallucination-detection.md
```

### Database Migrations
> Schema changes, data migration, rollback strategy

```
@ai-agent-standards/prompts/sample-use-cases/database-migration.md
```

### Caching & Performance
> Redis, cache invalidation, query optimization

```
@ai-agent-standards/prompts/sample-use-cases/refactor-cache-strategy.md
```

### Unit Test Generation
> Writing tests for existing or new code

```
@ai-agent-standards/prompts/sample-use-cases/generate-unit-tests.md
```

### Security Audit
> Scanning for vulnerabilities in existing code

```
@ai-agent-standards/prompts/sample-use-cases/security-audit.md
```

### API Development
> REST endpoints, rate limiting, authentication

```
@ai-agent-standards/prompts/sample-use-cases/create-api-with-rate-limiting.md
```

### Mobile Development
> Android, iOS, Flutter, React Native — lifecycle, permissions, offline

```
@ai-agent-standards/prompts/sample-use-cases/mobile-development-cookbook.md
```

---

## Multi-Agent Setup

Assign the appropriate file as system instructions for each agent:

| Agent | File to load |
|-------|-------------|
| Coder | `@ai-agent-standards/multi-agent/coder-agent.md` |
| Test | `@ai-agent-standards/multi-agent/test-agent.md` |
| Reviewer | `@ai-agent-standards/multi-agent/reviewer-agent.md` |
| Documentation | `@ai-agent-standards/multi-agent/documentation-agent.md` |

---

## Combining References

For complex tasks, combine multiple references:

```
# Example: Build a secure API with tests

@ai-agent-standards/risk-management/security-constraints.md
@ai-agent-standards/prompts/sample-use-cases/create-api-with-rate-limiting.md
@ai-agent-standards/prompts/PROMPT-TEMPLATE.md

Build POST /api/v1/register with email validation,
bcrypt password hashing, and JWT response.
Include unit tests and Self-Check report.
```

---

## Verify Agent Skills

At any time, ask your agent:

> **"What coding standards are you following?"** or type **`/standards`**

Expected:
> ✅ AI-Coding-Standards Standards v1.3 with Karpathy Principles active.
