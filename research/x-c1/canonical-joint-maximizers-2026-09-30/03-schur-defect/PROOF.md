# JOINT SCHUR-DEFECT PROPORTIONALITY GATE

30. September 2026 · A9 nach A11 · beide Paritäten

Wissenschaftlicher Status: **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Lokales Prüfpaket; noch nicht im Repository integriert.

## Ergebnis

**In beiden Paritäten existiert keine zulässige gemeinsame Vervollständigung
mit \(W_0=\gamma M_0\).** Das folgt quantitativ aus dem abgeschlossenen
gemeinsamen Diskriminantenblock. Das vorliegende Paket formuliert dieses
Ergebnis als Schurdefekt-Korollar, prüft die algebraische Identität exakt und
reproduziert die vorherige rationale Rechnung bytegleich.

Zusätzlich wird der vorgeschlagene direkte Eintragstest ausgewertet:
**Gerade ist bereits \(F_1<0\) uniform zertifiziert.** Ungerade enthalten die
einzelnen Hüllen für \(F_1\) und \(F_2\) null; deren gleichzeitiges Verschwinden
ist durch den gemeinsamen Gap trotzdem ausgeschlossen.

| Parität | \(\gamma_+-\gamma_-\) mindestens | Abstand von skalaren Matrizen mindestens |
| --- | ---: | ---: |
| gerade | \(7.8612134\cdot10^{11}\) | \(3.9306067\cdot10^{11}\) |
| ungerade | \(1.4812085\cdot10^9\) | \(7.4060427\cdot10^8\) |

Die letzte Spalte bezeichnet die Operatornorm nach Weißung mit \(M_0\),
wie unten definiert. Alle Zahlen sind nach außen gerundet und gelten
jeweils für beide gebundenen Präzisionsquittungen aus 1024 und 1280 Bit.
Es handelt sich um Eigenwertabstände des verallgemeinerten Problems,
nicht um Spektrallücken des ursprünglichen Energieoperators \(Q\).

## Gemeinsame Familie und vorhandene Eingaben

Wir behalten dieselben tatsächlichen kanonischen Räume und die Rohbasis
\(V_0=P_BU_BN\) mit

\[
N=\begin{bmatrix}-Y_l^{-1}Y_r\\I_2\end{bmatrix},\qquad YN=0,
\quad G=V_0^*V_0,\quad L=V_0^*Q_BV_0,\quad Z=V_0^*Q_B^{-1}V_0.
\]

Die Indizes 0 werden im Folgenden weggelassen. Die Bedingungen (1), (5)
bis (11) des Projektorberichts bleiben gemeinsam mit den geerbten
Resolventen- und Energieschranken erhalten. Insbesondere gelten

\[
\begin{pmatrix}L&G\\G&Z\end{pmatrix}\succeq0,\qquad
L_-\preceq L\preceq L_+,\quad L\preceq N^*S_BN,\quad L\preceq\theta G,
\]

\[
N^*T^-N-N^*S_BN/\nu^2\preceq Z\preceq N^*T^+N.
\]

Der im beigefügten Diskriminantenarchiv dokumentierte Beweis hält \(Y,N,G\)
und die Faktorprodukte mit \(N\) gemeinsam fest. Er zertifiziert auf dieser
Familie eine Spuruntergrenze \(t_0\) und eine Minimax-Obergrenze \(u\) für
\(\beta_-\), sodass

\[
\beta_+-\beta_-\ge t_0-2u>0.
\]

Die beiden nach unten gerundeten Grenzen sind
\(2.2718906\cdot10^{14}\) gerade und \(4.2806927\cdot10^{11}\) ungerade.
Die zusätzlichen Bedingungen eines gemeinsamen Spektralmaßes verkleinern
diese bereits getrennte äußere Familie. Eintragsintervalle werden nicht
als voneinander unabhängig wählbare Operatorgrößen behandelt.

Der Projektorbericht allein endete noch bei einem offenen Gap. Der danach
abgeschlossene Diskriminantenblock beantwortet diese Frage positiv. Der
vorliegende Block ist dessen Korollar und beansprucht keinen zweiten
unabhängigen Erstbeweis des gemeinsamen Gaps.

## Exakte Schurdefekt Reduktion

