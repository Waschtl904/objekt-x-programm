# P11-C1z-B2-C5e — Even terminal gauge / target-square-root convergence

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C5e]`  
**Vorgänger:** C1z-B2-C5d  
**Schnittstellen:** C1z-B2-C2; C1z-B2-C5c/C5d; P03-Haar-L2-Firewall  
**P11-Status:** `PASS-A ACTIVE` — kein SYN, kein Seal

## Status

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C5e]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm pos,even-terminal-gauge}
+
\checkmark[M]_{\rm pos,even-directed-limit}
}
\]

Der in C5d isolierte Engpass ist auf dem **gesamten geraden Graphraum** positiv lösbar:

\[
\boxed{
W_{R,S,+}^{[T]}
\xrightarrow[T\to\infty]{\rm s}
W_{R,S,+}^{[\Gamma]}
}
\qquad (R<S\text{ fest}),
\]

wobei

\[
W_{R,S,+}^{[T]}
=
(G_{S,T}^{+})^{1/2}
J_{R,S}^{+}
(G_{R,T}^{+})^{-1/2}
\]

und

\[
\boxed{
W_{R,S,+}^{[\Gamma]}
=
(\Gamma_S^{+})^{1/2}
J_{R,S}^{+}
(\Gamma_R^{+})^{-1/2}.
}
\]

Der entscheidende Punkt ist, dass dafür **keine** globale starke Konvergenz

\[
(G_{S,T}^{+})^{1/2}
\to
(\Gamma_S^{+})^{1/2}
\]

benötigt wird. Die fehlende positive Target-Quadratwurzel wird durch einen bewegten Testvektor

\[
y_T=(G_{S,T}^{+})^{-1/2}g
\]

eliminiert. Die bereits in C5d bewiesene starke Konvergenz der **inversen** Quadratwurzeln reicht zusammen mit der exakten finite-horizon Isometrie aus.

---

# 0. Urteil

C5d hatte korrekt die Firewall stehen gelassen:

\[
G_{R,T}^{+}\xrightarrow{\rm s.r.}\Gamma_R^{+}
\]

liefert zwar

\[
(G_{R,T}^{+})^{-1/2}
\xrightarrow{\rm s}
(\Gamma_R^{+})^{-1/2},
\]

aber nicht automatisch

\[
(G_{R,T}^{+})^{1/2}
\xrightarrow{\rm s}
(\Gamma_R^{+})^{1/2}.
\]

Diese Firewall bleibt **vollständig bestehen**. C5e beweist die globale starke Konvergenz der positiven Quadratwurzeln nicht und benötigt sie auch nicht.

Stattdessen wird die spezielle normalisierte Komposition

\[
(G_{S,T}^{+})^{1/2}
J_{R,S}^{+}
(G_{R,T}^{+})^{-1/2}
\]

direkt behandelt. Ihre finite-horizon Isometrie liefert eine uniforme Normkontrolle, und die inverse Target-Gauge erzeugt genau die Testvektoren, auf denen sich die unbeschränkte/unkontrollierte positive Target-Quadratwurzel algebraisch wegkürzt.

Damit ist der in C5d formulierte **Transportengpass** im geraden Kanal geschlossen.

---

# 1. Verbindliche Daten aus C2 und C5d

Fixiere

\[
R<S.
\]

Setze zur Abkürzung

\[
\mathcal H_R:=\mathcal K_{X,R}^{+},
\qquad
\mathcal H_S:=\mathcal K_{X,S}^{+},
\qquad
J:=J_{R,S}^{+}.
\]

Für `T>S` schreiben wir

\[
A_T:=G_{R,T}^{+},
\qquad
B_T:=G_{S,T}^{+},
\]

und im Gamma-Limes

\[
A:=\Gamma_R^{+},
\qquad
B:=\Gamma_S^{+}.
\]

## 1.1 Exakte finite-horizon Pullback-Identität

C2 beweist auf dem vollen Graphraum

\[
G_{R,T}=J_{R,S}^{*}G_{S,T}J_{R,S}.
\]

Da Parität nach C5 erhalten bleibt, gilt auf dem geraden Kanal:

\[
\boxed{
A_T=J^{*}B_TJ.
}
\tag{C5e.1}
\]

Damit ist

\[
\boxed{
U_T:=B_T^{1/2}JA_T^{-1/2}
=W_{R,S,+}^{[T]}
}
\tag{C5e.2}
\]

für jedes endliche `T` eine Isometrie:

\[
\boxed{
U_T^{*}U_T=I_{\mathcal H_R}.
}
\tag{C5e.3}
\]

Insbesondere

\[
\boxed{
\|U_Tf\|_{\mathcal H_S}=\|f\|_{\mathcal H_R}
}
\tag{C5e.4}
\]

für alle `f\in\mathcal H_R`, uniform in `T`.

Es wird ausdrücklich **keine** uniforme Schranke für

\[
\|B_T^{1/2}\|
\]

benötigt.

## 1.2 Gamma-Pullback

C5d identifiziert die gerade Grenzform mit der Gammaform und liefert die exakte Kompatibilität

\[
\boxed{
A=J^{*}BJ.
}
\tag{C5e.5}
\]

Daher ist

\[
\boxed{
U:=B^{1/2}JA^{-1/2}
=W_{R,S,+}^{[\Gamma]}
}
\tag{C5e.6}
\]

ebenfalls eine Isometrie:

\[
\boxed{
U^{*}U=I_{\mathcal H_R}.
}
\tag{C5e.7}
\]

## 1.3 Bereits bewiesene inverse Gauge-Konvergenz

Aus der Mosco-Konvergenz in C5d folgt stark:

\[
\boxed{
A_T^{-1/2}\xrightarrow{\rm s}A^{-1/2},
\qquad
B_T^{-1/2}\xrightarrow{\rm s}B^{-1/2}.
}
\tag{C5e.8}
\]

Die Gammaoperatoren sind auf den festen Graphräumen positiv und invertierbar; C5d besitzt sogar feste levelweise Schranken

\[
0<c_RI\le A\le C_RI,
\qquad
0<c_SI\le B\le C_SI.
\]

Damit ist insbesondere `B^{-1/2}` auf ganz `\mathcal H_S` beschränkt und surjektiv.

---

# 2. Abstraktes Lemma — inverse-gauge moving-test principle

## Satz C5e.1

Seien `\mathcal H_1,\mathcal H_2` Hilberträume, `J:\mathcal H_1\to\mathcal H_2` beschränkt und

\[
A_n>0\text{ auf }\mathcal H_1,
\qquad
B_n>0\text{ auf }\mathcal H_2,
\]

sowie positive invertierbare Grenzoperatoren `A,B`. Angenommen:

1. die normalisierten Operatoren
   \[
   U_n:=B_n^{1/2}JA_n^{-1/2}
   \]
   sind Isometrien;
2. 
   \[
   A_n^{-1/2}\xrightarrow{\rm s}A^{-1/2};
   \]
3. 
   \[
   B_n^{-1/2}\xrightarrow{\rm s}B^{-1/2};
   \]
4. 
   \[
   U:=B^{1/2}JA^{-1/2}
   \]
   ist eine Isometrie;
5. `B^{-1/2}` hat dichten Bildraum — hier sogar Bildraum `\mathcal H_2`.

Dann

\[
\boxed{
U_n\xrightarrow{\rm s}U.
}
\tag{C5e.9}
\]

### Beweis

Fixiere

\[
f\in\mathcal H_1,
\qquad
g\in\mathcal H_2.
\]

Definiere den bewegten Target-Testvektor

\[
\boxed{
y_n:=B_n^{-1/2}g.}
\tag{C5e.10}
\]

Nach Voraussetzung 3 gilt

\[
y_n\to y:=B^{-1/2}g
\qquad\text{stark in }\mathcal H_2.
\tag{C5e.11}
\]

Nun kürzt sich die problematische positive Quadratwurzel exakt gegen die inverse Target-Gauge:

\[
\begin{aligned}
\langle U_nf,y_n\rangle
&=
\left\langle
B_n^{1/2}JA_n^{-1/2}f,
B_n^{-1/2}g
\right\rangle
\\
&=
\langle JA_n^{-1/2}f,g\rangle.
\end{aligned}
\tag{C5e.12}
\]

Wegen der starken Konvergenz von `A_n^{-1/2}` und der Beschränktheit von `J` folgt

\[
\langle U_nf,y_n\rangle
\to
\langle JA^{-1/2}f,g\rangle.
\tag{C5e.13}
\]

Für den Grenzoperator gilt analog

\[
\begin{aligned}
\langle Uf,y\rangle
&=
\left\langle
B^{1/2}JA^{-1/2}f,
B^{-1/2}g
\right\rangle
\\
&=
\langle JA^{-1/2}f,g\rangle.
\end{aligned}
\tag{C5e.14}
\]

Also

\[
\langle U_nf,y_n\rangle
\to
\langle Uf,y\rangle.
\tag{C5e.15}
\]

Der Wechsel vom bewegten `y_n` zum festen `y` kostet wegen der Isometrie nur

\[
\begin{aligned}
|\langle U_nf,y-y_n\rangle|
&\le
\|U_nf\|\,\|y-y_n\|
\\
&=
\|f\|\,\|y-y_n\|
\to0.
\end{aligned}
\tag{C5e.16}
\]

Damit

\[
\langle U_nf,y\rangle
\to
\langle Uf,y\rangle
\tag{C5e.17}
\]

für jedes `y` im Bild von `B^{-1/2}`. Unter Voraussetzung 5 ist dieses Bild dicht; im vorliegenden P11-Fall ist es sogar ganz `\mathcal H_2`. Wegen

\[
\sup_n\|U_nf\|=\|f\|
\]

folgt

\[
U_nf\rightharpoonup Uf.
\tag{C5e.18}
\]

Da sowohl `U_n` als auch `U` Isometrien sind,

\[
\|U_nf\|=\|f\|=\|Uf\|.
\tag{C5e.19}
\]

Schwache Konvergenz plus Normkonvergenz ergibt starke Konvergenz:

\[
\boxed{
U_nf\to Uf.
}
\tag{C5e.20}
\]

Da `f` beliebig war, ist (C5e.9) bewiesen. `\square`

---

# 3. Anwendung auf die even terminal gauge

Setze in Satz C5e.1

\[
A_n=G_{R,T}^{+},
\qquad
B_n=G_{S,T}^{+},
\qquad
A=\Gamma_R^{+},
\qquad
B=\Gamma_S^{+}.
\]

Alle Voraussetzungen sind bereits durch C2 und C5d erfüllt:

- C2: exakte Pullback-Identität und finite-horizon Isometrie;
- C5d: starke Konvergenz beider inverser Quadratwurzeln;
- C5d: exakte Gamma-Pullback-Identität;
- C5d: Positivität und Invertierbarkeit der Gammaoperatoren.

Daher folgt ohne weiteren analytischen Input:

\[
\boxed{
W_{R,S,+}^{[T]}
\xrightarrow[T\to\infty]{\rm s}
W_{R,S,+}^{[\Gamma]}
}
\tag{C5e.21}
\]

für jedes feste `R<S` auf **ganz** `\mathcal K_{X,R}^{+}`.

Dies ist kein bloßer Core-Satz.

---

# 4. C5e-A — Quadratwurzelproblem

Die ursprüngliche Frage lautete, ob man genug Kontrolle auf

\[
J_{R,S}^{+}(G_{R,T}^{+})^{-1/2}f
\]

bekommt, um anschließend

\[
(G_{S,T}^{+})^{1/2}
J_{R,S}^{+}(G_{R,T}^{+})^{-1/2}f
\]

konvergieren zu lassen.

Die Antwort ist:

\[
\boxed{
\text{Ja — aber nicht durch separate Konvergenz der positiven Target-Quadratwurzel.}
}
\]

Die spezielle Sequenz wird nur innerhalb des exakt isometrisch normalisierten Produkts behandelt. Der Target-Faktor wird dual gegen

\[
(G_{S,T}^{+})^{-1/2}g
\]

getestet und verschwindet dadurch algebraisch.

Damit bleibt die C5d-Firewall unangetastet:

\[
\boxed{
\text{C5e beweist nicht }
(G_{S,T}^{+})^{1/2}\xrightarrow{\rm s}(\Gamma_S^{+})^{1/2}
\text{ auf }\mathcal K_{X,S}^{+}.
}
\tag{C5e.22}
\]

Bewiesen ist ausschließlich die wesentlich spezifischere und für den gerichteten Apparat genau ausreichende Aussage (C5e.21).

---

# 5. C5e-B — Formnorm-Route

Die Formnorm-Sequenz aus der Aufgabenstellung ist

\[
\boxed{
x_T:=J A_T^{-1/2}f.}
\tag{C5e.23}
\]

Aus (C5e.8) und der Beschränktheit von `J` folgt unmittelbar

\[
\boxed{
x_T\to x:=JA^{-1/2}f}
\tag{C5e.24}
\]

stark in `\mathcal H_S`.

Außerdem ist die Formenergie nicht nur asymptotisch kontrolliert, sondern **exakt konstant**:

\[
\begin{aligned}
\mathfrak q_{S,T}^{+}[x_T]
&=
\|B_T^{1/2}x_T\|^2
\\
&=
\|U_Tf\|^2
\\
&=
\|f\|^2.
\end{aligned}
\tag{C5e.25}
\]

Im Grenzsystem ebenso:

\[
\begin{aligned}
q_{\Gamma,S}^{+}[x]
&=
\|B^{1/2}x\|^2
\\
&=
\|Uf\|^2
\\
&=
\|f\|^2.
\end{aligned}
\tag{C5e.26}
\]

Also

\[
\boxed{
\mathfrak q_{S,T}^{+}[x_T]
\to
q_{\Gamma,S}^{+}[x]
}
\tag{C5e.27}
\]

sogar mit Gleichheit aller Werte.

## Firewall B

Aus

\[
x_T\to x
\]

und

\[
\mathfrak q_{S,T}^{+}[x_T]
\to q_{\Gamma,S}^{+}[x]
\]

allein darf **nicht** ohne Zusatzargument gefolgert werden, dass

\[
B_T^{1/2}x_T\to B^{1/2}x
\]

stark. Die Formenergien kontrollieren die Normen, aber nicht von selbst die Richtung der Bildvektoren in einem variierenden Operatorproblem.

Genau diese fehlende Richtungsinformation liefert Satz C5e.1 über die bewegten inversen Gauge-Testvektoren.

Damit ist die Formnorm-Route diagnostisch korrekt, aber erst zusammen mit der inverse-gauge Dualität vollständig.

---

# 6. C5e-C — Polarbildraum-Route

Die alternative Darstellung

\[
W_{R,S}^{[T]}=V_{S,T}^{*}V_{R,T}
\]

bleibt strukturell richtig und erklärt die Isometriegeometrie. Für den Grenzübergang wäre eine separate Konvergenz der zugehörigen Polarbildräume jedoch zusätzlicher Aufwand: Man müsste eine geeignete Topologie für die variierenden Bildprojektionen kontrollieren.

C5e benötigt diesen Schritt nicht.

Die Polarstruktur wird nur in ihrer bereits bewiesenen Konsequenz benutzt:

\[
\|W_{R,S,+}^{[T]}f\|=\|f\|.
\]

Diese uniforme Normidentität ist genau das, was den Fehler

\[
\langle U_Tf,y-y_T\rangle
\]

im moving-test Beweis auf null zwingt.

Urteil zu Route C:

\[
\boxed{
\text{kompatibel, aber für C5e nicht erforderlich.}
}
\tag{C5e.28}
\]

Es wird insbesondere **keine** Konvergenz verschachtelter Polarbildräume behauptet.

---

# 7. Exakter gerichteter Gamma-Apparat im geraden Kanal

Für feste

\[
R<S<U
\]

gilt bereits auf Gamma-Ebene

\[
\begin{aligned}
W_{S,U,+}^{[\Gamma]}W_{R,S,+}^{[\Gamma]}
&=
(\Gamma_U^{+})^{1/2}
J_{S,U}^{+}
(\Gamma_S^{+})^{-1/2}
(\Gamma_S^{+})^{1/2}
J_{R,S}^{+}
(\Gamma_R^{+})^{-1/2}
\\
&=
(\Gamma_U^{+})^{1/2}
J_{R,U}^{+}
(\Gamma_R^{+})^{-1/2}
\\
&=
W_{R,U,+}^{[\Gamma]}.
\end{aligned}
\]

Also

\[
\boxed{
W_{S,U,+}^{[\Gamma]}W_{R,S,+}^{[\Gamma]}
=
W_{R,U,+}^{[\Gamma]}.
}
\tag{C5e.29}
\]

Zusammen mit

\[
(W_{R,S,+}^{[\Gamma]})^{*}W_{R,S,+}^{[\Gamma]}=I
\]

und (C5e.21) erhält man einen echten kohärenten isometrischen gerichteten Grenzapparat auf dem gesamten geraden Kanal.

Wichtig ist der Scope:

\[
\boxed{
\text{Dies ist ein Satz über den geraden Source-/Graphsektor von P11.}
}
\]

Er löst weder den ungeraden Boundary-Jet-Kanal noch die globale Objekt-X-Positivitätsfrage und ist kein RH-Beweis.

---

# 8. Was C5e nicht beweist

Nicht bewiesen und nicht benötigt sind:

1. globale starke Operator-Konvergenz
   \[
   (G_{S,T}^{+})^{1/2}
   \to
   (\Gamma_S^{+})^{1/2};
   \]
2. eine uniforme Schranke
   \[
   \sup_T\|G_{S,T}^{+}\|<\infty;
   \]
3. Konvergenz der Polarbildprojektionen `V_{S,T}V_{S,T}^{*}`;
4. irgendeine entsprechende Aussage im ungeraden Kanal;
5. Positivität der vollständigen Weilform oder RH;
6. ein SYN oder Seal von P11.

Diese Firewalls sind wesentlich, weil der Beweis die Target-Quadratwurzel **nur innerhalb der normalisierten Isometrie** kontrolliert.

---

# 9. C5e-Endsatz

## Satz C5e.2 — even terminal-gauge limit

Für jedes feste `R<S` gilt auf dem gesamten geraden Graphraum

\[
\boxed{
W_{R,S,+}^{[T]}
\xrightarrow[T\to\infty]{\rm s}
(\Gamma_S^{+})^{1/2}
J_{R,S}^{+}
(\Gamma_R^{+})^{-1/2}.
}
\tag{C5e.30}
\]

Der Grenzoperator ist eine Isometrie, und die Familie erfüllt den exakten gerichteten Kokyklus

\[
\boxed{
W_{S,U,+}^{[\Gamma]}W_{R,S,+}^{[\Gamma]}
=
W_{R,U,+}^{[\Gamma]}.
}
\tag{C5e.31}
\]

Damit ist der in C5d verbliebene **even terminal gauge / target-square-root**-Engpass geschlossen.

Die mathematisch relevante neue Einsicht lautet:

\[
\boxed{
\text{inverse square-root convergence}
+
\text{exact metric pullback}
+
\text{isometry}
\Longrightarrow
\text{strong terminal-gauge convergence}.
}
\tag{C5e.32}
\]

Die positive Target-Quadratwurzel muss nicht separat konvergieren.

---

# 10. Folgeknoten

C5e schließt den geraden relativen Transport. Der nächste erzwungene Schritt liegt deshalb **nicht** mehr in C5a/b/c/d und auch nicht in einer weiteren globalen Quadratwurzelabschätzung.

Der offene Hauptkontrast lautet nun:

- **gerader Kanal:** kanonischer kohärenter Gamma-Grenztransport existiert;
- **ungerader Kanal:** absolute Zukunftsmetriken divergieren, vollständiger Boundary-Jet kodiert den ganzen Sektor, relativer Transport bleibt offen.

Der natürliche nächste Auditknoten sollte daher den **ungeraden relativen Terminaltransport** direkt auf dem Cross-Terminal-Kern

\[
\mathscr K_{R,S}^{T,U}
=
(W_{R,S}^{[T]})^{*}W_{R,S}^{[U]}
\]

beziehungsweise nach einer geeigneten ungeraden Renormierung untersuchen.

P11 bleibt dabei ausdrücklich

\[
\boxed{\texttt{PASS-A ACTIVE}}
\]

ohne SYN und ohne Seal.
