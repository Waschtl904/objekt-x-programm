# P11/R32 — SW1-A10 Finite Cross-Gram Fiber Candidate

> **Stand:** 29. August 2026  
> **Stacked base:** research/sw1-a9-knf-separator@e727e067af228765219cbaaa1a717b80918b68c0  
> **Status:** ?[O] — A10-H0 Hub-Phasenalgebra zertifiziert; endliche Cross-Gram-Faser und Injektivität noch offen; keine Promotion.  
> **Scope:** Übergang von den in A9 endlichen freien KNF-Punktkomponenten zum eigentlichen Annulus-/Cross-Gram-Test. Kein HT-RED, kein Objekt X, keine RH-Folgerung.

---

## 0. Ziel und wichtigste Firewall

A9 liefert im kleinen unteren Subchamber

\[
0<\varepsilon<\varepsilon_*,
\qquad
\varepsilon_*:=\frac{6\Delta-L}{4},
\]

endliche physische Punktkomponenten des vollständigen freien KNF-Gramgraphen von

\[
\mathfrak G_R=J_R^*(I+A)J_R.
\]

Dies ist ein wesentlicher Fortschritt, aber noch **nicht** die Roadmap-A-Nichtentartung.

Denn \(\mathfrak G_R\) ist nach A3 ohnehin coerciv und invertierbar. Ein weiterer Beweis

\[
\det G_C\ne0
\]

auf einem endlichen Komponentenblock \(C\) würde daher lediglich bereits bekannte Positivität wiederholen.

Der eigentliche Zieloperator ist

\[
\boxed{
\mathcal L_{\rm ann}^{\rm SW1}
=
\left[
I-(I+A)J_R\mathfrak G_R^{-1}J_R^*
\right]
HE_{\mathcal A},
}
\tag{A10.1}
\]

mit

\[
\boxed{
\ker\mathcal L_{\rm ann}^{\rm SW1}
=
\ker(\mathscr M_I^*\mathscr M_A)
=
\ker\Gamma_I.
}
\tag{A10.2}
\]

A10 muss deshalb die **Annulusvariablen \(w\)** und die Hubkopplung in dieselbe endliche Faserstruktur einbauen.

---

## 1. Warum endliche freie Gramkomponenten allein nicht genügen

Setze für

\[
z_w:=HE_{\mathcal A}w
\]

die eindeutige freie Normalgleichung

\[
\mathfrak G_R\xi_w
=
J_R^*z_w.
\tag{A10.3}
\]

A3 gibt

\[
\xi_w
=
\mathfrak G_R^{-1}J_R^*z_w.
\]

Wenn die \(\mathfrak G_R\)-Punktkomponenten endlich sind, kann die linke Seite auf jeder solchen Komponente endlich gelöst werden.

Aber die Kernelbedingung lautet stärker:

\[
\boxed{
z_w=(I+A)J_R\xi_w.
}
\tag{A10.4}
\]

Die Normalgleichung A10.3 allein besagt nur, dass der Residualvektor

\[
z_w-(I+A)J_R\xi_w
\]

orthogonal zu \(K\) ist. Er muss zusätzlich **Null** sein.

Daher ist die relevante finite-level Nichtentartung nicht die Invertierbarkeit von \(\mathfrak G_R\), sondern die Injektivität des induzierten Annulus-/Cross-Gram-Residualblocks.

---

## 2. Hubterm

Für ungerades, auf dem Annulus nullfortgesetztes \(w\) gilt nach A1 exakt

\[
\boxed{
\begin{aligned}
(HE_{\mathcal A}w)(x)
={}&
p[w(x-a)-w(x+a)]\\
&+
r[w(x-b)-w(x+b)]\\
&+
q[w(x-T)-w(x+T)].
\end{aligned}
}
\tag{A10.5}
\]

Auf dem **signierten Annulus** sind dies sechs affine Source-Shifts

\[
x\mapsto x\pm a,
\qquad
x\mapsto x\pm b,
\qquad
x\mapsto x\pm T.
\]

---

## 3. A10-H0 — Phasenalgebra der sechs Hubshifts

Mit

\[
a=L+\Delta,
\qquad
T=2L+2\Delta,
\qquad
b=\frac32L+2\Delta
\]

folgen modulo \(L\):

### 3.1 \(a\)-Shifts

\[
\pm a\equiv\pm\Delta.
\]

