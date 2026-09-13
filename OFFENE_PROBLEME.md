# Offene Probleme — A1-SCHUR

> **Stand:** 13. September 2026.  
> Operative Audits: [NP-DUAL-COMP](audits/P11_NP_DUAL_COMPLETION_SCREW_AUDIT_2026-09-13.md) · [A1-TAIL](audits/P11_A1_HIGHFREQ_PROLATE_TAIL_2026-09-13.md).

## Neu geschlossen

### `[A1-FOURIER]` `✓[M]`

Bei `a=1` besitzt `q_1` exakt den ganzen Fouriermultiplikator

```math
m_1(\xi)=
\operatorname{Re}\psi\left(\frac14+\frac{i\xi}{2}\right)-\log\pi
-2\sum_{n\in\{2,3,4,5,7\}}
\frac{\Lambda(n)}{\sqrt n}\cos(\xi\log n).
```

Für zeitbegrenztes `v` gilt ohne zusätzlichen Fensterrest

```math
q_1(v)=\int m_1(\xi)|\widehat v(\xi)|^2d\xi.
```

### `[A1-HIGHFREQ]` `✓[K/M]`

Der Exact-Head-Arb-Gate zertifiziert

```math
\boxed{m_1(\xi)>0.04\quad(|\xi|\ge2300).}
```

### `[A1-PROLATE-TAIL]` `✓[K/M]`

Für das Band `[-2300,2300]` auf dem Zeitintervall `[-1,1]` gilt `c=2300`. Die explizite Karnik--Romberg--Davenport-Schranke liefert intervallrigoros

```math
\boxed{\lambda_{1490}(2300)<0.0035.}
```

Daraus folgt auf dem gesamten orthogonalen Prolate-Tail

```math
\boxed{
q_1(v)>0.01\|v\|^2.
}
```

Der unendlichdimensionale Tail selbst ist damit geschlossen.

### `[PARITY-TAIL]` `✓[M]`

Die ersten `1490` PSWF-Moden zerfallen in `745` even und `745` odd Moden. Die Tailzerlegung ist mit der theorematischen parity-completion kompatibel.

---

## Priorität 0 — `[A1-SCHUR]` `?[O]`

Für die kanonische Completion

```math
A_1=q_1+\mathcal E^*\mathcal E
```

und

```math
L^2(-1,1)=R_{1490}\oplus T_{1490}
```

ist bereits

```math
A_{TT}>0.01I
```

bewiesen.

Zu schließen ist nur noch

```math
\boxed{
A_{RR}-A_{RT}A_{TT}^{-1}A_{TR}\succeq0.
}
```

### Pflichten

1. resolved PSWF-Formmatrix `A_RR` rigoros/Arb einschließen;
2. Momentzeilen in der PSWF-Basis einschließen;
3. `lambda=1` als ersten predeclared Completionwert benutzen;
4. resolved Inertia und kleinste Eigenwertuntergrenze zertifizieren;
5. `||A_RT||` rigoros begrenzen;
6. finalen Schur-Komplement-Gate schließen.

Ein einfacher sufficient gate ist

```math
A_{RR}\succeq\mu_R I,
\qquad
\|A_{RT}\|^2\le0.01\mu_R.
```

---

## Priorität 1 — `[A1-RESOLVED]` `?[O]`

Die neue finite Größe ist `1490 x 1490`, parity-getrennt `745 x 745` pro Sektor.

Zu entscheiden:

- direkte Arb-Quadratur der PSWF-Matrixelemente;
- zertifizierte Spektralmethode für die PSWFs;
- alternativ eine basisunabhängige resolved-space Untergrenze, die den vollen Matrixbau vermeidet.

Die früheren 12-dimensionalen Dirichlet-Ritzwerte sind hierfür nur Diagnostik.

---

## Priorität 2 — `[A1-CROSS]` `?[O]`

Gesucht ist eine normierte Schranke für den resolved--tail Block. Prolate diagonalisiert nur den Bandkonzentrationsoperator, nicht `q_1`; daher muss die Kopplung separat kontrolliert werden.

Mögliche Mechanismen:

- split `m_1=m_{in}+m_{out}` und nutze PSWF band-concentration identities;
- subtractiere einen positiven Außenboden `0.04` und schätze nur den verbleibenden bounded multiplier;
- parity-separierte Hilbert--Schmidt-/Schur-Bounds, sofern endlich;
- graph norm statt bloßer `L^2`-Norm, falls `m_1` unbeschränkt wächst.

---

## Danach — `[A1-CERT]` `?[O]`

Wenn `A1-SCHUR` grün ist, folgt ein rigoroses fixed-window Nullpol-Completion-Zertifikat bei `a=1`.

Erst danach lohnt sich die Frage nach Skalierung in `a` oder weiteren Fenstern.

---

## Firewalls

- positive high-frequency symbol alone != full positivity;
- Prolate tail positivity != resolved block positivity;
- PSWF basis diagonalizes concentration, not `q_1`;
- finite resolved PSD without crossblock != theorem;
- previous finite Dirichlet diagnostics remain non-certified;
- fixed-window `a=1` != RH;
- all-a NP-GAP, Object X and RH remain open.
