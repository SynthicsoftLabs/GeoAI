import math

from geoai.geometry import GodelMetric


def test_metric_inverse_diagonal_identity():
    g = GodelMetric().matrix(0.7)
    gi = GodelMetric().inverse(0.7)
    product = [[sum(g[i][k] * gi[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            assert math.isclose(product[i][j], 1.0 if i == j else 0.0, abs_tol=1e-12)


def test_determinant():
    x = 0.3
    assert math.isclose(GodelMetric().determinant(x), -0.5 * math.exp(2 * x))


def test_stationary_proper_time():
    assert GodelMetric().proper_time_rate(0.0, (1.0, 0.0, 0.0, 0.0)) == 1.0


def test_gtt_inverse_component():
    assert GodelMetric().inverse(1.2)[0][0] == 1.0
