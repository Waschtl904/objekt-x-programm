# Vollständige Shiftbilder und primal-duale Y68-Trennung

Status: **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Quellenbasis: `main@b27a18c32058a9a2a4e4c1611a18a67caa586c15`.

Der Full-Shift-Block allein endet UNRESOLVED. Acht zusätzliche adjungierte
Resolventenkandidaten liefern danach rigoros

`Y68 in [0.0410706614, 0.0725344674]`.

Die signierte Gate-Reserve ist größer als `0.0069620524`.
Der bisherige gedrehte Gegenzeuge ist ausgeschlossen. Der gemeinsame
Odd-Winkeltest mit allen Nebenintervallen liefert weiterhin keinen Korridor
unter 10°. Sieben Proben der bisherigen gemeinsamen Familie liefern keinen
neuen Nachweis eines Gegenpaares mit mehr als 10° Abstand. Diese Stichproben
zertifizieren keinen einheitlichen Winkelbereich.

- [Full-Shift-Bericht](01-full-shift/REPORT.md) · [Beweis](01-full-shift/PROOF.md)
- [Primal-Dual-Bericht](02-primal-dual/REPORT.md) · [Beweis](02-primal-dual/PROOF.md)
- [Signierte Abnahme](02-primal-dual/gate.json) · [Winkeltest](02-primal-dual/angle.json)
- [Begrenzte Familiensuche](02-primal-dual/counterfamily.json)
- [Quellen und Originalhashes](SOURCE_BINDINGS.json)

## Unveränderte Originalpakete

Die beiden ZIPs in `archives/` enthalten die vollständigen, unveränderten
Originalpakete. Die sichtbaren Beweise, Berichte und Quittungen sind bytegleiche
Kopien daraus. Der Replay entpackt außerhalb des Repositorys und prüft jedes
Archivmitglied gegen den Originalhash und das Paketmanifest. Dadurch bleiben
die ursprünglichen abgeschlossenen Pakete samt ihren Replay-Einstiegspunkten
unverändert. Angaben über den lokalen Publikationsstand in den Originalen
beziehen sich auf ihren jeweiligen Versiegelungszeitpunkt.

## Reproduktion

Für bytegleichen Replay: Windows, Python 3.13 und `python-flint==0.9.0`.
Die Originalquittungen enthalten Windows-Zeilenenden; die CI verwendet
deshalb einen Windows-Runner. Die Archive werden nicht umformatiert.

```
python -B research/x-c1/canonical-full-shift-primal-dual-2026-10-02/replay.py --output C:/Temp/full-shift-primal-dual-replay
```

Das Zielverzeichnis muss neu sein und außerhalb des Repositorys liegen.
Der Replay erstellt einen lokalen Checkout der historischen Quellenbasis,
bindet unveränderte Eingabequellen, führt die kleinen unabhängigen Kontrollen
und die rationale Fehlerrechnung aus und reproduziert Gate, Winkeltest und
begrenzte Familiensuche bytegleich. `--full` berechnet zusätzlich die großen
Operatorintegrale erneut. Die reguläre CI verwendet den schnellen Modus.

Die Abnahmeprotokolle dokumentieren bereits durchgeführte vollständige
Stichproben-Replays: einen primalen und einen dualen Pol. Alle übrigen
Polrechnungen wurden vollständig erzeugt, aber nicht nochmals vollständig
wiederholt. Die große Operatorimplementierung ist nicht unabhängig neu
implementiert. CI und Integration ändern den externen Review-Status nicht.

## Aussagegrenze

Der alte STRUCTURAL-OPEN-Nachweis gilt weiterhin für seine ursprüngliche
Relaxation; sein Gegenpaar trägt nicht auf die neue Y68-Relaxation über.
Deren einheitlicher ungerader Winkelkorridor bleibt offen. Der aktuelle
Winkeltest wertet die Ausgangsbox ohne neue Unterteilung aus.
Neue duale Y58-Daten, bandweise Momente tatsächlicher Maximierer, allgemeines
Renewal, A13-Positivität, eine kofinale positive Familie, globales Objekt X
und RH werden nicht behauptet. PR #187 bleibt separat.

## Verbindliche Integrationsprüfungen

Vor dem Merge: beide Paket-Replays einschließlich der kleinen unabhängigen
Kontrollen, signierter rationaler Abnahme und bytegleichen Winkel-/Familien-
quittungen; Manifest-/Archiv-/Quellenprüfung; Registry-Validatoren; technische
Fehler- und CI-Routing-Kontrollen; sämtliche anwendbare CI auf dem finalen
PR-Head. Die dokumentierten großen Stichproben-Replays sind gebundene Belege.
Ein erneuter vollständiger Lauf aller großen Integrale ist ein zusätzlicher
Audit und nicht Teil des regulären Integrationslaufs.
