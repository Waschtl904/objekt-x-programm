# NEU-242 — Abschlussaudit zu [O-229-3B.1f-b.1]

**Datum:** 27. Juli 2026  
**Auditierter Restblock:** NEU-221e, NEU-226, NEU-227, NEU-229  
**Gesamter festgelegter Quellenblock:** NEU-155, NEU-157, NEU-158, NEU-166a, NEU-168, NEU-221e, NEU-226, NEU-227, NEU-229

---

## 1. Interpretationsfreier Primärextrakt

### 1.1 NEU-221e

NEU-221e definiert den algebraischen Liftbereich und die primitive Projektion durch

$$
B_{3,p}^{\mathrm{lift}}\subseteq B_3,
\qquad
\pi_{\mathrm{prim},p}: B_{3,p}^{\mathrm{lift}} \longrightarrow \mathbb{C}\varepsilon_p,
$$

sowie $\widehat{\varepsilon}_p^{\,0}+K_p$.

Die Liftfaser ist damit eine **affine Faser** über $K_p$. Die normierte Zulässigkeitsbedingung wird als quadratische Gleichung formuliert; die zugehörige Lösungsmenge ist im Allgemeinen kein komplexer Vektorraum.

Als relativer Rohzielraum wird

$$
\operatorname{span}\left\{ E^{\mathrm{rel}}_{r;\,m\xrightarrow{p}pm} \right\}
$$

definiert. Das Radikal der relativen Wres-Form ist

$$
\left\{ v\in\mathscr{V}_{\mathrm{rel},p,N}^{\mathrm{pre}} : \langle v,w\rangle_{\mathrm{Wres,rel}}=0 \ \forall w \right\}.
$$

Danach werden die Quotientenabbildung

$$
Q_{\mathrm{Wres,rel}}: \mathscr{V}_{\mathrm{rel},p,N}^{\mathrm{pre}} \longrightarrow \mathscr{V}_{\mathrm{rel},p,N}^{\mathrm{pre}} / \mathcal{N}_{\mathrm{Wres,rel}}
$$

und eine Hilbertraumrealisierung $\mathcal{H}_{\mathrm{rel},p,N}$ eingeführt.

Die Rohkopplung ist eine gewöhnliche lineare Abbildung

$$
\widetilde{T}_{p,N}^{\mathrm{raw}}(x) := \Pi_{\mathrm{rel},J,N}\,\widetilde{\omega}_2(x,L_3^\circ) \in \mathscr{V}_{\mathrm{rel},p,N}^{\mathrm{pre}},
$$

und die quotientierte Kopplung lautet $Q_{\mathrm{Wres,rel}} \circ \widetilde{T}_p^{\mathrm{raw}}$.  
Für einen gewählten Lift wird daraus $T_p^{\mathrm{rel}}(\widehat{\varepsilon}_p) \in \mathcal{H}_{\mathrm{rel},p,N}$.

NEU-221e behandelt danach Quotientabstieg, Rang-eins-Kopplung, Spektralmaßinvarianz und den globalen direkten Summenvektor.

**Auditantwort zu NEU-221e**

- Es wird kein Komplex $(C^\bullet, d)$, $d^2=0$ auf dem Liftbereich definiert.
- Es existiert keine typisierte Einbettung $K_p$, $E_p^{\mathrm{ch}}$ oder $\mathcal{A}_p^{\mathrm{adm}} \longrightarrow C^r$ in ein Gradstück eines Komplexes.
- $\widetilde{T}_p^{\mathrm{raw}}$ und $T_p^{\mathrm{rel}}$ werden als lineare Operatoren mit anschließender Quotientierung behandelt, nicht als Komponenten einer graduierten Abbildung.
- Die Volltextprüfung liefert weder eine Differential- noch eine Kettenabbildungsdefinition.

---

### 1.2 NEU-226

