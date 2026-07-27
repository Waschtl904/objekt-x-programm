# NEU-229 — Intrinsische verbundene Form und Mischblock: Gram-Geometrie der Hebungsfaser

**Katalog-ID:** NEU-229
**Knoten:** `[O-229-1-intrinsic-connected-form-and-mixed-Gram-block]`
**Stand:** 27. Juli 2026
**Vorgänger:** NEU-228
**Ergebnis:** $B_p^{\mathrm{raw}}$ kann nicht die vollständige verbundene Form sein. Die blockdiagonale Reparatur
ist strukturell ungeeignet. Der Rohkopplungs-Kernblock ist partiell kontrolliert. Die entscheidende
Primärdefinition des intrinsischen Mischblocks $\beta_p$ fehlt weiterhin.

---

## 0. Auditurteil

$$
\boxed{\ [O\text{-}229\text{-}1\text{-intrinsic-connected-form-and-mixed-Gram-block}]
\quad \checkmark[M]_{\mathrm{neg,Quelle}} \ }
$$

**Umfang:** Dieses Urteil betrifft die Konstruktion der vollständigen verbundenen Form aus der
gegenwärtigen Architektur. Der Rohkopplungs-Kernblock bleibt als partiell geschlossener Baustein
erhalten. Das Urteil beweist nicht, dass kein intrinsischer Mischblock für Objekt $(X)$ existieren kann.

Vier Befunde:

1. **$B_p^{\mathrm{raw}}(e_p, e_p) = 0$ widerspricht $h_p(e_p,e_p)=1$** für jedes skalare Vielfache.
   `✓[M]_neg`
2. **Die blockdiagonale Reparatur $h_p^{\mathrm{dec}}$ erzeugt $\mathcal{L}_p = \emptyset$** im positiv
   definiten Kernblock. `✓[M]_neg`
3. **Rohkopplungs-Kernblock** $a_p^{\mathrm{raw}}$ ist positiv semidefinit; Radikal und Rang strukturell
   kontrolliert. `✓[M]_part` — `[O-229-1-α]`
4. **Intrinsischer Mischblock $\beta_p$** aus dem gegenwärtigen Quellenbestand nicht konstruierbar.
   `✓[M]_neg,Quelle` — `[O-229-1-β]`

---

## 1. Vorgängerknoten (geschlossen)

| Knoten | Aussage | Status |
|---|---|---|
| `[O-228-2a1]` | $h_p = \alpha_p B_p^{\mathrm{raw}}$ widerspricht Normierung | `✓[M]_neg` |
| `[O-228-2a1-blockdiag]` | Blockdiagonale Reparatur erzeugt $\mathcal{L}_p = \varnothing$ | `✓[M]_neg` |
| `[O-228-2a1-primary-Wres-computation]` | $\mathrm{Tr}^{\mathrm{conn}}_{W_{\mathrm{res}}}$ auf Fourier-Liftbasis nicht konstruktiv definiert | `✓[M]_neg,Quelle` |
| `[O-228-2a]` | Teilweise beantwortet — negativer Teil geschlossen, konstruktiver Teil offen | `✓[M]_part` |

---

## 2. Minimale Typisierung (Teil A)

### 2.1 Algebraischer Liftraum

Die vorhandenen Quellen bestimmen keinen abgeschlossenen Hilbertraum, auf dem gleichzeitig
$\pi_{\mathrm{prim},p}$, $T_p^{\mathrm{raw}}$, $\sharp$ und $h_p$ vollständig definiert sind.
Es wird mit einem algebraischen gemeinsamen Definitionsbereich gearbeitet:

$$
\mathcal{D}_p^{\mathrm{lift}} \subseteq \operatorname{Dom}\pi_{\mathrm{prim},p} \cap \operatorname{Dom}T_p^{\mathrm{raw}},
\qquad e_p \in \mathcal{D}_p^{\mathrm{lift}}, \quad \pi_{\mathrm{prim},p}(e_p) = \varepsilon_p \neq 0.
$$

