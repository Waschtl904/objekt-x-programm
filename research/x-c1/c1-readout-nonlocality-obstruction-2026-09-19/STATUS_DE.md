# C1: Räumliche Lokalität lässt sich nicht durch endlich viele globale Merkmale reparieren

Stand: 2026-09-19. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.
Anker: `617ffe2a3bfe12bef768b536b9eeffbbfb21f1da`.

Der neue Beitrag bearbeitet die benannte C1-Schnittstelle durch den
Ausschluss konkreter Kandidatenklassen. Er konstruiert noch keinen
positiven Readout und kein Objekt X.

**Erster Ausschlusssatz:** Für jeden B<=a<=1 kann ein exakter positiver
Gram-Readout der Weil-Form nicht aus einem räumlichen Anteil mit Reichweite
R<a plus einer beliebigen globalen Korrektur endlichen Ranges bestehen.
Die beiden Anteile müssen dabei nicht orthogonal sein. Die Aussage setzt
eine physische Ortsstruktur des lokalen Ausgaberaums voraus; sie betrifft
nicht jeden abstrakten Hilbertraum-Readout.

Der Beweis verwendet tatsächliche H1-Quellen
phi=(D^2-1/4)psi mit kompakter Unterstützung und exakt den beiden
ursprünglichen Mellinbedingungen. Zwischen getrennten Quellenblöcken
verschwinden sämtliche Prime- und L2-Paarungen. Die verbleibende
Gamma-Paarung hat trotzdem unendlichen Rang: Nach Auslöschung ihres
ersten Exponentialmodus bleiben unendlich viele positive Modengewichte.
Eine exakte Vandermonde-Identität liefert Rang N für jedes N. Eine
globale Korrektur vom Rang m könnte hingegen höchstens Mischrang 2m
erzeugen. N=2m+1 ergibt den Widerspruch.

Damit können auch 31 oder 191 globale Merkmale einen räumlich lokalen
unendlichen Rest nicht zu einer exakten C1-Gram-Darstellung ergänzen.
Dies widerspricht keinem früheren Schur-Satz: Dessen vollständiger
Hard-Raum und seine Form wurden nie als räumlich lokal vorausgesetzt.

Für einen rein räumlich begrenzten Readout ohne globale Zusatzkorrektur,
R<73/200, gibt es außerdem einen festen Even/Odd-Zeugen im bereits
positiven B-Core mit relativem Darstellungsfehler >10^-11. Eine negative
gemischte Paarung ist dabei keine negative Weil-Energie einer Quelle.

**Zweiter Ausschlusssatz:** Jeder strikt aktive Prime-Power-Kanal hat
innerhalb jeder Parität beide Vorzeichen, sogar auf Quellen, bei denen
alle anderen arithmetischen Beiträge verschwinden. Ein einzelner
signierter Prime-Beitrag kann deshalb keine positive Gram-Komponente
sein. Der Checker enthält zwanzig exakte Fälle für 2,3,4,5,7 am Endpunkt
a=1. Das beweist dort keine Positivität der vollständigen Weil-Form.

Weiter offen bleiben nichtlokale gemeinsame Prime-/Gamma-Readouts,
indefinite Kanalbeobachtungen in einem positiven Mediator, dessen
Intertwining, Moving 191D Low/Profile, nicht summierbarer Transport,
Full C1-GEOM, Objekt X und RH. Die nächste C1-Konstruktion muss die
vollständige nichtlokale Kopplung berücksichtigen; eine endliche globale
Korrektur zu einem kurzreichweitigen Readout genügt nicht.

**Reproduktion:** 84 neue exakte Prüfungen, sechs byte-/SHA-/Git-gebundene
analytische Herkunftsdateien, rationale Quellennormen und Restschranken,
ein exaktes Rang-drei-Beispiel und alle zwanzig Kanal-/Paritätsfälle.
JSON, Log und sieben Payload-Hashes werden bytegleich reproduziert.
Der allgemeine Rang- und Ausschlusssatz ist analytisch bewiesen; der
Checker ersetzt keine unabhängige Prüfung. Die früheren Matrixzertifikate
bleiben unverändert und werden von diesem neuen Checker nicht erneut
ausgeführt.

**Breitenvergleich:** Der Faktor 200 in 617ffe2 bezog sich ausdrücklich
auf b1c0186 mit 5*10^-13. Gegenüber ca3849a mit 5*10^-19 ist der Faktor
200 Millionen. Beide Rechnungen sind richtig; die Vergleichsanker sind
verschieden. Historische Dateien benötigen dafür keine Korrektur.
