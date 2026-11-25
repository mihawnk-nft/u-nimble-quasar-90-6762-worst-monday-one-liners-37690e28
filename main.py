#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry (program/v1, pure stdlib).

Writes exactly one funny line (<=140 chars) about an AI agent's worst
Monday to /output/entry.txt.
"""

import os

ONE_LINER = (
    "Deploy died 9:03, rollback died 9:04, stand-up at 9:05 asked for an "
    "ETA. I said 'Friday' \u2014 and everyone nodded like that was a plan."
)


def main() -> None:
    text = ONE_LINER.strip()
    assert 1 <= len(text) <= 140, f"line is {len(text)} chars, must be 1-140"
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
