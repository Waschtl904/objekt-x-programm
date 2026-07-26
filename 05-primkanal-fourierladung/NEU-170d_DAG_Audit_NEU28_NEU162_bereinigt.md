# NEU-170d — Bereinigter DAG-Stand nach Direktaudit NEU-20/26/28/29/161/162

**Datum:** 18. Juli 2026  
**Status:** Epistemisch bereinigt. Quellenbasiert.  
**Auditierter Quellenkegel:** NEU-20, NEU-26, NEU-28, NEU-29, NEU-161, NEU-162, NEU-170a, NEU-170b, NEU-170c  
**Vorgänger:** NEU-170c  

---

## Zentrale Hauptdiagnose

$$\boxed{\begin{gathered}
\text{Der Einmodenansatz liefert eine algebraisch nichtverschwindende skalare Vorfaktorstruktur,}\\
\text{aber weder seine Herkunft aus }[L_3]\text{ noch das Nichtverschwinden}\\
\text{des Zielkantenvektors }E_{1;\,1\to p}^{\mathrm{rel}}\text{ ist bewiesen.}
\end{gathered}}$$

Der Hauptpfad ist **zweifach blockiert** — logisch unabhängig:

$$[L_3] \not\longmapsto L_3^\circ = e_1 V_1 \qquad \text{(Herkunftsblockade)}$$

$$(p-1)\log p \neq 0 \;\not\Rightarrow\; C_p(e_{1-p}V_p) \neq 0 \qquad \text{(Zielkantenblockade, ohne }[H\text{-}163\text{-}2]\text{)}$$

---

## 1. Abgeschlossene Auditbefunde

| Punkt | Inhalt | Status |
|---|---|---|
| `[O-170b-1]` | NEU-20 konstruiert $L_3$ | `✓[M]neg` |
| `[O-170c-2g]` | NEU-28 konstruiert $L_3$, $L_3\|_{\mathrm{diag}}$ oder beweist $C_L \neq 0$ | `✓[M]neg` |
| `[O-170c-2i-audit]` | NEU-161 weist $s \neq 0$ korrekt als Eingangsannahme aus, enthält keinen neuen Fehler | `✓[M]` |
| `[O-170c-2j-audit]` | NEU-162 beweist keinen geladenen Koeffizienten des gegebenen $[L_3]$ | `✓[M]neg` |
| `[O-170c-2k-audit]` | $dP^{\mathrm{ch}} = P^{\mathrm{ch}}d$ wird im auditierten Quellenkegel nicht konstruiert | `✓[M]neg` |

**Präzisierung zu `[O-170c-2k-audit]`:** Dies ist ein negativer *Quellenbefund*, kein mathematischer Unmöglichkeitssatz. Für ein mathematisch negatives Ergebnis wäre eine konkrete Kochain $H$ mit $dP^{\mathrm{ch}}H \neq P^{\mathrm{ch}}dH$ erforderlich — die im Quellenkegel nicht konstruiert wurde.

---

## 2. Offene Punkte

| Punkt | Inhalt | Status |
|---|---|---|
| `[O-170b-2]` | Raumtyp: $L_3 \in C^4(B_3,B_3)$? $B_3$? $A_{BC}^{an}$? $\mathrm{End}(\mathcal{H})$? | `?[O]` |
| `[O-170b-3]` | Definition von $L_3\|_{\mathrm{diag}}$ und Bedeutung „diagonal" | `?[O]` |
| `[O-170b-4]` | Kanonische Auswahl $\sigma_{L_3}: [L_3] \mapsto L_3$ | `?[O]` |
| `[O-170b-5]` | Repräsentantenunabhängigkeit des $Wres$-Insertionsfunktionals | `?[O]` |
| `[O-170c-2h]` | $a = L_3$ typzulässig in NEU-28-Spurformel | `?[O]` |
| `[O-170c-2i]` | $P^{\mathrm{ch}}(L_3^\circ) \neq 0$ | `?[O]` |
| `[O-170c-2j-exist]` | $\exists\, L \in \mathrm{Rep}([L_3])$ mit $P^{\mathrm{ch}}(L) \neq 0$ | `?[O]` |
| `[O-170c-2k-exist]` | $P^{\mathrm{ch}}$ als Kettenprojektor neu konstruierbar? ($dP^{\mathrm{ch}} = P^{\mathrm{ch}}d$) | `?[O]` |
| `[O-170c-2ℓ]` | $[P^{\mathrm{ch}}]([L_3]) \neq 0$ | **gesperrt** bis `[O-170c-2k-exist]` |

