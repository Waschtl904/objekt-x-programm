# Abnahme der Entscheidungsvorlage, vor dem Abnahmelauf festgelegt

Mathematische Änderung: lokaler Zwölfer-Featurefehler und zulässige größere
K-Untergrenze; Herleitung des gemeinsamen Schuranschlusses; Auswahl eines Piloten.
Historische Eingaben und Zertifikate bleiben unverändert.

Verpflichtend:

- E_F als vollständigen Zwölfer-Featurefehler und D96_lower als tatsächliche
  Untergrenze gegen gebundene Herleitung und Erzeuger prüfen.
- Zwölf positive Pivots für G_F und zwölf für den Zulässigkeitsabstand von K_star.
- Gemeinsamen Anschluss (E_star>=E, unveränderte R/M, neues nu) prüfen;
  K nicht mit äußerem K_P verwechseln.
- Entscheidungsevidenz aus frischem Git-Paketarchiv bytegleich reproduzieren;
  alle übernommenen Repository-Eingaben dabei per Hash prüfen. Kein erneuter
  vollständiger Repository- oder Großintegrations-Replay gefordert.
- Python -O und manipulierten gebundenen Paketinhalt abweisen.
- Registry-Validator, erzeugte Ansichten, bestehende Registry-Tests und
  Diff-/Scope-Kontrolle. Remote Tree gleich dem lokal geprüften finalen Tree.

Nicht ausführen: P_star-Aufbau, neue Teilenergie, U8-/Schur-Piloten,
R_L-Rechnung, neue Integration, externe Prüfung oder Merge. Das feste
Protokoll des ausgewählten späteren Piloten steht in PROOF.md Abschnitt 7.
