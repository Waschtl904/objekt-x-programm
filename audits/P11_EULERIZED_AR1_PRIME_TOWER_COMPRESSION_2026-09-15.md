# P11 Audit — Eulerized AR(1) prime-tower compression

**Datum:** 15. September 2026  
**Branch:** `research/critical-half-green-tree-bridge-2026-09-13`  
**Rolle:** theorem-level Prime-Kompression nach dem Hard Audit.  
**Registry:** unveraendert.  
**Nonclaim:** kein NP-GAP-/Object-X-/RH-Beweis; keine Publikationsneuheit behauptet.

---

## 0. Kurzurteil

Der gesamte Weil-gewichtete Prime-Power-Jump-Turm einer festen Primzahl `p`
laesst sich exakt auf **einen** stabilen AR(1)-/Euler-Zustand komprimieren.

Setze

```math
h=\log p,
\qquad q=p^{-1/2},
\qquad U=T_h.
```

Definiere

```math
\boxed{
B_p
:=
\sqrt{\frac{h q(1+q)}{1-q}}
\,(U-I)(I-qU)^{-1}.
}
```

Dann gilt auf `L^2(R)` exakt

```math
\boxed{
B_p^*B_p
=
\sum_{k\ge1}h q^k K_{kh}^*K_{kh},
}
```

also

```math
\boxed{
\|B_pv\|_2^2
=
\sum_{k\ge1}
\frac{\log p}{p^{k/2}}
\|K_{k\log p}v\|_2^2.
}
```

Der Nenner `(I-qU)^(-1)` ist derselbe AR(1)-Resolvent, der im P11-Cholesky-/Innovationsfaktor auftritt. Die neue Operation ist die kanonische Eulerisierung des Kanalindex-Shifts durch den physischen Log-p-Shift `U=T_logp`.

Noch staerker: `B_p` stammt aus einer exakten positiven-real Storage-Identitaet mit demselben Zustandspol `q`.

Status:

```text
prime tower one-state compression                         ✓[M]
AR(1)/Euler denominator q=p^-1/2                         ✓[M]
passive KYP/storage identity                              ✓[M]
centered local-finiteness without prime-power cutoff      ✓[M]
exact PR91 Prime-2 mixed calibration                      ✓[M]
full lower-frame / Object X                               ?[O]
```

---

# 1. Operator identity

Recall

```math
K_t=T_{t/2}-T_{-t/2},
\qquad
K_t^*K_t=2I-T_t-T_{-t}.
```

For the fixed prime `p`, let `U=T_h`, `h=log p`. Then

```math
\sum_{k\ge1}h q^k K_{kh}^*K_{kh}
=
\sum_{k\ge1}h q^k(2I-U^k-U^{-k}).
```

Since `0<q<1`, the geometric series converge in operator norm:

```math
\sum_{k\ge1}q^k U^k
=qU(I-qU)^{-1},
```

and similarly for `U^*`.

On the other hand,

```math
B_p
=
\sqrt{\frac{hq(1+q)}{1-q}}
(U-I)(I-qU)^{-1}.
```

Because `U` is unitary, functional calculus on the unit circle reduces the equality to

```math
\frac{hq(1+q)}{1-q}
\frac{|z-1|^2}{|1-qz|^2}
=
\sum_{k\ge1}hq^k(2-z^k-z^{-k}),
\qquad |z|=1.
```

The right side is the elementary Poisson/geometric identity

```math
2h\sum_{k\ge1}q^k(1-\cos k\theta)
=
\frac{hq(1+q)}{1-q}
\frac{|e^{i\theta}-1|^2}{|1-qe^{i\theta}|^2}.
```

Hence the operator identity follows.

---

# 2. One-state form

Set

```math
s_q:=\sqrt{1-q^2},
\qquad
\alpha_q:=\sqrt{\frac{1+q}{1-q}}
=\frac{1+q}{s_q}.
```

Define the causal/logarithmic AR(1) state

```math
\boxed{
\xi_p
:=s_q U(I-qU)^{-1}v.
}
```

Equivalently,

```math
\boxed{
\xi_p=qU\xi_p+s_qUv.
}
```

Then

```math
\xi_p-\alpha_qv
=
\alpha_q(U-I)(I-qU)^{-1}v,
```

and therefore

```math
\boxed{
B_pv
=\sqrt{hq}\,(\xi_p-\alpha_qv).
}
```

Thus the full infinite prime-power positive Gram tower is represented by a single scalar AR(1) state in one copy of `L^2(R)`.

This is not the native P11 Rest map applied directly to the jump-channel sequence. It is a **mediated Eulerization** of the same AR(1) recurrence under the intrinsic identification `k -> k log p`. This distinction is essential because the native P11 Rest/Feshbach pairing is already known to miss the exact Prime-2 mixed calibration.

