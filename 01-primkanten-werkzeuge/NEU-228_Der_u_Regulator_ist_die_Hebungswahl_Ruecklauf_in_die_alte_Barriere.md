# NEU-228 — Der $u$-Regulator ist die Hebungswahl: Rücklauf in die alte Barriere

**Katalog-ID:** NEU-228
**Knoten:** `[O-228-1a]`–`[O-228-1e]`, `[O-226-3]`, `[O-226-4]`
**Stand:** 26. Juli 2026
**Vorgänger:** NEU-227
**Ergebnis:** Der $u$-Regulator ist kein neuer Freiheitsgrad. Er ist die Hebungswahl aus
NEU-153. Die neue Hauptlinie läuft in dieselbe offene Barriere wie die alte.

---

## 0. Auditurteil

$$
\boxed{\ [O\text{-}226\text{-}3] \ \equiv\ [O\text{-}153] \ \equiv\ [O\text{-}221\text{-}1c1a0] \qquad \text{— die Hebungsunabhängigkeit.} \ }
$$

Vier Befunde:

1. **Die $u$-Summe in (51.2) ist die Entwicklung einer Hebung $\widehat\varepsilon_p$**, kein
   nachträglich gewählter Regulator. `✓[M]`
2. **Option R2 in ihrer wörtlichen Form ist widerlegt.** Der Primkanalprojektor
   $\pi_{\mathrm{prim}}$ wählt $u=0$, und der Faktor $-us\log p$ vernichtet dann die gesamte
   Kopplung. Das ist Fall C. `✓[M]_neg`
3. **Der Symmetrie-No-Go (Fall D) tritt nicht ein.** $\pi_{\mathrm{prim}}$ bricht die
   Fouriertranslation bereits selbst; sie ist keine zu erhaltende Symmetrie. `✓[M]`
4. **Auch `[O-226-4]` ist nicht neu.** Der Gramoperator der Hebungsfaser ist NEU-153
   $g^{(p)}_{uu}$, $g^{(p)}_{0u}$ — dort seit dem 13. Juli 2026 offen. `✓[M]`

---

## 1. `[O-228-1a]` — Wirkungsseite und Herkunft der $u$-Summe

### 1.1 Woher die Summe kommt

NEU-153 (Einleitung) definiert den Kopplungsvektor als

$$
\boxed{\ \Psi_p(\widehat\varepsilon_p) = \Pi_{W_{\mathrm{res}}}\,\widetilde\omega_2\bigl(\widehat\varepsilon_p,\ L_3^\circ\bigr) \ \in\ \mathcal H_{J,N} \ }
$$

und daraus das Primkanalgewicht
$\lvert c_p\rvert^2 := \lVert\Psi_p(\widehat\varepsilon_p)\rVert^2_{W_{\mathrm{res}}}$.

Mit der Fourierregel (43.1) $\widetilde\omega_2(e_uV_p, e_sV_m) = -us\log(p)\,e_{u+ps}V_{pm}$
und der Hebungsentwicklung $\widehat\varepsilon_p = \sum_u a_{p,u}\,e_uV_p$ folgt

$$
V_p(e_sV_m) \;=\; \widetilde\omega_2\bigl(\widehat\varepsilon_p, e_sV_m\bigr) \;=\; \sum_u a_{p,u}\,(-us\log p)\,\eta_{p;m;s,u} .
$$

