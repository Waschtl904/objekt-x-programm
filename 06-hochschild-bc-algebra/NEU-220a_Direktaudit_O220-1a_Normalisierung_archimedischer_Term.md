# NEU-220a — Direktaudit $[O\text{-}220\text{-}1a]$: Exakte Normalisierung des archimedischen Weil-/Gammafaktorterms

**Stand:** 2026-08-05  
**Repository:** Waschtl904/objekt-x-programm  
**Typ:** Geschlossener Auditknoten  
**Vorgänger:** NEU-220 (Commit b749e3f)  
**Geprüfte Datei:** `NEU-220_Eroeffnung_Archimedischer_Weil_Gammafaktorpfad.md`

---

## 1. Gesamturteil

$$\boxed{[O\text{-}220\text{-}1a]\quad\checkmark[M]}$$

Eine vollständig normalisierte Fassung liegt vor. Festgelegt sind:
- Fouriertransformation und Inversion;
- Nullstellen-, Pol-, Prim- und archimedischer Term;
- sämtliche Faktoren $2\pi$, $\log\pi$ und Digammaargumente;
- die Distribution $W_\infty$;
- das Funktional $\Lambda_\infty$;
- ein kanonischer gemeinsamer Testfunktionskern;
- Realitätssymmetrie und Eindeutigkeit;
- drei unabhängige Normalisierungstests.

Der archimedische Term umfasst den vollständigen Faktor
$$
\Gamma_{\mathbb{R}}(s) = \pi^{-s/2}\Gamma(s/2).
$$
Insbesondere gehört $-f(0)\log\pi$ zum archimedischen Kanal, **nicht** zum Polterm.

---

## 2. Verbindliche Fourierkonvention

$$
\boxed{\hat{f}(t) = \int_{\mathbb{R}} f(u)\,e^{-itu}\,du}
$$
$$
\boxed{f(u) = \frac{1}{2\pi}\int_{\mathbb{R}} \hat{f}(t)\,e^{itu}\,dt}
$$

Involution:
$$
\boxed{f^\sharp(u) = \overline{f(-u)}}
$$

Dann gilt $\widehat{f^\sharp}(t)=\overline{\hat{f}(t)}$ und:
$$
\boxed{\widehat{h^\sharp*f}(t) = \overline{\hat{h}(t)}\,\hat{f}(t).}
$$

Die sesquilineare Konvention ist:
$$
Q_\infty(f,h) = \Lambda_\infty(h^\sharp * f),
$$
linear in $f$, konjugiert-linear in $h$.

---

## 3. Autoritative Referenzformel

Referenz: **Guinand–Weil-Formel** in der Normalisierung
$$
\hat{h}_{!2\pi}(x) = \int_{\mathbb{R}} h(t)\,e^{-2\pi ixt}\,dt.
$$

Sie lautet:
$$
\sum_\rho h\!\left(\frac{\rho-\tfrac12}{i}\right)
= h\!\left(\tfrac{1}{2i}\right) + h\!\left(-\tfrac{1}{2i}\right)
- \frac{\hat{h}_{!2\pi}(0)}{2\pi}\log\pi
+ \frac{1}{2\pi}\int_{\mathbb{R}} h(t)\,\operatorname{Re}\psi\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right)dt
- \frac{1}{2\pi}\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt{n}}
\Bigl[\hat{h}_{!2\pi}\!\left(\tfrac{\log n}{2\pi}\right)+\hat{h}_{!2\pi}\!\left(-\tfrac{\log n}{2\pi}\right)\Bigr],
$$
mit $\psi(z)=\Gamma'(z)/\Gamma(z)$, über nichttriviale Nullstellen mit Multiplizität, ohne Annahme der Riemannschen Vermutung.

---

## 4. Umrechnung auf die Projektkonvention

Setze $h(t)=\hat{f}(t)$. Dann:
$$
\hat{h}_{!2\pi}(x) = 2\pi f(-2\pi x), \quad
\hat{h}_{!2\pi}(0) = 2\pi f(0),
$$
$$
\hat{h}_{!2\pi}\!\left(\tfrac{\log n}{2\pi}\right) = 2\pi f(-\log n), \quad
\hat{h}_{!2\pi}\!\left(-\tfrac{\log n}{2\pi}\right) = 2\pi f(\log n).
$$

