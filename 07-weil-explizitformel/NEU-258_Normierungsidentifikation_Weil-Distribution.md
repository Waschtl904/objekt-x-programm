# NEU-258 — Normierungsidentifikation der Repo-Weil-Form mit der Literatur-Weil-Distribution

**Katalog-ID:** NEU-258  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07 (Patch 1: 2026-08-08)  
**Auftrag:** Einmaliger formaler Abgleich aller Normierungsfaktoren: Fourierkonvention, Polterme, Gammafaktor, Primzahlpotenzgewicht, Koordinate $s=\frac{1}{2}+it$. Schließt NEU-257 Buchung $(1\text{-Norm})$.  
**Patch 1:** §4–6 vollständig neu typisiert. Vier Fehler behoben: (i) fehlender $1/\pi$-Faktor in $B_\Gamma$; (ii) Testfunktionsebenen-Verwechslung $\hat g = \hat a$; (iii) fehlerhafte $\operatorname{Re}\gamma_\infty$-Definition ohne $1/2$-Faktor; (iv) algebraisch falsche $p^{-k/2}$-Nennerform im Prim-Literaturausdruck.  
**Vorgänger:** NEU-257 (Patch), NEU-252 (Patch), NEU-220k, NEU-220b, NEU-220d

---

## 0. Ziel

