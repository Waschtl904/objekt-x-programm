# NEU-219k — Multiplikator-, Paarungs- und algebraischer Morita-Audit

**DAG-Position:** Nachfolger von NEU-219j (Commit 66f2581).  
**Geschlossen:** [O-219-5e2-mult0] ✓[M]; [O-219-5e1e-full-alg] ✓[M]; [O-219-5e1e-local-units] ✓[K/M].  
**Negativbefund:** [O-219-5e2-formula-current] ✓[M]$_{\mathrm{neg}}$ — aktueller Formeltyp nicht definiert.  
**Primäre offene Knoten:** [O-219-5e1e-corner-core]; [O-219-5e2-modmult]; [O-219-5e2-pair].

---

## 1. Der Multiplikator wirkt automatisch auf Algebraelemente

Sei $\widetilde{A} = C_0(\mathbb{A}_f) \rtimes_\gamma \mathbb{Q}_+^\times$. Für jeden Multiplikator $U \in M(\widetilde{A})$ und jedes $x \in \widetilde{A}$ gilt definitionsgemäß $Ux \in \widetilde{A}$ und $xU \in \widetilde{A}$, da $\widetilde{A}$ ein zweiseitiges essentielles Ideal in seinem Multiplikatorverband ist.

$$\boxed{ [O\text{-}219\text{-}5e2\text{-mult0}]: \quad U_{g^{-1}}x \in \widetilde{A} \text{ für jedes } x \in \widetilde{A} \quad \checkmark[M]. }$$

Sobald $a_0 \widetilde{L}(a_1,\ldots,a_4) \in \widetilde{A}$ bewiesen wäre, gäbe es kein zusätzliches Multiplikatorproblem auf der Algebraseite.

---

## 2. Der erste exakte Fehler: Modulwertigkeit von $\widetilde{L}$

Der geplante Kochainlift hat den Typ:
$$
\widetilde{L}: \widetilde{A}_{\mathrm{alg}}^{\otimes 4} \longrightarrow \widetilde{M}_{\mathrm{orb}}.
$$

Folglich liegt $a_0 \widetilde{L}(a_1,\ldots,a_4)$ im abstrakten Bimodul $\widetilde{M}_{\mathrm{orb}}$, nicht in $\widetilde{A}$. Der Ausdruck
$$
\widetilde{\omega}\bigl(U_{g^{-1}}\,a_0\,\widetilde{L}(a_1,\ldots,a_4)\bigr)
$$
mit einem Gewicht $\widetilde{\omega}: \widetilde{A} \to \mathbb{C}$ ist gegenwärtig **nicht typdefiniert**. Der erste exakte Fehler ist nicht $U_{g^{-1}} \notin \widetilde{A}$, sondern:
$$
\boxed{\widetilde{L}(\ldots) \notin \widetilde{A} \text{ nach dem bisher konstruierten Typ.}}
$$

$$\boxed{ [O\text{-}219\text{-}5e2\text{-formula-current}] \quad \checkmark[M]_{\mathrm{neg}}. }$$

Ausgeschlossen ist nur die unveränderte Verwendung eines Algebra-KMS-Gewichts auf einem abstrakt modulwertigen Ausdruck.

---

## 3. Zwei typkorrekte Reparaturrouten

### Route A — konkrete Modulrealisierung (abhängig von [O-219-5e1d3])

Konstruiere einen $\widetilde{A}_{\mathrm{alg}}$-Bimodulhomomorphismus
$$
\Pi: \widetilde{M}_{\mathrm{orb}} \longrightarrow \widetilde{A} \quad\text{oder}\quad \Pi: \widetilde{M}_{\mathrm{orb}} \longrightarrow M(\widetilde{A}),
$$
sodass $\Pi(a_0 \widetilde{L}(\ldots))$ im Definitionsbereich der Multiplikatorinsertion und des Gewichts liegt. Erforderlich für den Nichtverschwindensnachweis: $\Pi(a_0 \widetilde{L}(\ldots)) \neq 0$ auf dem ausgezeichneten Testwert.

### Route B — genuines duales Modulgewicht (unabhängig von $\Pi$)

Alternativ direkt:
$$
\boxed{\Omega: \widetilde{M}_{\mathrm{orb}} \longrightarrow \mathbb{C}}
$$
mit modularer Bimodulidentität:
$$
\Omega(\xi \cdot a) = \Omega(\widetilde{\sigma}_\beta(a) \cdot \xi) \tag{3.1}
$$
für $a \in \widetilde{A}_{\mathrm{alg}}$, $\xi \in \widetilde{M}_{\mathrm{orb}}$. Route B benötigt keine Einbettung des Moduls in die Algebra.

Die Wirkung von $U_{g^{-1}}$ auf $\widetilde{M}_{\mathrm{orb}}$ folgt für ein blou00dfalgebraisches Bimodul nicht automatisch aus $U_{g^{-1}} \in M(\widetilde{A})$; hierfür wird eine nichtdegenerierte bzw. **firm** ausgeweitete Modulstruktur oder ein eigener Multiplikatormodul benötigt.

