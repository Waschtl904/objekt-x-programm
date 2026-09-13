# Aktueller Stand — Objekt X / COMMON-JUMP → NP-OVERLAP

> **Stand:** 13. September 2026; Registry unverändert.  
> Details: [CURRENT-FRONT](../CURRENT-FRONT.md), [COMMON-JUMP](../audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md), [Q0 first channel](../audits/P11_NP_GAP_Q0_FIRST_CHANNEL_2026-09-13.md), [Review correction / Prime overlap](../audits/P11_NP_GAP_REVIEW_CORRECTION_PRIME_OVERLAP_2026-09-13.md).

## 1. Gemeinsame positive Geometrie `✓[M]`

Für

```math
K_t=T_{t/2}-T_{-t/2}
```

liegen archimedischer Ort und Primzahlpotenzen in derselben positiven Featurearchitektur. Auf Nullpol gilt exakt

```math
\boxed{Q_W(v)=\|X_av\|^2-\Gamma_a\|v\|^2.}
```

## 2. `Q_0` / erster Gamma-Kanal `✓[M]`

Mit

```math
A_\alpha=\int_0^\infty e^{-\alpha t}K_t^*K_tdt
```

ist

```math
A_\alpha=\frac2\alpha(-\partial_x^2)(-\partial_x^2+\alpha^2)^{-1}.
```

Für `alpha=1/2` und `Q_0=-partial_x^2+1/4`:

```math
\boxed{A_{1/2}Q_0=-4\partial_x^2.}
```

Außerdem

```math
Q_0:C_c^\infty(-a,a)\cong D_{NP}(a)
```

support-erhaltend.

## 3. Höhere Kanalabschätzung `✓[M]`

Der komprimierte Resolventenkern liefert per Schur-Test

```math
\boxed{
\langle v,A_\alpha v\rangle
\ge\frac2\alpha e^{-\alpha a}\|v\|^2.
}
```

Die externe Exponentenfrage ist damit geschlossen.

## 4. Short-window: Mathematik bleibt, Neuheitsbuchung korrigiert

Die COMMON-JUMP/Q0-Architektur reproduziert auf einem expliziten kleinen Fensterbereich Coercivity. Die Existenz von Kleinfensterpositivität ist aber **kein neuer Literatur-Satz**: Suzuki Theorem 1.4 beweist bereits eine stärkere Positivität auf der vollen lokalen Klasse.

Daher:

```text
architekturinterne short-window Coercivity     ✓[M]_part
short-window positivity als neuer Satz         ×[M]
```

Für den projektinternen Bound gilt mit `x=e^{-a/2}`

```math
B(a)=\frac{4\pi^2}{\pi^2+a^2}
+\log\frac{1+x}{1-x}+2\arctan x-4x.
```

Ein eigener Arb-Gate zertifiziert die Wurzel `B(a_*)=kappa_*` im Intervall

```math
0.1033784517534<a_*<0.1033784517535<\frac12\log2.
```

## 5. Exakte Prime-overlap-Restform `✓[M]`

Definiere den archimedischen Überschuss

```math
\mathcal A(v)
=\int_0^\infty\frac{e^{-t/2}}{1-e^{-2t}}\|K_tv\|^2dt
-\kappa_*\|v\|^2.
```

Dann gilt auf `D_NP(a)` exakt

```math
\boxed{
Q_W(v)=\mathcal A(v)-\mathcal O_a(v),
}
```

mit

```math
\boxed{
\mathcal O_a(v)
=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\operatorname{Re}\langle T_{\log n}v,v\rangle.
}
```

Die große Prime-Diagonalmasse cancelt vollständig gegen den Prime-Anteil der Schwelle. Übrig bleibt ausschließlich die gewichtete Überlappung der inneren Prime-Power-Shifts.

## 6. `Q_0`-Transport des arithmetischen Defekts `✓[M]`

Für `v=Q_0u`:

```math
\operatorname{Re}\langle T_tv,v\rangle
=
\operatorname{Re}\langle T_tu'',u''\rangle
+\frac12\operatorname{Re}\langle T_tu',u'\rangle
+\frac1{16}\operatorname{Re}\langle T_tu,u\rangle.
```

Damit ist die neue Hauptfrage eine endliche gewichtete Shift-Korrelationsfrage auf Sobolev-Ebenen `0,1,2`.

## 7. Neue Hauptfront

```math
\boxed{
(A_\infty-\kappa_*I)|_{D_{NP}(a)}
\succeq
\mathbf O_a|_{D_{NP}(a)}
\quad\forall a>0.
}
```

Status:

```text
COMMON-JUMP                                  ✓[M]
Q0 first-channel / support map               ✓[M]
centered Prime-overlap decomposition         ✓[M]
short-window internal reproduction           ✓[M]_part
short-window novelty claim                   ×[M]
all-a NP-OVERLAP                             ?[O]
forward Object-X candidate architecture      ✓[M]_part
full positive Object-X / RH                  ?[O]
```

Die endliche Mehrkanal-Gamma-Leiter ist strukturell zulässig, aber auxiliary, solange sie `O_a` nicht quantitativ kontrolliert.