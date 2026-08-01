# Archiv: Revisionsaudit NEU-202

**Datum:** 1. August 2026
**Datei:** `NEU-202_Konvergenz_Singulaerer_Zeuge_Kommutatorquotient.md`
**Gesamtstatus:** ✓[M]_part

> Dieser Audittext ist unveränderlich. Er ergänzt `ARCHIV-AUDIT-2026-07.md`.
> Aktive Knotenstände in `ZWISCHENBILANZ_2026-08-01.md`.

---

## 1. Auditumfang

Gepüft wurden: NEU-202 vollständig; revidierter Kandidat aus NEU-201; Augmentationscharakter aus NEU-185; BC-Präsentation und Gradierung aus NEU-183; aktuelle Ordnerstruktur.

NEU-202 widerlegt den konkreten Kandidaten H_sing = sum_{p prim} (log p)^{-1} mu_p e(1/p) durch drei Korrekturen: keine Normkonvergenz; Kommutatorformel nur für endliche Partialsummen; KMS-Auswertung verschwindet. Diese drei Kernkorrekturen sind im Wesentlichen richtig. Die Datei behält jedoch einige Typ-, Quellen- und Reichweitenfehler aus NEU-201 bei.

---

## 2. Primärextrakt

NEU-202 erklärt den positiven Beweisversuch vollständig für gescheitert:
- [O-202-conv]: ✓[M]_neg
- [O-202-comm-fin]: ✓[M] (vollständig korrekt, nicht nur part)
- [O-202-KMS]: ✓[M]_neg

Hauptargumente: Augmentationsschranke ||H_{F'}-H_F|| >= sum_{p in F'\F} (log p)^{-1}; endliche Kommutatorformel; Zeitinvarianz von KMS-Zuständen.

---

## 3. Augmentationscharakter auf der C*-Algebra

[O-202-eps-C*]: ✓[K/M]

NEU-185 konstruiert algebraisch den Charakter mit epsilon(mu_n)=1, epsilon(mu_n*)=1. NEU-202 verwendet ohne Zwischenschritt einen stetigen Charakter auf der vollen BC-C*-Algebra. Der Übergang ist reparierbar: Die Generatorzuordnung ist eine eindimensionale *-Darstellung der universellen BC-Präsentation und daher kontraktiv. ||epsilon||=1 folgt automatisch.

**Korrigierte Begründung:** epsilon respektiert die involutiven BC-Relationen und erstreckt sich daher zu einem unitalen *-Charakter auf die volle BC-C*-Algebra.

---

## 4. Normkonvergenz

[O-202-conv]: ✓[M]_neg

Für endliche Primzahlmengen F: ||H_F|| >= epsilon(H_F) = sum_{p in F} (log p)^{-1}. Somit ||H_{F'}-H_F|| >= sum_{p in F'\F} (log p)^{-1}. Da die skalare Primreihe divergiert (PNS/Chebyshev: sum_{p<=x} (log p)^{-1} >= pi(x)/log x ~ x/(log x)^2 -> inf), ist das Netz nicht norm-Cauchy.

**Umfangsklausel:** Nur der konkrete Kandidat mit Koeffizienten (log p)^{-1} ausgeschlossen. Andere Koeffizientenfolgen, andere Summationsverfahren, andere Erweiterungsräume: nicht ausgeschlossen.

---

## 5. Falsche Mertens-Berufung

[O-202-Mertens]: x[M]

NEU-202 schreibt zuerst, die Divergenz von sum_p (log p)^{-1} folge aus "Mertens' zweitem Satz", korrigiert sich aber intern, da der Mertenssatz sum_{p<=x} (1/p) betrifft. Korrekte Begründung: PNS oder Chebyshev. sum_{p<=x} (log p)^{-2} >= pi(x)/(log x)^2 ~ x/(log x)^3 -> inf.

---

## 6. l^2-Behauptung

[O-202-l2]: ✓[M]_neg

sum_p (log p)^{-2} = +inf. Korrekte Präzisierung: sum_{p<=x} (log p)^{-2} >= pi(x)/(log x)^2.