Der minimale algebraische Kern ist

$$
K_p^{\mathrm{alg}} := \ker\!\left(\pi_{\mathrm{prim},p}\big|_{\mathcal{D}_p^{\mathrm{lift}}}\right),
\qquad \mathcal{V}_p^{\mathrm{alg}} := \mathbb{C}e_p \oplus K_p^{\mathrm{alg}}.
$$

Eine topologische Aussage $K_p = \overline{K_p^{\mathrm{alg}}}$ ist erst zulässig nach bewiesener
Stetigkeit bzw. Abgeschlossenheit von $\pi_{\mathrm{prim},p}$ (vgl. NEU-153, Stetigkeitsannahme).

### 2.2 Kernform

$$
a_p : \mathcal{D}(a_p) \times \mathcal{D}(a_p) \longrightarrow \mathbb{C}, \qquad \mathcal{D}(a_p) \subseteq K_p^{\mathrm{alg}},
$$

hermitesch und positiv semidefinit. Nullraum: $N_{a_p} := \{k \in \mathcal{D}(a_p) : a_p(k,k) = 0\}$.
Vervollständigung des Quotienten: $H_{a,p} := \overline{\mathcal{D}(a_p)/N_{a_p}}^{a_p}$.

### 2.3 Mischblock

$$
\beta_p : \mathcal{D}(a_p) \longrightarrow \mathbb{C}, \qquad \beta_p(k) := h_p(e_p, k),
$$

festgelegt sobald $h_p$ existiert. Positivität erzwingt $|\beta_p(k)|^2 \le a_p(k,k)$, daher muss
$\beta_p$ den Nullraum $N_{a_p}$ vernichten und stetig auf $H_{a,p}$ absteigen.

### 2.4 Vollständige Form

$$
h_p(ce_p + k,\, de_p + \ell)
= \bar{c}\,d + \bar{c}\,\beta_p(\ell) + \overline{\beta_p(k)}\,d + a_p(k,\ell),
$$

auf dem Formbereich $\mathbb{C}e_p \oplus \mathcal{D}(a_p)$.

---

## 3. `[O-229-1-α]` — Rohkopplungs-Kernblock

### 3.1 Definition

Sei $\mathcal{D}(a_p) \subseteq K_p \cap \operatorname{Dom}T_p^{\mathrm{raw}}$ und $\alpha_p > 0$ fest
(intrinsisch vorgegeben). Dann:

$$
a_p^{\mathrm{raw}}(k,\ell) := \alpha_p \left\langle T_p^{\mathrm{raw}}k,\, T_p^{\mathrm{raw}}\ell \right\rangle.
$$

### 3.2 Positivität

$a_p^{\mathrm{raw}}$ ist hermitesch und positiv semidefinit:

$$
a_p^{\mathrm{raw}}(k,k) = \alpha_p\,\|T_p^{\mathrm{raw}}k\|^2 \ge 0.
$$

### 3.3 Radikal

Bei definitem Zielskalarprodukt:

$$
\operatorname{Rad}(a_p^{\mathrm{raw}}) = \ker\!\left(T_p^{\mathrm{raw}}\big|_{\mathcal{D}(a_p)}\right).
$$

Bei entartetem oder erst zu quotierenden Zielraum gilt allgemeiner:

$$
\operatorname{Rad}(a_p^{\mathrm{raw}}) = \left\{ k \in \mathcal{D}(a_p) : T_p^{\mathrm{raw}}k \in \mathcal{N}_{\mathrm{Ziel}} \right\}.
$$

Für den $W_{\mathrm{res}}$-relativen Quotienten entsprechend:

$$
\operatorname{Rad}(a_p^{\mathrm{raw}}) = (T_p^{\mathrm{raw}})^{-1}\!\left(\mathcal{N}_{W_{\mathrm{res}},\mathrm{rel}}\right).
$$

