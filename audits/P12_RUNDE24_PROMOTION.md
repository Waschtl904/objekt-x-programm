# P12 Runde 24 — Promotion nach unabhängiger GREEN-Prüfung

**Status:** R24-A `✓[M]_part`; R24-B `✓[M]_part`.  
**Review basis:** Round-24 candidate chain ending at `main@a682d054f36bdddcba55b5e951f23c942676e87b`.  
**Firewall:** P11 FROZEN; R14 unchanged; no Polar Gauge, Terminal Transport, Objekt X or RH claim.

## 1. Independent verdict

Perplexity independently reconstructed the Round-24 algebra from the committed Round-23 raw-row generator and returned:

- `R24-A: GREEN`
- `R24-B: GREEN`

The reviewer independently reproduced the exact 42x42 algebra at a point with `R<omega`, the two new support-shell rows, the exact 44x44 determinant factorization, the beta-parity relation of the degree-9 factors, and strict positivity of both normalized factors using exact rational interval arithmetic.

The reviewer did **not** independently rerun the 30000/25000 random whole-chamber stress loops and did **not** independently rerun the complete 142-candidate horizon-wall enumeration. Accordingly, the horizon one-step diagnostic is not promoted here to a theorem or no-go statement.

---

## 2. R24-A — enlarged fixed-42 chamber

Define

\[
\eta=e-2\delta,\qquad \chi=3\delta-e,\qquad \kappa=e-\delta,
\]
with
\[
\eta+\chi=\delta.
\]

For
\[
0<R<\rho
\]
assume
\[
R<x<\delta-R,
\]
\[
\chi-R<x<\eta+R,
\]
\[
\max\{x,\delta-x\}<\sigma<\min\{\kappa-x,x+\eta\},
\]
\[
\max\{\kappa-x,x+\eta\}<\varepsilon<\varepsilon_{\max}.
\]

Then the same 42 Round-23 sources reconstruct the same exact 42x42 raw matrix `M42`; hence every live coordinate vanishes and in particular
\[
\boxed{h(x)=0.}
\]

This chamber contains points with `R<omega`, e.g.
\[
(R,x,\sigma,\varepsilon)=(0.01,\delta/2,0.04,0.07).
\]
Thus `R=omega` is not a wall of this fixed 42-row raw block.

**Booking:**
\[
\boxed{\text{R24-A C42 scope extension }\;✓[M]_{\rm part}.}
\]

No global lower-radius threshold is inferred.

---

## 3. R24-B — next support shell / 44x44 chamber

Define the support-entry modes
\[
U_-=T+\kappa-x,\qquad U_+=T+x+\eta,
\]
and add the paired next-shell sources
\[
V_-=T+2\delta-x\leftrightarrow(-1,4,4),
\]
\[
V_+=T+x+\delta\leftrightarrow(1,4,3).
\]

In the local chamber
\[
R<x<\delta-R,\qquad \chi-R<x<\eta+R,
\]
\[
\max\{\kappa-x,x+\eta\}<\sigma<\min\{2\delta-x,x+\delta\},
\]
\[
\max\{2\delta-x,x+\delta\}<\varepsilon<\varepsilon_{\max},
\]
the new raw rows are exactly
\[
V_-:\ \{(-1,2,3):p,\ (-1,1,2):r,\ (-1,0,2):q\},
\]
\[
V_+:\ \{(1,2,2):p,\ (1,1,1):r,\ (1,0,1):q\},
\]
with no additional visibility variables.

The resulting raw matrix has size 44x44 and preserves the two-sheet involution
\[
J(s,m,n)=(-s,m,n+s).
\]
In paired order
\[
M_{44}=\begin{pmatrix}A_{22}&B_{22}\\B_{22}&A_{22}\end{pmatrix}.
\]
Exact symbolic elimination gives
\[
\boxed{\det M_{44}=-p^{18}r^6(p-q)(p+q)G_-G_+.}
\]
With
\[
\beta=q/p,\qquad v=(r/p)^2,
\]
the normalized degree-9 factors form a parity pair under `beta -> -beta`. For the actual P12 weights, independent exact interval arithmetic gives strict positivity near
\[
0.03770850382320942
\]
and
\[
0.6120433841588828.
\]
Since `p>q>0` and `r>0`,
\[
\det M_{44}\ne0.
\]
Hence all 44 live coordinates vanish in this local chamber.

**Booking:**
\[
\boxed{\text{R24-B C44 support-shell theorem }\;✓[M]_{\rm part}.}
\]

---

## 4. Horizon walls remain open

At
\[
\varepsilon+x=\kappa
\]
and
\[
\varepsilon=x+\eta
\]
one of the paired source rows leaves the horizon, producing a 41-row/42-variable system for the old block.

The retained verifier contains a finite 142-candidate one-step replacement search, but this part was not independently rerun in the GREEN review. Therefore it remains a research diagnostic only:

\[
\boxed{\text{Horizon-wall closure: }?[O].}
\]

No no-go theorem is booked.
