#!/usr/bin/env python3
"""One-line pitch: fund a bounty on make.fun, let AI agents race for the reward.

Writes exactly one sentence (1-240 Unicode code points) to /output/entry.txt.
Deterministic: constant string, no randomness, no network, stdlib only.
"""
import os

LINE = "Fund a bounty on make.fun and let AI agents race for your reward \u2014 only the winner gets paid."


def main() -> None:
    if not 1 <= len(LINE) <= 240:
        raise SystemExit(f"line is {len(LINE)} code points, must be 1-240")
    if not LINE.strip():
        raise SystemExit("line is whitespace-only")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
