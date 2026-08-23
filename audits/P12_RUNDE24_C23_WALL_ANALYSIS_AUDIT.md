# P12 Runde 24 — systematische C23-Wandanalyse und nächste Quellschale

**Status:** Audit-/Theorem-Kandidaten; **nicht promotet**.  
**Repo-Basis:** `Waschtl904/objekt-x-programm`, `main@c5f91fe07d4c1fac45ec83d769ddf13d8d1f6f41`.  
**Eingang:** A15.1b2g / Round 23, exakter 42×42-C23-Seed `✓[M]_part`.  
**Firewall:** P11 FROZEN; R14 unverändert; keine Aussage zu Polar Gauge, Terminal Transport, Objekt X oder RH.

---

## 0. Ziel und Ergebnis in einem Satz

Die sechs C23-Wandfamilien wurden aus dem kanonischen Rohoperator

\[
Lh(u)=
p[h(u-a)-h(u+a)]
+r[h(u-b)-h(u+b)]
+q[h(u-T)-h(u+T)]
\]

neu rekonstruiert.

Die wichtigsten Resultate sind:

1. \(R=\omega\), \(x=\eta\) und \(x=\chi\) sind **keine Rohoperator-Facetten des ausgewählten 42-Zeilen-Blocks**.
2. Der unveränderte Round-23-Block besitzt eine deutlich größere \(J\)-symmetrische Pattern-Kammer, die bis unter \(\omega\) reicht.
3. Die beiden echten Support-Wände
   \[
   \sigma+x=\kappa,\qquad \sigma-x=\eta
   \]
   lassen jeweils eine neue gepaarte Tail-Variable eintreten.
4. Genau dort existiert eine natürliche nächste Quellschale
   \[
   V_-=T+2\delta-x,\qquad V_+=T+x+\delta,
   \]
   die zu einem neuen exakt invertierbaren \(44\times44\)-System führt.
5. Die beiden Horizon-Wände
   \[
   \varepsilon+x=\kappa,\qquad \varepsilon=x+\eta
   \]
   sind für die aktuelle Konstruktion wesentlich härter: dort geht jeweils eine Zeile verloren, und eine exhaustive one-step-Suche findet keinen einzelnen Ersatzquellpunkt, dessen Zeile ausschließlich in den alten 42 Sichtbarkeitsvariablen lebt.

Keine neue kanonische \(R\)-Schwelle wird gebucht.

---

## 1. Konstanten und Involution

Wie bisher:

\[
\delta=\frac12\log\frac98,\qquad
e=\frac12\log\frac43,
\]
\[
\eta=e-2\delta,\qquad
\chi=3\delta-e,\qquad
\kappa=e-\delta.
\]

Es gelten exakt

\[
\boxed{\eta+\chi=\delta},
\qquad
\boxed{\kappa-\delta=\eta}.
\]

Die Round-23-Involution ist

\[
\boxed{J_x:x\mapsto\delta-x.}
\]

Für affine Gitterkoordinaten

\[
u=sx+me+n\delta
\]

wirkt sie als

\[
\boxed{
J(s,m,n)=(-s,m,n+s).
}
\]

Die 42 Round-23-Quellen sind unter \(J\) abgeschlossen: 21 negative und 21 positive Quellen bilden Paare. Ebenso bilden die 42 Sichtbarkeitsvariablen 21 \(J\)-Paare. In geeigneter Ordnung gilt exakt

\[
\boxed{
M_{42}=
\begin{pmatrix}
A_{21}&B_{21}\\
B_{21}&A_{21}
\end{pmatrix}.
}
\]

Dies ist die algebraische Grundlage der gesamten Wandanalyse.

---

# 2. Wandfamilie 1
## \(\omega<R<x<\sigma<\varepsilon<\varepsilon_{\max}\)

Diese Zeile enthält mehrere geometrisch verschiedene Hyperflächen.

### 2.1 \(R=\omega\)

