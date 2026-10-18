# Entscheidungsvorlage: U8, K und Schurvergleich

18. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Basis: `849e4d7f6a2bde34d83c4b1acc8dd2c8213c7b50`.
Alle mathematischen Aussagen sind bedingt auf die gebundenen Operator-,
Formdomänen-, Quellenmodell- und Integrationsvoraussetzungen.

## Entscheidung

**Genau ein Pilot wird ausgewählt: den alten Zwölfer-Untervergleich K im
geraden Fall durch K_star ersetzen und die Inversmajorante gemeinsam über
K_star, E_star, P_star und nu_star erneuern.**

\[
K_\ast=K+\frac{13}{10^8}G_F,
\qquad 0<K<K_\ast\preceq K_B:=(D-G^*U_8G)_{FF}.
\tag{1}
\]

Hier ist G_F die gebundene rationale Fehlermetrik des alten Zwölferblocks,
kein Einheitsoperator und kein neuer physischer Gram der Schalenrichtungen.
Die konkrete zulässige Verstärkung (1) ist bereits mit einer kleinen
gerichteten 12x12-Rechnung bestätigt. Ihre Energieauswirkung ist **noch nicht
berechnet**. Der eigentliche Pilot mit neuer P-Matrix und Fehlertransport
wird durch diese Entscheidungsvorlage nicht gestartet.

Das ist eine Änderung des Formuntervergleichs, keine weitere skalare
Young-Umgewichtung. U8, die äußere Antwortmatrix X0, die gerade Prüfrichtung
aus #238, die alten Galerkinantworten Z=J X_ans und alle Funktionen bleiben
fest. Der äußere Budgetwert K_P bleibt ebenfalls unverändert. K und K_P
sind verschiedene Objekte.

Meilenstein 4, beide Paritäten für einen späteren vollständigen Anschluss,
N12 insgesamt und die externe Prüfung bleiben offen.

## 1. Gemeinsame Entscheidungsgrundlage

Die abgeschlossene Majoranten-Vorprüfung zeigt gerade:

- Die echte skalare Verkleinerung bei gleichem Dualgewicht lässt noch einen
  Ausschlussabstand >4.13359e-6.
- Sogar der Hilfsuntervergleich mit P-Faktor 1 liegt >2.27301e-6 über K_P.
- Dieser zweite Befund schließt die damalige skalare Gewichtungsfamilie
  bei unveränderten U8,K,P und Quellenabbildungen aus. Er ist keine untere
  Grenze für die tatsächliche A9-Inverse und kein allgemeines Majoranten-No-Go.

Die gerade Modellenergie enthält etwa 2.897e-6 hohe U8-Energie,
8.589e-6 endliche U8-Energie, [3.994,4.117]e-6 Zwölferenergie und
4.506e-5 P-Energie mit Faktor 1.1. Große Beiträge oder Fehlerobergrenzen
allein beweisen keine verfügbare Einsparung. Alle Kandidaten müssen daher
an einer zulässigen **gemeinsamen** Formänderung gemessen werden.

## 2. Vergleich der drei Wege

| Weg | Bisherige Ungleichung und konkreter Ersatz | Quantitative Grundlage und offene Vermutung |
|---|---|---|
| U8 | A8^-1 <= U8(delta,F8). Eine konkrete erste Variante wäre delta=1.82198 statt 1.8219, mit dazu konsistent neu gebildeter endlicher Schuruntergrenze F8_star und neuer Inverskongruenz. Nicht nur delta in der Endformel austauschen. | Die bestehende volle Hochraumabschätzung erlaubt delta<1.821983999987. Allein die direkte hohe Modellenergie könnte dadurch höchstens ungefähr 1.336e-10 sinken; das ist keine Grenze für die gesamte gekoppelte Änderung. Ein ausreichender Gewinn über die endlichen/kohärenten Beiträge ist bislang unbelegt. |
| K, ausgewählt | Der bisherige globale 96-Quellenfehler gamma_96 G wird für die K-Untergrenze durch den vollständigen Fehler allein der zwölf F-Quellen ersetzt. Daraus folgt (1); die gesamte nachfolgende Schurkontrolle wird gemäß Abschnitt 4 angepasst. | gamma_96 etwa 4.34881736e-7, gerichteter gamma_F <3.04583464e-7. Die konkrete größere Untergrenze K_star ist bestätigt. Es ist noch nicht bewiesen, dass sie den geraden Energievergleich rettet. |
| Schur allein | H_*^-1 <= a beta^-1 R_L+b J P J* soll durch eine engere Kontrolle der vollständigen Inverse desselben H_* ersetzt werden; U8 und K bleiben fest. Ein möglicher Ansatz erhält in Woodbury Delta und R* S^-1 nu gemeinsam, statt sie durch skalare Preise zu trennen. | Für die skalare Familie besteht bereits das No-Go. Der große P-Beitrag ist kein Beleg für entsprechenden Überschätzungsfehler. Eine ausreichend kleinere zulässige Operatorobergrenze liegt nicht vor. Vor einer solchen Konstruktion ist ein endlicher variationaler Untertest besonders günstig. |

