# Neuer Stand: Fenstervergrößerung und quantitatives Neustartlemma

2026-09-19. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

Ausgangspunkt ist `a659047e00d024c0daa3991ea59fd21afd9f8793`.
Mit B=log(5)/2 gelten für alle tatsächlichen komplexen H1_0-Quellen
unter genau den ursprünglichen zwei Mellinbedingungen:

| Rechter Endpunkt höchstens | Physischer All-Parity-Gap |
| --- | --- |
| B+10^-19 | >3*10^-15 |
| B+4*10^-19 | >10^-15 |
| B+5*10^-19 | >3*10^-16 |

Die äußerste Breite ist fünfzigmal so groß wie zuvor. Der Odd-Gap
bleibt auf allen drei Bereichen >10^-12. Die exakten ursprünglichen
Schur-Matrizen werden um einen rationalen skalaren Abzug fortgesetzt;
alle unendlichen Tails und Mischblöcke bleiben berücksichtigt.

Daneben ist ein Neustartlemma mit uniformen analytischen Konstanten
für B<=a<b<=1 bewiesen: Aus q_a>=epsilon I, 0<epsilon<=1, folgt bei
0<b-a<=2^(-ceil(1600/epsilon)) der neue Gap epsilon/2. Die vollständige
relative Profil-Schur-Norm ist <49/200. Die beiden Mellinbedingungen,
Formbereiche, Konditionierung und alle Kanäle 2,3,4,5,7 einschließlich
neuer Schalen-Selbstwechselwirkungen sind explizit kontrolliert.

Der vollständige Kern wird direkt abgeschätzt; separate mitwandernde
Legendre-Tailreserven werden durch volle Kernkoerzivität und volle
Kern-Profil-Operatorkontrolle ersetzt. Keine Quelle wird neu gewählt
oder physisch renormiert, keine zusätzliche Bedingung eingeführt.

Eine konkrete unendliche Folge von Neustarts ist für jeden endlichen
Schritt zertifiziert. Ihre garantierten Breiten sind jedoch summierbar,
ihre Gaps gehen gegen null. Das ist kein Transport ohne Akkumulation
und kein uniform positiver Satz am Grenzendpunkt. Der nächste offene
Gate ist Reserveerneuerung beziehungsweise nicht summierbarer
zertifizierter Fortschritt. Connected Unit-Window Coercivity, historisches
P11/R43 Strong Terminal, C1-GEOM, Objekt X, globale Weil-Positivität und
RH bleiben offen.

Der zwischenzeitliche Commit `829019d7e62f936ab4db903bb9c7758edf427609`
bleibt vollständig erhalten. Seine andere schrumpfende Kette behält
autorenseitig einen positiven uniformen Gap-Floor auf einem kleineren
Endpunktband. Die hier gewählte Halbungskette schwächt diesen Befund
nicht ab. Der zusätzliche Fortschritt dieses Pakets besteht im größeren
tatsächlich erreichten Fenster und den bedingten Neustartkonstanten bis
b<=1 einschließlich Kanal 7. Beide Beiträge lassen nicht summierbaren
Fenstertransport offen. Der parallele Beitrag wird hier nicht als
mathematischer Input verwendet oder als extern auditiert dargestellt.

88 neue exakte Prüfungen bestehen; 95 Eingabedateien sind kryptographisch gebunden. Die vollständige
51/41/38/40/31/28/43/9-Kette und 349 universelle algebraische Regressionen
werden reproduziert. Alle neuen Entscheidungen verwenden ausschließlich
Ganzzahlen, rationale Zahlen und gerichtete Intervalle. Der analytische
Beweis bleibt unabhängig zu prüfen; Reproduktion ist kein externes Audit.
