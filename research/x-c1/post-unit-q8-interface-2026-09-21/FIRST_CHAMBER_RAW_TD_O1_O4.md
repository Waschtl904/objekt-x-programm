Exakter roher T/D-Transport in der ersten geschlossenen Horizontkammer

Stand: 2026-09-22. Zusammen mit dem [O5–O7-Nachtrag](Erste-Kammer-O5-O7-Nachtrag-2026-09-22.md): **FIRST-CHAMBER RAW T/D COCYCLE, O1–O7 — AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN** für die ausdrücklich definierte C1a-Fortführung. Dies beschreibt den lokalen Arbeitsbeweis, keine Änderung der kanonischen Registry.

## Ergebnis und Geltungsbereich

Die explizite, unten festgelegte Fortführung der vorhandenen C1a-Multiplikatoren erfüllt für

\[
1\le A\le B\le C\le A_8:=\frac12\log 8
\]

exakte Rohgleichheiten unter physischer Nullfortsetzung. Daraus entstehen zwei getrennte Familien kanonischer isometrischer Inklusionen zwischen den abgeschlossenen T- bzw. D-Bildräumen, jeweils mit Identitäts- und Cocycle-Gesetz. Die Transportabschätzungen haben konstant den Wert 1 auf der gesamten geschlossenen Kammer.

Die vorhandene Vorbereitung formuliert für neue Horizonte bisher ein Interface. Der folgende Satz legt deshalb die konkrete Operatorfamilie ausdrücklich fest. Er betrifft diese Fortführung der C1a-Formeln, nicht jede denkbare Terminalrealisierung.

Dieses Basisdokument liefert O1–O4. Der verlinkte Nachtrag beweist zusätzlich die uniformen Defektoperatoren, ihr R-Intertwining und die Formnaturality auf den vollständigen Quellen; damit erfüllt das gemeinsame Paket O1–O7 innerhalb der ersten geschlossenen Kammer. Ein gemeinsames V, signierte Operatorkongruenz, neue terminale Positivität, positive korrigierte Transporte und ein Wall-Crossing werden nicht behauptet.

## 1. Eingaben und konkrete Definitionen

Commitgebundene Eingaben:

- [C1a, Abschnitte 1–2: physische Quellen, Gamma-Symbol und gekoppelte Multiplikatoren](https://github.com/Waschtl904/objekt-x-programm/blob/5557d94d048dc05e7c3b4534a5a2d1711bdc71dc/research/x-c1/c1-coupled-spectral-mediator-2026-09-20/PROOF.md). Kanonischer C1a-Resultatcommit: `5557d94d048dc05e7c3b4534a5a2d1711bdc71dc`. Die dortigen Sätze bleiben auf ihren ursprünglichen Horizont beschränkt; verwendet werden hier ihre ausdrücklich angegebenen Formeln und der unten gebundene skalare Ledger.
- [C0: physische Nullfortsetzung und Definition der verschobenen Formvervollständigung](https://github.com/Waschtl904/objekt-x-programm/blob/cad1ca1ea8d6303873c92ce83ee8634ac1971007/research/x-c1/x-interface-directed-system-2026-09-19/PROOF.md).
- [Vorbereitendes Horizont-Interface, insbesondere O1–O4](https://github.com/Waschtl904/objekt-x-programm/blob/32594e6c697baeed3d144e90cdeaa06018e9ce2b/research/x-c1/post-unit-q8-interface-2026-09-21/PROOF_OBLIGATIONS.md).

Es gelten physische Koordinaten auf der ganzen reellen Achse und die feste unitäre Fouriertransformation

\[
\widehat f(\xi)=(2\pi)^{-1/2}\int_{\mathbb R}e^{-ix\xi}f(x)\,dx.
\]

Für jeden Horizont A definieren wir

\[
W_A=\{u\in H^1_0((-A,A)):E^A_+u=E^A_-u=0\},\qquad
E^A_\pm u=\int_{-A}^{A}u(x)e^{\pm x/2}\,dx.
\]

Z_A bezeichnet die Nullfortsetzung nach R, J_{A,B} die Nullfortsetzung von (-A,A) nach (-B,B). Die H1-Norm enthält die L2-Norm und die L2-Norm der schwachen Ableitung. Es findet keine zusätzliche Skalierung des Quell- oder Frequenzarguments statt.

Die Terminalformeln werden ausschließlich durch die aktive Menge parametrisiert:

\[
\mathcal Q_A=\{p^k:k\ge1,\ \log(p^k)<2A\},\quad
\ell_q=\log q,\quad w_q=\frac{\Lambda(q)}{\sqrt q},
\]
\[
\kappa=\log(8\pi)+\gamma+\pi/2,\qquad
g(\xi)=\sum_{j=0}^{\infty}\frac{2\xi^2}{\lambda_j(\lambda_j^2+\xi^2)},
\quad\lambda_j=2j+\tfrac12,
\]
\[
\omega_A=\sum_{q\in\mathcal Q_A}w_q,\qquad
c_A(\xi)=\sum_{q\in\mathcal Q_A}w_q\cos(\ell_q\xi),\qquad
s_A=\kappa+2\omega_A,
\]
\[
h_A=g+s_A,\qquad m_A=g+\omega_A-c_A,\qquad n_A=\kappa+\omega_A+c_A.
\]

Die Bezeichnung h_A ersetzt hier die spektrale Bezeichnung A=g+s aus C1a, damit sie nicht mit dem Terminalhorizont verwechselt wird. In zwei getrennt bezeichneten, festen Kopien K_T und K_D von L2(R,dξ) setzen wir

\[
\widetilde T_Au=\frac{m_A}{\sqrt{h_A}}\widehat{Z_Au}\in K_T,
\qquad
\widetilde D_Au=\frac{n_A}{\sqrt{h_A}}\widehat{Z_Au}\in K_D.
\tag{1}
\]

Die Quadratwurzel in (1) gehört zur explizit positiven Hüllfunktion h_A, nicht zu I-R_A*R_A. Sie setzt keine Positivität der gewünschten Weil-Form voraus.

## 2. Quellräume, Momente und Randverhalten

Die Funktionale E^A_± sind auf L2((-A,A)) stetig:

\[
|E^A_\pm u|\le(2\sinh A)^{1/2}\|u\|_2.
\]

Daher ist W_A ein abgeschlossener Unterraum von H1_0((-A,A)). Für u in H1_0 wähle u_n in C∞_c((-A,A)) mit u_n→u in H1. Ihre Nullfortsetzungen liegen in C∞_c((-B,B)) bzw. H1(R), und die H1-Norm wird dabei exakt erhalten. Durch Grenzübergang folgt

\[
J_{A,B}u\in H^1_0((-B,B)),\quad Z_Au\in H^1(\mathbb R),\quad
(Z_Au)'=Z_A(u'),\quad \|J_{A,B}u\|_{H^1} =\|u\|_{H^1}.
\tag{2}
\]

Dies zeigt insbesondere, dass an ±A keine Dirac-Randterme entstehen. Äquivalent: Die inneren und äußeren Spuren passen wegen der Nullspur von u zusammen. Für A<B ist die Erweiterung nahe ±B identisch null; A=B ist der Identitätsfall.

Die Momentbedingungen bleiben wörtlich erhalten:

\[
E^B_\pm(J_{A,B}u)=E^A_\pm u=0.
\tag{3}
\]

Somit ist J_{A,B}:W_A→W_B eine isometrische Einbettung für die H1-Norm. Außerdem gelten schon als physische Funktionen

\[
Z_BJ_{A,B}=Z_A,\qquad J_{A,A}=I,\qquad
J_{B,C}J_{A,B}=J_{A,C}.
\tag{4}
\]

Die approximierenden u_n in diesem Argument müssen nicht selbst die beiden Momente annullieren: (2) wird für H1_0 bewiesen, (3) anschließend direkt für u. Es wird kein unbewiesener momentenerhaltender Dichtesatz vorausgesetzt.

## 3. Konstante Multiplikatoren einschließlich A_8

Aus 7<e²<8 folgt für 1≤A≤A_8

\[
7<e^{2A}\le8.
\]

Die Primzahlenpotenzen im Bereich [2,8) sind genau 2,3,4,5,7. Wegen der strikten Aktivierungsbedingung ist daher auf der gesamten geschlossenen Kammer

\[
\mathcal Q_A=\mathcal Q_*=\{2,3,4,5,7\}.
\tag{5}
\]

Insbesondere erfüllt q=8 bei A=A_8 nur log 8=2A_8 und ist nicht aktiv. Als ergänzende Randprüfung: Eine Translation um 2A_8 überlappt mit [-A_8,A_8] höchstens in einem einzelnen Punkt; ihr Korrelationsintegral verschwindet. Das ist kein Wall-Crossing rechts des Endpunkts.

Die verwendete elementare Schranke benötigt keinen Dezimaltest. Für den Rest der Exponentialreihe gilt

\[
\sum_{n=4}^{\infty}\frac1{n!}
\le\frac1{4!}\sum_{k=0}^{\infty}5^{-k}
=\frac5{96},
\]

weil (4+k)!≥4!·5^k. Daher e>1+1+1/2+1/6=8/3 und e≤8/3+5/96=87/32<11/4, also e²>7 und e²<8.

In den Definitionen (1) ist g eine feste volle Gamma-Reihe. Auch κ, die Fourierkonvention, die Gewichte w_q und die Verschiebungen ℓ_q sind fest. Mit (5) folgt unmittelbar

\[
\omega_A=\omega_*,\ c_A=c_*,\ s_A=s_*,\ h_A=h_*,\ m_A=m_*,\ n_A=n_*.
\tag{6}
\]

Dies prüft die gesamte in (1) zugelassene Terminalabhängigkeit. Eine zusätzliche A-abhängige Normierung, Frequenzskalierung, Profilprojektion oder andere Hüllfunktion wäre eine andere Konstruktion und fällt nicht unter diesen Satz.

Der reine skalare Ledger ist ausdrücklich an [C1a, Gleichung (5), Commit `5557d94`](https://github.com/Waschtl904/objekt-x-programm/blob/5557d94d048dc05e7c3b4534a5a2d1711bdc71dc/research/x-c1/c1-coupled-spectral-mediator-2026-09-20/PROOF.md#L108) gebunden:

\[
10<s_*<\frac{23}{2}<12.
\]

Diese Eingabe bleibt wegen der unveränderten Familie Q_* dieselbe; sie ist keine Übertragung eines Positivitätssatzes auf größere Quellen.

## 4. Wohldefiniertheit auf W_A und exakte Rohgleichheiten

Die Gamma-Reihe konvergiert lokal gleichmäßig auf der reellen Frequenzachse: Für |ξ|≤M ist jeder Summand durch 2M²/λ_j³ majorisiert, und die Reihe dieser Majoranten konvergiert. Der Weierstraßsche Majorantentest liefert daher auf jedem kompakten Frequenzintervall gleichmäßige Konvergenz. Insbesondere ist g endlich, stetig, gerade und nichtnegativ. Außerdem gilt

\[
0\le g(\xi)\le\frac{131}{8}\xi^2.
\]

Für die Abschätzung genügt bei j=0 der Koeffizient 16 und für j≥1 die Schranke 1/(4j³), deren Summe höchstens 3/8 ist. Aus |c_*|≤ω_* und κ>0 ergeben sich

\[
h_*>0,\qquad 0\le m_*\le h_*,\qquad \kappa\le n_*\le s_*.
\]

Damit gilt

\[
\frac{m_*^2}{h_*}\le g+s_*,\qquad
\frac{n_*^2}{h_*}\le s_*.
\]

Plancherel und (2) liefern

\[
\|\widetilde T_Au\|^2\le\frac{131}{8}\|u'\|_2^2+s_*\|u\|_2^2,
\qquad
\|\widetilde D_Au\|^2\le s_*\|u\|_2^2.
\tag{7}
\]

Beide Rohoperatoren sind also auf den deklarierten Quellen definiert und H1-stetig. Es wird kein nur für Träger in [-1,1] bewiesener unterer T-Bound auf größere Quellen übertragen.

Aus Z_BJ_{A,B}u=Z_Au folgt Gleichheit ihrer Fouriertransformierten. Zusammen mit (6) ergibt dies in den jeweils gemeinsamen Umgebungsräumen

\[
\boxed{\widetilde T_BJ_{A,B}u=\widetilde T_Au\quad\text{in }K_T,}
\qquad
\boxed{\widetilde D_BJ_{A,B}u=\widetilde D_Au\quad\text{in }K_D.}
\tag{8}
\]

Insbesondere sind beide Normen exakt erhalten. Der Schluss verwendet die Operatorformeln und die Gleichheit physischer Quellen, nicht lediglich Gleichheit von Quadratikformen.

## 5. Quotientenabstieg und abgeschlossene Bildräume

Definiere mit den geerbten L2-Normen

\[
\mathcal H_A^T=\overline{\widetilde T_A(W_A)}^{K_T},\qquad
\mathcal H_A^D=\overline{\widetilde D_A(W_A)}^{K_D}.
\tag{9}
\]

T_A und D_A bezeichnen nun die entsprechenden Abbildungen mit den eingeschränkten Zielräumen H_A^T und H_A^D. Diese beiden Zielraumfamilien werden nicht miteinander identifiziert.

Wenn T_Au=T_Av, liefert (8)

\[
T_BJ_{A,B}(u-v)=0.
\]

Also ist T_Au↦T_BJ_{A,B}u unabhängig vom Repräsentanten. Dieselbe Rechnung gilt unabhängig für D. Beide Abbildungen auf den Rohbildern erhalten die Norm exakt; ihre Schranken sind C^T_{A,B}=C^D_{A,B}=1. Eine Injektivitätsannahme ist für diesen Quotientenabstieg nicht nötig.

Aus (8) und J_{A,B}W_A⊂W_B folgt außerdem

\[
\widetilde T_A(W_A)\subset\widetilde T_B(W_B),\qquad
\widetilde D_A(W_A)\subset\widetilde D_B(W_B).
\]

Nach Abschluss in den jeweils gemeinsamen L2-Räumen erhält man H_A^T⊂H_B^T und H_A^D⊂H_B^D. Daher sind die eindeutigen stetigen Erweiterungen der Rohabbildungen genau die wörtlichen Inklusionen

\[
M^T_{A,B}:\mathcal H_A^T\hookrightarrow\mathcal H_B^T,
\qquad
M^D_{A,B}:\mathcal H_A^D\hookrightarrow\mathcal H_B^D.
\tag{10}
\]

Sie sind isometrisch. Ihre Bilder sind abgeschlossene Unterräume, weil H_A^T bzw. H_A^D schon im gemeinsamen Umgebungsraum abgeschlossen sind. Es wird nicht behauptet oder benötigt, dass die Rohbilder T_A(W_A) oder D_A(W_A) selbst abgeschlossen sind.

Die mit den Zielräumen typkorrekten Transportgleichungen lauten

\[
\boxed{M^T_{A,B}T_A=T_BJ_{A,B},\qquad
M^D_{A,B}D_A=D_BJ_{A,B}.}
\tag{11}
\]

Die Gleichheiten ohne M in (8) beziehen sich ausdrücklich auf die Umgebungsräume. Soll T_A bereits die eingeschränkten Zielräume tragen, müssen die entsprechenden Einbettungen in K_T bzw. K_D mitgeschrieben werden.

## 6. Cocycle zuerst auf Rohbildern, dann auf Abschlüssen

Für u∈W_A und 1≤A≤B≤C≤A_8 gilt

\[
\begin{aligned}
M^T_{B,C}M^T_{A,B}T_Au
&=M^T_{B,C}T_BJ_{A,B}u\\
&=T_CJ_{B,C}J_{A,B}u\\
&=T_CJ_{A,C}u\\
&=M^T_{A,C}T_Au.
\end{aligned}
\]

T_A(W_A) ist per Definition dicht in H_A^T. Beide Seiten sind beschränkte Operatoren von H_A^T nach H_C^T, also gilt auf dem gesamten abgeschlossenen Raum

\[
\boxed{M^T_{B,C}M^T_{A,B}=M^T_{A,C}.}
\]

Genau dieselbe Rechnung wird gesondert mit D ausgeführt. Somit

\[
\boxed{M^D_{B,C}M^D_{A,B}=M^D_{A,C},\qquad
M^T_{A,A}=I_{\mathcal H_A^T},\quad
M^D_{A,A}=I_{\mathcal H_A^D}.}
\tag{12}
\]

Dies schließt die vier hier geprüften Schritte für die ausdrücklich konstruierte Rohfamilie auf der gesamten ersten geschlossenen Kammer, einschließlich beider Endpunkte. Es ist eine einzige Formel für alle Paare und Tripel, keine Kette kleiner Fortsetzungsschritte.

## 7. Quellenvervollständigung: explizite Fortsetzung des C0-Modells

Der bisherige Beweis benötigt nur W_A mit H1-Norm und die abgeschlossenen Ausgabebilder. Um zusätzlich die im Interface verwendete verschobene Formvervollständigung zu typisieren, kann dieselbe Konstruktion wie folgt auf diese Quellen erweitert werden.

Setze für die konkrete Kammerform

\[
w_*(\xi)=g(\xi)-\kappa-2c_*(\xi),\qquad
q_A(u,v)=\int w_*\overline{\widehat{Z_Au}}\widehat{Z_Av}\,d\xi,
\]
\[
b_*=w_*+17,\qquad
\|u\|_{A,17}^2=q_A[u]+17\|u\|_2^2.
\]

Diese q_A ist die Fortführung der konkreten vollen Gamma-/endlichen Prime-Form aus C1a in der Kammer. Es wird kein zusätzlicher globaler Weil-Testklassen-Satz benutzt. Der in Abschnitt 3 commitgebundene C1a-Ledger (5) gibt 10<s_*<23/2<12; er ist wegen (6) unverändert. Daher

\[
b_*\ge g+17-s_*>g+5>0.
\tag{13}
\]

Realisieren wir F_A als Abschluss von Z_A(W_A) im gemeinsamen Hilbertraum

\[
\mathscr F_* = \{f\in L^2(\mathbb R):\int b_*|\widehat f|^2<\infty\},
\]

so ist dies genau die deklarierte Vervollständigung in der Norm q_A+17||·||². Der Umgebungsraum ist vollständig, weil die Fouriertransformation ihn isometrisch mit L2(R,b_*dξ) identifiziert und b_*≥5 die inverse Fouriertransformation nach L2 erlaubt. Diese Definition setzt keine Positivität von q_A voraus. Aus (13) folgt stetige Einbettung in L2. Deshalb behalten Grenzquellen Träger in [-A,A] und beide Momente null. H1-Regularität oder klassische Randspuren werden für sämtliche Elemente von F_A nicht behauptet.

Da alle F_A in demselben gewichteten Fourier-Raum abgeschlossen werden und Z_BJ_{A,B}=Z_A gilt, setzt sich J_{A,B} eindeutig als isometrische Inklusion F_A↪F_B fort und behält sein Cocycle-Gesetz.

Schreibe t=m_*/sqrt(h_*) und d=n_*/sqrt(h_*). Die algebraische Identität m_*+n_*=h_* ergibt t²-d²=w_*, also

\[
b_*=t^2+(17-d^2),\quad d^2\le s_*<12,\quad
t^2\le b_*,\quad d^2\le \frac{s_*}{17-s_*}\,b_*.
\tag{14}
\]

Damit sind T_A und D_A auch für die F_A-Norm beschränkt und besitzen eindeutige Fortsetzungen F_A→H_A^T bzw. F_A→H_A^D. Ihre Bildabschlüsse bleiben (9): W_A ist dicht in F_A, und die stetigen Fortsetzungen nehmen ihre Werte in den entsprechenden abgeschlossenen Rohbildräumen an. (8), (11) und (12) gelten dort durch Dichte weiterhin.

Die hier verwendete Differenz der skalaren Gramsymbole ist keine signierte Operatorkongruenz zwischen Terminalräumen. Für O1–O4 werden weder ein Defektoperator R noch die Surjektivität oder ein beschränkter inverser T_A-Operator benötigt. Der Nachtrag konstruiert R mit einem neu bewiesenen Kammer-Floor und zeigt zusätzlich, dass T_A:F_A→H_A^T für diese Quellenvervollständigung ein beschränkter Isomorphismus ist. Ein gemeinsamer Transport V wird nicht behauptet.

## 8. Gemeinsamer Ergebnisscope und offene Folgeaufgaben

Dieses Dokument und der [O5–O7-Nachtrag](Erste-Kammer-O5-O7-Nachtrag-2026-09-22.md) liefern gemeinsam das rohe erste Kammerpaket O1–O7 für die hier ausdrücklich deklarierte C1a-Fortführung auf 1≤A≤B≤C≤A_8. Dazu gehören jetzt R-Intertwining auf den richtigen abgeschlossenen Trägern und Formnaturality auf F_A. Der lokale mathematische Status ist **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**. Ein vollständiges unbeschränktes TERMINAL-HORIZON-C1-COCYCLE wird damit nicht geschlossen; die weitergehenden Anforderungen beim Eintritt neuer Kanäle bleiben getrennt.

Unbehandelt bleiben ein gemeinsames V, signierte Operatorkongruenz, neue terminale Positivität, korrigierte positive Transporte, Wall-Crossing rechts von A_8, wachsende Profile und kofinale/global fensterunabhängige Readouts. Die Schranke ||R_A||≤sqrt(90) beweist keine Kontraktion. Auch P11-Fixed-Pair bleibt eine getrennte Aussage.

Die konkrete Operatorwahl (1) und die neue explizite C0-Fortsetzung aus Abschnitt 7 gehören zum Scope dieses Ergebnisses. Jede zusätzliche terminalabhängige Änderung dieser Wahl erfordert eine neue Prüfung von (6)–(8). Der nächste offene Positivitätsschritt ist O8; eine gesonderte Vorbereitung der q=8-Wall-Architektur nimmt ihn nicht vorweg.