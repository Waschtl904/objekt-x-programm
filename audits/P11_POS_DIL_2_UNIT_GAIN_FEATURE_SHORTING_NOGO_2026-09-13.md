# P11 / POS-DIL-2 — Unit-gain feature-shorting no-go at a=1/2

> **Stand:** 13. September 2026  
> **Rolle:** theorem-level interner Audit des nach POS-DIL-1 vorab definierten FEATURE-SHORTING-Gates; keine Registry-Promotion, kein Object-X-/RH-Abschluss.  
> **Basis:** `main@ecf8216f3d66c9b0be6636afea216bdfd53142ac` nach Merge von PR #101.  
> **Scope:** lokalisierte positive Suzuki-/OX-GRAM-Featureform `G_a^+` bei `a=1/2`, Testklasse `H_0^1(-a,a)`, Nullfortsetzung für Prime-Kanäle. Ausgeschlossen wird die **unit-gain kontraktive** Feature-Shorting-/Target-observable-Klasse. Nicht ausgeschlossen werden positive Erweiterungen mit zusätzlicher intrinsischer Masse, Gain `>1` oder veränderter Featuregeometrie.

## 0. Kurzurteil

POS-DIL-1 erzeugt die minimale positive Rang-2-Masse

```math
\|\mathcal Ev\|^2=|E_+(v)|^2+|E_-(v)|^2
```

und realisiert zugleich

```math
R_0(v,w)=\langle V_Nv,\mathbb P_NV_Nw\rangle
```

im selben positiven Prime-moment-Zielraum.

Der anschließend **vorab definierte** POS-DIL-2-Gate fragte, ob diese Masse kontraktiv in der bereits vorhandenen positiven Featureform `G_a^+` sitzt, insbesondere ob

```math
\|\mathcal Ev\|^2\le G_a^+(v)
```

gilt bzw. ob ein kontraktives Target-Shorting existiert.

Bei

```math
a=\frac12
```

ist die Antwort exakt **nein**.

Es gibt eine explizite Folge reeller gerader Funktionen

```math
v_\varepsilon\in H_0^1\!\left(-\frac12,\frac12\right)
```

für die

```math
|R_0(v_\varepsilon,v_\varepsilon)|
>G_{1/2}^+(v_\varepsilon)
```

für alle hinreichend kleinen `epsilon>0`.

Damit ist nicht nur die spezielle Prime-moment-Postkompression als Kontraktor ausgeschlossen. Es gibt **keinen** Hilbertraum-Featureoperator `F` mit

```math
\|Fv\|^2=G_{1/2}^+(v)
```

und keinen Zielraumoperator `A` mit `||A||<=1`, der

```math
R_0(v,w)=\langle Fv,AFw\rangle
```

auf der Testklasse realisiert.

Status dieser unit-gain Klasse:

```text
\boxed{\times[M]}
```

---

## 1. Benutzte Formeln

Für `a<=1` lautet die positive Featureform

```math
G_a^+(v)
=\frac14\iint_{(-a,a)^2}
\frac{|v(x)-v(y)|^2}{|x-y|}\,dx\,dy
+\sum_{n\le e^{2a}}\frac{\Lambda(n)}{\sqrt n}\|K_nv\|_2^2
-\frac12\int_{-a}^a\log(a^2-x^2)|v(x)|^2\,dx.
```

Die Prime-Kanäle sind

```math
K_n=T_{\frac12\log n}-T_{-\frac12\log n}
```

auf der Nullfortsetzung.

Für reelle gerade `v` gilt

```math
E_+(v)=E_-(v)
```

und deshalb

```math
\boxed{
R_0(v,v)=-2E_+(v)^2=-\|\mathcal Ev\|^2.
}
```

Somit ist bei geraden reellen Testfunktionen jede kontraktive Target-Realisierung von `R_0` notwendigerweise an die Diagonalbedingung

```math
\boxed{\|\mathcal Ev\|^2\le G_a^+(v)}
```

gebunden.

---

## 2. Plateaufolge in H_0^1

Setze

```math
a=\frac12,
\qquad
I=(-a,a).
```

Für `0<epsilon<a` definiere die gerade reelle Plateau-Funktion

```math
v_\varepsilon(x)=
\begin{cases}
1, & |x|\le a-\varepsilon,\\
\dfrac{a-|x|}{\varepsilon}, & a-\varepsilon<|x|<a,\\
0, & |x|\ge a.
\end{cases}
```

