# FULL SHIFT-IMAGE CORRECTED RESOLVENT

**Abnahme: UNRESOLVED.** Die vollständige Shiftkorrektur senkt die zertifizierten
Fehlerschranken deutlich. Die beiden Zielgrößen schließen den gedrehten
Gegenzeugen weiterhin nicht aus. Der Odd-Winkeltest wurde deshalb nicht gestartet.

Status: **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.

## Kanonischer Ausgangspunkt

Cross-Projector-Gate und High-Response-Gate sind über
[PR #197](https://github.com/Waschtl904/objekt-x-programm/pull/197) und
[PR #198](https://github.com/Waschtl904/objekt-x-programm/pull/198) integriert.
Der bestätigte Integrationsstand ist `main@b27a18c32058a9a2a4e4c1611a18a67caa586c15`.
Die finale Main-CI `36904222676` war erfolgreich. Beide großen ursprünglichen
Pakete wurden lokal vollständig mit bytegleichen Ausgaben nachgerechnet.
PR #187 bleibt separat und unangetastet. Dieser neue Forschungsblock liegt
als lokales Prüfpaket vor.

## Vollständige Vierpolrechnung

Alle aktiven Shiftbilder wurden als vollständige stückweise polynomiale
Funktionen behandelt. Der hohe Anteil ist **P_>593 bei A9** beziehungsweise
**P_>571 bei A11**. Es wurde kein größeres endliches High-Fenster eingeführt.
Filter `t=1/300, m=8`, Kandidatenpräzision 1024 Bit und Integralpräzision
3072 Bit bleiben gleich.

Die vollständig ausgewertete Korrektur verwendet pro Pol eine gemeinsame
Richtung: die gewichtete Summe aller vollständigen hohen Shiftbilder.
Für A9/5, A9/6 und A11/8 wurden alle vier oberen Filterpole gerechnet.

Obere Schranken des Projektorfehlers aus Filter und vollständigen Residuen
(angezeigte Werte nach außen aufgerundet):

| Spalte | Vorher: 128-Moden-Korrektur | Vollständige gemeinsame Richtung |
|---|---:|---:|
| A9 / 5 | 0.007134994 | 0.002250303 |
| A9 / 6 | 0.518099275 | 0.166637627 |
| A11 / 8 | 0.683998775 | 0.241680479 |

Das sind Verbesserungen der Schranken um ungefähr 65–68 Prozent.
Die Aussage betrifft die zertifizierten Fehlergrenzen der gewählten Kandidaten.

## Die zwei Zielgrößen

Für die Überlappungen wird zusätzlich die bereits gültige Energieschranke
`||(I-P)u|| <= sqrt(S_ii/nu)` verwendet. Zusammen mit dem vollständig integrierten
Abstand zum Kandidaten liefert sie teilweise kleinere Fehlergrenzen als der
Resolvententest allein.

| Ziel | Kandidatenzentrum, ungefähr | Neue direkte Radius-Schranke |
|---|---:|---:|
| Y58 | 0.001764710937 | 0.053369410 |
| Y68 | 0.056802908372 | 0.104034486 |

Nach Schnitt mit dem bisherigen Zertifikat bleiben die Hüllen unverändert:

- **Y58:** `[0.0014825793, 0.0020794829]`.
- **Y68:** `[0.0324264060, 0.0784351101]`.

Die angegebenen Dezimalintervalle sind äußere Rundungen; die exakten rationalen
Grenzen stehen in `aggregate_targets.json`. Weder die geforderte obere
Y58-Trennung noch die untere Y68-Trennung ist bewiesen. Daraus folgt keine
neue gemeinsame zulässige Vervollständigung und kein No-Go für die Architektur.

## Zusätzliche Proben am ersten A11-Pol

| Kandidat | Vollständige physische Residuumschranke |
|---|---:|
| Gemeinsame Shiftbildrichtung | 0.247484566 |
| Diagonal vorkonditionierte vollständige Antwort | 0.259945359 |
| Sieben getrennte vollständige Shiftkanäle | 0.239404712 |

Die diagonale Probe behält den gesamten unendlichen Tail. Nur auf den schon
vorhandenen 128 Graden 573–827 wird der skalare Tailfaktor durch die angenäherte
diagonale Inverse ergänzt. Der alte niedrige Kandidat bleibt dabei fest;
die Rückwirkung in den niedrigen Block ist im Residuum enthalten.

Diese beiden Zusatzproben betreffen jeweils **nur den ersten A11-Pol**.
Für sie wurde kein vollständiger Projektor und keine eigene Y-Hülle behauptet.
Die Vierpol-Abnahme oben gehört zur gemeinsamen Shiftbildrichtung.
Beim Kanalkandidaten dienen die Mittelpunkte einer breiten Matrixhülle nur
zur Kandidatenwahl. Die Zertifizierung erfolgt vollständig durch das danach
berechnete physische Residuum; ein enges Matrixzertifikat wird nicht behauptet.

## Engster nächster Gate

Für `e_A=P_Au_A-a` und `e_B=P_Bu_B-b` gilt exakt

`K-<a,J*b> = <e_A,J*b> + <a,J*e_B> + <e_A,J*e_B>`.

Der letzte Term hat jetzt eine Schranke von ungefähr `3.3624e-5` bei Y58
beziehungsweise `2.7049e-3` bei Y68. Für einen Ausschluss genügt beispielsweise,
die Summe der **beiden linearen Terme** im Betrag strikt unter

- `2.6086e-4` für Y58 oder
- `1.9980e-2` für Y68

zu zertifizieren. Die exakten, etwas größeren Schwellen und die weniger
restriktiven gerichteten Bedingungen stehen in `primal_dual_budget.json`.
Das sind **offene Abnahmebedingungen**. Adjungierte Resolventenresiduen für
diese transportierten Zielrichtungen wurden in diesem Paket nicht berechnet.
Das Produkt zweier Vektorfehler ersetzt die beiden linearen Terme nicht.

## Prüfung und Aussagegrenze

- Vollständige Shift- und Gamma-Aktionen sowie sämtliche Sprunglogarithmen.
- Exakte Zellidentitäten; lokale Polynomprodukte und bezahlte Taylorreste für
  nichtsinguläre Logarithmen bei unveränderter Arithmetikpräzision.
- Kleine unabhängige Kernintegrale, Vergleich mit der bisherigen Normengine,
  volle und halbierte Odd-Integration und eine Negativkontrolle ohne Sprungterme.
- Getrennte rationale Prüfung von Quellenbindungen, Punktkandidaten,
  Residuenbudget, Spektralabständen, Filtergewichten und Y-Abnahme.

Die großen neuen Operatorintegrale wurden nicht unabhängig neu implementiert.
`PROOF.md` beschreibt die analytische Begründung. Das kompakte Paket bewahrt
die Punktkandidaten und alle Daten zur Rekonstruktion der vollständigen
Funktionen; die Hashes der großen Originalausgaben bleiben gebunden.
`replay.py --full` rechnet diese Ausgaben und die Zielintegrale erneut.

Es gibt weiterhin keine neue Aussage über Renewal, A13-Positivität, eine
kofinale positive Familie, ein globales Objekt X oder RH.