$$
\boxed{\ \text{Die „Summationsreichweite über } u\text{" aus (51.1) ist die \textbf{Hebungswahl} } \widehat\varepsilon_p. \ \text{NEU-51 schreibt sie mit } a_{p,u}\equiv1. \ }
$$

Damit ist auch die Wirkungsseite entschieden: der Regulator sitzt auf der **Eingangsseite**,
als Wahl eines Vektors auf der $p$-Linie — nicht als Projektor $P_p$ auf dem Zielraum
$\mathscr F_p$.

### 1.2 Die Zulässigkeitsbedingung

NEU-153 §D.0 definiert die Hebungsfaser

$$
\mathcal L_p := \bigl\{\widehat\varepsilon\in B_3 \ :\ \pi_{\mathrm{prim}}(\widehat\varepsilon) = \varepsilon_p,\ \ \lVert\widehat\varepsilon\rVert_{\mathrm{conn}} = 1,\ \ \widehat\varepsilon \text{ hat Fourierladung}\bigr\},
\qquad \varepsilon_p = e_0V_p ,
$$

mit affiner Struktur

$$
\widehat\varepsilon_p = e_0V_p + f_p, \qquad f_p\in\ker\pi_{\mathrm{prim}} .
$$

$$
\boxed{\ \text{Der Regulator ist \textbf{nicht frei}: er ist auf die affine Faser } \mathcal L_p \ \text{eingeschränkt. Er ist aber auch nicht eindeutig.}\ }
$$

---

## 2. `[O-228-1b/1c]` — Option R2 ist in ihrer wörtlichen Form widerlegt

### 2.1 Was der Projektor tut

NEU-153 (Z. 179) wörtlich:

> *„**Der Ausgangshebungsvektor $e_uV_p$ mit $u\neq0$ allein ist keine zulässige Hebung**,
> denn er erfüllt nicht $\pi_{\mathrm{prim}}(e_uV_p) = \varepsilon_p$. Er liegt selbst im Kern."*

Also $\pi_{\mathrm{prim}}(e_0V_p) = \varepsilon_p$ und $\pi_{\mathrm{prim}}(e_uV_p) = 0$ für
$u\neq0$. Der Projektor **selektiert genau die Mode $u=0$**.

### 2.2 Fall C tritt ein

Der Kopplungskoeffizient in (43.1) ist $-us\log p$. Für $u=0$ verschwindet er identisch:

$$
\boxed{\ \widehat\varepsilon_p = e_0V_p \ \ (\text{d.h. } f_p=0) \quad\Longrightarrow\quad V_p^{\mathrm{can}} = 0 . \ }
$$

$$
\boxed{\ \text{Option R2 „} u \text{ durch den } p\text{-Kanalprojektor fixiert" vernichtet die Kopplung.} \quad \checkmark[M]_{\mathrm{neg}}\ }
$$

Genau deshalb verlangt NEU-153 (Z. 188) für eine zulässige Hebung ausdrücklich

$$
\widehat\varepsilon_p = e_0V_p + f_p, \qquad f_p\in\ker\pi_{\mathrm{prim}}, \qquad \boxed{f_p \neq 0} .
$$

Die Bedingung *„hat Fourierladung"* in $\mathcal L_p$ ist genau die Forderung $f_p\neq0$.

### 2.3 Rang: die Antwort auf `[O-228-1b]`

$$
\boxed{\ \dim P_p\mathscr F_{p;m,s} = 1 \ \text{trifft zu — aber für die \textbf{falsche} Mode } u=0. \ }
$$

Die verlangte Kombination aus Eindeutigkeit (`226-3a`) und Nichtnullheit (`226-3b`) ist mit
$\pi_{\mathrm{prim}}$ **nicht** gleichzeitig erfüllbar. Was $\pi_{\mathrm{prim}}$ eindeutig
auswählt, ist gerade das, was $\widetilde\omega_2$ annulliert.

$$
\boxed{\ \text{Die zulässige } u\text{-Menge ist } \{u\neq0\} \ \text{— also \textbf{unendlich}, nicht eine Mode.}\ }
$$

---

## 3. `[O-228-1d]` — Der Symmetrie-No-Go tritt nicht ein

Das bedingte Lemma lautete: existiert eine Fouriertranslation $U_k\eta_u = \eta_{u+k}$, die
erhalten werden muss, so kann kein nichtverschwindender Projektor mit eindimensionalem Bild
$\mathbb C\eta_{u_0}$ existieren.

**Die Voraussetzung ist nicht erfüllt.** Aus §2.1 gilt

$$
\pi_{\mathrm{prim}}\,U_k \;\neq\; U_k\,\pi_{\mathrm{prim}} ,
$$

denn $\pi_{\mathrm{prim}}U_k(e_0V_p) = \pi_{\mathrm{prim}}(e_kV_p) = 0$, aber
$U_k\pi_{\mathrm{prim}}(e_0V_p) = U_k\varepsilon_p \neq 0$ für $k\neq0$.

$$
\boxed{\ \text{Der } p\text{-Kanal bricht die volle Fouriertranslation \textbf{geometrisch}. Sie ist keine zu erhaltende Symmetrie. Fall D entfällt.} \quad \checkmark[M]\ }
$$

Das ist kein Freibrief: es bedeutet nur, dass die Einzelmodenselektion nicht an einer
Symmetrie scheitert — sie scheitert an §2.2.

---

## 4. `[O-228-1e]` / `[O-226-4]` — Der Gramoperator ist bereits offen

Die vorgeschlagene Zielstruktur

$$
\operatorname{Tr}(G^2) < \infty, \qquad \operatorname{Tr}G = \infty, \qquad G := V^*V
$$

verlangt die Gram-Matrix der Hebungsfaser. NEU-153 führt sie bereits und lässt sie offen:

| Größe | Befund | Status |
|---|---|---|
| $g^{(p)}_{uu}$, $u\neq0$ | $>0$ unter Positivdefinitheitsannahme; sonst unbekannt | `❓[O]` (NEU-153 Z. 461) |
| $g^{(p)}_{0u}$ | unbekannt | `❓[O]` (NEU-153 Z. 462) |
| Pullback induziert Hermiteform auf $\mathcal H_p^{\mathrm{lift}}$ | — | `❓[O]` (Z. 506) |
| Positivität/Definitheit dieser Form | — | `❓[O]` (Z. 507) |
| Vollständigkeit von $\mathcal H_p^{\mathrm{lift}}$ bzgl. $\lVert\cdot\rVert_{\mathrm{conn}}$ | — | `❓[O]` (Z. 508) |

$$
\boxed{\ [O\text{-}226\text{-}4] \ \text{ist kein neuer Knoten. Es ist NEU-153 §D.0.5, offen seit 13. Juli 2026.}\ }
$$

---

## 5. Der Rücklauf: die Schichtenverschiebung entkommt der alten Barriere nicht

NEU-153 führt drei Invarianzstufen, **alle offen**:

| Stufe | Aussage | Status |
|---|---|---|
| 153.A | Starke Vektorinvarianz $\Psi_p' = \Psi_p$ | `❓[O]` |
| 153.B | Schwache Norminvarianz $\lVert\Psi_p'\rVert = \lVert\Psi_p\rVert$ | `❓[O]` |
| 153.D.0 | Geometrie der Hebungsfaser $\mathcal L_p$ — vier Prüffragen | `❓[O]` |
| 153.D.0.5 | Hilbertgeometrische Entscheidung | `✓[M]` **bedingt**; Voraussetzungen `❓[O]` |

Ebene XVI führt dasselbe als `[O-221-1c1a0]`: *„Hebungsunabhängigkeit des zyklischen
Spektralmaßes $\mu^{D_N^{\mathrm{rel}}}_{\Psi_p}$"* — `❓[O]`.

$$
\boxed{\ \text{Solange 153.A/B offen sind, ist } V \ \text{und damit die Schattenklasse von } K(z) \ \textbf{hebungsabhängig}. \ }
$$

$$
\boxed{\ \text{Die neue Hauptlinie läuft in \textbf{dieselbe} Barriere wie die alte — von einer anderen Seite.}\ }
$$

**Das ist kein Rückschritt, sondern eine Konvergenz.** Zwei unabhängige Zugänge — der
Primkanalgewichtszugang aus Strang 05 und der Feshbach-Transferzugang aus Strang 01 —
enden am selben Knoten. Das erhöht dessen Gewicht erheblich: er ist nicht mehr eine
Nebenfrage der Primkanalgewichte, sondern die **Wohldefiniertheitsbedingung der gesamten
Transferschicht**.

---

## 6. Ein registriertes Leerfaser-Risiko

NEU-153 (Z. 207) hält eine mögliche Katastrophe fest:

> *„**Kritische Konsequenz:** Falls die verbundene Form positiv definit ist und $e_0V_p$
> bereits normiert und $\perp\ker\pi_{\mathrm{prim}}$ liegt, **existiert kein zulässiger Lift
> mit Fourierladung**. Die Menge $\mathcal L_p$ wäre leer."*

$$
\boxed{\ \mathcal L_p = \emptyset \quad\Longrightarrow\quad \text{es gibt \textbf{keine} zulässige Kopplung } V_p, \ \text{und die gesamte Feshbach-Linie entfällt.} \ }
$$

Dieser Fall ist quellenseitig **nicht ausgeschlossen**. Er ist der schärfste denkbare Ausgang
von `[O-226-3]` und muss vor jeder Schattenklassenrechnung geprüft werden. `❓[O]`

> **Umfang.** Ein leeres $\mathcal L_p$ widerlegt die **Feshbach-Transferlinie in dieser
> Konstruktion** — nicht HP-2 für Objekt X und nicht den Jacobi- oder Stieltjeskanal.

---

## 7. Klassifikation der drei Regulatoroptionen — abschließend

| Option | Beschreibung | Urteil |
|---|---|---|
| **R1** | gewichtete $u$-Summe mit freier Folge $w_{p,m,s}(u)$ | `✓[M]_neg` — freie Zusatzwahl, Anti-Fitting-Firewall (X.neg, A.8). **Nicht** ausgeschlossen sind Gewichte, die aus einem kanonischen Operatorfunktionalkalkül entstehen |
| **R2** | Auswahl durch $\pi_{\mathrm{prim}}$ | `✓[M]_neg` — selektiert $u=0$, vernichtet die Kopplung (§2.2) |
| **R3** | endliche Fourierprojektion $\lvert u\rvert\le U_p$ | `✓[M]_neg` für frei gewähltes $U_p$. Rehabilitierbar nur, wenn $\mathbf 1_{[-U_p,U_p]}(Q)$ Spektralprojektion eines kanonisch vorhandenen Ladungsoperators $Q$ ist **und** die Schwelle intrinsisch feststeht — beides gegenwärtig nicht gegeben |
| **R4** | **die tatsächliche Struktur:** Wahl von $\widehat\varepsilon_p\in\mathcal L_p$, d.h. $f_p\in\ker\pi_{\mathrm{prim}}\setminus\{0\}$ | `❓[O]` — eingeschränkt, aber nicht eindeutig. Intrinsisch **genau dann**, wenn 153.A oder 153.B gilt |

$$
\boxed{\ \text{Intrinsizität des Regulators } \iff \text{Hebungsunabhängigkeit (153.A/B).} \ }
$$

---

## 8. Reichweitenkorrektur zu den Schattenbedingungen

| Aussage | Status |
|---|---|
| $V\in\mathcal S_2 \Rightarrow \operatorname{Im}K(z)\in\mathcal S_1$, also ist $V\notin\mathcal S_2$ **notwendig** für den Nicht-$\mathcal S_1$-Zeugen | `✓[M]` (NEU-227 §2.7) |
| $V\in\mathcal S_4 \Rightarrow K(z)\in\mathcal S_2$ — **hinreichend**, nicht notwendig | `✓[M]` |
| $V\notin\mathcal S_4$ schließt $K(z)\in\mathcal S_2$ **nicht** aus — der Resolvent kann zusätzlich glätten | `✓[M]` |
| Zielmuster $\operatorname{Tr}(G^2)<\infty$, $\operatorname{Tr}G=\infty$ mit $G=V^*V$ | `❓[O]` — auswertbar erst nach `[O-226-4]` |

Die logische Zielstruktur ist damit asymmetrisch:

$$
V\notin\mathcal S_2 \ \text{notwendig für den Nicht-}\mathcal S_1\text{-Nachweis;} \qquad
V\in\mathcal S_4 \ \text{hinreichend für Hilbert–Schmidt.}
$$

---

## 9. Statusbilanz

| Aussage | Status |
|---|---|
| $u$-Summe = Hebungsentwicklung, nicht freier Regulator | `✓[M]` |
| Regulator wirkt eingangsseitig ($Q_p$), nicht zielseitig ($P_p$) | `✓[M]` |
| $\pi_{\mathrm{prim}}(e_0V_p)=\varepsilon_p$, $\pi_{\mathrm{prim}}(e_uV_p)=0$ für $u\neq0$ | `✓[M]` (153 Z.179) |
| **Option R2 vernichtet die Kopplung (Fall C)** | **`✓[M]_neg`** |
| Zulässige $u$-Menge ist $\{u\neq0\}$, unendlich | `✓[M]` |
| Eindeutigkeit und Nichtnullheit gleichzeitig mit $\pi_{\mathrm{prim}}$ | `✓[M]_neg` unmöglich |
| Symmetrie-No-Go (Fall D) | `✓[M]` **tritt nicht ein** — $\pi_{\mathrm{prim}}$ bricht Translation selbst |
| Gramoperator $g^{(p)}_{uu}$, $g^{(p)}_{0u}$ | `❓[O]` — NEU-153 Z.461/462, nicht neu |
| $[O\text{-}226\text{-}3] \equiv [O\text{-}153] \equiv [O\text{-}221\text{-}1c1a0]$ | `✓[M]` |
| Hebungsunabhängigkeit 153.A/B | `❓[O]` |
| Leerfaser-Risiko $\mathcal L_p=\emptyset$ | `❓[O]` — quellenseitig nicht ausgeschlossen |
| Schattenklasse von $K(z)$ ist ohne 153.A/B **hebungsabhängig** | `✓[M]` |

---

## 10. Nächste Knoten

| Knoten | Aufgabe | Priorität |
|---|---|---|
| `[O-228-2]` | **Leerfaser zuerst.** Ist $\mathcal L_p\neq\emptyset$? Konkret: liegt $e_0V_p$ orthogonal zu $\ker\pi_{\mathrm{prim}}$ bezüglich $\langle\cdot,\cdot\rangle_{\mathrm{conn}}$? (NEU-153 Z.207) | **1** |
| `[O-153-A/B]` | Hebungsunabhängigkeit — starke Vektorinvarianz oder schwache Norminvarianz | **2** |
| `[O-226-4]` | Gramoperator $g^{(p)}_{0u}$, $g^{(p)}_{uu}$; Positivität, Vollständigkeit (NEU-153 §D.0.5) | **3** |
| `[O-226-5/6]` | $\mathcal S_2$-Kriterium und Nicht-$\mathcal S_1$-Zeuge — **gesperrt** bis 1–3 | danach |
| `[O-225-3]` | Zusammengesetzte Sektoren | parallel möglich |

> **Sperrvermerk.** Keine Schattenklassenrechnung vor `[O-228-2]`. Ein leeres $\mathcal L_p$
> würde die gesamte Rechnung gegenstandslos machen.

> **Anti-Fitting.** Der Hebungsparameter $f_p$ darf **nicht** so gewählt werden, dass
> $\mathcal S_2\setminus\mathcal S_1$ oder die $\Xi$-Identität herauskommt. Nur ein aus
> $\mathcal L_p$ **intrinsisch** bestimmter oder ein hebungsunabhängiger Wert ist zulässig.

---

## Abhängigkeiten

| Referenz | Verwendet für |
|---|---|
| NEU-41 | Kopplungsoperator, $\Psi_p$, Wohlbestimmtheitsbedingung (41.4) |
| NEU-43 | (43.1) $\widetilde\omega_2(e_uV_p,e_sV_m)=-us\log(p)e_{u+ps}V_{pm}$ |
| NEU-51 | (51.1) Regulatoroptionen, (51.2) Kopplungsform |
| **NEU-153** | $\Psi_p(\widehat\varepsilon_p)$, Faser $\mathcal L_p$, $\pi_{\mathrm{prim}}$, Z.179/188/207, Gram $g^{(p)}$, Stufen 153.A/B/D.0 |
| NEU-157 | $K_p=\ker\pi_{\mathrm{prim}}$, affine Faser, $\mathcal A_p^{\mathrm{adm}}$ |
| NEU-221e | Spektralmaßabstieg $\Psi_p$, Hebungsfaser |
| NEU-225/226/227 | Transportgenerator, Primkanalüberlappung, Spektralmaßform |
