# P11 Audit — RP2 zonal irreducibility and symmetry-average no-go

**Datum:** 15. September 2026  
**Basis:** RP2 transverse kernel + point-Weyl mixer audits.  
**Rolle:** theorem-level Staerke-/No-Go-Analyse des konkreten Rang-1-Mixers.  
**Registry:** unveraendert.  
**Nonclaim:** keine Object-X-Konstruktion, kein NP-GAP-/RH-Beweis, keine Publikationsneuheit.

---

## 0. Kurzurteil

Der Punkt-Weyl-Mixer

```math
M_y=|g_y\rangle\langle g_y|,
\qquad
g_y=P^{-2}\delta_y,
\qquad
P=\sqrt{\Delta_{RP^2}+1/4},
```

koppelt den P11-Grundzustand nicht nur an jede einzelne zonale Gamma-Stufe. Zusammen mit der Gamma-Massenleiter `P` entfernt er auf dem gesamten punktselektierten zonalen Sektor **jede nichttriviale Superselektion**.

Sei

```math
\mathcal Z_y
:=\overline{\bigoplus_{m\ge0}\mathbb C\zeta_{m,y}},
```

wobei `zeta_{m,y}` die normierte zonale Richtung im `m`-ten `RP^2`-Eigenspace ist. Dann gilt

```math
\boxed{
\{P|_{\mathcal Z_y},M_y|_{\mathcal Z_y}\}'
=\mathbb C I.
}
```

Aequivalent erzeugen ein beliebiger injektiver beschraenkter Spektraltransform von `P` (z.B. `(I+P)^{-1}`) und `M_y` in der von-Neumann-Abschliessung die volle Operatoralgebra

```math
\boxed{B(\mathcal Z_y).}
```

Der P11-Grundzustand `e_0=zeta_{0,y}` ist dabei zyklisch.

Gleichzeitig gilt ein scharfes Symmetrie-No-Go:

```math
\boxed{
\int_{RP^2}M_y\,dy=P^{-4}.
}
```

Das Isometrie-Mitteln der Punktwahl stellt also volle Symmetrie wieder her, zerstoert aber exakt die Nichtdiagonalitaet: `P^{-4}` kommutiert mit `P`.

Status:

```text
exact zonal coefficients of g_y                         ✓[M]
P + M_y irreducible on zonal ladder                    ✓[M]
W*( (I+P)^-1, M_y ) = B(Z_y)                           ✓[M]
P11 ground state cyclic for this algebra                ✓[M]
Isom-average int M_y dy = P^-4                         ✓[M]
averaging restores symmetry and kills mixing            ✓[M]
correct radius/source insertion into P11 Feshbach        ?[O]
Object X / NP-GAP / RH                                  ?[O]
```

---

# 1. Exakte Koeffizienten des Punkt-Green-Vektors

Aus dem Point-Weyl-Audit gilt

```math
\dim E_m=d_m=4m+1,
\qquad
\mu_m=2m+\frac12,
\qquad
d_m=2\mu_m,
```

und bei

```math
V=\operatorname{vol}(RP^2)=2\pi
```

ist

```math
\langle\zeta_{m,y},g_y\rangle
=\frac{\sqrt{d_m/V}}{\mu_m^2}.
```

Mit `d_m=2mu_m` und `V=2pi` folgt die besonders einfache Formel

```math
\boxed{
 c_m
:=\langle\zeta_{m,y},g_y\rangle
=\frac1{\sqrt\pi\,\mu_m^{3/2}}.
}
```

Insbesondere

```math
\boxed{c_m>0\quad\text{fuer alle }m.}
```

Somit

```math
\boxed{
g_y
=\sum_{m=0}^{\infty}
\frac1{\sqrt\pi\,\mu_m^{3/2}}\zeta_{m,y}}
```

mit Konvergenz in `L^2`.

Als Kontrolle:

```math
\|g_y\|^2
=\frac1\pi\sum_{m\ge0}\mu_m^{-3}<\infty.
```

---

