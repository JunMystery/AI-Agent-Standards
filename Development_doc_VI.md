TÀI LIỆU TIÊU CHUẨN KỸ THUẬT

**Tên tài liệu:** Phương pháp luận AI Agent Coding – Quy trình có kiểm soát dành cho Kỹ sư Hệ thống  
**Chịu trách nhiệm nội dung:** Nguyễn Hoàng Thanh Tú  
**Mục tiêu tài liệu:** Tiêu chuẩn hóa phương pháp, thiết lập các nguyên tắc ứng dụng thực tiễn và xây dựng lộ trình phát triển năng lực tích hợp AI trong quy trình phát triển phần mềm.  

---

TÓM TẮT NỘI DUNG (ABSTRACT)

Tài liệu này trình bày khuôn khổ làm việc (framework) nhằm tích hợp AI Agents vào quy trình phát triển phần mềm một cách an toàn và hiệu quả.  
Trọng tâm là dịch chuyển từ mô hình lập trình thủ công sang mô hình “Phát triển có kiểm soát với AI” (Controlled AI-Assisted Development), nhấn mạnh vai trò của kỹ sư trong việc định hướng kiến trúc, kiểm soát bảo mật và quản trị rủi ro hệ thống.  
Phiên bản 2.1 bổ sung các hướng dẫn thực hành chi tiết, quy trình làm việc nhóm, kiểm soát chi phí, chiến lược xử lý ngoại lệ và lộ trình áp dụng mở rộng.

---

## MỤC LỤC

