# NEU-243 — Kompatibilitätsfirewall für neue Quell- und Zielkomplexe

**Datum:** 27. Juli 2026  
**Quellenblock:** NEU-221e, NEU-226, NEU-227, NEU-229 (via NEU-242)  
**Vorgänger:** NEU-242 — Abschlussaudit [O-229-3B.1f-b.1], \(\checkmark[M]_{\mathrm{neg,Quelle}}\)

---

## Neuer Hauptknoten

$$
\boxed{[O\text{-}229\text{-}3B.1f\text{-}c\text{-compatible-nontrivial-chain-extension}]
\quad ?[O]_{\mathrm{offen}}.}
$$

Gesucht ist **nicht** lediglich irgendeine formale Komplexstruktur, sondern eine intrinsische und nichttriviale Erweiterung

$$
F^\bullet:
(C_{p,\mathrm{lift}}^\bullet, d_{\mathrm{lift}})
\longrightarrow
(C_{p,\mathrm{tar}}^\bullet, d_{\mathrm{tar}}),
$$

mit einer ausgezeichneten Komponente

$$
F^r = Q_{\mathrm{Wres,rel}} \circ T_p^{\mathrm{raw}}
$$

bzw., im Prequotient-first-Zweig,

$$
F^r = T_p^{\mathrm{raw}},
$$

aus der ein typisiertes kohomologisches Randdatum gewonnen werden kann.

---

## 1. Quellengegebenes Typinventar

### 1.1 Liftseite

Quellengegeben (aus NEU-221e, NEU-229) sind:

$$
\pi_{\mathrm{prim},p}^{-1}(\varepsilon_p)
$$

eine **affine Liftfaser** — daher definitiv kein lineares Gradstück eines Differentialkomplexes.

Lineare Kandidaten:

$$
K_p^{\mathrm{alg}}, \qquad \mathcal{D}(a_p) \subseteq K_p^{\mathrm{alg}}, \qquad \mathbb{C}e_p \oplus K_p^{\mathrm{alg}},
$$

sowie Nullraum und Quotientenvervollständigung:

$$
N_{a_p} = \{k \in \mathcal{D}(a_p) : a_p(k,k)=0\},
\qquad
H_{a,p} = \overline{\mathcal{D}(a_p)/N_{a_p}}^{\,a_p}.
$$

**Typpräzisierung:** Der algebraische Definitionsbereich
$$
\mathcal{D}_p^{\mathrm{lift}} \subseteq \operatorname{Dom}\pi_{\mathrm{prim},p} \cap \operatorname{Dom}T_p^{\mathrm{raw}}
$$
ist als Schnitt von Definitionsbereichen linear, soweit $T_p^{\mathrm{raw}}$ auf ihm als linear angegeben wird. Der Quellenblock liefert jedoch noch **keine ausgezeichnete lineare und topologische Typisierung** von $\mathcal{D}_p^{\mathrm{lift}}$ als Gradstück eines Komplexes. Festzuhalten ist lediglich: Die **affine** normierte Liftfaser $\pi_{\mathrm{prim},p}^{-1}(\varepsilon_p)$ ist kein Gradstück.

Der Quellenblock liefert **keine** ausgezeichnete Gradzuweisung, kein Differential und keine Kettenstruktur auf diesen Objekten.

### 1.2 Zielseite

Quellengegeben (aus NEU-221e, NEU-226, NEU-229) sind:

$$
\mathscr{V}_{\mathrm{rel},p,N}^{\mathrm{pre}}, \qquad \mathcal{N}_{\mathrm{Wres,rel}},
$$

$$
\mathscr{V}_{\mathrm{rel},p,N}^{\mathrm{pre}} / \mathcal{N}_{\mathrm{Wres,rel}}, \qquad \mathcal{H}_{\mathrm{rel},p,N},
$$

sowie

$$
\overline{\operatorname{Ran}T_p^{\mathrm{raw}}} \subseteq \mathcal{H}_{\mathrm{rel},p,N}.
$$

Der Quellenblock liefert weder eine Graduierung noch ein Differential auf diesen Räumen.

---

## 2. Architekturentscheidung auf der Zielseite

Vor der Konstruktion eines Differentials ist zwischen zwei **nicht äquivalenten** Architekturen zu entscheiden.

### Typ A — Quotient-first

$$
C_{p,\mathrm{tar}}^{r+s} := \mathscr{V}_{\mathrm{rel},p,N}^{\mathrm{pre}} / \mathcal{N}_{\mathrm{Wres,rel}}.
$$

Ein Differential $\bar{d}_{\mathrm{tar}}$ wird **unmittelbar auf dem Quotienten** definiert.

In diesem Zweig ist **keine** Radikalstabilität eines Rohdifferentials vorausgesetzt; es gibt kein Differential auf $\mathscr{V}^{\mathrm{pre}}$.

### Typ B — Prequotient-first

