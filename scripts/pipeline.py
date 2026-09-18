#!/usr/bin/env python3
"""One-process cleanup → QC → vector PDF. Avoids three interpreter starts.

Usage:
  python3 scripts/pipeline.py plate-raw.png --out-dir run --pdf plate-a4.pdf
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def run(cmd: list[str]) -> int:
    print("+", " ".join(cmd), file=sys.stderr)
    return subprocess.call(cmd)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path)
    p.add_argument("--out-dir", type=Path, default=Path("."))
    p.add_argument("--pdf", type=Path, default=None)
    p.add_argument("--jpeg", type=Path, default=None)
    p.add_argument("--skip-qc", action="store_true")
    p.add_argument("--orientation", default="portrait")
    args = p.parse_args()
    if not args.input.is_file():
        print(f"FAIL missing {args.input}", file=sys.stderr)
        return 2
    out = args.out_dir
    out.mkdir(parents=True, exist_ok=True)
    clean = out / "plate-clean.png"
    svg = out / "plate.svg"
    pdf = args.pdf or (out / "plate-a4.pdf")
    py = sys.executable
    rc = run(
        [
            py,
            str(ROOT / "cleanup_lines.py"),
            str(args.input),
            str(clean),
            "--threshold",
            "128",
            "--min-long-edge",
            "3200",
            "--smooth",
            "1.2",
        ]
    )
    if rc != 0:
        return rc
    if not args.skip_qc:
        report = out / "qc-report.json"
        rc = run([py, str(ROOT / "qc_plate.py"), str(clean), "--report", str(report)])
        if report.is_file():
            data = json.loads(report.read_text())
            if not data.get("ok", False):
                print("QC FAIL — not composing PDF", file=sys.stderr)
                return 1
        elif rc != 0:
            return rc
    cmd = [
        py,
        str(ROOT / "vectorize_plate.py"),
        str(clean),
        str(svg),
        "--pdf",
        str(pdf),
        "--orientation",
        args.orientation,
        "--margin-mm",
        "14",
    ]
    if args.jpeg:
        cmd += ["--jpeg", str(args.jpeg)]
    return run(cmd)


if __name__ == "__main__":
    raise SystemExit(main())
