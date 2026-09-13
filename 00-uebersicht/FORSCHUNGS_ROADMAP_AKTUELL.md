# Objekt X — kanonische Forschungsroadmap v3.9

> **Stand:** 13. September 2026; Registry und Arbeitsdefinition unverändert.

## Gate C0 — Gesicherte Completionstruktur `✓[M]`

```text
COMMON-JUMP / Q0
rank-2 completion / Morse / parity
canonical lambda=1
exact a=1 Fourier multiplier
moment-augmented Prolate Schur theorem
```

## Gate C1 — Sharpened high-frequency band `✓[K/M]`

Exact-head Arb zertifiziert

```math
\boxed{m_1(\xi)>0.1\quad(|\xi|\ge1551).}
```

Der Beweis benutzt eine rigorose Gitter-/Lipschitzkontrolle auf `[1551,2500]` und einen monotonen far-field Digamma-Bound.

## Gate C2 — Reduced bounded lower operator `✓[M] / ✓[K/M]`

```math
c=0.1,
\quad
r=(m_1-c)1_{[-1551,1551]},
\quad
K=P_I\mathcal F^{-1}M_r\mathcal F P_I,
```

```math
q_1\succeq cI+K.
```

Arb zertifiziert

```math
\|r\|_\infty<12.
```

## Gate C3 — Moment-augmented PSWF split `✓[M]`

```math
R_N=\operatorname{span}\{\psi_0,\ldots,\psi_{N-1}\}
+\operatorname{span}\{e^{x/2},e^{-x/2}\},
\qquad
T_N=R_N^\perp.
```

Dann `E|T_N=0` und

```math
\|(L_1)_{RT}\|\le\|r\|_\infty\sqrt{\lambda_N},
```

```math
(L_1)_{TT}\succeq
[c-(\Gamma_1+c)\lambda_N]I.
```

## Gate C4 — Certified N=1210 Schur constants `✓[K/M]`

Für `c_PSWF=1551`:

```math
\lambda_{1210}<1.5\times10^{-42},
```

```math
\tau_{1210}>0.099,
```

```math
\boxed{\text{Schur penalty}<2.2\times10^{-39}.}
```

Der Exact-Head-Upper-Bound des Penalty ist etwa `2.11526e-39`.

## Gate C5 — A1-FINITE-1212 `?[O]`

Es genügt jetzt nur noch

```math
\boxed{
(L_1)_{RR}\succeq3\times10^{-39}I.
}
```

Resolved dimension:

```text
at most 1212 total
606 even + 606 odd.
```

`3e-39` wurde vor resolved-space Numerik festgelegt und ist kein gemessener Eigenwert.

## Gate C6 — certified a=1 completion `?[O]`

C5 plus der bereits zertifizierte Schur-Penalty ergibt die volle kanonische Completion bei `a=1` und damit Nullpolpositivität in diesem Fenster.

## Gate C7 — all-window mechanism `?[O]`

Erst danach:

```text
a=1 fixed-window theorem
  |
further windows / structural scaling
  |
all-a NP-GAP
  |
RH-hard global criterion.
```

## Firewalls

- Der ältere `2300/1680`-Gate bleibt gültig, ist aber gröber.
- `3e-39` ist ein sufficient threshold, kein beobachteter Eigenwert.
- Resolved lower bound bleibt offen.
- Fixed-window `a=1`, Object X und RH sind nicht bewiesen.
- Registry/Arbeitsdefinition unverändert.
