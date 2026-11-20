# Begrenzte Datenprüfung für eine geänderte Antwortmatrix

Ergebnis: **NO_DATA_SUPPORTED_RESPONSE_CANDIDATE**. Die alten Residualdaten
und die späteren K-/Schur-Daten liefern die fehlenden Antwortkreuzpaarungen
nicht nach. Es wird keine Matrix ausgewählt und keine Variante ausgeschlossen.

[Herleitung und Entscheidung](PROOF.md): Eine feste eindimensionale Änderung
benötigt nur zwei neue gewichtete Energiekoeffizienten samt vollständiger
Fehlerkontrolle. Das ist eine Datenspezifikation, kein gestarteter Pilot.

Vorab festgelegte Pflichtprüfung dieses Pakets: Eingabebindungen, Schema und
gemeinsame Zeugenherkunft; exakte rationale Kontrollen der gemeinsamen
Budget-/Energieänderung, der symmetrischen Updateformel und eines Gegenmodells
zur Rekonstruktion fehlender Kreuzinformationen; bytegleicher isolierter
Replay. Keine neue Quadratur, Optimierung, RL-Rechnung oder Wiederholung
unveränderter großer Zertifikatsläufe. Externe Prüfung bleibt offen.

Aus dem Repository, Python >=3.10, nur Standardbibliothek:

```sh
python research/x-c1/w9-response-information-gate-2026-10-20/verify.py --check
```

Die Ausgabe `RESULT.json` enthält Datenbefunde und Algebra-Kontrollen, keine
neue gerichtete Objekt-X-Energie. `INPUT_BINDINGS.json` benennt den Prüfumfang;
die geerbte mathematische Eingabekette wird dadurch nicht erneut abgenommen.
`ACCEPTANCE.json` dokumentiert den isolierten Replay dieses Umfangs.

Historische Belege und das Forschungsregister bleiben unverändert. Punkt 4,
N12 und die Auswahl eines aussichtsreichen neuen Vergleichs bleiben offen.
