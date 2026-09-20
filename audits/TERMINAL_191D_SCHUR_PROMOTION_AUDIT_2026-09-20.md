# Terminal 191D Schur — promotion audit

**Date:** 2026-09-20  
**Audit status:** PASS for the fixed-horizon terminal theorem; external review remains open.  
**Mathematical input frontier before promotion:** `79988874cceeb01f17e0cda67485838c0b7c4f63`.  
**Candidate package:** `research/x-c1/terminal-191d-schur-enclosure-2026-09-20/`.

This audit addresses the release conditions imposed after the floating-point
preflight failed calibration. It does not alter any global-horizon claim.

## 1. Same-engine endpoint calibration

Workflow run `35518951368`, job `106099567779`, executed the Arb/Legendre
assembly at
[
B=rac{log 5}{2}
]
with Python 3.13 and `python-flint==0.9.0`.

The new Arb assembly was compared entry-by-entry with the frozen PR-137
Fraction engine. In both parities:

- `A_nonoverlap = 0`;
- `Gact_nonoverlap = 0`;
- `delta_overlap = true`;
- `lower_nonoverlap = 0`;
- all 31 directed LDL pivots are positive.

Directed physical gaps:

[
arepsilon_B^{mathrm{even}}
>
1.0423892675689327	imes10^{-13},
]
[
arepsilon_B^{mathrm{odd}}
>
2.3831654046764897	imes10^{-11}.
]

Thus the same assembly reproduces the independently known endpoint theorem,
including the complete High response, and exceeds the required
(10^{-13}) all-parity floor.

Artifact ID: `10607872401`.  
Artifact ZIP SHA-256:
`143b7e556cddcb38f9d24155fac51bb337d80d1e71a515710e75f7e6e452b5f7`.

## 2. Fresh terminal verify/recompute replay

Workflow run `35519233118`, job `106100314824`, used a fresh runner:

- Linux 6.17.0-1022-azure x86_64;
- Python 3.13.15;
- `python-flint==0.9.0`;
- glibc 2.39;
- terminal Arb precision 2048 bits.

Command:

```text
python check_terminal.py --verify --recompute
```

The matrix generation was repeated from the bound mathematical inputs.
Reported recomputation time: 154.06611490249634 seconds.

Replay verdict:

- `TOTAL 442 terminal certificate checks PASS`;
- both parities `STRICT_POSITIVE`;
- every regenerated actual A/G matrix enclosure matches the stored certificate;
- byte-identical stored result/log verification passes;
- all twelve package payload hashes pass;
- physical gap (>10^{-26}) on the fixed horizon is re-certified.

Replay artifact ID: `10607328659`.  
Replay artifact ZIP SHA-256:
`2e1e4a082369b8de6fc2bec269860894a70204e8e9a45820b78576bc87770f90`.

## 3. Terminal High floor (delta=7/10)

The raw parity High spaces begin at Legendre degree 384 (even) and 385
(odd). Every raw High vector is orthogonal to the constant function.

The physical reference form at (a=1) is
[
q_1=D_H+V+q_0 I-K-S,
]
with (Vge0).

### 3.1 Regular Gamma operator

The regular Gamma kernel (g(r)) is positive decreasing on (0<rle2),
with (g(0+)=1/4). Since raw High vectors have mean zero, the constant
kernel (g(2)) contributes zero to the quadratic form. Hence Schur's test
gives
[
|K|_{mathrm{High}}
le
2left(rac14-g(2)ight).
]

This is a structural mean-zero improvement; it does not use the desired
full-window positivity.

### 3.2 Prime-power shifts

At (a=1), the active channels are exactly (2,3,4,5,7).

For (q=3,4,5,7), (log q>1), so the two branches of the partial
translation have disjoint support and
[
|T_{log q}|le1.
]

For (q=2), (d=log2<1), but (3d>2). Decomposing the interval into
translation orbits gives path graphs with at most three vertices. Their
adjacency norm is at most (sqrt2). Therefore
[
w_2|T_{log2}|
le
rac{log2}{sqrt2}sqrt2
=
log2.
]

Thus
[
|S|
le
log2+
rac{log3}{sqrt3}
+rac{log2}{2}
+rac{log5}{sqrt5}
+rac{log7}{sqrt7}.
]

The directed terminal checker combines this with (D_Hge H_{384}) and
the scalar (q_0) and verifies the raw High floor
[
q_1[y]>rac{73}{100}|y|^2.
]

### 3.3 Mellin reconstruction

