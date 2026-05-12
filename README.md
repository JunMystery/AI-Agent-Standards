# AI Agent Coding Standards - Framework Phát triển Có kiểm soát

**Phiên bản:** 1.0.0 | **Ngày release:** 2026-05-12 | **Status:** ✓ Active

---

## 📋 Tổng quan

Framework này tiêu chuẩn hóa phương pháp tích hợp AI Agents vào quy trình phát triển phần mềm **một cách an toàn, hiệu quả và kiểm soát được**.

**Triết lý cốt lõi:** AI là công cụ hỗ trợ (tool), không phải hệ thống ra quyết định. Kỹ sư luôn giữ quyền kiểm duyệt (human gate) đối với mọi output.

---

## 🚀 Quick Start (5 phút)

### Cho Kỹ sư Mới

1. **Đọc tài liệu:**
   - [`onboarding/quick-reference.md`](onboarding/quick-reference.md) (1 trang - in ra được)
   - [`onboarding/first-task-walkthrough.md`](onboarding/first-task-walkthrough.md) (ví dụ chi tiết)

2. **Setup project mới:**
   ```bash
   # Copy folder này vào project
   cp -r .ai-agent-standards /path/to/your/project/
   
   # Update .cursorrules nếu cần
   # Edit: .ai-agent-standards/.cursorrules
   ```

3. **Thực hiện task đầu tiên:**
   - Làm theo hướng dẫn [`first-task-walkthrough.md`](onboarding/first-task-walkthrough.md)
   - Áp dụng Pipeline kiểm soát từ [`quality-control/`](quality-control/)
   - Ghi lại metrics trong [`metrics/`](metrics/)

---

## 📁 Cấu trúc Thư mục & Mục đích

| Folder | Mục đích | Key Files |
|--------|---------|-----------|
| **`prompts/`** | Thư viện Prompt mẫu chuẩn | `HEADER-TEMPLATE.yaml`, 5 sample prompts |
| **`templates/`** | Template reusable cho project mới | `.cursorrules`, task templates |
| **`quality-control/`** | Pipeline kiểm soát chất lượng | Self-Check, Code Review, Audit checklists |
| **`risk-management/`** | Quản lý rủi ro & escalation | Failure Log, Security constraints, Mitigation |
| **`metrics/`** | Tracking KPIs & performance | KPI definitions, CSV tracking, reports |
| **`onboarding/`** | Training & hướng dẫn (simplified) | Quick-ref, walkthrough, common mistakes |
| **`multi-agent/`** | P2 Roadmap | Placeholder cho Multi-Agent framework |
| **`reference/`** | Tài liệu tham chiếu | Error tables, Cookbook, Glossary |

**Xem chi tiết:** [`INDEX.md`](INDEX.md)

---

## 🔄 7 Bước Pipeline Tiêu chuẩn

```
1. PHÂN TÍCH & PHÂN RÃ
   ↓
2. THIẾT KẾ DỮ LIỆU ĐỘC LẬP  (Kỹ sư quyết định)
   ↓
3. ÁP ĐẶT NGUYÊN TẮC KIẾN TRÚC
   ↓
4. PHÁT TRIỂN BOTTOM-UP  (Core → Services → UI)
   ↓
5. VẬN HÀNH PIPELINE KIỂM SOÁT ⚙️
   - AI Generate → Self-Check → Self-Fix → Output
   ↓
6. HUMAN GATE - CỔNG KIỂM DUYỆT 👤
   [APPROVE] → Merge + Checkpoint Backup
   [REJECT] → Iterate
   ↓
7. TỰ ĐỘNG HÓA TÀI LIỆU
   (API specs, README updates)
```

**Chi tiết:** [`quality-control/`](quality-control/)

---

## 📊 Kiểm soát Rủi ro

### Non-Negotiable Constraints (Lớp nền)
- ✓ **Bảo mật Zero-Trust:** Không nhúng API keys, passwords, PII vào prompt
- ✓ **Xác thực dữ liệu:** Bắt buộc input validation/sanitization
- ✓ **Tuân thủ kiến trúc:** Không phá vỡ design patterns hiện hành

**Xem thêm:** [`risk-management/security-constraints.md`](risk-management/security-constraints.md)

### Escalation Path
Khi AI không hợp tác (>2 vòng Self-Fix):
1. Ghi nhận AI Failure Log
2. Kỹ sư phân tích nguyên nhân
3. Thay đổi strategy prompt hoặc tự code thủ công
4. Update prompt library để tránh lặp lại

