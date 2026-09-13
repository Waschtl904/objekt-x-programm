# Einstiegsprompt — Neue Chat-Session

> **Aktueller Stand: 13. September 2026.**

Forschungsprogramm **Objekt X** im Repository `Waschtl904/objekt-x-programm`.

Arbeite als strenger mathematischer Auditor. ChatGPT übernimmt Repo-Arbeiten; externe Modelle sind Reviewer. Keine Promotion allein durch Merge, CI oder Numerik.

## Zuerst lesen

1. `CURRENT-FRONT.md`
2. `audits/P11_A1_OMEGA1551_REDUCTION_2026-09-13.md`
3. `audits/P11_A1_SCHUR_BOUNDED_REMAINDER_2026-09-13.md`
4. `audits/P11_A1_HIGHFREQ_PROLATE_TAIL_2026-09-13.md`
5. `audits/P11_NP_DUAL_COMPLETION_SCREW_AUDIT_2026-09-13.md`
6. Registry/Arbeitsdefinition nur als unveränderte Governancequellen.

## Gesicherte Kette

```text
COMMON-JUMP / Q0                         ✓[M]
rank-2 completion / Morse / parity      ✓[M]
canonical lambda=1                      ✓[M]
exact a=1 Fourier multiplier            ✓[M]
Omega1551 high-frequency floor          ✓[K/M]
N=1210 Prolate/Schur reduction          ✓[K/M]
```

## Certified reduced band

```math
\boxed{m_1(\xi)>0.1\quad(|\xi|\ge1551).}
```

Mit

```math
r=(m_1-0.1)\mathbf1_{[-1551,1551]}
```

ist

```math
\|r\|_\infty<12.
```

Für den moment-augmentierten PSWF-Raum

```math
R_N=
\operatorname{span}\{\psi_0,\ldots,\psi_{N-1}\}
+\operatorname{span}\{e^{x/2},e^{-x/2}\}
```

liefert `N=1210`

```math
\lambda_{1210}<1.5\times10^{-42},
```

und den zertifizierten Schur-Penalty

```math
<2.2\times10^{-39}.
```

## Default-Auftrag — A1-FINITE-1212

Es bleibt nur noch zu beweisen:

```math
\boxed{
(L_1)_{RR}\succeq3\times10^{-39}I.
}
```

Resolved dimension höchstens:

```text
1212 total
606 even + 606 odd.
```

Arbeitsreihenfolge:

1. rigorose Darstellung des augmented PSWF-Raums wählen;
2. parity-getrennte finite Matrix von `L_1` intervallzertifizieren;
3. kleinste Eigenwertuntergrenze gegen `3e-39` prüfen;
4. nur bei bestandenem Gate fixed-window `a=1` promoten.

### Firewalls

- `3e-39` ist ein vorab deklarierter sufficient threshold, kein beobachteter Eigenwert.
- Der ältere `2300/1680`-Gate bleibt gültig, ist aber gröber.
- Frühere Dirichlet-Ritzwerte bleiben Diagnostik.
- Fixed-window `a=1`, all-a NP-GAP, Object X und RH bleiben offen.
- Aktuelle arXiv-v2-Metadaten von 2608.24827 führen Xuefeng Zhu als Autor; ältere Projekttexte mit Marcus Chuk sind bibliographisch superseded.
- Registry/Arbeitsdefinition unverändert.