Ein Differential
$$
d_{\mathrm{pre}}: \mathscr{V}_{\mathrm{rel},p,N}^{\mathrm{pre},n} \longrightarrow \mathscr{V}_{\mathrm{rel},p,N}^{\mathrm{pre},n+1}
$$
wird zunächst auf einem **graduierten Rohzielraum** definiert.

Damit es auf den Wres-Quotienten absteigt, ist **notwendig**:

$$
d_{\mathrm{pre}}\,\mathcal{N}_{\mathrm{Wres,rel}}^n \subseteq \mathcal{N}_{\mathrm{Wres,rel}}^{n+1}.
$$

Erst dann entsteht ein induziertes Differential $[d_{\mathrm{pre}}v]$ auf dem Quotienten.

Die Radikalstabilitätsbedingung ist damit **keine architekturunabhängige Minimalbedingung** — sie gehört ausschließlich zum Prequotient-first-Zweig (Typ B).

---

## 3. Nichttrivialitätsfirewall

### 3.1 Die triviale Lösung ist kein Abschluss

Die Setzungen

$$
d_{\mathrm{lift}} = 0, \qquad d_{\mathrm{tar}} = 0
$$

erzeugen formal Komplexe und machen **jede** lineare Abbildung zu einer Kettenabbildung:

$$
d_{\mathrm{tar}} \circ T_p^{\mathrm{raw}} = F^{r+1} \circ d_{\mathrm{lift}} = 0. \qquad \checkmark\ (\text{formal})
$$

Sie lösen jedoch den Randdatenknoten **nicht**. Ein derart konstruierter Mapping Cone enthielte keinerlei neue arithmetische, kohomologische oder analytische Information und erzeugte insbesondere nicht automatisch

$$
b_p, \qquad \beta_p, \qquad \Lambda_p \quad\text{oder}\quad \tau_p.
$$

Ebenso gilt: Eine beliebige Gradbezeichnung $r, s \in \mathbb{Z}$ ist formal möglich, aber **ohne intrinsische Motivation** und ohne nichttriviale Differentiale mathematisch noch keine relevante Brückenarchitektur. Schicht I (Gradzuweisung) gilt daher erst dann als abgeschlossen, wenn sie intrinsisch motiviert ist.

### 3.2 Nichttrivialitätskriterien

Eine zulässige Konstruktion muss mindestens **eines** der folgenden Kriterien erfüllen:

**(NT1)** Das Differential entsteht **intrinsisch** aus bereits motivierten algebraischen, Hochschild-, zyklischen, modularen oder operatorischen Daten.

**(NT2)** Die relevante Kohomologie ist nicht lediglich der unveränderte gesamte Gradraum:
$$
H^n(C^\bullet, d) \neq C^n \qquad \text{für mindestens einen relevanten Grad } n.
$$

**(NT3)** Die Konstruktion liefert eine typisierte Transgression oder Randabbildung
$$
\tau_p: H^r(C_{p,\mathrm{lift}}^\bullet) \longrightarrow \mathcal{D}(a_p)^*
$$
oder ein äquivalentes Objekt.

**(NT4)** Das erzeugte Funktional faktorisiert durch den Rohoperator:
$$
\Lambda_p \circ T_p^{\mathrm{raw}}, \qquad \text{mit} \quad |\Lambda_p| \le \sqrt{\alpha_p}.
$$

**(NT5)** Die Konstruktion verwendet weder $\beta_p$, $b_p$, $\Lambda_p$ noch die gewünschte Determinanten- oder $\Xi$-Identität als **nachträglich eingepasste** Eingabedaten.

---

## 4. Neue Teilknoten

### Teilknoten c.1 — Zielarchitektur

$$
\boxed{[O\text{-}229\text{-}3B.1f\text{-}c.1\text{-target-complex-architecture}]
\quad ?[O]_{\mathrm{offen}}.}
$$

Zu entscheiden ist: Wird der Zielkomplex nach **Typ A (quotient-first)** oder **Typ B (prequotient-first)** konstruiert?

- Im Typ-A-Zweig: direktes Differential $\bar{d}_{\mathrm{tar}}$ auf $\mathscr{V}^{\mathrm{pre}}/\mathcal{N}_{\mathrm{Wres,rel}}$, keine Radikalstabilitätspflicht.
- Im Typ-B-Zweig: Differential $d_{\mathrm{pre}}$ auf dem Rohraum, **zusätzlich zu beweisen:**
$$
d_{\mathrm{pre}}\,\mathcal{N}_{\mathrm{Wres,rel}} \subseteq \mathcal{N}_{\mathrm{Wres,rel}}.
$$

In beiden Zweigen gilt die Nichttrivialitätsfirewall (Abschnitt 3).

### Teilknoten c.2 — Quellkomplex

$$
\boxed{[O\text{-}229\text{-}3B.1f\text{-}c.2\text{-intrinsic-lift-complex}]
\quad ?[O]_{\mathrm{offen}}.}
$$

Zu konstruieren ist ein linearer, graduierter Quellkomplex mit einem relevanten Gradstück