---

## 7. Nichtorthogonalität

[O-202-nonorth]: ✓[M]

Für verschiedene Primzahlen p != q: mu_p* mu_q = e(-1/p) mu_p* mu_q e(1/q) != 0 wegen koprime Relation mu_q* mu_p != 0. Nichtorthogonalität korrekt.

---

## 8. Gradmischung kein C*-Typfehler

[O-202-gradmischung]: x[M]

Eine vollständige gradierte C*-Algebra enthält auch inhomogene Elemente. Die Gradmischung ist kein Typfehler für die volle Algebra.

**Korrigierter Befund:**
- Als Element der vollen BC-C*-Algebra: scheitert am Konvergenzproblem, nicht an der Gradmischung.
- Als Kandidat für die homogene Potentialroute: typologisch ungeeignet, weil kein fester Ladungsgrad g vorliegt.

---

## 9. Weitere Konvergenztopologien

- H_sing nicht in A_Q^alg: ✓[M]_neg (keine Endlichkeitsbedingung)
- [O-202-weak]: ✓[M]_neg (Banach-schwach; Augmentationswerte divergieren)
- [O-202-SOT/WOT-faithful]: ✓[M]_neg (Partialsummen normunbeschränkt; UBP erzwingt Normbeschränktheit bei SOT/WOT)
- [O-202-distributional]: ?[O] (kein Raum definiert)

---

## 10. Konvergenz im Kommutatorquotienten

[O-202-quot-conv]: ✓[M]_neg

Jeder Charakter, insbesondere epsilon, faktorisiert über B/overline{[B,B]}. Daher ||[H_F]|| >= |epsilon(H_F)| -> inf. Auch kein Grenzwert im topologischen Quotienten. Im rein algebraischen Quotienten B/[B,B] ist "Konvergenz" ohne Topologie nicht definiert.

---

## 11. Endliche Kommutatorformel

[O-202-comm-fin]: ✓[M] (aufgewerted von part)

H_F mu_2 = sum_{p in F} (log p)^{-1} mu_{2p} e(2/p), mu_2 H_F = sum_{p in F} (log p)^{-1} mu_{2p} e(1/p).
Also [H_F, mu_2] = sum_{p in F} (log p)^{-1} mu_{2p} (e(2/p)-e(1/p)).
Vollständig korrekt. Status auf ✓[M] aufgewertet.

---

## 12. Korrektur des p=2-Terms

[O-202-p2]: ✓[M]

e(2/2)=e(1)=e(0)=1. Daher: (1/log 2) mu_4 (1-e(1/2)). Das Gruppenelement e(1/2) erfüllt e(1/2)^2=1, ist aber in der Gruppenalgebra nicht mit dem Skalar -1 identisch.

---

## 13. Unendlicher Kommutator

[O-202-comm-inf]: x[M]

Da H_sing nicht in B liegt, ist [H_sing, mu_2] kein wohlgeformter interner Kommutator. Auch das Netz [H_F, mu_2] kann nicht durch Stetigkeit des Kommutators aus einem Grenzwert gewonnen werden, weil der erforderliche Grenzwert fehlt.

---

## 14. Kommutatorquotient tautologisch trivial

[O-202-full-quot]: ✓[M]_neg

Für jedes endliche F: H_F in B, mu_2 in B, also [H_F, mu_2] in [B,B]. Somit [H_F, mu_2] = 0 in B/[B,B] tautologisch. NEU-202 zeigt nur KMS=0; der stärkere und einfachere Grund ist die definitorische Kommutatortrivialität.

**Umfangsklausel:** Nicht ausgeschlossen: externer Implementierer T not in A, da [T,b] nicht notwendig Kommutator zweier interner Algebraelemente.

---

## 15. KMS-Korrektur

[O-202-KMS]: ✓[M]_neg

