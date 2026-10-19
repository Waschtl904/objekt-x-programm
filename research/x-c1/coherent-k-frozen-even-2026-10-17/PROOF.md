# Ein gemeinsames k-Ellipsoid für den festen geraden Kandidaten

17. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN.**
Alle Aussagen sind bedingt auf die gebundenen Operator-, Domänen- und vollständigen
Quellenmodellvoraussetzungen. Die großen Quellenintegrationen werden hier nicht
unabhängig repliziert. Der Kandidat aus #232 bleibt exakt eingefroren; der
gerichtete Skalar aus #233 und das tatsächliche K_P aus #234 sind Eingaben.

## 1. Ergebnis und Reichweite

Für den festen geraden Kandidaten ist der modellierte Residualskalar eingeschlossen
in

\[
\mathcal L=[1.238460,\;1.748815].
\]

Der bisherige Stand aus #234 war \([-5.961,8.948]\) und damit unentschieden.
Die neue Einschließung folgt aus vollständigem Fehlertransport, ohne numerischen
hohen Mittelpunkt. Die hinreichende Ausschlussschwelle bleibt ungefähr
3.31424941794. Der stärkere Vergleich verwendet sogar den **unteren** Endpunkt
des tatsächlichen K_P-Intervalls:

\[
\sup|\mathcal L|+\varepsilon_D
 <\sqrt{(10q/11)\,\underline K_P},
\]

mit einer gerichteten Reserve größer als 1.56543546. Dabei ist
\(\varepsilon_D\) die gebundene skalare Antwortmodellfehlergrenze. Das ist ein
**DOES_NOT_EXCLUDE_FOR_DIRECTION** für genau diese Richtung. Es bestätigt
weder die Antwortregel noch N12 oder einen Vergleich auf dem ganzen Schalenraum.

## 2. Exakte Zerlegung und nur eine Änderung von k

Wir übernehmen die Räume, Momentabbildung M, Phi, T_h, B, C, delta und rho aus
`gpt2-stufe4-hochantwort/HERLEITUNG.txt`, insbesondere

\[
V=C^*(\Phi^*-BT_h/\delta),\quad
U_8=T_h^*T_h/\delta+V^*V/(1-\rho),\quad \delta=18219/10000.
\]

C ist die rationale Kongruenzmatrix; ihr Faktor \(1/(1-\rho)\) wird nicht
weggelassen. F bezeichnet die zwölf physischen alten Quellen. Für ihre ganze
Operatorquellenfamilie g_F definieren wir

\[
Y_F=T_hg_F,\quad V_F=Vg_F,\quad C_F=CV_F/(1-\rho),\quad
R_F=Y_F-B^*C_F.
\]

Dann ist \(U_8g_F=\Phi C_F+T_h^*R_F/\delta\). Mit
\(H=F-J_{old}U_8g_F\) gilt bei festem k_0 und festem X_fix

\[
\chi_p(k)-\chi_p(k_0)=-H\Delta k,\qquad \Delta k=k-k_0.
\]

Das gebundene Paket gibt \(\|\Delta k\|_K\le\eta\) und die exakt rationale
Matrix \(G=\eta^2K^{-1}\). Der Prüfer bestätigt 12 positive rationale
LDL-Pivots, alle 144 Einträge von \(KK^{-1}=I\) und alle 144 Einträge dieser
G-Identität. k_0 wird mit der ursprünglichen Psi-Definition exakt abgeglichen.

Für die gebundenen Residualdaten h, h_8 schreiben wir
\(\ell=\Phi^*h_8\), \(b_F=F^*h\), \(y_h=T_hh_8\). Der gesamte
k-abhängige Skalar besitzt den Kovektor

\[
a=b_F-C_F^*\ell-R_F^*y_h/\delta.
\]

Sein Fehler ist höchstens \(\sqrt{a^*Ga}\). Wir zertifizieren eine konservative
Obergrenze dafür. Die bisherigen getrennten Budgets `psi_k_coherent_error`,
`finite_response_k_change_error` und die tatsächliches-k enthaltende alte
Hochantwortschranke werden **nicht zusätzlich addiert**.

