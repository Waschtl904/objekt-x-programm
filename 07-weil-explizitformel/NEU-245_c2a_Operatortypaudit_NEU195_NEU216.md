# NEU-245 — [c.2a] Operatortypaudit: Bewertungsderivationen und Log-Koeffizientenoperator

**Datum:** 27. Juli 2026  
**Quellenblock:** NEU-195, NEU-216 (direkt gelesen)  
**Entschiedener Vorknoten:** \([O\text{-}229\text{-}3B.1f\text{-}c.2a\text{-existing-operator-type-audit}]\)

---

## Leitmaxime

$$
\boxed{\text{Derivation oder unbeschränkter Operator} \;\neq\; \text{Differential eines Komplexes.}}
$$

Aus der Leibnizregel folgt insbesondere **nicht** $\delta_p^2 = 0$. Ein Log-Koeffizientenoperator liefert nicht automatisch eine Graduierung, einen invarianten Liftbereich oder einen quadratnullen Operator. Alle Befunde unten setzen diese Firewall als Prüfmassstab voraus.

---

## 1. Audit: Bewertungsderivationen $\delta_p$ (NEU-195)

### 1.1 Exakter Typ laut Quelle

Definiert (NEU-195, Formel 195.1) auf homogenen Elementen:

$$
\delta_p(a_q) := v_p(q)\,a_q, \qquad a_q \in A_q,
$$

erweitert durch Linearität auf $A = \bigoplus_{q\in\mathbb{Q}_+^\times} A_q$. [cite:9]

| Frage | Auditbefund |
|---|---|
| Definitions- und Zielraum exakt? | Ja: $\delta_p: A \to A$, beide = $A = \bigoplus A_q$ |
| $A$ graduiert? | Ja: $A_q A_r \subseteq A_{qr}$, multiplikative Graduierung |
| $\delta_p \in Z^1(A,A)$? | Ja: quellengegeben (195.2), Derivation, $b\delta_p = 0$ |
| Gewicht von $\delta_p$? | Gewicht $0$: $\delta_p(A_q) \subseteq A_q$ (skaliert, verändert Grad nicht) |
| $\delta_p$ erhöht den Grad um $1$? | **Nein.** $\delta_p$ ist ein Grad-$0$-Operator (Multiplikation mit $v_p(q)$) |
| $\delta_p^2 = 0$? | **Nein.** $\delta_p^2(a_q) = v_p(q)^2 a_q \neq 0$ für $v_p(q) \neq 0, 1$ |
| Kommutator $[\delta_p, \delta_\ell]$? | $[\delta_p, \delta_\ell](a_q) = (v_p(q)v_\ell(q) - v_\ell(q)v_p(q))a_q = 0$: **kommutiert** |
| Invarianz $K_p^{\mathrm{alg}}$ oder $\mathcal{D}(a_p)$? | Nicht direkt quellengegeben; $A_q$-Graduierung ist nicht die Liftbereichsgraduierung |
| Radikalstabilität $\delta_p(N_{a_p}) \subseteq N_{a_p}$? | Nicht quellengegeben; $N_{a_p}$ aus NEU-229, $\delta_p$ aus NEU-195 — kein direkter Schnitt |
| Formabschätzung $a_p(\delta_p k, \delta_p k) \le C\,a_p(k,k)$? | Nicht quellengegeben |

### 1.2 Schlußfolgert

$\delta_p = d_{\mathrm{lift}}$ ist **nicht zulässig**: weder $\delta_p^2 = 0$ noch Grad-$1$-Erhöhung. [cite:9]

Die Derivationen $\delta_p$ sind jedoch **paarweise kommutierend** — das ist die strukturelle Voraussetzung für einen Koszul-Kandidaten (siehe Abschnitt 3).

$$
\boxed{
[O\text{-}229\text{-}3B.1f\text{-}c.2a\text{-}\delta_p\text{-type-audit}]
\quad \checkmark[M]_{\mathrm{neg}}:
\text{kein direktes Differential, aber Kommutatoreigenschaft gesichert.}
}
$$

---

## 2. Audit: Log-Koeffizientenoperator $D_g$ und $\mathcal{A}^{\log}$ (NEU-216)

### 2.1 Exakter Typ laut Quelle

Definiert (NEU-216, 195.10–11 via NEU-195, und NEU-216 Abschn. 216.H) als: [cite:10]

$$
D_g: A_{\mathrm{alg}} \longrightarrow \mathcal{A}^{\log},
\qquad D_g(A_q) \subseteq A_{gq}^{\log},
$$

wobei $\mathcal{A}^{\log} = \operatorname{span}_{\mathrm{fin}}\{\mu_m \mathcal{B}^{\log} \mu_n^* : (m,n)=1\}$.

