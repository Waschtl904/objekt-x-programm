# Destruktiver Review des positiven Wurzelankers

**Prüfstand:** 7. September 2026. **Repository-Pin:** `55a3a1617513cc5d82c47d0cfd606c6b0894c984`. **Gegenstand:** Kandidat `c6_direct_noescape.md`, §§1–9, insbesondere N11, N16 und N17–N23. §10 wurde nicht als Eingang verwendet.

**Neuester Abschlussstand: §17 — READY / SCOPED GREEN.** Auch die letzte PA-Typisierungspräzisierung ist jetzt implementiert und geprüft. Der vollständige Diff enthält ausschließlich diese deklarative Korrektur; QR und alle drei betroffenen TeX-Dateien sind gegenüber dem bestätigten Stand byteidentisch. Die früheren Warnungen über ausstehende R17- oder PA-Textkorrekturen sind im chronologischen Prüfverlauf überholt; im geprüften Scope bleibt kein offener Befund.

## 1. Urteil – mit einer konkreten Quellenbeanstandung

**N11 ist richtig. N16 folgt daraus exakt.** Es gibt keinen fehlenden Normfaktor, keine Phasenlücke, keinen unzulässigen Grenzübergang durch eine große positive Wurzel und keinen versteckten Übergang von endlichen Kompressionen zum vollen Operator. Das ist unten unabhängig bewiesen, nicht lediglich durch erfolglose Gegenbeispielsuche bewertet.