$$\boxed{ [O\text{-}219\text{-}5e2\text{-modmult}]: \quad U_{g^{-1}} \text{ wirkt auf }\widetilde{M}_{\mathrm{orb}} \quad ?[O]. }$$

$$\boxed{ [O\text{-}219\text{-}5e2\text{-pair}]: \quad \exists\,\Omega: \widetilde{M}_{\mathrm{orb}} \to \mathbb{C} \text{ mit (3.1) und Nichtverschwindensbedingung} \quad ?[O]. }$$

---

## 4. Der konjugierte Randtwist bleibt korrekt

Angenommen, Modulmultiplikation mit $U_{g^{-1}}$ und $\Omega$ seien definiert. Im Rand verbleibt die Differenz:
$$
\Omega\bigl(U_{g^{-1}}a_0\widetilde{L}(a_1,\ldots,a_4)a_5\bigr)
- \Omega\bigl(U_{g^{-1}}\tau(a_5)\,a_0\widetilde{L}(a_1,\ldots,a_4)\bigr).
$$

Mit (3.1) wird der erste Term zu $\Omega(\widetilde{\sigma}_\beta(a_5)\,U_{g^{-1}}a_0\widetilde{L}(\ldots))$. Damit die Terme übereinstimmen, wird benötigt:
$$
\tau(a)\,U_{g^{-1}} = U_{g^{-1}}\,\widetilde{\sigma}_\beta(a),
$$
also:
$$
\boxed{\tau = \gamma_g \circ \widetilde{\sigma}_\beta.}
$$

Der konjugierte Twist aus NEU-219i ist typologisch richtig und hängt jetzt präzise an [O-219-5e2-modmult] und [O-219-5e2-pair].

---

## 5. Algebraische Vollheit des Eckprojektors

Für ein erzeugendes Monom $\gamma_r(\iota(f))U_s \in \widetilde{A}_{\mathrm{alg}}$:
$$
\boxed{\gamma_r(\iota(f))U_s = (\gamma_r(e)U_r)\cdot e \cdot (\iota(f)U_{r^{-1}s}).} \tag{5.1}
$$

Beide äußeren Faktoren liegen im algebraischen Crossed-Product. Somit liegt jedes erzeugende Monom in $\widetilde{A}_{\mathrm{alg}}\,e\,\widetilde{A}_{\mathrm{alg}}$:
$$
\boxed{\widetilde{A}_{\mathrm{alg}}\,e\,\widetilde{A}_{\mathrm{alg}} = \widetilde{A}_{\mathrm{alg}}.} \tag{5.2}
$$

$$\boxed{ [O\text{-}219\text{-}5e1e\text{-full-alg}] \quad \checkmark[M]. }$$

Dies ist stärker als die bloße Dichtheit des von $e$ erzeugten $C^*$-Ideals.

---

## 6. Lokale Einheiten des algebraischen Crossed-Products

Der Kern $\widetilde{B}_{\mathrm{alg}}$ besteht aus kompakt getragenen, lokal konstanten Funktionen auf $\mathbb{A}_f$. Für eine endliche Menge von Monomen $F_i U_{s_i}$: Wähle kompakt-offenes $K \subseteq \mathbb{A}_f$ mit $\operatorname{supp}F_i \cup s_i^{-1}\operatorname{supp}F_i \subseteq K$. Dann $p := 1_K \in \widetilde{B}_{\mathrm{alg}}$ und:
$$
p(F_i U_{s_i}) = F_i U_{s_i}, \qquad (F_i U_{s_i})p = F_i U_{s_i}.
$$

$$\boxed{ \widetilde{A}_{\mathrm{alg}} \text{ besitzt lokale Einheiten.} }$$

$$\boxed{ [O\text{-}219\text{-}5e1e\text{-local-units}] \quad \checkmark[K/M]. }$$

Dies verbessert die Voraussetzungen für eine nichtunitale bzw. **firme** Morita-Konstruktion erheblich.

---

## 7. Was die $C^*$-Morita-Äquivalenz noch nicht liefert

Aus der $C^*$-Morita-Äquivalenz $A_{C^*} \sim_M \widetilde{A}$ folgt nicht automatisch die Morita-Invarianz der algebraischen Hochschildkomplexe der gewählten dichten Unteralgebren. Vor einem expliziten Transfer muss insbesondere geprüft werden:

$$
\boxed{e\,\widetilde{A}_{\mathrm{alg}}\,e \stackrel{?}{=} j_A(A_{\mathrm{alg}}).} \tag{7.1}
$$

Die algebraische Vollheit (5.2) ist notwendig und nun bewiesen; die exakte Identifikation des algebraischen Eckkerns ist davon unabhängig.

$$
\boxed{ [O\text{-}219\text{-}5e1e\text{-corner-core}]: \quad e\widetilde{A}_{\mathrm{alg}}e \stackrel{?}{=} j_A(A_{\mathrm{alg}}) \quad ?[O]. }
$$

---

