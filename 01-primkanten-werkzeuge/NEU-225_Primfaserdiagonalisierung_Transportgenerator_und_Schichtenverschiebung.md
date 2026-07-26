# NEU-225 — Primfaserdiagonalisierung: $D_{\mathrm{rel}}$ als Transportgenerator

**Katalog-ID:** NEU-225
**Knoten:** `[O-224-1b1]`–`[O-224-1b4]`, Reaudit NEU-56, Konventionsbereinigung
**Stand:** 26. Juli 2026
**Vorgänger:** NEU-224
**Ergebnis:** Der reduzierte kompakte Resolvent ist ausgeschlossen. HP-2 ist die falsche
Forderung an diese Schicht.

---

## 0. Ergebnis

$$
\boxed{\ D_{\mathrm{rel}}\big|_{\mathcal H_{p,a}} \ \cong\ 2ic_p\frac{d}{dt} \ \ \text{auf } L^2(\mathbb R)\oplus L^2(\mathbb R), \qquad c_p = \tfrac12\gamma_N\,p\log p \ }
$$

Damit auf jeder Primfaser: rein absolutstetiges Spektrum $\sigma = \mathbb R$, **keine**
Eigenwerte, insbesondere **kein Kern** — die Faser liegt vollständig in
$(\ker D_{\mathrm{rel}})^\perp$ — und

$$
\boxed{\ \bigl(1+D_{\mathrm{rel}}^2\bigr)^{-1/2}\Big|_{(\ker D_{\mathrm{rel}})^\perp} \notin \mathcal K . \qquad \times[M]\ \text{(vorbehaltlich §5.4)} \ }
$$

$$
\boxed{\ D_{\mathrm{rel}} \ \text{ist kein Hilbert–Pólya-Operator, sondern ein Transportgenerator.} \ }
$$

---

## 1. Konventionsbereinigung (Redaktionsschulden aus NEU-224 §7)

### 1.1 Normierung von $J_N^-$ — verbindlich

$$
\boxed{\ J_N^- := \tfrac12\bigl(\Theta_N - \Theta_N^\dagger\bigr) \ }
\tag{37.1}
$$

Dies ist die einzige Fassung mit $(J_N^-)^* = -J_N^-$ (54.3) und damit die einzige, für die
$D_{\mathrm{rel}} = \overline{iJ^-}$ selbstadjungiert ist.

Die Schreibweise $\frac{1}{2i}(\Theta_N-\Theta_N^{\mathrm{Wres}})$ aus NEU-35 (Z. 220) und
NEU-62 (Z. 98) bezeichnet einen **anderen, selbstadjungierten** Operator. Sie wird umbenannt:

$$
S_N := \tfrac{1}{2i}\bigl(\Theta_N-\Theta_N^{\dagger}\bigr) = -\,i\,J_N^-, \qquad S_N^* = S_N .
$$

Es gilt $D_{\mathrm{rel}} = \overline{iJ_N^-}\big|_{N\to\infty} = \overline{-S_N}\big|_{N\to\infty}$ bis aufs Vorzeichen.
$S_N$ und $J_N^-$ dürfen **nicht** als dasselbe Objekt geführt werden. `✓[M]`

### 1.2 Basis und Skalarprodukt — verbindlich

$$
\bigl\{\eta_{p;m;r,u}\bigr\}\ \text{ist eine Orthonormalbasis von } \mathcal H_{\mathrm{rel}}:\qquad
\bigl\langle \eta_{p;m;r,u},\ \eta_{p';m';r',u'}\bigr\rangle = \delta_{pp'}\delta_{mm'}\delta_{rr'}\delta_{uu'} .
$$

**Begründung, quellenintern:** (55.4) setzt $\lVert J^-\eta_a\rVert^2 = \sum_b\lvert\Theta_{ba}\rvert^2$
an; diese Identität gilt genau dann, wenn $\{\eta_b\}$ orthonormal ist. NEU-52 (52.D0) hält
zugleich fest, dass es sich um eine **Graph**basis handelt, nicht um eine Eigenbasis von
$D_{\mathrm{rel}}$. Beides ist verträglich. `✓[M]`

### 1.3 Wörterbuch $(r,n) \leftrightarrow (p,m,r,u)$ — verbindlich

