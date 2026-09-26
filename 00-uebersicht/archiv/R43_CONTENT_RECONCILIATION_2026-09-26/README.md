# R43 — Inhaltszuordnung und Erhalt der drei historischen Fassungen

**HISTORICAL-SOURCE-PRESERVED / NO_MATHEMATICAL_PROMOTION**

Prüfbasis: `main@4526360b928a1a8e96f810ce8f939dda012262fa`. Dieser Nachtrag ergänzt ausschließlich die R43-Fälle U343, U344 und U543 der [datierten Inhaltskarte](../UNIQUE_BRANCH_CONTENT_MAP_2026-09-24.json) und des [Familienberichts](../UNIQUE_BRANCH_FAMILY_REVIEW_2026-09-24.md). Die ursprünglichen Eingangssnapshots bleiben unverändert. Die bereits abgeschlossenen 21er-/Zweier-Chargen, der Integritätsfall und die anderen Familien werden nicht neu bewertet.

## Entscheidung je Fassung

| ID / Branch | Befund am geprüften Main | Konkrete Zuordnung |
|---|---|---|
| U343 / `r43-full-rest-local-decay-cond-limit` | Weder Originalpfad noch Originalblob vorhanden. Die vorhandene feste-U-COND-Uniformität formuliert Normpräkompaktheit; sie ist kein vollständiger Ersatz für die hier behauptete quantitative RL17-Abschätzung und die RL22–RL27-Grenzwerte. | [Vollständige historische Fassung](U343.md), exakt eingebettete 24.243 Originalbytes. Keine Einstufung als unabhängig verifizierter Main-Satz. |
| U344 / `r43-post-c6-source-descent-weil-separation` | Weder Originalpfad noch Originalblob vorhanden. Der Feshbach-Nachfolger verwendet in §1 ausdrücklich den PR-#91-Zeugen und die Identität F1. Das belegt die Übernahme dieses Bausteins, aber nicht des gesamten Quellenabstiegs SD3–SD10 oder sämtlicher SD3–SD23-Ableitungen. | [Vollständige historische Fassung](U344.md), exakt eingebettete 19.636 Originalbytes. Der Quellenstatus „unabhängiger Review offen“ bleibt bestehen. |
| U543 / derselbe Post-C6-Branch | Weder Originalpfad noch Originalblob vorhanden. Das vorhandene rationale Feshbach-Skript prüft eine andere Implikation unter vorgegebenen Momentenschranken; es ersetzt nicht den damaligen 41-Kontrollen-Code für den glatten Primzahl-2-Zeugen. | [Vollständiger historischer Prüfcode als Text](U543.md), exakt eingebettete 5.263 Originalbytes. Keine neue Ausführung und kein neues Zertifikat behauptet. |

## Vorhandene Main-Bezüge und ihre Reichweite

