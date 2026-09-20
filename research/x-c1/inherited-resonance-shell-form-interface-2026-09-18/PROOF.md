# X-C1 INHERITED RESONANCE — shell form domain and inverse-free relative Schur criterion

**Date:** 2026-09-18  
**Status:** `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`  
**Research branch:** `research/x-c1-inherited-resonance-shell-schur-2026-09-18`  
**Parent:** `0ec5276b2e0a2fe0aa700503e40b4a6a0acb65ff`.  
**Scope:** form-domain interface for the complete nonorthogonal shell lift to the right of `B=log(5)/2`. No new positive endpoint.

## 1. Input from the coordinate gate

Put
\[
B=\frac{\log5}{2},\qquad B<b\le1,
\]
and let
\[
\mathcal W_b^{\rm e}
=\{u\in H^1_0((-b,b)):u(-x)=u(x),\ \langle u,\cosh(x/2)\rangle=0\}.
\]
The preceding shell-coordinate theorem gives the topological direct sum
\[
\mathcal W_b^{\rm e}
=J_{B,b}\mathcal W_B^{\rm e}\ \dotplus\ L_{B,b}\mathcal S_{B,b},
\qquad
\mathcal S_{B,b}=\{s\in H^1(B,b):s(b)=0\},                 \tag{1}
\]
with a bounded linear lift `L_(B,b)` and exact old-core window law
\[
Q_b[J_{B,b}w]=Q_B[w].                                      \tag{2}
\]
The sum in (1) is deliberately nonorthogonal. No `L^2` projection onto the old core is used.

## 2. Common-jump representation on the lifted shell

On the two-Mellin class the frozen common-jump identity is
\[
Q_b[u]=\|\mathcal X_bu\|_{\mathscr H_b}^2-\Gamma_b\|u\|_2^2, \tag{3}
\]
where
\[
\Gamma_b=\kappa_*+2\sum_{\substack{q=p^k\\ \log q<2b}}\frac{\Lambda(q)}{\sqrt q},
\qquad
\kappa_*=\log(8\pi)+\gamma+\frac\pi2,                    \tag{4}
\]
and `X_b` is the positive continuous-plus-atomic common-jump feature map. Equality at a channel entrance is immaterial because the centered contribution is zero there.

For `s,t in S_(B,b)` define the actual shell block
\[
D_b(s,t)=Q_b(L_{B,b}s,L_{B,b}t).                           \tag{5}
\]
Then exactly
\[
\boxed{
P_b(s,t):=D_b(s,t)+\Gamma_b\langle Ls,Lt\rangle
=\langle\mathcal X_bLs,\mathcal X_bLt\rangle.
}                                                            \tag{6}
\]
In particular
\[
P_b[s]\ge0,\qquad D_b[s]\ge-\Gamma_b\|Ls\|_2^2.          \tag{7}
\]
This is a structural identity, not a shell-positivity theorem.

## 3. Continuity on the original `H^1` shell coordinates

For every fixed `b<=1`, the common-jump map is bounded from `H^1_0(-b,b)` to its feature Hilbert space. For the continuous channel, for `0<t<=1`,
\[
\|K_tu\|_2\le t\|u'\|_2,
\]
while `h(t)=O(1/t)` near zero; for `t>=1`,
\[
\|K_tu\|_2\le2\|u\|_2
\]
and `h(t)=O(e^{-t/2})`. The active prime-power set is finite. Hence
\[
\|\mathcal X_bu\|\le C_b\|u\|_{H^1(-b,b)}.                \tag{8}
\]
The previous coordinate theorem gives
\[
\|L_{B,b}s\|_{H^1(-b,b)}\le C_{L,b}\|s\|_{H^1(B,b)}.     \tag{9}
\]
Therefore `P_b`, `D_b`, and the cross form
\[
C_b(w,s)=Q_b(J_{B,b}w,L_{B,b}s)                            \tag{10}
\]
are continuous sesquilinear forms on the original `H^1` coordinate spaces. In particular all expressions in the later variational Schur criterion are well-defined on every actual source.

No claim is made that `D_b` controls the full `H^1` norm. The logarithmic/harmonic form is weaker than a derivative norm, so `H^1` coercivity would be an unjustified strengthening.

## 4. Canonical shell graph-energy space

Define on `S_(B,b)`
\[
\|s\|_{\mathfrak G_b}^2
:=\|L_{B,b}s\|_2^2+P_b[s]
=\|Ls\|_2^2+\|\mathcal X_bLs\|^2.                         \tag{11}
\]
Since `L_(B,b)` is injective, (11) is a norm. Let
\[
\mathfrak G_b=\overline{\mathcal S_{B,b}}^{\|\cdot\|_{\mathfrak G_b}}. \tag{12}
\]
The maps
\[
s\mapsto Ls,\qquad s\mapsto\mathcal X_bLs
\]
extend by continuity to bounded maps
\[
\bar L_b:\mathfrak G_b\to L^2(-b,b),\qquad
\bar X_b:\mathfrak G_b\to\mathscr H_b.                  \tag{13}
\]
Define on the whole Hilbert space `G_b`
\[
\overline D_b(x,y)
=\langle\bar X_bx,\bar X_by\rangle
-\Gamma_b\langle\bar L_bx,\bar L_by\rangle.              \tag{14}
\]
Then `overline D_b` is an everywhere-defined bounded Hermitian form on `G_b`, hence a closed semibounded form in this chosen shell-energy Hilbert space. Its positive shift is exactly
\[
\overline P_b(x,y)=\langle\bar X_bx,\bar X_by\rangle.      \tag{15}
\]
The construction does **not** assert that the graph completion is a new `H^1` source space or that the coordinate direct sum (1) extends as a direct sum after completion. It is only the canonical closed energy realization of the shell block. The all-source coordinate identity continues to be used on the actual `H^1` sources where it was proved.

