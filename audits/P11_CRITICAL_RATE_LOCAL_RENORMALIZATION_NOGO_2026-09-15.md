# P11 Audit — Critical-rate local-renormalization no-go

**Datum:** 15. September 2026  
**Branch:** `research/critical-half-green-tree-bridge-2026-09-13`  
**Rolle:** enger Klassen-No-Go fuer die lokale Positivierung des Critical-half-Finite-Part-Transfers.  
**Registry:** unveraendert.  
**Nonclaim:** kein No-Go gegen relative Determinanten, Streuung, Spektralverschiebung oder groessere nichtlokale positive Systeme.

---

## 0. Kurzurteil

Der Critical-half-Finite-Part-Tail

```math
J_\Delta(L)
=e^{L/2}
\left(L-\gamma-\sum_{\log n<L}\frac{\Lambda(n)}{n}\right)
```

ist die endliche Differenz zweier bei der kritischen Rate einzeln divergenter positiver Tail-Amplituden. Der naheliegende Versuch,

1. Prime- und Continuum-Amplitude in einem positiven `2x2`-Hamiltonian zu mischen und
2. danach nur die gemeinsame skalare Divergenz von der Diagonale abzuziehen,

kann **keinen positiven endlichen lokalen Hamiltonian** liefern.

Schon am Root `L=0` ist der verbleibende nichttriviale Eigenwert

```math
2J_\Delta(0)=-2\gamma<0.
```

Damit ist die Klasse

```text
positive Prime+Continuum 2-channel Hamiltonian
+ common scalar counterterm
+ local finite positive limit
```

rigoros ausgeschlossen.

Status:

```text
cutoff Prime amplitude positive                         ✓[M]
cutoff continuum amplitude positive                     ✓[M]
Hadamard 2-channel parent positive                      ✓[M]
common-divergence subtraction finite                    ✓[M]
positive local finite-part limit                        ×[M]
relative / transfer / spectral-shift realization        ?[O]
```

---

# 1. Positive cutoff amplitudes

Fix `L>=0` and an upper depth cutoff `T>L`. At the critical amplitude rate define

```math
\boxed{
J_P^{(T)}(L)
=
\sum_{L\le\log n\le T}
\frac{\Lambda(n)}{\sqrt n}
 e^{-(\log n-L)/2}
=
e^{L/2}
\sum_{L\le\log n\le T}
\frac{\Lambda(n)}{n}.
}
```

This is positive.

For the continuous pole compensator,

```math
\boxed{
J_0^{(T)}(L)
=
\int_L^T
 e^{-(t-L)/2}e^{t/2}dt
=e^{L/2}(T-L),
}
```

also positive.

Their difference converges, in the canonical Abel/finite-part sense and equivalently under the usual prime-number-theorem asymptotics, to `J_Delta(L)`.

---

# 2. Canonical positive two-channel mixing

Take the direct sum of the two positive scalar reservoirs and apply the fixed Hadamard rotation. The resulting local Hamiltonian is

```math
\boxed{
\mathbb H_T(L)
=
\begin{pmatrix}
J_P^{(T)}+J_0^{(T)} & J_P^{(T)}-J_0^{(T)}\\
J_P^{(T)}-J_0^{(T)} & J_P^{(T)}+J_0^{(T)}
\end{pmatrix}.
}
```

Its eigenvalues are exactly

```math
2J_P^{(T)}(L),
\qquad
2J_0^{(T)}(L),
```

so

```math
\boxed{\mathbb H_T(L)\succeq0.}
```

The off-diagonal entry tends to the desired signed finite-part transfer coefficient `J_Delta(L)`.

---

# 3. The common diagonal divergence

Both positive amplitudes have the same leading divergence

```math
J_P^{(T)}(L)
=
e^{L/2}(T-L)+J_\Delta(L)+o(1),
```

```math
J_0^{(T)}(L)
=
e^{L/2}(T-L).
```

Hence the diagonal of `H_T` diverges like

```math
2e^{L/2}(T-L).
```

The canonical scalar counterterm that removes this common divergence is

```math
2J_0^{(T)}(L)I.
```

Subtracting it gives

```math
\mathbb H_T-2J_0^{(T)}I
=
\begin{pmatrix}
J_P^{(T)}-J_0^{(T)} & J_P^{(T)}-J_0^{(T)}\\
J_P^{(T)}-J_0^{(T)} & J_P^{(T)}-J_0^{(T)}
\end{pmatrix}.
```

Its limit is

```math
\boxed{
\mathbb H_{\rm fp}(L)
=
J_\Delta(L)
\begin{pmatrix}1&1\\1&1\end{pmatrix}.
}
```

The eigenvalues are

```math
0,
\qquad
2J_\Delta(L).
```

---

# 4. Root obstruction

From the exact finite-part formula,

```math
J_\Delta(0)=-\gamma.
```

Therefore

```math
\operatorname{spec}\mathbb H_{\rm fp}(0)
=\{0,-2\gamma\}.
```

Since `gamma>0`,

```math
\boxed{
\mathbb H_{\rm fp}(0)\not\succeq0.
}
```

Thus positivity is destroyed already at the root by the canonical common-counterterm subtraction.

More generally, whenever `J_Delta(L)<0`, the same local obstruction occurs.

---

# 5. Scope of the no-go

The argument excludes only a very specific but natural class:

```text
- two local positive reservoirs (Prime and continuum),
- fixed unitary/Hadamard mixing,
- a common scalar diagonal counterterm removing the shared divergence,
- positivity demanded after taking the finite local limit.
```

It does not exclude:

```text
- keeping the positive cutoff parent unrenormalized and extracting only a relative observable;
- a relative Fredholm determinant;
- Krein spectral shift / scattering phase;
- a boundary transfer obtained before the cutoff is removed;
- nonlocal coupling in L;
- a larger conservative colligation;
- an indefinite intermediate observable inside an overall positive Hilbert dilation.
```

---

# 6. Strategic consequence

The signed coefficient `J_Delta` is **not** to be treated as a renormalized positive Hamiltonian density.

The only surviving use consistent with the hard audit is as a relative quantity:

```math
\boxed{
J_\Delta
=
\text{Prime boundary response}
-
\text{free-continuum boundary response}.
}
```

The next Object-X candidate therefore has to keep the positive Prime and continuum reservoirs themselves and recover the Weil term through a relative boundary observable (transfer matrix, scattering phase, determinant ratio, spectral shift, etc.), rather than by subtracting their energies pointwise.