Aus der Fourier-Multiplikationsstruktur (NEU-043, Formel 43.1)
$\widetilde{\omega}_2(e_u V_p, e_s V_m) = -us\log(p)\cdot e_{u+ps}V_{pm}$
folgt, dass $T_p^{\mathrm{raw}}$ auf geladenen Fouriermoden $e_u V_p \in K_p$ ($u \neq 0$) generisch
nicht verschwindet. Das Radikal ist daher im Fourier-generischen Fall trivial.

### 3.4 Nicht geschlossen

Nicht geschlossen durch diesen Teilknoten sind: kanonische Normierung von $\alpha_p$,
vollständige Abgeschlossenheit der Form, und $W_{\mathrm{res}}$-Quotientenabstieg.

$$
\boxed{\ [O\text{-}229\text{-}1\alpha] \quad \checkmark[M]_{\mathrm{part}} \ }
$$

**Umfang:** Geschlossen ist nur die Positivitäts- und Radikalstruktur des gewählten
Rohkopplungs-Kernblocks. Nicht bewiesen ist, dass dieser Kernblock die intrinsische verbundene Form
eindeutig oder vollständig bestimmt.

---

## 4. `[O-229-1-β]` — Intrinsischer Mischblock

### 4.1 Notwendige Faktorisierung

Eine positive hermitesche Erweiterung verlangt

$$
|\beta_p(k)|^2 \le a_p(k,k).
$$

Für den Rohkopplungs-Kernblock folgt daraus die notwendige Faktorisierung:

$$
\boxed{\ \beta_p(k) = \sqrt{\alpha_p}\,\langle b_p, T_p^{\mathrm{raw}}k \rangle, \qquad b_p \in \overline{\operatorname{Ran}T_p^{\mathrm{raw}}},\quad |b_p| \le 1. \ }
$$

Die Rohkopplungsform selbst liefert $b_p = 0$, also $\beta_p = 0$, da $T_p^{\mathrm{raw}}e_p = 0$.

### 4.2 Kandidaten-Audit (acht Mechanismen)

| Mechanismus | Befund |
|---|---|
| $W_{\mathrm{res}}$-Randpaarung $\operatorname{Tr}^{\mathrm{conn}}_{W_{\mathrm{res}}}(e_p^\sharp k)$ | Keine der sechs Anforderungen vollständig erfüllt; NEU-156: $x^\sharp y$ auf Liftraum nur formale Notation |
| Polarisation einer verbundenen quadratischen Form | Reproduziert nur bereits definierte Form; Rohpolarisation liefert $\beta_p = 0$ |
| KMS-/modularer Randterm $\varphi_\beta(\iota(e_p)^*\iota(k))$ | Einbettung $\iota$ und Quotientenverträglichkeit nicht primär definiert |
| Kopplung mit $L_3^\circ$ / Pullback via $T_p^{\mathrm{raw}}$ | Erzwingt $h_p(e_p,k)=0$; kanonischer Zielvektor $b_p$ nicht konstruiert |
| Intrinsische Variation der Rohform am Basispunkt $e_p$ | Linearer Variationsterm verschwindet; Variation an geladenen Lifts zirkulär |
| Feshbach-Selbstenergie / Weyl-Funktion | Setzt Hebungsgeometrie voraus; logisch nach Mischblock im DAG |
| Hochschild-/zyklische Paarung | Keine vollständig typisierte Kontraktion $K_p \to \mathbb{C}$ konstruiert |
| Primkanalprojektion / bedingte Erwartung | Verschwindet identisch auf $K_p$ (da $\pi_{\mathrm{prim},p}|_{K_p} = 0$) |

**Exakt fehlende Primärstruktur** (äquivalente Formulierungen):

$$
\beta_p(k) = h_p(e_p, k) \quad \text{für eine konstruktiv definierte verbundene Form } h_p,
$$

oder

$$
\beta_p(k) = \sqrt{\alpha_p}\,\langle b_p, T_p^{\mathrm{raw}}k \rangle \quad \text{für einen intrinsisch ausgezeichneten, nichtverschwindenden kontraktiven Vektor } b_p \in \overline{\operatorname{Ran}T_p^{\mathrm{raw}}}.
$$

