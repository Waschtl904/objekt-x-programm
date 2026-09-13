# Einstiegsprompt — Neue Chat-Session

> **Aktueller Stand: 13. September 2026.**

Forschungsprogramm **Objekt X** im Repository `Waschtl904/objekt-x-programm`.

Arbeite als strenger mathematischer Auditor. ChatGPT übernimmt Repo-Arbeiten; externe Modelle sind Reviewer. Keine Promotion allein durch Merge, CI oder Numerik.

## Zuerst lesen

1. `CURRENT-FRONT.md`
2. `audits/P11_NP_DUAL_A1_MORSE_DIAGNOSTIC_2026-09-13.md`
3. `audits/P11_NP_DUAL_COMPLETION_SCREW_AUDIT_2026-09-13.md`
4. `audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md`
5. `00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md`
6. Registry und Objekt-X-Arbeitsdefinition nur als unverändert gültige Governancequellen.

## Aktueller Kern

```math
q_a=X_a^*X_a-\Gamma_a I,
\qquad
\mathcal E=(E_+,E_-),
\qquad
D_{NP}(a)=\ker\mathcal E.
```

Volle lokale Weilform:

```math
Q_W^a=q_a+\mathcal E^*P\mathcal E,
\qquad
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
```

### Exact dual completion `✓[M]`

Strict:

```math
\boxed{
q_a\ge\delta I\text{ on }\ker E
\iff
\exists\lambda,\mu>0:
q_a+\lambda E^*E\succeq\mu I.
}
```

Semidefinite:

```math
\boxed{
q_a\ge0\text{ on }\ker E
\iff
\forall\varepsilon>0\ \exists\lambda_\varepsilon>0:
q_a+\varepsilon I+\lambda_\varepsilon E^*E\succeq0.
}
```

### Morse filters `✓[M]`

```math
q_a+E^*HE\succeq0
\Longrightarrow
n_-(q_a)\le n_+(H)\le2.
```

For the physical pole matrix `P`, `n_+(P)=1`, hence

```math
Q_W^a\succeq0\Longrightarrow n_-(q_a)\le1.
```

A certified third negative direction of `q_a` falsifies any rank-2 NP completion; a certified second negative direction rules out the physical `P`-completion.

### Parity reduction `✓[M]`

Reflection symmetry allows every Hermitian completion to be reduced to

```math
H=\begin{pmatrix}\alpha&\beta\\\beta&\alpha\end{pmatrix},
```

or two real even/odd dual parameters.

In that basis

```math
P\sim\operatorname{diag}(+1,-1).
```

Under physical Weil positivity, the odd sector of `q_a` is nonnegative and any negative direction must be even.

### Canonical first candidate

```math
\boxed{
q_a+E^*E
=Q_W^a+E^*(I-P)E,
\qquad I-P\succeq0.
}
```

Therefore `lambda=1` is the first predeclared scalar completion candidate.

### Literaturkorrekturen

- The pole-cleared discrepancy is not a new arithmetic object; it is the Prime+Polar derivative block of Suzuki's screw function.
- arXiv:2608.24827 (*Weil positivity in compact windows: certified two-sided bounds and a Landau--Widom decay law*) is by **Marcus Chuk**, not Xuefeng Zhu.
- Chuk certifies full-class positivity at `L=0.8` with lower bound `8.9e-18`; a fixed-window extension should therefore target `a>0.8`.

## Current diagnostic at `a=1` — no status

Predeclared Dirichlet basis

```math
\phi_n(x)=\sin\left(\frac{n\pi(x+1)}2\right),
\qquad -1<x<1.
```

Observed null-pole finite Ritz minima:

```text
N=4    ~8.22e-4
N=6    ~6.21e-7
N=8    ~3.26e-9
N=10   ~2.70e-9
N=12   ~6.67e-11
```

At `N=12`, the finite full `q_1` block showed one negative numerical direction, in the even sector, and the scalar completion crossed numerical PSD at `lambda≈1`.

**No Arb matrix enclosure and no tail: diagnostic only.**

## Default-Auftrag — A1-CERT

Versuche einen rigorosen Completion-Certificate bei

```text
a=1.0.
```

Pflichtreihenfolge:

1. parity-adaptierte Basis/Trunkierung **vor** Resultat festlegen;
2. Arb-enclosed Formmatrix und `E_±`-Momentzeilen bauen;
3. `lambda=1` zuerst testen; erst danach zwei reflection-symmetrische dual parameters optimieren;
4. finite inertia / PSD intervallzertifizieren;
5. rigorous lower bound for unresolved even/odd tails;
6. rigorous resolved-tail coupling estimate;
7. final Schur complement;
8. nur wenn 4--7 zusammen grün sind: fixed-window theorem promoten.

### Firewalls

- finite Ritz/SDP PSD ohne tail ist kein Beweis;
- die aktuellen `a=1` Zahlen sind nicht zertifiziert;
- `a<=0.8` wäre keine Erweiterung des Marcus-Chuk-Benchmarks;
- scalar Turán failure falsifiziert NP-GAP nicht;
- existence of arbitrary completion != physical pole matrix `P`;
- all-a completion ist RH-hart;
- Registry/Arbeitsdefinition unverändert.

## Status

```text
COMMON-JUMP / Q0                         ✓[M]
Suzuki screw redundancy                 ✓[M]
D as new arithmetic object             ×[M]
scalar Turan exactness                  ×[M]
rank-2 completion duality              ✓[M]
Morse filters                           ✓[M]
parity-reduced 2-parameter dual         ✓[M]
canonical lambda=1 identity             ✓[M]
a=1 finite diagnostic                  non-certified
rigorous a=1 tail / Schur complement   ?[O]
certified a=1 completion               ?[O]
all-a NP-GAP                            ?[O]
forward Object-X architecture          ✓[M]_part
full positive Object-X / RH            ?[O]
```