The exact one-moment correction has norm below (10^{-100}) at the
terminal cutoff. The inherited uniform energy estimates
[
|q(y,e)|<8|y||e|,
qquad
|q[e]|<12|e|^2
]
therefore give
[
q_1[mathcal M y]
ge
q_1[y]-16epsilon|y|^2-12epsilon^2|y|^2
>
rac7{10}|mathcal M y|^2.
]

Hence the terminal High reserve (delta=7/10) is independently justified
without assuming terminal positivity.

## 4. Complete High-response enclosure

The Active-Set theorem gives, after the finite moment congruence,
[
F=
egin{pmatrix}
A&C^*\
C&D
end{pmatrix},
qquad Dsucceqdelta I.
]

The model coupling Gram (G) is the complete
[
P_Y(V-K^p-S)^*(V-K^p-S)P_Z
]
Gram: (V^2), (S^2), (V/S) cross terms and the complete finite support
of the Gamma polynomial beyond the Low cutoff are retained. It is not a
sampled High-mode truncation.

With model error (e) and (t=10^{-3}),
[
C^*C
preceq
G_{mathrm{act}}
=
rac{1001}{1000}G+1001e^2I.
]

Therefore
[
A-C^*D^{-1}C
succeq
A-rac{1001}{1000,delta}G
-left(e+rac{1001e^2}{delta}ight)I.
]

This is exactly the lower matrix verified by the terminal checker.
The inequality direction agrees with the already audited Active-Set Schur
theorem and was independently calibrated at (B).

## 5. Rational preconditioner is a witness, not an assumption

The stored lower-triangular rational matrix (P) is not trusted for its
origin. The checker reconstructs the directed lower matrix (L) and computes
[
B=PLP^T
]
with Arb interval arithmetic.

For every row it proves
[
B_{ii}-sum_{j
e i}|B_{ij}|>rac9{10}.
]

Hence (Bsucc(9/10)I). This also forces (P) to be invertible. The
additional directed LDL run after subtracting (9/10,I) produces all
191 positive pivots in each parity.

If (operatorname{tr}(PP^T)sigma<9/10), then
[
Lsucceqsigma I.
]
The checker verifies this inequality for the stored (sigma). Thus the
preconditioner is merely a verified congruence witness and cannot inject a
sign assumption.

## 6. Physical norm and defect conversion

The complete coupling bound yields
[
|D^{-1}C|^2<169,
]
so the triangular square-completion shear has norm factor below
[
(1+13)^2=196.
]

The exact Mellin correction has reference norm factor (1+eta<2).
Consequently, since the Schur reserve is far smaller than (delta),
[
q_1[u]
ge
rac{sigma}{392}|u|_2^2.
]

The checked stored reserves imply an all-parity physical lower bound
[
q_1[u]>10^{-26}|u|_2^2
]
for every nonzero admissible two-Mellin source.

By exact zero-extension form naturality, the same fixed-horizon statement
propagates to smaller windows (0<ale1).

For the C1 defect candidate, the previously audited envelope constant satisfies
[
s=kappa+2omega<rac{23}{2}.
]
Hence a physical gap (arepsilon=10^{-26}) gives
[
I-R_1^*R_1
succeq
rac{arepsilon}{23/2+arepsilon}I
>
10^{-28}I.
]
In particular
[
|R_1^p|<1
]
in both parities. The previously proved nesting/monotonicity gives the same
strict contraction on the fixed horizon.

## 7. Audit conclusion and scope

The release conditions introduced after the failed floating-point preflight
are satisfied for the terminal fixed-horizon theorem:

1. same-engine (B) calibration: PASS;
2. directed endpoint enclosure reproduces the known theorem: PASS;
3. fresh pinned `python-flint==0.9.0` terminal `--verify --recompute`: PASS;
4. complete A/G interval regeneration: PASS;
5. terminal High-floor derivation and enclosure direction: analytically
   consistent with the bound inputs and noncircular;
6. preconditioner and physical norm conversion: verified as consequence
   checks, not assumptions.

Therefore the package supports promotion of the fixed-horizon terminal result
to an **AUTHOR_DERIVED** reusable result while keeping
`EXTERNAL_REVIEW_OPEN`.

This audit does **not** establish:

- any horizon beyond (1);
- unrestricted-horizon C1 compatibility;
- a global/cofinal Weil test class;
- Strong Terminal in any broader historical sense;
- global Objekt X;
- global Weil positivity;
- RH.
