"""Generate closed-loop geometric Bellman values for a parameter grid."""
from __future__ import annotations

import csv
from pathlib import Path

from geoai.bellman import closed_loop_value


def main() -> None:
    out = Path("results/closed_loop_values.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["kappa", "loop_proper_time", "loop_reward", "Q"])
        for kappa in (0.1, 0.25, 0.5, 1.0):
            for tau in (0.25, 0.5, 1.0, 2.0, 4.0):
                q = closed_loop_value(1.0, tau, kappa)
                writer.writerow([kappa, tau, 1.0, q])


if __name__ == "__main__":
    main()
