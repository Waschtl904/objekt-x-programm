# Nachweis der positiven Fortsetzung für vier feste Quellen

4. Oktober 2026 · AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN

## 1. Aussage, Koordinaten und Voraussetzungen

Setze \(a=A_8=3\log(2)/2\), \(b=A_9=\log(3)\). \(J:F_a\to F_b\) ist die physische Nullfortsetzung. Übernommen werden die dokumentierte Formraumidentifikation, die Operatorformel und die Naturality \(q_b[Ju]=q_a[u]\). Ebenfalls übernommen werden die analytische vollständige alte hohe Reserve \(\delta=2/3\) und die ursprünglichen Modell-/Restidentitäten. Die zugrunde liegenden Dokumente sind mit ihrem Repository-Stand in `SOURCE_BINDINGS.json` bezeichnet; relevante Originaltexte liegen unter `provenance/`.

Die Paritäten werden getrennt behandelt. \(z_j\) sind die beiden neuen momentkorrigierten physischen Quellen mit Graden \(m=2,4\) bzw. \(m=3,5\), genau wie im vorherigen 764-Paarungs- und Vier-Antworten-Paket. Alle Koeffizienten beziehen sich auf diese unnormalisierte Zweierfamilie. Mit \(Z\alpha=\sum_j z_j\alpha_j\) und \(D=Z^*Q_bZ\) lautet die Aussage

\[
\inf_{u\in F_a^p}q_b[Ju+Z\alpha]
=\alpha^*S_p\alpha\ge\kappa_p\|\alpha\|_{\mathbb C^2}^2,
\quad
\kappa_0=10^{-5},\quad\kappa_1=33\cdot10^{-6}.
\tag{1}
\]

Die Infimierung geht über den vollständigen alten Formraum. Eine Gesamtpositivität von \(q_b\) wird nicht verwendet. Die Aussage erstreckt sich auf komplexe Koeffizienten, da die reellen symmetrischen Matrixungleichungen auch hermitesch gelten.

Die vorhandenen rationalen Näherungsantworten \(P\) bleiben unverändert. Deren große vollständige Funktionsreste stehen nicht im Widerspruch zu (1): entscheidend ist ihre Energie in der alten inversen Form.

## 2. Vollständige alte Kopplung

Auf \(H=L^2((-1,1),dx/2)\) sei \(\Phi=ME\) die Familie der 191 alten niedrigen momentkorrigierten Profile. \(Y\) enthält alle rohen Grade ab 384 bzw. 385, jeweils mit der alten Formdomäne. Mit \(e=e_p\), der hohen Momentkomponente \(r\) und \(J_Hy=y-e\langle r,y\rangle\) hat jede alte Quelle eindeutig die Koordinaten

\[
u=U_a^{-1}(\Phi x+J_Hy),\quad x\in\mathbb C^{191},\ y\in Y\cap\mathcal D.
\]

In diesem Dokument hat \(B:Y\to\mathbb C^{191}\) niedrige Zeilen. Das entspricht der Orientierung in `A8_PROOF.md`; das gleichnamige B in `GRAPH_SCHUR.md` ist adjungiert. Die tatsächliche alte Form erfüllt

\[
q_a[u]\ge x^*Ax+2\operatorname{Re}(x^*By)+\delta\|y\|^2.
\tag{2}
\]

Die gespeicherten Größen sind \(A_{\rm mod}=\Phi^*Q_a^P\Phi\), \(B_0=\Phi^*Q_a^P|_Y\), \(G_0=B_0B_0^*\). Setze

\[
\gamma_a=\frac{21}{10}\epsilon_{K,a},\quad e_L=4\gamma_a,
\quad e_B=2\gamma_a+24\epsilon_p,
\]
\[
H_B=\frac{1001}{1000}G_0+1001e_B^2I,
\qquad F=A_{\rm mod}-e_LI-\delta^{-1}H_B.
\tag{3}
\]

Hier ist mit \(n=384+p\), \(z_0=21/40\)

\[
\epsilon_p=\frac{z_0^n}{n!\,[1-z_0^2/((n+1)(n+2))]}
\begin{cases}1,&p=0,\\4,&p=1.\end{cases}
\]

