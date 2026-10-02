# PRIMAL-DUAL CROSS-PROJECTOR GATE — Y68

**Y68: TARGET_EXCLUSION / GREEN 1.** Alle acht vorgeschriebenen Dualpole sind
vollständig ausgewertet. Die gerichtete Y68-Schranke schließt den bisherigen
gedrehten Gegenzeugen rigoros aus. Der danach ausgeführte gemeinsame
Odd-Winkeltest bleibt **UNRESOLVED**.

Status: **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Kanonische Quellen: `main@b27a18c32058a9a2a4e4c1611a18a67caa586c15`.
Zum Versiegelungszeitpunkt liegen beide Pakete lokal und ungemergt vor.
PR #187/A13 wurde nicht verändert.

## Gerechneter Umfang

- Vier adjungierte Pole bei A9 für den festen Zielvektor `J* b8`.
- Vier adjungierte Pole bei A11 für den festen Zielvektor `J a6`.
- Derselbe vollständige gemeinsame Shift-Korrekturraum mit einer hohen
  Richtung je Pol; 1024 Bit für Punktkandidaten, 3072 Bit für Integrale.
- Jede transportierte Zelle, der vollständige hohe Anteil und sämtliche
  Sprunglogarithmen bleiben in den Residuen enthalten.

Die Primaldaten stammen unverändert aus dem versiegelten Full-Shift-Paket.
Der fehlgeschlagene erste Versuch einer direkten Monomprojektion wurde
durch die dort bewährte stabile Gauss-Projektion ersetzt. Er lieferte keine
Zertifikatsaussage und führte zu keiner Vergrößerung des Korrekturraums.

## Die acht Beiträge

Die Residuen sind zertifizierte obere Schranken. d ist eine untere
Spektralabstandsschranke. Die signierte Spalte enthält bereits das Filtergewicht.
Der Fehler enthält Produktrest sowie Modell-, Quellen- und Trägerfehler;
der skalare Filterfehler kommt einmal pro Kammer hinzu. Dezimalintervalle
und Schranken sind nach außen gerundet. Exakte rationale Werte stehen in `gate.json`.

| Kammer | Pol | Primal rho ≤ | Dual sigma ≤ | d ≥ | Signierte Korrektur | Gewichteter Fehler ≤ |
|---|---:|---:|---:|---:|---:|---:|
| A9 | 0 | 0.1694838970 | 0.0712871616 | 0.0031977905 | [-8.739E-8, -8.738E-8] | 0.0031485349 |
| A9 | 1 | 0.1662210891 | 0.0641802735 | 0.0032798065 | [-8.127E-8, -8.126E-8] | 0.0027105550 |
| A9 | 2 | 0.1619049555 | 0.0548402330 | 0.0033333333 | [-7.433E-8, -7.432E-8] | 0.0022197264 |
| A9 | 3 | 0.1590440060 | 0.0486115624 | 0.0033333333 | [-7.038E-8, -7.037E-8] | 0.0019328445 |
| A11 | 0 | 0.2474845652 | 0.0152559720 | 0.0031749115 | [-1.451E-8, -1.450E-8] | 0.0009910034 |
| A11 | 1 | 0.2412373701 | 0.0134636480 | 0.0032713010 | [-9.51E-9, -9.50E-9] | 0.0008273811 |
| A11 | 2 | 0.2331605117 | 0.0110959609 | 0.0033333333 | [-4.52E-9, -4.51E-9] | 0.0006467850 |
| A11 | 3 | 0.2279159920 | 0.0094932913 | 0.0033333333 | [-2.06E-9, -2.05E-9] | 0.0005409183 |

| Kammer | Summe signierter Korrekturen | Produktrest ≤ | Vollständiger linearer Term |
|---|---:|---:|---:|
| A9 | [-3.134E-7, -3.133E-7] | 0.0100116606 | [-0.0100119740, 0.0100113473] |
| A11 | [-3.06E-8, -3.05E-8] | 0.0030060877 | [-0.0030061183, 0.0030060571] |

## Gerichteter Abnahmetest

`L_A + L_B` liegt zertifiziert in **[-0.0130180923, 0.0130174044]**.
Für GREEN muss die Untergrenze strikt größer als `-B68` sein,
mit `B68 ≈ 0.019980144720918858`.
Die nach unten gerundete Gate-Reserve ist
**0.0069620524 > 0**. Der Test ist bestanden.

