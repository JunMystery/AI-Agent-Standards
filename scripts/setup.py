#!/usr/bin/env python3
"""
AI Agent Coding Standards — Automated Setup Script

This script copies the AI instruction file for the selected agent from the
standards directory to the project root and rewrites internal links so the
agent can auto-discover the framework. Choose all if you are unsure which
agent will be used.

Usage:
    python AI-Agent-Standards/scripts/setup.py            # auto-detect project root
    python AI-Agent-Standards/scripts/setup.py /path/to   # explicit project root
"""

import argparse
import os
import re
import shutil
import sys

# Ensure UTF-8 encoding is used for stdout/stderr on Windows to handle emojis correctly
if sys.platform.startswith("win"):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")



# Files to copy from the standards repo root → project root
AGENT_CHOICES = [
    {
        "key": "codex",
        "label": "OpenAI Codex / Codex VS Code",
        "files": ["AGENTS.md"],
    },
    {
        "key": "claude",
        "label": "Claude Code",
        "files": ["CLAUDE.md"],
    },
    {
        "key": "gemini",
        "label": "Gemini Code Assist / Gemini CLI",
        "files": ["GEMINI.md"],
    },
    {
        "key": "copilot",
        "label": "GitHub Copilot Chat",
        "files": ["COPILOT.md"],
    },
    {
        "key": "vscode-copilot",
        "label": "VS Code Copilot",
        "files": [".instructions.md"],
    },
    {
        "key": "cursor",
        "label": "Cursor",
        "files": [".cursor/rules/karpathy-guidelines.mdc"],
    },
    {
        "key": "windsurf",
        "label": "Windsurf / Cursor legacy fallback",
        "files": [".cursorrules"],
    },
]

PROJECT_STANDARDS_FILE = "PROJECT-STANDARDS.md"
ALL_CHOICE_FILES = [
    file_path
    for choice in AGENT_CHOICES
    for file_path in choice["files"]
] + [PROJECT_STANDARDS_FILE]

# Paths that appear in the source files (relative to the standards repo root).
# setup.py will prepend the computed relative prefix to each of these.
LINK_TARGETS = [
    "karpathy/",
    "ai-agent-standards/",
    "skills/",
    "SKILL-REFERENCE.md",
    "SKILL-REFERENCE_VI.md",
]


def find_project_root(start_dir: str) -> str:
    """Walk upward from *start_dir* until we hit a VCS or package marker."""
    markers = (".git", ".hg", "package.json", "Cargo.toml", "go.mod", "pom.xml",
               "build.gradle", "settings.gradle", "pyproject.toml", "Makefile")
    current = os.path.abspath(start_dir)
    while True:
        if any(os.path.exists(os.path.join(current, m)) for m in markers):
            return current
        parent = os.path.dirname(current)
        if parent == current:            # filesystem root reached
            return os.path.abspath(start_dir)
        current = parent


def add_prefix(content: str, prefix: str) -> str:
    """Add the relative prefix to all known internal link targets.

    Source files use bare relative paths (e.g. ``karpathy/principles.md``).
    After copying to an external project root, the paths need the standards
    folder prefix (e.g. ``AI-Agent-Standards/karpathy/principles.md``).
    """
    for target in LINK_TARGETS:
        # Match the target only when it is NOT already prefixed.
        # Look for it after common delimiters: (, space, >, newline, or start-of-line.
        # This avoids double-prefixing.
        pattern = r'(?<![/\w])' + re.escape(target)
        replacement = f"{prefix}/{target}"
        content = re.sub(pattern, replacement, content)
    return content


def select_rule_files(agent_key: str = None) -> list[str]:
    """Return rule files to install, prompting when no agent is provided."""
    choices_by_key = {choice["key"]: choice for choice in AGENT_CHOICES}
    if agent_key:
        normalized = agent_key.lower()
        if normalized == "all":
            return ALL_CHOICE_FILES
        if normalized in choices_by_key:
            return choices_by_key[normalized]["files"]
        valid = ", ".join([choice["key"] for choice in AGENT_CHOICES] + ["all"])
        print(f"Error: Unknown agent '{agent_key}'. Valid choices: {valid}")
        sys.exit(1)

    print("Choose which AI agent instruction file to install:")
    print("  0. Cancel")
    for number, choice in enumerate(AGENT_CHOICES, start=1):
        files = ", ".join(choice["files"])
        print(f"  {number}. {choice['label']} ({files})")
    all_number = len(AGENT_CHOICES) + 1
    print(f"  {all_number}. Choose all (install every supported instruction file)")
    print()

    while True:
        selected = input(f"Select 0-{all_number}: ").strip()
        if selected == "0":
            print("Setup cancelled.")
            sys.exit(0)
        if selected.isdigit():
            selected_number = int(selected)
            if 1 <= selected_number <= len(AGENT_CHOICES):
                return AGENT_CHOICES[selected_number - 1]["files"]
            if selected_number == all_number:
                return ALL_CHOICE_FILES
        print(f"Please enter a number from 0 to {all_number}.")