Die in NEU-257 verwendeten Sätze (Bochner-Schwartz; Benedetto-Joyner RH $\Leftrightarrow$ $W\in\mathcal{S}'$; Weils Positivitätskriterium; Suzuki $\mathcal{H}_W\cong L^2(\tau)$) gelten nur für die kanonische normalisierte Weil-Distribution $W_{\rm Lit}$. Dieser Knoten identifiziert $W_{\rm NEU-252}=W_{\rm Lit}$ explizit durch Nebeneinanderschreiben aller relevanten Faktoren.

---

## 1. Fourierkonvention (NEU-220k, verbindlich)

$$
\boxed{\hat f(t):=\int_{\mathbb{R}}f(u)\,e^{itu}\,du,\qquad\|\hat f\|_2^2=2\pi\|f\|_2^2.} \qquad (1\text{-FC})
$$

Das ist die **analyst's convention** mit $e^{+itu}$ (nicht $e^{-itu}$). Suzuki 2011/2026 verwendet dieselbe Konvention (vgl. Suzuki 2011, S. 1, Notation). Bombieri 2000 §3 setzt ebenfalls $\hat f(s)=\int f(u)e^{su}\,du$ auf $\operatorname{Re}(s)=0$, also $s=it$, identisch zu $(1\text{-FC})$.

$$
\text{Fourierkonvention: Repo = Literatur.}\quad\checkmark[K/M] \qquad (1\text{-FC-Check})
$$

---

## 2. Koordinate und kritische Linie

Die Weil-Distribution wird über die Testfunktion
$$
g(u):=h(e^{u/2})e^{u/2}, \qquad h\in C_c^\infty(\mathbb{R}_{>0}) \qquad (2\text{-Change})
$$
von der multiplikativen Gruppe $\mathbb{R}_{>0}$ auf die additive Gruppe $\mathbb{R}$ gehoben. In der Koordinate $s=\frac{1}{2}+it$:
$$
\hat g(t)=\int_{\mathbb{R}}g(u)\,e^{itu}\,du=\hat h\left(\tfrac{1}{2}+it\right):=H\left(\tfrac{1}{2}+it\right). \qquad (2\text{-Coord})
$$

Suzuki (2011, (0.1)) und Weil (1952, §5) schreiben das Positivitätskriterium in der Form:
$$
\sum_\rho H(\rho)+\text{Polterme}+\text{Primterme}\ge0 \qquad (2\text{-Weil})
$$
mit $\rho=\frac{1}{2}+i\gamma$ unter RH, also $H$ ausgewertet auf der kritischen Linie. Das stimmt mit der Repo-Konvention $s=\frac{1}{2}+it$ und $(2\text{-Coord})$ überein.

$$
\text{Koordinate }s=\tfrac{1}{2}+it:\text{ Repo = Literatur.}\quad\checkmark[K/M] \qquad (2\text{-Check})
$$

---

## 3. Polterme

Die Repo-Polterme (NEU-252, §3, $(\text{A-Pole})$):
$$
B_{\rm pole}(a,b) = h_{a,b}\!\left(\tfrac{i}{2}\right)+h_{a,b}\!\left(-\tfrac{i}{2}\right),\qquad h_{a,b}(z):=\widehat{g_{a,b}}(z). \qquad (3\text{-Repo})
$$

Die Weil-Explizitformel-Polterme (Bombieri 2000 §3; Suzuki 2011 (0.1)): In der additiven Koordinate $u=\log x$ kommen Beiträge von $s=1$ (trivialer Pol) und $s=0$ (Pol bei $0$), entsprechend Auswertungen von $H$ bei $\frac{1}{2}+i\cdot\frac{i}{2}=0$ und $\frac{1}{2}+i\cdot(-\frac{i}{2})=1$, also
$$
H(0)+H(1)=\widehat{g_{a,b}}\!\left(\tfrac{i}{2}\right)+\widehat{g_{a,b}}\!\left(-\tfrac{i}{2}\right)=B_{\rm pole}(a,b). \qquad (3\text{-Lit})
$$

$$
\text{Polterme: Repo = Literatur (identische Auswertungspunkte).}\quad\checkmark[K/M] \qquad (3\text{-Check})
$$

---

## 4. Gammafaktor / archimedischer Block

**Definitionen** (NEU-220b, NEU-220d, NEU-252; autoritativ):
$$
\boxed{h_{a,b}(z) := \widehat{g_{a,b}}(z) = \int_{\mathbb{R}} g_{a,b}(u)\,e^{izu}\,du} \qquad (4\text{-hab})
$$
$h_{a,b}$ ist eine ganze Paley-Wiener-Funktion (NEU-252).

$$
\boxed{\gamma_\infty(t) := -\frac{1}{2}\log\pi + \frac{1}{2}\psi\!\left(\frac{1}{4}+\frac{it}{2}\right)} \qquad (4\text{-gam})
$$
wobei $\psi = \Gamma'/\Gamma$ die Digammafunktion bezeichnet. Diese Definition stimmt mit NEU-220b überein.

$$
\boxed{\Lambda_\Gamma(h) := \frac{1}{2\pi}\int_{\mathbb{R}} \gamma_\infty(t)\,h(t)\,dt} \qquad (4\text{-LamGam})
$$

**Masterform** (NEU-220k, NEU-252; autoritativ, Faktor $2$ darf nicht stillschweigend entfernt werden):
$$
\boxed{B_\Gamma(a,b) := 2\Lambda_\Gamma(h_{a,b}).} \qquad (4\text{-BG-Master})
$$

**Diagonalkorollar.** Auf der Diagonale gilt
$$
h_{a,a}(t) = \widehat{g_{a,a}}(t) = \frac{1}{2}\bigl(|\hat a(t)|^2+|\hat a(-t)|^2\bigr), \qquad (4\text{-diag-h})
$$
und $\operatorname{Re}\gamma_\infty(t)$ ist gerade. Daher:
$$
\boxed{B_\Gamma(a,a) = \frac{1}{\pi}\int_{\mathbb{R}} |\hat a(t)|^2 \operatorname{Re}\gamma_\infty(t)\,dt.} \qquad (4\text{-BG-diag})
$$

Äquivalent (nach Auflösen von $(4\text{-gam})$):
$$
\boxed{B_\Gamma(a,a) = \frac{1}{2\pi}\int_{\mathbb{R}} \left[\operatorname{Re}\psi\!\left(\frac{1}{4}+\frac{it}{2}\right)-\log\pi\right]|\hat a(t)|^2\,dt.} \qquad (4\text{-BG-Suzuki})
$$

Das ist genau Suzukis archimedischer Fourierblock (2026).

**Literaturabgleich.** In der Weil-Explizitformel (Bombieri 2000 §3; Suzuki 2011 (0.1); Suzuki 2026) erscheint der archimedische Beitrag:
$$
\frac{1}{2\pi}\int_{-\infty}^{\infty}\left[\operatorname{Re}\psi\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right)-\log\pi\right]|\hat a(t)|^2\,dt. \qquad (4\text{-Lit})
$$

