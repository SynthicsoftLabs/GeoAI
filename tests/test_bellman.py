import math

from geoai.bellman import closed_loop_value, geometric_bellman, finite_horizon_return


def test_geometric_backup():
    assert math.isclose(geometric_bellman(2.0, 10.0, 1.0, 1.0), 2.0 + math.exp(-1.0) * 10.0)


def test_closed_loop_fixed_point():
    r, tau, kappa = 3.0, 2.0, 0.4
    q = closed_loop_value(r, tau, kappa)
    assert math.isclose(q, r + math.exp(-kappa * tau) * q)


def test_finite_return():
    value = finite_horizon_return([1.0, 2.0], [1.0, 1.0], 1.0)
    assert math.isclose(value, 1.0 + 2.0 * math.exp(-1.0))
