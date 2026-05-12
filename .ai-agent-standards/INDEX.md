# INDEX - Bảng Mục Lục Chung AI Agent Coding Standards

**Hướng dẫn tìm file bạn cần trong framework này.**

---

## 🎯 Theo Mục đích (Dành cho...)

### Kỹ Sư Mới

| File | Mục đích | Độ ưu tiên |
|------|---------|-----------|
| [`README.md`](README.md) | Overview & quick-start | ⭐⭐⭐ |
| [`onboarding/quick-reference.md`](onboarding/quick-reference.md) | Cheat sheet 1 trang (in được) | ⭐⭐⭐ |
| [`onboarding/first-task-walkthrough.md`](onboarding/first-task-walkthrough.md) | Hướng dẫn chi tiết task đầu | ⭐⭐⭐ |
| [`onboarding/common-mistakes.md`](onboarding/common-mistakes.md) | Lỗi phổ biến & cách tránh | ⭐⭐ |
| [`prompts/PROMPT-TEMPLATE.md`](prompts/PROMPT-TEMPLATE.md) | Khuôn mẫu prompt chuẩn | ⭐⭐ |

### Code Reviewer / QA

| File | Mục đích | Độ ưu tiên |
|------|---------|-----------|
| [`quality-control/code-review-checklist.md`](quality-control/code-review-checklist.md) | Checklist reviewer bắt buộc | ⭐⭐⭐ |
| [`quality-control/audit-ai-code-full.md`](quality-control/audit-ai-code-full.md) | Checklist audit chi tiết | ⭐⭐⭐ |
| [`quality-control/hallucination-detection.md`](quality-control/hallucination-detection.md) | Cách phát hiện lỗi AI | ⭐⭐ |
| [`reference/error-reference-complete.md`](reference/error-reference-complete.md) | Bảng lỗi AI thường gặp | ⭐⭐ |

### Kỹ Sư Kỳ Cựu / Tech Lead

| File | Mục đích | Độ ưu tiên |
|------|---------|-----------|
| [`quality-control/`](quality-control/) | Toàn bộ Pipeline kiểm soát | ⭐⭐⭐ |
| [`risk-management/escalation-workflow.md`](risk-management/escalation-workflow.md) | Xử lý khi AI không hợp tác | ⭐⭐⭐ |
| [`risk-management/security-constraints.md`](risk-management/security-constraints.md) | Non-negotiable constraints | ⭐⭐⭐ |
| [`prompts/sample-use-cases/`](prompts/sample-use-cases/) | Mẫu prompt cho từng use case | ⭐⭐⭐ |
| [`metrics/kpi-definitions.md`](metrics/kpi-definitions.md) | Định nghĩa KPIs chi tiết | ⭐⭐ |

### Quản Lý / Product Owner

| File | Mục đích | Độ ưu tiên |
|------|---------|-----------|
| [`reference/methodology-for-management.md`](reference/methodology-for-management.md) | Giải thích phương pháp | ⭐⭐⭐ |
| [`metrics/kpi-definitions.md`](metrics/kpi-definitions.md) | Metrics & ROI tracking | ⭐⭐⭐ |
| [`metrics/sample-weekly-report.md`](metrics/sample-weekly-report.md) | Ví dụ báo cáo | ⭐⭐ |
| [`risk-management/cost-control-policy.md`](risk-management/cost-control-policy.md) | Kiểm soát chi phí AI | ⭐⭐ |

---

## 📁 Theo Thư Mục

### 📂 `prompts/` - Thư viện Prompt Mẫu
Cấu trúc prompt chuẩn hóa & ví dụ cho các use case phổ biến.

| File | Nội dung |
|------|---------|
| [`prompts/README.md`](prompts/README.md) | Hướng dẫn sử dụng thư viện |
| [`prompts/HEADER-TEMPLATE.yaml`](prompts/HEADER-TEMPLATE.yaml) | YAML header chuẩn cho mỗi prompt |
| [`prompts/PROMPT-TEMPLATE.md`](prompts/PROMPT-TEMPLATE.md) | Khuôn mẫu prompt (Context → Task → Constraints → Output) |
| **Use Cases:** |  |
| [`create-api-with-rate-limiting.md`](prompts/sample-use-cases/create-api-with-rate-limiting.md) | API endpoint + xác thực + rate limiting |
| [`refactor-cache-strategy.md`](prompts/sample-use-cases/refactor-cache-strategy.md) | Tối ưu cache & performance |
| [`generate-unit-tests.md`](prompts/sample-use-cases/generate-unit-tests.md) | Tự động sinh unit tests |
| [`security-audit.md`](prompts/sample-use-cases/security-audit.md) | Kiểm tra lỗ hổng bảo mật |
| [`database-migration.md`](prompts/sample-use-cases/database-migration.md) | Schema migration an toàn |
| [`indexed-by-category.md`](prompts/indexed-by-category.md) | Chỉ mục phân loại prompts |