KMS-Zustände sind im Allgemeinen keine Spuren. Für homogenen Summanden a_p = mu_{2p}(e(2/p)-e(1/p)) mit Zeitgewicht 2p: sigma_t(a_p) = (2p)^{it} a_p. KMS-Invarianz: phi_beta(a_p) = (2p)^{it} phi_beta(a_p) fuer alle t. Wegen 2p != 1: phi_beta(a_p) = 0. Somit phi_beta([H_F, mu_2]) = 0.

**Umfangsklausel:** Nicht ausgeschlossen: algebraische Dualfunktionale aus NEU-197, die nicht auf KMS beschränkt sind.

---

## 16. Historische Diagnose Commit e77deb3

[O-202-hist]: ✓[M]_neg,Quelle

Diagnose plausibel: phi_beta(mu_4) hat Zeitgewicht und muss verschwinden, phi_beta(mu_4 mu_4*) ist neutral. Commit e77deb3 über aktuelle Repositoryansicht nicht als prüfbare Primärfassung zugänglich. Aktuelle korrigierte KMS-Rechnung davon unberührt.

---

## 17. Grenzwert und Kommutator

[O-202-lim-comm]: x[M]

Für normkonvergente Folgen x_n -> x wäre [x_n, mu_2] -> [x, mu_2] erlaubt. Hier fehlt die Normkonvergenz. Daher kein lim_F H_F; Vertauschen von Grenzwert und Kommutator nicht erlaubt. Für schwache, starke oder distributionelle Grenzwerte: eigene Domänen- und Stetigkeitsargumente nicht gegeben.

---

## 18. Grenzwert und Dualfunktional

[O-202-regularized-KMS]: ?[O]

Für stetiges Funktional phi und Normkonvergenz dürfte phi(lim H_F) = lim phi(H_F) gelten. Normkonvergenz fehlt. Endliche Werte phi_beta([H_F, mu_2]) = 0. Ohne definierte Quotienten- oder Distributionentopologie kein Wert des unendlichen Kommutators. Regularisierter KMS-Grenzwert: ?[O] für künftig definiertes Verfahren; der in NEU-201 behauptete Wert: x[M].

---

## 19. Kein Hochschildkozykel

NEU-202 konstruiert keine geladene Derivation D_g in Der(A,A)_g. H_sing existiert nicht und besitzt keinen festen Ladungsgrad. Keine Vierkokette, kein Grenzwert für Kozykelprüfung.

- Geladene Derivation aus NEU-201/202-Kandidat: x[M]
- "Grenzwert bleibt Hochschildkozykel": nicht anwendbar
- Allgemeiner externer Implementierer T not in A, [T,A] subset A, deg T=g: ?[O]

---

## 20. DAG-Rückbau 201.B/C

**201.B:** Aufgebaut auf [X!=0 in B/[B,B] <=> exists KMS-Zustand mit phi(X)!=0]. Diese Aussage ist widerlegt. **201.B in ursprünglicher Form: x[M].** Ein neu formulierter Detektorknoten kann offen bleiben.

**201.C:** Wollte b_4(H_sing) in HH^4 gewinnen. Typologisch falsch, unabhängig vom Kandidaten. **201.C in ursprünglicher Form: x[M].** Neuer Cup- oder Dualzyklusknoten muss vollständig neu typisiert werden.

---

## 21. Anforderungen an nächsten Kandidaten

**21.1 Termweise Augmentationsneutralität**
epsilon(x_p)=0 ist hinreichend, nicht notwendig. Notwendig ist nur, dass die skalaren Partialsummen sum_{p in F} c_p epsilon(x_p) konvergieren.
- Termweise Augmentationsneutralität als notwendige Bedingung: x[M]

**21.2 Absolute Normsummierbarkeit**
sum_p ||c_p x_p|| < inf ist hinreichend, nicht notwendig. Korrekte notwendige und hinreichende Bedingung:
Forall epsilon>0, exists F_0, forall E mit E cap F_0 = empty: ||sum_{p in E} c_p x_p|| < epsilon.
- Absolute Normsummierbarkeit als notwendige Bedingung: x[M]

