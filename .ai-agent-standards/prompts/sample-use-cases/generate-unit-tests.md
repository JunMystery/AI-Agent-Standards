---
id: PROMPT-003
version: 1.0
author: AI Agent Coding Framework
last_updated: 2026-05-12
applicable_stack: [Node.js, Jest, TypeScript]
category: Testing
difficulty: Simple
---

# Prompt: Generate Unit Tests - Jest Test Suite Generation

**Mục đích:** Tự động sinh unit tests cho business logic module

---

## [CONTEXT - NGỮ CẢNH HỆ THỐNG]

- **Tech stack:** Node.js 18, Jest 29.x, TypeScript
- **Module cần test:**
  ```typescript
  // src/utils/calculator.ts
  export class Calculator {
    add(a: number, b: number): number { return a + b; }
    subtract(a: number, b: number): number { return a - b; }
    divide(a: number, b: number): number {
      if (b === 0) throw new Error('Division by zero');
      return a / b;
    }
  }
  ```
- **Test setup:** Jest đã configured, test runner ready

---

## [TASK - YÊU CẦU NGHIỆP VỤ]

**Mục tiêu:** Tạo unit tests cover `Calculator` class

**Acceptance Criteria:**
- [ ] 100% code coverage (add, subtract, divide methods)
- [ ] Test normal cases (valid inputs)
- [ ] Test edge cases (zero, negative numbers)
- [ ] Test error cases (division by zero)
- [ ] Mỗi method có min 3 test cases
- [ ] Test naming: `describe()` + `it()` descriptive
- [ ] File: `src/utils/calculator.spec.ts`

---

## [CONSTRAINTS - RÀNG BUỘC KỸ THUẬT CỨNG]

**YÊU CẦU BẮT BUỘC:**
- ✓ Sử dụng Jest + TypeScript
- ✓ Mỗi test case phải independent
- ✓ Sử dụng `expect()` assertions
- ✓ Comments giải thích test purpose
- ✓ Không mock nếu không cần

**HÀNH VI BỊ CẤM:**
- ❌ Không test private methods
- ❌ Không skip tests (`it.skip()`)

---

## [OUTPUT FORMAT - ĐỊNH DẠNG ĐẦU RA]

- **Format:** TypeScript Jest spec file
- **Kèm:** Coverage report (screenshot or metrics)
- **Độ dài:** Code chỉ

---

## 📝 Reference

- Testing Best Practices: [`../../reference/use-case-cookbook.md`](../../reference/use-case-cookbook.md)