NEU-226 identifiziert $V_p = C_p^{\mathrm{rel}}$ und definiert

$$
V_N = \sum_{p\le N} V_p, \qquad V_N^*(D_{\mathrm{rel}}-s)^{-1}V_N,
$$

sowie die Blöcke $V_p^*(D_{\mathrm{rel}}-s)^{-1}V_q$.

$V_N$ ist ausdrücklich eine Summe und keine direkte Summe. Die Datei behandelt Kopplungsbilder, Primkanalüberlappungen, Resolventenmatrixelemente und Schattenklassenbedingungen.

Die zunächst verwendete Eigenbasisform wird wegen des rein absolut kontinuierlichen Spektrums verworfen. Als korrekte Ersatzform wird ein Spektralintegral

$$
\int_{\mathbb{R}} \frac{d\mu_{a,b}(\lambda)}{\lambda-s}
$$

verlangt. Außerdem werden Bedingungen wie

$$
|D_{\mathrm{rel}}-s|^{-1/2}V_N\in\mathcal{S}_2 \Longrightarrow K_N(s)\in\mathcal{S}_1
$$

untersucht.

**Auditantwort zu NEU-226**

- $\mathcal{N}_{\mathrm{Wres,rel}}$ wird in NEU-226 nicht als graduierter Unterraum definiert.
- Es wird kein Differential $d_{\mathrm{tar}}$ auf einem Wres-Rohzielraum oder einem Wres-Quotienten definiert.
- Eine Stabilitätsaussage $d_{\mathrm{tar}}\,\mathcal{N}_{\mathrm{Wres,rel}}^n \subseteq \mathcal{N}_{\mathrm{Wres,rel}}^{n+1}$ kommt nicht vor.
- $V_p$ wird als Kopplungsoperator in einem Resolventensandwich verwendet, nicht als Komponente einer Kettenabbildung.
- Die Volltextprüfung findet weder „Differential" noch „Kettenabbildung" noch eine Bedingung $d^2=0$.

---

### 1.3 NEU-227

NEU-227 definiert das Koordinatenwörterbuch

$$
\eta_{p;m;s,u} \longleftrightarrow e_R V_M, \qquad M=pm, \qquad R=u+ps,
$$

und behandelt die Dynamik des Transportoperators $J^-$.

Für den Feshbach-Transfer wird ein selbstadjungierter Operator $D = D_{\mathrm{rel}} = D_{\mathrm{rel}}^*$ mit projektionswertigem Spektralmaß

$$
E_D: \mathcal{B}(\mathbb{R}) \longrightarrow \operatorname{Proj}(\mathcal{H}_{\mathrm{rel}})
$$

verwendet. Das Kreuzspektralmaß lautet $\langle V_p a, E_D(B) V_q b\rangle$. Damit wird

$$
\int_{\mathbb{R}} \frac{d\mu_{pq}^{a,b}(\lambda)}{\lambda-z}
$$

beziehungsweise im schwachen Operatorsinn

$$
\int_{\mathbb{R}} \frac{dM_{pq}(\lambda)}{\lambda-z}, \qquad M_{pq}(B)=V_p^*E_D(B)V_q,
$$

definiert.

Weiter wird ein Quellhilbertraum $\mathscr{E}_N$ mit Orthonormalbasis $(e_j)$ verwendet, um Schattenklassenkriterien für $V$ und $K_N(z)$ zu formulieren. Die noch offenen Knoten betreffen den $u$-Regulator, die Quellhilbertisierung, den Gramoperator und Schattenklassen.

**Auditantwort zu NEU-227**

- $\mathscr{E}_N$ ist ein Hilbertraum, kein Gradstück eines Differentialkomplexes.
- $\mathcal{H}_{\mathrm{rel}}$ ist der Hilbertraum des selbstadjungierten Operators $D$, kein Zielkomplex.
- Das projektionswertige Spektralmaß $E_D$, die Resolvente und die operatorwertigen Borelmaße sind keine Differentiale.
- Weder $V_p$ noch $K_{pq}(z)$ werden als Komponenten einer Kettenabbildung typisiert.
- Die Volltextprüfung findet keine Differential-, Kettenabbildungs- oder $d^2=0$-Definition.

