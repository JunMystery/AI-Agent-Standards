# Install Guide

## Quick Start (1 step)

Copy the entire `AI-Agent-Coding` folder into the root of your project:

### Windows (PowerShell)
```powershell
# From your project root
Copy-Item -Recurse "path\to\AI-Agent-Coding\*" -Destination ".\" -Exclude ".git"
```

### macOS / Linux
```bash
# From your project root
rsync -av --exclude='.git' path/to/AI-Agent-Coding/ ./
```

### Git Subtree (recommended for version tracking)
```bash
git subtree add --prefix=ai-agent-standards https://github.com/YourOrg/AI-Agent-Coding.git main --squash
```

That's it. Your AI agents will automatically detect and load the instruction files.

---

## What Gets Loaded by Each AI Tool

| File | Tool | Auto-detected? |
|------|------|----------------|
| `CLAUDE.md` | Claude Code | ✅ Yes |
| `GEMINI.md` | Gemini Code Assist / Gemini CLI | ✅ Yes |
| `COPILOT.md` | GitHub Copilot Chat | ✅ Yes (custom instructions) |
| `.instructions.md` | VS Code Copilot | ✅ Yes |
| `.cursor/rules/karpathy-guidelines.mdc` | Cursor | ✅ Yes (alwaysApply) |
| `.cursorrules` | Cursor / Windsurf (legacy) | ✅ Yes |

---

## Verify Installation

After copying, open your project in the AI tool and ask:

> **"What coding standards are you following?"**

or type:

> **`/standards`**

Expected response:

> ✅ **AI-Agent-Coding Standards v1.1** with Karpathy Principles active.  
> Framework: Controlled AI-Assisted Development  
> Principles: (1) Think Before Coding, (2) Simplicity First, (3) Surgical Changes, (4) Goal-Driven Execution

If the AI doesn't respond with this format, the instruction file wasn't loaded. Check that the files are in the project root.

---

## What to Customize

After installing, you may want to customize:

1. **`.cursorrules`** — Add your project's tech stack, naming conventions, and folder structure
2. **`CLAUDE.md` / `GEMINI.md`** — Add project-specific rules under a `## Project-Specific Guidelines` section
3. **`ai-agent-standards/templates/`** — Adjust templates for your team's workflow

---

## Minimal Install (Karpathy Principles Only)

If you only want the 4 Karpathy Principles without the full framework:

```bash
# Copy just the karpathy module and one instruction file
mkdir -p karpathy
cp AI-Agent-Coding/karpathy/principles.md karpathy/
cp AI-Agent-Coding/karpathy/examples.md karpathy/

# Pick your tool:
cp AI-Agent-Coding/CLAUDE.md .        # For Claude Code
cp AI-Agent-Coding/GEMINI.md .        # For Gemini
cp AI-Agent-Coding/.cursorrules .     # For Cursor/Windsurf
```