---

### 📂 `templates/` - Template Reusable

| File | Mục đích |
|------|---------|
| [`templates/README.md`](templates/README.md) | Hướng dẫn về templates |
| [`templates/project-cursorrules-template`](templates/project-cursorrules-template) | Template `.cursorrules` cho project mới |
| [`templates/project-structure-template.md`](templates/project-structure-template.md) | Gợi ý cấu trúc project tối ưu |
| [`templates/task-description-template.md`](templates/task-description-template.md) | Mẫu task trong Jira/Trello |

---

### 📂 `quality-control/` - Pipeline Kiểm soát Chất lượng

| File | Nội dung |
|------|---------|
| [`quality-control/README.md`](quality-control/README.md) | Tổng quan Pipeline |
| [`quality-control/self-check-report-template.md`](quality-control/self-check-report-template.md) | Mẫu báo cáo tự kiểm tra (Phụ lục C) |
| [`quality-control/code-review-checklist.md`](quality-control/code-review-checklist.md) | Checklist cho reviewer **[BẮTBUỘC]** |
| [`quality-control/audit-ai-code-full.md`](quality-control/audit-ai-code-full.md) | Checklist audit chi tiết (bản mở rộng Phụ lục B) |
| [`quality-control/hallucination-detection.md`](quality-control/hallucination-detection.md) | Nhận diện & xử lý hallucination |
| [`quality-control/ci-cd-gates.md`](quality-control/ci-cd-gates.md) | Quy tắc CI/CD integration |

---

### 📂 `risk-management/` - Quản Lý Rủi ro

| File | Nội dung |
|------|---------|
| [`risk-management/README.md`](risk-management/README.md) | Tổng quan Risk Management |
| [`risk-management/security-constraints.md`](risk-management/security-constraints.md) | Lớp nền Tiên quyết (Non-Negotiable) |
| [`risk-management/ai-failure-log-template.md`](risk-management/ai-failure-log-template.md) | Mẫu ghi nhận lỗi AI |
| [`risk-management/escalation-workflow.md`](risk-management/escalation-workflow.md) | Quy trình leo thang khi AI không hợp tác |
| [`risk-management/cost-control-policy.md`](risk-management/cost-control-policy.md) | Kiểm soát chi phí API sử dụng |
| [`risk-management/incident-response-plan.md`](risk-management/incident-response-plan.md) | Kế hoạch ứng phó sự cố |
| [`risk-management/mitigation-strategies.md`](risk-management/mitigation-strategies.md) | Chiến lược giảm thiểu rủi ro |

---

### 📂 `metrics/` - Tracking KPIs & Performance

| File | Nội dung |
|------|---------|
| [`metrics/README.md`](metrics/README.md) | Hướng dẫn setup metrics |
| [`metrics/kpi-definitions.md`](metrics/kpi-definitions.md) | Định nghĩa chi tiết từng KPI |
| [`metrics/tracking-template.csv`](metrics/tracking-template.csv) | CSV template log task AI-Assisted |
| [`metrics/sample-weekly-report.md`](metrics/sample-weekly-report.md) | Ví dụ báo cáo hàng tuần |
| [`metrics/dashboard-guide.md`](metrics/dashboard-guide.md) | Hướng dẫn setup dashboard |
| [`metrics/analysis-queries.sql`](metrics/analysis-queries.sql) | Query SQL sample trích xuất metrics |

---

### 📂 `onboarding/` - Training & Hướng dẫn (Simplified)

| File | Nội dung |
|------|---------|
| [`onboarding/README.md`](onboarding/README.md) | Tổng quan onboarding program |
| [`onboarding/quick-reference.md`](onboarding/quick-reference.md) | **Cheat sheet 1 trang - IN RA ĐƯỢC** ⭐ |
| [`onboarding/first-task-walkthrough.md`](onboarding/first-task-walkthrough.md) | Hướng dẫn task đầu tiên chi tiết |
| [`onboarding/common-mistakes.md`](onboarding/common-mistakes.md) | Lỗi phổ biến & cách tránh |

