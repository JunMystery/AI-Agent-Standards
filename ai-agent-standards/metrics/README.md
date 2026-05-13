# Metrics & KPIs

Monitoring AI-assisted development efficiency.

---

## 📊 KPI Definitions

### 1. Defect Rate
- **Definition:** % of AI-assisted code with bugs after merge
- **Formula:** (Bugs found post-merge / Total AI tasks) × 100
- **Target:** < 5%
- **Trend:** Should decrease over time as team learns

### 2. Cycle Time
- **Definition:** Days from task start to merge
- **For AI tasks:** Compare vs manual coding
- **Formula:** (Task merge date - Task start date)
- **Target:** 50% faster than manual

### 3. Test Coverage
- **Definition:** % of code covered by unit tests
- **For AI code:** Must be >= 80%
- **Formula:** (Covered lines / Total lines) × 100
- **Enforce:** CI/CD gate rejects if < 80%

### 4. AI Iteration Count
- **Definition:** # of Self-Fix rounds needed
- **Average Target:** <= 2 rounds
- **Range:** 1 (perfect) to 5+ (escalated)
- **Tracking:** Log in [`tracking-template.csv`](tracking-template.csv)

### 5. Technical Debt Ratio (AI)
- **Definition:** Lines of "debt" created by AI per 1000 lines
- **Measurement:** SonarQube scoring
- **Target:** Same or lower than manual code
- **Review:** Monthly via SAST reports

---

## 📈 Tracking Template

**File:** [`tracking-template.csv`](tracking-template.csv)

Columns:
```
date,engineer,task_id,prompt_id,ai_iterations,test_coverage_%,
review_time_min,defects_found,time_to_merge_days,notes
```

**Example:**
```
2026-05-12,alice,TASK-123,PROMPT-001,1,85,25,0,1,approved_first_try
2026-05-13,bob,TASK-124,PROMPT-002,2,92,35,1,2,minor_security_issue_fixed
2026-05-14,charlie,TASK-125,PROMPT-003,3,78,45,2,3,escalated_after_2_rounds
```

---

## 📊 Sample Reports

### Weekly Report
- Total tasks: X
- Avg iterations: Y
- Avg test coverage: Z%
- Defects found: N
- Time savings vs manual: M%

### Monthly Trends
- Iteration count trending down? (Good!)
- Defect rate stable? (Good!)
- Test coverage improving? (Good!)
- Cost per task? (Monitor)

---

## 🔍 Metrics to Watch

| Metric | Green 🟢 | Yellow 🟡 | Red 🔴 |
|--------|---------|---------|--------|
| **Defect Rate** | <3% | 3-7% | >7% |
| **Avg Iterations** | <1.5 | 1.5-2.5 | >2.5 |
| **Test Coverage** | >=85% | 80-85% | <80% |
| **Review Time** | <20m | 20-40m | >40m |
| **Cycle Time** | <1 day | 1-2 days | >2 days |

---

## 📁 Files in This Folder

| File | Purpose |
|------|---------|
| [`kpi-definitions.md`](kpi-definitions.md) | Detailed KPI definitions |
| [`tracking-template.csv`](tracking-template.csv) | Data logging template |
| [`sample-weekly-report.md`](sample-weekly-report.md) | Sample report |
| [`dashboard-guide.md`](dashboard-guide.md) | Dashboard metrics setup |
| [`analysis-queries.sql`](analysis-queries.sql) | SQL queries |

---

## 🎯 Usage

1. **Log each task** in [`tracking-template.csv`](tracking-template.csv)
2. **Weekly:** Generate report (see sample)
3. **Monthly:** Analyze trends
4. **Quarterly:** Review & adjust targets

---

**Metrics v1.0 | Last updated: 2026-05-12**

[View detailed KPI definitions →](kpi-definitions.md)
