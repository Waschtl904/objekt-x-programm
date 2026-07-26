# NEU-219y — Direktaudit: Zieltypbrücke für $D_g$ von NEU-211 über NEU-216/217

**Datei:** `katalog/NEU-219y_Direktaudit_Dg_Zieltypbruecke_NEU211_NEU217.md`  
**DAG-Position:** Nachfolger von NEU-219x (Commit 759151a). Quellen- und Typbrückenaudit zwischen NEU-211 und NEU-216/217.  
**Primärer Knoten:** `[O-219-5e1j-Dg-target-from-NEU211]` (negativ, bereits in NEU-219x festgehalten) vs. `[O-219-5e1j-Dg-global-target]` (dieser Knoten).  
**Der ursprünglich geplante Cup-Rotationsaudit wird auf NEU-219z verschoben.**  
**Datum:** 2026-07-25

---

## 0. Korrektur des Vorgängerbefunds

NEU-219x (Commit 759151a) hat korrekt und ausschließlich festgehalten:

$$
\boxed{\text{NEU-211 allein beweist nicht } D_g(A_{\mathrm{alg}}) \subseteq M_g.}
$$
$$
[O\text{-}219\text{-}5e1j\text{-Dg-target-from-NEU211}] \quad \checkmark[M]_{\mathrm{neg,Quelle}}.
$$

Daraus folgt **nicht** $D_g(A_{\mathrm{alg}}) \not\subseteq M_g$ und auch nicht, dass der Cup-Rotationsaudit mathematisch gesperrt bleibt. Dieser Knoten prüft die spätere Zieltypbrücke in NEU-216/217.

---

## 1. Atomarer Prüfauftrag

Zu beweisen ist die vollständige Abbildungskette
$$
A_{\mathrm{alg}} \xrightarrow{D_g} \mathcal{A}^{\log} \supseteq \mathfrak{M}_{\mathrm{glob}}^{\log} = \bigoplus_{h\in\Gamma} M_h,
$$
genauer:
$$
\boxed{D_g\bigl((A_{\mathrm{alg}})_h\bigr) \subseteq M_{gh}.}
$$

---

## 2. Wortgetreue Extraktion aus NEU-216

Aus `NEU-216_Log_Koeffiziententyp_B-log.md`:

$$
\mathcal{B}_{\mathrm{alg}} \subsetneq \mathcal{B}^{\log} \subsetneq C(\widehat{\mathbb{Z}}) \text{ Banach-}*\text{-Algebra}, \qquad \sigma_k,\rho_k,T_a : \mathcal{B}^{\log} \to \mathcal{B}^{\log}, \qquad G_{a,d} \in \mathcal{B}^{\log}. \tag{216.1}
$$
$$
D_g(A_{\mathrm{alg}}) \subseteq \mathcal{A}^{\log} := \operatorname{span}_{\mathrm{fin}}\{\mu_m \mathcal{B}^{\log}\mu_n^* : (m,n)=1\} \subset A_{C^*}. \tag{216.2}
$$

**Ergebnis:** NEU-216 schließt die Einbettung der $G_{a,d}$-Elemente aus NEU-211 in die kontrollierte Banach-$*$-Algebra $\mathcal{B}^{\log}$ ab und konstruiert $\mathcal{A}^{\log}$ als Zwischenraum. **NEU-216 ist NICHT identisch mit $\mathfrak{M}_{\mathrm{glob}}^{\log}$** — letzteres wird erst in NEU-217 konstruiert. Status laut NEU-216 selbst: „NEU-216 vollständig geschlossen. Nächster Schritt: NEU-217 (lokaler $p$-Block)."

---

## 3. Wortgetreue Extraktion aus NEU-217 [O-217-2c-6]

### 3.1 Definition von $\mathfrak{M}_{\mathrm{glob}}^{\log}$ und seiner $\Gamma$-Gradierung

