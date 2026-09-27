# O8: neue Tail-Reduktion und Vorbereitung des Terminals A₈

27. September 2026 · **Lokaler mathematischer Entwurf, unabhängig ungeprüft. O8 bleibt OPEN.**

## Ergebnis und nächster Schritt

Der fachliche Engpass bleibt eine **strikte Reserve auf dem gesamten neuen Terminalraum**:

\[
G_A=I-R_A^*R_A\succeq\eta_A I,\qquad \eta_A>0.
\]

Als konkreten neuen Terminal wählen wir **A=A₈=log(8)/2**. Das nutzt die ganze erste Kammer. Ein positiver Reserveboden dort würde sich über die bereits konstruierten rohen isometrischen Inklusionen auf alle kleineren Terminals dieser Kammer übertragen; die Konstruktion korrigierter positiver Transporte bleibt O9.

Die lokale Vorbereitung liefert einen neuen analytischen Reduktionsentwurf für **1≤A≤A₈**, beide Paritäten, genau die ursprünglichen Mellinbedingungen:

| Größe | Neu hergeleitete Schranke |
|---|---|
| Vollständiger physischer hoher Raum | q_A[u] ≥ (1/2)‖u‖₂² |
| Niedrige Koordinaten | 191 je Parität |
| Hoher Defektblock | ‖R_Ah‖² ≤ (23/24)‖h‖² |
| Hohe Defektreserve | 1/24 |
| Noch offen | Strikte Positivität der beiden tatsächlichen niedrigen Schurreste einschließlich der vollständigen hohen Antwort |

Die Zahl 191 wird unten durch Tail- und Kodimensionsargument neu begründet. Die alten Terminalmatrizen bei A=1 sind kein Zertifikat am neuen Endpunkt.

**Nächste konkrete Rechnung:** Am Terminal A₈ die beiden tatsächlichen niedrigen Formmatrizen und vollständigen Kopplungs-Grams neu einschließen. Dafür die vorhandenen allgemeinen A-Skalierungsformeln aus der B-Kalibrierung übernehmen, die Gamma-Restabschätzung für das größere Intervall ersetzen und anschließend die vollständige Schur-Untereinschließung samt positiver Reserve prüfen. Ein fehlgeschlagener unterer Schur-Bound wäre zunächst eine unzureichende Einschließung.

## 1. Aktueller Stand und verwendete Quellen