$$
C_{p,\mathrm{lift}}^r \subseteq K_p^{\mathrm{alg}} \quad\text{oder}\quad C_{p,\mathrm{lift}}^r \subseteq \mathcal{D}(a_p),
$$

samt $d_{\mathrm{lift}}^2 = 0$ und intrinsischer Motivation (NT1).

Zusätzlich sind zu prüfen:
- **Definitionsbereichsstabilität:** $d_{\mathrm{lift}}(C_{p,\mathrm{lift}}^r) \subseteq C_{p,\mathrm{lift}}^{r+1}$.
- **Formkontrolle** (falls analytisch benötigt): Ist $d_{\mathrm{lift}}$ formbeschränkt bezüglich $a_p$?

Die affine Liftfaser $\pi_{\mathrm{prim},p}^{-1}(\varepsilon_p)$ scheidet als Gradstück aus.

### Teilknoten c.3 — Kettenabbildungserweiterung

$$
\boxed{[O\text{-}229\text{-}3B.1f\text{-}c.3\text{-chain-map-extension}]
\quad ?[O]_{\mathrm{offen}}.}
$$

Zu konstruieren sind weitere Komponenten $F^n$, sodass die Kettenabbildungsidentität

$$
d_{\mathrm{tar}} \circ F^n = F^{n+1} \circ d_{\mathrm{lift}}
$$

gilt, und im ausgezeichneten Grad

$$
F^r = Q_{\mathrm{Wres,rel}} \circ T_p^{\mathrm{raw}}.
$$

Als **notwendige Konsequenz** der Kettenabbildungsidentität im Grad $r$ folgt für
$x \in (T_p^{\mathrm{raw}})^{-1}(\mathcal{N}_{\mathrm{Wres,rel}})$:

$$
F^{r+1} \circ d_{\mathrm{lift}}\,x = d_{\mathrm{tar}} \circ F^r\,x = d_{\mathrm{tar}}[0] = 0,
$$

woraus folgt:

$$
d_{\mathrm{lift}}\bigl((T_p^{\mathrm{raw}})^{-1}(\mathcal{N}_{\mathrm{Wres,rel}})\bigr) \subseteq \ker F^{r+1}.
$$

Diese Bedingung ist **kein eigenständiger Ersatz** für die Konstruktion von $F^{r+1}$, sondern eine notwendige Folge einer vollständigen Kettenabbildung. Sie kann jedoch als **Konsistenztest** für einen Kandidaten $F^{r+1}$ dienen.

### Teilknoten c.4 — Randdatenausgabe

$$
\boxed{[O\text{-}229\text{-}3B.1f\text{-}c.4\text{-boundary-transgression-output}]
\quad ?[O]_{\mathrm{offen}}.}
$$

Zu beweisen ist, dass die neue Komplexarchitektur tatsächlich ein **nichtverschwindendes und typisiertes Randdatum** erzeugt:

$$
\tau_p, \qquad b_p, \qquad \beta_p \quad\text{oder}\quad \Lambda_p,
$$

mit der analytischen Schranke

$$
|\beta_p(k)|^2 \le a_p(k,k).
$$

Dieses Kriterium entspricht (NT3) und (NT4) der Nichttrivialitätsfirewall.

---

## 5. Knotenabhängigkeiten

```
[c.1] Zielarchitektur-Entscheidung
    ↓ (bestimmt den Typ des Differentials auf der Zielseite)
[c.2] Quellkomplex-Konstruktion
    ↓ (bestimmt d_lift und die Liftstruktur)
[c.3] Kettenabbildungserweiterung F^•
    ↓ (setzt c.1 und c.2 voraus)
[c.4] Randdatenausgabe
    ↓ (setzt vollständiges F^• voraus)
[b.2] Mapping Cone — noch blockiert
    ↓
[b.3] — noch blockiert
```

Ein Mapping Cone darf erst nach Abschluss von [c.1], [c.2] und [c.3] konstruiert werden.

---

## 6. Gesamtstatus

Die vorhandenen Typen **widersprechen** einer zukünftigen Kettenabbildungserweiterung nicht.

Sie **erzwingen** jedoch noch keine solche Erweiterung und bestimmen weder die Grade noch die Differentiale.

$$
\boxed{[O\text{-}229\text{-}3B.1f\text{-}c] \quad ?[O]_{\mathrm{offen}}.}
$$

Die bloße Wahl von Nulldifferentialen gilt **nicht** als Lösung von [c], solange daraus kein intrinsisches Randdatum gemäß [c.4] entsteht.

---

## 7. Blockadestatus der Folgeknoten

$$
\boxed{[O\text{-}229\text{-}3B.1f\text{-}b.2] \quad ?[O]_{\mathrm{blockiert}}: \text{wartet auf [c.1]+[c.2]+[c.3]}.}
$$

$$
\boxed{[O\text{-}229\text{-}3B.1f\text{-}b.3] \quad ?[O]_{\mathrm{blockiert}}: \text{wartet auf [b.2]}.}
$$
