# Quick Reference - Cheat Sheet (1 Page)

**Print this page and keep it handy while learning.**

---

## 🚀 Karpathy Principles (Core Philosophy)

**Apply these 4 principles to EVERY AI task — they prevent 80% of common mistakes.**

### 1️⃣ **Think Before Coding**
- State assumptions explicitly before coding starts
- If request is ambiguous, present multiple interpretations
- Ask questions BEFORE implementing
- Don't pick one silent answer

### 2️⃣ **Simplicity First**  
- Minimum code solving the problem
- No extra features, no speculative abstractions
- No "flexibility" that wasn't requested
- If you write 200 lines, could it be 50? Simplify.

### 3️⃣ **Surgical Changes**
- Touch ONLY what you must
- Match existing style—don't "improve"
- Clean up only YOUR OWN mess
- Every changed line traces to the request

### 4️⃣ **Goal-Driven Execution**
- Define success criteria upfront (not "make it work")
- Write tests BEFORE coding
- Verify success before submitting
- Iterate until criteria met

💡 **Detailed guide:** See [karpathy-framework.md](../principles/karpathy-framework.md)

---

## 🎯 7-Step Pipeline

```
1. Write Prompt (from PROMPT-TEMPLATE.md)
   ↓
2. Paste to AI (Claude/Copilot/ChatGPT)
   ↓
3. AI Generates Code + Self-Check Report
   ↓
4. Review Code + Self-Check Report ← YOU ARE HERE
   ├─ Use: code-review-checklist.md
   └─ Check: Security, tests, errors
   ↓
5. Approve OR Request Changes
   ├─ [✓ OK] → Merge
   └─ [✗ Wrong] → Back to step 2
   ↓
6. Merge to Git
   ↓
7. Done! Log metrics in tracking-template.csv
```

---

## ✅ What AI MUST Include

- ✓ Code that works
- ✓ Self-Check Report (see template)
- ✓ Unit tests (>= 80% coverage)
- ✓ No hardcoded secrets (API keys, passwords)
- ✓ Try-catch for errors
- ✓ Input validation
- ✓ Comments for complex logic

---

## 🚫 What AI MUST NOT Do

- ✗ Hardcode API keys / passwords
- ✗ Skip error handling
- ✗ Create security vulnerabilities (SQL injection, XSS)
- ✗ Make breaking changes without tests
- ✗ Use unknown libraries
- ✗ Leave console.log() in production

---

## 🔍 Your Checklist (Before Merge)

- [ ] Self-Check Report present?
- [ ] Code solves stated problem?
- [ ] No hardcoded secrets?
- [ ] Error handling (try-catch)?
- [ ] Tests >= 80%?
- [ ] Security OK (no SQL injection)?
- [ ] Backward compatible?
- [ ] Comments clear?

**If ANY fail → Request changes**

---

## 🚨 Red Flags (AUTO REJECT)

- ❌ Hardcoded API key
- ❌ No error handling
- ❌ No input validation
- ❌ SQL injection pattern
- ❌ Test coverage < 50%

Ask AI to fix → Iterate

---

## 💡 Prompt Template (Copy This)

```markdown
### [CONTEXT]
- Tech: [Your tech stack]
- Current: [What exists]
- Schema: [Data structure]

### [TASK]
- Goal: [What to build]
- Input/Output: [Example]
- Requirements: [Acceptance criteria]

### [CONSTRAINTS]
- Forbidden: [What NOT to do]
- Required: [What MUST do]
- Rules: [Special rules]

### [OUTPUT]
- Format: [Code only / With tests]
- Include: Self-Check report
```

---

## 🎯 Common Scenarios

### Scenario 1: API Endpoint
1. Prompt: [`../prompts/sample-use-cases/create-api-with-rate-limiting.md`](../prompts/sample-use-cases/create-api-with-rate-limiting.md)
2. Review: code-review-checklist.md + audit-ai-code-full.md
3. Check: Security (SQL injection?), Tests, Error handling

### Scenario 2: Unit Tests
1. Prompt: [`../prompts/sample-use-cases/generate-unit-tests.md`](../prompts/sample-use-cases/generate-unit-tests.md)
2. Review: Coverage >= 80%
3. Check: Edge cases, mocks correct

### Scenario 3: Security Audit
1. Prompt: [`../prompts/sample-use-cases/security-audit.md`](../prompts/sample-use-cases/security-audit.md)
2. Review: Vulnerabilities fixed
3. Check: No hardcoded secrets

---

## 📞 When to Escalate

**If AI fails 2+ times (Self-Fix rounds):**
1. Stop → Don't keep asking
2. Log in: [`../risk-management/ai-failure-log-template.md`](../risk-management/ai-failure-log-template.md)
3. Escalate to: [Mentor name / Tech lead]
4. Or: Code manually yourself

---

## 🆘 Help Resources

| Need | Where |
|------|-------|
| Prompt examples | `../prompts/sample-use-cases/` |
| Review checklist | `../quality-control/code-review-checklist.md` |
| AI error detection | `../quality-control/hallucination-detection.md` |
| Security rules | `../risk-management/security-constraints.md` |
| Common mistakes | `./common-mistakes.md` |
| Error reference | `../reference/error-reference-complete.md` |
| Full docs | `../README.md` |

---

## 📊 Metrics to Track

**For each task, record:**
- Prompt ID + version
- # iterations (Self-Fix rounds)
- Time taken
- Test coverage %
- Any issues found

→ Store in your project's task tracker

---

## 💬 Slack / Message Templates

**When asking for help:**
```
"Task: [description]
Prompt: PROMPT-001 v1.0
AI iteration: 2 (failed on X)
Issue: [What went wrong]
Help: [Specific question]"
```

---

**Print this page & keep handy! 👆**

---

*Quick Reference v1.0 | Last updated: 2026-05-12*
