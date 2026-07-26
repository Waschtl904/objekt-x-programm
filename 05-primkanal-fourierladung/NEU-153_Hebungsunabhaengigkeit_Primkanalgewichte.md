# NEU-153 — Hebungsunabhängigkeit und Wohldefiniertheit der Primkanalgewichte

> Stand: 13. Juli 2026.  
> Vorgänger: NEU-41 (Fourier-Hebung, Kopplungsoperator), NEU-44 (Primkanten-Grundlagen).  
> Nachfolger: NEU-152 (Nichtentartung — logisch nachgelagert).  
> Typ: Wohldefiniertheitsbarriere. Kein Beweisblatt; präzise Prüffrage.

---

## Einleitung und Motivation

NEU-41 konstruiert für jede Fourier-geladene Primhebung \(\widehat{\varepsilon}_p\) den Kopplungsvektor

\[
\Psi_p(\widehat{\varepsilon}_p)
= \Pi_{W_{\mathrm{res}}} \widetilde{\omega}_2(\widehat{\varepsilon}_p, L_3^\circ)
\in \mathcal{H}_{J,N}.
\]

Aus diesem Vektor wird das Primkanalgewicht definiert:

\[
|c_p|^2 := \|\Psi_p(\widehat{\varepsilon}_p)\|^2_{W_{\mathrm{res}}}.
\]

**Das Problem:** Diese Definition hängt a priori von der Wahl der Hebung \(\widehat{\varepsilon}_p\) ab. Die Wohlbestimmtheitsbedingung (41.4) aus NEU-41,

\[
\widehat{\varepsilon}_p \sim \widehat{\varepsilon}_p'
\;\Longrightarrow\;
C_p C_p^\# = C_p' C_p'^\# \quad \text{im } W_{\mathrm{res}}\text{-Quotienten,}
\tag{41.4}
\]

ist dort ausdrücklich als **offen** markiert (Status: ❓[O]).

Solange (41.4) nicht bewiesen ist, gilt:

\[
\boxed{|c_p|^2 \text{ ist kein wohldefiniertes intrinsisches Primgewicht.}}
\]

**Konsequenz für NEU-152:** Eine untere Schranke \(|c_p|^2 \gtrsim (\log p)^2/p\) kann erst als Eigenschaft des Primkanals formuliert werden, nachdem die Wohldefiniertheit von \(|c_p|^2\) gesichert ist.

---

## DAG-Position

```
NEU-41  ──►  NEU-153  ──►  NEU-152  ──►  NEU-150 (R-Cutoff)
```

- **NEU-41** konstruiert \(\Psi_p\) relativ zur Hebung.  
- **NEU-153** (dieses Blatt) prüft, ob \(|c_p|^2\) hebungsunabhängig ist.  
- **NEU-152** untersucht danach die termweise Nichtentartung.  
- **NEU-150** nutzt die zweiseitige Skalierung für den \(R\)-Cutoff.

---

## Prüfrahmen

Sei \(h_p \in \ker \pi_{\mathrm{prim}}\) eine zulässige Hebungsänderung:

\[
\widehat{\varepsilon}_p' = \widehat{\varepsilon}_p + h_p,
\qquad
\pi_{\mathrm{prim}}(h_p) = 0.
\]

Definierende Abkürzungen:

\[
A_p := \Pi_{W_{\mathrm{res}}} \widetilde{\omega}_2(\widehat{\varepsilon}_p, L_3^\circ),
\qquad
D_p(h) := \Pi_{W_{\mathrm{res}}} \widetilde{\omega}_2(h, L_3^\circ).
\]

Dann gilt:

\[
\Psi_p(\widehat{\varepsilon}_p') = A_p + D_p(h_p).
\]

---

## 153.A — Starke Invarianz

**Aussage:**

\[
D_p(h_p) = \Pi_{W_{\mathrm{res}}} \widetilde{\omega}_2(h_p, L_3^\circ) = 0
\quad \text{für alle zulässigen } h_p \in \ker \pi_{\mathrm{prim}}.
\]

**Konsequenz:** \(\Psi_p(\widehat{\varepsilon}_p') = \Psi_p(\widehat{\varepsilon}_p)\). Der Vektor ist intrinsisch, nicht nur seine Norm.

**Hinreichende Bedingung:** 
\[
\widetilde{\omega}_2(\ker \pi_{\mathrm{prim}}, L_3^\circ) \subseteq \ker \Pi_{W_{\mathrm{res}}}.
\]

Das wäre der Fall, wenn die \(\widetilde{\omega}_2\)-Kopplung von Elementen im Hebungskern grundsätzlich in den \(W_{\mathrm{res}}\)-Nullraum fällt.

**Status: ❓[O].**

---

## 153.B — Schwache Norminvarianz

**Aussage:**

\[
\|\Psi_p(\widehat{\varepsilon}_p')\|_{W_{\mathrm{res}}} = \|\Psi_p(\widehat{\varepsilon}_p)\|_{W_{\mathrm{res}}},
\quad \text{d.h.} \quad
|c_p(\widehat{\varepsilon}_p')|^2 = |c_p(\widehat{\varepsilon}_p)|^2.
\]

Das ist die **minimale Aussage**, die NEU-152 benötigt.

**Status: ❓[O].** Aus \(153.A\) würde \(153.B\) folgen; umgekehrt nicht.

---

## 153.C — Explizite Differenzformel

Aus elementarer Norm-Entwicklung:

\[
\|A_p + D_p(h)\|^2 - \|A_p\|^2
= 2\operatorname{Re}\langle A_p, D_p(h)\rangle_{W_{\mathrm{res}}}
+ \|D_p(h)\|^2_{W_{\mathrm{res}}}.
\tag{153.1}
\]

**Status: \checkmark[M]** — elementare Identität.

**Konsequenz:** Norminvarianz (153.B) äquivaliert zu

\[
2\operatorname{Re}\langle A_p, D_p(h)\rangle_{W_{\mathrm{res}}} + \|D_p(h)\|^2_{W_{\mathrm{res}}} = 0
\quad \text{für alle zulässigen } h.
\tag{153.2}
\]

---

## 153.D.0 — Geometrie der normierten Hebungsfaser

> Eingefügt 13. Juli 2026. **Voraussetzung für jeden Falsifikationstest.**

### Identifikation der Zulässigkeitsbedingungen aus NEU-41 §3

NEU-41 §3 listet drei Bedingungen an eine zulässige Fourier-geladene Primhebung:

1. **Projektionsbedingung:** \(\pi_{\mathrm{prim}}(\widehat{\varepsilon}_p) = \varepsilon_p = e_0 V_p\)
2. **Fourierladungsbedingung:** \(\widehat{\varepsilon}_p = \sum_{u\neq 0} a_{p,u} e_u V_p + \cdots\) mit mindestens einem \(a_{p,u} \neq 0\)
3. **Normierungsbedingung:** \(\operatorname{Tr}^{\mathrm{conn}}_{W_{\mathrm{res}}}(\widehat{\varepsilon}_p^\# \widehat{\varepsilon}_p) = 1\)

Die **normierte Hebungsfaser** ist die Schnittmenge aller drei Bedingungen:

\[
\mathcal{L}_p := \bigl\{ \widehat{\varepsilon} \in B_3 : \pi_{\mathrm{prim}}(\widehat{\varepsilon}) = \varepsilon_p,\ \|\widehat{\varepsilon}\|_{\mathrm{conn}} = 1,\ \widehat{\varepsilon} \text{ hat Fourierladung} \bigr\}.
\]

---

### D.0.1 — Zulässige Struktur eines Ausgangshebungsvektors

**Beobachtung aus NEU-41 (41.3):** Wegen \(\widetilde{\omega}_2(e_0 V_p, L_3^\circ) = 0\) (Fourierfaktor \(r = 0\)) ist der Nullmodus \(e_0 V_p\) für die Kopplung wirkungslos.

Daher ist jede zulässige Hebung der Form

\[
\widehat{\varepsilon}_p = e_0 V_p + \underbrace{\sum_{u \neq 0} a_{p,u} e_u V_p + \cdots}_{=: f_p \in \ker \pi_{\mathrm{prim}}},
\qquad f_p \neq 0.
\tag{D.0.1}
\]

Das bedeutet: **Der Ausgangshebungsvektor \(e_u V_p\) mit \(u \neq 0\) allein ist keine zulässige Hebung**, denn er erfüllt nicht \(\pi_{\mathrm{prim}}(e_u V_p) = \varepsilon_p\). Er liegt selbst im Kern. Ein Testfall der Form \(\widehat{\varepsilon}_p = e_u V_p\) \((u \neq 0)\) ist zulässigkeitswidrig.

---

### D.0.2 — Konsistenzfrage: Sind alle drei Bedingungen gleichzeitig erfüllbar?

Zerlege einen allgemeinen Vektor (D.0.1) in Nullmodus + geladenen Anteil:

\[
\widehat{\varepsilon}_p = e_0 V_p + f_p, \qquad f_p \in \ker \pi_{\mathrm{prim}}, \quad f_p \neq 0.
\]

Die Normierungsbedingung ergibt:

\[
\|\widehat{\varepsilon}_p\|_{\mathrm{conn}}^2
= \|e_0 V_p\|_{\mathrm{conn}}^2 + 2\operatorname{Re}\langle e_0 V_p, f_p\rangle_{\mathrm{conn}} + \|f_p\|_{\mathrm{conn}}^2 = 1.
\tag{D.0.2}
\]

Hierbei treten drei Subfälle auf:

**Subfall (a) — Nullmodus normiert und \(\perp\) Kern:**
\[
\|e_0 V_p\|_{\mathrm{conn}} = 1, \quad \langle e_0 V_p, f_p \rangle_{\mathrm{conn}} = 0.
\]
Dann verlangt (D.0.2): \(\|f_p\|_{\mathrm{conn}}^2 = 0\), also \(f_p = 0\).

> **Kritische Konsequenz:** Falls die verbundene Form positiv definit ist und \(e_0 V_p\) bereits normiert und \(\perp \ker \pi_{\mathrm{prim}}\) liegt, **existiert kein zulässiger Lift mit Fourierladung**. Die Menge \(\mathcal{L}_p\) wäre leer (Widerspruch zur Voraussetzung). Dieser Subfall schließt aus, dass die verbundene Form auf \(\{e_0 V_p\} \oplus \ker\pi_{\mathrm{prim}}\) definitiv und diagonal ist.

**Subfall (b) — \(\langle e_0 V_p, f_p\rangle_{\mathrm{conn}} \neq 0\):**
Bedingung (D.0.2) kann mit \(f_p \neq 0\) erfüllbar sein, wenn der Kreuzterm negativ genug ist. Hierzu müssen die Werte \(\|e_0 V_p\|_{\mathrm{conn}}\), \(\|e_u V_p\|_{\mathrm{conn}}\) und \(\langle e_0 V_p, e_u V_p\rangle_{\mathrm{conn}}\) aus NEU-44 bestimmt werden.

**Subfall (c) — Verbundene Form indefinit oder degeneriert:**
Falls \(\|\cdot\|_{\mathrm{conn}}\) keine positive Hilbertnorm ist (z.\,B. indefinit oder semidefinit), könnte (D.0.2) mit \(f_p \neq 0\) erfüllbar sein, auch wenn der Kreuzterm verschwindet.

---

### D.0.3 — Zulässige Tangentialvektoren an \(\mathcal{L}_p\)

Angenommen, \(\mathcal{L}_p\) ist nichtleer und \(\widehat{\varepsilon}_p \in \mathcal{L}_p\). Ein infinitesimaler Tangentialvektor \(h\) an \(\mathcal{L}_p\) bei \(\widehat{\varepsilon}_p\) muss erfüllen:

- **Projektionsbedingung:** \(\pi_{\mathrm{prim}}(h) = 0\), d.h. \(h \in \ker \pi_{\mathrm{prim}}\).
- **Normtangentialbedingung:** \(\operatorname{Re}\langle \widehat{\varepsilon}_p, h\rangle_{\mathrm{conn}} = 0\).

Der **Tangentialraum** an \(\mathcal{L}_p\) bei \(\widehat{\varepsilon}_p\) ist daher:

\[
T_{\widehat{\varepsilon}_p} \mathcal{L}_p
= \ker \pi_{\mathrm{prim}} \cap \{h : \operatorname{Re}\langle \widehat{\varepsilon}_p, h\rangle_{\mathrm{conn}} = 0\}.
\tag{D.0.3}
\]

Falls \(T_{\widehat{\varepsilon}_p} \mathcal{L}_p \neq \{0\}\), existieren echte infinitesimale Variationen. Für eine endliche Kurve \(\widehat{\varepsilon}_p(t) \in \mathcal{L}_p\) benötigt man zusätzlich eine Korrektur zweiter Ordnung:

\[
\widehat{\varepsilon}_p(t) = \widehat{\varepsilon}_p + th + t^2 k + O(t^3),
\qquad h \in T_{\widehat{\varepsilon}_p}\mathcal{L}_p,
\quad k \in \ker \pi_{\mathrm{prim}},
\]

so dass \(\|\widehat{\varepsilon}_p(t)\|_{\mathrm{conn}}^2 = 1 + O(t^3)\). Die Bedingung an \(k\) ergibt sich als:

\[
2\operatorname{Re}\langle \widehat{\varepsilon}_p, k\rangle_{\mathrm{conn}} + \|h\|_{\mathrm{conn}}^2 = 0.
\tag{D.0.4}
\]

Eine globale Skalierung (Division durch \(\|\widehat{\varepsilon}_p + th\|_{\mathrm{conn}}\)) ist **keine** exakte Kurve in \(\mathcal{L}_p\), denn die Projektionsbedingung würde auf \(\varepsilon_p / \|\widehat{\varepsilon}_p + th\|_{\mathrm{conn}} \neq \varepsilon_p\) führen.

---

### D.0.4 — Vier Prüffragen für \(\mathcal{L}_p\)

| Frage | Was zu zeigen ist | Status |
|---|---|---|
| **D.0.I** | \(\mathcal{L}_p \neq \emptyset\): Existenz eines zulässigen Lifts mit Fourierladung | ❓[O] — hängt von Subfall (a)/(b)/(c) |
| **D.0.II** | \(\#\mathcal{L}_p > 1\): Mehr als ein Punkt in der Faser | ❓[O] — fällt mit D.0.I zusammen |
| **D.0.III** | \(T_{\widehat{\varepsilon}_p}\mathcal{L}_p \neq \{0\}\): Existenz echter Variationsrichtungen | ❓[O] — benötigt Metrikdaten aus NEU-44 |
| **D.0.IV** | Expliziter Tangentialvektor für Falsifikationstest | ❓[O] — erst nach D.0.I, D.0.III |

---

### D.0.5 — Hilbertgeometrische Entscheidung der normierten Liftfaser

> Eingearbeitet 13. Juli 2026. Ersetzt den Platzhalter-§153.D.0.5.  
> Status: ❓[O] — Typprüfung offen; Existenzfrage scharf lokalisiert.

Sei \(\pi_{\mathrm{prim}}: \mathcal{H}_p^{\mathrm{lift}} \to \mathcal{H}_p^{\mathrm{prim}}\) die primitive Projektion, angenommen als beschränkte lineare Projektion (dann ist \(K_p := \ker\pi_{\mathrm{prim}}\) abgeschlossen in der Lift-Hilbertnorm \(\|\cdot\|_{\mathrm{lift}}\)), und \(v_p := e_0 V_p\) der kanonische Lift von \(\varepsilon_p\).

Aus der \(\delta_{r,0}\)-Regel (NEU-41 §3) folgt zunächst

\[
E_p^{\mathrm{ch}} := \operatorname{span}\{e_u V_p : u \neq 0\} \subseteq K_p.
\]

Dies ist ein algebraischer Unterraum; sein Abschluss hängt von der verwendeten Norm ab (s. offene Punkte 4a/4b unten).

**Terminologie:** Im Folgenden bezeichnet „geladener Lift" einen Lift, dessen Hebungsänderung in \(E_p^{\mathrm{ch}} \setminus \{0\}\) liegt. Hebungsänderungen mit einem zusätzlichen neutralen Anteil aus \(K_p \setminus E_p^{\mathrm{ch}}\) sind damit nicht ausgeschlossen, fallen aber nicht unter die hier untersuchte Existenzfrage.

Die drei relevanten Fasermengen sind (konditional auf die Wohldefiniertheit von \(q_{\mathrm{conn}}\), s. D.0.5.A):

\[
\mathcal{L}_p^{\mathrm{full}} := \bigl\{ v_p + k : k \in K_p,\; q_{\mathrm{conn}}(v_p + k) = 1 \bigr\},
\]

\[
\mathcal{L}_p^{\mathrm{ch}} := \bigl\{ v_p + k : k \in E_p^{\mathrm{ch}} \setminus \{0\},\; q_{\mathrm{conn}}(v_p + k) = 1 \bigr\},
\]

wobei \(q_{\mathrm{conn}}(x) := \langle x, x\rangle_{\mathrm{conn}}\). Es gilt \(\mathcal{L}_p^{\mathrm{ch}} \subseteq \mathcal{L}_p^{\mathrm{full}}\), \(v_p \in \mathcal{L}_p^{\mathrm{full}}\), \(v_p \notin \mathcal{L}_p^{\mathrm{ch}}\).

---

#### D.0.5.A — Notwendige Typprüfung

NEU-41 §3 führt den Ausdruck

\[
\operatorname{Tr}^{\mathrm{conn}}_{W_{\mathrm{res}}}(x^\# y)
\]

ein. **Zu prüfen ist**, ob und durch welchen Pullback dieser Ausdruck eine Hermiteform auf \(\mathcal{H}_p^{\mathrm{lift}}\) definiert.

Die Edge-Label-Zerlegung

\[
W_{\mathrm{res,rel}} = \bigoplus_{(m,p)} H_{m\to pm}
\]

trägt eine positive Hilbertform auf dem **Zielraum** der relativen Operatoren \(C_p^{\mathrm{rel}}\). Die Liftvektoren \(e_u V_p\) liegen dagegen im **Quellraum** \(\mathcal{H}_p^{\mathrm{lift}}\).

Eine Identifikation beider Paarungen ist nur zulässig, falls die folgende Aussage explizit bewiesen wird:

\[
\langle x, y\rangle_{\mathrm{conn}}
= \langle C_p^{\mathrm{rel}} x,\, C_p^{\mathrm{rel}} y\rangle_{W_{\mathrm{res,rel}}}.
\tag{D.0.5.1}
\]

Eine alternative Formulierung: Ist die Lift-Hilbertnorm selbst durch

\[
\langle x, y\rangle_{\mathcal{H}_p^{\mathrm{lift}}} = \langle C_p^{\mathrm{rel}} x,\, C_p^{\mathrm{rel}} y\rangle_{W_{\mathrm{res,rel}}}
\tag{D.0.5.2}
\]

gegeben, so bleibt zusätzlich zu prüfen, ob \(\langle\cdot,\cdot\rangle_{\mathrm{conn}} = \langle\cdot,\cdot\rangle_{\mathcal{H}_p^{\mathrm{lift}}}\) gilt. Eine Formulierung „\(C_p^{\mathrm{rel}}\) ist isometrisch" ohne Angabe der Quellnorm ist unvollständig und zirkulär, solange \(\langle\cdot,\cdot\rangle_{\mathrm{conn}}\) selbst die offene Größe ist.

**Kritische Warnung:** Die Orthogonalität verschiedener Edge-Label-Räume \(H_{m\to pm} \perp H_{m'\to p'm'}\) impliziert für sich allein **keine** Orthogonalität verschiedener Fouriermoden \(e_u V_p\). Der Index \(u\) ist ein Fourierindex *innerhalb* eines Kanals; \((m,p)\) sind Kantenlabels im *Zielraum*. Ohne (D.0.5.1) kann aus der Edge-Label-Zerlegung kein Wert für \(\langle e_0 V_p, e_u V_p\rangle_{\mathrm{conn}}\) abgeleitet werden.

**Status:** ❓[O] — Quell/Ziel-Identifikation nicht bewiesen.

---

#### D.0.5.B — Positiv definiter Fall

**Voraussetzungen dieses Abschnitts:**

- Die verbundene Paarung induziert (über den Pullback D.0.5.1) eine **positive definite Hermiteform** \(\langle\cdot,\cdot\rangle_{\mathrm{conn}}\) auf \(\mathcal{H}_p^{\mathrm{lift}}\). — ❓[O]
- \(\|v_p\|_{\mathrm{conn}} = 1\) (verbundene Normierungsannahme; folgt nicht automatisch aus \(\|v_p\|_{\mathfrak{p}_N} = 1\), solange der Konventionstransfer aus NEU-41 §3 offen ist). — ⚠[Konventionstransfer offen]
- \(\mathcal{H}_p^{\mathrm{lift}}\) ist bezüglich \(\|\cdot\|_{\mathrm{conn}}\) vollständig; andernfalls wird in der Hilbertvervollständigung \(\widehat{\mathcal{H}}_{p,\mathrm{conn}}^{\mathrm{lift}}\) gearbeitet. — ❓[O]

Unter diesen Voraussetzungen definiert \(\langle\cdot,\cdot\rangle_{\mathrm{conn}}\) zunächst eine Prähilbertstruktur auf \(\mathcal{H}_p^{\mathrm{lift}}\). Bezeichne mit

\[
K_{p,\mathrm{conn}}^{\mathrm{ch}}
:= \overline{E_p^{\mathrm{ch}}}^{\,\widehat{\mathcal{H}}_{p,\mathrm{conn}}^{\mathrm{lift}}}
\]

den Abschluss von \(E_p^{\mathrm{ch}}\) in dieser Vervollständigung. Dann ist die Orthogonalprojektion \(P_{K_{p,\mathrm{conn}}^{\mathrm{ch}}}^{\mathrm{conn}}\) ohne weitere Voraussetzung definiert.

Für alle \(k \in E_p^{\mathrm{ch}}\) gilt:

\[
\|v_p + k\|_{\mathrm{conn}}^2
= 1 + 2\operatorname{Re}\langle v_p, k\rangle_{\mathrm{conn}}
+ \|k\|_{\mathrm{conn}}^2.
\]

**Satz (positiv definiter Fall):**

\[
\boxed{
\mathcal{L}_p^{\mathrm{ch}} = \varnothing
\quad\Longleftrightarrow\quad
v_p \perp E_p^{\mathrm{ch}},
}
\]

äquivalent zu \(P_{K_{p,\mathrm{conn}}^{\mathrm{ch}}}^{\mathrm{conn}} v_p = 0\).

*Beweis.*

**Zunächst** (\(v_p \perp E_p^{\mathrm{ch}} \Rightarrow \mathcal{L}_p^{\mathrm{ch}} = \varnothing\)):
Ist \(\langle v_p, k\rangle_{\mathrm{conn}} = 0\) für alle \(k \in E_p^{\mathrm{ch}}\), so gilt

\[
\|v_p + k\|_{\mathrm{conn}}^2 = 1 + \|k\|_{\mathrm{conn}}^2.
\]

Die Normierungsbedingung erzwingt \(\|k\|_{\mathrm{conn}}^2 = 0\), also \(k = 0\). Kein geladener normierter Lift existiert.

**Umgekehrt** (\(v_p \not\perp E_p^{\mathrm{ch}} \Rightarrow \mathcal{L}_p^{\mathrm{ch}} \neq \varnothing\)):
Sei \(w \in E_p^{\mathrm{ch}}\) mit \(\langle v_p, w\rangle_{\mathrm{conn}} \neq 0\). Wähle \(\eta \in \mathbb{T}\) so, dass

\[
c := \operatorname{Re}\langle v_p,\, \eta w\rangle_{\mathrm{conn}} \neq 0,
\]

und setze \(\widetilde{w} := \eta w \in E_p^{\mathrm{ch}}\). Definiere

\[
t_0 := -\frac{2c}{\|\widetilde{w}\|_{\mathrm{conn}}^2} \neq 0.
\]

Dann gilt:

\[
\|v_p + t_0 \widetilde{w}\|_{\mathrm{conn}}^2
= 1 + 2t_0 c + t_0^2 \|\widetilde{w}\|_{\mathrm{conn}}^2
= 1 - \frac{4c^2}{\|\widetilde{w}\|^2} + \frac{4c^2}{\|\widetilde{w}\|^2}
= 1.
\]

Damit ist \(v_p + t_0 \widetilde{w}\) ein geladener normierter Lift mit \(t_0 \widetilde{w} \in E_p^{\mathrm{ch}} \setminus \{0\}\). \(\square\)

Falls zusätzlich \(K_p = K_{p,\mathrm{conn}}^{\mathrm{ch}}\) gilt (s. offene Punkte 4a/4b), darf \(K_p\) an die Stelle von \(E_p^{\mathrm{ch}}\) bzw. \(K_{p,\mathrm{conn}}^{\mathrm{ch}}\) gesetzt werden.

---

#### D.0.5.C — Eindimensionaler Modentest

Für eine einzelne Richtung \(k = a\, e_u V_p\) mit \(u \neq 0\), \(a \in \mathbb{C}\), seien

\[
g_{00}^{(p)} := \langle v_p, v_p\rangle_{\mathrm{conn}},\quad
g_{uu}^{(p)} := \langle e_u V_p, e_u V_p\rangle_{\mathrm{conn}},\quad
g_{0u}^{(p)} := \langle v_p, e_u V_p\rangle_{\mathrm{conn}}
\]

(alle drei nur definiert unter dem Pullback D.0.5.1; Linearitätskonvention noch offen).
Die Normierungsbedingung lautet konventionsfrei:

\[
2\operatorname{Re}\langle v_p,\, a\,e_u V_p\rangle_{\mathrm{conn}}
+ |a|^2\, g_{uu}^{(p)} = 0,
\tag{D.0.5.3}
\]

bei \(g_{00}^{(p)} = 1\) (verbundene Normierungsannahme). Je nach Konvention:

\[
\text{Zweites Argument linear: }
2\operatorname{Re}\!\bigl(a\, g_{0u}^{(p)}\bigr) + |a|^2 g_{uu}^{(p)} = 0;
\tag{D.0.5.3a}
\]

\[
\text{Erstes Argument linear: }
2\operatorname{Re}\!\bigl(\bar{a}\, g_{0u}^{(p)}\bigr) + |a|^2 g_{uu}^{(p)} = 0.
\tag{D.0.5.3b}
\]

Das Existenzkriterium ist von dieser Konvention **unabhängig**:

**Folgerung:** Unter den Voraussetzungen von D.0.5.B (insbesondere \(g_{uu}^{(p)} > 0\), was für \(e_u V_p \neq 0\) aus positiver Definitheit folgt):

\[
\exists\, a \neq 0 \text{ mit } \|v_p + a\,e_u V_p\|_{\mathrm{conn}} = 1
\quad\Longleftrightarrow\quad
g_{0u}^{(p)} \neq 0.
\]

- Bei \(g_{0u}^{(p)} = 0\): Einzige Lösung von (D.0.5.3) ist \(a = 0\).
- Bei \(g_{0u}^{(p)} \neq 0\): Die Lösungsmenge bildet einen Kreis durch \(a = 0\); jeder Punkt \(a \neq 0\) auf diesem Kreis liefert einen geladenen normierten Lift.

**Statusübersicht:**

| Größe | Wert | Quelle | Epistemischer Status |
|---|---|---|---|
| \(g_{00}^{(p)}\) | \(1\) unter verbundener Normierungsannahme | NEU-44 §44.2 + Konventionstransfer | ⚠[Konventionstransfer offen] |
| \(g_{uu}^{(p)}\), \(u \neq 0\) | \(> 0\) unter pos. def. Annahme; sonst unbekannt | NEU-41 §3 | ❓[O] |
| \(g_{0u}^{(p)}\) | unbekannt | NEU-41 §3 + Pullback (D.0.5.1) | ❓[O] |

---

#### D.0.5.D — Semidefinite Alternative

Falls \(\langle\cdot,\cdot\rangle_{\mathrm{conn}}\) lediglich positiv semidefinit ist, muss der Nullraum

\[
N_{\mathrm{conn}} := \{x : \|x\|_{\mathrm{conn}} = 0\}
\]

bestimmt werden. Für \(k \in E_p^{\mathrm{ch}} \cap N_{\mathrm{conn}}\) verschwinden alle Cross-Terme automatisch (Cauchy-Schwarz für semidefinite Formen):

\[
|\langle x, k\rangle_{\mathrm{conn}}|^2 \leq q_{\mathrm{conn}}(x)\cdot q_{\mathrm{conn}}(k) = 0.
\]

Daher gilt \(q_{\mathrm{conn}}(v_p + \lambda k) = q_{\mathrm{conn}}(v_p) = 1\) für alle \(\lambda \in \mathbb{C}\). Die normierte Fourier-Liftfaser enthält dann eine ganze affine Linie:

\[
\{v_p + \lambda k : \lambda \in \mathbb{C}\} \subseteq \mathcal{L}_p^{\mathrm{full}},
\]

deren punktierter Anteil

\[
\{v_p + \lambda k : \lambda \in \mathbb{C}^\times\} \subseteq \mathcal{L}_p^{\mathrm{ch}}
\]

eine nichttriviale geladene Liftfaser liefert — auch ohne \(g_{0u}^{(p)} \neq 0\).

**Konsequenz:** \(g_{uu}^{(p)} > 0\) darf nicht ohne Definitheitsnachweis vorausgesetzt werden.

**Status:** ❓[O] — semidefiniter Fall nicht ausgeschlossen.

---

#### D.0.5.E — Status und Lokalisierung

Der kanonische Lift \(v_p = e_0 V_p\) liegt stets in \(\mathcal{L}_p^{\mathrm{full}}\) (sofern \(\|v_p\|_{\mathrm{conn}} = 1\)). Die Faser \(\mathcal{L}_p^{\mathrm{full}}\) ist nichtleer; \(\mathcal{L}_p^{\mathrm{ch}}\) kann leer sein.

Noch offen:

1. **Pullback-Typprüfung:** Induziert \(\operatorname{Tr}^{\mathrm{conn}}_{W_{\mathrm{res}}}(x^\#y)\) eine Hermiteform auf \(\mathcal{H}_p^{\mathrm{lift}}\) via (D.0.5.1)? — ❓[O]
2. **Positivität/Definitheit** dieser induzierten Form. — ❓[O]
3. **Vollständigkeit** von \(\mathcal{H}_p^{\mathrm{lift}}\) bezüglich \(\|\cdot\|_{\mathrm{conn}}\). — ❓[O]
4. **Konventionstransfer** \(\|v_p\|_{\mathrm{conn}} = 1\): erfordert \(\operatorname{Tr}^{\mathrm{conn}}(v_p^\# v_p) = 1\) in NEU-41. — ⚠[O]
5. **Kernvergleich** — zwei getrennte Topologiefragen:
   - 5a. \(K_p \stackrel{?}{=} \overline{E_p^{\mathrm{ch}}}^{\,\|\cdot\|_{\mathrm{lift}}}\) — ❓[O]
   - 5b. \(K_{p,\mathrm{conn}}^{\mathrm{ch}} = \overline{E_p^{\mathrm{ch}}}^{\,\|\cdot\|_{\mathrm{conn}}}\) — per Definition; ob \(K_p = K_{p,\mathrm{conn}}^{\mathrm{ch}}\), ist Normvergleichsfrage. — ❓[O]
6. **Projektionswert** \(P_{K_{p,\mathrm{conn}}^{\mathrm{ch}}}^{\mathrm{conn}} v_p\) bzw. die Familie \(g_{0u}^{(p)}\) für \(u \neq 0\). — ❓[O]
7. **Im semidefiniten Fall:** Schnitt \(E_p^{\mathrm{ch}} \cap N_{\mathrm{conn}}\). — ❓[O]

**Hauptergebnis §153.D.0.5:**

\[
\boxed{
\text{Im positiv definiten Fall: }
\mathcal{L}_p^{\mathrm{ch}} = \varnothing
\iff
v_p \perp E_p^{\mathrm{ch}},
}
\]

äquivalent zu \(P_{K_{p,\mathrm{conn}}^{\mathrm{ch}}}^{\mathrm{conn}} v_p = 0\).

Die Edge-Label-Orthogonalität von \(W_{\mathrm{res,rel}}\) entscheidet diese Frage **nicht** ohne Pullback (D.0.5.1). Der nächste Beweisschritt ist die Typ- und Positivitätsprüfung der verbundenen Form auf \(\mathcal{H}_p^{\mathrm{lift}}\) (NEU-41 §3), dann die Bestimmung von \(P_{K_{p,\mathrm{conn}}^{\mathrm{ch}}}^{\mathrm{conn}} v_p\).

---

## 153.D — Falsifikationstest (korrigiert)

> **Hinweis:** Dieser Abschnitt setzt voraus, dass §153.D.0 positiv abgeschlossen ist, insbesondere dass \(\mathcal{L}_p \neq \emptyset\) (D.0.I) und \(T_{\widehat{\varepsilon}_p}\mathcal{L}_p \neq \{0\}\) (D.0.III) bekannt sind. Alle folgenden Tests sind **bedingt auf D.0.I, D.0.III**.

### D.1 — Zulässiger Ausgangslift

Verwende einen Lift der Form (D.0.1):

\[
\widehat{\varepsilon}_p = e_0 V_p + a_{p,u} e_u V_p, \qquad a_{p,u} \neq 0,
\]

der die Normierungsbedingung (D.0.2) erfüllt. Dessen Existenz muss durch D.0.I gesichert sein.

### D.2 — Test auf 153.A: Zulässiger Tangentialvektor

Nehme \(h \in T_{\widehat{\varepsilon}_p}\mathcal{L}_p\) (bekannt nach D.0.III), d.h.

\[
\pi_{\mathrm{prim}}(h) = 0, \qquad \operatorname{Re}\langle \widehat{\varepsilon}_p, h\rangle_{\mathrm{conn}} = 0.
\]

Berechne:

\[
D_p(h) = \Pi_{W_{\mathrm{res}}} \widetilde{\omega}_2(h, L_3^\circ).
\]

Falls \(h = e_{u'} V_p\) mit \(u' \neq 0\), dann:

\[
D_p(e_{u'} V_p) = -\log(p) \sum_{s,m} u' s \,\ell_{s,m}\, \Pi_{W_{\mathrm{res}}}(e_{u'+ps} V_{pm}).
\tag{D.2.1}
\]

Die Labelabbildung \((s,m) \mapsto (u'+ps, pm)\) ist injektiv — keine Kollision verschiedener \((s,m)\) für dasselbe Label. Es gibt also keine **interne** Auslöschung innerhalb dieser Summe.

**Bedingter Befund \(D_p(h) \neq 0\):**

\[
D_p(h) \neq 0
\quad\Longleftrightarrow\quad
\exists\, (s_0, m_0):\ s_0 \neq 0,\ \ell_{s_0,m_0} \neq 0,\ \Pi_{W_{\mathrm{res}}}(e_{u'+ps_0} V_{pm_0}) \neq 0.
\tag{D.2.2}
\]

**Status von D.2.2:** ⚠[bedingt] — Die Existenz eines solchen Paares \((s_0, m_0)\) ist noch zu belegen. Erst dann ist \(D_p(h) \neq 0\) gesichert, und 153.A widerlegt.

### D.3 — Test auf 153.B mit renormierter Faserkurve

Verwende eine echte Faserkurve \(\widehat{\varepsilon}_p(t) = \widehat{\varepsilon}_p + th + t^2 k + O(t^3) \in \mathcal{L}_p\) mit \(h \in T_{\widehat{\varepsilon}_p}\mathcal{L}_p\) und \(k\) bestimmt durch (D.0.4). Die zu prüfende Größe ist

\[
|c_p(t)|^2 = \|\Psi_p(\widehat{\varepsilon}_p(t))\|^2_{W_{\mathrm{res}}}
= \|A_p + t D_p(h) + t^2 D_p(k) + O(t^3)\|^2.
\]

In erster Ordnung:

\[
\frac{d}{dt}|c_p(t)|^2\big|_{t=0}
= 2\operatorname{Re}\langle A_p, D_p(h)\rangle_{W_{\mathrm{res}}}.
\tag{D.3.1}
\]

In zweiter Ordnung (falls (D.3.1) verschwindet):

\[
\frac{d^2}{dt^2}|c_p(t)|^2\big|_{t=0}
= 2\|D_p(h)\|^2_{W_{\mathrm{res}}} + 2\operatorname{Re}\langle A_p, D_p(k)\rangle_{W_{\mathrm{res}}}.
\tag{D.3.2}
\]

Norminvarianz (153.B) bedeutet: alle Ableitungen (D.3.1), (D.3.2), \ldots verschwinden für alle zulässigen Richtungen \(h\).

**Wichtig:** Das in der Vorversion verwendete Argument \(Q''(0) = 2(d - a\beta) \neq 0\) *generisch* ist **kein Beweis** und darf nicht als \checkmark[M] markiert werden. Die Aussage bleibt:

\[
\boxed{153.B\ \text{erscheint nicht automatisch; Entscheidung offen.}}
\]

**Status von §153.D gesamt:** ⚠[bedingt auf D.0.I, D.0.III, D.2.2]

---

## 153.E — Verhältnis der Aussagen

| Aussage | Inhalt | Stärke | Status |
|---|---|---|---|
| **153.A** | Starke Vektorinvarianz: \(\Psi_p' = \Psi_p\) | stärkste | ❓[O] |
| **153.B** | Schwache Norminvarianz: \(\|\Psi_p'\| = \|\Psi_p\|\) | mittlere | ❓[O] |
| **153.C** | Differenzformel (153.1) | Identität | ✅[M] |
| **153.D.0** | Geometrie der Hebungsfaser \(\mathcal{L}_p\) | Voraussetzung | ❓[O] — 4 Prüffragen offen |
| **153.D.0.5** | Hilbertgeometrische Entscheidung | Satz im pos. def. Fall | ✅[M] bedingt; Voraussetzungen ❓[O] |
| **153.D** | Falsifikationstest | bedingt auf D.0 | ⚠[bedingt] |

Implikation: \(153.A \Rightarrow 153.B\). Umkehrung gilt nicht.

---

## 153.F — Mögliche Ausgänge

| Ausgang | Inhalt | Konsequenz für NEU-152 |
|---|---|---|
| **I** | \(D_p(h) = 0\) für alle zulässigen \(h\) | \(|c_p|^2\) intrinsisch; NEU-152 unbedingt formulierbar |
| **II** | \(D_p(h) \neq 0\), aber \(|c_p(t)|^2 = \mathrm{const}\) längs \(\mathcal{L}_p\) | \(|c_p|^2\) wohldefiniert; NEU-152 formulierbar |
| **III** | Kanonische Hebung \(\widehat{\varepsilon}_p^{\mathrm{can}}\) explizit fixiert | \(|c_p|^2\) hebungsrelativ; NEU-152 bedingt mit Vorbehalt |
| **IV** | Weder Invarianz noch kanonische Wahl | \(|c_p|^2\) kein intrinsisches Primgewicht; NEU-152 vorläufig blockiert |

**Aktueller Stand:** Ausgang **IV** — kein Beweis von I/II, keine fixierte kanonische Hebung.

---

## 153.G — Rückwirkung auf Nachfolgeblätter

**NEU-152:** Alle Aussagen zur Nichtentartung \(|c_p|^2 \gtrsim (\log p)^2/p\) sind bis zum Abschluss von NEU-153 entweder hebungsrelativ oder bedingt. NEU-152 enthält einen Abhängigkeitsverweis (§152.6).

**NEU-150 (R-Cutoff):** Die Zusatzannahme [ZA]: \(R_p \asymp p/\log p\) setzt zweiseitige Kontrolle von \(|c_p|^2\) voraus. Ebenfalls hebungsrelativ, solange NEU-153 offen ist.

**Kein Eingriff in NEU-44:** Das Grundlagenblatt bleibt reines Definitions- und Konventionsblatt.

---

## Verweise

- **NEU-41** §3: Wohlbestimmtheitsbedingung (41.4), \(\delta_{r,0}\)-Regel, verbundene Paarung — direkte Quellen für §153.D.0.5  
- **NEU-41** §2: Verschwindung von \(\widetilde{\omega}_2(e_0 V_p, L_3^\circ)\) — Gründe für (D.0.1)  
- **NEU-41** §12: Minimaler Testfall (nur nach Klärung von D.0 verwendbar)  
- **NEU-44**: Metrikdaten \(\|e_r V_p\|_{\mathrm{conn}}\), \(\langle e_0 V_p, e_u V_p\rangle_{\mathrm{conn}}\) — Quell/Ziel-Identifikation offen  
- **NEU-128B** §6: Status ❓[O] für Hebungsunabhängigkeit  
- **NEU-152** §152.6: Abhängigkeitsverweis (Vorrangbarriere)
