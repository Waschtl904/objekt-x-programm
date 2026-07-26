# NEU-201 — Singuläres Potential H im Kommutatorquotienten: Sichtbarkeitstest

**Status:** ?[O]  
**Erstellt:** 2026-07-19  
**Vorgänger:** NEU-200 (reguläre H unsichtbar), NEU-199 ([O-199-3]_copr), NEU-197 (universelles Detektionskriterium)  
**Obstruktionspfeil:** [O-199-3]_sing  

---

## Frage (atomar)

Kann ein **singuläres** Element $H \in B$ den Kommutatorquotienten
$$Q_{h,p} := \frac{[D_g^H,\, e(\mu_k)]}{[D_g^H,\, e(\mu_k)]_{\mathrm{reg}}}$$
**sichtbar** machen, d.h. gibt es ein singuläres $H$ mit
$$[H,\, B]_{\mathrm{mod\,Komm}} \not\equiv 0 \quad \text{in } B/[B,B]\,?$$

---

## Kontext und Motivation

### 201.1 — Ergebnis aus NEU-200 (Ausgangspunkt)

NEU-200 hat gezeigt (200.1–200.8): Für **reguläres** $H \in B_{\mathrm{reg}}$
gilt
$$[H,\, b]_{\mathrm{mod\,Komm}} = 0 \quad \forall\, b \in B,$$
d.h. reguläre Potentiale sind im Kommutatorquotienten $B/[B,B]$
vollständig unsichtbar. Dies entspricht dem Status $[O\text{-}199\text{-}3]_{\mathrm{reg}}\;\checkmark[M]_{\mathrm{neg}}$.

### 201.2 — Singulärstruktur der BC-Algebra

Die Bost-Connes-Algebra $B = C^*(\mathbb{Q}/\mathbb{Z}) \rtimes \mathbb{N}$ besitzt
eine natürliche Filtrierung nach der Singularitätsordnung. Ein Element
$H \in B$ heißt **singulär** (vom Typ $\mathrm{sing}$), falls
$$H = \sum_{n \in \mathbb{N}} a_n \cdot \mu_n + \sum_{m \in \mathbb{N}} b_m \cdot \mu_m^*$$
mit einer Koeffizientenfolge $(a_n), (b_n)$, die **nicht** in
$\ell^1(\mathbb{N})$ liegt, oder falls $H$ einen nicht-kontrollierbaren
Träger in den Isometrien $\mu_n$ besitzt (vgl. NEU-183, NEU-187).

### 201.3 — Geladene Derivation $D_g^H$ (Import aus NEU-199)

Aus NEU-199 (Formel 199.10–199.12) gilt die Generatorformel:
$$D_g^H(\mu_k) = g(k)\cdot [H,\, \mu_k]_B$$
wobei $g: \mathbb{N} \to \mathbb{C}$ ein Gewichtscharakter mit
$g(k) \neq 0$ für alle $k \in \mathbb{N}$ ist.  
Der Quotiententest $G_i^H$ (NEU-199, 199.18–199.21) prüft:
$$G_i^H := \mathrm{ev}_{\mu_i}\!\left([D_g^H,\, e(\mu_k)]\right) \in B/[B,B].$$

---

## Teilfragen (Zerlegung des Knotens)

### 201.A — Existenz eines singulären Zeugen $H_{\mathrm{sing}}$

**Frage:** Existiert ein singuläres $H_{\mathrm{sing}} \in B \setminus B_{\mathrm{reg}}$, sodass
$$[H_{\mathrm{sing}},\, \mu_k] \not\in [B,B] \quad \text{für mindestens ein } k \in \mathbb{N}\,?$$

**Kandidat:** Setze
$$H_{\mathrm{sing}} := \sum_{p \text{ prim}} \frac{1}{\log p}\, \mu_p \cdot e(1/p).$$
Diese Reihe konvergiert schwach in $B$, liegt aber nicht in
$B_{\mathrm{reg}}$, da $\sum_p \frac{1}{\log p}$ divergiert.

**Prüfschema (201.A.1):**
$$[H_{\mathrm{sing}},\, \mu_k] = \sum_{p \text{ prim}} \frac{1}{\log p}\,
\bigl[\mu_p \cdot e(1/p),\, \mu_k\bigr]_B.$$
Für $\gcd(p,k) = 1$ gilt $[\mu_p \cdot e(1/p),\, \mu_k]_B \neq 0$
generisch (teilerfremder Sektor, vgl. NEU-199 [O-199-1/2] $\checkmark[M]_{\mathrm{part}}$).

**Status 201.A:** ?[O] — Konvergenz in $B/[B,B]$ zu klären.

---

### 201.B — Quotiententest $G_i^{H_{\mathrm{sing}}}$

