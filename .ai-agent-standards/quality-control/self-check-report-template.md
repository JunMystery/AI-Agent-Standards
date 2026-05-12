# AI Self-Check Report Template

**Mẫu báo cáo tự kiểm tra - AI phải fill in trước output**

*Phụ lục C từ tài liệu gốc*

---

## 📋 Template

```markdown
## AI Self-Check Report

**Metadata:**
- Prompt ID: PROMPT-XXX
- Prompt Version: 1.0  
- Task: [Brief description of what was built]
- Date: [YYYY-MM-DD HH:MM]
- AI Iteration Count: [Number of Self-Fix rounds]

---

### Checklist ✓

**Security & Architecture:**
- [ ] Tuân thủ Lớp nền Tiên quyết (Non-Negotiable Constraints)?
  - No hardcoded secrets
  - Input validation implemented
  - Error handling complete
- [ ] Code tương thích kiến trúc hiện hành?
- [ ] Không vi phạm bảo mật (SQLi, XSS, CSRF)?

**Code Quality:**
- [ ] Code duplication = 0?
- [ ] Complexity score acceptable?
- [ ] Dead code / unused imports = 0?
- [ ] All variables properly typed (TypeScript)?

**Error Handling:**
- [ ] Bắt buộc try-catch cho async/DB operations?
- [ ] Null/undefined checks present?
- [ ] Error messages không leak sensitive data?
- [ ] Logging appropriate (not verbose)?

**Testing:**
- [ ] Test coverage >= 80% (for new code)?
- [ ] Edge cases covered?
- [ ] Mock setup correct?

**Performance & Regression:**
- [ ] Database queries optimized (no N+1)?
- [ ] No memory leaks / dangling references?
- [ ] Regression risk assessment: LOW / MEDIUM / HIGH?
- [ ] Backward compatibility maintained?

---

### Self-Fix History

**Round 1:** [If needed - what was fixed]
- Issue: [Describe]
- Fix: [What changed]

**Round 2:** [If needed]
- Issue: [Describe]
- Fix: [What changed]

---

### Notes & Warnings

**Potential Issues:**
- [List any concerns AI couldn't self-fix]
- [Flag for human review]

**Recommendations:**
- [Performance improvement ideas]
- [Security hardening suggestions]

**References:**
- Constraint source: [Link to constraint doc]
- Test coverage tool: [jest/nyc]
- Linter used: [eslint/prettier]

---

### Final Status

**✅ READY FOR HUMAN REVIEW** 

All checklist items passed. Code ready for `code-review-checklist.md`

**OR**

**⚠️ REQUIRES ATTENTION**

Failed items:
- [ ] Item 1
- [ ] Item 2

Recommend: [Reject & iterate / Manual fix required]

---

**Generated at:** 2026-05-12 10:30 UTC
**AI Model:** Claude 3.5 Sonnet
**Total Duration:** X minutes
```

---

## 📝 Cách Dùng

### Cho AI (khi sinh code)

1. **Fill in metadata** (Prompt ID, version, task)
2. **Chạy qua từng item** trong checklist
3. **Mark [x]** nếu pass, [ ] nếu fail
4. **Document Self-Fix history** nếu có
5. **Đưa ra final status:** READY hoặc REQUIRES ATTENTION

### Cho Human Reviewer

1. **Xem mục "Failed items"** nếu có
2. **Cross-check** các items quan trọng (Security, Testing)
3. **Verify** regression risk assessment
4. **Decide:** Approve → Merge, hoặc Reject → Back to AI

---

## 🎯 Key Items (Tuyệt Đối Bắt Buộc)

**Nếu AI không pass được 3 items này → Escalate ngay:**
1. ✓ Security constraints
2. ✓ Error handling
3. ✓ Test coverage >= 80%

---

## 📊 Metrics từ Report

**Theo dõi theo thời gian:**
- Average iteration count per task
- Common fail items (pattern detect)
- Time to pass Self-Check
- Defect escape rate (% được human catch)

---

## 🔗 Reference

- Code Review Checklist: [`code-review-checklist.md`](code-review-checklist.md)
- Audit Full: [`audit-ai-code-full.md`](audit-ai-code-full.md)
- Phụ lục C: Tài liệu gốc "AI Agent Coding"

---

**Template Version:** 1.0 | **Last Updated:** 2026-05-12