def copy_and_link(standards_dir: str, project_root: str, rule_files: list[str]) -> None:
    """Copy rule files and rewrite links."""
    # Compute the path from project root to standards directory. On Windows,
    # os.path.relpath cannot cross drive letters, so fall back to an absolute
    # path that Markdown-capable agents can still resolve.
    try:
        rel_prefix = os.path.relpath(standards_dir, project_root).replace("\\", "/")
    except ValueError:
        rel_prefix = os.path.abspath(standards_dir).replace("\\", "/")

    print(f"  Standards folder : {standards_dir}")
    print(f"  Project root     : {project_root}")
    print(f"  Link prefix      : {rel_prefix}/")
    print()

    copied = 0
    skipped = 0

    for rel_path in rule_files:
        src = os.path.join(standards_dir, rel_path)
        dst = os.path.join(project_root, rel_path)

        if not os.path.exists(src):
            print(f"  ⚠  Skip (not found): {rel_path}")
            skipped += 1
            continue

        # Don't overwrite PROJECT-STANDARDS.md if user already customized it
        if rel_path == "PROJECT-STANDARDS.md" and os.path.exists(dst):
            with open(dst, "r", encoding="utf-8") as f:
                existing = f.read()
            if "<!-- ADD YOUR STANDARDS BELOW -->" not in existing:
                print(f"  ⏭  Skip (customized): {rel_path}")
                skipped += 1
                continue

        # Ensure destination directories exist
        dst_dir = os.path.dirname(dst)
        if dst_dir:
            os.makedirs(dst_dir, exist_ok=True)

        # Copy
        shutil.copy2(src, dst)

        # Rewrite links: add the relative prefix so paths resolve from project root
        with open(dst, "r", encoding="utf-8") as f:
            content = f.read()
        content = add_prefix(content, rel_prefix)
        with open(dst, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"  ✅ {rel_path}")
        copied += 1

    print()
    print(f"Done: {copied} copied, {skipped} skipped.")
    
    # Auto-update project's .gitignore to ignore standard configuration files
    update_gitignore(project_root, standards_dir, rule_files)
    
    print()
    print('Verify by asking your AI agent: "What coding standards are you following?"')


def update_gitignore(project_root: str, standards_dir: str = None, installed_files: list[str] = None) -> None:
    """Add standard configuration files to the project's .gitignore."""
    gitignore_path = os.path.join(project_root, ".gitignore")
    
    standards_folder = "AI-Agent-Standards"
    if standards_dir:
        standards_folder = os.path.basename(standards_dir)

    files_to_ignore = [f"{standards_folder}/"]
    if installed_files:
        files_to_ignore.extend(
            file_path
            for file_path in installed_files
            if file_path != PROJECT_STANDARDS_FILE
        )


    # Read existing content if .gitignore exists, trying common encodings
    lines = []
    detected_encoding = "utf-8"
    if os.path.exists(gitignore_path):
        for enc in ["utf-8", "utf-8-sig", "utf-16", "latin-1"]:
            try:
                with open(gitignore_path, "r", encoding=enc) as f:
                    lines = f.readlines()
                detected_encoding = enc
                break
            except (UnicodeDecodeError, LookupError):
                continue

    # Normalize paths and check existing entries
    existing_rules = set()
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            # Normalize slashes for comparison
            normalized = stripped.lstrip("/").replace("\\", "/")
            existing_rules.add(normalized)

    # Filter out files that are already ignored
    to_add = []
    for item in files_to_ignore:
        if item not in existing_rules:
            to_add.append(item)

    if to_add:
        print()
        print("  📝 Updating .gitignore...")
        with open(gitignore_path, "a", encoding=detected_encoding) as f:
            # Ensure file ends with a newline before appending
            if lines and not lines[-1].endswith("\n"):
                f.write("\n")
            f.write("\n# AI Agent Coding Standards\n")
            for item in to_add:
                f.write(f"{item}\n")
                print(f"     Ignored: {item}")




def main():
    parser = argparse.ArgumentParser(
        description="Install AI Agent Coding Standards into your project."
    )
    parser.add_argument(
        "project_root",
        nargs="?",
        default=None,
        help="Path to the project root. Auto-detected if omitted.",
    )
    parser.add_argument(
        "--agent",
        choices=[choice["key"] for choice in AGENT_CHOICES] + ["all"],
        default=None,
        help="Install one agent instruction file without prompting. Use 'all' to install every supported file.",
    )
    args = parser.parse_args()

    # Resolve standards directory (parent of scripts/)
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    standards_dir = os.path.dirname(scripts_dir)

    # Resolve project root
    if args.project_root:
        project_root = os.path.abspath(args.project_root)
    else:
        project_root = find_project_root(os.path.dirname(standards_dir))

    if os.path.abspath(project_root) == os.path.abspath(standards_dir):
        print("Error: Project root is the same as the standards directory.")
        print("Run this script from your project, or pass the project root as argument.")
        sys.exit(1)

    print()
    print("🔧 AI Agent Coding Standards — Setup")
    print("=" * 42)
    rule_files = select_rule_files(args.agent)
    copy_and_link(standards_dir, project_root, rule_files)


if __name__ == "__main__":
    main()