Mit \(B=L+17G\) gilt ohne Vertauschbarkeitsannahme

\[
M=BL^{-1}B=L+34G+289GL^{-1}G,\qquad
R=L+34G+289Z.
\]

Weil \(L\succ0\), liefert das Schurkomplement

\[
W:=Z-GL^{-1}G\succeq0,\qquad \boxed{R=M+289W.}
\]

Damit sind die beiden Eigenprobleme exakt äquivalent:

\[
Rx=\beta Mx\quad\Longleftrightarrow\quad
Wx=\gamma Mx,\qquad \beta=1+289\gamma.
\]

Die maximierende Gerade bleibt dieselbe. Die bisherige quadrierte
Kopplungskonvention liefert weiterhin

\[
1-\kappa=\frac1{\beta_+}=\frac1{1+289\gamma_+},\qquad
\beta_+-\beta_-=289(\gamma_+-\gamma_-).
\]

## Proportionalität und Summe der Quadrate

Schreibe

\[
M=\begin{pmatrix}a&b\\b&c\end{pmatrix}\succ0,\qquad
W=\begin{pmatrix}p&q\\q&r\end{pmatrix}\succeq0,\quad d=ac-b^2>0,
\]

\[
F_1=aq-bp,\qquad F_2=ar-cp.
\]

Hier bezeichnet \(a=M_{11}\). Im vorherigen Diskriminantenbericht bezeichnete
\(a\) dagegen \(\det M\); der neue Prüfer berücksichtigt diesen Unterschied.

Aus \(F_1=F_2=0\) folgen wegen \(a>0\) die Gleichungen
\(q=bp/a\), \(r=cp/a\), also \(W=(p/a)M\). Die Umkehrung ist unmittelbar.
Wegen \(W\succeq0\) ist \(p/a\ge0\). Nach Weißung ist ein symmetrisches
zweidimensionales Eigenproblem genau dann doppelt, wenn seine Matrix ein
Vielfaches der Identität ist. Folglich

\[
\gamma_+=\gamma_-
\quad\Longleftrightarrow\quad W=\gamma M\ (\gamma\ge0)
\quad\Longleftrightarrow\quad F_1=F_2=0.
\]

Sei \(M=CC^*\) die untere Cholesky-Zerlegung und
\(A=C^{-1}WC^{-*}\). Direkte Rechnung ergibt

\[
A_{12}=\frac{F_1}{a\sqrt d},\qquad
A_{11}-A_{22}=\frac{-aF_2+2bF_1}{ad}.
\]

Der Eigenwertabstand einer reellen symmetrischen Zweiermatrix erfüllt
\((\gamma_+-\gamma_-)^2=(A_{11}-A_{22})^2+4A_{12}^2\). Daher exakt

\[
\boxed{(\gamma_+-\gamma_-)^2=
\frac{(-aF_2+2bF_1)^2+4dF_1^2}{a^2d^2}.}
\]

Der Prüfer kontrolliert die zugrunde liegende Polynomidentität in allen
sechs formalen Variablen mit rationalen Koeffizienten. Eine numerische
Cholesky-Zerlegung von \(M\) wird dafür nicht gebraucht.

## Quantitative Trennung

Sei \(g_\beta=t_0-2u\) die exakt rationale, erneut geprüfte Untergrenze
aus dem Diskriminantenblock und \(g_\gamma=g_\beta/289>0\). Dann gilt uniform

\[
\frac{(-aF_2+2bF_1)^2+4dF_1^2}{a^2d^2}\ge g_\gamma^2>0.
\]

Dies schließt jede proportionale gemeinsame Vervollständigung aus.
Außerdem gilt mit \(A=C^{-1}WC^{-*}\)

\[
\inf_{\gamma\ge0}\|A-\gamma I\|_{\mathrm{op}}
=\frac{\gamma_+-\gamma_-}{2}\ge\frac{g_\gamma}{2}.
\]

Der Mittelpunkt beider nichtnegativer Eigenwerte erreicht das Infimum.
Diese Distanz und der Gap sind basisunabhängig: Eine andere gemeinsame
Basis führt bei der Weißung zu einer orthogonalen Ähnlichkeit. Die
einzelnen Größen \(F_1,F_2\) beziehen sich hingegen auf die festgelegte Rohbasis.

