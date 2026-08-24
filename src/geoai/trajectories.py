"""Numerical trajectory utilities."""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Iterable, Sequence

from .geometry import GodelMetric


@dataclass(frozen=True)
class State:
    t: float
    x: float
    y: float
    z: float


@dataclass(frozen=True)
class Segment:
    start: State
    velocity: Sequence[float]
    duration: float


def proper_time_segment(segment: Segment, metric: GodelMetric | None = None) -> float:
    metric = metric or GodelMetric()
    return segment.duration * metric.proper_time_rate(segment.start.x, segment.velocity)


def proper_time(segments: Iterable[Segment], metric: GodelMetric | None = None) -> float:
    return math.fsum(proper_time_segment(s, metric) for s in segments)
