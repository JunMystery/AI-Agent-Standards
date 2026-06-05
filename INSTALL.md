# Install Guide

## Quick Start - Automated Setup (Recommended)

Run the setup script from **your project directory**. It will:
1. Ask which AI agent you use and copy only that instruction file to your project root
2. Auto-rewrite all internal links to match the actual folder path

### Option A: Standards folder inside your project

```
your-project/
+-- AI-Agent-Standards/    <- clone or copy the repo here
+-- src/
+-- ...
```

```bash
# From your project root
python AI-Agent-Standards/scripts/setup.py
```

### Option B: Standards folder in a custom location

```bash
# Explicitly specify your project root
python /path/to/AI-Agent-Standards/scripts/setup.py /path/to/your-project
```

### Option C: Git Submodule (recommended for version tracking)

```bash
# From your project root
git submodule add https://github.com/JunMystery/AI-Agent-Standards.git AI-Agent-Standards
python AI-Agent-Standards/scripts/setup.py
```

> **What the script does:** It copies the selected instruction file, or every supported instruction file when you choose all, then rewrites all embedded links (e.g., `AI-Agent-Standards/karpathy/principles.md`) to match the real relative path of your standards folder.

By default, the script prompts you to choose one agent instruction file:

```text
0. Cancel
1. OpenAI Codex / Codex VS Code
2. Claude Code
3. Gemini Code Assist / Gemini CLI
4. GitHub Copilot Chat
5. VS Code Copilot
6. Cursor
7. Windsurf / Cursor legacy fallback
8. Choose all
```

Use `0` to cancel. Choose one agent to keep the project root tidy, or choose all if you are not sure which AI agent will be used.

For non-interactive setup:

```bash
python AI-Agent-Standards/scripts/setup.py --agent codex
python AI-Agent-Standards/scripts/setup.py --agent claude
python AI-Agent-Standards/scripts/setup.py --agent all
```

---

## Manual Setup (Alternative)

If you prefer to copy files manually:

### Windows (PowerShell)
```powershell
# From your project root
Copy-Item -Path "AI-Agent-Standards\AGENTS.md","AI-Agent-Standards\CLAUDE.md","AI-Agent-Standards\GEMINI.md","AI-Agent-Standards\COPILOT.md","AI-Agent-Standards\.instructions.md","AI-Agent-Standards\.cursorrules","AI-Agent-Standards\PROJECT-STANDARDS.md" -Destination ".\"
Copy-Item -Recurse "AI-Agent-Standards\.cursor" -Destination ".\"
```

### macOS / Linux
```bash
# From your project root
cp AI-Agent-Standards/{AGENTS.md,CLAUDE.md,GEMINI.md,COPILOT.md,.instructions.md,.cursorrules,PROJECT-STANDARDS.md} .
cp -r AI-Agent-Standards/.cursor .
```

> WARNING **Note:** With manual setup, internal links default to `AI-Agent-Standards/` as the folder prefix. If your standards folder has a different name, you must search-and-replace `AI-Agent-Standards/` with the correct path in the copied files.

---

## What Gets Loaded by Each AI Tool

| File | Tool | Auto-detected? |
|------|------|----------------|
| `AGENTS.md` | OpenAI Codex / Codex VS Code | [OK] Yes |
| `CLAUDE.md` | Claude Code | [OK] Yes |
| `GEMINI.md` | Gemini Code Assist / Gemini CLI | [OK] Yes |
| `COPILOT.md` | GitHub Copilot Chat | [OK] Yes (custom instructions) |
| `.instructions.md` | VS Code Copilot | [OK] Yes |
| `.cursor/rules/karpathy-guidelines.mdc` | Cursor | [OK] Yes (alwaysApply) |
| `.cursorrules` | Cursor / Windsurf (legacy) | [OK] Yes |

---

## Verify Installation

After running the setup script, open your project in the AI tool and ask:

> **"What coding standards are you following?"**

or type:

> **`/standards`**

Expected response:

> [OK] **AI-Coding-Standards v2.6.1** with 6 Core Principles active.
> Framework: Controlled AI-Assisted Development
> Principles: (1) Think Before Coding, (2) Simplicity First, (3) Surgical Changes, (4) Goal-Driven Execution, (5) DRY & Reusability, (6) Code Organization

If the AI doesn't respond with this format, the instruction file wasn't loaded. Check that the files are in the project root.

---

## What to Customize

After installing, you may want to customize:

1. **`PROJECT-STANDARDS.md`** - Add your project-specific rules (naming conventions, architecture, preferred libraries). The setup script will not overwrite this file once you've customized it.
2. **`AGENTS.md` / `CLAUDE.md` / `GEMINI.md`** - Add project-specific rules under a `## Project-Specific Guidelines` section.

---

## Asking the AI Agent to Self-Install

If your AI agent has file-writing capabilities (e.g., Codex, Claude Code, Gemini CLI, Cursor), you can simply prompt it:

> **"Use the standards from the `AI-Agent-Standards` folder. Run `python AI-Agent-Standards/scripts/setup.py` to install them."**

The AI will execute the setup script, choose the matching agent option, and rewrite all links automatically.

---

## Minimal Install (6 Core Principles Only)

If you only want the 6 Core Principles without the full framework:

```bash
# Copy just the karpathy module and one instruction file
mkdir -p karpathy
cp AI-Agent-Standards/karpathy/principles.md karpathy/
cp AI-Agent-Standards/karpathy/examples.md karpathy/

# Pick your tool:
cp AI-Agent-Standards/AGENTS.md .       # For OpenAI Codex / Codex VS Code
cp AI-Agent-Standards/CLAUDE.md .        # For Claude Code
cp AI-Agent-Standards/GEMINI.md .        # For Gemini
cp AI-Agent-Standards/.cursorrules .     # For Cursor/Windsurf
```

---

## Updating

To update the standards to the latest version:

```bash
# If using git submodule:
cd AI-Agent-Standards && git pull && cd ..
python AI-Agent-Standards/scripts/setup.py --agent all

# If using a copied folder:
# Replace the AI-Agent-Standards folder, then re-run setup
python AI-Agent-Standards/scripts/setup.py --agent all
```

The setup script will re-copy and re-link the selected files. Use `--agent all` to refresh every supported instruction file. Your `PROJECT-STANDARDS.md` will be preserved if you've already customized it.