$$
\boxed{\ [O\text{-}229\text{-}1\beta] \quad \checkmark[M]_{\mathrm{neg,Quelle}} \ }
$$

**Umfang:** Der Befund schließt nur die Konstruktion eines nichtverschwindenden Mischblocks aus dem
gegenwärtig gelesenen Quellenbestand. Er beweist nicht, dass kein intrinsischer Mischblock für
Objekt $(X)$ existieren kann.

---

## 5. `[O-229-1-γ]` — Positivitätsklassifikation

### 5.1 Formtheoretisches Schur-Kriterium (ohne Invertierbarkeitsannahme)

Direkte Minimierung in $c \in \mathbb{C}$ ergibt:

$$
\boxed{\ h_p \ge 0 \iff a_p \ge 0 \quad \text{und} \quad |\beta_p(k)|^2 \le a_p(k,k) \quad \forall k \in \mathcal{D}(a_p). \ }
$$

Das Minimum bezüglich $c$ wird bei $c = -\beta_p(k)$ angenommen mit Wert $a_p(k,k) - |\beta_p(k)|^2$.

### 5.2 Riesz-Darstellung

Nach dem Riesz-Satz existiert ein eindeutig bestimmter Vektor

$$
b_p \in H_{a,p}, \qquad |b_p|_{a,p} \le 1, \qquad \beta_p(k) = \langle b_p, [k] \rangle_{a,p}.
$$

### 5.3 Invertierbarkeit

Eine Verwendung von $A_p^{-1}$ ist nur nach bewiesener Invertierbarkeit zulässig. Allgemein ist mit
$\overline{\operatorname{Ran}A_p^{1/2}}$ bzw. der Moore-Penrose-Inversen $A_p^\dagger$ zu arbeiten:

$$
1 - \|A_p^{\dagger/2} b_p\|^2 \ge 0.
$$

Nur falls $A_p$ streng positiv und invertierbar: $1 - \langle b_p, A_p^{-1} b_p \rangle \ge 0$.

$$
\boxed{\ [O\text{-}229\text{-}1\gamma] \quad \checkmark[M] \ }
$$

---

## 6. `[O-229-1-δ]` — Geladene Liftfaser und Quotientenabstieg

### 6.1 Rein geometrische Nichtleerheit

Ist $h_p \ge 0$ und $\beta_p \neq 0$, so existiert auf dem Formniveau stets ein nichttrivialer
normierter Lift: Wähle $w$ mit $\beta_p(w) \neq 0$, Phase so dass $\operatorname{Re}\beta_p(w) > 0$,
setze $t = -2\operatorname{Re}\beta_p(w) / a_p(w,w)$, $k = tw$. Dann gilt
$2\operatorname{Re}\beta_p(k) + a_p(k,k) = 0$.

### 6.2 Vier getrennte Nichttrivialitätsbedingungen

Ein zulässiger geladener Feshbach-Lift erfordert gleichzeitig:

$$
k \neq 0, \qquad P_{\mathrm{ch}} k \neq 0, \qquad T_p^{\mathrm{raw}} k \neq 0, \qquad T_p^{\mathrm{raw}} k \notin \mathcal{N}_{W_{\mathrm{res}},\mathrm{rel}}.
$$

Ein gemeinsamer Zeuge für alle vier Bedingungen liegt nicht vor.

### 6.3 Abstieg des Radikals

$$
\boxed{\ T_p^{\mathrm{raw}}\bigl(\operatorname{Rad}h_p \cap K_p\bigr) \subseteq \mathcal{N}_{W_{\mathrm{res}},\mathrm{rel}} \ }
$$

ist äquivalent zu $T_p^{\mathrm{raw}}(N_{a_p}) \subseteq \mathcal{N}_{W_{\mathrm{res}},\mathrm{rel}}$. Diese Bedingung
ist im Rohkopplungsmodell tautologisch erfüllt, wenn der Kernblock über den $W_{\mathrm{res}}$-Quotienten
definiert wird — setzt aber genau die noch nicht konstruierten Voraussetzungen voraus (Quotienten,
hermitesches inneres Produkt, typkorrekter Operator, Wohldefiniertheit der Quotientenklasse).

