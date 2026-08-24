# GeoAI

## Geometric Reinforcement Learning on Gödel Spacetime

GeoAI is a research and computational framework for reinforcement learning whose temporal discount functional is defined from Lorentzian spacetime geometry.

The reference spacetime is the Gödel universe:

$$ds^2=-(dt+e^x dz)^2+dx^2+dy^2+\frac12e^{2x}dz^2.$$

The metric tensor is

$$g_{\mu\nu}=\begin{pmatrix}-1&0&0&-e^x\\0&1&0&0\\0&0&1&0\\-e^x&0&0&-\frac12e^{2x}\end{pmatrix}.$$

Its inverse is

$$g^{\mu\nu}=\begin{pmatrix}1&0&0&-2e^{-x}\\0&1&0&0\\0&0&1&0\\-2e^{-x}&0&0&2e^{-2x}\end{pmatrix}.$$

The determinant and volume density are

$$\det g=-\frac12e^{2x},\qquad\sqrt{-g}=\frac{e^x}{\sqrt2}.$$

## Geometric discount

For a timelike trajectory $x^\mu(\lambda)$,

$$d\tau=\sqrt{-g_{\mu\nu}\dot x^\mu\dot x^\nu}\,d\lambda.$$

GeoAI defines

$$\Gamma[\gamma]=\exp\left(-\kappa\int_\gamma d\tau\right),$$

and the geometric Bellman operator

$$\mathcal T_gQ(s,a)=\mathbb E\left[r(s,a)+\Gamma[\gamma_{s,a}]\max_{a'}Q(s',a')\right].$$

The optimal value satisfies

$$Q^*=\mathcal T_gQ^*.$$

For a closed timelike learning loop with total proper time $\tau_C$ and loop reward $R_C$,

$$Q_C=R_C+e^{-\kappa\tau_C}Q_C,$$

so

$$Q_C=\frac{R_C}{1-e^{-\kappa\tau_C}}.$$

## Repository

- `src/geoai/geometry.py` — metric, inverse metric, determinant, proper-time density, CTC threshold.
- `src/geoai/discount.py` — geometric discount functional.
- `src/geoai/bellman.py` — geometric Bellman operators and closed-loop fixed points.
- `src/geoai/trajectories.py` — trajectory representations and numerical proper time.
- `src/geoai/validation.py` — symbolic and numerical verification routines.
- `tests/` — executable mathematical validation.
- `experiments/` — reproducible numerical experiments.
- `docs/` — formal mathematical specification.

## Quick start

```bash
python -m pip install -e .[dev]
pytest -q
python -m geoai.validation
```

## Research identity

GeoAI treats the spacetime metric as a first-class component of the learning environment. Geometry determines proper time; proper time determines trajectory discounting; trajectory discounting enters the Bellman recursion; closed timelike trajectories convert temporal recursion into a global fixed-point condition.

## License

MIT License.