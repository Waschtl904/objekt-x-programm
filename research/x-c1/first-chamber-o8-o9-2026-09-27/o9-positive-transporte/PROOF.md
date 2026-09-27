# O9: positive korrigierte Transporte in der ersten geschlossenen Kammer

27. September 2026 · **AUTHOR_DERIVED_LOCAL / EXTERNAL_REVIEW_OPEN**

## Satz und Geltungsbereich

Für die konkrete C1a-Fortführung aus O1–O7 und das lokal reproduzierte O8-Ergebnis auf

\[
1\le A\le B\le C\le A_8=\tfrac12\log8
\]

existiert eine Familie positiver korrigierter Readouts und isometrischer Transporte

\[
T_{X,A}:\mathcal F_A\longrightarrow\mathcal K_{X,A},
\qquad U^X_{A,B}:\mathcal K_{X,A}\longrightarrow\mathcal K_{X,B},
\]

mit den Identitäten

\[
\langle T_{X,A}u,T_{X,A}v\rangle=q_A(u,v),
\quad U^X_{A,B}T_{X,A}=T_{X,B}J_{A,B},
\quad U^X_{B,C}U^X_{A,B}=U^X_{A,C}.
\tag{1}
\]

Die Quellen bleiben die ursprünglichen vollständigen Zwei-Mellin-Formräume. Die aktiven Kanäle sind {2,3,4,5,7}; q=8 bleibt auch bei A=A₈ inaktiv. Der Nachweis ist eine analytische Folgerung aus den unten gebundenen O1–O8-Eingaben. Er enthält keine neue Positivitätsrechnung und reicht nicht rechts über A₈ hinaus.

## 1. Gebundene Eingaben