Daher kann weder $\widehat{\varepsilon}_p \mapsto [T_p^{\mathrm{raw}}\widehat{\varepsilon}_p]$ als
hebungsunabhängige Abbildung noch $V_p^*(D_{\mathrm{rel}} - z)^{-1}V_p$ als intrinsischer
Feshbach-Transfer aus dem gegenwärtigen Gramblock abgeleitet werden.

$$
\boxed{\ [O\text{-}229\text{-}1\delta] \quad ?\![O] \ }
$$

---

## 7. Statusbilanz

| Aussage | Status |
|---|---|
| $T_p(e_0 V_p) = 0$ quellseitig (NEU-153 Z.179) | `✓[M]` |
| $B_p^{\mathrm{raw}}(e_p,e_p) = 0$, $B_p^{\mathrm{raw}}(e_p,k) = 0\ \forall k \in K_p$ | `✓[M]` |
| $h_p = \alpha_p B_p^{\mathrm{raw}}$ unmöglich auf $\mathbb{C}e_p \oplus K_p$ | `✓[M]_neg` |
| Blockdiagonale Reparatur $h_p^{\mathrm{dec}}$ mit pos. def. Kernblock $\Rightarrow \mathcal{L}_p = \emptyset$ | `✓[M]_neg` |
| Allgemeinste Form mit $h_p(e_p,e_p)=1$ erfordert Mischblock $\beta_p$ | `✓[M]` |
| $B_p^{\mathrm{raw}}$ erzeugt $\beta_p = 0$ — strukturell ungeeignet | `✓[M]_neg` |
| Rohkopplungs-Kernblock $a_p^{\mathrm{raw}}$: positiv semidefinit, Radikal $= \ker(T_p^{\mathrm{raw}}\|_{K_p})$ (generisch trivial) | `✓[M]_part` |
| Positivitätsklassifikation: $h_p \ge 0 \iff a_p \ge 0$ und $\|\beta_p\|_{a_p} \le 1$ | `✓[M]` |
| Intrinsischer nichtverschwindender Mischblock $\beta_p$ aus verfügbaren Quellen | `✓[M]_neg,Quelle` |
| Gemeinsamer Zeuge für alle vier Nichttrivialitätsbedingungen | `?[O]` |
| Hebungsunabhängigkeit, Feshbach-Wohldefiniertheit | **gesperrt** bis `[O-229-1-δ]` |

---

## 8. Strategische Aussage

$$
\boxed{\ \text{Die Transferschicht benötigt nicht bloß eine normierte Fourierhebung,}\ }
$$

$$
\boxed{\ \text{sondern eine neue intrinsische verbundene Form mit nichttrivialem Mischblock.}\ }
$$

Die eigentliche Nachfolgerfrage ist nicht mehr „Wie berechnet man $g_{0u}^{(p)}$?", sondern:

$$
\boxed{\ \text{Welche Primärstruktur zeichnet den kontraktiven Zielvektor } b_p \in \overline{\operatorname{Ran}T_p^{\mathrm{raw}}} \text{ intrinsisch aus?}\ }
$$

> **Anti-Fitting.** $\beta_p$ darf nicht so gewählt werden, dass $\mathcal{S}_2 \setminus \mathcal{S}_1$
> oder die $\Xi$-Identität herauskommt. Nur ein aus der intrinsischen $W_{\mathrm{res}}$-Geometrie
> kanonisch bestimmter Wert ist zulässig.

> **Sperrvermerk.** Kein Hebungsabstieg, keine Schattenklassenrechnung vor `[O-229-1-δ]`.

---

## 9. Neuer Hauptknoten: `[O-229-2]`

$$
\boxed{\ [O\text{-}229\text{-}2\text{-intrinsic-source-of-mixed-boundary-vector}] \quad ?\![O] \ }
$$