---

### 1.4 NEU-229

NEU-229 arbeitet zunächst mit einem algebraischen gemeinsamen Definitionsbereich

$$
\mathcal{D}_p^{\mathrm{lift}} \subseteq \operatorname{Dom}\pi_{\mathrm{prim},p} \cap \operatorname{Dom}T_p^{\mathrm{raw}}.
$$

Der algebraische Kern und der zugehörige Vektorraum sind $\mathbb{C}e_p \oplus K_p^{\mathrm{alg}}$.

Es wird ausdrücklich festgehalten, dass die Quellen keinen abgeschlossenen Hilbertraum bestimmen, auf dem alle beteiligten Operationen gleichzeitig vollständig definiert sind.

Die Kernform ist

$$
a_p: \mathcal{D}(a_p)\times\mathcal{D}(a_p) \longrightarrow \mathbb{C}, \qquad \mathcal{D}(a_p)\subseteq K_p^{\mathrm{alg}},
$$

mit Nullraum $\{k\in\mathcal{D}(a_p) \mid (k,k)=0\}$ und Quotientenvervollständigung $\overline{\mathcal{D}(a_p)/N_{a_p}}^{\,a_p}$.

Die vollständige Form wird auf dem Formbereich $\mathbb{C}e_p \oplus \mathcal{D}(a_p)$ definiert.

Für den Rohkopplungs-Kernblock gilt

$$
\alpha_p \langle T_p^{\mathrm{raw}} k,\, T_p^{\mathrm{raw}} \ell \rangle,
$$

und im Wres-relativen Fall $(T_p^{\mathrm{raw}})^{-1}\!\bigl(\mathcal{N}_{\mathrm{Wres,rel}}\bigr)$.

Der Mischblock muss gegebenenfalls über

$$
\sqrt{\alpha_p}\,\langle b_p, T_p^{\mathrm{raw}} k\rangle, \qquad b_p\in\overline{\operatorname{Ran}T_p^{\mathrm{raw}}},
$$

faktorisieren.

**Auditantwort zu NEU-229**

- $\mathcal{D}(a_p)$ wird ausschließlich als Formbereich verwendet.
- $N_{a_p}$ wird als Nullraum einer positiv semidefiniten Form verwendet.
- $H_{a,p}$ wird als Vervollständigung eines Formquotienten definiert.
- $\overline{\operatorname{Ran}T_p^{\mathrm{raw}}}$ erscheint als abgeschlossener Zielraum bzw. als möglicher Aufenthaltsraum des Vektors $b_p$.
- Weder $\mathcal{D}(a_p)$ noch $N_{a_p}$, $H_{a,p}$ oder $\overline{\operatorname{Ran}T_p^{\mathrm{raw}}}$ werden graduiert.
- Es wird kein Differential auf einem dieser Räume definiert.
- $T_p^{\mathrm{raw}}$ wird als gewöhnlicher Operator verwendet: zur Definition einer Pullback-Form, zur Bestimmung eines Radikals, für Quotientenabstiegsbedingungen, und für die Faktorisierung eines Mischfunktionals.
- Es wird nicht als Komponente einer Kettenabbildung definiert.
- NEU-229 hält sogar fest, dass die Hochschild-/zyklische Kandidatenroute keine vollständig typisierte Kontraktion $K_p\to\mathbb{C}$ liefert.
- Die Volltextprüfung findet keine Differential-, Kettenabbildungs- oder $d^2=0$-Definition.

---

## 2. Abschlusstabelle

