Objekt X — Basis84-Prüfung und vollständiger L-Energiegram
10. Oktober 2026

Zuerst PRUEFVERMERK.txt lesen. ANSCHLUSS_GPT2.txt beschreibt den nächsten
konkreten Rechenauftrag und trennt die beiden 203er-Funktionalblöcke.

Neu enthalten sind zwei tatsächliche 84x84-Energiegrame E84=L[J,J],
jeweils mit rationaler Mittelpunktmatrix und vollem Löwner-Radius 10^-58.
Sie stehen unter expected/L_ENERGY_84_EVEN.json und ..._ODD.json.
J wird unverändert aus dem separat vorgelegten Originalpaket übernommen.

S_eta besitzt unter der geerbten hohen Schranke auf diesem Ansatzraum
eine Konditionszahl unter 13,51. Sein konkreter Block H[J,J], die Daten
A0 J und der vollständige Residualgram wurden hier nicht integriert.
Der tatsächliche tau-Tail bleibt offen.

Reproduktion:
Python 3.12 und python-flint==0.9.0 sind erforderlich.
Das unveränderte Originalarchiv wird separat benötigt. Sein SHA256 steht
in SOURCE_BINDINGS.json; es ist nicht noch einmal in diesem Paket enthalten.

  python reproduce_review.py /pfad/Objekt-X-Basis84-und-Abdeckungspruefung-2026-10-10.zip --work /neuer/arbeitsordner

Optional bei separater Installation der Bibliothek:
  --deps /pfad/zum/python-modulordner

Der Arbeitsordner muss neu sein und Platz für die entpackten Vorgänger
bieten. Die Originalarchive bleiben unverändert. Der Replay berechnet
die neue Basis-/Fitrechnung erneut, kontrolliert die sechs Ergebnisdateien
und reproduziert die zusätzlichen rationalen Kontrollen und Energiegrame.
Er führt keine früheren großen Prim-/Gamma-Quellintegrationen erneut aus.

expected/ enthält die in dieser Prüfung tatsächlich berechneten Ergebnisse.
Ihre Berechnung wird durch die mitgelieferten Skripte reproduziert.
Die geerbten analytischen Identitäten und die Bedeutung der vollständigen
Operatormajoranten bleiben von dieser arithmetischen Prüfung getrennt.

FULL_REMAINDER_CERTIFIED=false.
