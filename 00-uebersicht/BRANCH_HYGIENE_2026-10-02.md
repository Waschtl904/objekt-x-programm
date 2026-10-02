# Branch-Bereinigung vom 2. Oktober 2026

Geprüfte Main-Basis: `95a916a18b3b61d239b52cc15c2ee6c420980a94`.
Der Nutzer hat die Bereinigung vollständig integrierter, inaktiver Branches
ausdrücklich beauftragt.

## Ergebnis

Von 26 Remote-Branches wurden **23 vollständig integrierte, ungeschützte
Branches ohne offene PRs** gelöscht. Für jeden Head wurde die Abstammung in
Main geprüft. Die atomare Löschung war an die zuvor gelesenen Commit-IDs
gebunden; eine zwischenzeitliche Änderung hätte sie abgebrochen.

Erhalten bleiben:

- `main`;
- `research/q11-wall-a13-prep-2026-09-28`: [PR #187](https://github.com/Waschtl904/objekt-x-programm/pull/187), acht eigene Commits bei dieser Bestandsaufnahme;
- `research/x-c1-inherited-resonance-shell-schur-2026-09-18`: eingefrorener
  `KEEP_AUDIT`-Anker, geschützt durch [Ruleset 24067043](https://github.com/Waschtl904/objekt-x-programm/rules/24067043).

**Alle 102 Tags bleiben unverändert:** 101 unter `archive/...` und
`a1-comp-2026-09-16`. Die vollständigen Tag-Referenzen wurden vor und nach
der Löschung verglichen. Schutzregeln wurden nicht verändert.

Diese Zahlen beschreiben den Abschluss der Bereinigungscharge. Neue aktive
Arbeitsbranches können danach hinzukommen. Der Dokumentations-PR für diesen
Bericht wird nach seinem Merge und grüner Main-CI ebenfalls bereinigt.

## Wiederauffindbare Heads

Die Commits bleiben über Main erreichbar. Das Löschen eines Branchnamens
entfernt keine integrierten Dateien oder Commits. Bei Bedarf kann ein Branch
vom hier gebundenen Commit wieder angelegt werden.

| Gelöschter Branch | Letzter Commit |
| --- | --- |
| `docs/canonical-adaptive-odd-angle-registry-2026-10-02` | [`1b8ff3e1b804`](https://github.com/Waschtl904/objekt-x-programm/commit/1b8ff3e1b8046030f7fd9015be9d2a3f133f39e9) |
| `docs/canonical-cross-high-response-registry-2026-10-01` | [`ef173884c3d1`](https://github.com/Waschtl904/objekt-x-programm/commit/ef173884c3d1131229a1dfb2fefb61f60dd91f7c) |
| `docs/canonical-joint-maximizers-registry-2026-09-30` | [`4e5647bf7865`](https://github.com/Waschtl904/objekt-x-programm/commit/4e5647bf7865aa4078f79546dcb409f666861f76) |
| `docs/canonical-odd-structural-open-registry-2026-10-01` | [`ef10c9b01210`](https://github.com/Waschtl904/objekt-x-programm/commit/ef10c9b012100c48a1c6894f8b782130a6fd5ae8) |
| `docs/canonical-primal-dual-y68-registry-2026-10-02` | [`d8f12e999b46`](https://github.com/Waschtl904/objekt-x-programm/commit/d8f12e999b46c27555708759b750058022cffac4) |
| `docs/current-front-and-repo-hygiene-2026-10-02` | [`95a916a18b3b`](https://github.com/Waschtl904/objekt-x-programm/commit/95a916a18b3b61d239b52cc15c2ee6c420980a94) |
| `docs/objekt-x-gesamtueberblick-2026-09-28` | [`254eaac4d481`](https://github.com/Waschtl904/objekt-x-programm/commit/254eaac4d48120f4020a38b8b553b6f133559b5d) |
| `docs/p11-gamma-scope-clarification-2026-09-28` | [`b719e0dbafb1`](https://github.com/Waschtl904/objekt-x-programm/commit/b719e0dbafb11c20fb132a19e72db194a9ca75df) |
| `docs/p12-scope-injectivity-2026-09-28` | [`46b699e1ef8d`](https://github.com/Waschtl904/objekt-x-programm/commit/46b699e1ef8d7c0477f05f8fc3da5d0bac8941f7) |
| `docs/project-entry-nachpflege-2026-09-27` | [`d6f975d9a56f`](https://github.com/Waschtl904/objekt-x-programm/commit/d6f975d9a56f5c0bf11478a7f49f080189734a78) |
| `fix/early-adelic-audit-clarifications-2026-09-27` | [`ec54213e6b2b`](https://github.com/Waschtl904/objekt-x-programm/commit/ec54213e6b2b81e92d969db0916cfb5985cf567c) |
| `fix/m4-gamma-normalization-2026-09-27` | [`7707397c2ffd`](https://github.com/Waschtl904/objekt-x-programm/commit/7707397c2ffd8f664c65d6b0198a973217d69ad5) |
| `fix/p02-port-firewall-2026-09-27` | [`a44519f725c3`](https://github.com/Waschtl904/objekt-x-programm/commit/a44519f725c379406fef0c9d87c567491a13f3f4) |
| `fix/p04-global-shift-firewall-2026-09-27` | [`d5be0f000b65`](https://github.com/Waschtl904/objekt-x-programm/commit/d5be0f000b6582e6e91148db8a4f4075c1841f32) |
| `fix/p07-rh-free-herglotz-typing-2026-09-28` | [`0d5bcca302f8`](https://github.com/Waschtl904/objekt-x-programm/commit/0d5bcca302f8a04d3f89eb9f8f0ce8532a71769b) |
| `fix/suzuki-finite-window-firewall-2026-09-27` | [`d037184d877d`](https://github.com/Waschtl904/objekt-x-programm/commit/d037184d877db61cbfbe055ddb650db6716438a4) |
| `fix/weil-coordinate-sign-2026-09-27` | [`7d8c28578bb3`](https://github.com/Waschtl904/objekt-x-programm/commit/7d8c28578bb30db34e1401dda3814589844a4a66) |
| `research/canonical-adaptive-odd-angle-2026-10-02` | [`cb73f0ef223f`](https://github.com/Waschtl904/objekt-x-programm/commit/cb73f0ef223f4f3f0d51002f7d8127fac90a954f) |
| `research/canonical-cross-high-response-2026-10-01` | [`b91589923f57`](https://github.com/Waschtl904/objekt-x-programm/commit/b91589923f5738148c9c9702155fb3dc02f7b1a1) |
| `research/canonical-full-shift-primal-dual-2026-10-02` | [`219ab401013d`](https://github.com/Waschtl904/objekt-x-programm/commit/219ab401013d2d4d8f5d8d6e4807ef6407e4b5ff) |
| `research/canonical-joint-maximizers-2026-09-30` | [`2172de38d0de`](https://github.com/Waschtl904/objekt-x-programm/commit/2172de38d0def2c4b42c255e6c1290a720e3e94e) |
| `research/canonical-odd-structural-open-2026-10-01` | [`ed94c19f824c`](https://github.com/Waschtl904/objekt-x-programm/commit/ed94c19f824c947f63e4867fb3c202f71e36e631) |
| `research/first-chamber-o8-o9-2026-09-27` | [`3ee52c370cdb`](https://github.com/Waschtl904/objekt-x-programm/commit/3ee52c370cdb119c60fbef3f41fb0bfef0a09f93) |

## Künftige Pflege

Nach abgeschlossener Integration wird im Rahmen des jeweiligen Auftrags
geprüft, ob der Arbeitsbranch noch benötigt wird. Löschkandidaten haben
keine eigenen Commits gegenüber Main, keine offenen PRs und keine aktive
Nutzung. Geschützte Auditanker und Archivtags bleiben erhalten. Vor jeder
Löschung werden die tatsächlichen Heads erneut verglichen.

Es wurde keine pauschale automatische Löschung aktiviert. Die bestehenden
[Abnahme- und Freigaberegeln](../CONTRIBUTING.md) gelten weiter.
