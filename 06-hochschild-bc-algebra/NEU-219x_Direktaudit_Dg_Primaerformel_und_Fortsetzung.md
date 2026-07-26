# NEU-219x — Direktaudit $D_g$: Primärformel und Fortsetzung

**Datei:** `katalog/NEU-219x_Direktaudit_Dg_Primaerformel_und_Fortsetzung.md`  
**DAG-Position:** Nachfolger von NEU-219w; Vorläufer von NEU-219y.  
**Primärer offener Knoten:** `[O-219-5e1j-Dg-explicit]`  
**Gesperrter Knoten:** `[O-219-5e1j-explicit-cup-rotation]`  
**Datum:** 2026-07-24 (Audit-Ergebnis ergnzt)  
**Voraussetzungen:** NEU-211 (vollständig gelesen), NEU-219n, NEU-219r.

---

## 0. Ausgangslage

Der globale Knoten `[O-219-5e1j-explicit-cup-rotation]` verlangt den typkorrekten Vergleich
$$
\Phi_0(a_0,\ldots,a_4) = \varpi_{\beta,\chi}\!\bigl(j_A(a_0)\,j_M(D_g(a_1)\,\Theta^\wedge(a_2,a_3,a_4))\bigr)
$$
mit $(t\Phi_0)(a_0,\ldots,a_4) = \varpi_{\beta,\chi}\!\bigl(j_A(a_4)\,j_M(D_g(a_0)\,\Theta^\wedge(a_1,a_2,a_3))\bigr)$.
Dieser Vergleich benötigt $D_g$ auf **allen** $a_i \in A_{\mathrm{alg}}$ mit Ziel $M_g \subseteq \mathfrak{M}_{\mathrm{glob}}^{\log}$.

---

## 1. Audit-Ergebnis aus NEU-211 (wortgetreu extrahiert)

### 1.1 Generatorformeln (NEU-211, Satz [O-211-3])

Mit $g = m/n$, $d := (n,k)$, $n = dn_0$, $k = dk_0$, $(n_0,k_0) = 1$,  
und $G_{a,d} := \lim_{N\to\infty}(T_a(X_N) - \rho_d(X_N)) \in B_{C^*}$:

$$D_g(e(r)) = 0, \tag{X.1}$$
$$D_g(\mu_k) = \mu_{mk_0}\, G_{k_0,d}\, \mu_{n_0}^*, \qquad d=(n,k),\; n=dn_0,\; k=dk_0, \tag{X.2}$$
$$D_g(\mu_k^*) = -\mu_{m_0}\, G_{k_1,e}\, \mu_{nk_1}^*, \qquad e=(m,k),\; m=em_0,\; k=ek_1. \tag{X.3}$$

Diese Formeln **gelten für alle $k \ge 1$** ohne Einschränkung an $\gcd(k,mn)$. Der nichtteilerfremde Fall $(d > 1)$ ist in der gcd-Zerlegung vollständig enthalten. Reduktion auf den teilerfremden Fall: $d=1 \Rightarrow G_{k,1} = T_k(X_N) - X_N$, identisch mit NEU-210.

**Abdeckung aller $k,m,n$:** \checkmark[M] — vollständig via gcd-Aufspaltung.

### 1.2 Produktregel (NEU-211, Beweis [O-211-3])

Explizit angegeben (NEU-211.C): $D_g$ ist **gleichmäßiger Grenzwert** von Derivationen $\operatorname{ad}(Y_N)$, daher selbst eine Derivation:
$$D_g(ab) = D_g(a)\,b + a\,D_g(b) \quad \forall\, a,b \in A_{\mathrm{alg}}. \tag{X.4}$$
Keine gradierte oder getwistete Variante — die gewöhnliche ungradierte Leibnizregel gilt.

### 1.3 Normalformformel auf $\mu_m f \mu_n^*$

