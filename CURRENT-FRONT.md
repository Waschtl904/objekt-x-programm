# CURRENT FRONT — Objekt X / NULLPOL-COMMON → NP-GAP

> **Operative Kopfschicht — zuerst lesen.**  
> **Stand:** 13. September 2026; keine Registry-Promotion.  
> **Kanonischer neuer Audit:** [NULLPOL common jump-Gram](audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md).  
> Vorheriger strategischer Filter: [Nullpol-Reklassifikation](audits/P11_NULLPOLE_STRATEGIC_RECLASSIFICATION_2026-09-13.md).

Diese Datei ordnet die Arbeit; sie beweist nichts. Registry und Arbeitsdefinition bleiben unverändert.

## 1. Nullpol-Hauptklasse

Mit

```math
M(v)(s)=\int_{\mathbb R}v(x)e^{(s-1/2)x}\,dx
```

gilt exakt

```math
E_-(v)=M(v)(0),\qquad E_+(v)=M(v)(1).
```

Auf

```math
\mathscr D_{NP}=\ker M(0)\cap\ker M(1)
```

verschwinden daher `R_0` und `\mathcal E`. Connes–Consani Proposition C.1 liefert global einen RH-äquivalenten Weil-Scope mit diesen Nullbedingungen. Keine fixed-`a`-Äquivalenz wird behauptet.

## 2. Der gemeinsame Prime-/archimedische Kanal `✓[M]`

Setze für `t>0`

```math
\boxed{K_t:=T_{t/2}-T_{-t/2}.}
```

Dann

```math
K_t^*K_t=2I-T_t-T_{-t}.
```

Die archimedische positive Dichte ist

```math
\boxed{
h(t)=\frac{e^{-t/2}}{1-e^{-2t}}
=\frac{e^{t/2}}{e^t-e^{-t}}>0.
}
```

Die Prime-Power-Gewichte sind

```math
w_n=\frac{\Lambda(n)}{\sqrt n}.
```

Für `supp(v),supp(w) subset [-a,a]` sei

```math
\mathcal P_a=\{n=p^k:\log n\le2a\}.
```

Definiere die positive gemischte Maßstruktur

```math
\boxed{
\mu_a=h(t)dt+\sum_{n\in\mathcal P_a}w_n\delta_{\log n}.
}
```

**Archimedes = kontinuierlicher Teil, Primzahlpotenzen = atomarer Teil desselben `K_t`-Features.**

## 3. Positive Featureabbildung `✓[M]`

Ein natürlicher Hilbert-Zielraum ist

```math
\mathscr H_a=
L^2((0,\infty),h(t)dt;L^2(\mathbb R))
\oplus
\bigoplus_{n\in\mathcal P_a}L^2(\mathbb R).
```

Setze

```math
\boxed{
\mathcal X_av=
\left(
[t\mapsto K_tv],
[\sqrt{w_n}K_{\log n}v]_{n\in\mathcal P_a}
\right).
}
```

Dann

```math
\boxed{
\langle\mathcal X_av,\mathcal X_aw\rangle
=
\int_0^\infty h(t)\langle K_tv,K_tw\rangle dt
+
\sum_{n\in\mathcal P_a}w_n
\langle K_{\log n}v,K_{\log n}w\rangle.
}
```

Diese Form ist vorwärts konstruiert und positiv; keine Weil-Positivität und keine RH-Annahme gehen ein.

## 4. Exakte archimedische Schwelle `✓[M]`

Direkt aus dem Integralterm der expliziten Formel:

```math
2\int_0^\infty h(t)(1-e^{-t/2})dt
=\log2+\frac\pi2.
```

Daher

```math
\boxed{
\kappa_*
=\log(8\pi)+\gamma+\frac\pi2
=\log\pi-\psi(1/4).
}
```

und

```math
\boxed{
\Gamma_a=
2\sum_{n\in\mathcal P_a}\frac{\Lambda(n)}{\sqrt n}
+\log\pi-\psi(1/4).
}
```

## 5. Exakte COMMON-JUMP-GRAM-Normalform `✓[M]`

