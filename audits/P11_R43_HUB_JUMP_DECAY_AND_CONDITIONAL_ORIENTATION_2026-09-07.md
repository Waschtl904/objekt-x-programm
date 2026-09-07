# P11 / R43: Hub-Sprungabfall und bedingter Orientierungsabschluss

Datum: 2026-09-07. Exakte Basis: korrigierter LOCAL-O1-Head
`775158ee656d03bc3601857e8cb0e47fa791caf1`.

Status bei Erstellung: neue analytische Ableitung zur destruktiven
Exact-Head-Prüfung. Keine Repository-Registry-Promotion, kein Merge,
kein unbedingter Strong-Terminal- oder RH-Beweis.

## Gegenstand und Reichweite

LOCAL-O1 beweist stückweise Operatornormstetigkeit des tatsächlichen
Transports auf jedem beschränkten Terminalintervall, einschließlich
einseitiger Normgrenzwerte an den arithmetischen Hub-Aktivierungen.
Die bisherigen Argumente ließen jedoch eine zusätzliche
Orientierungspflicht nach Tightness offen
([LOCAL-O1](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md),
[bisheriges R43-Sign-Kriterium](https://github.com/Waschtl904/objekt-x-programm/blob/2a43813480629c56200d2910963294fa0c4137fd/audits/P11_REFEREE_E2E_R43_SINGLE_NORMAL_C6_GATE_2026-09-02.md)).

Die folgende Rechnung liefert einen globalen Abfall der einzelnen
Sprunggrößen am echten Operator. Gemeinsam mit LOCAL-O1 folgt daraus:
Wenn die echte Restbahn stark gegen null geht, dann stabilisiert sich
das terminale Vorzeichen automatisch. Der Satz ist eine bedingte
Orientierungsschließung, kein Beweis der benötigten Tightness.

## Feste Räume und einseitige Werte

Fixiere \(0<R<S\). Alle Quellmetriken wirken in den unveränderten
ungeraden Graph-Hilberträumen \(\mathcal H_R,\mathcal H_S\).
Schreibe \(J=J_{R,S}\) für die feste beschränkte Nullerweiterung und
\[
W_V=G_{S,V}^{1/2}JG_{R,V}^{-1/2}.
\]
Die feste Graphraumeinbettung \(j_X:\mathcal H_X\to L^2(\mathbb R)\)
hat Norm höchstens eins. Für \(X=R,S\) gelten
\[
G_{X,V}=\Gamma_X+j_X^*\widehat\Sigma(V)j_X,\qquad
G_{X,V}\succeq c_XI,\qquad
c_X=(1+\|H_X^{\mathrm{hub}}\|^2)^{-1}>0.
\]
Insbesondere ist \(c_X\) unabhängig vom späteren Terminal \(V\);
es wird keine globale obere Metrikschranke vorausgesetzt
([LOCAL-O1, LI9–LI10](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md)).

Die möglichen Sprungstellen sind
\[
\mathcal A=\left\{\frac12\log(p^k):p\ \text{prim},\ k\ge1\right\}.
\]
Diese Menge ist lokal endlich. Zu jedem \(t\in\mathcal A\) gehört
genau ein Paar \((p,k)\), denn eine ganze Zahl kann nicht Potenz
zweier verschiedener Primzahlen sein.

Für \(t>S\) bezeichnen \(G_{X,t-},G_{X,t+}\) und \(W_{t-},W_{t+}\)
die einseitigen Operatornormgrenzen aus LOCAL-O1. Die tatsächlichen
Werte am Aktivierungspunkt sind die rechten Werte, entsprechend
dem originalen Hub-Cutoff mit \(\le\)
([LOCAL-O1, LI6 und §§4–6](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md)).

## Lemma: elementare globale Hubmajorante

Setze
\[
h_t=2\sum_{p^k\le e^{2t}}
\sqrt{\log p}\,p^{-3k/4}.
\]
Dann gilt für \(e^{2t}\ge2\)
\[
h_t\le8\sqrt{2t}\,e^{t/2}.
\tag{J1}
\]

Beweis: Die Primzahlpotenzen sind eine Teilmenge der ganzen Zahlen
\(n\ge2\), ohne doppelte Darstellung als \(p^k\). Außerdem ist
\(\sqrt{\log p}\le\sqrt{\log(p^k)}\le\sqrt{2t}\). Somit
\[
h_t\le2\sqrt{2t}\sum_{2\le n\le e^{2t}}n^{-3/4}
\le2\sqrt{2t}\int_1^{e^{2t}}x^{-3/4}\,dx
\le8\sqrt{2t}\,e^{t/2}.
\]
Benutzt werden weder Primzahlsatz noch eine Auslöschung zwischen
Primzahlkanälen. Die Majorante wächst mit \(t\); das wird im
folgenden Sprungtransfer ausdrücklich mitgeführt.

## Lemma: Schur- und Quellmetrik-Sprünge

Sei \(t=\frac12\log(p^k)>S\) und
\[
\alpha_t=\sqrt{\log p}\,p^{-3k/4}
\le\sqrt{2t}\,e^{-3t/2}.
\tag{J2}
\]
Im gemeinsamen Umgebungsraum seien \(\widehat H_{t\pm}\) die
einseitigen Hubwerte. Dann
\[
\widehat H_{t+}-\widehat H_{t-}
=\alpha_t M_tD_{k\log p}M_t=:\Delta H_t,
\qquad
\|\Delta H_t\|\le2\alpha_t.
\tag{J3}
\]
Die Fenster- und Tiefenmasken besitzen an \(t\) denselben starken
Grenzwert von beiden Seiten; der vollständige Rest und seine
Resolvente haben daher keinen arithmetischen Sprung. Es gilt an
diesem einen Aktivierungspunkt für beide Seiten dieselbe
\(\widehat B_t=(I+\widehat R(t)^*\widehat R(t))^{-1}\), mit
\(\|\widehat B_t\|\le1\). Hier wird keine Operatornormstetigkeit der
rohen Resolventen behauptet; ihre einseitigen starken Grenzen
genügen zur Identifikation der beiden Schurwerte
([LOCAL-O1, LI3–LI8](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md)).

Folglich
\[
\begin{aligned}
\widehat\Sigma_{t+}-\widehat\Sigma_{t-}
&=\Delta H_t\,\widehat B_t\,\widehat H_{t+}^*
+\widehat H_{t-}\,\widehat B_t\,\Delta H_t^* .
\end{aligned}
\tag{J4}
\]
Beide einseitigen Hubnormen sind höchstens \(h_t\). Daher
\[
\|\widehat\Sigma_{t+}-\widehat\Sigma_{t-}\|
\le4h_t\alpha_t
\le64t\,e^{-t}.
\tag{J5}
\]
Insbesondere wird der quadratische neue Hubterm nicht verloren;
er steckt in der Verwendung von \(\widehat H_{t+}\) im ersten
Summanden von J4.

Mit der festen Graphraum-Adjunktion und \(\|j_X\|\le1\) folgt
\[
\boxed{\|G_{X,t+}-G_{X,t-}\|\le64t\,e^{-t}},
\qquad X=R,S.
\tag{J6}
\]
Die Gamma-Form ist dabei unverändert. Die Schur-Inkremente dürfen
indefinit sein; J5 und J6 sind Normabschätzungen, keine
Loewner-Monotoniebehauptungen.

## Satz: die echten Transportsprünge verschwinden exponentiell

Für \(t\in\mathcal A\), \(t>\max\{S,1\}\), gilt
\[
\boxed{
\|W_{t+}-W_{t-}\|
\le C_{R,S}\,t^{3/2}e^{-t/2},
}
\tag{J7}
\]
mit der gültigen festen Konstante
\[
C_{R,S}
=32\|J\|
\left[
\frac1{\sqrt{c_Sc_R}}+
\frac{1+8\sqrt2}{c_R^{3/2}}
\right].
\tag{J8}
\]

Beweis: Beide Grenzmetriken erfüllen
\[
c_XI\preceq G_{X,t\pm}\preceq M_tI,\qquad
M_t=1+h_t^2.
\]
Die obere Schranke betrifft genau die Aktivierung \(t\), nicht ein
festgehaltenes globales Intervallende. Sie folgt unmittelbar aus
den tatsächlichen endlichen Summen auf beiden Seiten und LI9;
die rechte Seite enthält genau die Indizes \(p^k\le e^{2t}\)
([LOCAL-O1, LI6–LI10](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md)).

Die nichtkommutativen Wurzelabschätzungen aus LOCAL-O1 ergeben
\[
\|A^{1/2}-B^{1/2}\|\le\frac{\|A-B\|}{2\sqrt c},
\qquad
\|A^{-1/2}-B^{-1/2}\|
\le\frac{\|A-B\|}{2c^{3/2}}
\quad(A,B\succeq cI)
\]
([LI12–LI14](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md)).
Die exakte Produktdifferenz ist
\[
\begin{aligned}
W_{t+}-W_{t-}
={}&(G_{S,t+}^{1/2}-G_{S,t-}^{1/2})JG_{R,t+}^{-1/2}\\
&+G_{S,t-}^{1/2}J
(G_{R,t+}^{-1/2}-G_{R,t-}^{-1/2}).
\end{aligned}
\]
Mit J6 erhält man deshalb
\[
\|W_{t+}-W_{t-}\|
\le32\|J\|\,t e^{-t}
\left[
\frac1{\sqrt{c_Sc_R}}
+\frac{\sqrt{1+h_t^2}}{c_R^{3/2}}
\right].
\tag{J9}
\]
Nun sind \(\sqrt{1+h_t^2}\le1+h_t\),
\(h_t\le8\sqrt{2t}e^{t/2}\) und
\(t e^{-t}\le t^{3/2}e^{-t/2}\) für \(t\ge1\).
Einsetzen liefert J7–J8. Dies beweist den Satz am vollständigen
Transport zwischen den wirklichen Graph-Hilberträumen.

Die Schranke kontrolliert ausschließlich die einzelnen
Aktivierungssprünge. Weder die kontinuierliche Bewegung zwischen
ihnen noch die Summe über alle Aktivierungen ist dadurch
kontrolliert. Insbesondere wird keine uniforme kleine
Normbewegung auf jedem Intervall fester Länge behauptet.

## Satz: Tightness schließt nun die Orientierung mit

Bezeichne wie in R43
\[
w_V=W_V\varepsilon_R=b_V\varepsilon_S+h_V,\qquad
b_V\in\mathbb R,\qquad \|h_V\|^2=1-b_V^2.
\]
Die Realität folgt aus den reellen P11-Formen, der
konjugationsverträglichen Funktionalrechnung und der festen
kanonischen reellen Wahl der Normalen; sie ist nicht eine
nachträgliche terminalabhängige Phasenwahl
([R43.44–R43.47](https://github.com/Waschtl904/objekt-x-programm/blob/2a43813480629c56200d2910963294fa0c4137fd/audits/P11_REFEREE_E2E_R43_SINGLE_NORMAL_C6_GATE_2026-09-02.md)).

**Behauptung:** Unter \(\|h_V\|\to0\) besitzt \(b_V\) ein
gemeinsames terminales Vorzeichen und
\[
w_V\longrightarrow\sigma\varepsilon_S
\quad\text{für ein }\sigma\in\{-1,1\}.
\tag{J10}
\]

Beweis: Aus der Voraussetzung folgt \(|b_V|\to1\). Wähle einen
festen hinreichend späten Start \(T_*>S\), sodass
\[
|b_V|>3/4\quad(V\ge T_*),\qquad
\|W_{t+}-W_{t-}\|<1
\quad(t\in\mathcal A,\ t\ge T_*).
\]
Die zweite Wahl ist durch J7 möglich, die erste durch die
ausdrückliche Tightness-Voraussetzung. Beide Bedingungen gelten
auf dem gesamten reellen Tail, nicht nur an Abtastpunkten.

Auf jeder offenen Aktivierungszelle ist \(b_V\) stetig nach
LOCAL-O1. Dort kann das Vorzeichen nicht wechseln, da ein Wechsel
einen Nullwert erzwingen würde. Die einseitigen Grenzwerte an einer
späten Aktivierung haben Betrag mindestens \(3/4\). Entgegengesetzte
Vorzeichen würden daher
\[
|b_{t+}-b_{t-}|\ge3/2
\]
ergeben; andererseits gilt
\[
|b_{t+}-b_{t-}|
\le\|W_{t+}-W_{t-}\|<1.
\]
Das ist unmöglich. Der tatsächliche Wert am Sprungpunkt ist der
rechte Grenzwert, sodass kein isolierter Ausreißer übrig bleibt.

Zwischen zwei beliebigen endlichen Horizonten jenseits \(T_*\)
liegen nur endlich viele Aktivierungen. Die Vorzeichenübereinstimmung
propagiert durch diese Zellen und Sprungstellen. Also ist das
Vorzeichen auf dem gesamten Tail gleich \(\sigma\); aus
\(|b_V|\to1\) und \(h_V\to0\) folgt J10.

Der Beweis importiert keine globale Stetigkeit oder Darboux-Eigenschaft.
Er nutzt die jetzt bewiesene zellenweise Stetigkeit und zusätzlich
die neue quantitative Schranke der tatsächlichen Sprünge.

## Konsequenz für den C6-Beweispfad

R43 leitet unter seinen ausgewiesenen GC-AC-/Zyklizitätsannahmen
aus B-FLAGTIGHT die Aussage \(h_V\to0\) ab. Gemeinsam mit J10 und
dem R42-Normalbahnrahmen ergibt sich damit
\[
\boxed{
\text{unter dem genannten P11-/R42-/GC-AC-Rahmen:}\qquad
\mathrm{B\!-\!FLAGTIGHT}_{R,S}
\ \Longleftrightarrow\
\mathrm{C6}_{R,S}.
}
\tag{J11}
\]
Die Vorwärtsrichtung benutzt den neuen bedingten
Orientierungsabschluss. Für die Rückrichtung liegt ein starker
Normalbahn-Limes unter dem GC-AC-Clusterinput in
\(\mathbb C\varepsilon_S\); damit ist \(h_V\to0\), also
Flag-Tightness
([R43-Normalbahn- und Tightness-Rahmen](https://github.com/Waschtl904/objekt-x-programm/blob/2a43813480629c56200d2910963294fa0c4137fd/audits/P11_REFEREE_E2E_R43_SINGLE_NORMAL_C6_GATE_2026-09-02.md),
[Flag-Tightness-Kriterium](https://github.com/Waschtl904/objekt-x-programm/blob/2a43813480629c56200d2910963294fa0c4137fd/audits/P11_R43_FLAG_TIGHTNESS_COCYCLE_AND_SIGN_HARDENING_2026-09-03.md)).

GC-AC und die jeweiligen R42-/Flaggen-Eingänge behalten ihren
bisher ausgewiesenen Status. J11 ist kein unbedingter C6-Beweis
und keine automatische Aufwertung eines Candidate-Eingangs.
Der neue Inhalt ist enger: Eine **zusätzliche unabhängige
Orientierungsabschätzung nach starker Rest-Tightness** ist für
diese konkrete P11-Familie nicht mehr nötig.

Es wurde weder \(\|h_V\|\to0\), das globale Flagbudget noch
kanonischer Reverse-Normal-Decay bewiesen. Kleine Sprünge lassen
weiterhin kontinuierliche Flucht in immer tiefere Flaggen zu.

## Exaktes Endpunkt-/Ausschlagsbudget

Die vorgeschlagene Budgetabschwächung ist von J1–J11 unabhängig.
Sie dient ausschließlich dazu, die verbleibende Tightness-Aufgabe
nicht unnötig durch das Aufsummieren zurückgenommener Ausschläge
zu verstärken.

Fixiere eine von \(m\) unabhängige, den ganzen Tail abdeckende
Kette \(U_k\to\infty\). Für \(q_m(U)=\|P_mw_U\|^2\) seien
\[
\delta_{m,k}=(q_m(U_{k+1})-q_m(U_k))_+,\qquad
\Omega_{m,k}=\sup_{V\in[U_k,U_{k+1}]}
(q_m(V)-q_m(U_k))_+,
\]
\[
\mathcal B_{m,K}=\sup_{N\ge K}
\left(\sum_{j=K}^{N-1}\delta_{m,j}+\Omega_{m,N}\right).
\tag{J12}
\]
Dann gilt durch exaktes Teleskopieren
\[
\sup_{V\ge U_K}q_m(V)
\le q_m(U_K)+\mathcal B_{m,K},
\qquad
\mathcal B_{m,K}\le\sum_{k\ge K}\Omega_{m,k}.
\tag{J13}
\]

Für die praktische Aufteilung setze
\[
S_{m,K}:=\sum_{j\ge K}\delta_{m,j},\qquad
O_{m,K}:=\sup_{N\ge K}\Omega_{m,N}.
\]
Im erweiterten nichtnegativen Sinn gilt sogar
\[
\boxed{
\max\{S_{m,K},O_{m,K}\}
\le\mathcal B_{m,K}
\le S_{m,K}+O_{m,K}
\le2\max\{S_{m,K},O_{m,K}\}.
}
\tag{J14}
\]
Die untere Schranke für \(S\) folgt aus den monoton wachsenden
Partialsummen, die für \(O\) aus ihrer Nichtnegativität; die
obere ist unmittelbar. Daher genügen **aufsummierte positive
Endpunktzuwächse plus ein einziger supremaler später Ausschlag**,
nicht die Summe aller vorübergehenden Ausschläge.

Wenn am tatsächlichen P11-Objekt
\[
\forall\epsilon>0\ \exists m,K:
\quad q_m(U_K)+\mathcal B_{m,K}<\epsilon^2
\tag{J15}
\]
bewiesen wird, folgt Flag-Tightness; zusammen mit dem Rahmen von
J11 dann C6. J15 ist hier noch nicht bewiesen.

Auch diese Bedingung ist nur hinreichend. Eine konvergente
Einheitsbahn kann an geraden Endpunkten nach \(e_0\) zurückkehren
und an ungeraden Endpunkten einen Anteil der quadrierten Größe
\(1/k\) in Richtung \(e_k\) tragen; normstetige Verbindungen sind
möglich und konvergieren gleichmäßig gegen \(e_0\). Für jedes feste
\(m\) hat die Summe positiver Endpunktzuwächse dennoch einen
divergenten harmonischen Teil. Dies ist ein abstrakter Hinweis
gegen eine Notwendigkeitsbehauptung, kein P11-Gegenbeispiel.

## Nicht behauptete Folgerungen und Arbeitsstand

- **Keine gesamte Terminalvariation:** J7 darf nicht über eine
  unkontrollierte Anzahl von Aktivierungen aufsummiert werden.
- **Keine kontinuierliche Rate:** LOCAL-O1 liefert Normstetigkeit
  zwischen Aktivierungen, aber noch keine globale Variation dort.
- **Keine unbedingte Orientierung:** Der Beweis J10 verwendet
  ausdrücklich \(|b_V|\to1\), gewonnen aus starker Rest-Tightness.
- **Keine neue GC-AC-Zertifizierung:** Der Rahmen in J11 bleibt
  bedingt auf die bereits ausgewiesenen Eingänge.
- **Keine automatische Statuspromotion:** Weder Registry,
  Strong Terminal, Objekt X noch RH werden hier unbeschränkt
  als abgeschlossen gebucht.

Der nächste noch offene mathematische Hauptauftrag ist eine
echte globale Tightness-Abschätzung, etwa J15 oder ein schwächerer
direkter No-escape-Nachweis. Dieser Text liefert einen
globalen Sprungabfall und nimmt innerhalb des dokumentierten
Rahmens die gesonderte Orientierungspflicht nach Tightness heraus.