Sie erhalten die Halbperiodenparität und ändern den lokalen Index um \(\pm1\).

### 3.2 \(T\)-Shifts

\[
\pm T\equiv\pm2\Delta.
\]

Sie erhalten die Parität und ändern den lokalen Index um \(\pm2\).

### 3.3 \(b\)-Shifts

\[
\pm b
\equiv
\frac L2\pm2\Delta
\pmod L.
\]

Sie wechseln die Parität und ändern den lokalen Index um \(\pm2\).

Damit besitzt die signierte Hubrelation maximale lokale Indexreichweite

\[
\boxed{2}
\]

und weiterhin nur dieselbe irrationale Basisrotation

\[
t_{n+1}=t_n+\Delta\pmod L.
\]

---

## 4. Odd-Folding

Falls der ungerade Annulus auf die positive Hälfte gefaltet wird, muss zusätzlich die Negation behandelt werden.

Wegen

\[
2b\equiv4\Delta\pmod L
\]

gilt exakt

\[
\boxed{
-P_{n,\eta}
=
\overline Q_{n+4,\eta}
\pmod L,
}
\tag{A10.6}
\]

und

\[
\boxed{
-\overline Q_{n,\eta}
=
P_{n-4,\eta}
\pmod L.
}
\tag{A10.7}
\]

Die Odd-Faltung erzeugt also ebenfalls **keine neue irrationale Phase**. Sie ist ein endlicher Blattwechsel mit Indexsprung \(4\).

Damit ist die natürliche A10-Arbeitsdarstellung entweder

1. der signierte Annulus mit Hubreichweite \(2\), oder
2. der positive Odd-Quotient mit zusätzlichem Negationssprung \(4\).

Für die exakte Frontierarbeit ist die signierte Darstellung zunächst vorzuziehen.

---

## 5. Zertifikat A10-H0

Zertifikat:

scripts/certify_sw1_a10_hub_phase_algebra.py

Commit:

c26a8922329877ebe7f7b7c1ca71dcf61605920b

Committed Script-Blob:

9c5eea6de4aa5a3ee3659d04c0ba11d3669c344a

Der aus GitHub gelesene Inhalt wurde lokal erneut nach dem Git-Blob-Verfahren gehasht und ergab exakt denselben SHA.

Ergebnis der committed Ausführung:

SW1-A10-H0 HUB PHASE ALGEBRA CERTIFICATE: PASS

Exakte Arithmetik: Python fractions.Fraction.

Damit:

\[
\boxed{
\mathrm{A10\!-\!H0}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate)}
}
\]

im expliziten Phasenalgebra-Scope.

---

## 6. Nächster notwendiger Knoten

Ein Annuluswert \(w(y)\) kann über mehrere der sechs Hubshifts an verschiedene freie Punkte gekoppelt sein.

Daher kann ein einzelner Annulusvertex zwei formal verschiedene A9-Gramkomponenten verbinden.

Der nächste korrekte Test ist somit **nicht** sofort ein Determinantentest, sondern:

\[
\boxed{
\text{A10-H1: vollständige zweistufige Hub-Inzidenzrelation}
}
\]

auf den freien Punkten.

Für zwei Hubinzidenzen

