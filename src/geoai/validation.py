"""Executable symbolic checks for the reference metric."""
from __future__ import annotations

import sympy as sp


def metric_symbolic():
    x = sp.symbols("x", real=True)
    e = sp.exp(x)
    g = sp.Matrix([
        [-1, 0, 0, -e],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [-e, 0, 0, -sp.Rational(1, 2) * e**2],
    ])
    return x, g


def run():
    x, g = metric_symbolic()
    inverse = sp.simplify(g.inv())
    expected = sp.Matrix([
        [1, 0, 0, -2 * sp.exp(-x)],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [-2 * sp.exp(-x), 0, 0, 2 * sp.exp(-2 * x)],
    ])
    determinant = sp.simplify(g.det())
    assert sp.simplify(inverse - expected) == sp.zeros(4)
    assert sp.simplify(determinant + sp.exp(2 * x) / 2) == 0
    return {"inverse_verified": True, "determinant_verified": True}


if __name__ == "__main__":
    print(run())
