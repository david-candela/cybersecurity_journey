#!/usr/bin/env python3
"""
publish.py — Cybersecurity Journey Publishing Automation

Usage:
    python publish.py

Prompts for room/topic details, generates a formatted markdown file,
updates the relevant index page, commits, and pushes to GitHub.
"""

import os
import re
import sys
import shutil
import subprocess
import tempfile
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).parent.resolve()
DOCS_DIR = REPO_ROOT / "docs"
SITE_URL = "https://david-candela.github.io/cybersecurity_journey"


# ── Helpers ──────────────────────────────────────────────────────────────────

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    while True:
        response = input(f"{prompt}{suffix}: ").strip()
        if response:
            return response
        if default:
            return default
        print("  This field is required. Please enter a value.")


def ask_optional(prompt: str) -> str:
    return input(f"{prompt} (press Enter to skip): ").strip()


def pick(prompt: str, options: list[tuple[str, str]]) -> str:
    """Display a numbered menu and return the chosen key."""
    print(f"\n{prompt}")
    for i, (_, label) in enumerate(options, 1):
        print(f"  [{i}] {label}")
    default_key = options[0][0]
    while True:
        raw = input(f"Choice [1]: ").strip() or "1"
        try:
            idx = int(raw) - 1
            if 0 <= idx < len(options):
                return options[idx][0]
        except ValueError:
            pass
        print(f"  Please enter a number between 1 and {len(options)}.")


# ── Note input ────────────────────────────────────────────────────────────────

def get_notes_via_editor() -> str:
    """Open $EDITOR with a temp file; fall back to terminal paste."""
    editor = os.environ.get("EDITOR") or os.environ.get("VISUAL")
    if not editor:
        for candidate in ("nano", "vim", "vi", "notepad"):
            if shutil.which(candidate):
                editor = candidate
                break

    if not editor:
        print("  No text editor found — falling back to terminal paste.")
        return get_notes_via_terminal()

    placeholder = "<!-- Write your notes here, then save and close the editor -->\n\n"
    with tempfile.NamedTemporaryFile(suffix=".md", mode="w", delete=False, encoding="utf-8") as f:
        f.write(placeholder)
        tmpfile = f.name

    try:
        result = subprocess.run([editor, tmpfile])
        if result.returncode != 0:
            print(f"  Editor exited with code {result.returncode}. Using empty notes.")
            return ""
        with open(tmpfile, encoding="utf-8") as f:
            content = f.read()
        content = content.replace(placeholder, "").strip()
        return content
    finally:
        try:
            os.unlink(tmpfile)
        except OSError:
            pass


def get_notes_via_terminal() -> str:
    print("\nPaste your notes below.")
    print("When finished, press Enter then Ctrl+D (macOS/Linux) or Ctrl+Z + Enter (Windows):\n")
    lines = []
    try:
        while True:
            lines.append(input())
    except EOFError:
        pass
    return "\n".join(lines).strip()


def get_notes() -> str:
    choice = pick(
        "How would you like to write your notes?",
        [("editor", "Open in text editor"), ("terminal", "Paste directly in terminal")],
    )
    if choice == "editor":
        return get_notes_via_editor()
    return get_notes_via_terminal()


# ── Markdown templates ────────────────────────────────────────────────────────

def build_tryhackme(
    room_name: str,
    category: str,
    difficulty: str,
    notes: str,
    key_takeaways: str,
    tools_used: str,
    today: str,
) -> str:
    takeaways = key_takeaways or "_To be added._"
    tools = tools_used or "_To be added._"
    return f"""\
# {room_name}

**Platform:** TryHackMe
**Category:** {category}
**Difficulty:** {difficulty}
**Date:** {today}

---

## Overview

{notes or "_Notes to be added._"}

---

## Key Takeaways

{takeaways}

---

## Tools Used

{tools}
"""


def build_notes(topic_name: str, category: str, notes: str, today: str) -> str:
    return f"""\
# {topic_name}

**Category:** {category}
**Date:** {today}

---

## Notes

{notes or "_Notes to be added._"}
"""


# ── Index update ──────────────────────────────────────────────────────────────

def update_tryhackme_index(index_path: Path, name: str, slug: str) -> None:
    content = index_path.read_text(encoding="utf-8")
    today_str = date.today().strftime("%d/%m/%Y")
    new_row = f"| [{name}]({slug}.md) | | {today_str} | |\n"

    # Insert after the table header row
    header_pattern = re.compile(
        r"(\| Room \| Difficulty \| Date \| Focus \|\n\|[-|]+\|\n)"
    )
    match = header_pattern.search(content)
    if match:
        content = content[: match.end()] + new_row + content[match.end() :]
    else:
        # Fallback: append before the final admonition or at end of file
        last_hr = content.rfind("\n---\n")
        insert_at = last_hr if last_hr != -1 else len(content)
        content = content[:insert_at] + f"\n- [{name}]({slug}.md)\n" + content[insert_at:]

    index_path.write_text(content, encoding="utf-8")
    print(f"  Updated: {index_path.relative_to(REPO_ROOT)}")


