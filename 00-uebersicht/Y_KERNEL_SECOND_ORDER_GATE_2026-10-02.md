# Gemeinsamer Y-Kernel und ungerade Eigenlinie zweiter Ordnung

**Planstatus: OPEN.** Dieser Text legt den nächsten Versuch und seine Abnahme
fest. Er enthält kein neues numerisches Zertifikat.

## Ausgangspunkt

Das integrierte [Direct-Line-Paket](../research/x-c1/canonical-direct-odd-line-2026-10-02/README.md)
verbessert zwei bedingte Vier-Y-Schnitte auf 3.405363° beziehungsweise
3.765366°. Root und die acht früheren Diagnoseboxen bleiben UNRESOLVED.
Die affine Engine erhält viele gemeinsame Variablen, behandelt aber die
eingeschlossene Y-left-Inverse unabhängig von Y-left. Höhere gemeinsame
Produkte werden teilweise in getrennte Restintervalle überführt.

## Rechenansatz

Verwende die gemeinsame Gleichung

```math
Y_L X + Y_R=0,
\qquad Y_L=A_0+\Delta A,\quad Y_R=B_0+\Delta B.
```

A_0 und B_0 sind feste rationale Zentren. A_0 muss nachweislich invertierbar
sein; setze **exakt** X_0=-A_0^{-1}B_0 und X=X_0+ΔX. Bei einem nur näherungsweise
gelösten Zentrum müsste sein Residuum zusätzlich vollständig bezahlt werden.
Mit

```math
H=A_0^{-1}\Delta A,
\qquad q=-A_0^{-1}(\Delta B+\Delta A X_0)
```

folgt exakt

```math
(I+H)\Delta X=q,
\qquad
\Delta X=q-Hq+H^2(I+H)^{-1}q.
```

Die linearen und quadratischen Terme behalten dieselben ΔA-/ΔB-Symbole.
Ein möglicher rigoroser Restnachweis verwendet eine submultiplikative
Matrixnorm, etwa die induzierte Zeilensummennorm. Wenn auf der **ganzen**
jeweiligen Eingabebox nachgewiesen ist, dass ||H||≤h<1, gilt

```math
\|H^2(I+H)^{-1}q\|\le\frac{h^2}{1-h}\,\|q\|.
```

Die Schranke und alle Rundungsfehler müssen gerichtet eingeschlossen werden.
Alternativ ist ein vollständig verifizierter gemeinsamer Krawczyk-/Newton-
oder Taylor-Modell-Nachweis zulässig. Eine numerische Näherungsinverse oder
ein empirisch kleiner Rest genügt nicht.

Trage die gemeinsamen Terme durch N, NᵀG_BN, NᵀL_BN, NᵀZ_BN und die skalierte
2×2-Liniengleichung. Jede verworfene höhere Ordnung erhält einen expliziten
Rest. Die geerbten Intervall-, Moment-, Positivitäts- und Quellbedingungen
bleiben erhalten; Schnittbildung darf keine zulässigen Daten verlieren.

## Feste Vergleichsfälle und Abnahme

Verwende genau dieselben 19 Fälle und dieselbe physische Referenz wie im
Direct-Line-Paket: Root, fünf bekannte vollständige Punkte, deren fünf
Vier-Y-Schnitte und acht frühere Diagnoseblätter.

1. Die fünf bekannten Punkte bleiben vollständig enthalten und werden auf
   dem **maximalen** Eigenwertast zertifiziert.
2. Die bedingten Schnitte central und quarter werden mindestens so gut
   eingeschlossen wie die bereits zertifizierten Obergrenzen 3.405363° und
   3.765366°. Berichte zusätzlich den Vergleich mit den exakten alten Grenzen.
3. Prüfe insbesondere die bisher offenen Schnitte half, two_thirds und
   five_eighths sowie alle acht Diagnoseboxen. Dokumentiere jede neu
   isolierte Linie und ihre physische Winkelhülle; eine Isolation allein
   bedeutet noch keinen Gesamtwinkel unter zehn Grad.
4. **Uniformer Abschluss:** Nur eine auf der gesamten Root-Familie
   zertifizierte maximale Linie mit gemeinsamem physischem Gesamtwinkel
   strikt unter 10° schließt den Lokalisierungsgate. Die Winkeldefinition
   bleibt zweimal die obere Abweichung von derselben festen Referenz.
5. Bleibt Root offen, werden isolierte Teilfälle als solche berichtet.
   Wenn alle acht repräsentativen Diagnoseboxen isolieren und die neue
   Engine einen belegten Nutzen zeigt, kann anschließend ein neuer
   adaptiver Versuch begründet werden. Diese acht Diagnoseboxen ersetzen
   für sich genommen keine vollständige Überdeckung der Root-Familie.

Vor einer Ergebnispromotion stehen algebraische Positiv-/Negativkontrollen,
gerichtete Rest- und Winkelprüfungen, Quellenbindungen und ein vollständiger
deterministischer Replay. Ein erneutes UNRESOLVED bleibt ein gültiger Ausgang;
es beweist keine strukturelle Offenheit und kein Scheitern aller höheren Modelle.

## Umfang

Der erste Versuch verwendet ausschließlich vorhandene Daten. Keine neuen
Operatorintegrale, Y58-Dualdaten, L_B-Daten oder großen adaptiven Bäume.
PR #187/A13 bleibt separat. Bandweise Momente tatsächlicher Maximierer folgen
nach erfolgreicher Richtungslokalisierung; ein vorwärts gerichtetes Renewal-
Gesetz bleibt eine eigene Forschungsaufgabe.
