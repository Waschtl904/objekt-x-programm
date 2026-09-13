# P11 Audit — Critical-half rigidity and analytic Schur-gap

**Datum:** 13. September 2026  
**Basis:** Branch `research/critical-half-green-tree-bridge-2026-09-13`, nach dem Critical-half Green/tree Audit.  
**Rolle:** theorem-level Folgerungen aus der neuen Green-/OU-Brücke.  
**Registry:** unverändert.  
**Nonclaim:** kein globaler NP-GAP-, Object-X- oder RH-Abschluss; keine Publikationsneuheit behauptet.

---

## 0. Kurzurteil

Die neue Green-/OU-Brücke besitzt eine **rigide Massenskala**. In der natürlichen Einparameterfamilie

```math
kappa_sigma(alpha,beta)=e^{-sigma d(alpha,beta)},
\qquad sigma>0,
```

wird `sigma=1/2` gleichzeitig und eindeutig durch drei bereits unabhängig vorhandene Projektstrukturen erzwungen:

1. den P11-Prime-Power-AR(1)-Kern `p^{-|j-k|/2}` und den erzwungenen P11-Hubexponenten `3/4`;
2. die beiden Nullpol-Moden `e^{±x/2}`, also die Pole `s=0,1` um den Mittelpunkt `1/2`;
3. den Grundmodus `mu_0=1/2` der archimedischen Gamma-Resolventenleiter `mu_m=2m+1/2`.

Damit ist die im Green/tree Audit gefundene `1/2` **nicht frei gewaehlt**: innerhalb dieser natuerlichen OU-/Green-Familie ist sie die einzige gemeinsame Skala.

Zusaetzlich liefert dieselbe Resolventenleiter eine rein analytische, unkonditionale Lower-Frame-Schranke fuer kleine Fenster. Der saubere elementare Bereich

```math
0<a<=1/16
```

ist vollständig zertifiziert. Diese kleine-Fenster-Positivitaet ist **nicht als literarisch neu** zu verstehen; bekannte Arbeiten reichen wesentlich weiter. Ihr Wert hier ist, dass sie direkt aus dem neuen Critical-half-Mechanismus folgt und damit dessen analytische Tragfaehigkeit testet.

Status:

```text
critical-half rigidity sigma=1/2                     ✓[M]
P11 exponent identity beta=1/4+sigma -> sigma=1/2   ✓[M]
NULLPOL-pole rigidity                                ✓[M]
Gamma-ground-mode rigidity                           ✓[M]
archimedean Schur frame bound S(a)                   ✓[M]
strict NP-GAP for every 0<a<=1/16                    ✓[M]
new global NP-GAP mechanism beyond known local range ?[O]
publication novelty                                  ?[O]
RH / full Object X                                   ?[O]
```

---

# 1. Die normierte OU-Familie auf dem Prim-Sternbaum

Fuer `sigma>0` definiere im selben Sternbaum-Hilbertraum

```math
\boxed{
\Phi^{(\sigma)}_{p,x}
:=
e^{-\sigma x}e_o
\oplus
\left[
\sqrt{2\sigma}\,\mathbf1_{[0,x]}(s)e^{-\sigma(x-s)}
\right]_p.
}
```

Dann

```math
\|\Phi^{(\sigma)}_{p,x}\|^2
=e^{-2\sigma x}
+2\sigma\int_0^xe^{-2\sigma(x-s)}ds
=1.
```

Direkte Integration liefert fuer beliebige Baumknoten

```math
\boxed{
\langle\Phi^{(\sigma)}_\alpha,
       \Phi^{(\sigma)}_\beta\rangle
=e^{-\sigma d(\alpha,\beta)}.
}
```

Die zuvor gefundene Critical-half-Geometrie ist der Spezialfall `sigma=1/2`; dort ist `sqrt(2 sigma)=1` und zugleich der normierte OU-Kern identisch mit dem unskalierten Green-Kern von `D^2+1/4`.

---

# 2. P11 erzwingt `sigma=1/2`

Die Weil-Diagonalgewichte sind

