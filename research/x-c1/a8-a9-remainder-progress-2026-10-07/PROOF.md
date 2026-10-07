# A8→A9: acht Quellen und partielle Operatorzertifikate des vollständigen Restes

7. Oktober 2026 · **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**

## Aussagen und Voraussetzungen

Dieses Paket bindet die sechs unveränderten Forschungsarchive vom 5.–7. Oktober.
Die ursprünglichen A8/A9-Formidentitäten, Formraumidentifikation, Naturality,
Integralmajoranten und der alte hohe Boden δ=2/3 bleiben Voraussetzungen der
jeweiligen Originalbeweise. Neue A9-Gesamtpositivität wird nicht vorausgesetzt.
Der vollständige Rest und Objekt X bleiben offen.

### 1. Acht feste Quellen

Für vier Quellen je Parität (gerade Grade 2,4,6,8; ungerade 3,5,7,9) gilt nach
Elimination des gesamten alten A8-Raumes

\[
 S_e\succeq4\cdot10^{-12}W_e,\qquad S_o\succeq3\cdot10^{-11}W_o.
\]

Hier ist W die vorab festgelegte gewöhnliche L²-Grammatrix der gewählten
Vertreter. Die zusätzliche Quotientennorm ist eine getrennte Aussage.
Die gemeinsamen 4×4-Matrizen erhalten die Off-Diagonalen. Der Faktor 3 im
Fehlerbudget zählt drei Abbildungen; vier Spalten mit Fehlernorm ≤e geben
gemeinsam Δh*Δh≤4e²I. Beide gespeicherten Präzisionsläufe bestehen unabhängig
den exakten LDL-Schlusscheck. Tatsächliche Modellintegrale überlappen;
separat gerundete abgeleitete Majoranten können geringfügig abweichen.

Vollständige Herleitung: [Acht-Quellen-Beweis](packages/eight-source/PROOF.txt).
Die historische Wahlverfeinerung ist in [REFINEMENT](packages/eight-source/REFINEMENT.json)
gebunden; das Archiv allein beweist keine externe historische Zeitfolge.

### 2. Vollständige Restdarstellung und kompakter Defekt

Die momentkorrigierte Schalenabbildung Λ und W_X identifizieren den neuen
Quotienten. Nach dem zertifizierten Viererraum V je Parität ist R=V^{⊥W_X}.
Mit C als dessen vier Schurkopplungen und M_- als positiver Untermatrix gilt

\[
 P_R=q_b[\Lambda\cdot]+19I,\qquad
 B_R=P_R^{-1/2}(19I+g_R^*A_{old}^{-1}g_R+C^*M_-^{-1}C)P_R^{-1/2}.
\]

P_R^{-1/2} und B_R sind kompakt. Die zu S und U_- gehörenden selbstadjungierten
Operatoren besitzen kompakte Resolvente. Dies behauptet keine Kompaktheit
dieser unbeschränkten Operatoren selbst. Die analytischen Aussagen sind
hergeleitet, aber nicht maschinell bewiesen oder extern fachlich abgenommen.

Belege: [Restdarstellung](packages/remainder/BEWEIS.txt),
[Operatordomäne und Kompaktheit](packages/domain/LEMMATA.txt).

### 3. Eingefrorene Geometrie und vollständige Halbinversenbilder

Die acht Richtungen je Parität entstehen aus den W_X-projizierten lokalen
Legendre-Graden 4,…,11. Der volle orthogonale Projektor P8 ist festgelegt.
Die geometrischen Prüfungen bei 768/1024 Bit zertifizieren diese Raumwahl.
Anschließend wurden die vollständigen Bilder R_half e_j=P_R^{-1/2}e_j
eingeschlossen. Es gelten P_R≥20I und gemeinsam

\[
 \Delta^*\Delta\preceq\varepsilon_p^2 I_8,\quad \Delta=R_{half}-Y,
 \quad\varepsilon_e=0.000303687347,\quad\varepsilon_o=0.000307046420.
\]

