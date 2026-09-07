# P11 / R43: Conditioning-Uniformität über alle Zukunftshorizonte

Datum: 2026-09-07. Definitionsbasis:
`775158ee656d03bc3601857e8cb0e47fa791caf1` einschließlich LOCAL-O1.
Neue analytische Ableitung zur Exact-Head-Prüfung, keine
Registry-Promotion und kein globaler C6-Abschluss.

## Aussage und ihre entscheidende Begrenzung

Fixiere \(0<R<S<U<\infty\). Für diesen festen alten Horizont \(U\)
sei \(V\) beliebig in \((U,\infty)\). Dann sind die tatsächlichen
Conditioning-Metriken \(G_{X,\mathrm{cond}}^{U,V}\), \(X=R,S\),
relativ kompakt in Operatornorm. Beide vollständigen O1-Kanäle
dieses Conditioning-Schritts erfüllen
\[
\boxed{
\lim_{m\to\infty}\sup_{V>U}
\left(
\|P_m\mathcal T_{\mathrm{mod}}^{\mathrm{cond}}(U,V)\|
+\|P_m\mathcal T_{\mathrm{ph}}^{\mathrm{cond}}(U,V)\|
\right)=0.
}
\tag{CF1}
\]

Dies betrifft die exakte Zwischenmetrik aus PR66, nicht die
vollständige Terminalmetrik \(G_{X,V}\). Der alte Hub bleibt fest.
Uniformität über alle Zukunftshorizonte \(V\) bei festem \(U\)
ist **keine** gemeinsame Uniformität in \(U,V\to\infty\)
([PR66, BR1–BR7](https://github.com/Waschtl904/objekt-x-programm/blob/2a43813480629c56200d2910963294fa0c4137fd/audits/P11_R43_COND_DIRECT_FLAGDYN_REVERSE_NORMAL_BRIDGE_2026-09-06.md)).

## Die tatsächliche kompakte Sandwich-Darstellung

Sei \(j_X:\mathcal H_X\to L^2(\mathbb R)\) die feste kompakte
Gamma-Graphraumeinbettung und setze
\[
K_{X,U}:=\widehat H(U)^*j_X.
\]
Dieser Operator ist kompakt, weil \(U\) fest und der tatsächliche
Hub an diesem Horizont beschränkt ist
([LOCAL-O1, §§4–5](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md)).

Die exakte Conditioning-Definition liefert
\[
\boxed{
G_{X,\mathrm{cond}}^{U,V}
=\Gamma_X+K_{X,U}^*\widehat B(V)K_{X,U}.
}
\tag{CF2}
\]
Tatsächlich ist \(K_{X,U}\) im alten Fenster getragen. Für
\(V>U\) stimmt die Wirkung der Umgebungsraumresolvente
\(\widehat B(V)=E_VB_VP_V+(I-M_V)\) auf diese Vektoren genau
mit der benötigten komprimierten Resolvente überein;
der äußere Identitätssummand trägt dort nicht bei. Alle
Adjunktionen von \(K_{X,U}\) sind Graphraum-Adjunktionen
([BR1–BR4](https://github.com/Waschtl904/objekt-x-programm/blob/2a43813480629c56200d2910963294fa0c4137fd/audits/P11_R43_COND_DIRECT_FLAGDYN_REVERSE_NORMAL_BRIDGE_2026-09-06.md),
[LOCAL-O1, LI5 und LI9](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md)).

## Elementares Lemma mit uniformem Fehler

Für einen festen kompakten Operator \(K:\mathcal H\to\mathcal Z\)
ist die Menge
\[
\{K^*TK: T\in\mathcal B(\mathcal Z),\ 0\preceq T\preceq I\}
\]
relativ kompakt in Operatornorm.

Beweis: Wähle endlichrangige orthogonale Projektionen \(F_n\to I\)
stark auf \(\mathcal H\). Dann gilt
\(\|K(I-F_n)\|\to0\), beispielsweise durch Anwendung des
Kompakttransfer-Lemmas auf \(K^*\) und anschließende Adjunktion.
Die Zerlegung
\[
K^*TK-F_nK^*TKF_n
=(K-KF_n)^*TK+(KF_n)^*T(K-KF_n)
\]
gibt die explizite uniforme Schranke
\[
\boxed{
\sup_{0\preceq T\preceq I}
\|K^*TK-F_nK^*TKF_n\|
\le2\|K\|\,\|K(I-F_n)\|\longrightarrow0.
}
\tag{CF3}
\]
Die approximierenden Operatoren wirken auf dem festen
endlichdimensionalen Raum \(F_n\mathcal H\) und sind gleichmäßig
beschränkt. Endliche Netze in diesen Matrixräumen und CF3
beweisen die Behauptung.

Es wird weder eine Konvergenz noch Kompaktheit der mittleren
Familie \(\widehat B(V)\) verlangt. Ihre Positivität und
Kontraktionseigenschaft reichen aus; auch keine gemeinsame
Eigenbasis wird vorausgesetzt.

## Anwendung auf sämtliche \(V>U\)

Für CF2 ergibt sich aus CF3
\[
\sup_{V>U}
\left\|
G_{X,\mathrm{cond}}^{U,V}
-\left(\Gamma_X+
F_nK_{X,U}^*\widehat B(V)K_{X,U}F_n\right)
\right\|
\le2\|K_{X,U}\|\,\|K_{X,U}(I-F_n)\|.
\tag{CF4}
\]
Die rechte Seite geht bei festem \(U\) gegen null. Die
\(\Gamma_X\)-Komponente bleibt dabei unverändert und muss
nicht selbst kompakt sein.

Zudem gelten für alle Zukunftshorizonte
\[
c_XI\preceq G_{X,\mathrm{cond}}^{U,V}
\preceq(1+\|K_{X,U}\|^2)I,
\qquad
c_X=(1+\|H_X^{\mathrm{hub}}\|^2)^{-1}>0.
\tag{CF5}
\]
Die Untergrenze folgt aus der Gamma-Form, die obere aus
\(\Gamma_X\preceq I\) und \(0\preceq\widehat B(V)\preceq I\).
Auch die approximierenden Metriken in CF4 bleiben
\(\succeq c_XI\)
([Gamma-Graphnorm und Spektralschranken](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md)).

Die relativen Metriken bezüglich \(G_{X,U}\), ihre positiven
Wurzeln, inversen Wurzeln und die tatsächlichen unitären
Polarfaktoren haben deshalb ebenfalls relativ normkompakte
Familien. Dies folgt aus normstetiger Funktionalrechnung auf
den Spektralintervallen CF5; es wird keine Stetigkeit des
Parameters \(V\) benötigt
([nichtkommutative Wurzelkontrolle, LOCAL-O1 LI12–LI15](https://github.com/Waschtl904/objekt-x-programm/blob/775158ee656d03bc3601857e8cb0e47fa791caf1/audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md)).

Jede Differenz \(G_{X,\mathrm{cond}}^{U,V}-G_{X,U}\) ist kompakt,
denn die beiden Schurteile haben denselben festen kompakten
Außenfaktor \(K_{X,U}\). Damit sind auch die entsprechenden
Gauge- und Polardifferenzen gegen die Identität kompakt.

Die echte Source-Pullback-Identität BR3 gibt
\[
W_{\mathrm{cond}}(U,V)
=(G_{S,\mathrm{cond}}^{U,V})^{1/2}
J_{R,S}(G_{R,\mathrm{cond}}^{U,V})^{-1/2},
\qquad W_{\mathrm{cond}}^*W_{\mathrm{cond}}=I.
\]
Mit \(Y_{\mathrm{cond}}=\mathcal U_S W_U\mathcal U_R^*\)
lauten die beiden vollständigen Conditioning-O1-Defekte exakt
\[
\mathcal T_{\mathrm{mod}}^{\mathrm{cond}}
=W_{\mathrm{cond}}-Y_{\mathrm{cond}},
\qquad
\mathcal T_{\mathrm{ph}}^{\mathrm{cond}}
=Y_{\mathrm{cond}}-W_U.
\tag{CF6}
\]
Die O1-Algebra gilt hier aufgrund der tatsächlich vorhandenen
Pullback-Kompatibilität, nicht aufgrund einer additiven
Zerlegung der vollen Terminalwurzel
([BR3–BR7](https://github.com/Waschtl904/objekt-x-programm/blob/2a43813480629c56200d2910963294fa0c4137fd/audits/P11_R43_COND_DIRECT_FLAGDYN_REVERSE_NORMAL_BRIDGE_2026-09-06.md),
[O1-Defektidentitäten](https://github.com/Waschtl904/objekt-x-programm/blob/2a43813480629c56200d2910963294fa0c4137fd/audits/P11_R43_FLAGDYN_O1_MODULUS_PHASE_REDUCTION_2026-09-04.md)).

Somit sind beide Defekte kompakte Operatoren von Norm
höchstens zwei. Ihre Familien sind relativ kompakt in
Operatornorm, als stetige Bilder der gemeinsamen kompakten
Abschlüsse der beiden Metrikfamilien. Da \(P_m\to0\) stark
für die tatsächliche kanonische Flagge gilt, macht ein
endliches Operatornormnetz den Grenzwert \(\|P_mK\|\to0\)
gleichmäßig über die ganze Defektfamilie. Dies beweist CF1.

## Präziser Nutzen und verbleibender Rest

Für jeden festen alten Horizont \(U_k\) folgt insbesondere
die projizierte Uniformität BR42 des Conditioning-Modulus,
sogar mit \(\sup_{V>U_k}\) statt nur dem beschränkten
Intervallsupremum. Für die bereits vorhandene
Conditioning-Modulus-Summationsbrücke bleibt deshalb als
quantitative Voraussetzung BR39 beziehungsweise eine
geeignete summierbare Quadratwurzelmajorante übrig
([PR66, BR39–BR43](https://github.com/Waschtl904/objekt-x-programm/blob/2a43813480629c56200d2910963294fa0c4137fd/audits/P11_R43_COND_DIRECT_FLAGDYN_REVERSE_NORMAL_BRIDGE_2026-09-06.md)).

Diese Aussage macht weder den vollständigen Terminalorbit
noch die volle Modulus-/Polarphasenbewegung global tight.
Der Faktor \(K_{X,U}\), die obere Schranke in CF5 und die
benötigten endlichen Netze dürfen sich mit \(U\) verschlechtern.
Ein von \(U\) abhängiger Projektionsindex ist kein Beweis
der ursprünglichen globalen Flag-Tightness.

Insbesondere werden GEO und NEW nicht in CF2 versteckt;
der fixierte alte Hub ist der entscheidende Grund für die
all-future-Uniformität. Für den vollen wachsenden Hub ist
genau diese feste-Faktor-Eigenschaft nicht vorhanden.
Registry, GC-AC-Status, Strong Terminal und RH erhalten
aus diesem Satz keine unbedingte neue Buchung.