### Leitfrage

Existiert aus der vorhandenen singulären HH-, $W_{\mathrm{res}}$-, modularen oder Primkanalarchitektur
ein intrinsisch ausgezeichneter Vektor

$$
b_p \in \overline{\operatorname{Ran}T_p^{\mathrm{raw}}}
$$

oder äquivalent ein lineares Funktional $\beta_p : \mathcal{D}(a_p) \to \mathbb{C}$, so dass

$$
\beta_p(k) = \sqrt{\alpha_p}\,\langle b_p, T_p^{\mathrm{raw}}k \rangle, \qquad |b_p| \le 1,
$$

und mindestens ein $k \in \mathcal{D}(a_p)$ gleichzeitig erfüllt:

$$
2\operatorname{Re}\beta_p(k) + a_p(k,k) = 0, \qquad P_{\mathrm{ch}}k \neq 0, \qquad T_p^{\mathrm{raw}}k \neq 0, \qquad T_p^{\mathrm{raw}}k \notin \mathcal{N}_{W_{\mathrm{res}},\mathrm{rel}}?
$$

### Anti-Zirkularitätsbedingungen

Ein Kandidat für $b_p$ oder $\beta_p$ ist nur zulässig, wenn:

- er **vor** der Wahl eines gewünschten normierten Lifts definiert ist;
- er **nicht** aus dem noch undefinierten Feshbach-Transfer $K_p(z)$ rückwärts konstruiert wird;
- seine Normierung **nicht** an eine gewünschte Schattenklasse oder Determinantenidentität angepasst wird;
- sein Definitionsbereich und Quotientenabstieg **explizit** angegeben sind;
- seine Nichttrivialität durch eine Primärformel oder vollständige Rechnung **bewiesen** wird.

---

## 10. Nächste Knoten

| Knoten | Aufgabe | Priorität |
|---|---|---|
| `[O-229-2]` | Intrinsische Quelle für $b_p \in \overline{\operatorname{Ran}T_p^{\mathrm{raw}}}$ oder $\beta_p$ — Kandidaten aus singulärer HH-Struktur, $W_{\mathrm{res}}$-Modulgeometrie, Primkanalgrenzoperator | **1** |
| `[O-229-1-δ]` | Gemeinsamer Zeuge für alle vier Nichttrivialitätsbedingungen — abhängig von `[O-229-2]` | **2** |
| `[O-153-A/B]` | Hebungsunabhängigkeit — gesperrt bis `[O-229-1-δ]` | danach |
| `[O-226-4]` | Gramoperator $g_{0u}^{(p)}$, $g_{uu}^{(p)}$ — gesperrt bis `[O-229-1-γ]` | danach |

---

## Abhängigkeiten

| Referenz | Verwendet für |
|---|---|
| NEU-041 | Kopplungsoperator $T_p$, Wohlbestimmtheitsbedingung (41.4) |
| NEU-043 | (43.1) Fourierregel $\widetilde{\omega}_2(e_uV_p, e_sV_m) = -us\log(p)\,e_{u+ps}V_{pm}$ |
| NEU-051 | Regulatoroptionen, Kopplungsform (51.2) |
| **NEU-153** | $T_p(e_0V_p)=0$ (Z.179), Faser $\mathcal{L}_p$, Gram $g^{(p)}$, Stufen 153.A/B/D.0 |
| NEU-014 | KMS-Zustand auf $B_3$ — Kandidat für $b_p$ in `[O-229-2]` |
| NEU-042 | Fourier-Laplace-Hebung — Kandidat für $b_p$ in `[O-229-2]` |
| NEU-143 | Primärdefinition verbundene Form (Quelle fehlt teilweise) |
| NEU-156 | $\operatorname{Tr}^{\mathrm{conn}}_{W_{\mathrm{res}}}$ und $x^\sharp y$ auf Liftraum nicht konstruiert |
| NEU-225/226/227/228 | Transportgenerator, Feshbach-Transfer, Spektralmaßform, Hebungswahl |