## 8. Aufspaltung von [O-219-5e1e-alg]

Ein Standard-Morita-Resultat liefert einen Kohomologieisomorphismus nur nach vollständiger Angabe der algebraischen Morita-Daten und des übertragenen Koeffizientenmoduls. Es liefert nicht automatisch eine konkrete Formel für $\widetilde{L}$. Daher:

$$\boxed{ [O\text{-}219\text{-}5e1e\text{-corner-core}] \quad ?[O], }$$

$$\boxed{ [O\text{-}219\text{-}5e1e\text{-Morita-data}]: \quad \text{firme Morita-Daten und induzierter Koeffiziententyp} \quad ?[O], }$$

$$\boxed{ [O\text{-}219\text{-}5e1e\text{-chain}]: \quad \text{explizite Hochschild-Kettenabbildung} \quad \text{gesperrt durch corner-core/Morita-data}, }$$

$$\boxed{ [O\text{-}219\text{-}5e1e\text{-NV}]: \quad [\widetilde{L}] \neq 0 \quad \text{gesperrt.} }$$

---

## 9. Revidierter DAG

| Knoten | Inhalt | Status |
|--------|--------|--------|
| [O-219-5e2-mult0] | $U_{g^{-1}}x \in \widetilde{A}$ für $x \in \widetilde{A}$ | ✓[M] |
| [O-219-5e1e-full-alg] | $\widetilde{A}_{\mathrm{alg}}\,e\,\widetilde{A}_{\mathrm{alg}} = \widetilde{A}_{\mathrm{alg}}$ | ✓[M] |
| [O-219-5e1e-local-units] | $\widetilde{A}_{\mathrm{alg}}$ besitzt lokale Einheiten | ✓[K/M] |
| **[O-219-5e2-formula-current]** | Aktueller Formeltyp nicht definiert | **✓[M]$_{\mathrm{neg}}$** |
| **[O-219-5e1e-corner-core]** | $e\widetilde{A}_{\mathrm{alg}}e = j_A(A_{\mathrm{alg}})$? | **?[O] primär** |
| [O-219-5e1e-Morita-data] | Firme Morita-Daten, induzierter Koeffizient | ?[O] |
| [O-219-5e1e-chain] | Explizite Kettenabbildung | gesperrt |
| [O-219-5e1e-NV] | $[\widetilde{L}] \neq 0$ | gesperrt |
| **[O-219-5e2-modmult]** | $U_{g^{-1}}$ wirkt auf $\widetilde{M}_{\mathrm{orb}}$ | **?[O]** |
| **[O-219-5e2-pair]** | $\Omega: \widetilde{M}_{\mathrm{orb}} \to \mathbb{C}$ mit (3.1) | **?[O]** |
| [O-219-5e2] | $b^\tau\widetilde{\Phi}=0$, $\lambda_\tau\widetilde{\Phi}=\widetilde{\Phi}$ | gesperrt |

```
[O-219-5e1e-full-alg]   A-tilde-alg * e * A-tilde-alg = A-tilde-alg  [M]
[O-219-5e1e-local-units] lok. Einheiten via 1_K                       [K/M]
      |
[O-219-5e1e-corner-core]  e*A-tilde-alg*e = j_A(A_alg)?              ?[O] PRIMAER
      |
[O-219-5e1e-Morita-data]  firme Morita-Daten, Koeff.-Transfer        ?[O]
      |
[O-219-5e1e-chain]   explizite Kettenabbildung L^cup -> C^4           gesperrt
      |
[O-219-5e1e-NV]      [L-tilde] != 0                                   gesperrt

[O-219-5e2-modmult]  U_{g^{-1}} wirkt auf M-orb (firm/ndeg Modul)    ?[O] parallel
[O-219-5e2-pair]     Omega: M-orb -> C mit Bimodulidentitaet (3.1)    ?[O] parallel
      |
[O-219-5e2]  b^tau Phi-tilde = 0, lambda_tau Phi-tilde = Phi-tilde    gesperrt
```

---

## 10. Naechster atomarer Schritt

$$
\boxed{e\,\widetilde{A}_{\mathrm{alg}}\,e \stackrel{?}{=} j_A(A_{\mathrm{alg}}).}
$$

Diese Eckidentität entscheidet, ob der algebraisch volle Idempotent $e$ tatsächlich eine Morita-Brücke zwischen den beiden im Projekt verwendeten algebraischen Kernen erzeugt. Parallel kann untersucht werden, ob $\widetilde{M}_{\mathrm{orb}}$ als nichtdegenerierter bzw. firmer Modul eine kanonische Erweiterung der $\widetilde{A}_{\mathrm{alg}}$-Wirkung auf geeignete Multiplikatoren besitzt.

**Korrekturpunkt aus NEU-219j:** Das Multiplikatorproblem auf der **Algebra** ist gelöst ([O-219-5e2-mult0]). Offen ist die Multiplikatorwirkung und die modulare Paarung auf dem **Koeffizientenmodul** ([O-219-5e2-modmult], [O-219-5e2-pair]).
