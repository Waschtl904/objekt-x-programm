# NEU-252 — M3: Hermitesche Polarisation der vollständigen Weil-Form

**Katalog-ID:** NEU-252  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07 (Patch: 2026-08-07)  
**Auftrag:** M3 — Komponentenweiser Nachweis: Pol-, Gamma- und Primzahlpotenzblock respektieren alle dieselbe $g_{a,b}$-Polarisation; vollständige hermitesche sesquilineare Weil-Form $B_W(a,b)$; adelischer Transport via $R_{\rm PW}$; Positivitäts-Firewall.  
**Patch:** §1.3 Typkorrektur: $h_{a,b}\in\mathcal{A}_{\rm PW}$ zurückgezogen; $\mathcal{H}_{\rm PW}^{\mathbb{C}}$ eingeführt; Gamma-Block über $h_{a,b}|_{\mathbb{R}}\in\mathcal{S}(\mathbb{R})$ formuliert.  
**Gesamtausgang:** M3 $\checkmark[K/M]$. $\mathcal{S}_{\rm adel}^{\rm amp}\to(\mathcal{A}_{\rm PW},B_W)$ vollständig hermitesch, RH-frei.  
**Vorgänger:** NEU-220l (PD5a2a–f), NEU-220k (Masterform), NEU-220b/c (Gamma-Block), NEU-250m (M2-Patch), NEU-250r (Amplitudenport)

---

## 0. Ausgangslage und Auftrag

NEU-220l (PD5a2f) stellt fest: Die hermitesche sesquilineare Form $(a,b)\mapsto\mathfrak{W}(a,b)$ ist **bedingungslos** durch Polarisation verfügbar. M3 führt den stärkeren **komponentenweisen** Nachweis: Jeder der drei Blöcke der Masterform aus NEU-220k/l — Polterm, Gamma-Block, Primzahlpotenzterm — ist für sich sesquilinear und hermitesch unter derselben Polarisation $g_{a,b}$.

$$
\boxed{\text{M3 konstruiert nicht die Polarisation erstmals. M3 beweist die komponentenweise Konsistenz.}} \qquad (0\text{-Scope})
$$

---

## 1. Amplitudenraum, Polarisation und Typenräume

### 1.1 Amplitudenraum

$$
\boxed{\mathcal{A}_{\rm PW}:=C_c^\infty(\mathbb{R};\mathbb{C}).} \qquad (1\text{-APW})
$$

### 1.2 Polarisierte Kreuzkorrelation und Evenisierung

Für $a,b\in\mathcal{A}_{\rm PW}$ setze
$$
C_{a,b}(t):=\langle a,U_tb\rangle=\int_{\mathbb{R}}a(v)\overline{b(v-t)}\,dv \qquad (1\text{-Cab})
$$
und
$$
\boxed{g_{a,b}(t):=\frac{1}{2}\bigl(C_{a,b}(t)+C_{a,b}(-t)\bigr)\in\mathcal{G}_{\rm ev}^{\mathbb{C}}:=C_c^\infty(\mathbb{R};\mathbb{C})_{\rm even}.} \qquad (1\text{-gab})
$$

**Drei Grundeigenschaften:**

$$
g_{a,b}\in\mathcal{G}_{\rm ev}^{\mathbb{C}}\quad\checkmark \qquad (1\text{-i})
$$

*Beweis:* Geradheit: $g_{a,b}(-t)=g_{a,b}(t)$. Träger: $\operatorname{supp}(C_{a,b})\subset\operatorname{supp}(a)-\operatorname{supp}(b)$ kompakt, also $g_{a,b}\in C_c^\infty$.

$$
g_{b,a}(t)=\overline{g_{a,b}(t)}\quad\checkmark \qquad (1\text{-ii})
$$

*Beweis:* $C_{b,a}(t)=\overline{C_{a,b}(-t)}$, also $g_{b,a}(t)=\tfrac{1}{2}(\overline{C_{a,b}(-t)}+\overline{C_{a,b}(t)})=\overline{g_{a,b}(t)}$.

$$
g_{a,a}(t)=\operatorname{Re}\langle a,U_ta\rangle=g_a(t)\in C_c^\infty(\mathbb{R};\mathbb{R})_{\rm even}\quad\checkmark \qquad (1\text{-iii})
$$

### 1.3 Drei Typenräume und der komplexe Paley-Wiener-Kern

$$
\boxed{\begin{aligned}
&a,b\in\mathcal{A}_{\rm PW}=C_c^\infty(\mathbb{R};\mathbb{C}),\\
&g_{a,b}\in\mathcal{G}_{\rm ev}^{\mathbb{C}}=C_c^\infty(\mathbb{R};\mathbb{C})_{\rm even},\\
&h_{a,b}\in\mathcal{H}_{\rm PW}^{\mathbb{C}}\quad(\text{ganze Paley-Wiener-Funktion}).
\end{aligned}} \qquad (1\text{-Types})
$$