Aus (X.4) mit $f \in B_{\mathrm{alg}} = C_{\mathrm{alg}}(\hat{\mathbb{Z}})$:
$$D_g(\mu_m f \mu_n^*) = D_g(\mu_m)\cdot f\mu_n^* + \mu_m\cdot D_g(f)\cdot\mu_n^* + \mu_m f\cdot D_g(\mu_n^*). \tag{X.5}$$
Da $D_g(e(r)) = 0$ und $f$ algebraische Kombination von $e(r)$:
$$D_g(f) = 0 \quad \forall\, f \in B_{\mathrm{alg}}. \tag{X.6}$$
Damit vereinfacht sich (X.5) zu:
$$D_g(\mu_m f\mu_n^*) = D_g(\mu_m)\cdot f\mu_n^* + \mu_m f \cdot D_g(\mu_n^*). \tag{X.7}$$
Beide Terme in $A_{C^*}$ via (X.2) und (X.3) auswertbar.

**Diese Normalformformel ist vollständig und explizit für alle $f \in B_{\mathrm{alg}}$.**

### 1.4 Relationsaudit — BC-Relationen durch $D_g$ annihiliert?

Dies ist der höchst-informative Konsistenztest. Jede BC-Relation $R = 0$ in $A_{\mathrm{alg}}$ muss
$D_g(R) = 0$ in $A_{C^*}$ implizieren. Da $D_g = \lim_N \operatorname{ad}(Y_N)$ und jedes $\operatorname{ad}(Y_N)$ trivialerweise alle Relationen annihiliert (innere Derivation), folgt durch Grenzübergang in Norm:

**Relation $\mu_m\mu_n = \mu_{mn}$:**
$$D_g(\mu_m\mu_n) = D_g(\mu_m)\mu_n + \mu_m D_g(\mu_n) \stackrel{!}{=} D_g(\mu_{mn}).$$
Beide Seiten sind via (X.2) auswertbar; Gleichheit folgt aus der Multiplikativität der gcd-Zerlegung. \checkmark[M]

**Relation $\mu_n^*\mu_n = 1$:**
$$D_g(\mu_n^*\mu_n) = D_g(\mu_n^*)\mu_n + \mu_n^* D_g(\mu_n) = 0.$$
Direkttest mit $k = n$ in (X.2): $d = (n,n) = n$, $n_0 = 1$, $k_0 = 1$, also
$D_g(\mu_n) = \mu_m G_{1,n}\mu_1^* = \mu_m G_{1,n}$. Mit $e = (m,n)$, $D_g(\mu_n^*) = -\mu_{m_0}G_{n/e,e}\mu_{n \cdot n/e}^*$.
Die Summe $D_g(\mu_n^*)\mu_n + \mu_n^* D_g(\mu_n) = 0$ folgt in $A_{C^*}$ aus dem Grenzargument. \checkmark[M] (per Derivationsargument; direkter Term-Ausgleich in $A_{C^*}$, nicht in $A_{\mathrm{alg}}$)

**Relation $\mu_n\mu_n^* = E_n$:**
$$D_g(E_n) = D_g(\mu_n\mu_n^*) = D_g(\mu_n)\mu_n^* + \mu_n D_g(\mu_n^*). \tag{X.8}$$
Da $E_n = \rho_n(1) \in B_{\mathrm{alg}}$: $D_g(E_n) = 0$ wegen (X.6). Konsistenz erfordert also
$$D_g(\mu_n)\mu_n^* + \mu_n D_g(\mu_n^*) = 0 \in A_{C^*}. \tag{X.9}$$
Gilt in $A_{C^*}$ per Derivationsargument. \checkmark[M]

**Relation $\mu_n e(r)\mu_n^* = \rho_n(e(r))$:**
$$D_g(\mu_n e(r)\mu_n^*) = D_g(\rho_n(e(r))) = 0 \text{ (da }\rho_n(e(r)) \in B_{\mathrm{alg}}\text{)}.$$
Linke Seite $= D_g(\mu_n)e(r)\mu_n^* + \mu_n e(r)D_g(\mu_n^*) = 0$ in $A_{C^*}$. \checkmark[M]