---

# 3. Positive-real realization

On a fibre modulo `h`, use a discrete index `n` and define

```math
x_{n+1}=q x_n+s_q u_n,
```

```math
y_n
=-\frac{hq}{s_q}x_n
+\frac{hq}{1-q}u_n.
```

The transfer function, with the standard one-step state delay, is

```math
\boxed{
H_p(z)
=\frac{hq(1-z)}{(1-q)(1-qz)}
=h\sum_{k\ge1}q^k(1-z^k).
}
```

Set the storage coefficient

```math
\boxed{
P_p:=\frac{hq}{1-q^2}>0.
}
```

A direct expansion gives the exact KYP/storage identity

```math
\boxed{
2\operatorname{Re}(\overline{u_n}y_n)
-P_p(|x_{n+1}|^2-|x_n|^2)
=hq\left|
x_n-\sqrt{\frac{1+q}{1-q}}u_n
\right|^2
\ge0.
}
```

The associated `2x2` KYP matrix has determinant zero and is positive semidefinite of rank one. Hence this is a lossless/passive one-state realization of the full p-power positive-real jump response.

Summing over a fibre for compactly supported input telescopes the storage term, and the total dissipation is exactly the prime-tower Gram energy from Section 1.

---

# 4. Centered window form is cutoff-free per prime

Let `v` be supported in `[-a,a]`. Define

```math
c_p:=\sum_{k\ge1}hq^k=\frac{hq}{1-q}.
```

The centered p-block is

```math
Q_p(v)
:=
\sum_{k\ge1}hq^k
\left(\|K_{kh}v\|^2-2\|v\|^2\right).
```

For every `kh>2a`, the shifted supports are disjoint and

```math
\|K_{kh}v\|^2=2\|v\|^2.
```

Therefore the centered sum is actually finite on every compact support and

```math
\boxed{
Q_p(v)
=\|B_pv\|^2-2c_p\|v\|^2.
}
```

If `h=log p>2a`, every term is exterior and

```math
Q_p(v)=0.
```

Thus the Prime-Power cutoff is unnecessary at the level of the centered one-state p-block: local finiteness is automatic.

---

# 5. Exact Prime-2 firewall PASS

Use the exact PR #91 mixed witness `a,b` with

```math
\langle a,b\rangle=0,
```

and whose correlation support meets the Prime-Power lattice only at `log 2`, with

```math
g_{a,b}(\log2)=1/2.
```

The exact Weil Prime-2 mixed target is

```math
-\frac{\log2}{\sqrt2}.
```

By the operator identity,

```math
\langle B_2a,B_2b\rangle
=
\sum_{k\ge1}\frac{\log2}{2^{k/2}}
\langle K_{k\log2}a,K_{k\log2}b\rangle.
```

All `k>=2` terms vanish by support. For `k=1`,

```math
\langle K_{\log2}a,K_{\log2}b\rangle=-1.
```

Hence

```math
\boxed{
\langle B_2a,B_2b\rangle
=-\frac{\log2}{\sqrt2},
}
```

exactly the required mixed Weil calibration.

This is important relative to the earlier native P11 Rest/Feshbach firewalls: the Eulerized one-state mediator is outside those failed native classes and passes their calibration witness with no fitted coefficient.

---

# 6. Relation to the local Euler factor

The internal state denominator is

```math
(1-qz)^{-1}.
```

With

```math
q=p^{-1/2},
\qquad z=e^{-s\log p},
```

this becomes

```math
\boxed{
\frac1{1-p^{-(s+1/2)}},
}
```

the local Euler factor. Thus the same one-state recurrence simultaneously encodes:

```text
P11 AR(1) transition q
Prime-power geometric tail
local Euler denominator
positive prime jump tower
```

No novelty claim is made for the individual state-space or Euler identities. The project-specific point is that the already-derived P11 AR(1) parameter yields an exact forward mediator for the complete prime-tower positive Gram and passes the pre-existing exact mixed-pair firewall.

---

# 7. What remains open

The theorem compresses the positive Prime-Power feature family, but it does not remove the centered scalar

```math
2c_p I.
```

Summed over active primes and combined with the archimedean finite-part mass, these scalars are exactly the sharp NP-GAP threshold problem in another form.

Therefore this result does **not** prove positivity. It improves the candidate state architecture:

```math
Prime powers for p
   -> one canonical AR(1)/Euler state B_p
Gamma modes
   -> one canonical stable first-order state per mu_m.
```

The next gate is whether these already-passive local states admit a canonical nonorthogonal/global storage coupling (forced by the overlap-cone/stopped-OU geometry) that absorbs the centered feedthrough masses without importing Lagarias positivity or RH.
