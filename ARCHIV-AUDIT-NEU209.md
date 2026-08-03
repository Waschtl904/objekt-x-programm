# Direktaudit NEU-209 — Singulärer Träger separierbarer Primkanäle und Charakterkern-No-go

**Gesamtstatus: ✓[M]_part**

---

## Auditumfang

Geprüft wurden:
- `NEU-209_Singulartraeger_Separierbarer_Primkanaele_und_Charakterkern_NoGo.md` vollständig.
- Die separierbaren Primpotentiale aus NEU-208.
- Die geladenen Sandwichformeln aus NEU-205/206.
- NEU-210 unmittelbar hinsichtlich der dort behaupteten Schließung von `[O-209-5]` und `[O-209-6]`.
- Die aktuelle Ordnerstruktur.

NEU-209 weist korrekt nach, dass die einzelnen separierbaren Primkanäle auf großen Koordinatenhyperflächen `K_p` singulär werden und dass diese Singularität von geeigneten Charakterfehlermultiplikatoren gesehen wird. Der daraus abgeleitete No-go gegen den naiven geladenen Sandwichansatz ist belastbar.

---

## Interpretationsfreier Primärextrakt

NEU-209 definiert die normalisierten Primkanäle `\widetilde X_{p,N}=X_{p,N}-c_0\,1` und die Koordinatenhyperfläche

\[
K_p=\bigcap_{N\ge 0} p^N\widehat{\mathbb Z}=\{x\in\widehat{\mathbb Z}:x_p=0\}.
\]

Die Datei behauptet: Auf `K_p` divergiert `\widetilde X_{p,N}` wie `c_N-c_0\to\infty`. Für einen lokal konstanten Multiplikator `M`, der über einen zu `p` teilerfremden Modul `L` faktorisiert, soll `\|M|_{K_p}\|=\|M\|` gelten. Daraus wird der naive geladene Ansatz

\[
\mu_m\left(\sum_{p\in F} \widetilde X_{p,N_p}\right)\mu_n^*
\]

ausgeschlossen. Anschließend definiert die Datei

\[
Z_g:=\bigcap_{r\in\mathbb Q/\mathbb Z} Z(M_{g,r})
\]

und vermutet zunächst `Z_g=\{0\}`. Als neuen Kandidaten schlägt sie schließlich ein bei `0` konzentriertes Potential auf Basis von `E_{\operatorname{lcm}(1,\ldots,N)}` vor.

---

## Kernbefunde

### Belastbare Resultate

| Knoten | Aussage | Status |
|---|---|---|
| [O-209-1a] | `\widetilde X_{p,N}|_{K_p}=c_N-c_0\to\infty` | ✓[M] |
| [O-209-1b] | `\operatorname{Sing}(\widetilde X_p)=K_p` punktweise | ✓[M] |
| [O-209-2] | `p\nmid L \Rightarrow \|M|_{K_p}\|=\|M\|` und `\|M\widetilde X_{p,N}\|\to\infty` | ✓[M] |
| [O-209-4a] | `Z_g=\bigcap_r Z(M_{g,r})` als geschlossene Untergruppe | ✓[M] |
| [O-209-5] | `Z_g=\{0\}` für `g\neq 1` | ✓[M] |
| [O-209-6b] | Ursprungspotential mit konvergenten Transportdifferenzen und konvergentem `M_{g,r}X_N` | ✓[M] durch NEU-210 |
| Normgleichheit im Sandwich | `\|\mu_m b\mu_n^*\|=\|b\|` | ✓[M] |

### Widerlegte Resultate

| Knoten | Aussage | Status |
|---|---|---|
| [O-209-3] | Naiver positiver separierbarer Sandwichansatz | ✓[M]_neg |
| [O-209-separable-necessary] | `\mu_k`-Konvergenz erzwingt primweise Separierbarkeit | ×[M] |
| [O-209-tail] | `X_N=f(N)E_{\mathrm{lcm}(1,\ldots,N)}` besitzt konvergente `\mu_k`-Kommutatoren | ×[M] |

### Offene Knoten

| Knoten | Aussage | Status |
|---|---|---|
| [O-209-4b] | Positive lokal gleichmäßige Singularität muss in `Z_g` liegen | ✓[K/M] |
| [O-209-4c] | Allgemeiner Singularträgerzwang für beliebige Approximationen | ?[O] |
| [O-209-6a] | Starke Absorption `M_{g,r}X_N\to 0` für alle `r` | ?[O] |
| [O-210-generator] | Vollständiger geladener Generatoraudit | ?[O] |
| [O-charged-HH1-analytic] | `[D_g]\neq 0` in `HH^1(A_{alg},A_{C^*})_g` | ?[O] |
| [O-charged-HH1-algebraic] | `[D_g]\neq 0` in `HH^1(A_{alg},A_{alg})_g` | ?[O] |

---

## Ersetzte Aussagen

1. **Status von `Z_g`:** Statt `?[O]` gilt `✓[M]`; exakt ist `Z_g=\{0\}`.
2. **Separierbarkeit:** Zu stark war `\mu_k`-Sektor verlangt Separierbarkeit. Korrekt ist: Der `\mu_k`-Sektor verlangt kontrollierte Transportdifferenzen; Separierbarkeit und beschränkte Transportbänder sind zwei verschiedene Realisationsmöglichkeiten.
3. **Ursprungskandidat:** Der reine Tailkandidat `X_N=f(N)E_{\mathrm{lcm}(1,\ldots,N)}` ist falsch als Isometrie-kontrollierter Kandidat. Tatsächlich gilt `\|[X_N,\mu_k]\|=|f(N)|` für jedes feste `k>1` und hinreichend große `N`.
4. **Charakterabsorption:** Zu stark ist `M_{g,r}X_N\to 0`. Für den Bau der Derivation genügt, dass `M_{g,r}X_N` norm-Cauchy ist beziehungsweise konvergiert; NEU-210 erreicht sogar eventuelle Konstanz.

---

## Beitrag zu Objekt X

NEU-209 liefert einen präzisen geometrischen Ausschluss: Unabhängige positive Prim-Singularitäten sind mit einer geladenen Charakterkopplung nicht vereinbar. Außerdem ist der gemeinsame Nullträger exakt `Z_g=\{0\}`.

Damit wird die Suchgeometrie erheblich präzisiert: Eine positive, lokal divergente geladene Potentialroute muss ihre unbeschränkte Masse am globalen Ursprung konzentrieren. Der reine Tailkandidat der Datei scheitert aber; der korrekte nächste Schritt ist nicht bloß Lokalisierung bei `0`, sondern `Lokalisierung bei 0 + gesättigte Schalen + gleichmäßig beschränktes Transportband`.

**Nächster Direktaudit:** NEU-210 — Faktorielle Ursprungssingularität, Transportband und Charakterabsorption.
