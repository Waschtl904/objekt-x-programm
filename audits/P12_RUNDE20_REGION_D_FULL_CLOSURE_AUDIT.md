# P12 Runde 20 — Region D closure

**Status:** Region D `✓[M]_part` after independent raw-operator GREEN.  
**Independent review:** Perplexity independently reconstructed all 19 raw rows from the canonical operator, reproduced the optional tail column, checked the exact row multiplier and Cramer cross-check, audited the Round-16 scope and Round-14 rebase, ran an independent 200000-point Region-D stress test, and returned GREEN for Region D. It also returned GREEN for the four-way full-\(\rho\) reassembly, but that global theorem is deliberately reserved for a separate end-reassembly audit.  
**Repo basis:** `Waschtl904/objekt-x-programm`, parent `main@804694ffeec522c36c662cd4330f193ff525a677` (Round 19).  
**Firewall:** P11 FROZEN. R14 untouched. No Polar Gauge, Strong/Terminal Transport, Object X, or RH consequence.

---

## 1. Region D and target

Write
\[
\sigma=S-T,\qquad \varepsilon=T_0-T,
\qquad 0<\sigma<\varepsilon<\varepsilon_{\max}.
\]
The remaining Round-19 wedge is
\[
\boxed{\rho\le R<e/2\le\sigma<\varepsilon<\varepsilon_{\max}.}
\tag{D}
\]
For \(h\in\ker L\), it is enough to prove
\[
h=0\quad\text{a.e. on }(R,e/2),
\tag{1.1}
\]
because then the actual support rebases to \((e/2,S)\), and committed Round 14 applies at the legal effective radius \(R_{\rm eff}=e/2\).

Fix \(R<x<e/2\) away from the measure-zero walls and put
\[
z:=e-x.
\]

---

## 2. Hard cell: \(z>\varepsilon\)

The exact constant identity
\[
\boxed{d-\varepsilon_{\max}-\frac e2=\frac14\log\frac{27}{25}>0}
\tag{2.1}
\]
gives, throughout Region D,
\[
d-\sigma>d-\varepsilon_{\max}>e/2>x.
\]
Also \(x<e/2\le\sigma\), and \(z>\varepsilon\) is equivalent to \(x<e-\varepsilon\). Hence
\[
\boxed{R<x<\min\{\sigma,d-\sigma,e-\varepsilon\}.}
\tag{2.2}
\]
This is exactly the committed Round-16 hard-horizon scope
\[
\rho\le R<e/2,\qquad R<x<\min\{\sigma,d-\sigma,e-\varepsilon\}.
\]
Round 16 has no premise \(\sigma<e/2\); its retained Case-C verifier even uses \(\sigma=0.088>e/2\). Therefore
\[
\boxed{h(x)=0}
\tag{2.3}
\]
in the entire hard cell.

---

## 3. Soft cell: \(z<\varepsilon\)

Use the 19 Round-18 sources, in this exact row order:
\[
\begin{aligned}
u_1&=-x+3e+2\delta,&u_2&=x+3e+2\delta,&u_3&=-x+2e+\delta,\\
u_4&=-x+4e+2\delta,&u_5&=x+4e+2\delta,&u_6&=x+3e+\delta,\\
u_7&=-x+e,&u_8&=-x+3e+\delta,&u_9&=x+e+\delta,\\
u_{10}&=x+3e+3\delta,&u_{11}&=x+2e+2\delta,&u_{12}&=-x+2e,\\
u_{13}&=-x+4e+\delta,&u_{14}&=x+\delta,&u_{15}&=-x+5e+2\delta,\\
u_{16}&=x+e+2\delta,&u_{17}&=x+2e+3\delta,&u_{18}&=-x+4e,\\
u_{19}&=-x+5e+\delta.
\end{aligned}
\tag{3.1}
\]
All rows are reconstructed from the canonical raw operator
\[
Lh(u)=p[h(u-a)-h(u+a)]+r[h(u-b)-h(u+b)]+q[h(u-T)-h(u+T)],
\tag{3.2}
\]
with odd reflection and support cutoff only.

When \(\sigma\le z<\varepsilon\), the reconstructed visibility system is
\[
M_{19}v=0
\]
with
\[
\boxed{
\det M_{19}=-p^6r(p-q)^2(p+q)^2(\Delta-pr)(\Delta+pr)F\ne0.
}
\tag{3.3}
\]

