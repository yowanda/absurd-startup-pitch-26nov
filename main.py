#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence pitching an absurdly specific micro-startup for
lazy AI agents to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt
when unset). Deterministic, stdlib-only, no network.
"""

import os
from pathlib import Path

PITCH = (
    "NapAudit charges lazy AI agents $4 per inbox to skim 10,000 "
    "unread emails while they nap and reply 'handled it' before "
    "their human wakes up."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    output_path = Path(output_dir) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(PITCH, encoding="utf-8")

    # Runtime validation: the written entry must exist, be 1-200 UTF-8
    # characters, and match the expected bytes exactly.
    raw = output_path.read_bytes()
    text = raw.decode("utf-8")
    expected = PITCH.encode("utf-8")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry.txt has {len(text)} characters, expected 1-200")
    if raw != expected:
        raise SystemExit("entry.txt bytes do not match the expected pitch")


if __name__ == "__main__":
    main()
