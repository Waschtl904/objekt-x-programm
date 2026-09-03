# P11 R43 — orbit-adapted flag leakage: self-correction and fixed-source dynamics

Date: 2026-09-03

## Status

This companion note records a same-day self-correction to the first orbit-adapted
telescoping formulation.

The inequality based on
[
mathcal T_{U	o V}=W_VW_U^*
]
is mathematically valid, but its off-flag term is **not** a pure terminal increment.
The canonical R43 file now contains the corrected formulation R43.59p0--R43.59t7.

R43 remains OPEN.  No freeze, no formal independent-GREEN booking, no `✓[M]`, no
Strong-Terminal/C6, Object-X, or RH promotion.

---

## 1. Exact fixed-source flag effect

Let
[
P_m=P_{mathcal H_S^{[m]}},
qquad
w_U=W_Uarepsilon_R=b_Uarepsilon_S+h_U.
]
Define
[
oxed{
Q_{m,U}:=W_U^*P_mW_U.
}
]
Then (Q_{m,U}) is a positive contraction on the fixed source space and
[
oxed{
q_m(U)
:=
langlearepsilon_R,Q_{m,U}arepsilon_Rangle
=
|P_mh_U|^2.
}
]
Thus
[
oxed{
	ext{B-FLAGTIGHT}
iff
lim_{m	oinfty}limsup_{U	oinfty}q_m(U)=0.
}
]
For each fixed (U), (Q_{m,U}	o0) strongly.  The only issue is uniformity as the
terminal horizon escapes.

---

## 2. Why the partial-isometry off-flag block is statically contaminated

The exact moving-range cocycle is
[
mathcal T_{U	o V}=W_VW_U^*.
]
On the moving range it transports (w_U) to (w_V), but as an operator on the whole target
space
[
mathcal T_{U	o U}=W_UW_U^*=R_U,
]
the projection onto (operatorname{Ran}W_U).

Therefore
[
delta_{U,U}(m)
=
|P_mR_U(I-P_m)|
]
need not vanish.

If
[
B_{m,U}=P_mR_UP_m,
]
then
[
oxed{
delta_{U,U}(m)^2
=
|B_{m,U}-B_{m,U}^2|.
}
]
Hence the off-flag block measures a principal-angle defect between the moving transport range
and the fixed C6a flag, even when the terminal horizon does not move at all.

The same issue affects the orbit-adapted quantity
[
lambda_m(U,V)
=
|P_mmathcal T_{U	o V}(I-P_m)w_U|:
]
it is a legitimate sufficient term in the triangle inequality, but it is not automatically
small for (Vapprox U).

Accordingly the first version of this companion note was too optimistic in calling
(lambda_m) the primary local-dynamics quantity.

---

## 3. The old telescoping inequalities remain valid but strong

One still has
[
|P_mh_V|
le
|P_mh_U|
+
delta_{U,V}(m),
]
and likewise with the smaller orbit-adapted term
[
|P_mh_V|
le
|P_mh_U|
+
lambda_m(U,V).
]

Therefore summable bounds for either quantity along terminal chains are sufficient for
B-FLAGTIGHT.

But because both quantities contain the static range/flag angle, such bounds are now
classified as **strong sufficient diagnostics**, not as the preferred incremental route.

---

## 4. Genuine terminal increment on the fixed source space

Define
[
oxed{
D_m^{U,V}:=Q_{m,V}-Q_{m,U}.
}
]
Then
[
D_m^{U,U}=0
]
exactly.

C2 supplies the genuine horizon-gauge changes
[
C_X^{U	o V}
=
G_{X,V}^{1/2}G_{X,U}^{-1/2},
qquad
Xin{R,S},
]
with
[
W_V
=
C_S^{U	o V}W_U(C_R^{U	o V})^{-1}.
]
Consequently
[
oxed{
Q_{m,V}
=
(C_R^{U	o V})^{-*}
W_U^*
(C_S^{U	o V})^*
P_m
C_S^{U	o V}
W_U
(C_R^{U	o V})^{-1}.
}
]

This formula is P11-specific and isolates the actual sources of flag motion:

1. target flag distortion under (C_S^{U	o V});
2. source renormalization under ((C_R^{U	o V})^{-1});
3. coupling through (W_U).

O1 already decomposes each horizon gauge into relative modulus/range-leakage and polar-phase
pieces, so it is the natural prior structure to reuse.

---

## 5. Positive-variation criterion

Choose a partition
[
U_0<U_1<U_2<cdots	oinfty
]
and define
[
Omega_{m,k}
:=
sup_{Vin[U_k,U_{k+1}]}
igl(q_m(V)-q_m(U_k)igr)_+.
]
Then
[
sup_{Uge U_0}q_m(U)
le
q_m(U_0)
+
sum_{kge0}Omega_{m,k}.
]
Since (q_m(U_0)	o0) for fixed (U_0),
[
oxed{
lim_{m	oinfty}sum_{kge0}Omega_{m,k}=0
Longrightarrow
	ext{B-FLAGTIGHT}.
}
]

This is still a sufficient criterion stronger than the exact iterated-limsup formulation,
but it has the correct incremental normalization: the contribution of a zero terminal step
is exactly zero.

---

## 6. Current front

The live question is no longer booked as

> make the partial-isometry off-flag block small merely because (V-U) is small.

Instead it is

[
oxed{
	extbf{B-FLAGDYN: control the positive terminal variation of }
q_m(U)=
langlearepsilon_R,W_U^*P_mW_Uarepsilon_Rangle
	extbf{ through the exact horizon-gauge dynamics.}
}
]

The old (delta)- and (lambda)-routes remain valid strong sufficient routes, but their
static range/flag-angle contamination is explicit.

No bound on B-FLAGDYN is proved in this note.
