# Der kanonische relative κ-Block

29. September 2026 · AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN

Basis: [`main@8a82b7a972172c45cc4d3bc0297cc7fc0bbb2c7b`](https://github.com/Waschtl904/objekt-x-programm/tree/8a82b7a972172c45cc4d3bc0297cc7fc0bbb2c7b).

## Ergebnis und Reichweite

**Die relative Kopplung lässt sich exakt auf eine 1×1- bzw. 2×2-Matrix auf dem echten kanonischen Ergänzungsraum reduzieren.** Dafür braucht man die Kompression der Energie und der inversen Energie auf diesen Raum. Der 5- bzw. 6-dimensionale transportierte Block muss in der abschließenden Auswertung nicht eigens invertiert werden.

Die vorhandenen Terminalböden und oberen kritischen Spektralschranken liefern außerdem bereits vier rigorose, aber sehr konservative Einschließungen:

| Übergang | Parität | dim E | Sichere Untergrenze für 1−κ |
| --- | --- | ---: | ---: |
| A₈ → A₉ | gerade | 1 | 1.78224·10⁻²⁹ |
| A₈ → A₉ | ungerade | 1 | 2.71653·10⁻³¹ |
| A₉ → A₁₁ | gerade | 2 | 1.18203·10⁻⁴⁴ |
| A₉ → A₁₁ | ungerade | 2 | 2.32270·10⁻⁴⁶ |

Jeweils gilt zusätzlich 1−κ≤1. Die Tabelle gibt **Untergrenzen**, keine gemessenen Größenordnungen des tatsächlichen Rests an. Insbesondere folgt daraus nicht, dass der kanonische κ-Wert nahe eins liegt. Diese Aussage bleibt offen.

Die Grenzen übernehmen die bereits bewiesene Positivität des neuen Terminals. Sie schließen κ<1 retrospektiv ab, liefern aber keinen unabhängigen Renewal-Beweis. **Eine scharfe Einschließung der echten inversen Energiemomente auf E wurde in diesem Block noch nicht berechnet.** Die kleine Matrixformel macht diese verbleibende Aufgabe präzise.

## 1. Exakte Räume und Konvention

Wir verwenden die veröffentlichten Definitionen

\[
b=q+17\|\cdot\|_2^2,\qquad
K_A=\operatorname{ran}\mathbf1_{(0,10^{-4})}(\mathcal A_A),
\]

\[
T=P_BJ_{A,B}|_{K_A},\quad
W=TK_A,\quad E=K_B\ominus_b W.
\]

Die Ränge sind 5→6→8 pro Parität, somit dim E=1 bzw. 2. T ist injektiv. Auf K_B sei

\[
\mathscr A=\mathcal A_B|_{K_B}
=\begin{pmatrix}S&C\\C^*&D\end{pmatrix}
\quad\text{in }W\oplus_b E.
\]

Alle Koordinaten dieser Darstellung sind b-orthonormal. Der robuste Raum K_B^{⊥b} ist q-orthogonal zu K_B. Seine Elimination verändert diesen Block deshalb nicht. Seine bereits bewiesenen Schranken bleiben Teil der vorgelagerten Spektralraumzertifizierung.

Wir verwenden weiterhin die **quadrierte** Norm

\[
\kappa=\|S^{-1/2}CD^{-1}C^*S^{-1/2}\|
=\|S^{-1/2}CD^{-1/2}\|^2.
\tag{1}
\]

Sie ist von der unquadrierten Kopplungsnorm und einer Matrix-Konditionszahl zu unterscheiden. Die winzigen Reserven der früheren Diagnoseräume dürfen nicht als Werte von (1) übernommen werden: Dort wurden andere Räume zerlegt.

## 2. Exakte Reduktion auf E

Sei U eine beliebige b-orthonormale Basismatrix von E. Definiere

\[
D=U^\dagger\mathscr A U,\qquad
H=U^\dagger\mathscr A^{-1}U.
\]

Hier bedeutet H die **Kompression der Inversen**. Im Allgemeinen ist H≠D⁻¹.

**Satz.** Für den bereits positiven Terminal gilt exakt

\[
\boxed{1-\kappa
=\frac1{\lambda_{\max}(D^{1/2}HD^{1/2})}.}
\tag{2}
\]

**Beweis.** Die inverse Blockformel liefert

\[
H=(D-C^*S^{-1}C)^{-1}.
\]

Die beiden Produkte von N=S⁻¹ᐟ²CD⁻¹ᐟ² besitzen dieselben nichtverschwindenden Eigenwerte. Da dim W≥dim E und die Normen beider Produkte gleich sind,

\[
1-\kappa
=\lambda_{\min}(I-N^*N)
=\lambda_{\min}(D^{-1/2}H^{-1}D^{-1/2}).
\]

Invertieren ergibt (2). Die inverse Matrix existiert hier durch die bereits zertifizierte neue Positivität. Eine Wahl einzelner echter Eigenvektoren ist für die Identität nicht nötig.

### Eindimensionale Ergänzung

Für E=span{e} mit ‖e‖b=1 ist (2) eine skalare Gleichung:

\[
\boxed{1-\kappa
=\frac1{q_B[e]\,b_B(e,\mathscr A^{-1}e)}.}
\tag{3}
\]

Seien λ_j die echten b-Spektralwerte in K_B und p_j die quadrierten b-Koeffizienten von e, also p_j≥0 und ∑p_j=1. Dann ist der Nenner

\[
\left(\sum_jp_j\lambda_j\right)
\left(\sum_j\frac{p_j}{\lambda_j}\right)
=1+\sum_{i<j}p_ip_j
\frac{(\lambda_i-\lambda_j)^2}{\lambda_i\lambda_j}.
\tag{4}
\]

Das erklärt die relevante Geometrie: Eine sehr kleine Komponente von e in einer Richtung mit extrem kleiner Energie kann das inverse Moment stark vergrößern. Die bloße räumliche Außenmasse misst diese Komponente nicht. κ=0 gilt in Dimension eins genau dann, wenn e in einem einzigen Eigenraum liegt; verschiedene Eigenwerte mit positiven Gewichten erzeugen Kopplung.

## 3. Formulierung mit physischen L²-Momenten

Der Außenmassenblock definiert eine echte L²-orthonormale E-Basis durch Polarprojektion einer Hilfsbasis. Diese exakte Definition kann weiterverwendet werden. Für eine solche Basismatrix V setze

\[
L=V^*Q_BV,\qquad Z=V^*Q_B^{-1}V,\qquad B_E=L+17I,
\]

\[
R=L+34I+289Z.
\]

Die inverse physische Form ist hier durch das bestehende Terminalzertifikat beschränkt. Weil E⊂K_B und K_B spektral invariant ist, stimmen ihre Einschränkung und die entsprechende Inverse innerhalb K_B überein. Es wird kein hoher Anteil durch Trunkierung ersetzt.

Aus \(\mathcal A_B^{-1}=I+17Q_B^{-1}\) folgt

\[
R_{ij}=b_B(V_i,\mathcal A_B^{-1}V_j).
\]

Damit lautet (2) äquivalent

\[
\boxed{1-\kappa=
\frac1{\lambda_{\max}(R B_E^{-1}L B_E^{-1})}.}
\tag{5}
\]

Das angezeigte Produkt muss nicht symmetrisch sein. Es ist jedoch ähnlich zu der positiv definiten symmetrischen Matrix

\[
L^{1/2}B_E^{-1}R B_E^{-1}L^{1/2}.
\]

Für eine beliebige, nicht L²-orthonormale E-Basis mit Gram-Matrix G gelten dieselben Formeln mit B_E=L+17G und R=L+34G+289Z. Diese Faktoren sind wesentlich.

Bei dim E=2 genügt am Ende die größere Nullstelle des charakteristischen Polynoms des Produkts in (5):

\[
\lambda_+=\tfrac12\left(\operatorname{tr}V_0+
\sqrt{(\operatorname{tr}V_0)^2-4\det V_0}\right),
\quad V_0=R B_E^{-1}L B_E^{-1}.
\]

Ein Intervallprüfer muss die gemeinsame Matrixeinschließung und ihre Positivität erhalten. Eintragsweise Extremwerte eines unsymmetrischen Produkts sind keine Loewner-Schranken.

## 4. Was die vorhandenen Daten bereits rigoros liefern

Aus q_B≥c_BI und der zertifizierten oberen kritischen Rayleighgrenze Θ_B folgt

\[
mI\preceq\mathscr A\preceq MI,
\qquad m=\frac{c_B}{c_B+17},\quad
M=\frac{\Theta_B}{\Theta_B+17}.
\]

Verwendet werden die physischen Böden c₉=10⁻³⁵ und c₁₁=10⁻⁵⁰. Der Nenner enthält hier **17** aus der gemeinsamen b-Norm. Die ursprünglichen Defektböden mit 12 bzw. 13 sind andere Normierungen und werden nicht eingesetzt.

Die oberen Θ-Werte werden aus den beiden veröffentlichten gerichteten physischen Ritzmatrizen neu gebildet. Gleiche Dimension von Testraum und echtem kritischem Raum plus Minimax rechtfertigen die obere Spektralschranke; die Testvektoren werden dabei nicht als Eigenvektoren behandelt.

**Lemma.** Für jede b-orthogonale Zerlegung dieses positiven Spektralbands gilt

\[
\boxed{0\le\kappa\le\left(\frac{M-m}{M+m}\right)^2,
\qquad 1-\kappa\ge\frac{4mM}{(m+M)^2}.}
\tag{6}
\]

**Beweis.** Auf [m,M] gilt λ+mM/λ≤m+M. Funktionalkalkül und Kompression auf E geben

\[
D+mMH\preceq(m+M)I.
\]

Nach Kongruenz mit D¹ᐟ² folgt

\[
D^{1/2}HD^{1/2}
\preceq\frac{(m+M)D-D^2}{mM}
\preceq\frac{(m+M)^2}{4mM}I.
\]

Zusammen mit (2) ergibt dies (6). Die Grenze ist bei alleiniger Kenntnis von m und M scharf: Eine eindimensionale Ergänzung mit gleichen Gewichten in den m- und M-Eigenrichtungen erreicht Gleichheit.

Das ist eine Anwendung der klassischen Kantorovich-/Wielandt-Ungleichungen, keine neue allgemeine Matrixungleichung. Zum Hintergrund siehe Lin und Sinnamon, [The Generalized Wielandt Inequality in Inner Product Spaces](https://arxiv.org/abs/1201.6294), insbesondere die Winkelabschätzungen. Die hier benötigte Form ist oben vollständig hergeleitet.

Die Tabelle am Anfang folgt mit rationaler Arithmetik aus (6). Sie benutzt ausschließlich das Spektralband des neuen Terminals. Die konkrete Lage des transportierten alten Raums verbessert sie noch nicht. Deshalb ist sie ein Kontrollwert für spätere genauere Rechnungen, kein Beleg für eine brauchbare gemeinsame Renewal-Reserve.

## 5. Weshalb die bisherigen Projektorfehler nicht genügen

Schon ein zweidimensionales Beispiel zeigt das Problem. Sei die Energie, bis auf einen gemeinsamen positiven Faktor,

\[
\mathscr A=\operatorname{diag}(\varepsilon,1),\quad
e=(s,c),\quad s^2+c^2=1,
\]

und W das gewöhnliche orthogonale Komplement von e. Dann gilt exakt

\[
1-\kappa=
\frac{\varepsilon}{\varepsilon+(1-\varepsilon)^2s^2c^2}.
\tag{7}
\]

Mit t=1/200, s=2t/(1+t²), c=(1−t²)/(1+t²) und ε=10⁻⁴⁰ ist der Projektorabstand zu einer Eigenrichtung kleiner als 0.01. Trotzdem liegt 1−κ zwischen 10⁻³⁶ und 1.001·10⁻³⁶. Eine gemeinsame Skalierung kann beide Eigenwerte unter die kritische Schwelle bringen, ohne κ zu ändern.

Das ist ein allgemeines Empfindlichkeitsbeispiel, kein Modell des tatsächlichen kanonischen Übergangs. Es beweist, dass eine kleine ungewichtete Winkelgrenze allein keine robuste relative Energieschranke trägt.

Die vorhandenen Polarabstände von ungefähr 0.03–0.07 kontrollieren die L²-Lage der echten Ergänzung. Bei direkter Verwendung von ‖Q_B⁻¹‖≤1/c_B könnten Fehler im inversen Moment um den Faktor 1/c_B verstärkt werden. Höhere Rechenpräzision der gleichen Hilfsintegrale beseitigt diese analytische Unsicherheit nicht. Für eine Verbesserung werden relative Energiefehler oder eine direkte Resolventeneinschließung benötigt.

## 6. Präzises Abnahmekriterium für den nächsten numerischen Schritt

Für eine feste echte b-orthonormale E-Basis genügen gemeinsame positive Loewner-Einschließungen

\[
0<D_-\preceq D\preceq D_+,
\qquad 0<H_-\preceq H\preceq H_+.
\]

Definiere

\[
\Lambda_\pm=\lambda_{\max}(H_\pm^{1/2}D_\pm H_\pm^{1/2}).
\]

Die größte Produkteigenzahl ist für positive Faktoren in jedem Faktor monoton. Daher

\[
\Lambda_-\le\lambda_{\max}(D^{1/2}HD^{1/2})\le\Lambda_+,
\]

\[
\boxed{\frac1{\Lambda_+}\le1-\kappa
\le\min\{1,\frac1{\Lambda_-}\}.}
\tag{8}
\]

Eine noch gröbere Auswertung könnte λmax nach oben durch die Spur begrenzen. In Dimension eins und zwei ist eine gerichtete direkte Eigenwertauswertung jedoch günstig.

Damit lautet die nächste konkrete Rechenaufgabe:

1. L und Z=V*Q_B⁻¹V auf der **echten** kanonischen Ergänzung einschließen; alternativ D und H direkt in einer gemeinsamen b-orthonormalen Basis.
2. Die Übertragung von einer Hilfsbasis in q- und inverser q-Norm bezahlen. Die bisherigen Außenmassenintervalle ersetzen diesen Schritt nicht.
3. Bei Verwendung vollständiger Low-/High-Resolventenabschätzungen den ganzen hohen Raum erhalten.
4. Erst danach (5) oder (8) auswerten und den tatsächlichen Abstand 1−κ beidseitig einschließen.

Die endgültige Matrixgröße beträgt nur 1 bzw. 2. Die Kontrolle ihrer wahren Einträge kann trotzdem Rechnungen mit den vorhandenen vollständigen Modellen erfordern.

Ein über viele Übergänge unabhängiger oberer Wert Λ_+≤C würde retrospektiv 1−κ≥1/C liefern. Für einen **vorwärts gerichteten** Renewal-Satz müssten außerdem die benötigten Räume und inversen Formen ohne bereits vorausgesetzte neue Gesamtpositivität zugänglich sein. Die kleine Matrixformel allein löst diesen logischen Schritt nicht.

## 7. Tatsächlich ausgeführte Prüfung

- 26 Eingabedateien wurden byteweise an `8a82b7a…` gebunden. Die 18 historischen Quellenbindungen des Außenmassenpakets stimmen unverändert.
- Die oberen physischen Ritzgrenzen wurden aus der Hülle der veröffentlichten 1024-/1280-Bit-Intervallmatrizen mit exakten rationalen Zahlen erneut gebildet und gegen den bestehenden Prüfbeleg verglichen.
- Alle vier Grenzen aus (6) sowie ihre nach unten gerundeten Anzeigen wurden exakt rational berechnet.
- Neun rationale Formelprüfungen bestanden: sechs nichtorthogonale E-Basen der Dimension 1/2 mit drei Formverschiebungen, zwei scharfe Spektralbandbeispiele und das Empfindlichkeitsbeispiel (7). Sie prüfen Normierungsfaktoren, Schur-/Inverse-Kompression, nichtverschwindende Kopplungseigenwerte und die Bandgrenze. Der allgemeine Beweis steht in diesem Bericht; endliche Beispiele ersetzen ihn nicht.
- Die ursprünglichen Terminalmodelle, vollständigen Spektralzertifikate und Integrations-CI wurden in diesem Block nicht neu ausgeführt. Sie bleiben gebundene Voraussetzungen.

Die maßgeblichen rationalen Ergebnisse stehen in `verification.json`. `verify_relative_kappa.py` verwendet nur die Python-Standardbibliothek.

Dieser Block wurde lokal erstellt. Main und Registry bleiben auf dem bestätigten integrierten Stand; PR #187 ist keine Eingabe. Der neue Befund ist eine exakte Reduktion mit geerbten κ-Schranken. **Eine scharfe kanonische κ-Messung und ein allgemeiner Renewal-Satz bleiben offen.**
