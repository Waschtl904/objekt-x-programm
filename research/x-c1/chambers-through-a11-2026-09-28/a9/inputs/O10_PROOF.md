# O10: gekoppelte rohe Transporte über die q=8-Wand

27. September 2026 · **Lokale Herleitung / EXTERNAL_REVIEW_OPEN**

Repository-Basis: `69eb8773acd483978e2453019d1e2d5cf009a990`.
Dieser Text ergänzt den geprüften O8/O9-Stand um einen analytischen Rohtransportsatz.
Er ändert keinen Repository- oder Registry-Status.

## Ergebnis

Setze `A8=log(8)/2` und `A9=log(9)/2=log(3)`. Für die konkrete C1a-Familie
existieren für **alle** `1 <= A <= B <= C <= A9` zwei getrennte beschränkte
Rohtransportfamilien auf den abgeschlossenen T- und D-Bildräumen. Sie erfüllen
Quotientenabstieg, Quellintertwining, Identität, beide Cocycle-Gesetze,
Defektintertwining und Formnaturality auf den vollständigen Quellenformräumen.

Innerhalb jeder der beiden Kammern sind sie die bisherigen wörtlichen
Inklusionen. Für `A <= A8 < B` werden sie durch die verschiedenen Multiplikatoren

\[
a_T=\frac{m_+}{m_-}\sqrt{\frac{h_-}{h_+}},\qquad
a_D=\frac{n_+}{n_-}\sqrt{\frac{h_-}{h_+}}
\tag{1}
\]

realisiert. Die erste Formel gilt fast überall; ihr Wert bei `xi=0` kann
beliebig innerhalb der folgenden Grenzen festgelegt werden. Es gelten

\[
\sqrt{20/21}\le a_T\le5/4,\qquad
\sqrt{20/21}\le a_D\le11/10.
\tag{2}
\]

Damit sind auch die Wandtransporte nach unten beschränkt und haben
abgeschlossene Bilder. Eine Surjektivität auf den gesamten größeren
Terminalraum wird nicht beansprucht.

Der Satz behandelt O10 im präzisen Rohscope der bisherigen Obligation.
**Eine positive Reserve für den gesamten neuen Terminalraum rechts von A8
ist ein weiterer offener Schritt.** Insbesondere wird dort kein positiver
Operator `Delta_B=G_B^(1/2)` vorausgesetzt.

## 1. Eingaben, Bindungen und Notation

Verwendet werden die expliziten Definitionen und skalaren Schranken aus:

