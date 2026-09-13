# Einstiegsprompt — Neue Chat-Session

> **Aktueller Stand: 13. September 2026.**

Forschungsprogramm **Objekt X** im Repository `Waschtl904/objekt-x-programm`.

Arbeite als strenger mathematischer Auditor. ChatGPT übernimmt Repo-Arbeiten; externe Modelle sind Reviewer. Keine Promotion allein durch Merge, CI oder Numerik.

## Zuerst lesen

1. `CURRENT-FRONT.md`
2. `audits/P11_A1_LEGENDRE_QUADRATURE_BUDGET_2026-09-13.md`
3. `audits/P11_A1_LEGENDRE_FINITE_CERTIFICATE_2026-09-13.md`
4. `audits/P11_A1_OMEGA1551_REDUCTION_2026-09-13.md`
5. `audits/P11_A1_SCHUR_BOUNDED_REMAINDER_2026-09-13.md`
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

## Kanonischer finite Gate — PSWF

Es genügt

```math
\boxed{(L_1)_{RR}\succeq3\times10^{-39}I}
```

auf höchstens

```text
1212 total = 606 even + 606 odd.
```

Diese kleinere PSWF-Route bleibt die kanonische Beweisobligation.

## Alternative explizite Backend — Legendre

Mit

```math
T_n(x)=\sqrt{n+\frac12}P_n(x),
\qquad n=0,\ldots,2149,
```

ist die Basis orthonormal, `G=I`, und die beiden finite Blöcke haben Dimension

```text
1075 even + 1075 odd.
```

PR #117 zertifiziert Tail/Cross und setzt den finite target

```math
10^{-35}I.
```

### Neu geschlossen: Quadraturbudget `✓[K/M]`

Predeclared:

```text
panel width <=0.4
Gauss-Legendre q=40
analytic strip |Im xi|<=0.4
```

Exact-Head Arb zertifiziert

```math
|r(z)|<42
```

und für jeden Paritätsblock

```math
\boxed{\|K-\widetilde K\|_{op}<4\times10^{-38}.}
```

Der analytische Quadraturfehler liegt damit >250-fach unter `1e-35`.

## Default-Auftrag — LEGENDRE-MATRIX

Baue den **vollständig verifizierten** finalen Matrix-Gate:

1. beide `1075 x 1075` Paritätsmatrizen mit ausreichend hoher Präzision assemblieren;
2. sphärische Bessel-/Digamma-/Momentwerte interval-zertifizieren;
3. zusätzlich zum bereits geschlossenen `<4e-38` Quadraturbudget ein `eps_eval` für Special-function/Rounding bestimmen;
4. `A_even-1e-35 I` und `A_odd-1e-35 I` mit Arb-LDL/Cholesky oder gleichwertiger rigoroser Inertia-Methode prüfen;
5. Pivotintervalle, die `0` enthalten, als **undecided** behandeln und Präzision adaptiv erhöhen;
6. Residual/Weyl-Budget explizit dokumentieren;
7. nur wenn beide Paritätsblöcke grün sind, `a=1` promoten.

Parallel darf die kleinere PSWF-1212-Route weiterverfolgt werden; die Legendre-Route ersetzt sie nicht.

### Firewalls

- Quadrature budget != finite PSD.
- Float-Cholesky oder Float-Eigenwerte haben keinen Beweisstatus.
- `1e-35` ist ein predeclared sufficient target, kein beobachteter Eigenwert.
- Fixed-window `a=1`, all-a NP-GAP, Object X und RH bleiben offen.
- Aktuelle arXiv-v2-Metadaten von 2608.24827 führen Xuefeng Zhu als Autor.
- Registry/Arbeitsdefinition unverändert.