**Rohoperator-Befund:** Keine der ausgewählten 42 Quellen wird hier horizon-legal oder illegal. Keine der 252 Rohslots trifft hier eine untere oder obere Supportgrenze.

Das ist strukturell zu erwarten: alle ausgewählten Quellen und ihre Shift-Slots haben \(s=\pm1\), daher tragen ihre unteren Support-Wände \(R\pm x=\text{Gitterkonstante}\); eine reine konstante Wand \(R=\omega\) kann für diesen Block nicht entstehen.

Der retained verifier bestätigt:

```text
OMEGA_NOT_M42_EVENT = PASS
```

Daher ist \(\omega\) **keine Facette des 42er-Rohblocks**.

### 2.2 \(x=R\)

Hier trifft die Sichtbarkeit \(h(x)\) selbst die untere Supportgrenze. Sechs Rohslots enthalten diese Koordinate.

Auf der Seite \(x<R\) ist \(h(x)\) bereits support-null. Algebraisch entsteht aus \(M_{42}\) der 42×41-Block, der durch Löschen der \(h(x)\)-Spalte erhalten wird. Da die Spalten von \(M_{42}\) unabhängig sind, besitzt dieser Block exakt vollen Spaltenrang 41.

Keine neue Quelle wird horizon-legal.

### 2.3 \(\sigma=x\)

Hier trifft

\[
T+x
\]

die obere Supportgrenze. Drei Rohslots ändern sich. Auf der Seite \(\sigma<x\) verschwindet genau die Spalte

\[
(1,4,2)=T+x.
\]

Wieder entsteht \(M_{42}\) mit einer Spalte weniger, also automatisch voller Spaltenrang 41.

Keine neue Quelle wird horizon-legal.

### 2.4 \(\sigma=\varepsilon\)

Dies ist keine unabhängige Facette der C23-Rohgeometrie. Aus

\[
\sigma-x<\eta
\]

und

\[
x+\eta<\varepsilon
\]

folgt bereits strikt

\[
\sigma<\varepsilon.
\]

### 2.5 \(\varepsilon=\varepsilon_{\max}\)

Der ausgewählte 42er-Block erfährt an dieser Hyperfläche keinen internen Pattern-Wechsel. Aber dies ist die arithmetische P12-Grenze

\[
T_0=c=\frac12\log5.
\]

Ein Überschreiten würde die nächste arithmetische Shift-Familie öffnen und liegt außerhalb des aktuellen P12-Drei-Shift-Satzes. Diese Wand wird **nicht** überschritten.

---

# 3. Wandfamilie 2
## \(\eta<x<\chi\)

Überraschend sind beide Grenzen keine Facetten des ausgewählten \(M_{42}\).

### 3.1 \(x=\eta\)

Es toggelt nur die bislang nicht verwendete Quellpaarung

\[
(1,-1,2):\quad u=x-\eta,
\]
\[
(-1,1,-2):\quad u=\eta-x.
\]

Für \(x>\eta\) ist die erste Quelle positiv/horizon-legal; für \(x<\eta\) die zweite. Die beiden rekonstruierten Rohzeilen sind nach odd reflection identisch.

**Wichtig:** Keine der 42 bereits verwendeten Zeilen ändert sich.

### 3.2 \(x=\chi\)

Analog toggelt

\[
(-1,-1,3):\quad u=\chi-x
\]

gegen

\[
(1,1,-3):\quad u=x-\chi.
\]

Auch hier bleibt der komplette 42×42-Block unverändert.

### 3.3 Konsequenz

Die ursprüngliche Bedingung

\[
\eta<x<\chi
\]

war für den 42er-Determinantenblock stärker als nötig.

Die tatsächlichen unteren versteckten Supportbedingungen sind

\[
\boxed{
\chi-R<x<\eta+R.
}
\]

Sie entsprechen

\[
|\chi-x|<R,\qquad |x-\eta|<R
\]

in der durch die übrigen Facetten festgelegten Orientierung.

---