1. [C1a, §§1–2, Commit 5557d94](https://github.com/Waschtl904/objekt-x-programm/blob/5557d94d048dc05e7c3b4534a5a2d1711bdc71dc/research/x-c1/c1-coupled-spectral-mediator-2026-09-20/PROOF.md).
2. [O1–O4, Commit 6623047](https://github.com/Waschtl904/objekt-x-programm/blob/6623047361578b819ae44358fbbbf0b3fdeac9ff/research/x-c1/post-unit-q8-interface-2026-09-21/FIRST_CHAMBER_RAW_TD_O1_O4.md).
3. [O5–O7, Commit 6623047](https://github.com/Waschtl904/objekt-x-programm/blob/6623047361578b819ae44358fbbbf0b3fdeac9ff/research/x-c1/post-unit-q8-interface-2026-09-21/FIRST_CHAMBER_O5_O7_ADDENDUM.md).
4. [O10-Obligation am Arbeitsausgangspunkt](https://github.com/Waschtl904/objekt-x-programm/blob/69eb8773acd483978e2453019d1e2d5cf009a990/research/x-c1/post-unit-q8-interface-2026-09-21/PROOF_OBLIGATIONS.md).

Die SHA-256-Bindungen stehen in `SOURCE_BINDINGS.json`. Historische Aussagen
dieser Eingaben zu damals offenen O8/O9-Schritten gelten für ihren Textstand.
Die neue Argumentation benötigt für den Rohsatz keine O8-Positivität.
Nur die Folgerung über den alten positiven Teilraum in §9 verwendet den
[O8-Beweis am Commit 82a1f9d](https://github.com/Waschtl904/objekt-x-programm/blob/82a1f9d661b1668cc71eb0d5f8806c5cee73e471/research/x-c1/first-chamber-o8-o9-2026-09-27/o8-rechenstand/PROOF.md).

Wir behalten physische Nullfortsetzung, die Fourierkonvention
`fhat(xi)=(2pi)^(-1/2) integral exp(-ix xi)f(x)dx` und Skalarprodukte mit
konjugiert linearem erstem Argument. T- und D-Ausgaben liegen in getrennten
festen Kopien `K_T`, `K_D` von `L²(R,d xi)`.

Die volle Gammafunktion bleibt

\[
g(\xi)=\sum_{j=0}^{\infty}
\frac{2\xi^2}{\lambda_j(\lambda_j^2+\xi^2)},\qquad
\lambda_j=2j+\tfrac12.
\tag{3}
\]

Sie ist endlich, stetig, gerade, nichtnegativ und außerhalb von Null positiv.
Insbesondere liefern ihre positiven Summanden

\[
g(\xi)\ge g_0(\xi):=\frac{4\xi^2}{1/4+\xi^2},\qquad
g(\xi)\le\frac{131}{8}\xi^2.
\tag{4}
\]

Diese beiden allgemeinen Symbolschranken hängen nicht vom Quellenhorizont ab.
Plancherel und die Fortsetzung der Fouriertransformation auf L² werden mit
derselben Normierung wie in den gebundenen Eingaben verwendet; allgemeiner
Hintergrund: [MIT, Fourier transform and L²](https://math.mit.edu/~rbm/18-102-S18/Chapter4.pdf).

## 2. Aktivierung und der gekoppelte neue Mediator

Die Aktivierungsbedingung lautet strikt `log(q)<2A`. Deshalb gelten

\[
Q_- =\{2,3,4,5,7\}\quad(1\le A\le A_8),\qquad
Q_+ =Q_-\cup\{8\}\quad(A_8<A\le A_9).
\tag{5}
\]

Bei `A=A8` ist 8 ausgeschlossen; bei `A=A9` ist 9 ausgeschlossen.
Es tritt in diesem Bereich kein weiterer Primzahlpotenzkanal ein.
Schreibe

\[
v=w_8=\frac{\log2}{\sqrt8},\quad \ell=\log8=3\log2,
\quad z(\xi)=\cos(\ell\xi).
\]

Die gebundenen alten Daten erfüllen `5<kappa<11/2` und `10<s_-<23/2`.
Für eine elementare rationale Zusatzkontrolle gilt `log(2)<7/10`, denn schon
die Summe der Terme bis Grad 3 in der Reihe von `exp(7/10)` ist größer als 2.
Außerdem ist `(14/5)^2<8`. Somit

\[
0<v<1/4,\qquad0<\ell<21/10<3,\qquad
10<s_+=s_-+2v<12.
\tag{6}
\]

Mit den bisherigen Definitionen

\[
\omega_\sigma=\sum_{q\in Q_\sigma}w_q,
\quad c_\sigma=\sum_{q\in Q_\sigma}w_q\cos(\ell_q\xi),
\quad s_\sigma=\kappa+2\omega_\sigma
\]

setzen wir für `sigma=-,+`

\[
h_\sigma=g+s_\sigma,\quad
m_\sigma=g+\omega_\sigma-c_\sigma,\quad
n_\sigma=\kappa+\omega_\sigma+c_\sigma,
\quad t_\sigma=m_\sigma/\sqrt{h_\sigma},\quad
d_\sigma=n_\sigma/\sqrt{h_\sigma}.
\tag{7}
\]

Der Eintritt von 8 ändert **dieselben gemeinsamen** Zähler und den Nenner:

\[
m_+=m_-+v(1-z),\qquad n_+=n_-+v(1+z),\qquad h_+=h_-+2v.
\tag{8}
\]

Die Rohoperatoren sind `T_Au=t_sigma fhat`, `D_Au=d_sigma fhat` für die
physisch nullfortgesetzte Quelle `f`. Insbesondere wird T nicht um einen
orthogonalen Einzelkanalblock erweitert. Beispielsweise enthält sein neuer
Gramzähler

\[
m_+^2=m_-^2+2v m_-(1-z)+v^2(1-z)^2
\]

alle hierdurch erzeugten alten/neuen Gamma-/Prime-Kreuzterme.
Aus `m_sigma+n_sigma=h_sigma` folgt exakt

\[
t_\sigma^2-d_\sigma^2
=w_\sigma:=g-\kappa-2c_\sigma,
\qquad w_+-w_-=-2v\cos(\ell\xi).
\tag{9}
\]

## 3. Vollständige Quellen und Formnaturality über die Wand

Beginne mit den unveränderten Quellen

\[
W_A=H^1_0((-A,A))\cap\ker E_+\cap\ker E_-,\qquad
E_\pm u=\int_{-A}^{A}u(x)e^{\pm x/2}\,dx.
\]

Definiere `F_A` als Abschluss der physisch nullfortgesetzten `W_A` im
gemeinsamen Gamma-Formraum `G` mit Norm
`integral (1+g)|fhat|²`. Versehen wird `F_A` mit der Terminalnorm

\[
\|u\|_{A,17}^2=\int b_A|\widehat u|^2,
\qquad b_A=w_{\sigma(A)}+17.
\tag{10}
\]

Wegen (6) und `|c_sigma|<=omega_sigma` gilt überall

\[
g+5<b_A<g+29,\qquad
1+g\le b_A\le29(1+g).
\tag{11}
\]

Also ist dies genau der Abschluss in `q_A+17||.||²` und ein vollständiger
Hilbertraum. Links der Wand stimmt er mit dem bereits definierten `F_A`
einschließlich seiner Norm überein. Die Grenzquellen haben Träger in `[-A,A]`
und beide Momente null, da diese Bedingungen unter L²-Konvergenz bei festem
Träger erhalten bleiben. Es werden für allgemeine Grenzquellen keine
H¹-Regularität oder klassischen Randspuren verlangt.

Physische Nullfortsetzung gibt zunächst `J_{A,B}W_A subset W_B` ohne
Rand-Dirac-Terme. In der gemeinsamen G-Realisierung setzen sich diese
Abbildungen als Inklusionen `F_A subset F_B` fort; (11) sichert bereits ihre
Stetigkeit. Identität und Cocycle gelten als Gleichheiten physischer Quellen.

Die Form `q_A(u,v)=integral w_sigma conj(uhat)vhat` ist stetig, denn

\[
|w_\sigma|\le g+s_\sigma\le\frac{12}{5}b_A.
\tag{12}
\]

Innerhalb derselben Kammer ist ihr Symbol unverändert. Im einzigen anderen
Fall `A<=A8<B` sind beide alten Quellen in `[-A,A]` getragen und
`ell=2A8>=2A`. Die Träger einer solchen Quelle und der um `+ell` oder `-ell`
verschobenen anderen Quelle schneiden sich höchstens in einer Nullmenge.
Deshalb verschwinden **beide sesquilinearen** Translationspaarungen.
Plancherel und (9) liefern auf den vollständigen Quellen

\[
q_B(J_{A,B}u,J_{A,B}v)=q_A(u,v),\qquad
\|J_{A,B}u\|_{B,17}=\|u\|_{A,17}.
\tag{13}
\]

Dies beweist die isometrische Quellfortsetzung über die Wand. Die Nullmenge
am Kontaktpunkt wird nicht als positive Überlappung behandelt. Für allgemeine
Quellen mit Träger rechts über A8 hinaus verschwindet der neue Kanal dagegen
nicht; (13) ist ausschließlich eine Aussage auf dem alten Quellenbild.

## 4. Schranken für die Wandmultiplikatoren auf allen Frequenzen

Der mögliche kritische Nenner ist `m_-(0)=0`. Die volle Gammafunktion behebt
diese Schwierigkeit durch eine Schranke, die keine Frequenzabtastung benötigt:

\[
0\le1-\cos(\ell\xi)\le g_0(\xi)\le g(\xi).
\tag{14}
\]

Beweis: Für `|xi|<=1/2` gelten
`1-cos(ell xi)<=ell² xi²/2 <=(441/200)xi² <8xi²` und
`g0(xi)>=8xi²`. Für `|xi|>=1/2` gelten `1-cos(ell xi)<=2` und `g0(xi)>=2`.
Bei Null sind beide Seiten null. Da `m_->=g>0` außerhalb von Null, folgt

\[
1\le m_+/m_-\le1+v<5/4\quad\text{fast überall}.
\tag{15}
\]

Unabhängig davon ist `n_->=kappa>5`; daher

\[
1\le n_+/n_-\le1+2v/\kappa<11/10.
\tag{16}
\]

Schließlich liefert `h_->10`, `2v<1/2`

\[
20/21<\frac{h_-}{h_-+2v}<1.
\tag{17}
\]

(15)–(17) beweisen (2). Den Wert von `a_T` bei Null wählen wir als 1;
dies ändert keinen L²-Operator. `a_D` ist durch (1) auch dort definiert.
Die Funktionen sind gerade, messbar, beschränkt und von Null weg beschränkt.
Ihre Multiplikationsoperatoren auf den jeweiligen Umgebungs-L²-Räumen sind
beschränkte Isomorphismen; ihre inversen Normen sind höchstens `sqrt(21/20)`.

## 5. Beide Carrier, Quotientenabstieg und Wandtransporte

Für jeden Terminal seien

\[
\mathcal H_A^T=\overline{T_A(W_A)}^{K_T},\qquad
\mathcal H_A^D=\overline{D_A(W_A)}^{K_D}.
\tag{18}
\]

Aus `0<=m_sigma<=h_sigma`, `kappa<=n_sigma<=s_sigma<12` folgen
`d_sigma²<=s_sigma<12` und mittels (9)

\[
b_A=t_\sigma^2+17-d_\sigma^2,\qquad
t_\sigma^2\le b_A,\quad d_\sigma^2\le(12/5)b_A.
\tag{19}
\]

T und D setzen sich somit eindeutig stetig von `W_A` auf `F_A` fort, und
ihre Werte liegen in den Carriern (18). Die Abschlüsse ihrer vollständigen
Quellenbilder sind weiterhin (18).

Für `A<=B` definiere `a^T_{A,B}=a^D_{A,B}=1`, wenn beide Terminals in derselben
Kammer liegen. Für `A<=A8<B` definiere die Funktionen getrennt durch (1).
Auf den Umgebungsräumen gilt direkt aus der unveränderten physischen Quelle

\[
a^T_{A,B}T_Au=T_BJ_{A,B}u,\qquad
a^D_{A,B}D_Au=D_BJ_{A,B}u.
\tag{20}
\]

Jede dieser Vorschriften steigt unabhängig auf ihr Quellenbild ab: Verschwindet
die linke Eingabe für die Differenz zweier Vertreter, verschwindet auch die
rechte Ausgabe. Eine gemeinsame Identifikation von T und D wird nicht benutzt.

Für `x_n=T_Au_n -> x` in `H_A^T` ist `a^T x_n=T_BJ u_n` eine konvergente
Folge in dem abgeschlossenen Raum `H_B^T`. Ihr Grenzwert ist `a^T x`.
Genau dasselbe Argument mit D gibt die beschränkten Operatoren

\[
M^T_{A,B}=\operatorname{Mult}(a^T_{A,B})|_{\mathcal H_A^T}:
\mathcal H_A^T\longrightarrow\mathcal H_B^T,
\]
\[
M^D_{A,B}=\operatorname{Mult}(a^D_{A,B})|_{\mathcal H_A^D}:
\mathcal H_A^D\longrightarrow\mathcal H_B^D.
\tag{21}
\]

Die unteren Schranken in (2) zeigen Injektivität und abgeschlossenes Bild.
Die Inversen werden nur auf diesen Bildern beansprucht. Auf allen `F_A` gilt
durch Stetigkeit das typkorrekte Quellintertwining

\[
M^T_{A,B}T_A=T_BJ_{A,B},\qquad M^D_{A,B}D_A=D_BJ_{A,B}.
\tag{22}
\]

Innerhalb jeder Kammer ist (21) die wörtliche isometrische Inklusion.
Über die Wand sind (2) die bewiesenen Normschranken; die innerhalb der alten
Kammer bewiesene rohe Isometrie wird hierfür nicht vorausgesetzt.

## 6. Identität und beide Cocycle-Gesetze

Für `A=B` ist jeder Multiplikator 1. Für ein geordnetes Tripel im Bereich
`[1,A9]` gibt es entweder keinen Wechsel oder genau einen Wechsel von minus
nach plus. Somit gilt fast überall getrennt

\[
a^T_{B,C}a^T_{A,B}=a^T_{A,C},\qquad
a^D_{B,C}a^D_{A,B}=a^D_{A,C}.
\tag{23}
\]

Es handelt sich um dasselbe feste Verhältnis der zwei Symbolfamilien,
unabhängig von der Wahl der Terminals innerhalb ihrer Kammern. Nach (21)
liegen die Zwischenwerte im richtigen mittleren Carrier; Einschränkung von
(23) liefert daher auf den gesamten abgeschlossenen Räumen

\[
M^T_{B,C}M^T_{A,B}=M^T_{A,C},\qquad
M^D_{B,C}M^D_{A,B}=M^D_{A,C},\qquad M^T_{A,A}=M^D_{A,A}=I.
\tag{24}
\]

Dies ist ein Satz für alle Paare und Tripel bis A9. Insbesondere sind sowohl
`A<A8=B<C` als auch `A<B=A8<C` erfasst; ein Wandtransport tritt jeweils nur
beim strikt größeren Endterminal auf. Es wird keine Kette kleiner Schritte
oder unbelegte Produktkonvergenz benötigt.

## 7. Defektoperatoren und vollständige Quellräume bis A9

Für die physisch getragene Quelle gilt weiterhin die volle Gamma-Energie

\[
\Gamma[u]=\int_0^\infty
\frac{e^{-r/2}}{1-e^{-2r}}\|\tau_ru-u\|_2^2\,dr.
\]

Für `r>2A` haben die beiden Träger keinen Überlapp, also ist das Normquadrat
`2||u||²`. Damit folgt auf `W_A` für alle `A<=A9`

\[
\Gamma[u]\ge4e^{-A}\|u\|^2\ge\tfrac43\|u\|^2.
\tag{25}
\]

Die nichtstrikte Fassung genügt und setzt sich auf `F_A` fort, da `g<=b_A`.
Dies ist ein neuer Trägerbound bis A9; der ältere Horizontsatz wird nicht
einfach umetikettiert. Für die monotone konvexe Funktion `f_s(x)=x²/(x+s)`
ergeben Jensen, `m_sigma>=g` und `s_sigma<12`

\[
\|T_Au\|^2\ge\tfrac2{15}\|u\|^2,\qquad
\|D_Au\|^2\le12\|u\|^2.
\tag{26}
\]

Jensen wird auf `|uhat|²/||u||²` angewandt; für `u=0` gilt (26) direkt.
Der Gamma-Erwartungswert ist endlich, und `0<=f_s(g)<=g` legitimiert den
Schritt. Die Schranken setzen sich durch (19) auf sämtliche `F_A` fort.
Folglich gilt wieder

\[
\|T_Au\|^2\le\|u\|_{A,17}^2
\le\tfrac{257}{2}\|T_Au\|^2.
\tag{27}
\]

Also ist `T_A:F_A -> H_A^T` ein beschränkter Isomorphismus: (27) macht sein
Bild abgeschlossen, und das Bild enthält den per Definition dichten
Unterraum `T_A(W_A)`. T hat trivialen Kern. Auch D hat trivialen Kern, denn
sein Multiplikator `n_sigma/sqrt(h_sigma)` ist überall positiv; für D wird
keine beschränkte inverse Quellabbildung verlangt.

Definiere auf `T_A(W_A)` den Operator `R_A(T_Au)=D_Au`. Aus (26) folgen
Wohldefiniertheit und `||R_A||<=sqrt(90)`, also die eindeutige Erweiterung
`R_A:H_A^T -> H_A^D` mit `D_A=R_AT_A` auf `F_A`.

Auf dem dichten T-Quellenbild geben (22) und diese Faktorisierung

\[
R_BM^T_{A,B}T_Au=D_BJ_{A,B}u=M^D_{A,B}R_AT_Au.
\]

Beide Operatorprodukte sind beschränkt und richtig typisiert. Deshalb

\[
R_BM^T_{A,B}=M^D_{A,B}R_A
\quad\text{auf ganz }\mathcal H_A^T.
\tag{28}
\]

Der neue T-Floor beweist Beschränktheit dieses Defekts; `sqrt(90)>1` ist
keine neue Positivitätsreserve für `G_A=I-R_A^*R_A`.

## 8. Gramkompression aus der Formnaturality

Die Identität (9) und die Faktorisierung zeigen
`q_A(u,v)=<T_Au,G_AT_Av>`. Mit (13), (22) und der Surjektivität von T_A folgt

\[
(M^T_{A,B})^*G_BM^T_{A,B}=G_A.
\tag{29}
\]

Hier wird über die Wand weder `(M^T)^*M^T=I` noch `(M^D)^*M^D=I`
eingesetzt. Äquivalent ist die aus (28) und (29) folgende Bilanz

\[
(M^T)^*M^T-I
=R_A^*\big((M^D)^*M^D-I\big)R_A.
\tag{30}
\]

Die Änderungen der beiden Grams kompensieren sich auf dem alten Quellenbild.
Das ist eine hergeleitete Kompression zwischen verschiedenen Carriern,
keine Behauptung eines gemeinsamen T/D-Transports oder einer invertierbaren
Kongruenz auf dem gesamten größeren Terminalraum.

## 9. Was die alte positive Reserve rechts der Wand tatsächlich liefert

O8 liefert für `A<=A8` den gebundenen Defektboden
`eta_*=24/(23*10^30+24)>10^(-30)`. Für `A<=A8<B<=A9` und
`y=M^T_{A,B}x` folgt aus (29) und `||M^T||<=5/4`

\[
\langle y,G_By\rangle=\langle x,G_Ax\rangle
\ge\eta_*\|x\|^2\ge\tfrac{16}{25}\eta_*\|y\|^2.
\tag{31}
\]

Der positive alte Teilraum besitzt damit im neuen Carrier einen expliziten
komprimierten Boden. Er ist abgeschlossen. Weder seine Invarianz unter G_B
noch eine Reserve auf seinem gesamten orthogonalen Komplement folgt daraus.
Gerade Quellen, die den neu verfügbaren Trägerbereich nutzen, werden durch
O8 nicht positiv kontrolliert.

Für einen positiven Abschluss des vollen zweiten Kammerraums bleiben daher
eine neue Terminalreserve einschließlich vollständiger Kopplung und
anschließend die zugehörigen korrigierten Transporte zu beweisen. Für eine
solche neue Positivitätsrechnung wird hier weder die Dimension 191 noch
ein hoher Tail-Floor übernommen.

## 10. Abnahme, Reichweite und Ergebnisstatus

Der analytische Nachweis deckt sämtliche Anforderungen des gebundenen O10-
Rohinterfaces ab: gekoppelte neue Symbole, zwei getrennte Quotientenabstiege,
beschränkte Wandtransporte, Quellenidentitäten auf den vollständigen Räumen,
beide Cocycle-Gesetze und Kompatibilität mit den benachbarten Kammertransporten.
Zusätzlich sind (28), (29) und der auf das alte Bild beschränkte Boden (31)
hergeleitet. Die Formeln bewahren die Paritätssektoren, da alle Multiplikatoren
gerade sind und physische Nullfortsetzung mit Spiegelung kommutiert.

`verify_o10.py` kontrolliert die rationalen Konstanten, die Symbolidentitäten
durch exakte Polynomarithmetik, die Aktivierungsendpunkte und eine exakte
Translationsgeometrie einschließlich Mellin-annullierender Testquellen.
Ein endliches Gegenmodell prüft ausdrücklich, dass die Gramkompression eines
positiven alten Teilraums keine Positivität des größeren Carriers beweist.
Der Prüfer ersetzt weder die Vollständigkeits- noch die Dichteargumente.

Status: **lokal hergeleitet, externe analytische Prüfung offen**. Eine
Repository-Statusübernahme bedarf der gesonderten Integration dieses Pakets.
Offen bleiben Positivität rechts von A8 auf dem gesamten neuen Terminalraum,
der Eintritt von 9 strikt rechts von A9, erneuerbare Profilreserve,
unbeschränkte/kofinale positive Fortsetzung und sämtliche globalen Aussagen.
