# Einstiegsprompt — Neue Chat-Session

> **Aktueller Stand: 14. September 2026.**

Forschungsprogramm **Objekt X** im Repository `Waschtl904/objekt-x-programm`.

Arbeite als strenger mathematischer Auditor. ChatGPT übernimmt Repo-Arbeiten; externe Modelle sind Reviewer. Keine Promotion allein durch Merge, CI oder Numerik.

## Zuerst lesen

1. `CURRENT-FRONT.md`
2. `audits/P11_A1_OSIPOV1102_REDUCTION_2026-09-14.md`
3. `audits/P11_A1_OMEGA1551_REDUCTION_2026-09-13.md`
4. `audits/P11_A1_LEGENDRE_QUADRATURE_BUDGET_2026-09-13.md`
5. `audits/P11_A1_LEGENDRE_FINITE_CERTIFICATE_2026-09-13.md`
6. Registry/Arbeitsdefinition nur als unveränderte Governancequellen.

## Gesicherte Kette

```text
COMMON-JUMP / Q0                         ✓[M]
rank-2 completion / Morse / parity      ✓[M]
canonical lambda=1                      ✓[M]
exact a=1 Fourier multiplier            ✓[M]
Omega1551 high-frequency floor          ✓[K/M]
```

## Kanonischer finite Gate — PSWF / Osipov

Osipov Theorem 4 liefert für den finite-Fourier-Eigenwert

```math
|\lambda_n^F|\le
\frac{\sqrt\pi\,c^n(n!)^2}{(2n)!\Gamma(n+3/2)},
```

und damit für die Konzentration

```math
\mu_n=\frac{c}{2\pi}|\lambda_n^F|^2.
```

Für die vorab festgelegten Werte

```text
c=1551,
N=1102
```

hat der Arb-Gate bereits auf dem aktuellen Main-basierten Head zertifiziert

```math
\mu_{1102}<10^{-43},
\qquad
\tau_{1102}>0.099,
```

```math
\text{Schur penalty}<1.5\times10^{-40}.
```

Nach dem finalen Exact-Head-Rerun genügt kanonisch nur noch

```math
\boxed{(L_1)_{RR}\succeq3\times10^{-39}I}
```

auf höchstens

```text
1104 total = 552 even + 552 odd.
```

Der PSWF-Tail wird durch Osipovs analytischen Eigenwertbound kontrolliert; dafür müssen keine PSWF-Eigenvektoren numerisch konstruiert werden.

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

PR #118 zertifiziert zusätzlich für jeden Paritätsblock

```math
\boxed{\|K-\widetilde K\|_{op}<4\times10^{-38}.}
```

Die Legendre-Route bleibt ein unabhängiger, basisexpliziter Backup-/Crosscheck-Backend; die kleinere PSWF-/Osipov-Route bleibt kanonisch.

## Default-Auftrag nach Abschluss von Durchlauf A

**Nicht in diesem Durchlauf ausführen:**

1. finite resolved Darstellung für die kanonische `<=1104`-Route festlegen;
2. parity-getrennte `552 x 552`-Zertifikatsstrategie wählen;
3. Arb/LDL/Cholesky mit adaptiver Präzision und fail-closed Pivots entwerfen;
4. alternativ den bereits vorbereiteten Legendre-Backend weiterführen;
5. fixed-window `a=1` nur bei vollständigem finite PSD-Gate promoten.

### Firewalls

- Osipov-Numerik erst nach finalem Exact-Head-Rerun dauerhaft promoten.
- Float-Cholesky oder Float-Eigenwerte haben keinen Beweisstatus.
- `3e-39` und `1e-35` sind predeclared sufficient targets, keine beobachteten Eigenwerte.
- Fixed-window `a=1`, all-a NP-GAP, Object X und RH bleiben offen.
- Aktuelle arXiv-v2-Metadaten von 2608.24827 führen Xuefeng Zhu als Autor.
- Registry/Arbeitsdefinition unverändert.
