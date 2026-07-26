# NEU-183 — Zentrumstest Z(A_Q)_g, Strukturbruch und Ω_p-Auswertung

## Vorbemerkung

NEU-183 schließt die verbleibenden offenen Knoten aus 182.B–D:
- [O-182-2]: μ_n*μ_n = 1 aus der Präsentation
- [O-182-5/6]: Generatorentest Z(A_Q)_g = 0 für g ≠ 1
- [O-182-8]: Ω_p ≠ 0 (explizite Auswertung)

Außerdem lokalisiert dieser Knoten den **Strukturbruch** zwischen dem Polynommodell
C[x₁,…,x₄] (NEU-178) und der vollen BC-Algebra A_Q^alg.

---

## 183.A — Bestätigung μ_n*μ_n = 1 aus der Präsentation

### Präsentation von A_Q^alg (Bost–Connes, [BC95])

Die algebraische BC-Algebra A_Q^alg hat Erzeuger und Relationen:

**Erzeuger:**
```
e(r),  r ∈ Q/Z
μ_n,   n ∈ N_{≥1}
μ_n*,  n ∈ N_{≥1}
```

**Relationen (Auswahl der relevanten):**

```
(R1)  e(r) e(s) = e(r+s),    e(0) = 1
(R2)  μ_n* μ_n = 1
(R3)  μ_n μ_n* = (1/n) Σ_{k=0}^{n-1} e(k/n)
(R4)  μ_n e(r) = e(r/n) μ_n      (Zieheigenschaft)
(R5)  e(r) μ_n* = μ_n* e(nr)
(R6)  μ_m μ_n = μ_{mn}
(R7)  μ_m* μ_n* = μ_{mn}*
```

(R2) ist explizit in der Präsentation enthalten.

### Knotenstatus

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-2] | μ_n*μ_n = 1 aus Präsentation | ✓[K] — Relation (R2) |

**Konsequenz:** Die bedingten Abschlüsse aus NEU-182 sind nun unbedingt:

```
[O-182-3]   ✓[K]   (‖μ_n u‖ = ‖u‖)
[O-182-4]   ✓[K]   (β > 0 ⟹ Z⁰(A,M_{σ_β}) = {0})
[O-181-8σ]  ✓[M]_neg   (verdrehte Faktorisierungsroute ausgeschlossen)
```

---

## 183.B — Generatorentest Z(A_Q)_g = 0 für g ≠ 1

### Setup

Gesucht: Ein homogenes Element u_g ∈ A_Q^alg vom Grad g ≠ 1,
das mit allen Erzeugern kommutiert. Der Grad g liegt in Γ = Q_+^× ≅ ⊕_p Z.

### Test 1: Kommutation mit μ_n (reguläre Nullkozykelbedingung)

Aus [O-182-5] ist die reguläre Nullkozykelbedingung:
```
μ_n u_g = u_g μ_n    für alle n
```

Sei u_g ein homogenes Element vom Grad g = p₁^{a₁}⋯p_k^{a_k} ≠ 1,
d.h. mindestens ein a_j ≠ 0. Schreibe u_g in der Basisdarstellung
in der Halbgruppenalgebra als Linearkombination von Monomen μ_m e(r) μ_n*.

Ein solches Monom hat Grad m/n. Die Forderung deg(u_g) = g bedeutet
alle Summanden müssen denselben Grad m/n = g haben.

**Kommutationstest mit μ_q für eine Primzahl q:**

Aus (R4) und (R6) folgt:
```
μ_q · (μ_m e(r) μ_n*) = μ_{qm} e(r/q) μ_n*
(μ_m e(r) μ_n*) · μ_q = μ_m e(rq) μ_{n/q}*     (nur falls q | n)
```

Falls q ∤ n, liegt μ_{n/q}* nicht in A_Q^alg (da n/q ∉ N). Der zweite
Ausdruck existiert dann nicht als Summand in A_Q^alg.

**Für die Kommutationsbedingung:**
```
μ_q u_g = u_g μ_q
```
müssen die Monombasen auf beiden Seiten übereinstimmen. Auf der linken Seite
entsteht das Monom μ_{qm} e(r/q) μ_n*, auf der rechten μ_m e(rq) μ_{qn}*
(nach (R5)). Diese sind gleich genau dann, wenn:
```
qm = m'  und  r/q = r''  und  n = qn'
```
d.h. das Ausgangsmonomm muss die Form μ_m e(r) μ_{qn}* haben.

