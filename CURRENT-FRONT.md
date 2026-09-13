# CURRENT FRONT — Objekt X / COMMON-JUMP → NP-OVERLAP-AR1

> **Operative Kopfschicht — zuerst lesen.**  
> **Stand:** 13. September 2026; keine Registry-Promotion.  
> **Hauptaudits:** [COMMON-JUMP](audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md) · [Q0 first channel](audits/P11_NP_GAP_Q0_FIRST_CHANNEL_2026-09-13.md) · [Review correction / Prime overlap](audits/P11_NP_GAP_REVIEW_CORRECTION_PRIME_OVERLAP_2026-09-13.md) · [Prime-overlap AR(1)](audits/P11_NP_OVERLAP_AR1_FIBERIZATION_2026-09-13.md).

Diese Datei ordnet die Arbeit; sie beweist nichts. Registry und Arbeitsdefinition bleiben unverändert.

## 1. COMMON-JUMP `✓[M]`

Mit

```math
K_t=T_{t/2}-T_{-t/2}
```

entstehen archimedischer Ort und Primzahlpotenzen aus derselben positiven Featurefamilie. Auf

```math
D_{NP}=\ker M(0)\cap\ker M(1)
```

gilt für jedes `a>0`

```math
\boxed{Q_W(v)=\|X_av\|^2-\Gamma_a\|v\|^2.}
```

Die Architektur bleibt `✓[M]`; der forward Object-X-Kandidat bleibt `✓[M]_part`.

## 2. Q0 / Gamma-Kanäle `✓[M]`

Für

```math
A_\alpha=\int_0^\infty e^{-\alpha t}K_t^*K_tdt
```

gilt

```math
A_\alpha=\frac2\alpha(-\partial_x^2)(-\partial_x^2+\alpha^2)^{-1}.
```

Mit

```math
Q_0=-\partial_x^2+\frac14
```

folgt

```math
\boxed{A_{1/2}Q_0=-4\partial_x^2,}
\qquad
\boxed{Q_0:C_c^\infty(-a,a)\cong D_{NP}(a)}
```

support-erhaltend. Für höhere Kanäle beweist der Schur-Test

```math
\boxed{A_\alpha\succeq\frac2\alpha e^{-\alpha a}I.}
```

## 3. Short-window-Buchung korrigiert

COMMON-JUMP/Q0 reproduziert Kleinfenster-Coercivity architekturintern `✓[M]_part`. Die Positivität kleiner Fenster ist aber kein neuer Literatur-Satz: Suzuki Theorem 1.4 beweist bereits eine stärkere volle-Klasse-Aussage. Daher

```text
short-window internal reproduction       ✓[M]_part
short-window positivity as NEW theorem    ×[M]
```

Ein eigener Arb-Exact-Head-Gate zertifiziert den projektinternen Schnittpunkt `a_*` von `B(a)=kappa_*`; die vorgesehene Bracket ist

```math
0.1033784517534<a_*<0.1033784517535<\frac12\log2.
```

## 4. Exakte zentrierte Restform `✓[M]`

Definiere

```math
\mathcal A(v)
=\int_0^\infty\frac{e^{-t/2}}{1-e^{-2t}}\|K_tv\|^2dt
-\kappa_*\|v\|^2.
```

Dann gilt auf Nullpol exakt

```math
\boxed{Q_W(v)=\mathcal A(v)-\mathcal O_a(v)}
```

mit

```math
\boxed{
\mathcal O_a(v)
=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\operatorname{Re}\langle T_{\log n}v,v\rangle.
}
```

Die gesamte Prime-Diagonalmasse cancelt gegen den Prime-Anteil der Schwelle. Der harte arithmetische Rest besteht nur aus den überlappenden inneren Prime-Power-Shifts.

## 5. Exakte Einzelshift-Geometrie `✓[M]`

Für

```math
S_t=\frac12(T_t+T_{-t})
```

auf `L^2(-a,a)` ergibt die Faserung modulo `t` Pfadgraphen. Für `0<t<2a` gilt exakt

```math
\boxed{
\|S_t\|
=\cos\left(\frac{\pi}{\lceil2a/t\rceil+1}\right),
}
```

und für `t>=2a` ist `S_t=0`.

