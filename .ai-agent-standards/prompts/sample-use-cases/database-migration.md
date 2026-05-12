---
id: PROMPT-005
version: 1.0
author: AI Agent Coding Framework
last_updated: 2026-05-12
applicable_stack: [Node.js, TypeScript, PostgreSQL, Alembic]
category: Database_Management
difficulty: Intermediate
---

# Prompt: Database Migration - Safe Schema Changes

**Mục đích:** Tạo database migration an toàn cho schema changes (add column, rename table, etc)

---

## [CONTEXT - NGỮ CẢNH HỆ THỐNG]

- **Tech stack:** Node.js, TypeScript, PostgreSQL 14, Alembic migrations
- **Current Schema:**
  ```sql
  CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
  );
  ```
- **Migration Tool:** Alembic (Python) hoặc db-migrate (Node.js)
- **Data:** ~500k existing users

---

## [TASK - YÊU CẦU NGHIỆP VỤ]

**Mục tiêu:** Add `phone` column to users table (optional, nullable)

**Acceptance Criteria:**
- [ ] Add `phone VARCHAR(20)` column (nullable)
- [ ] Rollback function tạo (down migration)
- [ ] Không lock table > 1 second
- [ ] Migration scripts tested locally
- [ ] Data backup trước migration

---

## [CONSTRAINTS - RÀNG BUỘC KỸ THUẬT]

**HÀNH VI BỊ CẤM:**
- ❌ Không drop existing data
- ❌ Không make non-nullable columns nullable
- ❌ Không remove constraints

**YÊU CẦU BẮT BUỘC:**
- ✓ Bắt buộc down (rollback) migration
- ✓ Comments giải thích schema change
- ✓ Test rollback locally

---

## [OUTPUT FORMAT - ĐỊNH DẠNG ĐẦU RA]

- **Format:** Migration scripts (up + down)
- **Kèm:** Rollback test results
- **Độ dài:** Code chỉ

---

## 📝 Reference

- Risk Management: [`../../risk-management/`](../../risk-management/)
