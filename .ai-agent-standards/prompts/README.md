# Thư viện Prompt - Hướng dẫn Sử dụng

Thư mục này chứa các mẫu prompt chuẩn hóa cho các use case phổ biến trong phát triển phần mềm.

---

## 📋 Cấu trúc Thư mục

```
prompts/
├── README.md                          (file này)
├── HEADER-TEMPLATE.yaml               (template YAML header)
├── PROMPT-TEMPLATE.md                 (khuôn mẫu prompt)
├── indexed-by-category.md             (chỉ mục phân loại)
└── sample-use-cases/
    ├── create-api-with-rate-limiting.md
    ├── refactor-cache-strategy.md
    ├── generate-unit-tests.md
    ├── security-audit.md
    └── database-migration.md
```

---

## 🚀 Cách Sử dụng Prompt

### 1. Chọn Prompt Phù hợp
- Xem [`indexed-by-category.md`](indexed-by-category.md) để tìm use case của bạn
- Hoặc duyệt [`sample-use-cases/`](sample-use-cases/) cho ví dụ trực tiếp

### 2. Copy Prompt Mẫu
```bash
# Copy nội dung prompt vào IDE hoặc chat interface
# Ví dụ: Copy nội dung create-api-with-rate-limiting.md
```

### 3. Tuỳ Chỉnh cho Project
- Update `[CONTEXT]` section với tech stack cụ thể
- Thay đổi constraint nếu cần (ví dụ: framework khác)
- Giữ nguyên `[TASK]` hoặc customize chi tiết cần thiết

### 4. Gửi cho AI & Xử lý Output
- Paste prompt vào Claude / ChatGPT / Copilot
- AI sẽ tự chạy Self-Check (nếu được hướng dẫn trong prompt)
- Xem [`quality-control/self-check-report-template.md`](../quality-control/self-check-report-template.md) để verify

### 5. Lưu Kết quả
Ghi lại: `prompt_id`, `prompt_version`, `ai_iteration_count` vào task (xem [`metrics/tracking-template.csv`](../metrics/tracking-template.csv))

---

## 📝 Khuôn Mẫu Header (YAML)

Mỗi prompt file phải bắt đầu với:

```yaml
---
id: PROMPT-001                                    # Duy nhất ID
version: 1.0                                      # Phiên bản
author: [Tên kỹ sư]                              # Người tạo
last_updated: 2026-05-12                         # Ngày cập nhật cuối
applicable_stack: [React, Node.js, PostgreSQL]   # Tech stack phù hợp
category: API_Development                        # Phân loại
difficulty: Intermediate                         # Độ khó: Simple/Intermediate/Complex
---
```

---

## 🎯 Khuôn Mẫu Prompt Tiêu chuẩn (Phần III.2)

```markdown
### [CONTEXT - NGỮ CẢNH HỆ THỐNG]
- Tech stack: [VD: React v18, Node.js, PostgreSQL]
- Trạng thái hiện tại: [Mô tả kỹ thuật tóm tắt]
- Schema/Interfaces: [Cung cấp cấu trúc dữ liệu]

### [TASK - YÊU CẦU NGHIỆP VỤ]
- Mục tiêu: [Mô tả chi tiết & độc lập 1 tính năng]
- Acceptance Criteria: [Danh sách clear conditions]

### [CONSTRAINTS - RÀNG BUỘC KỸ THUẬT CỨNG]
- HÀNH VI BỊ CẤM: [VD: Không sửa file .env]
- YÊU CẦU BẮT BUỘC: [VD: Try-catch bắt buộc, bổ sung comments]
- Quy trình: Bắt buộc chạy Self-Check (Phần III.4)

### [OUTPUT FORMAT - ĐỊNH DẠNG ĐẦU RA]
- [VD: Chỉ xuất code thay đổi, kèm Self-Check report]
```

---

## ✨ Best Practices

### Khi Viết Prompt Mới

1. **Single-Task Prompting:** 1 prompt = 1 tính năng rõ ràng
   - ❌ Sai: "Xây dựng toàn bộ authentication module"
   - ✅ Đúng: "Tạo endpoint POST /login với JWT + rate limiting"

2. **Context Tối ưu:** Cung cấp context đủ nhưng không quá
   - Gồm schema, interfaces, existing code snippet
   - Không paste cả codebase vào (tốn token)

3. **Constraints Rõ ràng:** Liệt kê chi tiết những gì AI **KHÔNG ĐƯỢC** làm
   - "Không import thư viện ngoài [list]"
   - "Bắt buộc sử dụng [specific pattern]"

4. **Output Format Cụ thể:** Định rõ format kỳ vọng
   - "Chỉ code, không giải thích"
   - "JSON format + Self-Check report"

### Khi Dùng Prompt

1. **Cập nhật YAML header** với info cụ thể (author, version)
2. **Test prompt** trên 1 model trước (ví dụ: Claude)
3. **Lưu prompt version** khi prove effective
4. **Update indexed-by-category.md** nếu là prompt mới

---

## 📊 Prompt Library Stats

| Loại | Số lượng | Status |
|------|---------|--------|
| Sample Use Cases | 5 | ✓ Ready |
| Template Templates | 2 | ✓ Ready |
| Advanced Prompts | TBD | Upcoming |

---

## 🔄 Vòng Đời Prompt

```
1. CREATE (Kỹ sư tạo prompt mới)
   ↓
2. TEST (Thử trên model, verify output)
   ↓
3. SAVE (Commit vào repo, update indexed-by-category.md)
   ↓
4. TRACK (Log prompt_id khi dùng trong tasks)
   ↓
5. ITERATE (Cải tiến dựa trên metrics)
```

---

## 📋 Danh Sách Use Cases Có Sẵn

1. **`create-api-with-rate-limiting.md`** - API endpoint + auth + rate limit
2. **`refactor-cache-strategy.md`** - Tối ưu caching & performance
3. **`generate-unit-tests.md`** - Sinh unit tests tự động
4. **`security-audit.md`** - Kiểm tra lỗ hổng bảo mật
5. **`database-migration.md`** - Schema migration an toàn

---

## 🆘 Troubleshooting

| Vấn đề | Giải pháp |
|--------|---------|
| AI output không phù hợp | Review lại [CONSTRAINTS] section, có thể chưa đủ chi tiết |
| Output quá dài | Thêm "Output Format: Chỉ code, không giải thích" |
| AI không tuân thủ pattern | Thêm ví dụ cụ thể trong context |
| Lặp lại lỗi tương tự | Update prompt, lưu version mới, track metrics |

---

## 🔗 Reference

- Template: [`PROMPT-TEMPLATE.md`](PROMPT-TEMPLATE.md)
- Header: [`HEADER-TEMPLATE.yaml`](HEADER-TEMPLATE.yaml)
- Chỉ mục: [`indexed-by-category.md`](indexed-by-category.md)
- Self-Check: [`../quality-control/self-check-report-template.md`](../quality-control/self-check-report-template.md)
- Full Standards: Tài liệu gốc "AI Agent Coding - Phần II & III"

---

**Ghi chú:** Prompt library này sẽ được mở rộng dần khi có thêm kinh nghiệm. Đóng góp prompt mới vào thư mục này & commit vào repo.
