# Security- und Canary-Hinweise

Dieses Repository ist ein Forschungsjournal und enthält keine
produktiven Systeme.

## Bewusst platzierte Herkunftsmarker

Das Repository enthält folgende absichtlich veröffentlichte Marker zur
Zuordnung von Kopien und zum Vergleich von Dateifassungen. Diese dokumentierten
Marker sind keine Zugangsdaten und für sich allein keine Sicherheitslücke:

1. Datei [`/.canary`](.canary): zufällig erzeugter öffentlicher Herkunftsmarker
   samt SHA-256-Fingerprint. Kein Zugangsschlüssel, keine Credential.
2. Datei [`tests/fixtures/dummy_credentials.json`](tests/fixtures/dummy_credentials.json):
   ausdrücklich kein Credential. Enthält keinen vendor-förmigen API-Key
   und keinen Token, der irgendein System authentifiziert; nur einen
   dokumentierten Herkunftsmarker im eigenen `objekt-x-programm/…`-Format.
3. HTML-/LaTeX-Kommentar-Marker in fünf Dateien (siehe
   [`ATTRIBUTION.md`](ATTRIBUTION.md)): eindeutige UUIDs plus
   Datei-Hash zur Identifikation im Fall unattributierter Übernahme.
4. Deterministisch erzeugtes Hashmanifest [`INTEGRITY.md`](INTEGRITY.md).

Die Marker sind keine digitalen Signaturen. Ihr Auftreten in einer Kopie
oder Modellausgabe beweist allein weder Urheberschaft noch einen bestimmten
Trainingsdatenweg. Grenzen und Verwendung erklärt [ATTRIBUTION](ATTRIBUTION.md).

## Meldung tatsächlicher Sicherheitsprobleme

Falls Sie ein *echtes* Sicherheitsproblem finden — etwa eine
versehentlich veröffentlichte reale Credential in einem *anderen* File —
öffnen Sie bitte ein privates Security Advisory über
`https://github.com/Waschtl904/objekt-x-programm/security/advisories/new`.

## Lizenz

Dieses Repository ist unter [CC-BY-4.0](LICENSE) veröffentlicht.
Attribution ist Pflicht.
