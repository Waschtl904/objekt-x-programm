# Ausschluss der festen ausreichenden Komplementmajorante an ell12

Stand 28. Oktober 2026. Projektinterne gerichtete Abnahme unter den
geerbten Voraussetzungen einschließlich H1–H4; externe Begutachtung offen.
Die Originale stehen im unveränderten GPT1-Abschlussarchiv, dessen Identität
[ARCHIVE.json](ARCHIVE.json) bindet. Der ausführliche
[Abschlussbericht](review/GPT1_ABSCHLUSS.txt) dokumentiert die analytische
Anwendung, die unabhängige Rekombination und deren Prüfgrenzen.

## 1. Festgehaltener Vergleich

Für dieselbe feste Richtung t=ell12, dieselbe physische Antwort und dieselbe
Majorante lautet der hinreichende Vergleich

    S_suff[t] = D_N[t] − (20/19)(W9[C_N t] + K),
    K = k_N(t)^T Gp^(-1) k_N(t).

Die zwölf gemeinsamen Kopplungen werden in der geprüften Basis B ausgewertet:
r=B^T k_N und Q=(B^T Gp B)^(-1)>0, also K=r^T Qr. Es wird kein Hauptblock
unter Weglassen unbekannter übriger Koordinaten verwendet.

## 2. Bezahlte Kopplungsuntergrenze

Die unabhängig rekombinierte Modellenergie erfüllt

    E_model,lo > (10387809/5000000)^2.

Für die gesamte Abweichung gilt in derselben inversen Grammetrik

    ||r − r_model||_Q < 1879/500000 = 0,003758.

Dieser Preis enthält den gemeinsam transportierten Kraftfehler einschließlich
der historischen Gamma160-/A160-Fehler sowie sämtliche übrigen Quellen-,
Basis-, Moment-, Antwort- und Matrixfehler. Die jeweiligen Metriken werden
nicht gleichgesetzt. Die gemeinsame Kraftabweichung wird mit
sqrt(tr(Q L^T L)) bezahlt; die übrigen positiven Preise werden konservativ
über |Q_ij| transportiert. Die ganze Momentfunktion besitzt eine eigene
analytische Hülle; ein auf null gerundetes JSON-Intervall ist dafür kein Beweis.

Die umgekehrte Dreiecksungleichung ergibt strikt

    K > (10387809/5000000 − 1879/500000)^2
      = 107516555022361/25000000000000
      > 215033/50000.

## 3. Rationale Entscheidung

Aus W9>=0 und der bereits geprüften direkten Formobergrenze folgt

    (20/19)(W9 + K) > 215033/47500,
    D_N[t] <= 437284983429949477/100000000000000000,
    S_suff[t] < −292905314830959937/1900000000000000000
              < −0,154160692.

Die ganze W9-Obergrenze und die Restintegration von nu sind für diesen
Ausschluss nicht erforderlich. Sie wurden nicht gestartet.

## 4. Belegumfang und Reichweite

Der einzige gemeinsame Hauptlauf enthält 424 Funktionsabschnitte, beide
Endstreifen und 71 direkte Abschnitte. GPT1 hat die gespeicherten Beiträge
unabhängig rekombiniert, die vollständige Partition kontrolliert und die
Fehleranwendung geprüft. Das unveränderte Autorenfeld mit früherer Angabe
68 wird durch einen separaten, hashgebundenen Metadatennachtrag auf 71
korrigiert. Der Archivprüfer bindet sämtliche Originalabschnitte und führt
nur den letzten rationalen Schluss samt Schutzkontrollen frisch aus.
Eine wiederholte numerische Integration wird damit nicht behauptet.

Der frühere notwendige Ein-Skalar-Test bleibt richtig: Er lieferte keinen
Ausschluss, weil er nur einen Teil der Kopplungsenergie erfasste. Ein älterer
UNRESOLVED-Bericht bleibt als damaliger Stand erhalten; das spätere Votum
steht ausdrücklich daneben.

Ausgeschlossen ist ausschließlich diese ausreichende U_E-Komplementroute.
Die tatsächliche Schurform und A_E-Inversenergie sind damit nicht widerlegt.
Der bestandene [v2-Zwölfervergleich](../w9-grad11-new-comparison-even-2026-10-26/revision-v2/README.md)
und die Gültigkeit der Inversmajorante auf E bleiben unberührt. H1–H4 werden
übernommen, nicht nochmals bewiesen. Punkt 4, ungerade Parität, externe
Begutachtung und das unendliche Komplement bleiben offen; Checkliste 3/10.
