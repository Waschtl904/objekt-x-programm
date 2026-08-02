# Archiv: Direktaudit NEU-205

**Datum:** 2. August 2026
**Datei:** `NEU-205_Geladener_Dyadischer_Twist_Generatorfehlerterm.md`
**Gesamtstatus:** ✓[M]_part

> Unveränderliches Archivdokument. Aktive Knotenstände in `ZWISCHENBILANZ_2026-08-01.md`.

---

## 1. Auditumfang

Geprüft wurden: NEU-205 vollständig; die dyadische Schalenkonstruktion und die kanonische Semigruppendarstellung aus NEU-204; die BC-Relationen und die homogene Gradierung aus NEU-183; der Restriktionssatz aus NEU-187; NEU-206 nur insoweit, wie es unmittelbar auf die Architekturentscheidung von NEU-205 aufbaut.

Die aktuelle Ordnerliste bestätigt NEU-205 als direkten Nachfolger von NEU-204 und NEU-206 als nächsten tatsächlichen Knoten.

---

## 2. Primärextrakt

NEU-205 versucht, die neutrale dyadische Folge
X_N = sum_{j=0}^{N-1} c_j q_j + c_N P_N

durch einen homogenen Faktor vom Grad g = m/n != 1 zu laden. Untersucht werden die drei Platzierungen
- V_g X_N
- X_N V_g
- mu_m X_N mu_n*
mit V_g = mu_m mu_n*.

Die Datei behauptet für alle drei Platzierungen die Divergenz bestimmter Kommutatoren mit e(r), schließt homogene Projektionen in A_g aus und schlägt anschließend homogene Partialisometrieschalen als nächste Architektur vor.

---

## 3. Harter Relationsfehler in (205.1.1)

[O-205-rel]: ×[M]

NEU-205 schreibt
- mu_k e(r) = e(kr) mu_k
- e(r) mu_k* = mu_k* e(kr)

Diese Richtungen sind falsch. In der kanonischen Semigruppendarstellung folgt korrekt:
- e(r) mu_k = mu_k e(kr)
- mu_k* e(r) = e(kr) mu_k*

Die Gegenrichtungen benötigen die Transferabbildung alpha_k(e(r)) = (1/k) sum_{ks=r} e(s). Damit ist Formel (205.1.1) in der angegebenen Form falsch.

---

## 4. Grundformel für V_g

[O-205-basic]: ✓[M]

Trotz der falsch orientierten Vorrelationen ist die anschließend verwendete Formel korrekt:
[V_g, e(r)] = mu_m ( e(nr) - e(mr) ) mu_n*.

Denn
- V_g e(r) = mu_m e(nr) mu_n*
- e(r) V_g = mu_m e(mr) mu_n*

mit M_{g,r} := e(nr)-e(mr).

---

## 5. Charakterfehler M_{g,r}

⚠[M]

Es gilt M_{g,r} = e(mr)(e((n-m)r)-1). Sei t=(n-m)r. Im Fouriermodell auf Zhat ist die Nullmenge von M_{g,r} die offene Untergruppe d(t) Zhat, wobei d(t) die additive Ordnung von t ist. Insbesondere gilt M_{g,r}(0)=0, und M_{g,r} verschwindet auf einer offenen Umgebung des Ursprungs.

Nicht korrekt ist jedoch die Formulierung, M_{g,r} sei „außerhalb von U gleichmäßig positiv“. M_{g,r} ist im Allgemeinen komplexwertig; korrekt ist nur eine Abschätzung des Betrags außerhalb des vollständigen Charakterkerns.

---

## 6. Exakte dyadische Dichotomie

✓[M]

Für den Fehlerterm M_{g,r} ergeben sich zwei Fälle:

**Fall A:** d(t)=2^a ist eine Zweierpotenz. Dann gilt M_{g,r} q_J = 0 für alle J >= a; der Fehlerterm verschwindet also auf dem gesamten hochbewerteten dyadischen Schwanz.

**Fall B:** d(t) besitzt einen ungeraden Primteiler. Dann enthält jede hinreichend hohe dyadische Schale Punkte außerhalb des Charakterkerns, und es existiert eta_t>0 mit ||M_{g,r} q_J|| >= eta_t für beliebig große J.

NEU-205 trennt diese beiden Fälle nicht, obwohl genau diese Dichotomie darüber entscheidet, ob das Wachstum der Koeffizienten c_J in die Kommutatornorm hineinreicht.

---

## 7. Gegenbeispiel zur behaupteten Divergenz für alle r