# 4. Wandfamilie 3
## \(R+x<\delta<\sigma+x<\kappa\)

Hier liegen drei echte Ereignisse.

## 4.1 \(R+x=\delta\)

Die Koordinate

\[
D_0:=\delta-x
\quad\leftrightarrow\quad
(-1,0,1)
\]

trifft die untere Supportgrenze.

Sechs Rohslots verlieren diese Koordinate. Auf der Seite

\[
R+x>\delta
\]

ist der neue 42×41-Block exakt \(M_{42}\) ohne die \(D_0\)-Spalte.

Daher:

\[
\boxed{\operatorname{rank}=41}
\]

exakt, ohne neuen Determinantenfaktor.

Keine Quelle ändert ihre Horizon-Legalität.

## 4.2 \(\sigma+x=\delta\)

Die Koordinate

\[
T+\delta-x
\quad\leftrightarrow\quad
(-1,4,3)
\]

trifft die obere Supportgrenze.

Drei Rohslots verlieren diese Spalte. Auf der Seite

\[
\sigma+x<\delta
\]

entsteht wieder \(M_{42}\) mit genau einer Spalte weniger und damit voller Spaltenrang 41.

Keine Quelle ändert ihre Horizon-Legalität.

## 4.3 \(\sigma+x=\kappa\)

Dies ist die erste **genuine support-entry wall**.

Definiere

\[
\boxed{
U_-(x):=T+\kappa-x
}
\]

mit affinem Label

\[
U_-\leftrightarrow(-1,5,1).
\]

Im C23-Bereich gilt

\[
\sigma<\kappa-x<\varepsilon,
\]

also liegt \(U_-\) oberhalb des Supports, aber seine Quellgleichung ist horizon-legal.

Beim Überschreiten

\[
\sigma+x>\kappa
\]

wird \(U_-\) als neue Sichtbarkeitsvariable live. Konkret erhält die Zeile zur Quelle

\[
(-1,3,0)
\]

den zusätzlichen Term

\[
-p\,U_-.
\]

Der alte 42×42-Block bleibt als Untermatrix erhalten; es entsteht

\[
\boxed{42\times43,\qquad \operatorname{rank}=42.}
\]

Das ist ein exakter Rangdefekt von eins für den bisherigen Block.

### 4.3.1 Neue Hilfsquelle

Die natürliche nächste Quelle ist

\[
\boxed{
V_-(x):=T+2\delta-x
}
\]

mit Label

\[
\boxed{(-1,4,4)}.
\]

Sie ist horizon-legal, sofern

\[
2\delta-x<\varepsilon.
\]

Ihre Rohzeile reduziert sich in der relevanten Nachbarzelle exakt zu

\[
\boxed{
p\,h(-x+2e+3\delta)
+r\,h(-x+e+2\delta)
+q\,h(-x+2\delta)=0.
}
\]

In affinen Labels:

\[
\boxed{
\{(-1,2,3):p,\ (-1,1,2):r,\ (-1,0,2):q\}.
}
\]

Diese Zeile führt **keine neue Variable** ein und schließt den einseitigen 43×43-Block.

---

# 5. Wandfamilie 4
## \(\sigma-x=\eta\)

Dies ist exakt die \(J\)-Spiegelwand von 4.3.

Definiere

\[
\boxed{
U_+(x):=T+x+\eta
}
\]

mit Label

\[
U_+\leftrightarrow(1,5,0).
\]

C23 hält

\[
\sigma<x+\eta<\varepsilon.
\]

Beim Überschreiten

\[
\sigma-x>\eta
\]

tritt \(U_+\) als neue Supportvariable ein. Die Zeile zur Quelle

\[
(1,3,-1)
\]

erhält den neuen Term

\[
-p\,U_+.
\]

Es entsteht erneut

\[
\boxed{42\times43,\qquad \operatorname{rank}=42.}
\]

Die \(J\)-gespiegelte Hilfsquelle ist

\[
\boxed{
V_+(x):=T+x+\delta
}
\]

