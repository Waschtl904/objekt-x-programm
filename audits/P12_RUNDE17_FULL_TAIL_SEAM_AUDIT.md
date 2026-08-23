# P12 Runde 17 — full-tail seam kill below e/2

**Repo basis:** `Waschtl904/objekt-x-programm`, `main`, HEAD `865283deefb40711ace37eeeea694b2c86be2bfa`.  
**Scope:** P12 only. P11 FROZEN. R14 firewall untouched.  
**Status:** ✓[M]_part. Local full-tail lemma independently reconstructed GREEN by Perplexity; full rho-descent remains ?[O].

## 0. Executive status

This round starts from the post-defect null interval
\[
h=0\quad\text{a.e. on }(0,\sigma)
\]
in the remaining low-radius overlap regime
\[
\rho\le R<\sigma<e/2,\qquad \sigma<\varepsilon<\varepsilon_{\max}.
\]

A new horizon-legal transfer structure proves the stronger statement
\[
\boxed{H(t)=h(T+t)=0\quad\text{for a.e. }0<t<\sigma.}
\]
Thus the entire tail `(T,S)` dies, not merely the old small tail `0<t<R`.
The proof uses one 3x3 transfer and one 7x7 transfer (plus its reflection), with determinants
\[
\det M_3=\Psi,
\qquad
\det M_7=-(\Psi-qr\Delta)(\Psi+qr\Delta)
          =-\Psi^2(1-\gamma^2),
\]
nonzero from Runde 16 (`\Psi<0`, `0<\gamma<1`).

This is a local mathematical seam result. Perplexity independently reconstructed the raw rows, chamber partition, determinants, hidden C4 slot and whole-chamber stress and returned GREEN for the local lemma. The **full rho-descent remains formally unpromoted** because the separate interface from the local defect kills to `h=0` on all `(R,\sigma)` has not yet been independently established in every low-radius overlap cell.

---

## 1. Correction to the handoff constants

The handoff listed
\[
\delta<\rho<e/2.
\]
That order is false.

Indeed
\[
\rho=\varepsilon_{\max}-\delta,
\]
and the already established comparison
\[
\varepsilon_{\max}<2\delta\iff 80<81
\]
implies
\[
\boxed{\rho<\delta<e/2.}
\]
Numerically
\[
\rho\approx0.05268025783,
\qquad
\delta\approx0.05889151783.
\]

Status of the handoff statement `delta < rho`: **×[M]**.

Two further inequalities used below are
\[
\eta<\rho
\]
(which is `256/243 < 10/9`, i.e. `2304<2430`) and the Runde-15H bound
\[
\kappa<2\rho
\]
(equivalent there to `24<25`).

---

## 2. Raw audit of the two proposed small-tail equations

Assume the post-defect null interval `h=0` on `(0,\sigma)` and fix
\[
0<t<\sigma<e/2.
\]
Since
\[
d-t>d-\sigma>d-e/2=e/2+\delta>\sigma,
\]
the tail value `H(d-t)=0`.

### 2.1 B-minus source — correct

At `u=b-t`, the canonical raw row is
\[
p h(d-t)-pH(d-t)-r h(t)-q h(e+t)=0.
\]
Using `H(d-t)=0` and `h(t)=0`,
\[
\boxed{p h(d-t)-q h(e+t)=0.}
\]
Status: **✓[M]**.

### 2.2 Source `u=a+e+t` — the globally stated two-term row is false

The exact raw row is
\[
\boxed{
p h(e+t)
+r\,\operatorname{sgn}(t-\delta)h(|t-\delta|)
-q h(d-t)=0.
}
\]
The middle `r`-slot is zero except in the narrow chamber
\[
\sigma<\delta-t
\quad\Longleftrightarrow\quad
\sigma<\delta,
\quad 0<t<\delta-\sigma.
\]
There it is live and the row is
\[
p h(e+t)-r h(\delta-t)-q h(d-t)=0.
\]
Hence the globally asserted equation
\[
p h(e+t)-q h(d-t)=0
\]
is **×[M] as a global statement**. It is valid only outside this corner.