**Typkorrektur** ($\times[M]$ erste Fassung, dort stand $h_{a,b}\in\mathcal{A}_{\rm PW}$):

$$
\boxed{h_{a,b}\in\mathcal{A}_{\rm PW}\quad\times[M].} \qquad (1\text{-TypeErr})
$$

Das Fourier-Bild einer $C_c^\infty(\mathbb{R})$-Funktion ist **nicht** wieder kompakt getragen, sondern eine ganze Paley-Wiener-Funktion (Paley-Wiener-Satz). Auf der reellen Achse liegt es in $\mathcal{S}(\mathbb{R})$.

**Korrekte Definition:** Für $g_{a,b}\in\mathcal{G}_{\rm ev}^{\mathbb{C}}$ setze
$$
\boxed{h_{a,b}(z):=\int_{\mathbb{R}}g_{a,b}(u)e^{izu}\,du\in\mathcal{H}_{\rm PW}^{\mathbb{C}}.} \qquad (1\text{-hab})
$$

Eigenschaften von $h_{a,b}$:
- **Ganz:** $h_{a,b}$ ist eine ganze Funktion auf $\mathbb{C}$ (exponentieller Typ).
- **Gerade:** $g_{a,b}(-u)=g_{a,b}(u)$ $\Rightarrow$ $h_{a,b}(-z)=h_{a,b}(z)$.
- **Schwartz auf der reellen Achse:** $h_{a,b}|_{\mathbb{R}}\in\mathcal{S}(\mathbb{R})$.

$$
\boxed{h_{a,b}|_{\mathbb{R}}\in\mathcal{S}(\mathbb{R}),\quad h_{a,b}\text{ ganz und gerade.}\quad\checkmark[K/M]} \qquad (1\text{-PW})
$$

**Weil-Kern:** Setze
$$
\boxed{F_{a,b}(s):=h_{a,b}\!\left(\frac{s-\tfrac{1}{2}}{i}\right)\in\mathcal{W}_{\mathbb{C}}.} \qquad (1\text{-Fab})
$$

**Weil-Symmetrie:** $h_{a,b}(-z)=h_{a,b}(z)$ $\Rightarrow$ $F_{a,b}(1-s)=F_{a,b}(s)$. $\checkmark$ NEU-220k unmittelbar anwendbar.

---

## 2. Komponentenweise Polarisation: Polterm

$$
\boxed{B_{\rm pole}(a,b):=h_{a,b}(i/2)+h_{a,b}(-i/2)=2h_{a,b}(i/2).} \qquad (2\text{-Bpole})
$$

(Letztes Gleichzeichen wegen Geradheit.)

**Sesquilinearität in $a$:** $g_{a,b}$ linear in $a$ $\Rightarrow$ $h_{a,b}$ linear in $a$ $\Rightarrow$ $B_{\rm pole}$ linear in $a$. $\checkmark$

**Hermitizität:** $h_{b,a}=\widehat{g_{b,a}}=\widehat{\overline{g_{a,b}}}$; auf der imaginären Achse: $h_{b,a}(i/2)=\overline{h_{a,b}(i/2)}$, also $B_{\rm pole}(b,a)=\overline{B_{\rm pole}(a,b)}$. $\checkmark$

**Diagonale:** $B_{\rm pole}(a,a)=h_a(i/2)+h_a(-i/2)$ nach NEU-220l. $\checkmark$

$$
\boxed{B_{\rm pole}(a,b)\text{ sesquilinear, hermitesch.}\quad\checkmark[K/M]} \qquad (2\text{-status})
$$

---

## 3. Komponentenweise Polarisation: Gamma-Block

$$
\boxed{B_\Gamma(a,b):=2\Lambda_\Gamma(h_{a,b}).} \qquad (3\text{-BGamma})
$$

Normierung $\Lambda_\Gamma$ aus NEU-220k (keine ältere offene PD-3d-Normierung).

**Wohldefiniertheit:** NEU-220b zeigt: $T_\Gamma^{\rm raw}$ auf $\mathcal{S}(\mathbb{R})$ wohldefiniert und involutionsverträglich. Da $h_{a,b}|_{\mathbb{R}}\in\mathcal{S}(\mathbb{R})$ (nicht $\mathcal{A}_{\rm PW}$ — Typkorrektur aus §1.3), ist $\Lambda_\Gamma(h_{a,b})$ wohldefiniert. $\checkmark$

