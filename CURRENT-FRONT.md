# CURRENT FRONT — Objekt X / A1-FINITE-1212

> **Stand:** 13. September 2026; Registry und Objekt-X-Arbeitsdefinition unverändert.  
> **Hauptaudits:** [A1 Omega1551](audits/P11_A1_OMEGA1551_REDUCTION_2026-09-13.md) · [A1 bounded Schur remainder](audits/P11_A1_SCHUR_BOUNDED_REMAINDER_2026-09-13.md) · [A1-TAIL](audits/P11_A1_HIGHFREQ_PROLATE_TAIL_2026-09-13.md) · [NP-DUAL-COMP](audits/P11_NP_DUAL_COMPLETION_SCREW_AUDIT_2026-09-13.md).

## 1. Gesicherte Completion-Architektur `✓[M]`

Mit

```math
q_a=X_a^*X_a-\Gamma_aI,
\qquad
\mathcal E=(E_+,E_-),
```

ist `D_NP(a)=ker E`. Rank-2 Completion-Dualität, Morse-Index-Filter, Reflection/Parity-Reduktion und die kanonische Completion `lambda=1` sind geschlossen.

## 2. Exact `a=1` Fourier form `✓[M]`

Für zero-extended `v` mit Träger in `(-1,1)` gilt exakt

```math
q_1(v)=\int_{\mathbb R}m_1(\xi)|\widehat v(\xi)|^2d\xi,
```

```math
m_1(\xi)=
\operatorname{Re}\psi\left(\frac14+\frac{i\xi}{2}\right)-\log\pi
-2\sum_{n\in\{2,3,4,5,7\}}
\frac{\Lambda(n)}{\sqrt n}\cos(\xi\log n).
```

Die Fensterbedingung erzeugt keinen zusätzlichen quadratischen Rest.

## 3. Sharpened high-frequency certificate `✓[K/M]`

Der neue Exact-Head-Arb-Gate kombiniert:

- 64 positive Digamma-Reihenterme plus rigorosen Integralrest;
- einen globalen Ableitungsbound `|m_1'|<8.214249` für `|xi|>=1551`;
- ein rationales `0.02`-Gitter auf `[1551,2500]`;
- einen monotone Worst-Case-Bound für `|xi|>=2500`.

Zertifiziert ist

```math
\boxed{m_1(\xi)>0.1\qquad(|\xi|\ge1551).}
```

Konservative Zwischenschranken:

```text
grid-point lower bound > 0.2315764
compact global floor  > 0.1078
far-field floor       > 0.1259187
```

Der ältere `m_1>0.04`-Satz ab `2300` bleibt gültig, ist für die finite Reduktion aber überholt.

## 4. Reduced bounded-band operator `✓[M] / ✓[K/M]`

Setze

```math
c=0.1,
\qquad
\Omega=1551,
```

```math
r(\xi)=(m_1(\xi)-c)\mathbf1_{[-\Omega,\Omega]}(\xi),
\qquad
K=P_I\mathcal F^{-1}M_r\mathcal F P_I.
```

Dann

```math
q_1\succeq cI+K.
```

Der Exact-Head-Gate zertifiziert

```math
\boxed{\|r\|_\infty<12.}
```

## 5. Moment-augmented Prolate Schur theorem `✓[M]`

Für die PSWFs des Bandes `[-1551,1551]` setze

```math
R_N=
\operatorname{span}\{\psi_0,\ldots,\psi_{N-1}\}
+\operatorname{span}\{e^{x/2},e^{-x/2}\},
\qquad
T_N=R_N^\perp.
```

Dann `E|_{T_N}=0`; der Completionterm besitzt keinen Tail- und keinen Crossblock. Für

```math
L_1=0.1I+K+E^*E
```

gilt

```math
\|(L_1)_{RT}\|\le\|r\|_\infty\sqrt{\lambda_N},
```

```math
(L_1)_{TT}\succeq
[0.1-(\Gamma_1+0.1)\lambda_N]I.
```

Daher reicht

```math
(L_1)_{RR}\succeq\mu_RI,
\qquad
\mu_R\ge
\frac{\|r\|_\infty^2\lambda_N}
{0.1-(\Gamma_1+0.1)\lambda_N}.
```

## 6. Certified `N=1210` reduction `✓[K/M]`

Für den Prolate-Parameter `c_PSWF=1551` liefert Karnik--Romberg--Davenport plus Arb

```math
\boxed{\lambda_{1210}(1551)<1.5\times10^{-42}.}
```

Tatsächlicher Exact-Head-Upper-Bound:

```math
<1.468930504452317\times10^{-42}.
```

Außerdem

```math
\tau_{1210}>0.099,
```

und

```math
\boxed{\text{Schur penalty}<2.2\times10^{-39}.}
```

Tatsächlicher Upper-Bound:

```math
2.115259926411337\times10^{-39}.
```

## 7. Einziger verbleibender `a=1`-Gate — A1-FINITE `?[O]`

Vor jeder resolved-space Rechnung wurde der sufficient target festgelegt:

```math
\boxed{
(L_1)_{RR}\succeq3\times10^{-39}I.
}
```

Die ersten `1210` PSWF-Moden sind `605 even + 605 odd`; die Momentaugmentation erhöht die Dimension auf höchstens

```text
1212 total = 606 even + 606 odd.
```

Nach dieser Zertifizierung wäre der gesamte kanonische `a=1`-Completion-Satz geschlossen. Es bleibt kein separates Infinite-Tail- oder Crossblockproblem.

## 8. Status

```text
COMMON-JUMP / Q0                                      ✓[M]
rank-2 completion / Morse / parity                    ✓[M]
exact a=1 Fourier multiplier                          ✓[M]
Omega1551: m_1>0.1                                    ✓[K/M]
||r||<12 on |xi|<=1551                                ✓[K/M]
KRD lambda_1210<1.5e-42                               ✓[K/M]
Schur penalty <2.2e-39                                ✓[K/M]
1212-dimensional finite reduction                     ✓[K/M]
resolved lower bound >=3e-39                          ?[O]
certified a=1 completion                              ?[O]
all-a NP-GAP                                          ?[O]
forward Object-X candidate architecture               ✓[M]_part
full positive Object-X / RH                           ?[O]
```

## 9. Literature metadata firewall

The current arXiv v2 metadata for arXiv:2608.24827 lists **Xuefeng Zhu** as author and notes that the author name/affiliation were updated in v2. Historical project text that temporarily stated `Marcus Chuk` should be read as superseded bibliographic metadata; the mathematical benchmark claims are unchanged.

## 10. Firewalls

Do not claim:

- the resolved `3e-39` lower bound has been proved;
- `3e-39` is an observed or fitted eigenvalue;
- the older `2300/1680` reduction was wrong (it remains valid but coarser);
- fixed-window `a=1`, all-window NP-GAP, Object X, or RH is solved.