Intrinsische Konstruktion [O-217-2c-6b-def]:
$$
M_{\mathrm{glob},G}^{\log} := \bigcap_{N \in \mathscr{C}} N, \qquad
M_{\mathrm{glob}}^{\log} := \overline{B_{\mathrm{alg}} + M_{\mathrm{glob},G}^{\log}}^{\|\cdot\|_{B^{\log}}}, \tag{217.1–2}
$$
wobei $\mathscr{C}$ die Familie aller abgeschlossenen $N \subseteq B^{\log}$ mit $B_{\mathrm{alg}}NB_{\mathrm{alg}} \subseteq N$, $\sigma_n(N) \subseteq N$, $\rho_n(N) \subseteq N$, $G_{k,d} \in N$ ist.

Graduierter Bimodul [O-217-2c-6c]:
$$
\mathfrak{M}_{\mathrm{glob}}^{\log} := \operatorname{span}_{\mathrm{fin}}\{a\,\xi\,b : a,b \in A_{\mathrm{alg}},\, \xi \in M_{\mathrm{glob}}^{\log}\} \subseteq \mathcal{A}^{\log}. \tag{217.3}
$$
Einbettungskette: $M_{\mathrm{glob}}^{\log} \subseteq B^{\log} \hookrightarrow C(\widehat{\mathbb{Z}}) \hookrightarrow A_{C^*}$ (isometrisch, via NEU-216); $A_{\mathrm{alg}} \subseteq \mathcal{A}^{\log}$; damit $\mathfrak{M}_{\mathrm{glob}}^{\log} \subseteq \mathcal{A}^{\log} \subseteq A_{C^*}$ (217.E).

Die $\Gamma$-Gradierung ($\Gamma = \mathbb{Q}_{>0}^\times$, multiplikative Gradgruppe) ist implizit durch die Homogenität der Erzeuger $\mu_u\xi\mu_v^*$ mit Grad $u/v$ gegeben; $M_h$ bezeichnet die homogene Komponente vom Grad $h$.

### 3.2 Landung auf Generatoren — direkter Bezug zu NEU-211

Die Tabelle in [O-217-2c-6c] ("Landung auf Generatoren, Leibnizschluss") verwendet **wortgetreu** die NEU-211-Formeln:

| Generator | $D_g$-Wert | Quelle | Liegt in |
|---|---|---|---|
| $\mu_k$ | $\mu_u G_{a,d}\mu_v^*$ | **NEU-211** | $(\mathfrak{M}_{\mathrm{glob}}^{\log})_g$ |
| $\mu_k^*$ | $-\mu_{u'}G_{a',d'}\mu_{v'}^*$ | **NEU-211** | $(\mathfrak{M}_{\mathrm{glob}}^{\log})_g$ |
| $e(r)$ | neutraler Charakterkoeffizient $\in B_{\mathrm{alg}}$ | Charakterabsorption | $B_{\mathrm{alg}} \subseteq M_{\mathrm{glob}}^{\log}$ |