| Datei | Quellkomplex | Zielkomplex | Differential ($d^2=0$) | $T_p$ oder $V_p$ als Kettenkomponente |
|-------|-------------|-------------|------------------------|----------------------------------------|
| NEU-221e | Nein; affine Liftfaser, Kern, Quadrik und Differenzmenge | Nein; Rohvektorraum, Radikal, Quotient und Hilbertraum | Nein | Nein |
| NEU-226 | Nein; gewöhnliche Quelldomänen der Kopplungsoperatoren | Nein; relativer Hilbertraum und Resolventenoperatoren | Nein | Nein |
| NEU-227 | Nein; Quellhilbertraum $\mathscr{E}_N$ | Nein; $\mathcal{H}_{\mathrm{rel}}$ mit Spektralmaß | Nein | Nein |
| NEU-229 | Nein; algebraischer Definitionsbereich und Formbereich | Nein; Formquotient und abgeschlossener Bildraum | Nein | Nein |

---

## 3. Architekturtrennung

### 3.1 Gewöhnlicher operator- und hilbertraumtheoretischer Typ

Im auditierten Quellenbestand treten folgende gewöhnliche Strukturen auf:

$$
T_p^{\mathrm{raw}}: \text{algebraischer oder formtheoretischer Definitionsbereich} \longrightarrow \text{Rohzielraum},
$$

$$
Q_{\mathrm{Wres,rel}} \circ T_p^{\mathrm{raw}}, \qquad V_p: \mathscr{E}_p \longrightarrow \mathcal{H}_{\mathrm{rel}}, \qquad V_p^*(D-z)^{-1}V_q.
$$

Hinzu kommen affine Liftfasern, nichtlineare Zulässigkeitsmengen, Formbereiche, Radikale, Quotienten, Hilbertraumvervollständigungen, Spektralmaße und Schattenklassenbedingungen.

Diese Strukturen sind mathematisch typisiert, soweit die jeweiligen Dateien sie angeben. Sie erzeugen jedoch **keine Differentialkomplexe**.

### 3.2 Existenz einer echten Komplexstruktur

Für einen **Quellkomplex** wären Daten der Form

$$
C_{p,\mathrm{lift}}^\bullet, \qquad d_{\mathrm{lift}}: C_{p,\mathrm{lift}}^n \longrightarrow C_{p,\mathrm{lift}}^{n+1}, \qquad d_{\mathrm{lift}}^2=0,
$$

sowie eine typisierte Inklusion $\mathcal{D}(a_p)\hookrightarrow C_{p,\mathrm{lift}}^r$ erforderlich.

Für einen **Zielkomplex** wären Daten der Form

$$
C_{p,\mathrm{tar}}^\bullet, \qquad d_{\mathrm{tar}}: C_{p,\mathrm{tar}}^n \longrightarrow C_{p,\mathrm{tar}}^{n+1}, \qquad d_{\mathrm{tar}}^2=0,
$$

sowie eine typisierte Inklusion $\operatorname{Ran}T_p^{\mathrm{raw}} \hookrightarrow C_{p,\mathrm{tar}}^{r+s}$ erforderlich.

**Keine dieser Daten wird im festgelegten Quellenblock definiert.**

Insbesondere gelten nicht: Gradstück eines Komplexes, Unterkomplex, graduierter Unterkomplex, Differentialkomplex.

### 3.3 Gemeinsame Gradzuweisung

Eine quellengegebene Gradzuweisung müsste mindestens die Form

$$
T_p^{\mathrm{raw}}: C_{p,\mathrm{lift}}^r \longrightarrow C_{p,\mathrm{tar}}^{r+s}
$$

besitzen und mit den Differentialen kompatibel sein: $\pm T_p^{\mathrm{raw}} d_{\mathrm{lift}}$ bzw. mit weiteren Komponenten zu einer vollständigen Kettenabbildung ergänzt werden.

Da weder Quell- noch Zielkomplex definiert sind, existiert im auditierten Quellenbestand auch **keine gemeinsame Gradzuweisung** $(r,s)$.