Noch wichtiger: dieselbe scharfe Norm wird bereits auf `D_{NP}(a)` erreicht:

```math
\boxed{
\sup_{0\ne v\in D_{NP}(a)}
\frac{\operatorname{Re}\langle T_tv,v\rangle}{\|v\|^2}
=
\cos\left(\frac{\pi}{\lceil2a/t\rceil+1}\right).
}
```

Damit

```text
single-shift null-pole norm improvement    ×[M]
```

Die beiden Momentbedingungen helfen **nicht** bei einem einzelnen Shift. Ein all-window-Beweis muss kollektive Struktur mehrerer Prime-Power-Shifts oder deren Kopplung an den archimedischen Operator nutzen.

## 6. Vollständiger Block einer Primzahl = AR(1) `✓[M]`

Fixiere `p` und setze

```math
\ell_p=\log p,
\qquad q_p=p^{-1/2}.
```

Der vollständige `p`-Overlapblock ist

```math
\mathbf O_{p,a}
=2(\log p)\sum_{k\ell_p<2a}q_p^kS_{k\ell_p}.
```

Nach Faserung modulo `ell_p` ist eine `N`-Punkt-Faser exakt

```math
\boxed{
\mathbf O_{p,a}^{(N)}
=(\log p)\left(R_{q_p}^{(N)}-I_N\right),
}
```

mit

```math
R_q^{(N)}=(q^{|j-k|})_{j,k}.
```

Das ist exakt die Kac--Murdock--Szegő-/AR(1)-Korrelationsmatrix aus dem früheren Prime-Power-Strang.

Der zentrierte Symbolfaktor lautet

```math
\boxed{
P_q(\theta)-1
=\frac{2q(\cos\theta-q)}{1-2q\cos\theta+q^2}.
}
```

Der gefährliche positive Sektor ist also

```math
\boxed{|\theta|<\arccos q}
```

(modulo `2pi`): niedrige Frequenzen auf dem logarithmischen `p`-Gitter.

## 7. Kollektive Multi-Prime-Interferenz = neue Default-Front `?[O]`

Für verschiedene Primzahlen `p!=r` gilt

```math
\frac{\log p}{\log r}\notin\mathbb Q.
```

Die exakten AR(1)-Faserungen leben daher auf inkommensurablen Gittern. Die neue scharfe Frage lautet:

> Wie groß kann die **gleichzeitige** positive Niedrigfrequenzmasse derselben Funktion in den AR(1)-Blöcken vieler inkommensurabler Prime-Gitter sein?

Zu beweisen bleibt

```math
\boxed{
(A_\infty-\kappa_*I)|_{D_{NP}(a)}
\succeq
\sum_p\mathbf O_{p,a}|_{D_{NP}(a)}
\quad\forall a>0.
}
```

Priorität:

1. quantitative Inkompatibilität der positiven AR(1)-Sektoren verschiedener `p`;
2. Rückbindung an die bereits bewiesene AR(1)/Markov-/Weil-tail-Faktorisierung;
3. `Q_0`-Sobolevtransport der Shift-Korrelationen;
4. Parität und Randvariable `delta_n=2a-log n`;
5. keine Rückkehr zu unabhängigen Einzelshift-Normabschätzungen als Hauptstrategie.

## 8. Auxiliary

Die finite Gamma-null ladder bei `{-2m,2m+1}` ist nach Connes--Consani zulässig; negative gerade Punkte sind triviale Zeta-Nullstellen. Sie bleibt auxiliary, solange sie den kollektiven Prime-overlap nicht quantitativ kontrolliert.

## 9. Status

```text
COMMON-JUMP architecture                                  ✓[M]
Q0 first-channel / support map                            ✓[M]
centered Prime-overlap decomposition                      ✓[M]
exact compressed single-shift fiber geometry              ✓[M]
single-shift null-pole improvement                        ×[M]
exact per-prime AR(1) fiberization                        ✓[M]
positive low-frequency AR(1) sector                       ✓[M]
incommensurable Prime lattices                            ✓[M]
collective multi-prime suppression                        ?[O]
all-a NP-OVERLAP domination                               ?[O]
forward Object-X candidate architecture                   ✓[M]_part
full positive Object-X / RH                               ?[O]
```

Registry und Objekt-X-Arbeitsdefinition bleiben unverändert.