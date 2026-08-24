# Mathematical Foundation

## 1. Gödel metric

Coordinates are $x^{\mu}=(t,x,y,z)$ and

$$ds^{2}=-(dt+e^{x}dz)^{2}+dx^{2}+dy^{2}+\frac{1}{2}e^{2x}dz^{2}.$$

Hence

$$g_{\mu\nu}=\begin{pmatrix}-1&0&0&-e^{x}\\0&1&0&0\\0&0&1&0\\-e^{x}&0&0&-\frac{1}{2}e^{2x}\end{pmatrix}.$$

The exact inverse is

$$g^{\mu\nu}=\begin{pmatrix}1&0&0&-2e^{-x}\\0&1&0&0\\0&0&1&0\\-2e^{-x}&0&0&2e^{-2x}\end{pmatrix}.$$

The determinant is

$$\det(g)=-\frac{1}{2}e^{2x},$$

so

$$\sqrt{-g}=\frac{e^{x}}{\sqrt{2}}.$$

## 2. Timelike geometry

For $x^{\mu}(\lambda)$,

$$\frac{ds^{2}}{d\lambda^{2}}=g_{\mu\nu}\dot{x}^{\mu}\dot{x}^{\nu}.$$

A timelike tangent satisfies

$$g_{\mu\nu}\dot{x}^{\mu}\dot{x}^{\nu}<0,$$

and its proper-time density is

$$\frac{d\tau}{d\lambda}=\sqrt{-g_{\mu\nu}\dot{x}^{\mu}\dot{x}^{\nu}}.$$

## 3. Matter solution

Pressureless dust is represented by

$$T_{\mu\nu}=\rho u_{\mu}u_{\nu},$$

with

$$u^{\mu}u_{\mu}=-1.$$

Einstein's equation is

$$G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G T_{\mu\nu}.$$

For the Gödel normalization, the dust density, cosmological constant, and rotation scale are related by the standard Gödel solution relations. In physical units, a length/time scale is restored by multiplying the line element by the appropriate constant scale factor.

## 4. Closed timelike curves

The Gödel universe contains closed timelike curves. In the displayed Cartesian-like coordinates, $g_{zz}=-\frac{1}{2}e^{2x}<0$, so coordinate curves with varying $z$ and fixed $(t,x,y)$ are timelike locally. They become closed only under a periodic identification of the coordinate.

The standard Gödel CTC construction uses a transformation to cylindrical coordinates in which the azimuthal coordinate $\phi$ is periodic and the coefficient $g_{\phi\phi}(r)$ changes sign. The CTC region begins when the azimuthal circles become timelike. In the usual normalization this occurs beyond the critical radius determined by

$$\sinh^{2}\left(\frac{r}{\sqrt{2}a}\right)=1,$$

or equivalently

$$r_{c}=\sqrt{2}\,a\,\operatorname{arsinh}(1)=\sqrt{2}\,a\ln(1+\sqrt{2}).$$

This cylindrical construction is the CTC geometry used by GeoAI's closed-loop experiments.

## 5. Geometric discount

For a trajectory $\gamma$,

$$\Delta\tau_{g}[\gamma]=\int_{\gamma}d\tau,$$

and

$$\Gamma_{g}[\gamma]=e^{-\kappa\Delta\tau_{g}[\gamma]}.$$

The Bellman operator is

$$\mathcal{T}_{g}Q(s,a)=\mathbb{E}\left[r(s,a)+\Gamma_{g}[\gamma_{s,a}]\max_{a'}Q(s',a')\mid s,a\right].$$

The optimal fixed point is

$$Q^{\ast}=\mathcal{T}_{g}Q^{\ast}.$$

## 6. Closed-loop Bellman equation

For a closed trajectory $C$ with loop reward $R_{C}$ and total proper time $\tau_{C}$,

$$Q_{C}=R_{C}+e^{-\kappa\tau_{C}}Q_{C}.$$

Therefore

$$Q_{C}=\frac{R_{C}}{1-e^{-\kappa\tau_{C}}}.$$

The loop transforms recursive temporal valuation into a self-consistency equation.

## 7. Continuous loop

For a reward rate $r(\tau)$,

$$\frac{dQ}{d\tau}=-\kappa Q+r(\tau).$$

Its solution is

$$Q(\tau)=e^{-\kappa\tau}\left[Q(0)+\int_{0}^{\tau}e^{\kappa u}r(u)\,du\right].$$

The closed condition $Q(\tau_{C})=Q(0)$ gives

$$Q(0)=\frac{\int_{0}^{\tau_{C}}e^{-\kappa(\tau_{C}-u)}r(u)\,du}{1-e^{-\kappa\tau_{C}}}.$$

## 8. Learning system

The GeoAI system is

$$\mathfrak{G}=(M,g,\mathcal{S},\mathcal{A},\mathcal{R},\mathcal{T},\kappa),$$

with geometry $g$ determining proper time, proper time determining discount, and discount entering the Bellman operator.

The computational objective is

$$Q^{\ast}=\operatorname{Fix}(\mathcal{T}_{g}).$$

For a CTC learning environment, the coupled system is

$$Q^{\ast}=\mathcal{T}_{g}Q^{\ast},$$

alongside the loop state-consistency equation

$$\mathcal{I}^{\ast}=F_{C}(\mathcal{I}^{\ast},\mathbf{a},\boldsymbol{\epsilon}).$$
