# Offene Probleme — A1-FINITE

> **Stand:** 13. September 2026.  
> Operative Audits: [A1-TAIL](audits/P11_A1_HIGHFREQ_PROLATE_TAIL_2026-09-13.md) · [A1 bounded Schur remainder](audits/P11_A1_SCHUR_BOUNDED_REMAINDER_2026-09-13.md).

## Neu geschlossen

### `[A1-TAIL]` `✓[K/M]`

Der gesamte unendlichdimensionale Prolate-Tail ist bereits positiv:

```math
q_1>0.01I
```

auf dem orthogonalen Komplement der ersten `1490` PSWF-Moden.

### `[A1-BOUNDED-LOWER]` `✓[M]`

Mit `c=0.04` und

```math
r=(m_1-c)\mathbf1_{[-2300,2300]}
```

ist

```math
q_1\succeq cI+K,
\qquad
K=P_I\mathcal F^{-1}M_r\mathcal F P_I.
```

Für `A_1=q_1+E^*E` genügt also `L_1=cI+K+E^*E`.

### `[A1-MOMENT-AUGMENT]` `✓[M]`

```math
R_N=\operatorname{span}\{\psi_0,\ldots,\psi_{N-1}\}
+\operatorname{span}\{e^{x/2},e^{-x/2}\},
\qquad
T_N=R_N^\perp.
```

Dann `E|T_N=0`; der Completionterm hat keinen Tail-/Crossblock.

### `[A1-CROSS-ABSTRACT]` `✓[M]`

```math
\|(L_1)_{RT}\|
\le\|r\|_\infty\sqrt{\lambda_N},
```

```math
(L_1)_{TT}\succeq
\tau_NI,
\qquad
\tau_N=0.04-(\Gamma_1+0.04)\lambda_N.
```

Daher genügt

```math
(L_1)_{RR}\succeq\mu_RI,
\qquad
\mu_R\ge\frac{\|r\|_\infty^2\lambda_N}{\tau_N}.
```

---

## Priorität 0 — `[A1-CROSS-1680]` candidate `✓[K/M]`

Vorab festgelegter exact-head Gate:

```text
Omega = 2300
N = 1680
c = 0.04
```

Zu zertifizieren:

```math
\|r\|_\infty<12,
\quad
\lambda_{1680}<1.1\times10^{-39},
```

```math
\tau_{1680}>0.039,
\quad
\text{Schur penalty}<4.1\times10^{-36}.
```

Bis zum grünen CI-Lauf keine strenge Numerikpromotion.

---

## Priorität 1 — `[A1-RESOLVED-5E36]` `?[O]`

Wenn der Cross-Gate grün ist, ist **nur noch** zu beweisen:

```math
\boxed{
(L_1)_{RR}\succeq5\times10^{-36}I.
}
```

Resolved dimension höchstens

```text
1682 total
841 even + 841 odd.
```

Pflichten:

1. rigorose Darstellung des augmented PSWF-Raums;
2. Arb-Einschließung der finite Formmatrix;
3. parity-getrennte Inertia/PSD;
4. lower eigenvalue bound `>=5e-36`.

`5e-36` ist ein **vorab deklarierter sufficient threshold**, kein beobachteter Eigenwert.

---

## Danach — `[A1-CERT]` `?[O]`

Resolved lower bound + zertifizierter Schur-Penalty ergibt die volle kanonische Completion bei `a=1`.

Erst dann ist ein fixed-window theorem erreicht.

---

## Firewalls

- Cross-Konstanten erst nach exact-head CI promoten.
- resolved lower bound ist offen.
- vorherige 12-dimensionale Ritzwerte bleiben Diagnostik.
- fixed-window `a=1` ist noch nicht bewiesen.
- all-a NP-GAP, Object X und RH bleiben offen.
