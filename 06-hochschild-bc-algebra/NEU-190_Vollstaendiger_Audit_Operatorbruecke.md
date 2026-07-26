# NEU-190 — Vollständiger Quellenbefund zur Operatorrealisierung von Hochschild-Vierkozykeln

**Datum:** 19. Juli 2026  
**Anschluss:** NEU-189  
**Status:** ✓[K] (Auditarchitektur), ✓[M]_neg,Quelle ([O-190-1] abgeschlossen)

---

## 190.A — DAG-Stand

NEU-189 hat die Typfrage korrekt isoliert:

```
Hom_C(A^⊗4, A)
```

Gesucht war im Katalog NEU-1–188 eine bereits konstruierte Abbildung

```
ρ_op : Z⁴(A,A) ⟶ O(H)
```

oder

```
ρ_op : HH⁴(A,A) ⟶ O(H),
```

bzw. eine konkret komponierbare Kette mit diesem Ausgangstyp.

NEU-190 als Auditarchitektur: **✓[K]**.

---

## 190.B — Kandidat 1: Frühe L₃-Quellen NEU-15–20, NEU-28

**Auditzeile:**

| Feld | Befund |
|---|---|
| Quelle | NEU-15–17, NEU-20, NEU-28 |
| Eingangstyp | Abstrakte Bezeichnung [L₃] bzw. formal eingesetztes L₃ |
| Zusatzdaten | Filtration, Symbol-Lift, Spur und KMS-Gewicht nur teilweise bezeichnet |
| Ausgangstyp | Formal ein Algebraelement oder Insertionsoperator in Spurformeln |
| Korandverhalten | Nicht definiert |

NEU-20 konstruiert keinen Operator L₃, sondern weist lediglich einen Koeffizienten in einer vorgelagerten Rechnung als nichtverschwindend aus. NEU-28 beweist eine Spurformel für ein Algebraelement a, setzt anschließend aber formal a = L₃, ohne L₃ ∈ A oder L₃ ∈ B(H) zu begründen.

Ein Hochschildkomplex, ein Koeffizientenbimodul, eine Repräsentantenabbildung und eine Operatorrealisierung treten nicht gemeinsam in einem typisierten Diagramm auf.

**Befund:** Kein Kandidat für Z⁴(A,A) → O(H) und kein Teiltreffer. Es fehlen mehrere voneinander unabhängige Typbrücken.

---

## 190.C — Kandidat 2: Operatorwertiger Zweikozykel aus Dirac-Struktur

**Auditzeile:**

| Feld | Befund |
|---|---|
| Quelle | Früher Dirac-/Spektralstrang |
| Eingangstyp | (a,b) ∈ A^⊗2 |
| Zusatzdaten | Darstellung von A und ein Operator D |
| Ausgangstyp | Operatorwertiger Hochschild-Zweicochain ω_D(a,b) = [D,a][D,b] ∈ B(H) |
| Korandverhalten | Nur für diesen speziellen Zweicochain diskutiert |

Dies ist eine konkrete operatorwertige Grad-2-Konstruktion. Sie liefert jedoch keine Abbildung Z⁴(A,A) → O(H). Es fehlen: eine Vorschrift, die einen beliebigen A-wertigen Vierkozykel Ω in diese Dirac-Konstruktion einsetzt; eine Kontraktion der vier Eingabestellen zu einem Einzeloperator; ein Vergleich mit Ω_p; ein Nachweis der Korandinvarianz.

**Befund:** Kein Teiltreffer.

---

## 190.D — Kandidat 3: ω̃₂-Kopplung und Jacobi-Operatoren NEU-34–35

**Auditzeile:**

| Feld | Befund |
|---|---|
| Quelle | NEU-34–35 |
| Eingangstyp | Der fest vorgegebene Zweicochain ω̃₂ und ein gewählter Modus |
| Zusatzdaten | Trunkierung, Basis, Wres-Form und Adjungierung |
| Ausgangstyp | Gewichteter Shift bzw. Jacobi-Operator |
| Korandverhalten | Nicht als Abbildung auf Hochschildklassen behandelt |

Dom(ρ) ≠ Z⁴(A,A). Die vorhandene Grad-2-Slotfixierung ist ein methodischer Präzedenzfall, aber keine nahezu vollständige Grad-4-Operatorbrücke.

**Befund:** Kein Teiltreffer.

---

## 190.E — Kandidat 4: C_p-Konstruktionen NEU-41 und NEU-44

**Auditzeile:**

