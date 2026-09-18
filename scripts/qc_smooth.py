#!/usr/bin/env python3
"""Stair-step smoothness helpers for qc_plate.py.

Jagged 1-bit plates have many 2x2 checkerboard stairs on ink.
Calibrated: 1152px binary shuttle ~1.28 stairs/1k perimeter (FAIL),
300dpi/smoothed plates ~0.01–0.18 (PASS).
"""
from __future__ import annotations

import numpy as np

STAIR_PER_1K_FAIL = 0.80
MIN_LONG_EDGE = 2400


def stair_mask(ink: np.ndarray) -> np.ndarray:
    a = ink[:-1, :-1]
    b = ink[:-1, 1:]
    c = ink[1:, :-1]
    d = ink[1:, 1:]
    s = np.zeros_like(ink, dtype=bool)
    s[:-1, :-1] = (a & d & ~b & ~c) | (b & c & ~a & ~d)
    return s


def perimeter_px(ink: np.ndarray) -> int:
    p = np.pad(ink, 1, constant_values=False)
    er = p[1:-1, 1:-1] & p[:-2, 1:-1] & p[2:, 1:-1] & p[1:-1, :-2] & p[1:-1, 2:]
    return int((ink & ~er).sum()) or 1


def smoothness_report(ink: np.ndarray, orig_wh: tuple[int, int]) -> dict:
    stairs = stair_mask(ink)
    peri = perimeter_px(ink)
    n = int(stairs.sum())
    per_1k = round(1000.0 * n / peri, 2)
    long_edge = max(orig_wh)
    fails: list[str] = []
    if long_edge < MIN_LONG_EDGE:
        fails.append(
            f"too coarse for print ({long_edge}px) — lines will look jagged on A4"
        )
    if per_1k > STAIR_PER_1K_FAIL and n > 20:
        fails.append(
            f"jagged stair-step lines ({per_1k} stairs/1k perimeter) — not smooth"
        )
    return {
        "stair_pixels": n,
        "perimeter_px": peri,
        "stair_per_1k": per_1k,
        "long_edge": long_edge,
        "smooth_ok": len(fails) == 0,
        "smooth_fails": fails,
        "_stair_mask": stairs,
    }
