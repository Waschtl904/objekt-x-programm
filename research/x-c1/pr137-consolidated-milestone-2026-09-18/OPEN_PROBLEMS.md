# Scope firewall and open problems

## Proven in the present author-derived milestone

- Connected NULLPOL positivity through `a=log(5)/2` with exactly two Mellin conditions.
- Universal finite active-set prime-power operator family.
- Exact window functoriality under zero extension.
- Infinite-tail and moment treatment for the certified endpoint instances.
- Explicit real near-null even source at `a=log(5)/2`.
- Nonincreasing optimal window gap under domain expansion.

## Not proved

- all-source positivity at `log(7)/2`;
- all-source positivity at `a=1`;
- a prime-independent positive reserve valid across every later segment;
- a canonical positive C1 output/readout compatible with all individual channels;
- the global C0/C1 intertwiner;
- positivity on arbitrary unbounded windows or the full global Weil test class;
- full C1-GEOM;
- Object X;
- RH;
- publication novelty or priority;
- indepent external mathematical validation.

## Immediate next research front — outside this milestone

Let

\[
B=\frac{\log5}{2},\qquad
E_{B,b}=J_{B,b}\mathcal W_B^{\rm even}
\subset\mathcal W_b^{\rm even}.
\]

For `b>B`, decompose the already constrained even source space in `L^2`:

\[
\mathcal W_b^{\rm even}=E_{B,b}\oplus Z_b
\]

and write

\[
F_b=\begin{pmatrix}A_B&C_b^*\\ C_b&D_b\end{pmatrix}.
\]

The next qualitative gate is the inherited-resonance / new-direction shell-Schur problem:

1. prove `D_b >= delta_sh(b) I > 0` on a right interval;
2. control the actual core-shell coupling `C_b`, especially on the inherited near-null sector;
3. prove positivity of `A_B-C_b^*D_b^{-1}C_b` on the full inherited core;
4. determine whether newly available directions leave the inherited gap unchanged or push it lower.

A failed lower comparison is not a negative Weil vector. C15 is not forced unless a genuine controlled nonpositive direction or another structural obstruction is established.

## Recommended repository/process boundary

Treat the mathematical state through `fc597f6129db57787c85ec20627ed608233187ba` as the frozen positive milestone for PR #137. A documentation-only consolidation commit may sit on top of that parent. New shell-Schur experiments should be developed in a separate PR/research branch so that the positive milestone remains auditable and stable.

No merge or status promotion should be interpreted as independent review. External review must separately cover the imported connected identity, analytic operator arguments, tail completeness, moment transport, and endpoint interval arithmetic.
