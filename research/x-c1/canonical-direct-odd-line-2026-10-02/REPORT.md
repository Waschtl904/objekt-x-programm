# Direkte gemeinsame ungerade Eigenlinie

**Ergebnis: UNRESOLVED für die gesamte verstärkte Familie.** Die direkte
Linienrechnung verbessert zwei bedingte Schnitte deutlich, isoliert aber
weder die gesamte Ausgangsbox noch eine der acht terminalen Diagnoseboxen.

`AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN` · lokales, noch nicht integriertes Paket.

## Was der Test tatsächlich verbessert

- Der zentrale Vier-Y-Schnitt fällt von einer oberen Gesamtwinkelhülle von
  **163.162463° auf 3.405363°**.
- Der Vier-Y-Schnitt `quarter` fällt von **165.457773° auf 3.765366°**.
- Dabei bleiben alle übrigen Y- und Momentintervalle frei. Beide Aussagen
  gelten nur auf ihrem jeweiligen bedingten Schnitt.
- Alle fünf vollständig bekannten zulässigen Punkte werden auf dem
  **maximalen Eigenwertast** zertifiziert. Das zentrale Modell ist darunter.
- Die volle Familie und alle acht Endboxen bleiben unentschieden. Die Zahl
  180° bezeichnet dort nur den trivialen Rückfallwert bei fehlender
  Linienisolation, keinen errechneten tatsächlichen Winkel.

Damit ist ein Teil des bisherigen Einschließungsverlusts konkret nachgewiesen.
Eine uniforme ungerade Lokalisierung folgt daraus weiterhin nicht.

## Drei kleine, vergleichbare Rechnungen

Alle Rechnungen verwenden dieselben 19 Fälle: Ausgangsbox, fünf bekannte
vollständige Punkte, deren fünf Vier-Y-Schnitte und acht frühere Diagnoseblätter.
Es wurden keine neuen Operatorintegrale, Y58-Dualdaten oder L_B-Daten erzeugt.

1. **Direkte Linie:** Die positive Skalierung M_tilde=det(L) M entfernt die
   L-Inverse aus der Richtungsrechnung. Die quadratische Gleichung für (s,1)
   ersetzt M^{-1}R und das Projektorprodukt KK^*.
2. **Zentrierte Kompression:** N=N_0+E erhält gleiche Faktoren in den
   Momentkompressionen. Alle Restterme sind enthalten.
3. **Gemeinsame affine Form:** 156 Eingabesymbole werden durch N,G,L,Z,
   die Polynomkoeffizienten und die Endpunkt-/Ableitungstests mitgeführt.
   Nichtlineare Reste und sämtliche Rundungsfehler werden bezahlt.

Eine akzeptierte Linie besitzt uniforme entgegengesetzte Endpunktvorzeichen
und positive Ableitung. Damit ist sie eindeutig und maximiert den
generalisierten Rayleighquotienten. Die Newton-Schritte verkleinern ihre
Hülle. Der physische Winkel wird direkt an N(s,1) im G_B-Skalarprodukt bestimmt.
Alle Tabellenwerte sind obere **Gesamtwinkelhüllen**, also zweimal die obere
Abweichung von derselben festen Referenz.

| Fall | Bisher | Direkt | Zentriert | Gemeinsame affine Form |
| --- | ---: | ---: | ---: | ---: |
| root | 180.000000° | offen | offen | offen |
| point/central | 1.903077° | 1.903077° | 1.903077° | 1.903077° |
| slice/central | 163.162463° | 5.864042° | 5.864042° | 3.405363° |
| point/half | 2.180335° | 2.180335° | 2.180335° | 2.180335° |
| slice/half | 169.585133° | offen | offen | offen |
| point/two_thirds | 2.360824° | 2.360824° | 2.360824° | 2.360824° |
| slice/two_thirds | 174.899164° | offen | offen | offen |
| point/five_eighths | 2.316013° | 2.316013° | 2.316013° | 2.316013° |
| slice/five_eighths | 173.231350° | offen | offen | offen |
| point/quarter | 1.967736° | 1.967736° | 1.967736° | 1.967736° |
| slice/quarter | 165.457773° | offen | offen | 3.765365° |
| terminal/rLLLLL | 179.880789° | offen | offen | offen |
| terminal/rLRLLLLRRLRL | 180.000000° | offen | offen | offen |
| terminal/rLRLLRLRRLRL | 180.000000° | offen | offen | offen |
| terminal/rLRRLLRRLLLL | 180.000000° | offen | offen | offen |
| terminal/rRRLLLLLLLR | 178.492590° | offen | offen | offen |
| terminal/rRRLLLRRR | 177.914891° | offen | offen | offen |
| terminal/rRRLLRRRR | 178.059773° | offen | offen | offen |
| terminal/rRRRR | 178.054653° | offen | offen | offen |

## Prüfung und Reproduktion

Die algebraischen Kontrollen umfassen 40 skalierte Stifte, 160 exakte
Stationaritäts-/Rayleigh-Identitäten, Kontrollen gegen den minimalen Ast und
Entartung, 486 affine Punkt-/Rundungskontrollen und 16 zentrierte Kontrollen.
Der separate rationale Audit bestätigt 19 akzeptierte maximale Wurzelhüllen
über die drei Varianten und 124 Newton-Schritte. Arb mit 768 Bit prüft elf
verschiedene Winkelobergrenzen. Die Kontrollen ersetzen nicht den Beweis;
die Herleitungen und Aussagegrenzen stehen in `PROOF.md`.

`replay.py --out <neues Verzeichnis>` rechnet alle 57 Fälle erneut und
verlangt bytegleiche Vergleichs-, Kontroll- und Auditquittungen. Python 3.13
und python-flint 0.9.0 genügen. Das Originalpaket mit 41 Dateien ist unter
`inputs/baseline` unverändert enthalten. Das Manifest bindet alle Dateien.

## Nächster offener Schritt

Die jetzige affine Näherung bezahlt nichtlineare Abhängigkeiten teilweise
noch als getrennte Restfehler. Außerdem behandelt sie die Einträge der
vorhandenen Y-left-Inversenhülle als unabhängige Symbole. Der Test ist daher
kein Ausschluss stärkerer gemeinsamer Verfahren. Ein gezielter nächster
Test sollte diese Reste und die Inversenbeziehung genauer erhalten, etwa mit
einem höheren Taylor-Modell oder einer durch die gemeinsamen Momentbedingungen
eingeschränkten Wurzelsuche. Ein neuer großer Vier-Y-Baum wurde nicht gestartet:
in keiner der acht repräsentativen Endboxen gelang bereits eine Isolation.

Das Ergebnis beweist weder strukturelle Offenheit der verstärkten Familie
noch die Notwendigkeit neuer Operatorinformationen. Zufallssampling wird
nicht als Zertifikat verwendet. Allgemeines Renewal, A13-Positivität,
kofinale positive Familie, globales Objekt X und RH bleiben offen. PR #187
wird nicht verändert.