Der [O1–O4-Basisbeweis](https://github.com/Waschtl904/objekt-x-programm/blob/6623047361578b819ae44358fbbbf0b3fdeac9ff/research/x-c1/post-unit-q8-interface-2026-09-21/FIRST_CHAMBER_RAW_TD_O1_O4.md) und der [O5–O7-Nachtrag](https://github.com/Waschtl904/objekt-x-programm/blob/6623047361578b819ae44358fbbbf0b3fdeac9ff/research/x-c1/post-unit-q8-interface-2026-09-21/FIRST_CHAMBER_O5_O7_ADDENDUM.md) liefern auf den ganzen abgeschlossenen Räumen:

1. Die beschränkten Isomorphismen T_A:𝓕_A→𝓗_Aᵀ und die beschränkten Defektoperatoren R_A:𝓗_Aᵀ→𝓗_Aᴰ mit D_A=R_AT_A.
2. Die **getrennten** isometrischen Rohtransporte Mᵀ und Mᴰ, deren Identitäts- und Cocycle-Gesetze sowie Mᵀ_{A,B}T_A=T_BJ_{A,B}.
3. R_BMᵀ_{A,B}=Mᴰ_{A,B}R_A und q_A(u,v)=⟨T_Au,(I−R_A*R_A)T_Av⟩.
4. Die Normkontrolle

\[
\|T_Au\|^2\le\|u\|_{A,17}^2
\le\tfrac{257}{2}\|T_Au\|^2.
\tag{2}
\]

Setze G_A=I−R_A*R_A. Das [O8-Paket](../o8-rechenstand/PROOF.md), seine [Schuranbindung](../o8-schur-abgleich/GRAPH_SCHUR.md) und die dokumentierte [Zertifikatsreproduktion](../o8-reproduktion/REPRODUKTION.md) liefern kammerweit

\[
\eta_* I\preceq G_A\preceq I,
\qquad
\eta_*:=\frac{24}{23\cdot10^{30}+24}>10^{-30}.
\tag{3}
\]

Die obere Schranke folgt zusätzlich direkt aus R_A*R_A≥0. Die neue Konstruktion wird auf genau diese vollständigen Räume und diese Operatoren bezogen. Die Herkunft der Repository-Eingaben steht in [SOURCE_BINDINGS.json](../SOURCE_BINDINGS.json); das gemeinsame [SHA256SUMS](../SHA256SUMS) bindet sämtliche hier veröffentlichten Dateien.

## 2. Kompressionsgesetz ohne Identifikation der Rohtransporte

Aus der Isometrie von Mᵀ, dem Defektintertwining und der Isometrie von Mᴰ folgt

\[
\begin{aligned}
(M^T_{A,B})^*G_BM^T_{A,B}
&=I-(R_BM^T_{A,B})^*(R_BM^T_{A,B})\\
&=I-R_A^*(M^D_{A,B})^*M^D_{A,B}R_A\\
&=I-R_A^*R_A=G_A.
\end{aligned}
\tag{4}
\]

Alle Produkte sind typkorrekt. Die Rechnung benötigt keine Gleichsetzung von Mᵀ und Mᴰ. Das Ergebnis ist eine Kompressionsidentität; daraus wird kein Intertwining der unveränderten Rohtransporte mit Quadratwurzeln abgeleitet.

## 3. Korrekte Quadratwurzeln und korrigierte Quellenbilder

Die stetige Funktionalrechnung auf dem jeweiligen vollständigen Raum 𝓗_Aᵀ definiert eindeutig

\[
\Delta_A=G_A^{1/2}.
\]

Aus (3) folgt

\[
\sqrt{\eta_*}I\preceq\Delta_A\preceq I,
\quad \Delta_A^2=G_A,
\quad\|\Delta_A^{-1}\|\le\eta_*^{-1/2}<10^{15}.
\tag{5}
\]

Die positive Quadratwurzel und ihre Inverse sind also überall definiert und beschränkt. Wähle die lokalen korrigierten Zielräume mit ihrer bestehenden Hilbertnorm als

\[
\mathcal K_{X,A}:=\Delta_A\mathcal H_A^T=\mathcal H_A^T,
\qquad T_{X,A}:=\Delta_AT_A.
\tag{6}
\]

Die Gleichheit der Zielräume als Mengen folgt aus der Surjektivität von Δ_A. Sie behauptet keine Gleichheit von T_{X,A} und T_A. Für alle u,v∈𝓕_A gilt exakt sesquilinear

\[
\langle T_{X,A}u,T_{X,A}v\rangle
=\langle T_Au,G_AT_Av\rangle=q_A(u,v).
\tag{7}
\]

Mit (2) und (3) erhält man

\[
\frac{2\eta_*}{257}\|u\|_{A,17}^2
\le q_A[u]\le\|u\|_{A,17}^2.
\tag{8}
\]

Somit ist die q_A-Norm der bereits vollständigen Quellenformnorm äquivalent. Es ist kein weiterer Abschluss nötig. Der Operator T_{X,A} ist unitär von (𝓕_A,q_A) auf seinen ganzen Zielraum 𝓚_{X,A}.

Insbesondere gilt

\[
\ker T_{X,A}=\ker T_A=\{0\}.
\tag{9}
\]

Die positive Korrektur erzeugt keine zusätzliche Identifikation von Quellen. Auf einem als Quotient geschriebenen Quellenbild ist der folgende Transport daher wohldefiniert. Seine Stetigkeit und Fortsetzung werden im nächsten Abschnitt auf den vollständigen Räumen direkt bewiesen.

## 4. Korrigierter Transport und Isometrie

Definiere

\[
\boxed{U^X_{A,B}:=\Delta_BM^T_{A,B}\Delta_A^{-1}.}
\tag{10}
\]

Dies ist ein überall definierter beschränkter Operator 𝓚_{X,A}→𝓚_{X,B}. Mit (4) folgt

\[
\begin{aligned}
(U^X_{A,B})^*U^X_{A,B}
&=\Delta_A^{-1}(M^T_{A,B})^*G_BM^T_{A,B}\Delta_A^{-1}\\
&=\Delta_A^{-1}G_A\Delta_A^{-1}=I.
\end{aligned}
\tag{11}
\]

U^X ist daher isometrisch, mit geschlossenem Bild und Norm 1. Es ist unitär auf sein Bild. Eine Surjektivität auf den gesamten größeren Terminalraum wird nicht benötigt.

Für alle u∈𝓕_A gilt auf den abgeschlossenen Räumen

\[
\begin{aligned}
U^X_{A,B}T_{X,A}u
&=\Delta_BM^T_{A,B}T_Au\\
&=\Delta_BT_BJ_{A,B}u
=T_{X,B}J_{A,B}u.
\end{aligned}
\tag{12}
\]

Damit ist auch die Quellvorschrift T_{X,A}u↦T_{X,B}J_{A,B}u mit (10) identisch. Wegen der Surjektivität von T_{X,A} ist U^X der eindeutige Operator, der diese Quellidentität erfüllt.

## 5. Identität und vollständiges Cocycle-Gesetz

Für A=B folgt U^X_{A,A}=I. Für jedes zulässige Tripel gilt

\[
\begin{aligned}
U^X_{B,C}U^X_{A,B}
&=\Delta_CM^T_{B,C}\Delta_B^{-1}\Delta_BM^T_{A,B}\Delta_A^{-1}\\
&=\Delta_CM^T_{B,C}M^T_{A,B}\Delta_A^{-1}\\
&=\Delta_CM^T_{A,C}\Delta_A^{-1}=U^X_{A,C}.
\end{aligned}
\tag{13}
\]

Die Inversen heben sich auf dem richtigen mittleren Carrier 𝓗_Bᵀ auf. Weder müssen die Rohtransporte surjektiv sein, noch müssen sie mit den Quadratwurzeln kommutieren. (10)–(13) gelten gleichzeitig für alle Paare und Tripel der Kammer, ohne eine Kette kleiner Fortsetzungsschritte.

## 6. Äquivalente Realisierung in einem gemeinsamen Terminalraum

Fixiere einen Endterminal C≤A₈. Für 1≤A≤C setze

\[
\widehat{\mathcal K}^{\,C}_{X,A}
:=\Delta_CM^T_{A,C}\mathcal H_A^T\subset\mathcal H_C^T,
\qquad
\widehat T^{\,C}_{X,A}:=\Delta_CM^T_{A,C}T_A.
\tag{14}
\]

Das Rohbild Mᵀ_{A,C}𝓗_Aᵀ ist abgeschlossen; Δ_C ist ein beschränkter Isomorphismus. Deshalb ist auch der korrigierte Teilraum abgeschlossen. Aus dem rohen Cocycle folgt seine Verschachtelung in A. Die verbindenden Abbildungen sind dort die wörtlichen isometrischen Inklusionen und

\[
\widehat T^{\,C}_{X,B}J_{A,B}=\widehat T^{\,C}_{X,A}.
\tag{15}
\]

Die lokalen und die gemeinsamen Zielräume sind durch die unitären Abbildungen auf das jeweilige Bild

\[
V_A^C:=\Delta_CM^T_{A,C}\Delta_A^{-1}=U^X_{A,C}
\]

verbunden. Es gelten V_A^CT_{X,A}=T̂_{X,A}^C und V_B^CU^X_{A,B}=V_A^C. Auch bei einem Wechsel des Endterminals innerhalb der Kammer bleibt die Konstruktion kompatibel:

\[
U^X_{C,D}\widehat T^{\,C}_{X,A}=\widehat T^{\,D}_{X,A}
\qquad(1\le A\le C\le D\le A_8).
\tag{16}
\]

Für C=A₈ erhält man insbesondere eine einzige terminale Quadratwurzelrealisierung über der ganzen ersten Kammer. Sie ist zur lokalen Konstruktion (6), (10) unitär äquivalent. Dies verwendet das Prinzip des gebundenen C1d-Beweises; dessen alten Horizontsatz wird dadurch keine größere Reichweite zugeschrieben.

## 7. Warum das rohe Quadratwurzel-Intertwining nicht vorausgesetzt wird

Ein exaktes endliches Beispiel zeigt den Unterschied. Setze

\[
\Delta_C=\begin{pmatrix}
9/40&0&3/10\\
0&1/2&0\\
3/10&0&9/20
\end{pmatrix},\quad
\Delta_B=\operatorname{diag}(3/8,1/2),\quad\Delta_A=3/8.
\]

Alle Matrizen sind strikt positiv und höchstens I. Setze G_j=Δ_j² und verwende die gewöhnlichen Koordinateneinbettungen als M. Dann gelten exakt die Kompressionsgesetze und der rohe Cocycle. Dennoch ist

\[
\Delta_CM^T_{B,C}\ne M^T_{B,C}\Delta_B.
\]

Der korrekt konjugierte Transport ist dagegen

\[
U^X_{B,C}
=\begin{pmatrix}3/5&0\\0&1\\4/5&0\end{pmatrix},
\]

also eine Isometrie, die das benötigte Intertwining und den Cocycle erfüllt. Die endlichen exakten Kontrollen in `check_transport_algebra.py` prüfen gerade diese Unterscheidung sowie die Formeln (11)–(16). Sie ersetzen den obigen Hilbertraumbeweis nicht.

## 8. Ergebnis und Grenzen

Relativ zu den gebundenen O1–O8-Eingaben sind sämtliche in [PROOF_OBLIGATIONS.md](https://github.com/Waschtl904/objekt-x-programm/blob/6623047361578b819ae44358fbbbf0b3fdeac9ff/research/x-c1/post-unit-q8-interface-2026-09-21/PROOF_OBLIGATIONS.md) genannten O9-Punkte auf der ersten geschlossenen Kammer hergeleitet: positive terminale Quadratwurzeln, vollständige korrigierte Räume, Kernel-/Quotientenverträglichkeit, isometrische Transporte, Quellintertwining und Cocycle.

Der lokale Beweis behält **EXTERNAL_REVIEW_OPEN**. Die operative Registrierung und Integration werden getrennt in RESEARCH_STATE.yaml geführt. Rechts von A₈ fehlen weiterhin die O10-Daten für den aktivierten q=8-Kanal und die zugehörigen rohen Wandtransporte. Eine unbeschränkte beziehungsweise kofinale positive Fortsetzung und globale Weil-Positivität folgen daraus nicht.