```math
w_{p,k}=(\log p)p^{-k/2},
```

also

```math
\sqrt{w_{p,k}}
=\sqrt{\log p}\,p^{-k/4}.
```

Der Root-Korrelationsfaktor der `sigma`-Familie am Prime-Power-Knoten `x=k log p` ist

```math
\langle\Phi_o,\Phi^{(\sigma)}_{p,k\log p}\rangle
=p^{-\sigma k}.
```

Damit besitzt die gewichtete Rootamplitude notwendigerweise den Exponenten

```math
\boxed{
\beta(\sigma)=\frac14+\sigma,
}
```

denn

```math
\sqrt{w_{p,k}}p^{-\sigma k}
=\sqrt{\log p}\,p^{-(1/4+\sigma)k}.
```

P11 hat unabhaengig aus der Martingalmultiplizitaet und der geforderten Weil-Diagonale bereits exakt

```math
\beta=\frac34
```

erzwungen. Daher

```math
\boxed{
\frac14+\sigma=\frac34
\iff
\sigma=\frac12.
}
```

Dasselbe folgt direkt aus dem normalisierten same-prime Kern:

```math
p^{-\sigma|j-k|}
=p^{-|j-k|/2}
\quad\text{fuer alle }j,k
\iff
\sigma=\frac12.
```

Somit ist die Critical-half-Skala bereits rein aus dem P11-Prime-Ledger eindeutig bestimmt.

---

# 3. NULLPOL erzwingt dieselbe Skala

Fuer die allgemeine massive Operatorfamilie

```math
L_\sigma=D^2+\sigma^2=-\partial_x^2+\sigma^2
```

sind die homogenen exponentiellen Moden

```math
e^{\pm\sigma x}.
```

Genau wie im Green/tree Audit gilt auf einem kompakten Fenster:

```math
L_\sigma C_c^\infty(-a,a)
=
\left\{
v\in C_c^\infty(-a,a):
\int e^{\sigma x}v(x)dx
=
\int e^{-\sigma x}v(x)dx
=0
\right\}.
```

Die reale Nullpolklasse verwendet aber exakt

```math
M(v)(0)=\int e^{-x/2}v(x)dx=0,
\qquad
M(v)(1)=\int e^{x/2}v(x)dx=0.
```

Daher stimmt eine `L_sigma`-Range genau mit NULLPOL ueberein nur fuer

```math
\boxed{\sigma=1/2.}
```

Aequivalent: die beiden Pole `s=0,1` liegen relativ zum Mellin-Mittelpunkt `1/2` bei den Abstaenden `±1/2`.

---

# 4. Die Gamma-Schicht erzwingt dieselbe Skala

Die positive archimedische Dichte aus NULLPOL-COMMON ist

```math
h(t)=\frac{e^{-t/2}}{1-e^{-2t}}
=\sum_{m=0}^\infty e^{-\mu_m t},
\qquad
\mu_m=2m+\frac12.
```

Daraus folgt die positive Resolventenleiter

```math
\Phi_\infty(D)
=
\sum_{m=0}^\infty
\frac{2}{\mu_m}D^2(D^2+\mu_m^2)^{-1}.
```

Ihr Grundoperator ist

```math
D^2+\mu_0^2
=D^2+\frac14
=L_{1/2}.
```

Damit wird aus der Gamma-Schicht selbst

```math
\boxed{\sigma=\mu_0=1/2.}
```

erzwungen.

Die drei Mechanismen — P11 Prime-Ledger, NULLPOL und Gamma-Grundmodus — treffen daher auf **derselben eindeutig bestimmten Massenskala** zusammen.

---

# 5. Critical-half rigidity theorem

## Satz 5.1

Betrachte die natuerliche OU-/Green-Einparameterfamilie `e^{-sigma d}` auf dem logarithmischen Prim-Sternbaum und den zugehoerigen massiven Quellenoperator `L_sigma=D^2+sigma^2`. Fordere gleichzeitig:

1. die P11-Weil-Diagonalnormalisierung und den bereits erzwungenen Hubexponenten `beta=3/4`;
2. die exakte lokale Range-Identifikation mit den Nullpolbedingungen bei `s=0,1`;
3. Uebereinstimmung des Grundoperators mit der positiven Gamma-Resolventenleiter.

Dann existiert genau ein Parameter:

```math
\boxed{\sigma=\frac12.}
```

Jede der drei Bedingungen fixiert `sigma` bereits separat; ihre Gleichzeitigkeit ist daher kein Parameterfit.

### Bedeutung

Die Zahl `1/2` erscheint hier in vier algebraisch verschiedenen Rollen:

```text
critical Mellin midpoint / pole distance,
OU decay mass,
Prime-power AR(1) exponent,
Gamma resolvent ground mass.
```

Innerhalb der dokumentierten Familie sind diese Rollen exakt dieselbe Geometrie.

---

# 6. Schur-Untergrenze fuer jeden Gamma-Resolventenmodus

Setze fuer `mu>0`

```math
R_\mu=(D^2+\mu^2)^{-1}.
```

Der volle Linienkern ist

```math
R_\mu(x,y)=\frac1{2\mu}e^{-\mu|x-y|}.
```

Sei `v` in `[-a,a]` getragen. Dann ist fuer `x in [-a,a]`

```math
\int_{-a}^aR_\mu(x,y)dy
=
\frac{1-e^{-\mu a}\cosh(\mu x)}{\mu^2}
\le
\frac{1-e^{-\mu a}}{\mu^2}.
```

Der Schur-Test gibt daher

```math
\boxed{
\langle v,R_\mu v\rangle
\le
\frac{1-e^{-\mu a}}{\mu^2}\|v\|_2^2.
}
```

Da

```math
D^2(D^2+\mu^2)^{-1}
=I-\mu^2R_\mu,
```

folgt

```math
\boxed{
\left\langle v,
D^2(D^2+\mu^2)^{-1}v
\right\rangle
\ge e^{-\mu a}\|v\|_2^2.
}
```

Diese Ungleichung benutzt weder RH noch Weil-Positivitaet noch Nullpol.

---

# 7. Geschlossene archimedische Frame-Untergrenze

Mit `mu_m=2m+1/2` folgt durch Summation der positiven Moden

```math
\langle v,\Phi_\infty(D)v\rangle
\ge
S(a)\|v\|_2^2,
```

wobei

```math
\boxed{
S(a)
:=2\sum_{m=0}^\infty\frac{e^{-\mu_m a}}{\mu_m}.
}
```

Setze

```math
x=e^{-a/2}.
```

Dann

```math
S(a)
=4\sum_{m=0}^\infty\frac{x^{4m+1}}{4m+1}
=4\int_0^x\frac{dt}{1-t^4}.
```

Die elementare Stammfunktion liefert

```math
\boxed{
S(a)
=
\log\frac{1+e^{-a/2}}{1-e^{-a/2}}
+2\arctan(e^{-a/2}).
}
```

`S(a)` ist streng fallend in `a` und divergiert fuer `a downarrow0`.

---

# 8. Rein elementarer Zertifikatbereich `0<a<=1/16`

Fuer `a<=1/16` gilt

```math
2a<=1/8<\log2,
```

also ist noch kein Prime-Power-Atom aktiv und

```math
\Gamma_a=\kappa_*
=\log(8\pi)+\gamma+\frac\pi2.
```

Wegen der Monotonie genuegt `a=1/16`. Setze

```math
x=e^{-1/32}>1-\frac1{32}=\frac{31}{32}.
```

Dann

```math
\log\frac{1+x}{1-x}>\log63.
```

Ferner

```math
\frac\pi4-\arctan x
=\int_x^1\frac{dt}{1+t^2}
<1-x<\frac1{32},
```

also

```math
2\arctan x>\frac\pi2-\frac1{16}.
```

Daher

```math
S(1/16)
>
\log63+\frac\pi2-\frac1{16}.
```

Um dies mit `kappa_*` zu vergleichen, benutzen wir nur die elementaren Schranken

```math
\pi<\frac{22}{7},
\qquad
\gamma<\frac23.
```

