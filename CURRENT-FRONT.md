# CURRENT FRONT — Objekt X / OX-GEN-B

> **Operative Kopfschicht — zuerst lesen.**  
> **Redaktioneller Stand:** 13. September 2026; keine Registry-Promotion.  
> **Aktuelle Audits:** [OX-GEN-A](audits/P11_OX_GEN_A_COMMON_EXPONENTIAL_GENERATOR_2026-09-13.md), [POS-DIL-1](audits/P11_POS_DIL_1_PRIME_MOMENT_HILBERTIZATION_2026-09-13.md), [POS-DIL-2A No-Go](audits/P11_POS_DIL_2_UNIT_GAIN_FEATURE_SHORTING_NOGO_2026-09-13.md), [POS-DIL-2B exterior shell](audits/P11_POS_DIL_2B_FIRST_EXTERIOR_PRIME_SHELL_2026-09-13.md), [POS-DIL-2C radius](audits/P11_POS_DIL_2C_EXTERIOR_SHELL_RADIUS_0_1_2026-09-13.md), [POS-DIL-2C exact shell gauge / `R_0` absorption](audits/P11_POS_DIL_2C_EXACT_SHELL_GAUGE_R0_ABSORPTION_2026-09-13.md).

Diese Datei ordnet die Arbeit; sie beweist nichts. Registry und Arbeitsdefinition werden nicht automatisch durch Merge/CI promoviert.

## 1. Gesicherte Basis

Fixed-pair Strong Terminal/C6 liegt für jedes feste `0<R<S` im ungeraden P11-Graphraum vor. Die Prime-Power-Seite besitzt die exakte AR(1)/Weil-Tail-Struktur

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}p^{-|j-k|/2},
\qquad T_q^*T_q+uu^*=R_q.
```

Für `0<a<=1` gilt die lokalisierte Suzuki-/Weil-Normalform

```math
Q_{B_a}=G_a^+-c_aI-R_0-R_1.
```

Die bloße rückwärts definierte Kontraktorexistenz bleibt als Object-X-Gate gesperrt.

## 2. OX-GEN-A / POS-DIL-1

Mit

```math
\mathcal Ev=(E_+(v),E_-(v)),
\qquad
\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\mathcal EK_n=D_n\mathcal E
```

liegt `R_0` auf derselben Translation-/Reflexions-Generator-Ebene:

```math
R_0(v,w)=\langle\mathcal Ev,-P\mathcal Ew\rangle.
```

Die Prime-moment-Hilbertisierung erfüllt

```math
\|V_Nv\|^2=\|\mathcal Ev\|^2,
\qquad
R_0(v,w)=\langle V_Nv,\mathbb P_NV_Nw\rangle.
```

Für `n=p^k`, `q_p=p^{-1/2}`:

```math
\sqrt{w_{p,k}}D_{p^k}=\sqrt{\log p}(1-q_p^k)S.
```

## 3. POS-DIL-2A — bestehende lokale `G^+`-Masse allein `×[M]`

Bei `a=1/2` ist die unveränderte `G_{1/2}^+`-Norm zu klein für unit-gain Shorting. Der Plateau-Defekt erfüllt

```math
\delta_0
=32\sinh^2\frac14-1-\sqrt2(\log2)^2
>\frac5{32}.
```

## 4. Erster äußerer Prime-Shift-Shell

Definiere

```math
\mathscr S_a^{out}=\{n=p^k:a<c_n\le2a\},
\qquad c_n=\frac12\log n,
```

```math
H_a^{out}(v,w)=\sum_{n\in\mathscr S_a^{out}}
\frac{\Lambda(n)}{\sqrt n}\langle K_nv,K_nw\rangle.
```

Für jeden Außenkanal `c_n>a` sind die verschobenen Fenster disjunkt, also polarisiert

```math
\boxed{w_n\langle K_nv,K_nw\rangle
=2w_n\langle v,w\rangle.}
```

Somit

```math
H_a^{out}=2B_a^{out}I.
```

## 5. Radiusfrage geschlossen `✓[M]`

Setze

```math
A_a^{out}=G_a^++H_a^{out}.
```

Für alle `0<a<=1` wurde elementar bewiesen

```math
\boxed{
A_a^{out}(v,v)\ge\|\mathcal Ev\|^2.
}
```

Also ist

```math
D_a^{out}:=A_a^{out}-\mathcal E^*\mathcal E\succeq0
```

im Form-Sinn.

## 6. POS-DIL-2C-B — exakte Außenkanal-Gauge geschlossen `✓[M]`

Für **jede** endliche Außenkanalmenge `J` mit `c_n>a` gilt

```math
H_{a,J}=b_JI,
\qquad
b_J=2\sum_{n\in J}\frac{\Lambda(n)}{\sqrt n}.
```

Daher die exakte Gauge-Identität

```math
\boxed{
Q_{B_a}
=(G_a^++H_{a,J})-(c_a+b_J)I-R_0-R_1.
}
```

Für den ersten Außenshell:

```math
\boxed{
Q_{B_a}
=A_a^{out}-c_a^{out}I-R_0-R_1,
}
```

mit

```math
c_a^{out}=c_a+2B_a^{out}.
```

Schreibt man

```math
A_X=2\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n},
```

so ist

```math
\boxed{
c_a^{out}=c_a+A_{e^{4a}}-A_{e^{2a}}.}
```

Die volle Weilform bleibt exakt unverändert. Der isolierte Wert von `c_a` ist deshalb innerhalb dieser Prime-cutoff-Gauge **nicht kanonisch**; kanonisch ist die vollständige Differenzbuchung.

## 7. Exakte positive Absorption von `R_0` `✓[M]`

Setze

```math
L_+(v)=E_+(v)+E_-(v)
=2\int_{-a}^a\cosh(x/2)v(x)\,dx.
```

Polarisiert gilt exakt

```math
\boxed{
\mathcal E^*\mathcal E-R_0=L_+^*L_+.
}
```

Daher

```math
\begin{aligned}
P_a^{(0)}
&:=A_a^{out}-R_0\\
&=(A_a^{out}-\mathcal E^*\mathcal E)
 +(\mathcal E^*\mathcal E-R_0)\\