Vollständig konvertierte Formel:
$$
\boxed{
\sum_\rho \hat{f}\!\left(\frac{\rho-\tfrac12}{i}\right)
= \hat{f}\!\left(\tfrac{i}{2}\right) + \hat{f}\!\left(-\tfrac{i}{2}\right)
+ \Lambda_\infty(f)
- \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt{n}}\bigl(f(\log n)+f(-\log n)\bigr).}
$$

Hier ist:
$$
\boxed{
\Lambda_\infty(f)
= -f(0)\log\pi
+ \frac{1}{2\pi}\int_{\mathbb{R}} \hat{f}(t)\,\operatorname{Re}\psi\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right)dt.}
$$

---

## 5. Kompakte Form über $\Gamma_{\mathbb{R}}$

$$
\boxed{\Gamma_{\mathbb{R}}(s) = \pi^{-s/2}\Gamma(s/2)}
$$

$$
\frac{\Gamma_{\mathbb{R}}'}{\Gamma_{\mathbb{R}}}(s)
= -\tfrac{1}{2}\log\pi + \tfrac{1}{2}\psi(s/2).
$$

Auf der kritischen Geraden $s=\tfrac{1}{2}+it$:
$$
2\operatorname{Re}\frac{\Gamma_{\mathbb{R}}'}{\Gamma_{\mathbb{R}}}\!\left(\tfrac{1}{2}+it\right)
= \operatorname{Re}\psi\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right) - \log\pi.
$$

Damit:
$$
\boxed{
\Lambda_\infty(f)
= \frac{1}{2\pi}\int_{\mathbb{R}} \hat{f}(t)\,A_\infty(t)\,dt,}
\qquad
\boxed{A_\infty(t) = \operatorname{Re}\psi\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right) - \log\pi.}
$$

Äquivalent aus dem Gammafaktor direkt:
$$
\boxed{
\Lambda_\infty(f)
= \frac{1}{\pi}\int_{\mathbb{R}} \hat{f}(t)\,
\operatorname{Re}\frac{\Gamma_{\mathbb{R}}'}{\Gamma_{\mathbb{R}}}\!\left(\tfrac{1}{2}+it\right)dt.}
$$

---

## 6. Die archimedische Distribution $W_\infty$

$$
\boxed{\langle W_\infty,f\rangle := \frac{1}{2\pi}\int_{\mathbb{R}}\hat{f}(t)\,A_\infty(t)\,dt,
\qquad \Lambda_\infty(f) = \langle W_\infty,f\rangle.}
$$

Formal: $W_\infty = \mathcal{F}^{-1}[A_\infty]$ in der oben festgelegten Konvention.

Aufspaltung:
$$
\boxed{W_\infty = W_\Gamma - (\log\pi)\delta_0,}
\qquad
\langle W_\Gamma,f\rangle = \frac{1}{2\pi}\int_{\mathbb{R}}\hat{f}(t)\operatorname{Re}\psi\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right)dt.
$$

Digammaasymptotik für große Argumente: $\psi(z)=\log z - \tfrac{1}{2z}+O(|z|^{-2})$, daher:
$$
\boxed{A_\infty(t) = \log\frac{|t|}{2\pi} + O(t^{-2}) \qquad (|t|\to\infty).}
$$

Der Multiplikator wächst nur logarithmisch $\Rightarrow$ temperierter Fouriermultiplikator:
$$
\boxed{W_\infty \in \mathcal{S}'(\mathbb{R}).}
$$

---

## 7. Saubere Trennung der vier Beiträge

### 7.1 Nullstellenterm
$$\boxed{\Lambda_{\mathrm{zero}}(f) = \sum_\rho \hat{f}\!\left(\frac{\rho-\tfrac12}{i}\right)}$$

### 7.2 Polterm
$$\boxed{\Lambda_{\mathrm{pole}}(f) = \hat{f}\!\left(\tfrac{i}{2}\right)+\hat{f}\!\left(-\tfrac{i}{2}\right)
= \int_{\mathbb{R}} f(u)\bigl(e^{u/2}+e^{-u/2}\bigr)\,du}$$

Diese Terme entsprechen den Punkten $s=1$ und $s=0$.

### 7.3 Archimedischer Term
$$\boxed{\Lambda_\infty(f) = -f(0)\log\pi + \frac{1}{2\pi}\int_{\mathbb{R}}\hat{f}(t)\operatorname{Re}\psi\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right)dt}$$

Der Anteil $-f(0)\log\pi$ gehört zum Faktor $\pi^{-s/2}$, also zum archimedischen Kanal.

### 7.4 Primzahlpotenzterm
$$\boxed{\Lambda_{\mathrm{prime}}(f) = \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt{n}}\bigl(f(\log n)+f(-\log n)\bigr)
= \sum_p\sum_{m\ge1}\frac{\log p}{p^{m/2}}\bigl(f(m\log p)+f(-m\log p)\bigr)}$$

