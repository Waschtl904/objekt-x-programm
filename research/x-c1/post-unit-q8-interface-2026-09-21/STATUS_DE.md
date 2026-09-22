# STATUS_DE - post-unit q=8 horizon interface

Stand: 2026-09-22.

## Paketstatus

`POST-UNIT-Q8-HORIZON-INTERFACE`

- Mathematischer Status: `OPEN`
- Review-Status: `EXTERNAL_REVIEW_OPEN`
- Integrationsstatus: `RESEARCH_BRANCH_UNMERGED`
- Typ: Interface-/Obligationspaket, kein neuer Satz
- Positivitaet fuer Terminalhorizonte >1: nicht behauptet
- C1-Horizont-Cocycle unbeschränkt: `OPEN`
- erste geschlossene Kammer bis log(8)/2: `AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN` (O1-O7, ausdrücklich definierte C1a-Fortführung)
- X4-Q8-Wall-Crossing: `OPEN`

## Typisierung des naechsten Satzes

Der erste Kammersatz ist inzwischen separat bewiesen und registrierbar; für weitere Horizonte bzw. die q=8-Wand müssen weiterhin zwei rohe Transportfamilien unterschieden werden:

[
M^T_{A,B}:\mathcal H_A^T\to\mathcal H_B^T,
\qquad
M^D_{A,B}:\mathcal H_A^D\to\mathcal H_B^D.
]

Mindestens zu beweisen sind

[
M^T_{A,B}T_A=T_BJ_{A,B},
\qquad
M^D_{A,B}D_A=D_BJ_{A,B},
]

sowie

[
M^T_{B,C}M^T_{A,B}=M^T_{A,C},
\qquad
M^D_{B,C}M^D_{A,B}=M^D_{A,C}.
]

Vor diesen Gleichungen stehen die Kernel-/Quotientenbedingungen,
Wohldefiniertheit auf den Bildraeumen und Beschraenktheit der Erweiterungen.

Falls spaeter `D_A=R_AT_A` und `D_B=R_BT_B` gelten, ist auch

[
R_BM^T_{A,B}=M^D_{A,B}R_A
]

ein eigener Beweisschritt und keine automatische Folgerung.

## Forschungsreihenfolge

1. `TERMINAL-HORIZON-C1-COCYCLE`
2. `FIRST-GLOBAL-CHAMBER-1-TO-LOG8/2`
3. `X4-Q8-WALL-CROSSING`
4. erst danach positive korrigierte Terminaltransporte und kofinale Fortsetzung

Am Endpunkt

[
A_8=\frac12\log8
]

ist `q=8` wegen `log q < 2A` noch nicht aktiv. Die geschlossene erste
Kammer endet daher mit der alten Familie `{2,3,4,5,7}`. Der Kanal `8`
gehoert erst in den Satz strikt rechts der Wand.

## Firewalls

Nicht behauptet:

- Positivitaet fuer A>1;
- Uebernahme der Zahl 191 auf neue Horizonte;
- Gleichheit der T- und D-Transporte;
- lokale Quadratwurzel-Intertwinings;
- positive Einzelkanalzerlegung von q=8;
- kompatible positive korrigierte Raeume ueber verschiedene Terminalhorizonte;
- unbeschraenkte/kofinale C1-Geometrie;
- vollstaendige globale Weil-Testklasse;
- globales Objekt X;
- globale Weil-Positivitaet;
- RH.

`P11-FIXED-PAIR-STRONG-TERMINAL` bleibt davon strikt getrennt.


## Neuer abgeschlossener Unterblock

Das Paket [`FIRST-CHAMBER-RAW-TD-COCYCLE-O1-O7`](../first-chamber-raw-td-cocycle-o1-o7-2026-09-22/PROOF.md) schließt O1-O7 ausschließlich für

\[
1\le A\le B\le C\le \tfrac12\log 8.
\]

Dort gelten getrennte isometrische T-/D-Transporte, beide Cocycle-Gesetze, beschränkte Defektoperatoren mit \(\|R_A\|\le\sqrt{90}\), das typkorrekte R-Intertwining und Formnaturality auf den vollständigen Quellen. O8 (neue Terminalpositivität), positive korrigierte Transporte und das q=8-Wall-Crossing bleiben offen.