Dann

```math
v_\varepsilon\in H_0^1(I),
\qquad 0\le v_\varepsilon\le1,
```

und für

```math
v_0=1_I
```

gilt

```math
v_\varepsilon\to v_0
```

punktweise und in `L^2(R)`.

Der Punkt `v_0` selbst wird **nicht** als Testvektor verwendet; er dient nur zur Berechnung der Grenzwerte einer zulässigen `H_0^1`-Folge.

---

## 3. Die logarithmische Douglasenergie verschwindet

Schreibe

```math
\mathcal D(v)
=\frac14\iint_{I^2}
\frac{|v(x)-v(y)|^2}{|x-y|}\,dx\,dy.
```

Sei

```math
B_\varepsilon
=\{x\in I: |x|>a-\varepsilon\}.
```

Dann `|B_epsilon|=2epsilon` und außerhalb `B_epsilon` ist `v_epsilon` konstant.

Außerdem ist `v_epsilon` global `1/epsilon`-Lipschitz auf `I` und zwischen `0` und `1`. Daher

```math
|v_\varepsilon(x)-v_\varepsilon(y)|^2
\le
\min\!\left(1,\frac{|x-y|^2}{\varepsilon^2}\right).
```

Da nur Paare mit mindestens einem Punkt in `B_epsilon` beitragen,

```math
4\mathcal D(v_\varepsilon)
\le
2\int_{B_\varepsilon}\int_I
\min\!\left(\frac1{|x-y|},\frac{|x-y|}{\varepsilon^2}\right)
\,dy\,dx.
```

Die Intervalllänge ist `1`. Für jedes feste `x` ist deshalb grob

```math
\int_I
\min\!\left(\frac1{|x-y|},\frac{|x-y|}{\varepsilon^2}\right)dy
\le
2\int_0^1\min\!\left(\frac1h,\frac h{\varepsilon^2}\right)dh
=1+2\log\frac1\varepsilon.
```

Folglich

```math
\boxed{
0\le\mathcal D(v_\varepsilon)
\le
\varepsilon\left(1+2\log\frac1\varepsilon\right)
\longrightarrow0.
}
```

Damit ist der Grenzvektor kein versteckter Douglas-Randenergieeffekt.

---

## 4. Exponentialmomente und R_0-Grenzwert

Auf dem kompakten Intervall konvergieren die Momente durch dominierte Konvergenz:

```math
E_\pm(v_\varepsilon)\longrightarrow E_\pm(v_0).
```

Wegen der Geradheit sind beide gleich und

```math
E_+(v_0)
=\int_{-1/2}^{1/2}e^{x/2}dx
=4\sinh\frac14.
```

Daher

```math
\boxed{
\|\mathcal Ev_\varepsilon\|^2
\longrightarrow
32\sinh^2\frac14.
}
```

und

```math
\boxed{
R_0(v_\varepsilon,v_\varepsilon)
\longrightarrow
-32\sinh^2\frac14.
}
```

---

## 5. Aktive Prime-Kanäle bei a=1/2

Hier ist

```math
e^{2a}=e.
```

Da

```math
2<e<3,
```

ist die einzige Prime-Power mit `n<=e` genau

```math
n=2.
```

Setze

```math
c_2=\frac12\log2.
```

Da `log2<1`, ist `c_2<a`. Für den Grenzindikator `v_0=1_I` sind `T_{c_2}v_0` und `T_{-c_2}v_0` Indikatoren zweier Einheitsintervalle, deren Mittelpunkte Abstand `2c_2` haben. Ihre symmetrische Differenz hat Maß `4c_2`. Also

```math
\boxed{
\|K_2v_0\|_2^2=4c_2=2\log2.
}
```

Da Translationen auf `L^2(R)` unitär und `K_2` beschränkt sind,

```math
\|K_2v_\varepsilon\|_2^2
\longrightarrow
2\log2.
```

Mit

```math
w_2=\frac{\log2}{\sqrt2}
```

folgt für den Prime-Block

```math
\boxed{
w_2\|K_2v_\varepsilon\|_2^2
\longrightarrow
\sqrt2\,(\log2)^2.
}
```

---

## 6. Log-Multiplikator-Grenzwert

Der nichtnegative Gewichtsfaktor

```math
-\frac12\log\left(\frac14-x^2\right)
```

ist auf `I` integrierbar. Da `0<=v_epsilon<=1`, liefert dominierte Konvergenz