Nach $(4\text{-BG-Suzuki})$ gilt $(4\text{-BG-diag}) = (4\text{-Lit})$. ✓

$$
\text{Gammafaktor: Repo = Literatur (exakt, ohne Absorptionsbehauptung).}\quad\checkmark[K/M] \qquad (4\text{-Check})
$$

---

## 5. Primzahlpotenzgewicht

**Repo-Primblock** (verbindliche M3-Form, NEU-252, $(\text{A-Fin})$):
$$
\boxed{B_{\rm fin}(a,b)=-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt{n}}\,g_{a,b}(\log n).} \qquad (5\text{-Repo})
$$

**Literaturabgleich.** Suzukis kanonische Weil-Distribution (Suzuki 2026, Bombieri 2000 (3.2)) hat für beide Richtungen denselben Faktor $\Lambda(n)/\sqrt{n}$:
$$
-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt{n}}\bigl[g(\log n)+g(-\log n)\bigr]. \qquad (5\text{-Lit})
$$

Für gerades $g_{a,b}$ (d.h. $g_{a,b}(-u)=g_{a,b}(u)$) gilt $g_{a,b}(-\log n)=g_{a,b}(\log n)$, also stimmen $(5\text{-Repo})$ und $(5\text{-Lit})$ überein.

$$
\text{Vorfaktor }-2\Lambda(n)/\sqrt{n}\text{: Repo = Literatur.}\quad\checkmark[K/M] \qquad (5\text{-Check})
$$

---

## 6. Gesamtidentifikation

Alle fünf Bestandteile stimmen überein:

| Bestandteil | Repo (NEU-252/220k) | Literatur | Status |
|---|---|---|---|
| Fourierkonvention | $\hat f(t)=\int fe^{itu}du$ | Suzuki 2011/2026; Bombieri 2000 | $\checkmark[K/M]$ |
| Koordinate | $s=\frac{1}{2}+it$, $t\in\mathbb{R}$ | Weil 1952; Suzuki 2011 | $\checkmark[K/M]$ |
| Polterme | $h_{a,b}(i/2)+h_{a,b}(-i/2)$ | $H(0)+H(1)$ | $\checkmark[K/M]$ |
| Gammafaktor | $B_\Gamma=2\Lambda_\Gamma(h_{a,b})$, $\Lambda_\Gamma=\frac{1}{2\pi}\int\gamma_\infty h$ | Suzuki 2026 $(4\text{-Lit})$ | $\checkmark[K/M]$ |
| Primvorfaktor | $-2\Lambda(n)/\sqrt{n}$ | $-2\Lambda(n)/\sqrt{n}$ | $\checkmark[K/M]$ |

$$
\boxed{W_{\rm NEU-252}=W_{\rm Lit}.\quad\checkmark[K/M]} \qquad (6\text{-ID})
$$

---

## 7. Freigeschaltete NEU-257-Buchungen

Mit $(6\text{-ID})$ ist der Normierungsvorbehalt $(1\text{-Norm})$ aus NEU-257 geschlossen. Alle vier NEU-257-Buchungen sind jetzt ohne Vorbehalt hart:

$$
\boxed{L^2\text{-Semibeschränktheit von }B_W\Longleftrightarrow\text{RH.}\quad\checkmark[K/M]} \qquad (7\text{-a})
$$
$$
\boxed{\text{RH}\Longrightarrow B_W\text{ nicht abschließbar auf Haar-}L^2(\mathbb{R},du).\quad\checkmark[K/M]} \qquad (7\text{-b})
$$
$$
\boxed{\text{Kato/KLMN auf }H_0=L^2(\mathbb{R},du):\;\times[M].} \qquad (7\text{-c})
$$
$$
\boxed{\mathcal{H}_W\cong L^2(\tau)\cong\ell^2(\Gamma,m_\gamma)\quad\checkmark[K/M]\text{ (konditional unter RH, Suzuki 2025/2026).}} \qquad (7\text{-d})
$$

---

