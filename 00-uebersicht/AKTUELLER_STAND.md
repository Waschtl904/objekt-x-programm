# Aktueller Stand — Objekt X / NP-OVERLAP-AR1

> **Stand:** 13. September 2026; Registry unverändert.  
> Details: [CURRENT-FRONT](../CURRENT-FRONT.md), [Prime-overlap AR(1)](../audits/P11_NP_OVERLAP_AR1_FIBERIZATION_2026-09-13.md), [Review correction](../audits/P11_NP_GAP_REVIEW_CORRECTION_PRIME_OVERLAP_2026-09-13.md).

## 1. COMMON-JUMP und Q0 `✓[M]`

Auf der Nullpolklasse gilt

```math
Q_W(v)=\|X_av\|^2-\Gamma_a\|v\|^2.
```

Der erste archimedische Kanal erfüllt mit `Q0=-partial_x^2+1/4`

```math
A_{1/2}Q_0=-4\partial_x^2,
\qquad
Q_0:C_c^\infty(-a,a)\cong D_{NP}(a).
```

Für höhere Kanäle gilt rigoros

```math
A_\alpha\succeq\frac2\alpha e^{-\alpha a}I.
```

Die projektinterne Kleinfenster-Coercivity bleibt `✓[M]_part`, ist aber kein neuer Kleinfenster-Positivitätssatz der Literatur (`×[M]` als Neuheitsclaim; Suzuki Theorem 1.4 ist stärker).

## 2. Zentrierte Restform `✓[M]`

Nach exakter Prime-Zentrierung:

```math
\boxed{Q_W(v)=\mathcal A(v)-\mathcal O_a(v)}
```

mit

```math
\mathcal O_a(v)
=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\operatorname{Re}\langle T_{\log n}v,v\rangle.
```

Der harte Rest ist also ein endlicher gewichteter Overlap-Operator, nicht die nackte Prime-Schwelle.

## 3. Einzelshift exakt — und als Strategie ausgeschöpft

Für

```math
S_t=\frac12(T_t+T_{-t})
```

liefert Faserung modulo `t`

```math
\boxed{
\|S_t\|
=\cos\frac{\pi}{\lceil2a/t\rceil+1}
\quad(0<t<2a).
}
```

Dieselbe Norm wird bereits auf `D_NP(a)` erreicht. Daher

```text
single-shift null-pole norm improvement   ×[M]
```

Nullpol allein verbessert keinen einzelnen Shiftkanal. Kollektive Prime-Struktur ist notwendig.

## 4. Prime-Power-Block = exakte AR(1)-Matrix `✓[M]`

Für eine Primzahl `p`,

```math
\ell_p=\log p,
\qquad q_p=p^{-1/2},
```

ist nach Faserung modulo `ell_p` auf einer `N`-Punkt-Faser

```math
\boxed{
O_{p,a}^{(N)}
=(\log p)(R_{q_p}^{(N)}-I_N),
\qquad
R_q^{(N)}=(q^{|j-k|})_{j,k}.
}
```

Der positive Symbolsektor ist

```math
|\theta|<\arccos(q_p).
```

Damit kehrt die bereits bekannte Prime-Power-AR(1)-Geometrie exakt als Faserstruktur des neuen Overlap-Problems zurück.

## 5. Neue Hauptfront `?[O]`

Für verschiedene Primzahlen sind `log p/log r` irrational. Die zentrale Frage ist daher die **gleichzeitige** Konzentration derselben Funktion in den positiven Niedrigfrequenzsektoren vieler inkommensurabler AR(1)-Gitter.

Zu beweisen bleibt

```math
\boxed{
(A_\infty-\kappa_*I)|_{D_{NP}(a)}
\succeq
\sum_p O_{p,a}|_{D_{NP}(a)}.
}
```

## 6. Status

```text
COMMON-JUMP / Q0                              ✓[M]
centered Prime-overlap form                   ✓[M]
exact single-shift fiber theorem              ✓[M]
single-shift null-pole improvement            ×[M]
exact per-prime AR(1) fiberization            ✓[M]
collective multi-prime suppression            ?[O]
forward Object-X candidate architecture       ✓[M]_part
full positive Object-X / RH                   ?[O]
```
