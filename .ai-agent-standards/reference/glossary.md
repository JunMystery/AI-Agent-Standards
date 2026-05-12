# Glossary - Thuật Ngữ Chuyên dụng

**Định nghĩa các thuật ngữ trong framework.**

---

## A

**Agentic Coding**
- Tiếp cận sử dụng AI làm trợ lý dưới kiểm soát chặt chẽ
- Khác với "Vibe Coding" (kiểu phó mặc cho AI)

**Acceptance Criteria**
- Danh sách conditions rõ ràng task phải đạt
- Viết trong [TASK] section của prompt

---

## B

**Backward Compatibility**
- Code mới không break existing code
- API endpoints not changed unexpectedly
- Database schemas support migration

**Bắt buộc (Mandatory)**
- Rule phải tuân thủ, không exception
- Ví dụ: Try-catch bắt buộc cho async

---

## C

**CI/CD (Continuous Integration/Deployment)**
- Pipeline tự động build, test, deploy
- Gates kiểm soát quality trước deploy

**Code Review**
- Human duyệt AI code trước merge
- Sử dụng [`code-review-checklist.md`](../quality-control/code-review-checklist.md)

**Constraints (Ràng buộc)**
- Rules kỹ thuật AI phải follow
- Forbidden behaviors + Required behaviors

---

## D

**Definition of Done (DoD)**
- Criteria để task coi là hoàn thành
- Bao gồm: tests, review, docs

**Defect**
- Bug tìm thấy sau merge (regression)
- Tracked trong metrics

**Duplication (Code)**
- Lặp lại code pattern không cần thiết
- Target: 0% duplication

---

## E

**Escalation**
- Báo cáo lên level cao hơn khi problem không giải quyết được
- Path: Self → Mentor → Tech Lead → Architect

**Error Handling**
- Try-catch + graceful fallback
- Meaningful error messages

---

## F

**Failure Log**
- Ghi nhận khi AI fail > 2 lần
- Dùng: [`ai-failure-log-template.md`](../risk-management/ai-failure-log-template.md)

---

## G

**Gate (CI/CD)**
- Checkpoint tự động trong pipeline
- Format, lint, tests, security scans

**Glossary**
- File này - định nghĩa thuật ngữ

---

## H

**Hallucination**
- AI tạo code/references không thực tại
- Ví dụ: import library không tồn tại
- Detection: [`hallucination-detection.md`](../quality-control/hallucination-detection.md)

---

## I

**Input Validation**
- Check user input trước xử lý
- Prevent injection attacks
- Use: zod, joi libraries

---

## J

**Jira / Linear**
- Project management tools
- Tag AI tasks: `[AI-Assisted]`

---

## K

**KPI (Key Performance Indicator)**
- Metrics đo lường hiệu suất
- Examples: Defect rate, Cycle time, Coverage
- Details: [`kpi-definitions.md`](../metrics/kpi-definitions.md)

---

## L

**Layer (Architecture)**
- Controller, Service, Model, Utils
- AI code phải ở layer đúng

**Linting**
- Tự động kiểm tra code style
- Tool: ESLint
- Enforce: Format consistent

---

## M

**Merge**
- Combine code vào main branch (Git)
- Only after all gates pass & review approve

**Metrics**
- Data đo lường AI effectiveness
- Tracked in: [`tracking-template.csv`](../metrics/tracking-template.csv)

---

## N

**Non-Negotiable Constraints**
- Rules tuyệt đối không vi phạm
- Examples: No hardcoded secrets, input validation
- Details: [`security-constraints.md`](../risk-management/security-constraints.md)

**N+1 Query**
- Inefficient DB query pattern
- Loop calls DB nhiều lần thay vì 1 lần

---

## O

**Output Format**
- Expected format của AI output
- Examples: Code only, Code + Tests, JSON

---

## P

**Pipeline**
- 7-step process AI → Review → Merge
- Phần III.4 trong docs gốc

**Prompt**
- Instruction gửi cho AI
- Template: [`prompts/PROMPT-TEMPLATE.md`](../prompts/PROMPT-TEMPLATE.md)

**Prompt Library**
- Collection chuẩn hóa prompts
- Location: [`prompts/`](../prompts/)

---

## Q

**Quality Control**
- Multi-layer checks trước merge
- Details: [`quality-control/`](../quality-control/)

---

## R

**Regression**
- Bug mới tạo ra do thay đổi
- Prevent: Unit tests + review

**Refactor**
- Rewrite code mà không change behavior
- Improve: Performance, readability, maintainability

**Review**
- Human kiểm tra AI code
- Use: [`code-review-checklist.md`](../quality-control/code-review-checklist.md)

---

## S

**SAST (Static Application Security Testing)**
- Tool scan code tìm security issues
- Examples: SonarQube, Snyk

**Schema**
- Data structure definition
- Database tables, API types

**Security Constraints**
- Non-negotiable security rules
- Details: [`security-constraints.md`](../risk-management/security-constraints.md)

**Self-Check Report**
- AI báo cáo tự kiểm tra
- Template: [`self-check-report-template.md`](../quality-control/self-check-report-template.md)

**SQL Injection**
- Security vulnerability từ unsanitized input
- Prevent: Parameterized queries

---

## T

**Task**
- Unit của work (story, bug fix)
- Tagged with prompt ID + version when AI-assisted

**Technical Debt**
- Code quality issues accumulated over time
- Must be reduced regularly

**Test Coverage**
- % of code executed by tests
- Target: >= 80%

**Try-Catch**
- Exception handling block
- Bắt buộc cho async operations

---

## U

**Unit Test**
- Test individual function/method
- Must be > 80% coverage

---

## V

**Vibe Coding**
- Phó mặc cho AI mà không kiểm soát
- ⚠️ Not recommended - risky!

---

## W

**Walkthrough**
- Step-by-step guide
- First task: [`onboarding/first-task-walkthrough.md`](../onboarding/first-task-walkthrough.md)

---

## X

**XSS (Cross-Site Scripting)**
- Security vulnerability
- Prevent: Input sanitization + CSP headers

---

## Y

**YAML**
- Data format for configs
- Prompt headers use YAML format

---

## Z

**Zero-Trust Security**
- Assume nothing is trusted by default
- Verify all inputs, no hardcoded secrets

**Zod**
- TypeScript-first schema validation library
- Use for input validation

---

**Glossary v1.0 | Last updated: 2026-05-12**

*More terms will be added as framework evolves.*