Für die U8-Zeile wird nur die unveränderte analytische Hochraumschranke
aus der Common96-Herleitung ausgeschöpft:

\[
\delta<\frac{1.822-16\cdot10^{-6}-12\cdot10^{-12}}{1+10^{-12}}.
\]

Die angegebene Energieeinsparung bezieht sich ausschließlich auf den
vorhandenen Modellterm ||y_h||²/delta. Sie weder begrenzt noch bestätigt
den Gewinn bei einer vollständigen U8-Änderung.

## 3. Warum der K-Schritt tatsächlich zulässig ist

Die [Common96-Herleitung, Abschnitt 5](../a9-inverse-renewal-2026-10-13/original/sources/COMMON96_HERLEITUNG.txt)
liefert für die vollständigen U8-Features der zwölf alten Quellen

\[
\delta\Psi_F^*\delta\Psi_F\preceq E_F,
\quad U_{0,F}=\Psi_{0,F}^*\Psi_{0,F},\quad G_F>0.
\]

E_F enthält auch den hohen Anteil; hier wird kein Fehler weggelassen.
Setze

\[
e_F^2=\operatorname{tr}(G_F^{-1}E_F),\quad
t_F=\operatorname{tr}(G_F^{-1}U_{0,F}),\quad
\gamma_F=2\sqrt{e_F^2t_F}+e_F^2.
\]

Aus dem Normdreieck für die G_F-normalisierten Features folgt die
vollständige gemeinsame Matrixschranke

\[
-\gamma_FG_F\preceq U_{FF}-U_{0,F}\preceq\gamma_FG_F.
\tag{2}
\]

Die Rechnung ergibt gamma_F ungefähr 3.045834639965036e-7 und bestätigt
gerichtet den rationalen Cap

\[
\bar\gamma_F=\frac{38072933}{125000000000000}
=3.045834640000000\cdot10^{-7}.
\]

Die gespeicherte direkte untere 96er-Matrix enthält bereits alle direkten
Zuschläge. Die neue Rechnung bestätigt mit zwölf strikt positiven
Intervall-LDL-Pivots

\[
D_{FF,\rm lower}-U_{0,F}-\bar\gamma_FG_F-K_\ast>0.
\tag{3}
\]

Zusammen mit (2) folgt (1). Die positive Definitheit von G_F wird separat
mit zwölf Pivots geprüft. Der kleinste Pivot von (3) liegt über
1.2668e-19 in den verwendeten Koordinaten; dies wird **nicht** als
physischer Koerzivitätsboden ausgegeben. K_star ist exakt durch (1)
definiert; der kanonische rationale Matrixdigest steht in `EXPECTED.json`.

Der relative Spurpreis der Erhöhung erfüllt

\[
\operatorname{tr}(K^{-1}(K_\ast-K))<1.279221\cdot10^{-6}.
\]

Das ist eine kleine, aber nachgewiesene Verstärkung des Untervergleichs.
Es ist weder die prozentuale Energieeinsparung noch eine Zusage, den
Ausschlussabstand zu überwinden. Die Schurabbildung kann solche Änderungen
anders gewichten; gerade deshalb wird die Wirkung gemeinsam geprüft.

