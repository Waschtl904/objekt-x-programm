# P11 Audit — Critical transfer as stopped Root-trace defect

**Datum:** 16. September 2026  
**Branch:** `research/critical-half-green-tree-bridge-2026-09-13`  
**Registry:** unveraendert.  
**Nonclaim:** kein Positivitaets-/RH-/Object-X-Abschluss.

---

## 0. Result

The critical finite-part kernel

```math
J_\Delta(L)
=e^{L/2}\left(
L-\gamma-
\sum_{\log n<L}\frac{\Lambda(n)}n
\right)
```

has an exact P11 stopped-root interpretation.

For the normalized OU/P11 branch at prime `p`, with `h_p=log p` and

```math
q_p=p^{-1/2},
```

the normalized root correlation of channel `k` is

```math
\langle\Phi_o,\Phi_{p,k}\rangle=q_p^k=p^{-k/2}.
```

Therefore the squared root correlation is `p^{-k}`, and the stopped visible root trace

```math
\boxed{
M_P(L)
:=\sum_{p,k:\,k\log p<L}
(\log p)\,
|\langle\Phi_o,\Phi_{p,k}\rangle|^2
}
```

is exactly

```math
\boxed{
M_P(L)
=\sum_{\log n<L}\frac{\Lambda(n)}n.
}
```

Hence

```math
\boxed{
J_\Delta(L)=e^{L/2}\bigl(L-\gamma-M_P(L)\bigr).
}
```

At a spatial P11 point `x` in window radius `R`, the stopped depth is

```math
L_R(x)=2(R-|x|).
```

Thus `J_Delta(L_R(x))` is determined directly by the root trace of precisely the P11 channels already visible at that boundary depth.

The smooth reference `L` itself also splits into the already existing positive Riemann-R continuum root layer plus the Gamma-ground root layer. Consequently the whole finite-part coefficient is a relative stopped-root balance of the same geometry.

---

# 1. Prime stopped-root trace

The windowless normalized prime-branch covariance is

```math
R_q(j,k)=q^{|j-k|}.
```

Its root component is `u_k=q^k`. Therefore the diagonal trace of the root projection, with the natural base-spacing weight `h_p=log p`, is

```math
\sum_k h_p|u_k|^2
=\sum_k(\log p)p^{-k}.
```

Stopping at depth `L` retains exactly the indices satisfying

```math
k\log p<L.
```

Thus

```math
\begin{aligned}
M_P(L)
&=\sum_p\sum_{k\log p<L}(\log p)p^{-k}\\
&=\sum_{n=p^k:\log n<L}\frac{\Lambda(n)}n.
\end{aligned}
```

No prime-number theorem or RH is used.

---

# 2. Critical scaling converts root-square mass into Weil mass

When `L` crosses a node

```math
L_0=k\log p,
```

the visible root trace jumps upward by

```math
\Delta M_P(L_0)
=(\log p)p^{-k}.
```

Since

```math
J_\Delta(L)=e^{L/2}(L-\gamma-M_P(L)),
```

the corresponding jump of `J_Delta` is

```math
\begin{aligned}
\Delta J_\Delta(L_0)
&=-e^{L_0/2}(\log p)p^{-k}\\
&=-\frac{\log p}{p^{k/2}}.
\end{aligned}
```

Thus the Critical-half rescaling converts

```text
squared normalized root correlation:  p^{-k}
                    into
Weil prime-power weight:              p^{-k/2}.
```

This is exactly the atomic jump already required by

```math
d\Delta=\frac12J_\Delta dL-dJ_\Delta.
```

---

# 3. The smooth root trace is the R-continuum plus Gamma ground

The positive Riemann-R cell density satisfies

```math
\int_0^\infty\rho(h)
\sum_{k\ge1}h\,\delta_{kh}(dt)dh
=(e^t-1)dt.
```

The normalized OU root correlation at depth `t` has squared modulus `e^{-t}`. Therefore the stopped R-continuum root mass is

```math
\begin{aligned}
M_R(L)
&=\int_0^Le^{-t}(e^t-1)dt\\
&=\int_0^L(1-e^{-t})dt\\
&=L-1+e^{-L}.
\end{aligned}
```

The Gamma-ground root contribution is

```math
\boxed{
M_{\Gamma,0}(L)
=\int_0^Le^{-t}dt
=1-e^{-L}.
}
```

Hence

```math
\boxed{M_R(L)+M_{\Gamma,0}(L)=L.}
```

The critical finite-part coefficient therefore has the exact relative-storage bookkeeping

```math
\boxed{
e^{-L/2}J_\Delta(L)
=M_R(L)+M_{\Gamma,0}(L)-M_P(L)-\gamma.
}
```

Every nonconstant term on the right is a stopped positive root trace from geometry already present in the branch.

---

# 4. Relation to the spatial stopped filtration

For the actual P11 masks,

```math
L_R(x)=2(R-|x|),
\qquad
m_p(x)=\left\lfloor\frac{L_R(x)}{\log p}\right\rfloor
```

away from threshold equalities. Hence the locally visible normalized root trace is exactly

```math
M_P(L_R(x)).
```

The overlap-cone Volterra coefficient from the critical finite-part audit can therefore be rewritten as

```math
\boxed{
J_\Delta(L_R(x))
=e^{R-|x|}
\left(
M_R(L_R(x))
+M_{\Gamma,0}(L_R(x))
-M_P(L_R(x))
-\gamma
\right).
}
```

Thus the scalar arithmetic transfer coefficient is not an external fitted function when restricted to the P11 overlap cone: it is the Critical-half rescaling of the stopped root-trace defect between the discrete prime tree and its positive smooth reference.

---

# 5. First-level versus higher prime powers

Split

```math
M_P(L)
=\sum_{p<e^L}\frac{\log p}{p}
+
\sum_{\substack{k\ge2\\k\log p<L}}\frac{\log p}{p^k}.
```

The higher-power total converges absolutely:

```math
\boxed{
\sum_p\sum_{k\ge2}\frac{\log p}{p^k}
=\sum_p\frac{\log p}{p(p-1)}<\infty.
}
```

Hence all critical large-depth renormalization lies in the first prime/root level `k=1`. The higher root levels are an absolutely summable correction.

This is the time-domain counterpart of

```math
\log\zeta(S)
=\sum_pp^{-S}
+\sum_{m\ge2}\frac1m\sum_pp^{-mS},
```

where the `m>=2` part converges absolutely for `Re S>1/2`.

Consequently the unresolved global storage gate can be narrowed further:

```text
hard relative channel: first prime/root level versus smooth root continuum;
higher prime powers: absolutely summable correction;
local Euler cells: already passively subordinate to Gamma ground.
```

---

# 6. Firewall

The relative root trace

```math
M_R+M_{Gamma,0}-M_P-\gamma
```

changes sign. It is not a positive local storage density. The earlier root-only coupling no-go also remains valid: the scalar root trace cannot by itself repair the full higher-rank physical channel defect.

What is new here is narrower: the **coefficient** of the already exact nonlocal Volterra transfer is now reconstructed canonically from the stopped P11 root filtration and its positive smooth reference. A successful Object-X mechanism would still have to place this signed relative root balance as a boundary/transfer term of a larger positive system.
