# C1-Kandidat: gemeinsamer Spektralraum mit kompaktem Gramdefekt

20.09.2026 — **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

Ausgangspunkt: `f77116a`. Der neue Schritt konstruiert einen konkreten
Kandidaten mit genauem Fehlerterm. Er liefert keinen weiteren allgemeinen
Ausschluss und setzt die Positivitaet der Weil-Form nicht voraus.

## Konstruktion

Auf dem festen physischen Horizont 1 werden alle fuenf Prime-Power-Kanaele
2, 3, 4, 5, 7 gemeinsam mit dem vollstaendigen Gamma-Symbol g verwendet.
Mit Gewichts-Summe omega, Kosinussumme c und `s=kappa+2 omega` lautet
der Readout im positiven Hilbertraum `L2(dxi)`:

    T u = (g + omega - c) / sqrt(g+s) * Fourier(u).

Die Fensterraeume `H_a=closure(T W_a)` sind unendlichdimensional. Ihre
Uebergaenge sind isometrische Inklusionen und erfuellen exakt

    T_b J_ab = I_ab T_a,    I_bc I_ab = I_ac.

Der Kandidat ist wesentlich nichtlokal: Bei explizit beschriebenen glatten
geraden und ungeraden Zwei-Mellin-Quellen haben seine physischen Ausgaben
keinen kompakten Support. Ein echter Pol im Quadrat des analytisch
fortgesetzten Multiplikators beweist dies; seine Lage wird rational durch
`2/5 < beta < 9/20` eingeschlossen.

## Exakter verbleibender Defekt

Mit

    D u = (kappa + omega + c) / sqrt(g+s) * Fourier(u)

gilt `q(u,v)=<Tu,Tv>-<Du,Dv>`. Beide Ausgaben enthalten gekoppelte
Prime-/Gamma-Daten. Die einzelnen indefiniten Prime-Kanaele werden nicht
als getrennte positive Gram-Summanden ausgegeben.

Der Gramfehler `E_a=-<D,D>` ist auf jeder von null verschiedenen Quelle
strikt negativ. Der unberichtigte Readout erfuellt C1c also nicht.
Diese negative Abweichung ist keine negative volle Weil-Energie.

Auf H_a ist `R_a(Tu)=Du` kompakt, injektiv und von unendlichem Rang.
Die Defektuebergaenge sind exakt: `R_b I_ab=R_a`. Fuer `C_a=R_a* R_a`
gilt die Kompressionsidentitaet `I_ab* C_b I_ab=C_a`; daraus folgt kein
automatisches Intertwining lokaler Quadratwurzelkorrekturen.

Die Restobligation lautet nun konkret:

    ||R_a|| <= 1.

Sie ist aequivalent zur Positivitaet der vollen Form auf diesem Fenster.
Kompaktheit laesst nur endlich viele moegliche Eigenwerte von C_a bei oder
ueber eins zu, beweist aber nicht deren Abwesenheit. Ein explizites
Frequenz-/Taylorverfahren liefert normkonvergente endlichrangige
Approximationen mit rational auswertbarem Rest. Die hier ausgewiesene
konservative Schranke schliesst den Kontraktionsgate nicht.

## Einordnung

Geschlossen sind die Konstruktion und das Intertwining dieses benannten
C1-Kandidaten, einschliesslich gemeinsamen Kanalbeobachtungen und exakt
kontrolliertem kompaktem Defekt. Die abgeschlossene Quellenklasse und
beide urspruenglichen Mellinbedingungen bleiben erhalten. Die geerbte
Near-Null-Quelle wurde nicht geaendert.

Der Readout haengt vom erklaerten Horizont 1 ab. Die fuenf Kanaele bleiben
auch auf kleineren Fenstern Teil derselben Formel. Ein Wechsel des
Horizonts oder der Kanalmenge ist nicht durch den Uebergangssatz gedeckt.

Offen bleiben C1c, der volle positive C1-Mediator, eine kompatible
unbeschraenkte Horizontfolge, Moving-191D Low/Profile, nicht summierbarer
Transport, Strong Terminal, Objekt X und RH. Der bisherige positive
Bereich bis B+10^-10 und der uniforme High-Tail bis 1 werden nicht erweitert.

Die 53 exakten neuen Pruefungen einschliesslich fuenf Herkunftsbindungen
sind reproduzierbar; JSON und Log werden bytegleich verglichen, sieben
Nutzdateien gehasht. Dies ist kein unabhaengiger analytischer Audit und
keine erneute Ausfuehrung der alten Matrixzertifikate.
