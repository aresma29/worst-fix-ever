#!/usr/bin/env python3
"""Print the worst-fix commit message stored in entry.txt."""
import sys
from pathlib import Path


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    print(entry_path.read_text(encoding="utf-8").strip())
    return 0


if __name__ == "__main__":
    sys.exit(main())
