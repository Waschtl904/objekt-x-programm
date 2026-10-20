# Abnahmeplan vor dem festen Pilotlauf

Genau der gerade Kandidat aus #245, Head a60f7602335f654ca7b42e8362e47af243e20462:
K_new unveraendert, b=51/50, c=1977/500000, a=500000/399173.
Alter physischer Zeuge, aeussere Antwortmatrix und K_P bleiben unveraendert.
Keine Richtungssuche, keine Nachschaerfungsserie, keine Integration, kein R_L.

Pflicht: hashgepruefte Eingabeschnappschuesse; rationale K-Zulaessigkeit;
1024-bit-Loesung der 203er-Matrix; rationale P-Obermatrix mit 10^-40
Diagonalsicherheitsabstand; 287 positive gerichtete rationale LDL-Pivots
bei 120 Dezimalstellen. Neue gemeinsame nu, Fehlerpreise und Teilnormgrenze;
saemtliche urspruenglichen F-J-Fehler bleiben erhalten.

Jeder vollstaendige Rechenaufruf wird durch einen Elternprozess nach
spaetestens 1800 Sekunden beendet. Technischer Abbruch bedeutet keine
mathematische Entscheidung. Es gibt genau einen Kandidaten und keine
automatische Wiederholung bei Timeout. Der identische Archiv-Replay
ist eine vorab festgelegte Reproduzierbarkeitspruefung, keine neue Suche.

Abnahme: beide Ergebnisdateien bytegleich aus frischem Paketarchiv;
unabhaengige rationale Endpunkt-/Gewichtspruefung; Zurueckweisung fehlender
und manipulierter Bindungen sowie von Python -O; Registry-Validator,
erzeugte Ansichten, bestehende Registry-Tests, Diff- und Scopepruefung,
anwendbare CI auf dem veroeffentlichten Head.

Entscheidung an veroeffentlichten rationalen Endpunkten:
Unterenergie > Budgetobergrenze: PILOT_COMPARISON_EXCLUDED, kein R_L.
Oberenergie < Budgetuntergrenze: PILOT_PARTIAL_PASS, nur Restbudget und
hinreichende ungewichtete Dualenergieschwelle beta*Restbudget/a ausweisen.
Sonst PILOT_INCONCLUSIVE, dominierenden Fehler benennen; keine Nachserie.
Ein Teilpass betrifft nur diesen festen Zeugen, nicht den ganzen Raum.
Punkt 4, N12, vollstaendige Dualkontrolle und externe Pruefung bleiben offen.
