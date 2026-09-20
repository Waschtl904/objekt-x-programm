# Nächste Forschungsaufgaben

> GENERATED FILE — DO NOT EDIT
> Quelle: [RESEARCH_STATE.yaml](RESEARCH_STATE.yaml). Navigation, keine Satzpromotion.

Genau zwei Hauptfronten. Die vollständigen Beweise und Eingabebindungen stehen in den verlinkten Paketen.

## Transport: Moving 191D Low-Block und Profilreserve

`MOVING-191D-LOW-PROFILE` — OPEN. B<=a<=1; bisherige volle Positivität reicht bis B+10^-10. Der uniforme hohe Tail und die Core-Schur-Kongruenz sind belegt; Low/Profile bleibt offen.

Offene Obligationen:

- `MOVING-191D-FINITE-SCHUR-POSITIVITY`: Tatsächliche endliche Schur-Einträge einschließen und positives Vorzeichen beweisen — Größere zusammenhängende Bereiche in B<=a<=1; volle hohe Antwort einbeziehen.
- `MOVING-PROFILE-RESERVE-RENEWAL`: Erneuerbare Low/Profile-Reserve konstruieren — Zusätzliche Kopplungen bei der physischen Fortsetzung a->b; die Core-Kongruenz allein reicht nicht.
- `NON-SUMMABLE-TRANSPORT`: Nicht summierbares oder uniformes Fortsetzungsgesetz beweisen — Über das vorhandene endliche positive Band hinaus; quantitative Schrittweiten.
- `CHANNEL-7-FULL-POSITIVE-CONTROL`: Tatsächlichen Kanal-7-Eintritt positiv kontrollieren — Vollständige niedrige und hohe Quellen einschließlich Profilkopplungen; qualitative Stetigkeit und hoher Tail sind vorhanden.

Akzeptierter strategischer Fortschritt:

- Uniformer positiver Low-Schurblock auf einem größeren Band mit vollständiger hoher Antwort.
- Erneuerbare Profilreserve mit nicht kollabierendem Gesetz.
- Nicht summierbarer oder uniformer Transport.
- Vollständige positive Kontrolle beim tatsächlichen Eintritt von Kanal 7.

Nicht ausreichend:

- Bloße mikroskopische Breitenverbesserung ohne neue skalierbare Methode.
- Eine endliche Matrix ohne vollständige Tail- und Mischtermkontrolle.
- Die bereits bewiesene Core-Kongruenz als erneuten Abschluss der Low/Profile-Aufgabe ausgeben.

Verwendbare Registereinträge: `ALL-PARITY-BAND-B-PLUS-1E-10`, `MOVING-HIGH-TAIL-1-OVER-41`, `C1-MOVING-191D-SCHUR-CONGRUENCE`.

## C1: kompakte Defektkontraktion

`C1c-COMPACT-DEFECT-CONTRACTION` — OPEN. Fester Horizont 1, B<=a<=1: q_a>=0 genau dann, wenn ||R_a||<=1, äquivalent S_a^p>=0 je Parität. C1a und C1b sind für den benannten Kandidaten autorenseitig abgeleitet.

Offene Obligationen:

- `MOVING-191D-FINITE-SCHUR-POSITIVITY`: Tatsächliche endliche Schur-Einträge einschließen und positives Vorzeichen beweisen — Größere zusammenhängende Bereiche in B<=a<=1; volle hohe Antwort einbeziehen.
- `C1c-COMPACT-DEFECT-CONTRACTION`: Unabhängig ||R_a||<=1 beweisen — Ziel B<=a<=1, insbesondere a=1; äquivalent S_a^p>=0 in beiden Paritäten, ohne Rückschluss aus vorausgesetzter Weil-Positivität.
- `C1d-COMPATIBLE-POSITIVE-COMPLETION`: Intrinsischen positiven Defektabschluss mit Übergängen konstruieren — Kompressionsidentität von R_a*R_a allein beweist kein Intertwining korrigierter Readouts.
- `UNBOUNDED-HORIZON-COMPATIBILITY`: Kompatible unbeschränkte Horizontfolge konstruieren — Der bisherige Spektralkandidat verwendet den festen Horizont 1.
- `FULL-WEIL-TEST-CLASS`: Vollständige geeignete Weil-Testklasse identifizieren — Exakte Normalisierung, kanonischer globaler Readout und nichtzirkuläre Rückbindung an das Weil-Kriterium.

Akzeptierter strategischer Fortschritt:

- Rigorose Einschließung der tatsächlichen endlichen Schur-Einträge zusammen mit dem bereits vollständigen High-Response-Rest.
- Rationale obere Einschließung des größten Singularwerts und unabhängiger Kontraktionsnachweis.
- Quantitative endpunktuniforme Kontrolle über die vorhandene qualitative Stetigkeit hinaus.
- Die bewiesene Verbindung zum Moving-191D-Core für einen positiven endlichen Abschluss nutzen.
- Global kompatibler positiver Defektabschluss und kontrollierte Erweiterung des Horizonts.

Nicht ausreichend:

- Ausschließlich endlichrangige Diagnostik oder kleine Modellmatrizen.
- Lokale Kontraktion aus bereits bekannter Weil-Positivität zurückfolgern.
- Eine formale Quadratwurzel ohne Beweis von Intrinsizität und Übergangskompatibilität.
- Den bereits kontrollierten hohen Singularwerttail oder die vorhandene Low/High-Zerlegung erneut als offenen Gate präsentieren.

Verwendbare Registereinträge: `C1-NOGO-SHORT-RANGE-FINITE-RANK`, `C1-NOGO-INDIVIDUAL-PRIME-POSITIVE-BLOCK`, `C1a-COUPLED-SPECTRAL-MEDIATOR`, `C1b-ZERO-EXTENSION-INTERTWINING`, `C1-COMPACT-DEFECT-IDENTITY`, `C1-191D-HIGH-DEFECT-CONTRACTION`, `C1-MOVING-191D-SCHUR-CONGRUENCE`, `C1-COMPLETE-HIGH-RESPONSE-BOUND`, `C1-MOVING-SINGULAR-CONTINUITY`.

Horizont und Testklasse sind gemäß dem jeweiligen Scope zu beachten. Ein lokaler Gate-Abschluss ist keine RH-Promotion.