Einmal lesend bestätigt: [Main 876f9c7](https://github.com/Waschtl904/objekt-x-programm/commit/876f9c79d555019217c745923cae3bef5da8af17), zwei sichtbare Remote-Branches, keine offenen PRs. Die anderen sichtbaren einschlägigen Codex-Aufgaben waren inaktiv; federführend ist „Forschungsarbeit fortsetzen“.

Die vorhandene Navigationsarbeitskopie steht tatsächlich bei `afb1271a6d5467c239abb8e1f9268f7c23c00883`, nicht beim Main-Mergecommit. Ihr gespeicherter Git-Tree stimmt mit dem aktuell über GitHub gelesenen Main-Tree `fb0c6a0b3a73bd1a2039b95f1e65ac8023133f0a` überein. Aus genau diesem Tree wurde eine separate lokale Quellextraktion unter `work/main-source` erstellt. Vorhandene Arbeitskopien wurden nicht verändert. Im Git-Tree und den geprüften übergeordneten Arbeitsverzeichnissen wurde keine einschlägige AGENTS.md gefunden. CONTRIBUTING.md wurde gelesen.

RESEARCH_STATE.yaml, CURRENT_STATE.md, NEXT_GATES.md und SURVIVOR_REGISTRY.md führen weiterhin O8 als nächsten lokalen Gate. Ihre älteren Integrationsbeobachtungen und der Verifikationssnapshot `5f19065e28b9f2e09ae93bef0b4c752ab58997d4` werden nicht auf den aktuellen Main-Head verschoben.

Wiederverwendeter fachlicher Stand:

- **A=1:** Terminalpositivität und positiver C1-Abschluss sind in den gebundenen Paketen dokumentiert, mit `AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN`. Physische Reserve >10⁻²⁶; Defektreserve >10⁻²⁸. Beweisanker: [Terminalpaket](https://github.com/Waschtl904/objekt-x-programm/blob/2d361bed76248d0a966d6d6453ce0364eae9007d/research/x-c1/terminal-191d-schur-enclosure-2026-09-20/PROOF.md), [C1d](https://github.com/Waschtl904/objekt-x-programm/blob/a0c57ddd5c4b7dd2cf18c17b19f5af4069915387/research/x-c1/c1d-terminal-square-root-completion-2026-09-20/PROOF.md).
- **1≤A≤A₈:** O1–O7 konstruieren die getrennten rohen T-/D-Carriers, isometrische Transporte, beide Cocycle-Gesetze, R-Intertwining und Formnaturality. Die Schranke ‖R_A‖≤√90 genügt nicht für O8. Beweisanker: [O1–O4](https://github.com/Waschtl904/objekt-x-programm/blob/6623047361578b819ae44358fbbbf0b3fdeac9ff/research/x-c1/post-unit-q8-interface-2026-09-21/FIRST_CHAMBER_RAW_TD_O1_O4.md), [O5–O7](https://github.com/Waschtl904/objekt-x-programm/blob/6623047361578b819ae44358fbbbf0b3fdeac9ff/research/x-c1/post-unit-q8-interface-2026-09-21/FIRST_CHAMBER_O5_O7_ADDENDUM.md).
- Die aktiven Kanäle sind {2,3,4,5,7}; q=8 ist auch am Endpunkt A₈ inaktiv. [Obligationen O8–O10](https://github.com/Waschtl904/objekt-x-programm/blob/6623047361578b819ae44358fbbbf0b3fdeac9ff/research/x-c1/post-unit-q8-interface-2026-09-21/PROOF_OBLIGATIONS.md).
- Die allgemeine skalierte Formidentität wird aus [Universal Prime-Power Family, §§1–3](https://github.com/Waschtl904/objekt-x-programm/blob/876f9c79d555019217c745923cae3bef5da8af17/research/x-c1/universal-prime-power-family-2026-09-18/PROOF.md) verwendet. Der alte [High-Tail-Beweis](https://github.com/Waschtl904/objekt-x-programm/blob/a0ea6f80f317e4ef1132fc02c86be5bd2064e738/research/x-c1/moving-endpoint-uniform-high-tail-2026-09-19/PROOF.md) und die [Schurbrücke](https://github.com/Waschtl904/objekt-x-programm/blob/79988874cceeb01f17e0cda67485838c0b7c4f63/research/x-c1/compact-defect-moving-191d-schur-bridge-2026-09-20/PROOF.md) dienen als methodische Quellen; ihre auf A≤1 beschränkten Resultate werden nicht als neue Hypothesen importiert.

Die bytegebundenen lokalen Eingaben stehen in `source_bindings.json`. Das ist die Provenienz dieser Vorbereitung, kein neues Verifikationsregister.

## 2. Neue analytische Tail-Abschätzung

### 2.1 Form, Skalierung und Parameterbereich

Setze H=L²((-1,1),dx/2) und (U_Au)(x)=√(2A)u(Ax). Die allgemeine Formidentität lautet

\[
q_A=D_H+V+q_0(A)I-K_A-S_A,
\]
\[
D_HP_n=H_nP_n,\quad V=-\tfrac12\log(1-x^2)\ge0,
\quad q_0(A)=-\log(2\pi A)-\gamma.
\]

Hier ist S_A die Summe der fünf gewichteten partiellen Translationen. Für den regulären Gamma-Kern verwenden wir zur Unterscheidung vom Fourier-Symbol den Namen

\[
k_{\rm reg}(t)=\frac{e^{-t/2}}{1-e^{-2t}}-\frac1{2t},\qquad
(K_Af)(x)=2A\int k_{\rm reg}(A|x-y|)f(y)\,d\mu(y).
\]

Exakte logarithmische Zeugen ergeben 1<A₈<21/20<log 3. Die folgenden Abschätzungen verwenden A≤21/20, aber die aktive Kanalfamilie wird ausschließlich für A≤A₈ behauptet.

### 2.2 Gamma-Kern auf dem neuen Intervall

Mit z=t/2 gilt

\[
k_{\rm reg}(2z)=\tfrac14\left(\operatorname{sech}z+
\operatorname{csch}z-\frac1z\right).
\]

Aus sinh z≥z und sech z≤1 folgt k_reg≤1/4. Ferner ist (2j+1)!≥6ʲ, sodass für 0<z≤21/20

\[
\frac{\sinh z}{z}\le\frac1{1-z^2/6},\qquad
\operatorname{csch}z\ge\frac1z-\frac z6.
\]

Die rationale Taylor-Restabschätzung liefert cosh(21/20)<13/8. Somit

\[
k_{\rm reg}(2z)>
\frac14\left(\frac8{13}-\frac7{40}\right)
=\frac{229}{2080}>\frac1{10}.
\]

Der Grenzwert bei z=0 ist 1/4. Daher gilt auf dem gesamten benötigten Intervall 0≤t≤2A≤21/10:

\[
\boxed{\frac1{10}\le k_{\rm reg}(t)\le\frac14.}
\]

Insbesondere ‖K_A‖≤A/2≤21/40. Auf Quellen y mit ⟨1,y⟩=0 verschwindet zusätzlich der konstante Kern 1/4 in der quadratischen Form. Der Schurtest für K_A minus diesen konstanten Rang-eins-Operator ergibt

\[
|\langle y,K_Ay\rangle|
\le2A\left(\frac14-\frac1{10}\right)\|y\|^2
\le\frac{63}{200}\|y\|^2.
\tag{1}
\]

Dieser Schritt behandelt das größere Intervall analytisch; eine alte Monotonieabschätzung für t≤2 wird nicht verwendet.

### 2.3 Alle Prime-Kanäle und der Rand A₈

Für q=2 zerfällt die partielle Translation in Ketten modulo log 2. Weil 2A≤log 8=3log 2, haben diese Ketten fast überall höchstens drei Knoten. Am Gleichheitsendpunkt würden vier Knoten nur für eine Nullmenge auftreten. Die Adjazenzmatrix einer Dreierkette hat Norm √2; daher

\[
\|T_{\log2/A}\|\le\sqrt2,\qquad
w_2\|T_{\log2/A}\|\le\log2.
\]

Für q=3,4,5,7 gilt log(q)/A>1, also Norm ≤1. Folglich

\[
\|S_A\|\le\log2+\frac{\log3}{\sqrt3}
+\frac{\log2}{2}+\frac{\log5}{\sqrt5}+\frac{\log7}{\sqrt7}
<\frac{63}{20}.
\tag{2}
\]

Ein expliziter rationaler oberer Zeuge ist

\[
\frac7{10}+\frac{110}{173}+\frac7{20}+\frac{161}{223}+\frac{65}{88}<\frac{63}{20}.
\]

Verwendet werden log2<7/10, log3<11/10, log5<161/100, log7<39/20 sowie √3>173/100, √5>223/100, √7>66/25. Die Rechnung prüft diese Ungleichungen mit rationalen Restschranken.

Mit π<22/7, γ<3/5 und 2πA<33/5 gilt außerdem

\[
-q_0(A)<\log(33/5)+3/5<19/10+3/5=5/2.
\tag{3}
\]

### 2.4 Hohe Grade und exakte Mellinrekonstruktion

Im geraden Sektor beginne der rohe hohe Raum bei P₃₈₄, im ungeraden bei P₃₈₅. Beide liegen orthogonal zu P₀. Aus (1)–(3), V≥0 und H₃₈₄>261/40 folgt für jeden solchen Formvektor y≠0

\[
q_A[y]>
\left(\frac{261}{40}-\frac52-\frac{63}{200}-\frac{63}{20}\right)\|y\|^2
=\frac{14}{25}\|y\|^2.
\tag{4}
\]

Vor der Momentkorrektur bezeichnet q_A hier die durch dieselbe Gamma-/Prime-Formel definierte Form ohne Polterme auf dem noch nicht durch Mellinbedingungen eingeschränkten Referenzformraum. Die zulässige Zwei-Mellin-Quelle entsteht erst durch M_p,A.

Für p=0,1 setze m₀,A(x)=cosh(Ax/2), m₁,A(x)=sinh(Ax/2) und

\[
M_{p,A}y=y-\frac{\langle m_{p,A},y\rangle}{\langle m_{p,A},P_p\rangle}P_p.
\]

Die Paarung ist hier im zweiten Argument linear. Für z=A/2≤21/40 ergeben die Taylor-Reste und die Orthogonalität zu niedrigeren Monomen

\[
\|M_{0,A}y-y\|\le\epsilon_e\|y\|,\qquad
\epsilon_e\le\frac{(21/40)^{384}}{384!\,[1-(21/40)^2/(385\cdot386)]},
\]
\[
\|M_{1,A}y-y\|\le\epsilon_o\|y\|,\qquad
\epsilon_o\le\frac{4(21/40)^{385}}{385!\,[1-(21/40)^2/(386\cdot387)]}.
\]

Für den ungeraden Nenner gilt ⟨m₁,A,P₁⟩≥A/6 und ‖P₁‖=1/√3; sein inverser Normfaktor ist ≤2√3/A<4. Der gerade Nenner ist ≥1. Beide ε sind kleiner als 10⁻⁶.

Die elementare L²-Schranke ‖V‖₂²<3/2 für die Funktion V liefert ‖VP_p‖<4‖P_p‖; eine beschränkte Multiplikatornorm von V wird nicht behauptet. Da y zu P_p orthogonal ist, verschwinden die D_H- und q₀-Mischterme. Zusammen mit ‖K_A‖≤21/40 und (2) folgen

\[
|q_A(y,P_p)|<8\|y\|\|P_p\|,\qquad
|q_A[P_p]|<12\|P_p\|^2.
\]

Für ε=max(ε_e,ε_o) ergibt sich daher

\[
q_A[M_{p,A}y]>
(14/25-16\epsilon-12\epsilon^2)\|y\|^2
>\tfrac12(1+\epsilon^2)\|y\|^2
\ge\tfrac12\|M_{p,A}y\|^2.
\tag{5}
\]

Damit ist der neue vollständige physische Tail-Floor 1/2 hergeleitet. Für den Nullvektor und den Gebrauch auf abgeschlossenen Räumen verwenden wir die schwache Fassung ≥1/2.

### 2.5 Formabschluss und Kodimension

Dieser Schritt gehört zur neuen Reduktion. Sei 𝒢 die volle Gamma-Formdomäne mit Norm ∫(1+g)|û|². In der Kammer sind diese Norm und q_A+17‖·‖² äquivalent, weil die unveränderten Nicht-Gamma-Terme durch s<23/2 beschränkt sind.

Es gilt für die konkrete O1–O7-Vervollständigung

\[
F_A=\{u\in\mathcal G:\operatorname{supp}u\subset[-A,A],\ E_+u=E_-u=0\}.
\tag{6}
\]

Die rechte Seite ist abgeschlossen. Für die umgekehrte Inklusion wird u zunächst durch eine unitäre Dilatation r<1 ins Innere geschrumpft. Die Gamma-Reihe gibt g(tξ)≤max(1,t²)g(ξ), also gleichmäßig beschränkte, stark gegen die Identität konvergierende Dilatationen in 𝒢. Die dabei entstehenden, gegen null gehenden Momentfehler werden durch zwei feste glatte Innenfunktionen mit invertierbarer Momentmatrix beseitigt; in fester Parität genügt eine. Anschließend wird mit einem hinreichend kleinen glatten kompakten Mollifier gefaltet. Das erhält beide Nullmomente wegen E_±(u*ρ)=E_±(u)E_±(ρ), bleibt im Inneren und konvergiert in 𝒢. Damit entstehen tatsächliche glatte H¹₀-Quellen und (6) folgt für jedes A in der Kammer.

Nullfortgesetzte Polynome haben endliche Gamma-Energie: Ihre Translationsinkremente sind im Quadrat O(min(r,1)); der Gamma-Kern ist nahe null O(1/r) und bei unendlich integrierbar. Deshalb liegen die momentkorrigierten Polynome in F_A, auch wenn ihre klassischen Randspuren nicht null sind. Sie sind Formkoordinaten, keine behaupteten H¹₀-Quellen.

Mit e_n=√(2n+1)P_n definieren die Koordinaten ⟨e_n,U_Au⟩ für

\[
I_0=\{2,4,\ldots,382\},\qquad
I_1=\{3,5,\ldots,383\}
\]

jeweils 191 stetige Funktionale auf F_A^p. Ihre gemeinsame Nullstelle V_A,p ist geschlossen. Die Vertreter U_A⁻¹M_p,A e_n haben die Identität als niedrige Koordinatenmatrix, also ist die Koordinatenabbildung surjektiv und die Kodimension genau 191. Jeder Vektor im Kern ist eine hohe Legendre-Quelle mit genau der oben beschriebenen P_p-Momentkorrektur. Endliche Subtraktionen dieser Formvektoren erhalten die Domäne; (4)–(5) gelten somit auf dem vollständigen hohen Raum.

**Damit folgt 191 aus einem neuen Kammerargument.**

## 3. Defekt-Schur-Gate nach der neuen Reduktion

O5–O7 liefern T_A:F_A→H_Aᵀ als beschränkten Isomorphismus, ‖D_Au‖²≤s‖u‖² mit s<23/2 und q_A[u]=‖T_Au‖²−‖D_Au‖². Für u∈V_A,p folgt aus (5)

\[
\|D_Au\|^2\le2s\,q_A[u],\qquad
\|T_Au\|^2\le(1+2s)q_A[u]\le24q_A[u].
\]

Der hohe T-Bildraum ist geschlossen und hat Kodimension 191. Mit seiner orthogonalen Zerlegung und C_A=R_A*R_A schreibe

\[
C_A=\begin{pmatrix}\alpha&\beta^*\\\beta&K\end{pmatrix},\qquad
0\le K\le\theta I,\quad\theta=23/24.
\]

Der noch zu prüfende tatsächliche niedrige Schurrest lautet

\[
\boxed{S_A=I-\alpha-\beta^*(I-K)^{-1}\beta.}
\]

Hier ist die gesamte unendliche hohe Antwort enthalten. Ein positiver endlicher Hauptblock I−α allein genügt nicht. Ein zertifiziertes S_A≥σ_AI mit σ_A>0 würde zusammen mit der hohen Reserve δ=1/24 die gewünschte volle Reserve ergeben, beispielsweise

\[
\eta_A\ge\frac{\min(\sigma_A,\delta)}{(1+\|(I-K)^{-1}\beta\|)^2}>0.
\]

Alternativ liefert die Neumannreihe eine explizite Restkontrolle. Mit S_N=I−α−β*∑_{j=0}^N Kʲβ und ‖R_A‖²≤90 gilt β*β≤90θI, folglich

\[
0\le S_N-S_A\le2160(23/24)^{N+2}I.
\]

Dies beschreibt einen vollständigen kontrollierten Rechenweg, keinen schon ausgeführten Schurtest. Die physische Legendre-Matrix muss über die vollständige hohe Elimination und eine korrekt hergeleitete Kongruenz an diesen Defekt-Schurrest gebunden werden.

Bei einem positiven Endpunktzertifikat gilt für A≤A₈ aufgrund der beiden isometrischen Rohtransporte und R-Intertwining

\[
(M^T_{A,A_8})^*G_{A_8}M^T_{A,A_8}=G_A.
\]

Eine Endpunktreserve würde daher dieselbe Reserve auf der ganzen geschlossenen Kammer liefern. Diese Aussage setzt keine lokalen Quadratwurzel-Intertwinings voraus und erledigt O9 nicht.

## 4. Konkrete Vorbereitung der neuen Matrixrechnung

Die vorhandene Terminal-Engine ist an mehreren Stellen ausdrücklich auf A=1 festgelegt. Die bestehende B-Kalibrierung enthält bereits die benötigten allgemeinen Skalierungsformeln; diese lassen sich gezielt verwenden.

| Rechenteil | Vorbereitung für A=A₈ |
|---|---|
| Aktive Kanäle | {2,3,4,5,7}; q=8 bleibt inaktiv |
| Referenzverschiebungen | d_q=log(q)/A₈; d₂=2/3 exakt behandeln |
| Konstanter Formterm | q₀=−log(2πA₈)−γ |
| Gamma-Spalten | Koeffizientenfaktor 2A₈(A₈/2)ᵏ; allgemeine Formel `gamma_columns_at` der B-Kalibrierung |
| Gamma-Polynom | Grad 160 als vorbereiteter Kandidat; neue uniforme Restabschätzung auf 0≤t/2≤21/20 |
| Mellinmomente | z=A₈/2 in Leitkoeffizienten, positiver Reihe und Rest; keine z=1/2-Konstanten übernehmen |
| Niedrige rohe Grade | 0,…,383; nach Parität und exakter Momentkorrektur 191 Koordinaten |
| Vollständige Kopplung | V², S², V/S-Mischterme, Gamma-Anteile und vollständige Gamma/Shift-Mischterme neu bilden |
| Polynomialer Gamma-Support | Bei N=383,M=160 bis N+M+1=544 berücksichtigen; der übrige Gamma-Rest bleibt im Fehlerbudget |
| Hohe physische Reserve | Neu hergeleitet 1/2; die alte terminale Reserve 7/10 wird nicht übernommen |
| Endprüfung | Neue gerichtete Schur-Untermatrix, ggf. neuer rationaler Vorconditioner, positive LDL-Pivots und volle Norm-/Shear-Umrechnung |

### Neuer Gamma-Rest

Für x=t/2 werden die rationalen inversen Taylorpolynome p_c zu cosh x und p_s zu sinh(x)/x gebildet, dann p=(p_c+(p_s−1)/x)/4. Die endlichen Residuen p_c C_D−1 und p_s S_D−1 werden exakt berechnet; im zweiten Residuum wird vor der Majorisierung durch x dividiert. Die verbleibenden Denominator-Tails werden durch geometrische Schranken ihrer Fakultätsquotienten eingeschlossen. Beide wirklichen Nenner sind ≥1. Damit entsteht eine uniforme rationale Fehlerobergrenze auf [0,21/20].

Die ausgeführte Rechnung ergibt folgende gerundete Darstellungen exakter rationaler Obergrenzen:

| Grad | Gamma-Kernfehler | Operatorfehler ≤2A·Kernfehler |
|---|---:|---:|
| 128 | 6,407·10⁻²⁴ | 1,346·10⁻²³ |
| 160 | 1,618·10⁻²⁹ | 3,397·10⁻²⁹ |

Die neue Grad-128-Majorante überschreitet bereits für den Gamma-Operator das alte gesamte Formbudget 5·10⁻²⁶. Das beweist keine entsprechende Untergrenze für den tatsächlichen Fehler; es zeigt, dass diese Einschließung das alte Budget nicht rechtfertigt. Grad 160 bietet eine brauchbare Ausgangsbasis. Das vollständige Matrix-, Moment- und Kopplungsfehlerbudget muss dennoch neu hergeleitet werden.

## 5. Ausgeführte Prüfung und verbleibender Umfang

`python check_constants.py` läuft ausschließlich mit der Python-Standardbibliothek und schreibt `constants.json`. **34 exakte rationale Prüfungen bestehen.** Logarithmen und cosh werden mit Reihen und Resten eingeschlossen, Quadratwurzeln durch rationale Quadrate, π über die Machin-Identität und γ über H₃₂−log32. Hinzu kommen harmonische Summen, Momentreste und die beiden neuen Gamma-Residualrechnungen. Dezimalwerte dienen nur der Anzeige.

Die arithmetischen Prüfungen bestätigen die Konstanten; sie ersetzen keine unabhängige Prüfung des analytischen Arguments, insbesondere von Formdomäne, Kodimension, Kettenzerlegung und vollständiger hoher Elimination.

Noch nicht ausgeführt: neue A₈-Matrizen, positive niedrige Schurreserven, volle Terminalreserve η_A₈ und deren unabhängige Prüfung. O8 bleibt daher **OPEN**; O9 und O10 bleiben getrennt offen. Die bestehenden mathematischen Verifikationssnapshots und Registry-Status wurden nicht verändert. GitHub-Schreibzugriffe, Commits, PRs und Löschungen wurden nicht ausgeführt. Für eine spätere Veröffentlichung wäre eine konkret begrenzte Freigabe mit `EXECUTION_AUTHORIZED` erforderlich; diese lokale Vorbereitung benötigt sie nicht.