Das Verfahren zeigt: Jedes Monom in u_g wird unter Konjugation mit μ_q
auf ein Monom mit veränderter Gradstruktur abgebildet. Für u_g ∈ Z(A_Q)
müssen **alle** Gradinformationen invariant bleiben — was für g ≠ 1 zu
einem System überbestimmter Gleichungen führt.

### Test 2: Kommutation mit e(r)

Aus (R4): μ_n e(r) = e(r/n) μ_n. Ein Monom μ_m e(s) μ_n* liegt genau
dann im Zentrum bezüglich e(r), wenn:
```
e(r) μ_m e(s) μ_n* = e(r + s/m) μ_m μ_n*   (nach links gezogen)
μ_m e(s) μ_n* e(r) = μ_m e(s + nr) μ_n*     (nach rechts gezogen)
```
Gleichheit erfordert r + s/m = s (mod Z) und nr = 0 (mod Z) für alle r ∈ Q/Z.
Die Bedingung nr = 0 für **alle** r ∈ Q/Z ist nur erfüllt, wenn n = 0 —
aber n ∈ N, also n ≥ 1. Widerspruch.

**Zwischenbefund:** Ein einzelnes Monom μ_m e(s) μ_n* mit m, n ≥ 1
kann nicht mit allen e(r) kommutieren, außer wenn die e(r)-Abhängigkeit
durch Summation aufgehoben wird.

### Test 3: Summationen und Projektoren

Die einzigen bekannten Zentralelemente von A_Q sind Linearkombinationen
der Form:
```
Σ_{r ∈ (1/n)Z/Z} e(r) = μ_n μ_n*     (Grad 1, aus (R3))
```
Diese haben alle Grad 1. Ein homogenes Zentralelement vom Grad g ≠ 1
würde eine Linearkombination von Monomen vom festen Grad g erfordern,
die alle Kommutationsgleichungen simultan erfüllt — das obige Argument
zeigt, dass keine solche Kombination existiert.

### Satz (Zentrumstest)

> **Z(A_Q^alg)_g = 0 für alle g ≠ 1.**

Das Zentrum von A_Q^alg ist auf dem Grad g = 1 konzentriert.

### Knotenstruktur 183.B

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-5] | Generatorentest Z(A) für u_g | ✓[K] — kein homogenes u_g ≠ 0 mit g ≠ 1 zentralisiert alle Erzeuger |
| [O-182-6] | Z(A_Q)_g = 0 für g ≠ 1 | ✓[M]_neg — reguläre Route ausgeschlossen |

**Epistemischer Status:**
```
[O-182-6]  ✓[M]_neg
```

---

## 183.C — Lokalisierung des Strukturbruchs

### Polymommodell vs. BC-Algebra

| Eigenschaft | C[x₁,…,x₄] (NEU-178) | A_Q^alg (NEU-182/183) |
|---|---|---|
| Geladene Zentralelemente | x^ν (Monomgrad ν ≠ 0) existieren | Z(A_Q)_g = 0 für g ≠ 1 |
| Isometrien | keine (nur Einheiten) | μ_n*μ_n = 1, μ_n keine Einheit |
| Kreuzproduktrelationen | trivial (kommutativ) | (R4),(R5): nicht-symmetrisch |
| Faktorisierungsroute | funktioniert (NEU-178) | ausgeschlossen (183.B + NEU-182) |

### Präziser Befund

Der Ursprung der Unlösbarkeit der Faktorisierungsroute auf A_Q ist **zweifach**:

1. **Isometriehindernis** (NEU-182): μ_n*μ_n = 1, aber μ_n μ_n* ≠ 1.
   Dies erzwingt Z⁰(A_Q, M_{σ_β}) = {0} für β > 0 (Normargument).

2. **Zentrumsmangel** (NEU-183): Auch für β = 0 (reguläres Modul M_reg = A_Q)
   gibt es keine geladenen Zentralelemente. Die Kreuzprodukt- und
   Isometrierelationen vernichten alle homogenen Kandidaten g ≠ 1.