**Die tatsächliche Normalbahnaussage benötigt weder R42-Tangentialkonvergenz noch GC-AC, LOCAL-O1, Sprungkontinuität, ein Budget oder höhere Jetordnungen.** Sie benötigt den vollständigen globalen Randunterbau, seine duale Normkonvergenz und die scharfe feste **m=0**-Energie. Die dafür beanspruchten P11-/R27-Aussagen stehen tatsächlich in den Quellen; die maßgebliche R27-Unterordnung ist ausdrücklich eine Aussage für jeden Quellvektor im ursprünglichen Graphraum. ([R27, R27.2–R27.5](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R27_CONSTRAINED_GAMMA_MOSCO_LIMIT_2026-08-15.md#L128-L173); [P11, Satz 6.1](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L764-L791))

**Konkreter destruktiver Befund im vorgelagerten vollständigen Beweis von 6.1:** Die behauptete \(L^2\)-Lipschitz-Differentiation des nullfortgesetzten Quellenfeldes in (6.21c) übersieht bewegte Rand-Sprungterme. Die angegebene globale Lipschitzbehauptung ist in dieser wörtlichen Form falsch. Das betrifft die Beweispassage, nicht den Rang-eins-Unterbau und nicht N11. Unten wird die falsche Behauptung durch eine explizite lokale Gegenrechnung nachgewiesen und eine ausreichende \(1/2\)-Hölder-Reparatur für den allein benötigten m=0-Satz gegeben. ([Vollbeweis von 6.1, Step 5](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex))

**Daher kein blindes End-to-End-PASS für den unveränderten gesamten Quellenstack.** Das neue abstrakte Argument besteht den Review; die konkrete Normalfolgerung besteht mit dem m=0-Eingang, dessen hier gefundene Textlücke lokal reparierbar ist, ohne neue asymptotische Hypothese. Der volle ungerade C6-Limes folgt zusätzlich aus dem R42-Tangentialtheorem bzw. dem darunterliegenden R27-Mosco-Eingang. Dessen operatorischer Anschluss wurde unabhängig nachgerechnet; eine neue vollständige Zertifizierung aller vorgelagerten arithmetischen Recovery-Beweise wird nicht behauptet. ([R42, 7A.5–7A.7](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R42_DUAL_NORMAL_DIRECTION_AND_ETA_BLINDNESS_2026-09-02.md#L1322-L1480))

**Keine Repository-Änderung, keine Veröffentlichung, keine Registry-Promotion; keine Aussage zur Schließung von R37/G4c, Objekt X oder RH.**

## 2. Quellen- und Integritätsprüfung

Der tatsächliche HEAD stimmt mit dem verlangten Pin überein; die geprüften getrackten Quelldateien stimmen mit diesem Commit überein. Bereits zu Beginn existierte eine ungetrackte Datei `audits/P11_R43_QUADRATIC_ACTIVATION_JUMP_BUDGET_2026-09-07.md`; sie wurde weder als Quelle benutzt noch verändert. Die Prüfung ist gegenüber dem Repository read-only.

| Baustein | Tatsächliche Fundstelle | Mathematischer Befund |
|---|---|---|
| Ursprünglicher fester Graphraum | P11 Haupttext, (3.2)–(3.3), Zeilen 291–347; R27 §1 | Die terminale Quadratform wird in genau dem festen Hilbertraum repräsentiert, in dem ihre positive Wurzel genommen wird. |
| Endliche Positivität, Invertierbarkeit, Pullback, Isometrie | P11 (4.5)–(4.8), Zeilen 665–715 | Keine Zusatzhypothese: folgt aus Definition, Gammauntergrenze und Nullfortsetzungskokyklus. |
| Vollständige Restzeilen | P11 (3.4)–(3.5), Zeilen 350–423 | Primzahlpotenzen innerhalb derselben Martingalzeile bleiben summiert; Cross-Terme werden nicht entfernt. |
| Globale untere Rang-eins-Form | R27.5; TC1 MJ.7 | Tatsächliche globale Variationsschranke, keine nur endliche Jetkompression. |
| Duale Normkonvergenz und scharfer Nenner | R27.2–R27.4; 6.1-Vollbeweis Step 1 | \(\ell_U\) wird in der festen Graphdualnorm normiert; \(d_U=2U+O(1)\), nicht nur \(O(U)\). |
| Scharfe feste m=0-Energie | P11 Theorem `thm:odd`, (6.1) | Als Satz mit \(1+o(1)\) formuliert und mit Vollbeweis versehen, nicht als offenes Axiom; Step 5 hat die unten dokumentierte Rand-Lipschitzlücke. |
| Glatter Graphkern | DT.24, Zeilen 296–338 | Form-/Graphkerndichte, keine unzulässige Behauptung eines Operatorkerns. |
| Jetkompatibilität | DT.6, Zeilen 43–62 | Exakt unter Nullfortsetzung, auch für den komplexen linearen Jet. |
| R42-Tangentiallimit | R42.40, R42.47–48, R42.51–52 | Im Dokument hergeleiteter Satz; nicht bloß unterstellte Tangentialkonvergenz. Grundlage ist R27-Mosco, nicht GC-AC. |

Die ersten drei Zeilen stützen sich auf den [P11-Haupttext](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex); die nächsten drei auf [R27](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R27_CONSTRAINED_GAMMA_MOSCO_LIMIT_2026-08-15.md), [TC1](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_TC1_MixedJet.tex) und den [6.1-Vollbeweis](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex); die Kern- und Kompatibilitätszeilen auf den [Direct Terminal Bridge](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Direct_Terminal_Bridge.tex); die letzte Zeile auf [R42, §7A](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R42_DUAL_NORMAL_DIRECTION_AND_ETA_BLINDNESS_2026-09-02.md#L1156-L1209).

Governance ist von Mathematik zu trennen: R42 enthält historische interne Candidate-Warnungen, einschließlich einer solchen vor §7A; der aktuelle Fronttext führt R38–R42 dagegen unter `FROZEN — independently verified AI-GREEN`. Dieser projektinterne Status ist keine neue menschliche oder formale Zertifizierung durch diesen Review. Die spätere Integrationsakte belässt unbedingtes Strong Terminal/C6 ausdrücklich offen. ([Aktueller Fronttext](r43_global_budget_55a3/CURRENT-FRONT.md), Zeilen 40–48; [R42, historischer Dokumentstand](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R42_DUAL_NORMAL_DIRECTION_AND_ETA_BLINDNESS_2026-09-02.md); [Integrationsakte](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/R43_LOCAL_O1_AND_ORIENTATION_INTEGRATION_2026-09-07.md#L67-L89))

## 3. Unabhängiger Beweis von N11

Verwende das im ersten Argument lineare Skalarprodukt. Setze
\[
\beta(f)=\langle f,\nu\rangle,\qquad \nu\ne0,\qquad
\rho=\|\nu\|,\qquad e=\nu/\rho.
\]
Bei dieser Konvention bedeutet \(B_\nu f=\langle f,\nu\rangle\nu\). Somit
\[
\langle B_\nu f,f\rangle=|\beta(f)|^2,\qquad
B_\nu^{1/2}=B_\nu/\rho.
\]

Für jeden einzelnen Parameter sei \(M_u\) beschränkt und positiv und gelte
\[
M_u\ge B_{\nu_u},\qquad \nu_u\to\nu
\]
in Norm. Die Operator-Monotonie der positiven Quadratwurzel gibt
\[
T_u:=M_u^{1/2}\ge B_{\nu_u}/\|\nu_u\|.
\]
Hier wird der volle Operator geordnet. Die Resolventenintegralformel des Kandidaten ist korrekt: Am Ursprung genügt \(O(t^{-1/2})\), am Unendlichen für das jeweilige feste Operatorpaar \(O(t^{-3/2})\). Keine Konstante muss in \(u\) uniform sein.

Sei nun \(f\in D\) mit \(\beta(f)=1\). Dann
\[
\|T_uf\|^2\to1.
\]
Für festes \(g\in D\cap\ker\beta\) gilt
\[
\|T_ug\|\to0,\qquad
\langle T_uf,g\rangle=\langle f,T_ug\rangle\to0.
\]
Da diese Tests im Hyperraum dicht sind und \(T_uf\) beschränkt ist, gehört jeder schwache Cluster zu \(\mathbb Ce\). Schreibe ihn \(ce\). Schwache Unterhalbstetigkeit liefert \(|c|\le1\).

Die positive Wurzelunterordnung liefert dagegen
\[
\langle T_uf,f\rangle
\ge\frac{|\langle f,\nu_u\rangle|^2}{\|\nu_u\|}
\longrightarrow\frac1\rho.
\]
Der linke Ausdruck ist reell. Im schwachen Cluster ist er
\[
\langle ce,f\rangle
=c\langle e,f\rangle
=c/\rho,
\]
denn \(\beta(f)=1\) ist reell. Also ist \(c\) reell und \(c\ge1\). Daher \(c=1\). Es folgen eindeutige schwache Konvergenz und mit der Normkonvergenz starke Konvergenz:
\[
T_uf\longrightarrow e.
\]
Für beliebiges \(f\in D\) skaliert man mit \(f/\beta(f)\); auf \(\ker\beta\) ist die Behauptung schon bewiesen. Also
\[
\boxed{M_u^{1/2}f\longrightarrow\beta(f)e\qquad(f\in D).}
\]

**Keine versteckte Separabilität:** Für reelle Terminalparameter genügt das Widerspruchsfolgenargument: Bei fehlender starker Konvergenz existiert \(u_n\to\infty\) mit festem positivem Distanzabstand; aus der beschränkten Hilbertfolge kann eine schwach konvergente Teilfolge extrahiert werden, für die der obige Beweis starke Konvergenz erzwingt. Für allgemeine gerichtete Netze kann man stattdessen schwache Kompaktheit und Teilnetze benutzen. Alternativ geben die Abschätzungen in §7 ganz ohne Clusterargument dieselbe Aussage.

**Redundante Hypothese:** Für dichtes lineares \(D\) und stetiges \(\beta\ne0\) folgt die Dichte von \(D\cap\ker\beta\) bereits: Mit \(f_0\in D\), \(\beta(f_0)=1\), ersetzt man jede Approximation \(d_n\to h\in\ker\beta\) durch \(d_n-\beta(d_n)f_0\). Das ist genau die im Kandidaten benutzte zulässige Jetkorrektur.

## 4. Ein wirklich schwächerer Quelleneingang: nur m=0

Der Hinweis des Hauptagenten ist richtig. Man muss weder die Vollständigkeit aller Jets noch den Satz 6.1 für \(m\ge1\) importieren.

Sei \(E_U(z)=\langle M_Uz,z\rangle\), und gelte lediglich
\[
E_U(z)\to|\beta(z)|^2
\quad\text{für jedes feste glatte }z\text{ mit }\beta(z)\ne0.
\]
Wähle ein festes glattes \(f_0\) mit \(\beta(f_0)=1\). Für \(g\in D\cap\ker\beta\) besitzen \(f_0+g\) und \(f_0-g\) beide Jet eins. Die Parallelogrammidentität gibt exakt
\[
E_U(g)
=\tfrac12E_U(f_0+g)+\tfrac12E_U(f_0-g)-E_U(f_0)
\longrightarrow0.
\]
Dies funktioniert unverändert für komplexes \(g\). Damit folgt die gesamte Energiehypothese von N11 aus dem festen m=0-Satz. In P11 ist \(c_0=1\), sodass der führende Koeffizient wirklich eins ist. ([P11, 6.1](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L764-L791))

## 5. Prüfung des tatsächlichen P11-Unterbaus und aller Normierungen

Im ursprünglichen Graphraum \(\mathcal H_X=\mathcal K_{X,X}^{-}\) gilt mit dem **vollständigen** Rest
\[
\langle C_X(U)f,f\rangle
=\mathfrak c_{\Gamma,X}[f]
+\|\mathcal A_U^{-1/2}H_U^*J_{X,U}f\|_2^2,\qquad
\mathcal A_U=I+R_U^*R_U.
\]
Cauchy–Schwarz gegen \(\mathcal A_U^{1/2}\mathbf1_U\) liefert für alle \(f\in\mathcal H_X\)
\[
\langle C_X(U)f,f\rangle
\ge\frac{|\ell_{X,U}(f)|^2}{d_U}.
\]
Weder ein Primzahlpotenzsummand noch ein Vorzeichen wurde aus der vollständigen Restenergie entfernt. ([P11, Schurform und Vollrest](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L291-L347); [R27.5](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R27_CONSTRAINED_GAMMA_MOSCO_LIMIT_2026-08-15.md#L128-L173))

Setze
\[
\lambda_U=e^U/U^2,\qquad
\gamma_{X,U}=e^{-U/2}\sqrt U\,\ell_{X,U}.
\]
Dann lautet die exakte Umrechnung
\[
\alpha_{X,U}
=-\frac{\ell_{X,U}}{\sqrt{\lambda_Ud_U}}
=-\sqrt{\frac U{d_U}}\,\gamma_{X,U}
\longrightarrow
-\frac1{\sqrt2}(-\sqrt2\,\beta_X)=\beta_X
\]
in der **festen** Graphdualnorm. Deshalb konvergieren die Rieszvektoren in der zugehörigen Graphnorm zu \(\nu_X\). Insbesondere gibt es keinen übersehenen Faktor \(\sqrt2\), \(U^{1/2}\), \(\rho_X\) oder eine radiusabhängige führende Skala. ([R27.2–R27.4](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R27_CONSTRAINED_GAMMA_MOSCO_LIMIT_2026-08-15.md#L128-L164))

Die Quellenberechnung von \(d_U\) ist tragfähig: Auf einer Tiefenschale \(J_{p,U}=j\) verschwinden für den konstanten Terminalvektor alle Beiträge \(k\le j\); die vollständige Summe \(k>j\) wird mit der tatsächlichen Martingalunterdrückung abgeschätzt. Erst zwischen verschiedenen Primsektoren wird orthogonal summiert. Die resultierende Majorante ist proportional zu \(\sum_p(\log p)^2/p^2<\infty\), somit \(d_U=2U+O(1)\). Hier fand sich kein Cross-Term-Fehler. ([6.1-Vollbeweis, Step 1](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex#L29-L78))

**Originalnormal versus standardisierte Normale:** Das hier verwendete \(e_X=\nu_X/\|\nu_X\|\) ist der Einheitsnormalenvektor in \(\mathcal H_X\), entsprechend R42s \(\varepsilon_X\). Unter \(x=B_X^{1/2}f\) ist die standardisierte Jetfunktionalnormale dagegen
\[
r_X=B_X^{-1/2}\nu_X,
\]
und ihr Einheitsvektor ist \(r_X/\|r_X\|\), im Allgemeinen nicht \(e_X\). Der Beweis von N16 benötigt diesen Darstellungswechsel überhaupt nicht. ([R42, ursprüngliche Normale](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R42_DUAL_NORMAL_DIRECTION_AND_ETA_BLINDNESS_2026-09-02.md#L1427-L1453); [R42, Standardisierung](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R42_DUAL_NORMAL_DIRECTION_AND_ETA_BLINDNESS_2026-09-02.md#L1156-L1209))

## 6. N16: exakt der richtige Umgang mit den bewegten Ankern

Wähle ein einziges festes glattes \(f_R\), \(\beta_R(f_R)=1\), und setze \(f_S=Jf_R\). Die Nullfortsetzung ist glatt kompakt getragen im größeren Fenster und bewahrt den Jet. Aus N11 folgen
\[
x_{X,U}=\lambda_U^{-1/2}C_X(U)^{1/2}f_X\to e_X.
\]
Für jedes endliche Terminal gilt algebraisch
\[
\begin{aligned}
W_Ux_{R,U}
&=C_S(U)^{1/2}JC_R(U)^{-1/2}
  \lambda_U^{-1/2}C_R(U)^{1/2}f_R\\
&=\lambda_U^{-1/2}C_S(U)^{1/2}Jf_R=x_{S,U}.
\end{aligned}
\]
Das ist nicht \(\sqrt{J^*C_SJ}=J^*\sqrt{C_S}J\); eine solche falsche Kompressionsregel kommt nirgendwo vor.

Da \(W_U\) eine Isometrie ist,
\[
\boxed{\|W_Ue_R-e_S\|
\le\|e_R-x_{R,U}\|+\|x_{S,U}-e_S\|\to0.}
\]
Der einzige auf einen kleinen bewegten Fehler angewandte Operator ist \(W_U\) mit Norm eins. Die eventuell große Zielwurzel wird nie auf einen asymptotisch kleinen, ansonsten unkontrollierten Rest angewendet. Die endlichen Identitäten sind die tatsächlichen P11-Identitäten. ([P11, (4.5)–(4.8)](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L665-L715))

## 7. N17–N23: richtige Abschätzung, aber keine effektive Rechenzertifizierung

Alle Gleichungen N17–N23 sind mit den angegebenen Quantoren korrekt. Für festes glattes \(g\) mit \(\beta(g)=1\), \(\delta=\|g-e/\rho\|\), gilt
\[
\operatorname{Re}\langle T_Ug,e\rangle
\ge\rho\frac{|\alpha_U(g)|^2}{\|\nu_U\|}
-\rho\delta\sqrt{E_U(g)}.
\]
Hier ist \(\langle T_Ug,g\rangle\) reell positiv; dies ist auch im komplexen Fall die richtige reelle Distanzabschätzung. Folglich
\[
\|T_Ug-e\|^2
\le E_U(g)+1
-2\rho\frac{|\alpha_U(g)|^2}{\|\nu_U\|}
+2\rho\delta\sqrt{E_U(g)}
=Z_U(g).
\]
Insbesondere ist der exakte Ausdruck \(Z_U(g)\) nichtnegativ, solange \(\nu_U\ne0\), was für alle hinreichend großen \(U\) gilt.

Für \(t_X=f_X-g_X\in\ker\beta_X\) liefern Dreiecksungleichung und die Isometrie
\[
\|W_Ue_R-e_S\|
\le\sum_{X=R,S}\left(\sqrt{E_{X,U}(t_X)}+\sqrt{Z_{X,U}(g_X)}\right)
=\mathcal E_U.
\]
Die benötigten tangentialen Energielimiten folgen schon aus §4. Bei vorab festem \(g_X\) gilt
\[
E_{X,U}(t_X)\to0,\qquad Z_{X,U}(g_X)\to2\rho_X\delta_X.
\]
Also
\[
\limsup_U\mathcal E_U
\le\sqrt{2\rho_R\delta_R}+\sqrt{2\rho_S\delta_S}.
\]
Erst werden die beiden glatten Approximationen gewählt, dann ein für alle größeren reellen Terminalwerte gültiger Schwellwert. Es wird kein uniformer glatter Einheitssphärensatz benutzt.

Für orthogonale Flagprojektionen \(P_m\), die \(e_S\) vernichten, folgt
\[
q_m(U)=\|P_m(I-|e_S\rangle\langle e_S|)W_Ue_R\|^2
\le\|W_Ue_R-e_S\|^2\le\mathcal E_U^2.
\]
Damit ist
\[
\forall\varepsilon>0\;\exists U_0\;\forall U\ge U_0\;\forall m\ge1:
\quad q_m(U)<\varepsilon^2
\]
richtig und stärker als der iterierte B-FLAGTIGHT-Limes. Die kanonischen Projektionen haben genau diese Tangentialraumwirkung. ([R43, Flagquantoren](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R43_SINGLE_NORMAL_C6_GATE_2026-09-02.md#L3579-L3619))

**Wichtige Scopekorrektur:** „Vier feste Quellvektoren“ heißt endlich viele Tests, nicht endlichdimensionale Berechnung. \(E_{X,U}\) enthält weiterhin den vollen Schurresolventenoperator; \(\|\nu_{X,U}\|\) ist eine volle Graphdualnorm und \(\delta_X\) ein Abstand zur exakten Graph-Rieszrichtung. Ohne zusätzlich zertifizierte Fehlerkontrolle dafür ist N21 kein numerisch effektives Vier-Proben-Zertifikat und liefert keinen berechenbaren Schwellwert oder eine Rate. Der Kandidat verneint eine effektive Rate bereits zutreffend.

## 8. Konkrete Quellenlücke in P11 (6.21c)

### 8.1 Warum die globale Lipschitzbehauptung falsch ist

Der Vollbeweis setzt auf \(0<t<T\)
\[
k_T^0(t)=k_T(t)-K_T/T,\qquad
C_T(r,t)=2k_T^0(t)\alpha(2r-t),
\]
mit \(\alpha\in C_c^\infty(0,\varepsilon)\), \(\int\alpha=1\), setzt \(C_T\) außerhalb seines natürlichen Supports gleich null und bildet
\[
\Phi_T(r)(v)=C_T(r,v)-C_T(r,2r-v).
\]
Anschließend behauptet er global in \(L^2(0,T)\)
\[
\partial_r\Phi_T(r)(v)
=4k_T^0(v)\alpha'(2r-v)
-4(k_T^0)'(2r-v)\alpha(v).
\]
Diese Formel lässt die Distributionsterme aus den Sprüngen der Nullfortsetzung von \(k_T^0\) bei \(0,T\) weg. ([6.1-Vollbeweis, Zeilen 279–315](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex))

Dies ist nicht nur eine abstrakte Möglichkeit. Wegen \(a_*>\rho_f+2\varepsilon\) ist \(k_T(t)=0\) in einer festen Umgebung von \(T\). Für einen festen m=0-Vektor ist \(K_T\ne0\) für große \(T\), sodass \(k_T^0(T-)=-K_T/T\ne0\). Wähle \(v_0\in(0,\varepsilon)\) mit \(\alpha(v_0)\ne0\), und \(r_0=(T+v_0)/2\). In dieser oberen Randzone ist das tatsächliche Feld auf dem relevanten \(v\)-Intervall
\[
\Phi_T(r)(v)=\frac{2K_T}{T}\alpha(v)\,1_{\{v>2r-T\}}.
\]
Deshalb gilt für kleine \(h>0\)
\[
\|\Phi_T(r_0+h)-\Phi_T(r_0)\|_2^2
=\frac{4|K_T|^2}{T^2}
\int_{v_0}^{v_0+2h}|\alpha(v)|^2\,dv
\sim\frac{8|K_T|^2}{T^2}|\alpha(v_0)|^2h.
\]
Der Lipschitzquotient wächst wie \(h^{-1/2}\). Die im Paper behauptete \(L^2\)-Ableitung existiert dort nicht. Auch die historische R1-Reconciliation wiederholt diese unzutreffende globale Schlussfolgerung; ihr PASS-Label ersetzt diese fehlende Randrechnung nicht. ([R1-Reconciliation, Zeilen 40–76](r43_global_budget_55a3/audits/P11_REFEREE_E2E_R1_RECONCILIATION_2026-08-13.md))

### 8.2 Ausreichende Reparatur für den benötigten m=0-Satz

Die Lücke zerstört den m=0-Satz nicht. Es genügt eine wesentlich schwächere Quadraturkontrolle. Setze
\[
F_T=1_{(0,T)}k_T^0,\qquad
A_T=\|k_T^0\|_\infty+\|(k_T^0)'\|_\infty.
\]
Für \(|h|\le1\) liefert Zerlegung in den gemeinsamen Intervallteil und die beiden Randstreifen
\[
\|F_T(\cdot+h)-F_T\|_2
\le \sqrt T\,\|(k_T^0)'\|_\infty|h|
+C\|k_T^0\|_\infty|h|^{1/2}.
\]
Da \(\alpha\) glatt ist, folgt für das **wirklich nullfortgesetzte** Quellenfeld
\[
\|\Phi_T(r+h)-\Phi_T(r)\|_2
\le C_\alpha A_T\bigl(\sqrt T\,|h|+|h|^{1/2}\bigr).
\tag{QH}
\]
Diese Abschätzung behandelt beide bewegten Randstellen und verlangt keine falsche Operator-Lipschitzregel.

Für die positiven massennormierten Zellgewichte des Papers gilt exakt
\(\sum_{q\in I}\lambda_q=|I|\). Daher folgt direkt aus (QH)
\[
\left\|\sum_{q\in I}\lambda_q\Phi_T(r_q)
-\int_I\Phi_T(r)\,dr\right\|_2
\le C_\alpha |I|A_T
\bigl(\sqrt T\,|I|+|I|^{1/2}\bigr).
\]
Alle tatsächlich verwendeten Zukunftszellen liegen in \(r\le(T+\varepsilon)/2\); ihre Gesamtbreite ist \(O(T)\), und der im Paper verwendete Short-PNT-Eingang liefert \(\delta_T:=\max|I|\le Ce^{-2T/5}\). Weiter geben (6.10) und (6.12) für festes m=0
\[
A_T\le C_f e^{T/2}/\sqrt T,\qquad
\sqrt{M_T}\asymp_f e^{T/2}/T.
\]
Somit ist der tatsächliche Quadraturrest beschränkt durch
\[
\|Z_T^{\rm quad}\|_2
\le C_f T A_T(\sqrt T\,\delta_T+\sqrt{\delta_T})
\le {\rm poly}(T)e^{3T/10}
=o(\sqrt{M_T}).
\]
Das genügt genau für (6.23) und den scharfen m=0-Squeeze. Die Normkosten des diskreten Zertifikats bleiben \(o(M_T)\): Die Zellkostenidentität (6.20) kombiniert mit den lokalen Betragsmajoranten für \(C_T(r,\cdot)\), nicht mit einer Ableitung, ergibt die Kostenkontrolle aus (6.17)/(6.22). Bewegte Endpunktschnitte vergrößern diese Betragsmajoranten nicht. Der volle \(a=0\)-Lift mit seinem Primzahlpotenztail bleibt unverändert. ([6.1-Vollbeweis, Steps 4–7](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex))

**Status dieser Reparatur:** analytisch ausreichende Ergänzung des m=0-Beweises; keine neue Vermutung und kein Gegenbeispiel zu 6.1. Die im Quellenstack benutzte Primzahlverteilungsabschätzung wurde hier als vorhandener klassischer/externer Eingang übernommen, nicht erneut bewiesen.

### 8.3 Warum die grobe Reparatur allein R17 noch nicht neu zertifiziert

Die obige globale Hölderschranke liefert für exponentiell große Hubprofile nur einen relativ kleinen, möglicherweise absolut großen Fehler. R16/R17 benötigen teilweise absolutes \(o(1)\), nicht nur \(o(\sqrt{M_T})\). Man darf deshalb diesen Teil des Stacks nicht mit derselben groben Rechnung automatisch als vollständig neu geprüft ausgeben. ([R16, Zeilen 123–166](r43_global_budget_55a3/audits/P11_REFEREE_E2E_R16_TC1_NEARNULL_REMAINDER_2026-08-14.md); [R17, Zeilen 93–105](r43_global_budget_55a3/audits/P11_REFEREE_E2E_R17_VANISHING_NEARNULL_CORE_2026-08-14.md))

Eine präzisere lokale Randreparatur ist möglich: Für eine Sprungstelle \(r=v/2\) bzw. \(r=(T+v)/2\) unterscheiden sich diskrete Zellmasse und Lebesguemasse nur innerhalb der sie enthaltenden Zelle; beide haben dort dieselbe Gesamtmasse \(|I|\). Deshalb ist der punktweise kumulative Massefehler höchstens \(C|I|\), nicht bloß \(C|I|^{1/2}\). Die fehlenden Randbeiträge sind folglich in \(L^2_v\) höchstens
\[
C_\alpha |k_T^0(0)|e^{-4T/5}
+C_\alpha |k_T^0(T)|e^{-2T/5}.
\]
Für die im R16-Beweis kontrollierte Familie gilt
\[
|k_T^0(0)|\le C e^{T/2}/\sqrt T+C|K_T|/T,\qquad
|k_T^0(T)|=|K_T|/T,\qquad |K_T|=O(\sqrt T),
\]
also gehen beide Randfehler absolut gegen null. Die regulären Ableitungsteile können weiter mit dem lokalen Zellfaktor \(e^{-4(T-r)/5}\) kontrolliert werden. Das identifiziert eine konkrete Reparaturroute auch dort; es ersetzt nicht eine erneute vollständige Ausarbeitung sämtlicher R16/R17-Zertifikate in diesem Review.

## 9. R42-Tangentialinput: hergeleitet, aber mit eigener Abhängigkeitskette

R42.51 ist nicht als Annahme hingeschrieben: R42 §7A.1 leitet aus R27-Mosco und der uniformen Gammauntergrenze den ursprünglichen inversen Wurzellimes her; §7A.3 behandelt die individuellen Polarfaktoren; §7A.5 setzt diese Ergebnisse mit R38.12 zusammen. Diese operatorischen Schritte sind korrekt. Die Zweitordnungsresultate R41/R42 über \(\gamma_X,q_{1,X}\) werden für R42.51 nicht gebraucht. ([R42, §7A](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R42_DUAL_NORMAL_DIRECTION_AND_ETA_BLINDNESS_2026-09-02.md#L1322-L1480))

Es gibt sogar eine kürzere unabhängige Kontrolle direkt in den ursprünglichen Räumen. Aus R27-Mosco folgt
\[
C_X(U)^{-1/2}\xrightarrow{\rm SOT}
\Lambda_X^{-1/2}P_{H_X^0},
\]
wobei \(\Lambda_X\) die Gammaform auf \(H_X^0\) repräsentiert. Die exakte Identität
\[
C_S(U)^{-1/2}W_U=J\,C_R(U)^{-1/2}
\]
zeigt für \(v\in H_R^0\) und einen schwachen Cluster \(W_Uv\rightharpoonup y\):
\[
\Lambda_S^{-1/2}P_{H_S^0}y=J\Lambda_R^{-1/2}v.
\]
Also
\[
P_{H_S^0}y=Y_0v,\qquad
Y_0=\Lambda_S^{1/2}J\Lambda_R^{-1/2}.
\]
Gamma-Kompatibilität liefert
\[
\|Y_0v\|^2
=\mathfrak c_{\Gamma,S}[J\Lambda_R^{-1/2}v]
=\mathfrak c_{\Gamma,R}[\Lambda_R^{-1/2}v]
=\|v\|^2.
\]
Damit ist die gesamte mögliche Clusternorm schon tangential verbraucht; \(y=Y_0v\) und \(W_Uv\to Y_0v\) stark. Dies ist R42.51 in vereinfachter Darstellung.

**Exakte Abhängigkeit:** Volles ungerades C6 braucht neben dem neuen Normalanker die R27-Mosco-Recovery bzw. ein bereits gesichertes R42.51. Der neue Normalbeweis selbst braucht das nicht. GC-AC und die dritte inverse-root-Ordnung treten in keinem dieser operatorischen Anschlüsse auf.

## 10. Eigene unendlichdimensionale Zerstörungstests

Alle folgenden Modelle leben auf \(H=\ell^2(\mathbb N_0)\) mit Standardbasis \(e_n\) und dichtem linearem Kern \(D=c_{00}\), sofern nichts anderes gesagt wird. Sie sind **keine** Gegenbeispiele gegen N11 unter seinen vollständigen Annahmen und **keine** P11-Gegenbeispiele.

### A. Globale Unterordnung weggelassen: vollständige Normflucht

Auf \(\operatorname{span}\{e_0,e_n\}\) setze
\[
T_n=\begin{pmatrix}n^{-1}&1\\1&n\end{pmatrix}+n^{-2}I,
\]
und auf dem orthogonalen Rest \(T_n=n^{-2}I\). Dann ist \(T_n\) positiv und für jedes \(n\) invertierbar. Setze \(M_n=T_n^2\).

Für jedes feste \(f\in c_{00}\) gilt
\[
\langle M_nf,f\rangle\to|\langle f,e_0\rangle|^2.
\]
Trotzdem
\[
M_n^{1/2}e_0=(n^{-1}+n^{-2})e_0+e_n\rightharpoonup0,
\qquad \|M_n^{1/2}e_0\|\to1.
\]
Eine globale Unterordnung mit \(\nu_n\to e_0\) ist unmöglich, da deren Wurzelunterordnung den Diagonaleintrag gegen mindestens eins zwingen würde.

**Stärkerer Kompressionscheck:** Für jede feste Koordinatenkompression, die \(e_0\) enthält, gilt schließlich sogar \(P_FM_nP_F\ge P_{e_0}\), weil \(e_n\notin F\). Alle festen endlichen Kompressionen bestehen also den unteren Test, der volle Operator nicht. Das trennt die tatsächliche globale Hypothese scharf von einem finite-block-Ersatz.

### B. Nur schwache Konvergenz der unteren Rieszrichtung

Setze \(\nu_n=e_0+e_n\) und \(M_n=|\nu_n\rangle\langle\nu_n|\). Dann gilt die Unterordnung mit Gleichheit, \(\nu_n\rightharpoonup e_0\), und auf \(c_{00}\) dieselbe scharfe Energieasymptotik. Aber
\[
M_n^{1/2}e_0=(e_0+e_n)/\sqrt2
\]
konvergiert nicht stark gegen \(e_0\). Normkonvergenz der Richtung, nicht nur schwache Konvergenz, ist wesentlich. Durch Addition von \(n^{-2}I\) kann man die Metriken invertierbar machen, ohne den Gegenbefund zu ändern.

### C. Scharfe Sättigung durch bloße Größenordnung ersetzt

Für \(n\ge2\) setze auf \(\operatorname{span}\{e_0,e_n\}\)
\[
T_n=\begin{pmatrix}2&1\\1&n\end{pmatrix},\qquad M_n=T_n^2,
\]
und auf dem Rest \(T_n=n^{-2}I\). Dann
\[
M_n-P_{e_0}
=\begin{pmatrix}4&n+2\\n+2&n^2+1\end{pmatrix}\ge0,
\]
denn die Determinante ist \(3n^2-4n>0\). Doch
\[
T_ne_0=2e_0+e_n,\qquad
\langle M_nf,f\rangle\to5|\langle f,e_0\rangle|^2
\quad(f\in c_{00}).
\]
Tangentiale feste Kernenergien verschwinden, die Normrichtung im Unterbau ist exakt, aber die führende Energie sättigt den Unterbau nicht. Es bleibt Normflucht. Ein \(\asymp\)-Satz würde nicht reichen.

### D. Keine Erweiterung der Wurzelkonvergenz auf ganz \(H\)

Setze
\[
M_n=P_{e_0}+n^4P_{e_n}+n^{-2}I.
\]
Alle N11-Annahmen gelten auf \(c_{00}\), die Wurzelkonvergenz dort ist richtig. Für den festen Hilbertvektor \(h=\sum_{k\ge1}k^{-1}e_k\) gilt jedoch
\[
\|M_n^{1/2}h\|\ge\frac{\sqrt{n^4+n^{-2}}}{n}\sim n.
\]
Dies zerstört eine unzulässige Dichte-Erweiterung von N11 auf ganz \(H\), nicht N16, dessen letzter Schritt die normbeschränkten Isometrien benutzt.

### E. Normalanker allein erzwingt kein tangentiales C6

Man kann blockdiagonale positive Metriken mit \(C_S(U)=\lambda_UP_{e_0}\oplus B_U\oplus I\) wählen, wobei \(B_U\) auf einem festen tangentialen Zweierblock zwischen \(I\) und \(\begin{pmatrix}2&1\\1&2\end{pmatrix}\) wechselt. Wähle dort \(J=\operatorname{diag}(2,1)\), auf der Normalgeraden \(J=1\), und setze \(C_R(U)=J^*C_S(U)J\).

Dann gelten die exakte Pullbackidentität, Isometrie und sämtliche normal skalierten N11-Eingänge; sogar \(W_Ue_0=e_0\) exakt. Auf dem Zweierblock ist \(W_U\) aber abwechselnd \(I\) bzw. der nichttriviale Polarfaktor von \(B_U^{1/2}J\). Er konvergiert nicht. Zusätzliche orthogonale Zielkopien liefern bei Bedarf eine echte nichtsurjektive Einbettung. Dieses Modell belegt, warum der R42-/Mosco-Tangentialeingang im vollen C6-Satz separat benannt werden muss.

Die rationalen 2×2-Prüfungen und die lokale Rand-Sprungrechnung sind als Begleitdaten gespeichert; die Beweiskraft liegt in den obigen unendlichdimensionalen Familien, nicht in endlichen numerischen Experimenten. ([Gegenmodellprüfungen](c6_root_anchor_countermodel_checks.json); [Randstellenprüfung](c6_root_anchor_endpoint_check.json))

## 11. Exakt neu geschlossen versus weiterhin bedingt

### Mathematisch geschlossene neue Aussage

Unter den in §§3–5 ausgeschriebenen P11-Normierungs- und m=0-Quelleneingängen gilt für jedes **feste** \(0<R<S\)
\[
\boxed{W_{R,S}^{[U]}e_R\to e_S\quad(U\to\infty).}
\]
Daraus folgen ohne GC-AC
\[
b_U=\langle W_Ue_R,e_S\rangle\to1,\qquad
\|(I-|e_S\rangle\langle e_S|)W_Ue_R\|\to0,
\qquad \sup_{m\ge1}q_m(U)\to0.
\]
Die Orientierung ist positiv festgelegt. Keine terminale Stetigkeit, kein Nullstellenverbot für eine skalare Phase und kein positives Variationsbudget wird gebraucht.

### Zusätzlich aus R42 bzw. R27-Mosco

Wenn der separat ausgewiesene tangentiale Eingang gilt, folgt auf dem gesamten **ungeraden** festen Graphraum
\[
\boxed{
W_{R,S}^{[U]}(v+ae_R)
\longrightarrow
\Lambda_S^{1/2}J\Lambda_R^{-1/2}v+ae_S,
\qquad v\in H_R^0.
}
\]
Das ist ein starker Isometriegrenztransport. Es folgt auch
\[
L_{R,S}^{T,U}\to1\qquad(T,U\to\infty),
\]
mit der N20-basierten Kreuzterminalabschätzung des Kandidaten. Für eine Aussage über beide Paritätssektoren muss der bereits vorhandene gerade Grenztransport separat hinzugefügt werden; er war nicht Gegenstand dieses Reviews.

### Nicht geschlossen / nicht behauptet

- Keine Operatornormkonvergenz von \(M_U\) oder \(W_U\), keine Wurzel-SOT auf ganz \(H\) aus N11 allein.
- Keine summierbare positive Gesamtvariation, kein FD23-/J12–J15-Budget und keine gemeinsame COND-Uniformität.
- Keine neue vollständige Zertifizierung von R16/R17/R27 durch bloßes Zitieren der Registry.
- Keine R37-/G4c-, Objekt-X-, Seal-, SYN- oder RH-Folgerung.

## 12. Empfohlene minimale Überarbeitung vor einer Ankündigung

1. **N11 und N16 beibehalten.** Die neuen logischen Schritte sind korrekt.
2. **S2 auf m=0 plus Parallelogramm reduzieren.** Das entfernt unnötige höhere Jetabhängigkeiten.
3. **Die falsche globale Lipschitzbehauptung im vorgelagerten 6.1-Beweis nicht stillschweigend übergehen.** Die Hölder-Reparatur aus §8.2 explizit als geprüfte Ergänzung führen; für einen neu beanspruchten vollständigen R27-End-to-End-Abschluss die absolute lokale Randreparatur separat ausarbeiten.
4. **„Finite-source error bound“ als endlich viele feste Quelltests, nicht als effektives numerisches Zertifikat bezeichnen.**
5. **Schlussformulierung trennen:** Normal-No-escape und positive Orientierung ohne GC-AC; voller ungerader C6-Transport zusätzlich mit R42-Tangential-/R27-Mosco-Eingang.

**Gesamtfazit:** Der Versuch, das neue Wurzelankerlemma zu zerstören, scheitert aus einem positiven Grund: sein Beweis ist vollständig. Der destruktive Quellenreview findet jedoch eine echte, lokal reparierbare Randregularitätslücke im älteren Beweis der scharfen Energie. Sie darf bei einer behaupteten lückenlosen Gesamtquellenzertifizierung nicht verschwinden. Nach der angegebenen m=0-Reparatur bleibt kein neuer normaler No-escape-Gate übrig; der separat ausgewiesene tangentiale Quellenstack und sein Reviewstatus bleiben sauber zu benennen.

## 13. Nachprüfung der neuen kanonischen Fassung PA1–PA19

Auf zusätzliche Anforderung wurde auch `audits/P11_R43_POSITIVE_ROOT_ANCHOR_STRONG_TERMINAL_2026-09-07.md` vollständig gelesen, einschließlich der m=0-Parallelogrammreduktion und des Gegenmodells. **Exakt geprüfter Git-Blob:** `d6489e38e82185406eb41b9464eb72ff18dfde71`. Dieser Blob ist nicht Bestandteil des gepinnten Basiscommits, sondern die während der Prüfung vom Hauptagenten angelegte lokale Kandidatenfassung. Der Reviewer selbst hat keine Repositorydatei verändert.

### Ergebnis pro Gleichungsgruppe

| Gruppe | Urteil |
|---|---|
| PA3–PA5, PA13 | Die beabsichtigten P11-Identitäten und die Normierung sind korrekt. Die unten benannte pauschale Adjunktionskonvention muss eingeschränkt werden. |
| PA6 | Korrekte Verwendung des m=0-Satzes. Die upstream-Lipschitzlücke aus §8 dieses Reviews bleibt auch für diesen exakten Kandidaten relevant. |
| PA7 | Exakte Parallelogrammreduktion; keine höhere Jetvollständigkeit benötigt. |
| PA8–PA12 | Abstraktes Lemma und Beweis korrekt, einschließlich komplexer Phase und ganzer reeller Parameterfamilie. |
| PA14–PA16 | Starke Wurzelanker und exakte Übertragung durch die Isometrie korrekt. |
| PA17–PA18 | Für die benannten tiefen Tangentialflaggen korrekt; zur Vermeidung eines Indexmissverständnisses überall \(m\ge1\) ausdrücklich schreiben. |
| PA1, PA19 | Normal-No-escape und gemeinsamer Kreuzterminal-Cauchytest korrekt unter den P11-Quelleneingängen. |
| PA2 | Korrekt mit dem ausdrücklich separat importierten R42.51; kein GC-AC-Eingang. |
| Gegenmodell, Zeilen 300–323 | Richtig auf \(\ell^2\); die fehlende globale Unterordnung wird genau identifiziert. |

Die Gleichungsnummern und Zeilen dieser Tabelle beziehen sich auf die [exakt geprüfte lokale Fassung](r43_global_budget_55a3/audits/P11_R43_POSITIVE_ROOT_ANCHOR_STRONG_TERMINAL_2026-09-07.md), Blob `d6489e38e82185406eb41b9464eb72ff18dfde71`.

### Zusätzlicher konkreter Typisierungsfehler in dieser Fassung

Zeilen 55–56 sagen:

> „Alle Adjunktionen im Folgenden sind Adjunktionen der jeweils festen Graph-Hilberträume.“

Das ist **wörtlich zu weit und für PA4–PA5 falsch**. Die Adjunktionen von \(J\), \(G\), \(W\) und die Rieszabbildung erfolgen in den festen Graph-Hilberträumen. Dagegen bleiben \(H_U^*\), \(R_U^*\), \(\mathcal A_U=I+R_U^*R_U\), \(\ell_{X,U}\) und \(d_U\) die ursprünglichen terminalen **\(L^2\)-** bzw. Restzielraumobjekte. Eine Umdeutung von \(R_U^*\) oder \(d_U\) als Graphadjunktion/Graphskalarprodukt würde die zitierte Quellenschranke und \(d_U=2U+O(1)\) nicht mehr wiedergeben. ([Exakte Kandidatenfassung, Zeilen 55–71](r43_global_budget_55a3/audits/P11_R43_POSITIVE_ROOT_ANCHOR_STRONG_TERMINAL_2026-09-07.md); [P11, ursprüngliche Hub-/Rest- und Schurdefinitionen](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L168-L253))

**Präziser Ersatz:**

> „Die Adjunktionen von \(J\), \(G\) und \(W\), ihre positiven Wurzeln und die Rieszvektoren beziehen sich auf die jeweils festen ursprünglichen Graph-Hilberträume. Die terminalen Hub-/Restoperatoren \(H_U,R_U\), ihre Adjunktionen sowie \(\ell_{X,U}\), \(d_U\) und \(\mathcal A_U\) behalten ihre ursprünglichen P11-\(L^2\)- bzw. Restzielraumkonventionen.“

Zusätzlich sollten die Skalarprodukte bei \(\ell_{X,U}\) und \(d_U\) mit \(L^2(-U,U)\) gekennzeichnet werden. Das korrigiert die Deklaration, nicht den mathematisch beabsichtigten Wurzelankerbeweis.

### Regressionscode

Der separat gelesene und ausgeführte Code `scripts/check_r43_positive_root_anchor.py` meldet **110 bestandene algebraische Prüfungen**; darunter reelle/komplexe endliche Modelle, Pullback-/Isometrieidentitäten, Wurzelunterordnung, der Übertragungsfehler und das entworfene Fluchtgegenmodell. Die dort geprüften ursprünglichen fünf Quellenblobs stimmen mit dem Basiscommit überein. Dies ist nur eine algebraische Regression und ausdrücklich weder eine P11-Unendlichkeitshorizontrechnung noch ein Beweiszertifikat. ([Gespeichertes Regressionsprotokoll](c6_root_anchor_canonical_regression.json))

**Exact-Blob-Votum:** PA8/PA16 **mathematisches PASS**. Für eine wörtlich typkorrekte, lückenlos quellengeprüfte kanonische Fassung **zwei klar benannte Korrekturen vor Freigabe**: die Adjunktionsdeklaration einschränken und die upstream-Rand-Lipschitzpassage durch eine gültige m=0-Quadraturbegründung ergänzen bzw. deren vorhandene Reparatur explizit zum Eingangsrahmen machen. Kein Gegenbeispiel gegen den neuen Satz unter seinen tatsächlichen Hypothesen gefunden; diese Hypothesen erzwingen den Satz durch den bewiesenen Mechanismus.

## 14. Vertiefte Zusatzprüfung: starke punktweise BV-Reparatur für R16 **und** R17

**Aktualisierung gegenüber §8:** Dort wurde nur die grobe relative Hölder-Reparatur vollständig gebucht und die absolute R16-Reparatur als präzise Route benannt. Auf zusätzliche Anforderung wurden jetzt die stärkeren vorgeschlagenen BV-Reparaturen vollständig gelesen und unabhängig nachgerechnet. **Die starke Schranke besteht den mathematischen Review.** Wichtig ist noch eine zusätzliche Endpunktpräzisierung für R17s *zweite* Absorption, die unten ausdrücklich bewiesen wird. ([Zusatzkandidat S11–S13](c6_m0_source_deep_review.md#8-zusätzliche-scharfe-reparatur-der-ursprünglichen-kurzintervall-quadratur); [zweite Quellenprüfung, §5](c6_root_anchor_source_review.md#5-härtung-des-alten-scharfen-full-rest-oberbeweises))

### 14.1 Zulässiges Fehlermaß und seine gewichtete kumulative Schranke

Behalte die ursprünglichen Kurzintervallzellen und unveränderten positiven Gewichte:
\[
\delta_I=|I|\asymp e^{-4(T-r_I)/5},\qquad
\sum_{q:r_q\in I}\lambda_q^{(I)}=\delta_I.
\]
Für das signierte Fehlermaß
\[
\eta_T=\sum_{I,q\in I}\lambda_q^{(I)}\delta_{r_q}-dr
\]
verschwindet die Masse auf jeder Zelle exakt. Die kumulative Fehlerfunktion \(D_T\) verschwindet daher an konsistent zugeordneten Zellrändern und erfüllt
\[
|D_T(r)|\le 2\delta_I\le C e^{-4T/5+4r/5},\qquad r\in I.
\tag{BV1}
\]
Tatsächlich genügt der Faktor eins bei der üblichen rechtsgeschlossenen Zellkonvention. Es werden nur Positivität, exakte Zellmasse und die bereits vorhandene Zellbreitenskala gebraucht; keine zusätzliche Primzahlkorrelation und keine Fourierauslöschung. Die ursprüngliche Kurzintervall-PNT bleibt ein unveränderter arithmetischer Quelleneingang. ([P11, (6.18)–(6.20)](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex#L232-L270))

Endzellen können zusammengelegt oder außerhalb des tatsächlichen Feldträgers vollständig gewählt werden, sodass keine degenerierende Restzelle eine untere Primzahlmassenschranke vortäuscht. Wegen \(\alpha\in C_c^\infty(0,\varepsilon)\) ist der Feldträger von den äußeren Grenzen des benutzten Bereichs \([0,(T+\varepsilon)/2]\) getrennt. Die modifizierten Randzellen behalten dieselbe Vergleichsskala.

### 14.2 Der gültige **skalare** BV-Schritt

Schreibe \(m_T=K_T/T\), \(F_T=(k_T-m_T)1_{(0,T)}\). Für fast jedes feste \(v\in(0,T)\) gilt
\[
\Phi_T(r)(v)=2F_T(v)\alpha(2r-v)-2\alpha(v)F_T(2r-v).
\]
Diese Funktion ist als Funktion **des skalaren Parameters \(r\), bei festem \(v\)** von beschränkter Variation. Ihre reguläre Ableitung ist
\[
4F_T(v)\alpha'(2r-v)
-4\alpha(v)k_T'(2r-v)1_{0<2r-v<T}.
\tag{BV2}
\]
Hinzu kommen die Sprünge
\[
-2\alpha(v)F_T(0+)\quad\text{bei }r=v/2,\qquad
+2\alpha(v)F_T(T-)\quad\text{bei }r=(T+v)/2.
\tag{BV3}
\]
Damit liefert skalare partielle Integration gegen \(D_T\) punktweise
\[
\begin{aligned}
|Z_T(v)|\le{}&
4|F_T(v)|\int |D_T(r)|\,|\alpha'(2r-v)|\,dr\\
&+4|\alpha(v)|\int_{0<2r-v<T}|D_T(r)|\,|k_T'(2r-v)|\,dr\\
&+2|\alpha(v)|\bigl(
|F_T(0+)|\,|D_T(v/2)|
+|F_T(T-)|\,|D_T((T+v)/2)|\bigr).
\end{aligned}
\tag{BV4}
\]
Das ist gerade die Rechnung, die der falschen globalen Hilbert-Lipschitzbehauptung fehlte. **Keine Hilbert-BV-Eigenschaft von \(r\mapsto\Phi_T(r)\) wird behauptet.** Treffen Primatome genau auf eine bewegte Sprungstelle, betrifft dies für festes \(T\) nur endlich viele \(v\), also eine \(L^2\)-Nullmenge; damit entsteht keine Wahlabhängigkeit der \(L^2\)-Repräsentanten. Die Endpunktformel folgt direkt aus den ursprünglichen Definitionen. ([P11, (6.13), (6.16), (6.21a)](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex#L166-L295))

### 14.3 Alle vier Beiträge separat gerechnet

Für die ursprünglichen wachsenden glatten Kerne verwenden wir die schwächere, aber ausreichende Hülle
\[
|k_T(t)|+|k_T'(t)|\le C_f e^{(T-t)/2},
\qquad k_T(T-)=0.
\]
Der letztere Randwert folgt aus dem festen Abstand \(a_*-\rho_f>2\varepsilon\); die Quellschranke ist also auch für die uniforme feste glatte R16-Familie zulässig. ([P11, (6.9)–(6.10)](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex#L94-L145); [R16, feste glatte Familie und uniformer Kern](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R16_TC1_NEARNULL_REMAINDER_2026-08-14.md#L57-L76))

1. **Erster regulärer Beitrag.** Auf dem Träger von \(\alpha'(2r-v)\) ist \(r=(v+s)/2\), \(s\in(0,\varepsilon)\). Deshalb ist er punktweise höchstens
   \[
   C e^{-4T/5+2v/5}|F_T(v)|
   \le C_f e^{-3T/10-v/10}
   +C|m_T|e^{-4T/5+2v/5}.
   \]
   Die \(L^2(0,T)\)-Norm beträgt höchstens
   \[
   C_f e^{-3T/10}+C|m_T|e^{-2T/5}.
   \]
   Hier fällt **kein \(\sqrt T\)** an: \(\int_0^T e^{-v/5}dv\) ist beschränkt und \(\int_0^T e^{4v/5}dv=O(e^{4T/5})\).

2. **Zweiter regulärer Beitrag.** Substitution \(t=2r-v\) und \(v\in\operatorname{supp}\alpha\) geben
   \[
   C|\alpha(v)|e^{-4T/5+2v/5}
   \int_0^T e^{2t/5}|k_T'(t)|dt
   \le C_f|\alpha(v)|e^{-3T/10+2v/5}.
   \]
   Denn der verbleibende Integralexponent ist \(-t/10\). Seine \(L^2_v\)-Norm ist \(O_f(e^{-3T/10})\).

3. **Unterer Sprung.** Auf dem festen Träger von \(\alpha\) gilt
   \[
   |D_T(v/2)|\le Ce^{-4T/5},\quad
   |F_T(0+)|\le C_fe^{T/2}+|m_T|.
   \]
   Somit ist seine \(L^2\)-Norm höchstens
   \[
   C_fe^{-3T/10}+C|m_T|e^{-4T/5}.
   \]

4. **Oberer Sprung.** Da \(F_T(T-)=-m_T\) und
   \[
   |D_T((T+v)/2)|\le Ce^{-2T/5},
   \]
   ist seine Norm höchstens \(C|m_T|e^{-2T/5}\).

Zusammen folgt die gewünschte starke Reparatur exakt in der vorgeschlagenen Skala:
\[
\boxed{\|Z_T^{\rm quad}\|_2
\le C_fe^{-3T/10}
+C\frac{|K_T|}{T}e^{-2T/5}.}
\tag{BV5}
\]
Die Konstanten hängen nur von den festen gemeinsamen glatten Schranken, dem inneren Trägerabstand und \(\alpha\) ab, nicht von \(T\).

### 14.4 Relative m=0- und absolute R16-Folgerung

Für m=0 ist \(|K_T|\asymp_f e^{T/2}/\sqrt T\) und \(\sqrt{M_T}=|K_T|/\sqrt{2T}\). Der Quotient des zweiten Terms aus BV5 durch \(\sqrt{M_T}\) beträgt \(O(T^{-1/2}e^{-2T/5})\); der erste Quotient ist \(O_f(Te^{-4T/5})\). Also bleibt der scharfe obere Koeffizient eins erhalten. ([P11, (6.12)–(6.14)](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex#L154-L187))

Für die R16-Familie gilt dagegen \(|K_T|=O(\sqrt T)\) bei uniformen glatten Konstanten. BV5 liefert somit **absolute**
\[
\|Z_T^{\rm quad}\|_2
\le Ce^{-3T/10}+CT^{-1/2}e^{-2T/5}\to0.
\tag{BV6}
\]
Das repariert konkret R16.7 und damit den entsprechenden Eingang R17.5. Die zugehörigen diskreten Zertifikatskosten lassen sich unabhängig von irgendeiner Hilbert-Lipschitzannahme durch die punktweise Kernhülle und positive Zellmassen kontrollieren; sie bleiben \(O(T^{-1})\). Der vollständige höhere-Potenz-Lift bleibt unverändert mit Norm \(O(\sqrt{T+1}e^{-T/2})\). ([R16, (R16.2), (R16.6)–(R16.8)](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R16_TC1_NEARNULL_REMAINDER_2026-08-14.md#L95-L167))

### 14.5 Zusätzlicher R17-Punkt: \(k_g(T-)\) ist **nicht** null

**Ein zusätzlich zu korrigierender tatsächlicher Quellensatz:** R17 behauptet für die zweite Absorption eines festen geraden glatten mittelwertfreien \(g\) wieder eine uniforme Quellenfeldableitung. Dabei ist
\[
k_g^{(T)}(t)=2g(T-t),\quad K_T=0,\quad
k_g^{(T)}(0+)=0,\quad k_g^{(T)}(T-)=2g(0).
\]
Der letzte Wert muss nicht null sein. Daher darf man BV5s **spezialisierte** Randgröße \(|K_T|/T\) nicht ungeprüft auf diesen Kern übertragen: sonst verschwände fälschlich der obere Sprung. Die globale Hilbert-Lipschitzbegründung ist auch hier falsch, wenn \(g(0)\ne0\). ([R17, Zeilen 142–165](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R17_VANISHING_NEARNULL_CORE_2026-08-14.md#L142-L165); [eingebundener P11-Beweis, Zeilen 125–141](r43_global_budget_55a3/papers/P11_sections/P11_O3p_Vanishing_NearNull_Core.tex))

**Die allgemeine Formel BV4 repariert aber auch diesen Fall vollständig.** Wähle \(L\) mit \(\operatorname{supp}g\subset[-L,L]\).

- Der erste reguläre Term hat \(v\in[T-L,T]\), beschränkte Amplitude und dort Zellgewicht \(O_g(e^{-2T/5})\).
- Im zweiten regulären Term liegt \(t\in[T-L,T]\); das gewichtete Integral hat dieselbe Größe \(O_g(e^{-2T/5})\).
- Der untere Sprung verschwindet für große \(T\).
- Der obere Sprung hat die Größe \(O_g(|g(0)|e^{-2T/5})\), nicht null.

Damit
\[
\boxed{\|Z_{T,g}^{\rm quad}\|_2\le C_g e^{-2T/5}\to0.}
\tag{BV7}
\]
Auch hier sind Kosten \(O_g(e^{-T/2})\) und vollständiger Lift unverändert. Die zweite Absorption R17.11 ist somit erhalten, einschließlich des zuvor unterschlagenen oberen Endpunkts. **Empfohlene Quellenergänzung:** Die allgemeine BV4 in den kanonischen Quadraturbaustein aufnehmen und im R17-Absorptionslemma explizit auf BV7 verweisen; nicht allein die Spezialform BV5 zitieren.

### 14.6 Anschluss an R27 und R42; präziser neuer Gesamtstatus

Die zusätzlich gelesenen R17-Abschnitte 1–4 verwenden außer den so reparierten beiden Absorptionsschritten absolute \(L^1\cap L^2\)-Summierbarkeit der höheren Potenzkoeffizienten, exakte Nullmittelwerte vollständiger Translationsdifferenzen und die Reihenfolge „erst festen glatten Approximanten wählen, dann \(T\to\infty\), dann Approximationsfehler gegen null“. In diesen Anschlüssen fand sich kein weiterer Fehler; insbesondere folgt \(K_T\to0\) aus echter \(L^1\)-Konvergenz, nicht aus einer unzulässigen Paarung mit wachsenden Konstantenvektoren. R27s Recovery baut dann genau auf diesem R17-Ergebnis auf. ([R17, §§1–4](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R17_VANISHING_NEARNULL_CORE_2026-08-14.md#L43-L229); [R27, Recovery und Diagonalisierung](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R27_CONSTRAINED_GAMMA_MOSCO_LIMIT_2026-08-15.md#L218-L268))

**Aktualisiertes mathematisches Votum:** Der entdeckte Randregularitätsfehler ist durch BV1–BV7 auf **beiden** nötigen Fehlerskalen repariert, einschließlich R17s zweiter Absorption. Nach expliziter Aufnahme dieser Reparatur und der in §13 benannten Typisierungs-/Indexpräzisierungen fand dieser destruktive Review keinen verbleibenden neuen mathematischen Blocker für den positiven Wurzelanker und seinen fixed-pair **ungeraden** C6-Anschluss über R27/R42. Die P11-Graph-/Vollrestkonstruktion und der angegebene Kurzintervall-PNT-Eingang bleiben explizite vorgelagerte Quellen; kein umfassendes externes Neu-Zertifikat sämtlicher arithmetischer Grundlagen wird behauptet. Der **unveränderte Pintext** bleibt hinsichtlich der genannten Lipschitzsätze falsch; das darf nicht nachträglich als fehlerfreier früherer Stand bezeichnet werden.

## 15. Exact-File-Prüfung des anschließend tatsächlich implementierten Pakets

Auf erneute Anforderung wurden die aktuelle PA-Fassung, der vollständige QR-Audit und der tatsächliche TeX-Diff zum Ausgangspin nochmals gelesen. Es handelt sich um folgende **exakten geprüften Blobs**, nicht mehr um die ursprüngliche PA-Fassung aus §13:

| Datei / Objekt | Geprüfter Git-Blob | Urteil |
|---|---|---|
| PA1–PA19, neue kanonische Wurzelankerfassung | `53dbdbc1b540f8c750da4876823d02f157b2ffe9` | Mathematischer Kern PASS; Reparaturabhängigkeit und \(m\ge1\) jetzt ausdrücklich richtig. Pauschale Adjunktionsdeklaration noch zu korrigieren. |
| QR1–QR5, implementierter Randspur-Audit | `300001d99259f3dbb5fd2c18155adb92cf4c551c` | PASS für die behauptete relative P11- und absolute R16-Reparatur. |
| TeX-Vollbeweis, tatsächlich gepatchter Step 5 | `6df7308cf269f09c6564ab162ed9b647cb3929da` | PASS des Diffs: reguläre Ableitung, kumulatives Fehlermaß, beide Endpunktspuren, scharfe Fehlerbilanz und Kostenhülle sind gültig. |

Die Dateien sind [PA-Kandidat](r43_global_budget_55a3/audits/P11_R43_POSITIVE_ROOT_ANCHOR_STRONG_TERMINAL_2026-09-07.md), [QR-Audit](r43_global_budget_55a3/audits/P11_R43_QUADRATURE_BOUNDARY_TRACE_REPAIR_2026-09-07.md) und [lokaler TeX-Vollbeweis](r43_global_budget_55a3/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex). Der Hauptagent, nicht der Reviewer, hat diese lokalen Änderungen vorgenommen; es wurde nichts veröffentlicht.

### Noch offene **Textkorrekturen** dieses genauen Paketstands

1. **PA, jetzt Zeilen 60–61:** Die pauschale Aussage „Alle Adjunktionen … Graph-Hilberträume“ ist unverändert zu weit. Der Ersatz aus §13 trennt die Graphadjunktionen von den ursprünglichen terminalen \(L^2\)-Hub-/Restadjunktionen; die Definitionsskalarprodukte von \(d_U,\ell_{X,U}\) sollten entsprechend gekennzeichnet werden.

2. **R17s zweites Absorptionslemma:** Das TeX-Paket korrigiert jetzt den wachsenden P11-Kern und seine R16-Near-null-Familie. Die weiterhin vorhandene globale Quellenfeldableitungsbehauptung in `P11_O3p_Vanishing_NearNull_Core.tex`, Zeilen 136–141, hat zusätzlich den oberen Sprung \(2g(0)\), auch wenn \(K_T=0\). **Die neu implementierte allgemeine Spurformel (6.21e)/QR3 reicht zur Reparatur aus**, aber ihr Einsatz muss dort explizit gemacht werden. Sie gibt genau BV7 aus §14.5, also \(O_g(e^{-2T/5})\). Das ist keine zusätzliche Hypothese und kein Gegenbeispiel gegen R17; es ist ein noch nicht ersetzter falscher Begründungssatz im eingebundenen Text.

**Präziser vorgeschlagener Ersatz für R17, englisch entsprechend dem TeX-Kontext:**

> “The zero extension of \(k_g^{(U)}\) may jump at \(t=U\), with trace \(k_g^{(U)}(U-)=2g(0)\); therefore no global Hilbert-space derivative assertion is used. Apply the scalar cumulative-error and endpoint-trace estimate (6.21d–e). The regular terms are supported where \(t\) or \(v\) lies in \([U-L,U]\), and the upper jump is weighted by \(O_g(e^{-2U/5})\). The lower trace vanishes for large \(U\). Consequently the quadrature source error is \(O_g(e^{-2U/5})\to0\); the certificate cost and the full-rest lift are unchanged.”

**Freigabestatus dieses genauen Stands:** Das neue Wurzelankerlemma, seine Anwendung, QR1–QR5 und der implementierte Step-5-Diff sind mathematisch bestätigt. Die feste ungerade C6-Folgerung ist korrekt mit dem ausgewiesenen R42.51; zur Aussage „der eingebundene gesamte betroffene Quellenpfad ist textlich repariert“ fehlen noch genau die beiden vorstehenden Präzisierungen. Die zweite ist durch BV7 bereits vollständig analytisch aufgelöst. Kein Anspruch auf Operatornormkonvergenz, Uniformität in \(R,S\), Variationssummation, vollständiges Objekt X oder RH.

## 16. Letzter Folgecheck: R16 und R17 jetzt tatsächlich korrekt implementiert

Der Hauptagent hat anschließend auch beide eingebundenen Folgebeweise korrigiert. Die **vollständigen tatsächlichen Diffs** wurden gelesen und gegen die unabhängige Rechnung in §14 geprüft; sie bestehen den Review.

| Neu geprüfte Datei | Git-Blob | Urteil |
|---|---|---|
| QR-Audit einschließlich des R17-Festprofilabsatzes | `08936b6ed315510a606986f96802b1e914b385be` | PASS; ersetzt den in §15 aufgeführten früheren QR-Blob. |
| `P11_O3o_TC1_NearNull_Remainder_Collapse.tex` | `741124dd8dbab29452b24ca9af5d4be5dd7a8f67` | PASS; benutzt die richtige absolute Spurformel mit \(K_U=O(\sqrt U)\). |
| `P11_O3p_Vanishing_NearNull_Core.tex` | `1fb4217407e68ac3e2be3d2259ccd97ef450a40d` | PASS; behält \(k_g^{(U)}(U-)=2g(0)\), kontrolliert regulären Teil und oberen Sprung jeweils durch \(O_g(e^{-2U/5})\). |

Der [aktuelle QR-Audit](r43_global_budget_55a3/audits/P11_R43_QUADRATURE_BOUNDARY_TRACE_REPAIR_2026-09-07.md), die [R16-Folgekorrektur](r43_global_budget_55a3/papers/P11_sections/P11_O3o_TC1_NearNull_Remainder_Collapse.tex) und die [R17-Folgekorrektur](r43_global_budget_55a3/papers/P11_sections/P11_O3p_Vanishing_NearNull_Core.tex) implementieren damit genau die oben als notwendig benannte Fortführung; weder der konstante Abzug noch die zusätzliche R17-Spur wurden fallengelassen.

Die bereits geprüften weiteren Paketblobs bleiben:

- PA1–PA19: `53dbdbc1b540f8c750da4876823d02f157b2ffe9`.
- P11 Vollbeweis/Step 5: `6df7308cf269f09c6564ab162ed9b647cb3929da`.

**Konkretes Abschlussvotum: mathematisches GREEN für den Wurzelanker, die vollständige implementierte Randspur-Reparatur auf den drei betroffenen TeX-Pfaden und den fixed-pair ungeraden C6-Schluss im ausdrücklich ausgewiesenen P11/R27/R42-Rahmen.** Der zusätzliche R17-Blocker aus §15 ist jetzt erledigt. **Vor wörtlicher Textfreigabe nur noch PA, Zeilen 60–61, auf die tatsächlichen Graphadjunktionen einschränken und die terminalen \(L^2\)-Objekte ausnehmen**; der genaue Ersatz steht in §13. Dies ist eine lokale Typisierungskorrektur, kein neuer analytischer Eingang und keine Widerlegung des beabsichtigten Arguments.

Der frühere Pintext enthielt echte Fehler; der korrigierte lokale Stand bewahrt die benötigten Resultate durch die jetzt explizit geprüfte Reparatur. Kein öffentlicher Commit, keine Registry-Promotion und keine Repositoryänderung durch diesen Reviewer.


## 17. Abschließende Provenienz: letzte PA-Typisierungspräzisierung erledigt

Die ersten 82 Zeilen der finalen PA-Fassung und der **vollständige Diff** zur zuvor geprüften Fassung wurden gelesen. Der Diff ersetzt ausschließlich die beiden zu weit gefassten Graphadjunktionszeilen durch sechs deklarative Zeilen: Quellmetriken und J-Adjunktionen im festen Graphraum; terminale H-/R-/A-Operatoren sowie d-/ell-Paarungen mit ihren ursprünglichen L²-/Restzielraumkonventionen. Kein anderer Beweisschritt oder Formelinhalt wurde verändert. ([Finale PA-Fassung](r43_global_budget_55a3/audits/P11_R43_POSITIVE_ROOT_ANCHOR_STRONG_TERMINAL_2026-09-07.md))

**Final geprüfter PA-Git-Blob:** `a3229f0882a31046434389e5915badea686dae73`. Die Typisierungsbeanstandung I2 ist damit **erledigt**. Die SHA-/Blobkontrolle bestätigt unverändert QR `08936b6ed315510a606986f96802b1e914b385be`, P11 `6df7308cf269f09c6564ab162ed9b647cb3929da`, R16 `741124dd8dbab29452b24ca9af5d4be5dd7a8f67`, R17 `1fb4217407e68ac3e2be3d2259ccd97ef450a40d`. ([Aktualisiertes Prüfprotokoll](c6_root_anchor_destructive_review.json))

**Endvotum: READY / SCOPED GREEN.** Keine verbleibende mathematische oder typisierende Beanstandung im ausdrücklich geprüften Paket. Der vorher bestätigte fixed-pair ungerade C6-Scope mit R42.51 bleibt unverändert; weder eine weitere Recherche noch eine erneute Vollpapieranalyse war für diesen rein deklarativen Abschlussdiff nötig. Dies ist keine Veröffentlichung oder Registry-Promotion.