**Frage:** Ist der Quotiententest
$$G_i^{H_{\mathrm{sing}}} = \mathrm{ev}_{\mu_i}\!\left([D_g^{H_{\mathrm{sing}}},\, e(\mu_k)]\right)$$
für geeignetes $i, k$ von Null verschieden in $B/[B,B]$?

**Ansatz (201.B.1):** Wende das universelle Detektionskriterium aus NEU-197
(Satz 197.1) an. Dieses besagt: Ein Element $X \in B$ ist in
$B/[B,B]$ nichttrivial genau dann, wenn ein KMS$_\beta$-Funktional
$\phi_\beta$ mit $\phi_\beta(X) \neq 0$ existiert.

**Kritische Beobachtung (201.B.2):** Für das KMS$_1$-Funktional
$\phi_1$ der BC-Algebra gilt (Connes-Marcolli):
$$\phi_1\!\left(\mu_n \cdot e(r) \cdot \mu_m^*\right) = \delta_{n,m}\cdot \zeta(1)^{-1}\sum_{k=1}^n e^{2\pi i r k/n}.$$
Da $\zeta(1)$ divergiert (regulierter Grenzwert nötig), könnte
$\phi_1(G_i^{H_{\mathrm{sing}}})$ einen nichttrivialen endlichen Wert
annehmen, der für reguläres $H$ verschwindet (vgl. 200.5–200.7).

**Status 201.B:** ?[O] — KMS-Regularisierung für singuläre $H$ offen.

---

### 201.C — Obstruktionspfeil-Struktur: Kompatibilität mit [O-197-4]

**Frage:** Ist der Sichtbarkeitsmechanismus für singuläres $H$ mit dem
atomaren Rest $[O\text{-}197\text{-}4]$ (alternativer Dualzyklus, NEU-196)
kompatibel, oder erzeugt singuläres $H$ eine **neue** Obstruktionsklasse
in $HH^4(B)$?

**Ansatz (201.C.1):** Aus NEU-196 (Satz 196.1, Verschwindung Defekt bei 0)
folgt, dass der Dualzyklus $\Gamma_{\mathrm{alt}}$ nur für reguläre
Inputs defektfrei ist. Singuläres $H$ könnte einen nicht-verschwindenden
Defekt $\delta(H_{\mathrm{sing}}) \neq 0$ in $HH^4$ induzieren.

**Erwartetes Ergebnis:** Falls $\delta(H_{\mathrm{sing}}) \neq 0$, dann
liefert dies den gesuchten Sichtbarkeitszeugen im Kommutatorquotienten —
oder aber eine neue Obstruktion, die den Ansatz blockiert.

**Status 201.C:** ?[O] — Direkter Kohomologietest ausständig.

---

## DAG-Einbettung

```
[O-199-3]_sing (?[O])
      |
      +---> 201.A: Existenz H_sing-Zeuge (?[O])
      |         |
      |         +--> teilerfremder Sektor (NEU-199 ✓[M]_part) [INPUT]
      |
      +---> 201.B: KMS-Quotiententest G_i^{H_sing} (?[O])
      |         |
      |         +--> Universelles Detektionskriterium (NEU-197 ✓[M]) [INPUT]
      |         +--> KMS_1-Regularisierung singulärer Terme [NEU]
      |
      +---> 201.C: HH4-Kompatibilität / neuer Defekt (?[O])
                |
                +--> Satz 196.1 (Verschwindung Defekt reg.) [INPUT]
                +--> Alternativer Dualzyklus [O-196-2]_neg [INPUT]
```

---

## Nächste Schritte

1. **201.A auflösen:** Schwache Konvergenz von $H_{\mathrm{sing}}$ in $B/[B,B]$ via
   $\ell^2$-Schranken für Primreihen klären (vgl. NEU-187 Restriktionssatz).
2. **201.B auflösen:** KMS$_1$-Regularisierung für singulären Kandidaten
   $H_{\mathrm{sing}}$ explizit durchführen; endlichen Wert oder Divergenz bestimmen.
3. **201.C auflösen:** Hochschild-Randoperator $b_4$ auf $H_{\mathrm{sing}}$ anwenden;
   Defektklasse $\delta(H_{\mathrm{sing}}) \in HH^4(B)$ berechnen.

---

## Offene Obstruktionen (Ausblick)

| Knoten | Frage | Status |
|--------|-------|--------|
| [O-199-3]_sing | Singuläres $H$ sichtbar in $Q_{h,p}$? | ?[O] |
| 201.A | Existenz schwach-konvergenter Zeuge | ?[O] |
| 201.B | KMS-Test für $G_i^{H_{\mathrm{sing}}}$ | ?[O] |
| 201.C | $HH^4$-Defekt bei singulärem $H$ | ?[O] |
| [O-197-4] | Alternativer Dualzyklus (NEU-196) | ?[O] |
