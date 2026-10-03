# Direktaudit NEU-211 — Nichtteilerfremder Faktorialaudit, Geladene Äußere Derivation

**Gesamtstatus: ✓[M]_part**  
**Auditdatum:** 2026-08-03  
**Auditiert von:** Chat-Session (Perplexity/Akademisch)  
**Vorgänger-Audit:** ARCHIV-AUDIT-NEU210.md

---

## Auditumfang

Geprüft wurden:
- `NEU-211_Nichtteilerfremder_Faktorialaudit_Geladene_Aeussere_Derivation.md` vollständig.
- Nica-Formel und gcd-Zerlegung für $\mu_n^* \mu_k$.
- Normkonvergenz des gemischten Transportdefekts $T_a(X_N) - \rho_d(X_N)$.
- Definition $D_g(e(r)) := 0$ — auf BC-Kreuzrelations-Kompatibilität.
- Nichtinnerheitsbeweis via Offdiagonaltest.
- Algebraischer Zieltyp.
- Hochschild-Klasse.

---

## Interpretationsfreier Primärextrakt

NEU-211 setzt $Y_N = \mu_m X_N \mu_n^*$ und leitet für $d = (n,k)$, $n = dn_0$, $k = dk_0$, $(n_0,k_0)=1$ ab:
$$\mu_n^* \mu_k = \mu_{k_0} \mu_{n_0}^*.$$
Daraus folgen die exakten Kommutatorformeln:
$$[Y_N, \mu_k] = \mu_{mk_0}(T_{k_0}(X_N) - \rho_d(X_N))\mu_{n_0}^*,$$
$$[Y_N, \mu_k^*] = -\mu_{m_0}(\rho_e(X_N) - T_{k_1}(X_N))\mu_{nk_1}^*, \quad e = (m,k).$$

---

## Kernbefunde

### Belastbare Resultate

| Knoten | Aussage | Status |
|---|---|---|
| [O-211-1] | Nichtteilerfremde Nica-/gcd-Formeln exakt | ✓[M] |
| [O-211-2] | $G_{a,d;N} \to G_{a,d}$ in Norm; Grenzwertfunktion explizit | ✓[M] |
| [O-211-3corr] | $D_g^{\mathrm{corr}}$ mit korrekter Charakterwirkung ist geladene Derivation $A_{\mathrm{alg}} \to A_{C^*}$ | ✓[M] |
| [O-211-4corr] | Nichtinnerheit via Offdiagonaltest: $\langle \delta_{mt}, (W-T)\delta_{nt}\rangle = c_{\nu(t)} \to \infty$ | ✓[M] |
| **[O-charged-HH1-analytic]** | $[D_g^{\mathrm{corr}}] \neq 0$ in $HH^1(A_{\mathrm{alg}}, A_{C^*})_g$ | **✓[M]** |
| [O-211-5a] | $D_g^{\mathrm{corr}}(A_{\mathrm{alg}}) \not\subseteq A_{\mathrm{alg}}$ — konkreter Kandidat nicht algebraisch-wertig | ✓[M]_neg |

### Widerlegte Resultate (geschriebene Fassung)

| Knoten | Aussage | Status |
|---|---|---|
| [O-211-3] geschrieben | $D_g(e(r)) := 0$ — verletzt BC-Kreuzrelation | ×[M] |
| [O-211-4] geschrieben | Nichtinnerheitsschluss auf Basis der falschen Charaktersetzung | ×[M] |

### Offene Knoten

| Knoten | Aussage | Status |
|---|---|---|
| [O-charged-HH1-algebraic] | Geladene äußere Klasse in $HH^1(A_{\mathrm{alg}}, A_{\mathrm{alg}})_g$ | ?[O] |
| [O-211-6] | Intermediäres Koeffizientenmodul und Cup-Brücke | ?[O] |

---

## Ersetzte / korrigierte Aussagen

### 1. Kritischer Fehler: $D_g(e(r)) := 0$ — ×[M]

NEU-210 hat bewiesen: $\lim_N [Y_N, e(r)] = \mu_m C_{m,n;r} \mu_n^*$ mit
$$C_{m,n;r} = \lim_N M_{m,n;r} X_N = \sum_{j=0}^{J(r)-1} c_j M_{m,n;r} q_j \in B_{\mathrm{alg}}.$$
Insbesondere ist $C_{m,n;r}$ im Allgemeinen **nicht** null.

**Expliziter Gegenbeweis:** Wähle $m=2$, $n=1$, $g=2$, $k=2$, $r=\tfrac{1}{4}$. Die BC-Relation $e(\tfrac{1}{4})\mu_2 = \mu_2 e(\tfrac{1}{2})$ liefert bei Annahme $D_g(e(r))=0$:
$$e(\tfrac{1}{4}) D_g(\mu_2) - D_g(\mu_2) e(\tfrac{1}{2}) = 0.$$
Mit $D_g(\mu_2) = \mu_4 B_2$ und $B_2(1) = \log\tfrac{3}{2}$, $e(\tfrac{1}{2})(1) = -1$:
$$\mu_4 B_2(1 - e(\tfrac{1}{2})) \ni \mu_4 B_2(1) \cdot 2 = 2\log\tfrac{3}{2} \neq 0.$$
Damit ist die in NEU-211.C definierte Abbildung **keine** Derivation.