**Wichtige Begrenzung:** Der kleinere gamma_F darf nur im F-F-Block benutzt
werden. Die Fehler der F-J-Kreuze, a_fin und der vollständigen 96er-Geometrie
werden nicht dadurch kleiner. Ihre bisherigen gemeinsamen Schranken bleiben
für den neuen Fehlertransport erhalten.

## 4. Gemeinsamer Anschluss ohne neue globale Restintegration

Die [Inversherleitung, Abschnitte 2 und 6](../a9-inverse-renewal-2026-10-13/original/HERLEITUNG.txt)
verwendet fest S, A_force=(a_low,a_fin), Z=J X_ans, M_upper und

\[
D_0=\operatorname{diag}((1-\rho)I_{191},K),\quad
E_0=D_0-M_{\rm upper}>0,\quad
R=A_{\rm force}^*-SZ.
\]

Bei festem U8 ist a_fin unverändert. Mit

\[
D_\ast=D_0+\operatorname{diag}(0_{191},K_\ast-K),\qquad
E_\ast=E_0+\operatorname{diag}(0_{191},K_\ast-K)
\tag{4}
\]

bleiben R und M unverändert. Daher wird aus der gebundenen vollständigen
Restschranke unmittelbar

\[
R^*R_LR\preceq c\beta E_0\preceq c\beta E_\ast.
\tag{5}
\]

Es werden keine neuen 203 Residualfunktionen integriert. Die alten
vollständigen Restbedingungen gelten weiter, einschließlich ihrer extern
offenen Voraussetzungen. Außerdem

\[
H_\ast^{\rm neu}=S-A_{\rm force}^*D_\ast^{-1}A_{\rm force}
\succeq H_\ast^{\rm alt}>0.
\]

Die neue endliche Korrektur ist zunächst exakt definiert durch

\[
P_\ast^{\rm exact}=X_{\rm ans}E_\ast^{-1}X_{\rm ans}^*.
\tag{6}
\]

Im Pilot wird eine rationale Obermatrix P_star durch den vollständigen
Schurblock [[E_star,X_ans*],[X_ans,P_star]] zertifiziert. Die exakte
Matrix (6) ist <= der alten exakten Matrix; daraus folgt ohne zusätzliche
Prüfung keine Ordnung zweier unabhängig gerundeter Obermatrizen.

Für die unveränderte physische Residualquelle f aus #238 gelten h und v
weiter wie bisher, aber

\[
\nu_\ast=f_T-g^*U_8h-a_{\rm fin}^*K_\ast^{-1}v.
\tag{7}
\]

Mit fest a=11/10 und b=1/(1-11c), c=1977/500000, liefert dieselbe gültige
Inversherleitung die neue vollständige Majorante

\[
\langle f,W_\ast f\rangle=
\langle h,U_8h\rangle+v^*K_\ast^{-1}v+
\frac a\beta\langle\nu_\ast,R_L\nu_\ast\rangle+
b(J^*\nu_\ast)^*P_\ast(J^*\nu_\ast),
\quad A_9^{-1}\preceq W_\ast.
\tag{8}
\]

Das Einsetzen von K_star bei unverändertem nu oder unverändert behandeltem
Schurblock wäre kein solcher Nachweis. In der vollständigen ursprünglichen
Quadratergänzung gilt vielmehr exakt

\[
Q_{\rm lower,new}=Q_{\rm lower,old}+(K_\ast-K)[z],
\quad
Q_{\rm lower,old}\preceq Q_{\rm lower,new}\preceq A_9.
\tag{9}
\]

Hier ist z die alte Zwölferkoordinate der A9-Zerlegung, nicht die neue
festgefrorene Schalenrichtung. Die exakte inverse Vergleichsform verbessert
sich also monoton. Ob auch die konkret konstruierte Obermajorante (8) den
benötigten gerichteten Gewinn liefert, bleibt der Pilotfrage vorbehalten.

## 5. Vorhandene und fehlende Daten

