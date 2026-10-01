# Ungerade Extremalprojektoren und die Grenze der bisherigen Relaxation

30. September 2026 · **ODD EXTREMAL PROJECTOR LOCALIZATION**

Status: **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**. Lokales Prüfpaket.

## Ergebnis und Aussagegrenze

Der positive ungerade Extremalgap bleibt bestehen. Die Untersuchung liefert
jedoch **noch keinen engen Winkelbereich für den tatsächlichen ungeraden
Maximierer**. Die bloße Wahl einer anderen Projektivkarte oder der
Spektralprojektorformel genügt nicht, wenn man nur die bisher ausdrücklich
ausgewertete äußere Zertifikatsfamilie benutzt.

Zwei exakt definierte rationale Vervollständigungen dieser äußeren Familie
haben einfache größte Eigenwerte, aber obere Eigenrichtungen mit einem
physischen \(L^2\)-Winkel von mindestens

\[
\boxed{89.93632^\circ.}
\]

Beide erfüllen die unten aufgelisteten Moment-, Intervall- und
Loewnerbedingungen, getrennt gegen beide Präzisionsquittungen geprüft.
Die vollständigen Momente werden pro Kammer sogar durch ein einziges
positives Spektralmaß mit der richtigen kritischen Rangzahl realisiert.

**Die gedrehte Alternative ist trotzdem kein Gegenmodell zum tatsächlichen
gemeinsamen Operatorpaar.** Sie verletzt eine zusätzliche notwendige
gemeinsame \(b\)-Grammatrix-Bedingung. Ein Isometrieoperator \(J\), der diese
Alternative als wirkliche Überlappung realisiert, wird ausdrücklich nicht
behauptet. Gerade dieser Verstoß zeigt die Grenze der bisherigen äußeren
Relaxation und benennt eine konkrete fehlende Kopplung.

## Ausgangspunkt und geprüfte äußere Familie

Wir behalten \(R=M+289W\), \(W=Z-GL^{-1}G\succeq0\),
\(M=(L+17G)L^{-1}(L+17G)\) und die einfache obere Eigenzahl bei.
Die beiden früheren rationalen Certifier werden vollständig reproduziert;
beide Ergebnisdateien müssen bytegleich mit ihren archivierten Quittungen
sein. Die Eigenwerte jedes neuen Beispiels werden zusätzlich direkt geprüft.

Mit den gebundenen Ritzmatrizen \(S_A,S_B\), Resolventenschranken
\(T^-\preceq T\preceq T^+\) und Komplementböden \(\nu\) prüfen wir:

- Alle bisherigen Eintragshüllen für \(Y\), den exakten Annullator
  \(N=[-Y_l^{-1}Y_r;I_2]\), die vollen projizierten Momente und \(G,L,Z\).
- Die exakte Beziehung \(YN=0\) sowie die gemeinsame Kompression
  \(G=N^*G_PN\), \(L=N^*L_PN\), \(Z=N^*Z_PN\).
- Gemeinsame hohe Momente \(D_0,D_1,D_{-1}\), ihre Diagonalschranken,
  \(D_1\succeq\nu D_0\succeq\nu^2D_{-1}\), beide positiven Blockmomentmatrizen
  und den kritischen Spektralschnitt.
- \(L_-\preceq L\preceq L_+\), \(L\preceq N^*S_BN\),
  \(L\preceq\theta G\) sowie
  \(N^*T^-N-N^*S_BN/\nu^2\preceq Z\preceq N^*T^+N\).
- Den bisherigen positiven Gap, die obere Schranke für \(\beta_-\) und
  beide Schranken für \(\beta_+\).

Dies ist die explizite äußere Familie des Diskriminantenbeweises, ergänzt
um eine gemeinsame Realisierung der vollen Kammermomente. Sie umfasst
keine vollständige Realisierbarkeitsprüfung des gemeinsamen Transports.
Die Definition von \(Y\) durch die tatsächlichen Projektoren ist stärker
als diese endlich ausgewerteten notwendigen Bedingungen.

## Exakte Konstruktion der gemeinsamen Kammermomente

Die Eingabematrizen werden symmetrisiert gemittelt: \(S\) aus seiner engen
Ritzhülle und \(T\) aus den beiden Resolventenschranken. Die Einhaltung
aller Eingabeordnungen wird anschließend mit gerichteter rationaler
Arithmetik bewiesen. Es wird keine Zugehörigkeit nur aus einem Mittelpunkt
gefolgert.

Setze pro Kammer

\[
A=\nu I-S,\quad K=\nu^2T-2\nu I+S,
\quad L_P=AK^{-1}A,
\]

\[
G_P=(L_P+A)/\nu,\quad H=I-G_P,\quad Z_P=T-H/\nu.
\]

