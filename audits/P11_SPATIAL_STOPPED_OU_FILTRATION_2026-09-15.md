# P11 Audit — Spatial masks as a stopped OU filtration

**Datum:** 15. September 2026  
**Branch:** `research/critical-half-green-tree-bridge-2026-09-13`  
**Rolle:** theorem-level Reinterpretation der bereits vorhandenen P11-Fenstermasken.  
**Registry:** unveraendert.  
**Nonclaim:** keine Weil-Identitaet, kein Object-X-/RH-Abschluss, keine Publikationsneuheit.

---

## 0. Kurzurteil

Die P11-Fenstermasken sind nicht bloss technische Cutoffs. Sie implementieren punktweise eine **gestoppte AR(1)/OU-Filtration**, deren sichtbare Tiefe exakt durch den Abstand zum Fensterrand bestimmt wird.

Fuer das Fenster `(-R,R)` und eine Primzahl `p` mit

```math
h_p=\log p,
\qquad
q_p=p^{-1/2},
```

ist der vorhandene P11-Sektor `a>=0` auf

```math
\boxed{
\Omega_{p,a,R}
=
\left\{x:\ |x|\le R-\frac{(a+1)h_p}{2}\right\}
}
```

getragen. Definiere die Randtiefe

```math
d_R(x)=R-|x|
```

und fuer fast jedes `x`

```math
\boxed{
m_p(x)=\left\lfloor\frac{2d_R(x)}{h_p}\right\rfloor.}
```

Dann sind am Punkt `x` genau die Innovationslagen

```text
a=0,...,m_p(x)-1
```

aktiv.

Addiert man den P11-Hub und diese aktiven Restlagen, so ist die lokale same-prime Kanalkovarianz

```math
\boxed{
C_{jk}^{(p,m)}
=(\log p)p^{-3(j+k)/4}p^{\min(j,k,m)}.
}
```

Nach Weil-Diagonalnormalisierung ergibt sich

```math
\boxed{
R_{q}^{(m)}(j,k)
=q^{j+k-2\min(j,k,m)}.
}
```

Dies ist exakt die Kovarianz eines stationaeren AR(1)-Prozesses, bei dem nur Root und Innovationen bis Tiefe `m` sichtbar sind. Fuer `j,k>m` sind die spaeteren Zustaende auf ihre bedingten Erwartungen aus Ebene `m` reduziert.

Die Radius-/Tiefenentwicklung ist positiv Rang eins:

```math
\boxed{
R_q^{(m+1)}-R_q^{(m)}
=d_{m+1}d_{m+1}^*\succeq0,
}
```

mit

```math
(d_{m+1})_j
=\sqrt{1-q^2}\,q^{j-m-1}\mathbf 1_{j\ge m+1}.
```

Damit besitzt P11 bereits intern eine radiuskonsistente positive Filtration: beim Wachsen der sichtbaren Randtiefe wird jeweils genau eine neue OU-Innovation freigegeben.

Status:

```text
mask = boundary-depth threshold                           ✓[M]
local capped AR(1) covariance                            ✓[M]
stopped-OU / conditional-expectation interpretation      ✓[M]
rank-one positive depth increments                       ✓[M]
P11 masks as discrete sections of common overlap cone    ✓[M]
P11 stopped filtration = Weil/Object X                   not claimed
```

---

# 1. Existing P11 mask and the boundary depth

The finite-window P11 rest sector is, in the existing implementation/convention,

```math
\Phi_{p,a,R}
=
P_{\Omega_{p,a,R}}
\sum_{k\ge a+1}p^{-3k/4}K_{p,k}P_R,
```

up to the already documented scalar sector factors, with

```math
K_{p,k}=K_{k\log p}.
```

For `R=1`, the committed checker implements

```text
omega = 1 - (a+1) log(p)/2,
```

and retains exactly positions with `|x|<=omega`. The general P11 mask is therefore

```math
\Omega_{p,a,R}
=
\left(-R+\frac{(a+1)h_p}{2},
       R-\frac{(a+1)h_p}{2}\right)
```

up to irrelevant endpoint conventions in `L^2`.

Equivalently,

```math
x\in\Omega_{p,a,R}
\iff
(a+1)\frac{h_p}{2}\le d_R(x).
```

Hence the number of active innovation layers at `x` is almost everywhere

```math
m_p(x)=\left\lfloor\frac{2d_R(x)}{h_p}\right\rfloor.
```

At the discrete equality surfaces the choice of closed/open endpoint does not affect the `L^2` form.

---

# 2. Local channel coefficient after summing active sectors

Fix one prime `p`, one spatial point `x`, and write

```math
m=m_p(x).
```

The P11 hub contributes the primitive channel coefficient

```math
(\log p)p^{-3(j+k)/4}.
```

A rest sector `a` contributes to the pair `(j,k)` precisely when

```text
a+1 <= j,
a+1 <= k,
a < m,
```

with multiplicity factor

```math
(p-1)p^a.
```

Therefore the total local coefficient is

```math
\begin{aligned}
C_{jk}^{(p,m)}
&=(\log p)p^{-3(j+k)/4}
\left[
1+
\sum_{a=0}^{\min(j,k,m)-1}(p-1)p^a
\right]\\
&=(\log p)p^{-3(j+k)/4}
 p^{\min(j,k,m)}.
\end{aligned}
```

This proves

```math
\boxed{
C_{jk}^{(p,m)}
=(\log p)p^{-3(j+k)/4}p^{\min(j,k,m)}.
}
```

When `m>=min(j,k)` one recovers the windowless P11 ledger exactly.

