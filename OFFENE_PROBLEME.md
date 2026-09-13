# Offene Probleme — CRITICAL-HALF / NP-GAP

> **Stand:** 13. September 2026.  
> Operative Quellen: [CURRENT-FRONT](CURRENT-FRONT.md), [Common-Jump-Audit](audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md), [Critical-half Green/tree](audits/P11_CRITICAL_HALF_GREEN_TREE_BRIDGE_2026-09-13.md), [Critical-half rigidity / Schur-gap](audits/P11_CRITICAL_HALF_RIGIDITY_AND_SCHUR_GAP_2026-09-13.md).

## Neu geschlossen

### `[NP-R1]` separate Geometriefrage — `✓[M]`

`R_1`, der logarithmische archimedische Anteil, Prime shifts und Exterior-shell-Masse sind in der gemeinsamen positiven Translation-Differenz-Geometrie

```math
K_t=T_{t/2}-T_{-t/2}
```

subsumiert.

### `[NP-COMMON]` — `✓[M]`

```math
\mu_a=\frac{e^{-t/2}}{1-e^{-2t}}dt
+\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}
```

liefert die positive Featureform `X_a^*X_a`.

### `[COMMON-JUMP-NORMAL-FORM]` — `✓[M]`

```math
Q_W(v,w)
=\langle Ev,PEw\rangle
+\langle X_av,X_aw\rangle
-\Gamma_a\langle v,w\rangle,
```

und auf Nullpol

```math
\boxed{Q_W|_{NP}=X_a^*X_a-\Gamma_aI.}
```

### `[CRIT-HALF-RANGE]` — `✓[M]`

Mit

```math
L_{1/2}=-\partial_x^2+1/4
```

gilt fuer jedes `a>0`

```math
\boxed{
C_c^\infty(-a,a)\cap\ker M(0)\cap\ker M(1)
=L_{1/2}C_c^\infty(-a,a).
}
```

Der Green-Kern ist

```math
G_{1/2}(x,y)=e^{-|x-y|/2}.
```

### `[CRIT-HALF-TREE]` — `✓[M]`

Derselbe Kernel, auf den logarithmischen Prime-Power-Knoten `k log p` abgetastet, ist

```math
p^{-|j-k|/2},
```

also exakt der P11-AR(1)-Kern. Eine explizite OU-/Sternbaum-Hilbertgeometrie reproduziert den fensterlosen P11-Hub+Rest-Kanalindex-Ledger inklusive cross-prime Root-Korrelation.

### `[CRIT-HALF-RIGIDITY]` — `✓[M]`

In der OU-Familie `e^{-sigma d}` ist die gewichtete Rootamplitude

```math
sqrt(log p) p^{-(1/4+sigma)k}.
```

P11 erzwingt den Exponenten `3/4`; daher `sigma=1/2`. Dieselbe Skala wird separat durch NULLPOL (`e^{±x/2}`) und durch den Gamma-Grundmodus `mu_0=1/2` erzwungen.

### `[NP-GAP-LIFT]` — `✓[M]`

Setze eindeutig

```math
v=L_{1/2}u,
\qquad u\in C_c^\infty(-a,a).
```

Dann ist NP-GAP eine **momentfreie** Coercivity-Frage. Die Gamma-Schicht besitzt die positive Resolventenleiter

```math
\Phi_\infty(D)
=\sum_{m\ge0}\frac{2}{\mu_m}D^2(D^2+\mu_m^2)^{-1},
\qquad
\mu_m=2m+1/2,
```

und der erste Modus wird lokal:

```math
4\|u''\|^2+\|u'\|^2.
```

### `[CRIT-HALF-SCHUR]` kleiner Radius — `✓[M]`

Der forward Schur-Test liefert

```math
\Phi_\infty(D)\succeq S(a)I,
```

```math
S(a)=
\log\frac{1+e^{-a/2}}{1-e^{-a/2}}
+2\arctan(e^{-a/2}),
```

und rein elementar `S(a)>kappa_*` fuer `0<a<=1/16`. Damit ist NP-GAP dort unkonditional geschlossen. Kein Neuheits-/Radiusrekord: bekannte lokale Weil-Positivitaet reicht weiter.

---