Der Prüfer bestätigt \(L_P\succ0\), \(G_P\succ0\), \(H\succ0\),
\(L_P\prec\theta G_P\) mit \(\theta<17/9999<\nu\), und exakt

\[
S=L_P+\nu H,\qquad T=Z_P+H/\nu,\qquad
\boxed{Z_P=G_PL_P^{-1}G_P.}
\]

Damit sind diese Matrizen echte Momente eines einzigen positiven Maßes:
Auf dem kritischen Teil verwende
\(Q_\ell=G_P^{-1/2}L_PG_P^{-1/2}\), auf dem hohen Teil den Wert \(\nu\),
und als orthonormale Trialabbildung

\[
U=\begin{bmatrix}G_P^{1/2}\\H^{1/2}\end{bmatrix}.
\]

Dann \(U^*U=I\), \(U^*QU=S\), \(U^*Q^{-1}U=T\). Der kritische Rang
ist sechs bei A9 und acht bei A11. Ferner

\[
D_0=H,\quad D_1=\nu H,\quad D_{-1}=H/\nu.
\]

Die hohe Blockmomentmatrix ist deshalb positiv und die kritische
Blockmomentmatrix hat Schurkomplement null. Das sind exakte gemeinsame
Momentbeziehungen und keine unabhängig ausgewählten Eintragshüllen.

## Zwei festgelegte Überlappungsmatrizen

Die erste Matrix \(Y^{(0)}\) ist der Mittelpunkt der gebundenen
Trialüberlappung. Für die zweite wird ein fester Eckpunkt \(Y^{(v)}\) der
bisherigen \(Y\)-Hülle gewählt. Seine Wahl ist in Prüfer und Parameterdatei
vollständig festgelegt: Mit der ersten Zeile \(f\) des mittleren oberen
Resolventenfaktors, \(H_0=f_l(Y_l^{(0)})^{-1}\) und \(N_0=N(Y^{(0)})\)
wählt das Vorzeichen von \((H_0)_i(N_0)_{j2}\) den oberen oder unteren Rand.

Der zweite feste Punkt ist

\[
Y^{(1)}=(1-t)Y^{(0)}+tY^{(v)},\qquad
t=\frac{85450543459305353673}{10^{20}}.
\]

Dieser rationale Parameter ist eine Vorschlagszahl. Der Certifier prüft
seine Folgen direkt; eine vorherige numerische Nullstellensuche ist keine
Beweisvoraussetzung. Beide Beispiele werden mit denselben A11-Momenten
komprimiert. Sie werden unverändert gegen beide geerbten Eingabeläufe
geprüft.

## Spektralprojektor ohne Eigenvektorquotient

Die vom Nutzer vorgeschlagene Formel ist korrekt. Für eine Weißung
\(A_w=M^{-1/2}WM^{-1/2}\) lautet sie

\[
P_+=(A_w-\gamma_-I)/(\gamma_+-\gamma_-).
\]

Für die Rechnung können die Quadratwurzeln von \(M\) umgangen werden.
Setze in Rohkoordinaten

\[
T_M=M^{-1}R,\qquad K_M=T_M-\beta_-I.
\]

Nach der exakten charakteristischen Identität gilt
\(K_M=(\beta_+-\beta_-)\Pi_+\). Die Matrix \(\Pi_+\) ist der
\(M\)-orthogonale obere Spektralprojektor. Ihre Spalten spannen genau die
obere Rohkoordinatengerade auf.

Für \(G=C_GC_G^*\) und \(J_G=C_G^*\) ist daher der physische orthogonale
Projektor in der \(L^2\)-orthonormalen kanonischen Basis exakt

\[
\boxed{
P_{\rm phys}=\frac{J_GK_MK_M^*J_G^*}
 {\operatorname{tr}(J_GK_MK_M^*J_G^*)}.}
\]

Der Nenner ist positiv, weil \(K_M\) Rang eins hat und \(G\succ0\).
Es wird durch keine Eigenvektorkoordinate dividiert. Die Eigenwertwurzeln
werden gerichtet eingeschlossen; \(\beta_-\) wird aus
\(\det(T_M)/\beta_+\) berechnet, um Auslöschung zu vermeiden.

| Beispiel | Geprüfte Projektoraussage |
| --- | --- |
| zentral | \((P_{\rm phys})_{11}\in[5.8538626\cdot10^{-8},5.8538627\cdot10^{-8}]\) |
| gedreht | \((P_{\rm phys})_{22}\in[4.6895606\cdot10^{-37},4.6895607\cdot10^{-37}]\) |