mit Label

\[
\boxed{(1,4,3)}.
\]

Sie ist horizon-legal, sofern

\[
x+\delta<\varepsilon.
\]

Ihre Rohzeile ist exakt

\[
\boxed{
\{(1,2,2):p,\ (1,1,1):r,\ (1,0,1):q\}.
}
\]

Auch sie führt in der Nachbarzelle keine neue Variable ein.

---

# 6. Wandfamilie 5
## \(\kappa<\varepsilon+x\)

Diese Bedingung ist äquivalent zu

\[
\kappa-x<\varepsilon.
\]

Sie sagt genau, dass die Quellposition

\[
U_-=T+\kappa-x
\]

noch unter dem Horizont liegt.

An der Wand

\[
\boxed{\varepsilon+x=\kappa}
\]

verliert die Quelle

\[
\boxed{(-1,5,1)}
\]

ihre Horizon-Legalität.

Auf der anderen Seite verschwindet genau diese eine Rohzeile. Die 42 alten Sichtbarkeitsvariablen bleiben bestehen:

\[
\boxed{41\times42,\qquad \operatorname{rank}=41.}
\]

Der Rang 41 ist exakt, weil 41 Zeilen eines invertierbaren 42×42-Blocks unabhängig bleiben.

### One-step-Ersatzsuche

Ein einzelner Ersatzquellpunkt, dessen nichtverschwindende Rohzeile ausschließlich in den alten 42 Variablen lebt, müsste einen Quellmittelpunkt besitzen, der um genau einen der Shifts \(a,b,T\) von \(\pm\) einer alten Sichtbarkeitskoordinate entfernt liegt.

Dies liefert eine **endliche exhaustive Kandidatenmenge von 142 Quellen**.

Im retained verifier gilt auf der Horizon-Loss-Seite:

```text
HORIZON_NO_SINGLE_OLDVAR_REPLACEMENT = PASS 142 candidates
```

Es existiert dort kein horizon-legales, nichttriviales Ein-Zeilen-Replacement innerhalb der alten Sichtbarkeitsmenge.

Dies ist **kein globaler No-Go-Satz**. Es bedeutet nur: die Horizon-Wand verlangt eine tiefere Quell-/Variablenschale als ein u15-artiges One-Step-Replacement.

---

# 7. Wandfamilie 6
## \(x+\eta<\varepsilon\)

Dies ist die \(J\)-Spiegelung von Wandfamilie 5.

An

\[
\boxed{\varepsilon=x+\eta}
\]

verliert

\[
\boxed{(1,5,0)}
\]

seine Horizon-Legalität.

Wieder entsteht

\[
\boxed{41\times42,\qquad \operatorname{rank}=41.}
\]

Die gleiche exhaustive 142-Quellen-One-Step-Suche liefert kein Ersatzrow, der ausschließlich in den alten 42 Variablen lebt.

Damit sind die beiden Horizon-Wände die derzeit härtesten echten Wände.

---

# 8. Die wahre \(42\)-Pattern-Kammer

Aus der vollständigen Rohslot-Inventur ergibt sich als natürliche \(J\)-symmetrische Erweiterung des Round-23-C23-Seeds folgende Kammer.

Für

\[
0<R<\rho
\]

sei

\[
\boxed{
R<x<\delta-R,
}
\tag{C42.1}
\]

\[
\boxed{
\chi-R<x<\eta+R,
}
\tag{C42.2}
\]

\[
\boxed{
\max\{x,\delta-x\}
<
\sigma
<
\min\{\kappa-x,x+\eta\},
}
\tag{C42.3}
\]

\[
\boxed{
\max\{\kappa-x,x+\eta\}
<
\varepsilon
<
\varepsilon_{\max}.
}
\tag{C42.4}
\]

Diese Bedingungen sind unter

\[
x\mapsto\delta-x
\]

invariant.

Der ursprüngliche C23-Bereich ist darin enthalten.

