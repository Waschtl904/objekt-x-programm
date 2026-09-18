# Theorem overview and dependency graph

## 1. Main consolidated theorem

At commit `6a16d90b551588572c87e622c21c2df7f7b1adc2` the endpoint

\[
B=\frac{\log 5}{2}
\]

is certified with active channels `2,3,4`, channel `5` at zero-measure entrance, and exactly the two original Mellin conditions:

\[
Q_W[u] > 10^{-13}\|u\|_2^2
\quad
(0<a\le B,\ 0\ne u\in\mathcal W_a).
\]

The interval conclusion uses exact zero extension, not a parameter grid.

Status: `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`.

## 2. Structural theorems

### Universal prime-power family — `28351975097ed024ffa6a65145bc4a4d9b63d827`

On the fixed reference space:

\[
q_a=D_H+V+q_0(a)I-K_a-
\sum_{q=p^k,\ \log q<2a}\frac{\Lambda(q)}{\sqrt q}\,T_{\log q/a}.
\]

It includes unitary scaling, the exact prime-power weights, bounded self-adjoint partial shifts for arbitrary `0<d<2`, finite active sets, exact Mellin transport, cutoff treatment at `d=2`, and exact window functoriality.

### Active-set segment Schur — `a18f90a867bfba2798068d5566a4e38a09013c01`

For an arbitrary finite active set, including overlapping shift bands `d<1`, the complete low/tail Gram of

`V - K_gamma - sum_q w_q T_dq`

is reduced to exact band-intersection polynomial integrals plus analytic logarithmic moments. The finite low block does not replace the infinite operator; the entire tail is retained through Parseval identities.

### Exact window functoriality

For `0<a<=b`:

\[
q_b[J_{a,b}f]=q_a[f],\qquad
\|J_{a,b}f\|_2=\|f\|_2,
\]

and

\[
M_{b,\pm}(J_{a,b}f)=\sqrt{a/b}\,M_{a,\pm}(f).
\]

Thus an endpoint theorem transfers to every smaller connected window with the same gap.

## 3. Diagnostic theorems after the endpoint

### Explicit near-null source — `9d9c48de2d6e4d56556f38f45489d133c17bd181`

The explicit even source at `B=log(5)/2` has direct Rayleigh quotient approximately

\[
3.296290826616\times10^{-12}.
\]

A separate exact-Mellin full-window transported family remains positive through `log(7)/2`, but this is one selected family and not an all-source endpoint theorem.

### Window-gap monotonicity — `fc597f6129db57787c85ec20627ed608233187ba`

For the true variational infima:

\[
a<b\Longrightarrow
\lambda_e(b)\le\lambda_e(a),\quad
\lambda_o(b)\le\lambda_o(a),\quad
\lambda(b)\le\lambda(a).
\]

The physical zero extension of the near-null source therefore gives a permanent upper ceiling below `3.3e-12` for the later even gap.

## 4. Logical dependency graph

```text
Imported connected nonpole identity
        |
        +------------------------------+
        |                              |
        v                              v
Universal prime-power family      Active-set segment Schur
28351975...                       a18f90a8...
        |                              |
        +---------------+--------------+
                        v
Endpoint B = log(5)/2, active {2,3,4}
6a16d90...
                        |
             +----------+----------+
             |                     |
             v                     v
Near-null source audit       Exact zero-extension law
9d9c48de...                  (structural family)
             |                     |
             +----------+----------+
                        v
Window-gap monotonicity / inherited resonance
fc597f6...
```

The earlier Prime-2 theorem `eea8ff64...` and Prime-2/3 theorem `213edfd3...` are important independently reproducible predecessor theorems and cross-checks. The final `log(5)/2` theorem recomputes its endpoint certificate and should not be represented as merely concatenating their numerical gaps.

## 5. Imported anchor and epistemic firewall

The endpoint packages import the corrected connected nonpole-form identity, cited in the research line by anchor `9aa5cb1edac72fc683c5c9aba5a1f0639fbbf8bb` and its surrounding corrected C1 sources.

This consolidation does **not** re-audit that imported identity externally. It remains part of the independent review obligation. The same applies to the analytic domain arguments, full-tail identities, moment transports and exact-form correspondence used downstream.
