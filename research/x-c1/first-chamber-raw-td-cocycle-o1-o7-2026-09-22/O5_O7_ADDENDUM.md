# Erste geschlossene Kammer: Nachtrag zu O5–O7

2026-09-22. Gemeinsamer lokaler Ergebnisstand mit dem Basisdokument: **FIRST-CHAMBER RAW T/D COCYCLE, O1–O7 — AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**. Dieser Nachtrag ändert für sich allein keinen Registry- oder Integrationsstatus.

Ergänzung zum Basisbeweis. Das Basisdokument enthält O1–O4; dieser Nachtrag ergänzt O5 und O6 samt uniformer Kontrolle für O7. Beide Texte verwenden denselben präzisen Kammer-Scope.

## 1. Gegenstand und bereits konstruierte Daten

Betrachtet wird ausschließlich die konkrete Fortführung der C1a-Formeln aus dem Arbeitsbeweis für

\[
1\le A\le B\le C\le A_8=\frac12\log8.
\]

Es gelten die dort definierten Quellen \(W_A\) mit beiden Mellinmomenten null, die neue explizite Fortsetzung \(F_A\) des C0-Modells und die beiden getrennten abgeschlossenen Bildräume \(\mathcal H_A^T\) und \(\mathcal H_A^D\). Das rohe O1–O4-Lemma liefert isometrische Inklusionen \(M^T,M^D\), die Quellidentitäten sowie beide Cocycle-Gesetze.

Die Multiplikatoren sind kammerweit dieselben:

\[
h=g+s,\quad m=g+\omega-c,\quad n=\kappa+\omega+c,
\quad t=\frac m{\sqrt h},\quad d=\frac n{\sqrt h},
\]
\[
m\ge g\ge0,\quad \kappa\le n\le s<12,\quad
t^2-d^2=w=g-\kappa-2c.
\]

Die exakte Eingabe

\[
10<s<\frac{23}{2}<12
\]

steht in C1a, Gleichung (5), am kanonischen Resultatcommit \(\texttt{5557d94d048dc05e7c3b4534a5a2d1711bdc71dc}\). Sie betrifft nur die unveränderten skalaren Daten der Familie \(\{2,3,4,5,7\}\). Es wird keine alte, auf \([-1,1]\) beschränkte T-Untergrenze ungeprüft auf neue Quellen übertragen.

## 2. Neuer uniformer Gamma-Floor auf der ganzen Kammer

Für die physisch nullfortgesetzte Quelle \(u\in W_A\) lautet die volle Gamma-Energie

\[
\Gamma[u]=\int_0^\infty k(r)\|\tau_ru-u\|_2^2\,dr
=\int_{\mathbb R}g(\xi)|\widehat u(\xi)|^2\,d\xi,
\qquad
k(r)=\frac{e^{-r/2}}{1-e^{-2r}}.
\]

