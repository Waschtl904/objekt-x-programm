# NEU-220c — Direktaudit $[O\text{-}220\text{-}1c]$: Positivitätsklassifikation des archimedischen Multiplikators

**Stand:** 2026-08-05  
**Repository:** Waschtl904/objekt-x-programm  
**Typ:** Geschlossener Auditknoten (negativ entschieden)  
**Vorgänger:** NEU-220a (Commit 8a92f5a)

**Geprüfter Ausgangsstand:**
$$
A_\infty(t) = \operatorname{Re}\psi\!\left(\tfrac14+\tfrac{it}{2}\right) - \log\pi,
\qquad
Q_\infty(f,h) = \frac{1}{2\pi}\int_{\mathbb{R}}\overline{\hat h(t)}\,\hat f(t)\,A_\infty(t)\,dt.
$$

---

## 1. Gesamturteil

$$\boxed{[O\text{-}220\text{-}1c]\quad\checkmark[M]_{\mathrm{neg}}}$$

Die Positivitätsklassifikation fällt eindeutig in **Fall D**:
$$\boxed{Q_\infty\text{ besitzt unendlichen negativen Index.}}$$

Kernbefunde:
- $A_\infty$ ist reell, gerade und auf $(0,\infty)$ streng wachsend.
- $A_\infty$ besitzt genau zwei reelle Nullstellen $\pm t_\infty$, numerisch $t_\infty = 6.2898359888369027796650901008\ldots$
- $A_\infty(t)<0 \iff |t|<t_\infty$; der negative Bereich ist beschränkt, aber besitzt positives Maß.
- Der negative Index ist auf $\mathcal{S}(\mathbb{R})$ und $C_c^\infty(\mathbb{R})$ **unendlich**.
- Der Polterm hat Rang $\le 2$ und kann den unendlichen negativen Index nicht beseitigen — dies gilt für **jede** endlich-rangige Korrektur $R$.

Damit existiert **keine** Darstellung $Q_\infty(f,h)=\langle T_\infty f,T_\infty h\rangle_{H_\infty} - R_\infty(f,h)$ mit positivem Hilbertraumterm und endlichdimensionalem Defekt $R_\infty$.

---

## 2. Reihenformel für den Multiplikator

Digamma-Partialbruchentwicklung (DLMF 5.7.6), mit $a=\tfrac14$, $y=\tfrac t2$:
$$
\boxed{A_\infty(t) = -\gamma-\log\pi + \sum_{k=0}^{\infty}\left[\frac{1}{k+1} - \frac{k+\tfrac14}{(k+\tfrac14)^2+\tfrac{t^2}{4}}\right].}
$$
Lokal gleichmäßig konvergent in $t$; direkt geeignet für Vorzeichen- und Monotonieaudit.

---

## 3. Geradheit und strenge Monotonie

Aus der Reihenform: $A_\infty(-t)=A_\infty(t)$ (gerade).