**21.3 Quotientendetektor**
Korrekt: Funktional muss Kommutatorraum annihilieren. Für vollen Quotienten B/[B,B]: jeder interne Kommutator ist tautologisch null. Neuer interner Kandidat kann die Sichtbarkeitsfrage nicht lösen.

---

## 22. Kandidatenskizzen y_p und z_p

**y_p = mu_p mu_p* - (1/p) 1:**
- epsilon(y_p) = 1 - 1/p: korrekt
- "Rang-1-Projektion" für mu_p mu_p*: x[M]. Korrekt: BC-Projektion = (1/p) sum_{k=0}^{p-1} e(k/p)

**z_p = mu_p mu_p* - mu_{p+1} mu_{p+1}*:**
- epsilon(z_p) = 0: korrekt
- "Projektionen gleichen Rangs": nicht bewiesen, abstrakt nicht sinnvoll
- z_p liegt im neutralen Grad
- Kommutator intern: tautologisch null im vollen Quotienten
- keine geladene Potentialderivation festen Grades
- z_p-Route als Lösung von [O-199-3]_sing: x[M]

**Umfangsklausel:** Elemente z_p können in anderem analytischen Kontext untersucht werden.

---

## 23. Korrigierter Hauptsatz von NEU-202

Das Netz (H_F) der endlichen Partialsummen von sum_p (log p)^{-1} mu_p e(1/p) bildet weder in der Norm- noch in der Banach-Schwachtopologie der BC-C*-Algebra ein konvergentes Netz.

Für jedes endliche F gilt:
- [H_F, mu_2] = sum_{p in F} (log p)^{-1} mu_{2p} (e(2/p)-e(1/p)): korrekte endliche Formel
- [H_F, mu_2] = 0 in B/[B,B]: tautologisch
- phi_beta([H_F, mu_2]) = 0 für jeden KMS-Zustand

Daraus folgt: Der konkrete Primreihenkandidat erzeugt weder einen singulären Quotientenzeugen noch eine geladene Hochschildderivation.

---

## 24. Vollständige Statustabelle NEU-202

| Bestandteil | Status | Befund |
|---|---|---|
| Algebraischer Augmentationscharakter | ✓[M] | In NEU-185 relationsgeprüft |
| Stetige C*-Erweiterung | ✓[K/M] | Richtig, aber in NEU-202 nicht typisiert |
| Normkonvergenz H_sing | ✓[M]_neg | Augmentationsschranke schließt sie aus |
| Schwache Banachkonvergenz | ✓[M]_neg | Augmentationswerte divergieren |
| SOT/WOT in treuer Darstellung | ✓[M]_neg | Partialsummen normunbeschränkt |
| Berufung auf Mertens | ×[M] | Falscher Satz; PNS/Chebyshev genügt |
| l^2-Behauptung | ✓[M]_neg | Reihe divergiert |
| Nichtorthogonalität | ✓[M] | Produkt verschiedener Summanden nicht null |
| Gradmischung als C*-Typfehler | ×[M] | Inhomogene Elemente in C*-Algebra zulässig |
| Gradmischung für homogene Potentialroute | ✓[M]_neg | Kein fester Ladungsgrad |
| Endliche Kommutatorformel | ✓[M] | Vollständig korrekt |
| p=2-Korrektur | ✓[M] | e(1/2) != -1 als Algebraelement |
| Unendlicher Kommutator | ×[M] | Kein Implementierer vorhanden |
| KMS-Test für endliche Partialsummen | ✓[M]_neg | Zeitgewicht erzwingt Null |
| Interner Kommutator im vollen Quotienten | ✓[M]_neg | Tautologisch quotiententrivial |
| 201.B ursprüngliche Form | ×[M] | Falsches universelles KMS-Kriterium |
| 201.C ursprüngliche Form | ×[M] | Nicht typisierte HH^4-Konstruktion |
| Termweise Augmentationsneutralität notwendig | ×[M] | Nur hinreichend |
| Absolute Normsummierbarkeit notwendig | ×[M] | Nur hinreichend |
| Kandidat y_p als Rang-1-Projektion | ×[M] | Falsche Rangbezeichnung |
| Kandidat z_p als geladene Fortsetzung | ×[M] | Neutral und intern |
| Echte geladene Derivation | ×[M] | Nicht konstruiert |
| Allgemeiner singulärer Potentialknoten | ?[O] | Bleibt offen |
| **Gesamtstatus NEU-202** | **✓[M]_part** | Richtiger Kandidaten-No-go, fehlerhafte Nachfolgerarchitektur |