Die Fourierdarstellung folgt aus Plancherel und Tonelli; ihre Herleitung hängt nicht von der speziellen Trägergrenze 1 ab. Für H1-Quellen ist die Energie endlich: nahe \(r=0\) gilt \(\|\tau_ru-u\|_2\le r\|u'\|_2\), und für große \(r\) gilt \(\|\tau_ru-u\|_2\le2\|u\|_2\), während \(k\) dort exponentiell abfällt.

Für \(r>2A\) sind die Träger disjunkt bis auf Nullmengen. Deshalb

\[
\|\tau_ru-u\|_2^2=2\|u\|_2^2
\]

und für \(u\ne0\)

\[
\Gamma[u]\ge 2\|u\|_2^2\int_{2A}^\infty k(r)\,dr
>2\|u\|_2^2\int_{2A}^\infty e^{-r/2}\,dr
=4e^{-A}\|u\|_2^2.
\]

Nun gilt uniform auf der geschlossenen Kammer

\[
4e^{-A}\ge4e^{-A_8}=\sqrt2>\frac43.
\]

Damit ist neu bewiesen:

\[
\boxed{\Gamma[u]>\frac43\|u\|_2^2\quad(u\in W_A\setminus\{0\}).}
\tag{1}
\]

Für sämtliche \(u\in W_A\), einschließlich \(u=0\), lautet die verwendbare Fassung

\[
\Gamma[u]\ge\frac43\|u\|_2^2.
\]

Nur für \(u\ne0\) wird eine strikte Ungleichung behauptet.

## 3. Jensen-Schritt und untere T-Schranke

Für \(u\ne0\) ist \(d\mu=|\widehat u(\xi)|^2d\xi/\|u\|_2^2\) ein Wahrscheinlichkeitsmaß. Die Funktion

\[
f_s(x)=\frac{x^2}{x+s},\quad
f_s'(x)=\frac{x(x+2s)}{(x+s)^2},\quad
f_s''(x)=\frac{2s^2}{(x+s)^3}
\]

ist für \(x\ge0\) monoton und konvex. Es gilt \(\int g\,d\mu<\infty\), und auch \(\int f_s(g)d\mu\) ist endlich, weil \(0\le f_s(g)\le g\). Wegen \(m\ge g\) und (1) erhält man

\[
\begin{aligned}
\frac{\|T_Au\|^2}{\|u\|_2^2}
&\ge\int f_s(g)\,d\mu\\
&\ge f_s\!\left(\frac{\Gamma[u]}{\|u\|_2^2}\right)\\
&>f_{12}(4/3)=\frac{(4/3)^2}{4/3+12}=\frac2{15}.
\end{aligned}
\]

Dabei wird im letzten Schritt zusätzlich \(s<12\) verwendet. Somit

\[
\boxed{\|T_Au\|^2>\frac2{15}\|u\|_2^2\quad(u\ne0),}
\qquad
\boxed{\|D_Au\|^2\le s\|u\|_2^2.}
\tag{2}
\]

Beide Abschätzungen sind uniform in \(A\). Für sämtliche \(u\in W_A\), einschließlich \(u=0\), verwenden wir

\[
\|T_Au\|^2\ge\frac2{15}\|u\|_2^2,\qquad
\|D_Au\|^2\le s\|u\|_2^2\le12\|u\|_2^2.
\]

Diese nichtstrikten Fassungen setzen sich durch die bereits bewiesene Stetigkeit auf alle \(u\in F_A\) fort. Ebenso setzt sich die nichtstrikte Gamma-Untergrenze fort: Aus \(0\le g\le b\) folgt die Stetigkeit von \(u\mapsto\sqrt g\,\widehat u\) bezüglich der \(F_A\)-Norm. Strikte Aussagen auf den Vervollständigungen werden für diese Folgerungen nicht benötigt.

## 4. O5: wohldefinierter Defektoperator und Intertwining

Auf dem dichten Rohbild \(T_A(W_A)\) definieren wir

\[
R_A^0(T_Au)=D_Au.
\]

Diese Vorschrift ist wohldefiniert. Denn \(T_Au=T_Av\) impliziert nach (2) \(u=v\) als L2-Quellen und folglich \(D_Au=D_Av\). Unabhängig davon liefert die Normabschätzung unmittelbar die benötigte Kernelinklusion.

Aus (2) folgt

\[
\|D_Au\|^2\le\frac{15s}{2}\|T_Au\|^2\le90\|T_Au\|^2.
\]

Da \(\mathcal H_A^D\) abgeschlossen und vollständig ist, besitzt \(R_A^0\) die eindeutige beschränkte Erweiterung

\[
\boxed{R_A:\mathcal H_A^T\longrightarrow\mathcal H_A^D,
\qquad \|R_A\|\le\sqrt{90}.}
\tag{3}
\]

Die Werte der Erweiterung liegen tatsächlich in \(\mathcal H_A^D\): Sie sind Grenzwerte von \(D_Au_n\) mit \(u_n\in W_A\). Es wird nicht nur ein Operator in einen unpräzisierten gemeinsamen Umgebungsraum konstruiert. Die Gleichheit \(D_A=R_AT_A\) gilt zunächst auf \(W_A\) und anschließend durch Stetigkeit auf \(F_A\).

Für \(u\in W_A\) gilt nun in \(\mathcal H_B^D\)

\[
\begin{aligned}
R_BM^T_{A,B}T_Au
&=R_BT_BJ_{A,B}u\\
&=D_BJ_{A,B}u\\
&=M^D_{A,B}D_Au\\
&=M^D_{A,B}R_AT_Au.
\end{aligned}
\]

Beide Seiten sind beschränkte Operatoren \(\mathcal H_A^T\to\mathcal H_B^D\), und \(T_A(W_A)\) ist dicht in \(\mathcal H_A^T\). Daher

\[
\boxed{R_BM^T_{A,B}=M^D_{A,B}R_A
\quad\text{auf }\mathcal H_A^T.}
\tag{4}
\]

Dies ist ein eigener Beweis des Intertwinings nach Herstellung der nötigen Beschränktheit. Es wird nicht als bloße Definition der Rohtransporte vorausgesetzt.

## 5. Kontrolle der expliziten Quellenvervollständigung

Der Arbeitsbeweis realisiert \(F_A\) mit der Norm

\[
\|u\|_{A,17}^2=q_A[u]+17\|u\|_2^2
=\|T_Au\|^2+17\|u\|_2^2-\|D_Au\|^2.
\]

Die neue Untergrenze (2) ergibt auf \(W_A\) nun sogar die uniforme Normäquivalenz

\[
\boxed{
\|T_Au\|^2\le\|u\|_{A,17}^2
\le\frac{257}{2}\|T_Au\|^2.
}
\tag{5}
\]

Links wird \(s<12<17\) verwendet; rechts wird der negative D-Term weggelassen und \(\|u\|_2^2\le(15/2)\|T_Au\|^2\) eingesetzt. Die Ungleichungen setzen sich auf \(F_A\) fort.

Damit ist \(T_A:F_A\to\mathcal H_A^T\) für diese explizite Fortsetzung ein beschränkter Isomorphismus: Die untere Schranke für \(T_A\) relativ zur \(F_A\)-Norm macht sein Bild abgeschlossen, während \(T_A(W_A)\) darin dicht in \(\mathcal H_A^T\) liegt. Insbesondere ist die Arbeit mit den vollständigen Quellen konsistent. Dieser Schluss ist eine neue Folge des Kammer-Floors; er wurde im O1–O4-Arbeitsbeweis noch nicht benötigt oder behauptet.

## 6. O6: Formnaturality und Stetigkeit auf F_A

Auf der Kammer ist

\[
w=g-\kappa-2c,\qquad b=w+17\ge g+17-s>g+5.
\]

Um den Abschluss ausdrücklich zu rechtfertigen, gilt punktweise

\[
|w|\le g+s\le C_s b,
\quad C_s:=\max\left\{1,\frac{s}{17-s}\right\}\le\frac{12}{5}.
\tag{6}
\]

Denn \((g+s)/(g+17-s)\) ist ein gewichtetes Mittel der Zahlen \(1\) und \(s/(17-s)\). Gewichtete Cauchy–Schwarz liefert daher

\[
|q_A(u,v)|\le\frac{12}{5}\|u\|_{A,17}\|v\|_{A,17}.
\tag{7}
\]

Die volle Gamma-Energie und sämtliche fünf aktiven Prime-Kanäle sind im gemeinsamen Symbol enthalten. Für \(u,v\in W_A\) ergibt physische Nullfortsetzung ohne Änderung der Fourierkonvention

\[
\begin{aligned}
q_B(J_{A,B}u,J_{A,B}v)
&=\int w\,
\overline{\widehat{Z_BJ_{A,B}u}}
\widehat{Z_BJ_{A,B}v}\,d\xi\\
&=\int w\,
\overline{\widehat{Z_Au}}\widehat{Z_Av}\,d\xi\\
&=q_A(u,v).
\end{aligned}
\]

Die Stetigkeit (7), die Dichte von \(W_A\) in \(F_A\) und die bereits konstruierte isometrische Erweiterung \(J_{A,B}:F_A\to F_B\) schließen den Grenzübergang:

\[
\boxed{q_B(J_{A,B}u,J_{A,B}v)=q_A(u,v)
\quad(u,v\in F_A).}
\tag{8}
\]

Dies ist O6 innerhalb der geschlossenen ersten Kammer. Bei \(A=A_8\) ist \(q=8\) weiterhin inaktiv. Eine Translation um \(\log8=2A_8\) hat auf Quellen mit Träger in \([-A_8,A_8]\) nur Überlappung in einer Nullmenge. Aussagen über neue Rohoperatoren rechts der Wand sind damit nicht bewiesen.

## 7. Präziser O7-Scope

Zusammen mit dem O1–O4-Arbeitsbeweis liegen für die ausdrücklich definierte Familie auf \([1,A_8]\) nun vor:

- die Quellen und ihre neue explizite C0-Verallgemeinerung \(F_A\);
- beide Rohgleichheiten und beide isometrischen Transportfamilien;
- beide Identitäts- und Cocycle-Gesetze auf den abgeschlossenen Bildräumen;
- die Defektoperatoren \(R_A\) mit uniformer Schranke \(\sqrt{90}\) und das typkorrekte Intertwining (4);
- die Formnaturality (8) auf den vollständigen Quellen;
- uniforme Normkontrollen, einschließlich (5) und (7), für die gesamte geschlossene Kammer.

Damit ist die mathematische Bezeichnung gerechtfertigt:

**FIRST-CHAMBER RAW T/D COCYCLE, O1–O7 für die deklarierte C1a-Fortführung — AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN.**

Dies ist kein Abschluss des unbeschränkten TERMINAL-HORIZON-C1-COCYCLE. Insbesondere impliziert \(\|R_A\|\le\sqrt{90}\) keine Kontraktion und keine Positivität von \(I-R_A^*R_A\). Ein gemeinsames \(V\), signierte Operatorkongruenz, positive korrigierte Transporte, Positivität für neue Terminals, das q=8-Wall-Crossing und sämtliche globalen Aussagen werden nicht behauptet. O8 und alle weiteren entsprechenden Gates bleiben davon getrennt.

Die Benennung beschreibt den lokalen Arbeitsbeweis. Review- und Integrationsstatus der kanonischen Registry werden dadurch nicht verändert.
