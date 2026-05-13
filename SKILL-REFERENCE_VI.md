# Hướng Dẫn Sử Dụng Skill — Tra Cứu Nhanh

**Bạn cần reference file nào cho từng loại công việc?**

Sao chép các lệnh `@file` bên dưới vào prompt của bạn để kích hoạt skill tương ứng cho AI agent.

---

## Công việc hàng ngày (không cần reference thêm)

AI agent **đã tự động load** 4 Nguyên tắc Karpathy từ file gốc (`CLAUDE.md`, `GEMINI.md`, v.v.) ngay khi mở project. Bạn chỉ cần mô tả yêu cầu bình thường — agent sẽ tự tuân thủ các nguyên tắc:

1. **Think Before Coding** — Nêu giả định, hỏi khi không rõ
2. **Simplicity First** — Code tối thiểu, không thêm tính năng dư thừa
3. **Surgical Changes** — Chỉ sửa đúng phần cần thiết
4. **Goal-Driven Execution** — Xác định tiêu chí thành công trước khi code

**→ Không cần gõ thêm gì. Agent đã biết.**

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

**Giải thích:** Cookbook tiêu chuẩn cho phát triển ứng dụng di động. Bao gồm: 10 lỗi thường gặp khi AI sinh code mobile (main thread blocking, context leak, lifecycle, hardcoded strings...), cấu trúc thư mục mẫu cho 3 nền tảng, và Self-Check report chuyên mobile.

```
@ai-agent-standards/prompts/sample-use-cases/mobile-development-cookbook.md
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
> ✅ **AI-Agent-Coding Standards v1.3** with Karpathy Principles active.  
> Framework: Controlled AI-Assisted Development  
> Principles: (1) Think Before Coding, (2) Simplicity First, (3) Surgical Changes, (4) Goal-Driven Execution

Nếu agent không trả về format trên → file instruction chưa được load. Kiểm tra lại file có nằm đúng root project không.
