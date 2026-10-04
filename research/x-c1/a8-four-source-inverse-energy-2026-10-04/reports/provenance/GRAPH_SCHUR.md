# Vom ausgeführten A₈-Check zum exakten Defekt-Schurrest

27. September 2026 · **AUTHOR_DERIVED_LOCAL / EXTERNAL_REVIEW_OPEN**

Dieser Nachtrag verbindet den eingereichten Formraum-/Graphnachtrag mit dem tatsächlich ausgeführten [A₈-Rechenstand](../o8-rechenstand/PROOF.md). Er verwendet dessen separat hergeleitete hohe physische Reserve δ=2/3. Der dortige ursprüngliche Versuch mit δ=1/2 und sein negativer Befund bleiben unverändert dokumentiert.

## 1. Gemeinsame Räume und Orientierung der Kopplung

Fixiere eine Parität. Es gelten H=L²((-1,1),dx/2), e=e_p und die 191 niedrigen rohen Legendregrade aus dem Rechenstand. Y bezeichnet den gesamten abgeschlossenen rohen hohen L²-Unterraum, beginnend bei Grad 384 beziehungsweise 385. Seine Formdomäne ist Y∩𝒟. Mit m=cosh(Ax/2) beziehungsweise sinh(Ax/2), d=⟨m,e⟩>0 und der Paarung linear im zweiten Argument sei

\[
r=\Pi_Ym/d,\qquad J_Hy=y-e\langle r,y\rangle,
\qquad \Phi=ME.
\]

Die Formraumidentifikation aus §1 des vorhandenen Beweises und Abschnitt B des eingereichten Nachtrags ergibt

\[
u=U_A^{-1}(\Phi c+J_Hy),\qquad c\in\mathbb C^{191},\ y\in Y\cap\mathscr D.
\]

Der gemeinsame Kern der niedrigen Koordinaten ist genau das Bild von Y∩𝒟 unter U_A⁻¹J_H. Die Polynome Φc gehören zur Formdomäne und ihre Formwirkung QΦc ist ein L²-Vektor.

Zur eindeutigen Zuordnung verwenden wir hier:

\[
C=\Pi_YQ\Phi:\mathbb C^{191}\to Y,\quad
\lambda=e^*Q\Phi:\mathbb C^{191}\to\mathbb C,
\quad B=J_H^*Q\Phi=C-r\lambda.
\]

Dieses B ist das Adjungierte des mit B bezeichneten Operators Y→ℂ¹⁹¹ im bisherigen `PROOF.md`. Das dortige B₀ ist außerdem bereits ein Gamma-Modelloperator. Im eingereichten Nachtrag bezeichnet B₀ dagegen die **tatsächliche** rohe Kopplung C. Diese zwei Unterschiede sind bei einem Formelvergleich zu beachten.

Aus e⊥Y folgt exakt

\[
G_H=J_H^*J_H=I+rr^*,\qquad
G_H^{-1}=I-\frac{rr^*}{1+\|r\|^2}\preceq I.
\tag{1}
\]

Die Korrektur rλ enthält die gesamte Trägerwirkung von Q, einschließlich D_H und q₀. Lediglich im rohen Ausdruck C verschwinden deren hohe Projektionen.

## 2. Vollständige hohe Elimination

Die hohe Form a[y]=q_A[U_A⁻¹J_Hy] erfüllt durch die verschärfte Tail-Herleitung

\[
a[y]\ge\delta\|J_Hy\|^2
=\delta\langle y,G_Hy\rangle,\qquad\delta=2/3.
\tag{2}
\]

Sie ist dicht auf Y definiert: endliche rohe hohe Legendrekombinationen liegen in ihrer Domäne und sind L²-dicht. Sie ist geschlossen: J_H bildet die Domäne auf den formabgeschlossenen hohen Quellenraum ab; auf diesem Raum sind wegen (2) die q- und die verschobene Formnorm äquivalent. Bei einer Cauchyfolge in der hohen Formnorm konvergieren sowohl J_Hy in der Quellenformnorm als auch y in L². Die L²-Stetigkeit von J_H identifiziert beide Grenzwerte und erhält die Domäne.

Der zugehörige positive selbstadjungierte Operator 𝒜_H besitzt deshalb einen beschränkten inversen Operator. Die Formordnung in (2) liefert

\[
\mathcal A_H^{-1}\preceq\delta^{-1}G_H^{-1}\preceq\delta^{-1}I.
\tag{3}
\]

Für die tatsächliche niedrige Formmatrix L=Φ*QΦ folgt aus Minimierung über den vollständigen hohen Raum

\[
S_{\rm phys}=L-B^*\mathcal A_H^{-1}B
\succeq L-\delta^{-1}B^*G_H^{-1}B
\succeq L-\delta^{-1}B^*B.
\tag{4}
\]

Die Minimierer sind y=−𝒜_H⁻¹Bc und gehören zur Operatordomäne. Es wird keine endliche hohe Modensumme eingesetzt.

