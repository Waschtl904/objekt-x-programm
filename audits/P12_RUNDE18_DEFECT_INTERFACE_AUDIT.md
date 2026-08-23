# P12 Runde 18 — Low-radius defect interface closure

**Status:** `✓[M]_part` — interface independently GREEN-reviewed; full \(\rho\)-descent remains `?[O]`.  
**Repo basis:** `Waschtl904/objekt-x-programm`, current `main` after Runde 17.  
**Scope:** P12 / audits / consolidation only. P11 FROZEN. R14 firewall unchanged.

## 0. Goal

Runde 17 proved, independently GREEN-reviewed, the conditional full-tail lemma

\[
h=0\ {\rm a.e.}\ {\rm on}\ (0,\sigma)
\quad\Longrightarrow\quad
H(t)=l(t)=0\ {\rm a.e.}\ (0<t<\sigma)
\]

for

\[
\rho\le R<\sigma<e/2,\qquad \sigma<\varepsilon<\varepsilon_{\max}.
\]

The missing global interface is therefore exactly:

> prove \(h=0\) a.e. on \((R,\sigma)\) throughout the low-radius overlap chamber.

This package closes that interface by splitting at the single horizon wall
\[
e-x=\varepsilon.
\]

No full-\(\rho\)-descent theorem is promoted in this package. Perplexity independently reconstructed the interface from the raw operator on 2026-08-23 and returned GREEN; the final global reassembly remains a separate audit target.

---

## 1. Geometry: only one residual wall exists

Assume

\[
\rho\le R<\sigma<e/2,\qquad
\sigma<\varepsilon<\varepsilon_{\max},
\qquad
R<x<\sigma.
\]

Because \(e/2<d/2\),

\[
x<\sigma<e/2<d/2
\]

implies

\[
\boxed{x<d-\sigma.}
\]

Hence the `d-sigma` wall from the general hard-horizon statement is automatically inactive in the entire Runde-17 overlap regime.

Therefore the whole interval \(R<x<\sigma\) splits, up to the equality wall \(x=e-\varepsilon\), into only:

### H — hard-horizon cell
\[
x<e-\varepsilon
\quad\Longleftrightarrow\quad
e-x>\varepsilon.
\]

Then Runde 16 applies directly, because

\[
R<x<\min\{\sigma,d-\sigma,e-\varepsilon\}.
\]

Thus

\[
\boxed{h(x)=0.}
\]

### S — soft-horizon cell
\[
x>e-\varepsilon
\quad\Longleftrightarrow\quad
e-x<\varepsilon.
\]

Here the formerly illegal source
\[
u_{15}=T+e-x
\]
becomes horizon-legal:
\[
u_{15}<T+\varepsilon=T_0.
\]

The rest of this audit proves that this single source kills the unique 18-source Runde-15H mode.

The equality wall has measure zero in \(x\), so this two-cell split is sufficient for the \(L^2\)/a.e. theorem.

---

## 2. The 18-source core persists throughout the whole overlap chamber

Use the committed Runde-15H source family, excluding \(u_{15}\):

\[
\begin{aligned}
u_1&=b-x,&u_2&=b+x,&u_3&=a-x,&u_4&=T-x,\\
u_5&=T+x,&u_6&=a+e+x,&u_7&=e-x,&u_8&=a+e-x,\\
u_9&=d+x,&u_{10}&=3d+x,&u_{11}&=2d+x,&u_{12}&=2e-x,\\
u_{13}&=T-\delta-x,&u_{14}&=\delta+x,&
u_{16}&=d+\delta+x,&u_{17}&=a+2\delta+x,\\
u_{18}&=4e-x,&u_{19}&=a+3e-x.
\end{aligned}
\]

The key observation is that the *support-visibility pattern of these 18 sources does not use* \(e-x>\varepsilon\). That inequality was needed only to exclude \(u_{15}\) from the source horizon.

Under the weaker assumptions of §1, every one of these 18 sources is horizon-legal and their reduced raw rows are exactly the committed Runde-15H rows.

### 2.1 Three lower-support kills

All omitted lower slots reduce to one of the following three forms.

#### L1: \( |x-\delta|<R \)

If \(x\ge\delta\), then
\[
x-\delta<\sigma-\delta<e/2-\delta<\rho\le R,
\]
where \(e/2<\varepsilon_{\max}=\rho+\delta\).

If \(x<\delta\), then
\[
\delta-x<\delta-R\le\delta-\rho<\rho\le R,
\]
using
\[
\delta<\kappa<2\rho.
\]

Hence
\[
\boxed{|x-\delta|<R.}
\]

