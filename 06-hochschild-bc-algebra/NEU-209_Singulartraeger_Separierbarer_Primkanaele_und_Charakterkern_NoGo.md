# NEU-209 — Singularträger separierbarer Primkanäle und Charakterkern-No-go

**Status:** [O-209-1] ✓[M], [O-209-2] ✓[M], [O-209-3] ✓[M]_neg, [O-209-4] ✓[K]; [O-209-5], [O-209-6] ?[O]  
**Erstellt:** 2026-07-20  
**Vorgänger:** NEU-208 ([O-208-5] ?[O] — Kopplung an geladene Charakterkerne offen)  
**Ziel:** Nachweis der Singularitätsmengen separierbarer Primkanäle; Ausschluss des naiven Sandwichansat­zes; Definition der gemeinsamen Charakterkernmenge $Z_g$ als neuer zentraler Begriff

---

## 209.0 — Ausgangslage

NEU-208 hat den neutralen separierbaren Kanal
$$X_{F,\mathbf N} = \sum_{p \in F} X_{p,N_p}$$
konstruiert und dessen Refinementstabilität für alle $\mu_k$-Kommutatoren bewiesen. Der offene Kopplungsschritt [O-208-5] verlangt, diesen Kanal mit den geladenen Charakterkern-Partialisometrien $w_{F,\alpha} = \mu_m Q_{F,\alpha}\mu_n^*$ aus NEU-206 zu verbinden.

NEU-209 zeigt, dass dieser naive Ansatz scheitert, und identifiziert präzise, warum: Die separierbaren Primkanäle tragen ihre Singularität auf Koordinatenhyperflächen $K_p$, die für die Charakterfehlermultiplikatoren sichtbar sind. Die gemeinsame Nullmenge $Z_g$ ist der korrekte neue Zentralbegriff.

---

## 209.A — Singularitätsmenge eines einzelnen Primkanals

**Definition.** Normalisiere den NEU-208-Kanal durch Abzug des skalaren Anfangswerts:
$$\widetilde X_{p,N} := X_{p,N} - c_0 \cdot 1.$$
Da Skalare mit allen Generatoren kommutieren, ändern sich die Kommutatorformeln nicht.

Unter $\widehat{\mathbb Z} \cong \prod_{\ell} \mathbb Z_\ell$ definiere die Koordinatenhyperfläche
$$K_p := \bigcap_{N \ge 0} p^N\widehat{\mathbb Z} = \{x \in \widehat{\mathbb Z} : x_p = 0\}.$$
Dies ist nicht nur der globale Punkt $\{0\}$, sondern eine große abgeschlossene Koordinatenhyperfläche: Die $p$-Komponente ist null, alle anderen Primkomponenten bleiben frei.

**Satz ([O-209-1]).** *Für $x \in K_p$ gilt*
$$q_{p,j}(x) = 0, \qquad E_{p^N}(x) = 1,$$
*und daher*
$$\widetilde X_{p,N}(x) = c_N - c_0.$$
*Insbesondere*
$$\boxed{\|\widetilde X_{p,N}|_{K_p}\| = c_N - c_0 \longrightarrow \infty.}$$

**Beweis.** Für $x \in K_p$ gilt $v_p(x) = \infty$ (die $p$-adische Bewertung ist unendlich), also $p^N \mid x$ für alle $N$, d.h. $E_{p^N}(x) = 1_{p^N\widehat{\mathbb Z}}(x) = 1$. Daher $q_{p,j}(x) = E_{p^j}(x) - E_{p^{j+1}}(x) = 0$ für alle $j \ge 0$. Es folgt
$$\widetilde X_{p,N}(x) = \sum_{j=0}^{N-1}(c_j - c_0)q_{p,j}(x) + (c_N - c_0)E_{p^N}(x) = c_N - c_0. \quad\square$$

$$\boxed{[O\text{-}209\text{-}1] \quad \checkmark[M]}$$

---