### 2. Korrekte geladene Derivation — ✓[M]

$$D_g^{\mathrm{corr}}(e(r)) := \mu_m C_{m,n;r} \mu_n^*,$$
$$D_g^{\mathrm{corr}}(\mu_k) := \mu_{mk_0} G_{k_0,d} \mu_{n_0}^*,$$
$$D_g^{\mathrm{corr}}(\mu_k^*) := -\mu_{m_0} G_{k_1,e} \mu_{nk_1}^*.$$

Dies sind exakt die Normgrenzwerte $\lim_N [Y_N, a]$ auf allen drei Generatorfamilien. Leibniz-Regel folgt aus $[Y_N, ab] = [Y_N,a]b + a[Y_N,b]$ und Normkonvergenz jedes Summanden.

### 3. Nichtinnerheitsbeweis — nach Korrektur ✓[M]

Der Offdiagonaltest in NEU-211.D ist für $D_g^{\mathrm{corr}}$ gültig: Mit $W = \pi(\mu_m) H \pi(\mu_n)^*$, $H\delta_t = c_{\nu(t)}\delta_t$, und einem hypothetischen Implementierer $T = \pi(x)$ folgt aus $[W-T, \pi(e(r))]=0$ für alle $r$, dass $W-T$ diagonal ist. Daher:
$$\langle \delta_{mt}, (W-T)\delta_{nt}\rangle = c_{\nu(t)} = c_j \to \infty$$
für $t = L_j = (j+1)!$. Dies widerspricht der Beschränktheit jedes $T \in A_{C^*}$.

**Hinweis:** Der originale Beweis in NEU-211.D zieht aus $D_g(e(r))=0$ den Schluss $[W-T, e(r)]=0$. Dieser Schluss ist für die *falsche* Derivation unzulässig, für $D_g^{\mathrm{corr}}$ aber korrekt, weil $[W, \pi(e(r))] = \pi(D_g^{\mathrm{corr}}(e(r)))$ genau den Charakterkommutator realisiert.

### 4. Algebraischer Zieltyp — ✓[M]_neg (Umfangsklausel)

Für $\ell \nmid mn$ prim: $B_\ell \notin B_{\mathrm{alg}}$ (stetig bei 0, aber in keiner Umgebung lokal konstant). Daher $D_g^{\mathrm{corr}}(A_{\mathrm{alg}}) \not\subseteq A_{\mathrm{alg}}$.

**Umfangsklausel:** Ausgeschlossen ist nur der algebraische Zieltyp für den konkreten faktoriellen Kandidaten. Die allgemeine Frage $[D] \neq 0$ in $HH^1(A_{\mathrm{alg}}, A_{\mathrm{alg}})_g$ bleibt offen: **[O-charged-HH1-algebraic] ?[O]**.

### 5. Konsequenz für NEU-212

NEU-212 setzt erneut $\widetilde{D}_g(e(r)) := 0$ (212.C). Diese Setzung erbt den ×[M]-Befund aus NEU-211. Die korrekte Formel für die regularisierte Derivation lautet:
$$\widetilde{D}_g(e(r)) = \mu_m \widetilde{C}_{m,n;r} \mu_n^*, \quad \widetilde{C}_{m,n;r} = \frac{C_{m,n;r}}{\log(\nu(\cdot)+2)}.$$

Zusätzlich ist die Behauptung in NEU-212.B
$$\frac{(j+1)^k}{(j+2)\log(j+2)} \to 0 \quad \text{für alle } k$$
falsch: für $k \geq 2$ divergiert der Ausdruck wie $j^{k-1}/\log j$. Damit ist [O-212-2] in seiner geschriebenen Fassung ×[M].

---

## Hauptbuchungsposten dieses Audits

$$\boxed{[O\text{-charged-HH1-analytic}] \quad \checkmark[M]}$$

$$[D_g^{\mathrm{corr}}] \neq 0 \quad \text{in} \quad HH^1(A_{\mathrm{alg}}, A_{C^*})_g, \qquad g \neq 1.$$

Dies ist der erste vollständig gesicherte positive Hochschild-Klassen-Befund im geladenen Sektor des Programms.

---

## Beitrag zu Objekt X

**Positiver Kernbefund:** Eine geladene, nicht-innere analytische Derivation $D_g^{\mathrm{corr}} : A_{\mathrm{alg}} \to A_{C^*}$ ist konstruiert und ihre Kohomologieklasse ist nichttrivial.

**Verbleibende Lücken:**
- $A_{C^*}$-wertiger Zieltyp, kein $A_{\mathrm{alg}}$-wertiger Kandidat (✓[M]_neg für konkreten Fall)
- Intermediäres Modul $\mathcal{A}^\infty$ und Nichtinnerheit darin (?[O])
- Cup-Aufstieg nach $HH^4$ (?[O])
- Algebraische geladene Klasse (?[O])

**Nächster Direktaudit:** NEU-212 — Zieltypbrücke, Intermediäres Koeffizientenmodul $\mathcal{A}^\infty$.
