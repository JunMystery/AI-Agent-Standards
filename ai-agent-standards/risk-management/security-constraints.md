# Security Constraints — Non-Negotiable Baseline

**Non-Negotiable Rules — Absolutely no violations permitted**

Section III.1 from original documentation

---

## 🚫 Constraint 1: Zero-Trust for Secrets

**Rule:** NEVER embed secrets in code

### Forbidden Secrets
- ✗ API Keys (OpenAI, Stripe, AWS)
- ✗ Database passwords
- ✗ JWT secrets
- ✗ OAuth tokens
- ✗ PII (email, SSN, passport numbers)

### Storage
- ✓ `.env` file (local, gitignored)
- ✓ Environment variables (production)
- ✓ Secrets manager (AWS Secrets Manager, Vault)

### How AI Violates (Detect)
```javascript
// ❌ VIOLATION
const apiKey = "sk-abc123xyz";  // Hardcoded!
const db = connect('user:password@localhost');  // Credentials!
```

### Consequence
- ✗ Fail code review
- ✗ Security breach risk
- ✗ May block production deployment

---

## 🚫 Constraint 2: Mandatory Input Validation

**Rule:** ALL user input must be validated before use

### What to Validate
- [ ] Type (string, number, array)
- [ ] Length (min/max)
- [ ] Format (email, URL, phone)
- [ ] Range (min/max values)
- [ ] Allowed values (enum)

### Tools
- ✓ zod (TypeScript-first)
- ✓ joi (schema validation)
- ✓ validator.js (specific checks)

### How AI Violates
```javascript
// ❌ VIOLATION
const email = req.body.email;  // No validation!
sendEmail(email);  // What if "x" or SQL injection?

// ✓ CORRECT
const schema = z.object({ email: z.string().email() });
const { email } = schema.parse(req.body);
sendEmail(email);
```

### Consequence
- ✗ SQL injection possible
- ✗ XSS attack vector
- ✗ System crashes
- ✗ Fail code review

---

## 🚫 Constraint 3: No Unhandled Errors

**Rule:** ALL async/risky operations must be wrapped in try-catch

### Risky Operations
- [ ] Database queries
- [ ] API calls
- [ ] File operations
- [ ] JSON parsing
- [ ] Crypto operations

### How AI Violates
```javascript
// ❌ VIOLATION - Will crash if User not found
const user = await User.findById(id);
res.json(user);  // If crash, no error message

// ✓ CORRECT
try {
  const user = await User.findById(id);
  if (!user) return res.status(404).json({ error: 'Not found' });
  res.json(user);
} catch (error) {
  logger.error('DB error:', error);
  res.status(500).json({ error: 'Server error' });
}
```

### Consequence
- ✗ Production crashes
- ✗ Poor error messages
- ✗ Hard to debug
- ✗ Fail code review

---

## 🚫 Constraint 4: No Code Injection

**Rule:** NEVER execute user input with eval(), Function(), or raw SQL

### Forbidden Patterns
```javascript
// ❌ SQL INJECTION
db.query("SELECT * FROM users WHERE id = " + userId);

// ❌ COMMAND INJECTION
exec("ls " + userInput);

// ❌ CODE INJECTION
eval(userCode);
new Function(userCode)();

// ✓ SAFE
db.query("SELECT * FROM users WHERE id = $1", [userId]);  // Parameterized
exec("ls", [userInput]);  // Safe shell
// Don't eval user code at all
```

### Consequence
- 🚨 **CRITICAL** Security breach
- 🚨 **CRITICAL** Must reject PR
- 🚨 **CRITICAL** Cannot deploy

---

## 🚫 Constraint 5: No Sensitive Data in Logs

**Rule:** NEVER log passwords, tokens, or PII

### Forbidden
```javascript
// ❌ VIOLATION
logger.info('Login attempt', { email, password });  // Password logged!
logger.debug('Request', req.body);  // Could contain secrets!
console.log('User:', user);  // Might log passwords
```

### Allowed
```javascript
// ✓ CORRECT
logger.info('Login attempt', { email });  // Only email
logger.debug('Request received', { method, path });  // Safe info only
console.log('User ID:', user.id);  // Just ID
```

### Consequence
- ✗ Info leak in logs
- ✗ Forensic trail compromised
- ✗ Compliance violation
- ✗ Fail code review

---

## 🚫 Constraint 6: Architecture Compliance

**Rule:** Respect existing architecture patterns

### Forbidden
```javascript
// ❌ Violates layered architecture
// In controller (shouldn't talk to DB directly)
const user = db.query("SELECT * FROM users");

// ✓ CORRECT - Use service layer
const user = userService.getAllUsers();
```

### Check Before Merge
- [ ] Code in correct layer (controller, service, model)?
- [ ] Follows pattern (MVC, hexagonal, etc)?
- [ ] Respects module boundaries?
- [ ] No circular dependencies?

### Consequence
- ✗ Hard to maintain
- ✗ Breaks design principles
- ✗ Technical debt
- ✗ Fail code review

---

## ✅ Compliance Checklist

**Before approving AI code, verify ALL:**

- [ ] **No hardcoded secrets** (API keys, passwords)
- [ ] **All input validated** (zod/joi present)
- [ ] **Error handling complete** (try-catch present)
- [ ] **No code injection risks** (parameterized queries)
- [ ] **No PII in logs** (passwords/tokens not logged)
- [ ] **Architecture respected** (correct layers, patterns)

**If ANY fail → REJECT → Ask AI to fix**

---

## 📋 Verification Commands

```bash
# Secrets scan
git diff HEAD | grep -i "secret\|password\|key\|token"

# Lint check (ESLint should catch many issues)
npm run lint

# Type check (TypeScript)
npm run type-check

# Manual review
grep -r "eval\|Function\|\.query(" src/  # Check for injection
grep -r "logger\|console" src/ | grep password  # Check logs
```

---

## 🚨 Severity: CRITICAL

**Violation of ANY constraint:**
- 🛑 Fail code review
- 🛑 Cannot merge
- 🛑 Block production deployment
- 🛑 Security incident if deployed anyway

**This is NOT negotiable.**

---

## 🔗 Reference

- OWASP Top 10: https://owasp.org/www-project-top-ten/
- CWE-Injection: https://cwe.mitre.org/data/definitions/89.html
- Node.js Security: https://nodejs.org/en/docs/guides/security/

---

**Security Constraints v1.0 | Last updated: 2026-05-12**

**Non-Negotiable Status: 🚫 ABSOLUTE - No exceptions**
