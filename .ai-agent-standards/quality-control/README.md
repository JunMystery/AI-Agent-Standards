# Quality Control Pipeline - Kiểm soát Chất lượng AI Output

Hệ thống kiểm duyệt 4 tầng cho tất cả code AI sinh ra.

---

## 🔄 Pipeline Tổng quan

```
[ REQUEST FROM ENGINEER ]
          ↓
┌─────────────────────────────────────────────────┐
│ 1. AI GENERATE - Sinh code                       │
├─────────────────────────────────────────────────┤
│ 2. AI SELF-CHECK - Tự kiểm tra (Bắt buộc)       │
│    - Security, duplication, error handling       │
│    - Regression risk, best practices             │
├─────────────────────────────────────────────────┤
│ 3. AI SELF-FIX - Tự sửa lỗi (Max 2 rounds)     │
│    - Nếu Self-Check fail → Auto fix              │
│    - Nếu vẫn fail → Report & escalate            │
├─────────────────────────────────────────────────┤
│ 4. OUTPUT - Kết xuất code + report               │
└─────────────────────────────────────────────────┘
          ↓
[ HUMAN GATE - CODE REVIEW BỞI KỸ SƯ ]
  ├─ Review with: code-review-checklist.md
  ├─ Audit with: audit-ai-code-full.md
  └─ Decision:
      [✓ APPROVE] → Merge + Checkpoint
      [✗ REJECT/REWORK] → Back to step 1
```

---

## 📋 Key Files in This Folder

| File | Mục đích | Bắt buộc? |
|------|---------|---------|
| [`self-check-report-template.md`](self-check-report-template.md) | Mẫu báo cáo tự kiểm tra | ✓ **YES** |
| [`code-review-checklist.md`](code-review-checklist.md) | Checklist khi review code | ✓ **YES** |
| [`audit-ai-code-full.md`](audit-ai-code-full.md) | Audit chi tiết AI output | ✓ **YES** |
| [`hallucination-detection.md`](hallucination-detection.md) | Phát hiện lỗi AI | ✓ **YES** |
| [`ci-cd-gates.md`](ci-cd-gates.md) | Quy tắc CI/CD integration | ⚠️ Optional |

---

## ✅ Self-Check Report (AI-Generated)

**Bắt buộc AI xuất report này trước mọi output.**

Xem template: [`self-check-report-template.md`](self-check-report-template.md)

```markdown
### AI Self-Check Report
Prompt ID: PROMPT-001
Checklist:
- [x] Tuân thủ Non-Negotiable Constraints
- [x] Code duplication = 0
- [x] Security check passed (no SQL injection, XSS)
- [x] Error handling bắt buộc (try-catch, null checks)
- [x] Regression risk: LOW
- [x] Self-Fix rounds: 1 (nếu có lỗi ban đầu)
Ghi chú: [Tùy ý - AI comment]
```

---

## 👤 Code Review Checklist (Human)

**Engineer phải check trước merge code AI.**

Xem checklist đầy đủ: [`code-review-checklist.md`](code-review-checklist.md)

### Quick Version
- [ ] Self-Check report đã hoàn thành?
- [ ] Code matches prompt requirements?
- [ ] No hardcoded secrets/credentials?
- [ ] Try-catch & error handling OK?
- [ ] Test coverage >= 80%?
- [ ] Comments giải thích logic?
- [ ] Tính tương thích backward?

---

## 🔍 Audit AI Code (Detailed)

**Dành cho senior reviewer hoặc security-sensitive modules.**

Xem chi tiết: [`audit-ai-code-full.md`](audit-ai-code-full.md)

### Areas Audited
- Security vulnerabilities (SQLi, XSS, CSRF)
- Performance bottlenecks
- Memory leaks, dangling references
- Code duplication & dead code
- Error handling completeness
- Test quality & coverage

---

## ⚠️ Hallucination Detection

**Phát hiện khi AI tạo code không thực tại.**

Dấu hiệu: [`hallucination-detection.md`](hallucination-detection.md)

```
❌ Import non-existent library
❌ Call API method không tồn tại
❌ Logic algorithm vi phạm constraints
❌ Reference file/class không có
```

**Cách fix:** Verify with official docs, update prompt, iterate

---

## 🚀 CI/CD Gates (Tự động)

**Integrate với CI/CD pipeline để tự động kiểm tra.**

Xem: [`ci-cd-gates.md`](ci-cd-gates.md)

```bash
# Example GitHub Actions
- Run ESLint + Prettier
- Run unit tests (jest)
- Run SAST (SonarQube, Snyk)
- Check test coverage >= 80%
- Flag: AI-Assisted code (special handling)
```

---

## 📊 Metrics từ Pipeline

Theo dõi từ Self-Check Reports:
- **Defect Escape Rate:** % lỗi không được AI detect
- **Human Review Time:** Thời gian review code
- **Iteration Count:** Số vòng Self-Fix trung bình
- **Hallucination Rate:** % output chứa hallucination

---

## 🔗 Integration Points

| With | Purpose |
|------|---------|
| Jira | Label task `[AI-Assisted]`, attach Self-Check report |
| Git | Commit hooks validate Self-Check presence |
| Metrics System | Track review time, iteration count |
| Alerting | Flag high defect rate hoặc regression |

---

## 🎯 Best Practices

1. **Luôn chạy Self-Check** - không exception
2. **Code review bắt buộc** - con người cuối cùng quyết định
3. **Track metrics** - biết pattern nào đang fail
4. **Document hallucination** - improve prompts
5. **Escalate nếu cần** - xem [`risk-management/escalation-workflow.md`](../risk-management/escalation-workflow.md)

---

## 📝 Timeline

Tổng thời gian từ prompt → merged code:

```
1. Prompt → AI Generate:        5-30 min (tùy độ phức tạp)
2. Self-Check:                  < 5 min
3. Self-Fix (nếu cần):          5-10 min (max 2 rounds)
4. Human Review:                10-30 min
─────────────────────────────────────
Tổng:                           20-75 min
```

---

## 🆘 Troubleshooting

| Vấn đề | Giải pháp |
|--------|---------|
| AI fail Self-Check 3+ lần | Escalate, review prompt, possibly code manually |
| Reviewer reject nhiều | Improve prompt clarity, add more constraints |
| High hallucination rate | Update prompt with more doc references |
| CI/CD gate fail | Check linter rules, coverage threshold |

---

## 📌 Checklist Setup Mới

- [ ] Đã create team Slack channel `#ai-code-review`?
- [ ] Đã setup Jira label `[AI-Assisted]`?
- [ ] Đã brief team về Self-Check requirement?
- [ ] Đã update CI/CD pipeline (nếu dùng)?
- [ ] Đã assign primary reviewer?

---

**Reference:** Phần III.4 - Pipeline Kiểm soát Chất lượng (Tài liệu gốc)

**Last updated:** 2026-05-12
