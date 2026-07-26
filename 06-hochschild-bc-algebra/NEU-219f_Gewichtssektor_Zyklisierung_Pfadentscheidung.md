# NEU-219f — Gewichtssektor, Zyklisierungsannihilation, Pfadentscheidung

**DAG-Position:** Nachfolger von NEU-219e (Commit 8f3bb78).  
**Abgeschlossen:** [O-219-5c1c-para] ✓[K/M]; [O-219-5c1c-cyc] ✓[M]$_{\mathrm{neg}}$.  
**Offene Primärknoten:** [O-219-5d1] Hopf-Aktion; [O-219-5e1] Dilatationsalgebra.

---

## 1. Geladener parazyklischer Gewichtsraum

Sei $C_\sigma^n(A)$ der $\sigma_\beta$-getwistete parazyklische Kochainraum und $T_n := \lambda_{\sigma_\beta,n}^{\,n+1}$.
Für $w \in \mathbb{C}^\times$ definiere den $w$-Eigenraum:
$$
C_{\sigma,w}^n(A) := \{\varphi \in C_\sigma^n(A) : T_n\varphi = w\varphi\}.
$$

Da die parazyklischen Identitäten implizieren $b^{\sigma_\beta} T_n = T_{n+1} b^{\sigma_\beta}$, ist
$$
\boxed{ C_{\sigma,w}^\bullet(A) }
$$
ein wohldefinierter **Hochschildunterkomplex** für jedes $w$.

Für den konstruierten Kozykel gilt $w = g^{-\beta}$, also:
$$
\Phi_{\beta,\chi} \in Z^4\!\left(C_{\sigma,g^{-\beta}}^\bullet(A),\, b^{\sigma_\beta}\right).
$$

$$\boxed{ [O\text{-}219\text{-}5c1c\text{-para}] \quad \checkmark[K/M]. }$$

Der geladene Gewichtssektor ist als parazyklische Buchhaltung der Ladung mathematisch sinnvoll. Er besitzt $b^{\sigma_\beta}\Phi = 0$ und $T\Phi = g^{-\beta}\Phi$, aber — wie Abschnitt 2 zeigt — keine gewöhnliche zyklische Klasse.

---

## 2. Gewöhnliche Zyklisierung annihiliert den geladenen Sektor

Für $g \neq 1$ und $\beta > 0$ gilt $w = g^{-\beta} \neq 1$, also wirkt auf dem $w$-Eigenraum:
$$
1 - T_n = (1-w)\operatorname{id},
$$
und $1 - T_n$ ist dort invertierbar.

### Invariantenmodell

Die standardmäßige getwistete zyklische Theorie verlangt $T_n\varphi = \varphi$. Daher:
$$
C_{\sigma,w}^n(A) \cap \ker(1 - T_n) = \{0\} \qquad (w \neq 1).
$$

### Koinvariantenmodell

Alternativ zyklisiert man durch den Quotienten $C_\sigma^n(A)/(1-T_n)C_\sigma^n(A)$.
Für $\varphi \in C_{\sigma,w}^n(A)$ gilt jedoch:
$$
\varphi = \frac{1}{1-w}(1-T_n)\varphi,
$$
also ist die Klasse im Koinvariantenquotienten null: $[\varphi] = 0$.

Insbesondere:
$$
\boxed{ [\Phi_{\beta,\chi}]_{\mathrm{zyklisiert}} = 0 \qquad (g \neq 1). }
$$

$$\boxed{ [O\text{-}219\text{-}5c1c\text{-cyc}] \quad \checkmark[M]_{\mathrm{neg}}. }$$

Der ausgeschlossene Kandidat ist präzise:
> *Der reine $g^{-\beta}$-parazyklische Gewichtssektor liefert ohne weitere Koeffizienten eine gewöhnliche getwistete zyklische Klasse.*

$$\boxed{ \text{Pfad I erklärt die Ladung, beseitigt sie aber nicht zyklisch.} }$$

---

## 3. Konsequenz für Pfad I

Pfad I ist für das Projektziel zu schwach, sofern eine Connes-$B$-Struktur, Periodizität oder eine standardmäßige zyklische Paarung benötigt wird. Ein neu definierter Ausdruck $HC_{\sigma_\beta,g}^{4,\mathrm{para}}(A)$ wäre eine genuinely neue parazyklische Theorie und dürfte nicht als gewöhnliches $HC^4$ bezeichnet werden.

---

## 4. Pfad II: Hopf-zyklischer Ansatz

**Typologisch kürzester konstruktiver Kandidat.**

Der Ausschluss aus NEU-219e betrifft eine eindimensionale $A$-Bimodullinie. Er schließt nicht aus, eine eindimensionale Koeffizientenstruktur über der Skalierungs-Hopf-Algebra
$$
\mathcal{H} = \mathbb{C}[\mathbb{Q}_+^\times]
$$
zu verwenden. Die Ladung könnte durch einen Charakter $\delta_{g,\beta}: \mathcal{H} \to \mathbb{C}$ bzw. durch ein **modulares Paar** oder ein **stabiles Anti-Yetter–Drinfeld-Modul (SAYD)** getragen werden.

Der Koeffizient wäre dann kein eindimensionaler $A$-Bimodul; das frühere No-go aus NEU-219e greift nicht unmittelbar.

**Nächster Typaudit:**