## 3. Warum der bestehende positive Check bereits gültig bleibt

Setze Qᴾ für den Operator mit polynomialem regulärem Gamma-Kern und

\[
\widetilde C=\Pi_YQ^P\Phi,\qquad
L_0=\Phi^*Q^P\Phi,\qquad G_0=\widetilde C^*\widetilde C.
\]

Dies sind genau die gespeicherten Modellgrößen; G₀ umfasst die vollständige rohe hohe Antwort. Mit γ_K als neu hergeleitetem Gamma-Operatorfehler und ‖Φ‖≤2 gilt

\[
\|L-L_0\|\le4\gamma_K=e_L,\qquad
\|C-\widetilde C\|\le2\gamma_K.
\]

Die Trägerabschätzung ‖Qe‖<12 liefert ‖λ‖<24. Daher ist

\[
\|B-\widetilde C\|\le2\gamma_K+24\varepsilon_p=e_B,
\quad\|r\|\le\varepsilon_p.
\tag{5}
\]

Gleichung (5) ist die im ausgeführten `check_a8.py` verwendete Fehlerformel. Zusammen mit Youngs Ungleichung ergibt sie

\[
B^*B\preceq\frac{1001}{1000}G_0+1001e_B^2I.
\]

Somit gilt unmittelbar

\[
\boxed{
S_{\rm phys}\succeq
L_0-e_LI-\delta^{-1}
\left(\frac{1001}{1000}G_0+1001e_B^2I\right)
=F_{\rm bisher}.}
\tag{6}
\]

Die Graphmetrik erzeugt hier keinen fehlenden Fehlerterm: Der bisherige Beweis verwendet bewusst die letzte, schwächere Schranke in (3), während (5) die tatsächliche beidseitig momentkorrigierte Kopplung einschließt. Die gespeicherten positiven LDL-Pivots von F_bisher sind deshalb mit dem neuen Graphnachtrag vereinbar.

## 4. Zusätzliche Rechnung mit separatem Graphfehler

Die im eingereichten Nachtrag verwendeten groben Normen lassen sich in denselben Koordinaten begründen. Es gelten H₃₈₃<7, ‖Φ‖≤2 und in beiden Paritäten

\[
\sum_{n\in I_p}(2n+1)<272^2.
\]

Aus 0≤V(x)≤−(1/2)log(1−|x|) folgt ‖V‖²₂≤1/2. Damit genügen insbesondere ‖Qe‖<12 und

\[
\|Q\Phi\|
<14+272+8+2(5/2+21/40+63/20)<400.
\]

Der V-Term wird hier auf den endlichen niedrigen Vertretern abgeschätzt. Eine beschränkte Multiplikatornorm von V auf ganz L² wird nicht benötigt. Es folgen ‖C‖<400, ‖λ‖<24 und ‖B‖<401. Damit

\[
\|B^*G_H^{-1}B-C^*C\|
\le19224\varepsilon_p+160801\varepsilon_p^2=:h_p.
\tag{7}
\]

Für (7) zerlegt man in B*(G_H⁻¹−I)B und B*B−C*C. Der erste Term ist höchstens 401²ε_p², der zweite höchstens (401+400)24ε_p. Die neuen exakten rationalen Vergleiche bestätigen

\[
\varepsilon_0<1{,}73\cdot10^{-935},\quad
\varepsilon_1<9{,}39\cdot10^{-938},\quad
2h_p<10^{-930},\quad\delta^{-1}h_p<10^{-930}.
\]

Mit e_C=2γ_K ist daher die separate Untereinschließung

\[
\boxed{
F_{\rm graph}=L_0-\frac{3003}{2000}G_0
-\left(e_L+\frac{3003}{2}e_C^2+10^{-930}\right)I
\preceq L-\delta^{-1}B^*G_H^{-1}B
\preceq S_{\rm phys}.}
\tag{8}
\]

Die Konstanten 3003/2000 und 3003/2 folgen aus δ⁻¹=3/2 und der gleichen Young-Wahl τ=1/1000. Es gibt keine Vorkonditionierung, die den skalaren Fehlerterm verändern würde.

Auch ohne erneuten LDL-Lauf folgt aus dem skalaren Vergleich

\[
F_{\rm graph}-F_{\rm bisher}
=\left[\delta^{-1}1001(e_B^2-e_C^2)-10^{-930}\right]I
\succeq-10^{-930}I
\]

die Positivität, denn der gespeicherte positive σ-Boden ist in beiden Paritäten größer als 2·10⁻⁹³⁰. Dieser Vergleich wird exakt rational geprüft. Zusätzlich hat `check_graph_schur.py` (8) tatsächlich aus den gespeicherten L₀-/G₀-Intervallen aufgebaut und beide 191-dimensionalen LDL-Zerlegungen erneut gerichtet ausgeführt. Jeweils alle 191 Pivots sind strikt positiv.