**Sesquilinearität:** $h_{a,b}$ linear in $a$; $\Lambda_\Gamma$ linear; $B_\Gamma$ linear in $a$. $\checkmark$

**Hermitizität:** $h_{b,a}|_{\mathbb{R}}=\overline{h_{a,b}|_{\mathbb{R}}}$; $\Lambda_\Gamma$ reell auf reell-geraden Schwartzfunktionen (NEU-220b/c); also $B_\Gamma(b,a)=\overline{B_\Gamma(a,b)}$. $\checkmark$

**Diagonale:** $B_\Gamma(a,a)=2\Lambda_\Gamma(h_a)$. $\checkmark$

$$
\boxed{B_\Gamma(a,b)\text{ sesquilinear, hermitesch; }\Lambda_\Gamma\text{ auf }h_{a,b}|_{\mathbb{R}}\in\mathcal{S}(\mathbb{R}).}\quad\checkmark[K/M] \qquad (3\text{-status})
$$

---

## 4. Komponentenweise Polarisation: Primzahlpotenzterm

$$
\boxed{B_{\rm fin}(a,b):=-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt{n}}\,g_{a,b}(\log n).} \qquad (4\text{-Bfin})
$$

**Konvergenz (endlich):** Kompakter Träger von $g_{a,b}\in\mathcal{G}_{\rm ev}^{\mathbb{C}}$ $\Rightarrow$ $g_{a,b}(\log n)=0$ für $n>e^{2R}$ $\Rightarrow$ Summe endlich. Die Endlichkeit hängt an der Kompaktheit von $g_{a,b}$, **nicht** von $h_{a,b}$. $\checkmark$

**Sesquilinearität:** $g_{a,b}$ linear in $a$; endliche Summe; $B_{\rm fin}$ linear in $a$. $\checkmark$

**Hermitizität:** $g_{b,a}=\overline{g_{a,b}}$ $\Rightarrow$ $B_{\rm fin}(b,a)=\overline{B_{\rm fin}(a,b)}$. $\checkmark$

**Diagonale:** $B_{\rm fin}(a,a)=-2\sum_n\frac{\Lambda(n)}{\sqrt{n}}g_a(\log n)$. $\checkmark$

$$
\boxed{B_{\rm fin}(a,b)\text{ sesquilinear, hermitesch, endlich auf }\mathcal{A}_{\rm PW}.}\quad\checkmark[K/M] \qquad (4\text{-status})
$$

---

## 5. Vollständige hermitesche Weil-Form

$$
\boxed{B_W(a,b):=B_{\rm pole}(a,b)+B_\Gamma(a,b)+B_{\rm fin}(a,b).} \qquad (5\text{-BW})
$$

$$
\boxed{B_W:\mathcal{A}_{\rm PW}\times\mathcal{A}_{\rm PW}\to\mathbb{C}\quad\text{sesquilinear und hermitesch.}\quad\checkmark[K/M]} \qquad (5\text{-Main})
$$

$$
\boxed{B_W(a,a)=\mathfrak{W}(a).\quad\checkmark[K/M]} \qquad (5\text{-Diag})
$$

*Beweis:* $B_{\rm pole}(a,a)+B_\Gamma(a,a)+B_{\rm fin}(a,a)=h_a(i/2)+h_a(-i/2)+2\Lambda_\Gamma(h_a)-2\sum_n\frac{\Lambda(n)}{\sqrt{n}}g_a(\log n)=\mathfrak{W}(a)$ nach NEU-220l PD5a2d. $\square$

---

## 6. Adelischer Transport

$$
\boxed{B_W^{\rm adel}(F,G):=B_W(R_{\rm PW}F,\,R_{\rm PW}G),\qquad F,G\in\mathcal{S}_{\rm adel}^{\rm amp}.} \qquad (6\text{-BWadel})
$$

$B_W^{\rm adel}$: wohldefiniert $\checkmark$, hermitesch $\checkmark$, sesquilinear $\checkmark$, Diagonale $=\mathfrak{W}(R_{\rm PW}F)$ $\checkmark$.

$$
\boxed{B_W^{\rm adel}:\mathcal{S}_{\rm adel}^{\rm amp}\times\mathcal{S}_{\rm adel}^{\rm amp}\to\mathbb{C}\text{ wohldef., sesquilinear, hermitesch.}\quad\checkmark[K/M]} \qquad (6\text{-status})
$$

---

## 7. Positivitäts-Firewall

$$
\boxed{B_W(a,b)\text{ ist hermitesch. Positivität }B_W(a,a)\ge0\text{ ist nicht bewiesen und nicht behauptet.}} \qquad (7\text{-Fire})
$$

$$
B_W=T^*T\quad\times[M].\qquad(\text{nicht bewiesen}) \qquad (7\text{-noTT})
$$

