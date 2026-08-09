# P11-C1z-B2-C1 — Feshbach-Colligation, Polar-Isometrisierung und Kokyklusobstruktion

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1z-B2-C1]`  
**Vorgänger:** C1z-B2-C  
**Schnittstellen:** C1z-B/B1/B2-A/B2-B; P03-Haar-L2-Firewall; P04 nur als spätere strukturelle Analogie

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C1]
\quad
\checkmark[K/M]_{\rm part}
\;+
\checkmark[M]_{\rm neg,one\text{-}sided}
}
\]

mit vier getrennten Befunden:

\[
\boxed{
J_{R,S}^X\text{ ist für jedes }R<S\text{ nach unten beschränkt und hat geschlossenen Bildraum};
}
\]

\[
\boxed{
V_{R,S}:=J_{R,S}^X\bigl((J_{R,S}^X)^*J_{R,S}^X\bigr)^{-1/2}
\text{ ist eine kanonische paarweise Isometrie};
}
\]

\[
\boxed{
\text{der signierte metrische Defekt besitzt eine kanonische zweiseitige Hilbert-Colligation};
}
\]

aber

\[
\boxed{
\text{der Kokyklus der polar-isometrisierten Transitionen ist noch }?[O].
}
\]

Außerdem ist die ursprünglich anvisierte einseitige Zielraumdilatation mit unverändertem ersten Kanal

\[
f\longmapsto(J_{R,S}^Xf,D_{R,S}f)
\]

als **globales Transitionsprinzip** ausgeschlossen: bereits beim ersten Aktivieren des Labels `n=2` ist `J_{R,S}^X` strikt expansiv auf geeigneten Vektoren.

---

# 0. Urteil

C1z-B2-C hatte erstmals ein kohärentes System

\[
\mathcal K_{X,R}
\xrightarrow{J_{R,S}^X}
\mathcal K_{X,S}
\xrightarrow{J_{S,T}^X}
\mathcal K_{X,T}
\]

mit beschränkten injektiven Transitionen und exaktem Kokyklus konstruiert.

Offen war die Zielfrage

\[
\exists\;\widetilde J_{R,S}^X:
\mathcal K_{X,R}\to
\mathcal K_{X,S}\oplus\mathcal B_{R,S}
\quad\text{isometrisch, source-kanonisch und kokzyklisch?}
\]

Der vorliegende Knoten trennt diese Frage in drei logisch verschiedene Ebenen.

## Ebene A — einseitige Defektdilatation mit festem `J`

Eine Abbildung

\[
\widetilde Jf=(Jf,Df)
\]

kann nur dann isometrisch sein, wenn `J` eine Kontraktion ist.

Dies ist im C1z-System **nicht global der Fall**. Es gibt explizite Übergänge `R<S`, für die

\[
\|J_{R,S}^Xf\|_{X,S}>
\|f\|_{X,R}
\]

für geeignete `f` gilt.

Damit ist die naive Form der Zielraum-Randdilatation `×[M]` als allgemeines Transitionsprinzip.

## Ebene B — paarweise metrische Isometrisierung

Trotzdem ist jedes `J_{R,S}^X` nach unten beschränkt. Daher ist

\[
G_{R,S}:=(J_{R,S}^X)^*J_{R,S}^X
\]

positiv, beschränkt und invertierbar.

Die Polar-Isometrie

\[
\boxed{
V_{R,S}:=J_{R,S}^XG_{R,S}^{-1/2}
}
\]

ist eine **kanonische Isometrie**

\[
V_{R,S}:\mathcal K_{X,R}\hookrightarrow\mathcal K_{X,S}
\]

mit demselben Bildraum wie `J_{R,S}^X`.

Paarweise ist die isometrische Transitionfrage also positiv gelöst — sogar ohne zusätzlichen Randraum.

## Ebene C — Kohärenz

Die paarweisen Polar-Isometrien müssen aber nicht automatisch den ursprünglichen Kokyklus erben.

Der exakte neue Engpass lautet:

\[
\boxed{
V_{S,T}V_{R,S}\stackrel?=V_{R,T}.
}
\]

Dies ist äquivalent zu einer präzisen Intertwining-Identität zwischen den positiven Metrikoperatoren `G_{R,S}`.

Damit ist die eigentliche Objekt-X-Frage erneut geschärft:

\[
\boxed{
\text{Nicht Existenz von Transitionen, nicht paarweise Isometrie,}
\quad
\text{sondern kohärente Isometrisierung ist jetzt der harte Punkt.}
}
\]

---

# 1. Verbindliche finite-level Graphräume

Aus C1z-B2-C:

\[
\mathcal K_{X,R}
:=
\bigl(\mathcal D(q_{\Gamma,R}),\|\cdot\|_{X,R}\bigr),
\]

mit

\[
\boxed{
q_R^X(f)
=
q_{\Gamma,R}(f)
+\sigma_R(f),
}
\tag{C1zB2C1.1}
\]

und

\[
\boxed{
\sigma_R(f)
=
\langle H_R^*f,B_RH_R^*f\rangle,
\qquad
B_R=(I+R_R^*R_R)^{-1}.
}
\tag{C1zB2C1.2}
\]

Es gilt

\[
0<B_R\le I,
\]

also

\[
0\le\sigma_R(f)
\le\|H_R\|^2\|f\|_2^2.
\]

Da

\[
q_{\Gamma,R}(f)\ge\|f\|_2^2,
\]

folgt die bereits bewiesene Normäquivalenz

\[
\boxed{
q_{\Gamma,R}(f)
\le q_R^X(f)
\le(1+\|H_R\|^2)q_{\Gamma,R}(f).
}
\tag{C1zB2C1.3}
\]

Für `R<S` ist

\[
J_{R,S}^Xf=E_{R,S}f
\]

die Nullfortsetzung zwischen den Graphräumen.

C1z-B2-C beweist

\[
\boxed{
J_{S,T}^XJ_{R,S}^X=J_{R,T}^X.
}
\tag{C1zB2C1.4}
\]

---

# 2. Neue Untergrenze: jede Transition ist ein topologisches Embedding

C1z-B2-C hatte die obere Schranke

\[
q_S^X(J_{R,S}^Xf)
\le
(1+\|H_S\|^2)q_R^X(f)
\]

bewiesen.

Für C1 benötigen wir nun die Gegenrichtung.

Da der Gammaanteil unter Nullfortsetzung exakt kompatibel ist,

\[
q_{\Gamma,S}(E_{R,S}f)
=q_{\Gamma,R}(f),
\]

und `sigma_S>=0`, gilt

\[
q_S^X(J_{R,S}^Xf)
\ge
q_{\Gamma,R}(f).
\]

Mit (C1zB2C1.3):

\[
q_{\Gamma,R}(f)
\ge
\frac{1}{1+\|H_R\|^2}q_R^X(f).
\]

Daher:

\[
\boxed{
\frac{1}{1+\|H_R\|^2}
q_R^X(f)
\le
q_S^X(J_{R,S}^Xf)
\le
(1+\|H_S\|^2)q_R^X(f).
}
\tag{C1zB2C1.5}
\]

Äquivalent:

\[
\boxed{
(1+\|H_R\|^2)^{-1/2}\|f\|_{X,R}
\le
\|J_{R,S}^Xf\|_{X,S}
\le
(1+\|H_S\|^2)^{1/2}\|f\|_{X,R}.
}
\tag{C1zB2C1.6}
\]

## Konsequenzen

Für jedes `R<S`:

1. `J_{R,S}^X` ist injektiv;
2. `J_{R,S}^X` ist nach unten beschränkt;
3. `Ran(J_{R,S}^X)` ist geschlossen in `K_{X,S}`;
4. `J_{R,S}^X` ist ein Banach-/Hilbert-Isomorphismus von `K_{X,R}` auf seinen geschlossenen Bildraum;
5. die Inverse auf dem Bild erfüllt

\[
\boxed{
\|(J_{R,S}^X)^{-1}\|_{\operatorname{Ran}J}
\le
\sqrt{1+\|H_R\|^2}.
}
\tag{C1zB2C1.7}
\]

Status: `✓[K/M]`.

Dies ist stärker als C1z-B2-C: Die finite-level Graphgeometrien sind nicht nur durch injektive beschränkte Maps verbunden, sondern durch **topologische Einbettungen mit geschlossenem Bild**.

---

# 3. Metrikoperator der Transition

Definiere bezüglich der `X`-Hilberträume

\[
\boxed{
G_{R,S}
:=(J_{R,S}^X)^*J_{R,S}^X
\in\mathcal B(\mathcal K_{X,R}).
}
\tag{C1zB2C1.8}
\]

Dann ist `G_{R,S}` positiv selbstadjungiert und

\[
\langle G_{R,S}f,f\rangle_{X,R}
=
\|J_{R,S}^Xf\|_{X,S}^2.
\]

Aus (C1zB2C1.5):

\[
\boxed{
\frac{1}{1+\|H_R\|^2}I
\le
G_{R,S}
\le
(1+\|H_S\|^2)I.
}
\tag{C1zB2C1.9}
\]

Insbesondere

\[
\boxed{G_{R,S}>0\text{ und }G_{R,S}^{-1}\in\mathcal B(\mathcal K_{X,R}).}
\tag{C1zB2C1.10}
\]

Der signierte Defekt aus C1z-B2-C ist exakt

\[
\mathfrak D_{R,S}=G_{R,S}-I.
\]

Damit ist die gesamte metrische Transition in einem einzigen positiven invertierbaren Operator kodiert.

---

# 4. Harte Bedingung für eine einseitige Zielraumdilatation

Sei allgemein

\[
J:H\to K
\]

beschränkt und

\[
D:H\to B
\]

ein weiterer Hilbertoperator.

Angenommen

\[
\widetilde J:H\to K\oplus B,
\qquad
\widetilde Jf=(Jf,Df)
\]

ist isometrisch.

Dann

\[
\|f\|_H^2
=
\|Jf\|_K^2+\|Df\|_B^2
\ge
\|Jf\|_K^2.
\]

Also notwendig

\[
\boxed{J^*J\le I.}
\tag{C1zB2C1.11}
\]

Umgekehrt: Falls `J^*J<=I`, setzt man

\[
D_J:=(I-J^*J)^{1/2}
\]

und erhält

\[
\boxed{
f\longmapsto(Jf,D_Jf)
\text{ isometrisch}.}
\tag{C1zB2C1.12}
\]

Damit gilt exakt:

\[
\boxed{
\exists D:\ (J,D)\text{ isometrisch}
\iff
J\text{ ist eine Kontraktion}.}
\tag{C1zB2C1.13}
\]

Für unser System ist die ursprüngliche Zielfrage mit unverändertem ersten Kanal daher äquivalent zu

\[
G_{R,S}\le I
\qquad\forall R<S.
\]

C1z-B2-C hatte gerade davor gewarnt, eine solche Monotonie anzunehmen.

Der nächste Abschnitt zeigt: global ist sie sogar falsch.

---

# 5. Expliziter Expansionszeuge beim ersten Prime-Power-Label

Setze

\[
a_2:=\frac12\log2,
\qquad
a_3:=\frac12\log3.
\]

Wähle

\[
\boxed{0<R<a_2<S<a_3.}
\tag{C1zB2C1.14}
\]

Dann gilt

\[
e^{2R}<2,
\]

also ist auf Level `R` kein Prime-Power-Label aktiv:

\[
\mathcal N_R=\varnothing.
\]

Daher

\[
H_R=0,
\qquad
R_R=0,
\qquad
\sigma_R=0,
\]

und somit

\[
\boxed{q_R^X=q_{\Gamma,R}.}
\tag{C1zB2C1.15}
\]

Auf Level `S` gilt dagegen

\[
2<e^{2S}<3.
\]

Somit ist exakt das Label `n=2` aktiv:

\[
\mathcal N_S=\{2\}.
\]

Der Huboperator lautet daher

\[
\boxed{
H_S
=c_2P_SD_{\log2}E_S,
\qquad
c_2=\sqrt{\log2}\,2^{-3/4}>0.
}
\tag{C1zB2C1.16}
\]

Wähle

\[
0<\delta<\min\{R,S-a_2,a_2\}
\]

und

\[
0\ne f\in C_c^\infty((-\delta,\delta)).
\]

Dann liegen beide verschobenen Kopien des `D_{log2}`-Kanals vollständig in `(-S,S)` und sind disjunkt.

Folglich

\[
D_{\log2}E_{R,S}f\ne0,
\]

also

\[
H_S^*E_{R,S}f\ne0.
\]

Da

\[
B_S=(I+R_S^*R_S)^{-1}>0
\]

invertierbar ist,

\[
\boxed{
\sigma_S(E_{R,S}f)
=
\langle H_S^*Ef,B_SH_S^*Ef\rangle
>0.
}
\tag{C1zB2C1.17}
\]

Der Gammaanteil bleibt exakt gleich. Daher

\[
\boxed{
q_S^X(E_{R,S}f)
=
q_R^X(f)+\sigma_S(E_{R,S}f)
>
q_R^X(f).
}
\tag{C1zB2C1.18}
\]

Somit

\[
\boxed{
G_{R,S}\not\le I
}
\tag{C1zB2C1.19}
\]

für diese Übergänge.

### Urteil

Die einseitige Zielraumdilatation

\[
f\mapsto(J_{R,S}^Xf,D_{R,S}f)
\]

mit dem **unveränderten** ersten Kanal `J_{R,S}^X` kann daher nicht für alle `R<S` existieren.

Status:

\[
\boxed{\checkmark[M]_{\rm neg,one\text{-}sided}.}
\]

**Scope-Firewall:** Dies beweist nicht, dass `J_{R,S}^X` für alle großen `R<S` expansiv ist. Es schließt nur die naive Forderung aus, dass alle Transitionen Kontraktionen seien und daher ein einziges einseitiges Zielraum-Defektschema tragen.

---

# 6. Paarweise Polar-Isometrisierung

Da `G_{R,S}` positiv und invertierbar ist, definiere

\[
\boxed{
M_{R,S}:=G_{R,S}^{1/2},
\qquad
V_{R,S}:=J_{R,S}^XM_{R,S}^{-1}.
}
\tag{C1zB2C1.20}
\]

Dann

\[
\begin{aligned}
V_{R,S}^*V_{R,S}
&=
M_{R,S}^{-1}
(J_{R,S}^X)^*J_{R,S}^X
M_{R,S}^{-1}\\
&=
M_{R,S}^{-1}G_{R,S}M_{R,S}^{-1}\\
&=I.
\end{aligned}
\]

Also

\[
\boxed{
V_{R,S}:\mathcal K_{X,R}\hookrightarrow\mathcal K_{X,S}
\text{ ist isometrisch}.}
\tag{C1zB2C1.21}
\]

Da `M_{R,S}^{-1}` ein Automorphismus von `K_{X,R}` ist,

\[
\boxed{
\operatorname{Ran}V_{R,S}
=
\operatorname{Ran}J_{R,S}^X.
}
\tag{C1zB2C1.22}
\]

Damit ist `V_{R,S}` exakt der isometrische Faktor in der Polarzerlegung

\[
\boxed{
J_{R,S}^X=V_{R,S}M_{R,S}.
}
\tag{C1zB2C1.23}
\]

## Interpretation

Die Metrikverzerrung der Nullfortsetzung ist vollständig im positiven Operator

\[
M_{R,S}=\bigl((J_{R,S}^X)^*J_{R,S}^X\bigr)^{1/2}
\]

konzentriert.

Der geometrische Anteil

\[
V_{R,S}
\]

ist bereits isometrisch.

Dies liefert eine positive Antwort auf die **paarweise** Isometrisierungsfrage.

Status: `✓[K/M]`.

**Kanonizitäts-Firewall:** `V_{R,S}` ist funktionalanalytisch kanonisch relativ zu den bereits konstruierten Graphräumen und Nullfortsetzungs-Transitionen. Noch nicht gezeigt ist, dass `M_{R,S}^{-1}` selbst eine lokale arithmetic/source-Operation besitzt.

---

# 7. Der signierte Defekt besitzt eine kanonische zweiseitige Hilbert-Colligation

C1z-B2-C hatte

\[
\mathfrak D_{R,S}
=G_{R,S}-I
\]

und seine positive/negative Spektralzerlegung eingeführt.

Setze nun

\[
\boxed{
D_{R,S}^+
:=(G_{R,S}-I)_+^{1/2},
\qquad
D_{R,S}^-
:=(I-G_{R,S})_+^{1/2}.
}
\tag{C1zB2C1.24}
\]

Dann

\[
\boxed{
G_{R,S}
=I+(D_{R,S}^+)^2-(D_{R,S}^-)^2.
}
\tag{C1zB2C1.25}
\]

Für jedes `f in K_{X,R}` folgt

\[
\boxed{
\|J_{R,S}^Xf\|_{X,S}^2
+
\|D_{R,S}^-f\|_{X,R}^2
=
\|f\|_{X,R}^2
+
\|D_{R,S}^+f\|_{X,R}^2.
}
\tag{C1zB2C1.26}
\]

Dies ist eine exakte **zweiseitige Hilbert-Balance** des signierten Defekts.

Definiere die Defekträume

\[
\boxed{
\mathcal B_{R,S}^+
:=\overline{\operatorname{Ran}D_{R,S}^+},
\qquad
\mathcal B_{R,S}^-
:=\overline{\operatorname{Ran}D_{R,S}^-}.
}
\tag{C1zB2C1.27}
\]

und die beiden Graphabbildungen

\[
\mathcal A_{R,S}f
:=(f,D_{R,S}^+f)
\in
\mathcal K_{X,R}\oplus\mathcal B_{R,S}^+,
\]

\[
\mathcal C_{R,S}f
:=(J_{R,S}^Xf,D_{R,S}^-f)
\in
\mathcal K_{X,S}\oplus\mathcal B_{R,S}^-.
\]

Aus (C1zB2C1.26):

\[
\boxed{
\|\mathcal A_{R,S}f\|
=
\|\mathcal C_{R,S}f\|.
}
\tag{C1zB2C1.28}
\]

Da beide Graphabbildungen nach unten durch `||f||` beschränkt sind, haben sie geschlossene Bilder.

Daher existiert eindeutig ein unitärer Operator zwischen diesen **kanonischen Graphunterräumen**:

\[
\boxed{
\mathcal U_{R,S}:
\operatorname{Ran}\mathcal A_{R,S}
\stackrel{\cong}{\longrightarrow}
\operatorname{Ran}\mathcal C_{R,S},
\qquad
\mathcal U_{R,S}\mathcal A_{R,S}f
=\mathcal C_{R,S}f.
}
\tag{C1zB2C1.29}
\]

Dies ist die gesuchte **paarweise Feshbach-Colligation für den signierten Defekt**.

Sie benötigt keine Krein-Metrik: positive und negative Defektanteile werden auf zwei gewöhnliche Hilbert-Randräume verteilt.

Status: `✓[K/M]`.

**Firewall:** Es wird keine kanonische unitäre Erweiterung von `U_{R,S}` auf die vollständigen äußeren Direkt-Summen behauptet. Kanonisch ist die Unitariät zwischen den durch die Transition erzeugten Graphunterräumen.

---

# 8. Spezialfälle der Colligation

## 8.1 Kontraktiver Übergang

Falls

\[
G_{R,S}\le I,
\]

ist

\[
D_{R,S}^+=0.
\]

Dann reduziert sich (C1zB2C1.26) auf

\[
\|Jf\|^2+\|D^-f\|^2=\|f\|^2,
\]

also auf die ursprünglich gewünschte einseitige Zielraumdilatation.

## 8.2 Expansiver Übergang

Falls

\[
G_{R,S}\ge I,
\]

ist

\[
D_{R,S}^-=0,
\]

und

\[
\|Jf\|^2=\|f\|^2+\|D^+f\|^2.
\]

Der Randterm liegt dann natürlicherweise auf der **Source-Seite**.

Der in §5 konstruierte erste-Label-Übergang ist von diesem Typ:

\[
q_S^X(Ef)=q_R^X(f)+\sigma_S(Ef).
\]

## 8.3 Signierter Übergang

Wenn `G-I` beide Vorzeichen besitzt, sind beide Randräume nötig.

Dies ist genau der allgemeine C1z-B2-C-Scope nach Screening plus Hubwachstum.

---

# 9. Exakter Pullback-Kokyklus der Metrikoperatoren

Obwohl die Polar-Isometrien noch keinen bewiesenen Kokyklus besitzen, erfüllen die positiven Metrikoperatoren selbst eine exakte Kohärenzidentität.

Aus

\[
J_{R,T}^X
=J_{S,T}^XJ_{R,S}^X
\]

folgt

\[
\begin{aligned}
G_{R,T}
&=(J_{R,T}^X)^*J_{R,T}^X\\
&=(J_{R,S}^X)^*
(J_{S,T}^X)^*J_{S,T}^X
J_{R,S}^X.
\end{aligned}
\]

Also

\[
\boxed{
G_{R,T}
=(J_{R,S}^X)^*G_{S,T}J_{R,S}^X.
}
\tag{C1zB2C1.30}
\]

Dies ist ein exakter **operatorwertiger metrischer Pullback-Kokyklus**.

Für die zugehörigen quadratischen Formen:

\[
\boxed{
\langle G_{R,T}f,f\rangle_{X,R}
=
\langle G_{S,T}J_{R,S}^Xf,J_{R,S}^Xf\rangle_{X,S}.
}
\tag{C1zB2C1.31}
\]

Damit ist die metrische Verzerrung nicht unstrukturiert: sie ist bereits exakt kohärent **vor** der Quadratwurzel-/Polaroperation.

Dieser Befund ist wahrscheinlich die richtige Ausgangslage für einen späteren Grenzmetrikbau.

---

# 10. Warum der Polar-Kokyklus nicht automatisch folgt

Setze

\[
M_{R,S}:=G_{R,S}^{1/2}.
\]

Dann

\[
V_{R,S}=J_{R,S}M_{R,S}^{-1}.
\]

Die gewünschte Kohärenz wäre

\[
\boxed{
V_{S,T}V_{R,S}=V_{R,T}.
}
\tag{C1zB2C1.32}
\]

Einsetzen liefert

\[
J_{S,T}M_{S,T}^{-1}
J_{R,S}M_{R,S}^{-1}
=
J_{S,T}J_{R,S}M_{R,T}^{-1}.
\]

Da `J_{S,T}` injektiv ist, ist dies äquivalent zu

\[
\boxed{
M_{S,T}^{-1}
J_{R,S}M_{R,S}^{-1}
=
J_{R,S}M_{R,T}^{-1}.
}
\tag{C1zB2C1.33}
\]

Dies ist die **exakte Polar-Kokyklusbedingung**.

Sie folgt nicht formal aus dem Pullback-Kokyklus (C1zB2C1.30), weil Quadratwurzel und Pullback durch einen nichtisometrischen `J_{R,S}` nicht allgemein vertauschen.

Status:

\[
\boxed{?[O].}
\]

**Scope-Firewall:** Hier wird nicht behauptet, dass (C1zB2C1.33) im konkreten C1z-Modell falsch ist. Nur: Es ist ein zusätzlicher mathematischer Satz, der noch bewiesen werden müsste.

---

# 11. Ein kanonischer Kohärenz-Obstruktionsoperator

Definiere

\[
\boxed{
\Omega_{R,S,T}
:=V_{R,T}^*V_{S,T}V_{R,S}
\in\mathcal B(\mathcal K_{X,R}).
}
\tag{C1zB2C1.34}
\]

Da alle `V` Isometrien sind,

\[
\|\Omega_{R,S,T}\|\le1.
\]

Und

\[
\boxed{
\Omega_{R,S,T}=I
\iff
V_{S,T}V_{R,S}=V_{R,T}.
}
\tag{C1zB2C1.35}
\]

Der letzte Schluss gilt, weil für zwei Isometrien `A,B:H->K` aus `A^*B=I` folgt

\[
\|(B-A)f\|^2
=2\|f\|^2-2\operatorname{Re}\langle A^*Bf,f\rangle
=0.
\]

Damit ist der bisher diffuse Kokyklusfehler auf den konkreten Operator

\[
\boxed{\Omega_{R,S,T}-I}
\]

reduziert.

Dies ist ein neuer scharfer Prüfstein.

---

# 12. Zukunftsmetriken auf einem festen Source-Level

Für `S>R` definiere auf `K_{X,R}` die aus Level `S` zurückgezogene Metrik

\[
\boxed{
q_R^{(S)}(f)
:=
\|J_{R,S}^Xf\|_{X,S}^2
=
\langle G_{R,S}f,f\rangle_{X,R}.
}
\tag{C1zB2C1.36}
\]

Für `R<S<T` liefert (C1zB2C1.30):

\[
\boxed{
q_R^{(T)}(f)
=
q_S^{(T)}(J_{R,S}^Xf).
}
\tag{C1zB2C1.37}
\]

Die Familie

\[
\{q_R^{(S)}:S>R\}
\]

ist damit die natürliche **metrische Zukunftsentwicklung** eines festen Source-Levels.

Ein kanonischer Hilbert-Grenzträger könnte entstehen, falls für jedes feste `R`

\[
G_{R,S}
\]

in einer geeigneten Topologie gegen einen positiven invertierbaren Grenzoperator

\[
G_{R,\infty}
\]

konvergiert und diese Grenzoperatoren mit den Transitionen kompatibel sind.

Dies wird hier nicht behauptet.

Aber C1z-B2-C1 reduziert die Grenzraumfrage erstmals auf ein konkretes operatorwertiges Metrikproblem.

---

# 13. Beziehung zur Feshbach-Screening-Dilatation aus C1z-B2-C

C1z-B2-C hatte im gefrorenen Hub-Scope den neuen Restkanal

\[
D:H\to Z
\]

und die exakte Screeningidentität

\[
\|B^{1/2}h\|^2
=
\|\widetilde B^{1/2}h\|^2
+
\|(I+DBD^*)^{-1/2}DBh\|^2
\]

bewiesen.

Dieser konkrete source-geometrische Randkanal ist ein Spezialfall des negativen Defektanteils in der allgemeinen Balance (C1zB2C1.26).

Der neue abstrakte Operator

\[
D_{R,S}^-=(I-G_{R,S})_+^{1/2}
\]

ist jedoch **nicht bereits mit**

\[
(I+DBD^*)^{-1/2}DB
\]

identifiziert.

Warum nicht: Im vollständigen Übergang ändern sich gleichzeitig

1. Resttiefe;
2. Huboperator;
3. aktive Labelmenge;
4. Source-Annulus;
5. die Feshbach-Kompression des neuen Source-Raums.

Eine exakte source-geometrische Zerlegung von `D_{R,S}^\pm` in diese Bestandteile bleibt offen.

Dies ist eine wichtige Kanonizitätsfirewall.

---

# 14. Beziehung zur P03-Haar-L2-Firewall

Die Polar-Isometrien

\[
V_{R,S}
\]

sind **nicht** die Haar-Nullfortsetzungen.

Sie enthalten den nichttrivialen Metrikfaktor

\[
G_{R,S}^{-1/2}.
\]

Damit entsteht kein Widerspruch zur P03-Firewall, die einen positiven geschlossenen Endpunkt auf dem festen Haar-`L^2(R)` ausschließt, der `B_W` auf dem Testkern exakt fortsetzt.

Im Gegenteil: C1z-B2-C1 zeigt konkret, wie ein möglicher Grenzträger die Haar-Geometrie verlassen müsste:

\[
\boxed{
\text{Nullfortsetzung}
\quad+\quad
\text{nichttrivialer operatorwertiger Metriktransport}.
}
\]

Gerade dieser Metriktransport ist jetzt als `G_{R,S}^{-1/2}` explizit typisiert.

---

# 15. Beziehung zu P04 / Suzuki — Firewall

P04 besitzt offene Transitionen zwischen finite-interval Weil-/Suzuki-Räumen.

C1z-B2-C1 liefert nun im P11-Strang:

- konkrete bounded transitions `J_{R,S}^X`;
- positive Metrikoperatoren `G_{R,S}`;
- paarweise Polar-Isometrien `V_{R,S}`;
- signierte Defekträume `B_{R,S}^\pm`;
- einen exakten metrischen Pullback-Kokyklus.

Es wird **keine** Identifikation mit den P04-Transitionen behauptet.

Eine solche Brücke wäre frühestens ein P12-Thema und müsste die unterschiedlichen finite-level Formen explizit typisieren.

---

# 16. Statusmatrix

| Aussage | Status |
|---|---|
| `J_{R,S}^X` beschränkt/injektiv | `✓[K/M]` aus C1z-B2-C |
| `J_{R,S}^X` nach unten beschränkt | `✓[K/M]` |
| `Ran J_{R,S}^X` geschlossen | `✓[K/M]` |
| `G_{R,S}=J^*J` positiv invertierbar | `✓[K/M]` |
| explizite Zwei-Seiten-Schranke für `G_{R,S}` | `✓[K/M]` |
| alle `J_{R,S}^X` Kontraktionen | `×[M]` — expliziter erster-Label-Zeuge |
| einseitige Zielraumdilatation `(J,D)` für alle Übergänge | `×[M]` |
| paarweise Polar-Isometrie `V_{R,S}` | `✓[K/M]` |
| `Ran V_{R,S}=Ran J_{R,S}` | `✓[K/M]` |
| signierte zweiseitige Hilbert-Colligation | `✓[K/M]` |
| metrischer Pullback-Kokyklus `G_{R,T}=J_{R,S}^*G_{S,T}J_{R,S}` | `✓[M]` |
| Polar-Kokyklus `V_{S,T}V_{R,S}=V_{R,T}` | `?[O]` |
| source-lokale Zerlegung von `D_{R,S}^\pm` | `?[O]` |
| Grenzoperator `G_{R,\infty}` | `?[O]` |
| finaler Objekt-X-Hilbertlimes | `?[O]` |
| Identifikation mit exakter Weil-Geometrie | `?[O]` |

---

# 17. Strukturelles Gesamtbild

Die C1z-Kette hat sich damit von einem Divergenzproblem zu einem echten Metriktransportproblem entwickelt:

\[
\boxed{
\begin{array}{c}
\text{finite-adische source-Konditionierung}\\
\downarrow\\
\text{Gamma-Hub-Feshbach mit compact resolvent auf festem }R\\
\downarrow\\
\text{kein endlicher Schattenkanal}\\
\downarrow\\
\text{Gamma-Kompaktheit entweicht bei }R\to\infty\\
\downarrow\\
\text{eigene finite-level Graphräume }\mathcal K_{X,R}\\
\downarrow\\
\text{bounded injective }J_{R,S}^X\\
\downarrow\\
\text{positive invertierbare Metrikoperatoren }G_{R,S}\\
\downarrow\\
\text{paarweise isometrische Polartransporte }V_{R,S}.
\end{array}
}
\]

Der harte Rest ist jetzt nicht mehr die Existenz einer Hilbertgeometrie auf jedem Level und auch nicht mehr die Existenz isometrischer Paartransporte.

Er lautet:

\[
\boxed{
\text{Kann der operatorwertige Metriktransport kohärent über alle Source-Level trivialisiert werden?}
}
\]

Das ist eine wesentlich schärfere Objekt-X-Frage als die frühere Suche nach einem einzelnen Kompressor.

---

# 18. Scope-Firewalls

Aus C1z-B2-C1 folgt **nicht**:

1. dass `q_R^X` die exakte Weilform ist;
2. dass `V_{R,S}` einen Kokyklus bildet;
3. dass `V_{R,S}` source-lokal oder arithmetisch bereits explizit ist;
4. dass die Defekträume `B_{R,S}^\pm` prime-/Gammaweise zerfallen;
5. dass `G_{R,S}` für `S->infty` konvergiert;
6. dass ein Hilbert-Induktivlimes existiert;
7. dass dieser Grenzraum `K_X` oder `H_W` ist;
8. RH;
9. ein Abschluss von P10-O07;
10. eine Identifikation mit P04/Suzuki-Transitionen.

Insbesondere bleibt P11 `PASS-A ACTIVE`; kein SYN, kein Seal.

---

# 19. Nächster atomarer Knoten

Der nächste Test ist nun mathematisch erzwungen:

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C2]
\quad
\text{Kohärenzaudit des operatorwertigen Metrik-Kokyklus}.
}
\]

Zu prüfen sind in dieser Reihenfolge:

## C2-A — Polar-Kokyklus

Test der exakten Bedingung

\[
M_{S,T}^{-1}J_{R,S}M_{R,S}^{-1}
\stackrel?=
J_{R,S}M_{R,T}^{-1}.
\]

Falls ja:

\[
V_{S,T}V_{R,S}=V_{R,T}
\]

und wir besitzen einen echten isometrischen Hilbert-Induktivapparat.

## C2-B — falls nein: unitärer/defektiver 2-Kokyklus

Untersuche

\[
\Omega_{R,S,T}=V_{R,T}^*V_{S,T}V_{R,S}.
\]

Zu klären:

1. ist `Omega` unitär oder nur kontraktiv?
2. besitzt `Omega-I` eine source-lokale Faktorisation?
3. erfüllt `Omega` eine höhere Kokyklusidentität für `R<S<T<U`?
4. kann ein zusätzlicher Rand-/Defektraum diesen 2-Kokyklus absorbieren?

## C2-C — asymptotische Metrik

Prüfe für festes `R` die Familie

\[
G_{R,S},\qquad S\to\infty.
\]

Ein positiver invertierbarer Grenzwert

\[
G_{R,\infty}
\]

mit kompatiblem Pullback wäre ein direkter Kandidat für die eigentliche Objekt-X-Metrik auf dem algebraischen Grenzsystem.

Damit lautet die neue Leitfrage:

\[
\boxed{
\text{Objekt X könnte weniger ein einzelner Operator sein als eine kohärente Trivialisierung dieses Metrik-Kokyklus.}
}
\]
