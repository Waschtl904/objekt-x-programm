# Direktaudit NEU-210 — Faktorielle Ursprungssingularität, Transportband und Charakterabsorption

**Gesamtstatus: ✓[M]_part**  
**Auditdatum:** 2026-08-03  
**Auditiert von:** Chat-Session (Perplexity/Akademisch)  
**Commit-Basis:** 9debed0 (Import, 2026-07-26)  
**Vorgänger-Audit:** ARCHIV-AUDIT-NEU209.md

---

## Auditumfang

Geprüft wurden:
- `NEU-210_Faktoriale_Ursprungssingularitaet_Transportband_und_Charakterabsorption.md` vollständig.
- Rückbezug auf NEU-209-Forderungskatalog (drei Anforderungen an den Potentialtyp).
- Normgeometrie der Folge `(X_N)` und des geladenen Implementierers `(Y_N)`.
- Transportband-Definitionsbereich.
- Charakterabsorptionseigenschaft: Stabilisierung vs. Verschwinden.

---

## Interpretationsfreier Primärextrakt

NEU-210 definiert:
$$L_j = (j+1)!, \quad P_j = E_{L_j}, \quad q_j = P_j - P_{j+1},$$
$$X_N = \sum_{j=0}^{N-1} c_j q_j + c_N P_N, \quad c_j = \log(j+2).$$

Die Teleskopformel lautet:
$$\sum_{j=0}^{N-1} q_j + P_N = P_0 = 1.$$

Das punktweise Profil ist:
$$X_N(x) = c_{\min(\nu(x), N)}, \quad x \neq 0; \qquad X_N(0) = c_N \to \infty.$$

---

## Kernbefunde

### Belastbare Resultate

| Knoten | Aussage | Status |
|---|---|---|
| [O-210-1] | $Z_g = \{0\}$ für $g \neq 1$; Beweis via Torfreiheit von $\hat{\mathbb{Z}}$ | ✓[M] |
| [O-210-2] | Faktorielle Schalenfolge orthogonal und vollständig; $X$ als erweitertes Punktprofil | ✓[K/M] |
| [O-210-3] | Neutrale Kommutatoren $[X_N, \mu_k] \to \mu_k B_k$ in Norm (für $j \geq k$) | ✓[M]_part |
| [O-210-4a] | $M(0)=0 \Rightarrow MX_N$ schließlich exakt konstant | ✓[M] |
| [O-210-5] | Geladene Kommutatoren im teilerfremden $\mu_k$-Sektor normkonvergent | ✓[M]_part |

### Widerlegte Resultate

| Knoten | Aussage | Status |
|---|---|---|
| [O-210-4b] | $M_{g,r}X_N \to 0$ in Norm | ×[M] |

**Gegenbeispiel:** $m=2, n=1, r=\tfrac{1}{2}$. Dann $M_{2,1;1/2} = e(\tfrac{1}{2})-1$, dieser Multiplikator verschwindet auf $2\hat{\mathbb{Z}}$, nicht aber auf der ungeraden Restklasse. Mit $q_0 = 1 - E_2$ gilt $M_{2,1;1/2} q_0 = M_{2,1;1/2} \neq 0$, also
$$\lim_N M_{2,1;1/2} X_N = c_0 \cdot M_{2,1;1/2} \neq 0.$$

### Offene Knoten

| Knoten | Aussage | Status |
|---|---|---|
| [O-210-6a] | Vollständiger nichtteilerfremder Generatoraudit | ?[O] |
| [O-210-6b] | Nichtinnerheit in $A_{C^*}$ | ?[O] |
| [O-210-6c] | Algebraischer/intermediärer Zieltyp und Cup-Brücke | ?[O] |

---

## Ersetzte / korrigierte Aussagen

1. **[O-209-6] Aufspaltung:** Die in NEU-209 geforderte dritte Anforderung $M_{g,r}X_N \to 0$ wird durch NEU-210 **nicht** erfüllt. Korrekte Aufspaltung:
   - [O-209-6a] Ursprungslokalisierung $\operatorname{Sing}(X) = \{0\}$ → ✓[K/M]
   - [O-209-6b] Transportdifferenzen normkonvergent → ✓[M]
   - [O-209-6c] $M_{g,r}X_N \to 0$ → ×[M]
   - [O-209-6d] $M_{g,r}X_N$ schließlich konstant → ✓[M]

2. **Bandformel-Einschränkung:** Die Formel
   $$P_j \leq T_k(P_j) = E_{L_j/k} \leq P_{j-k}$$
   gilt nur für $j \geq k$. Für $j < k$ ist $P_{j-k}$ undefiniert. Die endlich vielen Anfangsschalen sind für die Normkonvergenz irrelevant.

3. **Normgeometrie (in Datei nicht explizit):** Aus der Teleskopzerlegung folgt:
   $$\|X_M - X_N\| = c_M - c_N = \log\frac{M+2}{N+2}.$$
   Damit ist $(X_N)$ nicht norm-Cauchy. Ebenso $\|Y_M - Y_N\| = c_M - c_N$, da $\|\mu_m b \mu_n^*\| = \|b\|$.

4. **Charakterabsorption — Terminologie:** Der Begriff "Absorption" in NEU-210 meint nur Entfernung des singulären Tails (eventuelle Konstanz), **nicht** Annihilation. Die schwächere, tatsächlich benötigte Eigenschaft ist vollständig bewiesen.

5. **NEU-222-Statusübernahme zu stark:** NEU-222 übernimmt [O-209-6] als vollständig geschlossen. Dies ist unzulässig, da [O-209-6c] ×[M] ist.

---

## Beitrag zu Objekt X

NEU-210 liefert die gesättigte faktorielle Schalenarchitektur als Ersatz für den gescheiterten reinen Tail-Kandidaten. Die Suchgeometrie ist nun präzise:
- Singularität ausschließlich bei $\{0\}$ — ✓[K/M]
- Gleichmäßig beschränktes Transportband — ✓[M]_part
- Eventuelle Konstanz der Charakterkommutatoren (nicht Verschwinden) — ✓[M]

Der fehlende adjungierte teilerfremde Sektor und der vollständige nichtteilerfremde Generatoraudit gehen an NEU-211.

**Nächster Direktaudit:** NEU-211 — Nichtteilerfremder Faktorialaudit, Geladene Äußere Derivation.
