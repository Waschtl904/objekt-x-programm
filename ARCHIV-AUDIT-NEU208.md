# Direktaudit NEU-208 — Separierbare Primpotentiale und Refinementstabilität

**Gesamtstatus:** `✓[M]_part`

---

## 1. Auditumfang

Geprüft: NEU-208 vollständig; eindimensionale Schalenkonstruktion aus NEU-204; Bewertungsgitter aus NEU-207; NEU-209 insoweit, wie dort der offene geladene Kopplungsansatz aus NEU-208 geprüft wird; aktuelle Ordnerliste.

NEU-208 ersetzt die nicht refinementstabile radiale Funktion $c(\alpha)=\log(2+|\alpha|_1)$ durch eine Summe unabhängiger eindimensionaler Primkanäle. Der neutrale separierbare Kanal ist **mathematisch stärker als NEU-208 selbst ausweist**: Er liefert eine echte äußere Klasse in $HH^1(A_{\mathrm{alg}},A_{C^*})_1$. Die angegebene Max-Norm ist jedoch falsch, und der naive geladene Kopplungsansatz wird bereits in NEU-209 ausgeschlossen.

---

## 2. DAG-Knoten

| Knoten | Aussage | Status |
|---|---|---|
| [O-208-1] | Radiale Funktion log(2+|α|₁) unter Primrefinement normstabil | `✓[M]_neg` |
| [O-208-2] | Separierbare Primpotentiale X_{F,N}=Σ_{p∈F} X_{p,N_p} | `✓[M]` |
| [O-208-3a] | Neue Primrichtung q∤k verändert [X,μ_k] nicht | `✓[M]` |
| [O-208-3b] | Entsprechende Stabilität für μ_k* und e(r) | `✓[M]` |
| [O-208-4a] | B_{p,a} existiert in B_{C*} mit Norm log((a+2)/2) | `✓[M]` |
| [O-208-4b-old] | Verschiedene Primkanäle orthogonal; Norm von B_k ist Maximum | `×[M]` |
| [O-208-4b] | ‖B_k‖ = Σ_{p∣k} log((v_p(k)+2)/2) | `✓[M]` |
| [O-208-4c] | D:A_alg→A_C* neutrale normunbeschränkte Derivation | `✓[M]` |
| [O-208-HH1-analytic] | [D]≠0 in HH¹(A_alg,A_C*)_1 | `✓[M]` |
| [O-208-algebraic] | D(A_alg)⊂A_alg für den logarithmischen Primkanal | `✓[M]_neg` |
| [O-208-5a] | Naiver geladener separierbarer Sandwichansatz | `✓[M]_neg` |
| [O-208-5b] | Gemeinsam lokalisierte geladene Architektur mit separierbaren Differenzen | `?[O]` |
| [O-charged-HH1-analytic] | Geladene äußere Klasse in HH¹(A_alg,A_C*)_g | `?[O]` |
| [O-charged-HH1-algebraic] | Geladene äußere Klasse in HH¹(A_alg,A_alg)_g | `?[O]` |

---

## 3. Kernfehler in NEU-208

### Fehler 1: Falsche Orthogonalität
NEU-208 behauptet, $B_{p,a}$ und $B_{q,b}$ ($p\neq q$) wirkten auf orthogonalen Teilräumen. **Falsch:** Im Fouriermodell ist $q_{p,j}\cdot q_{q,\ell}\neq 0$; die Träger überlappen.

### Fehler 2: Falsche Normformel
Behauptet: $\|B_k\|=\max_{p\mid k}\log\frac{v_p(k)+2}{2}$

Korrekt:
$$\|B_k\|=\sum_{p\mid k}\log\frac{v_p(k)+2}{2}$$
Diese Formel wird durch Wahl von $x\in\hat{\mathbb{Z}}$ mit $v_p(x)=0$ für alle $p\mid k$ realisiert. Die Normunbeschränktheit ist damit sogar stärker als angegeben.

---

## 4. Stärkster positiver Befund

$$\boxed{[D]\neq 0 \in HH^1(A_{\mathrm{alg}},A_{C^*})_1}$$

Der neutrale separierbare Kanal liefert:
- $D:A_{\mathrm{alg}}\to A_{C^*}$ wohldefinierte neutrale Derivation
- $D(a^*)=-D(a)^*$ (Sternstruktur)
- Normunbeschränktheit bereits auf Primzahlpotenzen: $\|D(\mu_{p^a})\|=\log\frac{a+2}{2}\to\infty$
- Kein Implementierer in $A_{C^*}$ (folgt aus Unbeschränktheit)

---

## 5. Ersetzte Aussagen

- `[O-208-2] ✓[K]` → `✓[M]`
- Normformel Max-Variante → durch Summennorm ersetzt
- „Grenzderivation auf den Generatoren" → präzisiert zu $D:A_{\mathrm{alg}}\to A_{C^*}$ mit $[D]\neq0\in HH^1(A_{\mathrm{alg}},A_{C^*})_1$
- `[O-208-5] ?[O]` → aufgespalten: `[O-208-5a] ✓[M]_neg` (naiver Sandwich) und `[O-208-5b] ?[O]` (allgemeine geladene Architektur)
- „Einzig verbleibender Schritt ist Kopplung" → `⚠[M]`

---

## 6. Neuer präziser Engpass

$$\boxed{\text{Finde eine gemeinsam lokalisierte geladene Singularität, deren Transportdifferenzen dennoch primweise separierbar bleiben.}}$$

**Nächster Auditknoten:** NEU-209 — Singularträger separierbarer Primkanäle und Charakterkern-No-go
