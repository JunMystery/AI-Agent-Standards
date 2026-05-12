# Onboarding - AI Agent Coding Standards

**Chương trình onboarding mới dành cho kỹ sư tham gia project dùng AI.**

---

## 🚀 Quick Start (Bắt đầu nhanh)

### Day 1: Orientation

1. **Đọc tài liệu (20 phút):**
   - [`quick-reference.md`](quick-reference.md) ← **START HERE** ⭐⭐⭐
   - [`first-task-walkthrough.md`](first-task-walkthrough.md)

2. **Setup project:**
   ```bash
   git clone [project-repo]
   cd project
   npm install
   ```

3. **Làm quen với .cursorrules:**
   - Open: `project/.ai-agent-standards/.cursorrules`
   - Hiểu: Framework, naming conventions, security rules

4. **Setup IDE (nếu dùng Cursor/Windsurf):**
   - Copy `.cursorrules` vào project root
   - Restart IDE

---

### Day 2-3: First Task

1. **Chọn simple task** (API endpoint, unit tests, refactor)
2. **Follow walkthrough:** [`first-task-walkthrough.md`](first-task-walkthrough.md) (30 min)
3. **Apply pipeline:** [`../quality-control/`](../quality-control/)
4. **Get code reviewed** by mentor

---

## 📋 Program Structure

| Phase | Duration | Content | Deliverable |
|-------|----------|---------|-------------|
| **Onboarding** | Day 1 | Read docs, setup | ✓ understand framework |
| **First Task** | Day 2-3 | Guided task with mentor | ✓ 1 approved PR |
| **Independent** | Week 1 | 2-3 tasks solo | ✓ 3 approved tasks |
| **Mastery** | Ongoing | Advanced tasks, mentoring others | ✓ Can review others' AI code |

---

## 📚 Essential Docs

Read in this order:

1. ⭐⭐⭐ [`quick-reference.md`](quick-reference.md) - Cheat sheet 1 page
2. ⭐⭐⭐ [`first-task-walkthrough.md`](first-task-walkthrough.md) - Step-by-step guide
3. ⭐⭐ [`common-mistakes.md`](common-mistakes.md) - What NOT to do
4. ⭐ [`../README.md`](../README.md) - Full overview

---

## ✅ Sign-Off Checklist

Before you're "ready to code independently", verify:

- [ ] Read quick-reference guide?
- [ ] Completed first task walkthrough?
- [ ] Understand pipeline: Generate → Self-Check → Human Gate?
- [ ] Know security constraints (no secrets)?
- [ ] Know when to escalate (> 2 Self-Fix rounds)?
- [ ] Can use code-review checklist?
- [ ] Mentor approved?

---

## 🤝 Mentoring

**Your mentor:** [Name]
- **Time:** [Scheduled times for Q&A]
- **Slack:** [Channel]
- **Office hours:** [Times]

**Escalation if mentor unavailable:**
- Team lead: [Name]
- Tech lead: [Name]

---

## 🎯 Success Criteria

**You're ready to code alone when:**

1. ✓ Complete 3 tasks with AI-Assisted (all approved)
2. ✓ Average iteration count <= 2 per task
3. ✓ 0 critical issues found in reviews
4. ✓ Understand when & how to escalate
5. ✓ Can review someone else's AI code

---

## 📞 FAQ

**Q: What if AI output is wrong?**
A: Check [`../quality-control/hallucination-detection.md`](../quality-control/hallucination-detection.md)

**Q: I need help with a prompt?**
A: Look at [`../prompts/sample-use-cases/`](../prompts/sample-use-cases/) for examples

**Q: Pipeline confusing?**
A: Read [`../quality-control/README.md`](../quality-control/README.md)

**Q: How do I track what I did?**
A: Use [`../metrics/tracking-template.csv`](../metrics/tracking-template.csv)

---

## 🔗 Quick Links

| Need | Link |
|------|------|
| Prompt examples | [`../prompts/sample-use-cases/`](../prompts/sample-use-cases/) |
| Code review checks | [`../quality-control/code-review-checklist.md`](../quality-control/code-review-checklist.md) |
| Security rules | [`../risk-management/security-constraints.md`](../risk-management/security-constraints.md) |
| Error help | [`../reference/error-reference-complete.md`](../reference/error-reference-complete.md) |
| Common mistakes | [`common-mistakes.md`](common-mistakes.md) |

---

**Onboarding Duration:** 3-5 days | **Success Rate Target:** 100%

Next step: Read [`quick-reference.md`](quick-reference.md) 👉