```math
-\frac12\int_I\log\left(\frac14-x^2\right)|v_\varepsilon(x)|^2dx
\longrightarrow
-\frac12\int_I\log\left(\frac14-x^2\right)dx.
```

Allgemein gilt

```math
\int_{-a}^a\log(a^2-x^2)dx
=4a\bigl(\log(2a)-1\bigr).
```

Für `a=1/2` daher

```math
\boxed{
-\frac12\int_{-1/2}^{1/2}
\log\left(\frac14-x^2\right)dx=1.
}
```

---

## 7. Exakter Grenzwert der positiven Featureform

Aus §§3,5,6 folgt

```math
\boxed{
G_{1/2}^+(v_\varepsilon)
\longrightarrow
1+\sqrt2\,(\log2)^2.
}
```

Dagegen gilt aus §4

```math
\boxed{
|R_0(v_\varepsilon,v_\varepsilon)|
\longrightarrow
32\sinh^2\frac14.
}
```

---

## 8. Strikte elementare Trennung

Es wird keine Dezimalarithmetik benötigt.

Zunächst

```math
32\sinh^2\frac14
=16\left(\cosh\frac12-1\right).
```

Aus der positiven Taylorreihe folgt strikt

```math
\cosh\frac12>1+\frac{(1/2)^2}{2}=1+\frac18,
```

also

```math
\boxed{32\sinh^2\frac14>2.}
```

Weiter ist

```math
\sqrt2<\frac32.
```

Außerdem

```math
e^{3/4}
>1+\frac34+\frac{(3/4)^2}{2}
=\frac{65}{32}>2,
```

also

```math
\log2<\frac34.
```

Damit

```math
1+\sqrt2(\log2)^2
<1+\frac32\frac9{16}
=\frac{59}{32}
<2.
```

Somit exakt

```math
\boxed{
32\sinh^2\frac14
>
1+\sqrt2(\log2)^2.
}
```

Die Grenzlücke ist insbesondere positiv:

```math
\boxed{
\delta_0
:=32\sinh^2\frac14
-1-\sqrt2(\log2)^2
>0.
}
```

Die groben rationalen Schranken geben sogar

```math
\delta_0>\frac5{32}.
```

---

## 9. Theorem — unit-gain FEATURE-SHORTING ist unmöglich `×[M]`

Wegen der strikten Grenzlücke existiert `epsilon_0>0`, so dass für alle

```math
0<\varepsilon<\varepsilon_0
```

gilt

```math
\boxed{
|R_0(v_\varepsilon,v_\varepsilon)|
>
G_{1/2}^+(v_\varepsilon).
}
```

Insbesondere auch

```math
\boxed{
\|\mathcal Ev_\varepsilon\|^2
>
G_{1/2}^+(v_\varepsilon).
}
```

### Korollar 9.1 — kein kontraktives Prime-moment-Shorting

Sei `F_{1/2}^+` irgendeine typkorrekte Hilbert-Featureabbildung mit

```math
\|F_{1/2}^+v\|^2=G_{1/2}^+(v).
```

Dann existiert kein Operator `C` mit

```math
\|C\|\le1,
\qquad
CF_{1/2}^+v=V_{N_{1/2}}v
```

für alle Testfunktionen.

Denn dies würde

```math
\|\mathcal Ev\|^2
=\|V_{N_{1/2}}v\|^2
\le G_{1/2}^+(v)
```

erzwingen.

### Korollar 9.2 — kein kontraktives Target-observable für R_0

Es gibt allgemeiner keinen Hilbertraum `H`, keine Abbildung `F` mit

```math
\|Fv\|^2=G_{1/2}^+(v)
```

und keinen Operator `A` mit `||A||<=1`, so dass

```math
R_0(v,w)=\langle Fv,AFw\rangle_H
```

für alle Testfunktionen gilt.

Denn diagonal müsste

```math
|R_0(v,v)|\le G_{1/2}^+(v)
```

gelten, im Widerspruch zu den `v_epsilon`.

### Korollar 9.3 — kein positiver unit-diagonal Schurblock

Die Formmatrix

```math
\begin{pmatrix}
G_{1/2}^+ & R_0\\
R_0 & G_{1/2}^+
\end{pmatrix}
```

kann auf der Testklasse nicht positiv semidefinit sein. Der Gegenvektor folgt bereits aus der Diagonaldominanzverletzung.