Der bilineare Rest wird mit `0.002704813535`
und die Energieumrechnung mit `0.000009341127`
zusätzlich bezahlt. Daraus folgt die direkte Y68-Hülle
**[0.0410706614, 0.0725344674]**.
Nach Schnitt mit dem bisherigen Zertifikat ergibt sich
**[0.0410706614, 0.0725344674]**.
Die gerundete Hülle des gedrehten Zeugen ist
**[0.0341086089, 0.0341086090]**.

Die vorgeschlagenen Schwellen `sigma_A ≤ 0.05`, `sigma_B ≤ 0.04` kontrollieren
nur den Produktrest. Auch wenn sie erfüllt sind, braucht GREEN zusätzlich
eine passende Schranke für die signierte Korrektur. Deshalb verwendet dieses
Paket die vollständige gerichtete Summe als Haupttest.

## Prüfung und Aussagegrenze

Die kleinen Kontrollen vergleichen Transport und Adjungiertenrelation,
Gauss-Projektionen mit exakten Polynommomenten, Gamma mit getrennten direkten
Kernintegralen, vollständige mit halbierten Odd-Normen sowie signierte
Logarithmusintegrale. Eine komplexe Matrixprobe prüft die primal-duale Identität;
eine Negativkontrolle widerlegt eine rein residualbasierte GREEN-Regel ohne
signierten Term.

Eine getrennte Prüfung mit rationaler Arithmetik kontrolliert alle acht
Quellen- und Kandidatenbindungen, Residuenbudgets, Spektralabstände,
Filtergewichte, Vorzeichen und die Y68-Abnahme. `PROOF.md` enthält die
analytische Begründung. Die großen Operatorintegrale wurden nicht unabhängig
neu implementiert. Ein vollständiger Stichproben-Replay von A9/Pol 1 berechnet
Dualresiduum und signierte Korrektur aus demselben festen Kandidaten erneut;
das Ergebnis ist bytegleich. `full_spot_replay.json` bindet diesen Replay an
die unveränderten numerischen Erzeugerdateien. Er fand vor der Versiegelung
statt. Das Paket kann alle acht großen Rechnungen erneut ausführen.

## Gemeinsamer Winkeltest und begrenzte Gegenmodellsuche

Nach der strikten Y68-Trennung wurden sämtliche bisherigen Stage-A-Einträge
mit der neuen Y68-Schranke in den gemeinsamen Odd-Maximierer-Auswerter
eingesetzt. Alle Nebenintervalle bleiben erhalten. Die Auswertung der
gesamten Ausgangsbox liefert nur die triviale obere Korridorbreite 180°,
also **keinen zertifizierten Korridor unter 10°**. Es wurde keine neue
Unterteilung der Box vorgenommen. 180° beschreibt die uninformative Hülle,
nicht einen nachgewiesenen tatsächlichen Winkel.

Danach wurden sieben feste Parameterwerte der bereits vorhandenen gemeinsamen
Cayley-Familie geprüft. Fünf erfüllen die endlichen gemeinsamen Bedingungen;
3/4 und 7/10 des alten Wurzelparameters scheitern an Y68. Die vier zulässigen
nichtzentralen Stichproben haben folgende zertifizierte Abstände zur zentralen
Referenzgeraden:

| Stichprobe | Physischer Linienwinkel zur zentralen Referenz |
|---|---:|
| half | [0.613725647, 0.613725648]° |
| two_thirds | [0.821602102, 0.821602103]° |
| five_eighths | [0.769085796, 0.769085797]° |
| quarter | [0.306308646, 0.306308647]° |

Dies sind **nur Stichproben**, keine einheitliche Schranke über die ganze
zulässige Familie. Ein neues Gegenpaar mit mehr als 10° Abstand wurde dabei
nicht gefunden. Die Suche endet **BOUNDED_SEARCH_UNRESOLVED**. Die geprüften
Vervollständigungen erfüllen die endliche Relaxation; eine vollständige
physische Realisierung aller Versuchsdaten wird nicht behauptet.

Der alte nahezu rechtwinklige Gegenzeuge ist ausgeschlossen. Deshalb trägt
der alte STRUCTURAL-OPEN-Nachweis nicht auf die jetzt verschärfte Relaxation
über. Deren Winkelstatus ist wieder offen. Der nächste sachliche Schritt ist
die gezieltere gemeinsame Winkelauswertung mit der neuen Y68-Korrelation;
Y58 ist durch diesen Block noch nicht als notwendige nächste Rechnung belegt.
Eine neue duale Y58-Rechnung wurde nicht ausgeführt.

Renewal, A13-Positivität, eine kofinale positive Familie, ein globales Objekt X
und RH bleiben außerhalb der Aussage.
