# P11 / POS-DIL-2B — First exterior prime-shell positive repair at a=1/2

> **Stand:** 13. September 2026  
> **Rolle:** theorem-level interner Audit eines positiven intrinsischen Mass-Augmentationsbausteins nach dem POS-DIL-2A-No-Go; keine Registry-Promotion, keine volle Weil-Gram-Identität, kein Object-X-/RH-Abschluss.  
> **Basis:** `main@1eeb13277cc4d2beb3c0a17c96d5e0721bdc724a` nach Merge von PR #102.  
> **Scope:** `a=1/2`, Testfunktionen `H_0^1(-a,a)` mit Nullfortsetzung; positive Augmentation durch den geometrisch definierten **ersten äußeren Prime-Shift-Shell**. Die Buchungs-/Renormalisierungsfrage dieser zusätzlichen Kanäle in einer vollständigen Weil-Identität bleibt offen.

## 0. Kurzurteil

POS-DIL-2A bewies bei `a=1/2`, dass die vorhandene lokale positive Featureform `G_{1/2}^+` die minimale Rang-2-Masse

```math
\|\mathcal Ev\|^2
```

nicht mit Gain `1` tragen kann.

Der erste natürliche positive Reparaturversuch wird **nicht** über die numerische Größe des Defekts definiert, sondern rein geometrisch über die Shift-Lage der bereits vorhandenen Prime-Kanäle:

```math
\boxed{
\mathscr S_a^{\mathrm{out}}
=\{n=p^k:\ a<c_n\le2a\},
\qquad c_n=\frac12\log n.
}
```

Definiere

```math
\boxed{
H_a^{\mathrm{out}}(v,w)
=\sum_{n\in\mathscr S_a^{\mathrm{out}}}
\frac{\Lambda(n)}{\sqrt n}
\langle K_nv,K_nw\rangle.
}
```

Bei `a=1/2` gilt für **alle** Testfunktionen

```math
\boxed{
\|\mathcal Ev\|^2
< G_{1/2}^+(v)+H_{1/2}^{\mathrm{out}}(v).
}
```

Damit ist die augmentierte positive Form stark genug, um `R_0` als kontraktive Kreuzform zu tragen. Insbesondere ist der blockpolarisierte Schur-Baustein

```math
\boxed{
\begin{pmatrix}
G_{1/2}^++H_{1/2}^{\mathrm{out}} & R_0\\
R_0 & G_{1/2}^++H_{1/2}^{\mathrm{out}}
\end{pmatrix}
\succeq0.
}
```

Dies ist der erste positive Reparaturbaustein nach dem POS-DIL-2A-No-Go, der **vorwärts aus echten vorhandenen Prime-Kanälen** erzeugt wird.

**Firewall:** Das ist noch keine vollständige Object-X-/Weil-Realisierung. Insbesondere ist noch nicht erklärt, wie die hinzugefügten äußeren Prime-Kanäle in einer exakten vollen Weil-Buchung kompensiert/renormalisiert werden müssen.

---

## 1. Definition des ersten äußeren Shift-Shells

Für

```math
K_n=T_{c_n}-T_{-c_n},
\qquad
c_n=\frac12\log n
```

liegt der lokale Suzuki-Cutoff bei

```math
c_n\le a
\quad\Longleftrightarrow\quad
n\le e^{2a}.
```

Der **erste äußere geometrische Shell** wird durch die unmittelbar nächste Shift-Skala definiert:

```math
\boxed{
a<c_n\le2a.
}
```

Äquivalent:

```math
\boxed{
e^{2a}<n\le e^{4a}.}
```

Die Obergrenze `2a` wird also nicht aus einem gefitteten Defektwert gewählt, sondern als erste volle Shift-Schale außerhalb des Fensters.

---

## 2. Äußere Kanäle sind auf dem Fenster reine lokale Masse `✓[M]`

Sei `v` in `L^2(-a,a)` und außerhalb des Fensters durch Null fortgesetzt.

Für `c_n>a` liegen die Träger von

```math
T_{c_n}v
```

und

```math
T_{-c_n}v
```

bis auf Nullmengen disjunkt, denn ihre Träger liegen in Intervallen mit Radius `a` und Mittelpunkten `-c_n` beziehungsweise `+c_n`, deren Abstand `2c_n>2a` ist.

Daher