Gliedweise Differentiation für $t>0$:
$$
\boxed{A_\infty'(t) = \frac{t}{2}\sum_{k=0}^{\infty}\frac{k+\tfrac14}{\left[(k+\tfrac14)^2+\tfrac{t^2}{4}\right]^2} > 0 \qquad (t>0).}
$$

$A_\infty$ ist auf $(0,\infty)$ streng wachsend — höchstens eine Nullstelle auf der positiven Halbachse.

$$\boxed{[O\text{-}220\text{-}1c\text{-monotonicity}]\quad\checkmark[M]}$$

---

## 4. Wert im Ursprung

Rationaler Digammawert: $\psi(\tfrac14) = -\gamma-\tfrac{\pi}{2}-3\log 2$ (DLMF 5.4.E9). Daher:
$$
\boxed{A_\infty(0) = -\gamma-\tfrac{\pi}{2}-3\log2-\log\pi \approx -5.3721834192256655822329574974\ldots < 0.}
$$

$A_\infty$ ist in einer ganzen Umgebung des Ursprungs strikt negativ.

---

## 5. Verhalten für große Frequenzen

Digamma-Asymptotik (DLMF 5.11): $\psi(z)\sim\log z - \tfrac{1}{2z} - \sum_{k\ge1}\tfrac{B_{2k}}{2kz^{2k}}$, mit $z=\tfrac14+\tfrac{it}{2}$:
$$
\boxed{A_\infty(t) = \log\frac{|t|}{2\pi} + O(t^{-2}) \qquad (|t|\to\infty), \qquad A_\infty(t)\to+\infty.}
$$

Mit $A_\infty(0)<0$ und strenger Monotonie auf $(0,\infty)$: genau eine positive Nullstelle.

---

## 6. Die reellen Nullstellen

$$\boxed{\{-t_\infty,t_\infty\}, \qquad t_\infty = 6.2898359888369027796650901008218533966583\ldots}$$

Vorzeichenklammer: $A_\infty(6.289835988)\approx-1.3334\times10^{-10}$, $A_\infty(6.289835989)\approx2.5985\times10^{-11}$.

$$
\boxed{A_\infty(t)\begin{cases}<0,&|t|<t_\infty\\=0,&|t|=t_\infty\\>0,&|t|>t_\infty\end{cases}}
$$

$$\boxed{[O\text{-}220\text{-}1c\text{-zeros/sign}]\quad\checkmark[M]}$$

---

## 7. Kompaktheit des negativen Spektralbereichs

$$\mathcal{N}_{\mathrm{spec}} = (-t_\infty,t_\infty), \qquad \overline{\mathcal{N}_{\mathrm{spec}}}=[-t_\infty,t_\infty]\text{ kompakt.}$$

**Wichtig:** Kompaktheit des Frequenzbereichs $\neq$ Endlichdimensionalität des negativen Index. Ein Frequenzintervall positiven Maßes trägt einen unendlichdimensionalen $L^2$-Raum.

---

## 8–9. Unendlicher negativer Index auf $\mathcal{S}(\mathbb{R})$ und $C_c^\infty(\mathbb{R})$

Für jedes kompakte $J\Subset(-t_\infty,t_\infty)$ existiert $c_J>0$ mit $A_\infty\le-c_J$ auf $J$. Für beliebig viele linear unabhängige $\varphi_1,\ldots,\varphi_N\in C_c^\infty(J)$ mit $f_j=\mathcal{F}^{-1}\varphi_j\in\mathcal{S}(\mathbb{R})$ gilt für jede nichttriviale Linearkombination $f=\sum\alpha_jf_j$: $Q_\infty(f,f)\le-\tfrac{c_J}{2\pi}\int_J|\hat f|^2<0$.

$$\boxed{\operatorname{ind}_-(Q_\infty|_{\mathcal S}) = \infty.}$$

Durch Abschneiden $f_{j,R}=\chi_Rf_j\to f_j$ in der Schwartz-Topologie und Stetigkeit von $Q_\infty$ konvergieren die Gram-Matrizen; für großes $R$ bleibt die Matrix strikt negativ definit.

$$\boxed{\operatorname{ind}_-(Q_\infty|_{C_c^\infty}) = \infty.}$$

$$\boxed{[O\text{-}220\text{-}1c\text{-negative-index}]\quad\checkmark[M]_{\mathrm{neg}}}$$

---

## 10. Auch der positive Index ist unendlich

Analog auf $J_+\Subset(t_\infty,\infty)$: $\operatorname{ind}_+(Q_\infty)=\infty$.

$$\boxed{(\operatorname{ind}_+,\operatorname{ind}_-) = (\infty,\infty).}$$

---

## 11. Kanonische spektrale Jordanzerlegung

Mit $A_{\infty,+}=\max\{A_\infty,0\}$, $A_{\infty,-}=\max\{-A_\infty,0\}$:
$$
\boxed{Q_\infty(f,h) = \langle T_{\infty,+}f,T_{\infty,+}h\rangle_{H_{\infty,+}} - \langle T_{\infty,-}f,T_{\infty,-}h\rangle_{H_{\infty,-}},}
$$
mit $H_{\infty,\pm} = L^2(\{|t|\gtrless t_\infty\}, \tfrac{|A_\infty(t)|}{2\pi}dt)$, $T_{\infty,\pm}f = \mathbf{1}_{\{|t|\gtrless t_\infty\}}\hat f(t)$. Beide Räume unendlichdimensional.

Echte Hilbert-Differenz- bzw. Kre\u012bnraumzerlegung, **keine** positive Gram-Realisierung.

$$\boxed{[O\text{-}220\text{-}1d\text{-sign/Jordan}]\quad\checkmark[M]}$$

---

## 12. Der Polterm als sesquilineare Form

$$
Q_{\mathrm{pole}}(f,h) = \overline{\hat h(-i/2)}\,\hat f(i/2) + \overline{\hat h(i/2)}\,\hat f(-i/2).
$$

Mit $E(f)=(\hat f(i/2),\hat f(-i/2))\in\mathbb{C}^2$: $Q_{\mathrm{pole}}$ hängt nur von $E(f), E(h)$ ab.

$$\boxed{\operatorname{rank}Q_{\mathrm{pole}}\le2, \qquad Q_{\mathrm{pole}}(f,f)=2\operatorname{Re}(\overline{\hat f(-i/2)}\hat f(i/2)).}$$

---

## 13–14. Warum der Polterm (und jede endlichrangige Korrektur) den negativen Index nicht beseitigt

Für negativ definites $V\subset C_c^\infty$, $\dim V=N+2$: $\dim\ker(E|_V)\ge N$. Auf diesem Kern verschwindet $Q_{\mathrm{pole}}$, also $(Q_\infty+Q_{\mathrm{pole}})(f,f)=Q_\infty(f,f)<0$.

$$\boxed{\operatorname{ind}_-(Q_\infty+Q_{\mathrm{pole}}) = \infty.}$$

**Verallgemeinerung:** Für jede hermitesche Form $R$ mit $\operatorname{rank}R=r<\infty$: negativ definiter Unterraum der Dimension $N+r$ wählen, Kern der Faktorisierungsdaten hat Dimension $\ge N$, $R$ verschwindet dort.

$$\boxed{\operatorname{ind}_-(Q_\infty+R) = \infty \text{ für jede endlich-rangige Form } R.}$$

$$\boxed{[O\text{-}220\text{-}1c\text{-pole-compensation}]\quad\checkmark[M]_{\mathrm{neg}}}$$

**Ausschluss der Fälle A, B, C:**

| Fall | Status |
|---|---|
| A: $Q_\infty\ge0$ | $\checkmark[M]_{\mathrm{neg}}$ |
| B: endlicher negativer Defekt | $\checkmark[M]_{\mathrm{neg}}$ |
| C: $Q_\infty+Q_{\mathrm{pole}}$ positiv/endl.-defekt | $\checkmark[M]_{\mathrm{neg}}$ |
| D: unendlicher negativer Index | $\checkmark[M]$ |

---

## 15. Strategische Bedeutung für Objekt X

$$\boxed{\text{Der isolierte archimedische Term kann kein positiver lokaler Gramkanal mit endlichdimensionalem Defekt sein.}}$$

Gilt auch nach Hinzunahme des Polterms. Eine termweise positive Zerlegung $Q_W = Q_{\infty,\mathrm{positive}} + \sum_p Q_{p,\mathrm{positive}} - R_{\mathrm{finite}}$ ist mit dem exakt normalisierten $Q_\infty$ **nicht möglich**.

**Nicht ausgeschlossen:** globale Kopplung $B_{\infty p}\neq0$; nichtdiagonale Gluung; unendlichdimensionaler negativer Begleitkanal (Kre\u012bnraum, erfüllt aber nicht das positive Hilbertraumziel); andere kanonisch begründete Zerlegung.

$$\boxed{\text{Der strategische Hauptpfad verschiebt sich von isolierter positiver archimedischer Kanal zu global gekoppelter Positivität von Archimedes- und Primkanälen.}}$$

---

## 16. Revidierte Knotenstatustabelle

| Knoten | Status | Befund |
|---|---|---|
| $[O\text{-}220\text{-}1c]$ | $\checkmark[M]_{\mathrm{neg}}$ | Fall D: unendlicher negativer Index |
| Geradheit | $\checkmark[M]$ | $A_\infty(-t)=A_\infty(t)$ |
| Monotonie $t>0$ | $\checkmark[M]$ | $A_\infty'(t)>0$ |
| Nullstellen | $\checkmark[M]$ | $\pm t_\infty$ |
| numerischer Wert | $\checkmark[M]$ | $t_\infty=6.2898359888369\ldots$ |
| negativer Bereich | $\checkmark[M]$ | $(-t_\infty,t_\infty)$ |
| Kompaktheit des Abschlusses | $\checkmark[M]$ | $[-t_\infty,t_\infty]$ kompakt |
| negativer Index auf $\mathcal{S}$ | $\checkmark[M]_{\mathrm{neg}}$ | unendlich |
| negativer Index auf $C_c^\infty$ | $\checkmark[M]_{\mathrm{neg}}$ | unendlich |
| positiver Index | $\checkmark[M]$ | ebenfalls unendlich |
| finite Defektkorrektur | $\checkmark[M]_{\mathrm{neg}}$ | unmöglich |
| Poltermkorrektur | $\checkmark[M]_{\mathrm{neg}}$ | Rang $\le2$, unzureichend |
| $[O\text{-}220\text{-}1d\text{-sign/Jordan}]$ | $\checkmark[M]$ | kanonische Krein-Zerlegung |
| positive lokale Hilbertraumrealisierung | $\checkmark[M]_{\mathrm{neg}}$ | ausgeschlossen |
| global gekoppelte Positivität | $?[O]$ | **neuer kritischer Pfad** |

---

## 17. Quellenfehler in NEU-220a (Nachtrag)

NEU-220a enthält eine interne Vorzeicheninkonsistenz zwischen der Definition
$$\Lambda_{\mathrm{prime}}(f) := \sum_{n\ge2}\tfrac{\Lambda(n)}{\sqrt n}(f(\log n)+f(-\log n))$$
und der zugleich verwendeten Formel $\Lambda_{\mathrm{zero}}=\Lambda_{\mathrm{pole}}+\Lambda_\infty-\sum_{n\ge2}\cdots$. Es ist genau eine Konvention zu wählen.

**Empfohlene Konvention:**
$$\boxed{\Lambda_{\mathrm{prime}}(f) := \sum_{n\ge2}\tfrac{\Lambda(n)}{\sqrt n}(f(\log n)+f(-\log n)), \qquad \Lambda_{\mathrm{zero}}=\Lambda_{\mathrm{pole}}+\Lambda_\infty+\Lambda_{\mathrm{prime}}.}$$

Der Wert von $\sum_{n\ge2}\cdots$ kann separat als $P_{\mathrm{prime}}(f)$ notiert werden; dann $\Lambda_{\mathrm{zero}}=\Lambda_{\mathrm{pole}}+\Lambda_\infty-P_{\mathrm{prime}}$.

$$\boxed{\text{Vorzeichen der Definition von }\Lambda_{\mathrm{prime}}\quad\times[M].}$$

Die Normalisierung von $A_\infty$, $W_\infty$, $\Lambda_\infty$ bleibt unberührt: $[O\text{-}220\text{-}1a]\ \checkmark[M]$.

---

## 18. Korrigierter DAG

```
[O-220-1a] exakte Normalisierung                     ✓[M]
      |
      +--> [O-220-1b-Herm] Hermiteschheit            ✓[M]
      |
      v
[O-220-1c] Positivitätsklassifikation                ✓[M]_neg
      |
      +--> A_infty gerade, streng wachsend t>0        ✓[M]
      +--> Nullstellen +-6.2898359888...              ✓[M]
      +--> negativer Bereich kompakt eingeschlossen   ✓[M]
      +--> negativer Index unendlich                  ✓[M]_neg
      +--> positiver Index unendlich                  ✓[M]
      +--> Polterm Rang <=2                           ✓[M]
      +--> Polterm kompensiert Negativität nicht      ✓[M]_neg
      +--> finite Defektkorrektur unmöglich           ✓[M]_neg
      |
      v
[O-220-1d-sign/Jordan] kanonische Krein-/Jordanzerlegung   ✓[M]
      |
      +--> positive lokale Hilbertraumarchitektur     ✓[M]_neg
      |
      v
[O-220-1f0] globale Archimedes-Prim-Kopplung B_{infty,pr}   ?[O]  <-- NEUER AKTIVER KNOTEN
      |
      +--> [O-220-1f] globale Gluung (nachgeordnet)   ?[O]
      +--> [O-220-1e] HH-Brücke (nachgeordnet)        ?[O]
```

---

## 19. Neuer Knoten: $[O\text{-}220\text{-}1f_0]$

$$\boxed{[O\text{-}220\text{-}1f_0]\quad\text{Kann der unendlichdimensionale negative archimedische Sektor durch echte globale Primkopplungen kompensiert werden?}}$$

Zu prüfen ist eine globale Blockform, keine direkte orthogonale Summe rein positiver lokaler Kanäle:
$$
\mathcal{Q}_X = \begin{pmatrix}A_\infty & B_{\infty,\mathrm{pr}} \\ B_{\infty,\mathrm{pr}}^* & A_{\mathrm{pr}}\end{pmatrix}.
$$

Zentrale Frage nicht mehr $A_\infty\ge0$ (negativ beantwortet), sondern:
$$\boxed{\mathcal{Q}_X\ge0 \quad\text{trotz}\quad A_\infty\text{ indefinit}?}$$

Schur-Komplement-Ansatz zu untersuchen: ob formal $A_\infty - B_{\infty,\mathrm{pr}}A_{\mathrm{pr}}^{-1}B_{\infty,\mathrm{pr}}^*\ge0$ (oder korrekt orientierte Variante) möglich ist — die endgültige Blockkonvention entscheidet die Richtung.

$$\boxed{\text{Kernaussage: Positivität kann nicht termweise lokal entstehen. Falls Objekt X existiert, muss die archimedische Negativität global gekoppelt, nichtdiagonal oder durch eine fundamental andere kanonische Zerlegung aufgehoben werden.}}$$

**Priorisierung für Folgeschritte (abhängigkeitsgesteuert, nicht linear NEU-220–250):**
1. Abgussmatrix (übergeordnetes Steckbrief-Dokument, alle Bedingungen S1–S11, HP-1–HP-7, $A_\infty$-Befund zusammenführen).
2. Numerischer Kopplungspilot: endliche Primblockmodelle $\mathcal{Q}_{S,N}$ testen, ob $B_{\infty,S,N}$ negative Eigenrichtungen von $A_{\infty,N}$ anheben kann.
3. NEU-57/NEU-223-Frage neu stellen: welcher Vergleichsoperator passt zur global gekoppelten Form (nicht mehr zum isolierten lokalen Kanal).
4. $[O\text{-}220\text{-}1f_0]$ als aktiver Knoten bearbeiten; $[O\text{-}220\text{-}1e]$ und der Rest von $[O\text{-}220\text{-}1f]$ bleiben nachgeordnet.