def update_notes_index(index_path: Path, name: str, slug: str, category: str) -> None:
    content = index_path.read_text(encoding="utf-8")
    new_item = f"- [{name}]({slug}.md)\n"

    # Try to find the right section heading
    section_map = {
        "linux": "## Linux",
        "windows": "## Windows",
        "security tools": "## Security Tools",
        "network": "## Network",
    }
    target_header = None
    for key, header in section_map.items():
        if key in category.lower():
            target_header = header
            break

    if target_header and target_header in content:
        # Find the section and append after its last list item
        section_start = content.index(target_header) + len(target_header)
        next_section = re.search(r"\n## ", content[section_start:])
        if next_section:
            section_end = section_start + next_section.start()
        else:
            # End at the next --- or end of file
            hr = content.find("\n---\n", section_start)
            section_end = hr if hr != -1 else len(content)

        section_body = content[section_start:section_end]
        # Find the last list item in this section
        last_item = list(re.finditer(r"^- .+$", section_body, re.MULTILINE))
        if last_item:
            insert_pos = section_start + last_item[-1].end()
            content = content[:insert_pos] + "\n" + new_item.rstrip("\n") + content[insert_pos:]
        else:
            content = content[:section_end] + "\n" + new_item + content[section_end:]
    else:
        # Append before the trailing --- / admonition
        last_hr = content.rfind("\n---\n")
        insert_at = last_hr if last_hr != -1 else len(content)
        content = content[:insert_at] + f"\n{new_item}" + content[insert_at:]

    index_path.write_text(content, encoding="utf-8")
    print(f"  Updated: {index_path.relative_to(REPO_ROOT)}")


# ── Git ───────────────────────────────────────────────────────────────────────

def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


def git_push(commit_message: str) -> None:
    print("\n=== Git ===")

    r = git("add", ".")
    if r.returncode != 0:
        print(f"  git add failed:\n{r.stderr.strip()}")
        sys.exit(1)

    r = git("commit", "-m", commit_message)
    if r.returncode != 0:
        if "nothing to commit" in r.stdout + r.stderr:
            print("  Nothing new to commit.")
            return
        print(f"  git commit failed:\n{r.stderr.strip()}")
        sys.exit(1)
    print(f"  Committed: {commit_message}")

    r = git("push")
    if r.returncode != 0:
        print(
            f"\n  git push failed. Push manually with:\n    git push\n\n"
            f"  Error details:\n{r.stderr.strip()}"
        )
        sys.exit(1)
    print("  Pushed to remote successfully.")


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    print("\n=== Cybersecurity Journey — Publish New Write-Up ===\n")

    today = date.today().strftime("%Y-%m-%d")

    # 1. Name
    name = ask("Room / Topic name (e.g. 'Advent of Cyber Day 3')")

    # 2. Section
    section = pick(
        "Which section does this belong to?",
        [("tryhackme", "TryHackMe Write-Up"), ("notes", "Study Notes")],
    )

    slug = slugify(name)

    if section == "tryhackme":
        output_dir = DOCS_DIR / "tryhackme"
        index_path = output_dir / "index.md"
        print()
        category = ask("Category (e.g. Phishing, Forensics, SOC, Networking)")
        difficulty = ask("Difficulty", default="Easy")
    else:
        output_dir = DOCS_DIR / "notes"
        index_path = output_dir / "index.md"
        print()
        category = ask("Category (e.g. Linux, Windows, Security Tools)")

    # 3. Notes
    print()
    notes = get_notes()

    # 4. Optional fields
    if section == "tryhackme":
        print()
        key_takeaways = ask_optional("Key Takeaways (brief summary or bullet points)")
        tools_used = ask_optional("Tools Used (comma-separated list)")

    # 5. Build content
    if section == "tryhackme":
        content = build_tryhackme(name, category, difficulty, notes, key_takeaways, tools_used, today)
    else:
        content = build_notes(name, category, notes, today)

    # 6. Save file
    output_path = output_dir / f"{slug}.md"
    if output_path.exists():
        overwrite = input(
            f"\n  {output_path.relative_to(REPO_ROOT)} already exists. Overwrite? [y/N]: "
        ).strip().lower()
        if overwrite != "y":
            print("  Aborted.")
            sys.exit(0)

    output_path.write_text(content, encoding="utf-8")
    print(f"\n  Created: {output_path.relative_to(REPO_ROOT)}")

    # 7. Update index page
    if index_path.exists():
        if section == "tryhackme":
            update_tryhackme_index(index_path, name, slug)
        else:
            update_notes_index(index_path, name, slug, category)
    else:
        print(f"  Note: index file not found at {index_path.relative_to(REPO_ROOT)}, skipping.")

    # 8. Remind about mkdocs.yml nav
    rel_path = f"{section}/{slug}.md"
    print(f"\n  Reminder: add the following line to your mkdocs.yml nav section if needed:")
    print(f"    - {name}: {rel_path}")

    # 9. Git commit + push
    git_push(f"Add write-up: {name}")

    # 10. Live URL
    live_url = f"{SITE_URL}/{section}/{slug}/"
    print(f"\n✓ Done! Your page will be live at:\n  {live_url}")
    print("  (GitHub Actions typically deploys within 1–2 minutes)\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Cancelled.")
        sys.exit(0)
