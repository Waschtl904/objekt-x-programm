# q=11: vierte Wandinstanz bis zum Terminal A13

28. September 2026 · **AUTHOR_DERIVED_LOCAL / EXTERNAL_REVIEW_OPEN**

## Ergebnis

Setze

\[
A_{11}=\frac12\log 11,\qquad A_{13}=\frac12\log 13.
\]

Auf der alten Kammer gilt

\[
\mathcal Q_-=\{2,3,4,5,7,8,9\},
\]

und strikt rechts von \(A_{11}\) bis einschließlich \(A_{13}\)

\[
\mathcal Q_+=\mathcal Q_-\cup\{11\}.
\]

Wegen der strikten Aktivierungsbedingung \(\log q<2A\) bleibt 11 bei
\(A=A_{11}\) selbst inaktiv und 13 bei \(A=A_{13}\) selbst ebenfalls
inaktiv. 12 ist keine Primzahlpotenz und erzeugt daher keine arithmetische
Wand.

Der q=11-Schritt ist eine direkte Instanz des allgemeinen Prime-Power-
Wandlemmas aus
research/x-c1/chambers-through-a11-2026-09-28/wall/PROOF.md.

Er liefert auf allen vollständigen Zwei-Mellin-Quellenräumen bis \(A_{13}\)
beschränkte getrennte T-/D-Rohtransporte, Quotientenabstieg, Quellintertwining,
beide Cocycles, Defektintertwining, Formnaturality und Gramkompression.

**Nicht bewiesen wird hier die Positivität des gesamten neuen Carriers in der
vierten Kammer.** Dafür bleibt ein neuer vollständiger Terminalnachweis bei
\(A_{13}\) erforderlich.

## 1. Wanddaten

Für q=11 gilt

\[
v=w_{11}=\frac{\log 11}{\sqrt{11}},
\qquad
\ell=\log 11,
\qquad
z(\xi)=\cos(\ell\xi).
\]

Die alte A11-Familie erfüllt nach dem gebundenen q=9/A11-Paket

\[
10<s_-<13,\qquad \kappa>5.
\]

Die gekoppelten Symbole ändern sich exakt nach dem allgemeinen Gesetz

\[
m_+=m_-+v(1-z),\qquad
n_+=n_-+v(1+z),\qquad
h_+=h_-+2v.
\]

Es wird kein orthogonaler neuer Primeblock angehängt; sämtliche alten/neuen
Kreuzterme entstehen durch dieselben gemeinsamen Zähler.

## 2. Explizite rationale Wandgrenzen

Aus

\[
\log 11<\frac{12}{5},\qquad
\sqrt{11}>\frac{33}{10}
\]

folgt

\[
0<v<\frac8{11}.
\]

Ferner ist \(\ell<12/5<4\). Im allgemeinen Wandlemma ist deshalb
\(C_\ell=1\). Damit gelten fast überall

\[
\boxed{
\sqrt{\frac{55}{63}}\le a_T\le\frac{19}{11},
\qquad
\sqrt{\frac{55}{63}}\le a_D\le\frac{71}{55}.}
\]

Die untere Schranke folgt aus \(s_->10\) und \(2v<16/11\):

\[
\frac{s_-}{s_-+2v}>
\frac{10}{10+16/11}
=\frac{55}{63}.
\]

Für die obere T-Schranke gilt \(1+v<19/11\); für D wegen \(\kappa>5\)

\[
1+\frac{2v}{\kappa}
<
1+\frac{16}{55}
=
\frac{71}{55}.
\]

Damit sind beide Wandmultiplikatoren auf ihren Umgebungs-L2-Räumen
beschränkt und von Null weg beschränkt. Ihre Einschränkungen auf die
vollständigen Carrier sind injektiv und besitzen abgeschlossenes Bild.

## 3. Vollständige Quellen und endlicher Horizont bis A13

Nach Eintritt des q=11-Kanals gilt

\[
s_+<13+\frac{16}{11}
=\frac{159}{11}
<\frac{29}{2}.
\]

Auf dem gesamten endlichen Horizont \(1\le A\le A_{13}\) darf daher im
allgemeinen Wandmodell

\[
S_L=\frac{29}{2},
\qquad
\rho=S_L+1=\frac{31}{2}
\]

verwendet werden. Die Hilfsform \(q_A+\rho\|\cdot\|_2^2\) ist damit auf den
vollständigen Quellenräumen zur Gamma-Norm äquivalent.

Der allgemeine Gamma-Trägerbound liefert

\[
\Gamma[u]\ge 4e^{-A}\|u\|_2^2
\ge 4e^{-A_{13}}\|u\|_2^2
=\frac4{\sqrt{13}}\|u\|_2^2
>\|u\|_2^2.
\]

Mit der im Wandlemma verwendeten Jensenfunktion folgt deshalb die einfache
gemeinsame T-Untergrenze

\[
\|T_Au\|_2^2\ge\frac{2}{31}\|u\|_2^2,
\]

