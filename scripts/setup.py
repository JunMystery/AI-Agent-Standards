#!/usr/bin/env python3
"""
AI Agent Coding Standards — Automated Setup Script

This script copies the required AI instruction files from the standards
directory to the project root and rewrites internal links so every AI
tool can auto-discover them.

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
RULE_FILES = [
    "CLAUDE.md",
    "GEMINI.md",
    "COPILOT.md",
    ".instructions.md",
    ".cursorrules",
    ".cursor/rules/karpathy-guidelines.mdc",
    "PROJECT-STANDARDS.md",
]

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


def copy_and_link(standards_dir: str, project_root: str) -> None:
    """Copy rule files and rewrite links."""
    # Compute the relative path from project root → standards directory
    rel_prefix = os.path.relpath(standards_dir, project_root).replace("\\", "/")

    print(f"  Standards folder : {standards_dir}")
    print(f"  Project root     : {project_root}")
    print(f"  Link prefix      : {rel_prefix}/")
    print()

    copied = 0
    skipped = 0

    for rel_path in RULE_FILES:
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
    update_gitignore(project_root)
    
    print()
    print('Verify by asking your AI agent: "What coding standards are you following?"')


def update_gitignore(project_root: str) -> None:
    """Add standard configuration files to the project's .gitignore."""
    gitignore_path = os.path.join(project_root, ".gitignore")
    files_to_ignore = [
        "AI-Agent-Standards/",
        "CLAUDE.md",
        "GEMINI.md",
        "COPILOT.md",
        ".instructions.md",
        ".cursorrules",
        ".cursor/rules/karpathy-guidelines.mdc",
    ]

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
                f.write(f"/{item}\n")
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
    copy_and_link(standards_dir, project_root)


if __name__ == "__main__":
    main()
