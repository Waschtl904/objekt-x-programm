# Einstiegsprompt — Neue Chat-Session

> **Aktueller Stand: 13. September 2026.**

Forschungsprogramm **Objekt X** im Repository `Waschtl904/objekt-x-programm`.

Arbeite als strenger mathematischer Auditor. ChatGPT übernimmt Repo-Arbeiten; externe Modelle sind Reviewer. Keine Promotion allein durch Merge, CI oder Numerik.

## Zuerst lesen

1. `CURRENT-FRONT.md`
2. `audits/P11_A1_SCHUR_BOUNDED_REMAINDER_2026-09-13.md`
3. `audits/P11_A1_HIGHFREQ_PROLATE_TAIL_2026-09-13.md`
4. `audits/P11_NP_DUAL_COMPLETION_SCREW_AUDIT_2026-09-13.md`
5. `00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md`
6. Registry/Arbeitsdefinition nur als unveränderte Governancequellen.

## Gesicherte Kette

```text
COMMON-JUMP / Q0                         ✓[M]
rank-2 completion / Morse / parity      ✓[M]
canonical lambda=1                      ✓[M]
exact a=1 Fourier multiplier            ✓[M]
high-frequency positivity               ✓[K/M]
full infinite Prolate tail              ✓[K/M]
```

## Bounded Schur reduction `✓[M]`

Mit

```math
c=0.04,
\qquad
r=(m_1-c)\mathbf1_{[-2300,2300]},
```

ist

```math
q_1\succeq cI+K,
\qquad
K=P_I\mathcal F^{-1}M_r\mathcal F P_I.
```

Für die kanonische Completion genügt

```math
L_1=cI+K+\mathcal E^*\mathcal E.
```

Definiere für PSWFs `psi_k`

```math
R_N=
\operatorname{span}\{\psi_0,\ldots,\psi_{N-1}\}
+\operatorname{span}\{e^{x/2},e^{-x/2}\},
\qquad
T_N=R_N^\perp.
```

Dann

```math
\mathcal E|_{T_N}=0,
```

```math
\|(L_1)_{RT}\|
\le\|r\|_\infty\sqrt{\lambda_N},
```

und

```math
(L_1)_{TT}\succeq
[0.04-(\Gamma_1+0.04)\lambda_N]I.
```

## Predeclared N=1680 gate — exact-head CI pending

Der neue Arb-Workflow soll zertifizieren

```math
\|r\|_\infty<12,
\quad
\lambda_{1680}(2300)<1.1\times10^{-39},
```

```math
\tau_{1680}>0.039,
```

und

```math
\text{Schur penalty}<4.1\times10^{-36}.
```

Bis zum grünen Exact-Head-Lauf: candidate `✓[K/M]`.

## Default-Auftrag — A1-FINITE

Wenn der Cross-Gate grün ist, ist nur noch zu beweisen:

```math
\boxed{
(L_1)_{RR}\succeq5\times10^{-36}I
}
```

auf dem augmented resolved space `R_1680`.

Dimension höchstens:

```text
1682 total
841 even + 841 odd.
```

Arbeitsreihenfolge:

1. neue Cross-Arb-Werte verifizieren und promoten;
2. rigorose PSWF-Darstellung des resolved Raums wählen;
3. parity-getrennte finite Matrix von `L_1` intervallzertifizieren;
4. kleinste Eigenwertuntergrenze gegen `5e-36` prüfen;
5. nur bei bestandenem Gate fixed-window `a=1` promoten.

### Firewalls

- `5e-36` ist ein sufficient threshold, kein beobachteter Eigenwert.
- Keine Promotion der Crosszahlen vor Exact-Head-CI.
- Frühere Dirichlet-Ritzwerte bleiben Diagnostik.
- Fixed-window `a=1`, all-a NP-GAP, Object X und RH bleiben offen.
- Registry/Arbeitsdefinition unverändert.
