---
id: PROMPT-004
version: 1.0
author: AI Agent Coding Framework
last_updated: 2026-05-12
applicable_stack: [Node.js, Express, TypeScript]
category: Security
difficulty: Intermediate
---

# Prompt: Security Audit - Vulnerability Detection

**Mục đích:** Audit code & model architecture để phát hiện lỗ hổng bảo mật

---

## [CONTEXT - NGỮ CẢNH HỆ THỐNG]

- **Tech stack:** Node.js, Express, TypeScript, PostgreSQL
- **Code to audit:** 
  ```javascript
  app.post('/api/search', (req, res) => {
    const query = req.body.q;
    const result = db.query("SELECT * FROM products WHERE name = '" + query + "'");
    res.send(result);
  });
  ```
- **Mục tiêu:** Phát hiện & fix vulnerabilities (SQL Injection, XSS, etc)

---

## [TASK - YÊU CẦU NGHIỆP VỤ]

**Mục tiêu:** Audit & đưa ra giải pháp fix

**Acceptance Criteria:**
- [ ] Phát hiện tất cả vulnerabilities
- [ ] Giải thích mỗi lỗi (CWE reference)
- [ ] Cung cấp fixed code
- [ ] Tất cả test cases verify fixes

---

## [CONSTRAINTS - RÀNG BUỘC KỸ THUẬT]

**YÊU CẦU BẮT BUỘC:**
- ✓ Parameterized queries bắt buộc
- ✓ Input validation + sanitization
- ✓ Error handling không reveal details
- ✓ Security comments

---

## [OUTPUT FORMAT - ĐỊNH DẠNG ĐẦU RA]

- **Format:** Audit report + fixed code
- **Kèm:** Security checklist + recommendations

---

## 📝 Reference

- Security Constraints: [`../../risk-management/security-constraints.md`](../../risk-management/security-constraints.md)
- Error Reference: [`../../reference/error-reference-complete.md`](../../reference/error-reference-complete.md)
