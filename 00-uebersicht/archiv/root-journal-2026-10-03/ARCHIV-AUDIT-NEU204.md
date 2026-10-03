# Archiv: Direktaudit NEU-204

**Datum:** 2. August 2026
**Datei:** `NEU-204_Dyadische_Schalen_Singulaere_Aeussere_Derivation.md`
**Gesamtstatus:** ✓[M]_part

> Unveränderliches Archivdokument. Aktive Knotenstände in `ZWISCHENBILANZ_2026-08-01.md`.

---

## 1. Auditumfang

Geprüft wurden: NEU-204 vollständig; die BC-Präsentation und homogene Normalform aus NEU-183; die in NEU-203 formulierte Projektionsdifferenzenroute; die aktuelle Ordnerliste zur Bestimmung des nächsten tatsächlichen Knotens.

NEU-204 konstruiert aus dyadischen Projektionen eine Folge X_N in B_alg subset A_alg, die selbst nicht normkonvergiert, deren Kommutatoren mit jedem algebraischen BC-Generator aber in A_{C*} normkonvergieren. Daraus entsteht eine neutrale Derivation D: A_alg -> A_{C*}. Die Datei beweist außerdem, dass kein Implementierer aus A_{C*} existiert, und dass bereits D(mu_2) notin A_alg. Diese Hauptaussagen sind mathematisch tragfähig.

---

## 2. Primärextrakt

NEU-204 definiert:
- P_j := E_{2^j} = mu_{2^j} mu_{2^j}*
- q_j := P_j - P_{j+1}
- c_j = log(j+2)
- X_N := sum_{j=0}^{N-1} c_j q_j + c_N P_N

Bewiesen werden:
- ||X_N|| = c_N
- ||X_M - X_N|| = c_M - c_N
- [X_N, mu_k] -> mu_k B_{v_2(k)}
- [X_N, mu_k*] -> - B_{v_2(k)} mu_k*
- B_a := sum_{j=0}^inf (c_{j+a}-c_j) q_j in B_{C*}
- D(e(r)) = 0, D(mu_k) = mu_k B_{v_2(k)}, D(mu_k*) = - B_{v_2(k)} mu_k*

---

## 3. Dyadische Projektionsgeometrie

[O-204-geom]: ✓[M]

Aus der BC-Relation E_n = mu_n mu_n* = (1/n) sum_{ns=0} e(s) folgt P_j in B_alg. Da P_{j+1} <= P_j, ist q_j = P_j - P_{j+1} eine Projektion. Außerdem gilt P_j P_l = P_{max(j,l)} und daher q_j q_l = 0 fuer j != l. Teleskopierung: 1 = q_0 + ... + q_{N-1} + P_N. Diese Projektionsgeometrie ist vollständig korrekt.

---

## 4. Exakte Normen

[O-204-1]: ✓[M]

Bezüglich 1 = q_0 + ... + q_{N-1} + P_N wirkt X_N diagonal mit Eigenwerten c_0, ..., c_N. Da c_j streng wächst: ||X_N|| = c_N = log(N+2).

Für M > N:
X_M - X_N = sum_{j=N}^{M-1} (c_j-c_N) q_j + (c_M-c_N) P_M.
Wegen Orthogonalität der Projektionen: ||X_M - X_N|| = c_M - c_N = log((M+2)/(N+2)). Mit M=2N folgt ||X_{2N}-X_N|| -> log 2, also (X_N) nicht norm-Cauchy.

---

## 5. Verschiebungsrelationen

[O-204-shift]: ✓[M]

Für S_a = mu_{2^a} gilt: P_j S_a = S_a P_{(j-a)_+}. Für ungerades u gilt wegen teilerfremder BC-Relationen: P_j mu_u = mu_u P_j und ebenso für mu_u*. Damit kommutieren q_j, X_N und später B_a mit allen ungeraden Isometrien und deren Adjungierten. Die Verschiebungsrelationen sind korrekt.

---

## 6. Endliche Kommutatorformel

[O-204-comm-fin]: ✓[M]

Für N >= a gilt [X_N, S_a] = S_a C_{N,a} mit
C_{N,a} = sum_{j=0}^{N-a-1} (c_{j+a}-c_j) q_j + sum_{j=N-a}^{N-1} (c_N-c_j) q_j.

Der obere Randterm ist wesentlich. Der Sättigungsterm c_N P_N verhindert unkontrollierte P_N- bzw. P_{N-a}-Terme. Damit bestätigt NEU-204 zugleich die Korrektur aus dem NEU-203-Audit: Es wird nicht die feste Reihe sum_j c_j q_j realisiert, sondern ein gesättigter Mechanismus.

---

## 7. Normgrenzwerte B_a

[O-204-2a]: ✓[M]

