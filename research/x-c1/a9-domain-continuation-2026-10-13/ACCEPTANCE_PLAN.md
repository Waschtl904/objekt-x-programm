# Vorab festgelegte Abnahme

14. Oktober 2026, vor dem neuen Integrationslauf. Nutzerauftrag: vorhandene
Ergebnisse in mehreren Schritten pushen und mergen. Dieser PR integriert
`A9-DOMAIN-FLOOR-LOCAL-CONTINUATION` samt Originalarchiv, Beweisanschluss und automatischem Replay.
Änderungsklassen: Mathematik (Claim/Belegbindung), Infrastruktur (Replay/CI),
Dokumentation. Frühere globale Verifikations- und externe Reviewstatus bleiben.

Pflichtprüfungen: vollständige Byte- und Mitgliedsprüfung der Archive und
lesbaren Originalkopien; unveränderter rationaler Paket-Replay mit ursprünglichem
Schur-Feldabgleich; identische mathematische Quittung; Gegenkontrollen für
Beschädigung, Pfade, fehlschlagende Unterprüfer und relevantes/irrelevantes
CI-Routing; Registry-Generator, bestehender Statusvalidator samt Tests,
historische Front, neue lokale Links und Diff. Anwendbare CI am finalen
PR-Head und anschließend am tatsächlichen Mergecommit muss erfolgreich sein.

Die neue analytische Herleitung und ihre Voraussetzungen werden als
AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN übernommen, nicht als extern begutachtet.
Große Vorgängerintegrationen werden nicht wiederholt. Die Registrierung der
beiden A9-Folgepakete erfolgt nach ihren tatsächlichen Merges separat.