| Frage | Auditbefund |
|---|---|
| Quell- und Zielraum gleich? | **Nein.** $D_g: A_{\mathrm{alg}} \to \mathcal{A}^{\log}$, echte Inklusion $A_{\mathrm{alg}} \subsetneq \mathcal{A}^{\log}$ |
| Erhaltung von $K_p^{\mathrm{alg}}$ oder $\mathcal{D}(a_p)$? | **Nein:** $D_g$ bildet aus $A_{\mathrm{alg}}$ heraus |
| Iteration $D_g^2$ definiert? | Nicht quellengegeben; $D_g$ bildet in $\mathcal{A}^{\log}$, zweite Anwendung würde Domänenerweiterung benötigen |
| $D_g^2 = 0$? | Nicht behauptet, nicht beweisbar ohne Domänenproblem |
| Grad-$1$-Erhöhung auf einem Komplex? | Nicht quellengegeben: $D_g$ erhöht den multiplikativen Grad um Faktor $g$, keine additive Graduierung |
| $D_g$ als Koeffizient in bestehendem Komplex? | Offen: nicht in NEU-195/216 konstruiert |

### 2.2 Schlussfolgert

$D_g = d_{\mathrm{lift}}$ ist **nicht zulässig**: unterschiedliche Quell- und Zielräume, Iteration nicht definiert, kein $d^2=0$. [cite:10]

$D_g$ ist jedoch als **Verbindungsoperator oder Koeffizient** in einem bereits vorhandenen Komplex prinzipiell verwendbar, sofern ein passender Rahmen konstruiert wird.

$$
\boxed{
[O\text{-}229\text{-}3B.1f\text{-}c.2a\text{-}D_g\text{-type-audit}]
\quad \checkmark[M]_{\mathrm{neg}}:
\text{kein direktes Differential; unterschiedliche Domänen schließen } d_{\mathrm{lift}} = D_g \text{ aus.}
}
$$

---

## 3. Koszul-Kandidat aus kommutierenden Bewertungsderivationen

Dies ist der **konstruktiv stärkste Kandidat**, weil die Nilpotenz nicht geraten, sondern aus einer auditierbaren Kommutatoridentität folgt.

### 3.1 Strukturelle Voraussetzung

Laut Abschnitt 1.1 gilt quellengegeben:

$$
[\delta_p, \delta_\ell] = 0 \qquad \text{für alle Primzahlen } p, \ell.
$$

### 3.2 Koszul-Konstruktion (Kandidat, noch nicht realisiert)

Falls ein gemeinsames liftseitiges Modul $M_p$ mit:
- Vektorraumstruktur,
- Wirkung aller $\delta_q$ ($q \in S$, $S$ endliche Primmenge),
- $\delta_q(M_p) \subseteq M_p$ für alle $q \in S$,

existiert, entsteht ein Koszul-Komplex:

$$
C_{p,\mathrm{lift}}^n = M_p \otimes \Lambda^n(\mathbb{C}^S),
\qquad
d_{\mathrm K}(m \otimes \omega) = \sum_{q \in S} \delta_q(m) \otimes e_q \wedge \omega.
$$

Dann gilt:

$$
d_{\mathrm K}^2 = \sum_{q < \ell} [\delta_q, \delta_\ell] \otimes e_q \wedge e_\ell \wedge (\,\cdot\,) = 0,
$$

da alle Kommutatoren verschwinden.

### 3.3 Offene Voraussetzungen (Firewall [c.2b])

Die folgenden Punkte sind **nicht quellengegebene Tatsachen** und müssen konstruiert oder widerlegt werden:

| Frage | Status |
|---|---|
| Was ist das gemeinsame Modul $M_p$? | $?[O]$: $K_p^{\mathrm{alg}}$ oder $\mathcal{D}(a_p)$ ist Kandidat, aber $\delta_q$-Invarianz nicht geprüft |
| Warum enthält $M_p$ die $\mathcal{D}(a_p)$-Struktur? | $?[O]$: $\mathcal{D}(a_p) \subseteq K_p^{\mathrm{alg}} \subseteq A$ muss $\delta_q$-stabil sein |
| Warum ist $S$ endlich und intrinsisch? | $?[O]$: Unendlicher Primindex erfordert Kontrollmechanismus |
| Radikalstabilität: $\delta_q(N_{a_p}) \subseteq N_{a_p}$? | $?[O]$: Notwendig für Abstieg auf $H_{a^{\mathrm{raw}},p}$ (Teilknoten c.2d) |
| Kohomologie nichttrivial? | $?[O]$: NT2-Kriterium aus NEU-243 muss erfüllt werden |
| Abstieg: $F_p^r \circ d_{\mathrm K}$ wohldefiniert auf Quotienten? | $?[O]$: Setzt $\delta_q(\ker F_p^r) \subseteq \ker F_p^r$ voraus |