Für festes a >= 1 setze d_j^(a) := c_{j+a} - c_j = log((j+a+2)/(j+2)). Dann d_j^(a) > 0 und d_j^(a) -> 0 monoton. Wegen der Orthogonalität der q_j konvergiert B_a := sum_{j=0}^inf d_j^(a) q_j in B_{C*} und ||B_a|| = d_0^(a) = log((a+2)/2).

Die Randterme in C_{N,a} verschwinden in Norm, also [X_N, mu_{2^a}] -> mu_{2^a} B_a. Für k = 2^a u mit u ungerade folgt [X_N, mu_k] -> mu_k B_a und [X_N, mu_k*] -> - B_a mu_k*.

---

## 8. Konstruktion der Derivation

[O-204-2]: ✓[M]

Da jeder Generatorgrenzwert existiert, kann fuer ein algebraisches Wort w = g_1 ... g_m die Identität [X_N, w] = sum_l g_1...g_{l-1}[X_N,g_l]g_{l+1}...g_m gliedweise im Grenzwert ausgewertet werden. Daraus entsteht D: A_alg -> A_{C*} mit
- D(e(r)) = 0
- D(mu_k) = mu_k B_{v_2(k)}
- D(mu_k*) = - B_{v_2(k)} mu_k*

Die Leibnizregel folgt direkt aus den inneren Kommutatoren. Die Definition ist unabhängig von der Wortdarstellung, weil jede algebraische Relation fuer jedes N exakt null ist. Zieltyp präzise: D in Der(A_alg, A_{C*}). Nicht bewiesen und für diesen Kandidaten falsch: D: A_alg -> A_alg.

---

## 9. Sternstruktur

✓[M]

Da X_N = X_N* gilt D(a*) = - D(a)*. Mit delta = iD erhält man die übliche Sternkonvention delta(a*) = delta(a)*. Dieser Teil ist korrekt.

---

## 10. Normunbeschränktheit

[O-204-unbdd]: ✓[M]

Für k = 2^a gilt D(mu_{2^a}) = mu_{2^a} B_a. Da mu_{2^a} Isometrie: ||D(mu_{2^a})|| = ||B_a|| = log((a+2)/2), waehrend ||mu_{2^a}|| = 1. Also sup_{||x||<=1} ||D(x)|| = inf. D ist bezüglich der C*-Norm unbeschränkt und besitzt keine beschränkte Derivationsfortsetzung auf die gesamte C*-Algebra.

[O-204-bounded-extension]: ✓[M]_neg

Fragen nach Abschließbarkeit oder Geschlossenheit bleiben offen: [O-204-closable] ?[O].

---

## 11. Neutralität

[O-204-neutral]: ✓[M]

Jedes X_N liegt im neutralen Grad. Daher erhält ad(X_N) jeden homogenen Sektor; ebenso der Grenzwert D. Also D((A_alg)_g) subseteq (A_{C*})_g. D besitzt Gewicht 1_Gamma, also neutrale Ladung.

[O-204-5]: ✓[M]_neg

Ausgeschlossen ist nur, dass die konkrete dyadische Konstruktion bereits eine geladene Derivation liefert. Ein späterer homogener Twist bleibt offen.

---

## 12. Nichtinnerheit in A_{C*}

[O-204-3]: ✓[M]

In der kanonischen Semigruppendarstellung auf l^2(N^x) wirken die e(r) diagonal und trennen die Basisvektoren. Jeder beschränkte Operator T, der mit allen pi(e(r)) kommutiert, muss diagonal sein: T delta_n = h(n) delta_n fuer eine beschränkte Folge h.

Angenommen pi(D(a)) = [T, pi(a)] für alle a. Aus D(mu_2)=mu_2 B_1 folgt rekursiv
h(2n)-h(n)=c_{v_2(n)+1}-c_{v_2(n)}.
Für ungerades n ergibt Iteration:
h(2^J n)-h(n)=sum_{j=0}^{J-1}(c_{j+1}-c_j)=c_J-c_0=log(J+2)-log 2,
Widerspruch zur Beschränktheit von h. Also existiert kein beschränkter Operator T, der D in dieser Darstellung implementiert. Insbesondere kein x in A_{C*} mit D(a)=[x,a].

**Umfangsklausel:** Nicht bewiesen und falsch wäre: D besitzt überhaupt keinen Implementierer. NEU-204 gibt selbst einen unbeschränkten diagonalen Implementierer an.

---

## 13. Unbeschränkter Implementierer und Hochschildklasse

[O-204-unbounded-implementer]: ✓[M]

In der Semigruppendarstellung implementiert der unbeschränkte diagonale Operator H delta_n = c_{v_2(n)} delta_n die Generatorformeln auf dem endlich getragenen Kern. „Äußer“ bedeutet hier also relativ zum Koeffizientenmodul A_{C*}, nicht vollständige Nichtimplementierbarkeit.