```math
\begin{aligned}
\|K_nv\|_2^2
&=\|T_{c_n}v-T_{-c_n}v\|_2^2\\
&=\|T_{c_n}v\|_2^2+\|T_{-c_n}v\|_2^2\\
&=2\|v\|_2^2.
\end{aligned}
```

Also für jeden äußeren Shell-Kanal exakt

```math
\boxed{\|K_nv\|_2^2=2\|v\|_2^2.}
```

Mit

```math
w_n=\frac{\Lambda(n)}{\sqrt n}
```

folgt

```math
\boxed{
H_a^{\mathrm{out}}(v)
=2B_a^{\mathrm{out}}\|v\|_2^2,
\qquad
B_a^{\mathrm{out}}
=\sum_{n\in\mathscr S_a^{\mathrm{out}}}w_n.
}
```

Dies ist intrinsische Prime-Masse, keine von Hand eingesetzte Diagonalform: die Skalarmasse ist die exakte Restriktion echter Prime-Kanalnormen auf das Fenster.

---

## 3. Spezialisierung auf a=1/2

Setze

```math
a=\frac12.
```

Dann

```math
\mathscr S_{1/2}^{\mathrm{out}}
=\{n=p^k:\ e<n\le e^2\}.
```

Für den folgenden unteren Bound genügt es, die drei positiven Shell-Mitglieder

```math
3,\ 4,\ 5
```

zu verwenden.

Sie liegen tatsächlich im Shell:

- `e<3`, also `3,4,5>e`;
- `e>1+1+1/2=5/2`, also `e^2>25/4>5`.

Alle drei sind Prime Powers.

Daher

```math
B_{1/2}^{\mathrm{out}}
\ge
\frac{\log3}{\sqrt3}
+\frac{\log2}{2}
+\frac{\log5}{\sqrt5}.
```

---

## 4. Vorhandener Log-Multiplikator liefert bereits log 2 lokale Masse

Der positive Log-Multiplikator in `G_a^+` ist

```math
L_a(v)
=-\frac12\int_{-a}^a
\log(a^2-x^2)|v(x)|^2dx.
```

Bei `a=1/2` gilt für jedes `|x|<1/2`

```math
\frac14-x^2\le\frac14,
```

also

```math
-\frac12\log\left(\frac14-x^2\right)
\ge
-\frac12\log\frac14
=\log2.
```

Somit

```math
\boxed{
L_{1/2}(v)\ge(\log2)\|v\|_2^2.
}
```

Da alle übrigen Komponenten von `G_{1/2}^+` nichtnegativ sind,

```math
\boxed{
G_{1/2}^+(v)
\ge(\log2)\|v\|_2^2.
}
```

---

## 5. Elementarer rationaler Lower Bound für die augmentierte Masse

Es gelten die strikten elementaren Abschätzungen

```math
\log2>\frac12,
```

weil für `0<x<1`

```math
e^x=\sum_{m\ge0}\frac{x^m}{m!}
<\sum_{m\ge0}x^m=\frac1{1-x},
```

also `e^{1/2}<2`.

Weiter

```math
\frac{\log3}{\sqrt3}>\frac12,
```

weil `e<3` und `sqrt3<2`.

Außerdem

```math
\frac{\log2}{2}>\frac14.
```

Schließlich

```math
\frac{\log5}{\sqrt5}>\frac13,
```

weil `e<5`, also `log5>1`, und `sqrt5<3`.

Daher

```math
\begin{aligned}
G_{1/2}^+(v)+H_{1/2}^{\mathrm{out}}(v)
&\ge
\left(
\log2
+2B_{1/2}^{\mathrm{out}}
\right)\|v\|_2^2\\
&>
\left(
\frac12
+2\left(\frac12+\frac14+\frac13\right)
\right)\|v\|_2^2\\
&=\frac83\|v\|_2^2.
\end{aligned}
```

Also

```math
\boxed{
G_{1/2}^+(v)+H_{1/2}^{\mathrm{out}}(v)
>\frac83\|v\|_2^2.
}
```

---

## 6. Universeller Moment-Upper-Bound

Durch Cauchy-Schwarz:

```math
|E_+(v)|^2
\le
\left(\int_{-a}^a e^x dx\right)\|v\|_2^2
=2\sinh(a)\|v\|_2^2.
```

Ebenso

```math
|E_-(v)|^2
\le2\sinh(a)\|v\|_2^2.
```

Damit allgemein