## 209.B — Fehlermultiplikatoren sehen $K_p$

**Satz ([O-209-2]).** *Sei $M \in B_{\mathrm{alg}} \setminus \{0\}$ ein lokal konstanter Fehlermultiplikator von Modul $L \ge 1$, und sei $p \nmid L$. Dann gilt*
$$\|M|_{K_p}\| = \|M\|,$$
*und daher*
$$\|M\widetilde X_{p,N}\| \longrightarrow \infty.$$

**Beweis.** Da $M$ lokal konstant ist, faktorisiert es über $\widehat{\mathbb Z} \to \mathbb Z/L\mathbb Z$. Da $p \nmid L$, ist die Einschränkung
$$K_p \longrightarrow \mathbb Z/L\mathbb Z$$
surjektiv: Das Festsetzen der $p$-Komponente auf null beschränkt keinen Quotienten, dessen Modul zu $p$ teilerfremd ist. Also nimmt $M|_{K_p}$ dieselben Werte an wie $M$, und $\|M|_{K_p}\| = \|M\|$.

Damit folgt:
$$\|M\widetilde X_{p,N}\| \ge \|(M\widetilde X_{p,N})|_{K_p}\| = (c_N - c_0)\|M|_{K_p}\| = (c_N - c_0)\|M\| \longrightarrow \infty. \quad\square$$

$$\boxed{[O\text{-}209\text{-}2] \quad \checkmark[M]}$$

---

## 209.C — Ausschluss des naiven Sandwichansat­zes

**Satz ([O-209-3]).** *Der naive geladene Kopplungsansatz*
$$Z_{F,\mathbf N} = \mu_m \Bigl(\sum_{p \in F}\widetilde X_{p,N_p}\Bigr)\mu_n^*$$
*ist für jeden nichtverschwindenden Charakterfehlermultiplikator $M_{g,r} \neq 0$ ausgeschlossen: Die $e(r)$-Kommutatornormen divergieren.*

**Beweis.** Aus der NEU-206-Faktorisierung:
$$[Z_{F,\mathbf N}, e(r)] = \mu_m M_{g,r} \Bigl(\sum_{p \in F}\widetilde X_{p,N_p}\Bigr) \mu_n^*.$$
Wegen der Isometrieeigenschaft $\|\mu_m b\mu_n^*\| = \|b\|$ (da $\mu_m^*\mu_m = 1$ und $\mu_n\mu_n^* \le 1$):
$$\|[Z_{F,\mathbf N}, e(r)]\| = \Bigl\|M_{g,r}\sum_{p \in F}\widetilde X_{p,N_p}\Bigr\|.$$
Da alle $\widetilde X_{p,N_p} \ge 0$ (positive Funktionen bei logarithmischen Koeffizienten), gilt
$$\sum_{p \in F}\widetilde X_{p,N_p} \ge \widetilde X_{p,N_p}$$
für jedes $p \in F$. Sei $L = L(g,r)$ der Modul von $M_{g,r}$. Da $L$ nur endlich viele Primteiler besitzt, gibt es unendlich viele Primzahlen $p \nmid L$. Für jede solche Primzahl und $N_p \to \infty$:
$$\Bigl\|M_{g,r}\sum_{p \in F}\widetilde X_{p,N_p}\Bigr\| \ge (c_{N_p}-c_0)\|M_{g,r}\| \longrightarrow \infty. \quad\square$$

$$\boxed{[O\text{-}209\text{-}3] \quad \checkmark[M]_{\mathrm{neg}}}$$

**Abgrenzung.** Dieser Negativbefund betrifft ausschließlich den naiven Sandwichansatz $\mu_m(\sum_p \widetilde X_{p,N_p})\mu_n^*$. Der neutrale Erfolg von NEU-208 bleibt vollständig bestehen.

---

## 209.D — Gemeinsame Charakterkernmenge

