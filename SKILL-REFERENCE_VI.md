# Hướng Dẫn Sử Dụng Skill — Tra Cứu Nhanh

**Bạn cần reference file nào cho từng loại công việc?**

Sao chép các lệnh `@file` bên dưới vào prompt của bạn để kích hoạt skill tương ứng cho AI agent.

---

## Công việc hàng ngày (không cần reference thêm)

AI agent **đã tự động load** 5 Nguyên tắc Karpathy từ file gốc (`CLAUDE.md`, `GEMINI.md`, v.v.) ngay khi mở project. Bạn chỉ cần mô tả yêu cầu bình thường — agent sẽ tự tuân thủ các nguyên tắc:

1. **Think Before Coding** — Nêu giả định, hỏi khi không rõ
2. **Simplicity First** — Code tối thiểu, không thêm tính năng dư thừa
3. **Surgical Changes** — Chỉ sửa đúng phần cần thiết
4. **Goal-Driven Execution** — Xác định tiêu chí thành công trước khi code
5. **DRY & Reusability** — Không lặp lại UI/Logic

**→ Không cần gõ thêm gì. Agent đã biết.**

*(Lưu ý: Nếu dự án có luật riêng, hãy viết vào file `PROJECT-STANDARDS.md` tại thư mục gốc. Agent sẽ tự động học các luật này.)*

---

## 🤖 Nhận diện kỹ năng tự động (Dynamic Auto-Discovery - v2.4.0)

Các AI Agent hiện đại (Cursor, Windsurf, Claude Code, Gemini tích hợp trong IDE) hiện đã được trang bị tính năng **Tự động nhận diện**. Khi yêu cầu của bạn có chứa các từ khóa như "Viết test", "Bảo mật", "Tối ưu hiệu năng", AI sẽ *tự động âm thầm* gọi lệnh đọc các file tiêu chuẩn tương ứng ở bên dưới.

Bạn CHỈ CẦN gõ lệnh `@reference` thủ công nếu bạn đang dùng các Chatbot web (không có quyền đọc file) hoặc muốn ép AI đọc một Cookbook cụ thể nào đó.

---

## Local Skills đã triển khai

Các skill capsule dạng on-demand hiện có trong [skills/](./skills/):

- [coding-standards](./skills/coding-standards/SKILL.md)
- [tdd-workflow](./skills/tdd-workflow/SKILL.md)
- [verification-loop](./skills/verification-loop/SKILL.md)
- [security-review](./skills/security-review/SKILL.md)
- [codebase-onboarding](./skills/codebase-onboarding/SKILL.md)
- [context-budget](./skills/context-budget/SKILL.md)
- [documentation-lookup](./skills/documentation-lookup/SKILL.md)
- [browser-qa](./skills/browser-qa/SKILL.md)
- [prompt-optimizer](./skills/prompt-optimizer/SKILL.md)
- [skill-scout](./skills/skill-scout/SKILL.md)
- [accessibility](./skills/accessibility/SKILL.md)
- [api-design](./skills/api-design/SKILL.md)
- [architecture-decision-records](./skills/architecture-decision-records/SKILL.md)
- [database-migrations](./skills/database-migrations/SKILL.md)
- [error-handling](./skills/error-handling/SKILL.md)
- [git-workflow](./skills/git-workflow/SKILL.md)
- [production-audit](./skills/production-audit/SKILL.md)
- [search-first](./skills/search-first/SKILL.md)
- [skill-stocktake](./skills/skill-stocktake/SKILL.md)
- [rules-distill](./skills/rules-distill/SKILL.md)

---

## Tra cứu theo loại công việc

### 🔒 Code liên quan bảo mật
> Xác thực (auth), thanh toán, mã hóa, xử lý dữ liệu người dùng, API key

**Giải thích:** File này chứa 12 ràng buộc bảo mật bắt buộc. Khi reference, agent sẽ tự động kiểm tra: không hardcode secret, validate input, hash password, dùng parameterized queries, v.v.

```
@ai-agent-standards/risk-management/security-constraints.md
```

---

### 🧠 RAG / AI Pipeline
> Truy xuất dữ liệu từ Vector DB, sinh văn bản bằng LLM, embeddings

**Giải thích:** Cookbook mẫu cho pipeline RAG an toàn. Bao gồm: chiến lược fallback khi không tìm thấy kết quả, trích dẫn nguồn bắt buộc, kiểm soát hallucination, và cấu trúc code mẫu (Python/LangChain).