# 2. Der zonale Gamma-Operator besitzt einfaches Spektrum

Auf

```math
\mathcal Z_y
=\overline{\operatorname{span}}
\{\zeta_{m,y}:m\ge0\}
```

gilt

```math
P\zeta_{m,y}=\mu_m\zeta_{m,y}.
```

Die Zahlen

```math
\mu_m=2m+1/2
```

sind paarweise verschieden. Also besitzt `P|_{Z_y}` einfaches reines Punktspektrum.

Zur Vermeidung von Domain-Fragen verwenden wir den beschraenkten Operator

```math
\boxed{R:=(I+P)^{-1}.}
```

Er besitzt dieselben Spektralprojektionen und die paarweise verschiedenen Eigenwerte

```math
r_m=(1+\mu_m)^{-1}.
```

---

# 3. Kommutantenbeweis der Irreduzibilitaet

Sei `A in B(Z_y)` und es gelte

```math
AR=RA,
\qquad
AM_y=M_yA.
```

Da `R` einfaches Spektrum besitzt, muss `A` diagonal in der zonalen Basis sein:

```math
A\zeta_{m,y}=a_m\zeta_{m,y}.
```

Der Mixer hat Matrixelemente

```math
\langle\zeta_{m,y},M_y\zeta_{n,y}\rangle
=c_mc_n.
```

Alle `c_m` sind strikt positiv. Aus `AM_y=M_yA` folgt fuer jedes `m,n`

```math
(a_m-a_n)c_mc_n=0.
```

Daher

```math
a_m=a_n
```

fuer alle `m,n` und somit

```math
\boxed{A=aI.}
```

Also

```math
\boxed{
\{R,M_y\}'=\mathbb C I.
}
```

Da `R` und `P` dieselben Spektralprojektionen besitzen, ist dies aequivalent zur entsprechenden Aussage fuer `P` im Spektralsinn.

---

# 4. Volle von-Neumann-Algebra auf dem zonalen Sektor

Nach dem Bikommutantensatz folgt unmittelbar

```math
\boxed{
W^*(R,M_y)=B(\mathcal Z_y).
}
```

Man kann dies auch konstruktiv sehen. Sei `E_m` jetzt die rang-eins Spektralprojektion von `R|_{Z_y}` auf `C zeta_m`. Dann

```math
E_mM_yE_n
=c_mc_n
|\zeta_{m,y}\rangle\langle\zeta_{n,y}|.
```

Da `c_mc_n !=0`, liegen nach Skalierung alle Matrixeinheiten

```math
|\zeta_m\rangle\langle\zeta_n|
```

in der von-Neumann-Algebra.

Damit ist die gesamte zonale Operatorgeometrie erzeugt.

### Firewall

Dies sagt **nicht**, dass die richtige Weil-/Object-X-Operatoralgebra gleich `B(Z_y)` sein soll. Der Satz misst nur die algebraische Staerke des konkreten Mixers und zeigt, dass im zonalen Gamma-Sektor keine Moden-Superselektion mehr uebrig bleibt.

---

# 5. Der P11-Grundzustand ist zyklisch

Aus dem vorigen Abschnitt folgt insbesondere

```math
E_mM_yE_0
=c_mc_0|\zeta_m\rangle\langle e_0|.
```

Daher liegt fuer jedes `m`

```math
\zeta_{m,y}
```

im Abschluss des Orbits der erzeugten Algebra auf `e_0`.

Somit

```math
\boxed{
\overline{W^*(R,M_y)e_0}=\mathcal Z_y.
}
```

Der bereits vorhandene P11-Grundzustand ist also ein zyklischer Startvektor fuer die komplette zonale Gamma-Leiter, sobald genau ein Punkt-Weyl-Mixer zugelassen wird.

---

# 6. Isometrie-Mittel des Mixers

Nun pruefen wir, ob man die Punktwahl durch Mittelung ueber `Y` eliminieren kann.

Fuer `f,h in L^2(Y)` gilt schwach