## 5. Normumrechnung ohne Gleichsetzung der Koordinatensysteme

Sei σ=1/tr(F_graph⁻¹)>0 der gerichtet berechnete Eigenwertboden. Setze Ψ=J_HG_H⁻¹ᐟ²; dann ist Ψ eine L²-Isometrie. Mit B̂=G_H⁻¹ᐟ²B und

\[
t=G_H^{1/2}y+\delta^{-1}\widehat Bc
\]

liefert die quadratische Ergänzung der konservativen hohen Form aus (2)

\[
q_A[u]\ge\sigma\|c\|^2+\delta\|t\|^2,
\quad
U_Au=(\Phi-\delta^{-1}\Psi\widehat B)c+\Psi t.
\]

Wähle b²=tr((1001/1000)G₀+1001e_B²I). Dann ist ‖B̂‖≤‖B‖≤b. Aus ‖Φ‖≤2 folgt

\[
\|u\|^2\le\left[(2+b/\delta)^2+1\right]
(\|c\|^2+\|t\|^2).
\]

Der neue Prüfer verwendet deshalb

\[
c_{\rm phys}=\frac{\min(\sigma,\delta)}{(2+b/\delta)^2+1},
\qquad
\eta=\frac{c_{\rm phys}}{c_{\rm phys}+23/2}.
\tag{9}
\]

Die Berechnung von (9) erfolgt erneut mit gerichteten Intervallen. Sie bestätigt in beiden Paritäten insbesondere die bisherigen gemeinsamen rationalen Böden c_phys≥12/10³⁰ und η>10⁻³⁰. Die günstigeren angezeigten Zahlen stammen aus dieser präziseren Normumrechnung; der gemeinsame bisherige Boden wird beibehalten.

## 6. Kongruenz zum tatsächlichen Defekt-Schurrest

Für die konkrete O1–O7-Fortführung ist T_A ein beschränkter Isomorphismus auf den abgeschlossenen T-Bildraum. Der hohe T-Raum

\[
\mathcal H=T_AU_A^{-1}J_H(Y\cap\mathscr D)
\]

ist abgeschlossen und hat Kodimension 191. Die hohe T-Reserve ist aus (2) und ‖D_Au‖²≤(23/2)‖u‖² mindestens

\[
\frac{2/3}{2/3+23/2}=\frac4{73}.
\]

In der orthogonalen T-Zerlegung in niedrigen und hohen Raum definiert man daher den wohldefinierten exakten Defekt-Schurrest

\[
S_{\rm def}=I-\alpha-\beta^*(I-K)^{-1}\beta.
\]

Sei Z_T=P_{\mathcal H^\perp}T_AU_A⁻¹Φ und G_T=Z_T*Z_T. Die niedrigen Vertreter sind unabhängig modulo dem hohen Quellenraum, also ist Z_T bijektiv auf den 191-dimensionalen niedrigen T-Raum und G_T strikt positiv. Mit U_T=Z_TG_T⁻¹ᐟ² erhält man aus derselben Minimierung über sämtliche hohen Richtungen

\[
\boxed{S_{\rm phys}=G_T^{1/2}S_{\rm def}G_T^{1/2}.}
\tag{10}
\]

Dies ist das Argument aus §5 der gebundenen alten Schurbrücke, hier mit den neu begründeten Kammerhypothesen. Es benötigt keine Kompaktheit und keine Identifikation der physischen Legendrekoordinaten mit einer orthonormalen T-Basis.

Die Positivität des exakten Defekt-Schurrests folgt aus (8) und (10). Der volle Defektboden folgt zudem direkt aus (9), q=‖T_Au‖²−‖D_Au‖² und der Surjektivität von T_A. Durch Minimierung im orthogonalen T-Raum gilt derselbe Boden auch für S_def: Für einen festen niedrigen Vektor x ist ‖U_Tx+y‖²≥‖x‖² für alle hohen y. Eine numerische Berechnung von G_T oder der Einträge von S_def wird dafür nicht vorausgesetzt.

## 7. Prüfgrenzen

Die 42 neuen Prüfungen umfassen die tatsächliche Neubildung und gerichtete Prüfung von F_graph, die skalaren Graphmajoranten, die Datenbindungen und die Normumrechnung. Die ursprünglichen Modellmatrizen und ihre vollständige Integralherleitung werden aus dem vorhandenen Paket übernommen. Die 24 im eingereichten Text gemeldeten Prüfungen werden nicht als reproduzierter Lauf ausgegeben.

Dieser Abgleich schließt die Verbindung zwischen dem eingereichten Graphargument und dem lokalen positiven Rechenergebnis. Er ist keine unabhängige externe Abnahme der gesamten analytischen Kette. Die hohe Reserve 2/3, die Formraumidentifikation und die vollständige Integralrepräsentation bleiben dafür ausdrücklich benannte Prüfgegenstände. O8 wurde im Repository nicht hochgestuft; GitHub wurde in diesem Arbeitsblock nicht verändert.
