# HIGH-RESPONSE ORIENTATION / CORRECTED RESOLVENT

1. Oktober 2026 · A9 → A11 · ungerade Parität

**Ergebnis: UNRESOLVED.** Die hohe Korrektur verbessert die rigorosen
Projektorfehlerschranken um etwa 17–19 %. Sie liefert aber keinen neuen
Bound für Y58 oder Y68 und schließt den gedrehten Gegenzeugen nicht aus.
Der ungerade physische Winkel bleibt offen.

Der neue Befund ist die Verteilung des Restes: Die ersten 128 hohen
Legendre-Moden erfassen nur etwa ein Drittel der ursprünglichen
Modellantwort. Nach der Korrektur liegt der Rest am gesondert geprüften
ersten Pol überwiegend oberhalb des Fensters; dort dominiert die
**Shiftantwort** gegenüber dem Potential- und Gamma-Anteil.

Status: **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**. Ausgangspunkt ist
`main@6302a47cab2132f0d87dec29bbf21d7ce98e8f75`. Dieses Paket bleibt lokal.
PR #187 wurde nicht verändert; A13-Forschungsdaten wurden nicht verwendet.

## 1. Capture-Diagnose für die ursprünglichen niedrigen Kandidaten

An allen vier oberen Polen wurden die signierten Koeffizienten von
\(\mathcal C_0^*x_z\) berechnet. Der Nenner kommt aus der bereits
veröffentlichten **vollständigen** Modell-Grammatrix, einschließlich des
unendlichen Parseval-Restes. Die folgende Tabelle gibt die Bereiche über
alle vier Pole nach außen gerundet an.

| Erste hohe Moden | A9, Spalte 5 | A9, Spalte 6 | A11, Spalte 8 |
| ---: | ---: | ---: | ---: |
| 8 | 2.19–2.21 % | 2.98–3.01 % | 5.72–5.73 % |
| 16 | 4.57–4.59 % | 5.74–5.77 % | 8.53–8.54 % |
| 32 | 9.82–9.85 % | 10.97–11.01 % | 13.37–13.41 % |
| 64 | 19.64–19.71 % | 21.42–21.51 % | 23.70–23.76 % |
| 128 | 32.44–32.52 % | 34.73–34.82 % | 37.38–37.45 % |

Bei A9 beginnt das ungerade hohe Fenster bei Grad 595 und reicht mit
128 Moden bis 849. Bei A11 reicht es von 573 bis 827. Die Zahlen
sind Modellenergieanteile, keine behaupteten Energieanteile der vollen
Resolventenlösung. Sie widerlegen für dieses Fenster die Erwartung eines
Capture-Anteils von 99 % oder 99,9 %.

## 2. Gekoppelte hohe Korrektur mit vollständigem Residualcheck

Aus Real- und Imaginärteilen dieser **auf das Fenster projizierten**
Antwortbilder wurden sieben Korrekturrichtungen bei A9 und fünf bei A11
gebildet. Die niedrigen und hohen Koeffizienten wurden anschließend
gemeinsam gelöst. Der Korrekturraum enthält damit noch nicht die
vollständigen unendlichen Antwortbilder.

Jede endliche Lösung ist nur ein Kandidat. Für die Zertifizierung wird
ihre gesamte Modellantwort als stückweise polynomiale und logarithmische
Funktion integriert. Der nicht dargestellte hohe Raum bleibt vollständig
enthalten. Die Mellinnormale, der tatsächliche Gamma-Modellfehler und die
Rundung der Quellbasis werden ausdrücklich bezahlt.

| Projizierte Trialspalte | Vorherige Fehlerschranke, ungefähr | Neue Fehlerschranke, nach oben gerundet |
| --- | ---: | ---: |
| A9, Spalte 5 | 0.00856305 | 0.007134994 |
| A9, Spalte 6 | 0.63139364 | 0.518099275 |
| A11, Spalte 8 | 0.84287706 | 0.683998775 |

Dies sind obere Fehlergrenzen, keine Messungen des tatsächlichen Fehlers.
Der Filter bleibt \(1/(1+(300\lambda)^8)\), die Kandidatenpräzision bleibt
1024 Bit. Die neuen vollständigen Integrale verwenden wie die bisherigen
Terminalintegrale 3072 Bit. Stabile Legendre-Auswertung, eine exakte
Gamma-Randwertidentität und lokale Zellkoordinaten verhindern dabei
unnötige Intervallaufweitung. Der Mellin-Taylorrest wird auch für die
höheren Polynomgrade vollständig kontrolliert.

## 3. Welcher hohe Kanal bleibt übrig?

Für den ersten oberen Pol wurde die vollständige Restenergie zusätzlich
durch Parseval in den dargestellten und den darüberliegenden Teil zerlegt.
Die Prozentangaben beziehen sich auf den um die Mellinnormale bereinigten
Modellrest, dessen Norm die physische Residualnorm kontrolliert.