```math
\begin{aligned}
\left\langle f,
\left(\int_Y M_y\,dy\right)h\right\rangle
&=
\int_Y
\langle f,P^{-2}\delta_y\rangle
\langle P^{-2}\delta_y,h\rangle dy\\
&=
\int_Y
(P^{-2}f)(y)\overline{(P^{-2}h)(y)}dy\\
&=
\langle f,P^{-4}h\rangle.
\end{aligned}
```

Daher exakt

```math
\boxed{
\int_Y M_y\,dy=P^{-4}.
}
```

Da `P^{-4}` ein Spektralmultiplikator ist,

```math
[P^{-4},P]=0.
```

Die volle Isometriemittelung beseitigt somit genau die nichtdiagonale Information, die den Punktmixer interessant macht.

---

# 7. Symmetriebrechung ist unvermeidlich, aber gaugeartig

Die beiden bisherigen Saetze ergeben zusammen:

```text
voll Isom(RP2)-invariant  -> kein ground/excited mixing,
Punktwahl y               -> irreduzibles zonales mixing,
Mittel ueber y            -> P^-4, wieder diagonal.
```

Also kann die notwendige Transversalkopplung nicht zugleich als **linearer Mixer** voll `RP2`-isometrieinvariant sein.

Andererseits sind alle Punktwahlen durch Isometrien unitär konjugiert. Daher kann die Symmetriebrechung prinzipiell gaugeartig sein: Ein endgueltiges skalares/konjugationsinvariantes Observable koennte von `y` unabhaengig sein, obwohl eine konkrete Faktorisierung einen Punkt waehlt.

Ob genau dies in der P11-Feshbach-/Radiusgeometrie geschieht, ist offen.

---

# 8. Radiusneutralitaet des transversalen Mixers

Sei `H_R` der bereits typisierte raeumliche P11-Hub und betrachte die transversale Einbettung

```math
\widetilde H_Rf:=H_Rf\otimes e_0.
```

Setze den festen transversalen Vektor

```math
c_y:=M_ye_0.
```

Der gemischte Kanal ist

```math
Z_Rf:=H_Rf\otimes c_y.
```

Da `c_y` nicht von `R` abhaengt, gilt fuer jede Nullfortsetzungsmap `E_{R,S}` rein algebraisch

```math
\boxed{
Z_SE_{R,S}-(E_{R,S}\otimes I)Z_R
=
\bigl(H_SE_{R,S}-E_{R,S}H_R\bigr)\otimes c_y.
}
```

Damit fuehrt die RP2-Transversalkopplung **keinen neuen Radiusdefekt** ein. Sie loest aber ebenso wenig den bereits vorhandenen P11-Hub-/Feshbach-Transportdefekt.

Der offene Radius-Gate wird also nicht vergroessert, sondern exakt geerbt.

---

# 9. Konsequenz fuer die Object-X-Suche

Die Frage

```text
"Gibt es ueberhaupt einen nichtdiagonalen Gamma/P11-Mixer?"
```

ist innerhalb der RP2-Geometrie beantwortet:

```math
\boxed{\text{Ja: }M_y=|P^{-2}\delta_y\rangle\langle P^{-2}\delta_y|.}
```

Und auf dem zonalen Sektor ist dieser Mixer maximal stark im Sinne irreduzibler Operatorerzeugung.

Der verbleibende Gate ist wesentlich spezifischer:

```math
\boxed{
\text{Ist dieser Punkt-Weyl-Kanal aus der bereits vorhandenen}
\atop
\text{P11 Source/Rest/Hub-Feshbach-Geometrie kanonisch ableitbar?}
}
```

Wenn nein, ist `y` zusaetzliche, unbegruendete Geometrie.

Wenn ja, muss die Ableitung zugleich

```text
- die source-conditioned Randdegeneration,
- die connecting maps R<S,
- Exterior-before-overlap,
- und die globale finite-part-Renormierung
```

respektieren.

Erst dann wird aus algebraischer Ausdrucksstaerke ein echter Object-X-Baustein.