| Größe | Bedeutung | Quelle |
|---|---|---|
| $r$ | Charakterindex, $r\in\mathbb Z$; unter $\Theta$ verschoben | NEU-27 Z.165 |
| $n$ | Isometrieindex $V_n$; unter $\Theta$ **erhalten** | NEU-27 Z.165 |
| $m$ | Fasernummer in der $\eta$-Indizierung; Kanten nur für $n\mid m$ | (55.3) |
| $p,u$ | Primträger und Bewertungsindex; von $\Theta$ nicht bewegt | (55.3) |

$$
\Theta\,\eta_{p;m;r,u} \;=\; \sum_{n\mid m} \alpha_{n}\,r\,\eta_{p;m;r+n,u},
\qquad \alpha_n = -\gamma_N\log n .
$$

Da $\log 1 = 0$, tragen nur Teiler $n>1$ bei. Die Faser $m$ ist invariant:
$\mathcal H_{\mathrm{rel}} = \bigoplus_m \mathcal H_m$. `✓[M]`

> **Restschuld `⚠[M]`.** Ob $m$ und $n$ in den Quellen tatsächlich denselben Wertebereich
> durchlaufen oder ob $\eta_{p;m;r,u}$ eine Überlagerung über $n\mid m$ ist, wird nirgends
> explizit gesagt. Die folgende Rechnung benutzt nur den Sektor $m=p$ **prim**, in dem beide
> Lesarten zusammenfallen: einziger Teiler $>1$ ist $n=p$.

---

## 2. Reaudit NEU-56 nach der Korrektur des effektiven Raums

Zwei Fragen, wie vorgegeben.

### 2.1 Benutzt der Widerspruch lediglich Testvektoren? — **Ja** `✓[M]`

Satz 56.1/56.2 argumentieren durchweg über einzelne Basisvektoren $\eta_a$ mit festem $r,n$:
(56.7) wertet $\lVert J^-\eta_a\rVert \sim \gamma_N\lvert r\rvert\log n$ aus, (56.8) vergleicht
mit $\lVert L\eta_a\rVert$. Die Bedingungen (N1), (N2), (K) sind punktweise Ungleichungen auf
$\mathcal D_0$.

### 2.2 Benutzt er die falsche Invarianz oder Spektralrestriktion? — **Nein** `✓[M]`

Nirgends in Satz 56.1–56.4 wird Invarianz oder Reduziertheit von
$\mathcal H^{\mathrm{eff}}_{\mathrm{rel}}$ benutzt.

### 2.3 Folgerung

$$
\boxed{\ \text{Satz 56.2 bleibt gültig. Nur die Raumbezeichnung wird korrigiert.} \ }
$$

Ein Vergleichsoperator auf dem größeren, korrekten Raum müsste dieselben Ungleichungen erst
recht auf dem kleineren Testbereich $\{r\neq0, m>1\}$ erfüllen. Invarianz des Testbereichs ist
für eine punktweise Abschätzungsobstruktion nicht erforderlich.

**Zurückgerollt** wird allein die Aussage, $\overline{\operatorname{span}}\{\eta_{m,r,u}: r\neq0,\ m>1\}$
sei ein reduzierender oder der kanonische kernfreie Spektralraum. `✓[M]_neg` Korrekt ist

$$
\mathcal H^{\mathrm{eff}}_{\mathrm{rel}} = \bigl(\ker D_{\mathrm{rel}}\bigr)^\perp = E_{D_{\mathrm{rel}}}\bigl(\mathbb R\setminus\{0\}\bigr)\mathcal H_{\mathrm{rel}} .
$$

---

## 3. `[O-224-1b1]` — Exakte Matrixkoeffizienten auf $m=p$

Einziger Teiler $n>1$ von $p$ ist $n=p$. Mit $\alpha_p = \gamma_N\log p$ (Vorzeichen in $J^-$
irrelevant) gilt auf $\mathcal H_p$, geschrieben $\eta_r := \eta_{p;p;r,u}$ bei festem $u$:

$$
\Theta\,\eta_r = \alpha_p\,r\,\eta_{r+p} .
$$

Die Adjungierte: $\langle\Theta^\dagger\eta_r,\eta_s\rangle = \overline{\langle\eta_r,\Theta\eta_s\rangle}
= \overline{\alpha_p s\,\delta_{r,s+p}}$, also (reelle Koeffizienten)

$$
\Theta^\dagger \eta_r = \alpha_p\,(r-p)\,\eta_{r-p} .
$$

Damit nach (37.1):

$$
\boxed{\ J^-\eta_r = \frac{\alpha_p}{2}\Bigl( r\,\eta_{r+p} \;-\; (r-p)\,\eta_{r-p} \Bigr) \ }
\tag{225.1}
$$