sowie

\[
\|D_Au\|_2^2\le\frac{29}{2}\|u\|_2^2.
\]

Damit

\[
\|T_Au\|_2^2
\le
\|u\|_{A,\rho}^2
\le
\frac{965}{4}\|T_Au\|_2^2,
\]

und der Defekttransfer \(R_A\), definiert durch \(D_A=R_AT_A\), ist auf
seinem vollständigen T-Carrier beschränkt mit der groben Schranke

\[
\|R_A\|^2\le\frac{899}{4}.
\]

Dieser Bound ist nur ein Wohldefiniertheits-/Beschränktheitsbound und liegt
weit über 1; er beweist keine neue Positivität.

## 4. Formnaturality und q=11-Wandtransport

Für alte Quellen mit Träger in \([-A,A]\), \(A\le A_{11}\), ist die neue
Shiftlänge

\[
\ell=\log11=2A_{11}\ge2A.
\]

Die Quelle und ihre um \(\pm\ell\) verschobene Kopie überlappen daher nur in
einer Nullmenge. Die neuen sesquilinearen Translationspaarungen verschwinden
auf dem alten Quellenbild. Also gilt über die Wand

\[
q_B(J_{A,B}u,J_{A,B}v)=q_A(u,v).
\]

Die T-/D-Wandmultiplikatoren aus §2 definieren damit die vollständigen
Rohtransporte

\[
M^T_{A,B}T_A=T_BJ_{A,B},\qquad
M^D_{A,B}D_A=D_BJ_{A,B}.
\]

Aus der allgemeinen Wandtheorie folgen Identität, Cocycle und

\[
R_BM^T_{A,B}=M^D_{A,B}R_A,
\]

sowie die Gramkompression

\[
\boxed{
(M^T_{A,B})^*G_BM^T_{A,B}=G_A,
\qquad
G_A=I-R_A^*R_A.}
\]

Keine rohe T-Isometrie wird über die Wand vorausgesetzt.

## 5. Was die alte positive A11-Reserve rechts der Wand liefert

Der unabhängig auditierte A11-Terminalboden lautet

\[
q_{A_{11}}[u]\ge 10^{-50}\|u\|_2^2.
\]

Wegen Formnaturality und physischer L2-Isometrie bleibt auf dem
transportierten alten Quellenbild derselbe physische Boden erhalten.

Da rechts der Wand bis \(A_{13}\)

\[
\|D_BJu\|_2^2\le\frac{29}{2}\|u\|_2^2,
\]

erhält der Defekt auf dem abgeschlossenen transportierten alten T-Bild den
expliziten Boden

\[
\boxed{
G_B\big|_{\operatorname{ran}M^T_{A_{11},B}}
\succeq
\frac{2}{29\cdot10^{50}+2}\,I.}
\]

Dies kontrolliert **nur** das alte Bild. Neue Quellen mit Trägeranteilen
strikt rechts von \(A_{11}\) werden dadurch nicht positiv kontrolliert.

## 6. Nächster eigenständiger Gate: A13-Terminalpositivität

Das allgemeine High-Tail-Prinzip garantiert bereits:

Für jeden gewünschten hohen Boden \(\delta>0\) gibt es auf dem festen
Horizont \(A_{13}\) einen endlichen Schnitt \(N(A_{13},\delta)\), sodass
der vollständige hohe Quellenkern in beiden Paritäten den Boden
\(q_A\ge\delta\|\cdot\|^2\) für alle \(1\le A\le A_{13}\) besitzt.

Dieser Satz bestimmt hier noch **keinen optimierten Schnitt** und keine
niedrige Terminalmatrix. Daher bleibt der vollständige Low-Schurrest bei
\(A_{13}\) offen.

Für einen Abschluss der vierten Kammer sind neu erforderlich:

1. ein expliziter zweckmäßiger High-Floor und zugehöriger Schnitt;
2. die exakte Low-Kodimension in beiden Paritäten;
3. ein vollständiger neuer Integralmodellaufbau mit dem q=11-Kanal;
4. vollständige High-Elimination und Fehlerbudget;
5. gerichtete Positivitätszertifikate für beide Low-Schurreste;
6. Reserveumrechnung auf die physische Form und den Defekt;
7. eine zweite Zertifikatsimplementierung;
8. ein direkter kleiner Normalisierungs-/Integralvergleich der neuen Engine.

Bis dahin ist **q=11 raw wall CLOSED / A13 terminal positivity OPEN**.

## Status

- q=11-Wandinstanz: **AUTHOR_DERIVED_LOCAL / EXTERNAL_REVIEW_OPEN**
- Rohtransporte bis A13: analytisch aus dem allgemeinen Wandlemma abgeleitet
- alter positiver A11-Bildraum: explizit positiv weitertransportiert
- vollständiger vierter Carrier: Positivität offen
- global/kofinal/Objekt X/RH: unverändert offen
