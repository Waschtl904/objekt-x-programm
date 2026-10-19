# Begrenzte Inversmajoranten-Vorprüfung

18. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.

Die vermeidbare Reserve der Young-Gewichtung lässt sich rigoros reduzieren:
Bei unverändertem vollständigem Dualgewicht 11/10 sinkt der P-Faktor auf
1.045472 gerade bzw. 1.082998 ungerade. Es gilt
A9^-1 <= W_neu <= W9. Trotzdem überschreitet schon die gerichtete Teilenergie
das unveränderte K_P-Budget in beiden #238-Richtungen.

Gerade scheitert sogar die ganze untersuchte skalare Gewichtungsfamilie:
Der untergeordnete Hilfsvergleich mit P-Faktor 1 liegt noch >2.27301e-6 über
dem Budget. Er ist selbst keine Inversmajorante. Andere Majoranten und
Antwortmatrizen sind damit nicht ausgeschlossen.

Ein zulässiger Trade mit P-Faktor 1.02 besteht ungerade nur den Teiltest und
erhöht das Gewicht des offenen Dualterms. Gerade scheitert er weiterhin.
**Kein vollständiger neuer Lauf empfohlen.** Nächster Entscheidungspunkt:
strukturelle Verbesserung der U8-/K-/Schur-Untervergleiche mit konsistenter
Operatorordnung und gemeinsamer Fehlerkontrolle.

Antwortmatrix, beide Prüfrichtungen, Paarungen und K_P bleiben unverändert.
Keine neuen Integrationen oder R_L-Rechnungen. Meilenstein 4 bleibt offen.
Die ±1-%-Matrixvarianten aus der vorherigen Vorprüfung bleiben unentschieden.

```sh
python research/x-c1/w9-majorant-preflight-2026-10-18/preflight.py --check
```

`PROOF.md` enthält Herleitung, Fehlertransport, Aussagegrenzen und Aufwand.
`EXPECTED.json` enthält exakte rationale Intervalle und Gewichte.
`INPUT_BINDINGS.json` und `MANIFEST.json` binden Bestand und Prüfpaket.
`ACCEPTANCE.json` dokumentiert den frischen kleinen Replay und lokale Checks.

Der Forschungsbranch ist ein begrenzter Entwurf, nicht gemergt.
