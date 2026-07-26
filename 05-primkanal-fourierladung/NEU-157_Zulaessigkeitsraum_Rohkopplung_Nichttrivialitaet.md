# NEU-157 — Zulässigkeitsraum und Nichtverschwindung der Rohkopplung

> Stand: 15. Juli 2026 (rev.3 — Revision nach Konsistenzaudit NEU-165b).  
> Vorgänger: NEU-156 §156.G, NEU-155 §155.H, NEU-153 §D.2.  
> Typ: **Existenzsatz-Vorbereitung**.  
> Revisionsgrund: NEU-165b hat ergeben, dass die bisherigen $R_{p,j}$ in keinem Blatt explizit konstruiert wurden und dass die $W^{\mathrm{res}}$-Normierung quadratisch ist und keinen linearen Kern erzeugt. Die bisherige Gleichung (157.A.1) war daher nicht als Definition eines exakten Zulässigkeitsraums gerechtfertigt.

---

## DAG-Position

```
NEU-156  ──►  NEU-157  ──►  NEU-159 (Dualzeuge, Zeugen-Konstruktion)
                   └──►  NEU-158 (Symmetrieeindeutigkeit)
                   └──►  NEU-165 (Matrixrahmen, bedingt)
```

---

## 157.A — Revisionsbefund

Der Konsistenzaudit NEU-165b hat ergeben:

- Die in der bisherigen Fassung verwendeten Operatoren $R_{p,j}$ sind weder in NEU-41 noch in NEU-157 explizit konstruiert.
- NEU-41 §3 enthält Bedingungen an zulässige Hebungen, aber keine einheitliche Familie homogener linearer Operatoren.
- Insbesondere ist die $W^{\mathrm{res}}$-Normierungsbedingung quadratisch und kann nicht als Kern eines komplex-linearen Operators dargestellt werden.

Daher ist die bisherige Definition

$$\mathcal{E}_p^{\mathrm{lin}} := \ker(\pi_{\mathrm{prim}}) \cap \bigcap_j\ker(R_{p,j})$$

nicht als Definition des **exakten** Zulässigkeitsraums gerechtfertigt.

Alle Aussagen, welche diese Identifikation verwenden, sind bis zur folgenden Neuformulierung als **bedingt** zu lesen.

---

## 157.B — Affine Liftfaser

Fixiere einen Ausgangslift $\widehat{\varepsilon}_p^{\,0}$ mit

$$\pi_{\mathrm{prim}}(\widehat{\varepsilon}_p^{\,0}) = \varepsilon_p.$$

Der Raum aller algebraisch möglichen Liftänderungen ist

$$K_p := \ker(\pi_{\mathrm{prim}}).$$

Die vollständige Liftfaser lautet somit $\widehat{\varepsilon}_p^{\,0} + K_p$. Die Primärbedingung ist damit bereits exakt in der affinen Faser kodiert und muss nicht erneut als unbekannter Regularitätsoperator eingeführt werden.

---

## 157.C — Klassifikation der Nebenbedingungen

Die Bedingungen aus NEU-41 §3 sind nach ihrem mathematischen Typ zu trennen.

### 157.C.1 — Homogen-lineare Bedingungen

Eine Bedingung ist homogen-linear, wenn sie für Liftänderungen durch einen expliziten linearen Operator

$$L_{p,a}: K_p \longrightarrow Y_{p,a}$$

in der Form $L_{p,a}(k) = 0$ beschrieben wird. Der exakt definierte lineare Nebenbedingungsraum ist dann

$$K_p^{\mathrm{hom}} := K_p \cap \bigcap_{a \in A_p} \ker(L_{p,a}).$$

Nur **explizit konstruierte** und als linear bewiesene Operatoren dürfen in diesen Schnitt aufgenommen werden. Die bisher nur postulierten Symbole $R_{p,j}$ werden nicht in die Definition übernommen.

### 157.C.2 — Affin-lineare Bedingungen

Sei eine Bedingung durch $A_{p,b}(\widehat{\varepsilon}_p) = c_{p,b}$ gegeben, wobei $A_{p,b}$ linear ist. Erfüllt der Ausgangslift bereits $A_{p,b}(\widehat{\varepsilon}_p^{\,0}) = c_{p,b}$, so reduziert sich die Bedingung an die Liftänderung auf $A_{p,b}(k) = 0$. Eine affin-lineare Bedingung darf daher erst nach Wahl und Prüfung eines zulässigen Ausgangslifts als homogener Kern auf $K_p$ behandelt werden.

### 157.C.3 — Quadratische $W^{\mathrm{res}}$-Normierung

