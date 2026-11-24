#!/usr/bin/env python3
"""Entrypoint for 'Break Production, Own It'.

Writes one brutally honest production-break confession to /output/entry.txt.
Gate: UTF-8, 1-200 characters, not only whitespace, single line.
"""

import os

LINE = (
    "I skipped the migration test, approved my own pull request, and deployed "
    "at 5:58 p.m. on a Friday. My cleanup script dropped the users table. "
    "Every row. Nobody else touched it. That was me."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line length {len(LINE)} outside 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)
    print(f"wrote {len(LINE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
