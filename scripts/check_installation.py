#!/usr/bin/env python3
"""Verify the coloring-book skill pack is complete."""
from __future__ import annotations

import sys
from pathlib import Path

REQUIRED_FILES = [
    "SKILL.md",
    "references/style-guide.md",
    "references/intensity.md",
    "references/inventory-card.md",
    "references/element-list.md",
    "references/qc-inspector.md",
    "references/style-memory.md",
    "references/ibon-print.md",
    "scripts/cleanup_lines.py",
    "scripts/region_edit.py",
    "scripts/compose_a4_pdf.py",
    "scripts/qc_plate.py",
    "scripts/vectorize_plate.py",
]


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    missing = [rel for rel in REQUIRED_FILES if not (root / rel).is_file()]
    try:
        from PIL import Image  # noqa: F401
        pillow = True
    except ImportError:
        pillow = False
    try:
        import numpy  # noqa: F401
        numpy_ok = True
    except ImportError:
        numpy_ok = False

    if missing or not pillow or not numpy_ok:
        print("INSTALL FAIL")
        for rel in missing:
            print(f"  missing {rel}")
        if not pillow:
            print("  Pillow is not importable")
        if not numpy_ok:
            print("  numpy is not importable")
        return 1
    print(f"INSTALL PASS {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