&=D_a^{out}+L_+^*L_+\succeq0.
\end{aligned}
```

Und die **exakte** lokalisierte Weil-Normalform wird

```math
\boxed{
Q_{B_a}=P_a^{(0)}-c_a^{out}I-R_1,
\qquad
P_a^{(0)}\succeq0,
\qquad0<a\le1.
}
```

Der elementare archimedische `r_0`-/`R_0`-Layer ist damit vollständig aus dem Rest entfernt und in einen positiven gemeinsamen Prime-/archimedischen Block absorbiert.

## 8. Neue Hauptfront — OX-GEN-B / `R_1` + gaugeinvarianter Skalarrest `?[O]`

Der verbleibende Rest ist

```math
\boxed{c_a^{out}I+R_1.}
```

Nicht mehr sinnvoll ist die Frage „Wie erklärt man den isolierten kanonischen Wert `c_a`?“, denn `c_a` verschiebt sich unter der exakten Prime-cutoff-Gauge.

Gesucht ist jetzt:

1. eine Generator-/Feature-Realisierung oder ein natürliches Klassen-No-Go für `R_1`;
2. eine **Gauge-Fixierung oder gaugeinvariante Skalar-Reststruktur**;
3. bevorzugt eine gemeinsame Behandlung von `R_1` und Skalarledger statt zwei post-hoc Korrekturen;
4. keine beliebige Diagonalaugmentation und keine rückwärts aus fertiger Weil-Positivität definierte Wurzel.

## 9. Firewalls

Nicht behaupten:

- `P_a^{(0)}` sei bereits die vollständige Weil-Gram-Realisierung;
- `Q_{B_a}` sei aus dieser Normalform ohne weitere Arbeit positiv;
- `R_1` sei absorbiert;
- `c_a^{out}` sei ein intrinsischer endgültiger Object-X-Skalar;
- die Aussage gelte bereits für `a>1`;
- Object X oder RH seien gelöst.

## 10. Status

```text
exterior Prime cutoff-gauge identity                  ✓[M]
first-shell scalar increment = A_{e^{4a}}-A_{e^{2a}} ✓[M]
cutoff-gauge dependence of isolated c_a               ✓[M]
positive defect form D_a^{out}                        ✓[M]
exact positive absorption A_a^{out}-R_0               ✓[M]
exact normal form Q=P_a^{(0)}-c_a^{out}I-R_1          ✓[M]
POS-DIL r_0-layer on 0<a<=1                           ✓[M]
OX-GEN-A2' overall                                     ✓[M]_part
R_1 / gauge-invariant scalar remainder                ?[O]
full Object-X realization / RH                        ?[O]
```

PR #91, PR #49 und R37/G4c bleiben separate Nebenfronten. Registry unverändert.