[O-205-dyadic-all-r]: ×[M]

Setze g=2, m=2, n=1, r=1/2. Dann
M_{2,1/2} = e(1/2)-1,
und dieses Element verschwindet auf 2 Zhat = P_1. Daher gilt für N>=1:
M_{2,1/2} X_N = c_0 M_{2,1/2} q_0.

Somit ist mu_2 M_{2,1/2} X_N ab N=1 konstant und insbesondere normbeschränkt. Damit ist die Behauptung widerlegt, für jedes nichttriviale r außerhalb (m-n)^(-1) Z divergiere der entsprechende Kommutator.

---

## 8. Der kandidatenspezifische No-go bleibt richtig

[O-205-1]: ✓[M]_neg
[O-205-2]: ✓[M]_neg
[O-205-3]: ✓[M]_neg

Für eine Derivation müssten die Kommutatoren mit jedem Generator e(r) konvergieren. Es genügt also, zu jedem g!=1 wenigstens ein r mit divergentem Fehlerterm zu finden.

Da Multiplikation mit n-m auf Q/Z surjektiv ist, kann r so gewählt werden, dass (n-m)r Ordnung 3 besitzt. Dann nimmt |e((n-m)r)-1| auf jeder hohen dyadischen Schale den Wert sqrt(3) an. Daraus folgt für passende Basisvektoren in der kanonischen Darstellung Normdivergenz der e(r)-Kommutatoren für alle drei konkreten Platzierungen.

Präzise ausgeschlossen sind damit nur die drei Kandidaten
- V_g X_N
- X_N V_g
- mu_m X_N mu_n*

Nicht bewiesen ist Divergenz für jeden nichttrivialen Charakter.

---

## 9. Harter Fehler in der Sandwichformel

[O-205-sandwich-formula]: ×[M]

NEU-205 behauptet implizit
(e(mnr)-e(mr)) Y_N^{(S)}.

Korrekt ist aber
[ mu_m X_N mu_n*, e(r) ] = mu_m X_N ( e(nr)-e(mr) ) mu_n*.

Der behauptete Transport durch mu_m ist unzulässig. Der kandidatenspezifische No-go bleibt mit der korrigierten Formel dennoch erhalten.

---

## 10. Normwachstum allein genügt nicht

✓[M]

Die Warnung
||X_N|| -> inf does not imply ||[V_g X_N,e(r)]|| -> inf
ist richtig.

Das in §205.5 notierte Gegenbeispiel mit einer beliebigen Nullmengenprojektion ist jedoch unvollständig, weil aus M_{g,r} p = 0 nicht automatisch M_{g,r} mu_n* p = 0 folgt. Die Projektion muss zusätzlich an den Transport durch mu_n* angepasst werden. Daher: Gegenbeispiel in der notierten Form nur ✓[M]_part.

---

## 11. Status des dyadischen Dilemmas

[O-205-4a]: ×[M]
[O-205-4b]: ✓[M]_neg

Korrekt ist nur:
Für jedes g != 1 existiert ein r, so dass der e(r)-Kommutator für jede der drei Platzierungen divergiert.

Falsch ist die stärkere Aussage:
Für alle r notin (m-n)^(-1) Z tritt Divergenz auf.

---

## 12. Keine homogenen Projektionen in A_g

[O-205-5b]: ✓[M]_neg

Sei q in A_g mit q=q*=q^2. Dann liegt q^2 in A_{g^2}, zugleich q in A_g. Wegen der direkten Gradierung folgt aus q^2=q!=0 die Gleichung g^2=g, also g=1. Daher enthält A_g für g!=1 keine nichttrivialen algebraischen homogenen Projektionen.

Nicht ausgeschlossen werden homogene Partialisometrien oder inhomogene Projektionen.

---

## 13. Architektur (III) ist nicht ausgeschlossen

[O-205-5c-proof]: ×[M]
[O-205-5c]: ?[O]

NEU-205 behauptet, aus kleinen Kommutatoren von V_g(N) und großem X_N folge notwendig ||V_g(N)|| -> 0 und daraus weiter das Verschwinden der Produktkommutatoren. Beide Normschlüsse sind unbegründet.

Korrekt ist lediglich die Produktabschätzung
||[V_N X_N, mu_k]|| <= ||V_N|| ||[X_N,mu_k]|| + ||[V_N,mu_k]|| ||X_N||,
und beide Terme müssen separat kontrolliert werden.

Ein relationsangepasster N-abhängiger homogener Twist ist durch NEU-205 also nicht ausgeschlossen.

---

## 14. Homogene Partialisometrieschalen

