# Gesamter reduzierter Core: positiver Gate auf einem viel kleineren Fenster

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**, 19. September 2026.

Neu bewiesen ist, gleichmaessig fuer B=log(5)/2 und
**0<h<=2^(-10^16)**:

- Theta_0(B+h)<1-2*10^-13 auf dem gesamten reduzierten Formbereich;
- R_0>=(331/500)*10^-13 I;
- Q_W[u]>10^-17 ||u||^2 fuer jede nichtverschwindende tatsaechliche
  gerade H1_0-Quelle mit den beiden urspruenglichen Mellinbedingungen.

Das ist ein Even-All-Source-Satz rechts von B. Das neue Fenster ist
jedoch **enorm viel kleiner als 10^-20**. Fuer den restlichen Bereich
2^(-10^16)<h<=10^-20 liefert dieses Paket keinen positiven Gate.
Es behauptet weder Negativitaet noch einen Abschluss der Odd-Fortsetzung.

Der Fortschritt beruht auf einer exakten Trace-Elimination fuer jeden
Corevektor. Der verbleibende Shellfunktional wird fuer beliebige
L2-Corefunktionen kontrolliert; der ganze Coretail, der ganze Shelltail
und alle gemischten Beitraege sind eingeschlossen. Der Shellboden wird
als wachsender Faktor log(2/h) behalten. Die gemeinsame H1-Spurbedingung
und der physische Ruecktransformationsfaktor 65 bleiben erhalten.

Die festgelegte Grad-62-Quelle wird nicht geaendert. Ihre Energieorthogonal-
Zerlegung mit vollstaendigem Komplement erhaelt zusaetzlich einen
Trace-Komplementbound unter 4.2*10^-11. Dieser Tracebound allein ist kein
vollstaendiger Schur-Gate auf dem groesseren Fenster.

Die Breite ist eine exakte positive rationale Zahl in Potenzschreibweise,
kein numerisch berechneter Nullwert. Der Checker prueft die notwendigen
Potenz- und Logarithmusvergleiche mit kleinen ganzen Zahlen. Er bindet
57 Eingabedateien und reproduziert die 31 Richtungspruefungen sowie die
28 Koordinaten-, 43 Shell- und 9 A-Gauge-Pruefungen der Voraussetzungen. Diese
Reproduktion ist kein unabhaengiger externer Audit.

Der zwischenzeitliche Commit 4ab3341 mit dem A-Gauge-Koordinatensatz
bleibt vollstaendig erhalten. Fuer dessen gesamten Core liefert derselbe
Residualbound Theta_A<=169/500. Mit dem Vorwaertsfaktor 65 folgt der
staerkere physische Abstand >10^-17. Theta_A wird dabei nicht mit dem
urspruenglichen L2-Gauge-Operator Theta_0 verwechselt; dessen oben
genannter positiver Gate bleibt separat bewiesen.

Offen bleiben das volle bisherige rechte Fenster, die Odd-Fortsetzung,
groessere Fenster, Objekt X und RH. Es gibt keine dritte Mellinbedingung,
kein A1, keinen neuen PR und keinen Merge. Vorgaengerpakete bleiben
unveraendert; das Paket wird nur auf der Forschungsbranch angehaengt.
