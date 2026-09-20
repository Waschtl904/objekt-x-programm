# Beweisprotokoll: terminale 191D-Schur-Einschlie�ung

## Status und Geltungsbereich

Dies ist ein autorenseitiges Zertifikat vom 20.09.2026. Der Review-Status
bleibt `EXTERNAL_REVIEW_OPEN`; dieses Paket ist kein neuer verifizierter
Snapshot. Es behandelt ausschlie�lich den festen Horizont `0<a<=1` am
Terminalpunkt `a=1`, die beiden Parit�ten und die bereits etablierte
191D-Schur-Kongruenz. Es liefert keine Aussage �ber einen gr��eren Horizont,
eine Profilfortsetzung, Objekt X, globale Weil-Positivit�t oder RH.

## Eingaben und exakte Modellierung

`input_bindings.json` bindet die analytischen Quellen und den vollst�ndigen
Schur-Br�ckensatz bytegenau an den Snapshot `79988874cceeb01f17e0cda67485838c0b7c4f63`.
Die terminale Rechnung verwendet die f�nf Kan�le `q=2,3,4,5,7`, rohe
Legendregrade `0,...,383`, Gamma-Grad `128` und Arb mit 2048 Bit.

Die Legendre-Rekursion, die Mellinmomente und die Gamma-Koeffizienten werden
als rationale Gr��en aufgebaut. Die Prime-Integrale werden mit der exakten
Gauss-Regel auf den jeweiligen Polynomialgrad ausgewertet. Die verschobenen
Mischzellen werden an allen Singularit�tsgrenzen getrennt integriert. Die
unendliche hohe Antwort wird nicht abgeschnitten: Der hohe Block wird durch
die vollst�ndige Gamma-Unterst�tzung und das explizite Restbudget eingebracht.
Die 64 elementaren Normalisierungsidentit�ten in `check_normalization.py`
pr�fen unabh�ngig die verwendeten Legendre-, Prime- und Gamma-Konventionen.

## Gerichtet eingeschlossene Matrizen

Aus dem physischen Formoperator `Q` und der vollst�ndigen hohen Kopplungs-
Gram-Matrix `Cgram` werden die beiden konkreten Low-Matrizen gebildet. Nach
der Parit�tsauswahl und der exakten Mellin-Nullbedingung haben beide Gr��en
Dimension 191. `terminal_matrices.json.gz` speichert f�r jede Matrix jedes
untere/obere Dezimalintervall mit 55 Stellen; die Breite ist Teil des
Zertifikats und wird beim Einlesen erneut in Arb-B�lle umgewandelt.

Sei `delta=7/10` die unabh�ngige terminale High-Reserve und `e=5*10^-26`
der rationale Form-/Gamma-/Momentfehler. F�r jede Parit�t wird die gerichtete
untere Matrix

```
L = A - (1001/1000)/delta * G
    - (e + 1001*e^2/delta) I
```

aus den Intervallen aufgebaut. Die Richtung ist entscheidend: F�r jeden
zul�ssigen tats�chlichen Eintrag liegt die reale Schurmatrix oberhalb dieser
Untereinschlie�ung. Die Rohmatrix wird nicht �ber numerische Eigenwerte
beurteilt.

## Rationale LDL*-Zertifizierung

F�r jede Parit�t ist ein rationales unteres Dreieck `P` mit Nenner `10^80`
gespeichert. Der Checker berechnet mit gerichteten Arb-Operationen

```
B = P L P^T.
```

F�r jede Zeile wird `B[i,i] - sum_{j!=i}|B[i,j]|` gerichtet nach unten
berechnet und als strikt gr��er als `9/10` gepr�ft. Nach Abzug dieser
Reserve f�hrt die zertifizierte LDL*-Routine alle 191 gerichteten Pivots
positiv. Damit ist `B` und folglich `L` strikt positiv definit. Die Rechnung
verwendet keine Gleitkomma-Eigenwerte; ein m�glicher Nullpivot w�rde als
unentschiedener Checker-Fehler abbrechen, ein negativer Pivot als gescheiterte
Zertifizierung.

Die Spur des Vorconditioners wird separat gegen die gespeicherte Schurreserve
gepr�ft. Ebenso werden die vollst�ndige inverse Shear-Schranke, die
physische Normumrechnung und die Parit�tsreserven gepr�ft. F�r beide
Parit�ten besteht die ausgewiesene physische L�cke mindestens in der
Gr��enordnung `10^-26` im Paket-Scope.

## Logische Grenze

Das Ergebnis ist eine strikte terminale Schur-Einschlie�ung im bereits
bewiesenen festen Horizont. Es ist kein eigenst�ndiger Nachweis
`||R_1||<=1` au�erhalb der etablierten positiven Gram-Kongruenz und kein
globaler Positivit�tssatz. Der alte negative Rohvergleich der nicht
vorconditionierten unteren Matrix wird nicht als negative zul�ssige Quelle
interpretiert. Umgekehrt ersetzt ein bestandener lokaler LDL*-Lauf keine
unabh�ngige Pr�fung der algebraischen Identit�ten, der Richtungen und der
vollst�ndigen High-Response-Konstruktion.

Der Gate `TERMINAL-191D-DEFECT-SCHUR-A1` bleibt daher in der Registry offen;
dieses Paket wird als `PENDING_STATUS_REVIEW` gef�hrt. Die unver�nderliche
Pr�fsumme von Code, Eingaben, Matrixintervallen, Log und Ergebnissen steht in
`SHA256SUMS`.