**Vollständige explizite Formel:**
$$\boxed{\Lambda_{\mathrm{zero}} = \Lambda_{\mathrm{pole}} + \Lambda_\infty + \Lambda_{\mathrm{prime}}.}$$

---

## 8. Quellraum

### 8.1 Archimedischer Kanal allein
Da $A_\infty(t)$ nur logarithmisch wächst, ist $\Lambda_\infty: \mathcal{S}(\mathbb{R})\to\mathbb{C}$ stetig.

### 8.2 Vollständige explizite Formel
Für den Primterm ist $\mathcal{S}(\mathbb{R})$ nicht automatisch ausreichend. Der kanonische gemeinsame Kern ist:
$$\boxed{\mathcal{S}_W^{(0)} = C_c^\infty(\mathbb{R}).}$$

Für $f\in C_c^\infty(\mathbb{R})$ ist die Primpotenzsumme endlich (nur $|\log n|\le\sup|\operatorname{supp}f|$). Außerdem ist $\hat{f}$ ganz und fällt auf jedem Horizontalstreifen schneller als jede Potenz.

### 8.3 Zur Formulierung „minimaler Raum“
$$\boxed{C_c^\infty(\mathbb{R})\text{ ist ein kanonischer gemeinsamer Kern,}}$$
**nicht** der eindeutig kleinste mögliche Raum. Ein absolut kleinster Testfunktionsraum ist nicht kanonisch definiert.

$$\boxed{[O\text{-}220\text{-}1a\text{-source-core}]\quad\checkmark[M]}$$

---

## 9. Realitätssymmetrie

Wegen $\psi(\bar{z})=\overline{\psi(z)}$: $A_\infty(-t)=A_\infty(t)\in\mathbb{R}$.

Der Multiplikator ist **reell und gerade**. Damit:
$$\boxed{\Lambda_\infty(f^\sharp) = \overline{\Lambda_\infty(f)}.}$$

Für $Q_\infty(f,h)=\Lambda_\infty(h^\sharp*f)$:
$$\boxed{Q_\infty(f,h) = \frac{1}{2\pi}\int_{\mathbb{R}}\overline{\hat{h}(t)}\,\hat{f}(t)\,A_\infty(t)\,dt,}$$
$$\boxed{Q_\infty(f,h) = \overline{Q_\infty(h,f)}.}$$

Nebenresultat:
$$\boxed{[O\text{-}220\text{-}1b\text{-Herm}]\quad\checkmark[M]}$$

*(Betrifft ausschließlich Wohldefiniertheit, Stetigkeit und Hermiteschheit — noch nicht Positivität.)*

---

## 10. Korrektur der spektralen Formel in der Eröffnungsdatei

Die Eröffnungsdatei schreibt schematisch:
$$Q_\infty(f,h) = \int \hat{h}(t)\,\overline{\hat{f}(t)}\,w_\infty(t)\,dt.$$

Bei der gleichzeitig festgelegten Definition $Q_\infty(f,h)=\Lambda_\infty(h^\sharp*f)$ ist die korrekte Reihenfolge:
$$\boxed{Q_\infty(f,h) = \frac{1}{2\pi}\int_{\mathbb{R}}\overline{\hat{h}(t)}\,\hat{f}(t)\,A_\infty(t)\,dt.}$$

Die bisherige Formel entspricht der entgegengesetzten Linearitätskonvention.
$$\boxed{\warning[M]}$$

Die Korrektur ist rein konventionell, muss aber **vor dem Positivitätsaudit** in die Eröffnungsdatei eingetragen werden.