This hidden wall is precisely why the corrected order `rho<delta` matters.

---

## 3. Six-source reduction to two tail-visible coordinates

Set
\[
E_-:=h(e-t),\qquad E_+:=h(e+t).
\]
Use the six horizon-legal sources
\[
a-t,\ a+t,\ b-t,\ b+t,\ T-t,\ T+t.
\]
Because `h(t)=H(d-t)=0`, their raw equations give exactly
\[
\begin{aligned}
h(d-t)&=\frac q p E_+,\\
h(d+t)&=\frac q p E_-,\\
h(a-t)&=-\frac r p E_-,\\
h(a+t)&=-\frac r p E_+,\\
H(t)&=\frac{qr}{p^2}(E_--E_+),\\
l(t)&=-H(t).
\end{aligned}
\tag{3.1}
\]
Therefore it suffices to prove
\[
\boxed{E_-=E_+=0.}
\]
Once these vanish, all five originally listed small-tail visibility values
`h(e-t), h(d+t), h(a-t), H(t), l(t)` vanish, and so do their reflected companions.

---

## 4. Two short transfer equations

Define
\[
W_+:=h(\delta+t),\qquad W_-:=h(\delta-t),
\]
with the convention that a value in `(0,\sigma)` is already zero.

The symmetric sources
\[
C_-:u=a+e-t,
\qquad
C_+:u=a+e+t
\]
combined with the B-rows in §3 give
\[
\boxed{\Delta E_- - pr W_+=0,}
\qquad
\boxed{\Delta E_+ - pr W_-=0.}
\tag{4.1}
\]
These formulas include the support-zero cases `W_\pm=0`.

---

## 5. Complete visibility partition

Away from the finitely many equality walls (irrelevant a.e. in `t`), exactly four chambers occur.
Let
\[
K_-:=h(\kappa-t).
\]

### C3 — both delta-values dead on the needed side
\[
\delta+t<\sigma.
\]
Then `W_+=W_-=0`; (4.1) immediately gives
\[
E_-=E_+=0.
\]

### C1 — `W_+` live, `W_-` dead, `K_-` dead
\[
\delta-t<\sigma<\delta+t,
\qquad
\kappa-t<\sigma.
\]
Then `E_+=0` from (4.1), while `E_-` is closed by the 3x3 system in §6.

### C2 — `W_+` and `K_-` live, `W_-` dead
\[
\delta-t<\sigma<\delta+t,
\qquad
\sigma<\kappa-t.
\]
Then `E_+=0`; the 7x7 minus-chain in §7 kills `E_-`.

### C4 — narrow reflected corner
\[
\boxed{\sigma<\delta-t.}
\]
Both `W_-` and `W_+` are live. The minus 7x7 chain kills `E_-`; its reflected plus-chain kills `E_+`.

The four cases exhaust `0<t<\sigma`.

---

## 6. C1: 3x3 Wickie transfer

Use variables
\[
E=h(e-t),\quad W=h(\delta+t),\quad V=h(2e-t).
\]
The exact raw rows are
\[
\begin{aligned}
\Delta E-prW&=0,\\
-rE+pW-qV&=0 && [u=2d+t],\\
-qW+pV&=0 && [u=T-\delta-t],
\end{aligned}
\]
where the `rK_-` slot in the final row is support-zero by C1.

Thus
\[
M_3=
\begin{pmatrix}
\Delta&-pr&0\\
-r&p&-q\\
0&-q&p
\end{pmatrix},
\]
and
\[
\boxed{\det M_3
=(\Delta-pr)(\Delta+pr)
=\Psi\ne0.}
\]
Hence `E_-=0`, and already `E_+=0`.

---

## 7. C2/C4: 7x7 transfer and reflection

### 7.1 Minus chain