| Weg | Vorhandene gemeinsame Daten | Für den kleinsten Test fehlt | Für einen positiven vollständigen Nachweis fehlt |
|---|---|---|---|
| U8 | alter voller B-Gram, 191er F-/Kongruenzdaten, hohe Projektionen und gemeinsame Quellgrame; #238-Paarungen | neue zulässige endliche inverse Metrik; konsistente U8-Wirkungen und Fehler auf F,J,h; bewiesener Anschluss an die globale A9-Unterform | transportierte oder erneuerte vollständige Schur-/Restkontrolle; vollständige neue Dualenergie |
| K | D96-Unter-/Obermatrix, U96, G_F, E_F, a_fin-Modelle/Fehler, K, E0, X_ans, sämtliche Paarungen für f und der feste K_P-Wert | nur endliche neue Matrizen aus (4)–(6), nu_star und vollständig angepasste gewichtete Fehler; keine neuen Funktionspaarungen | vollständige R_L-Energie für das neue nu_star oder eine bewiesene obere Ersatzabschätzung; später weitere Richtungen und beide Paritäten |
| Schur allein | J*nu, gemeinsame D/U/a_fin-Daten; daraus H_*[J,J]; vollständige Positivität des alten H_* | für den variationalen Untertest eine feste 84er-Testspalte und bezahlte Paarungs-/Formfehler; keine neue Integration | für eine obere Inverse volle S- oder H_*-Antworten mit vollständigem Rest und gemeinsamer Kreuzkontrolle; endliche Galerkinwerte reichen nicht |

Die K-Variante benötigt keine zusätzliche Datenbeschaffung oder Integral-
auflösung. Die neue P-Star-Obermatrix und die tatsächliche Teilenergie sind
bewusst noch nicht berechnet. Datenverfügbarkeit ersetzt diese Prüfung nicht.

## 6. Kleinste aussagekräftige Tests und Auswahl

| Weg | Begrenzter erster Test | Erfolg / Abbruch |
|---|---|---|
| U8, nicht ausgewählt | Fester delta-Kandidat, ein 191er-Inversaufbau und gemeinsame Auswertung der vorhandenen F/J/h-Features; vor der Energieentscheidung den gültigen vollständigen A9-Anschluss nachweisen | Kein Energiefortschritt aus der bloßen Hochraumkonstante ableiten. Ohne gültigen gemeinsamen Anschluss oder ausreichenden gerichteten Gewinn stoppen; kein automatischer neuer Globalresiduallauf. |
| K, ausgewählt | Ein Kandidat (1), ein gerader Zeuge, ein neuer endlicher Schur-/Inversaufbau und sein gewichteter Teilenergietest nach Abschnitt 7 | Teiluntergrenze über Budget: Variante verwerfen. Teilobergrenze unter tatsächlicher Budgetuntergrenze: nur für diesen Zeugen bereit zur gezielten Dualprüfung. Überlappung: unentschieden, mit dominantem Preis benennen. |
| Schur allein, nicht ausgewählt | Variationaler Test E_base+2 Re(nu_J* w)-H_*[Jw] für eine aus dem 84er-Modell gewonnene feste rationale Spalte w; eine 84er-Lösung, keine vollständige Inverse | Liegt die gerichtete Untergrenze über K_P, scheitert jede obere Inversabschätzung, die weiterhin Q_lower,old^-1 majorisiert. Liegt sie darunter, ist das noch kein positiver Energieanschluss und keine engere Majorante. |

**Warum K zuerst:** Hier liegt bereits eine konkrete strikt größere
zulässige Unterform vor, und die vollständige Restschranke (5) kann ohne
Neuintegration übernommen werden. Der Energieeffekt ist durch einen
begrenzten endlichen Test entscheidbar. U8 besitzt bisher keinen bezifferten
ausreichenden gemeinsamen Energiegewinn. Der Schur-Untertest wäre günstig
und informativ, baut aber noch keine bessere Unterform; er wird nicht als
zweiter Pilot parallel gestartet. Die Auswahl behauptet keine Wahrscheinlichkeit
für einen späteren N12-Erfolg.

## 7. Festes Pilotprotokoll