---

# 3. Weil-normalized stopped covariance

Recall

```math
w_{p,k}=(\log p)p^{-k/2}.
```

Thus

```math
\sqrt{w_{p,j}w_{p,k}}
=(\log p)p^{-(j+k)/4}.
```

Dividing the local coefficient by the Weil weights gives

```math
\begin{aligned}
R_q^{(m)}(j,k)
&=
\frac{C_{jk}^{(p,m)}}{\sqrt{w_{p,j}w_{p,k}}}\\
&=
p^{\min(j,k,m)-(j+k)/2}\\
&=q^{j+k-2\min(j,k,m)}.
\end{aligned}
```

Hence

```math
\boxed{
R_q^{(m)}(j,k)
=q^{j+k-2\min(j,k,m)}.
}
```

For `min(j,k)<=m` this is `q^{|j-k|}`. If both indices lie beyond the stopping depth,

```math
R_q^{(m)}(j,k)
=q^{j-m}q^{k-m}.
```

---

# 4. Exact stopped-OU realization

Let

```math
Z_0,Z_1,Z_2,...
```

be orthonormal coordinates. Define the AR(1) state

```math
X_j
=q^jZ_0
+\sqrt{1-q^2}\sum_{r=1}^j q^{j-r}Z_r.
```

Then

```math
\langle X_j,X_k\rangle=q^{|j-k|}.
```

Define the stopped state at depth `m`

```math
\boxed{
X_j^{(m)}
=q^jZ_0
+\sqrt{1-q^2}
\sum_{r=1}^{\min(j,m)}q^{j-r}Z_r.
}
```

For `j>m`, this is exactly the conditional expectation of the full state given the filtration generated by `Z_0,...,Z_m`.

Direct telescoping gives

```math
\begin{aligned}
\langle X_j^{(m)},X_k^{(m)}\rangle
&=
q^{j+k}
+(1-q^2)
\sum_{r=1}^{\min(j,k,m)}q^{j+k-2r}\\
&=
q^{j+k-2\min(j,k,m)}.
\end{aligned}
```

Therefore

```math
\boxed{
\langle X_j^{(m)},X_k^{(m)}\rangle
=R_q^{(m)}(j,k).
}
```

So the spatial P11 mask implements a literal stopped OU filtration, not merely an analogy.

---

# 5. Positive rank-one radius increments

Increasing the visible depth from `m` to `m+1` adds exactly the new innovation coordinate `Z_{m+1}`. Thus

```math
R_q^{(m+1)}(j,k)-R_q^{(m)}(j,k)
=(1-q^2)
q^{j-m-1}q^{k-m-1}
\mathbf 1_{j,k\ge m+1}.
```

Set

```math
(d_{m+1})_j
=\sqrt{1-q^2}\,q^{j-m-1}\mathbf1_{j\ge m+1}.
```

Then

```math
\boxed{
R_q^{(m+1)}-R_q^{(m)}
=d_{m+1}d_{m+1}^*\succeq0.
}
```

This is the exact channel-index Hamiltonian increment of the P11 boundary-depth flow.

---

# 6. The common overlap cone

The mask condition can be written

```math
(a+1)h_p\le2d_R(x).
```

Introduce the geometric cone

```math
\boxed{
\mathcal C_R
=
\{(x,t): |x|<R,\ 0<t<2(R-|x|)\}.
}
```

For the common-jump operator

```math
K_t=T_{t/2}-T_{-t/2},
```

the inequality

```math
t<2d_R(x)
```

is precisely the condition that both half-shifted points `x+-t/2` lie inside the support window.

The P11 innovation masks are the discrete prime-ray sections

```math
\boxed{
t=(a+1)\log p}
```

of this same overlap cone.

Thus a previously separate P11 spatial object and the COMMON-JUMP geometry share the exact same boundary-depth variable.

---

# 7. Direct-integral interpretation

At a fixed spatial point `x`, each prime branch has a finite visible innovation depth `m_p(x)`, while all prime branches share the root coordinate. Hence the finite-window P11 hub+rest target can be viewed as a direct integral over `x` of prime star-tree fibres whose branch depths are

```math
m_p(x)=\lfloor2d_R(x)/\log p\rfloor.
```

As `R` increases (with `x` fixed away from the moving boundary), each branch changes only when one of the surfaces

```math
2d_R(x)=r\log p
```

is crossed; the change is the positive rank-one innovation from Section 5.

This is a genuine radius-consistent positive filtration already present in P11.

---

# 8. Firewall from existing negative calibrations

This stopped-filtration theorem does **not** imply that the native P11 Gram equals the Weil form.

The already merged finite-window audits show that the native P11 Rest and native Feshbach/Schur pairing miss the exact Prime-2 Weil calibration on the documented `R=1` witness. Those results remain untouched.

What changes is the structural interpretation of the remaining search space:

```text
old view:  P11 masks are window technicalities;
new exact view: P11 masks are the positive depth filtration of the OU tree.
```

Therefore any future use of P11 for Object X should work with the **full stopped spatial filtration**, not only with the windowless AR(1) ledger.

---

# 9. Next gate

The natural next question is whether the stopped discrete OU filtration on

```math
\mathcal C_R\cap\{t=r\log p\}
```

and the continuous Critical-half/Gamma geometry on the same overlap cone can be embedded into one positive boundary-depth system whose Schur complement reproduces the pole-subtracted discrepancy normal form.

A successful construction must also overcome the existing Prime-2 native-Feshbach mismatch; merely renaming the current P11 Rest Gram does not suffice.
