#!/usr/bin/env python3
"""Compute dynamic pressure and force coefficients from a lab CSV.

Example:
  python tools/compute_coefficients.py labs/data-template.csv
"""

from __future__ import annotations

import argparse
import csv
import math
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path, help="Path to measurement CSV")
    args = parser.parse_args()

    if not args.csv_path.is_file():
        print(f"File not found: {args.csv_path}", file=sys.stderr)
        return 1

    with args.csv_path.open(newline="") as f:
        rows = list(csv.DictReader(f))

    if not rows:
        print("No data rows found.", file=sys.stderr)
        return 1

    print(
        f"{'run':>4} {'config':<10} {'v':>6} {'q':>8} {'Re':>10} "
        f"{'Cd':>7} {'Cl':>7} {'|Cl|/Cd':>8}"
    )
    for row in rows:
        try:
            v = float(row["airspeed_m_s"])
            rho = float(row["rho_kg_m3"])
            area = float(row["ref_area_m2"])
            length = float(row["length_L_m"])
            fd = float(row["F_drag_N"])
            fl = float(row["F_lift_N"])
        except (KeyError, ValueError) as exc:
            print(f"Skipping row {row.get('run_id')}: {exc}", file=sys.stderr)
            continue

        q = 0.5 * rho * v * v
        # Kinematic viscosity of air ~ 1.5e-5 m^2/s (room conditions)
        nu = 1.5e-5
        re = v * length / nu if nu else float("nan")
        cd = fd / (q * area) if q * area else float("nan")
        cl = fl / (q * area) if q * area else float("nan")
        eff = abs(cl) / cd if cd else float("nan")

        print(
            f"{row.get('run_id', ''):>4} {row.get('config_id', ''):<10} "
            f"{v:6.2f} {q:8.2f} {re:10.2e} {cd:7.3f} {cl:7.3f} {eff:8.3f}"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
