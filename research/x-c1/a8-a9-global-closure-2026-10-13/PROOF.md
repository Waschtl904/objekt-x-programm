# Bedingter konstruktiver Positivitätsübergang A8→A9

13. Oktober 2026 · **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**

## Aussage und gebundene Quellen

Für den festen Übergang von a=3 log(2)/2 zu b=log(3) ist der gesamte neue
Formraum in beiden Paritäten positiv, **unter den Voraussetzungen (A)–(D)**
unten. Der Beweis verwendet keine vorausgesetzte neue A9-Terminalpositivität.

Die Schlussrechnung ist gebunden an:

- `Objekt-X-Globaler-Schurabschluss-A8-A9-2026-10-13.zip`, SHA-256
  `65085974657257bd447d93342c5001d29e797b2fa70d876d53d36b587b16c2ba`;
- `Objekt-X-Schurabschluss-Gegenpruefung-und-Reserve-2026-10-13.zip`, SHA-256
  `6b29274d3eadf5ca0c97c65176bc20dfb9cfff42f9b36739028674edb14469d8`.

Die vollständigen ursprünglichen Herleitungen bleiben bytegleich lesbar:
[Schurabschluss](packages/objekt-x-globaler-schurabschluss-a8-a9-2026-10-13/HERLEITUNG.txt)
und [Reserve-Gegenprüfung](packages/objekt-x-schurabschluss-gegenpruefung-und-reserve-2026-10-13/PRUEFHERLEITUNG.txt).
Alle Vorgänger und ihre enthaltenen Matrixdaten sind durch
[SOURCE_BINDINGS.json](SOURCE_BINDINGS.json) gebunden und rekonstruierbar.

## Voraussetzungen

(A) Der alte A8-Block ist positiv und invertierbar. Die konsistent neu
aufgebaute Majorante U_neu kontrolliert seine vollständige Inversenergie
gemeinsam auf allen neuen Quellen, einschließlich sämtlicher Kreuzblöcke.

(B) Nach Abspaltung des alten Raums parametrisieren die zwölf physischen
Funktionen F=(z₁,…,z₄,ΛY₁,…,ΛY₈) und ΛT den gesamten neuen Formraum.
T, Liftung Λ, Momentkorrektur und W_X sind die exakten gebundenen Räume und
Abbildungen. Vollständigkeit und Domänenverträglichkeit dieser Zerlegung
werden übernommen; sie folgen nicht aus einem endlichen Rangtest.

(C) Auf T gilt q[r]=q_b[Λr] und q≥L≥(21/5)W_X. Für η=10⁻¹⁰ und den neuen
vollständigen alten Hochanteil gilt als geschlossene Form

\[
S=(1-\eta)q-H_{\rm neu}\succeq\beta L,
\qquad \beta=\frac{20209999981781}{182190000000000}>0.
\]

Die Formdomäne von S liegt in derjenigen von L; die betreffenden
Funktionale sind formstetig. R_L bezeichnet den Inversen der L-Form auf dem
exakten T, einschließlich der bezahlten Moment-/Geometriekorrektur.

(D) Die positive rationale Zwölfermetrik K=K12_neu erfüllt
K_actual=(D_direct−U_neu)[F,F]≥K. Die 203 Kräfte A bestehen aus 191 neuen
niedrigen Features und zwölf tatsächlichen physischen Kreuzzeilen.
D=diag((1−ρ)I₁₉₁,K) ist ihre feste positive Metrik. Alle Quellenfehler,
Formfehler und Matrixintervalle sind dieselben gebundenen Größen wie im
Antwort-, Außenrest-, Log- und Grampaket.

Diese Voraussetzungen und ihre analytischen Begründungen bleiben Teil der
extern zu prüfenden Kette. Rationale Nachrechnung ist kein maschineller Beweis
sämtlicher ursprünglicher Operator- und Domänenaussagen.

## Vollständiger Rest und gemeinsames Budget

Mit den festen rationalen Antworten Z_app=J84 X setzt man

\[
R=A^*-SZ_{\rm app},\qquad
M=AZ_{\rm app}+Z_{\rm app}^*A^*-Z_{\rm app}^*SZ_{\rm app}
\preceq M_{\rm upper}\prec uD.
\]

Es gelten u_even=999997138063/10¹² und u_odd=999982753528/10¹².
Das feste positive Budget ist T_b=β(D−M_upper)≥σD, σ=β(1−u).

Im Schalenraum X=L²((a,b),2dx) sei P=P_<104 die vollständige orthogonale
Projektion, g=R_X−B C_exact der um alle drei Logarithmusterme regularisierte
Rest und U_g=g*(I−P)g. Die gerichtete globale Integralrechnung mit vollständigem
Projektionsabzug und Modellfehler liefert U_g<q₀H, q₀=3/10000, H=E_dir/10920.
Dies ist eine obere Schranke für sämtliche Grade ab 104, kein endlicher
Abbruch hoher Legendrekoeffizienten.

Setze d=HarmonicNumber(104)+11/10, e=j+10⁻³⁰⁰ und Q=Qlog_bar.
Die gebundenen Matrizen erfüllen exakt

