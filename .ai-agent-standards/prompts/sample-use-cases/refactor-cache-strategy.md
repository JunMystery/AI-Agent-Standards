---
id: PROMPT-002
version: 1.0
author: AI Agent Coding Framework
last_updated: 2026-05-12
applicable_stack: [Node.js, Express, TypeScript, Redis, MongoDB]
category: Performance_Optimization
difficulty: Intermediate
---

# Prompt: Refactor Cache Strategy - Redis Caching Implementation

**Mục đích:** Tối ưu hiệu năng bằng Redis caching cho database queries thường xuyên

---

## [CONTEXT - NGỮ CẢNH HỆ THỐNG]

- **Tech stack:** Node.js 18, Express, TypeScript, Redis 7.x, MongoDB
- **Vấn đề hiện tại:** 
  - Endpoint GET `/api/products` bị N+1 queries
  - Response time > 500ms, cần tối ưu xuống < 100ms
  - Database không handle load peak
- **Database Queries:**
  ```javascript
  // Current (slow)
  const products = await Product.find();
  for (const product of products) {
    product.category = await Category.findById(product.categoryId);
  }
  ```
- **Traffic Pattern:** 80% read, 20% write
- **Cache Invalidation:** Sản phẩm update không thường xuyên (~1x/hour)

---

## [TASK - YÊU CẦU NGHIỆP VỤ]

**Mục tiêu:** Implement Redis caching + cache invalidation strategy

**Acceptance Criteria:**
- [ ] GET `/api/products` return response < 100ms (95th percentile)
- [ ] Cache hit rate > 80% sau 5 phút
- [ ] Cache TTL = 1 hour (configurable)
- [ ] Cache invalidation khi product/category được update
- [ ] Fallback to DB nếu cache miss hoặc Redis down
- [ ] Cache key format: `products:list` (clear convention)
- [ ] Support cache warming (pre-populate cache on startup)
- [ ] Log cache hit/miss metrics

---

## [CONSTRAINTS - RÀNG BUỘC KỸ THUẬT CỨNG]

**HÀNH VI BỊ CẤM:**
- ❌ Không hardcode Redis URL - phải từ .env
- ❌ Không cache sensitive data (passwords, tokens)
- ❌ Không cache response toàn bộ nếu chứa user-specific data
- ❌ Không sửa database schema

**YÊU CẦU BẮT BUỘC:**
- ✓ Try-catch cho Redis operations
- ✓ Graceful fallback khi Redis unavailable
- ✓ Implement cache invalidation logic
- ✓ Log cache performance metrics
- ✓ Unit tests cho cache layer
- ✓ Comments giải thích TTL & invalidation strategy

**Quy trình:**
- ✓ Chạy Self-Check
- ✓ Kèm test cases cho cache hit/miss scenarios

---

## [OUTPUT FORMAT - ĐỊNH DẠNG ĐẦU RA]

- **Format:** TypeScript files:
  - `src/cache/redis.service.ts` (Redis wrapper)
  - `src/services/product.service.ts` (caching logic)
  - `src/controllers/product.controller.ts` (updated endpoint)
- **Kèm:** Unit test + cache strategy diagram
- **Độ dài:** Code chỉ (không giải thích)

---

## 📝 Reference

- Performance Best Practices: [`../../reference/use-case-cookbook.md`](../../reference/use-case-cookbook.md)
- Metrics: [`../../metrics/kpi-definitions.md`](../../metrics/kpi-definitions.md)