**Kritischer Konsistenztest $D_g(\mu_k^*\mu_k) = 0$:**
$$D_g(\mu_k^*\mu_k) = D_g(\mu_k^*)\mu_k + \mu_k^* D_g(\mu_k) = 0.$$
Mit (X.2) und (X.3): $\mu_k^* D_g(\mu_k) = \mu_k^*\mu_{mk_0}G_{k_0,d}\mu_{n_0}^*$ und $D_g(\mu_k^*)\mu_k = -\mu_{m_0}G_{k_1,e}\mu_{nk_1}^*\mu_k$.
Die Summe ist null in $A_{C^*}$ — **nicht direkt** aus den expliziten gcd-Formeln durch Termkanzellation in $A_{\mathrm{alg}}$, sondern ausschließlich durch das Derivationsargument (Grenzwert innerer Derivationen). Eine **terme-für-terme Kanzellation in $A_{\mathrm{alg}}$ ist in NEU-211 nicht nachgewiesen**.

**BC-Relationen erhalten:** \checkmark[M] via Derivationsargument. Aber: Direkter algebraischer Kanzellationsnachweis fehlt für $D_g(\mu_k^*)\mu_k + \mu_k^* D_g(\mu_k) = 0$ in $A_{\mathrm{alg}}$.

### 1.5 Wohldefiniertheit auf $A_{\mathrm{alg}}$

NEU-211 etabliert Wohldefiniertheit auf $A_{\mathrm{alg}}$ als Derivation (Satz [O-211-3]): Der Grenzwert ist in $\operatorname{Der}(A_{\mathrm{alg}}, A_{C^*})_g$ wohldefiniert. Darstellungsunabhängigkeit folgt daraus direkt. \checkmark[M]

### 1.6 Zieltyp und Reichweite — **kritischer Befund**

NEU-211, Satz [O-211-3] (Formel 211.8) beweist:
$$D_g\bigl((A_{\mathrm{alg}})_h\bigr) \subseteq (A_{C^*})_{gh}. \tag{X.10}$$

NEU-211, Satz [O-211-5] beweist **explizit** (Formel 211.13):
$$D_g(\mu_\ell) \notin A_{\mathrm{alg}} \quad \text{für Primzahlen } \ell \nmid mn. \tag{X.11}$$

Der in NEU-219x benötigte Zieltyp ist $M_g \subseteq \mathfrak{M}_{\mathrm{glob}}^{\log}$, **nicht** $A_{C^*}$. NEU-211 beweist:
$$[D_g] \in HH^1(A_{\mathrm{alg}},\, A_{C^*})_g. \tag{X.12}$$

Die Frage, ob $D_g(A_{\mathrm{alg}}) \subseteq M_g \subseteq \mathfrak{M}_{\mathrm{glob}}^{\log}$, ist in NEU-211 **nicht beantwortet**. NEU-211 benennt [O-211-6] als offenen Flaschenhals: ein intermediares $\mathcal{A}^\infty$ mit
$$A_{\mathrm{alg}} \subsetneq \mathcal{A}^\infty \subsetneq A_{C^*}, \quad D_g(A_{\mathrm{alg}}) \subseteq \mathcal{A}^\infty.$$
Ob $\mathcal{A}^\infty \subseteq M_g$ oder $\mathcal{A}^\infty \supseteq M_g$, bleibt offen. Der Cup-Pfeil nach $HH^4_g$ mit Koeffizient in $M_g$ ist in NEU-211 **nicht konstruiert**.

---

## 2. Entscheidung

| Prüfpunkt | Befund |
|---|---|
| Generatorformeln vollständig für alle $k,m,n$ | \checkmark[M] |
| gcd-Aufspaltung alle Fälle abdeckend | \checkmark[M] |
| Produktregel (ungradiert) explizit | \checkmark[M] |
| Normalformformel $\mu_m f\mu_n^*$ | \checkmark[M] |
| BC-Relationen erhalten (Derivationsargument) | \checkmark[M] |
| Direkter Kanzellationsnachweis in $A_{\mathrm{alg}}$ | $\triangle$ (nur in $A_{C^*}$ per Grenzwert) |
| Darstellungsunabhängigkeit | \checkmark[M] |
| Zieltyp $D_g: A_{\mathrm{alg}} \to A_{C^*}$ | \checkmark[M] |
| Zieltyp $D_g(A_{\mathrm{alg}}) \subseteq M_g \subseteq \mathfrak{M}_{\mathrm{glob}}^{\log}$ | **nicht nachgewiesen** |
| $D_g(A_{\mathrm{alg}}) \subseteq A_{\mathrm{alg}}$ | \checkmark[M]$_{\mathrm{neg}}$ (NEU-211.E) |
| $[D_g] \in HH^1(A_{\mathrm{alg}}, A_{C^*})_g$ | \checkmark[M] |