**Präzisierung zu `[O-170c-2ℓ]`:** Der Ausdruck $[P^{\mathrm{ch}}]([L_3]) \neq 0$ ist derzeit nicht wohldefiniert — $P^{\mathrm{ch}}$ ist als linearer Projektor nichttrivial, aber ohne bewiesenen Kettenabstieg noch keine Abbildung auf $HH^4(B_3)$. Auch nach positivem Kettenabstieg müsste gezeigt werden, dass $[P^{\mathrm{ch}}]$ auf der möglicherweise verdrehten oder gefilterten Kohomologie wirkt.

---

## 3. Typblockade und Ladungsblockade — logisch unabhängig

**Typblockade:**
$$[L_3]\in HH^4(B_3) \quad\not\Rightarrow\quad L_3\in A_{BC}^{an}$$
Die Substitution $a = L_3$ in die allgemeine NEU-28-Spurformel ist typologisch unbelegt (`[O-170c-2h]`).

**Ladungsblockade:**
$$L_3 \neq 0 \quad\not\Longrightarrow\quad P^{\mathrm{ch}}(L_3) \neq 0$$
Ein nichttrivialer Repräsentant könnte vollständig im Nullmodus liegen:
$$L_3 = \sum_m \ell_{0,m} e_0 V_m \neq 0, \qquad P^{\mathrm{ch}}(L_3) = 0.$$

Eine Operatorrealisierung allein liefert noch keine Ladung; ein formal geladener Testvektor liefert noch keine Operatorrealisierung der Klasse.

---

## 4. NEU-28 — Präziser negativer Abschlussbefund

Im auditierten Quellenkegel NEU-20/26/28/29 findet sich keine Konstruktion des konkreten Operators $L_3$.

| Frage | Befund |
|---|---|
| $L_3$ konstruiert | Nein |
| Repräsentant von $[L_3]$ konstruiert | Nein |
| Hilbertdiagonale für $L_3$ definiert | Nein |
| $C_L \neq 0$ bewiesen | Nein — aus NEU-20 importiert, Import nicht gerechtfertigt |
| Substitution $a = L_3$ typologisch belegt | Nein → `[O-170c-2h]` |

Der Satz $\lambda_{\mathrm{mod}}(s) = C_L/\zeta(s)$ ist daher nur konditional gültig: vorausgesetzt, ein konkreter spurzulässiger Repräsentant $L_3 \in A_{BC}^{an}$ oder einem geeigneten Operatorideal existiert.

---

## 5. NEU-161 — Korrekte Einordnung

NEU-161 enthält keinen neuen Fehler. Es dokumentiert den in NEU-42 §10 bereits vorhandenen Engpass sauber:

- $s \neq 0$ ist **Eingangsvoraussetzung** der Rechnung in NEU-42 §10, kein hergeleitetes Resultat.
- NEU-161 benennt dies explizit als aktiven Engpass und gibt den Befund `?[O]`.

$$[O\text{-}170c\text{-}2i\text{-audit}] \;\checkmark[M]: \quad \text{NEU-161 weist }s\neq0\text{ korrekt als Eingangsannahme aus.}$$
$$[O\text{-}170c\text{-}2i] \;?[O]: \quad P^{\mathrm{ch}}(L_3^\circ)\neq0\text{ bleibt unbewiesen.}$$

---

## 6. NEU-162 — Rechenzulässig, nicht herkunftszulässig

NEU-162 trifft die freie Wahl $L_3^\circ = e_1 V_1$ und zeigt:
- $(p-1)\log p \neq 0$ für alle $p \geq 2$ — `✓[M]`
- $e_1 V_1 \in \mathcal{A}_3^\circ$ — `✓[M]`

**Aber:** $\mathcal{A}_3^\circ \not\subseteq \sigma_{L_3}([L_3])$, und eine solche Beziehung wird nicht definiert. Die Wahl ist:

$$\text{rechenzulässig, aber nicht herkunftszulässig.}$$

Der freie Wahlquantor in NEU-42 §6/§10 ist kein Existenzquantor über die Koeffizienten des durch $[L_3]$ bestimmten Objekts.

---

## 7. Route A — fünf Schritte

$$\begin{aligned}
\mathrm{A0:}\quad& \mathrm{Rep}_{\mathrm{op}}([L_3]) \text{ typkorrekt definieren}\\
&\quad\bigl(L \in C^4(B_3,B_3)?\; B_3?\; A_{BC}^{an}?\; \mathrm{End}(\mathcal{H})?\bigr) \\[4pt]
\mathrm{A1:}\quad& \mathrm{Rep}_{\mathrm{op}}([L_3]) \neq \varnothing \\[4pt]
\mathrm{A2:}\quad& L \mapsto L|_{\mathrm{diag}} \text{ und } C_L(L) \text{ definieren} \\[4pt]
\mathrm{A3:}\quad& \exists\, L \in \mathrm{Rep}_{\mathrm{op}}([L_3]) : C_L(L) \neq 0 \\
&\quad\Rightarrow \text{ erst dann: } L^\circ := C_L(L)^{-1} L \\[4pt]
\mathrm{A4:}\quad& \exists\, L \in \mathrm{Rep}_{\mathrm{op}}([L_3]) : C_L(L) \neq 0 \;\wedge\; P^{\mathrm{ch}}(L) \neq 0
\end{aligned}$$

**Wichtig:** A3 und A4 sind logisch unabhängig und müssen für **denselben** Repräsentanten gelten. Getrennte Existenz eines normierten $L_1$ und eines geladenen $L_2$ genügt nicht.

---

## 8. Route B — quellennegativ, mathematisch offen

Route B (kohomologischer Weg via $[P^{\mathrm{ch}}]([L_3]) \neq 0$) ist im bestehenden Quellenkegel nicht eröffnet. Sie müsste neu aufgebaut werden, beginnend mit `[O-170c-2k-exist]`. Sie ist nicht als mathematische Möglichkeit ausgeschlossen.

---

## 9. Eingangshypothesen NEU-163

NEU-163 steht unter mindestens drei Eingangsannahmen:

| Hypothese | Inhalt | Status |
|---|---|---|
| `[H-163-1]` | $L_3^\circ = e_1 V_1$ | externe Modellwahl, nicht aus $[L_3]$ hergeleitet |
| `[H-163-2]` | $E_{1;\,1\to p}^{\mathrm{rel}} \neq 0$ | offen — NEU-163 reduziert darauf, beweist es nicht |
| `[H-163-3]` | $R_{p,j}(e_{1-p}V_p) = 0$ für die benötigten $j$ | gegebenenfalls offen |

NEU-163 reduziert das Einmoden-Nichtverschwindensproblem konditional auf $E_{1;\,1\to p}^{\mathrm{rel}} \neq 0$ und gegebenenfalls weitere Liftbedingungen. Es beweist $E_{1;\,1\to p}^{\mathrm{rel}} \neq 0$ nicht.

Alle Resultate ab NEU-162/163 sind korrekt als **konditionale Aussagen innerhalb des Testmodells** $[H\text{-}163\text{-}1]$ zu lesen, nicht als Fortschritt auf dem unbedingten Objekt-$X$-Pfad.

---

## 10. Nächste sinnvolle Knoten

**Upstream (Hauptpfad):**
- `[O-170b-2]` / `[O-170b-4]`: Definition von $\mathrm{Rep}_{\mathrm{op}}([L_3])$ — Route A, Schritt A0
- `[O-170c-2k-exist]`: Konstruktion von $P^{\mathrm{ch}}$ als Kettenprojektor — Route B

**Konditional (Testmodell $[H\text{-}163\text{-}1]$):**
- NEU-163: Nichtverschwindung und Separation von $E_{1;\,1\to p}^{\mathrm{rel}}$

---

*Erstellt im Rahmen der Auditsitzung vom 18. Juli 2026. Quellenbasiert aus direktem Lesen von NEU-28, NEU-161, NEU-162, NEU-170a, NEU-170b.*