#### L2: \(0<\kappa-x<R\)

Since \(\delta<e/2\),
\[
\kappa=e-\delta>e/2>x.
\]
Also Runde 15H established \(\kappa<2\rho\). Therefore
\[
0<\kappa-x<\kappa-R<2\rho-R\le\rho\le R.
\]

Thus
\[
\boxed{0<\kappa-x<R.}
\]

#### L3: \(0<x-\eta<R\)

Because
\[
\eta<\rho\le R<x,
\]
we have \(x-\eta>0\). Also
\[
x-\eta<\sigma-\eta<e/2-\eta<\rho\le R.
\]

The last strict inequality is equivalent to
\[
(9/8)^6<25/12,
\]
i.e.
\[
6\,377\,292<6\,553\,600.
\]

Hence
\[
\boxed{0<x-\eta<R.}
\]

These are exactly the lower-support deletions needed by the 18 raw rows.

### 2.2 Upper-support deletions

Every omitted upper slot dominates one of the three seed quantities

\[
T+(e-x),\qquad
T+(d-x),\qquad
T+(x+\delta).
\]

Each is strictly above \(T+\sigma=S\):

1. \(e-x>e-\sigma>\sigma\) because \(\sigma<e/2\).

2. \(d-x>d-\sigma>\sigma\) because \(\sigma<d/2\).

3. \(x+\delta>\sigma\), because \(\sigma-x<\sigma-R<e/2-\rho<\delta\).

Therefore every omitted upper slot is outside support.

### 2.3 The 19 live coordinates

The stable live visibility set is exactly

\[
\begin{aligned}
(&h(2\delta+x),h(d+\delta+x),h(\delta+x),h(3d+x),h(2d+x),h(d-x),h(d+x),h(x),\\
&h(b+x),h(a-x),h(a+x),h(e+x),h(T-x),h(a+e-x),h(2e-x),h(T-\delta-x),\\
&h(3e-x),h(a-2\delta-x),h(e-x)).
\end{aligned}
\]

Thus the same exact \(18\times 19\) matrix \(M_{18}\) from Runde 15H applies throughout the entire low-radius overlap chamber.

Its rank is 18, because the committed minor is

\[
\det M_{\widehat Z}
=
-p^6qr(p-q)^3(p+q)^3(\Delta-pr)(\Delta+pr)\ne0.
\]

Hence the local visibility kernel is exactly one-dimensional.

---

## 3. Coordinates of the unique 18-source mode

Put
\[
X:=h(x),\qquad Z:=h(e-x),\qquad \Delta:=p^2-q^2,\qquad \Psi:=\Delta^2-p^2r^2.
\]

Runde 15H already gives
\[
Z=\gamma X,
\qquad
\gamma=-\frac{qr\Delta}{\Psi}.
\]

For the newly legal \(u_{15}\) row we also need
\[
N:=h(a+e-x),\qquad O:=h(2e-x).
\]

Exact elimination in the same \(18\times19\) system gives

\[
\boxed{N=\frac{pr(2p^2-2q^2-r^2)}{\Psi}\,X,}
\]
\[
\boxed{O=-\frac{q^2r^2}{\Psi}\,X,}
\]
\[
\boxed{Z=-\frac{qr\Delta}{\Psi}\,X.}
\]

These formulas are independently regenerated by the attached verifier from the 18 raw rows; they are not assumed.

---

## 4. The newly legal source \(u_{15}\)

In the soft-horizon cell \(e-x<\varepsilon\),
\[
u_{15}=T+e-x<T+\varepsilon=T_0,
\]
and \(u_{15}>0\).

Its six canonical raw slots reduce exactly to
\[
\boxed{p\,N+r\,O+q\,Z=0.}
\]

No new visibility coordinate is introduced.

Substituting the one-mode formulas from §3 gives
\[
pN+rO+qZ=\frac{rF}{\Psi}\,X,
\]
where
\[
F=2p^4-3p^2q^2-p^2r^2+q^4-q^2r^2.
\]

Runde 16 already established
\[
\Psi<0,\qquad F<0.
\]

Since \(r>0\),
\[
\boxed{\frac{rF}{\Psi}\ne0.}
\]

Therefore
\[
\boxed{X=h(x)=0.}
\]

Because the \(18\)-source kernel is one-dimensional, the entire 19-coordinate visibility vector then vanishes.

This is the desired soft-horizon local kill.

---

## 5. Equivalent 19×19 determinant cross-check

Appending the \(u_{15}\) row to \(M_{18}\) gives an exact square matrix \(M_{19}\). Direct symbolic computation gives