**Ergebnis:**

$$\boxed{[O\text{-}219\text{-}5e1j\text{-Dg-explicit}] \quad \checkmark[M]_{\mathrm{neg,Quelle}}}$$

Begründung: Der benötigte Zieltyp $D_g: A_{\mathrm{alg}} \to M_g \subseteq \mathfrak{M}_{\mathrm{glob}}^{\log}$ ist in NEU-211 **weder behauptet noch bewiesen**. Die nachgewiesene Abbildung landet in $A_{C^*}$, und der Weg zu einem intermediaren Modul $\mathcal{A}^\infty$ ist als [O-211-6] **explizit offen**. Eine Zieltypbrücke $\mathcal{A}^\infty \leftrightarrow M_g$ fehlt vollständig.

Dies ist **kein Fehler in NEU-211** — NEU-211 löst präzise die Fragen, die es stellen wollte. Die Zieltypbrücke ist strukturell der nächste Engpass.

---

## 3. Konsequenz für NEU-219y

Da `[O-219-5e1j-Dg-explicit]` mit $\checkmark[M]_{\mathrm{neg,Quelle}}$ entschieden ist:

$$\boxed{[O\text{-}219\text{-}5e1j\text{-explicit-cup-rotation}] \text{ bleibt gesperrt.}}$$

NEU-219y **kann nicht** den globalen Cup-Rotationsvergleich durchführen. Der Vorgänger-Pfad lautet:

$$\text{Zieltypbrücke } \mathcal{A}^\infty \leftrightarrow M_g
\;\longrightarrow\; D_g: A_{\mathrm{alg}} \to M_g
\;\longrightarrow\; \text{NEU-219y global freigegeben.}$$

Bis zur Schließung von [O-211-6] + Identifikation $\mathcal{A}^\infty \supseteq M_g$:

- Falls eine **Generatorsektorversion** genügt (d.h. nur $a_i \in \{\mu_k, \mu_k^*, e(r)\}$), kann NEU-219y als **partieller Sektortest** formuliert werden, da auf diesen Generatoren $D_g(\mu_k) \in A_{C^*}$ und $M_g \cap A_{C^*}$ ggf. genügt.
- Der **globale** Cup-Rotationstest auf $A_{\mathrm{alg}}$ bleibt bis zur Typbrücke gesperrt.

---

## 4. Voraussetzungsabgleich NEU-219n / NEU-219r (unverändert)

Die in \S2 der ursprünglichen Rahmendatei fixierten Eingaben aus NEU-219n und NEU-219r
($\varpi_{\beta,\chi}$, Modulgewichtsrelation, $\eta_0$, $\Pi_0 \circ \eta_0 = \iota_{M_0\hookrightarrow N_0}$, skalare Auswertungskette)
bleiben vollständig gültig und gelten als vorausgesetzt.

---

## 5. Gesamtstatus

$$\boxed{[O\text{-}219\text{-}5e1j\text{-Dg-explicit}] \quad \checkmark[M]_{\mathrm{neg,Quelle}} \quad (\text{Zieltyp }A_{C^*}\neq M_g)}$$

$$\boxed{[O\text{-}219\text{-}5e1j\text{-explicit-cup-rotation}] \quad \text{gesperrt bis Zieltypbrücke [O-211-6]}}$$

Empfohlene Reihenfolge:
$$\text{[O-211-6]: } \mathcal{A}^\infty \longrightarrow \text{Identifikation } \mathcal{A}^\infty \supseteq M_g \longrightarrow D_g: A_{\mathrm{alg}} \to M_g \longrightarrow \text{NEU-219y}.$$
