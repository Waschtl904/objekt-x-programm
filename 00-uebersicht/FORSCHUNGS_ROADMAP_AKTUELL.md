# Objekt X — operative Roadmap v4.0

> Stand: 16. September 2026. Verzweigte Arbeitsplanung, keine Fertigstellungsprognose oder Satzpromotion.
> [Kanonischer Einstieg](../CURRENT-FRONT.md); exakte Quellen/Heads stehen dort.

## Historischer Namensraum

[v3.12 am Originalcommit](https://github.com/Waschtl904/objekt-x-programm/blob/ac164bbbd2c46623aa64e567d21f813f41f164b0/00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md) bleibt vollständig erhalten.
Deren C0-C7 heißen in neuen Verweisen `A1-CERT/C0-C7`.
`X-C0-TYPE / X-C1-GEOM / X-C2-ID / X-C3-WINDOW` bezeichnen das andere, neue Konstruktionsprogramm.
Die historischen kleineren PSWF-Gates werden nicht nachträglich mit den Legendre-Zertifikaten identifiziert.

## P0 — Navigation und Aufbewahrung

Schlanke Pointer; Originalaudits, Journale, Registry und Spezifikationen nicht umschreiben.
Archivierung erhält die tatsächlichen Bytes plus Herkunft, nicht nur Hashlisten.
Geplanter Archivtag: `a1-comp-2026-09-16` auf `0a7c970fc5983c9c198915e2c7c1f6280834b13a`.
Ein veröffentlichtes Release ist erst nach zurückgelesenem Tag und vollständiger Assetprüfung als erledigt zu markieren.
Gutachten-ZIPs allein sind nicht das gesamte numerische Reproduktionspaket; ursprüngliche Matrixartefakte und historische Abhängigkeiten separat nennen.
[Draft-Triage](PR_TRIAGE_2026-09-16.md) ist eine Dispositionsnotiz, keine automatische Merge-/Close-Anweisung.

## P1 — unabhängige Prüfung, parallel

`A1-COMP@0a7c970 / AUTHOR-VERIFIED / EXTERNAL-OPEN` bleibt eingefroren.
Ein externes Vergleichszertifikat und ein Normierungslemma sind kein unabhängiger Review des anderen Operators L1.
Fremde Autorenbehauptungen, eigene Wiederholungen und externe Reproduktionen strikt trennen.

## P2 — rho1-Pilot, getrennte Nebenstrecke

Ziel: `rho_1=<d_1,Acal_1^(-1)d_1>`, `d_1=2sinh(x/2)`; Acal ist der volle Completionoperator.
Trial-/Galerkinwerte liefern untere Schranken. Ein oberer Vergleich aus L1 ist nur hinreichend.
Für u in D(Acal), r=d-Acal*u gilt `b(u)<=rho1<=b(u)+||r||^2/delta`, mit explizitem vollständigem Residual.
Resultat darf ein Enclosure, ein tatsächlich negativer Vollform-Zeuge oder eine Genauigkeitsbarriere sein; keine garantierte Entscheidung oder Frist.
Auf NULLPOL verschwindet D; P2 ist kein notwendiger Vorgänger von P3.

## P3 — X-C1-GEOM, aktive Hauptspur

C0-TYPE und die C1-Fluss-/Endpunktidentitäten sind Autorenresultate; positive vollständige Auswertung bleibt offen.
Kandidat benennt seine tatsächliche Änderung gegenüber dem ausgeschlossenen positiven kausalen Originalspeicher.
Vorwärts definierte quellen-/endpunktbedingte oder zweiseitige Geometrie; keine Fits, kein GNS aus angenommener Positivität.
Die vorhandenen Prime-, Gamma- und Polkanäle erhalten; festen Prime-2-Test einschließlich Gamma und f±ig behandeln.
Bei IN/OUT-Formen ist `||I_a v||<=||O_a v||` für JEDES v erforderlich; Vergleich der zwei Operatornormen genügt nicht.
Ein Arbeitsbudget begrenzt Versuche. Nur ein Beweis für eine benannte Klasse begründet deren No-Go; erfolglose Versuche allein nicht.

## P4/P5 — X-C2-ID und X-C3-WINDOW

Exakte polarisierte Identität auf dem gesamten genannten Testkern, dann Abschluss/Domain/Kernkontrolle.
Fensterkompatibilität ist schon beim Kandidaten zu berücksichtigen; additive F-Kokzyklen allein beweisen keinen positiven Readout.
Bei bereits exakten gemeinsamen Gramidentitäten ist `T_a v -> T_b v` auf erzeugten Räumen isometrisch; ein uniformer positiver L2-Gap ist dafür nicht nötig.
Konkrete Port-/Rand-Intertwiner und der vollständige globale Weil-/RH-Transfer bleiben eigene Beweispflichten.
Keine behauptete Äquivalenz von RH mit einer speziell vorgeschriebenen intrinsischen Architektur.