\[
H=\frac{d\theta}{1+\theta}
  \bigl[(1-c_8)T_b-eD-(1+\theta)Q\bigr],
\qquad Q\preceq c_{\log}T_b.
\]

Hier sind (θ,c₈,c_log)=(21,1/5000,1/500) gerade und
(15,13/20000,1/250) ungerade. j bezahlt den tatsächlichen Basis84-Anteil;
10⁻³⁰⁰ bezahlt die vollständige geometrische Momentkorrektur; c₈T_b bezahlt
alle acht Außenzeilen von Grad 96 bis 103. Die genaue Restgeometrie und die
Umrechnung auf die rohen Legendrezeilen bleiben enthalten.

Die Monotonie der Gewichte gibt Q_g≤U_g/d. Mit s=3/8 gerade und s=4/15
ungerade bezahlt Young alle Log/Rest-Kreuzterme. Somit gilt auf dem ganzen Rest

\[
R^*R_LR\preceq Q_{\rm final}
=eD+c_8T_b+(1+s)Q+(1+1/s)q_0H/d.
\]

Setzt man die vollständige Zielmatrix H ein und schreibt
f=(1+1/s)q₀θ/(1+θ), folgt die exakte Identität

\[
Q_{\rm final}=(1-f)eD+[c_8+f(1-c_8)]T_b
                   +[1+s-f(1+\theta)]Q.
\]

Alle drei Koeffizienten sind positiv. Daher darf D≤T_b/σ und Q≤c_log T_b
eingesetzt werden. Ohne Vertauschung von Matrizen folgt rational

\[
Q_{\rm final}\prec cT_b,\qquad
c_{\rm even}=1977/500000,\quad c_{\rm odd}=6967/1000000.
\]

Das sind 0,3954 % bzw. 0,6967 % des **gesamten** Formdualbudgets auf allen
203 Kräften. Die frühere Angabe 0,030 % bezieht sich nur auf U_g relativ
zu H und wird hier nicht mit dem Gesamtpreis verwechselt.

## Inversenidentität und Übergang zum gesamten Formraum

Die exakte Identität im Formdualraum lautet

\[
AS^{-1}A^*=M+R^*S^{-1}R
\preceq M_{\rm upper}+\beta^{-1}R^*R_LR.
\]

Der inverse Vergleich folgt auch variational aus S≥βL und der
Formdomäneninklusion. Eine zusätzliche starke Operatordomänenannahme für
jede Antwortspalte wird nicht benötigt. Aus dem vollen Restvergleich folgt

\[
AS^{-1}A^*\preceq M_{\rm upper}+c(D-M_{\rm upper})
\preceq(1-\kappa)D,\qquad \kappa=(1-c)(1-u)>0.
\]

Für den beschränkten Operator C=D⁻¹ᐟ²AS⁻¹ᐟ² liefert CC*≤(1−κ)I über
die Operatornorm auch C*C≤(1−κ)I. Somit gilt A*D⁻¹A≤(1−κ)S auf der
gesamten Formdomäne. Diese Aussage beruht auf dem vollständigen Residualgram,
nicht auf einer bloßen endlichen Galerkinprüfung.

## Zwei Schurergänzungen

Für B=D_direct−U_neu auf F+ΛT gilt K_actual≥K>0, also
K_actual⁻¹≤K⁻¹. Deshalb

\[
\operatorname{Schur}_F(B)
\succeq q-H_{\rm neu}-A^*D^{-1}A
\succeq\eta q+\kappa S
\succeq\frac{21}{5}(\eta+\kappa\beta)W_X.
\]

Die exakte rationale Auswertung bestätigt die konservativen Böden
>1,3285·10⁻⁶ W_X gerade und >7,9795·10⁻⁶ W_X ungerade. Quadratische
Ergänzung mit K_actual zeigt die Positivität von B auf F+ΛT.

Die tatsächliche alte-eliminierte Form dominiert B. Ihre Schurform dominiert
auch nach Eliminierung von F den Vergleich, denn die Ordnung bleibt beim
Infimum über dieselben endlichen Koordinaten erhalten. Mit (A) und der
vollständigen Zerlegung (B) folgt die bedingte Positivität des ganzen A9-Raums.

## Aussagegrenzen

Der gesonderte Tailboden 1/20 ist weder benötigt noch bewiesen noch widerlegt.
Die obigen W_X-Böden betreffen den bezeichneten reduzierten Schurvergleich.
Die unterschiedlichen früheren 203 Abdeckungsfunktionale werden nicht durch
die hier benutzten 203 Kräfte ersetzt. Weitere Horizontübergänge, eine
kofinale kompatible positive Familie, globaler Readout, exakte globale
Weil-Gramidentität, Objekt X und RH bleiben offen.

Die Integration wiederholt die vollständige gebundene rationale Schlusskette
und die zusätzliche exakte Reserveprüfung. Sie erzeugt die großen globalen
Integrationen nicht neu und ersetzt keine unabhängige externe Begutachtung.
