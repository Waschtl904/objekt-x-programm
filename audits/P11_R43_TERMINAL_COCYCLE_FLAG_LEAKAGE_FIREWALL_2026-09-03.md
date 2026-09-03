# P11 R43 — terminal cocycle / C6a flag-leakage firewall

Date: 2026-09-03

## Exact point

The companion hardening defines the exact moving-range partial isometry
\[
\mathcal T_{U\to V}=W_VW_U^*
:\operatorname{Ran}W_U\to\operatorname{Ran}W_V
\]
with
\[
\mathcal T_{V\to Z}\mathcal T_{U\to V}=\mathcal T_{U\to Z}
\]
on \(\operatorname{Ran}W_U\).

This settles the **algebraic cocycle prerequisite** for a discrete terminal telescoping
argument.  It does not supply a flag-leakage estimate.

## Why frozen C6a triangularity does not automatically solve the new gate

C6a proves triangularity for the **native source/profile inclusion**
\[
\iota_{R,S}:\mathcal H_R\hookrightarrow\mathcal H_S,
\qquad
\iota_{R,S}(\mathcal H_R^{[m]})\subseteq\mathcal H_S^{[m]},
\]
and in the canonical jet ONBs its matrix is lower triangular with positive diagonal.

The terminal isometry, however, is
\[
W_U
=
G_{S,U}^{1/2}J_{R,S}G_{R,U}^{-1/2},
\]
or in profile coordinates the corresponding square-root normalized map.  The positive
square-root factors need not preserve the jet flag.  C6a's own Gram-angle firewall proves
that self-Gram/Cholesky data do not determine the cross-terminal frame angle.

Therefore no implication
\[
\iota_{R,S}\text{ triangular}
\Longrightarrow
W_U\text{ triangular}
\Longrightarrow
\mathcal T_{U\to V}\text{ triangular}
\]
is permitted.

The remaining new mathematical problem is exactly the off-flag part of
\(\mathcal T_{U\to V}\).

## Quantitative target

For the canonical deep-flag projections
\[
P_S^{[m]}=P_{\mathcal H_S^{[m]}},
\]
seek estimates of the form
\[
\|P_S^{[m]}\mathcal T_{U\to V}x\|
\le
\|P_S^{[r(m)]}x\|+\operatorname{Leak}_{m}(U,V)\|x\|,
\]
with
\[
r(m)\to\infty,
\qquad
\operatorname{Leak}_{m}(U,V)\to0
\]
in a regime that is summable/telescopable along a cofinal terminal chain.

Equivalently, a clean operator block target is
\[
\boxed{
\|P_S^{[m]}\mathcal T_{U\to V}(I-P_S^{[r(m)]})\|
\le
\operatorname{Leak}_{m}(U,V).
}
\]
The domain here is implicitly restricted to \(\operatorname{Ran}W_U\), the natural domain
of the partial isometry.

This is the first place where one must control **relative terminal orientation plus jet
flag**, rather than self-Gram geometry alone.

## Status

- algebraic moving-range cocycle: exact;
- native C6a triangularity: frozen input;
- transfer of triangularity to terminal gauges: **not proved**;
- one-step terminal flag leakage: **OPEN**;
- B-FLAGTIGHT / Strong Terminal: **OPEN**.

No promotion follows from this firewall.