Für glatte kompakt getragene `v,w` in `[-a,a]`, **für jedes `a>0`**, gilt exakt

```math
\boxed{
Q_W(v,w)
=
\langle\mathcal Ev,P\mathcal Ew\rangle
+
\langle\mathcal X_av,\mathcal X_aw\rangle
-
\Gamma_a\langle v,w\rangle,
}
```

mit

```math
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
```

Auf Nullpol:

```math
\boxed{
Q_W(v,w)
=
\langle\mathcal X_av,\mathcal X_aw\rangle
-
\Gamma_a\langle v,w\rangle.
}
```

Damit sind `log|D|`, `R_1`, Prime shifts und Exterior-shell-Masse nicht mehr getrennte Geometriefragen: sie liegen in derselben positiven `K_t`-Jump-Gram-Struktur.

## 6. Fourier-Gegencheck

Die positive Featureform hat Symbol

```math
\Phi_a(z)=
\operatorname{Re}\psi\left(\frac14+\frac{iz}{2}\right)-\psi(1/4)
+2\sum_{n\in\mathcal P_a}w_n(1-\cos(z\log n))\ge0
```

für reelles `z`. Nach Abzug von `Gamma_a` erhält man exakt den nichtpolaren Suzuki-/Weil-Multiplikator.

## 7. Cutoff-Gauge jetzt geometrisiert `✓[M]`

Für `0<a<b` und bereits in `[-a,a]` getragenes `v,w` liefern neue Prime-Atome mit `2a<log n<=2b`

```math
\langle K_{\log n}v,K_{\log n}w\rangle
=2\langle v,w\rangle.
```

Daher wachsen positive Gramform und Schwelle um exakt denselben Skalar:

```math
\boxed{
\langle X_bv,X_bw\rangle-\Gamma_b\langle v,w\rangle
=
\langle X_av,X_aw\rangle-\Gamma_a\langle v,w\rangle.
}
```

Der invariant sinnvolle Gegenstand ist also die **zentrierte Gram-Paarung**, nicht ein isolierter `c_a`-Wert.

## 8. Neuer einziger Hauptengpass — NP-GAP `?[O]`

Auf der global RH-äquivalenten Nullpolklasse wird RH zu der scharfen Lower-Frame-Bedingung

```math
\boxed{
\|\mathcal X_av\|^2\ge\Gamma_a\|v\|_2^2
}
```

für jedes `a>0` und jede glatte Nullpol-Testfunktion mit Träger in `[-a,a]`.

Äquivalent:

```math
\lambda_{NP}(a)
:=
\inf_{\substack{0\ne v\in C_c^\infty(-a,a)\\M(v)(0)=M(v)(1)=0}}
\frac{\|\mathcal X_av\|^2}{\|v\|_2^2}
\stackrel{?}{\ge}\Gamma_a.
```

**Das ist jetzt der Default-Auftrag.** Ein Beweis für alle `a` wäre bereits RH; deshalb darf Weil-Positivität nicht rückwärts als Input verwendet werden.

## 9. Strategische Statusänderung

```text
NP-R1 separate geometry question                       closed/subsumed ✓[M]
NP-COMMON common Prime/archimedean feature family      ✓[M]
NP-SCALAR cutoff-gauge covariance                      ✓[M]
COMMON-JUMP exact normal form, all a>0                 ✓[M]
forward Object-X candidate architecture                ✓[M]_part
sharp NULLPOL frame/spectral gap                       ?[O]
full positive Object-X realization / RH                ?[O]
publication novelty                                    ?[O]
```

OX-GEN-A bleibt die exakte Polschicht. POS-DIL #101--#105 bleibt eine mathematisch gültige auxiliary full-class route.

## 10. Firewalls

Nicht behaupten:

- `Q_W>=0` sei bewiesen;
- der scharfe Lower-Frame-Bound sei bewiesen;
- ein einzelnes fixes `a` sei bereits RH-äquivalent;
- Publikationsneuheit sei geklärt;
- die Theorem-Registry werde durch diese Navigation promoviert;
- Object X oder RH seien gelöst.

PR #91, PR #49 und R37/G4c bleiben separate Nebenfronten.