Die explizit in NEU-211 bewiesenen Formeln (211.C):
$$
D_g(e(r)) = 0,\quad D_g(\mu_k) = \mu_{mk_0}G_{k_0,d}\mu_{n_0}^*,\quad D_g(\mu_k^*) = -\mu_{m_0}G_{k_1,e}\mu_{nk_1}^*
$$
sind **identisch** die Werte, die in [O-217-2c-6c] als "Quelle: NEU-211" tabelliert werden. **Es handelt sich um dieselbe Derivation, nicht um eine Neudefinition mit gleichem Symbol.** Die $G_{a,d}$-Elemente wurden zuvor in NEU-216 als Elemente von $\mathcal{B}^{\log}$ etabliert (216.1), und in [O-217-2c-6b-def] explizit in $M_{\mathrm{glob},G}^{\log} \subseteq M_{\mathrm{glob}}^{\log}$ aufgenommen (Bedingung „$G_{k,d} \in N$" in der definierenden Schnittfamilie $\mathscr{C}$).

### 3.3 Schlussformel [O-217-2c-6c]

$$
\boxed{D_g(A_{\mathrm{alg}}) \subseteq \left(\mathfrak{M}_{\mathrm{glob}}^{\log}\right)_g, \qquad D_g \in Z^1\!\left(A_{\mathrm{alg}},\,\mathfrak{M}_{\mathrm{glob}}^{\log}\right)_g.} \tag{217.4}
$$

Der Beweis verläuft über Erzeugung von $A_{\mathrm{alg}}$ durch $\{e(r),\mu_k,\mu_k^*\}$ und die Leibnizregel (Bimodulschluss): Da jeder Generator gemäß der Tabelle landet und $\mathfrak{M}_{\mathrm{glob}}^{\log}$ als $A_{\mathrm{alg}}$-Bimodul unter Multiplikation abgeschlossen ist (Definition 217.3), überträgt sich die Landung via Leibnizregel auf beliebige Produkte.

### 3.4 Stabilität und Gradkompatibilität

- **Stabilität unter Links-/Rechtsmultiplikation:** Direkt aus Definition (217.3), $\mathfrak{M}_{\mathrm{glob}}^{\log} = \operatorname{span}_{\mathrm{fin}}\{a\xi b\}$ ist per Konstruktion ein $A_{\mathrm{alg}}$-Bimodul. \checkmark[M]
- **$\sigma_n$-, $\rho_n$-Stabilität von $M_{\mathrm{glob}}^{\log}$:** [O-217-2c-6b-stab] ✓[M], via Transportformel (G1) $\sigma_n(G_{k,d}) = G_{nk/\delta,d/\delta} - \rho_{d/\delta}(G_{n/\delta,1})$, rechte Seite liegt in $M_{\mathrm{glob},G}^{\log}$ per Konstruktion.
- **Gradkonvention** $\deg D_g(a_h) = gh$: Folgt aus (211.8) in NEU-211 ($D_g((A_{\mathrm{alg}})_h) \subseteq (A_{C^*})_{gh}$) und der Homogenitätserhaltung der Einbettung $\mathfrak{M}_{\mathrm{glob}}^{\log} \subseteq A_{C^*}$. \checkmark[M] (konsistent, keine Umdefinition der Gradkonvention).

---

## 4. Identitätsprüfung der Derivation

Die in NEU-217 mit $D_g$ bezeichnete Abbildung ist explizit dieselbe wie in NEU-211: Die Tabelle in [O-217-2c-6c] zitiert die Werte **wörtlich als "Quelle: NEU-211"**, nicht als neue Konstruktion. Zudem verwendet [O-217-2c-6d] (Normdivergenzbeweis) explizit die NEU-211-Fallzerlegung $D_g(\mu_{p^r}) = \mu_{u_r}G_{p^{a_r},p^{b_r}}\mu_{v_r}^*$ und beruft sich in einem "zweiten Beweis" direkt auf NEU-211 [O-211-4] zur Nichtinnerheit. Dies bestätigt Identität, nicht Neukonstruktion. \checkmark[M]

---

## 5. Entscheidung

| Prüfpunkt | Befund |
|---|---|
| $\mathcal{A}^{\log}$ definiert (NEU-216) | \checkmark[M] |
| $\mathfrak{M}_{\mathrm{glob}}^{\log}$ definiert, $\Gamma$-graduiert (NEU-217) | \checkmark[M] |
| NEU-211-Generatorwerte landen in $(\mathfrak{M}_{\mathrm{glob}}^{\log})_g$ | \checkmark[M] (Tabelle [O-217-2c-6c], Quelle explizit NEU-211) |
| Bimodulstabilität unter $A_{\mathrm{alg}}$ | \checkmark[M] |
| $\sigma_n$-, $\rho_n$-Stabilität | \checkmark[M] |
| Gradkompatibilität $\deg D_g(a_h) = gh$ | \checkmark[M] |
| Identität der Derivation NEU-211 = NEU-217 | \checkmark[M] (explizite Quellenzuordnung, keine Neudefinition) |
| Globale Nichtinnerheit $[D_g] \neq 0$ in $HH^1(A_{\mathrm{alg}}, \mathfrak{M}_{\mathrm{glob}}^{\log})_g$ | \checkmark[M] ([O-217-2c-6d], zwei unabhängige Beweise) |

**Ergebnis: Fall A.**

$$
\boxed{D_g(A_{\mathrm{alg}}) \subseteq \mathfrak{M}_{\mathrm{glob}}^{\log}, \qquad D_g\bigl((A_{\mathrm{alg}})_h\bigr) \subseteq M_{gh}.}
$$

$$
\boxed{[O\text{-}219\text{-}5e1j\text{-Dg-global-target}] \quad \checkmark[M].}
$$

---

## 6. Auflösung des scheinbaren Widerspruchs zu NEU-219x

Kein Widerspruch: NEU-219x hat korrekt festgestellt, dass **NEU-211 allein** kein $D_g(A_{\mathrm{alg}}) \subseteq M_g$ beweist — NEU-211 endet explizit mit dem offenen Flaschenhals [O-211-6]. Der vorliegende Audit zeigt, dass dieser Flaschenhals **später**, in NEU-216 (Konstruktion von $\mathcal{B}^{\log}$, $\mathcal{A}^{\log}$) und NEU-217 (Konstruktion von $\mathfrak{M}_{\mathrm{glob}}^{\log}$, Landungsnachweis [O-217-2c-6c], Nichtinnerheit [O-217-2c-6d]) **geschlossen** wurde. [O-211-6] bleibt somit korrekt **historisch offen innerhalb von NEU-211**, ist aber **im Gesamt-DAG durch NEU-216/217 geschlossen**. Beide Befunde — NEU-219x ($\checkmark[M]_{\mathrm{neg,Quelle}}$ bezogen auf NEU-211 isoliert) und NEU-219y ($\checkmark[M]$ bezogen auf den Gesamt-DAG) — bleiben nebeneinander gültig und betreffen unterschiedliche Fragen.

---

## 7. Konsequenz: Freigabe für NEU-219z

Da `[O-219-5e1j-Dg-global-target]` \checkmark[M] entschieden ist, ist die Eingangsvoraussetzung für den globalen Cup-Rotationsaudit erfüllt:

$$
\boxed{D_g : A_{\mathrm{alg}} \to \mathfrak{M}_{\mathrm{glob}}^{\log} = M_g \text{ global explizit und wohldefiniert.}}
$$

Der ursprünglich für NEU-219y geplante explizite Vergleich
$$
a_4 D_g(a_0)\Theta^\wedge(a_1,a_2,a_3) \quad\text{gegen}\quad a_0 D_g(a_1)\Theta^\wedge(a_2,a_3,a_4)
$$
wird auf **NEU-219z** verschoben und ist dort **global freigegeben** (nicht nur sektorbeschränkt), da $D_g$ jetzt auf ganz $A_{\mathrm{alg}}$ mit Ziel $M_g \subseteq \mathfrak{M}_{\mathrm{glob}}^{\log}$ explizit bekannt ist.

---

## 8. Gesamtstatus

$$
\boxed{[O\text{-}219\text{-}5e1j\text{-Dg-global-target}] \quad \checkmark[M]}
$$
$$
\boxed{[O\text{-}219\text{-}5e1j\text{-explicit-cup-rotation}] \quad \text{entsperrt; Bearbeitung in NEU-219z}}
$$

Empfohlene Reihenfolge:
$$
\text{NEU-219y (diese Datei, abgeschlossen)} \longrightarrow \text{NEU-219z: expliziter globaler Cup-Rotationsvergleich.}
$$

| Schritt | Datei | Knoten | Status |
|---|---|---|---|
| Zieltypbrücke NEU-211→NEU-217 | NEU-219y | `[O-219-5e1j-Dg-global-target]` | **✓[M]** |
| Globaler Cup-Rotationsaudit | NEU-219z | `[O-219-5e1j-explicit-cup-rotation]` | **freigegeben, offen** |