Probe der Schiefsymmetrie: $\langle J^-\eta_r,\eta_{r+p}\rangle = \frac{\alpha_p}{2}r$ und
$\langle J^-\eta_{r+p},\eta_r\rangle = -\frac{\alpha_p}{2}r$. `✓[M]` (numerisch bestätigt, §6)

---

## 4. `[O-224-1b2]` — Reduktion nach $r \bmod p$

$J^-$ verschiebt $r$ nur um $\pm p$. Also zerfällt die Faser in Restklassen:

$$
\mathcal H_p = \bigoplus_{a=0}^{p-1}\mathcal H_{p,a}, \qquad
\mathcal H_{p,a} = \overline{\operatorname{span}}\{\eta_{a+kp} : k\in\mathbb Z\} .
$$

Mit $e_k := \eta_{a+kp}$, $\delta := a/p \in [0,1)$ und $r = p(k+\delta)$, $r-p = p(k-1+\delta)$:

$$
\boxed{\ J^-e_k = c_p\Bigl((k+\delta)\,e_{k+1} - (k-1+\delta)\,e_{k-1}\Bigr), \qquad c_p := \frac{\gamma_N\,p\log p}{2} \ }
\tag{225.2}
$$

In Koeffizienten: $(J^-x)_j = c_p\bigl[(j-1+\delta)x_{j-1} - (j+\delta)x_{j+1}\bigr]$.

> **Strukturbefund.** Das ist **keine konfinierende Jacobi-Matrix**. Die Gewichte wachsen
> linear in $k$, aber die beiden Nachbarterme haben **entgegengesetzte Vorzeichen** und nahezu
> gleichen Betrag — die Kette ist ein diskreter **Dilatationsgenerator**, kein
> Multiplikationsoperator mit divergierender Diagonale. Genau darum scheiterte das Konfinement
> in NEU-56: es wurde ein Transportgenerator gegen einen Energieoperator gestellt.

---

## 5. `[O-224-1b3]` — Unitäre Transformation

### 5.1 Fourier

Mit $\mathcal F: e_k \mapsto e^{ik\theta}/\sqrt{2\pi}$, also $k \leftrightarrow -i\partial_\theta$:

$$
\mathcal F J^-\mathcal F^{-1} = c_p\Bigl[\,2\sin\theta\,\partial_\theta + \cos\theta + i(2\delta-1)\sin\theta\,\Bigr]
\tag{225.3}
$$

$$
\mathcal F D_{\mathrm{rel}}\mathcal F^{-1} = i c_p\Bigl[2\sin\theta\,\partial_\theta + \cos\theta\Bigr] \;-\; c_p(2\delta-1)\sin\theta
\tag{225.4}
$$

