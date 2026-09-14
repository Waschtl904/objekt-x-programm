# Offene Probleme — A1-FINITE-1104 / LEGENDRE-CERT

> **Stand:** 14. September 2026.  
> Operative Audits: [A1 Omega1551](audits/P11_A1_OMEGA1551_REDUCTION_2026-09-13.md) · [A1 Osipov N1102](audits/P11_A1_OSIPOV1102_REDUCTION_2026-09-14.md) · [A1 Legendre finite backend](audits/P11_A1_LEGENDRE_FINITE_CERTIFICATE_2026-09-13.md) · [A1 Legendre quadrature budget](audits/P11_A1_LEGENDRE_QUADRATURE_BUDGET_2026-09-13.md).

## Neu geschlossen

### `[A1-OSIPOV-1102]` candidate `✓[K/M]` bis finaler Exact-Head-Rerun

Osipov Theorem 4 gibt für den finite-Fourier-Eigenwert

```math
|\lambda_n^F|\le
\nu(n,c)=
\frac{\sqrt\pi\,c^n(n!)^2}{(2n)!\Gamma(n+3/2)}.
```

Für die Konzentration gilt

```math
\mu_n=\frac{c}{2\pi}|\lambda_n^F|^2.
```

Der bereits grüne Arb-Gate auf dem aktuellen Main-basierten Head liefert bei

```text
c=1551,
N=1102
```

```math
\mu_{1102}<10^{-43},
\qquad
\tau_{1102}>0.099,
```

und

```math
\boxed{\text{Schur penalty}<1.5\times10^{-40}.}
```

Der tatsächliche Intervall-Upper-Bound des Penalty liegt bei etwa `1.229e-40`.

Nach der letzten Navigationsänderung wird diese Numerik erst nach dem erneuten finalen Exact-Head-Lauf fest auf `✓[K/M]` gebucht.

### `[A1-LEGENDRE-TAIL]` `✓[K/M]`

Die alternative orthonormale Legendre-Route mit `M=2150` besitzt einen rigorosen Tail-/Crossabschluss und reduziert auf zwei `1075 x 1075` Paritätsblöcke mit finite target `1e-35`.

### `[A1-LEGENDRE-QBUDGET]` `✓[K/M]`

Exact-Head Arb zertifiziert für jeden `1075 x 1075` Legendre-Paritätsblock

```math
\boxed{\|K-\widetilde K\|_{op}<4\times10^{-38}.}
```

Die analytische Quadraturtrunkation ist damit nicht mehr der Engpass.

---

## Priorität 0A — `[A1-RESOLVED-3E39]` `?[O]`

Nach final grünem Osipov-Gate ist die kanonische kleinere Route:

```math
\boxed{(L_1)_{RR}\succeq3\times10^{-39}I}
```

auf höchstens

```text
1104 total = 552 even + 552 odd
```

im moment-augmentierten PSWF-Raum.

`3e-39` ist ein vorab deklarierter sufficient threshold, kein beobachteter Eigenwert.

Keine numerische Konstruktion der PSWF-Eigenvektoren ist für die Osipov-Tail-Schranke nötig.

---

## Priorität 0B — `[A1-LEGENDRE-MATRIX]` `?[O]`

Alternative basisexplizite Zertifikatsroute:

```math
\boxed{
A_e\succeq10^{-35}I,
\qquad
A_o\succeq10^{-35}I
}
```

für zwei orthonormale Legendre-Blöcke `1075 x 1075`.

Bereits geschlossen:

- Gram `G=I` exakt;
- Parität exakt;
- Legendre Tail/Cross `✓[K/M]`;
- analytischer Quadratur-Operatorfehler `<4e-38` `✓[K/M]`.

Noch zu schließen:

1. Matrixassemblierung mit genügend Arbeitspräzision;
2. Special-function/Rounding-Enclosures;
3. verifizierte LDL/Cholesky-/Inertia-Prüfung;
4. vollständiges Residual/Weyl-Budget gegen den Shift `1e-35`.

Ein numerischer positiver Eigenwert oder Float-Cholesky genügt nicht.

---

## Danach — `[A1-CERT]` `?[O]`

**Eine** der beiden endlichen Routen genügt:

```text
PSWF <=1104-dimensional gate
          OR
Legendre two 1075x1075 blocks
          |
          v
canonical a=1 completion
```

Erst danach ist fixed-window `a=1` theorematisch geschlossen.

---

## Firewalls

- Osipov-Numerik erst nach finalem Exact-Head-Rerun dauerhaft promoten.
- Legendre quadrature budget != finite PSD certificate.
- Special-function/Rounding-Fehler müssen separat eingeschlossen werden.
- Pivotintervalle mit `0` sind undecided.
- Die Legendre-Route ersetzt die kleinere PSWF-Route nicht.
- Fixed-window `a=1` ist noch nicht bewiesen.
- All-a NP-GAP, Object X und RH bleiben offen.