$$\boxed{ [O\text{-}219\text{-}5d1]: \quad A_{\mathrm{alg}} \text{ ist eine }\mathcal{H}\text{-Modulalgebra?} \quad ?[O]. }$$

$$\boxed{ [O\text{-}219\text{-}5d2]: \quad \text{Eindimensionaler SAYD-/modularer Koeffizient mit Gewicht }g^\beta? \quad ?[O]. }$$

Zu prüfen:
- $A_{\mathrm{alg}}$ ist $\mathcal{H}$-Modulalgebra via $\sigma_\beta$-Wirkung
- $M = \mathfrak{M}^{\log}_{\mathrm{glob}}$ trägt kompatible $\mathcal{H}$-Struktur
- Ein eindimensionales SAYD-Modul $(\mathbb{C}_{g,\beta}, \delta, \rho)$ mit $\delta(\mathbf{e}) = g^\beta \cdot h_{[g]} \otimes \mathbf{e}$ existiert

---

## 5. Pfad III: Dilatationsalgebra / Crossed-Product

**Langfristig strukturell stärkster Kandidat (Weil- und Operatorbrücke).**

Erweiterung um invertierbaren Ladungsträger $u_g$ mit:
$$
\sigma_\beta(u_g) = g^\beta u_g, \qquad u_g a u_g^{-1} = \gamma_g(a).
$$

$\gamma_g$ muss eine tatsächlich definierte Automorphismuswirkung sein. Im BC-Kern sind die natürlichen Skalierungstransporte $\rho_g$ teilweise nicht unital bzw. nicht invertierbar; $\rho_g$ darf nicht ohne Weiteres als Automorphismus eingesetzt werden.

Dieser Pfad erfordert eine **Dilatations- oder Gruppenvervollständigung** der Semigruppenarchitektur.

$$\boxed{ [O\text{-}219\text{-}5e1]: \quad \text{Dilatationsalgebra mit invertierbarem }u_g \quad ?[O]. }$$

$$\boxed{ [O\text{-}219\text{-}5e2]: \quad \text{Zyklische Klasse der neutralisierten erweiterten Kochain} \quad \text{gesperrt durch [O-219-5e1].} }$$

---

## 6. Revidierter DAG

| Knoten | Inhalt | Status |
|--------|--------|--------|
| [O-219-5c1c-para] | $g^{-\beta}$-Gewichtseigenunterkomplex | ✓[K/M] |
| **[O-219-5c1c-cyc]** | Gewöhnliche Zyklisierung annihiliert $w \neq 1$ | **✓[M]$_{\mathrm{neg}}$** |
| **[O-219-5d1]** | $\mathcal{H}$-Modulalgebra-Struktur auf $A_{\mathrm{alg}}$ | **?[O] primär Hopf** |
| [O-219-5d2] | SAYD-Koeffizient mit Ladung $g$ | ?[O] bedingt |
| **[O-219-5e1]** | Dilatationsalgebra, invertierbares $u_g$ | **?[O] primär Crossed-Prod.** |
| [O-219-5e2] | Zyklische Klasse erweiterte Kochain | gesperrt |

```
[O-219-5c1c-para]  g^{-beta}-Eigenunterkomplex                  [K/M]
[O-219-5c1c-cyc]   Zyklisierung w!=1 -> [Phi]=0                 [M]_neg
      |
      +== Pfad II (Hopf-zyklisch, kuerzerer Typ) ==
      |         |
      |  [O-219-5d1]  A_alg ist H-Modulalgebra?               ?[O] PRIMAER
      |         |
      |  [O-219-5d2]  SAYD-Koeffizient dim 1, Gewicht g^beta   ?[O]
      |
      +== Pfad III (Dilatation/Crossed-Product, staerkere Arch.) ==
                |
      [O-219-5e1]  Dilatationsalgebra, u_g invertierbar        ?[O] PRIMAER
                |
      [O-219-5e2]  zyklische Klasse erweiterter Kochain        gesperrt
```

**Primärer nächster Audit (Hopf):** [O-219-5d1] — Prüfung der $\mathcal{H} = \mathbb{C}[\mathbb{Q}_+^\times]$-Modulalgebra-Struktur auf $A_{\mathrm{alg}}$.

**Primärer nächster Audit (Dilatation):** [O-219-5e1] — Konstruierbarkeit eines invertierbaren $u_g$ und Typdefinition der Automorphismuswirkung $\gamma_g$.

---

## 7. Gesamturteil

$$\boxed{ \text{Pfad I erklärt die Ladung, beseitigt sie aber nicht zyklisch.} }$$

Die drei verbleibenden Wege unterscheiden sich in Tiefe und Zeitaufwand:

| Pfad | Strategie | Zeithorizont |
|------|-----------|-------------|
| I (para) | Neuer Gewichtssektorbegriff | Erklärend, kein $HC$ |
| **II (Hopf)** | SAYD-Koeffizient über $\mathcal{H}$ | **Typologisch kürzester Weg** |
| III (Dilatation) | Crossed-Product mit $u_g$ | Stärkste Weil-Architektur |

Empfehlung: Zunächst [O-219-5d1] (Hopf) auditieren, da das No-go aus NEU-219e dort nicht greift und die Hopf-zyklische Maschinerie die Ladung als SAYD-Datum tragen kann, ohne die Algebrastruktur zu verändern. Parallel [O-219-5e1] vorbereiten.