Ein logischer Unterschied bleibt wesentlich: Der bloße Ausschluss einer
exakten Nullstelle liefert ohne zusätzliche Kompaktheit und Kontrolle von
\(M\succ0\) noch keine uniforme positive Gap-Untergrenze. Hier wird die
stärkere Aussage unmittelbar durch \(g_\gamma>0\) zertifiziert.

## Direkter Test der beiden Einträge

Die gleichen gemeinsamen Eingaben liefern folgende gerichtete Hüllen:

| Parität | \(F_1\) | \(F_2\) |
| --- | --- | --- |
| gerade | \([-1.8473127\cdot10^{33},-2.2666232\cdot10^{32}]\) | \([3.0370507\cdot10^{31},6.7459374\cdot10^{32}]\) |
| ungerade | \([-9.6234705\cdot10^{29},1.1254237\cdot10^{29}]\) | \([-4.2949857\cdot10^{28},5.0194267\cdot10^{29}]\) |

Dazu werden \(W=Z-GL^{-1}G\) und \(M=L+34G+289GL^{-1}G\) eingeschlossen.
Der Prüfer schneidet jeweils die direkte Hülle mit der äquivalenten Form

\[
F_1=(M_{11}R_{12}-M_{12}R_{11})/289,\qquad
F_2=(M_{11}R_{22}-M_{22}R_{11})/289.
\]

Gerade liefert \(|F_1|\ge2.2666232\cdot10^{32}\) bereits einen direkten
Proportionalitätsausschluss. Mit den mitgeprüften Obergrenzen für \(a,d\)
folgt zusätzlich

\[
\gamma_+-\gamma_-\ge\frac{2|F_1|}{a\sqrt d}
\ge1.2635714\cdot10^{11}.
\]

Das ist schwächer als die gemeinsame Schranke in der Ergebnistabelle,
bestätigt aber den vorgeschlagenen skalaren Test eigenständig.
Ungerade entscheidet der skalare Test nicht. Null in beiden getrennten
Hüllen ist kein Beleg für eine gemeinsame Nullstelle. Diese ist durch die
oben angegebene positive Summe der Quadrate ausgeschlossen.

## Reproduktion und Aussagegrenze

Das Paket enthält das unveränderte Diskriminanten-ZIP einschließlich Bericht,
gebundener Eingaben, Prüfern, Quellenquittungen und Manifest. Vor jeder
Reproduktion prüft der neue Certifier dessen festen SHA256 und sämtliche
internen Manifesteinträge. Er führt den rationalen Diskriminantenprüfer aus
und verlangt eine bytegleiche Ergebnisquittung. Erst dann berechnet er die
neuen Schurdefekt-Schranken. Einzelheiten stehen in `REPRODUKTION.md`.

Zusätzliche Kontrollen prüfen die formale Polynomidentität, ein
nichtkommutierendes rationales Schurbeispiel, eine proportionale Nullstelle,
den Fall \(F_1=0,F_2\ne0\) und die Ablehnung eines manipulierten Archivs.
Der abschließende Replay reproduziert auch die neue Quittung bytegleich.
Die alten großen Integral- und Operatorbeweise bleiben gebundene
Voraussetzungen; sie werden in diesem Block nicht erneut berechnet.

Der positive Gap und die Eindeutigkeit der tatsächlichen maximierenden
Geraden gelten in beiden Paritäten. Der vorherige Block hat gerade bereits
einen physischen Winkelbereich zertifiziert. Die quantitative ungerade
Richtungslokalisierung bleibt offen; ebenso die bandweisen Spektralmomente
des tatsächlichen Maximierers. Eindeutigkeit für jede zulässige Matrix
bedeutet nicht, dass alle zulässigen Matrizen dieselbe Gerade maximieren.

Der Maximierer bezeichnet weiterhin die inverse Antwort \(V_0x\), nicht
deren zugehörige Schurverschiebung \(V_0L^{-1}(L+17G)x\). Die Ergebnisse
bleiben auf dem bereits positiven Horizont bis A11. PR #187/A13,
Vorwärts-Erneuerung, kofinale Positivität, globales Objekt X und RH erhalten
durch dieses Korollar keinen neuen Status.