## 5. Uniform crude semibound on the unit-window range

For `b<=1`, only the prime powers
\[
2,3,4,5,7
\]
can be active; `8` enters only when `b>\log8/2>1`. Using the exact weights `Lambda(p^k)/sqrt(p^k)` and elementary outward bounds gives
\[
\Gamma_b<12\qquad(B<b\le1).                               \tag{16}
\]
Consequently
\[
\boxed{
D_b[s]\ge-12\|L_{B,b}s\|_2^2
\qquad(B<b\le1).
}                                                            \tag{17}
\]
This is only a domain/semiboundedness firewall. The next gate must improve (17) to a strictly positive shell reserve.

## 6. The actual positivity gate as a shell frame bound

By (6), a physical `L^2` shell gap
\[
D_b[s]\ge\delta_{\rm sh}(b)\|Ls\|_2^2,\qquad \delta_{\rm sh}(b)>0, \tag{18}
\]
is equivalent to the restricted common-jump frame bound
\[
\boxed{
\|\mathcal X_bLs\|^2
\ge\bigl(\Gamma_b+\delta_{\rm sh}(b)\bigr)\|Ls\|_2^2.
}                                                            \tag{19}
\]
Thus the shell-positivity problem is itself a sharply stated positive-frame problem on the **lifted shell subspace**, not a question of closing the form domain.

## 7. Inverse-free relative form-Schur theorem

The full pullback form on the exact source coordinates is
\[
\mathfrak F_b((w,s))
=A_B[w]+2\operatorname{Re}C_b(w,s)+D_b[s],                 \tag{20}
\]
where
\[
A_B[w]=Q_B[w]\ge c_B\|w\|_2^2,\qquad c_B=10^{-13}         \tag{21}
\]
is available from the merged milestone (strictly, the certified bound is larger; `10^-13` is the frozen common constant).

### Theorem 7.1 — inverse-free Schur criterion

Assume for one `b>B` that
\[
D_b[s]\ge\delta_b\|Ls\|_2^2\quad(s\in\mathcal S_{B,b}),\qquad \delta_b>0, \tag{22}
\]
and there is `0<=theta_b<1` such that
\[
\boxed{
|C_b(w,s)|^2\le\theta_b\,A_B[w]D_b[s]
\quad\text{for all }w,s.
}                                                            \tag{23}
\]
Then every `u=Jw+Ls in W_b^e` satisfies
\[
Q_b[u]
\ge(1-\sqrt{\theta_b})\bigl(A_B[w]+D_b[s]\bigr)           \tag{24}
\]
and therefore
\[
\boxed{
Q_b[u]\ge
\frac{1-\sqrt{\theta_b}}{2}
\min\{c_B,\delta_b\}\,\|u\|_2^2.
}                                                            \tag{25}
\]

### Proof

From (23),
\[
2|C_b(w,s)|\le2\sqrt{\theta_b}\sqrt{A_B[w]D_b[s]}.
\]
Hence
\[
\begin{aligned}
\mathfrak F_b
&\ge A_B+D_b-2\sqrt{\theta_b}\sqrt{A_BD_b}\\
&\ge(1-\sqrt{\theta_b})(A_B+D_b),
\end{aligned}
\]
because `2 sqrt(A_B D_b)<=A_B+D_b`. This proves (24). By (21)-(22),
\[
A_B+D_b\ge\min(c_B,\delta_b)(\|Jw\|_2^2+\|Ls\|_2^2).
\]
Finally
\[
\|Jw+Ls\|_2^2\le2(\|Jw\|_2^2+\|Ls\|_2^2),
\]
which gives (25). `square`

This criterion is equivalent in spirit to
\[
C_b^*D_b^{-1}C_b\preceq\theta_bA_B
\]
when an operator inverse is legitimately available, but **no inverse and no additional domain theorem is needed for (23)-(25)**. This is the preferred formulation for the next gate.

## 8. Consequences for the research order

The domain question and the positivity question are now separated:

1. **closed shell energy realization:** completed by (11)-(15);
2. **strict shell frame bound:** prove (18)/(19) on a right interval;
3. **relative core-shell coupling:** prove (23) with `theta<1` on the entire old core, not only on the near-null vector;
4. **local all-source continuation:** follows from Theorem 7.1, with explicit `L^2` gap (25).

The near-null vector remains a high-priority diagnostic for (23), but its source-level upper Rayleigh quotient `~3.296e-12` is not a certified reserve available for all old-core directions. For a purely certificate-based all-source proof, the frozen lower bound `c_B=10^-13` is the safe common core constant unless a stronger directional/relative estimate is established.

## Scope firewall

No strict positivity of `D_b` is proved here. No right interval beyond `B`, no endpoint at `log(7)/2` or `1`, and no full C1-GEOM claim follows. A failed attempt at (18) or (23) is not a negative Weil source unless an explicit admissible source with nonpositive energy is constructed.