Die isolierte 19I-Komponente von B00 besitzt die sicheren Normobergrenzen
0.8650653 bzw. 0.8657325 (nach außen gerundet). Diese Zahlen sind weder der
gesamte B00-Block noch tatsächlich gemessener Reserveverbrauch.
Die gemeinsamen Spaltenfehler werden nicht als unabhängig behandelt.

Belege: [Protokoll](packages/pilot/PROTOKOLL.txt),
[Halbinversen-Herleitung](packages/half-inverse/HERLEITUNG.txt).

### 4. Alte inverse Antwort mit sechs empfindlichen Kraftkombinationen

Die gebundene alte 191×191-Schurmatrix F besitzt die vollständig rationale
Oberform

\[
 F^{-1}\preceq T_0^*H T_0+\kappa P_J,
 \quad\kappa_e=37.657962,\quad\kappa_o=10.570239.
\]

T0 ist 6×191; H bleibt eine volle 6×6-Matrix. Alle 191 alten Koordinaten gehen
in die sechs korrigierten Kräfte ein. Die Wahl sechs folgt einer dokumentierten
Diagnose und ändert den eingefrorenen neuen Pilotraum nicht.
Die rationale Rundung von T0 ist bezahlt. Ganzzahlige Kongruenzen prüfen
beide 191×191-Positivitäts- und beide 185×185-Gap-Zertifikate erneut.

Für Δ sind zwei gemeinsame gewichtete Fehlergrame bereits kontrolliert:

| Fehlergram als Vielfaches von I8 | gerade | ungerade |
| --- | ---: | ---: |
| alter unendlicher hoher Anteil | 0.000001416613 | 0.000001448457 |
| altes 185-dimensionales Komplement | 0.001037473064 | 0.000264261855 |
| Summe | 0.001038889677 | 0.000265710312 |

Die Tabelle betrifft ausschließlich Fehlergrame. Für die volle Energie fehlen
Zentren und Kreuzterme. Das alte 185-dimensionale Komplement ist nicht der neue
unendliche B11-Block. Die sechs empfindlichen Fehlerkräfte und die vier
C-Kopplungen sind noch nicht ausgewertet.

Belege: [Faktorherleitung](packages/weighted-response/HERLEITUNG.txt),
[direkt verwendbare rationale Oberform](packages/weighted-response/RATIONAL_MAJORANT.json).

## Weiterhin offener vollständiger Gate

U00, G01, γ01, β_tail, η und α bleiben unberechnet. Erforderlich sind gemeinsame
Löwner-/Gramobergrenzen U00≥B00 und G01≥B01 B01*, die volle komprimierte
Tailnorm und anschließend

\[
 \beta_{tail}<1,\qquad I_8-U00-G01/(1-\beta_{tail})\succeq\eta I_8,
 \quad\eta>0.
\]

Mit γ01≥‖B01‖ wäre
α=min(η,1−β_tail)/(1+γ01/(1−β_tail))² eine volle positive Reserve.
Erst dann darf FULL_REMAINDER_CERTIFIED beziehungsweise ‖B_R‖<1 behauptet werden.
Ein späterer A9→A11-Rücktest, kofinale Fortsetzung, vollständige Testklasse und
Objekt X sind hier nicht abgeschlossen.

## Bindung und Prüfung

[SOURCE_BINDINGS.json](SOURCE_BINDINGS.json) bindet jedes Originalarchiv,
alle enthaltenen Dateien und jede lesbare Kopie. Originaltexte behalten ihre
damaligen Aussagen über lokale Arbeit und unverändertes GitHub. Der aktuelle
Integrationsstatus wird ausschließlich im Forschungsregister geführt.
Die [Abnahme](README.md#prüfung-und-reproduktion) trennt exakte Nachprüfung
gespeicherter Zertifikate, numerische Neuberechnung und analytischen Review.
