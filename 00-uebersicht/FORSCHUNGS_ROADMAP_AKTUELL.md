# Objekt X — kanonische Forschungsroadmap v3.7

> **Stand:** 13. September 2026; Registry und Arbeitsdefinition unverändert.

## Gate C0 — Gesicherte Architektur `✓[M]`

```text
COMMON-JUMP / Q0
rank-2 completion
Morse-index filters
reflection/parity reduction
canonical lambda=1 identity
```

Fixed-window Nullpolpositivität ist exakt ein zweikanaliges Completionproblem.

## Gate C1 — `a=1` exact multiplier `✓[M]`

Für zeitbegrenztes `v` auf `(-1,1)` gilt exakt

```math
q_1(v)=\int m_1(\xi)|\widehat v(\xi)|^2d\xi,
```

```math
m_1(\xi)=
\operatorname{Re}\psi\left(\frac14+\frac{i\xi}{2}\right)-\log\pi
-2\sum_{n\in\{2,3,4,5,7\}}
\frac{\Lambda(n)}{\sqrt n}\cos(\xi\log n).
```

Kein zusätzlicher Fensterrest tritt im quadratischen Wert auf.

## Gate C2 — High-frequency positivity `✓[K/M]`

Ein Exact-Head-Arb-Zertifikat beweist

```math
\boxed{m_1(\xi)>0.04\quad(|\xi|\ge2300).}
```

Die globale grobe Untergrenze lautet `m_1>=-Gamma_1`.

## Gate C3 — Prolate tail `✓[K/M]`

Für den Zeit-Band-Konzentrationsoperator auf `[-1,1]` mit Band `[-2300,2300]` ist `c=2300`.

Karnik--Romberg--Davenport Corollary 3 plus Arb liefert

```math
\boxed{\lambda_{1490}(2300)<0.0035.}
```

Daraus folgt für den orthogonalen Prolate-Tail

```math
\boxed{q_1(v)>0.01\|v\|^2\qquad(v\in T_{1490}).}
```

Damit ist der unendlichdimensionale Tail selbst geschlossen.

## Gate C4 — Parity-compatible finite reduction

Die ersten `1490` timelimitierten PSWF-Moden zerfallen in

```text
745 even + 745 odd.
```

Der Completionblock bleibt dadurch mit der bereits theorematischen even/odd Dualität kompatibel.

## Gate C5 — A1-SCHUR `?[O]`

Setze

```math
A_1=q_1+\mathcal E^*\mathcal E
```

und zerlege

```math
L^2(-1,1)=R_{1490}\oplus T_{1490}.
```

Bereits bewiesen:

```math
A_{TT}>0.01I.
```

Offen ist

```math
\boxed{
A_{RR}-A_{RT}A_{TT}^{-1}A_{TR}\succeq0.
}
```

Pflichten:

1. PSWF-resolved Formmatrix und Momentzeilen rigoros einschließen;
2. `lambda=1` zuerst testen;
3. finite Inertia/PSD zertifizieren;
4. `||A_RT||` rigoros einschließen;
5. finalen Schur-Komplement-Bound schließen.

Ein einfacher ausreichender Gate wäre

```math
A_{RR}\succeq\mu_RI,
\qquad
\|A_{RT}\|^2\le0.01\mu_R.
```

## Gate C6 — fixed-window `a=1` completion `?[O]`

Nur wenn C5 grün ist, wird

```text
certified a=1 null-pole completion
```

als theorematischer fixed-window Fortschritt gebucht. Der externe volle-Klasse-Benchmark von Marcus Chuk liegt derzeit bei `L=0.8`.

## Gate C7 — all-window mechanism `?[O]`

```text
A1-SCHUR
  |
fixed-a certificates / structural scaling
  |
all-a NP-GAP
  |
global restricted Weil criterion
  |
RH
```

## Auxiliary / Firewalls

- Frühere Dirichlet-Ritzwerte bleiben nicht zertifiziert.
- PSWFs diagonalieren den Konzentrationsoperator, nicht `q_1`.
- Tail positivity allein beweist `a=1` noch nicht.
- Kein finite resolved PSD ohne Crossblock-Schur als Theorem buchen.
- Registry/Arbeitsdefinition unverändert.