## 3. Ganze Modellantworten aus vorhandenen Gram-Matrizen

Ein Index 0 bezeichnet das feste Quellen-/Kopplungsmodell. Die gebundenen
niedrigen Matrizen liefern

\[
V_{F0}=C^*(L_{F0}-B_0Y_{F0}/\delta),\qquad
C_{F0}=CV_{F0}/(1-\rho),\qquad a_0=b_F-C_{F0}^*\ell.
\]

Die ganze hohe Familie braucht kein neues Funktionsnetz. Mit
\(H_F=Y_{F0}^*Y_{F0}\), \(B_F=B_0Y_{F0}\), \(G_0=B_0B_0^*\) gilt

\[
\mathcal R_0=R_{F0}^*R_{F0}
=H_F-B_F^*C_{F0}-C_{F0}^*B_F+C_{F0}^*G_0C_{F0}.
\]

Die Felder stammen aus dem hashgebundenen Stufe-3-Archiv:
`source_c_model`, `source_Bh_model`, `source_h_gram_model` und
`old_raw_coupling_gram` (letzteres mit dem dokumentierten Faktor 10^-100).
Es wird **keine hohe Legendre-Summe abgeschnitten**. Als Zusammensetzungskontrollen
prüfen wir alle 144 Einträge von

\[
H_F=\delta(U_{F0}-V_{F0}^*V_{F0}/(1-\rho)),
\]

die 144 Symmetrieeinträge von \(\mathcal R_0\), die 191 Koordinaten des
geerbten festen c_0 und die ganze feste Norm \(\|r_0\|^2\) aus dem
Hochantwortzertifikat. Beim H_J-Feld bleibt dessen alter Faktor 91/50 erhalten;
er wird nicht mit der neuen delta verwechselt. Intervallüberschneidungen sind
Zusammensetzungskontrollen, keine erneute unabhängige Quellenintegration.

Der bereits hergeleitete Momentlift liefert

\[
\|y_h\|\le\nu:=\sqrt{\gamma_M\|h_8\|^2-\|\ell\|^2},
\]

mit oberem gamma und gerichteter Intervallauswertung. Die Subtraktion findet
in orthogonalen Legendre-Koordinaten von \(M^*Uh_8\) statt, nicht in einer
angeblich orthogonalen physischen Phi-Basis.

Für den ganzen Modell-k-Term gilt folglich

\[
\|G^{1/2}a\|\ \le\ \sqrt{a_0^*Ga_0}
+\frac{\nu}{\delta}\sqrt{\operatorname{tr}(G\mathcal R_0)}
+\text{Modellfehler}.
\]

Dies benutzt das Hilbert--Schmidt-Majorant für \(R_{F0}G^{1/2}\).
Die verbleibende Dreiecksungleichung zwischen endlichem Kovektor und hoher
Paarung nimmt weder Unabhängigkeit noch verschwindende Kreuzterme an.
Es ist eine Obergrenze für **ein** Ellipsoidsupport, keine exakte Auswertung
des hohen Kovektors und keine mehrfache Bezahlung unabhängiger k-Fehler.

## 4. Vollständige Modellfehler im gemeinsamen Ellipsoid

E_F ist der Gram der **normalisierten vollständigen Featurefehler** aus
REFINED_COMMON96, E_hF der Gram der hohen Quellenfehler, e_B die gebundene
Kopplungsfehlernorm. Mit \(X=CC^*/(1-\rho)\),
\(J=\sqrt{\operatorname{tr}(XH_B)}\), \(H_B\succeq BB^*\), setzen wir

\[
e_F=\sqrt{\operatorname{tr}(GE_F)},\quad
e_y=\sqrt{\operatorname{tr}(GE_{hF})},\quad
e_c=e_B\sqrt{\operatorname{tr}(GC_{F0}^*C_{F0})}.
\]

