# Offene Probleme — A1-FINITE-1212 / LEGENDRE-CERT

> **Stand:** 13. September 2026.  
> Operative Audits: [A1 Omega1551](audits/P11_A1_OMEGA1551_REDUCTION_2026-09-13.md) · [A1 Legendre finite backend](audits/P11_A1_LEGENDRE_FINITE_CERTIFICATE_2026-09-13.md) · [A1 Legendre quadrature budget](audits/P11_A1_LEGENDRE_QUADRATURE_BUDGET_2026-09-13.md).

## Neu geschlossen

### `[A1-CROSS-1210]` `✓[K/M]`

KRD plus Arb liefert

```math
\lambda_{1210}(1551)<1.5\times10^{-42},
\qquad
\text{Schur penalty}<2.2\times10^{-39}.
```

Damit sind Infinite Tail und Crossblock der kanonischen PSWF-Route quantitativ absorbiert.

### `[A1-LEGENDRE-TAIL]` `✓[K/M]`

Die alternative orthonormale Legendre-Route mit `M=2150` besitzt einen rigorosen Tail-/Crossabschluss und reduziert auf zwei `1075 x 1075` Paritätsblöcke mit finite target `1e-35`.

### `[A1-LEGENDRE-QBUDGET]` `✓[K/M]`

Für die finale Legendre-Matrix ist nun ein konkreter Integrationsbackend zertifiziert:

```text
panel width <=0.4
Gauss-Legendre order 40
analytic strip |Im xi|<=0.4
```

Exact-Head Arb beweist

```math
|r(z)|<42
```

und

```math
\boxed{\|K-\widetilde K\|_{op}<4\times10^{-38}}
```

pro `1075 x 1075` Paritätsblock.

Die analytische Quadraturtrunkation ist damit nicht mehr der Engpass.

---

## Priorität 0A — `[A1-RESOLVED-3E39]` `?[O]`

Kanonische kleinere Route:

```math
\boxed{(L_1)_{RR}\succeq3\times10^{-39}I}
```

auf höchstens

```text
1212 total = 606 even + 606 odd
```

im moment-augmentierten PSWF-Raum.

`3e-39` ist ein vorab deklarierter sufficient threshold, kein beobachteter Eigenwert.

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
PSWF 1212-dimensional gate
          OR
Legendre two 1075x1075 blocks
          |
          v
canonical a=1 completion
```

Erst danach ist fixed-window `a=1` theorematisch geschlossen.

---

## Firewalls

- Legendre quadrature budget != finite PSD certificate.
- Special-function/Rounding-Fehler müssen separat eingeschlossen werden.
- Pivotintervalle mit `0` sind undecided.
- Die Legendre-Route ersetzt die kleinere PSWF-Route nicht.
- Fixed-window `a=1` ist noch nicht bewiesen.
- All-a NP-GAP, Object X und RH bleiben offen.
