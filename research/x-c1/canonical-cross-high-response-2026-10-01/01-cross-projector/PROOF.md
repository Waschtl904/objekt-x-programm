# CROSS-PROJECTOR RESIDUAL GATE

1. Oktober 2026 · A9 nach A11 · ungerade Parität

**Ergebnis: UNRESOLVED.** Gemeinsame Projektorgeometrie verschärft alle
48 Kreuzblockeinträge. Beide bisherigen Gegenzeugen liegen aber weiterhin
in diesen skalaren Einschließungen, und der gemeinsame Richtungsprüfer
liefert keinen Winkelkorridor unter 10° Gesamtbreite. Ein anschließender
direkter rationaler Filter ist im skalaren Spektrum sehr genau; seine
vollständigen hohen Lösungsrestschranken sind für die letzten Trialspalten
zu grob und verbessern die Richtungseinschließung nicht.

Status: **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**. Es wird keine neue
zulässige gekoppelte Gegenfamilie konstruiert; **STRUCTURAL OPEN 2 ist
damit nicht bewiesen**. Die bereits bewiesene Einfachheit und der positive
Extremalgap bleiben Voraussetzungen. Der tatsächliche ungerade Maximierer
bleibt quantitativ offen.

## Kanonischer Ausgangspunkt

Vor dieser Rechnung wurden die vier abgeschlossenen negativen Pakete
vollständig und unverändert integriert:

- Research-PR [#195](https://github.com/Waschtl904/objekt-x-programm/pull/195),
  Head `ed94c19f824c947f63e4867fb3c202f71e36e631`, Merge
  `eb4bd1b78b130a44987c4ee171ded8034c0948cc`.
- Registry-PR [#196](https://github.com/Waschtl904/objekt-x-programm/pull/196),
  Head `ef10c9b012100c48a1c6894f8b782130a6fd5ae8`, Merge und neuer Main
  **`6302a47cab2132f0d87dec29bbf21d7ce98e8f75`**.
- Alle anwendbaren PR-Prüfungen sind erfolgreich. Der
  [Main-Replay](https://github.com/Waschtl904/objekt-x-programm/actions/runs/36816858969)
  reproduziert vier Belege bytegleich. Die
  [finale Main-CI](https://github.com/Waschtl904/objekt-x-programm/actions/runs/36817745054)
  ist erfolgreich. Das Register enthält 45 Ergebnisse und keine ausstehende
  Paketübernahme.

49 Originaldateien und vier Archive bleiben unverändert. Der lokale Main
ist synchron, ohne ungepushte Branch-Commits. Der vorher vorhandene
unversionierte Python-Cache wurde belassen. PR #187 ist weiter offen auf
`18d752f492fde5f0a9a6dec8cf8ff42583f8b064`. Dieses neue Paket bleibt lokal;
die Integration ist in `INTEGRATION.json` gesondert dokumentiert.

## Stufe A mit gemeinsamer Projektorgeometrie

Für die echten projizierten Trialbasen setze

\[
V_A=P_AU_A=U_AG_A+E_A,
\qquad U_A^*E_A=0,
\qquad E_A^*E_A=G_A-G_A^2.
\]

Entsprechendes gilt bei B. Mit dem bekannten ungefilterten Überlapp O folgt
die gemeinsame Identität

\[
K=G_AOG_B+G_AU_A^*J^*E_B+E_A^*J^*U_BG_B+E_A^*J^*E_B.
\]

Die gerichteten Eintragseinschließungen verwenden dieselben G-Matrizen in
allen Faktoren. Zusätzlich wird der Vorwärtsrest
\((I-P_B)JV_A\) über Formnaturality und den vollständigen B-Komplementboden
kontrolliert. Dadurch erhält man eine zweite Hülle um \(G_AO\), die mit
der ersten geschnitten wird. Es wird kein inverses Intertwining angenommen.
Die Einzelprodukte der tatsächlichen hohen Residuen werden in Stufe A
noch nicht gesondert mit Vorzeichen berechnet.

Die hohen Projektorreste sind \(R_A=(I-P_A)U_A\) und
\(R_B=(I-P_B)U_B\). Ihr gemeinsamer Kreuzzerfall ist exakt

\[
K=O-R_A^*J^*U_B-U_A^*J^*R_B+R_A^*J^*R_B.
\]

Die Normierung bleibt exakt

\[
B_B=G_B+L_B/17,\qquad Y=K G_B^{-1}B_B,
\qquad |Y_{ij}-K_{ij}|\le\sqrt{(S_A)_{ii}(S_B)_{jj}}/17.
\]

Alle 48 bisherigen Eintragshüllen werden enger. Die besonders relevanten
neuen Y-Intervalle lauten, nach außen gerundet:

| Eintrag | Neue Einschließung | Zentraler alter Zeuge ungefähr | Gedrehter alter Zeuge ungefähr |
| --- | --- | ---: | ---: |
| Y58 | [0.0014825793, 0.0020794829] | 0.00178118 | 0.00205932 |
| Y68 | [0.032426406, 0.078435111] | 0.0554255 | 0.0341086 |

Bei Y68 trägt der Rest \(\langle JE_{A,6},U_{B,8}\rangle\) in der
Vorwärtshülle einen Radius von ungefähr **0.02225675** bei. Der zweite,
über den hohen B-Schnitt kontrollierte Term trägt etwa **0.00087108** bei.
Bei Y58 betragen diese beiden Beiträge ungefähr 0.00028776 und 0.00001079.
Die relative Lage des alten Projektorrestes ist damit der Hauptbeitrag
dieser günstigen Hülle.

Die neuen Hüllen werden in den bestehenden gemeinsamen Prüfer eingesetzt:
Y, seine Kernbasis N und sämtliche komprimierten Momente bleiben gekoppelt.
Der physische Rang-eins-Projektor wird mit G_B bewertet. Die festen
Referenzkoeffizienten aus dem integrierten Boxtest bleiben erhalten; sie
stehen in `combined_gate.json`. Die resultierende
Hülle für den quadrierten Sinus zum festgelegten Referenzvektor bleibt
**[0,1]**. Die alten Zeugen verletzen keinen neuen skalaren Y-Bound. Ihr
Überleben dieser notwendigen Hüllen ist ausdrücklich kein Nachweis, dass
sie sämtliche neuen gemeinsamen Projektoridentitäten realisieren.

## Stufe B mit rationalem Spektralfilter

Verwendet wird

\[
f(\lambda)=\frac{1}{1+(\lambda/t)^8},\qquad t=1/300.
\]

Die schon zertifizierten kritischen Obergrenzen und hohen Untergrenzen
liegen beiderseits von t. Vier konjugierte komplexe Polpaare reduzieren
den Filter auf acht verschobene Resolventen. Bei A9 beziehungsweise A11 werden nur die
vorhandenen sechs beziehungsweise acht ungeraden Trialspalten behandelt. Die
Abstände der Pole zum gesamten zertifizierten Spektrum werden bezahlt.
Die Pole sind komplex; es wird keine unzutreffende Positivitätsbehauptung
über alle reellen Teile der Verschiebungen verwendet.

Für jede verschobene Gleichung wird ein endlicher Lösungskandidat gewählt.
Sein Fehler wird am **vollständigen physischen Operator** abgeschätzt.
Der ganze hohe Raum geht über die vorhandene vollständige Kopplungs-Grammatrix
ein; er wird nicht durch eine endliche Modentrunkierung ersetzt.

Die Rechnungen bei **1024 und 1536 Bit** liefern überlappende Einschließungen.
Der ungefilterte Überlapp wird gegen das veröffentlichte Zertifikat geprüft.
Alle neu berechneten polynomialen Überlappungsradien müssen kleiner als
\(10^{-20}\) sein. Die tatsächlich erreichten Breiten der polynomialen Näherungswerte
Ktilde58 und Ktilde68 liegen im 1024-Bit-Lauf unter \(4.28\cdot10^{-91}\) beziehungsweise
\(5.18\cdot10^{-89}\). Diese Breiten betreffen die Integration
der Näherungsvektoren; die Operatorrestfehler kommen anschließend hinzu.

Der reine skalare Projektorfilterfehler ist kleiner als
**4.316·10⁻¹¹ bei A9** und **5.077·10⁻¹¹ bei A11**. Er begrenzt diesen
Versuch nicht. Die vollständigen Lösungsrestschranken ergeben dagegen
folgende nach oben gerundete Fehlergrenzen für die projizierten Spalten:

| Spalte | Normfehler höchstens |
| --- | ---: |
| A9 Spalte 5 | 0.008564 |
| A9 Spalte 6 | 0.631394 |
| A11 Spalte 8 | 0.842878 |

Die daraus gewonnenen direkten Y-Radien liegen bei ungefähr **0.851441
für Y58** und **1.474273 für Y68**. Sie verengen keine bisherige Y-Hülle.
Der gemeinsame Schnitt beider Präzisionsläufe mit Stufe A lässt die
Richtungseinschließung deshalb unverändert offen.

## Der begrenzende Restterm

Schreibe den vollständigen Operator in Mellin-Koordinaten als
\(\widehat Q=\bigl(\begin{smallmatrix}L&\mathcal C\\
\mathcal C^*&H\end{smallmatrix}\bigr)\). Für einen niedrigen
Resolventenkandidaten x_z enthält sein hoher Rest

\[
r_{H,z}=t_Ht_L^*(v+zx_z)-\mathcal C^*x_z.
\]

Der entscheidende bezahlte Beitrag ist

\[
\|\mathcal C^*x_z\|\le\sqrt{x_z^*H^{up}x_z}.
\]

Bei A11 Spalte 8 liegen diese oberen Normschranken über die vier Polpaare
ungefähr zwischen **0.7953 und 0.8628**. Der niedrige Rest ist zugleich
kleiner als **1.45·10⁻⁴⁶**, die hohe Massenkorrektur kleiner als
**8.14·10⁻⁵⁴**. Bei A9 Spalte 6 liegen die entsprechenden hohen
Kopplungsschranken ungefähr zwischen **0.6029 und 0.6419**, bei einem
niedrigen Rest unter **1.05·10⁻³²**.

Im Kreuzprojektorzerfall begrenzt damit vor allem die Hülle von
**\(U_A^*J^*R_{B,8}\)** die direkte Rechnung; bei Y68 kommt die große
Unsicherheit von **\(R_{A,6}^*J^*U_{B,8}\)** hinzu. Der gemeinsame
Residualterm \(R_A^*J^*R_B\) wird ebenfalls mitgeführt.
Dies sind grobe obere Fehlerschranken. Sie sind keine unteren Schranken
für die tatsächlichen Residuen oder für eine intrinsische Unschärfe der
tatsächlichen Maximierergeraden.

Der nächste gezielte Rechenschritt wäre daher eine gerichtete gemeinsame
Kontrolle der vollständigen hohen physikalischen Antworten oder eine
zusätzliche hohe Korrektur der Resolventenkandidaten. Die beiden Präzisionsläufe zeigen praktisch dieselben dominanten
Kopplungsrestschranken. Ein anderer Filter könnte andere Restgrenzen
ergeben; dieser Block untersucht ausschließlich den festgelegten Filter.

## Prüfung und Aussagegrenze

Die vorab festgelegte GREEN-Abnahme verlangt einen ausgeschlossenen alten
Gegenzeugen und einen tatsächlichen physischen Winkelkorridor unter 10°
Gesamtbreite. Beides wurde hier nicht erreicht. Für STRUCTURAL OPEN 2
wären neue vollständige gekoppelte Vervollständigungen einschließlich der
zusätzlichen Daten nötig; solche werden hier nicht behauptet.

Die Reproduktion prüft Quellenbindungen, die exakten rationalen Filterbudgets,
beide Präzisionsbelege sowie bytegleiche kleine Replays der Stufe A und der
gemeinsamen Richtungsrechnung. Unabhängige kleine Kontrollen prüfen
Filteridentität, vollständige Residuen, nichtorthogonale Masse, gemeinsame
Projektoridentitäten und das notwendige Beibehalten des hohen Restes.
Die beiden Arb-Läufe benutzen dieselbe Implementierung. Der kleine Replay
ist keine unabhängige Neuberechnung ihrer großen Operatorlösungen; der
optionale vollständige Replay ist in `REPRODUKTION.md` beschrieben.

Die ursprünglichen Terminalintegrale bleiben gebundene Voraussetzungen.
Es wurden keine A13-Forschungsdaten verwendet. Allgemeines Renewal,
kofinale positive Familie, globales Objekt X und RH erhalten keinen
neuen Status. Dieser Block schließt einen konkret ausgeführten Versuch
mit **UNRESOLVED** ab; er ist kein No-Go für die Kreuzprojektormethode.
