# Archiv: Direktaudit NEU-203

**Datum:** 2. August 2026
**Datei:** `NEU-203_Projektionsdifferenzen_Kommutatortrivialitaet.md`
**Gesamtstatus:** ✓[M]_part

> Unveränderliches Archivdokument. Aktive Knotenstände in `ZWISCHENBILANZ_2026-08-01.md`.

---

## 1. Auditumfang

Gepüft wurden: NEU-203 vollständig; BC-Relationen und algebraische Diagonalalgebra aus NEU-183; NEU-204 ausschließlich insoweit, wie NEU-203 [O-203-4] durch diese Datei für positiv geschlossen erklärt; Abgrenzung zum partiellen Quotienten aus NEU-197 und zur geladenen Potentialroute aus NEU-199–202.

NEU-203 definiert E_n = mu_n mu_n* und z_p = E_p - E_{p+1}. Projektions-, Norm- und Kommutatorgeometrie sind korrekt. Der positive Abschlussknoten [O-203-4] ist überdehnt: NEU-204 realisiert nicht die z_p-Reihe, sondern einen gesättigten dyadischen Mechanismus mit neutralem Zieltyp A_alg → A_{C*}.

---

## 2. Primärextrakt

NEU-203 formuliert:
- E_n := mu_n mu_n*, z_p := E_p - E_{p+1}
- Behauptungen: E_n in C[Q/Z], eps(z_p)=0, ||z_p||=1, z_p in [A,A]
- Normkonvergente Reihen x = sum c_p z_p liefern nur innere Derivation ad(x)
- Beschränkte trizielle Funktionale verschwinden auf solchen Grenzwerten
- Singularitätskriterium: x_N nicht norm-Cauchy, [x_N,a] für jeden Generator norm-Cauchy
- NEU-204 realisiert diesen Mechanismus positiv (Erklärung in NEU-203)

---

## 3. Algebrazugehörigkeit

[O-203-type]: ✓[M]

BC-Relation (R3): mu_n mu_n* = (1/n) sum_{k=0}^{n-1} e(k/n). Daher E_n = mu_n mu_n* in B_alg. Somit z_p = E_p - E_{p+1} in B_alg. Da B_alg kommutativ: [z_p, e(r)] = 0 für alle r in Q/Z.

---

## 4. Augmentationsneutralität

[O-203-1a]: ✓[M]

eps(E_n) = (1/n) sum_{k=0}^{n-1} eps(e(k/n)) = (1/n) * n * 1 = 1. Somit eps(z_p) = eps(E_p) - eps(E_{p+1}) = 1 - 1 = 0. Verhindert nur die konkrete positive Augmentationsdivergenz aus NEU-201/202; beweist weder Normkonvergenz noch Quotientennichttrivialität.

---

## 5. Exakte Norm

[O-203-1b]: ✓[M]

E_p und E_{p+1} sind kommutierende Projektionen in der abelschen Diagonalalgebra. z_p ist selbstadjungiert mit Spektralwerten in {-1, 0, 1}. Untere Schranke: In der Semigruppendarstellung E_p delta_p = delta_p, E_{p+1} delta_p = 0, also z_p delta_p = delta_p, folglich ||z_p|| >= 1. Damit ||z_p|| = 1.

Für Skalare c_p: ||c_p z_p|| = |c_p|. Normkonvergenz der Reihe aequivalent zu sum_p |c_p| < inf (absolute Normsummierbarkeit).

---

## 6. Kommutatorstruktur

[O-203-1c]: ✓[M]

Wegen mu_n* mu_n = 1: [mu_n, mu_n*] = mu_n mu_n* - mu_n* mu_n = E_n - 1.
Daher: z_p = E_p - E_{p+1} = [mu_p, mu_p*] - [mu_{p+1}, mu_{p+1}*] in [A_alg, A_alg].
Folglich z_p in [A_{C*}, A_{C*}].

---

## 7. Quotientennotation: Warnung

⚠[M]

NEU-203 verwendet A/[A,A] ohne Index. Nicht identisch mit dem partiellen homogenen Quotienten aus NEU-197. In B_alg gilt z_p != 0, aber [z_p] = 0 in A_alg/[A_alg, A_alg] (da z_p in [A_alg, A_alg]). Diese Unterscheidung trägt NEU-204 nach.

Künftig strikt zu unterscheiden:
- A_alg / [A_alg, A_alg] (algebraischer Quotient)
- A_{C*} / overline{[A_{C*}, A_{C*}]} (normabgeschlossener Quotient)

---

## 8. Normkonvergenz und Innerheit

[O-203-2]: ✓[M]_neg

(c_p) in l^1 => x = sum_p c_p z_p konvergiert absolut in C*-Norm => x in A_{C*} => D_x = ad(x) ist inner.

Korrekte Ersatzformel (allgemeiner als in NEU-203):
  x in A_{C*} => ad(x) ist inner.
Der abgeschlossene Kommutatorraum overline{[A,A]} wird erst für die Spurfrage relevant; Innerheit folgt bereits aus der Algebrazugehörigkeit des Implementierers.