[O-206-model]: ✓[K/M]

Der vorgeschlagene Ersatz w_j = mu_m p_j mu_n* ist typkorrekt, wenn p_j in B_alg eine Projektion ist. Dann sind
- w_j* w_j = mu_n p_j mu_n*
- w_j w_j* = mu_m p_j mu_m*
Projektionen.

Sind die p_j paarweise orthogonal, folgt biorthogonale Orthogonalität. NEU-206 konstruiert anschließend genau eine solche Familie und erreicht eventuelle Kommutation mit jedem fest gewählten e(r).

Nicht bewiesen sind in NEU-205 bereits die Konvergenz der Kommutatoren mit mu_k, mu_k* oder die Nichtinnerheit eines Grenzwerts.

---

## 15. Motivationsaussage zu D_g(e(r))

⚠[M]

Die Aussage „g!=1 implies D_g(e(r)) != 0“ ist pointwise falsch. Insbesondere gilt für jede Derivation D_g(1)=0.

Der Restriktionssatz aus NEU-187 liefert nur die kohomologische Aussage: Ist [D_g] != 0 in HH^1(A,A)_g, dann ist auch [D_g|_B] != 0. Daraus folgt nicht, dass jeder Charaktergenerator einzeln einen nichtverschwindenden Wert tragen muss.

---

## 16. Zielraum einer hypothetischen Grenzderivation

⚠[M]

Selbst wenn sämtliche Generatorkommutatoren der endlichen Kandidaten in Norm konvergierten, erhielte man zunächst nur einen Kandidaten
D_g : A_alg -> A_C*,

nicht automatisch
D_g : A_alg -> A_alg.

NEU-204 zeigt bereits im neutralen Fall, dass algebraische Kommutatoren in normierten Grenzwerten aus dem algebraischen Zielraum herausfallen können. Diese Zieltyptrennung ist in NEU-205 nicht explizit genug.

---

## 17. Dateistatus NEU-205

| Bestandteil | Auditstatus | Befund |
|---|---|---|
| Standardrelationen (205.1.1) | ×[M] | Verschiebungsrichtungen falsch |
| Formel [V_g,e(r)] = mu_m(e(nr)-e(mr))mu_n* | ✓[M] | Trotz falscher Vorrelation korrekt |
| M_{g,r}(0)=0 | ✓[M] | Charakterdifferenz verschwindet am Ursprung |
| „M_{g,r} außerhalb U positiv“ | ⚠[M] | Komplexwertig; vollständiger Nullkern nötig |
| Divergenz für jedes nichttriviale r | ×[M] | Zweierpotenz-Charaktere schneiden den dyadischen Schwanz ab |
| Linksplatzierung als geladener Kandidat | ✓[M]_neg | Für jedes g!=1 existiert ein divergenter Generator |
| Rechtsplatzierung als geladener Kandidat | ✓[M]_neg | Gleicher kandidatenspezifischer Ausschluss |
| Sandwichplatzierung als geladener Kandidat | ✓[M]_neg | No-go bleibt nach Formelkorrektur bestehen |
| Sandwichformel (205.4.3) | ×[M] | Falscher Transfer durch mu_m |
| Normwachstum allein reicht nicht | ✓[M] | Wichtige Warnung korrekt |
| Konkretes Gegenbeispiel mit p=1_U | ✓[M]_part | Projektion an mu_n*-Transport anpassen |
| Keine Projektionen in A_g, g!=1 | ✓[M]_neg | Für algebraische homogene Projektionen bewiesen |
| Ausschluss Architektur (III) | ×[M] | Zentrale Normschlüsse falsch |
| Allgemeiner Status Architektur (III) | ?[O] | Bleibt offen |
| Partialisometrieschalen als Modelltyp | ✓[K/M] | Typkorrekt; NEU-206 baut darauf auf |
| Kommutatorkonvergenz mit mu_k, mu_k* | ?[O] | In NEU-205 nicht erreicht |
| Geladene äußere Derivation | ✓[M]_neg,Quelle | In NEU-205 nicht konstruiert |
| Algebraischer Zieltyp | ?[O] | Selbst bei analytischer Konvergenz ungeklärt |
| **Gesamtstatus** | **✓[M]_part** | Kandidaten-No-go rettbar, mehrere Kernformeln falsch |

---

## 18. Ersetzte Aussagen

1. **BC-Relationen**
   Falsch:
   - mu_k e(r)=e(kr)mu_k
   - e(r)mu_k*=mu_k*e(kr)

   Korrekt:
   - e(r)mu_k=mu_k e(kr)
   - mu_k* e(r)=e(kr)mu_k*