**Eingefroren:** nur gerade; X0 und rationaler #238-Zeuge unverändert;
K_star genau (1); altes Z=J X_ans unverändert; a,b genau wie in (8).
Keine adaptive K-, Antwortmatrix- oder Richtungssuche. Ungerade bleibt
unberührt. Das vorhandene K_P-Zertifikat wird hashgebunden wiederverwendet.

**Umfang:** eine 203x203-Faktorisierung mit 84 rechten Seiten für (6),
eine vollständige rationale 287x287-Schurblockprüfung, 12er- und 84er-
Matrix-/Vektorprodukte für genau den geraden Zeugen. Richtwert der Arithmetik:
1024 Bit, rationale Blockprüfung mit der bewährten 120-Dezimalstellen-
Methodik. Ein fester Rechenaufbau; keine neue Quadratur, kein R_L-Solve.
Eine belastbare Laufzeit auf dem späteren Ausführungsrechner ist nicht
gemessen. Der Pilot erhält ein Rechenlimit von 30 Minuten; ein Timeout
wäre ein technischer Abbruch, kein mathematisches Ergebnis.

**Fehlerkontrolle:** `assemble.py`/`weights.py` dienen als gebundene
Herleitungsreferenz. Neue Gewichte werden explizit als Parameter geführt,
ohne historische Dateien umzuschreiben. K_star^-1, P_star, k_star=K_star^-1 a0
und nu_star werden gemeinsam eingesetzt. Die F-J-/a_fin-Fehler behalten
ihre bisherigen gemeinsamen Preise und werden genau einmal bezahlt.
Die ganze Residualmodellabweichung benötigt eine neu berechnete gültige
Teilnormmajorante. Eine unverändert übernommene alte Teilnormgrenze ist ohne
Ordnungsbeweis nicht zulässig. Modell-, Integrations-, Koeffizienten- und
Matrixrundungsfehler bleiben getrennt ausgewiesen.

**Entscheidung am festen Zeugen:** Für das neue tatsächliche Teilenergie-
intervall [E_lo,E_hi] und das vorhandene tatsächliche Budget [K_lo,K_hi]:

- E_lo>K_hi: `PILOT_COMPARISON_EXCLUDED`; keine Dualrechnung für diese Variante.
- E_hi<K_lo: `PILOT_PARTIAL_PASS`; Reserve r=K_lo-E_hi ausweisen.
  Ein anschließender positiver Vergleich für diesen Zeugen würde eine gültige
  obere Einschließung <nu_star,R_L nu_star><=beta r/a verlangen. Die Reserve
  ist kein bereits verfügbares Dualzertifikat.
- Sonst: `PILOT_INCONCLUSIVE`; dominierenden Fehler/fehlenden Anteil nennen.
  Keine automatische Erweiterung von Raum, Quellenzahl oder Integrationslauf.

Bei nichtpositivem Zertifikatspivot, falscher Bindung oder ungeklärter
Operatorordnung wird keine Energieentscheidung ausgegeben. Die neue
P-Obermatrix, der Fehlertransport und die Ausgabe werden vor einer
Auswertung des Ergebnisses aus einem frischen Prüfsnapshot reproduziert.

Ein Teilpass würde nur diesen einen geraden Test bestehen. Ein vollständiger
Anschluss braucht weiterhin volle Energie, geeignete Richtungs-/Raumkontrolle
und beide Paritäten. Keine Änderung der Arbeitsdefinition von Objekt X.

## 8. Abnahme dieser Entscheidungsvorlage

`verify.py` prüft die Eingabebindungen, Datenabmessungen, den lokalen
Zwölferfehler und (3). Es reproduziert die kleinen Entscheidungsbelege;
es führt ausdrücklich weder den neuen P-Aufbau noch den Pilot-Energietest aus.
`EXPECTED.json` enthält rationale Einschließungen und den Digest von K_star.
`ACCEPTANCE_PLAN.md` legt den Prüfbedarf vor dem Abnahmelauf fest;
`ACCEPTANCE.json` hält die tatsächlichen Checks fest.

Die Entscheidung ist **ein K-Pilot**. Der abgeschlossene Auftrag besteht
aus dieser begründeten Auswahl und ihrem festen Protokoll. Externe
mathematische Prüfung und Meilenstein 4 bleiben offen; kein Merge.