```math
\boxed{
\|\mathcal Ev\|^2
\le4\sinh(a)\|v\|_2^2.
}
```

Für `a=1/2` verwenden wir die positive Reihe

```math
\sinh x
=\sum_{j\ge0}\frac{x^{2j+1}}{(2j+1)!}
<\sum_{j\ge0}x^{2j+1}
=\frac{x}{1-x^2}
```

für `0<x<1`. Bei `x=1/2`:

```math
\sinh\frac12<\frac{2}{3}.
```

Also

```math
\boxed{
\|\mathcal Ev\|^2
<\frac83\|v\|_2^2.
}
```

---

## 7. Theorem — erster äußerer Shell repariert den unit-gain Defekt bei a=1/2 `✓[M]`

Aus §§5–6 folgt für jedes nichttriviale zulässige `v`

```math
\boxed{
\|\mathcal Ev\|^2
<
G_{1/2}^+(v)+H_{1/2}^{\mathrm{out}}(v).
}
```

Für `v=0` gilt Gleichheit `0=0`.

Somit gilt auf der ganzen Testklasse die nichtstrikte Form

```math
\boxed{
\|\mathcal Ev\|^2
\le
A_{1/2}^{\mathrm{out}}(v),
\qquad
A_{1/2}^{\mathrm{out}}
:=G_{1/2}^++H_{1/2}^{\mathrm{out}}.
}
```

Dies ist genau die unit-gain Dominanz, die POS-DIL-2A für `G_{1/2}^+` allein ausgeschlossen hatte.

---

## 8. R_0 sitzt kontraktiv in der augmentierten positiven Form `✓[M]`

Da

```math
R_0(v,w)=\langle\mathcal Ev,J\mathcal Ew\rangle,
\qquad \|J\|=1,
```

gilt

```math
|R_0(v,w)|
\le
\|\mathcal Ev\|\,\|\mathcal Ew\|.
```

Mit §7:

```math
\boxed{
|R_0(v,w)|
\le
\sqrt{A_{1/2}^{\mathrm{out}}(v)}
\sqrt{A_{1/2}^{\mathrm{out}}(w)}.
}
```

Damit ist `R_0` eine kontraktive Hermiteform relativ zur explizit positiven augmentierten Form `A_{1/2}^{out}`.

---

## 9. Positiver Schur-/Blockbaustein `✓[M]`

Betrachte die Form auf Paaren `(v,w)`:

```math
\mathfrak B_{1/2}^{\mathrm{out}}((v,w))
=A_{1/2}^{\mathrm{out}}(v)
+A_{1/2}^{\mathrm{out}}(w)
+2\operatorname{Re}R_0(v,w).
```

Aus §8 folgt

```math
\begin{aligned}
\mathfrak B_{1/2}^{\mathrm{out}}((v,w))
&\ge
A_{1/2}^{\mathrm{out}}(v)
+A_{1/2}^{\mathrm{out}}(w)
-2\sqrt{A_{1/2}^{\mathrm{out}}(v)A_{1/2}^{\mathrm{out}}(w)}\\
&=
\left(
\sqrt{A_{1/2}^{\mathrm{out}}(v)}
-
\sqrt{A_{1/2}^{\mathrm{out}}(w)}
\right)^2\\
&\ge0.
\end{aligned}
```

Also

```math
\boxed{
\begin{pmatrix}
A_{1/2}^{\mathrm{out}} & R_0\\
R_0 & A_{1/2}^{\mathrm{out}}
\end{pmatrix}
\succeq0.
}
```

Dies ist eine explizite positive Schur-Umgebung von `R_0` mit einer Diagonalmasse, die vollständig aus bereits vorhandenen positiven Featurekanälen stammt.

---

## 10. Feature-factor Korollar

Sei `F_{1/2}^{out}` eine direkte Hilbert-Featureabbildung, die die positiven Komponenten von

```math
A_{1/2}^{out}=G_{1/2}^++H_{1/2}^{out}
```

sammelt, also

```math
\|F_{1/2}^{out}v\|^2=A_{1/2}^{out}(v).
```

POS-DIL-1 liefert eine Prime-moment-Abbildung `V` mit

```math
\|Vv\|^2=\|\mathcal Ev\|^2.
```

Aus §7 folgt

```math
\|Vv\|\le\|F_{1/2}^{out}v\|.
```

Daher ist die Abbildung auf dem Range

