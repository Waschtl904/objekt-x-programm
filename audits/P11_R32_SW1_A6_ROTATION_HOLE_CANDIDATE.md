# P11/R32 — SW1-A6 Rotation-with-Hole Finite-Segment Candidate

> **Stand:** 29. August 2026  
> **Stacked base:** research/sw1-a5-two-sheet-transfer@86e9e2119cf4896d5bceb17881bd2dd7ea1caede  
> **Status:** ?[O] — unterer-Chamber-Rotationssubgraph hergeleitet; Zertifikat/Re-Review offen; keine Promotion.  
> **Scope:** nur der aus A4 stammende kontrahierte Rotationssubgraph. Keine Aussage über die vollständigen A1/A3-Komponenten.

---

## 0. Unterer Chamber

Wir arbeiten unter
\[
\boxed{
0<\varepsilon<\frac{\Delta}{2}.
}
\tag{A6.1}
\]

Setze
\[
A_\varepsilon:=2d-\varepsilon,
\qquad
B_\varepsilon:=T-\varepsilon,
\]
\[
I_\varepsilon:=(A_\varepsilon,B_\varepsilon),
\qquad
L:=B_\varepsilon-A_\varepsilon=a-\Delta.
\tag{A6.2}
\]

Identifiziere \(I_\varepsilon\) mit dem Kreis
\[
\mathbb T_L:=\mathbb R/L\mathbb Z
\]
durch
\[
t=x-A_\varepsilon.
\tag{A6.3}
\]

---

## 1. Der untere A4-Pfad bleibt bis zum Wrap-Cut erhalten

Definiere
\[
D_\varepsilon:=B_\varepsilon-\Delta
\tag{A6.4}
\]
und
\[
C_\varepsilon:=T+\varepsilon-\Delta.
\tag{A6.5}
\]

Dann
\[
C_\varepsilon-D_\varepsilon=2\varepsilon>0
\tag{A6.6}
\]
und
\[
B_\varepsilon-C_\varepsilon
=
\Delta-2\varepsilon>0.
\tag{A6.7}
\]

Somit
\[
A_\varepsilon<D_\varepsilon<C_\varepsilon<B_\varepsilon.
\tag{A6.8}
\]

### Bereich 1

Für
\[
x\in(A_\varepsilon,D_\varepsilon)
\]
ist der echte Zwei-Echo-Pfad
\[
r_{2b}\circ r_{3a}
\]
aktiv und liefert
\[
\boxed{
x\mapsto x+\Delta
\in I_\varepsilon.
}
\tag{A6.9}
\]

### Bereich 2

Für
\[
x\in(D_\varepsilon,C_\varepsilon)
\]
liegt
\[
x+\Delta
\in
(T-\varepsilon,T+\varepsilon),
\]
also im erweiterten \(T\)-Tail.

Dort ist der A4-Vier-Echo-Pfad
\[
r_{2b}\circ r_{4a}\circ r_{2b}\circ r_{3a}
\]
aktiv und liefert
\[
\boxed{
x\mapsto x+\Delta-L
\in I_\varepsilon.
}
\tag{A6.10}
\]

### Bereich 3 — Hole

Für
\[
x\in
H_\varepsilon
:=
(C_\varepsilon,B_\varepsilon)
\tag{A6.11}
\]
gilt
\[
3a-x
\in
(a+\varepsilon,2d-\varepsilon),
\tag{A6.12}
\]
also exakt in A1-R4I.

Dort ist der Wort-11-\(r_{2b}\)-Kanal geschlossen. Äquivalent wäre der formale nächste Wert
\[
x+\Delta>T+\varepsilon=T_0
\tag{A6.13}
\]
horizon-tot.

Damit existiert für den **A4-Rückkehrpfad** aus \(H_\varepsilon\) keine Kante zum nächsten Rotationspunkt.

Die Hole-Länge ist
\[
\boxed{
|H_\varepsilon|
=
\Delta-2\varepsilon>0.
}
\tag{A6.14}
\]

---

## 2. Kontrahierter Rotationsgraph

Sei
\[
R_\Delta:\mathbb T_L\to\mathbb T_L,
\qquad
R_\Delta(t)=t+\Delta\pmod L.
\tag{A6.15}
\]

A4 beweist
\[
\frac{\Delta}{L}\notin\mathbb Q.
\tag{A6.16}
\]

Nach Kontraktion der festen Zwei-/Vier-Echo-Pfade A6.9–A6.10 erhält man den ungerichteten Graphen
\[
\mathcal G_{\rm rot}^{\rm hole}
\]
mit Knoten \(\mathbb T_L\) und Kante
\[
\boxed{
\{t,R_\Delta t\}
\quad\Longleftrightarrow\quad
t\notin H_\varepsilon^{\rm circ},
}
\tag{A6.17}
\]
wobei \(H_\varepsilon^{\rm circ}\) das Bild von A6.11 im Kreis ist.