```
@ai-agent-standards/prompts/sample-use-cases/rag-implementation-cookbook.md
```

---

### 📝 Viết prompt phức tạp
> Yêu cầu nhiều bước, nhiều ràng buộc, định dạng đầu ra cụ thể

**Giải thích:** Template chuẩn gồm 4 phần: CONTEXT (ngữ cảnh), TASK (yêu cầu), CONSTRAINTS (ràng buộc), OUTPUT FORMAT (định dạng). Giúp agent hiểu chính xác bạn muốn gì.

```
@ai-agent-standards/prompts/PROMPT-TEMPLATE.md
```

---

### 🔍 Review / Audit code AI
> Kiểm duyệt code do AI sinh ra trước khi merge

**Giải thích:** Bảng kiểm tra 11 mục (bảo mật, hiệu năng, code quality, RAG pipeline, AI output safety). Dùng khi bạn muốn agent tự audit code trước khi xuất kết quả.

```
@ai-agent-standards/quality-control/audit-ai-code-full.md
@ai-agent-standards/quality-control/code-review-checklist.md
```

---

### 👻 Phát hiện Hallucination
> AI import thư viện không tồn tại, gọi API giả, bịa references

**Giải thích:** Hướng dẫn nhận diện và xử lý khi AI "bịa" — import thư viện ảo, gọi method không có trong docs, tạo citation không tồn tại. Đặc biệt quan trọng cho domain y tế/pháp lý.

```
@ai-agent-standards/quality-control/hallucination-detection.md
```

---

### 🗄️ Database Migration
> Thay đổi schema, di chuyển dữ liệu, chiến lược rollback

**Giải thích:** Prompt mẫu cho các tác vụ migration database. Ép buộc agent tạo migration script có rollback, không phá dữ liệu hiện có.

```
@ai-agent-standards/prompts/sample-use-cases/database-migration.md
```

---

### ⚡ Caching & Hiệu năng
> Redis, cache invalidation, tối ưu query

**Giải thích:** Prompt mẫu cho refactor chiến lược caching. Bao gồm: chọn cache layer, invalidation strategy, TTL configuration.

```
@ai-agent-standards/prompts/sample-use-cases/refactor-cache-strategy.md
```

---

### 🧪 Sinh Unit Test
> Viết test cho code mới hoặc code hiện có

**Giải thích:** Prompt mẫu yêu cầu agent sinh test đúng chuẩn: cover happy path, edge cases, error handling. Target coverage ≥ 80%.

```
@ai-agent-standards/prompts/sample-use-cases/generate-unit-tests.md
```

---

### 🛡️ Security Audit
> Quét lỗ hổng bảo mật trong code hiện có

**Giải thích:** Prompt mẫu để agent rà soát code tìm: SQL injection, XSS, hardcoded secrets, missing auth checks.

```
@ai-agent-standards/prompts/sample-use-cases/security-audit.md
```

---

### 🔌 Phát triển API
> REST endpoints, rate limiting, xác thực JWT

**Giải thích:** Prompt mẫu tạo API endpoint hoàn chỉnh với rate limiting, JWT auth, try-catch, logging. Bao gồm ví dụ Self-Check report.

```
@ai-agent-standards/prompts/sample-use-cases/create-api-with-rate-limiting.md
```

---

### 📱 Phát triển Mobile
> Android, iOS, Flutter, React Native — lifecycle, permissions, offline, accessibility

**Giải thích:** Cookbook tiêu chuẩn cho phát triển ứng dụng di động. Bao gồm: 10 lỗi thường gặp khi AI sinh code mobile, cấu trúc thư mục mẫu, và Self-Check report chuyên mobile.

```
@ai-agent-standards/prompts/sample-use-cases/mobile-development-cookbook.md
```

---

### 📚 Tài liệu & Changelog
> Viết README, API Specs, Docstrings, hoặc cập nhật Changelog

**Giải thích:** Ép AI tuân thủ chuẩn viết doc JSDoc, OpenAPI, Keep a Changelog và cấu trúc README chuẩn.

```
@ai-agent-standards/engineering-practices/DOCUMENTATION_STANDARDS.md
```

---

### 🚀 Phát hành & Git Branching
> Tăng version (SemVer), quản lý nhánh Gitflow, kiểm tra trước khi Release