\[
y=x+c_i,
\qquad
y=\pm(x'+c_j),
\qquad
c_i,c_j\in\{\pm a,\pm b,\pm T\},
\]

entstehen

- Translationen aus \(c_i-c_j\);
- nach Odd-Identifikation Reflexionen aus \(-c_i-c_j\).

Diese Relation muss vollständig klassifiziert und gegen die A9-Separatoren geprüft werden.

Erst wenn die augmentierten freien+\(w\)-Komponenten endlich sind, ist eine echte finite-level Cross-Gram-Faser legitim.

---

## 7. Roadmap-A-Firewall

A10-H0 beweist **nicht**

\[
\ker\Gamma_I=\{0\}.
\]

Der aktuelle logische Stand ist:

\[
\boxed{
\begin{array}{ll}
\text{A9-FINITE-SMALL}
&
\text{freie KNF-Punktkomponenten endlich}
\\[1mm]
\Downarrow&\\[-2mm]
\text{A10-H0}
&
\text{Hub führt keine neue irrationale Basisphase ein}
\\[1mm]
\Downarrow&\\[-2mm]
\text{A10-H1}
&
\text{augmentierte Hub-/Cross-Gram-Komponenten?}
\\[1mm]
\Downarrow&\\[-2mm]
\text{A10-FCG}
&
\text{endlicher Residual-/Cross-Gram-Block}
\\[1mm]
\Downarrow&\\[-2mm]
&
\ker\Gamma_I=\{0\}\ ? 
\end{array}
}
\]

Jeder Pfeil bezeichnet hier einen **Arbeitsweg**, keine bereits bewiesene mathematische Implikation über die noch offenen Stufen.

Keine Promotion.


---

## 8. A10-H1 — explizite Hub-Bridge über den A9-Separator

A9-FINITE-SMALL beweist endliche freie KNF-Punktkomponenten. Diese Endlichkeit überträgt sich jedoch **nicht formal automatisch** auf den augmentierten freien+\(w\)-Graphen.

Im A9-staggered Separatorfenster normiere \(\Delta=1\) und setze

\[
g:=s_*/\Delta\in(0,1/2),
\qquad
L=4+2g.
\]

Für

\[
0<R<\varepsilon<(1-g)/2,
\qquad
\varepsilon<s<1-\varepsilon-g
\]

ist der freie Zustand

\[
\boxed{x_L=L+s}
\]

das A8/A9-Label \(P_{0,0}^{(1)}\) auf der linken Seite.

Setze

\[
\boxed{t:=b-x_L.}
\]

Dann gilt exakt

\[
t=\frac L2+2-s.
\]

Der gleiche positive Annuluswert koppelt an

\[
\boxed{x_R:=a+t=\frac32L+3-s,}
\]

und \(x_R\) ist exakt das rechte staggered Label

\[
\overline Q_{1,1}^{(2)}.
\]

Die beiden Hubinzidenzen sind:

\[
x_L
\;\xleftrightarrow{\ r_b\text{-Hubast}\ }\;
t,
\]

\[
t
\;\xleftrightarrow{\ -a\text{-Hubast}\ }\;
x_R.
\]

Außerdem

\[
x_R=a+b-x_L.
\]

Die direkte freie KNF-Kante \(r_{a+b}\) ist an \(x_L\) jedoch inaktiv, denn

\[
x_L<a.
\]

Somit besitzt der augmentierte Graph eine \(w(t)\)-vermittelte Verbindung zwischen zwei freien A9-Seiten, obwohl der freie Gramgraph an genau dieser Stelle getrennt ist.

### 8.1 Exakte Gate-Margen

Das Zertifikat reduziert die benötigten Positivitäten unter den strikten A9-Slacks auf

\[
t-R
=
3+2g+(\varepsilon-R)+(1-\varepsilon-g-s)>0,
\]

\[
T_0-x_R
=
1+g+s+\varepsilon>0,
\]

\[
T-t
=
6+3g+s>0,
\]

und

\[
a-x_L
=
\varepsilon+g+(1-\varepsilon-g-s)>0.
\]

Es wird kein numerisches Vorzeichen verwendet.

### 8.2 Zertifikat

Zertifikat:

scripts/certify_sw1_a10_hub_bridge.py

Commit der reparierten Fassung:

0c945bec56feebc4388de4179ec6c80d4b443c57

Committed Script-Blob:

9854a2b13151752bd5d729bc06482926da8aa9ef

Der tatsächlich ausgeführte Dateiinhalt wurde erneut nach dem Git-Blob-Verfahren gehasht und ergab exakt denselben SHA.

Ergebnis:

SW1-A10-H1 HUB-BRIDGE CERTIFICATE: PASS

SymPy 1.14.0.

Damit ist zulässig:

\[
\boxed{
\mathrm{A10\!-\!H1\!-\!BRIDGE(part)}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate)}
}
\]

### 8.3 Exakte Negativaussage

Bewiesen ist ausschließlich:

\[
\boxed{
\text{Die Endlichkeit der freien A9-Komponenten überträgt sich nicht allein über denselben Separatorbeweis auf den augmentierten Hubgraphen.}
}
\]

Nicht bewiesen ist:

- eine unendliche augmentierte Komponente;
- Nichtinjektivität von \(\mathcal L_{\rm ann}^{\rm SW1}\);
- ein Cross-Gram-Kernvektor.

Der nächste Schritt ist die **vollständige Hub-Bridge-Familie**, nicht die Hochstufung dieses Einzelpfads zu einer globalen Graphbehauptung.
