# Install Guide

## Quick Start (1 step)

Copy the entire `AI-Coding-Standards` folder into the root of your project:

### Windows (PowerShell)
```powershell
# From your project root
Copy-Item -Recurse "path\to\AI-Coding-Standards\*" -Destination ".\" -Exclude ".git"
```

### macOS / Linux
```bash
# From your project root
rsync -av --exclude='.git' path/to/AI-Coding-Standards/ ./
```

### Git Subtree (recommended for version tracking)
```bash
git subtree add --prefix=ai-agent-standards https://github.com/YourOrg/AI-Coding-Standards.git main --squash
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

> ✅ **AI-Coding-Standards Standards v1.3** with Karpathy Principles active.  
> Framework: Controlled AI-Assisted Development  
> Principles: (1) Think Before Coding, (2) Simplicity First, (3) Surgical Changes, (4) Goal-Driven Execution

If the AI doesn't respond with this format, the instruction file wasn't loaded. Check that the files are in the project root.

---

## What to Customize

After installing, you may want to customize:

1. **`.cursorrules`** — Add your project's tech stack, naming conventions, and folder structure
2. **`CLAUDE.md` / `GEMINI.md`** — Add project-specific rules under a `## Project-Specific Guidelines` section

---

## Minimal Install (Karpathy Principles Only)

If you only want the 4 Karpathy Principles without the full framework:

```bash
# Copy just the karpathy module and one instruction file
mkdir -p karpathy
cp AI-Coding-Standards/karpathy/principles.md karpathy/
cp AI-Coding-Standards/karpathy/examples.md karpathy/

# Pick your tool:
cp AI-Coding-Standards/CLAUDE.md .        # For Claude Code
cp AI-Coding-Standards/GEMINI.md .        # For Gemini
cp AI-Coding-Standards/.cursorrules .     # For Cursor/Windsurf
```