---

## 11. Eindeutigkeit

Sobald festgelegt sind: Fourierkonvention, $\Gamma_{\mathbb{R}}(s)=\pi^{-s/2}\Gamma(s/2)$, separate Behandlung von $s=0,1$, ist der Multiplikator
$$A_\infty(t) = \operatorname{Re}\psi\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right) - \log\pi$$
eindeutig bestimmt. Da $\mathcal{F}$ auf $\mathcal{S}'(\mathbb{R})$ injektiv ist:
$$\boxed{W_\infty\text{ ist eindeutig bestimmt.}}$$

Scheinbare Mehrdeutigkeit (ob $-(\log\pi)\delta_0$ separat notiert wird) ändert den kombinierten $W_\infty$ nicht.

$$\boxed{[O\text{-}220\text{-}1a\text{-uniqueness}]\quad\checkmark[M]}$$

---

## 12. Unabhängige Normalisierungstests

### Test A — exakter Paritätstest

Sei $f$ reell und ungerade. Dann $f(0)=0$, $f(\log n)+f(-\log n)=0$ und $A_\infty$ gerade $\Rightarrow$ $\Lambda_\infty(f)=0$. Die Nullstellen treten unter $\rho\leftrightarrow1-\rho$ paarweise auf. Beide Seiten der Formel liefern $0=0$.

Dieser Test kontrolliert gleichzeitig: Vorzeichen bei $\pm\log n$; die beiden Pole; Geradheit des Gamma-Multiplikators; Argumentierung $(\rho-\tfrac12)/i$.

### Test B — Gaußfunktion $h_{0.01}(t)=e^{-0.01t^2}$

$$
\sum_\rho h_{0.01}\!\left(\tfrac{\rho-\tfrac12}{i}\right) \approx 0.2993960225075591417465445405683
$$
$$
\text{Pol + }\pi\text{ + Gamma + Prim} \approx 0.2993960225075591417465445405713
$$
$$
\text{Differenz} \approx -2.93\times10^{-30}.
$$

### Test C — Gaußfunktion $h_{0.02}(t)=e^{-0.02t^2}$

$$
\sum_\rho h_{0.02}\!\left(\tfrac{\rho-\tfrac12}{i}\right) \approx 0.03708258346263896139322932493505409735
$$
$$
\text{Rechte Seite} \approx 0.03708258346263896139322932493505409735
$$
$$
\text{Differenz} < 10^{-40}.
$$

Die Gaußtests reagieren empfindlich auf falsche $2\pi$-Faktoren, falsches Digammaargument oder falsche Zuordnung von $-\log\pi$. Die Übereinstimmung bestätigt die Normalisierung.

---

## 13. Antworten auf die sieben Leitfragen

| # | Frage | Antwort |
|---|---|---|
| 1 | Referenzversion | Guinand–Weil mit $\hat{h}_{!2\pi}$, exakt auf Projektkonvention konvertiert |
| 2 | Fourierkonvention | $\hat{f}(t)=\int f(u)e^{-itu}du$, $f(u)=\tfrac{1}{2\pi}\int\hat{f}(t)e^{itu}dt$ |
| 3 | Archimedischer Term | $\Lambda_\infty(f)=-f(0)\log\pi+\tfrac{1}{2\pi}\int\hat{f}(t)\operatorname{Re}\psi(\tfrac14+\tfrac{it}{2})dt$ |
| 4 | Polterm-Trennung | $\hat{f}(\pm i/2)$ = Polterm; $-f(0)\log\pi$ = archimedisch (Faktor $\pi^{-s/2}$) |
| 5 | Minimaler Kern | $C_c^\infty(\mathbb{R})$ ist kanonischer Kern; für $\Lambda_\infty$ allein ist $\mathcal{S}(\mathbb{R})$ ausreichend |
| 6 | Realitätssymmetrie | $A_\infty(-t)=A_\infty(t)\in\mathbb{R}$, äquivalent zu $\Lambda_\infty(f^\sharp)=\overline{\Lambda_\infty(f)}$ |
| 7 | Eindeutigkeit | Ja — nach Fixierung von Konvention, $\Gamma_{\mathbb{R}}$ und Polterm ist $W_\infty\in\mathcal{S}'(\mathbb{R})$ eindeutig |

