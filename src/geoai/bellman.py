"""Bellman operators for geometry-dependent discounting."""
from __future__ import annotations

import math
from typing import Callable, Iterable, Mapping, Sequence


def geometric_bellman(reward: float, next_value: float, proper_time_interval: float, kappa: float) -> float:
    """One-step geometric Bellman backup."""
    if proper_time_interval < 0 or kappa < 0:
        raise ValueError("proper_time_interval and kappa must be nonnegative")
    return reward + math.exp(-kappa * proper_time_interval) * next_value


def closed_loop_value(loop_reward: float, loop_proper_time: float, kappa: float) -> float:
    """Solve Q = R + exp(-kappa*tau) Q for a closed learning loop."""
    if loop_proper_time <= 0:
        raise ValueError("A positive proper-time loop is required for the finite closed-loop value.")
    if kappa <= 0:
        raise ValueError("kappa must be positive for the discounted closed-loop fixed point.")
    contraction = math.exp(-kappa * loop_proper_time)
    return loop_reward / (1.0 - contraction)


def finite_horizon_return(rewards: Sequence[float], proper_times: Sequence[float], kappa: float) -> float:
    if len(rewards) != len(proper_times):
        raise ValueError("rewards and proper_times must have equal length")
    value = 0.0
    cumulative = 0.0
    for reward, dtau in zip(rewards, proper_times):
        if dtau < 0:
            raise ValueError("proper times must be nonnegative")
        value += math.exp(-kappa * cumulative) * reward
        cumulative += dtau
    return value


def tabular_backup(q: Mapping[tuple, float], state_action: tuple, reward: float,
                   next_actions: Iterable[tuple], proper_time_interval: float,
                   kappa: float) -> float:
    """Deterministic tabular backup using the geometry-dependent discount."""
    if not next_actions:
        return reward
    next_value = max(q.get(a, 0.0) for a in next_actions)
    return geometric_bellman(reward, next_value, proper_time_interval, kappa)