---

### 📂 `multi-agent/` - Multi-Agent Framework (P2 Placeholder)

| File | Nội dung |
|------|---------|
| [`multi-agent/README.md`](multi-agent/README.md) | Tổng quan phần này (P2) |
| [`multi-agent/roadmap.md`](multi-agent/roadmap.md) | Lộ trình phát triển |
| [`multi-agent/orchestration-design.md`](multi-agent/orchestration-design.md) | Thiết kế sơ bộ (để phát triển) |

---

### 📂 `reference/` - Tài Liệu Tham chiếu

| File | Nội dung |
|------|---------|
| [`reference/README.md`](reference/README.md) | Hướng dẫn thư mục reference |
| [`reference/error-reference-complete.md`](reference/error-reference-complete.md) | Bảng lỗi AI thường gặp (Phụ lục B mở rộng) |
| [`reference/use-case-cookbook.md`](reference/use-case-cookbook.md) | Ví dụ chi tiết (Phụ lục A) |
| [`reference/methodology-for-management.md`](reference/methodology-for-management.md) | Giải thích phương pháp cho quản lý (Phụ lục F) |
| [`reference/glossary.md`](reference/glossary.md) | Thuật ngữ & định nghĩa |
| [`reference/external-links.md`](reference/external-links.md) | Liên kết tài liệu bên ngoài |

---

## 🔗 Root Level Files

| File | Mục đích |
|------|---------|
| `.cursorrules` | Quy tắc Cursor/Windsurf mặc định cho project |
| `.gitignore` | Loại trừ file nhạy cảm (API keys, secrets) |
| `README.md` | Quick-start guide tổng quát |
| `INDEX.md` | **File này** - bảng mục lục |
| `CHANGELOG.md` | Lịch sử phiên bản & cập nhật |

---

## 🎯 Quick Navigation

### "Tôi muốn..."

| Nhu cầu | Đi tới |
|--------|--------|
| Bắt đầu nhanh | [`README.md`](README.md) + [`onboarding/quick-reference.md`](onboarding/quick-reference.md) |
| Review code AI | [`quality-control/code-review-checklist.md`](quality-control/code-review-checklist.md) |
| Viết prompt mẫu | [`prompts/PROMPT-TEMPLATE.md`](prompts/PROMPT-TEMPLATE.md) + [`prompts/sample-use-cases/`](prompts/sample-use-cases/) |
| Xử lý lỗi AI | [`risk-management/escalation-workflow.md`](risk-management/escalation-workflow.md) |
| Track metrics | [`metrics/tracking-template.csv`](metrics/tracking-template.csv) |
| Báo cáo cho quản lý | [`metrics/sample-weekly-report.md`](metrics/sample-weekly-report.md) |
| Tìm giải pháp lỗi | [`reference/error-reference-complete.md`](reference/error-reference-complete.md) |
| Hiểu phương pháp | [`reference/methodology-for-management.md`](reference/methodology-for-management.md) |

---

## 📊 File Statistics

| Loại | Số lượng |
|------|---------|
| Thư mục chính | 8 |
| File hướng dẫn (README) | 9 |
| Prompt mẫu | 5 |
| Checklist & templates | 8+ |
| Tài liệu tham chiếu | 6 |
| **Tổng cộng** | **40+** |

---

## ✅ Validation Checklist

Khi setup project mới, kiểm tra:
- [ ] Tất cả 8 folder được copy
- [ ] `.cursorrules` được update cho tech stack
- [ ] `.gitignore` loại trừ secrets
- [ ] `README.md` & `INDEX.md` accessible
- [ ] Team đã review `onboarding/quick-reference.md`
- [ ] Metrics tracking được setup

---

## 🔄 Version Info

- **Framework Version:** 1.0.0
- **Last Updated:** 2026-05-12
- **Status:** ✓ Production Ready

---

**Cần tìm gì? Sử dụng Ctrl+F để search hoặc xem bảng ở trên.**

**Gợi ý: Nếu mới, hãy bắt đầu từ [`onboarding/quick-reference.md`](onboarding/quick-reference.md) 👉**
