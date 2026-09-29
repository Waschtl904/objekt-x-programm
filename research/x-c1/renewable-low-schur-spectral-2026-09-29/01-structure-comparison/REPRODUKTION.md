# Reproduktion des Strukturvergleichs

## Voraussetzungen

- Vollständige lokale Git-Arbeitskopie von `Waschtl904/objekt-x-programm` bei
  `d16ba43ebb20f2c61f43379fc65d7a9b9dba76de`.
- Python 3.13 mit `python-flint==0.9.0` für Matrix- und Intervallarithmetik.
- Python mit NumPy für die ausdrücklich approximative Winkelrechnung; hier
  Python 3.12.14 mit NumPy 2.3.5.
- Git. Die beiden Arb-Skripte verwenden für diese Windows-Umgebung den Pfad
  `C:\Program Files\Git\cmd\git.exe`; auf anderen Systemen ist diese
  Werkzeugpfadangabe anzupassen.

Die Skripte lesen die Forschungsdateien und schreiben ausschließlich in die
angegebenen Ausgabeverzeichnisse. Sie bauen keine neuen Integralmodelle,
ändern keine Beweise und aktualisieren keinen Repository-Status.

## Schritte

Platzhalter `REPO`, `ERGEBNIS` und `GEGENCHECK` durch lokale Pfade ersetzen.
Die Befehle setzen voraus, dass das jeweilige Python die benötigte Bibliothek
findet. Die Ausgabeverzeichnisse sollten getrennt von der Git-Arbeitskopie liegen.

```text
python low_schur_compare.py --repo REPO --out ERGEBNIS --bits 768
python low_schur_compare.py --repo REPO --out GEGENCHECK --bits 1024 --only A11-even
python low_schur_physical_angles.py --input ERGEBNIS/critical_vectors.json --output ERGEBNIS/physical_angles.json
python low_schur_verify_diagnostics.py --repo REPO --diagnostics ERGEBNIS/diagnostics.json --vectors ERGEBNIS/critical_vectors.json --precision-check GEGENCHECK/diagnostics.json --out ERGEBNIS/verification.json
```

Die hier beigelegte `precision-check.json` entspricht
`GEGENCHECK/diagnostics.json`. Alle ausgegebenen Zeiten hängen vom Rechner ab.
Die Gegenrechnung bestätigt dieselben 70 ausgegebenen Stellen der drei
diagnostischen A11-Eigenwerte im geraden Sektor.

## Aussagegrenzen der Dateien

`diagnostics.json` enthält Eigenpaar- und LDL-Diagnostik der rationalen
Mittelpunktsmatrizen. Diese numerischen Rechnungen ersetzen keine gerichtete
Eigenwertisolation und keinen allgemeinen Positivitätssatz.

`verification.json` prüft die eingelesenen Quellhashes, rekonstruiert die
Diagonaldifferenz-Zeugen aus den ursprünglichen Intervallmatrizen und wertet
konkrete rationale Richtungen mit den vollständigen niedrigen Intervallen und
den vorhandenen analytischen Fehlerbudgets aus. Die zugehörigen physischen
Quellen sind die exakt momentkorrigierten Polynome am jeweiligen Terminal.

`physical_angles.json` verwendet gerundete Vektoren und Gleitkomma-Gaussregeln.
Die darin enthaltenen äußeren Trägermassen nahe 10⁻¹⁴ dürfen nicht als rigorose
Schranken oder als exakte Nullen gelesen werden.

Die gelieferten Originalmatrizen bleiben Teil der gepinnten Git-Arbeitskopie;
sie werden hier nicht nochmals dupliziert. `SHA256SUMS` bindet alle Dateien
dieses separaten Vergleichspakets außer sich selbst.