Die jeweiligen normalisierten kanonischen Basen hängen von \(Y\) ab.
Deshalb wird der Abstand der Beispiele zusätzlich **im selben physischen
A11-Raum** geprüft. Für nichtverschwindende obere Rohvektoren \(x_i\)
setze \(u_i=N_i x_i\). Dann

\[
\cos^2\angle(u_0,u_1)=
\frac{|u_0^*G_Pu_1|^2}{(u_0^*G_Pu_0)(u_1^*G_Pu_1)}.
\]

Diese gerichtete Rechnung liefert den Winkel von mindestens
\(89.93632^\circ\). Die beiden Beispiele widerlegen somit einen gemeinsamen
engen Kegel allein aus der aufgelisteten äußeren Familie. Sie widerlegen
weder den positiven Gap noch die Eindeutigkeit pro Vervollständigung.

## Eine zusätzliche notwendige gemeinsame Grammatrix

Für die wirklichen Projektoren seien

\[
B_A=G_{P,A}+L_{P,A}/17,\qquad B_B=G_{P,B}+L_{P,B}/17.
\]

Die beiden Familien \(JP_AU_A\) und \(P_BU_B\) liegen im selben positiven
\(b_B/17\)-Skalarproduktraum. Die Nullfortsetzung \(J\) erhält \(b\).
Ihre gemeinsame Grammatrix erfüllt daher notwendig

\[
\boxed{\begin{pmatrix}B_A&Y\\Y^*&B_B\end{pmatrix}\succeq0.}
\]

Insbesondere gilt \(YB_B^{-1}Y^*\preceq B_A\). Aus
\(G_{P,A}\preceq I\), \(L_{P,A}\preceq S_A\) und analog für B folgt sogar
die schwächere, ausschließlich aus den vorhandenen Ritzdaten prüfbare
notwendige Bedingung

\[
\boxed{
I+S_A/17-Y(I+S_B/17)^{-1}Y^*\succeq0.}
\]

Für die gedrehte Alternative liegt deren sechster Diagonaleintrag in

\[
[-2.0494309\cdot10^{-2},-2.0494308\cdot10^{-2}].
\]

Damit scheitert diese Alternative eindeutig an einer echten gemeinsamen
Projektorbedingung. Sie besitzt pro Kammer konsistente Spektralmaße, aber
keine dadurch bewiesene gemeinsame Transportrealisierung. Die Unterscheidung
zwischen Momentrealisierung und gemeinsamem Operatorpaar ist hier wesentlich.

Diese Grammatrix ist eine weitere notwendige Bedingung für denselben
tatsächlichen Gegenstand. Ihre vollständige gemeinsame Auswertung zusammen
mit \(YN=0\) und den Momenten ist der nächste offene Rechenschritt.
Einfache Eintragsverengungen und einzelne lineare Funktionalschranken
lieferten in der vorliegenden Untersuchung noch keinen engen tatsächlichen
ungeraden Winkelbereich. Eine Unmöglichkeit für diese weiter verschärfte
Familie wird nicht behauptet.

## Residualwinkel und Zuordnung zum oberen Eigenwert

Der alternative Residualansatz bleibt möglich. Für ein symmetrisches
weißgemachtes Problem, \(\mu=y^*A_wy/\|y\|^2\) und
\(r=(A_w-\mu I)y\), folgt aus der Zerlegung in beide Eigenrichtungen

\[
\sin\angle(y,\operatorname{ran}P_+)
\le\frac{\|r\|}{\|y\|\,|\mu-\gamma_-|}.
\]

Dafür muss der Abstand von \(\mu\) zum **unteren** Eigenwert positiv
zertifiziert werden. Der bekannte Abstand beider Eigenwerte allein reicht
für diese Zuordnung nicht: Ein exakter unterer Eigenvektor hat Residuum
null. Der neue algebraische Test enthält diesen Fall als Negativkontrolle.
Auch nach einer erfolgreichen Weißungsrechnung bleibt die physische
Rücktransformation über \(M\) und \(G\) erforderlich.

## Abschlussstatus

Das Paket zertifiziert eine Grenze der bisher ausgewerteten äußeren
Relaxation und eine zusätzliche notwendige Kopplung. **Die tatsächliche
ungerade Richtungslokalisierung bleibt offen.** Die bandweisen Momente des
tatsächlichen Maximierers werden in diesem Block deshalb noch nicht
ausgewiesen. Der vorherige positive Gap in beiden Paritäten und die gerade
Richtungslokalisierung bleiben bestehen.

Die Rechnung betrifft weiterhin die inverse Antwort \(V_0x\). Sie ändert
keinen Status für PR #187/A13, Vorwärts-Erneuerung, kofinale Positivität,
globales Objekt X oder RH. Quellenbindungen, Reproduktion und Prüfungen
sind in `REPRODUKTION.md` beschrieben.
