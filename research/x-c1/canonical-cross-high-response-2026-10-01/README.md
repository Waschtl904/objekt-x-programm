# Kreuzprojektoren und hohe Resolventenantwort

Zwei abgeschlossene **UNRESOLVED**-Blöcke lokalisieren den Engpass der
ungeraden A9→A11-Maximiererrichtung. Status:
**AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.

1. [Kreuzprojektor-Residualgate](01-cross-projector/PROOF.md): gemeinsame
   Residuen verengen 48 Y-Hüllen. Die rationale Filterrechnung kontrolliert
   den vollständigen hohen Raum; ihre Vektorfehler reichen nicht für den
   Ausschluss des gedrehten Gegenzeugen.
2. [Hohe Antwort und korrigierte Resolventen](02-high-response/PROOF.md):
   die ersten 128 hohen Moden erfassen je nach Spalte und Pol ungefähr
   32.45–37.45 % der ursprünglichen Modellantwort. Endliche Korrekturräume
   senken die Fehlerobergrenzen von 0.6314 auf 0.5181 (A9/6) und von
   0.8429 auf 0.6840 (A11/8). Y58 und Y68 werden dadurch nicht enger.

Am **ersten oberen Pol** liegen 98.45–99.09 % der Energie des
normalbereinigten Modellresiduums oberhalb des Korrekturfensters.
Der Shiftanteil dominiert diese Diagnose. Diese Aussage ist weder eine
allpolige Kanaldiagnose noch eine Messung des tatsächlichen Lösungsfehlers.
Die vollständigen physischen Residuenobergrenzen sind separat bezahlt.

Die beiden Originalverzeichnisse und ZIPs bleiben bytegleich. PROOF.md
ist jeweils eine identische Berichtskopie außerhalb des unveränderten
Originalpakets. Historische Angaben zum lokalen Integrationsstand bleiben
erhalten; [CURRENT_STATE](../../../00-uebersicht/CURRENT_STATE.md) führt
den aktuellen Stand.

## Nächster Gate: FULL SHIFT-IMAGE CORRECTED RESOLVENT

Der nächste Kandidatenraum verwendet vollständige nullfortgesetzte
Shiftbilder und deren gesamten hohen Anteil (A11: alle Grade >571).
Eine diagonale Vorconditionierung durch `(D_H+q0-z)^-1` ist zu prüfen.
Die unendlichen Legendre-Anteile müssen einschließlich Operatorwirkung
zertifiziert werden. Eine Vergrößerung des bisherigen Modenfensters
erfüllt dieses Ziel nicht.

Zunächst sind allein Y58 und Y68 zu prüfen. Abnahme ist
`Y58_max < Y58_rotated_min` oder `Y68_min > Y68_rotated_max`.
Erst nach einem solchen Ausschluss folgt der gemeinsame Richtungstest
mit Ziel eines physischen Gesamtwinkelkorridors unter 10 Grad.
Bei weiter zu breiten Skalarfehlern kommt eine primal-duale
Resolventenidentität mit dem Produkt gerichteter Residuen in Betracht.
Filter und Präzision bleiben für diesen Methodenvergleich fest.

Das 1/N-Tailbild ist eine diagnostische Heuristik, kein zertifizierter
asymptotischer Satz. Ein neuer Gegenzeugenausschluss, STRUCTURAL OPEN 2,
enge ungerade Lokalisierung und bandweise Momente tatsächlicher Maximierer
sind nicht bewiesen. Allgemeines Renewal, A13-Positivität, kofinale
positive Familie, globales Objekt X und RH bleiben offen. #187 bleibt separat.

## Reproduktion

Python 3.13 und `python-flint==0.9.0`, vom Repository-Stamm:

```text
python -B research/x-c1/canonical-cross-high-response-2026-10-01/replay.py --output NEUER_PFAD_AUSSERHALB_DES_CHECKOUTS
```

Der Wrapper prüft alle Originaldateien, Archive und aktuellen Quellen,
erstellt einen lokalen Checkout des historischen Quellenpins und
reproduziert drei Quittungen bytegleich. Er wiederholt die kleinen
Arb-Kontrollen und die gemeinsamen Gate-Auswertungen. Die großen
Operatorintegrale werden im Standardlauf und in der regulären CI
**nicht erneut ausgeführt**. `--full` bietet zusätzlich die vollständigen
Paket-Replays; auch diese wären keine unabhängige Neuimplementierung.
CI ist keine externe mathematische Gesamtprüfung.
