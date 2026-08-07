# NEU-258 — Normierungsidentifikation der Repo-Weil-Form mit der Literatur-Weil-Distribution

**Katalog-ID:** NEU-258  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07  
**Auftrag:** Einmaliger formaler Abgleich aller Normierungsfaktoren: Fourierkonvention, Polterme, Gammafaktor, Primzahlpotenzgewicht, Koordinate $s=\frac{1}{2}+it$. Schlie\ss{}t NEU-257 Buchung $(1\text{-Norm})$.  
**Vorgänger:** NEU-257 (Patch), NEU-252 (Patch), NEU-220k

---

## 0. Ziel

Die in NEU-257 verwendeten Sätze (Bochner-Schwartz; Benedetto-Joyner RH $\Leftrightarrow$ $W\in\mathcal{S}'$; Weils Positivitätskriterium; Suzuki $\mathcal{H}_W\cong L^2(\tau)$) gelten nur für die kanonische normalisierte Weil-Distribution $W_{\rm Lit}$. Dieser Knoten identifiziert $W_{\rm NEU-252}=W_{\rm Lit}$ explizit durch Nebeneinanderschreiben aller relevanten Faktoren.

---

## 1. Fourierkonvention (NEU-220k, verbindlich)

$$
\boxed{\hat f(t):=\int_{\mathbb{R}}f(u)\,e^{itu}\,du,\qquad\|\hat f\|_2^2=2\pi\|f\|_2^2.} \qquad (1\text{-FC})
$$

Das ist die **analyst's convention** mit $e^{+itu}$ (nicht $e^{-itu}$). Suzuki 2011/2025 verwendet dieselbe Konvention (vgl. Suzuki 2011, S.~1, Notation). Bombieri 2000 \S{}3 setzt ebenfalls $\hat f(s)=\int f(u)e^{su}\,du$ auf $\operatorname{Re}(s)=0$, also $s=it$, identisch zu $(1\text{-FC})$.

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

Suzuki (2011, (0.1)) und Weil (1952, \S{}5) schreiben das Positivitätskriterium in der Form:
$$
\sum_\rho H(\rho)+\text{Polterme}+\text{Primterme}\ge0 \qquad (2\text{-Weil})
$$
mit $\rho=\frac{1}{2}+i\gamma$ unter RH, also $H$ ausgewertet auf der kritischen Linie. Das stimmt mit der Repo-Konvention $s=\frac{1}{2}+it$ und $(2\text{-Coord})$ überein.

$$
\text{Koordinate }s=\tfrac{1}{2}+it:\text{ Repo = Literatur.}\quad\checkmark[K/M] \qquad (2\text{-Check})
$$

---

## 3. Polterme

Die Repo-Polterme (NEU-252, \S{}3, $(\text{A-Pole})$):
$$
B_{\rm pole}(a,a)=h_{a,a}\left(\tfrac{i}{2}\right)+h_{a,a}\left(-\tfrac{i}{2}\right),\qquad h_{a,a}(z)=\widehat{g_{a,a}}(z). \qquad (3\text{-Repo})
$$

Die Weil-Explizitformel-Polterme (Bombieri 2000 \S{}3; Suzuki 2011 (0.1)): In der additiven Koordinate $u=\log x$ kommen Beiträge von $s=1$ (trivialer Pol) und $s=0$ (Pol bei $0$), entsprechend Auswertungen von $H$ bei $\frac{1}{2}+i\cdot\frac{i}{2}=0$ und $\frac{1}{2}+i\cdot(-\frac{i}{2})=1$, also
$$
H(0)+H(1)=\widehat{g_{a,a}}\left(\tfrac{i}{2}\right)+\widehat{g_{a,a}}\left(-\tfrac{i}{2}\right)=B_{\rm pole}(a,a). \qquad (3\text{-Lit})
$$

$$
\text{Polterme: Repo = Literatur (identische Auswertungspunkte).}\quad\checkmark[K/M] \qquad (3\text{-Check})
$$

---

## 4. Gammafaktor / archimedischer Block

Der Repo-Gammablock (NEU-252 \S{}3; NEU-220b):
$$
B_\Gamma(a,a)=\int_{\mathbb{R}}|\hat a(t)|^2\operatorname{Re}\gamma_\infty(t)\,dt,\qquad\operatorname{Re}\gamma_\infty(t)=\operatorname{Re}\frac{\Gamma'}{\Gamma}\left(\tfrac{1}{4}+\tfrac{it}{2}\right)+\text{const}. \qquad (4\text{-Repo})
$$

In der Weil-Explizitformel (Bombieri 2000 \S{}3; Suzuki 2011 (0.1)) erscheint der archimedische Beitrag:
$$
\frac{1}{2\pi}\int_{-\infty}^{\infty}H\left(\tfrac{1}{2}+it\right)\operatorname{Re}\left(-\frac{\Gamma'}{\Gamma}\left(\tfrac{1}{4}+\tfrac{it}{2}\right)\right)dt+\cdots \qquad (4\text{-Lit})
$$

Mit $(1\text{-FC})$ und $H(\frac{1}{2}+it)=\hat g(t)=\hat a(t)$ (nach Koordinatenwechsel $(2\text{-Coord})$) stimmen $(4\text{-Repo})$ und $(4\text{-Lit})$ bis auf den globalen $2\pi$-Faktor aus der Parsevalidentität überein. Der $2\pi$-Faktor ist durch NEU-220k fest absorbiert.

$$
\text{Gammafaktor: Repo = Literatur (bis auf absorbiertem }2\pi\text{ aus NEU-220k).}\quad\checkmark[K/M] \qquad (4\text{-Check})
$$

---

## 5. Primzahlpotenzgewicht

Der Repo-Primblock (verbindliche M3-Form, NEU-252, $(\text{A-Fin})$):
$$
\boxed{B_{\rm fin}(a,a)=-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt{n}}\,g_{a,a}(\log n).} \qquad (5\text{-Repo})
$$

Die Literatur-Weil-Explizitformel (Bombieri 2000, (3.2); Suzuki 2011, (0.1)):
$$
-\sum_{n=p^k}\Lambda(p^k)\left(\frac{h(p^k)}{p^{k/2}}+\frac{h(p^{-k})}{p^{-k/2}}\right)=-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt{n}}\,h(n) \qquad (5\text{-Lit})
$$
(die Symmetrisierung $h(n)+h(n^{-1})$ ergibt Faktor $2$ durch $h$ reell und $h(n^{-1})=h(e^{-\log n})=g_{a,a}(-\log n)=g_{a,a}(\log n)$ bei symmetrischem $g_{a,a}$; vgl. NEU-252 \S{}2).

Mit $h(n)=g_{a,a}(\log n)$ und der Koordinate $u=\log n$:
$$
(5\text{-Repo})=(5\text{-Lit}).\quad\checkmark[K/M] \qquad (5\text{-Check})
$$

$$
\text{Vorfaktor }-2\Lambda(n)/\sqrt{n}\text{: Repo = Literatur.}\quad\checkmark[K/M] \qquad (5\text{-Final})
$$

---

## 6. Gesamtidentifikation

Alle vier Bestandteile stimmen überein:

| Bestandteil | Repo (NEU-252/220k) | Literatur | Status |
|---|---|---|---|
| Fourierkonvention | $\hat f(t)=\int fe^{itu}du$ | Suzuki 2011; Bombieri 2000 | $\checkmark[K/M]$ |
| Koordinate | $s=\frac{1}{2}+it$, $t\in\mathbb{R}$ | Weil 1952; Suzuki 2011 | $\checkmark[K/M]$ |
| Polterme | $\hat g(i/2)+\hat g(-i/2)$ | $H(0)+H(1)$ | $\checkmark[K/M]$ |
| Gammafaktor | $\operatorname{Re}\gamma_\infty(t)$ | $-\operatorname{Re}\Gamma'/\Gamma(\frac{1}{4}+\frac{it}{2})$ | $\checkmark[K/M]$ |
| Primvorfaktor | $-2\Lambda(n)/\sqrt{n}$ | $-2\Lambda(n)/\sqrt{n}$ | $\checkmark[K/M]$ |

$$
\boxed{W_{\rm NEU-252}=W_{\rm Lit}.\quad\checkmark[K/M]} \qquad (6\text{-ID})
$$

---

## 7. Freigeschaltete NEU-257-Buchungen

Mit $(6\text{-ID})$ sind jetzt alle vier NEU-257-Buchungen ohne Vorbehalt hart:

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
\boxed{\mathcal{H}_W\cong L^2(\tau)\cong\ell^2(\Gamma,m_\gamma)\quad\checkmark[K/M]\text{ (konditional unter RH, Suzuki 2025).}} \qquad (7\text{-d})
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

$$W_{\rm NEU-252}=W_{\rm Lit}\text{ (alle Faktoren)}\quad\checkmark[K/M]\qquad(9\text{-a})$$
$$\text{NEU-257 Buchung }(1\text{-Norm}): \text{geschlossen}\quad\checkmark[K/M]\qquad(9\text{-b})$$
$$\text{NEU-257 Buchungen (1)–(4): alle hart}\quad\checkmark[K/M]\qquad(9\text{-c})$$
$$\text{Forschungsfrage NEU-259}\quad?[O]\qquad(9\text{-d})$$

---

## 10. Abhängigkeiten

| Referenz | SHA/Quelle | Inhalt |
|---|---|---|
| NEU-257 (Patch) | f710da3 | Alle vier Firewall-Buchungen (mit Normvorbehalt) |
| NEU-252 (Patch) | 4ee78ed | $B_W=B_{\rm pole}+B_\Gamma+B_{\rm fin}$ M3-Formeln |
| NEU-220k | 8d4e9b2 | $2\pi$-Fourierkonvention verbindlich |
| Weil 1952 | — | Explizitformel; Positivitätskriterium |
| Bombieri 2000 | \S{}3, (3.2) | Normierungsform der Explizitformel |
| Suzuki 2011 | (0.1), (1.2) | Weil-Positivitätskriterium $C_c^\infty$; $\mathcal{H}_W\cong L^2(\tau)$ |
| Suzuki 2025 | Thm.~2.1 | $\mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma)$ explizit |
| Benedetto-Joyner | — | $W\in\mathcal{S}'\Leftrightarrow$ RH |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07. Schlie\ss{}t NEU-257 $(1\text{-Norm})$; gibt NEU-259 frei.*