Use
\[
\begin{aligned}
E&=h(e-t),& W&=h(\delta+t),& V&=h(2e-t),\\
K&=h(\kappa-t),& J&=h(e+2\delta+t),\\
U&=h(2\delta+t),& M&=h(2e-\delta-t).
\end{aligned}
\]
The six additional horizon-legal sources are
\[
2d+t,
\quad T-\delta-t,
\quad 3d+t,
\quad 3e-t,
\quad 2e+3\delta+t,
\quad 4e-t.
\]
Together with (4.1), the exact system is
\[
\begin{aligned}
\Delta E-prW&=0,\\
-rE+pW-qV&=0,\\
-qW+pV+rK&=0,\\
rW-qK+pJ&=0,\\
pK-qJ-rU&=0,\\
-rK+pU-qM&=0,\\
-qU+pM&=0.
\end{aligned}
\tag{7.1}
\]
The last source has no hidden `r`-slot because it is proportional to
`h(|\eta-t|)` and
\[
|\eta-t|<\sigma
\]
for all `0<t<\sigma`, using `\eta<\rho<\sigma`.

In the variable order `(E,W,V,K,J,U,M)`,
\[
M_7=
\begin{pmatrix}
\Delta&-pr&0&0&0&0&0\\
-r&p&-q&0&0&0&0\\
0&-q&p&r&0&0&0\\
0&r&0&-q&p&0&0\\
0&0&0&p&-q&-r&0\\
0&0&0&-r&0&p&-q\\
0&0&0&0&0&-q&p
\end{pmatrix}.
\]
Exact symbolic elimination gives
\[
\boxed{
\det M_7
=-(\Psi-qr\Delta)(\Psi+qr\Delta)
=-\Psi^2(1-\gamma^2).
}
\]
Runde 16 proves `\Psi<0` and `0<\gamma<1`, hence
\[
\det M_7\ne0.
\]
Thus `E_-=0` in C2 and C4.

### 7.2 Reflected plus chain in C4

In C4 also use
\[
\begin{aligned}
E&=h(e+t),& W&=h(\delta-t),& V&=h(2e+t),\\
K&=h(\kappa+t),& J&=h(e+2\delta-t),\\
U&=h(2\delta-t),& M&=h(2e-\delta+t),
\end{aligned}
\]
with sources
\[
2d-t,
\quad T-\delta+t,
\quad 3d-t,
\quad 3e+t,
\quad 2e+3\delta-t,
\quad 4e+t.
\]
The coefficient matrix is exactly the same `M_7`.

The only delicate hidden slot in the final row is `h(\eta+t)`.  C4 gives
\[
t<\delta-\sigma,
\]
so
\[
\eta+t<\eta+\delta-\sigma=\kappa-\sigma.
\]
Since Runde 15H proved `\kappa<2\rho` and here `\sigma>\rho`,
\[
\kappa-\sigma<\sigma.
\]
Hence `h(\eta+t)=0`, and the reflected last row is genuinely two-term.
Therefore the same nonzero determinant gives `E_+=0`.

So every chamber yields
\[
\boxed{E_-=E_+=0.}
\]
By (3.1),
\[
\boxed{H(t)=l(t)=0\quad(0<t<\sigma)\ \text{a.e.}}
\]
and the entire tail vanishes.

**Local status:** `✓[M]_part` after independent GREEN review. The lemma itself is mathematically proved; `_part` records only that the global rho-descent target is still open.

---

## 8. Global rho-descent reassembly candidate

The following is a **promotion candidate**, not yet a promoted theorem.

### 8.1 Existing high-radius half

Round 14 already proves the mixed strip for every
\[
R\ge e/2.
\]

### 8.2 Low-radius, restricted-tail case `sigma <= R < e/2`

For `x\in(R,a)`, the tail term in the A-source/E-equation is absent because
`x>R\ge\sigma`. Thus the b1/A14.3a lower-half mechanism applies unchanged and gives
\[
h=0\quad\text{on }(R,a).
\]
For `0<t<\sigma\le R`, the three values in `D(t)` are zero by support or this lower-half kill, so P2 gives `H(t)=l(t)`. Also `d-t>\sigma` (indeed `\sigma<e/2<d/2`), hence P1 gives `H(t)+l(t)=0`. Thus the full tail vanishes. Then b1 closes the residual `(R,T)`.

