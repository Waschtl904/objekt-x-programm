# Antwortänderung: Informationsgrenze und kleinster gemeinsamer Test

20. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Ausgangsstand: `2e8e86770c0fde6ef5ea69b0178775eab34d5de4`.

## 1. Entscheidung dieses begrenzten Auftrags

**NO_DATA_SUPPORTED_RESPONSE_CANDIDATE.** Aus den bisher gespeicherten
Residualpaarungen wird keine verbesserte Antwortmatrix ausgewählt. Es gibt
keinen neuen gerichteten Energievergleich und keinen Ausschluss weiterer
Antwortregeln. Auch die früher untersuchten ±1-%-Varianten bleiben offen.

Die [Matrix-Vorprüfung vom 18. Oktober](../w9-response-preflight-2026-10-18/PROOF.md)
hat die fehlenden Antwort-/Residualkreuzgrame bereits benannt. Das spätere
K-Paket erneuert die Metrik; der Schur-Untertest und seine Fehlerschärfung
arbeiten weiterhin mit derselben Residualquelle. Keines dieser Pakete liefert
die fehlenden Antwortkanäle nach. Eine erneute Optimierung allein mit diesen
Residualdaten wäre kein neuer aussagekräftiger Matrixtest.

Neu präzisiert wird hier der kleinste Datenbedarf für **eine** vorab gewählte
Antwortänderung am festen geraden Zeugen: zwei gewichtete skalare Paarungen
mit gemeinsamer Fehlerkontrolle statt eines sofortigen Aufbaus aller zwölf
Antwortkanäle. Das ist eine Reduktion des Testumfangs, noch keine quantitative
Begründung für eine aussichtsreiche Matrix oder eine Integrationsfreigabe.

## 2. Zulässiger Spielraum am festen Zeugen

Verwende die physischen Räume und Domänen des gebundenen Arbeitsauftrags.
Es seien Phi die zwölf alten Antwortfunktionen, A=A9, D=A Phi,
A12=Phi* A Phi, F=Phi* C, und Fhat das zugelassene Kopplungsmodell.
Für einen festen exakt W-normierten geraden Schalenvektor z schreibe

    fhat=Fhat z, t0=X0 fhat, r0=Cz-D t0.

Eine feste endliche Matrix X definiert dieselbe Art von beschränkter Antwort
P_X=Phi X Fhat. Die Form-/Operatordomänen der zwölf Phi-Spalten bleiben dabei
Voraussetzung. Der neue Auswahlalgorithmus darf keine A11-Zielpositivität
verwenden und muss vor seiner gerichteten Abnahme festgelegt werden.

Auch wenn man wie bisher symmetrische reelle Matrizen verlangt, ist bei
fhat!=0 am einzelnen Zeugen jeder Koeffizientenschritt u algebraisch möglich:

    Y=(u fhat*+fhat u*)/(fhat* fhat)
      -(fhat* u) fhat fhat*/(fhat* fhat)^2,
    Y*=Y, Y fhat=u, X=X0+Y.

Dies ist eine Existenz-/Reduktionsformel für exakte reelle Daten, keine hier
gewonnene rationale Kandidatenmatrix. Eine rationale Einfrierung müsste ihre
Abweichung einschließen. Der ganze Schalenraum, Koeffizientenverstärkung und
Fehlertransport bleiben für X separat zu kontrollieren. Am gebundenen geraden
Zeugen schließt bereits die erste Fhat-Koordinate Null aus; `verify.py` prüft
dies aus den gespeicherten Intervallen und rationalen Rohkoeffizienten, ohne
eine neue Funktionsintegration.

## 3. Gemeinsame Veränderung von Budget und Energie

Für eine vorab festgelegte symmetrische rationale Matrix Y setze
X_s=X0+sY, v=Y fhat, r_s=r0-s Dv. s ist reell. Alle Größen müssen in derselben
physischen Metrik ausgewertet werden. Definiere

    g=Re(v*(Fz-A12 t0)), a=v* A12 v.