**Präzise Umfangsklausel:** Ausgeschlossen ist jede äußere Derivation, deren Implementierer normlimitär in der Algebra liegt.

---

## 9. Beschränkte trizielle Funktionale

[O-203-3]: ✓[M]_neg

Jedes beschränkte trizielle Funktional tau erfüllt tau([a,b]) = 0 für alle a,b in A_{C*}. Wegen Stetigkeit auch tau = 0 auf overline{[A_{C*},A_{C*}]}. Da x in overline{[A_{C*},A_{C*}]}, gilt tau(x) = 0.

**Umfangsklausel:** Nicht ausgeschlossen: unstetige algebraische Funktionale; nichttrizielle Funktionale; Funktionale auf partiellen Quotienten; externe Implementierer.

Hinweis: Falls x not in [A_alg, A_alg] aber x in overline{[A_{C*},A_{C*}]}, könnte eine nichttriviale Klasse im algebraischen Quotienten nur durch ein unstetiges quotiententaugliches Funktional detektiert werden.

---

## 10. Teleskopierung F.1–F.3

[O-203-F]: ✓[M]_neg,Quelle

NEU-203 erklärt alle drei Fälle (F.1–F.3) als erledigt. Die aktuelle Datei enthält weder Definition der drei Fälle noch entsprechende Rechnungen. Allgemeiner Satz (unbestritten): Normgrenzwert endlicher Kommutatorsummen liegt in overline{[A,A]}. Vollständigkeit und konkrete Ausführung der drei Fälle: nicht prüfbar.

---

## 11. Kommutatorregularisierungskriterium

[O-203-criterion]: ✓[K/M]

Kriterium: x_N nicht norm-Cauchy, aber [x_N, a] für jeden Generator a norm-Cauchy. Für jedes endliche Wort w = g_1 ... g_m entsteht dann D(w) = sum_{l=1}^m g_1...g_{l-1} D(g_l) g_{l+1}...g_m. Derivation auf A_alg, sofern: Werte in festgelegtem A-Bimodul; Relationen respektiert; repräsentantenunabhängig. NEU-204 führt diesen Übergang aus.

**Wichtige Gegenrichtung:** Nicht-Cauchy-Implementierer allein => Nichtinnerheit folgt NICHT. Beispiel: x_N = N*1 + x divergiert, [x_N, a] = [x, a] inner. Nichtinnerheit muss separat bewiesen werden.

---

## 12. Abhängigkeitsfehler [O-203-4]

[O-203-4-original]: ×[M]

NEU-203 erklärt [O-203-4] durch NEU-204 für positiv geschlossen. NEU-204 verwendet aber nicht die feste Reihe sum_p c_p z_p mit z_p = E_p - E_{p+1}, sondern dyadische Schalen q_j = E_{2^j} - E_{2^{j+1}} mit gesättigten Näherungen sum_{j=0}^{N-1} c_j q_j + c_N E_{2^N}. Der Sattigungsterm c_N E_{2^N} ist für die Kommutatorkonvergenz wesentlich und nicht in (203.12) enthalten.

Zusätzlich: NEU-204 liefert nur D: A_alg -> A_{C*} mit neutralem Grad deg D = 1_Gamma; keine algebraisch A_alg-wertige oder geladene Derivation.

**Korrigierte Aufspaltung:**

[O-203-4a]: Feste z_p-Reihe (203.12) mit diverg. Implementierer, konverg. Kommutatoren, nichtinnerer Derivation: ?[O]

[O-203-4b]: Gesättigte dyadische Folge X_N in B_alg, Generatorkommutatoren konvergieren, D: A_alg -> A_{C*} neutral und ohne Implementierer aus A_{C*}: ✓[M]_part
(Teilmarkierung, weil Zieltyp A_alg -> A_{C*} != benötigtem A_alg -> A_alg)

[O-203-4c]: D(A_alg) subset A_alg: ?[O]

[O-203-4d]: Geladene Variante deg D = g != 1: ?[O]

---

## 13. Geladene Potentialroute

[O-203-geladene-route]: ✓[M]_neg,Quelle

E_n, z_p in A_1 (neutraler Grad). Jede innere Derivation durch Linearkombinationen erhält Gradsektoren. Dyadische Grenzderivation aus NEU-204: deg D = 1_Gamma. Nicht konstruiert: D_g in Der(A_alg, A_alg)_g für g != 1. Kein allgemeiner No-go gegen spätere geladene Modifikationen.

---

## 14. Vollständige Statustabelle NEU-203