### 8.1 Kein \(\omega\)-Wall

Die neue Kammer enthält beispielsweise

\[
R=0.01,\qquad
x=\delta/2,\qquad
\sigma=0.04,\qquad
\varepsilon=0.07,
\]

obwohl

\[
0.01<\omega\approx0.01924026.
\]

An diesem Punkt rekonstruiert der Rohoperator **byte-for-byte dieselbe symbolische 42×42-Matrix** wie im committed Round-23-Seed.

Der retained verifier stresst 30000 zufällige Punkte in (C42.1)--(C42.4) und findet keine Pattern-Abweichung.

### 8.2 Die kleine Zahl unterhalb \(\omega\)

Die beiden versteckten unteren Supportintervalle können nur gleichzeitig offen sein, wenn

\[
\chi-R<\eta+R,
\]

also

\[
R>\frac{\chi-\eta}{2}.
\]

Dabei

\[
\boxed{
\frac{\chi-\eta}{2}
=
\frac14\log\frac{531441}{524288}
\approx0.00338775834459.
}
\]

Diese Zahl wird **nicht** als kanonische oder Operator-Schwelle gebucht.

Sie ist lediglich die Feasibility-Grenze der *festen 42-Quellen-Pattern-Kammer* (C42). Eine andere Quellschale kann darunter weiterreichen.

---

# 9. Neue symmetrische \(44\times44\)-Kammer hinter den Support-Wänden

Die beiden Support-Wände 4.3 und 5 können gemeinsam überschritten werden.

Dann liegen beide Moden

\[
U_-=T+\kappa-x,\qquad
U_+=T+x+\eta
\]

im Support.

Füge gleichzeitig die beiden \(J\)-gepaarten Quellen

\[
V_-=T+2\delta-x
\leftrightarrow(-1,4,4),
\]

\[
V_+=T+x+\delta
\leftrightarrow(1,4,3)
\]

hinzu.

Eine natürliche offene Kammer ist:

\[
\boxed{
R<x<\delta-R,
\qquad
\chi-R<x<\eta+R,
}
\tag{C44.1}
\]

\[
\boxed{
\max\{\kappa-x,x+\eta\}
<
\sigma
<
\min\{2\delta-x,x+\delta\},
}
\tag{C44.2}
\]

\[
\boxed{
\max\{2\delta-x,x+\delta\}
<
\varepsilon
<
\varepsilon_{\max}.
}
\tag{C44.3}
\]

Dort gibt es exakt 44 live Variablen und 44 horizon-legale Quellen.

## 9.1 Neue Involutionsstruktur

Die 44 Quellen sind wieder unter

\[
J(s,m,n)=(-s,m,n+s)
\]

abgeschlossen.

In 22+22-Paarordnung gilt exakt

\[
\boxed{
M_{44}
=
\begin{pmatrix}
A_{22}&B_{22}\\
B_{22}&A_{22}
\end{pmatrix}.
}
\]

Damit zerfällt die Algebra wieder in die \(J\)-geraden und \(J\)-ungeraden Sektoren.

## 9.2 Exakte Determinante

Symbolische Elimination liefert

\[
\boxed{
\det M_{44}
=
-p^{18}r^6(p-q)(p+q)\,G_-(p,q,r)\,G_+(p,q,r),
}
\]

wobei \(G_\pm\) homogen vom Grad 9 sind.

Mit

\[
\beta=q/p,\qquad v=(r/p)^2
\]

sind die normierten Faktoren ein Paritätspaar:

\[
\boxed{g_+(\beta,v)=g_-(-\beta,v).}
\]

Für die tatsächlichen P12-Gewichte zertifiziert dieselbe rationale
Intervallarithmetik wie in Round 23:

\[
\boxed{
g_-\in
(0.03770850382320942,\ 0.03770850382320942\ldots)
}
\]

und

\[
\boxed{
g_+\in
(0.6120433841588828,\ 0.6120433841588828\ldots).
}
\]

Beide sind strikt positiv. Außerdem

