# Abnahme vor dem endgültigen Prüflauf

Scope: eine neue K-Untergrenze mit matrixwertigem F-Fehler und ein festes
Young-Gewichtspaar auswählen. Nur gerade, alter physischer Zeuge und äußere
Antwortregel unverändert. Keine neue Integration und kein vollständiger
Energienachweis. Vorläufige Modellauswertungen sind Kandidatenauswahl.

Pflichtprüfungen:

- Vollständiges E_F und D_lower gegen die gebundenen Common96-Quellen prüfen.
- Matrix-Young-Herleitung und monotone Übertragung des vollständigen
  Restzertifikats auf K_neu >= K_star nachvollziehen.
- Rationale Kandidatenmatrix nach unten einschließen; positive rationale
  Pivots für K_neu-K_star und den Abstand zur eingeschlossenen zulässigen
  Obergrenze des Kandidaten prüfen.
- Exakte Gewichtszulässigkeit und nichtkommutierende rationale Kontrollfälle;
  den ungültigen Preis ohne den Faktor 1+1/epsilon im Fehlerterm abweisen.
- Auswahl aus unveränderlichen, hashgeprüften Eingaben reproduzieren;
  frischer Paketarchiv-Replay der Ergebnisdatei bytegleich. Kein Replay
  historischer Integrationen und kein erneuter historischer Großlauf.
- Unabhängiger Standardbibliothek-Audit der rationalen Matrixabstände,
  Gewichte und Modelldiagnose-Endpunkte; fehlende/manipulierte Eingaben sowie
  optimierten Python-Modus zurückweisen.
- Registry-Validator, erzeugte Ansichten, bestehende Registry-Tests,
  Diff-/Scope-Kontrolle und anwendbare CI.

Nicht Bestandteil: neue gerichtete Teilenergie, 287er-Zertifizierung einer
neuen P-Obermatrix, R_L-Rechnung, externe Prüfung oder Merge. Die
203er-Modellrechnung und der 84er-Modelluntertest dienen nur der Auswahl.
Ein kleiner Modellabstand wird nicht zur tatsächlichen Reserve erklärt.