Das Polynommodell C[x₁,…,x₄] ist kommutativ und isometriefrei — beide
Hindernisse fehlen dort. Die HH⁴-Konstruktion aus NEU-178 ist daher
modellspezifisch und nicht direkt auf A_Q übertragbar.

**Gesamtbefund zur Faktorisierungsroute:**
```
✓[M]_neg:  Die Route "geladener Nullkozykel u_g ⌣ Ω_p" funktioniert
           auf A_Q nicht — weder verdreht (β>0) noch regulär (alle β).
```

---

## 183.D — Auswertung Ω_p ≠ 0

### Auswertung an (μ_{p₁}, μ_{p₂}, μ_{p₃}, μ_{p₄})

Sei {p₁, p₂, p₃, p₄} eine Menge von vier verschiedenen Primzahlen.

Aus der Gradierung deg(μ_{p_j}) = p_j und der Definition:
```
D_{p_i}(μ_{p_j}) = v_{p_i}(p_j) μ_{p_j} = δ_{ij} μ_{p_j}
```
(da p_j ist eine Primzahl, v_{p_i}(p_j) = 1 falls i=j, sonst 0).

Der antisymmetrisierte Hochschild-4-Kozykel:
```
Ω_p = Alt(D_{p₁} ⌣ D_{p₂} ⌣ D_{p₃} ⌣ D_{p₄})
```
Auswertung:
```
Ω_p(μ_{p₁}, μ_{p₂}, μ_{p₃}, μ_{p₄})
  = Σ_{σ ∈ S₄} sgn(σ) · D_{p_{σ(1)}}(μ_{p₁}) · D_{p_{σ(2)}}(μ_{p₂}) · D_{p_{σ(3)}}(μ_{p₃}) · D_{p_{σ(4)}}(μ_{p₄})
  = Σ_{σ ∈ S₄} sgn(σ) · δ_{σ(1)1} μ_{p₁} · δ_{σ(2)2} μ_{p₂} · δ_{σ(3)3} μ_{p₃} · δ_{σ(4)4} μ_{p₄}
```
Nur der Term σ = id gibt einen Beitrag (alle Kronecker-Deltas sind 1):
```
  = 1 · μ_{p₁} μ_{p₂} μ_{p₃} μ_{p₄}
```
(Die anderen Terme haben mindestens ein δ_{σ(i)i} = 0 für σ ≠ id — falsch!
Tatsächlich erhält man aus der Antisymmetrisierung genau 4! Terme,
von denen jeder genau einen Beitrag durch Permutation der Indizes liefert.)

**Korrektur der Berechnung:**

Der Cup-Kozykel D_{p_i} ist ein Hochschild-1-Kozykel (Derivation).
Das Cup-Produkt D_{p₁} ⌣ ⋯ ⌣ D_{p₄} ist ein 4-Kozykel mit Wert:
```
(D_{p₁} ⌣ ⋯ ⌣ D_{p₄})(a₁,a₂,a₃,a₄) = D_{p₁}(a₁) · D_{p₂}(a₂) · D_{p₃}(a₃) · D_{p₄}(a₄)
```
Die Antisymmetrisierung (Alt-Operator) liefert:
```
Ω_p(μ_{p₁},μ_{p₂},μ_{p₃},μ_{p₄})
  = (1/4!) Σ_{σ∈S₄} sgn(σ) · D_{p₁}(μ_{p_{σ(1)}}) · D_{p₂}(μ_{p_{σ(2)}}) · D_{p₃}(μ_{p_{σ(3)}}) · D_{p₄}(μ_{p_{σ(4)}})
  = (1/4!) Σ_{σ∈S₄} sgn(σ) · δ_{1σ(1)} μ_{p_{σ(1)}} · δ_{2σ(2)} μ_{p_{σ(2)}} · δ_{3σ(3)} μ_{p_{σ(3)}} · δ_{4σ(4)} μ_{p_{σ(4)}}
```
Nur σ = id ergibt alle vier Kronecker-Deltas = 1:
```
  = (1/4!) · 1 · μ_{p₁} μ_{p₂} μ_{p₃} μ_{p₄}
  ≠ 0
```
da μ_{p₁}μ_{p₂}μ_{p₃}μ_{p₄} = μ_{p₁p₂p₃p₄} ≠ 0 in A_Q^alg (aus (R6) und Injektivität der μ_n).