Setze $h_p(x,y) := \langle x,y\rangle_{W^{\mathrm{res}}}$ und $q_p(x) := h_p(x,x)$.
Die Normierungsbedingung lautet $q_p(\widehat{\varepsilon}_p) = 1$.

Angenommen, $q_p(\widehat{\varepsilon}_p^{\,0}) = 1$. Für $\widehat{\varepsilon}_p^{\,0} + k$ ergibt sich

$$q_p(\widehat{\varepsilon}_p^{\,0}+k) - q_p(\widehat{\varepsilon}_p^{\,0}) = 2\operatorname{Re}\,h_p(\widehat{\varepsilon}_p^{\,0},k) + h_p(k,k).$$

Die **exakte** Normierungsbedingung an $k$ ist somit

$$2\operatorname{Re}\,h_p(\widehat{\varepsilon}_p^{\,0},k) + h_p(k,k) = 0.\tag{157.1}$$

Die zugeordnete quadratische Niveaumenge ist

$$\mathcal{Q}_p(\widehat{\varepsilon}_p^{\,0}) := \{k \in K_p : 2\operatorname{Re}\,h_p(\widehat{\varepsilon}_p^{\,0},k) + h_p(k,k) = 0\}.$$

Im Allgemeinen ist $\mathcal{Q}_p(\widehat{\varepsilon}_p^{\,0})$ **kein Vektorraum**. Falls OP-4.1 lediglich Nichtausgeartetheit liefert, ist sie als quadratische Niveaumenge (Quadrik), nicht als Einheitssphäre zu bezeichnen.

### 157.C.4 — Hebungsunabhängigkeit als Faktorisierungsbedingung

Ist $C_p$ linear, so gilt $C_p(\widehat{\varepsilon}_p^{\,0}+k) - C_p(\widehat{\varepsilon}_p^{\,0}) = C_p(k)$. Unabhängigkeit unter einer erlaubten Klasse von Liftänderungen $K_p^{\mathrm{allow}} \subseteq K_p$ ist daher äquivalent zu

$$K_p^{\mathrm{allow}} \subseteq \ker(C_p).$$

Dies ist eine **Faktorisierungsbedingung** an $C_p$ und nicht automatisch ein unabhängiger Regularitätsoperator. Erst wenn exakt festgelegt ist, unter welchen Liftänderungen Unabhängigkeit verlangt wird, darf daraus eine lineare Kernbedingung gewonnen werden.

---

## 157.D — Exakte Zulässigkeitsmenge

Seien $F_{p,\alpha}: \mathfrak{L}_p \to Z_{p,\alpha}$ alle verbleibenden exakt definierten, möglicherweise nichtlinearen Bedingungen. Dann ist die Menge exakt zulässiger Liftänderungen

$$\mathcal{A}_p^{\mathrm{adm}}(\widehat{\varepsilon}_p^{\,0}) := \left\{k \in K_p^{\mathrm{hom}} : k \in \mathcal{Q}_p(\widehat{\varepsilon}_p^{\,0}),\; F_{p,\alpha}(\widehat{\varepsilon}_p^{\,0}+k)=0\;\forall\alpha\right\}.\tag{157.2}$$

Die Menge exakt zulässiger Hebungen ist $\widehat{\varepsilon}_p^{\,0} + \mathcal{A}_p^{\mathrm{adm}}(\widehat{\varepsilon}_p^{\,0})$.

Im Allgemeinen sind weder $\mathcal{A}_p^{\mathrm{adm}}(\widehat{\varepsilon}_p^{\,0})$ noch $\mathfrak{L}_p^{\mathrm{adm}}$ Vektorräume. Die bisherige Bezeichnung $\mathcal{E}_p^{\mathrm{lin}}$ darf daher **nicht** als Synonym für den exakten Zulässigkeitsraum fortgeführt werden.

---

## 157.E — Tangentialraum

Der linearisierte Normierungsterm am Ausgangslift ist $2\operatorname{Re}\,h_p(\widehat{\varepsilon}_p^{\,0},k)$. Der Tangentialraum der Normierungsquadrik lautet

$$T_p^{\mathrm{norm}} := \{k \in K_p : \operatorname{Re}\,h_p(\widehat{\varepsilon}_p^{\,0},k) = 0\}.\tag{157.3}$$

Dieser Raum ist im Allgemeinen nur **reell-linear**, nicht komplex-linear.

Falls die übrigen Bedingungen $F_{p,\alpha}$ differenzierbar sind, definiere

$$\mathrm{Tan}_{\widehat{\varepsilon}_p^{\,0}}\,\mathfrak{L}_p^{\mathrm{adm}} := \left\{k \in K_p^{\mathrm{hom}} : \operatorname{Re}\,h_p(\widehat{\varepsilon}_p^{\,0},k) = 0,\; DF_{p,\alpha}(\widehat{\varepsilon}_p^{\,0})[k]=0\;\forall\alpha\right\}.\tag{157.4}$$

