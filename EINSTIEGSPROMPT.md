# Einstiegsprompt — Neue Chat-Session

> **Aktueller Stand: 13. September 2026.**

Forschungsprogramm **Objekt X** im Repository `Waschtl904/objekt-x-programm`.

Arbeite als strenger mathematischer Auditor. ChatGPT übernimmt Repo-Arbeiten; externe Modelle sind Reviewer. Keine Promotion allein durch Merge, CI oder Numerik.

## Zuerst lesen

1. `CURRENT-FRONT.md`
2. `audits/P11_A1_HIGHFREQ_PROLATE_TAIL_2026-09-13.md`
3. `audits/P11_NP_DUAL_A1_MORSE_DIAGNOSTIC_2026-09-13.md`
4. `audits/P11_NP_DUAL_COMPLETION_SCREW_AUDIT_2026-09-13.md`
5. `audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md`
6. `00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md`
7. Registry/Arbeitsdefinition nur als unveränderte Governancequellen.

## Gesicherte A1-Struktur

```math
q_a=X_a^*X_a-\Gamma_aI,
\qquad
\mathcal E=(E_+,E_-),
\qquad
D_{NP}(a)=\ker\mathcal E.
```

Rank-2 Completion, Morse-Index-Filter, parity reduction und die kanonische Completion `lambda=1` sind `✓[M]`.

### Exact `a=1` Fourier multiplier `✓[M]`

```math
\boxed{
q_1(v)=\int_{\mathbb R}m_1(\xi)|\widehat v(\xi)|^2d\xi
}
```

für `supp(v) subset (-1,1)`, mit

```math
m_1(\xi)=
\operatorname{Re}\psi\left(\frac14+\frac{i\xi}{2}\right)-\log\pi
-2\sum_{n\in\{2,3,4,5,7\}}
\frac{\Lambda(n)}{\sqrt n}\cos(\xi\log n).
```

Kein zusätzlicher Fensterrest.

### Certified high-frequency / Prolate tail `✓[K/M]`

Exact-head Arb plus eine elementare Digamma-Untergrenze beweist

```math
m_1(\xi)>0.04\qquad(|\xi|\ge2300).
```

Karnik--Romberg--Davenport plus Arb liefert für den PSWF-Parameter `c=2300`

```math
\lambda_{1490}<0.0035.
```

Daher auf dem orthogonalen Prolate-Tail

```math
\boxed{
q_1(v)>0.01\|v\|^2.
}
```

Der unendlichdimensionale Tail ist damit bereits rigoros geschlossen.

## Default-Auftrag — A1-SCHUR

Setze

```math
A_1=q_1+\mathcal E^*\mathcal E
```

und zerlege

```math
L^2(-1,1)=R_{1490}\oplus T_{1490}.
```

Bewiesen ist

```math
A_{TT}>0.01I.
```

Zu beweisen bleibt

```math
\boxed{
A_{RR}-A_{RT}A_{TT}^{-1}A_{TR}\succeq0.
}
```

Arbeitsreihenfolge:

1. PSWF-resolved space `R_1490` parity-separieren (`745+745`).
2. Arb-zertifizierte `A_RR`-Matrix und Momentzeilen bauen.
3. `lambda=1` als predeclared Completion benutzen.
4. kleinste resolved Eigenwertuntergrenze `mu_R` zertifizieren.
5. `||A_RT||` rigoros einschließen.
6. sufficient Schur gate `||A_RT||^2 <= 0.01 mu_R` testen oder den vollen Schur-Komplement-Bound führen.
7. Nur bei geschlossenem Crossblock fixed-window `a=1` promoten.

### Firewalls

- PSWF basis diagonalizes concentration, not `q_1`.
- positive infinite tail alone does not prove `a=1` positivity.
- previous Dirichlet Ritz values remain non-certified.
- finite resolved PSD without crossblock is no theorem.
- fixed-window `a=1` is not RH-equivalent.
- all-a NP-GAP, Object X and RH remain open.
- Registry/Arbeitsdefinition unverändert.

## Status

```text
COMMON-JUMP / Q0                         ✓[M]
rank-2 completion / Morse / parity      ✓[M]
exact a=1 multiplier                     ✓[M]
high-frequency positivity               ✓[K/M]
full Prolate tail positivity            ✓[K/M]
resolved 1490-mode Arb block            ?[O]
resolved-tail crossblock                ?[O]
final a=1 Schur certificate             ?[O]
all-a NP-GAP                            ?[O]
forward Object-X architecture          ✓[M]_part
full positive Object-X / RH            ?[O]
```