Dann gilt für das tatsächliche Budget exakt

    K_s=K_0-2s g+s^2 a.                                      (1)

Sei V eine feste positive berechenbare Teilmajorante, zum Beispiel die vier
berechneten Beiträge der K-Pilot-Majorante. Setze

    E_0=<r0,V r0>, gamma=Re<Dv,V r0>, beta=<Dv,V Dv>.

Damit folgen

    E_s=E_0-2s gamma+s^2 beta,                                (2)
    K_s-E_s=(K_0-E_0)+2s(gamma-g)+s^2(a-beta).                 (3)

Der notwendige neue Energieinhalt für diese eine Linie besteht aus gamma
und beta. g und a verwenden den alten A12-/F-Anschluss, jedoch mit ihren
ganzen Fehlern. K0 und E0 kommen aus dem **zum gewählten V passenden** Paket.
Das alte W9-Teilenergieintervall darf nicht als K*-Intervall eingesetzt werden.

Für die Skalierungslinie Y=X0 ist Dv=D t0 nur eine gemeinsame Antwortfunktion.
Dies würde die früher allein durch ein Normdreieck behandelten ±1-%-Fälle
erstmals gemeinsam auswertbar machen. Es ist keine Behauptung, dass diese
Linie einen Gewinn liefert. Eine freie 12-dimensionale Antwortsuche benötigt
weiterhin D* V D und D* V r0 (und für mehrere Zeugen ihre gemeinsamen Blöcke).

## 4. Fehler und Einseitigkeit

Schreibe V=L*L auf den benötigten Funktionen. Wenn q=L Dv und p=L r0 durch
q0,p0 mit vollständigen gewichteten Fehlern ||q-q0||<=e_q und
||p-p0||<=e_p dargestellt sind, gelten

    |gamma-Re<q0,p0>| <= ||q0|| e_p+||p0|| e_q+e_q e_p,
    |beta-||q0||^2| <= 2||q0|| e_q+e_q^2.                    (4)

Integrationsintervalle und gemeinsame Modellfehler sind dabei zusätzlich
vollständig zu enthalten; vorhandene Fehler dürfen nicht doppelt bezahlt
oder als verschwunden behandelt werden. Die hohe Projektion braucht ihre
ganze Selbst- und Kreuzpaarung, keinen Legendre-Abbruch. Die Norm- und
Koeffizientenfehler von v müssen in e_q eingehen. Kleinere reine F-F-Fehler
dürfen weiterhin nicht auf F-J übertragen werden.

Alternativ kann das neue Budget direkt wie in der Vorprüfung mit

    Khat_s=d[z]-2 Re<fhat,t_s>+t_s* A0 t_s,
    e_K(s)=2 delta_F ||t_s||+delta_A ||t_s||^2

eingeschlossen werden. d, fhat, Normierung und Koeffizientenintervalle bleiben
gerichtet. Die ganze Antwortnorm erhält für M=X_s X0^-1 den neuen Gram
G_s=M G0 M*. Ein guter Einzelzeuge ersetzt diese uniforme Kontrolle nicht.

Erst nach gerichteter Auswertung von (1)–(4) gilt am festen s:

- E_s,lower>K_s,upper: der gewählte Vergleich ist an dieser Richtung ausgeschlossen.
- E_s,upper<K_s,lower: nur die Teilenergie liegt darunter; der fehlende positive
  Dualterm und der ganze Raum bleiben offen.
- Überlappung: unentschieden; keine automatische Erweiterung des Rechenauftrags.

Ein niedriger variationaler **Untertest** ist weiterhin kein Teilpass. Er
kann das zweiseitige Teilenergieintervall in der zweiten Zeile nicht ersetzen.
Für eine vollständige Majorante W>=A^-1 wäre D* W D-A12>=0. Für den Teil V
ist beta>=a dagegen nicht garantiert. Ein scheinbar beliebig wachsender
Teilbudgetüberschuss ist deshalb kein Grund, große Antwortmatrizen auszuwählen.

## 5. Exakte Kontrolle der fehlenden Kreuzinformation