[O-204-HH1-analytic]: ✓[M]

A_{C*} ist ein A_alg-Bimodul. Im algebraischen Hochschildkomplex mit Koeffizienten in A_{C*} sind die Einskoränder genau die inneren Derivationen a -> xa-ax mit x in A_{C*}. Da D eine Derivation ist und kein solcher Implementierer existiert, folgt:
[D] != 0 in HH^1(A_alg, A_{C*})_1.

Dies ist der wichtigste positive Beitrag von NEU-204.

---

## 14. Scheitern des algebraischen Zieltyps

[O-204-4]: ✓[M]_neg

Unter der Fourieridentifikation B_{C*} cong C(Zhat) entspricht q_j der Indikatorfunktion der dyadischen Schale 2^j Zhat \ 2^{j+1} Zhat. Die Funktion B_1 nimmt auf der Schale exakter 2-adischer Bewertung j den Wert c_{j+1}-c_j > 0 an und besitzt am Ursprung den Wert 0.

Da c_{j+1}-c_j -> 0, ist B_1 stetig bei 0, aber nicht lokal konstant. Daher B_1 in B_{C*} \ B_alg. Folglich D(mu_2)=mu_2 B_1 notin A_alg. Somit ist fuer diesen Kandidaten D:A_alg->A_alg ausgeschlossen.

---

## 15. Verhältnis zu NEU-203

✓[M]

NEU-204 bestätigt den verallgemeinerten Knoten [O-203-4b], nicht aber die ursprüngliche feste Reihenform. Zu unterscheiden bleiben:
- [O-203-4a]: exakte feste z_p-Reihe — ?[O]
- [O-203-4b]: gesättigte dyadische Folge mit analytisch äußerer Derivation — ✓[M]

Die frühere Teilmarkierung aus NEU-203 kann für den verallgemeinerten analytischen Knoten auf ✓[M] angehoben werden.

---

## 16. Keine Cup- oder Dualzyklusbrücke

[O-204-cup]: ✓[M]_neg,Quelle

Aus [D] != 0 in HH^1(A_alg, A_{C*})_1 folgt noch keine Klasse in HH^4(A_alg, A_alg)_g. Für einen Cup-Aufstieg fehlen Typisierung des Produkts, Zielkomplex, Ladung/Zeitswirkung auf dem Koeffizientenmodul, Dualzeuge und Nicht-Korand-Nachweis. NEU-204 konstruiert diese Brücke nicht.

---

## 17. Terminologische Warnung

⚠[M]

„Singulär“ ist im Titel keine definierte algebraische oder operator-theoretische Klasse. Präzise bewiesen ist: D ist neutral, normunbeschränkt und A_{C*}-äußer; zugleich besitzt D einen unbeschränkten diagonalen Implementierer in der Semigruppendarstellung.

Bessere Bezeichnung: **neutrale, normunbeschränkte und A_{C*}-äußere Derivation**.

---

## 18. Vollständige Statustabelle NEU-204

| Bestandteil | Status | Befund |
|---|---|---|
| P_j,q_j in B_alg | ✓[M] | BC-Projektionsrelation |
| Orthogonalität der q_j | ✓[M] | Verschachtelte Projektionen |
| Teleskopzerlegung | ✓[M] | 1 = sum_{j<N} q_j + P_N |
| Konstruktion von X_N | ✓[M] | Endliches algebraisches Element |
| ||X_N|| = c_N | ✓[M] | Exakte Spektralnorm |
| Nicht-Cauchy-Eigenschaft | ✓[M] | Exakte Differenznorm |
| Verschiebungsrelationen | ✓[M] | Vollständiger Relationsbeweis |
| Endliche Kommutatorformel | ✓[M] | Sättigungsterm korrekt verarbeitet |
| Normkonvergenz zu B_a | ✓[M] | Orthogonale Schalen, d_j^(a)->0 |
| D: A_alg -> A_{C*} | ✓[M] | Wohldefiniert, Leibniz |
| Sternrelation | ✓[M] | D(a*) = -D(a)* |
| Neutralität | ✓[M] | Grad wird erhalten |
| Normunbeschränktheit | ✓[M] | Werte auf mu_{2^a} wachsen |
| Keine beschränkte Fortsetzung | ✓[M]_neg | Folgt aus Normunbeschränktheit |
| Kein Implementierer in A_{C*} | ✓[M] | Diagonaler Rekursionswiderspruch |
| Unbeschränkter Implementierer | ✓[M] | Wird ausdrücklich angegeben |
| [D] != 0 in HH^1(A_alg,A_{C*})_1 | ✓[M] | Wichtigster positiver Schluss |
| D(mu_2) in A_alg | ✓[M]_neg | B_1 stetig, aber nicht lokal konstant |
| Klasse in HH^1(A_alg,A_alg) | ✓[M]_neg | Für diesen Kandidaten typologisch ausgeschlossen |
| Geladener Grad g != 1 | ✓[M]_neg | Kandidat ist neutral |
| Cup-/Dualzyklusbrücke | ✓[M]_neg,Quelle | Nicht konstruiert |
| Abschließbarkeit | ?[O] | Nicht untersucht |
| **Gesamtstatus NEU-204** | **✓[M]_part** | Starke analytische Konstruktion, aber falscher Zieltyp |