| Feld | Befund |
|---|---|
| Quelle | NEU-41/44 |
| Eingangstyp | Primvektor ε_p, geladene Hebung ε̂_p und konkretes L₃° |
| Zusatzdaten | ω̃₂, Π_J, Wres bzw. relativer Graphraum |
| Ausgangstyp | Rang-eins-Kopplungsoperator C_p oder C_p^rel |
| Korandverhalten | Nicht definiert |

Entscheidend: L₃° ist Eingangsdatum von C_p, nicht Ergebnis einer Abbildung Ω ↦ C_p(Ω). Weder NEU-41 noch NEU-44 definieren Z⁴(A,A) → Hom(p_N, H_rel,N). Eine Ersetzung L₃° ↝ Ω_p ist typwidrig.

**Befund:** Kein Volltreffer und kein Teiltreffer.

---

## 190.F — Kandidat 5: Feshbach-, Spur- und Operatorrekonstruktion NEU-30–152

**Auditzeile:**

| Feld | Befund |
|---|---|
| Quelle | NEU-30–152 |
| Eingangstyp | Skalare Kernel, Jacobi-Matrizen, Kopplungsoperatoren, Zustände oder Spurgewichte |
| Zusatzdaten | Hilberträume, Resolventen, Feshbach-Blöcke, Funktionalkalkül |
| Ausgangstyp | Spektral-, Jacobi-, Feshbach- oder Rang-eins-Operatoren |
| Korandverhalten | Nicht anwendbar bzw. nicht definiert |

**Befund:** Kein Kandidat mit Eingangstyp Z⁴(A,A) oder HH⁴(A,A).

---

## 190.G — Kandidat 6: GNS/KMS NEU-122

**Auditzeile:**

| Feld | Befund |
|---|---|
| Quelle | NEU-122 |
| Eingangstyp | Algebra und positives Funktional bzw. Zustand (τ_β,N, A_N^-, Ω_N^KMS) |
| Zusatzdaten | Dirichlet-Cutoff, R_N ~ 1/log N, GNS/Krylov/Lanczos |
| Ausgangstyp | Jacobi-Operator A_N^Jac,- via Lanczos |
| Korandverhalten | Kein Bezug zum Hochschild-Kodifferential; die gesamte Kozykel-zu-Operator-Abbildung fehlt, nicht nur die Korandinvarianz |

**Befund:** Kein Teiltreffer. Ein Hilbertraum und eine GNS-Darstellung allein sind keine Hochschild-Operatorrealisierung.

---

## 190.H — Kandidat 7: Lift-, Quotienten- und Kopplungsblätter NEU-153–166

**Auditzeile:**

| Feld | Befund |
|---|---|
| Quelle | NEU-153–166 |
| Eingangstyp | Primvektoren, Liftvektoren und Liftänderungen |
| Zusatzdaten | π_prim, Wres-Normierung und vorhandene Kopplungsabbildungen |
| Ausgangstyp | Vektoren, Quotientenklassen oder Rang-eins-Kopplungen |
| Korandverhalten | Kein Hochschild-Korandtest |

NEU-157 stellt ausdrücklich fest, dass mehrere R_p,j nicht konstruiert waren. NEU-155 prüft die Konsistenz zwischen NEU-41 und NEU-44, konstruiert aber keinen Operator T_Ω aus einem Kozykel. NEU-161/162 besitzen keinen Eingang vom Typ Z⁴(A,A). NEU-165b hat festgestellt, dass die betreffenden Operatorfamilien im ursprünglichen Quellenkegel nicht vollständig konstruiert sind.

**Befund:** Kein Eingang vom Typ Z⁴(A,A) oder HH⁴(A,A). Alle Blätter liegen vollständig downstream der fehlenden Realisierung von L₃.

---

## 190.I — Kandidat 8: Quellen- und Typaudits NEU-167–173

**Auditzeile:**

| Feld | Befund |
|---|---|
| Quelle | NEU-167–173 |
| Eingangstyp | Frühere L₃-Behauptungen und ihre Quelltexte |
| Zusatzdaten | Typ- und Herkunftsaudits |
| Ausgangstyp | Negativer Quellenbefund |
| Korandverhalten | Als fehlend diagnostiziert |

**Befund:** Diese Blätter enthalten bewusst keine Operatorrealisierung; sie dokumentieren deren Fehlen.

---

## 190.J — Kandidat 9: Neuer Hochschildkomplex NEU-174–185

### Direktlesebefund NEU-174

NEU-174 definiert den Hochschild-Kochainkomplex

```
(C•(B₃^mod, M), b)
```

