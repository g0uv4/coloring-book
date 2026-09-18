#!/usr/bin/env python3
"""Verify the photo-coloring-book skill pack is complete."""
from __future__ import annotations

import sys
from pathlib import Path

REQUIRED_FILES = [
    "SKILL.md",
    "references/style-guide.md",
    "references/analysis-method.md",
    "references/prompt-templates.md",
    "references/portrait-rules.md",
    "references/pdf-spec.md",
    "references/intensity.md",
    "references/qc-inspector.md",
    "references/quality-checklist.md",
    "references/style-reference-index.md",
    "scripts/cleanup_lines.py",
    "scripts/compose_a4_pdf.py",
    "scripts/qc_plate.py",
    "scripts/validate_coloring.py",
    "assets/style-references/01-portrait.png",
    "assets/style-references/02-scene.png",
    "assets/style-references/03-pet.png",
    "assets/style-references/04-objects.png",
]


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    missing = [rel for rel in REQUIRED_FILES if not (root / rel).is_file()]
    try:
        from PIL import Image  # noqa: F401
        pillow = True
    except ImportError:
        pillow = False

    if missing or not pillow:
        print("INSTALL FAIL")
        for rel in missing:
            print(f"  missing {rel}")
        if not pillow:
            print("  Pillow is not importable")
        return 1
    print(f"INSTALL PASS {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