Ein etwaiger Operator $R_{p,j}$ darf künftig nur dann eingeführt werden, wenn ausdrücklich bewiesen wird, dass er gleich $DF_{p,j}(\widehat{\varepsilon}_p^{\,0})$ ist oder eine global gültige homogen-lineare Bedingung darstellt. Im ersten Fall ist er basispunktabhängig und entsprechend zu notieren: $R_{p,j}^{\,\widehat{\varepsilon}_p^{\,0}}$.

---

## 157.F — Exakter Existenzauftrag

Der Zielausdruck $T_p(\mathcal{E}_p^{\mathrm{adm}}) \neq \{0\}$ ist zu präzisieren. Der exakte Existenzauftrag lautet:

$$\boxed{\exists\, k \in \mathcal{A}_p^{\mathrm{adm}}(\widehat{\varepsilon}_p^{\,0}) \text{ mit } T_p(k) \neq 0.}\tag{157.5}$$

Alternativ, falls $T_p$ auf vollständige Hebungen wirkt:

$$\boxed{\exists\, \widehat{\varepsilon}_p \in \mathfrak{L}_p^{\mathrm{adm}} \text{ mit } T_p(\widehat{\varepsilon}_p) \neq 0.}\tag{157.6}$$

Ein Tangentialvektor $k \in \mathrm{Tan}_{\widehat{\varepsilon}_p^{\,0}}\,\mathfrak{L}_p^{\mathrm{adm}}$ ist noch kein exakt zulässiger Liftwechsel. Insbesondere folgt aus $T_p(k) \neq 0$ für einen Tangentialvektor allein noch kein exakter Zulässigkeitszeuge.

---

## 157.G — Verhältnis zwischen exakter Menge und Tangentialraum

**Lokale infinitesimale Aufgabe:**  
Zeige $\exists\, k \in \mathrm{Tan}_{\widehat{\varepsilon}_p^{\,0}}\mathfrak{L}_p^{\mathrm{adm}}$ mit $T_p(k) \neq 0$. Dies zeigt nur, dass $T_p$ auf einer infinitesimal zulässigen Richtung nicht verschwindet.

**Integrationsaufgabe:**  
Zeige, dass eine solche Tangentialrichtung durch eine Kurve exakt zulässiger Hebungen realisiert wird:
$$\gamma:(-\delta,\delta)\to\mathfrak{L}_p^{\mathrm{adm}},\quad \gamma(0)=\widehat{\varepsilon}_p^{\,0},\quad \gamma'(0)=k.$$
Dieser Schritt benötigt einen Satz über die lokale Geometrie der Nebenbedingungsmenge (impliziter Funktionensatz oder explizite Parametrisierung).

**Exakte globale Aufgabe:**  
Konstruiere direkt $\widehat{\varepsilon}_p \in \mathfrak{L}_p^{\mathrm{adm}}$ mit nichtverschwindendem $T_p$-Bild. Nur diese Aussage schließt den ursprünglichen Existenzauftrag vollständig.

---

## 157.H — Präprojektive Nichtverschwindung

Für $u \neq 0$ (NEU-41 (41.6), NEU-155 §155.A.1):

$$T_p^{\mathrm{pre}}(e_uV_p) := -\sum_{s,m}\ell_{s,m}\,u\,s\log p\;e_{u+ps}V_{pm}.\tag{157.B.1}$$

Die Indexabbildung $(s,m)\mapsto(u+ps,pm)$ ist bei fest gehaltenem $u$ injektiv. Daher sind die Summanden paarweise verschiedene Basisvektoren.

**Satz (präprojektiv):** Falls $\exists\,(s_0,m_0)$ mit $s_0\ell_{s_0,m_0}\neq0$, so gilt $T_p^{\mathrm{pre}}(e_uV_p)\neq0$.

*Beweis.* Lineare Unabhängigkeit der Summanden (Injektivität) und nichtverschwindender Koeffizient. $\square$

**Statusmarker:** ✅[M] als Satz; Anwendung (Existenz geeigneter $(s_0,m_0)$): ❓[O] → NEU-159.

---

## 157.I — Normierungslemma

**Lemma:** Falls $T_p(\mathcal{A}_p^{\mathrm{adm}}(\widehat{\varepsilon}_p^{\,0})) \neq \{0\}$, d.h. falls $\exists\, w \in \mathcal{A}_p^{\mathrm{adm}}(\widehat{\varepsilon}_p^{\,0})$ mit $T_pw \neq 0$, und falls $\mathcal{A}_p^{\mathrm{adm}}(\widehat{\varepsilon}_p^{\,0})$ skalierungsstabil ist, so ist