Ein zweidimensionales Kontrollmodell demonstriert die Informationsgrenze;
es modelliert keine Objekt-X-Funktion und liefert keinen neuen Objekt-X-No-Go.
In beiden Fällen seien

    A=I_2, W=[[2,1],[1,2]] >= I_2, d=5/2, X0=1, r0=e2.

Fall plus verwendet Phi=e1, C=e1+e2. Fall minus verwendet Phi=-e1,
C=-e1+e2. Dann sind in beiden Fällen

    A12=1, F=1, ||C||^2=2, K0=3/2, E0=2, D* W D=2.

Sogar W und die gesamte alte Residualfunktion sind identisch. Lediglich
die benötigte Antwortkreuzpaarung gamma ist +1 beziehungsweise -1.
Dieselbe neue Matrix X=3/2 liefert in beiden Fällen K=7/4, aber

    E_plus=3/2, K-E_plus=1/4,
    E_minus=7/2, K-E_minus=-7/4.

Die tatsächliche Schurreserve d-C* A^-1 C=1/2 ist in beiden Fällen positiv.
Somit kann aus altem Residualgram, A12, F, Budget und sogar Antwortselbstgram
allein weder das Vorzeichen des neuen Vergleichs noch das bessere Vorzeichen
der Änderung bestimmt werden. Die vollständigen Quelldefinitionen enthalten
natürlich zusätzliche Information: Ihre fehlenden Paarungen müssen ausgewertet
oder durch eine passende Identität hergeleitet werden. Das Beispiel behauptet
keine Unbestimmbarkeit aus dem gesamten Repository.

## 6. Datenabgleich, Aufwand und Stopentscheidung

`verify.py` prüft unveränderliche SHA-256-gebundene Eingabebytes, die vorhandenen
Schemas und die gemeinsame Herkunft des geraden Zeugen. Die 12 Spalten in
PAIRS sind gemäß Erzeuger und Beweis Residuen R0 z_j. Die dortigen 287×12
hohen Kreuzwerte und 96×12 baren Paarungen sind daher keine zwölf D-Kanäle.
Der K-Pilot nutzt denselben PAIRS-Hash; die Schur-Nachfolger denselben
physischen Kandidaten und dasselbe K_P-Zertifikat. Die archivierten Ergebnisse
werden als gebundene Voraussetzungen gelesen, nicht erneut zertifiziert.

Die fünf alten Varianten, der K-Pilot und die Schur-Fehlerschärfung werden
nicht wieder ausgeführt. Die neuen rationalen Kontrollmodelle, die symmetrische
Updateidentität und die gemeinsame Änderungsformel werden exakt überprüft.
Ein isolierter Replay umfasst nur dieses neue kleine Prüfpaket und seine
expliziten Eingaben, keinen vollständigen Repository-/Integrationsreplay.

**Entscheidung:** Kein Kandidat ist derzeit mit den vorhandenen numerischen
Vergleichsdaten zur Zertifizierung qualifiziert. Ein neuer großer
Antwortgramlauf ist durch diesen Auftrag nicht gerechtfertigt. Der kleinste
konkret beschriebene Datenauftrag wäre eine einzige kombinierte gerade
Antwortfunktion für eine vorab gewählte Linie, mit den zwei Kennzahlen und
Fehlern aus Abschnitt 3–4. Seine Implementierung und Laufzeit sind hier nicht
gemessen. Der alte 22–24-Minuten-Lauf pro Parität ist keine Laufzeitgarantie
für diesen anderen Auftrag. Für eine Auswahl fehlen weiterhin ein begründeter
Richtungsvorschlag und ein begrenzter Kosten-/Nutzenentscheid.

Damit ist die aktuelle **Datenprüfung** abgeschlossen, nicht die Auswahl
eines verbesserten Vergleichs. Das entsprechende offene Planhäkchen bleibt
offen. Andere Unterformen und Antwortregeln sind nicht ausgeschlossen;
Meilenstein 4, N12, Objekt X und externe Prüfung bleiben offen.