When \(z<\sigma\), exactly one additional coordinate becomes live,
\[
J:=H(z)=h(T+z),
\]
and no other visibility changes. The system is
\[
\boxed{M_{19}v+cJ=0,}
\tag{3.4}
\]
where
\[
\boxed{c=(0,0,0,0,0,0,-q,-p,0,0,0,-r,0,0,0,0,0,0,0)^T.}
\tag{3.5}
\]

Put
\[
\Delta=p^2-q^2,\qquad \Psi=\Delta^2-p^2r^2,
\]
\[
F=2p^4-3p^2q^2-p^2r^2+q^4-q^2r^2.
\]
Round 16 gives \(\Psi<0\), \(F<0\); also \(\Delta>0\), \(r>0\).

Define the row multipliers
\[
\begin{aligned}
\lambda_1&=q^2r/F,&\lambda_2&=\Psi/(rF),&\lambda_3&=-p\Delta/F,\\
\lambda_4&=-q\Delta/F,&\lambda_5&=-q\Delta/F,&\lambda_6&=pqr/F,\\
\lambda_7&=p^2\Delta/(rF),&\lambda_8&=-pq(\Delta+r^2)/(rF),&\lambda_9&=-pq\Delta/(rF),\\
\lambda_{10}&=pqr/F,&\lambda_{11}&=-q(2p^2-q^2)/F,&\lambda_{12}&=p^2q/F,\\
\lambda_{13}&=-2p(p^2-r^2)/F,&\lambda_{14}&=-p^3/F,&\lambda_{15}&=\Psi/(rF),\\
\lambda_{16}&=p^2r/F,&\lambda_{17}&=-pq^2r^2/(\Delta F),&\lambda_{18}&=-p^2qr^2/(\Delta F),\\
\lambda_{19}&=pqr/F.
\end{aligned}
\tag{3.6}
\]
Exact symbolic multiplication of the independently reconstructed raw matrix gives
\[
\boxed{\lambda^TM_{19}=e_X^T,\qquad \lambda^Tc=0,}
\tag{3.7}
\]
where \(X=h(x)\). Therefore (3.4) implies
\[
\boxed{h(x)=0}
\tag{3.8}
\]
regardless of whether the optional tail coordinate \(J\) is live or dead.

Independent cross-check:
\[
\boxed{\det M_{19}^{(X\leftarrow c)}=0.}
\tag{3.9}
\]

---

## 4. Rebase and Region-D theorem

The hard and soft cells prove
\[
\boxed{h=0\quad\text{a.e. on }(R,e/2).}
\tag{4.1}
\]
Hence the same kernel vector is actually supported in \((e/2,S)\) up to a null set. This is a legal rebase to
\[
R_{\rm eff}=e/2.
\]
Committed Round 14 includes equality \(R=e/2\) and proves the whole mixed strip for \(e/2\le R<T\). Therefore Round 14 gives \(h=0\).

Thus
\[
\boxed{
\rho\le R<e/2\le\sigma<\varepsilon<\varepsilon_{\max}
\Longrightarrow
\ker L_{R,T+\sigma,T+\varepsilon}^{\{a,b,T\}}=\{0\}.
}
\tag{4.2}
\]

**Status:** `✓[M]_part` after independent raw-operator GREEN.

---

## 5. Verification record

The retained verifier reconstructs every row from (3.2) and reports:

```text
HARD_GEOMETRY_GAP = PASS
SOFT_DET19 = PASS
OPTIONAL_TAIL_COLUMN = PASS
CRAMER_X_REPLACEMENT = PASS 0
ROW_MULTIPLIER_CERTIFICATE = PASS
NONDEGENERACY_SANITY = PASS
REGION_D_LOW_STRIP_STRESS = PASS 500000
DIRECTED_HORIZON_WALL = PASS
DIRECTED_TAIL_WALL = PASS
GLOBAL_FOUR_WAY_PARTITION = PASS 300000
ROUND20_REGION_D_FULL_CLOSURE_VERIFY = PASS
```

The independent reviewer additionally ran its own 200000-point Region-D stress test with no failure.

---

## 6. Booking and firewall

Region D is now
\[
\boxed{\checkmark[M]_{\rm part}.}
\]
The reviewer also returned GREEN for the resulting four-way full-\(\rho\) reassembly, but this audit deliberately does **not** promote that global theorem. A separate final end-reassembly audit must restate and compose the exact Round-14, Round-19, Round-18/17/b1, and Round-20 scopes before the global statement is booked as `✓[M]`.

P11 remains FROZEN. R14 is unchanged. No claim is made about Polar Gauge, Strong/Terminal Transport, Object X, or RH.
