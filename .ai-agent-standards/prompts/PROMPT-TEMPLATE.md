---
id: PROMPT-TEMPLATE
version: 1.0
author: [Your Name]
last_updated: 2026-05-12
applicable_stack: [NodeJS, React, etc]
category: General
difficulty: Intermediate
---

# Khuôn Mẫu Prompt Tiêu chuẩn

Sử dụng template này làm cơ sở cho mọi prompt mới.

---

## 📋 Cấu trúc

### [CONTEXT - NGỮ CẢNH HỆ THỐNG]
Cung cấp thông tin cần thiết về:
- **Tech stack:** Framework, libraries, versions
- **Trạng thái hiện tại:** Mô tả kỹ thuật tóm tắt
- **Schema/Interfaces:** Cấu trúc dữ liệu liên quan
- **Existing Code:** Code snippet nếu cần tham chiếu

*Ví dụ:*
```
- Tech stack: React v18, Node.js 18, PostgreSQL 14
- Trạng thái: Module auth đã có, cần tạo role-based access control
- Schema: User { id, email, role }, Role { id, name, permissions }
```

### [TASK - YÊU CẦU NGHIỆP VỤ]
Mô tả chi tiết & độc lập 1 tính năng duy nhất:
- **Mục tiêu:** Cái gì cần tạo/sửa
- **Input/Output:** Dữ liệu đầu vào & kỳ vọng
- **Acceptance Criteria:** Danh sách clear conditions

*Ví dụ:*
```
- Mục tiêu: Tạo endpoint POST /api/posts với validation
- Input: { title: string, content: string, userId: number }
- Output: { id, title, content, userId, createdAt }
- Acceptance:
  [x] Title max 200 chars, content max 5000 chars
  [x] userId phải tồn tại trong DB
  [x] Return 400 nếu input invalid, 201 nếu success
```

### [CONSTRAINTS - RÀNG BUỘC KỸ THUẬT CỨNG]
**Lớp nền tiên quyết:**
- **HÀNH VI BỊ CẤM:** Gì AI KHÔNG ĐƯỢC làm
  - ❌ Không sửa file .env
  - ❌ Không import thư viện ngoài [list]
  - ❌ Không sử dụng recursive approach cho bộ đặc lớn
- **YÊU CẦU BẮT BUỘC:** Gì AI PHẢI làm
  - ✓ Bắt buộc try-catch cho async operations
  - ✓ Bắt buộc input validation với zod/joi
  - ✓ Bắt buộc 80%+ test coverage
- **Quy trình:** 
  - ✓ Phải chạy Self-Check trước output (Phần III.4)
  - ✓ Output phải kèm Self-Check report

*Ví dụ:*
```
HÀNH VI BỊ CẤM:
- Không sửa database schema
- Không sử dụng any type trong TypeScript
- Không hardcode API endpoints

YÊU CẦU BẮT BUỘC:
- Try-catch cho tất cả API calls
- Validate input trước processing
- Log errors & return meaningful messages

Quy trình:
- Chạy Self-Check checklist trước xuất code
- Kèm theo Self-Check Report
```

### [OUTPUT FORMAT - ĐỊNH DẠNG ĐẦU RA]
Rõ ràng định dạng & cách trình bày kỳ vọng:
- Code chỉ / Code + expl anation?
- Single file / Multiple files?
- JSON / Markdown / Plain text?
- Kèm Self-Check report?

*Ví dụ:*
```
- Chỉ xuất code thay đổi (không giải thích dài)
- Format: Single TypeScript file
- Kèm: Self-Check report (checklist style)
- Định dạng code: ESLint + Prettier compatible
```

---

## ✅ Self-Check Checklist

**AI phải hoàn thành trước khi xuất output:**

```markdown
### AI Self-Check Report
- Prompt ID: [ID]
- Checklist:
  [ ] Tuân thủ Lớp nền Tiên quyết (Security, No hardcode)?
  [ ] Code duplication = 0?
  [ ] Xử lý bảo mật (SQLi, XSS, info leak)?
  [ ] Xử lý exception (null, timeout, errors)?
  [ ] Regression risk thấp (không break existing)?
- Ghi chú: [Tùy ý]
```

---

## 🎯 Best Practices

1. **Clarity:** Mỗi section rõ ràng, không mơ hồ
2. **Conciseness:** Ngắn gọn, cung cấp đủ info nhưng không quá
3. **Specificity:** Có ví dụ, code snippet, not just description
4. **Testability:** Output phải có cách xác minh
5. **Traceability:** Ghi context để sau có thể debug nếu cần

---

## 📊 Template Struktur

| Section | Bắt buộc? | Độ dài |
|---------|-----------|--------|
| CONTEXT | ✓ | 5-10 dòng |
| TASK | ✓ | 5-10 dòng |
| CONSTRAINTS | ✓ | 10-15 dòng |
| OUTPUT FORMAT | ✓ | 3-5 dòng |
| Self-Check | ✓ | Tự động |

---

## 🔗 Reference

- Full Standards: Tài liệu gốc "AI Agent Coding - Phần III.2"
- Sample Prompts: [`sample-use-cases/`](sample-use-cases/)
- Self-Check Report: [`../quality-control/self-check-report-template.md`](../quality-control/self-check-report-template.md)

---

**Ghi chú:** Copy template này & fill in details cho use case cụ thể. Đừng quên header YAML ở đầu file!
