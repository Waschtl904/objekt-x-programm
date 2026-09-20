# Terminaler 191D-Schurtest bei a=1

20.09.2026. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

Dieses Paket schlie�t den vollst�ndigen hohen Response in zwei tats�chlichen
191x191-Matrizen je Parit�t ein. Die Eingaben sind der eingefrorene
Schur-Br�ckensatz bis `79988874`; die analytischen Dateien werden �ber
`input_bindings.json` bytegenau gebunden.

F�r Even und Odd werden die exakten Mellinmomente, die f�nf Prime-Kan�le
`2,3,4,5,7`, das Gamma-Polynom und der komplette unendliche High-Response
mit Arb-Intervallen berechnet. Die gespeicherten Matrizen sind keine
Stichproben und keine numerischen Eigenwerttabellen.

Die gerichtete Untereinschlie�ung wird mit rationalen Intervallkoordinaten
vorconditioniert. Eine vollst�ndige Zeilensummenreserve `>9/10` und 191
positive gerichtete LDL*-Pivots je Parit�t liefern eine strikte terminale
Schurreserve. Die angegebene physische Reserve ist separat ausgewiesen.

Reproduktion:

```text
python check_terminal.py --verify
```

F�r die vollst�ndige erneute Matrixerzeugung:

```text
python check_terminal.py --verify --recompute
```

Die Zertifizierung ist autorenseitig und bleibt externer Pr�fung ge�ffnet.
Sie beendet weder die Registry-Obligation automatisch noch behauptet sie
globale Fortsetzung, Objekt X, globale Weil-Positivit�t oder RH.