\[
p>q>0,\qquad r>0.
\]

Daher

\[
\boxed{\det M_{44}\ne0.}
\]

Somit ist (C44) ein echter neuer lokaler Kill-Kandidat hinter den beiden Support-Wänden.

Der retained verifier meldet:

```text
M44_J_BLOCK = PASS
M44_PARITY_FACTOR_INTERVALS = PASS
DET44_FACTOR = PASS
C44_PATTERN_STRESS = PASS 25000
```

---

# 10. Ranking der sechs Wandfamilien

| Wandfamilie | Rohoperator-Ereignis | Algebra nach Crossing | Urteil |
|---|---|---:|---|
| 1: \(\omega<R<x<\sigma<\varepsilon<\varepsilon_{\max}\) | \(R=\omega\): keines; \(x=R,\sigma=x\): Spaltenverlust | unverändert bzw. voller Spaltenrang | **leicht / teils keine echte Wand** |
| 2: \(\eta<x<\chi\) | nur unbenutzte lower-horizon Quellpaare toggeln | \(M_{42}\) unverändert | **leichteste Scope-Erweiterung** |
| 3: \(R+x<\delta<\sigma+x<\kappa\) | zwei Spaltenverluste; bei \(\sigma+x=\kappa\) Eintritt \(U_-\) | 42×43, aber mit \(V_-\) 43×43 schließbar | **sehr guter echter Wall-Kandidat** |
| 4: \(\sigma-x<\eta\) | Eintritt \(U_+\) | 42×43, mit \(V_+\) 43×43 schließbar | **Spiegel von 3; sehr guter Kandidat** |
| 5: \(\kappa<\varepsilon+x\) | Verlust der Quellzeile \(U_-\) | 41×42; kein one-step old-var replacement | **hart** |
| 6: \(x+\eta<\varepsilon\) | Verlust der Quellzeile \(U_+\) | 41×42; kein one-step old-var replacement | **hart** |

---

# 11. Empfohlener nächster Schritt

Es gibt zwei verschiedene Arten von Fortschritt.

## 11.1 Sofortiger Scope-Fortschritt

Die Bedingungen

\[
R>\omega,\qquad \eta<x<\chi
\]

sollten nicht länger als intrinsische C23-Wände behandelt werden.

Der saubere Ersatz ist die \(J\)-symmetrische C42-Kammer (C42.1)--(C42.4).

Das ist die risikoärmste nächste Promotion, weil **keine neue Determinante** benötigt wird: man verwendet exakt den bereits GREEN-geprüften \(M_{42}\).

## 11.2 Echte neue Mathematik

Die stärkste neue Konstruktion ist die gepaarte Support-Wall-Erweiterung mit

\[
V_-=T+2\delta-x,\qquad
V_+=T+x+\delta,
\]

und dem invertierbaren \(M_{44}\).

Sie ist algebraisch geschlossen, involutionssymmetrisch und besitzt rigoros nichtverschwindende Paritätsfaktoren.

### Empfehlung

Für den nächsten unabhängigen Review sollte Round 24 in zwei getrennten Verdicts geprüft werden:

- **R24-A:** C42-Scope-Erweiterung mit unverändertem Round-23-\(M_{42}\);
- **R24-B:** neue C44-Support-Wall-Kammer mit \(M_{44}\).

Die Horizon-Wände 5/6 bleiben danach die natürliche nächste Forschungsfront.

---

# 12. Strikter Status

Vor unabhängigem GREEN:

\[
\boxed{\text{R24-A C42 extension}: ?[O]\ \text{(theorem candidate)}}
\]

\[
\boxed{\text{R24-B C44 support-shell}: ?[O]\ \text{(local theorem candidate)}}
\]

Die One-Step-Negativdiagnose an den Horizon-Wänden ist nur eine
Konstruktionsaussage und kein globaler No-Go-Satz.

Keine Aussage zu Polar Gauge, Terminal Transport, Objekt X oder RH.
