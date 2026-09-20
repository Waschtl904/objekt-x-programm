# Same-Engine-B-Kalibrierung — Status

20.09.2026. **CALIBRATION PASS / TERMINAL PROMOTION STILL BLOCKED**.

Die Arb-/Legendre-/Active-Set-Assembly aus dem terminalen Kandidatenpfad wurde
am unabhängig bekannten positiven Endpunkt

[
B=rac{log 5}{2}
]

mit `python-flint==0.9.0` ausgeführt.

In beiden Paritäten gilt beim Entry-by-entry-Vergleich zur eingefrorenen
Fraction-Engine:

- `A_nonoverlap = 0`;
- `Gact_nonoverlap = 0`;
- `delta_overlap = true`;
- `lower_nonoverlap = 0`.

Außerdem sind je Parität alle 31 gerichteten LDL-Pivots strikt positiv.

Die gerichteten physischen Untergrenzen sind

[
arepsilon_B^{m even}
>
1.0423892675689	imes10^{-13},
]

[
arepsilon_B^{m odd}
>
2.3831654046764	imes10^{-11}.
]

Damit reproduziert die neue Assembly den bekannten Endpoint-Satz einschließlich
vollständiger High-Antwort und überschreitet den vorgeschriebenen
Kalibrierungsboden (10^{-13}).

**Dies promoviert den terminalen (a=1)-Kandidaten noch nicht.**
Weiter offen bleiben insbesondere der gepinnte vollständige terminale
`--verify --recompute`-Replay und der unabhängige analytische Review der
terminalen High-Floor-/Enclosure-Richtung und Normrückrechnung.