Wegen A6.14 ist
\[
H_\varepsilon^{\rm circ}
\]
ein nichtleeres offenes Kreissegment.

---

## 3. Jede irrationale Bahn trifft das Hole in beide Richtungen

Für irrationale Kreisrotationen ist jede Bahn
\[
\{R_\Delta^n t:n\in\mathbb Z\}
\]
dicht in \(\mathbb T_L\).

Da
\[
H_\varepsilon^{\rm circ}
\]
offen und nichtleer ist, existieren für jedes \(t\) unendlich viele positive und negative ganze \(n\) mit
\[
R_\Delta^n t\in H_\varepsilon^{\rm circ}.
\tag{A6.18}
\]

Insbesondere existieren benachbarte Hole-Hit-Zeiten
\[
n_-<0\le n_+
\]
so, dass
\[
R_\Delta^{n_-}t,
\quad
R_\Delta^{n_+}t
\in H_\varepsilon^{\rm circ}
\]
und zwischen ihnen kein weiterer Hole-Hit liegt.

---

## 4. Komponenten sind endliche Rotationssegmente

Die Kante zwischen
\[
R_\Delta^n t
\quad\text{und}\quad
R_\Delta^{n+1}t
\]
fehlt genau dann, wenn
\[
R_\Delta^n t\in H_\varepsilon^{\rm circ}.
\tag{A6.19}
\]

Damit schneiden die Hole-Hit-Zeiten die volle \(\mathbb Z\)-Bahn in endliche Intervalle.

Folglich ist jede Zusammenhangskomponente von
\[
\mathcal G_{\rm rot}^{\rm hole}
\]
endlich.

Also:

\[
\boxed{
0<\varepsilon<\Delta/2
\Longrightarrow
\text{der kontrahierte A4-Rotationssubgraph zerfällt in endliche Segmente.}
}
\tag{A6.20}
\]

Dies ist die exakte untere-Chamber-Gegenstruktur zum oberen A4-No-Go.

---

## 5. Für festes \(\varepsilon\): uniforme endliche Segmentlänge

Für festes
\[
\varepsilon<\Delta/2
\]
überdecken die offenen Mengen
\[
\{R_\Delta^{-n}(H_\varepsilon^{\rm circ}):n\ge0\}
\]
den kompakten Kreis \(\mathbb T_L\), da jede Vorwärtsbahn das Hole trifft.

Aus Kompaktheit existiert ein endliches
\[
N_+(\varepsilon)
\]
so, dass bereits
\[
\bigcup_{n=0}^{N_+(\varepsilon)}
R_\Delta^{-n}(H_\varepsilon^{\rm circ})
=
\mathbb T_L.
\tag{A6.21}
\]

Analog existiert
\[
N_-(\varepsilon)
\]
für die Rückwärtsrichtung.

Daher besitzt jede Komponente höchstens
\[
\boxed{
N_+(\varepsilon)+N_-(\varepsilon)+1
}
\tag{A6.22}
\]
Rotationsknoten.

Es wird **keine** uniforme Schranke für den gesamten offenen Parameterchamber behauptet. Wenn
\[
\varepsilon\uparrow\Delta/2,
\]
schrumpft
\[
|H_\varepsilon|=\Delta-2\varepsilon\downarrow0,
\]
und die optimale Bound kann divergieren.

---

## 6. Firewall: volle Echo-Komponente bleibt offen

A6.20 betrifft ausschließlich den aus A4 kontrahierten Rotationssubgraphen.

Ein Punkt im Hole besitzt im vollständigen A1-Graphen weiterhin andere aktive Kanten, beispielsweise die direkte Wort-11-Reflexion
\[
x\mapsto2b-x
\]
aus A1-R5.

Diese Zusatzkanten können zwischen den zwei A5-Blättern wechseln.

Daher folgt aus A6.20 **nicht**
\[
\text{vollständige A1/A3-Punktkomponenten sind endlich}.
\]

Der nächste Knoten ist exakt die Bypass-Frage:
\[
\boxed{
\text{A7-LC: können die zusätzlichen Zwei-Blatt-Kanten die Hole-Segmente zu einer unendlichen Komponente verketten?}
}
\tag{A6.23}
\]

---

## 7. Bedeutung

A4 und A6 ergeben zusammen die scharfe Chamber-Dichotomie für den **einen konkret identifizierten Rotationsmechanismus**:

\[
\boxed{
\begin{array}{ll}
\varepsilon>\Delta/2:
&
\text{volle irrationale Rotation, a.e. unendliche Orbitsegmente;}\\[1mm]
\varepsilon<\Delta/2:
&
\text{irrationale Rotation mit offenem Hole, endliche kontrahierte Segmente.}
\end{array}
}
\tag{A6.24}
\]

Auf
\[
\varepsilon=\Delta/2
\]
kollabiert das Hole auf Nullmaß und gehört als eigener Grenzfall behandelt.

**Keine Aussage über Schur-Injektivität, \(\ker\Gamma_I\), HT-RED, Objekt X oder RH.**