\[
\boxed{\det M_{19}=-p^6r(p-q)^2(p+q)^2(\Delta-pr)(\Delta+pr)\,F.}
\]

Every factor is nonzero:

- \(p,r>0\),
- \(p\ne q\),
- \((\Delta-pr)(\Delta+pr)=\Psi<0\),
- \(F<0\).

Hence \(\det M_{19}\ne0\).

This determinant is a cross-check only; the preferred proof is the one-dimensional mode closure in §4.

---

## 6. Interface theorem

Combining the two cells, Runde 16 gives \(h(x)=0\) for \(x<e-\varepsilon\), while §4 gives \(h(x)=0\) for \(x>e-\varepsilon\). Therefore, for every candidate kernel vector in

\[
\rho\le R<\sigma<e/2,\qquad \sigma<\varepsilon<\varepsilon_{\max},
\]

\[
\boxed{h(x)=0\quad\text{for a.e. }x\in(R,\sigma).}
\]

Since \(h=0\) by support on \((0,R)\),

\[
\boxed{h=0\quad\text{a.e. on }(0,\sigma).}
\]

This is exactly the premise required by Runde 17.

**Promoted status after independent raw reconstruction:**
\[
\boxed{\checkmark[M]_{\rm part}.}
\]

---

## 7. Consequence after Runde-18 GREEN

The independent GREEN now establishes the interface premise, so:

1. Runde 18 gives \(h=0\) on \((0,\sigma)\) for \(R<\sigma<e/2\).
2. Runde 17 then gives \(H=0\) on \((0,\sigma)\), so the full tail \((T,S)\) vanishes.
3. The remaining support lies in \((\sigma,T)\); b1 applies with effective lower radius \(R_{\rm eff}=\sigma\).
4. The complementary low-radius cases \(\sigma\le R\) and \(\sigma\ge e/2\) must still be included explicitly in the final consolidation audit, using the already committed b1/b2b mechanisms.
5. Round 14 supplies all \(R\ge e/2\).

Only after a separate independent audit of that final reassembly may the global theorem

\[
\rho\le R<T,\qquad T<S<T_0<c
\Longrightarrow
\ker L_{R,S,T_0}^{\{a,b,2a\}}=\{0\}
\]

be promoted.

Until then:
\[
\boxed{\text{full }\rho\text{-descent remains }?[O].}
\]

---

## 8. Independent review record

Perplexity independently reconstructed the canonical raw operator rather than inheriting the reduced equations and reported GREEN for the interface. The following checklist was passed:

1. Verify that \(x<d-\sigma\) is automatic from \(\sigma<e/2\).
2. Verify the 18 Runde-15H sources remain horizon-legal without assuming \(e-x>\varepsilon\).
3. Reconstruct all 18 raw rows in the whole overlap chamber.
4. Verify the three lower-support kills L1–L3.
5. Verify all omitted upper slots are above \(S=T+\sigma\).
6. Verify exact rank \(18\) / the committed minor.
7. Independently solve the unique mode for \(N,O,Z\).
8. Verify \(u_{15}=T+e-x\) is horizon-legal precisely in the soft cell.
9. Reconstruct the raw \(u_{15}\) row \(pN+rO+qZ=0\).
10. Verify \(pN+rO+qZ=(rF/\Psi)X\).
11. Verify \(F\ne0\), \(\Psi\ne0\) from already committed Round-16 facts without circularity.
12. Cross-check \(\det M_{19}=-p^6r(p-q)^2(p+q)^2(\Delta-pr)(\Delta+pr)F\).
13. Stress the entire parameter chamber, including points arbitrarily close to \(x=e-\varepsilon\), \(R=\rho\), and \(\sigma=e/2\).
14. Do not promote full \(\rho\)-descent merely from this package; report separately on the final reassembly.

Independent stress reproduction matched the committed verifier exactly:

```text
WHOLE_OVERLAP_STRESS = PASS 150000
hard = 38081
soft = 111919
soft_nearwall = 31
SOFT19_NEAR_HORIZON_WALL = PASS 9999
```

Final Round-18 verdict:

- Low-radius defect interface closure: `GREEN / ✓[M]_part`.
- Round-16 inputs `F<0`, `Psi<0`: legitimate and non-circular.
- Hard/soft split at `x=e-epsilon`: confirmed.
- `u15` as the 1D-mode killer: confirmed.
- Full rho-descent: still `?[O]` pending a separate final reassembly audit.

P11/R14 must remain untouched. No Polar Gauge, Strong/Terminal Transport, Object X, or RH implication is asserted.