---

## 10. Quantitative notwendige Zusatzmasse

Jede positive Augmentation `H>=0`, die eine unit-gain kontraktive Realisierung in der augmentierten Diagonalform

```math
G_{1/2}^++H
```

erlauben soll, muss entlang der Plateaufolge mindestens die fehlende Masse liefern:

```math
\boxed{
\liminf_{\varepsilon\downarrow0}H(v_\varepsilon,v_\varepsilon)
\ge\delta_0
=32\sinh^2\frac14-1-\sqrt2(\log2)^2.
}
```

Insbesondere

```math
\liminf H(v_\varepsilon,v_\varepsilon)>\frac5{32}.
```

Das ist ein **notwendiger** Massendefekt, keine Behauptung über seine richtige Quelle.

---

## 11. Was genau ausgeschlossen ist

Ausgeschlossen ist die nach POS-DIL-1 vorab definierte Klasse:

```text
bestehende positive Featuregeometrie G_a^+
        +
unit-gain contraction / target observable
        +
R_0 bzw. minimale E-Masse als Kompression
```

bereits bei `a=1/2`.

Nicht ausgeschlossen sind:

1. eine positive Erweiterung mit **zusätzlicher intrinsischer Masse**;
2. eine nicht-kontraktive Targetabbildung mit Gain `>1`;
3. eine andere, aber weiterhin vorwärts definierte positive Featuregeometrie;
4. zusätzliche AR(1)-Root/Hub-Komponenten;
5. globale Prime-Kanäle außerhalb des lokalen Suzuki-Cutoffs, sofern ihre Buchung nicht zirkulär ist;
6. eine spätere Kopplung mit `r_1` oder dem Skalarblock, sofern deren Vorzeichen und Herkunft korrekt behandelt werden;
7. irgendeine vollständige Object-X-Realisierung.

POS-DIL-1 bleibt vollständig unangetastet: Seine positive Prime-moment-Hilbertisierung existiert weiterhin. Das neue Resultat sagt nur, dass die **vorhandene** `G_{1/2}^+`-Masse nicht groß genug ist, um sie mit Gain `1` zu tragen.

---

## 12. Neue Front — POS-DIL-2B / INTRINSIC-MASS-AUGMENTATION

Der nächste nichtzirkuläre Gate lautet:

> **Welche schwächste bereits vorhandene positive Prime-/AR(1)-Root/Hub-/`log|D|`-Geometrie kann den exakt nachgewiesenen Massendefekt `delta_0` liefern, ohne die fertige Weilform, `Q_{B_a}`, RH oder eine rückwärts definierte Positivitätswurzel zu verwenden?**

Ein erfolgreicher Kandidat muss mindestens:

1. seine positive Zusatzmasse vorwärts aus vorhandenen Daten erzeugen;
2. am Plateau-Gate `a=1/2` die notwendige Masse `delta_0` liefern;
3. `R_0` im selben positiven Umraum tragen;
4. erklären, warum die Zusatzmasse nicht bloß eine beliebige Diagonalergänzung ist;
5. ihre Buchungsrichtung gegenüber dem offenen `c_aI`-Block sauber halten.

Naheliegende, aber noch **nicht** als Lösung gebuchte Inputs sind:

- AR(1)-Root/Hub-Komponente `u_k=q_p^k`;
- die in POS-DIL-1 gefundene Amplitude `1-u_k`;
- globale Prime-Kanäle jenseits des lokalen Suzuki-Cutoffs, die auf dem Fenster reine lokale Masse tragen;
- logarithmische `log|D|`-Geometrie.

Beide Ausgänge bleiben offen: konstruktive intrinsische Massenergänzung oder ein enger weiterer Klassen-No-Go.

---

## 13. Statusbuchung

```text
POS-DIL-1 prime-moment Hilbertization                    ✓[M]
POS-DIL-2A unit-gain feature shorting at a=1/2          ×[M]
contractive target-observable R_0 inside G_{1/2}^+      ×[M]
unit-diagonal Schur block using existing G_{1/2}^+      ×[M]
necessary plateau mass deficit delta_0>0                ✓[M]
OX-GEN-A2' overall                                      ✓[M]_part
POS-DIL-2B / INTRINSIC-MASS-AUGMENTATION               ?[O]
r_1 / c_aI / full Object-X realization / RH             ?[O]
```

Keine Registry-Promotion aus diesem Audit allein.