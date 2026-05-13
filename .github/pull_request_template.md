## Description

[Brief description of changes]

## Type of Change

- [ ] AI-Assisted code
- [ ] Manual code (human-written only)
- [ ] Refactor
- [ ] Bug fix
- [ ] Documentation update

## Prompt Reference

> Fill in if AI-Assisted:

- **Prompt ID:** PROMPT-XXX
- **Prompt Version:** X.X
- **AI Iteration Count:** [number of Self-Fix rounds]
- **Self-Check Report:** Attached below / In commit message

---

## Systematic Code Audit Checklist

> **Required for all PRs labeled `AI-Assisted`.** Reviewer must check every item.

### 1. Karpathy Principles Validation

- [ ] **Think Before Coding** — Assumptions stated? Ambiguity clarified before implementation?
- [ ] **Simplicity First** — No over-engineering? No unnecessary abstractions or speculative features?
- [ ] **Surgical Changes** — Every changed line traces to the request? No drive-by refactors?
- [ ] **Goal-Driven Execution** — Success criteria defined and verified? Tests pass?

### 2. Zero-Trust Security Review

- [ ] No hardcoded API keys, passwords, tokens, or secrets
- [ ] No PII in logs or error messages
- [ ] All user input validated and sanitized
- [ ] SQL queries use parameterized statements (no string concatenation)
- [ ] No `eval()`, `exec()`, or `new Function()` on user input
- [ ] Sensitive operations use environment variables only
- [ ] `git diff` reviewed for accidental secret exposure

### 3. Code Quality & Over-Engineering Check

- [ ] Could this code be simpler? (If yes, request changes)
- [ ] No abstractions for single-use code
- [ ] No defensive error handling for impossible scenarios
- [ ] No "future-proofing" that wasn't explicitly requested
- [ ] Functions under 50 lines (or justified)
- [ ] Code duplication = 0
- [ ] Dead code / unused imports removed

### 4. Error Handling & Resilience

- [ ] Try-catch present for async / DB / API operations
- [ ] Null/undefined checks for critical paths
- [ ] Graceful fallback on failure (not silent swallow)
- [ ] Error messages are meaningful but don't leak internals
- [ ] Timeouts configured for external calls

### 5. Testing

- [ ] Unit tests included for new code
- [ ] Test coverage >= 80% for changed files
- [ ] Edge cases covered (empty, null, boundary values)
- [ ] Tests actually verify behavior (not just "runs without error")
- [ ] Mocks used appropriately (not over-mocked)

### 6. Two-Pair Eyes Verification

> **Required for:** authentication, authorization, payments, encryption, medical/legal logic, data deletion.

- [ ] Complex business logic reviewed by a second engineer
- [ ] Security-sensitive code reviewed by a second engineer
- [ ] Second reviewer name: _______________

### 7. RAG / AI Pipeline (if applicable)

- [ ] Retrieval fallback handles empty results safely
- [ ] AI responses cite source documents
- [ ] LLM temperature appropriate for domain
- [ ] No fabricated citations or hallucinated references

---

## Reviewer Decision

- [ ] **APPROVE** — All checklist items pass
- [ ] **REQUEST CHANGES** — Issues found (list below)
- [ ] **REJECT** — Critical security or architecture violation

### Issues Found

#### Critical (must fix)
1. _None_

#### Minor (nice to fix)
1. _None_

---

## Labels

<!-- Apply the appropriate labels -->
- [ ] `AI-Assisted`
- [ ] `needs-security-review`
- [ ] `needs-two-pair-eyes`
