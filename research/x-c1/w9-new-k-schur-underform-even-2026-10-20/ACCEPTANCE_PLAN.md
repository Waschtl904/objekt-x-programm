# Begrenzter Auftrag vor der Rechnung

20. Oktober 2026. Basis bf9375b26ecb2ad3060c91824501f460c060fc43.
Genau die unveränderte K_new-Unterform aus #245, derselbe physische gerade
Zeuge, äußere Antwortregel, K_P-Budget und dieselben gemeinsamen Paarungen.

1. Die ganze feste Young-Gewichtsfamilie ausschließlich algebraisch mit den
   rationalen Endpunkten von #246/#247 prüfen. C,B,D sind unverändert und
   nichtnegativ; die nötige Bedingung 1/(1-c)<=b0 wird separat geprüft.
2. Genau eine Mittelpunktslösung des neuen 84er-Systems rational einfrieren,
   vor der gerichteten Auswertung. Keine adaptive Suche oder zweite Richtung.
3. Vollständige Basis-, Paarungs-, F-J- und physische Residualfehler erneuern;
   die richtungsbezogene Formfehlerschärfung aus #239 für K_new verwenden.
4. Untergrenze > Budgetobergrenze: SCHUR_UNDERFORM_COMPARISON_EXCLUDED.
   Andernfalls SCHUR_LOWER_TEST_OPEN, kein Teilpass und keine Dualreserve.
   Offener Test rechtfertigt ohne quantitative Kontrolle der fehlenden Beiträge
   keine obere Großrechnung. Keine automatische Nachschärfung.
5. Harte Grenze 600 Sekunden pro vollständigem Aufruf (Auswahl, Zertifizierung,
   Replay). Technischer Abbruch ist keine mathematische Entscheidung.

Pflichtabnahme: Eingabe- und Paketbindungen; getrennt bytegleiche Auswahl und
Zertifizierung aus frischem vollständigem Git-Archiv; unabhängiger rationaler
Audit von Gewichtslemma, Formpreis und Endentscheidung; Negativkontrollen für
manipulierte/fehlende Eingaben, Python -O und unzulässige Passbehauptungen;
Register, erzeugte Ansichten, Active-Front-Prüfung und 60 Registry-Tests.
Die vorhandenen großen Integrationen und 287er-Pivots sind gebundene
Voraussetzungen, kein erneuter lokaler Pflichtlauf. Anwendbare CI erforderlich.
AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN; Punkt 4 und N12 bleiben offen.