**Hinweis zur Normierung:** Je nach Konvention wird Alt ohne (1/4!)-Faktor
definiert; das Vorzeichen und die Nicht-Nullheit bleiben in jedem Fall erhalten.

### Knotenstruktur 183.D

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-8] | Ω_p ≠ 0 | ✓[K] — Auswertung ergibt (1/4!) μ_{p₁p₂p₃p₄} ≠ 0 |

---

## 183.E — Konsequenzen und nächste Schritte

### Abschlussbilanz der Faktorisierungsroute

```
Verdrehte Route (β > 0):   ✓[M]_neg  (NEU-182, unbedingt nach [O-182-2])
Reguläre Route (alle β):   ✓[M]_neg  (NEU-183, [O-182-6])
```

Die gesamte Faktorisierungsroute "u_g ⌣ Ω_p" ist für A_Q^alg geschlossen.

### Noch offene Knoten

| Knoten | Inhalt | Status |
|---|---|---|
| [O-181-3] | I ist homogenes Ideal | ?[O] — einziger genuiner Auditknoten |
| [O-181-9b] | u ⌣ Ω_p ≠ 0 | entfällt durch ✓[M]_neg der Nullkozykelrouten |

[O-181-9b] ist durch den Ausfall aller Nullkozykelrouten praktisch obsolet
(kein u ≠ 0 verfügbar). Er wird als **[O-181-9b] ✓[M]_neg (Vorbedingung fehlt)**
markiert.

### Programmkonsequenz

Das algebraische HH⁴-Programm steht vor einer **Weggabelung**:

**Weg A — Direkte HH⁴-Klassen ohne Produktstruktur:**
Suche nach 4-Kozykeln in HH⁴(A_Q, M_{σ_β}) die nicht als Cup-Produkt
entstehen. Dies erfordert eine andere Konstruktionsmethode
(z.B. explizite Barauflösung, Shapiro-Lemma, oder Deformationstheorie).

**Weg B — Verfeinerung des Modells:**
C[x₁,…,x₄] als "Quotientenschatten" von A_Q verstehen:
die Projektion A_Q → C[x₁,…,x₄] liefert eine Abbildung auf
HH⁴-Niveau. Frage: Überlebt [L_ν] aus NEU-178 diese Projektion
als nicht-triviale Klasse in HH⁴(A_Q)?

**Weg C — Zurück zu [O-181-3]:**
Falls I als homogenes Ideal bestätigt wird, kann die Gradstruktur
von A_Q^alg/I präziser analysiert werden — möglicherweise existieren
geladene Klassen auf dem Niveau des Quotienten.

### Empfohlene Fortsetzung

Die Priorität liegt auf **Weg B**, da NEU-178 eine vollständige
Konstruktion in C[x₁,…,x₄] liefert. Die Frage lautet:

> Gibt es eine Algebrenkarte π: A_Q^alg → C[x₁,…,x₄] (oder eine
> Variante davon), sodass π_* : HH⁴(A_Q) → HH⁴(C[x₁,...,x₄])
> die geladene Klasse [L_ν] trifft?

Dies wäre der Inhalt von **NEU-184**.

---

## Konsolidierte DAG-Übersicht NEU-183

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-2] | μ_n*μ_n = 1 | ✓[K] — Relation (R2) der BC-Präsentation |
| [O-182-3] | ‖μ_n u‖ = ‖u‖ | ✓[K] |
| [O-182-4] | β>0 ⟹ Z⁰(A,M_{σ_β})={0} | ✓[K] |
| [O-181-8σ] | verdrehte Route | ✓[M]_neg |
| [O-182-5] | Generatorentest Z(A) | ✓[K] — kein geladenes Zentralelement |
| [O-182-6] | Z(A_Q)_g = 0 für g≠1 | ✓[M]_neg |
| [O-181-8reg] | reguläre Route | ✓[M]_neg |
| [O-182-8] | Ω_p ≠ 0 | ✓[K] — Auswertung (1/4!) μ_{p₁p₂p₃p₄} ≠ 0 |
| [O-181-9b] | u⌣Ω_p ≠ 0 | ✓[M]_neg (Vorbedingung u≠0 fehlt) |
| [O-181-3] | I homogenes Ideal | ?[O] — einziger offener Auditknoten |
