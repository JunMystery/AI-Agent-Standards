---
id: PROMPT-001
version: 1.0
author: AI Agent Coding Framework
last_updated: 2026-05-12
applicable_stack: [Node.js, Express, TypeScript, PostgreSQL]
category: API_Development
difficulty: Intermediate
---

# Prompt: Tạo API Endpoint với Rate Limiting & Xác thực

**Mục đích:** Tạo endpoint POST `/api/login` có xác thực JWT + rate limiting, phù hợp cho authentication flow

---

## [CONTEXT - NGỮ CẢNH HỆ THỐNG]

- **Tech stack:** Node.js 18, Express, TypeScript, PostgreSQL, jsonwebtoken, express-rate-limit
- **Trạng thái hiện tại:** Project có folder structure sẵn (`src/controllers`, `src/services`, `src/models`)
- **Database Schema:**
  ```typescript
  User {
    id: number (primary key)
    email: string (unique)
    password: string (hashed)
    created_at: timestamp
  }
  ```
- **Existing Code:** 
  - Database connection đã setup
  - User model có method `findByEmail()`, `comparePassword()`
  - Middleware auth global có sẵn

---

## [TASK - YÊU CẦU NGHIỆP VỤ]

**Mục tiêu:** Tạo endpoint login an toàn với xác thực JWT

**Input:**
```json
{
  "email": "user@example.com",
  "password": "secure_password"
}
```

**Output (Success - 200):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "user": {
    "id": 1,
    "email": "user@example.com"
  }
}
```

**Output (Error - 400/401):**
```json
{
  "error": "Invalid email or password"
}
```

**Acceptance Criteria:**
- [ ] Validate email format & password length (min 8 chars)
- [ ] Rate limiting: Max 5 attempts per 15 minutes per IP
- [ ] Return 429 (Too Many Requests) khi vượt limit
- [ ] Hash password KHÔNG lưu plaintext
- [ ] JWT token có expiry = 24 hours
- [ ] Log login attempts (success & failure)
- [ ] Return 400 nếu email/password missing
- [ ] Return 401 nếu email không tồn tại hoặc password sai

---

## [CONSTRAINTS - RÀNG BUỘC KỸ THUẬT CỨNG]

**HÀNH VI BỊ CẤM:**
- ❌ Không hardcode JWT secret - phải từ .env
- ❌ Không store plaintext password
- ❌ Không log sensitive data (passwords, tokens)
- ❌ Không sửa database schema
- ❌ Không sử dụng `any` type trong TypeScript

**YÊU CẦU BẮT BUỘC:**
- ✓ Try-catch bắt tất cả database queries
- ✓ Input validation với zod hoặc joi
- ✓ Rate limiter bắt buộc sử dụng `express-rate-limit`
- ✓ Error messages không reveal sensitive info
- ✓ Bắt buộc unit tests (min 80% coverage)
- ✓ Comments giải thích business logic

**Quy trình:**
- ✓ Chạy Self-Check trước output
- ✓ Kèm Self-Check report & unit test examples

---

## [OUTPUT FORMAT - ĐỊNH DẠNG ĐẦU RA]

- **Format:** TypeScript code cho `src/controllers/auth.controller.ts`
- **Kèm:** Service method `src/services/auth.service.ts` nếu logic phức tạp
- **Style:** ESLint + Prettier
- **Độ dài:** Code chỉ (không giải thích dài)
- **Kèm:** Self-Check report + unit test skeleton

---

## 📝 Tham chiếu

- Phần III.2: Khuôn mẫu Prompt Tiêu chuẩn
- Phần IV.5: Kiểm soát chi phí
- Code Review Checklist: [`../../quality-control/code-review-checklist.md`](../../quality-control/code-review-checklist.md)