NEU-220l PD5a2f: Positivität von $\mathfrak{W}(a)$ für alle $a$ ist äquivalent zu RH. GNS-Realisierung $\mathcal{H}_{\mathfrak{W}}$ erst nach M4. Globale Gram-/Krein-Geometrie: $\to$ NEU-253 M4.

---

## 8. Gesamtergebnis M3

$$
\boxed{\mathcal{S}_{\rm adel}^{\rm amp}\longrightarrow(\mathcal{A}_{\rm PW},B_W)\text{ vollständig hermitesch, RH-frei.}\quad\checkmark[K/M]} \qquad (8\text{-M3})
$$

---

## 9. Statusbuchungen

$$g_{a,b}\in\mathcal{G}_{\rm ev}^{\mathbb{C}},\;g_{b,a}=\overline{g_{a,b}},\;g_{a,a}=g_a\quad\checkmark[K/M] \qquad (9\text{-a})$$
$$h_{a,b}\in\mathcal{A}_{\rm PW}\quad\times[M]\;(\text{Paley-Wiener-Typfehler, Patch §1.3}) \qquad (9\text{-b})$$
$$h_{a,b}\in\mathcal{H}_{\rm PW}^{\mathbb{C}},\;h_{a,b}|_{\mathbb{R}}\in\mathcal{S}(\mathbb{R}),\;\text{ganz und gerade}\quad\checkmark[K/M] \qquad (9\text{-c})$$
$$F_{a,b}(s)=h_{a,b}((s-\tfrac{1}{2})/i)\in\mathcal{W}_{\mathbb{C}}\quad\checkmark[K/M] \qquad (9\text{-d})$$
$$B_{\rm pole}(a,b)\text{ sesquilinear, hermitesch}\quad\checkmark[K/M] \qquad (9\text{-e})$$
$$B_\Gamma(a,b)\text{ sesquilinear, hermitesch; }\Lambda_\Gamma\text{ auf }h_{a,b}|_{\mathbb{R}}\in\mathcal{S}(\mathbb{R})\quad\checkmark[K/M] \qquad (9\text{-f})$$
$$B_{\rm fin}(a,b)\text{ sesquilinear, hermitesch, endlich (Kompaktheit von }g_{a,b})\quad\checkmark[K/M] \qquad (9\text{-g})$$
$$B_W(a,b)=B_{\rm pole}+B_\Gamma+B_{\rm fin}\text{ sesquilinear, hermitesch}\quad\checkmark[K/M] \qquad (9\text{-h})$$
$$B_W(a,a)=\mathfrak{W}(a)\quad\checkmark[K/M] \qquad (9\text{-i})$$
$$B_W^{\rm adel}\text{ wohldef., sesquilinear, hermitesch}\quad\checkmark[K/M] \qquad (9\text{-j})$$
$$B_W=T^*T\quad\times[M]\;(\text{Positivität nicht behauptet}) \qquad (9\text{-k})$$
$$\text{M3}\quad\checkmark[K/M] \qquad (9\text{-M3})$$

---

## 10. Abhängigkeiten

| Referenz | SHA | Inhalt |
|---|---|---|
| NEU-220l | 1dc07b3 | Masterform $\mathfrak{W}(a)$; PD5a2a–f; Positivitäts-Firewall |
| NEU-220k (Masterkontur) | 495544d | Vorzeichen, Faktor 2, Polbuchhaltung |
| NEU-220k (Konturtransport) | dc45cf8 | Konvergenz, Explizitformel |
| NEU-220c | a98a2e9 | Weil-Normierung, Gamma-Vorfaktor |
| NEU-220b | 01c6d23 | $T_\Gamma^{\rm raw}$ auf $\mathcal{S}(\mathbb{R})$; Involutionsverträglichkeit |
| NEU-250m | ecc1c3b | $g_{a,b}$ hermitesche Polarisation M2-Patch; $B_{\rm fin}$ |
| NEU-250r (Patch) | bd1c0ab | $R_{\rm PW}$ surjektiv; $\mathcal{G}_{\rm ev}^{\mathbb{C}}$; Firewall aufgelöst |
| **NEU-253** | **neu** | **M4: RH-unabhängige geometrische Realisierung von $B_W$** |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07. Patch 2026-08-07: §1.3 $h_{a,b}\in\mathcal{A}_{\rm PW}$ $\times[M]$; $\mathcal{H}_{\rm PW}^{\mathbb{C}}$ eingeführt; $h_{a,b}|_{\mathbb{R}}\in\mathcal{S}(\mathbb{R})$; $F_{a,b}\in\mathcal{W}_{\mathbb{C}}$; Gamma-Block Typkorrektur.*