**Chi tiết:** [`risk-management/escalation-workflow.md`](risk-management/escalation-workflow.md)

---

## 📈 Metrics & KPIs

Theo dõi hiệu quả AI-Assisted development:
- **Defect Rate** (lỗi hồi quy)
- **Cycle Time** (thời gian hoàn thành)
- **Test Coverage** (độ bao phủ unit tests)
- **AI Iteration Count** (số vòng lặp Self-Fix)
- **Technical Debt Ratio**

**Template:** [`metrics/tracking-template.csv`](metrics/tracking-template.csv)
**Sample Report:** [`metrics/sample-weekly-report.md`](metrics/sample-weekly-report.md)

---

## 💡 Key Files to Read First

1. **Bạn là Kỹ sư mới:** 
   - [`onboarding/quick-reference.md`](onboarding/quick-reference.md) ⭐
   - [`onboarding/first-task-walkthrough.md`](onboarding/first-task-walkthrough.md)

2. **Bạn làm reviewer:**
   - [`quality-control/code-review-checklist.md`](quality-control/code-review-checklist.md)
   - [`quality-control/audit-ai-code-full.md`](quality-control/audit-ai-code-full.md)

3. **Bạn là quản lý:**
   - [`reference/methodology-for-management.md`](reference/methodology-for-management.md)
   - [`metrics/kpi-definitions.md`](metrics/kpi-definitions.md)

4. **Bạn cần Prompt mẫu:**
   - [`prompts/PROMPT-TEMPLATE.md`](prompts/PROMPT-TEMPLATE.md)
   - [`prompts/sample-use-cases/`](prompts/sample-use-cases/)

---

## 🛠️ Integration với Project Hiện tại

### Copy vào Project Mới
```bash
# 1. Copy folder
cp -r .ai-agent-standards /your/project/

# 2. Update .cursorrules nếu cần (tech stack specific)
# Edit: your-project/.ai-agent-standards/.cursorrules

# 3. Commit vào Git
git add .ai-agent-standards/
git commit -m "chore: add AI Agent Coding Standards framework"

# 4. Tạo task đầu tiên với label: [AI-Assisted]
# Áp dụng: quality-control/ pipeline
```

### Một dự án, nhiều phiên bản?
- Mỗi project copy riêng (không dùng submodule)
- Update khi có phiên bản mới từ repo gốc
- Track phiên bản via `CHANGELOG.md`

---

## 📞 Tham chiếu Nhanh

| Cần gì? | Tìm ở đây |
|--------|----------|
| Prompt mẫu | [`prompts/sample-use-cases/`](prompts/sample-use-cases/) |
| Checklist reviewer | [`quality-control/code-review-checklist.md`](quality-control/code-review-checklist.md) |
| Lỗi AI thường gặp | [`reference/error-reference-complete.md`](reference/error-reference-complete.md) |
| Tracking metrics | [`metrics/tracking-template.csv`](metrics/tracking-template.csv) |
| Training | [`onboarding/`](onboarding/) |
| Escalation | [`risk-management/escalation-workflow.md`](risk-management/escalation-workflow.md) |

---

## ✅ Verification Checklist

Sau khi setup, kiểm tra:
- [ ] Tất cả 8 subfolder được tạo
- [ ] `.cursorrules` đã cấu hình cho tech stack của bạn
- [ ] Đã commit vào Git
- [ ] Kỹ sư mới đã đọc `onboarding/quick-reference.md`
- [ ] Reviewer đã xem `quality-control/code-review-checklist.md`

---

## 📝 License & Attribution

Framework này dựa trên "Phương pháp luận AI Agent Coding" - Tài liệu Tiêu chuẩn Kỹ thuật.
- **Tác giả tài liệu gốc:** Nguyễn Hoàng Thanh Tú
- **Status:** ✓ Open framework cho team sử dụng & extend

---

## 🔗 Liên kết Toàn bộ

👉 **Chi tiết đầy đủ:** [`INDEX.md`](INDEX.md)

---

**Câu hỏi? Xem:** [`onboarding/`](onboarding/) hoặc gửi feedback cho team lead.

**Muốn extend framework? Cập nhật** [`CHANGELOG.md`](CHANGELOG.md) **và commit.**

---

*Phiên bản này được kiểm duyệt & sẵn sàng sử dụng.*
