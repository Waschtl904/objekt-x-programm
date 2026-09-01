# P11/R32 — SW1 M1-ND SALVAGE-A1/A2 Uniform Blind Wedge Candidate

> **Stand:** 1. September 2026  
> **Branch:** `research/sw1-m1-nd-salvage-phase-diagram`  
> **Status:** AI-GREEN candidate + exact finite/algebraic certificate for the
> new geometry; **no promotion yet**.  
> **Certificate:** `scripts/certify_sw1_m1_nd_salvage_a1_a2_uniform_blind_wedge.py`.

---

## 1. Statement

Set

[
h:=d-3Delta.
]

Using the physical constants one has

[
oxed{
h
=
rac{T-10Delta}{4}
=
rac{8log2-5log3}{2}
>0,
}
	ag{A12.1}
]

because

[
2^8=256>243=3^5.
]

Define

[
oxed{
arepsilon_c
:=
rac h2
=
rac{T-10Delta}{8}.
}
	ag{A12.2}
]

Candidate theorem:

> For every
> [
> 0<arepsilon<arepsilon_c,
> qquad
> 0<R<arepsilon,
> qquad
> 0<sigma<R,
> ]
> the current effective SW1 M1-ND operator satisfies
> [
> oxed{
> kermathscr N_R
e{0}.
> }
> 	ag{A12.3}
> ]

This is strictly stronger than the previously promoted single Small-(R)
witness: (R) may now range over the **entire** admissible interval
((0,arepsilon)).

---

## 2. The 24-gap Horizon barrier

Let

[
X_arepsilon=(0,T+arepsilon).
]

For

[
sin{0,a},
qquad
k=0,ldots,5,
qquad
jin{0,1},
]

define

[
F_{s,k,j}
=
left(
s+kDelta+jh+arepsilon,,
s+kDelta+(j+1)h-arepsilon
ight).
	ag{A12.4}
]

Because

[
0<arepsilon<h/2,
]

each interval has width

[
h-2arepsilon>0.
]

Let

[
oxed{
F_arepsilon
=
igcup_{s,k,j}
F_{s,k,j}.
}
	ag{A12.5}
]

There are exactly (24) such gaps.

The exact identities

[
h=d-3Delta,
]

[
h=a-(d+2Delta),
]

[
h=b-(a+3Delta),
]

[
h=T-(b+2Delta)
	ag{A12.6}
]

show why the barrier fits the physical centers.

The certificate proves uniformly on the entire open
(arepsilon)-interval that all 24 gaps are ordered, pairwise disjoint and
contained in ((0,T)).

Set

[
K_arepsilon
:=
X_arepsilonsetminus F_arepsilon
]

up to the null boundary points.

---

## 3. Maximal KNF sampling lies in (K_arepsilon)

Define the boundary-majorant sampling set

[
U_arepsilon^{max}
=
(a-arepsilon,a+arepsilon)
cup
(b-arepsilon,b+arepsilon)
cup
(T-arepsilon,T+arepsilon).
	ag{A12.7}
]

For every actual

[
0<R<arepsilon
]

the six KNF halfwindows satisfy

[
U_Rsubset U_arepsilon^{max}.
	ag{A12.8}
]

The certificate checks

[
oxed{
U_arepsilon^{max}cap F_arepsilon=arnothing.
}
	ag{A12.9}
]

Hence

[
U_Rsubset K_arepsilon.
]

---

## 4. FREE invariance

Use exactly the nine lower-chamber A7 maps and their exact domains:

[
	au_{pm a},
qquad
	au_{pm T},
qquad
r_a, r_T, r_{3a}, r_{4a}, r_{2b}.
]

For every forbidden gap and every active map/domain intersection, the
certificate checks exactly that the image is again covered by
(F_arepsilon).

There are

[
oxed{70}
]

nonempty forbidden-gap/map-domain image pieces, all certified.

The same script separately checks:

- (+aleftrightarrow-a) with matching inverse domains;
- (+Tleftrightarrow-T);
- (r_T,r_{3a},r_{4a},r_{2b}) are involutions on invariant domains;
- (r_a) swaps its two domain components.

Therefore (F_arepsilon) is invariant both forward and backward under the
graphing. Equivalently,

[
oxed{
K_arepsilon
	ext{ is invariant under the full A7 equivalence relation.}
}
	ag{A12.10}
]

Since

[
U_Rsubset K_arepsilon,
]

its full FREE saturation satisfies

[
oxed{
V_{arepsilon,R}
=
operatorname{Sat}_{mathcal E_arepsilon}(U_R)
subset
K_arepsilon.
}
	ag{A12.11}
]

This is the key point: no component-cardinality or Mass-Transport estimate is
needed.

---

## 5. Fourteen uniform Annulus gaps

Define the fourteen constants

[
mathcal C=
{
0,Delta,2Delta,3Delta,
d,d+Delta,d+2Delta,
a,a+Delta,a+2Delta,a+3Delta,
b,b+Delta,b+2Delta
}.
	ag{A12.12}
]

For (cinmathcal C) define

[
B_{arepsilon,c}
=
(c+arepsilon, c+h-arepsilon).
	ag{A12.13}
]

Let

