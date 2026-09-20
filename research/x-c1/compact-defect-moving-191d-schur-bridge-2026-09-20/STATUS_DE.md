# Kompakter Defekt: uniforme 191D-Schur-Bruecke

20.09.2026. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.
Anker: `5557d94`.

Der neue Schritt verbindet den konkreten C1-Defekttransfer mit dem
unabhaengig bewiesenen beweglichen High-Tail. Fuer jedes `B<=a<=1`
und beide Paritaeten gilt auf dem vollstaendigen hohen Bildraum:

    ||R_a|High||^2 <= 943/945,
    (I-R_a*R_a)|High >= (2/945) I.

Der komplementaere kritische Raum hat genau 191 Koordinaten je Paritaet.
Damit gilt `s_192(R_a^p)<999/1000`, gemeinsam `s_383(R_a)<999/1000`.
Hoechstens 191 Singularwerte je Paritaet koennen die Grenze eins erreichen.
Dies ist eine Aussage ueber den gesamten unendlichen Tail.

Die Verbindung zum Transportkern ist jetzt ein Satz in praezisem Scope:
Der physische bewegliche 191D-Core-Schurrest und der Defekt-Schurrest
sind durch eine positive Gram-Kongruenz verbunden. Die physischen
Legendre-Low-Vektoren werden nicht mit den fuehrenden Singularvektoren
gleichgesetzt. Letztere besitzen einen vollstaendigen, eigenwertabhaengigen
High-Anteil.

Der verbleibende Gate lautet

    S_a^p = I - alpha - beta* (I-K)^(-1) beta >= 0,
    0 <= K <= 943/945.

Der High-Inversenrest ist durch eine uniforme rationale Neumann-Schranke
vollstaendig bezahlt. Ein Kriterium fuer eine gerichtete obere Schranke
des groessten Singularwerts aus endlich vielen rigoros eingeschlossenen
Matrixeintraegen ist angegeben. Diese Eintraege und ihr positives Vorzeichen
sind auf neuen Fenstern noch nicht zertifiziert.

Die geordneten Singularwerte sind im Endpunkt stetig und monoton wachsend.
Der Eintritt von Prime-Kanal 7 erzeugt keinen Sprung und keinen neuen
Kandidaten: Der feste Horizont verwendet bereits alle fuenf Kanaele.
Aus Stetigkeit folgt hier noch keine quantitative oder nicht summierbare
Transportschrittweite.

Die urspruenglichen zwei Mellinbedingungen und der abgeschlossene
physische Formbereich bleiben erhalten. Die polynomiellen Low-Repräsentanten
werden korrekt als Formquellen behandelt und durch echte glatte Quellen
approximiert; ihnen wird keine falsche H1-Nullrandbedingung zugeschrieben.
Die geerbte Near-Null-Quelle bleibt unveraendert.

Offen bleiben der positive endliche Schurrest, volle Kontraktion bis 1,
die zusaetzlichen Low/Profile-Kopplungen, neue positive Fenster,
unbeschraenkte Horizontkompatibilitaet, positiver C1-Abschluss, Objekt X
und RH. Kein A1-Import, keine dritte Mellinbedingung, keine negative volle
Weil-Quelle und keine numerischen Eigenwerte als Beweis.

Die neue Pruefung besteht 67 Checks, bindet 24 Eingaben und reproduziert 53 Kandidatenchecks
sowie beide dokumentierten High-Tail-Modi (25 und 26 Checks). Die alten
Pakete werden nicht umgeschrieben. Kleine rationale Modellmatrizen dienen
nur der Kontrolle der Blockalgebra, nicht der Bewertung physischer
Singularwerte. Reproduktion ist kein unabhaengiger analytischer Audit.