2. **Sandwichfehlerterm**
   Falsch: (e(mnr)-e(mr)) Y_N^{(S)}.

   Korrekt:
   [mu_m X_N mu_n*, e(r)] = mu_m X_N (e(nr)-e(mr)) mu_n*.

3. **Dyadischer Ausschluss**
   Zu stark:
   r notin (m-n)^(-1) Z implies divergence.

   Korrekt:
   Für jedes g!=1 existiert ein r mit divergentem e(r)-Kommutator.

4. **Architektur (III)**
   Falsch:
   ||V_g(N)|| -> 0 implies ||[V_g(N)X_N,mu_k]|| -> 0.

   Korrekt ist nur die Produktabschätzung
   ||[V_N X_N,mu_k]|| <= ||V_N|| ||[X_N,mu_k]|| + ||[V_N,mu_k]|| ||X_N||.

---

## 19. Beitrag zu Objekt X

NEU-205 schließt drei unmittelbar naheliegende Ladungsversuche aus:
- V_g X_N
- X_N V_g
- mu_m X_N mu_n*

Der belastbare Grund lautet: Für jeden festen nichtneutralen Grad g existiert mindestens ein Charaktergenerator e(r), dessen Kommutator mit dem geladenen dyadischen Kandidaten divergiert.

Das ist ein echter, aber eng begrenzter No-go. Nicht erreicht werden eine geladene Derivation, ein geladener HH^1-Knoten, eine Cup-Konstruktion, ein Dualzeuge oder eine Operator-/Hilbertraumrealisierung.

Die vorgeschlagene Partialisometriearchitektur ist typologisch sinnvoll und führt korrekt zu NEU-206, aber ihr Konvergenz- und Nichtinnerheitsproblem ist in NEU-205 noch vollständig offen.

---

## 20. Aktualisierter DAG

| Knoten | Aussage | Status |
|---|---|---|
| [O-205-basic] | [mu_m mu_n*, e(r)] = mu_m(e(nr)-e(mr))mu_n* | ✓[M] |
| [O-205-rel] | mu_k e(r)=e(kr)mu_k und e(r)mu_k*=mu_k*e(kr) | ×[M] |
| [O-205-dyadic-all-r] | Jeder nichttriviale Charakterfehler divergiert auf dem dyadischen Schwanz | ×[M] |
| [O-205-1] | Linksplatzierung V_g X_N scheitert für jedes g!=1 an einem Generator | ✓[M]_neg |
| [O-205-2] | Rechtsplatzierung X_N V_g scheitert ebenso | ✓[M]_neg |
| [O-205-3] | Sandwich mu_m X_N mu_n* scheitert ebenso | ✓[M]_neg |
| [O-205-sandwich-formula] | (e(mnr)-e(mr))Y_N | ×[M] |
| [O-205-4a] | Divergenz für alle r notin (m-n)^(-1) Z | ×[M] |
| [O-205-4b] | Alle drei konkreten dyadischen Ladungsansätze scheitern | ✓[M]_neg |
| [O-205-5b] | Nichttriviale Projektion in A_g, g!=1 | ✓[M]_neg |
| [O-205-5c-proof] | N-abhängiger Twist durch Normargument allgemein ausgeschlossen | ×[M] |
| [O-205-5c] | Existenz eines relationsangepassten N-abhängigen homogenen Twists | ?[O] |
| [O-206-model] | Homogene biorthogonale Partialisometrieschalen | ✓[K/M] |
| [O-206-transport] | Normkonvergenz der mu_k- und mu_k*-Kommutatoren | ?[O] |
| [O-charged-analytic] | Geladene äußere Derivation A_alg -> A_C* | ?[O] |
| [O-charged-algebraic] | Geladene äußere Derivation A_alg -> A_alg | ?[O] |

---

## 21. Gesamturteil

**NEU-205: ✓[M]_part**

Der zentrale kandidatenspezifische No-go ist rettbar:
Die drei naiven geladenen dyadischen Platzierungen scheitern.

Zu korrigieren sind jedoch:
- die grundlegenden BC-Relationen,
- die Sandwichformel,
- die behauptete Divergenz für jeden nichttrivialen Charakter,
- das unvollständige Nullmengen-Gegenbeispiel,
- der unbegründete Ausschluss der N-abhängigen Twistarchitektur.

**Nächster tatsächlicher Auditknoten:** NEU-206 — Homogene Partialisometrieschalen, Orthogonalität und Charakterkern.