| Bestandteil | Status | Befund |
|---|---|---|
| E_n in B_alg | ✓[M] | BC-Relation (R3) |
| z_p in B_alg | ✓[M] | Differenz zweier Diagonalprojektionen |
| [z_p, e(r)] = 0 | ✓[M] | B_alg abelsch |
| eps(z_p) = 0 | ✓[M] | Beide Projektionen Augmentationswert 1 |
| ‖z_p‖ = 1 | ✓[M] | Differenz verschiedener kommutierender Projektionen |
| z_p in [A_alg, A_alg] | ✓[M] | Explizite Differenz zweier Kommutatoren |
| Notation A/[A,A] | ⚠[M] | Algebraischer und topologischer Quotient nicht getrennt |
| l^1-Reihe normkonvergent | ✓[M] | Absolute Normkonvergenz |
| Normkonverg. Impl. => inner | ✓[M]_neg | Derivation ist inner |
| Beschr. trizielle Funktionale | ✓[M]_neg | Verschwinden auf overline{[A,A]} |
| Teleskopierungsfälle F.1–F.3 | ✓[M]_neg,Quelle | In aktueller Datei nicht vorhanden |
| Kommutatorregularisierungskrit. | ✓[K/M] | Tragfähiges Konstruktionsschema |
| Nicht-Cauchy => nichtinner | ×[M] | Nichtinnerheit muss separat bewiesen werden |
| [O-203-4] z_p-Reihenform | ?[O] | NEU-204 realisiert nicht diese Reihe |
| Dyadischer Mechanismus [O-203-4b] | ✓[M]_part | Neutral und nur A_{C*}-wertig |
| Geladene Route | ✓[M]_neg,Quelle | Nicht konstruiert |
| Beitrag zu HH^1(A,A)_g | ?[O] | Aus NEU-203 folgt keine solche Klasse |
| **Gesamtstatus NEU-203** | **✓[M]_part** | Korrekte Projektionsgeometrie, überdehnter Nachfolgerstatus |

---

## 15. Ersetzte Aussagen

**Innerheitsgrund:** Korrekt: x in A_{C*} => ad(x) inner. (Nicht: x in overline{[A,A]} => inner.)

**Normkonvergenz:** Korrekt: sum_p c_p z_p normkonvergent in Algebra => ad(sum) inner. (Nicht: nur l^1 => inner.)

**[O-203-4]:** Korrekt: [O-203-4a] ?[O]; [O-203-4b] ✓[M]_part.

**"Positive Realisierung":** Korrekt: Eine neutrale normunbeschränkte Derivation D: A_alg -> A_{C*} wird durch Grenzwerte interner Kommutatoren realisiert. Nicht realisiert: D: A_alg -> A_alg; deg D = g != 1.

---

## 16. Beitrag zu Objekt X

Zwei belastbare methodische Einsichten:
1. Normkonvergenz des Implementierers kann keine äußere Derivation erzeugen.
2. Ein möglicher äußerer Grenzmechanismus muss die Kommutatoren, nicht den Implementierer selbst, regularisieren.

Der z_p-Pfad liefert keine positive Konstruktion. Nicht entstanden: geladene Derivation; A_alg-wertige äußere Derivation; Klasse in HH^1(A_alg,A_alg)_g; geladene Vierklasse; Operator- oder Positivitätsrealisierung der Weil-Form.

Der tatsächliche positive Teiltreffer aus NEU-204 gehört in einen analytischen Koeffizientenmodulpfad A_alg -> A_{C*}, nicht in den algebraischen geladenen HH^1(A,A)_g-Knoten.

---

## 17. DAG-Knoten NEU-203

| Knoten | Aussage | Status |
|---|---|---|
| [O-203-1a] | eps(z_p) = 0 | ✓[M] |
| [O-203-1b] | ‖z_p‖ = 1 | ✓[M] |
| [O-203-1c] | z_p in [A_alg, A_alg] | ✓[M] |
| [O-203-2] | Normkonvergenter Implementierer => innere Derivation | ✓[M]_neg |
| [O-203-3] | Beschr. trizielle Funktionale detektieren Normgrenzwerte aus overline{[A,A]} nicht | ✓[M]_neg |
| [O-203-F] | Vollständige Fälle F.1–F.3 | ✓[M]_neg,Quelle |
| [O-203-criterion] | Nicht-Cauchy-Impl., Cauchy-Generatorkommutatoren | ✓[K/M] |
| [O-203-4a] | Feste z_p-Reihe, diverg. Impl., nichtinnere Derivation | ?[O] |
| [O-203-4b] | Gesättigte dyadische Folge X_N, D: A_alg->A_{C*}, neutral | ✓[M]_part |
| [O-203-4c] | D(A_alg) subset A_alg | ?[O] |
| [O-203-4d] | Geladene Variante deg D=g!=1 | ?[O] |
| [O-199-3-sing] | Punktiertes singulaeres Potential | ?[O] |
| [O-203-geladene-route] | Geladene Route durch NEU-203 | ✓[M]_neg,Quelle |
| [O-203-4-original] | [O-203-4] z_p-Form durch NEU-204 bewiesen | ×[M] |

---

## 18. Gesamturteil

**NEU-203: ✓[M]_part**

Die Projektions-, Norm- und Kommutatorgeometrie ist korrekt. Das methodische Kommutatorregularisierungskriterium ist tragfähig.

Zu korrigieren:
- [O-203-4] in z_p-Reihenform ist nicht durch NEU-204 bewiesen (×[M])
- Nicht-Cauchy => nichtinner ohne Zusatzbedingung (×[M])
- Notation A/[A,A] ohne Präzisierung (⚠[M])

**Nächster Direktaudit:** NEU-204 — Dyadische Schalen und analytische äußere Derivation.