## 8. Neue Forschungsfrage (NEU-259-Vorbereitung)

Mit dem Normabgleich ist die verbleibende offene Frage des Programms klar:

$$
\boxed{\text{Kann }\mathcal{K}_X\text{ arithmetisch (BC/adelisch) RH-frei konstruiert werden, so dass }\mathcal{K}_X\xrightarrow{\rm RH}L^2(\tau)\cong\ell^2(\Gamma,m_\gamma)?} \qquad (8\text{-ObjX})
$$

Drei Wege nach NEU-259:

| Weg | Ansatz | Suzuki-Bezug |
|---|---|---|
| BC-/adelische Spektralquelle | Positive arithmetische Algebra/Spur erzeugt $\mu_X$ ohne Nullstellen; zeige $\mu_X\xrightarrow{\rm RH}\sum_\gamma m_\gamma\delta_\gamma$ | Indirekt (globale Struktur) |
| Finite-Intervall-Grenzwert | RH-freie positive Räume $\mathcal{H}_T$, Grenzwert $\mathcal{H}_T\to\mathcal{K}_X$ | Direkt (Suzuki endliche Screw-Function-Räume) |
| Moment-/Resolventenweg | Positive Resolvente/Momente aus BC/Adelen; spektrale Daten $\xrightarrow{\rm RH}$ Weil-Daten | NEU-221-Modernisierung |

$$
\boxed{\text{Objekt X = RH-frei konstruierte arithmetische Spektralgeometrie }\mathcal{K}_X,\text{ deren RH-Bild }\mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma)\text{ ist.}} \qquad (8\text{-ObjXDef})
$$

---

## 9. Statusbuchungen

$$W_{\rm NEU-252}=W_{\rm Lit}\text{ (alle fünf Faktoren)}\quad\checkmark[K/M]\qquad(9\text{-a})$$
$$\text{NEU-257 Buchung }(1\text{-Norm}): \text{geschlossen}\quad\checkmark[K/M]\qquad(9\text{-b})$$
$$\text{NEU-257 Buchungen (1)–(4): alle hart (vorbehaltlos)}\quad\checkmark[K/M]\qquad(9\text{-c})$$
$$\text{Forschungsfrage NEU-259}\quad?[O]\qquad(9\text{-d})$$

---

## 10. Abhängigkeiten

| Referenz | SHA/Quelle | Inhalt |
|---|---|---|
| NEU-257 (Patch) | 160433a | Alle vier Firewall-Buchungen (Normvorbehalt jetzt geschlossen) |
| NEU-252 (Patch) | 3d6b091 | $B_W=B_{\rm pole}+B_\Gamma+B_{\rm fin}$, M3-Formeln, $h_{a,b}:=\widehat{g_{a,b}}$ |
| NEU-220k (Masterkontur) | dc45cf8 | $\Lambda_\Gamma$-Normierung; Faktor-2-Warnung; verbindlich |
| NEU-220d | 7ff3afe | $\Lambda_\Gamma(h)=\frac{1}{2\pi}\int\gamma_\infty h$; archimedische Rohform |
| NEU-220b | 01c6d23 | $\gamma_\infty(t)=-\frac{1}{2}\log\pi+\frac{1}{2}\psi(\frac{1}{4}+\frac{it}{2})$; autoritativ |
| Weil 1952 | — | Explizitformel; Positivitätskriterium |
| Bombieri 2000 | §3, (3.2) | Normierungsform der Explizitformel |
| Suzuki 2011 | (0.1), (1.2) | Weil-Positivitätskriterium; $\mathcal{H}_W\cong L^2(\tau)$ |
| Suzuki 2025/2026 | Thm. 2.1 | $\mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma)$ explizit; archimedischer Fourierblock |
| Benedetto-Joyner | — | $W\in\mathcal{S}'\Leftrightarrow$ RH |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07. Patch 1 (2026-08-08): §4–6 vollständig neu typisiert. Vier Fehler behoben: $1/\pi$-Faktor, Testfunktionsebenen, $\gamma_\infty$-Definition, Prim-Literatur-Zwischenform. Schließt NEU-257 $(1\text{-Norm})$; gibt NEU-259 frei.*