---

## 4. Endgültiger Statusabschluss

$$
\boxed{[O\text{-}229\text{-}3B.1f\text{-}b.1b] \quad \checkmark[M]_{\mathrm{neg,Quelle}}.}
$$

Es existiert im auditierten Quellenbestand kein Quellkomplex, in dessen Gradstück der Liftbereich, $K_p$, $\mathcal{A}_p^{\mathrm{adm}}$ oder $\mathcal{D}(a_p)$ typisiert eingebettet ist.

$$
\boxed{[O\text{-}229\text{-}3B.1f\text{-}b.1c] \quad \checkmark[M]_{\mathrm{neg,Quelle}}.}
$$

Es existiert im auditierten Quellenbestand kein Zielkomplex, dessen Gradstück den Rohzielraum, den Wres-Quotienten oder $\overline{\operatorname{Ran}T_p^{\mathrm{raw}}}$ enthält.

$$
\boxed{[O\text{-}229\text{-}3B.1f\text{-}b.1d] \quad \checkmark[M]_{\mathrm{neg,Quelle}}.}
$$

Es existiert im auditierten Quellenbestand keine gemeinsame Gradzuweisung, unter der $T_p^{\mathrm{raw}}$ als Komponente einer graduierten Abbildung oder Kettenabbildung typisiert wäre.

Damit insgesamt:

$$
\boxed{[O\text{-}229\text{-}3B.1f\text{-}b.1] \quad \checkmark[M]_{\mathrm{neg,Quelle}}.}
$$

---

## 5. Umfangsklausel

**Bewiesen ist:**

Der vorhandene Operator $T_p$, bzw. seine späteren Roh- und Relativfassungen, ist im vollständig auditierten, für b.1 festgelegten Quellenbestand **nicht** als Komponente einer Kettenabbildung zwischen definierten Quell- und Zielkomplexen typisiert.

**Nicht bewiesen ist:**

$T_p^{\mathrm{raw}}$ könne grundsätzlich nicht zu einer Kettenabbildung erweitert werden.

Nicht ausgeschlossen ist daher eine zukünftige Neukonstruktion von

$$
(C_{p,\mathrm{lift}}^\bullet, d_{\mathrm{lift}}), \qquad (C_{p,\mathrm{tar}}^\bullet, d_{\mathrm{tar}})
$$

sowie einer Erweiterung

$$
F^\bullet: C_{p,\mathrm{lift}}^\bullet \longrightarrow C_{p,\mathrm{tar}}^\bullet,
$$

deren relevante Komponente mit $T_p^{\mathrm{raw}}$ übereinstimmt.

---

## 6. Konsequenzen für die Folgeknoten

Mangels quellengegebener Kettenabbildung darf weiterhin kein Mapping Cone konstruiert werden. Daher:

$$
\boxed{[O\text{-}229\text{-}3B.1f\text{-}b.2] \quad ?[O]_{\mathrm{blockiert}}.}
$$

$$
\boxed{[O\text{-}229\text{-}3B.1f\text{-}b.3] \quad ?[O]_{\mathrm{blockiert}}.}
$$

Die allgemeine analytische Positivitätsbedingung

$$
|\Lambda_p| \le \sqrt{\alpha_p} \qquad \text{bzw.} \qquad |\beta_p(k)|^2 \le a_p(k,k)
$$

bleibt gültig. Sie kann jedoch ohne definierten Zielkomplex, ohne Kandidatenkokette und ohne Transgressionsabbildung nicht als konkrete kohomologische Randbedingung geprüft werden.

---

## 7. Endurteil in einem Satz

$$
\boxed{T_p^{\mathrm{raw}} \text{ ist quellenmäßig ein Operator zwischen algebraischen, formtheoretischen oder Hilberträumen, aber keine Komponente einer Kettenabbildung.}}
$$