1. [PHẦN I: TỔNG QUAN VÀ TRIẾT LÝ VẬN HÀNH](#phần-i-tổng-quan-và-triết-lý-vận-hành)  
   1.1. [Bối cảnh và Sự phân hóa phương pháp](#11-bối-cảnh-và-sự-phân-hóa-phương-pháp)  
   1.2. [Triết lý tiếp cận "Vibe-Proof"](#12-triết-lý-tiếp-cận-vibe-proof)  
2. [PHẦN II: CHUẨN BỊ MÔI TRƯỜNG VÀ CẤU HÌNH](#phần-ii-chuẩn-bị-môi-trường-và-cấu-hình)  
   2.1. [Đánh giá Công cụ tích hợp (Tooling Stack)](#21-đánh-giá-công-cụ-tích-hợp-tooling-stack)  
   2.2. [Tiêu chuẩn hóa Ngữ cảnh & Cấu hình (Context Management)](#22-tiêu-chuẩn-hóa-ngữ-cảnh--cấu-hình-context-management)  
   2.3. [Quản trị Thư viện Prompt và Kiểm soát Phiên bản](#23-quản-trị-thư-viện-prompt-và-kiểm-soát-phiên-bản)  
3. [PHẦN III: QUY TRÌNH THỰC THI TIÊU CHUẨN](#phần-iii-quy-trình-thực-thi-tiêu-chuẩn)  
   3.1. [Lớp nền Tiên quyết (Non-Negotiable Constraints)](#31-lớp-nền-tiên-quyết-non-negotiable-constraints)  
   3.2. [Khuôn mẫu Prompt Tiêu chuẩn](#32-khuôn-mẫu-prompt-tiêu-chuẩn)  
   3.3. [Trình tự 7 Bước Triển khai](#33-trình-tự-7-bước-triển-khai)  
   3.4. [Pipeline Kiểm soát Chất lượng (AI Control Pipeline)](#34-pipeline-kiểm-soát-chất-lượng-ai-control-pipeline)  
   3.5. [Xử lý Ngoại lệ và Leo thang khi AI không hợp tác](#35-xử-lý-ngoại-lệ-và-leo-thang-khi-ai-không-hợp-tác)  
   3.6. [Tích hợp Pipeline vào Quy trình Nhóm (Scrum/Kanban)](#36-tích-hợp-pipeline-vào-quy-trình-nhóm-scrumkanban)  
4. [PHẦN IV: KIỂM SOÁT RỦI RO & ĐẢM BẢO CHẤT LƯỢNG](#phần-iv-kiểm-soát-rủi-ro--đảm-bảo-chất-lượng)  
   4.1. [Kiểm soát Hiện tượng AI Sinh thông tin sai lệch (Hallucination)](#41-kiểm-soát-hiện-tượng-ai-sinh-thông-tin-sai-lệch-hallucination)  
   4.2. [Rủi ro Pháp lý và Bản quyền](#42-rủi-ro-pháp-lý-và-bản-quyền)  
   4.3. [Tích hợp CI/CD và Kiểm thử Tự động](#43-tích-hợp-cicd-và-kiểm-thử-tự-động)  
   4.4. [Kiểm soát Nợ Kỹ thuật Đặc thù từ AI](#44-kiểm-soát-nợ-kỹ-thuật-đặc-thù-từ-ai)  
   4.5. [Quản trị Chi phí Sử dụng AI (API Cost)](#45-quản-trị-chi-phí-sử-dụng-ai-api-cost)  
5. [PHẦN V: ĐO LƯỜNG HIỆU SUẤT & QUẢN TRỊ TRI THỨC](#phần-v-đo-lường-hiệu-suất--quản-trị-tri-thức)  
   5.1. [Đo lường Định lượng (Metrics & KPIs)](#51-đo-lường-định-lượng-metrics--kpis)  
   5.2. [Chiến lược Quản trị Tri thức & Nâng cấp Kỹ năng](#52-chiến-lược-quản-trị-tri-thức--nâng-cấp-kỹ-năng)  
   5.3. [Lộ trình Đào tạo và Onboarding Kỹ sư Mới](#53-lộ-trình-đào-tạo-và-onboarding-kỹ-sư-mới)  
6. [PHẦN VI: LỘ TRÌNH PHÁT TRIỂN & PHỤ LỤC](#phần-vi-lộ-trình-phát-triển--phụ-lục)  
   6.1. [Hạng mục Chờ nghiên cứu (Living Document Placeholders)](#61-hạng-mục-chờ-nghiên-cứu-living-document-placeholders)  
   6.2. [Phụ lục A: Cookbook Tình huống Điển hình](#62-phụ-lục-a-cookbook-tình-huống-điển-hình)  
   6.3. [Phụ lục B: Bảng Lỗi Thường gặp của AI và Cách Xử lý](#63-phụ-lục-b-bảng-lỗi-thường-gặp-của-ai-và-cách-xử-lý)  
   6.4. [Phụ lục C: Mẫu Báo cáo Tự kiểm tra (Self-Check Report)](#64-phụ-lục-c-mẫu-báo-cáo-tự-kiểm-tra-self-check-report)  
   6.5. [Phụ lục D: Cấu trúc Thư viện Prompt Mẫu](#65-phụ-lục-d-cấu-trúc-thư-viện-prompt-mẫu)  
   6.6. [Phụ lục E: Kịch bản Mở rộng Multi-Agent](#66-phụ-lục-e-kịch-bản-mở-rộng-multi-agent)  
   6.7. [Phụ lục F: Diễn giải Phương pháp luận trong Quản trị](#67-phụ-lục-f-diễn-giải-phương-pháp-luận-trong-quản-trị)  

---

## PHẦN I: TỔNG QUAN VÀ TRIẾT LÝ VẬN HÀNH

### 1.1. Bối cảnh và Sự phân hóa phương pháp
Ngành công nghiệp phần mềm đang chứng kiến sự phân hóa rõ rệt giữa hai phương pháp ứng dụng AI:

- **Agentic Coding (Tiếp cận có hệ thống):** Sử dụng AI như một trợ lý chuyên biệt, hoạt động dưới các ràng buộc và sự kiểm duyệt chặt chẽ. Phương pháp này đang tối ưu hóa chu kỳ phát triển tại các tập đoàn công nghệ lớn.
- **Vibe Coding (Tiếp cận cảm tính):** Phó mặc luồng xử lý logic cho AI, áp dụng chu trình “thử và sai” liên tục mà thiếu sự đánh giá chuyên môn. Đây là phương pháp tiềm ẩn rủi ro hệ thống nghiêm trọng (Ví dụ: Sự cố AI Agent tự động xóa cơ sở dữ liệu production chỉ trong 9 giây).

### 1.2. Triết lý tiếp cận “Vibe-Proof”
Để đảm bảo chất lượng và tính bảo mật, bộ phận kỹ thuật tuân thủ các nguyên tắc cốt lõi:

- **AI là Công cụ hỗ trợ, không phải Hệ thống ra quyết định:** Khai thác AI để gia tăng năng suất, nghiêm cấm việc dùng AI để thay thế tư duy thiết kế kiến trúc và năng lực quản trị rủi ro của người kỹ sư.
- **Khước từ phương pháp “Vibe Code”:** Không được phép sao chép trực tiếp (copy-paste) mã nguồn do AI sinh ra vào dự án nếu chưa trải qua thẩm định (code review) và hiểu rõ luồng logic.
- **Định vị giá trị cốt lõi:** Năng lực của kỹ sư hệ thống được định hình bởi khả năng kiểm soát quy trình, chứ không phải tốc độ gõ mã nguồn.

### 1.3. Nền tảng hành vi: 4 Nguyên tắc Karpathy
Phiên bản 1.1.0 tích hợp 4 nguyên tắc lập trình của Andrej Karpathy làm nền tảng hành vi bắt buộc cho mọi AI Agent:

| # | Nguyên tắc | Mô tả | Ngăn chặn |
|---|-----------|-------|-----------|
| 1 | **Think Before Coding** | Nêu rõ giả định, trình bày các phương án, hỏi khi không rõ | Code sai hướng |
| 2 | **Simplicity First** | Code tối thiểu, không tính năng suy đoán | Over-engineering |
| 3 | **Surgical Changes** | Chỉ sửa đúng phần cần thiết, giữ style hiện có | Scope creep |
| 4 | **Goal-Driven Execution** | Định nghĩa tiêu chí thành công có thể kiểm chứng | Kết quả mơ hồ |

Tài liệu nguồn: `karpathy/principles.md` (source of truth) và `karpathy/examples.md` (ví dụ thực tế).

---

## PHẦN II: CHUẨN BỊ MÔI TRƯỜNG VÀ CẤU HÌNH

### 2.1. Đánh giá Công cụ tích hợp (Tooling Stack)
- **Cursor / Windsurf:** Môi trường IDE tích hợp AI ưu việt nhất hiện nay nhờ năng lực phân tích sâu (deep context awareness). Phù hợp để cấu trúc mã nguồn trực tiếp và refactor diện rộng.
- **Claude 3.5 Sonnet / GPT-4o:** Phù hợp cho giai đoạn phân tích ý tưởng hệ thống (brainstorming), phân tích thiết kế kiến trúc và soạn thảo tài liệu kỹ thuật phức tạp.
- **GitHub Copilot:** Hỗ trợ tối ưu cho việc hoàn thiện cú pháp (auto-complete) và mã nguồn boilerplate.

=> **Chính sách chọn model:** Kỹ sư cần chọn mô hình phù hợp với tác vụ. Sử dụng Claude 3.5 Sonnet cho thiết kế phức tạp, Copilot cho auto-complete, tránh lạm dụng mô hình đắt tiền cho tác vụ đơn giản nhằm kiểm soát chi phí.

### 2.2. Tiêu chuẩn hóa Ngữ cảnh & Cấu hình (Context Management)
- **Quản trị Bộ nhớ Ngữ cảnh:** Thay vì đính kèm toàn bộ dự án làm giảm độ chính xác của AI, kỹ sư chỉ cung cấp các tệp tin (files) liên quan trực tiếp đến luồng xử lý, đi kèm định nghĩa cấu trúc (schema/interfaces) và tài liệu API.
- **Tệp Cấu hình Hệ thống (Auto-Discovery):** Framework sử dụng cơ chế **zero-config** — mỗi AI tool tự động nhận diện instruction file tương ứng tại thư mục gốc dự án:

  | Công cụ AI | File tự nhận diện |
  |------------|-------------------|
  | Claude Code | `CLAUDE.md` |
  | Gemini Code Assist / CLI | `GEMINI.md` |
  | GitHub Copilot | `COPILOT.md` |
  | VS Code Copilot | `.instructions.md` |
  | Cursor | `.cursor/rules/*.mdc` + `.cursorrules` |
  | Windsurf | `.cursorrules` + `.instructions.md` |

  Quy trình sử dụng: (1) Copy repo vào project root → (2) Mở project bằng AI tool → (3) Agent tự nhận diện → (4) Xác minh bằng lệnh `/standards`.

- **Ngôn ngữ tài liệu:** Toàn bộ tài liệu framework trong `ai-agent-standards/` sử dụng **Tiếng Anh 100%** để đảm bảo mọi AI Agent đọc được chính xác. Tài liệu phương pháp luận gốc (Tiếng Việt) được giữ tại `Development_doc_VI.md`.

### 2.3. Quản trị Thư viện Prompt và Kiểm soát Phiên bản
Để đảm bảo tính nhất quán và tái sử dụng, mỗi dự án cần duy trì một thư viện prompt chuẩn hóa:

- **Cấu trúc thư viện:** Thư mục `prompts/` trong repository, chứa các tệp Markdown phân loại theo mục đích (ví dụ: `create-api.md`, `refactor-cache.md`, `generate-unit-test.md`).
- **Định dạng tệp:** Mỗi tệp bắt buộc có header YAML chứa:
  ```yaml
  ---
  id: PROMPT-001
  version: 1.2
  author: [tên kỹ sư]
  last_updated: 2025-01-15
  applicable_stack: [React, Node.js]
  ---
  ```
- **Quy trình thêm/xét duyệt prompt mới:** Kỹ sư tạo pull request vào thư viện prompt, trong đó ghi rõ mục đích, ngữ cảnh sử dụng và kết quả thử nghiệm. Pull request phải được một kỹ sư khác review về bảo mật (không chứa key, PII) và tính phù hợp trước khi merge.
- **Theo dõi hiệu quả:** Khi sử dụng prompt, kỹ sư ghi lại `prompt_id` và `prompt_version` trong task để dễ dàng đánh giá hiệu quả qua các chỉ số như AI Iteration Count.

---

## PHẦN III: QUY TRÌNH THỰC THI TIÊU CHUẨN

### 3.1. Lớp nền Tiên quyết (Non-Negotiable Constraints)
- **Bảo mật (Zero-Trust):** Tuyệt đối không nhúng dữ liệu nhạy cảm (API Keys, Passwords, PII, mã nguồn bảo mật cao) vào prompt.
- **Xác thực dữ liệu:** Bắt buộc áp dụng cơ chế làm sạch và kiểm tra dữ liệu đầu vào (Input Validation/Sanitization).
- **Tuân thủ Kiến trúc:** Mọi giải pháp AI đưa ra phải tương thích với quy chuẩn kiến trúc hiện hành của dự án.

### 3.2. Khuôn mẫu Prompt Tiêu chuẩn
```markdown
### [CONTEXT - NGỮ CẢNH HỆ THỐNG]
- Tech stack: [VD: React v18, Node.js, PostgreSQL]
- Trạng thái hiện tại: [Mô tả kỹ thuật tóm tắt chức năng đang hoạt động]
- Schema/Interfaces: [Cung cấp cấu trúc dữ liệu liên quan]

### [TASK - YÊU CẦU NGHIỆP VỤ]
- Mục tiêu: [Mô tả chi tiết và độc lập 1 tính năng. Áp dụng quy tắc Single-Task Prompting]

### [CONSTRAINTS - RÀNG BUỘC KỸ THUẬT CỨNG]
- HÀNH VI BỊ CẤM: [VD: Không sửa đổi file cấu hình môi trường]
- YÊU CẦU BẮT BUỘC: [VD: Bắt buộc triển khai try-catch, bổ sung comments nội tuyến]
- Quy trình: Bắt buộc chạy Pipeline Tự kiểm tra (Self-Check) trước khi kết xuất mã nguồn.

### [OUTPUT FORMAT - ĐỊNH DẠNG ĐẦU RA]
- [VD: Chỉ xuất mã nguồn thay đổi, không giải thích dài dòng / Định dạng JSON]
```

### 3.3. Trình tự 7 Bước Triển khai
1. **Phân tích & Phân rã tác vụ:** Nếu module phức tạp, yêu cầu AI lập bảng kế hoạch chi tiết (execution plan) trước. Kỹ sư duyệt bản thiết kế này rồi mới tiến hành yêu cầu code từng bước nhỏ.
2. **Thiết kế Dữ liệu Độc lập:** Kỹ sư nắm toàn quyền thiết kế Schema. AI chỉ đóng vai trò triển khai (implementation) dựa trên schema đã duyệt.
3. **Áp đặt Nguyên tắc Kiến trúc:** Ép buộc AI tuân thủ OOP, MVC, tính module hóa và Clean Code.
4. **Phát triển Bottom-up:** Bắt buộc xây dựng theo trình tự: Core Logic → Services/APIs → Front-end/UI.
5. **Vận hành Pipeline Kiểm soát:** (Chi tiết tại Mục 3.4).
6. **Lưu trữ Cột mốc (Milestone Backup):** Commit/Backup mã nguồn ngay trước và sau khi hoàn thành một module để thiết lập điểm phục hồi (Rollback point).
7. **Tự động hóa Tài liệu:** Chỉ định AI cập nhật API Specs và tệp README ngay sau khi mã nguồn được duyệt.

### 3.4. Pipeline Kiểm soát Chất lượng (AI Control Pipeline)
```
[ PHIẾU YÊU CẦU XỬ LÝ DÀNH CHO AI ] (Áp dụng Khuôn mẫu Prompt Mục 3.2)
          │
          ▼
┌─────────────────────────────────────────────────────────────┐
│ 1. AI GENERATE (Tiến trình Sinh mã nguồn)                   │
├─────────────────────────────────────────────────────────────┤
│ 2. AI SELF-CHECK (Tiến trình Tự kiểm tra - Bắt buộc)        │
│    AI phải phản hồi Checklist trước khi xuất output:        │
│    [ ] Đã tuân thủ Lớp nền Tiên quyết?                      │
│    [ ] Tỷ lệ lặp lại mã nguồn (Code Duplication) = 0?       │
│    [ ] Đã xử lý các rủi ro bảo mật (SQLi, XSS, Info Leak)?  │
│    [ ] Đã cấu hình xử lý ngoại lệ (Null, Timeout, Errors)?  │
│    [ ] Khả năng gây lỗi hồi quy (Regression risk) thấp?     │
├─────────────────────────────────────────────────────────────┤
│ 3. AI SELF-FIX (Tiến trình Tự sửa lỗi)                      │
│    Nếu Self-Check thất bại, AI tự kích hoạt luồng sửa lỗi.  │
│    (Giới hạn: Tối đa 2 chu kỳ. Vượt quá -> Báo cáo)         │
├─────────────────────────────────────────────────────────────┤
│ 4. OUTPUT (Kết xuất dữ liệu)                                │
│    Mã nguồn hoàn thiện + Báo cáo Self-Check                 │
└─────────────────────────────────────────────────────────────┘
          │
          ▼
[ HUMAN GATE - CỔNG KIỂM DUYỆT BỞI KỸ SƯ ]
├── Đánh giá tính toàn vẹn của Business Logic & Hiệu năng.
└── Ra quyết định:
      [APPROVE] ──────> Merge vào Codebase & Cập nhật Checkpoint
      [REJECT/REWORK] ──> Tinh chỉnh Prompt và lặp lại tiến trình
```

### 3.5. Xử lý Ngoại lệ và Leo thang khi AI không hợp tác
Khi AI vượt quá 2 chu kỳ Self-Fix mà vẫn không đạt yêu cầu:
- **Ghi nhận sự cố vào AI Failure Log:** Mỗi dự án duy trì một bảng `ai_failure_log.md` (hoặc tích hợp vào hệ thống wiki) gồm các trường: ngày, prompt ID, phiên bản prompt, mô tả ngắn gọn vấn đề, số vòng lặp, hành động tiếp theo.
- **Escalation path:**
  a) Kỹ sư thực hiện phân tích nguyên nhân, quyết định tự code thủ công phần giải pháp hoặc thay đổi chiến lược prompt.
  b) Nếu cản trở đến từ ràng buộc kiến trúc, tạo một technical spike để thảo luận với kiến trúc sư hoặc trưởng nhóm.
  c) Cập nhật prompt library hoặc tạo prompt mới sau khi tìm ra hướng giải quyết, tránh lặp lại lỗi tương tự.
- **Giới hạn thời gian:** Nếu một prompt tiêu tốn hơn 3 lần thời gian so với ước tính ban đầu mà không có kết quả khả quan, bắt buộc chuyển sang viết thủ công và gắn cờ để cải tiến.

### 3.6. Tích hợp Pipeline vào Quy trình Nhóm (Scrum/Kanban)
- **AI Task trong Jira/Trello:** Mỗi task sử dụng AI phải được gắn nhãn (label) **AI-Assisted**. Các trường tùy chỉnh (nếu có) bao gồm: `prompt_id`, `prompt_version`, `ai_iteration_count`, `human_gate_status`.
- **Definition of Done (DoD) mở rộng cho AI Task:** Ngoài các tiêu chí thông thường, phải có:
  - Self-Check report từ AI được lưu kèm trong task.
  - Code review bởi ít nhất một kỹ sư khác (xem mục 4.4).
  - Đã commit milestone backup.
- **AI Code Reviewer:** Trong quy trình code review, kỹ sư được phân công cần kiểm tra các đoạn mã AI sinh ra dựa trên **Checklist Audit AI Code** (xem Phụ lục B). Những phần logic quan trọng (xác thực, thanh toán…) phải có ít nhất hai kỹ sư xem xét (quy tắc “two-pair eyes”).

---

## PHẦN IV: KIỂM SOÁT RỦI RO & ĐẢM BẢO CHẤT LƯỢNG

### 4.1. Kiểm soát Hiện tượng AI Sinh thông tin sai lệch (Hallucination)
- **Dấu hiệu cảnh báo:** AI yêu cầu import thư viện không tồn tại/deprecated; gọi phương thức không có trong Official Documentation; thuật toán vi phạm logic khi mô phỏng (mocking) edge cases.
- **Quy trình xử lý:** Yêu cầu AI cung cấp link tài liệu chính thức (Verify by Docs). Kỹ sư chủ động đối chiếu chéo (Cross-check) trước khi hợp nhất mã nguồn.

### 4.2. Rủi ro Pháp lý và Bản quyền
- **Cảnh báo:** AI có thể vô tình tái tạo nguyên bản các đoạn mã nguồn mở có giấy phép hạn chế (như GPL).
- **Trách nhiệm:** Bắt buộc rà soát nguồn gốc (provenance check) đối với các khối thuật toán đặc thù phức tạp để tránh vi phạm sở hữu trí tuệ trong dự án thương mại.

### 4.3. Tích hợp CI/CD và Kiểm thử Tự động
- **Automated Testing:** Bắt buộc AI tự động sinh Unit Tests cho mọi logic cốt lõi.
- **CI/CD Gates:** Tích hợp công cụ phân tích mã nguồn tĩnh (SAST, ví dụ: SonarQube, Snyk, Checkmarx) để tự động quét lỗ hổng bảo mật và nợ kỹ thuật (technical debt) trong đường ống CI/CD. Mã nguồn do AI sinh ra vẫn phải qua các gate tự động này.

### 4.4. Kiểm soát Nợ Kỹ thuật Đặc thù từ AI
Mã AI sinh ra thường có xu hướng over-engineering, trùng lặp hoặc bỏ qua tối ưu hiệu suất. Do đó:
- **Chính sách Refactor Window:** Sau khi merge mã AI, mỗi module cần một phiên làm việc (có thể là task riêng) trong vòng 2 sprint để rà soát và tối ưu: loại bỏ dead code, đồng bộ naming convention, áp dụng design pattern phù hợp.
- **Quy tắc “Two-pair eyes” cho logic phức tạp:** Đối với các thành phần như xử lý tài chính, phân quyền, mã hóa dữ liệu, yêu cầu một kỹ sư senior không phải người viết prompt (độc lập) thực hiện review chuyên sâu.
- **Theo dõi nợ kỹ thuật AI:** Sử dụng tag hoặc label trong SonarQube để phân biệt code AI vs code thủ công, từ đó đo lường xu hướng Technical Debt Ratio của từng nguồn.

### 4.5. Quản trị Chi phí Sử dụng AI (API Cost)
- **Nguyên tắc tiết kiệm:** Nghiêm cấm gửi toàn bộ codebase vào prompt một cách vô tội vạ. Kỹ sư phải tối ưu ngữ cảnh theo mục 2.2. Đặt ngưỡng token tối đa cho mỗi lần gọi (ví dụ: 8k tokens), nếu vượt quá phải được trưởng nhóm phê duyệt.
- **Log và giám sát chi phí:** Sử dụng proxy hoặc middleware ghi nhận số token, mô hình sử dụng cho mỗi lần gọi, phân bổ theo dự án hoặc team. Dữ liệu này được tổng hợp hàng tuần để báo cáo chi phí, phục vụ cho phân tích CBA (Cost-Benefit Analysis) về sau.
- **Chính sách chọn mô hình (nhắc lại từ 2.1):** Dùng mô hình cao cấp cho thiết kế/phân tích, mô hình nhẹ cho tác vụ lặp lại.

---

## PHẦN V: ĐO LƯỜNG HIỆU SUẤT & QUẢN TRỊ TRI THỨC

### 5.1. Đo lường Định lượng (Metrics & KPIs)
Các chỉ số sau cần được theo dõi liên tục cho các task AI-Assisted:
- **Tỷ lệ lỗi hồi quy (Defect Rate):** Lỗi phát sinh sau khi merge mã AI. Gắn thẻ [AI-Assisted] trên Jira để dễ trích xuất.
- **Thời gian hoàn thành chu kỳ (Cycle Time):** So sánh với phương pháp thủ công cho cùng loại task.
- **Độ bao phủ kiểm thử (Test Coverage):** Mức độ che phủ của Unit Tests cho code AI sinh ra.
- **Số chu kỳ sửa lỗi (AI Iteration Count):** Số lần AI phải chạy vòng lặp Self-Fix trước khi đạt yêu cầu.
- **Technical Debt Ratio của AI:** Tỷ lệ nợ kỹ thuật riêng cho module AI (theo dõi qua công cụ SAST).

### 5.2. Chiến lược Quản trị Tri thức & Nâng cấp Kỹ năng
- **Nhận diện Khuôn mẫu (Pattern Matching):** Hệ thống hóa cấu trúc prompt hiệu quả cho từng nhóm vấn đề (Concurrency, Caching, Security...).
- **Nguyên lý Ghi chú Tối giản (“Quy tắc Một dòng”):** Lưu trữ bản chất giải pháp kỹ thuật làm tín hiệu kích hoạt tư duy. (Ví dụ: “Áp dụng Chain-of-Thought để xử lý concurrent file upload”, “Luôn ép buộc áp dụng pattern try-catch-rollback khi xử lý Database Transaction”).
- **Retrospective định kỳ về AI Practice:** Mỗi 2-3 sprint, team dành 30 phút để chia sẻ prompt hiệu quả, lỗi thường gặp, cập nhật thư viện prompt.

### 5.3. Lộ trình Đào tạo và Onboarding Kỹ sư Mới
Nhằm đảm bảo kỹ sư mới nhanh chóng làm chủ phương pháp, xây dựng gói onboarding gồm:
1. **Nghiên cứu tài liệu này** (phiên bản hiện hành).
2. **Thực hành trên dự án mẫu:** Thực hiện một user story giả định (ví dụ: “Xây dựng API đăng ký người dùng có kiểm tra email trùng lặp”) dưới sự hướng dẫn của mentor, áp dụng toàn bộ pipeline từ prompt đến Human Gate.
3. **Bài tập mô phỏng lỗi:** Mentor cung cấp một prompt cố tình chứa lỗi bảo mật và yêu cầu kỹ sư mới phát hiện qua Self-Check và giải thích.
4. **Chấm điểm đạt:** Kỹ sư mới phải hoàn thành ít nhất 3 AI task mẫu đạt Human Gate với số vòng lặp trung bình ≤ 2 và được mentor xác nhận trước khi tham gia dự án thật.

---

## PHẦN VI: LỘ TRÌNH PHÁT TRIỂN & PHỤ LỤC

### 6.1. Hạng mục Chờ nghiên cứu (Living Document Placeholders)
| Hạng mục | Mức ưu tiên | Trạng thái | Sản phẩm |
|----------|-------------|-----------|----------|
| **Prompt Engineering Cookbook** | P0 (Cao) | ✅ Hoàn thành | [`rag-implementation-cookbook.md`](./prompts/sample-use-cases/rag-implementation-cookbook.md) |
| **Systematic Code Audit Checklist** | P0 | ✅ Hoàn thành | Mở rộng [`audit-ai-code-full.md`](./quality-control/audit-ai-code-full.md) (11 sections) + [PR Template](../.github/pull_request_template.md) + [CI/CD Gate](../.github/workflows/ai-code-audit.yml) |
| **AI-Native Design Patterns** | P1 (Trung bình) | ⏳ Chờ nghiên cứu | Kiến trúc phần mềm tối ưu khi phát triển cùng AI |
| **Kế hoạch Phục hồi Thảm họa (Disaster Recovery)** | P1 | ⏳ Chờ nghiên cứu | Chiến lược Rollback nâng cao |
| **Phân tích Hiệu quả Đầu tư (Cost-Benefit Analysis)** | P1 | ⏳ Chờ nghiên cứu | Đánh giá triển khai quy mô team |
| **Multi-Agent Orchestration Framework** | P2 (Thấp) | ✅ Hoàn thành (v1) | [`coder-agent.md`](./multi-agent/coder-agent.md) + [`reviewer-agent.md`](./multi-agent/reviewer-agent.md) |

### 6.2. Phụ lục A: Cookbook Tình huống Điển hình
**Ví dụ 1: Xây dựng API login có rate limiting**
- Prompt mẫu: `prompts/create-api-rate-limit.md` (phiên bản 1.0)
- Mô tả ngắn: Yêu cầu AI tạo endpoint `/login` với Express, sử dụng `express-rate-limit`, xác thực JWT, có try-catch và logging.
- Kết quả Self-Check mẫu:
  - [x] Không import thư viện không tồn tại
  - [x] Kiểm tra đầu vào email/password
  - [x] Có cơ chế chống brute-force
- Trải nghiệm thực tế: Sau 1 vòng Self-Fix, output đạt Human Gate. Lưu ý: phải kiểm tra lại tham số `windowMs` và `max` phù hợp.

### 6.3. Phụ lục B: Bảng Lỗi Thường gặp của AI và Cách Xử lý
| Loại lỗi | Dấu hiệu | Cách xử lý |
|----------|----------|------------|
| Import thư viện ảo | Import `some-fake-lib` không tồn tại | Yêu cầu AI cung cấp link docs; nếu không có, bắt AI thay thế bằng thư viện chính thức |
| Lỗi bảo mật (SQLi) | Truy vấn nối chuỗi trực tiếp | Thêm constraint “must use parameterized queries” vào prompt |
| Logic kiểm tra null thiếu | Thiếu guard clause ở đầu hàm | Bổ sung constraint “always check null/undefined đầu hàm” |
| Over-engineering | Thừa lớp abstraction không cần thiết | Thêm giới hạn “keep design simple, avoid unnecessary abstraction” |
| Hiểu sai nghiệp vụ | Xử lý sai edge case | Mô tả edge case trong Context; nếu lặp lại, cung cấp bảng test case mẫu |

### 6.4. Phụ lục C: Mẫu Báo cáo Tự kiểm tra (Self-Check Report)
Khi AI hoàn thành bước Self-Check, nó sẽ xuất ra một báo cáo như dưới đây. Kỹ sư cần lưu kèm trong task.

```markdown
## AI Self-Check Report
- **Prompt ID:** PROMPT-001
- **Task:** API Rate Limiting
- **Date:** 2025-01-15
- **Checklist:**
  - [x] Tuân thủ Lớp nền Tiên quyết
  - [x] Code Duplication = 0
  - [x] Đã xử lý SQLi, XSS
  - [x] Đã xử lý ngoại lệ (null, timeout)
  - [ ] Có rủi ro hồi quy (thấp) – không ảnh hưởng module khác
- **Ghi chú:** Không import thư viện lạ, đã kiểm tra docs. Đề xuất thêm unit test cho edge case 500 request trong 1 phút.
```

### 6.5. Phụ lục D: Cấu trúc Repository & Thư viện Prompt
```
project-root/
│
│ ── AUTO-DISCOVERY (AI tự nhận diện) ──
├── CLAUDE.md / GEMINI.md / COPILOT.md
├── .instructions.md / .cursorrules
├── .cursor/rules/
│
│ ── KARPATHY PRINCIPLES ──
├── karpathy/
│   ├── principles.md              → 4 nguyên tắc (source of truth)
│   └── examples.md                → Anti-patterns & cách đúng
│
│ ── FRAMEWORK (100% English) ──
├── ai-agent-standards/
│   ├── onboarding/                → Đào tạo, quick reference
│   ├── prompts/                   → Prompt templates & 5 use cases mẫu
│   │   ├── PROMPT-TEMPLATE.md     → Khuôn mẫu chuẩn
│   │   ├── indexed-by-category.md → Tra cứu theo danh mục
│   │   └── sample-use-cases/      → Ví dụ thực tế
│   ├── quality-control/           → Review checklists, audit, CI/CD gates
│   ├── risk-management/           → Security, escalation, failure logs
│   ├── metrics/                   → KPIs & tracking
│   ├── reference/                 → Glossary, error reference
│   └── multi-agent/               → Lộ trình P2
│
├── INSTALL.md                     → Hướng dẫn cài đặt (1 bước)
├── README.md                      → Tài liệu chính (English)
└── Development_doc_VI.md          → Tài liệu phương pháp luận (Vietnamese)
```
Mỗi tệp prompt phải tuân thủ mẫu header YAML (đã nêu ở 2.3) và chứa đầy đủ các phần Context, Task, Constraints, Output Format theo khuôn mẫu 3.2.

### 6.6. Phụ lục E: Kịch bản Mở rộng Multi-Agent
Hiện tại, khung làm việc này tập trung vào mô hình **Single-Agent** dưới sự giám sát chặt chẽ của kỹ sư. Trong tương lai, nếu triển khai hệ thống nhiều agent phối hợp (ví dụ: một agent code, một agent review, một agent test), cần xây dựng thêm:

- **Lớp Agent Orchestrator:** Điều phối công việc giữa các agent, đảm bảo mỗi agent chỉ hoạt động trong phạm vi được giao.
- **Quy tắc cô lập dữ liệu:** Tuyệt đối không cho phép agent này truy cập dữ liệu nhạy cảm của agent khác mà không có sự đồng ý của kỹ sư.
- **Giao thức giao tiếp chuẩn:** Các agent trao đổi qua API được kiểm soát, mọi thông điệp phải được ghi log và có thể audit.

=> Mục này sẽ được phát triển chi tiết trong tài liệu “Multi-Agent Orchestration Framework” (ưu tiên P2).

### 6.7. Phụ lục F: Diễn giải Phương pháp luận trong Quản trị
**Ngữ cảnh:** Khi cần báo cáo hoặc phản biện cấp quản lý về sự khác biệt giữa quy trình này và “Vibe Coding”.

**Chiến lược diễn giải:**
Khẳng định đây là phương pháp Controlled AI-Assisted Development dựa trên 3 trụ cột kỹ thuật:
1. **Kiểm duyệt định lượng:** Toàn bộ output đi qua Pipeline kiểm duyệt với thông số rõ ràng (trình bày sơ đồ Pipeline Mục 3.4 như một bằng chứng kỹ thuật).
2. **Quản trị rủi ro tuyệt đối:** Hệ thống hóa các giới hạn cứng, thiết lập điểm khôi phục an toàn (Milestones backup), kiểm soát nợ kỹ thuật và chi phí.
3. **Kỹ sư là trung tâm:** AI chỉ đóng vai trò Implementation, toàn quyền quyết định về Architecture và Security thuộc về chuyên môn của kỹ sư.

Bổ sung thêm các dữ liệu thực tế từ việc theo dõi Metrics (5.1) để chứng minh hiệu quả và tính an toàn của phương pháp.

---

*Tài liệu này sẽ được cập nhật định kỳ dựa trên kinh nghiệm thực tế và các nghiên cứu mới. Các đóng góp xin gửi về nhóm chịu trách nhiệm nội dung.*