**Giải thích:** Hướng dẫn AI cách tự tính toán version nhảy bậc (Major/Minor/Patch) và tuân thủ checklist phát hành.

```
@ai-agent-standards/engineering-practices/RELEASE_PROCESS.md
```

---

### 🧪 Chiến lược Test & TDD
> Thiết lập Test Pyramid, ngưỡng Coverage, nguyên tắc FIRST

**Giải thích:** Chuẩn mực ép AI viết test nhanh, cô lập, lặp lại được. Đề cao TDD và mock đúng cách.

```
@ai-agent-standards/engineering-practices/TESTING_STANDARDS.md
```

---

### 🏎️ Hiệu năng & Tối ưu hóa DB
> Caching, truy vấn N+1, xử lý đồng thời, giới hạn thời gian phản hồi

**Giải thích:** Các quy tắc Non-Functional (NFRs) bắt buộc về tốc độ, tối ưu database (không N+1) và thiết lập Caching.

```
@ai-agent-standards/engineering-practices/NON_FUNCTIONAL_REQUIREMENTS.md
```

---

### ⚖️ Tiêu chuẩn Ngành & Tuân thủ
> Đối chiếu OWASP, NIST, CISA

**Giải thích:** Bảng mapping các ràng buộc bảo mật của Repo vào các tiêu chuẩn quản trị rủi ro quốc tế.

```
@ai-agent-standards/compliance/COMPLIANCE.md
```

---

### ♿ Khả năng tiếp cận UI (A11Y)
> Review HTML/React cho người khuyết tật (WCAG 2.1 AA)

**Giải thích:** Checklist bắt buộc về Semantic HTML, ARIA labels, màu sắc tương phản, và điều hướng bằng bàn phím.

```
@ai-agent-standards/compliance/A11Y_CHECKLIST.md
```

---

## Thiết lập Multi-Agent

Khi bạn muốn nhiều AI agent phối hợp, gán file tương ứng làm system instructions cho từng agent:

| Agent | Vai trò | File để load |
|-------|---------|-------------|
| **Coder** | Chỉ viết code, không sửa DB/env/kiến trúc | `@ai-agent-standards/multi-agent/coder-agent.md` |
| **Test** | Chỉ viết test, không sửa production code | `@ai-agent-standards/multi-agent/test-agent.md` |
| **Reviewer** | Chỉ audit & tối ưu, không thêm feature mới | `@ai-agent-standards/multi-agent/reviewer-agent.md` |
| **Documentation** | Chỉ viết tài liệu, không sửa code/test | `@ai-agent-standards/multi-agent/documentation-agent.md` |

**Pipeline:**
```
Coder Agent → Test Agent → Reviewer Agent → Kỹ sư duyệt
                                                  ↓
                                        Documentation Agent
```

**Lưu ý:** Tất cả agent đều tuân thủ quy tắc: **Kỹ sư con người nắm quyền phê duyệt cuối cùng.**

---

## Kết hợp nhiều reference

Với các tác vụ phức tạp, bạn có thể kết hợp nhiều file:

```
# Ví dụ: Xây API bảo mật kèm test

@ai-agent-standards/risk-management/security-constraints.md
@ai-agent-standards/prompts/sample-use-cases/create-api-with-rate-limiting.md
@ai-agent-standards/prompts/PROMPT-TEMPLATE.md

Tạo endpoint POST /api/v1/register với:
- Kiểm tra email trùng lặp
- Hash password bằng bcrypt
- Trả JWT token
- Viết kèm unit tests và Self-Check report
```

**Mẹo:** Bạn có thể viết yêu cầu bằng Tiếng Việt — agent vẫn hiểu. Nhưng các lệnh `@reference` phải giữ nguyên đường dẫn Tiếng Anh.

---

## Kiểm tra Agent đã load đúng skill chưa

Bất cứ lúc nào, hỏi agent:

> **"What coding standards are you following?"** hoặc gõ **`/standards`**

Kết quả mong đợi:
> ✅ **AI-Coding-Standards v2.4.0** with 6 Core Principles active.
> Framework: Controlled AI-Assisted Development  
> Principles: (1) Think Before Coding, (2) Simplicity First, (3) Surgical Changes, (4) Goal-Driven Execution, (5) DRY & Reusability, (6) Code Organization

Nếu agent không trả về format trên → file instruction chưa được load. Kiểm tra lại file có nằm đúng root project không.
