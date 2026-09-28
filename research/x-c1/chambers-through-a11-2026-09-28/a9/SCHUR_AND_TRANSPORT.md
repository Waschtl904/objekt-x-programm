# A9: Verbindung der Rechenmatrix mit dem vollständigen Defekt

27. September 2026 · Lokale analytische Herleitung · **EXTERNAL_REVIEW_OPEN**

Dieser Nachtrag beschreibt, was ein erfolgreicher A9-Zertifikatslauf beweist.
Den tatsächlich erreichten Rechenstand dokumentiert `README.md`.
Die neue Domäne, alle Konstanten und die Kodimension stehen in `PROOF.md`.
Das allgemeine Eliminationsschema ist an die
[veröffentlichte O8-Schurbrücke](https://github.com/Waschtl904/objekt-x-programm/blob/82a1f9d661b1668cc71eb0d5f8806c5cee73e471/research/x-c1/first-chamber-o8-o9-2026-09-27/o8-schur-abgleich/GRAPH_SCHUR.md)
gebunden. Hier wird es auf den neu begründeten A9-Raum mit seinen neuen
Konstanten angewandt und vollständig ausgeschrieben.

## 1. Hohe Graphmetrik und exakte Elimination

Fixiere eine Parität p. Es seien E die Einbettung der 296 niedrigen
normierten Legendrekoordinaten, Y der vollständige rohe hohe L²-Raum
ab Grad 594 beziehungsweise 595, e=e_p und m der entsprechende Mellinvektor.
Mit d=⟨m,e⟩>0, r=Π_Y m/d und der Paarung linear im zweiten Argument setze

\[
J_Hy=y-e\langle r,y\rangle,\quad \Phi=ME,\quad
G_H=J_H^*J_H=I+rr^*,\quad
G_H^{-1}=I-\frac{rr^*}{1+\|r\|^2}\preceq I.
\]

Jede zulässige Quelle besitzt eindeutig die Darstellung
`U_A u=Φc+J_H y`, wobei y in der hohen Formdomäne liegt.
Die in der Engine verwendete Kopplungsorientierung ist

\[
B=\Phi^*QJ_H:Y\to\mathbb C^{296},\qquad L=\Phi^*Q\Phi.
\]

Die hohe Form a[y]=q_A[U_A⁻¹J_Hy] ist dicht und geschlossen auf Y.
Endliche hohe Polynomkombinationen geben die Dichte. Für den Abschluss
benutzt man die Äquivalenz der q- und verschobenen Formnorm auf dem hohen
Quellenraum, die Stetigkeit von J_H und den Formabschluss aus `PROOF.md` §5.
Die neue physische Reserve δ=2/3 ergibt

\[
\mathcal A_H\succeq\delta G_H,\qquad
\mathcal A_H^{-1}\preceq\delta^{-1}G_H^{-1}\preceq\delta^{-1}I.
\]

Insbesondere wird der vollständige hohe Raum eliminiert:

\[
S_{\rm phys}=L-B\mathcal A_H^{-1}B^*
\succeq L-\delta^{-1}BB^*.
\tag{1}
\]

Der Minimierer `y=−𝒜_H⁻¹B*c` liegt in der Operatordomäne. Es wird keine
endliche hohe Trunkierung und keine Gleichsetzung von G_H mit I benötigt.

## 2. Die gespeicherte Gram-Matrix enthält die ganze hohe Modellantwort

Sei Qᴾ der Operator mit dem rationalen Gamma-Polynom vom Grad 224.
Die Engine speichert

\[
L_0=\Phi^*Q^P\Phi,\quad
B_0=\Phi^*Q^P|_Y,\quad G_0=B_0B_0^*.
\]

Auf dem rohen hohen Raum verschwinden die hohen Projektionen der niedrigen
D_H- und q₀-Anteile. Für V−S berechnet die Engine daher zunächst die volle
Funktions-Gram-Matrix aus V², S² und beiden gemischten Termen. Der gesamte
rohe niedrige Raum einschließlich e₀/e₁ wird durch Parseval abgezogen.
Danach ergänzt sie den Gamma-Gram und beide Gamma-Kreuzterme.
Nur das Gamma-Polynom besitzt den endlichen Support bis Grad 818;
V und die partiellen Translationen werden in ihrem vollständigen Bild erfasst.

Die hohen Momentkorrekturen sind im gespeicherten G₀ noch nicht enthalten.
Sie werden im anschließenden Fehlernachweis bezahlt. Aus
`||Φ||≤2`, `||Qe_p||<10`, `||r||≤ε_p` und dem neu berechneten Gammafehler folgt

\[
\|L-L_0\|\le e_L=4\gamma_K,\qquad
\|B-B_0\|\le e_B=2\gamma_K+20\epsilon_p.
\]

Somit liefern Youngs Ungleichung und (1)

\[
BB^*\preceq H^{up}:=\tfrac{1001}{1000}G_0+1001e_B^2I,
\qquad
S_{\rm phys}\succeq F:=L_0-e_LI-\tfrac32H^{up}.
\tag{2}
\]

Genau F wird aus den gespeicherten Modellintervallen aufgebaut und
gerichtet geprüft. Sämtliche 296 positiven LDL-Pivots sind erforderlich.
Bei Erfolg ist `σ=1/tr(F⁻¹)>0` ein Eigenwertboden. Die unabhängige
Ganzzahlprüfung rekonstruiert (2), den Gammafehler und alle Pivots.

## 3. Normumrechnung und der tatsächliche Defekt-Schurrest

Mit `b²=tr(Hup)`, `t=y+δ⁻¹B*c` und `||M||≤2` erhält man

\[
q_A[u]\ge\sigma\|c\|^2+\delta\|t\|^2,\qquad
\|u\|^2\le4(1+b/\delta)^2(\|c\|^2+\|t\|^2).
\]

Die gerichtete untere Schranke lautet also

\[
c_{\rm phys}=\frac{\min(\sigma,2/3)}{4(1+3b/2)^2},\qquad
\eta=\frac{c_{\rm phys}}{c_{\rm phys}+12}.
\tag{3}
\]

Die letzte Umrechnung folgt aus `||D_Au||²≤12||u||²` und
`||T_Au||²=q_A[u]+||D_Au||²`. T_A bildet die vollständige Formdomäne
isomorph auf ihren abgeschlossenen Carrier ab. Daher gilt der Boden η
auf dem gesamten Carrier, sobald beide Paritäten erfolgreich geprüft sind.

Auch die Verbindung zum orthogonalen T-Schurrest ist explizit.
Setze `ℋ=T_AU_A⁻¹J_H(Y∩𝒟)` und `Z_T=P_(ℋ⊥)T_AU_A⁻¹Φ`.
ℋ ist abgeschlossen und hat Kodimension 296. Z_T ist bijektiv auf ℋ⊥,
weil die niedrigen Koordinaten unabhängig modulo dem hohen Quellenraum sind.
Für `G_T=Z_T*Z_T>0` und `W_T=Z_TG_T⁻¹ᐟ²` gilt

\[
S_{\rm phys}=G_T^{1/2}W_T^*S_{\rm def}W_TG_T^{1/2},\qquad
S_{\rm def}=I-\alpha-\beta^*(I-K)^{-1}\beta.
\tag{4}
\]

Beide Seiten beschreiben dieselbe Minimierung über sämtliche hohen
Formrichtungen. Der neue hohe Defektboden 1/19 sichert die Invertierbarkeit
von I−K. (4) verlangt weder eine numerische Berechnung von G_T noch eine
Identifikation der Legendrebasis mit einer orthonormalen T-Basis.

## 4. Konsequenz für das gesamte Intervall bis A9

Sind c>0 und η=c/(c+12) gemeinsame Böden beider Paritäten am Terminal A9,
dann liefert die physische Nullfortsetzung J aus O10 für jedes `1≤A≤A9`

\[
q_A[u]=q_{A9}[J_{A,A9}u]\ge c\|J_{A,A9}u\|^2=c\|u\|^2.
\]

Damit gilt auf jedem vollständigen Carrier `G_A≥ηI`. Dieses Argument
benutzt die physische L²-Isometrie von J. Die beiden rohen T/D-Transporte
werden über die q=8-Wand nicht als Isometrien vorausgesetzt.

Mit `Δ_A=G_A^(1/2)` sind die korrigierten Transporte

\[
U^X_{A,B}=\Delta_BM^T_{A,B}\Delta_A^{-1}
\]

wohldefiniert und beschränkt. O10s Gramkompression liefert

\[
(U^X_{A,B})^*U^X_{A,B}
=\Delta_A^{-1}(M^T_{A,B})^*G_BM^T_{A,B}\Delta_A^{-1}=I.
\]

Sie sind folglich isometrische Einbettungen. Für `A≤B≤C≤A9` ergibt das
O10-Cocycle, nach Kürzung von Δ_B⁻¹Δ_B,

\[
U^X_{B,C}U^X_{A,B}=U^X_{A,C}.
\]

Mit `X_A=Δ_AT_A` gilt außerdem `U^X_{A,B}X_A=X_BJ_{A,B}`.
Alle Operatoren erhalten die Paritäten. Surjektivität auf einen größeren
Carrier folgt daraus nicht. Der Eintritt von q=9 strikt rechts von A9,
eine unbeschränkte positive Fortsetzung und globale Aussagen bleiben offen.

## Prüfgrenze

Der numerische Erfolg und die gemeinsame Reserve werden ausschließlich
aus den gespeicherten Ergebnissen übernommen. Dieser Text ist die lokale
analytische Verbindung zu den vollständigen Operatoren. Eine externe
Abnahme der Domäne, Integralrepräsentation und Operatorargumente bleibt offen.