$$k_0 := \frac{w}{\sqrt{\alpha_p}\,\|T_pw\|}$$

wohldefiniert und $\alpha_p\|T_pk_0\|^2 = 1$.

**Warnung:** Skalierungsstabilität der exakten Menge $\mathcal{A}_p^{\mathrm{adm}}$ ist im Allgemeinen nicht gesichert (die Normierungsquadrik ist nicht skalierungsstabil). Das Lemma gilt für den Tangentialraum automatisch, für die exakte Menge nur nach zusätzlicher Prüfung.

**Statusmarker:** ✅[M] für Tangentialraum; ❓[O] für exakte Menge.

---

## 157.J — Statusmatrix

| Aussage | Status |
|---|---|
| Primärbedingung definiert affine Liftfaser | ✅[M] |
| $W^{\mathrm{res}}$-Normierung ist quadratisch | ✅[M] |
| Exakte Erhaltung enthält Term $h_p(k,k)$ | ✅[M] |
| Linearisierter Normierungsterm ist $2\operatorname{Re}\,h_p(\widehat{\varepsilon}_p^{\,0},k)$ | ✅[M] |
| Exakte Zulässigkeitsmenge $\neq$ Tangentialraum | ✅[M] |
| Satzschema: Min. Zeuge $\Rightarrow T_p(\mathcal{A}_p^{\mathrm{adm}})\neq\{0\}$ | ✅[M] |
| Normierungslemma (157.I) für Tangentialraum | ✅[M] |
| Welche Bedingungen aus NEU-41 §3 sind tatsächlich homogen-linear? | ❓[O] → [O-157-R1] |
| Konstruktion der $L_{p,a}$ | ❓[O] → [O-157-R2] |
| Exakte Zulässigkeitsmenge $\mathcal{A}_p^{\mathrm{adm}}$ vollständig definiert | ❓[O] → [O-157-R3] |
| Tangentialraum explizit berechnet | ❓[O] → [O-157-R4] |
| Integrabilität zulässiger Tangentialrichtungen | ❓[O] → [O-157-R5] |
| Exakt zulässiger Zeuge mit $T_p(k)\neq0$ | ❓[O] → [O-157-R6] |
| Hebungsunabhängigkeit als $K_p^{\mathrm{allow}}\subseteq\ker(C_p)$ | ❓[O] |
| $R_{p,j}$ explizit konstruiert | ✗[M] (negativer Befund, NEU-165b) |

---

## 157.K — Konsequenz für NEU-165

Der Matrixrahmen von NEU-165 bleibt als **bedingte Theorie** linearer Nebenbedingungen gültig. Er darf jedoch erst angewendet werden, nachdem explizite Operatoren $L_{p,a}$ oder $R_{p,j}^{\,\widehat{\varepsilon}_p^{\,0}}$ konstruiert wurden.

Die quadratische Normierungsbedingung wird nicht in die Basisnullmengen $N_{p,j}^{\mathrm{bas}}$ aufgenommen. Sie ist separat über die Gleichung (157.1) zu behandeln.

---

## Offene Aufgaben

$$\boxed{\text{[O-157-R1]}}$$  
Jede Bedingung aus NEU-41 §3 als linear, affin, quadratisch, nichtlinear oder Quotientenbedingung klassifizieren.

$$\boxed{\text{[O-157-R2]}}$$  
Alle tatsächlich homogen-linearen Operatoren $L_{p,a}$ explizit konstruieren.

$$\boxed{\text{[O-157-R3]}}$$  
Die exakte Zulässigkeitsmenge $\mathcal{A}_p^{\mathrm{adm}}$ vollständig definieren.

$$\boxed{\text{[O-157-R4]}}$$  
Den Tangentialraum $\mathrm{Tan}_{\widehat{\varepsilon}_p^{\,0}}\,\mathfrak{L}_p^{\mathrm{adm}}$ separat berechnen.

$$\boxed{\text{[O-157-R5]}}$$  
Integrabilität zulässiger Tangentialrichtungen untersuchen.

$$\boxed{\text{[O-157-R6]}}$$  
Einen exakt zulässigen Zeugen $k$ beziehungsweise $\widehat{\varepsilon}_p$ mit nichtverschwindendem $T_p$-Bild konstruieren.

---

## Verweise

NEU-41 §3/§4, NEU-143, NEU-153 §D.2, NEU-155 §155.A.1/G–H, NEU-156 §156.B–E, NEU-158, NEU-159, NEU-165, NEU-165b.
