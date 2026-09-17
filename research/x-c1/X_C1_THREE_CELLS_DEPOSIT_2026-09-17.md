# X-C1-THREE-CELLS — Forschungsablage vom 17. September 2026

**Status:** AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN. Push zur Sicherung, kein Merge und keine Registry-Promotion.
**Vorhandener PR-#137-Head:** `192f443b4f1a26772e6c7d9d55fbf524ff1ee728`.
**Gelesener main:** `d18f545d8d0a662e978102f84341a5b11a40d5a4`.

## Gesicherter Umfang

[Originalnachweis](X_C1_THREE_CELLS_AND_INTERFACE.md), unverändert aus dem Gesprächspaket vom 16. September:
- konkrete drei getrennte Intervalle mit Prime-2- und Prime-3-Kopplung;
- H1-Quellenraum mit genau zwei GLOBALEN Mellinbedingungen;
- vollständige Gamma-Kopplung, induzierter Schur-Term `C_hat=C+BA*/c`;
- expliziter Output und Untergrenze `Q_W[u]>(53/100)||u||_2^2` auf genau W3;
- dritter Pivot des beschränkten Restblocks `Delta3>95749/90545 I>21/20 I`;
- Carleman-Nahtanalyse und ein separat typisierter bedingter Schur-Schritt.

Der Hinweis »keine Repoänderung« im Originalkopf beschreibt seine Entstehungsrunde am 16. September. Die jetzige Ablage ist die erste Übernahme dieses Dokuments in PR #137; der historische Text wird nicht rückwirkend umgeschrieben.

Die bereits vorhandene [Sechszellen-/Sparse-Graph-Spur](https://github.com/Waschtl904/objekt-x-programm/blob/192f443b4f1a26772e6c7d9d55fbf524ff1ee728/research/x-c1/X_C1_SPARSE_GRAPH_READOUT.md) bleibt vollständig erhalten. Deren dyadische Zellenfamilie und diese Prime-2/Prime-3-Dreizellengeometrie sind verschiedene Quellenfamilien. Keine Familie wird allein aus der Zellzahl als Verallgemeinerung der anderen ausgegeben; keine ungeprüfte familienübergreifende Verklebung.

## Präzise Grenzen für Folgeargumente

1. Der Carleman-Befund `||H_delta||_ess=pi/2` gilt für jede positive Zellbreite. Der bewiesene Vergleich `c_delta<pi/2` wird hingegen nur bei `delta=1/50` benutzt. Die Reserve ändert sich mit delta. **Kein allgemeines Verfeinerungs- oder Gershgorin-No-Go.** Der Originalnachweis §7.1 sagt das ausdrücklich.
2. Der Satz betrifft W3 mit H1-Topologie, nicht beliebige L2-Quellen mit eventuell unendlicher Gamma-Energie und nicht das ganze zusammenhängende Fenster.
3. I5 ist ein bedingter Schur-Schritt mit beschränktem positiv invertierbarem D und den angegebenen Momentabbildungen. Eine Kaskade muss die aktualisierten GLOBALEN Nebenbedingungen mitführen. Der Rang-zwei-Term ist kein in jeder Zelle erneut frei verfügbares Budget.
4. Die Normierung der Gesamtform und die vollständigen analytischen Operator-/Domainbeweise bleiben Teil des externen Prüfauftrags. Ein erfolgreicher Konstantenprüfer ist keine unabhängige mathematische Freigabe.

## Bytes und lokale Ausführung

Der [Prüfer](../../scripts/check_x_c1_three_cell_constants.py) ist bytegleich mit `check_triple_constants.py` aus dem ursprünglichen ZIP; nur sein Repository-Dateiname wurde angepasst.

| Gegenstand | Git-Blob-SHA1 | SHA-256 |
|---|---|---|
| Originalnachweis (21238 Bytes) | `2213eb7a50f140e5b197bb03413f714129d2528a` | `6bf7ce695d75fe3216e796be1817b4c4cf0f28a97658e0e835139ac4085140ef` |
| Unveränderter Prüfer (7411 Bytes) | `cacbc65e110a02ffa56c5a0d7d9a583243cbec5b` | `29da10271e906298a2863b868633acf63c33bb17c4fb785191c9cd1e2a1530d2` |

Am 17. September 2026 lokal mit Python 3.13.5 ausgeführt: **35 exakte rationale/skalar-algebraische Checks PASS, Exit 0**. Neuer Standardoutput und Ergebnis-JSON waren bytegleich zu den beiden archivierten Ausgaben. Kein A1-/C0-Replay und kein neuer Großlauf.

```text
triple_checks.log (1923 Bytes)
sha256 4854f9ba1ec8b35477582445fcdec44c0cd24817696cea57ac7854fdfef8b2ef
triple_rational_results.json (2377 Bytes)
sha256 1762ba3f8824d303364cbaf3f33ba86d9f7390bf0a2ba955bc82bce1b3fbdaa2
```

Originales Gesprächsarchiv: `X_C1_Dreizellen_2026-09-16.zip`, SHA-256 `6fd8af8fe15eb18eafa206a7eed3119e62b104d9e56f801820f39538c80376a5`. Seine vier Manifesteinträge wurden bei dieser Ablage geprüft. Das ZIP wird hier nicht als GitHub-Release-Asset behauptet; diese Ablage sichert Nachweis und ausführbaren Quellcode unmittelbar im Git-Baum.

Reproduktion ohne Dateien im Arbeitsbaum zu erzeugen, vom Repository-Root:

```bash
repo_root="$(pwd)"
work_dir="$(mktemp -d)"
(
  set -e
  cd "$work_dir"
  python "$repo_root/scripts/check_x_c1_three_cell_constants.py" > triple_checks.log
  cat triple_checks.log
  sha256sum triple_checks.log triple_rational_results.json
)
```

## Reviewgrenze und nächste Arbeit

Merge erst nach einem ausdrücklich auf den dann festgehaltenen Stand bezogenen externen Review der neuen analytischen Aussagen und dem dafür bestimmten Auftrag. Kein pauschales APPROVE für den wachsenden Gesamt-PR.

Die konstruktive Hauptaufgabe bleibt die nahtverträgliche Erweiterung auf die vollständige Quellenklasse: positive Gamma-Differenzenergie erhalten, Prime-Kopplungen gemeinsam buchen, die zwei globalen Momente korrekt transportieren. Diese Ablage ist kein Anlass für einen neuen Navigationspatch oder A1-Selbstaudit.

Unverändert bleiben main, Registry, A1/#131, ursprüngliche C0/C1-Texte und die vorhandene Sparse-Graph-Konstruktion. Kein vollständiger X-C1-GEOM-Abschluss, all-window NP-GAP-, RH- oder Neuheitsclaim. Kein neuer Workflow, angeforderter CI-Lauf, Merge oder Auto-Merge.