1. [Feste-U-COND-Uniformität, CF1 und feste-U-Grenzen](https://github.com/Waschtl904/objekt-x-programm/blob/4526360b928a1a8e96f810ce8f939dda012262fa/audits/P11_R43_COND_FIXED_OLD_ALL_FUTURE_UNIFORMITY_2026-09-07.md) ist der einschlägige ältere Eingang zu U343. Die neue RL-Behauptung wird hier nicht daraus abgeleitet.
2. [Vor-ι′ Feshbach-Firewall, §1 und F1](https://github.com/Waschtl904/objekt-x-programm/blob/4526360b928a1a8e96f810ce8f939dda012262fa/audits/P11_VOR_IOTA_PRIME_FESHBACH_FIREWALL_2026-09-11/audit.md) nennt den PR-#91-Zeugen explizit. Dies ist ein konkreter Main-Bezug für den Primzahl-2-Kalibrierungsbaustein von U344, kein Nachweis einer vollständigen Text- oder Beweisübernahme.
3. [Rationale Feshbach-Implikation](https://github.com/Waschtl904/objekt-x-programm/blob/4526360b928a1a8e96f810ce8f939dda012262fa/scripts/check_vor_iota_prime_rational_certificate.py) behält ihren dokumentierten Scope. U543 bleibt daneben historische Provenienz.

Es wird kein ungeprüfter vollständiger Main-Nachfolger behauptet. Die konkret fehlenden drei Originalfassungen sind nun vollständig auffindbar und rekonstruierbar. Die administrative Inhaltslücke wird durch diese belegte Originalerhaltung geschlossen; eine offene mathematische Prüfung wird dadurch weder erledigt noch aufgewertet.

## Hashgebundene Quellen und rekonstruierbare Originalbytes

```json
[
  {
    "id": "U343",
    "source_commit": "112f611727dbd3386bff5e11b9a5d5d143cdee6b",
    "source_path": "audits/P11_R43_FULL_REST_LOCAL_RESOLVENT_DECAY_AND_COND_LIMIT_2026-09-07.md",
    "source_blob": "3ff0d0d696c9dc455a6fefec14f7856b7ded5f3e",
    "source_sha256": "e2685e56e971b33d5ff73a45faf8d640b0f308d9768470429de79738798a48e2",
    "original_bytes": 24243,
    "branch": "r43-full-rest-local-decay-cond-limit",
    "preserved_payload": "U343.md",
    "disposition": "HISTORICAL-SOURCE-PRESERVED",
    "mathematical_status": "INDEPENDENT_REVIEW_PENDING",
    "exact_source_path_or_blob_on_base_main": false,
    "payload_byte_equal": true
  },
  {
    "id": "U344",
    "source_commit": "1a6c8777c803bcf7ef34e74b9979578f05c5b40b",
    "source_path": "audits/P11_R43_POST_C6_SOURCE_DESCENT_AND_WEIL_SEPARATION_2026-09-08.md",
    "source_blob": "8729430feb850402e37d10e258c6451c052623bd",
    "source_sha256": "b1499976e8677a3c875ac04d32d16f79728016155b75c911569b16113285e57a",
    "original_bytes": 19636,
    "branch": "r43-post-c6-source-descent-weil-separation",
    "preserved_payload": "U344.md",
    "disposition": "HISTORICAL-SOURCE-PRESERVED",
    "mathematical_status": "INDEPENDENT_REVIEW_PENDING",
    "exact_source_path_or_blob_on_base_main": false,
    "payload_byte_equal": true
  },
  {
    "id": "U543",
    "source_commit": "1a6c8777c803bcf7ef34e74b9979578f05c5b40b",
    "source_path": "scripts/check_r43_post_c6_prime2_witness.py",
    "source_blob": "674bfb3502fdde9ff02930d117d20b4fd8a29bc0",
    "source_sha256": "22c7035c45a5f5bf3a9d758412903b0ee83c17ac60ffdfdad19c7ea4016fb003",
    "original_bytes": 5263,
    "branch": "r43-post-c6-source-descent-weil-separation",
    "preserved_payload": "U543.md",
    "disposition": "HISTORICAL-SOURCE-PRESERVED",
    "mathematical_status": "INDEPENDENT_REVIEW_PENDING",
    "exact_source_path_or_blob_on_base_main": false,
    "payload_byte_equal": true
  }
]
```

Jede Quelldatei besitzt einen klar markierten historischen Vorspann und einen einzigen äußeren Textblock mit zehn Backticks. Die Bytes zwischen dessen Eröffnungszeile und Schlusszeile stimmen exakt mit dem angegebenen historischen Blob überein. Der Hash bezieht sich auf diese Originalbytes, nicht auf die umgebende Markdown-Datei. Dadurch bleiben auch ursprüngliche relative Links als Quelltext erhalten, ohne auf neue Ziele umgeschrieben zu werden.

## Status- und Erhaltungsgrenzen

- Beide Quelltexte bezeichnen sich als analytische Kandidaten mit Autorengegencheck und offenem unabhängigem Review. Die Einbettung übernimmt diesen historischen Status; sie setzt keinen Claim auf VERIFIED oder MERGED in der kanonischen Forschungsregistry.
- Der in U344 gemeldete historische Lauf von 41 Kontrollen wird als damalige Angabe erhalten. Er wurde in diesem Übernahmepass nicht wiederholt und nicht als heutiger unabhängiger Beweis ausgegeben.
- O8, C6, globale Weil-Positivität und RH sowie `RESEARCH_STATE.yaml`, Beweisanker, aktive Certifier und Workflows werden nicht verändert.
- Zur späteren Entfernung der beiden historischen Branchzeiger sind ihre vollständigen Commit-Historien zusätzlich durch geschützte Archivtags und einen frischen Head-/Referenz-/Schutzabgleich zu erhalten. Diese Inhaltsdatei behauptet selbst keine ausgeführte Tag-Anlage oder Branchlöschung.

## Prüfung dieses Dokumentationstransfers

Pflichtprüfungen sind der bytegenaue Abgleich aller drei eingebetteten Quellen mit ihren historischen Blob- und SHA-256-Werten, der Diff-/Linkcheck, unveränderte kanonische Statusdateien sowie die anwendbare Registry-/Routing-CI am endgültigen PR-Head. Keine der historischen Quellen wird als ausführbarer Produktions- oder Prüfcode integriert. Ein neuer mathematischer Zertifikatslauf ist für diesen reinen Provenienztransfer nicht vorgesehen.