[
oxed{
B_arepsilon
=
igcup_{cinmathcal C}
B_{arepsilon,c}.
}
	ag{A12.14}
]

The certificate proves uniformly:

1. all fourteen intervals are nonempty;
2. they are pairwise disjoint;
3. they lie in
   [
   (arepsilon,T).
   ]

The complement (K_arepsilon) consists of exactly (25) interval cells.

For each of those cells, the script evaluates all physical Hub-source pieces

[
|x-a|,quad x+a,quad
|x-b|,quad x+b,quad
|x-T|,quad x+T.
	ag{A12.15}
]

After splitting the absolute-value maps at their centers, this gives

[
oxed{153}
]

nonempty image pieces.

Every one of them is proved exactly disjoint from every interval in
(B_arepsilon).

Therefore

[
oxed{
H(K_arepsilon)
cap
B_arepsilon
=
arnothing.
}
	ag{A12.16}
]

Since (V_{arepsilon,R}subset K_arepsilon),

[
H(V_{arepsilon,R})
cap
B_arepsilon
=
arnothing.
	ag{A12.17}
]

Moreover, because (R<arepsilon) and (S=T+sigma>T),

[
B_arepsilon
subset
(arepsilon,T)
subset
(R,S).
	ag{A12.18}
]

Thus (B_arepsilon) is a genuine positive Annulus blind set for **every**
admissible (R,sigma) in the wedge.

---

## 6. Uniform blind measure

Every blind interval has width

[
h-2arepsilon.
]

Hence

[
egin{aligned}
|B_arepsilon|
&=
14(h-2arepsilon)\
&=
14left(
rac{T-10Delta}{4}
-
2arepsilon
ight)\
&=
oxed{
rac72
(T-10Delta-8arepsilon)
}.
end{aligned}
	ag{A12.19}
]

For

[
0<arepsilon<arepsilon_c
]

this is strictly positive.

Crucially,

[
oxed{
|B_arepsilon|
	ext{ has no }R	ext{-decay.}
}
	ag{A12.20}
]

This answers the strongest question raised on the new SALVAGE front:
the current geometry has an (R)-independent blind defect on an open
lower-(arepsilon) wedge.

---

## 7. Kernel construction

Choose

[
0
e w_+in L^2(B_arepsilon).
]

By IMG0 obtain the corresponding

[
0
e ginmathscr B_W.
]

Because the six Hub source maps from (V_{arepsilon,R}) avoid
(B_arepsilon),

[
Pi_{V_{arepsilon,R}}mathcal H_Rg=0.
	ag{A12.21}
]

The promoted IMG4 reducing-subspace mechanism gives

[
Pi_{V_{arepsilon,R}}
mathscr T_B^{-1}
=
mathscr T_B^{-1}
Pi_{V_{arepsilon,R}}.
	ag{A12.22}
]

Define

[
f
=
-mathscr T_B^{-1}mathcal H_Rg.
]

Then

[
Pi_{V_{arepsilon,R}}f=0.
]

Since

[
U_Rsubset V_{arepsilon,R},
]

all six KNF samples vanish, hence

[
finmathscr B_K.
]

Finally

[
mathscr N_R(f,g)
=
mathscr T_Bf+mathcal H_Rg
=
0.
]

Since (g
e0),

[
oxed{
kermathscr N_R
e{0}.
}
	ag{A12.23}
]

No Mass-Transport theorem and no finite-component bound enters this proof.

---

## 8. Interpretation

The earlier possibility that Small-(R) degeneracy might merely be a
thin boundary phenomenon is now strongly disfavored.

If A12.23 survives final audit, the current finite-level geometry is
degenerate on the open wedge

[
oxed{
0<arepsilon<
rac{T-10Delta}{8},
qquad
0<R<arepsilon,
qquad
0<sigma<R.
}
	ag{A12.24}
]

This is qualitatively different from the previous result:

- old proof: blind measure from a coarse (O(R)) visibility upper bound;
- new proof: explicit graph-invariant Horizon barrier and an
  (R)-independent positive Annulus blind set.

The linear phase-growth result (M_Nle288N+144) was therefore not itself the
uniform obstruction; it pointed toward a deeper **phase-placement defect**,
which A12.4–A12.19 make explicit.

---

## 9. Scope firewall

Not claimed yet:

- degeneracy for (arepsilongearepsilon_c);
- that (arepsilon_c) is the exact global phase boundary;
- injectivity anywhere on the visible side;
- any statement in the upper chamber;
- a separate promotion of (kerGamma_I
e0);
- Object-X failure;
- any RH conclusion.

The numerical phase-diagram probe suggests full support visibility at the
boundary-majorant (R=arepsilon) already by
(arepsilon=0.23Delta>arepsilon_c), but this is exploratory only.

---

## 10. Promotion gate

Before any (checkmark[M]_{m neg}) booking for A12.24:

1. run the exact certificate on the committed blob;
2. adversarially inspect the sign engine and the inference
   (F)-invariant + inverse graphing (Rightarrow K)-invariant;
3. verify the 153-piece Hub exclusion is on the actual IMG4 physical
   Hub-source list;
4. verify the imported IMG4 reducing/KNF mechanism is parameter-uniform in
   the entire lower chamber, not only at the old explicit witness.

Until these are checked, status remains candidate.
