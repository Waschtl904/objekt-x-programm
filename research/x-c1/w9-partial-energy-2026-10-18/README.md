# Gemeinsame W9-Teilenergie

Fortsetzung von #237 auf dessen unveränderter Basis
`0144b2feeb732c506f9ac19c059b2b849104dc0e`.
**Autorenresultat / EXTERNAL_REVIEW_OPEN**, unter den gebundenen
Operator-, Domänen- und Quellenmodellvoraussetzungen.

Für beide neu festgefrorenen Richtungen ist bereits die vollständig
bezahlte Teilenergie größer als das tatsächliche K_P-Budget:

| Größe | gerade | ungerade |
|---|---:|---:|
| Teilenergie | [6.0481910, 6.0713093] · 10^-5 | [5.3963217, 5.3979761] · 10^-6 |
| K_P | [5.4117169360, 5.4117169380] · 10^-5 | [5.2807764351, 5.2807764506] · 10^-6 |
| untere Teilenergie minus oberes Budget | >6.3647 · 10^-6 | >1.15545 · 10^-7 |

Alle Tabellenintervalle sind nach außen gerundet. Damit scheitert der
**festgelegte W9-Vergleich** für jede der beiden Richtungen und
die unveränderte Antwortmatrix. Das ist keine negative Weil-Richtung
und schließt andere Inversmajoranten oder Antwortregeln nicht aus.
Der enge Negativbefund trägt in META den Status `AUTHOR_DERIVED_NO_GO`;
der Registereintrag bleibt `PENDING_STATUS_REVIEW`. Die einzelnen
Rechenzertifikate bleiben bedingte Autorenresultate.

Dieses Paket führt die zwölf Residuen auf dem neuen Grad-11-Schalenraum
gemeinsam durch die hohe U8-Projektion, die endliche U8-Antwort, den
K-inversen Zwölferblock und den P_upper-Block. Pro Parität werden die
191 × 12 B-Paarungen, 12 × 12 alten Quellenpaarungen und 84 × 12
Basis-Paarungen einschließlich ihrer vollständigen hohen Kreuzanteile
aus gemeinsamen Funktionsmomenten berechnet. Die Differenzen entstehen
vor dem Quadrieren.

Der positive R_L-Dualterm bleibt offen. Eine gerichtete untere Teilenergie
kann bereits zum Ausschluss der festen Vergleichsregel genügen. Eine obere
Teilenergie ist dagegen keine obere Einschließung der vollständigen W9-Energie.
Ein endlicher R_L-Galerkinwert wäre ebenfalls zunächst nur eine Untergrenze.

## Rechenwege

- `integrate.py`: gemeinsame analytische Modelle, gerichtete Gaussreste,
  alle Primzellen und beide logarithmischen Ränder; noch ohne die separat
  zu bezahlenden Quellen- und Gamma-Modellfehler.
- `weights.py`: neue Normmajorante ausschließlich für die vier berechneten
  Features. Die Antwortmodellfehler werden damit in der richtigen Energie
  kontrolliert; keine vollständige W9-Norm wird behauptet.
- `assemble.py`: gemeinsame Differenzen, unabhängige Kontrollen und
  vollständiger Fehlertransport für eine feste Richtung.
- `select_candidate.py`: ausdrücklich ungerichtete Kandidatenauswahl.
  Die exakten Dezimalkoeffizienten werden vor der folgenden Rechnung gespeichert.
- `certify_k.py`: getrennte gerichtete K_P-Rechnung für einen bereits
  festgefrorenen Kandidaten. Dieser Lauf sucht keine neue Richtung.
- `controls.py` und `source_controls.py`: unabhängige Gamma-Primitiven
  und direkte Kernelintegrale, auch für die höchsten alten Grade.

Python 3 mit `python-flint==0.9.0` wird für die gerichtete Rechnung benötigt;
NumPy/SciPy nur für die ungerichtete Auswahl. `integrate.py` verwendet 3072 Bit,
die Energiearithmetik 800 Bit. Alle veröffentlichten Intervallendpunkte sind
nach außen auf ein rationales Raster gerundet.

Der vollständige Prüfer wird vom Repository aus aufgerufen:

```sh
python research/x-c1/w9-partial-energy-2026-10-18/verify.py
```

Er berechnet beide Paritäten aus leeren Zellverzeichnissen neu, prüft die
Kontrollen, die alte K_P-Referenz und die festgefrorenen neuen Kandidaten.
Die Kandidatensuche läuft dabei nicht erneut. Die dokumentierte Umgebung
ist Python 3.12.14 mit den angegebenen Paketversionen.

Zwischenstände unter `--work` sind nur lokale Fortsetzungsdaten. Sie binden
Quellcode, Eingaben und Parameter und speichern die Arb-Kugeln exakt, ohne
Pickle oder Dezimalrundung. Ein abgebrochener Zwischenstand ist kein Ergebnis
und wird nicht als Zertifikat veröffentlicht. Ein frischer Abnahmelauf benutzt
ein leeres Arbeitsverzeichnis.

Der Prüfer benutzt nach der Hashprüfung nur gespeicherte Eingabebytes und
führt die gebundenen eigenen Python-Module aus diesen Bytes aus. Eine
Regression verändert eine gelesene Testdatei und verlangt das unveränderte
Speicherabbild; falsche Hashes und ausbrechende Pfade werden abgewiesen.
`python -O` wird nicht als Abnahmelauf zugelassen.

## Grenzen

Keine Bestätigung der Antwortregel, kein vollständiger Energievergleich,
kein N12-Abschluss und kein A9→A11-Positivitätssatz. Bytegleiche Reproduktion
prüft den Rechenpfad und seine Bindungen; sie ersetzt keine unabhängige
mathematische Prüfung. Die verworfenen Entwicklungsläufe sind in
`PROOF.md` dokumentiert.