**Definition ([O-209-4]).** Für einen festen geladenen Grad $g = m/n \neq 1$ definiere
$$\boxed{Z_g := \bigcap_{r \in \mathbb Q/\mathbb Z} Z(M_{g,r}) \subseteq \widehat{\mathbb Z},}$$
wobei $Z(M_{g,r}) = \{x \in \widehat{\mathbb Z} : M_{g,r}(x) = 0\}$ die Nullmenge des Fehlermultiplikators ist.

$Z_g$ ist der größte abgeschlossene Teilraum, auf dem alle Charakterfehler gleichzeitig verschwinden.

**Notwendige Bedingung.** Ein erfolgreicher singulärer geladener Potentialansatz muss seine unbeschränkte Masse auf $Z_g$ konzentrieren:
$$\boxed{\operatorname{Sing}(X) \subseteq Z_g.}$$

**Geometrische Diagnose.** Die beiden Generatorsektoren verlangen entgegengesetzte Singularitätsgeometrien:

| Sektor | Verlangen | Grund |
|---|---|---|
| $\mu_k$-Sektor | Separierbarkeit: $X = \sum_p X_p$ | Neue Primrichtungen sollen feste $\mu_k$-Kommutatoren nicht verändern |
| $e(r)$-Sektor | Gemeinsame Lokalisierung: $\operatorname{Sing}(X) \subseteq Z_g$ | Fehlermultiplikatoren $M_{g,r}$ dürfen Singularität nicht sehen |

Separierbare Primkanäle tragen ihre Singularität auf Koordinatenhyperflächen $K_p = \{x_p = 0\}$, die viel größer als $Z_g$ sind (und für $M_{g,r}$ mit $p \nmid L(g,r)$ sichtbar bleiben).

$$\boxed{[O\text{-}209\text{-}4] \quad \checkmark[K]}$$

---

## 209.E — Berechnung von $Z_g$

**[O-209-5] ?[O]**

Aus NEU-205 gilt $M_{g,r} = e(nr) - e(mr)$ mit $g = m/n$. Die Nullmenge ist
$$Z(M_{g,r}) = \{x \in \widehat{\mathbb Z} : e(nr)(x) = e(mr)(x)\} = \{x : (m-n)r \cdot x \equiv 0 \pmod{\mathbb Z}\}.$$

Für $r = s/q$ (gekürzt) ist dies die Bedingung $(m-n)sx/q \in \mathbb Z$, also $q \mid (m-n)sx$ in $\widehat{\mathbb Z}$.

Die Schnittmenge über alle $r \in \mathbb Q/\mathbb Z$ verlangt, dass $x$ von allen ganzen Zahlen der Form $(m-n)L$ für beliebige $L$ geteilt wird. Falls die Elemente $e(nr)-e(mr)$ für alle $r$ ganz $\mathbb Q/\mathbb Z$ erzeugen, dann ist
$$Z_g = \{0\}.$$

**Prüfung erforderlich:** Ob $Z_g = \{0\}$ für alle $g = m/n \neq 1$ mit $(m,n)=1$ gilt, muss aus den exakten Formeln von NEU-205 hergeleitet werden. Konzeptionell ist dies zu erwarten, da die Charakterdifferenzen $e(nr)-e(mr)$ die Topologie von $\widehat{\mathbb Z}$ vollständig trennen.

$$\boxed{[O\text{-}209\text{-}5] \quad ?[O]}$$

---

## 209.F — Neuer Potentialtyp: globale 0-Lokalisierung mit separierbaren Transportdifferenzen

**[O-209-6] ?[O]**

Assuming $Z_g = \{0\}$: Gesucht ist ein Potential $X_N$ mit folgenden Eigenschaften:
1. **Singularität bei 0:** $\|X_N\| \to \infty$, aber $X_N$ ist auf $\widehat{\mathbb Z} \setminus \{0\}$ (im geeigneten Sinn) beschränkt.
2. **Separierbare Transportdifferenzen:** Für jedes $k$ gilt $[X_N, \mu_k]$ ist norm-Cauchy, und der Grenzmultiplikator hat separierbare Primstruktur.
3. **Charakterkernabsorption:** $M_{g,r} X_N \to 0$ in Norm für alle $r$.