Die geerbte Featureabschätzung impliziert
\(\|(V_F-V_{F0})G^{1/2}\|_{HS}\le\sqrt{1-\rho}\,e_F\).
Die exakte Differenzidentität

\[
R_F-R_{F0}=(Y_F-Y_{F0})-(B-B_0)^*C_{F0}-B^*(C_F-C_{F0})
\]

ergibt
\(\|(R_F-R_{F0})G^{1/2}\|_{HS}\le e_y+e_c+Je_F\).
Damit ist eine vollständige Supportobergrenze

\[
\kappa_k=\sqrt{a_0^*Ga_0}
+\frac\nu\delta\sqrt{\operatorname{tr}(G\mathcal R_0)}
+\frac{\|C^*\ell\|}{\sqrt{1-\rho}}e_F
+\frac\nu\delta(e_y+e_c+Je_F).
\]

Alle Modellfehler dürfen korreliert sein. Der Prüfer erhält, gerundet:

| Bestandteil | gerichtete Obergrenze |
|---|---:|
| gemeinsamer endlicher k-Kovektor | 4.339076e-6 |
| ganze hohe Modell-k-Antwort | 5.033630e-6 |
| Featuremodellfehler im endlichen k-Term | 4.023e-18 |
| Quellen-/Kopplungsmodellfehler im hohen k-Term | 6.383e-18 |
| gesamter einmaliger k-Support | 9.372706e-6 |

Insbesondere wird die große Zahl 2.791419… aus der vorherigen getrennten
Normschranke nicht übernommen. Die gerichteten Intervalle des Skalars,
des Kovektors und aller Matrixeinträge enthalten die Rundungsfehler.

## 5. Fester k_0-Anteil und Endintervall

Für die feste Quelle bei k_0 bleiben aus den Vorgängerpaketen die
Fehlergrenzen e_fixed für das normalisierte Feature, e_y,fixed für den hohen
Quellenanteil und die Modelle c_0, r_0 gebunden. Daher

\[
R_{high,0}=\frac\nu\delta\left(
\|r_0\|+e_{y,fixed}+e_B\|c_0\|+J e_{fixed}\right),\qquad
R_{fin,0}=\frac{\|C^*\ell\|}{\sqrt{1-\rho}}e_{fixed}.
\]

Gerichtet sind \(R_{high,0}<0.255167454\) und
\(R_{fin,0}<1.151\cdot10^{-10}\). Der gerichtete I_0-Eingang einschließlich
sämtlicher Koeffizienten- und Integrationsreste bleibt unverändert. Der
zusätzliche Quellenfunktionsmodellrest aus #233 wird ebenfalls vollständig
übernommen. Wir bilden

\[
\mathcal L=I_0+[-R,R],\qquad
R=\kappa_k+R_{fin,0}+R_{high,0}+E_{source}.
\]

Das resultierende Intervall liegt vollständig im bisherigen Intervall aus #234.
Kein numerisch geschätzter hoher Anteil verschiebt den Mittelpunkt.
Die in #234 verwendete Schwelle
\(\sqrt{(10q/11)\overline K_P}+\varepsilon_D\) wird anhand des gebundenen
Budgets neu abgeglichen. Zusätzlich besteht der strengere Vergleich aus §1,
sodass hier nicht allein eine grobe K_P-Obergrenze den Nichtausschluss erklärt.

## 6. Abnahme und offene Prüfung

Pflichtprüfungen sind Eingabe- und Eigenhashes, exakte K-Identitäten und positive
Pivots, die genannten Zusammensetzungskontrollen, alle gerichteten
Fehlerbestandteile, beide Schwellenvergleiche sowie bytegleicher Replay aus
einem frischen Repository-Archiv. Der Replay führt keine Subprozesse aus.

Offen bleibt die externe mathematische Prüfung dieser Herleitung und ihrer
übernommenen Operator-/Quellenvoraussetzungen. Determinismus, Hashbindungen
und CI sind keine solche Prüfung. Es gibt keine neue Richtungsoptimierung,
keine Zertifizierung des ganzen Grad-11-Raums und keine N12-Statuspromotion.
