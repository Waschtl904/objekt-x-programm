# H₀-Folgeuntersuchungen und Grenzen der Cut-Relaxation

Stand 3. Oktober 2026. **Root bleibt UNRESOLVED.** Die ursprünglichen lokalen
Pakete werden hier mit vollständiger Quellenkette und unveränderten Bytes
zugänglich gemacht. Mathematische Aussagen: `AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN`.
Die Aufnahme ins Repository und eine Registereintragung sind getrennte Schritte.

## Ergebnis und Belege

| Untersuchung | Ergebnis | Originalbericht |
| --- | --- | --- |
| Rücktest | Der untersuchte Relaxationszeuge ist physisch unzulässig; kein Ausschluss seiner ganzen Vier-Y-Faser. | [Rücktest](reports/pullback/REPORT.md) |
| Endpunkte und zwei H₀-Cuts | Neun maximale Linien; bedingter Gesamtwinkel auf five_eighths ≤4.933780°. Von 783 gespeicherten Zielen verbessern sich 271 nach den geerbten Koeffizientenschnitten; kein positiver Root-Rand. | [Endpunkt- und Multiplikatortest](reports/root/REPORT.md) |
| Drei-Cut-Relaxation | Ein exakt geprüfter Punkt erfüllt drei Cuts, hat ein überall negatives Surrogat und ist durch eine andere H₀-Richtung ausgeschlossen. Diese letzte Relaxation reicht nicht; kein Gegenbeispiel zur tatsächlichen Familie. | [Grenznachweis](reports/three_cut/REPORT.md) |

Die Schlussketten und Grenzen stehen in [PROOF.md](PROOF.md). Angaben wie
„lokal“, „GitHub nicht verändert“ und „PR ungemergt“ in den Originalberichten
beschreiben deren Entstehungsstand. Die aktuelle Integration steht im
[Forschungsregister](../../../00-uebersicht/RESEARCH_STATE.yaml).

Der spätere [übermittelte GPT-1-Bericht](reported/GPT1_H0_BLOCK_45.txt) behauptet
auch die Unzulänglichkeit des gesamten Hauptblocks (4,5). Seine neuen
Originalprogramme und Rechenquittungen wurden hier nicht geliefert.
**Seine Zahlen werden deshalb nicht als hier reproduziertes Zertifikat geführt.**
Die bekannte Drei-Cut-Unzulänglichkeit ist davon unabhängig nachgerechnet.
Keiner dieser Befunde entscheidet die vollständige H₀-Bedingung.

## Reproduktion

Vom Repository-Stamm mit Python 3.13:

```text
python -m pip install -r research/x-c1/canonical-h0-followups-2026-10-03/requirements.txt
python -B research/x-c1/canonical-h0-followups-2026-10-03/replay.py --output ../h0-followup-replay
```

Das Ausgabeverzeichnis muss neu sein und außerhalb des Repositorys liegen.
Der Wrapper prüft das äußere Archiv, entpackt die drei vollständig enthaltenen
Pakete, prüft jeden Datei-Hash und führt ihre Berechnungen und Audits aus.
Das äußere Archiv enthält die beiden früheren ZIPs bytegleich; sie werden
im Repository nicht nochmals separat gespeichert. Nach dem Entpacken stehen
sämtliche Skripte, Eingaben und Ergebnisquittungen zur Verfügung.

Der Lauf umfasst Rücktest und Faktoren-Audit, Endpunkt- und Cut-Erzeugung,
exakte Prüfung aller 783 gespeicherten Multiplikatorzertifikate sowie alle
acht Drei-Cut-Ergebnisquittungen. Er wiederholt keine Gleitkomma-Suche und
keine ursprünglichen Operatorintegrale. Der gemeinsame Y-Kernel hat seinen
[eigenen vollständigen 19-Fall-Replay](../canonical-y-kernel-second-order-2026-10-03/README.md).

[SOURCE_BINDINGS.json](SOURCE_BINDINGS.json) bindet Archive und lesbare
Originalkopien. Der Ausgabelauf enthält eine commitgebundene `REPLAY.json`.
Die Prüfungen sind projektintern und ersetzen keine externe Begutachtung.

## Weitere Arbeit

Die [Forschungsstrategie](../../../00-uebersicht/OBJEKT_X_FORSCHUNGSSTRATEGIE.md)
ordnet die Diagnose der konstruktiven Fortsetzung unter. Eine weitere
Matrixuntersuchung soll eine konkret benötigte Schranke für Kopplung oder
Residualenergie liefern. A13, neue Operatordaten und ein großer adaptiver Baum
gehören nicht zu dieser Integration.
