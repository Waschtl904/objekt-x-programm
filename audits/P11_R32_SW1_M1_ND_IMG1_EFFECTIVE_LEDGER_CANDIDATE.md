# P11 / R32 / SW1 — M1-ND-IMG1 effective 3x6 function-channel ledger candidate

## Status

`M1-ND-IMG1`: **candidate under certificate review**.

No `✓[M]` promotion. No injectivity claim.

This node is downstream of:

- `SW1-A10-C2-M1-FULL(r)`;
- `M1-ND-IMG0`;
- the analytic kernel bijection
  [
  ker mathscr N_R cong ker widehat{mathscr C}_R cong ker Gamma_I.
  ]

The active task here is only the exact effective assembly of
[
mathscr N_R
=
R_{P_0}^{m out},
widehat{mathscr C}_R,
(E_Hoplus E_W)
]
on the true image coordinates.

---

## 1. Domain and codomain firewall

The six independent input **function channels** are
[
u=(f_0,f_1,f_2,g_0,g_1,g_2),
qquad
finmathscr B_K,quad ginmathscr B_W.
]

This is not a six-dimensional vector space. Each entry is an (L^2)-function channel.

The output has the three (P_0) horizon lifts
[
(mathscr N_Ru)_0,quad
(mathscr N_Ru)_1,quad
(mathscr N_Ru)_2.
]

The formal (12_H+12_W=24) species/lift ambient slots are not independent variables and are not used as the IMG1 kernel domain.

---

## 2. Effective pullbacks

For an M1 input species
[
g_{m in}=(s,eta,kappa)
]
and original seven-layer shift (j), IMG0 gives
[
F_{g_{m in},k}(	heta+jDelta)
=
f_k!left(
ho_{g_{m in}}(	heta+jDelta)
ight)
]
or the analogous annulus channel.

Hence the effective base pullback is
[
oxed{
alpha_{g_{m in},j}(	heta)
=
s	heta+rac{eta}{2}L+(sj+kappa)Delta
pmod L.
}
]

The exact alphabet is the already certified 12-type set:
[
egin{aligned}
&	heta, 	hetapmDelta, 	hetapm2Delta,\
&-	heta+Delta, -	heta+2Delta, -	heta+3Delta, -	heta+4Delta,\
&-	heta+rac L2+2Delta, 
	heta+rac L2-2Delta, 
	heta+rac L2+2Delta.
end{aligned}
]

Only the three (B)-hub branches produce the (L/2) pullbacks.

---

## 3. Exact 3x6 operator form

On each open (B_{96})-atom the candidate certificate constructs
[
oxed{
(mathscr N_Ru)_a(	heta)
=
sum_{c=0}^{5}
sum_{alphainmathcal A_{12}}
C_{a,c,alpha},
u_c(alpha(	heta)),
qquad a=0,1,2,
}
]
where every active contribution stores exactly:

1. effective affine map (alpha);
2. Horizon/Annulus input block;
3. input lift (k=0,1,2);
4. (P_0) output lift (a=0,1,2);
5. exact symbolic coefficient;
6. physical FREE row or HUB branch;
7. source name;
8. original M1 input species;
9. original M1 shift (j).

Contributions with the same
[
(a,c,alpha)
]
are grouped explicitly, retaining the full coefficient/provenance multiset rather than silently overwriting or simplifying them.

---

## 4. Two independent assembly paths inside the certificate

For every one of the (64	imes96=6144) open reference atoms at (r_0=7/2), the script constructs the reduced row in two ways.

### Path A — direct physical (P_0) assembly

Starting from (x_{m out}=	heta+aL), the physical FREE and HUB source variables are computed directly. Their unique source lift and effective IMG0 pullback are then determined.

### Path B — M1 ledger followed by IMG0 elimination

The already certified operator-oriented M1 species/shift rules and exact lift-selector formula are evaluated first. The resulting valid species slot is then replaced by its base-lift pullback.

The required identity is the strong termwise equality
[
oxed{
	ext{direct reduced physical ledger}
=
	ext{reduced M1 ledger}
}
]
including coefficient and provenance, followed by equality of their aggregated (3	imes6) pullback signatures.

---

## 5. Certificate dependency

Script:

`scripts/certify_sw1_m1_nd_img1_effective_ledger.py`

It imports and reruns

`scripts/certify_sw1_a10_c2_m1_full_b96.py`

before performing IMG1. Thus the new certificate is explicitly downstream of the canonical M1-FULL reference certificate rather than a copied replacement implementation.

---

## 6. What IMG1 does not prove

Even after a GREEN certificate, IMG1 alone does **not** prove
[
kermathscr N_R={0}.
]

In particular it does not yet:

- eliminate the analytic constraint (finmathscr B_K);
- derive a recurrence/transfer system;
- invert any outer block;
- prove a cocycle dichotomy;
- construct or exclude a nonzero admissible kernel function;
- add a new actual-(r) promotion;
- imply anything about Objekt X globally or RH.

The next legitimate step after a hardened IMG1 ledger is transfer/recurrence analysis on the actual admissible function space.

---

## 7. Review criterion

IMG1 may be called certificate-GREEN only if the workflow records exact provenance and the script passes all 6144 atoms with:

- exact direct-vs-ledger reduced equality;
- exactly six independent input function channels;
- exactly three (P_0) output channels;
- no species variable surviving as an independent coordinate;
- effective alphabet exactly equal to the 12 IMG0 types;
- deterministic reduced-state fingerprint.

No `✓[M]` promotion is requested by this candidate.