## Priorität 0 — `[NP-GAP]` `?[O]`

Global bleibt

```math
\boxed{
\lambda_{NP}(a)
:=
\inf_{\substack{0\ne v\in C_c^\infty(-a,a)\\M(v)(0)=M(v)(1)=0}}
\frac{\|X_av\|^2}{\|v\|_2^2}
\stackrel?\ge\Gamma_a
}
```

fuer alle `a>0`.

Fuer die Familie aller Fenster ist dies die verbleibende RH-aequivalente Lower-Frame-/Spektralgap-Frage.

### `[NP-GAP-A]` Critical-half source lift — **Default**

Nicht mehr nur die Faktorisierung suchen; sie ist bewiesen. Jetzt die momentfreie Form

```math
v=L_{1/2}u
```

analytisch ausnutzen.

Prioritaet:

1. erste Gamma-Resolventenmoden in der `L_{1/2}`-Metrik lokal/coerciv behandeln;
2. Rest der Gamma-Leiter per Schur-/Resolventenabschätzung kontrollieren;
3. Prime-Jumps `L_{1/2}K_{log n}u` nicht wegwerfen, sondern mit der Critical-half-Tree-Geometrie koppeln;
4. nach einer in `a` stabilen Lower-Frame-Struktur suchen.

### `[NP-GAP-B]` Tree/Common-Jump comparison

Die Common-Jump-Form behandelt die `K_t`-Kanaele orthogonal, waehrend der P11-Kanalindex-Ledger einen kanonischen nichtorthogonalen OU-Tree-Kern besitzt.

Offen:

```text
Kann die Tree-Root/Innovationsgeometrie einen vorwaerts definierten
Kontraktor, Schur-Block oder Vergleichsoperator fuer X_a liefern,
der Gamma- und Prime-Energie gleichzeitig kontrolliert?
```

Kein rueckwaerts aus fertiger Weil-Positivitaet definierter Operator ist zulaessig.

### `[NP-GAP-C]` Threshold remainder

Der Integralteil

```math
J=2\int_0^\infty h(t)(1-e^{-t/2})dt
```

ist bereits die kontinuierliche mittlere Root-Chordenergie derselben Critical-half-OU-Geometrie.

Noch offen ist eine ebenso intrinsische Geometrisierung des verbleibenden festen Anteils

```math
\log(4\pi)+\gamma
```

in

```math
\kappa_*=\log(4\pi)+\gamma+J.
```

Dies ist **kein** isolierter Konstanten-Fit-Auftrag; gesucht wird nur eine vorwaerts erzwungene Operator-/Measure-Bedeutung.

### `[NP-GAP-D]` Klassen-No-Go

Falls ein radiusstabiler Bound nicht aus rein lokalen/diagonalen Moden folgen kann, soll dies mit einem vorab festgelegten Gegenbeispielmechanismus bewiesen werden. Besonders zu testen:

- rein punktweise Symboluntergrenzen;
- endliche Gamma-Moden ohne Prime-Jump-Kopplung;
- kanalweise getrennte Poincare-Schranken ohne Tree-Korrelation.

Ein enger No-Go zaehlt als Fortschritt.

---

## Danach

```text
CRITICAL-HALF SOURCE/TREE/RESOLVENT STRUCTURE
  |
  v
NP-GAP for every a
  |
  v
positive Weil form on global null-pole class
  |
  v
RH
```

Ein Beweis von NP-GAP fuer alle `a` waere bereits RH. Zirkularitaetskontrolle bleibt Pflicht.

## Auxiliary / separate

- OX-GEN-A: exakte Pole-layer geometry;
- POS-DIL #101--#105: auxiliary full-class route, mehrere Faktoren nun durch Tree-Root-Geometrie erklaert;
- R37/G4c, PR #91, PR #49 separat.

## Firewalls

Nicht behaupten:

- Critical-half Bridge beweise globalen NP-GAP;
- der Sternbaum allein realisiere bereits die volle Weilform;
- P11-Fensterprojektionen duerften entfallen;
- `log(4pi)+gamma` sei bereits geometrisiert;
- fixed-`a`-Positivitaet allein sei RH-aequivalent;
- Publikationsneuheit sei geklaert;
- Object X oder RH seien bewiesen.
