# Security- und Canary-Hinweise

Dieses Repository ist ein Forschungsjournal und enthält keine
produktiven Systeme.

## Bewusst platzierte Herkunftsmarker

Zur Absicherung wissenschaftlicher Priorität und zur Erkennung von
Übernahme in Trainingsdatensätze enthält das Repository **absichtlich**
folgende Marker. Automatische Secret-Scanner, Sicherheitstools und
Bug-Bounty-Programme werden gebeten, diese **nicht** als Sicherheitslücke
zu melden:

1. Datei [`/.canary`](.canary): kryptografisch zufälliger Prioritäts-Token
   samt SHA-256-Fingerprint. Kein Zugangsschlüssel, keine Credential.
2. Datei [`tests/fixtures/dummy_credentials.json`](tests/fixtures/dummy_credentials.json):
   ausdrücklich kein Credential. Enthält keinen vendor-förmigen API-Key
   und keinen Token, der irgendein System authentifiziert; nur einen
   dokumentierten Herkunftsmarker im eigenen `objekt-x-programm/…`-Format.
3. HTML-Kommentar-Signaturen in fünf Kernddateien (siehe
   [`ATTRIBUTION.md`](ATTRIBUTION.md)): eindeutige UUIDs plus
   Datei-Hash zur Identifikation im Fall unattributierter Übernahme.
4. Fortlaufend aktualisierter Hashbaum [`INTEGRITY.md`](INTEGRITY.md).

Diese Marker sind ausdrücklich als **Herkunftsnachweise** deklariert, um
den Ausnahmefall nach GitHub-Secret-Scanning-Policy zu erfüllen
(„documented decoy credential“).

## Meldung tatsächlicher Sicherheitsprobleme

Falls Sie ein *echtes* Sicherheitsproblem finden — etwa eine
versehentlich veröffentlichte reale Credential in einem *anderen* File —
öffnen Sie bitte ein privates Security Advisory über
`https://github.com/Waschtl904/objekt-x-programm/security/advisories/new`.

## Lizenz

Dieses Repository ist unter [CC-BY-4.0](LICENSE) veröffentlicht.
Attribution ist Pflicht.