Die alten Fehlerformeln geben \(\|B-B_0\|\le e_B\), \(BB^*\preceq H_B\), \(A-\delta^{-1}BB^*\succeq F\). Der neue Lauf bestätigt aus den ursprünglichen Matrixintervallen je 191 positive LDL-Pivots von F.

Für einen alten dualen Quellvektor \(\ell=(c,h)\) folgt aus der exakten quadratischen Ergänzung mit \(y'=y+\delta^{-1}B^*x\) die obere inverse Energie

\[
\ell^*\mathcal Q_a^{-1}\ell\le
\delta^{-1}h^*h+
(c-\delta^{-1}Bh)^*F^{-1}(c-\delta^{-1}Bh).
\tag{4}
\]

Dabei bezeichnet \(\mathcal Q_a\) die alte Form in den Koordinaten \((x,y)\). (4) folgt auch unmittelbar aus dem dualen Supremum \(\sup(2\operatorname{Re}\ell(u)-q_a[u])\). Die obere Rechnung darf das Supremum über alle L²-Koordinaten nehmen; die ursprüngliche Formdomäne kann es nur verkleinern. Die bereits bewiesene alte Koerzivität gewährleistet die tatsächliche inverse Antwort. Es wird keine endliche Approximation dieses Supremums eingesetzt.

## 3. Neue gemischte Quellpaarungen

Sei \(g_j(x)=\sqrt{a/b}\,(\widehat Q_b^{\rm ext}f_{b,m_j})((a/b)x)\) die auf das alte Intervall eingeschränkte neue Wirkung vor der alten Momentprojektion. Dann sind die dualen Komponenten

\[
C=\Phi^*g,\qquad h=J_H^*g.
\]

Das Modell \(\widetilde g\) verwendet den bisherigen neuen Gamma-Grad 128, die glatte Potentialreihe mit 640 Summanden und alle tatsächlichen partiellen Translationen. Setze \(h_0=\Pi_Y\widetilde g\), \(D_0=B_0h_0\). **D₀ wurde neu mit 191×2 Einträgen pro Parität integriert.** Es ist keine Abschätzung nur durch \(\|B_0\|\|h_0\|\).

Die neuen Funktionen werden unmittelbar aus den unveränderten gebundenen Routinen `source_core.py` und `full_gram.py` aufgebaut. Dadurch wird eine numerisch ungünstige Rekonstruktion durch Auslöschung großer alter Antwortpolynome vermieden. Die neuen Koeffizienten überlappen sämtlich die gespeicherten Funktionsintervalle.

Die neuen Integrationen verwenden gerichtete Arb-Polynomarithmetik:

- vollständige Monom- und Logarithmusmomente;
- alle zehn gemeinsamen positiven Integrationszellen der alten und neuen Translationen;
- Abzug sämtlicher 192 roher niedriger Grade je Parität, einschließlich des Momentträgers;
- den vollständigen polynomialen alten Gamma-Anteil.

Für den letzten Punkt wird die exakte Legendre-Primitive benutzt:

\[
\mathcal J e_n=\frac{e_{n+1}}{\sqrt{(2n+1)(2n+3)}}
-\frac{e_{n-1}}{\sqrt{(2n+1)(2n-1)}}.
\]

Für ungerade k und \(n>k+1\) gilt als Polynomidentität

\[
\int_{-1}^1|x-y|^k e_n(y)\,dy=2k!\,\mathcal J^{k+1}e_n(x).
\tag{5}
\]

Die Randpolynome verschwinden wegen der Orthogonalität zu Graden höchstens k. Genau in dem Bereich, der den hohen Raum erreicht, ist \(n\ge224\) bzw. 225 und \(k\le159\). Gerade Kernelpotenzen erreichen diesen hohen Raum nicht. Der Gamma-Modellsupport endet spätestens bei Grad 543. Das begrenzt ausschließlich diesen Polynomanteil; die Logarithmus- und Shiftwirkung bleibt vollständig und der wahre Gamma-Rest wird durch eB bezahlt.

Der separate rationale Prüfer kontrolliert (5) zusätzlich für 36 Paare \(n=10,\ldots,18\), \(k=1,3,5,7\), indem er die Primitive und die direkte stückweise Monomintegration exakt als Polynome vergleicht.

Zwei weitere Kontrollen betreffen die tatsächlichen großen Daten: Alle 764 niedrigen Paarungen stimmen bis zum sicheren Radius \(2\cdot10^{-33}\) mit den vorhandenen Quellmittelpunkten überein. Acht Kontraktionen \(P^*D_0\) überlappen die separat aus vollständigen alten/neuen Gramen mit rohem Niedrigabzug gewonnenen Werte. Die Kontraktionsintervalle müssen schmaler als \(10^{-25}\), einzelne neue Paarungsintervalle schmaler als \(10^{-40}\) sein. Bei 3072 und 4096 Bit sind sämtliche auf 70 Dezimalstellen nach außen gespeicherten numerischen Blöcke identisch.

## 4. Gemeinsames Fehlerbudget für die inverse Energie

\(C_0\) ist der vorhandene rationale Quellmittelpunkt; sein vorher geprüftes gemeinsames Budget lautet

\[
(C-C_0)^*(C-C_0)\preceq B_C.
\]

Die Gamma-Abweichung, der vollständige Rest der glatten Potentialreihe und die hohe Momentkorrektur werden einzeln bezahlt. Der Lauf prüft je Spalte

\[
\|h_j-h_{0,j}\|<7\cdot10^{-21},\qquad
(h-h_0)^*(h-h_0)\preceq B_h:=2(7\cdot10^{-21})^2I_2.
\tag{6}
\]

Der erste Vergleich verwendet die gespeicherten neuen Quellnormen, den Gamma-Rest \((11/5)\epsilon_{K,128}\), den glatten Potentialrest und \(\epsilon_p(\|\widetilde g_j\|+1)\). Die zugehörige Modell-Grammatrix wird aus dem vollständigen \(\widetilde g\)-Gram durch Abzug aller rohen niedrigen Momente gewonnen. Mit Young-Parameter \(10^{-16}\) entsteht ein tatsächlicher hoher Gram-Majorant \(H_h^+\succeq h^*h\).

Setze

\[
v_0=C_0-\delta^{-1}D_0,\qquad
t\ge\operatorname{tr}(F^{-1}),\quad
\beta\ge\operatorname{tr}(F^{-1}H_B).
\]

Für \(v=C-\delta^{-1}Bh\) ergibt die Aufteilung in \(C-C_0\), \(B_0(h-h_0)\) und \((B-B_0)h\)

\[
(v-v_0)^*F^{-1}(v-v_0)\preceq
\mathcal E:=3\left[tB_C+\delta^{-2}\beta B_h+
\delta^{-2}te_B^2H_h^+\right].
\tag{7}
\]

Hier genügen \(F^{-1}\preceq tI\) und
\(\|F^{-1/2}B_0\|^2\le\operatorname{tr}(F^{-1}G_0)\le\beta\).
Die Rechnung verwendet nach außen eingeschlossene Majoranten aller Terme.

Mit \(V_0^+\succeq v_0^*F^{-1}v_0\) und \(\eta=10^{-7}\) folgt aus (4)

\[
\ell^*\mathcal Q_a^{-1}\ell\preceq
T^+:=\delta^{-1}H_h^++(1+\eta)V_0^+
+(1+\eta^{-1})\mathcal E.
\tag{8}
\]

**Zertifizierung der Inversen.** Ein fester symmetrischer dyadischer Näherungsinverser \(J_F\) wird mit dem vollständigen Intervall-F rückgeprüft. Für \(\rho=\|I-J_FF\|_\infty<1/2\) gilt

\[
\|F^{-1}-J_F\|_2\le\|F^{-1}-J_F\|_\infty
\le\frac{\|J_F\|_\infty\rho}{1-\rho}=e_I.
\tag{9}
\]

Die erste Ungleichung gilt hier wegen der Symmetrie der Differenz. Damit werden t, β und \(V_0^+\) einschließlich des Inversenfehlers nach oben eingeschlossen. Der Lauf ergibt ungefähr \(\beta=36{,}5331\) bzw. \(36{,}3616\); der Operatorfehler der Inversen liegt unter \(3{,}59\cdot10^{-46}\) bzw. \(7{,}54\cdot10^{-52}\). Diese kleinen Fehler ersetzen keine Schranke für die große Norm der Inversen; beide Größen werden getrennt behandelt.

## 5. Restform und getrennte Residualenergie

Mit den unveränderten alten Vorschlägen P und den Restvertretern \(w=Z-J\Phi P\) ist

\[
K=q_b[w]=D-C^*P-P^*C+P^*AP.
\]

Der A9-Modellblock D wird ausschließlich für seine vier Formeinträge pro Parität verwendet. Sein Gamma-Rest vom Grad 224 wird mit \(4\gamma_bI\), \(\gamma_b=(11/5)\epsilon_{K,b}\), bezahlt. Es wird kein A9-Positivitätszertifikat verwendet.

Mit dem symmetrischen rationalen alten Mittelpunkt \(A_0\), \(E_0=C_0-A_0P\) und \(G_P=P^*P\) wird K stabil berechnet als

\[
K_0=D_{\rm mod}-\operatorname{sym}(C_0^*P)
-\operatorname{sym}(P^*E_0),\qquad
\operatorname{sym}(X)=(X+X^*)/2.
\]

Das gemeinsame Fehlerbudget lautet

\[
-E_K\preceq K-K_0\preceq E_K,\quad
E_K=(\alpha+\tau)G_P+\tau^{-1}B_C+4\gamma_bI,
\tag{10}
\]

mit \(\alpha=9{,}55\cdot10^{-99}+(501/500)\gamma_a\), \(\tau=10^{-32}\) gerade bzw. \(10^{-31}\) ungerade. Der Faktor 501/500 ist die vorher separat rational geprüfte Normquadratobergrenze der alten niedrigen Profilabbildung. Die Mittelpunkt- und Intervallfehler sind ebenfalls eingeschlossen.

Sei \(R=\ell-\mathcal Q_aP\) der vollständige alte Residualquellvektor in den entsprechenden alten Koordinaten. Exakt gilt

\[
W=R^*\mathcal Q_a^{-1}R
=\ell^*\mathcal Q_a^{-1}\ell+K-D.
\tag{11}
\]

Aus \(K^-\preceq K\preceq K^+\), \(D^-\preceq D\) und (8) folgt daher

\[
W\preceq W^+:=T^++K^+-D^-,\qquad
S=D-\ell^*\mathcal Q_a^{-1}\ell=K-W\succeq K^--W^+.
\tag{12}
\]

Die exakte Identität in (11) vermeidet die unnötige Multiplikation der vollständigen Residualnorm mit dem winzigen globalen alten Reserveboden. Trotzdem werden in der letzten Ungleichung K und W getrennt eingeschlossen.

Gerundete Anzeigen der Schlussmatrizen \(K^--W^+\):

\[
\begin{pmatrix}
0.0312546739725173&0.0427047920998667\\
0.0427047920998667&0.0583792646719772
\end{pmatrix}
\quad(\text{gerade}),
\]
\[
\begin{pmatrix}
0.0289750884064840&0.0364872187431845\\
0.0364872187431845&0.0460345636353542
\end{pmatrix}
\quad(\text{ungerade}).
\]

Diese Dezimalanzeigen sind keine Zertifikate. Der unabhängige Schlussprüfer nimmt die gespeicherten rationalen Intervallendpunkte, ersetzt Rundungsradien durch sichere diagonale Zeilensummen, bildet K− und W+ neu und prüft die drei Hauptminoren nach Abzug von \(10^{-5}I\) bzw. \(33\cdot10^{-6}I\). Sie sind exakt strikt positiv. Damit folgt (1).

## 6. Aussagegrenzen

Der berechnete positive Anschluss umfasst den vollständigen alten Raum und die vier festgelegten neuen Quellklassen. Er deckt den ganzen neuen Quotientenraum nicht ab. Es wird weder eine neue hohe Antwort als Funktion noch eine gemeinsame intrinsische Geometrie für alle erforderlichen Quellen hergestellt. Insbesondere ist dies noch keine Konstruktion von Objekt X.

Die ursprünglichen Modelle, Formraumidentitäten und alten analytischen Restmajoranten werden übernommen. Der neue Reproduktionslauf baut die gemischten Integrale und alle neuen Energieabschätzungen erneut auf; er erzeugt die alten vollständigen 191-dimensionalen Operatorgramme nicht nochmals aus ihren ursprünglichen Integralen. Externe analytische Prüfung bleibt offen. Repository-Status und GitHub wurden nicht verändert.