---

## 25. Beitrag zu Objekt X

NEU-202 schließt den konkreten Primreihenkandidaten belastbar aus. Kein Fortschritt zur Weil-Form oder Operatorrealisierung.

Nicht gebaut: A-wertige geladene Derivation; nichttriviale Klasse in HH^1(A,A)_g; geladene Klasse in HH^4(A,A)_g; zulässiger Quotientenzeuge; Spur- oder Operatorabbildung; positive Gram- oder Hilbertraumstruktur.

Allgemeiner Zielknoten bleibt:
```
exists H in LC(Zhat\{0}) \ LC(Zhat)
mit alpha_k(H)-H in LC(Zhat) für alle nötigen Generatoren
und nichttrivialem partiellem Quotienten G_i^H
```

---

## 26. Aktualisierter DAG (NEU-202-Knoten)

| Knoten | Aussage | Status |
|---|---|---|
| [O-202-eps-C*] | Augm.-Char. erstreckt sich auf BC-C*-Algebra | ✓[K/M] |
| [O-202-conv] | H_sing normkonvergent in B | ✓[M]_neg |
| [O-202-weak] | H_sing schwach konvergent in B | ✓[M]_neg |
| [O-202-SOT/WOT-faithful] | H_F konvergiert in treuer Darstellung | ✓[M]_neg |
| [O-202-comm-fin] | Endliche Kommutatorformel [H_F, mu_2] | ✓[M] |
| [O-202-comm-inf] | Unendlicher Kommutator [H_sing, mu_2] | ×[M] |
| [O-202-full-quot] | Interner Kommutator liefert Klasse in B/[B,B] | ✓[M]_neg |
| [O-202-KMS] | KMS-Zustand detektiert [H_F, mu_2] nichtverschwindend | ✓[M]_neg |
| [O-202-quot-conv] | H_F konvergiert in Norm von B/overline{[B,B]} | ✓[M]_neg |
| [O-201-B-original] | KMS-Zustände als universeller Quotientendual | ×[M] |
| [O-201-C-original] | b_4(H_sing) erzeugt Klasse in HH^4 | ×[M] |
| [O-202-next-augmentation] | Termweise epsilon(x_p)=0 notwendig | ×[M] |
| [O-202-next-absolute] | Absolute Normsummierbarkeit notwendig | ×[M] |
| [O-202-zp] | z_p-Route für geladene Potentialroute | ×[M] |
| [O-199-3-sing] | Echter punktierter Potentialkandidat | ?[O] |
| [O-external-implementer] | Externer homogener Implementierer T not in A | ?[O] |
| [O-202-distributional] | H_sing in Distributionen-/Bidualraum | ?[O] |

---

## 27. Gesamturteil

**NEU-202: ✓[M]_part**

Der mathematische No-go gegen den konkreten Kandidaten ist richtig: Primreihenkandidat aus NEU-201: ✓[M]_neg.

Die Datei ist dennoch nur teilweise tragfähig, weil sie:
- die Gradmischung fälschlich als C*-Typfehler bezeichnet (×[M])
- eine widersprüchliche Mertens-Quelle verwendet (×[M])
- die ursprünglichen Knoten 201.B und 201.C nicht konsequent verwirft (×[M])
- hinreichende Konvergenzbedingungen als notwendig ausgibt (×[M])
- mit z_p erneut interne, neutrale Elemente als Nachfolger der geladenen Route vorschlägt (×[M])

**Nächster Auditknoten:** NEU-203 — Projektionsdifferenzen und Kommutatortrivialität.

Damit ist der Block NEU-196 bis NEU-202 vollständig direktauditiert.