---

## 14. Revidierte Knotenstatustabelle

| Knoten / Gegenstand | Status | Befund |
|---|---|---|
| $[O\text{-}220\text{-}1a]$ | $\checkmark[M]$ | Exakte Normalisierung abgeschlossen |
| Fourierkonvention | $\checkmark[M]$ | Alle $2\pi$-Faktoren fixiert |
| $\Lambda_\infty$ | $\checkmark[M]$ | Vollständig normalisiert |
| $W_\infty$ | $\checkmark[M]$ | Eindeutige temperierte Distribution |
| Pol-/Gamma-Trennung | $\checkmark[M]$ | $-f(0)\log\pi$ ist archimedisch |
| Gemeinsamer Kern $C_c^\infty$ | $\checkmark[M]$ | Vollständige Formel wohldefiniert |
| „Minimalster Raum“ | $\warning[M]$ | Kein kanonischer Minimalitätsbegriff |
| Realitätssymmetrie | $\checkmark[M]$ | Multiplikator reell und gerade |
| $[O\text{-}220\text{-}1b\text{-Herm}]$ | $\checkmark[M]$ | Als Nebenresultat geschlossen |
| Positivität | $?[O]$ | Noch keinerlei positive Aussage |
| Spektrales Vorzeichen | $?[O]$ | Nächster Auditgegenstand |

---

## 15. Verbindlicher Repository-Korrekturblock für die Eröffnungsdatei

```
AUDITKORREKTUR [O-220-1a]

Fourierkonvention:
  fhat(t) = integral_R f(u)e^{-itu}du
  f(u) = (1/2pi) integral_R fhat(t)e^{itu}dt

Archimedischer Multiplikator:
  A_infty(t) = Re psi(1/4 + it/2) - log pi

Archimedisches Funktional:
  Lambda_infty(f) = (1/2pi) integral_R fhat(t) A_infty(t) dt
                 = -f(0)log pi
                   + (1/2pi) integral_R fhat(t) Re psi(1/4+it/2) dt

Archimedische Distribution:
  <W_infty,f> = Lambda_infty(f)
  W_infty = F^{-1}(A_infty)

Polterm:
  Lambda_pole(f) = fhat(i/2) + fhat(-i/2)

Primzahlpotenzterm:
  Lambda_prime(f) = sum_{n>=2} Lambda(n)/sqrt(n) [f(log n)+f(-log n)]

Vollständige explizite Formel:
  sum_rho fhat((rho-1/2)/i)
  = Lambda_pole(f) + Lambda_infty(f) + Lambda_prime(f)

Gemeinsamer Testfunktionskern:
  S_W^(0) = C_c^infty(R)

Korrektur der sesquilinearen Spektralform:
  Q_infty(f,h) = (1/2pi) integral_R conj(hhat(t)) fhat(t) A_infty(t) dt
  (nicht: hhat(t) conj(fhat(t)) ...)

Status:
  [O-220-1a]          checkmark[M]
  [O-220-1b-Herm]     checkmark[M]
  [O-220-1a-source-core]   checkmark[M]
  [O-220-1a-uniqueness]    checkmark[M]

Hinweis:
  C_c^infty(R) ist ein kanonischer gemeinsamer Kern,
  nicht der eindeutig kleinste mögliche Testfunktionsraum.
```

---

## 16. Nächster Auditknoten

$$\boxed{[O\text{-}220\text{-}1c]\quad\text{Positivitätsklassifikation des archimedischen Multiplikators}.}$$

Exakter Gegenstand:
$$\boxed{A_\infty(t) = \operatorname{Re}\psi\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right) - \log\pi.}$$

Zu prüfen:
- Reelle Nullstellen von $A_\infty(t)$;
- Intervalle mit $A_\infty(t)<0$ (Vorzeichen);
- Ob der negative Spektralbereich kompakt ist;
- Endlicher oder unendlicher negativer Index der Form;
- Ob der Polterm den negativen Anteil durch einen endlichdimensionalen Defekt kompensieren kann.

$$\boxed{W_\infty\text{ und }\Lambda_\infty\text{ sind exakt und eindeutig fixiert.}}$$

Die Normalisierungs-Firewall ist damit erfolgreich passiert.
