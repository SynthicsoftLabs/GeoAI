"""Gödel spacetime primitives.

Coordinates are ordered (t, x, y, z).
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Sequence, Tuple

Matrix = Tuple[Tuple[float, ...], ...]
Vector = Sequence[float]


@dataclass(frozen=True)
class GodelMetric:
    """Gödel metric in the normalization used by GeoAI."""

    def matrix(self, x: float) -> Matrix:
        e = math.exp(x)
        return ((-1.0, 0.0, 0.0, -e),
                (0.0, 1.0, 0.0, 0.0),
                (0.0, 0.0, 1.0, 0.0),
                (-e, 0.0, 0.0, -0.5 * e * e))

    def inverse(self, x: float) -> Matrix:
        em = math.exp(-x)
        return ((1.0, 0.0, 0.0, -2.0 * em),
                (0.0, 1.0, 0.0, 0.0),
                (0.0, 0.0, 1.0, 0.0),
                (-2.0 * em, 0.0, 0.0, 2.0 * em * em))

    def determinant(self, x: float) -> float:
        return -0.5 * math.exp(2.0 * x)

    def volume_density(self, x: float) -> float:
        return math.exp(x) / math.sqrt(2.0)

    def interval_squared(self, x: float, velocity: Vector) -> float:
        tdot, xdot, ydot, zdot = velocity
        e = math.exp(x)
        return -(tdot + e * zdot) ** 2 + xdot**2 + ydot**2 + 0.5 * e**2 * zdot**2

    def proper_time_rate(self, x: float, velocity: Vector) -> float:
        q = -self.interval_squared(x, velocity)
        if q < 0:
            raise ValueError("Trajectory is spacelike for the supplied tangent.")
        return math.sqrt(q)

    def ctc_threshold_x(self) -> float:
        """Critical x at which the constant-(t,x,y) z-circles become null."""
        return math.log(2.0)

    def z_circle_interval_squared(self, x: float, dz: float = 1.0) -> float:
        """ds^2 for dt=dx=dy=0 along a z-circle."""
        return -0.5 * math.exp(2.0 * x) * dz**2