So `sigma<=R` is not a remaining seam.

### 8.3 Low-radius overlap `R<sigma`

Use the already obtained post-defect interval
\[
h=0\quad\text{on }(0,\sigma).
\]

- If `sigma >= e/2`, rebase the effective lower support radius to
  `R_eff=sigma`.  The existing b2b restricted-tail theorem applies with
  tail width `sigma = R_eff`, hence kills `h`.

- If `sigma < e/2`, the new Runde-17 full-tail lemma kills
  `H` on `(0,\sigma)`. The remaining support lies in `(\sigma,T)`, so b1
  applies with effective radius `R_eff=sigma` and kills the residual.

Therefore, **conditional only on the already stated defect-to-null interface being globally valid**, all low-radius regimes `rho <= R < e/2` are closed. Combined with Round 14, this would give
\[
\boxed{
\rho\le R<T,\quad T<S<T_0<c
\ \Longrightarrow\
\ker L_{R,S,T_0}^{\{a,b,2a\}}=\{0\}.
}
\]

Formal programme status after independent local reconstruction:
\[
\boxed{\text{full rho-descent }?[O]\ \text{(promotion candidate)}}.
\]
Do **not** mark `✓[M]` or edit the P12 manuscript yet.

---

## 9. Verifier result

Self-contained verifier:
`round17_small_tail_full_tail_kill_verify.py`

It performs:

1. raw generation from all six canonical slots before comparison;
2. exact row matching in C1/C2/C3/C4;
3. exact symbolic `det M3 = Psi`;
4. exact symbolic `det M7 = -(Psi-qrDelta)(Psi+qrDelta)`;
5. explicit detection of the hidden `-r h(delta-t)` slot in C4;
6. 300,000 random whole-chamber pattern/horizon stresses.

Observed chamber counts:

- C1: 218299
- C2: 44629
- C3: 36429
- C4: 643

All passed.

---

## 10. Independent second review (Perplexity): GREEN locally, PARTIAL globally

Perplexity independently reconstructed the package from the six canonical raw slots and reported:

- correction `rho<delta<e/2`: confirmed;
- `B^-` row and the hidden C4 `-r h(delta-t)` slot: confirmed;
- all six base rows and the reduction to `E_-,E_+`: confirmed;
- C1--C4 partition: confirmed exhaustive a.e.;
- all minus-chain and reflected plus-chain raw rows: confirmed;
- `det M3=Psi`: confirmed exactly;
- `det M7=-(Psi-qrDelta)(Psi+qrDelta)=-Psi^2(1-gamma^2)`: confirmed exactly;
- Runde-16 nondegeneracy input `Psi<0`, `0<gamma<1`: confirmed non-circular;
- C4 hidden-slot arithmetic: confirmed;
- 300,000 whole-chamber stress points: reproduced exactly with
  `C1=218299`, `C2=44629`, `C3=36429`, `C4=643`, zero failures.

Verdict for the local statement:

after the hypothesis
\[
h=0\quad\text{a.e. on }(0,\sigma),
\]
in
\[
\rho\le R<\sigma<e/2,
\]
the raw operator forces
\[
\boxed{H(t)=l(t)=0\quad\text{for a.e. }0<t<\sigma.}
\]

Hence the local full-tail seam lemma is **GREEN / `✓[M]_part`**.

The global reassembly received only **PARTIAL** because the separate premise
\[
\text{complete low-radius defect kill}
\Longrightarrow
h=0\text{ on all }(R,\sigma)
\]
has not yet been independently proved across every low-radius overlap cell. Therefore
\[
\boxed{\text{full rho-descent }?[O]}
\]
remains unchanged. No P12 manuscript promotion is made in this round.

P11 remains FROZEN; the R14 firewall is untouched. No Polar Gauge, Strong/Terminal Transport, Object X, or RH implication is asserted.