(wobei **B₃^mod := A_Q**, die BC-Algebra über Q) und die mit dem Differential verträgliche BC-Zeitwirkung α_t^C. Das Dokument hält ausdrücklich fest, dass weder L₃ noch ρ_op in NEU-174 eingeführt werden — dies ist Gegenstand von NEU-175.

**Auditzeile:**

| Feld | Befund |
|---|---|
| Quelle | NEU-174 |
| Eingangstyp | Algebra B₃^mod := A_Q, Bimodul M |
| Zusatzdaten | BC-Zeitwirkung α_t, Kompatibilitätsbedingungen, b α_t^C = α_t^C b (✓[K]) |
| Ausgangstyp | Kochainkomplex (C•(B₃,M), b) und Fourierzerlegung ([O-174-6] ?[O] unter Kompaktheitsbedingung) |
| Korandverhalten | Kein Bezug zu O(H); reine Algebra-/Kohomologiekonstruktion |

### Direktlesebefund NEU-175

NEU-175 konstruiert auf C_fin• den geladenen Kettenprojektor

```
P^ch = Σ_{λ≠0} P_λ
```

mit b P^ch = P^ch b (✓[K]) und induzierter Abbildung [P^ch]: H•(C_fin) → H•(C_fin) (✓[K]). P^ch ist ein algebraischer Endomorphismus des Kochainkomplexes, **kein Element von B(H)**. NEU-175 benennt ρ_op ausdrücklich als "Gegenstand eines eigenen Folgeknotens" (NEU-176).

**Auditzeile:**

| Feld | Befund |
|---|---|
| Quelle | NEU-175 |
| Eingangstyp | C_fin• (Gewichtraumkomplex) |
| Zusatzdaten | Eigenkochains zu α_t^C, Eindeutigkeit der Zerlegung (✓[K]), b P^ch = P^ch b |
| Ausgangstyp | [P^ch]: H•(C_fin) → H•(C_fin) — kohomologischer Endomorphismus, kein Hilbertraumoperator |
| Korandverhalten | Korandkompatibilität von P^ch algebraisch gesichert; kein Bezug zu O(H) |

### Direktlesebefund NEU-176

NEU-176 formuliert einen Kandidaten L_{3,λ} ∈ C⁴_{fin,λ}. Die entscheidenden Knoten sind:

- **[O-176-2]** b L_{3,λ} = 0: **?[O]** — Kozykeleigenschaft noch unbewiesen
- **[O-176-3]** L_{3,λ} ∉ b C³_{fin,λ}: **?[O]** — zentraler unbewiesener Knoten
- **[O-176-4]** [L_{3,λ}] ≠ 0 in H⁴(C_{fin,λ}): **?[O]**

NEU-176 verschiebt ρ_op ausdrücklich auf NEU-177 (noch nicht vorhanden).

**Auditzeile:**

| Feld | Befund |
|---|---|
| Quelle | NEU-176 |
| Eingangstyp | Kandidat L_{3,λ} ∈ C⁴_{fin,λ} (Existenz unter Modellannahme [O-176-1a] ?[O]) |
| Zusatzdaten | Gewichtsadditivität, Kozykelbedingung offen |
| Ausgangstyp | Angestrebt: nichttriviale Klasse [L_{3,λ}] ≠ 0 in H⁴(C_{fin,λ}) — noch nicht konstruiert |
| Korandverhalten | [O-176-3] (Nichtrandbedingung) ist der zentrale unbewiesene Knoten; ρ_op auf NEU-177 verschoben |

### Kandidat NEU-183–185 (skalare Paarung)

NEU-183–185 liefern Ω_p ∈ Z⁴(A,A), b Ω_p = 0, einen Dualzyklus z_p^ε ∈ C_4(A,A^∨) und die skalare Paarung mit Wert 24. Dies beweist [Ω_p] ≠ 0 in HH⁴(A,A) (neutrale Klasse). Der stärkste kandidatennahe Befund des Audits:

```
Z⁴(A,A) × Z_4(A,A^∨) ⟶ C.
```

Er erzeugt einen Skalar, keinen Operator. Eine operatorwertige Vierzyklus-Paarung Z⁴(A,A) × Z_4^op → O(H) wird nicht definiert.

**Befund:** Nichttriviale Vierklasse: ✓[M]. Operatorrealisierung: nicht vorhanden.

---

## 190.K — Kandidat 10: NEU-186–188

**Auditzeile:**