**Symmetrieprobe.** Der Differentialteil hat die Gestalt $i\bigl(v\,\partial_\theta + \tfrac12 v'\bigr)$
mit $v(\theta) = 2c_p\sin\theta$ reell — das ist die symmetrische Lie-Ableitungsform. Der
Zusatzterm ist reelle Multiplikation. Beide symmetrisch. `✓[M]`

(225.3) numerisch bestätigt bis auf $7\cdot 10^{-7}$ relative Abweichung (§6).

### 5.2 Logarithmische Koordinate

$v$ verschwindet bei $\theta = 0,\pi$. Auf $(0,\pi)$ setze

$$
t = \log\tan\frac{\theta}{2}, \qquad \frac{dt}{d\theta} = \frac{1}{\sin\theta}, \qquad \sin\theta = \operatorname{sech} t,
$$

mit $\theta\to 0^+ \Rightarrow t\to-\infty$ und $\theta\to\pi^- \Rightarrow t\to+\infty$. Also
$(0,\pi)\to\mathbb R$ bijektiv. Die Gewichtskorrektur $g(t) = \sqrt{\sin\theta}\,f(\theta)$ ist
unitär $L^2((0,\pi),d\theta)\to L^2(\mathbb R,dt)$, und $2\sin\theta\,\partial_\theta = 2\partial_t$.
Der Differentialteil wird zu $2ic_p\,d/dt$:

$$
\mathcal F D_{\mathrm{rel}}\mathcal F^{-1}\Big|_{(0,\pi)} \;\cong\; 2ic_p\frac{d}{dt} \;-\; c_p(2\delta-1)\operatorname{sech} t .
$$

### 5.3 Das Potential ist eichbar

Mit $U = e^{i\phi(t)}$ gilt $U^{-1}\bigl(2ic_p\partial_t\bigr)U = 2ic_p\partial_t - 2c_p\phi'$.
Die Wahl

$$
\phi'(t) = \frac{2\delta-1}{2}\operatorname{sech} t
\qquad\Longrightarrow\qquad
\phi(t) = (2\delta-1)\arctan(\sinh t)
$$

entfernt den Potentialterm. $\phi$ ist **beschränkt** ($\lvert\phi\rvert \le \pi/2$), also ist
$U$ eine beschränkte unitäre Multiplikation ohne Domänenwirkung. `✓[M]`

$$
\boxed{\ D_{\mathrm{rel}}\big|_{\mathcal H_{p,a}} \ \cong\ 2ic_p\frac{d}{dt}\ \text{auf } L^2(\mathbb R)_{(0,\pi)} \oplus L^2(\mathbb R)_{(-\pi,0)} \ }
$$

### 5.4 Was **nicht** bewiesen ist — Domänenvorbehalt `❓[O]`

Der Operator $2ic_p\,d/dt$ ist auf $C_c^\infty(\mathbb R)$ wesentlich selbstadjungiert. Die
Fixpunkte $\theta=0,\pi$ liegen in der $t$-Koordinate im Unendlichen, sodass die beiden
Halbkreise **nicht** kommunizieren und keine künstlichen Randbedingungen entstehen — für den
**minimalen** Operator auf $C_c^\infty\bigl((0,\pi)\cup(-\pi,0)\bigr)$.

$$
\boxed{\ \text{Offen: Ist } \mathcal D_0 \ (\text{trigonometrische Polynome}) \ \text{ein Kern für diese selbstadjungierte Realisierung?} \ }
$$

Trigonometrische Polynome verschwinden **nicht** bei $\theta=0,\pi$. Eine symmetrische
Restriktion eines selbstadjungierten Operators muss nicht wesentlich selbstadjungiert sein.
NEU-55 (55.17) behauptet essentielle Selbstadjungiertheit auf $\mathcal D_0$ — aber nur
**bedingt** auf (55.5)/(55.9), die ihrerseits `❓[O]` sind. Der Vorbehalt ist damit derselbe,
der schon in NEU-55 offen war, und **kein neuer**. `❓[O]` `[O-225-1]`

> **Wichtig: das Ergebnis hängt nicht daran.** Die Nichtkompaktheit folgt unabhängig aus dem
> negativen Zeugen in §5.5, der nur $\mathcal D_0 \subseteq \operatorname{Dom}(\overline{J_0^-})$
> benutzt und für **jede** abgeschlossene Erweiterung von $J_0^-$ gilt.

### 5.5 `[O-224-1b4]` — Nichtkompaktheit, realisierungsunabhängig

Im $t$-Bild sei $\varphi\in C_c^\infty$ mit $\lVert\varphi\rVert = 1$ und
$g_n(t) := \varphi(t - T n)$ mit $T$ größer als die Trägerbreite. Dann:

- $\{g_n\}$ **orthonormal** (disjunkte Träger);
- $\lVert 2ic_p g_n'\rVert = 2c_p\lVert\varphi'\rVert$ — **konstant in $n$**.

Also ist $\sup_n\bigl(\lVert g_n\rVert + \lVert D_{\mathrm{rel}}g_n\rVert\bigr) < \infty$: eine
graphnormbeschränkte Orthonormalfolge. Die Graphnormeinbettung ist nicht kompakt.

$$
\boxed{\ \bigl(1+D_{\mathrm{rel}}^2\bigr)^{-1/2}\Big|_{\mathcal H_{p,a}} \notin\mathcal K . \ }
$$

Numerisch bestätigt (§6): drei verschobene Buckel, Norm $1{,}0000$, Graphnormanteil konstant
$2{,}0000$, Überlappung $5\cdot 10^{-32}$.

### 5.6 Die Primfasern liegen im reduzierten Raum

Der Impulsoperator hat rein absolutstetiges Spektrum und **keine** Eigenwerte, insbesondere
$\ker\bigl(D_{\mathrm{rel}}\vert_{\mathcal H_{p,a}}\bigr) = \{0\}$. Also

$$
\mathcal H_p \subseteq \bigl(\ker D_{\mathrm{rel}}\bigr)^{\perp} \qquad (p \text{ prim}).
$$

$$
\boxed{\ \text{Damit ist auch der \textbf{reduzierte} kompakte Resolvent ausgeschlossen.} \quad \times[M] \ }
$$

Nebenbefund: In den Primsektoren gibt es **keinen** Restkern — Teilantwort auf `[O-224-1b]`.

Da für jedes Primsektorpaar $(p,a)$ zwei Kopien auftreten und $a$ über $p$ Werte läuft, hat
das absolutstetige Spektrum **unendliche Multiplizität**.

---

## 6. Unabhängige numerische Kontrolle

Trunkierte Kette $\lvert k\rvert\le 40$, $c_p=1$, $\delta=0{,}37$:

| Prüfung | Ergebnis |
|---|---|
| $J^-$ schiefsymmetrisch | exakt `✓` |
| Fourierform (225.3) gegen Matrixwirkung | rel. Abweichung $6{,}9\cdot 10^{-7}$ `✓` |
| Verschobene Buckel $t_0=6,12,18$: Norm | $1{,}0000$ jeweils `✓` |
| dieselben: $\lVert 2ic_p g'\rVert$ | $2{,}0000$ jeweils — konstant `✓` |
| Überlappung $t_0=6$ gegen $18$ | $5\cdot 10^{-32}$ `✓` |

> **Grenze der Numerik (Regel aus G5).** Die Trunkierung liefert stets diskretes Spektrum; der
> beobachtete Eigenwert $0$ ist ein Artefakt ungerader Dimension einer reell
> schiefsymmetrischen Matrix. Die Numerik bestätigt hier **algebraische Identitäten**
> (225.1)–(225.3) und die Existenz des negativen Zeugen — sie beweist **nicht** den
> Spektraltyp des Grenzoperators. Dieser folgt aus §5.1–5.3.

---

## 7. Schichtenverschiebung: HP-2 an der falschen Schicht

### 7.1 Die Diagnose

$$
\boxed{\ D_{\mathrm{rel}} \ \text{ist ein Streu- bzw. Transportgenerator, kein Hilbert–Pólya-Operator.} \ }
$$

Das erklärt rückwirkend NEU-56: Konfinement scheiterte nicht an einer ungeschickten Wahl von
$\gamma_N$ oder $L$, sondern **strukturell**. Ein Dilatationsgenerator besitzt niemals
kompakten Resolventen, gleich welcher Vergleichsoperator gewählt wird. Der Versuch, ihn zu
konfinieren, sollte aufgegeben werden.

### 7.2 Die vorgeschlagene Arbeitsteilung

$$
\boxed{\ D_{\mathrm{rel}} \ \text{liefert die Streugeometrie;} \quad K(z)\ \text{bzw.}\ \Sigma(z)\ \text{liefert das kompakte spektrale Objekt.} \ }
$$

Kandidat, eine Ebene später:

$$
K_N(z) = V_N^*\bigl(D_{\mathrm{rel}} - z\bigr)^{-1}V_N ,
\qquad
\Sigma_N(z) = V_N^*\bigl(D_{\mathrm{rel}} - z\bigr)^{-1}V_N .
$$

Ein kontinuierlicher Grundoperator kann sehr wohl einen kompakten oder
Hilbert–Schmidt-artigen Kopplungsoperator erzeugen. Dort könnten zusammentreffen:
kontinuierliche Primkanäle, echte Off-Diagonal-Kopplung, $\mathcal S_2\setminus\mathcal S_1$
(HP-3), $\det\nolimits_2$ (HP-5) und die zyklische Weyl-Funktion.

> **Statusgrenze `❓[O]`.** Das ist eine **Arbeitshypothese**, kein Ergebnis. Weder ist gezeigt,
> dass $K_N(z)$ kompakt ist, noch dass es die Determinantenidentität HP-5/HP-6 trägt, noch
> dass ein intrinsischer zyklischer Vektor existiert. Nachfolgeknoten `[O-225-2]`.

### 7.3 Konsequenz für das HP-Profil

HP-2 ist damit **nicht** widerlegt für Objekt X. Widerlegt ist nur, dass
$H_X = D_{\mathrm{rel}}$ eine zulässige Realisierung sein kann. Die Umfangsklausel aus
NEU-223 §8 bleibt in Kraft: ausgeschlossen ist die erzwungene Vergleichsoperatorklasse des
gegenwärtigen relativen Jacobi-/Feshbachmodells — nicht jede denkbare Realisierung.

Ebenso unberührt: NEU-56 §4 — die RH-Hinrichtung über
$\mathrm{Spec}\subset\mathbb R$ braucht nur Selbstadjungiertheit. Der Jacobi- und der
Stieltjeskanal (XVI-C.2) sind nicht gesperrt.

---

## 8. Statusbilanz

| Aussage | Status |
|---|---|
| Konvention $J_N^-=\frac12(\Theta_N-\Theta_N^\dagger)$ verbindlich; $S_N:=\frac{1}{2i}(\cdots)$ umbenannt | `✓[M]` |
| $\{\eta_{p;m;r,u}\}$ orthonormal (quellenintern über 55.4) | `✓[M]` |
| Wörterbuch $(r,n)\leftrightarrow(p,m,r,u)$; Restschuld für $m$ nicht prim | `✓[M]` / `⚠[M]` |
| NEU-56 benutzt nur Testvektoren, keine Invarianz | `✓[M]` |
| **Satz 56.2 bleibt gültig**, nur Raumbezeichnung korrigiert | `✓[M]` |
| $\mathcal H^{\mathrm{eff}}$ nach (55.0) als reduzierender Raum | `✓[M]_neg` zurückgerollt |
| (225.1) Matrixkoeffizienten auf $m=p$ | `✓[M]` `[O-224-1b1]` |
| (225.2) Reduktion nach $r\bmod p$; Dilatationsgenerator | `✓[M]` `[O-224-1b2]` |
| (225.3)/(225.4) Fourierform, Symmetrie geprüft | `✓[M]` `[O-224-1b3]` |
| Logarithmische Koordinate, $\operatorname{sech}$-Potential eichbar ($\phi$ beschränkt) | `✓[M]` |
| $\mathcal D_0$ als Kern der selbstadjungierten Realisierung | `❓[O]` `[O-225-1]` — Vorbehalt aus 55.17 |
| Graphnormbeschränkte Orthonormalfolge, realisierungsunabhängig | `✓[M]` `[O-224-1b4]` |
| Kein Kern in den Primsektoren; $\mathcal H_p\subseteq(\ker D_{\mathrm{rel}})^\perp$ | `✓[M]` |
| **Reduzierter kompakter Resolvent ausgeschlossen** | **`✗[M]`** |
| $D_{\mathrm{rel}}$ kein HP-Operator, sondern Transportgenerator | `✓[M]` |
| Feshbach-/Birman–Schwinger-Transfer $K(z)$ trägt HP-2/HP-3/HP-5 | `❓[O]` `[O-225-2]` **Arbeitshypothese** |
| Restkern in Sektoren $m$ nicht prim | `❓[O]` |

---

## 9. Nachfolgeknoten

| Knoten | Aufgabe |
|---|---|
| `[O-225-1]` | Ist $\mathcal D_0$ ein Kern? Äquivalent: exakter Beweis von (55.5)/(55.9). Trägt die gesamte Selbstadjungiertheitsschicht |
| `[O-225-2]` | **Hauptlinie.** $K_N(z)=V_N^*(D_{\mathrm{rel}}-z)^{-1}V_N$: Kompaktheit, $\mathcal S_2\setminus\mathcal S_1$, $\det_2$-Identität, intrinsischer zyklischer Vektor |
| `[O-225-3]` | Sektoren $m$ nicht prim: mehrere Sprünge $\pm n$ über $n\mid m$, $n>1$ — zerfällt nicht mehr nach einer Restklasse. Restkern und Spektraltyp |
| `[O-225-4]` | Streutheoretische Deutung: Wellenoperatoren, Streumatrix, Bezug zur relativen Determinantenformel (HP-6) |

---

## Abhängigkeiten

| Referenz | Verwendet für |
|---|---|
| NEU-27 (Z.165) | $\Theta(e_rV_n)=r\log(n)e_{r+n}V_n$ |
| NEU-35 (Z.220), NEU-62 (Z.98) | abweichende Normierung, hier als $S_N$ umbenannt |
| NEU-37 (37.1) | verbindliche Konvention $J_N^-=\frac12(\Theta_N-\Theta_N^\dagger)$ |
| NEU-51 | $K_{pq}$, Spurklassekriterium — Anschluss für `[O-225-2]` |
| NEU-53, NEU-54 | $\mathcal D_0$, (54.3), (54.SEP) |
| NEU-55 | (55.0), (55.4) Orthonormalität, (55.17) bedingte Selbstadjungiertheit |
| NEU-56 | Satz 56.1–56.4, §4 (RH braucht nur SA), §7 |
| NEU-77 | Feshbach-Kollaps — Anschluss für `[O-225-2]` |
| NEU-220u | HP-1–HP-7 |
| NEU-223 Rev. 2, NEU-224 | Zielnormalform, Kernbefund, Knotenstruktur |