$$
\boxed{
[O\text{-}229\text{-}3B.1f\text{-}c.2b\text{-valuation-derivation-koszul-viability}]
\quad ?[O]_{\mathrm{offen}}.
}
$$

---

## 4. Vorabaudit: Invarianz von $\mathcal{D}(a_p)$ und $K_p^{\mathrm{alg}}$ unter $\delta_q$

Dies ist der **logisch erste Schritt** für [c.2b]. Aus den Quellen ist bekannt:

- $K_p^{\mathrm{alg}} \subseteq A$ ist ein linearer Teilraum (NEU-221e, NEU-229).
- $\mathcal{D}(a_p) \subseteq K_p^{\mathrm{alg}}$ ist ein Formbereich (NEU-229).
- $\delta_q(a_r) = v_q(r)\,a_r$ wirkt diagonalisierend auf homogene Elemente von $A$.

Observation: Falls $K_p^{\mathrm{alg}}$ aus homogenen Elementen besteht (d.h. $K_p^{\mathrm{alg}} = \bigoplus_{q} (K_p^{\mathrm{alg}} \cap A_q)$), dann gilt

$$
\delta_r(K_p^{\mathrm{alg}}) \subseteq K_p^{\mathrm{alg}}
$$

tautologisch, denn $\delta_r$ skaliert homogene Elemente ohne den Grad zu wechseln. Dies ist jedoch **kein quellengesigerter Befund** über $K_p^{\mathrm{alg}}$ — die Homogenität von $K_p^{\mathrm{alg}}$ muss aus NEU-221e/229 direkt verifiziert werden.

**Konsequenz für Radikalstabilität:** Wenn $K_p^{\mathrm{alg}}$ homogen ist und $N_{a_p} \subseteq K_p^{\mathrm{alg}}$ ebenfalls eine homogene Teilmenge, dann folgt $\delta_r(N_{a_p}) \subseteq N_{a_p}$. Dies muss in [c.2d] mit NEU-229 abgeglichen werden.

---

## 5. Rangliste der Kandidaten für $d_{\mathrm{lift}}$

| Kandidat | $d^2=0$-Begründung | Quellenverankerung | Status |
|---|---|---|---|
| $d_{\mathrm{lift}} = \delta_p$ | Nein ($\delta_p^2 \neq 0$) | NEU-195 | $\checkmark[M]_{\mathrm{neg}}$ |
| $d_{\mathrm{lift}} = D_g$ | Domänenproblem, unklar | NEU-216 | $\checkmark[M]_{\mathrm{neg}}$ |
| $d_{\mathrm{lift}} = d_{\mathrm K}$ (Koszul) | $[\delta_q, \delta_\ell]=0$ → strukturell | NEU-195 | $?[O]_{\mathrm{offen}}$ |
| $d_{\mathrm{lift}} = b$ oder $B$ (Hochschild) | Bereits $b^2=0$, $B^2=0$ | NEU-174ff. | Einbettung $?[O]$ |

---

## 6. Neue Teilknoten aus diesem Audit

$$
\boxed{[O\text{-}229\text{-}3B.1f\text{-}c.2a\text{-existing-operator-type-audit}] \quad \checkmark[K/M].}
$$

**Umfang:** $\delta_p$ und $D_g$ als direkte $d_{\mathrm{lift}}$-Kandidaten ausgeschlossen. Koszul-Kandidat $d_{\mathrm K}$ prinzipiell zulässig (Kommutator null, quellengegeben), aber Modulinvarianz noch offen.

Offene Folgeknoten:

$$
\boxed{[O\text{-}229\text{-}3B.1f\text{-}c.2b\text{-valuation-derivation-koszul-viability}] \quad ?[O]_{\mathrm{offen}}.}
$$

$$
\boxed{[O\text{-}229\text{-}3B.1f\text{-}c.2c\text{-hoch-cyclic-lift-embedding-audit}] \quad ?[O]_{\mathrm{offen}}.}
$$

$$
\boxed{[O\text{-}229\text{-}3B.1f\text{-}c.2d\text{-form-radical-and-quotient-descent}] \quad ?[O]_{\mathrm{offen}}.}
$$

---

## 7. Priorität für den nächsten Schritt

Der logisch erste Schritt für [c.2b] ist die Prüfung der $\delta_q$-Invarianz von $K_p^{\mathrm{alg}}$ und $\mathcal{D}(a_p)$ aus den Primärquellen NEU-221e und NEU-229. Erst danach kann die Modulinvarianz des Koszul-Komplexes auf solide Quellengrundlage gestellt werden.

Der Hochschild-/zyklische Einbettungskandidat ([c.2c]) ist nachrangig: Er setzt eine typisierte lineare Einbettung $\mathcal{D}(a_p) \hookrightarrow C^r(A,M)$ voraus, die noch nicht quellengegeben ist.