| Feld | Befund |
|---|---|
| Quelle | NEU-186–188 |
| Eingangstyp | Derivationen bzw. Gruppenkozykel |
| Zusatzdaten | Gradierung und Restriktion auf die Gruppenalgebra |
| Ausgangstyp | Mögliche Klassen in HH¹ |
| Korandverhalten | Im Grad 1 behandelt |

Selbst ein positiver Abschluss würde zunächst nur HH¹(A,A)_g ≠ 0 liefern. Eine Vierklasse erforderte weitere Cup-Produkte. Eine Operatorrealisierung wäre danach weiterhin offen.

**Befund:** Kein Kandidat für NEU-190.

---

## 190.L — Ausschluss eines Teiltreffers

Die quellenmäßig nächsten Strukturen sind:
- die Slotfixierung eines konkreten Zweikochains in NEU-34;
- die Konstruktion von C_p aus einem bereits konkreten L₃° in NEU-41;
- die GNS-Darstellung von Algebraelementen;
- die skalare Paarung von Ω_p mit einem Dualzyklus.

Für jeden Kandidaten fehlen mindestens **zwei logisch unabhängige Komponenten**:

```
Kontraktion der vier Slots
```

und

```
Operatorwirkung auf einem festgelegten Hilbertraum,
```

beziehungsweise zusätzlich

```
Korandinvarianz.
```

Der Status ✓[M]_part ist daher nicht gerechtfertigt.

**Wichtige methodische Präzisierung:** Bei den meisten geprüften Quellen fehlt nicht lediglich die Korandinvarianz. Es fehlt bereits eine Vorschrift, die einen Hochschild-Vierkozykel als Eingang annimmt. Insbesondere sind nach dem gesicherten Inhaltsstand als Nichttreffer einzuordnen: **NEU-122, NEU-153, NEU-155, NEU-161, NEU-162, NEU-165 und NEU-166**.

---

## 190.M — Endentscheidung

Im geprüften Katalog NEU-1–188 wurde kein typisierter Mechanismus gefunden, der eine Abbildung

```
Z⁴(A,A) ⟶ O(H)
```

oder

```
HH⁴(A,A) ⟶ O(H)
```

definiert.

Insbesondere existiert keine katalogintern definierte Vorschrift

```
Ω_p ↦ ρ_op(Ω_p),
```

und erst recht keine repräsentantenunabhängige Vorschrift

```
[Ω_p] ↦ ρ_op([Ω_p]).
```

**Endstatus:**

```
[O-190-1]   ✓[M]_neg,Quelle
```

**Globale Formulierung:**

> Im gesamten geprüften RH-Katalog NEU-1–188 (einschließlich der direkt gelesenen NEU-174–176) ist kein Mechanismus Z⁴(A,A) oder HH⁴(A,A) → O(H) konstruiert.

Dies ist ein **positiv abgeschlossener Audit mit negativem Quellenbefund**. Es ist **kein mathematischer Unmöglichkeitssatz**.

**Redaktionelle Fixierung:** Ab NEU-190 gilt durchgehend **B₃^mod := A_Q** (BC-Algebra über Q, rationaler Kern, wie in NEU-174 definiert). Beim ersten Auftreten von Z⁴(A,A) in Folgedokumenten ist A = B₃^mod = A_Q explizit auszuweisen.

---

## 190.N — Konsequenz für NEU-189

```
[O-189-2]   ?[O] gesperrt
```
— da keine Abbildung ρ_op vorliegt, deren Korandinvarianz geprüft werden könnte.

```
[O-189-3]   ?[O] gesperrt
```
— da der Ausdruck ρ_op([Ω_p]) noch nicht definiert ist.

```
[O-189-4]   ?[O] gesperrt
```
— da keine Operatorgröße existiert, deren Kompatibilität mit L₃°, C_p, ω̃₂, W_res,BC^top geprüft werden könnte.

**NEU-191 wird durch diesen Auditbefund nicht eröffnet.**

---

## DAG-Knotenübersicht

| Knoten | Inhalt | Status |
|---|---|---|
| NEU-190 als Auditarchitektur | Suchrahmen NEU-1–188 | ✓[K] |
| [O-190-1] | Quellenbefund: Z⁴(A,A) → O(H) im Katalog? | ✓[M]_neg,Quelle |
| [O-189-2] | Korandinvarianz von ρ_op | ?[O] gesperrt |
| [O-189-3] | Nichtverschwindung ρ_op([Ω_p]) | ?[O] gesperrt |
| [O-189-4] | Kompatibilität mit L₃°, C_p, W_res,BC^top | ?[O] gesperrt |

---

*Katalog: rh-fragenkatalog | Einheit: NEU-190 | Revision: 2026-07-19*