Ein natürlicher Kandidat wäre ein Potential, das aus den Projektionen $E_{p^N}$ für alle Primzahlen gleichzeitig aufgebaut ist:
$$X_N = f(N) \cdot E_{\mathrm{lcm}(1,\ldots,N)},$$
wobei $E_{\mathrm{lcm}(1,\ldots,N)}$ auf die durch $\mathrm{lcm}(1,\ldots,N)$ teilbaren Elemente projiziert, also eine wachsende Familie von Untergruppen ausschöpft, die gegen $\{0\}$ schrumpft.

Dies ist genau die Charakterkern-Erschöpfungskette aus NEU-206, jetzt jedoch als **neutrales Potential** verwendet. Die Verbindung zur geladenen Route erfordert die Kopplung an $\mu_m\,\cdot\,\mu_n^*$ — was den Konflikt mit den Transportdifferenzen wiederaufwirft.

$$\boxed{[O\text{-}209\text{-}6] \quad ?[O]}$$

---

## 209.G — Strukturkonflikt und neuer Flaschenhals

$$\boxed{\text{Separierbare Potentiale sind entlang von Koordinatenhyperflächen singulär; geladene Charakterfehler erlauben voraussichtlich nur eine gemeinsame Singularität am globalen Ursprung.}}$$

Der neue Flaschenhals ist wesentlich klarer als in NEU-207 und NEU-208:

$$\boxed{\text{Gesucht ist keine Summe unabhängiger Prim-Singularitäten, sondern eine gemeinsame, global bei }0\text{ lokalisierte Singularität mit separierbaren Transportdifferenzen.}}$$

Das ist ein direkter Schritt auf dem Weg zu Objekt $X$ (Schicht X.3, $[L_3]$-Klasse). Plan B wird dafür nicht benötigt.

---

## 209.H — Strukturbilanz

| Knoten | Status | Inhalt |
|---|---|---|
| [O-209-1] | ✓[M] | $\widetilde X_{p,N}|_{K_p} = c_N - c_0 \to \infty$; $K_p$ vollständige Singularitätshyperfläche |
| [O-209-2] | ✓[M] | $p \nmid L \Rightarrow \|M|_{K_p}\| = \|M\|$; Fehlermultiplikatoren sehen $K_p$ |
| [O-209-3] | ✓[M]_neg | Naiver Sandwichansatz $\mu_m(\sum_p \widetilde X_{p,N_p})\mu_n^*$ ausgeschlossen |
| [O-209-4] | ✓[K] | $Z_g = \bigcap_r Z(M_{g,r})$ als notwendige Singularitätsmenge definiert |
| [O-209-5] | ?[O] | Berechnung von $Z_g$ aus NEU-205-Formeln; Prüfung $Z_g = \{0\}$ |
| [O-209-6] | ?[O] | Potential mit Singularität bei $\{0\}$ und separierbaren Transportdifferenzen |

---

## 209.I — DAG-Stand

```
[O-208-5] ?[O]  (Kopplung geladene Atome)
      |
      +---> [O-209-1] ✓[M]       K_p = {x_p=0} vollständige Singularitätshyperfläche
      |
      +---> [O-209-2] ✓[M]       Fehlermultiplikatoren sehen K_p (p ∤ L)
      |
      +---> [O-209-3] ✓[M]_neg   Naiver Sandwichansatz ausgeschlossen
      |
      +---> [O-209-4] ✓[K]       Z_g = ⋂_r Z(M_{g,r}) definiert
      |
      +---> [O-209-5] ?[O]        Berechnung Z_g, Prüfung Z_g = {0}
      |
      +---> [O-209-6] ?[O]        Potential: Sing(X) ⊆ {0}, separierbare Transportdifferenzen
```
