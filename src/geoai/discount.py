"""Proper-time discounting."""
from __future__ import annotations

import math
from typing import Iterable

from .trajectories import Segment, proper_time
from .geometry import GodelMetric


def geometric_discount(proper_time_interval: float, kappa: float) -> float:
    if proper_time_interval < 0:
        raise ValueError("Proper time must be nonnegative.")
    if kappa < 0:
        raise ValueError("kappa must be nonnegative.")
    return math.exp(-kappa * proper_time_interval)


def trajectory_discount(segments: Iterable[Segment], kappa: float, metric: GodelMetric | None = None) -> float:
    return geometric_discount(proper_time(segments, metric), kappa)
