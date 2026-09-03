# P11 R43 — orbit-adapted flag-leakage telescoping reduction

Date: 2026-09-03

## Purpose

Refine the open B-FLAGTIGHT gate after the exact moving-range terminal cocycle
[
mathcal T_{U	o V}=W_VW_U^*
]
was isolated.

This note does **not** close B-FLAGTIGHT.  It separates three levels:

1. an exact fixed-source pullback formulation of the flag tail;
2. a tautology firewall for the cocycle itself;
3. a genuinely quantitative, orbit-adapted one-step leakage criterion whose summability is sufficient for B-FLAGTIGHT.

R43 remains OPEN.  No freeze, no formal independent-GREEN booking, no `✓[M]`, no Strong-Terminal/C6, Object-X, or RH promotion.

---

## 1. Fixed-source pullback of the target flag

Fix (0<R<S).  Write
[
W_U:=W_{R,S}^{[U]}:H_R	o H_S,
qquad
w_U:=W_Uarepsilon_R,
]
and let
[
P_m:=P_{mathcal H_S^{[m]}}
qquad(mge1).
]

Since (P_marepsilon_S=0) for (mge1), the decomposition
[
w_U=b_Uarepsilon_S+h_U
]
gives
[
P_mw_U=P_mh_U.
]

Define the positive contractions on the fixed source space
[
oxed{
Q_{m,U}:=W_U^*P_mW_U.
}
	ag{R43.FL1}
]

Then
[
0le Q_{m,U}le I,
]
and because (P_{m+1}le P_m),
[
Q_{m+1,U}le Q_{m,U}.
]

For the single unresolved source normal,
[
oxed{
|P_mh_U|^2
=
|P_mw_U|^2
=
langle arepsilon_R,Q_{m,U}arepsilon_Rangle.
}
	ag{R43.FL2}
]

Hence
[
oxed{
	ext{B-FLAGTIGHT}
iff
lim_{m	oinfty}limsup_{U	oinfty}
langle arepsilon_R,Q_{m,U}arepsilon_Rangle
=0.
}
	ag{R43.FL3}
]

For each fixed (U), (P_m	o0) strongly and therefore
[
Q_{m,U}	o0
]
strongly.  The entire issue is the noncommutation of the two limiting processes (m	oinfty) and (U	oinfty), tested on one fixed vector (arepsilon_R).

---

## 2. Tautology firewall for the moving-range cocycle

For every family of isometries (W_U:H_R	o H_S), not only for P11, one may define
[
mathcal T_{U	o V}:=W_VW_U^*.
]
Then
[
mathcal T_{U	o V}W_U=W_V
]
and
[
mathcal T_{V	o Z}mathcal T_{U	o V}
=
mathcal T_{U	o Z}
]
on (operatorname{Ran}W_U).

Therefore the **existence** of this cocycle is algebraically exact but by itself contains no P11-specific compactness or regularity.  Any future claim that "the cocycle implies tightness" must identify an additional quantitative estimate.

The natural P11-specific object is not the cocycle alone but its off-flag block
[
oxed{
P_mmathcal T_{U	o V}(I-P_m),
}
	ag{R43.FL4}
]
or, more weakly and more relevantly, this block tested on the actual normal orbit.

Because (P_m(I-P_m)=0),
[
P_mmathcal T_{U	o V}(I-P_m)
=
P_m[P_m,mathcal T_{U	o V}](I-P_m)
]
up to the harmless sign convention for the commutator.  Thus the live quantity is a one-sided flag-commutator block, not a terminal derivative.

No generator or differentiability theorem is used.

---

## 3. Exact one-step orbit inequality

Since
[
w_V=mathcal T_{U	o V}w_U,
]
decompose
[
w_U=P_mw_U+(I-P_m)w_U.
]
Then
[
P_mw_V
=
P_mmathcal T_{U	o V}P_mw_U
+
P_mmathcal T_{U	o V}(I-P_m)w_U.
]

Because (P_m) and (mathcal T_{U	o V}) are contractions,
[
|P_mmathcal T_{U	o V}P_mw_U|
le
|P_mw_U|.
]
Therefore
[
oxed{
|P_mw_V|
le
|P_mw_U|
+
lambda_m(U,V),
}
	ag{R43.FL5}
]
where the **orbit-adapted one-step leakage** is
[
oxed{
lambda_m(U,V)
:=
|P_mmathcal T_{U	o V}(I-P_m)w_U|.
}
	ag{R43.FL6}
]

This is strictly weaker than asking for the full operator bound
[
|P_mmathcal T_{U	o V}(I-P_m)|,
]
because only the actual shallow component of the unresolved normal orbit is tested.

The full off-flag operator norm remains a sufficient but unnecessarily strong target.

---

## 4. Telescoping theorem on a terminal partition

Choose a terminal partition
[
U_0<U_1<U_2<cdots	oinfty.
]
For each (m,k), define
[
oxed{
Lambda_{m,k}^{m orb}
:=
sup_{Vin[U_k,U_{k+1}]}
lambda_m(U_k,V).
}
	ag{R43.FL7}
]

