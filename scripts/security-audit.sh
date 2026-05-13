#!/bin/bash
# ============================================================================
# AI-Coding-Standards — Security Audit Script
# ============================================================================
# Runs all 12 security constraint checks locally or in CI/CD.
# Each tool is optional — skips gracefully if not installed.
#
# Usage:
#   chmod +x scripts/security-audit.sh
#   ./scripts/security-audit.sh
#
# Exit codes:
#   0 = All checks passed
#   1 = One or more checks failed
# ============================================================================

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

FAILURES=0
SKIPPED=0

pass()  { echo -e "${GREEN}[PASS]${NC} $1"; }
fail()  { echo -e "${RED}[FAIL]${NC} $1"; FAILURES=$((FAILURES + 1)); }
skip()  { echo -e "${YELLOW}[SKIP]${NC} $1 (not installed)"; SKIPPED=$((SKIPPED + 1)); }
header(){ echo -e "\n========== $1 =========="; }

# ── 1. Secret Scan (Constraints 1, 7) ──
header "Secret Scan"
if command -v gitleaks &> /dev/null; then
    if gitleaks detect --source . --no-banner 2>/dev/null; then
        pass "No secrets detected (gitleaks)"
    else
        fail "Secrets found in repository — fix before merge"
    fi
else
    # Fallback: grep-based scan
    SECRETS=$(grep -rn --include="*.js" --include="*.ts" --include="*.py" --include="*.java" \
        -iE "(api_key|apikey|secret|password|token|private_key)\s*[:=]\s*['\"][^'\"]{8,}['\"]" \
        --exclude-dir=node_modules --exclude-dir=.git --exclude-dir=vendor \
        . 2>/dev/null | grep -v "\.example\|\.template\|\.md\|test\|mock\|fixture" || true)
    if [ -z "$SECRETS" ]; then
        pass "No hardcoded secrets detected (grep fallback)"
    else
        fail "Potential hardcoded secrets found:"
        echo "$SECRETS"
    fi
fi

# ── 2. SAST Scan (Constraints 2, 3, 4) ──
header "SAST — Static Analysis"
if command -v semgrep &> /dev/null; then
    if semgrep --config=auto --error --quiet . 2>/dev/null; then
        pass "No SAST issues found (semgrep)"
    else
        fail "SAST issues detected — review semgrep output"
    fi
else
    skip "semgrep (install: pip install semgrep)"
fi

# ── 3. Weak Crypto Detection (Constraint 8) ──
header "Weak Crypto Detection"
WEAK_CRYPTO=$(grep -rn --include="*.py" --include="*.js" --include="*.ts" \
    -iE "md5\(|sha1\(|Math\.random|random\.randint|random\.random\(\)" \
    --exclude-dir=node_modules --exclude-dir=.git --exclude-dir=vendor \
    . 2>/dev/null | grep -v "test\|mock\|\.md\|comment\|hash.*file\|checksum" || true)
if [ -z "$WEAK_CRYPTO" ]; then
    pass "No weak crypto patterns found"
else
    fail "Weak crypto patterns detected:"
    echo "$WEAK_CRYPTO"
fi

# ── 4. Dependency Audit (Constraint 9 — Slopsquatting) ──
header "Dependency Audit"
if [ -f "package.json" ]; then
    if command -v npm &> /dev/null; then
        if npm audit --production --audit-level=high 2>/dev/null; then
            pass "npm audit passed (no high/critical CVEs)"
        else
            fail "npm audit found high/critical vulnerabilities"
        fi
    else
        skip "npm"
    fi
fi

if [ -f "requirements.txt" ]; then
    if command -v pip-audit &> /dev/null; then
        if pip-audit -r requirements.txt 2>/dev/null; then
            pass "pip-audit passed (no known CVEs)"
        else
            fail "pip-audit found vulnerabilities"
        fi
    else
        skip "pip-audit (install: pip install pip-audit)"
    fi
fi

if [ ! -f "package.json" ] && [ ! -f "requirements.txt" ]; then
    pass "No dependency files found — skipping"
fi

# ── 5. IaC Security Scan (Constraint 11) ──
header "Infrastructure-as-Code Security"
if command -v trivy &> /dev/null; then
    if trivy config --severity HIGH,CRITICAL --exit-code 1 . 2>/dev/null; then
        pass "IaC scan passed (trivy)"
    else
        fail "IaC security issues found — review trivy output"
    fi
else
    # Fallback: check Dockerfiles for common issues
    DOCKERFILES=$(find . -name "Dockerfile*" -not -path "./.git/*" 2>/dev/null)
    if [ -n "$DOCKERFILES" ]; then
        ROOT_CONTAINERS=$(grep -l "^USER" $DOCKERFILES 2>/dev/null || true)
        TOTAL=$(echo "$DOCKERFILES" | wc -l)
        SAFE=$(echo "$ROOT_CONTAINERS" | grep -c "." 2>/dev/null || echo "0")
        if [ "$SAFE" -eq "$TOTAL" ]; then
            pass "All Dockerfiles use non-root USER"
        else
            fail "Some Dockerfiles missing USER directive (running as root)"
        fi
    else
        pass "No Dockerfiles found — skipping"
    fi
fi

# ── 6. Instruction File Integrity (Constraint 10) ──
header "Instruction File Integrity"
INSTRUCTION_FILES="CLAUDE.md GEMINI.md COPILOT.md .cursorrules .instructions.md"
MODIFIED=0
for f in $INSTRUCTION_FILES; do
    if [ -f "$f" ]; then
        # Check if file was modified in last commit (potential poisoning)
        if git diff HEAD~1 --name-only 2>/dev/null | grep -q "^$f$"; then
            echo -e "${YELLOW}  [WARN]${NC} $f was modified in last commit — verify changes are intentional"
            MODIFIED=$((MODIFIED + 1))
        fi
    fi
done
if [ "$MODIFIED" -eq 0 ]; then
    pass "No instruction files modified in last commit"
else
    echo -e "${YELLOW}  [INFO]${NC} $MODIFIED instruction file(s) changed — requires human review"
fi

# ── 7. Code Injection Patterns (Constraint 4) ──
header "Code Injection Patterns"
INJECTION=$(grep -rn --include="*.js" --include="*.ts" --include="*.py" \
    -E "eval\(|new Function\(|exec\(|subprocess\.run.*shell=True" \
    --exclude-dir=node_modules --exclude-dir=.git --exclude-dir=vendor \
    . 2>/dev/null | grep -v "test\|mock\|\.md" || true)
if [ -z "$INJECTION" ]; then
    pass "No code injection patterns found"
else
    fail "Potential code injection patterns detected:"
    echo "$INJECTION"
fi

# ── Summary ──
header "SUMMARY"
echo ""
if [ "$FAILURES" -eq 0 ]; then
    echo -e "${GREEN}All checks passed.${NC} Skipped: $SKIPPED"
    echo "Ready for human review."
    exit 0
else
    echo -e "${RED}$FAILURES check(s) FAILED.${NC} Skipped: $SKIPPED"
    echo "Fix issues before merge."
    exit 1
fi