```math
F_{1/2}^{out}v\mapsto Vv
```

wohldefiniert und kontraktiv; sie besitzt die kanonische Nullfortsetzung auf das orthogonale Komplement des abgeschlossenen Feature-Ranges.

Wichtig: Diese Faktorisation wird **nicht** aus bekannter Weil-Positivität oder `Q_{B_a}` rückwärts gewonnen. Ihre Kontraktivität folgt aus der expliziten vorwärts bewiesenen Prime-Shell-Dominanz.

---

## 11. Warum dies nicht die alte „beliebige Diagonalmasse“ ist

Die Zusatzmasse ist nicht als

```math
tI
```

mit passend gewähltem `t` eingesetzt worden.

Stattdessen:

1. die zulässigen Kanäle sind die bereits vorhandenen echten Prime-Kanäle `K_n`;
2. die Shell-Klasse wird ausschließlich durch die Shift-Geometrie `a<c_n<=2a` definiert;
3. ihre Koeffizienten sind die kanonischen Weilgewichte `w_n=Lambda(n)/sqrt(n)`;
4. die resultierende lokale Skalarmasse `2B_a^{out}I` ist ein **Theorem** aus der Disjunktheit der verschobenen Fenster, nicht eine Definition.

Dies erfüllt die POS-DIL-Forderung nach intrinsischer positiver Masse im hier bewiesenen Radius-Scope.

---

## 12. Harte Firewalls

Nicht bewiesen ist:

1. dass derselbe erste Außenshell für **alle** `0<a<=1` die Momentmasse dominiert;
2. eine radienuniforme Aussage;
3. dass die äußeren Shell-Kanäle ohne weitere Kompensation in die exakte vollständige Suzuki-/Weilform aufgenommen werden dürfen;
4. dass ihre lokale Skalarmasse mit `c_aI` identisch ist;
5. eine Erklärung des `r_1`-Blocks;
6. eine vollständige Prime-/Archimedean-Weil-Gram-Identität;
7. Object X oder RH.

Insbesondere ist die noch offene **Buchungsfrage** zentral: Kanäle mit `c_n>a` treten in der lokalisierten Suzuki-Normalform als reine lokale Masse auf und wurden dort durch die endliche Buchung/Cutoffstruktur nicht als Teil von `G_a^+` behalten. Eine Object-X-Konstruktion muss erklären, wie der positive Außenshell in der vollen Identität bilanziert wird, statt ihn nur additiv anzuhängen.

---

## 13. Neue Front — POS-DIL-2C / SHELL-BOOKING-AND-RADIUS

Der nächste Gate zerfällt in zwei gekoppelte Fragen:

### 13.1 Radiusfrage

Für welche Radien `0<a<=1` gilt für den geometrisch definierten ersten Außenshell

```math
\|\mathcal Ev\|^2
\le
G_a^+(v)+H_a^{out}(v)
```

auf der ganzen Testklasse?

### 13.2 Buchungsfrage

Kann `H_a^{out}` in einer **exakten** gemeinsamen Prime-/Archimedean-Geometrie so eingebaut werden, dass keine künstliche Zusatzenergie erzeugt wird und die volle Weilform unverändert bleibt?

Diese zweite Frage ist wichtiger als ein bloßer weiterer Positivitätssweep.

Naheliegende Prüfpunkte:

- Zusammenhang der reinen Außenkanalmasse mit der bereits bekannten lokalen Identitätsmasse aus Kanälen `c_n>a`;
- Verhältnis zur AR(1)-Root/Hub-Zerlegung;
- ob eine telescopische Shell-Differenz oder Root/Hub-Gegenbuchung die Zusatzmasse natürlich bilanziert;
- erst danach mögliche Verbindung zum offenen Skalarblock `c_aI`.

---

## 14. Statusbuchung

```text
POS-DIL-2A unit-gain existing-G no-go at a=1/2        ×[M]
first exterior shell pure-mass identity                ✓[M]
first exterior shell unit-gain repair at a=1/2         ✓[M]
contractive R_0 Schur block after shell augmentation   ✓[M]
OX-GEN-A2' overall                                     ✓[M]_part
POS-DIL-2C radius extension                            ?[O]
POS-DIL-2C exact shell booking / renormalization       ?[O]
r_1 / c_aI / full Object-X realization / RH            ?[O]
```

Keine Registry-Promotion aus diesem Audit allein.