---

## 19. Ersetzte und ergänzte Aussagen

1. **Status [O-204-1]:** Nicht ✓[K], sondern ✓[M].
2. **Tatsächliche Hochschildklasse:** Ergänzung erforderlich: [D] != 0 in HH^1(A_alg, A_{C*})_1.
3. **Umfang der Außenheit:** Korrekt ist nur: kein Implementierer aus A_{C*} und kein beschränkter Implementierer in der Semigruppendarstellung. Ein unbeschränkter diagonaler Implementierer existiert.
4. **Verhältnis zu NEU-203:** Korrekt: [O-203-4a] ?[O], [O-203-4b] ✓[M].

---

## 20. Beitrag zu Objekt X

NEU-204 ist der erste Knoten dieses Teilstrangs, der tatsächlich eine nichttriviale äußere Hochschild-Einsklasse konstruiert — allerdings mit erweitertem Koeffizientenmodul:
[D] != 0 in HH^1(A_alg, A_{C*})_1.

Das ist ein echter mathematischer Fortschritt. Zugleich bleiben wesentliche Defizite für das Langzeitziel bestehen: neutral statt geladen; Zielraum A_{C*} statt A_alg; keine Klasse in HH^1(A_alg,A_alg)_g; keine typisierte Cup-Brücke; kein Dualzyklus; keine Operatorrealisierung; keine Positivitäts- oder Hilbertraumkonstruktion.

Der belastbare Beitrag lautet daher: Kommutatorregularisierung kann eine echte äußere Derivation erzeugen, aber nur im analytisch erweiterten neutralen Koeffiziententyp.

---

## 21. DAG-Knoten NEU-204

| Knoten | Aussage | Status |
|---|---|---|
| [O-204-geom] | Dyadische Projektionsgeometrie vollständig korrekt | ✓[M] |
| [O-204-1] | Gesättigte dyadische Folge X_N ist nicht norm-Cauchy | ✓[M] |
| [O-204-shift] | Verschiebungsrelationen korrekt | ✓[M] |
| [O-204-comm-fin] | Vollständige endliche Kommutatorformel | ✓[M] |
| [O-204-2a] | Alle Generatorkommutatoren konvergieren in A_{C*} | ✓[M] |
| [O-204-2] | D:A_alg->A_{C*} neutrale Derivation | ✓[M] |
| [O-204-unbdd] | D bzgl. C*-Norm unbeschränkt | ✓[M] |
| [O-204-bounded-extension] | Beschränkte Fortsetzung auf A_{C*} | ✓[M]_neg |
| [O-204-3] | Kein Implementierer x in A_{C*} | ✓[M] |
| [O-204-unbounded-implementer] | Unbeschränkter diagonaler Implementierer | ✓[M] |
| [O-204-HH1-analytic] | [D] != 0 in HH^1(A_alg,A_{C*})_1 | ✓[M] |
| [O-204-4] | D(A_alg) subset A_alg | ✓[M]_neg |
| [O-204-5] | Geladener Grad g != 1 | ✓[M]_neg |
| [O-204-closable] | D bzw. iD abschließbar? | ?[O] |
| [O-204-cup] | Cup-Aufstieg nach HH^4(A_alg,A_{C*}) | ?[O] |
| [O-203-4a] | Feste Reihe sum c_p z_p | ?[O] |
| [O-203-4b] | Gesättigte dyadische Folge mit analytisch äußerer Derivation | ✓[M] |
| [O-199-3-sing] | Geladene A_alg-wertige singuläre Potentialderivation | ?[O] |

---

## 22. Gesamturteil

**NEU-204: ✓[M]_part**

Der mathematische Konstruktionsteil ist weitgehend korrekt und stärker als in der Datei selbst ausgewertet:
[D] != 0 in HH^1(A_alg, A_{C*})_1.

Die Teilmarkierung bleibt nötig, weil der Knoten den angestrebten Zieltyp nicht erreicht:
- D(A_alg) notsubseteq A_alg
- Konstruktion neutral statt geladen

**Nächster tatsächlicher Auditknoten:** NEU-205 — Geladener dyadischer Twist und Generatorfehlerterm.