Dann

```math
\frac{63}{8\pi}
>
\frac{441}{176}
>
\frac52.
```

Aus der positiven `artanh`-Reihe folgt

```math
\begin{aligned}
\log\frac52
&=2\operatorname{artanh}\frac37\\
&>2\left(\frac37+\frac1{3}\left(\frac37\right)^3\right)
=\frac{312}{343}.
\end{aligned}
```

Und exakt

```math
\frac{312}{343}-\frac23-\frac1{16}
=\frac{2971}{16464}>0.
```

Somit

```math
\boxed{
S(1/16)>\kappa_*.
}
```

Also fuer jedes `0<a<=1/16` und jedes nichttriviale `v in C_c^infty(-a,a)`:

```math
\boxed{
\|\mathcal X_av\|^2
\ge
\langle v,\Phi_\infty(D)v\rangle
\ge
S(a)\|v\|_2^2
>
\Gamma_a\|v\|_2^2.
}
```

Insbesondere gilt auf NULLPOL strikt

```math
\boxed{
Q_W(v)>0
\qquad(0<a<=1/16,\ v\ne0).
}
```

Status:

```text
CRIT-HALF-SCHUR local NP-GAP on 0<a<=1/16  ✓[M]
```

### Literatur-/Neuheitsfirewall

Dieser Radius wird **nicht** als neuer Rekord oder Publikationsneuheit beansprucht. Unkonditionale lokale Weil-Positivitaet ist aus der Literatur fuer wesentlich groessere Fenster bekannt. Der Satz dient hier als forward analytic certificate dafuer, dass die neue Critical-half-Resolventenstruktur tatsaechlich einen Lower-Frame-Bound erzeugt, ohne bekannte Weil-Positivitaet rueckwaerts zu importieren.

---

# 9. Was dieser Durchlauf fuer Objekt X aendert

Vor diesem Durchlauf war der Common-Jump-Engpass ein zweifach momentbeschraenktes Frameproblem. Jetzt stehen zusaetzlich zur exakten Common-Jump-Geometrie drei neue harte Tatsachen zur Verfuegung:

1. `NULLPOL = Range(L_{1/2})` beseitigt die zwei Nebenbedingungen durch einen lokalen positiven Quellenoperator.
2. Der P11 Prime-Power-/Hub-Ledger ist die logarithmische Abtastung des zugehoerigen Critical-half-OU-Kerns.
3. Die Gamma-Schicht beginnt exakt mit demselben Resolventenoperator und liefert per Schur-Test bereits eigenstaendig eine echte Lower-Frame-Schranke.

Die Route ist daher nicht mehr nur

```text
COMMON-JUMP -> abstract NP-GAP,
```

sondern

```text
COMMON-JUMP
 -> critical-half rigidity
 -> NULLPOL source lift L_{1/2}
 -> OU/tree Prime geometry
 -> Gamma resolvent ladder
 -> analytic frame estimates.
```

Das schliesst NP-GAP global nicht, liefert aber erstmals innerhalb dieser Route einen expliziten coerciven Mechanismus und ein rigoroses Positivitaetszertifikat.

---

# 10. Naechster Gate

Die kleine-Fenster-Schur-Schranke ist absichtlich grob. Der naechste sinnvolle Angriff ist nicht, ihren Radius numerisch zu optimieren, sondern die **Nullpol-/Range-Struktur** zu nutzen, die in §6--8 noch gar nicht verwendet wurde.

Prioritaet:

1. Schur-/Resolventenabschätzung nach `v=L_{1/2}u` statt fuer beliebiges `v`;
2. endliche erste Gamma-Moden lokal in der `L_{1/2}`-Metrik behandeln, Rest per Schur;
3. Prime-Jump-Energie ab dem ersten Cutoff nicht wegwerfen, sondern mit der Tree-/Root-Geometrie koppeln;
4. suchen, ob daraus ein radiusstabiler Lower-Frame-Mechanismus entsteht.

Ein Beweis fuer alle `a` bleibt RH-aequivalent und offen.
