# Forschungsstand 5.–11. November 2026

**Erste feste Restspalte projektintern abgenommen. Zweite Restenergie und
gemeinsamer Zweiraumabschluss offen. Punkt 4 und externe Begutachtung offen.
Kein neuer physischer Hauptlauf begründet.** Alle Aussagen unter H1–H4 und den
übernommenen physischen Verträgen. Dies ist ein lokaler Integrationskandidat;
GPT1s Prüfung der Integrationsformulierungen und öffentliche Freigabe stehen aus.

| Bestandteil | Tatsächlicher Status | Belege |
| --- | --- | --- |
| Ganzkernlauf, 5. November | Ausgeführt, EINSCHLIESSUNG_UNENTSCHIEDEN; Startvorprüfung vorhanden, spätere Ergebnisabnahme nur berichtet | [Laufbericht](originals/gpt2-run-2026-11-05/BERICHT.txt), [Startvorprüfung](originals/gpt1-start-review-2026-11-05/GPT1_ABNAHME.txt) |
| Restbrücke, 9. November | Autorenherleitung; ganze q-Restkontrolle offen | [Herleitung](originals/gpt1-bridge-2026-11-09/ANALYTISCHE_BRUECKE.txt) |
| Budget, 10. November | Projektintern reproduziertes positives Budget unter übernommenen Verträgen | [Befund](originals/budget-review-2026-11-10/review_20261110/GEZIELTE_ABNAHME_UND_ENTSCHEIDUNG.txt) |
| Erste Restspalte | Ganze Energie hinreichend klein, unabhängige gezielte GPT2-Abnahme | [GPT1](originals/gpt1-first-column-2026-11-11/HERLEITUNG.txt), [GPT2](originals/gpt2-first-column-2026-11-11/Objekt-X-GPT2-Abnahme-Erste-Restspalte-2026-11-11.txt) |
| Zweite Restspalte | Bedingter C2-/Qq-Zahlenschluss bestätigt; ganze Energie nicht erreicht | [GPT2](originals/gpt2-second-column-2026-11-11/Objekt-X-GPT2-Zweitspaltenanschluss-und-Herkunftsluecke-2026-11-11.txt) |
| Native Herkunft | Drei Originalbindungen offen; abhängige Aussagen bleiben bedingt | [Herkunftslücken](NATIVE_PROVENANCE.md) |

Die [Datenkarte](originals/gpt2-data-map-2026-11-10/Objekt-X-GPT2-Statische-Restdatenkarte-2026-11-10.txt)
bleibt unverändert historisch erhalten. Ihre Erstspaltenlücke wird durch die
spätere Abnahme überholt, nicht stillschweigend aus dem Original entfernt.

[SOURCE_INDEX.json](SOURCE_INDEX.json) bindet jedes Archiv und jede lesbare
Originalkopie. Das vollständige große November-5-Archiv ist unverändert als
Release-Asset vorgesehen; [RELEASE_ASSETS.json](RELEASE_ASSETS.json) nennt Größe,
Hash und Ziel. Es ist noch nicht veröffentlicht. Die Vorbereitung liegt bereits
im Originalarchiv. Fehlende GPT1-Originale werden weder rekonstruiert noch als
vorhanden bezeichnet. [PROOF.md](PROOF.md) und [SCOPE.json](SCOPE.json) ordnen die
Belege zu, ohne einen neuen vollständigen Forschungsstand zu promoten.

## Vorab festgelegte Pflichtprüfungen dieser Integration

- Hash und Größe aller acht vorhandenen Originalarchive; Bytegleichheit aller
  veröffentlichten lesbaren Originalkopien mit ihren konkreten Archivmitgliedern.
- Vollständiger Paketmanifestabgleich und Prüfung der expliziten Statusgrenzen.
- Ein begrenzter Reproduktionstest des bereits vorhandenen rationalen
  Zweitspalten-Zahlenschlusses im portablen Paket; keine neue q-Auswertung.
- Schutzkontrollen gegen veränderte Bytes und falsche Abschluss-/Herkunftsaussagen.
- Deterministische Registeransichten, Registry-Validator samt Tests,
  Active-Front-Check, lokale Linkprüfung und Git-Diffprüfung.
- Prüfung der bereits im Register gepinnten historischen Integrations-CI;
  neue PR-/Merge-CI erst nach einer gesondert freigegebenen Veröffentlichung.

Der Erstspaltennachweis, der Budgetlauf und historische Großrechnungen werden
bei dieser Integration nicht nochmals ausgeführt. Ihre Belege bleiben unverändert.
Die technischen Integrationschecks sind keine neue mathematische Abnahme.

Lokaler Paketcheck: `python -B verify_integration.py --asset-dir PFAD_ZU_RELEASE_ASSETS`.
Ohne `--asset-dir` werden in CI nur die Git-Dateien und gebundenen Archivkopien
geprüft; der große Originalasset-Hash wird dabei ausdrücklich nicht erneut geprüft.