| Fall | Restenergie oberhalb des Fensters, ungefähr | Norm des gemeinsamen hohen Restes | Norm der hohen Shiftantwort | Norm des hohen Potentialanteils |
| --- | ---: | ---: | ---: | ---: |
| A9, Spalte 5, oberhalb Grad 849 | 99.089 % | 0.00699930 | 0.00699803 | 0.00013616 |
| A9, Spalte 6, oberhalb Grad 849 | 99.047 % | 0.52431913 | 0.52422812 | 0.01005675 |
| A11, Spalte 8, oberhalb Grad 827 | 98.453 % | 0.69480254 | 0.69452828 | 0.01526922 |

Die Gamma-Tailnorm ist in diesen drei Fällen kleiner als
\(1.24\cdot10^{-10}\). Oberhalb des letzten Kandidatengrades verschwinden
die polynomiellen Beiträge von Quelle, harmonischem Diagonaloperator,
Konstante und Verschiebungsparameter. Dort bleibt der gemeinsame Kanal

\[
\Pi_{>K}\bigl(K_{\rm model}w+Sw-Vw\bigr).
\]

Die Daten lokalisieren die verbleibende Breite damit im Wesentlichen in
der hohen Shiftantwort. Diese zusätzliche Kanalanalyse wurde am ersten
oberen Pol ausgeführt; die vollständigen Residualschranken wurden an allen
vier Polen berechnet.

## 4. Die beiden Zielgrößen und der gemeinsame Winkeltest

Die direkten neuen Y-Einschließungen haben ungefähr folgende Mittelpunkte
und Radien:

| Eintrag | Mittelpunkt | Radius |
| --- | ---: | ---: |
| Y58 | 0.00176401744 | 0.69113384 |
| Y68 | 0.05685964319 | 1.20210138 |

Sie sind trotz der verbesserten Operatorrestschranken breiter als die
bereits vorhandenen gemeinsamen Projektorhüllen. Nach dem Schnitt bleiben
daher unverändert, nach außen gerundet:

\[
Y_{58}\in[0.0014825793,\;0.0020794829],\qquad
Y_{68}\in[0.032426406,\;0.078435111].
\]

Keines der beiden strengen Ausschlusskriterien für den gedrehten Zeugen
ist erfüllt. Der gemeinsame Odd-Maximizer-Prüfer behält alle bisherigen
Moment- und Projektorkorrelationen bei; seine Einschließung des
quadrierten Sinus zum festen Referenzvektor bleibt [0,1]. Es gibt weder
PARTIAL GREEN noch GREEN. Neue gemeinsam zulässige Gegenmodelle werden
nicht behauptet.

## 5. Was daraus folgt

Die hohe Korrektur wirkt, aber dieses endliche Fenster trifft nur einen
Teil der breiten Shiftantwort. Der nächste gezielte Ansatz ist deshalb
ein Korrekturraum, der die vollständigen verschobenen Antwortfunktionen
oder ihre rigoros kontrollierten hohen Anteile besser darstellt. Die
hier getesteten projizierten Antwortbilder reichen noch nicht.

Das ist ein Ergebnis über diesen konkret gerechneten Kandidatenraum.
Ein Hindernis für jede hohe Korrektur, eine Unschärfe des tatsächlichen
Maximierers oder ein strukturelles No-Go folgt daraus nicht. Der positive
Gap und die eindeutige Maximierergerade bleiben vorhandene Voraussetzungen.
Renewal, A13-Positivität, kofinale positive Familie, Objekt X und RH erhalten
keinen neuen Status.

## Prüfung und Reproduktion

Das Paket enthält die Capture-Belege, die festen gekoppelten Kandidaten,
die vollständigen Residualbelege, die Kanalanalyse und den gemeinsamen
Richtungstest. Der Vorgänger ist bytegleich als ZIP enthalten.

Ein Prüfer nur mit Python-Standardbibliothek kontrolliert Manifest,
Quellenbindungen, gespeicherte Intervallbudgets und den bytegleichen
gemeinsamen Richtungsreplay. Optionale Arb-Kontrollen vergleichen die neue
Gamma- und Shiftrechnung sowie die vollständige Restintegration mit der
vorhandenen unabhängigen kleinen Terminal-Engine. Die großen gerichteten
Operatorintegrale wurden für dieses Paket berechnet; ihre zusätzliche
vollständige Wiederholung ist als `--full` verfügbar und wurde für den
Paketabschluss nicht nochmals ausgeführt. Eine unabhängige Implementierung
der großen Rechnungen wird nicht behauptet.

Details stehen in `ANALYTIC_ARGUMENT.txt`, `REPRODUKTION.md`,
`verification.json` und `verification_arb.json`.