Applying (R43.FL5) first to (U_k	o U_{k+1}) and then inductively gives
[
|P_mw_{U_k}|
le
|P_mw_{U_0}|
+
sum_{j<k}Lambda_{m,j}^{m orb}.
	ag{R43.FL8}
]

For arbitrary (Vin[U_k,U_{k+1}]),
[
|P_mw_V|
le
|P_mw_{U_k}|
+
Lambda_{m,k}^{m orb},
]
hence
[
oxed{
sup_{Uge U_0}|P_mw_U|
le
|P_mw_{U_0}|
+
sum_{kge0}Lambda_{m,k}^{m orb}.
}
	ag{R43.FL9}
]

Since (w_{U_0}) is fixed and (P_m	o0) strongly,
[
|P_mw_{U_0}|	o0.
]

Therefore:

### Proposition R43-FL — orbit-adapted summable leakage criterion

If there exists a terminal partition (U_k	oinfty) such that
[
oxed{
lim_{m	oinfty}
sum_{kge0}Lambda_{m,k}^{m orb}
=0,
}
	ag{R43.FL10}
]
then
[
oxed{
lim_{m	oinfty}
sup_{Uge U_0}
|P_mh_U|
=0.
}
	ag{R43.FL11}
]
In particular B-FLAGTIGHT holds.

This proves a stronger fixed-tail uniformity statement than the exact asymptotic B-FLAGTIGHT gate, so it is a sufficient criterion only.

---

## 5. Operator-norm version

Define
[
Lambda_{m,k}^{m op}
:=
sup_{Vin[U_k,U_{k+1}]}
|P_mmathcal T_{U_k	o V}(I-P_m)|.
	ag{R43.FL12}
]

Since (|w_{U_k}|=1),
[
Lambda_{m,k}^{m orb}
le
Lambda_{m,k}^{m op}.
]
Thus
[
oxed{
lim_{m	oinfty}
sum_{kge0}Lambda_{m,k}^{m op}=0
Longrightarrow
	ext{B-FLAGTIGHT}.
}
	ag{R43.FL13}
]

But (R43.FL13) is intentionally not promoted as the primary target.  It demands uniform flag control on the entire moving range, whereas R43 only needs the one unresolved normal orbit.

---

## 6. Relation to the old C6a tail route

Frozen C6a proves that the **native profile inclusion**
[
iota_{R,S}
]
is lower triangular in the canonical jet ONBs and explicitly warns that square-root metric normalization can reintroduce higher-layer mixing.

The present block
[
P_mmathcal T_{U	o V}(I-P_m)
]
is exactly where such mixing would have to be controlled.

Therefore no implication
[
iota_{R,S}	ext{ triangular}
Longrightarrow
mathcal T_{U	o V}	ext{ flag preserving}
]
is used.

The older C6a candidate tail quantities
[
Q_{R,N}M_{R,T}^{pm1/2}P_{R,N}
]
are conceptually related: both measure how square-root metric normalization leaks across a canonical jet cut.  The new formulation has two advantages for the current R43 problem:

1. it is directly attached to the exact last normal orbit;
2. it identifies an orbit-adapted leakage scalar rather than requiring full finite-window operator control.

No equivalence between the old C6a tail block and (R43.FL6) is currently claimed.

---

## 7. What R40/R41 may and may not contribute

R40/R41 provide a (U^{-1})-scale for the dual-normal channel.  This cannot be inserted into (R43.FL10) without a new estimate of the form
[
Lambda_{m,k}^{m orb}
le
epsilon_k,eta(m)
]
with
[
eta(m)	o0,
qquad
sum_kepsilon_k<infty.
]

A bare pointwise (U^{-1}) scale on linearly spaced terminals is not summable.  Choosing a sparse terminal partition does not by itself solve the problem, because (Lambda_{m,k}^{m orb}) is a supremum over the whole interval ([U_k,U_{k+1}]); the interval estimate must itself improve.

Thus no (U^{-1}Rightarrow) B-FLAGTIGHT inference is booked.

---

## 8. Current sharpened front

The live Strong-Terminal chain is now

[
oxed{
	ext{GC-AC candidate-closed}
longrightarrow
	ext{B-FLAGTIGHT}
longrightarrow
	ext{B-SIGN}.
}
]

Inside B-FLAGTIGHT, the next quantitative target is sharpened from a generic "deep-flag leakage bound" to:

[
oxed{
	ext{find a terminal partition and prove }
sum_k
sup_{Vin[U_k,U_{k+1}]}
|P_mmathcal T_{U_k	o V}(I-P_m)w_{U_k}|
longrightarrow0
quad(m	oinfty).
}
	ag{R43.FL14}
]

This is sufficient, orbit-adapted, derivative-free, and respects the C6a Gram-angle firewall.

It is not yet proved.
