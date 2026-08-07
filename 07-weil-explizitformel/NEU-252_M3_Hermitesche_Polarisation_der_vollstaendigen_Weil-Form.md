# NEU-252 — M3: Hermitesche Polarisation der vollständigen Weil-Form

**Katalog-ID:** NEU-252  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07  
**Auftrag:** M3 — Komponentenweiser Nachweis: Pol-, Gamma- und Primzahlpotenzblock respektieren alle dieselbe $g_{a,b}$-Polarisation; vollständige hermitesche sesquilineare Weil-Form $B_W(a,b)$; adelischer Transport via $R_{\rm PW}$; Positivitäts-Firewall.  
**Gesamtausgang:** M3 $\checkmark[K/M]$. $\mathcal{S}_{\rm adel}^{\rm amp}\to(\mathcal{A}_{\rm PW},B_W)$ vollständig hermitesch, RH-frei.  
**Vorgänger:** NEU-220l (PD5a2a–f), NEU-220k (Masterform), NEU-220b/c (Gamma-Block), NEU-250m (M2-Patch), NEU-250r (Amplitudenport)

---

## 0. Ausgangslage und Auftrag

NEU-220l (PD5a2f) stellt fest: Die hermitesche sesquilineare Form $(a,b)\mapsto\mathfrak{W}(a,b)$ ist **bedingungslos** durch Polarisation verfügbar. M3 führt den stärkeren **komponentenweisen** Nachweis: Jeder der drei Blöcke der Masterform aus NEU-220k/l—Polterm, Gamma-Block, Primzahlpotenzterm—ist für sich sesquilinear und hermitesch unter derselben Polarisation $g_{a,b}$.

$$
\boxed{\text{M3 konstruiert nicht die Polarisation erstmals. M3 beweist die komponentenweise Konsistenz.}} \qquad (0\text{-Scope})
$$

---

## 1. Amplitudenraum und Polarisation

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
\boxed{g_{a,b}(t):=\frac{1}{2}\bigl(C_{a,b}(t)+C_{a,b}(-t)\bigr).} \qquad (1\text{-gab})
$$

**Drei Grundeigenschaften:**

$$
g_{a,b}\in\mathcal{G}_{\rm ev}^{\mathbb{C}}:=C_c^\infty(\mathbb{R};\mathbb{C})_{\rm even}\quad\checkmark \qquad (1\text{-i})
$$

*Beweis:* $g_{a,b}(-t)=\tfrac{1}{2}(C_{a,b}(-t)+C_{a,b}(t))=g_{a,b}(t)$. Träger: $\operatorname{supp}(C_{a,b})\subset\operatorname{supp}(a)-\operatorname{supp}(b)$ kompakt, also $g_{a,b}\in C_c^\infty$.

$$
g_{b,a}(t)=\overline{g_{a,b}(t)}\quad\checkmark \qquad (1\text{-ii})
$$

*Beweis:* $C_{b,a}(t)=\int b(v)\overline{a(v-t)}\,dv=\overline{C_{a,b}(-t)}$, also
$g_{b,a}(t)=\tfrac{1}{2}(C_{b,a}(t)+C_{b,a}(-t))=\tfrac{1}{2}(\overline{C_{a,b}(-t)}+\overline{C_{a,b}(t)})=\overline{g_{a,b}(t)}$.

$$
g_{a,a}(t)=\operatorname{Re}\langle a,U_ta\rangle=g_a(t)\in C_c^\infty(\mathbb{R};\mathbb{R})_{\rm even}\quad\checkmark \qquad (1\text{-iii})
$$

### 1.3 Komplexifizierter Weil-Kern

$$
\boxed{h_{a,b}(z):=\int_{\mathbb{R}}g_{a,b}(u)e^{izu}\,du.} \qquad (1\text{-hab})
$$

$h_{a,b}\in\mathcal{A}_{\rm PW}$ (Fourier-Bild kompakt-getragener glatter Funktion), und wegen $g_{a,b}$ gerade:
$$
h_{a,b}(z)=h_{a,b}(-z).\qquad\checkmark \qquad (1\text{-even})
$$

**Weil-Symmetrie:** $h_{a,b}(z)=h_{a,b}(-z)$ impliziert $F_{a,b}(s):=h_{a,b}\bigl(\tfrac{s-1/2}{i}\bigr)$
erfüllt
$$
F_{a,b}(1-s)=h_{a,b}\bigl(\tfrac{(1-s)-1/2}{i}\bigr)=h_{a,b}\bigl(-\tfrac{s-1/2}{i}\bigr)=h_{a,b}\bigl(\tfrac{s-1/2}{i}\bigr)=F_{a,b}(s).\quad\checkmark \qquad (1\text{-sym})
$$

NEU-220k ist unmittelbar anwendbar. $\checkmark$

---

## 2. Komponentenweise Polarisation: Polterm

Der Polterm der Masterform (NEU-220k/l) lautet:
$$
B_{\rm pole}(a,a):=h_a(i/2)+h_a(-i/2). \qquad (2\text{-diag})
$$

Polarisierte Version:
$$
\boxed{B_{\rm pole}(a,b):=h_{a,b}(i/2)+h_{a,b}(-i/2).} \qquad (2\text{-Bpole})
$$

**Sesquilinearität in $a$:** $h_{a,b}(z)=\int g_{a,b}(u)e^{izu}\,du$, und $g_{a,b}(t)=\tfrac{1}{2}\int\bigl(a(v)\overline{b(v-t)}+a(v)\overline{b(v+t)}\bigr)dv$ ist linear in $a$. $\checkmark$

**Hermitizität:** $h_{b,a}(z)=\overline{h_{a,b}(\bar z)}=\overline{h_{a,b}(z)}$ (da $g_{b,a}=\overline{g_{a,b}}$ und $z=i/2$ reines Imaginär $\Rightarrow h_{a,b}(i/2)\in\mathbb{R}$ auf der Diagonale). Im Allgemeinen:
$$
B_{\rm pole}(b,a)=\overline{B_{\rm pole}(a,b)}.\quad\checkmark \qquad (2\text{-herm})
$$

**Diagonale:** $B_{\rm pole}(a,a)=h_a(i/2)+h_a(-i/2)$. $\checkmark$

$$
\boxed{B_{\rm pole}(a,b)\text{ sesquilinear, hermitesch.}\quad\checkmark[K/M]} \qquad (2\text{-status})
$$

---

## 3. Komponentenweise Polarisation: Gamma-Block

Der Gamma-Block der Masterform lautet (NEU-220k/l, Normierung aus NEU-220c/k):
$$
B_\Gamma(a,a):=2\Lambda_\Gamma(h_a). \qquad (3\text{-diag})
$$

Hier ist $\Lambda_\Gamma$ die in NEU-220k fixierte archimedische Gamma-Distribution (keine ältere offene PD-3d-Normierung).

Polarisierte Version:
$$
\boxed{B_\Gamma(a,b):=2\Lambda_\Gamma(h_{a,b}).} \qquad (3\text{-BGamma})
$$

**Wohldefiniertheit:** NEU-220b zeigt: $T_\Gamma^{\rm raw}$ ist auf der vollen $\mathcal{S}(\mathbb{R})$ definiert und involutionsverträglich. Da $h_{a,b}\in\mathcal{A}_{\rm PW}\subset\mathcal{S}(\mathbb{R})$ und $h_{a,b}(z)=h_{a,b}(-z)$, ist $\Lambda_\Gamma(h_{a,b})$ wohldefiniert. $\checkmark$

**Sesquilinearität:** $h_{a,b}$ ist linear in $a$, $\Lambda_\Gamma$ ist linear, also $B_\Gamma(a,b)$ linear in $a$. $\checkmark$

**Hermitizität:** $h_{b,a}=\overline{h_{a,b}}$ (auf reeller Achse), also
$$
B_\Gamma(b,a)=2\Lambda_\Gamma(h_{b,a})=2\Lambda_\Gamma(\overline{h_{a,b}})=2\overline{\Lambda_\Gamma(h_{a,b})}=\overline{B_\Gamma(a,b)}.\quad\checkmark \qquad (3\text{-herm})
$$

(Hier benutzen wir die reelle Linearität und die Konjugationseigenschaft von $\Lambda_\Gamma$, die NEU-220b/c nachweist.)

**Diagonale:** $B_\Gamma(a,a)=2\Lambda_\Gamma(h_a)$. $\checkmark$

$$
\boxed{B_\Gamma(a,b)\text{ sesquilinear, hermitesch.}\quad\checkmark[K/M]} \qquad (3\text{-status})
$$

---

## 4. Komponentenweise Polarisation: Primzahlpotenzterm

Der Primzahlpotenzterm der Masterform lautet (NEU-220l PD5a2d; NEU-250m M2-Patch):
$$
B_{\rm fin}(a,a):=-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt{n}}\,g_a(\log n). \qquad (4\text{-diag})
$$

Polarisierte Version (NEU-250m M2.3):
$$
\boxed{B_{\rm fin}(a,b):=-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt{n}}\,g_{a,b}(\log n).} \qquad (4\text{-Bfin})
$$

**Konvergenz:** Für $a,b\in\mathcal{A}_{\rm PW}$ mit $\operatorname{supp}(a),\operatorname{supp}(b)\subset[-R,R]$: $g_{a,b}(t)=0$ für $|t|>2R$, also $g_{a,b}(\log n)=0$ für $n>e^{2R}$. Summe **tatsächlich endlich**. $\checkmark$

**Sesquilinearität:** $g_{a,b}(\log n)$ linear in $a$; endliche Summe; $B_{\rm fin}(a,b)$ linear in $a$. $\checkmark$

**Hermitizität:**
$$
B_{\rm fin}(b,a)=-2\sum_n\frac{\Lambda(n)}{\sqrt{n}}\,g_{b,a}(\log n)=-2\sum_n\frac{\Lambda(n)}{\sqrt{n}}\,\overline{g_{a,b}(\log n)}=\overline{B_{\rm fin}(a,b)}.\quad\checkmark \qquad (4\text{-herm})
$$

**Diagonale:** $B_{\rm fin}(a,a)=-2\sum_n\frac{\Lambda(n)}{\sqrt{n}}g_a(\log n)$. $\checkmark$

Sprachliche Klarheit (NEU-250m): Der Faktor $-2$ ist global (Weil-Explizitformel). Der von-Mangoldt-Koeffizient $\Lambda(n)/\sqrt{n}>0$ ist lokal. Beide werden nicht identifiziert.

$$
\boxed{B_{\rm fin}(a,b)\text{ sesquilinear, hermitesch, endlich auf }\mathcal{A}_{\rm PW}.}\quad\checkmark[K/M] \qquad (4\text{-status})
$$

---

## 5. Vollständige hermitesche Weil-Form

$$
\boxed{B_W(a,b):=B_{\rm pole}(a,b)+B_\Gamma(a,b)+B_{\rm fin}(a,b).} \qquad (5\text{-BW})
$$

**Satz (M3-Hauptsatz):**

$$
\boxed{B_W:\mathcal{A}_{\rm PW}\times\mathcal{A}_{\rm PW}\to\mathbb{C}\quad\text{ist sesquilinear und hermitesch.}\quad\checkmark[K/M]} \qquad (5\text{-Main})
$$

*Beweis:* Endliche Summe sesquilinearer hermitescher Formen (\S\S2–4). $\square$

**Diagonale reproduziert die vollständige Weil-Quadratik:**
$$
\boxed{B_W(a,a)=\mathfrak{W}(a).\quad\checkmark[K/M]} \qquad (5\text{-Diag})
$$

*Beweis:* $B_{\rm pole}(a,a)+B_\Gamma(a,a)+B_{\rm fin}(a,a)=h_a(i/2)+h_a(-i/2)+2\Lambda_\Gamma(h_a)-2\sum_n\frac{\Lambda(n)}{\sqrt{n}}g_a(\log n)=\mathfrak{W}(a)$ nach NEU-220l PD5a2d. $\square$

---

## 6. Adelischer Transport

Mit dem surjektiven Port $R_{\rm PW}:\mathcal{S}_{\rm adel}^{\rm amp}\twoheadrightarrow\mathcal{A}_{\rm PW}$ (NEU-250r) setze:

$$
\boxed{B_W^{\rm adel}(F,G):=B_W(R_{\rm PW}F,\,R_{\rm PW}G),\qquad F,G\in\mathcal{S}_{\rm adel}^{\rm amp}.} \qquad (6\text{-BWadel})
$$

**Prüfung:**

$$
B_W^{\rm adel}\text{ wohldefiniert}\quad\checkmark \qquad (6\text{-wd})
$$
(da $R_{\rm PW}F,R_{\rm PW}G\in\mathcal{A}_{\rm PW}$ und $B_W$ auf $\mathcal{A}_{\rm PW}$ wohldefiniert)

$$
B_W^{\rm adel}\text{ hermitesch}\quad\checkmark \qquad (6\text{-herm})
$$
($B_W^{\rm adel}(G,F)=B_W(R_{\rm PW}G,R_{\rm PW}F)=\overline{B_W(R_{\rm PW}F,R_{\rm PW}G)}=\overline{B_W^{\rm adel}(F,G)}$)

$$
B_W^{\rm adel}\text{ sesquilinear}\quad\checkmark \qquad (6\text{-sql})
$$
($R_{\rm PW}$ ist $\mathbb{C}$-linear; $B_W$ ist sesquilinear)

$$
B_W^{\rm adel}(F,F)=\mathfrak{W}(R_{\rm PW}F)\quad\checkmark \qquad (6\text{-diag})
$$
(Diagonale reproduziert vollständige Weil-Quadratik via $R_{\rm PW}$)

$$
\boxed{B_W^{\rm adel}:\mathcal{S}_{\rm adel}^{\rm amp}\times\mathcal{S}_{\rm adel}^{\rm amp}\to\mathbb{C}\text{ wohldefiniert, sesquilinear, hermitesch.}\quad\checkmark[K/M]} \qquad (6\text{-status})
$$

---

## 7. Positivitäts-Firewall

$$
\boxed{B_W(a,b)\text{ ist hermitesch. Positivität }B_W(a,a)\ge0\text{ ist nicht bewiesen und nicht behauptet.}} \qquad (7\text{-Fire})
$$

Explizit ausgeschlossen:
$$
B_W=T^*T\quad\times[M].\qquad(\text{nicht bewiesen}) \qquad (7\text{-noTT})
$$

NEU-220l PD5a2f stellt klar: Positivität von $\mathfrak{W}(a)$ für alle $a$ ist äquivalent zu RH. Eine GNS-Realisierung aus $B_W$ wäre entweder konditional unter RH oder ein RH-Beweis. Beides gehört zu M4, nicht zu M3.

$$
\boxed{\text{GNS/Hilbert-Realisierung aus }B_W:\text{ erst nach M4.}} \qquad (7\text{-GNS})
$$

---

## 8. Gesamtergebnis M3

$$
\boxed{\mathcal{S}_{\rm adel}^{\rm amp}\xrightarrow{R_{\rm PW}}\mathcal{A}_{\rm PW}\xrightarrow{B_W}(\mathcal{A}_{\rm PW},B_W)\text{ vollständig hermitesch, RH-frei.}\quad\checkmark[K/M]} \qquad (8\text{-M3})
$$

Zum ersten Mal besteht:
$$
\boxed{\mathcal{S}_{\rm adel}^{\rm amp}\longrightarrow(\mathcal{A}_{\rm PW},B_W)\text{ mit vollständiger, RH-freier hermitescher adelisch transportierter Weil-Form.}} \qquad (8\text{-Record})
$$

---

## 9. Statusbuchungen

$$
g_{a,b}\in\mathcal{G}_{\rm ev}^{\mathbb{C}},\;g_{b,a}=\overline{g_{a,b}},\;g_{a,a}=g_a\quad\checkmark[K/M] \qquad (9\text{-a})
$$

$$
B_{\rm pole}(a,b)\text{ sesquilinear, hermitesch}\quad\checkmark[K/M] \qquad (9\text{-b})
$$

$$
B_\Gamma(a,b)\text{ sesquilinear, hermitesch (Normierung aus NEU-220k)}\quad\checkmark[K/M] \qquad (9\text{-c})
$$

$$
B_{\rm fin}(a,b)\text{ sesquilinear, hermitesch, endlich auf }\mathcal{A}_{\rm PW}\quad\checkmark[K/M] \qquad (9\text{-d})
$$

$$
B_W(a,b)=B_{\rm pole}+B_\Gamma+B_{\rm fin}\text{ sesquilinear, hermitesch}\quad\checkmark[K/M] \qquad (9\text{-e})
$$

$$
B_W(a,a)=\mathfrak{W}(a)\quad\checkmark[K/M] \qquad (9\text{-f})
$$

$$
B_W^{\rm adel}(F,G)=B_W(R_{\rm PW}F,R_{\rm PW}G)\text{ wohldef., sesquilinear, hermitesch}\quad\checkmark[K/M] \qquad (9\text{-g})
$$

$$
B_W=T^*T\quad\times[M]\qquad(\text{Positivität nicht behauptet}) \qquad (9\text{-h})
$$

$$
\text{M3}\quad\checkmark[K/M] \qquad (9\text{-M3})
$$

---

## 10. Nächster atomarer Auftrag: M4

$$
\boxed{\text{M4: Welche kanonische globale Geometrie realisiert }B_W\text{ und woher kommt ihre positive Reduktion?}} \qquad (10\text{-M4})
$$

Konkret:
- **M4-A:** Krein-Raumstruktur aus $B_W$: Signaturzerlegung $\mathcal{A}_{\rm PW}=\mathcal{H}_+\oplus\mathcal{H}_-$ (unter welcher Bedingung?).
- **M4-B:** Gram-Geometrie: Wann ist $B_W$ positiv-semidefinit? Äquivalenz mit RH nach NEU-220l PD5a2b.
- **M4-C:** Kanonische adelische Erweiterung: Ist $\mathcal{S}_{\rm adel}^{\rm amp}$ der richtige globale Quellenraum, oder braucht M4 eine größere Struktur?
- **M4-D:** GNS-Realisierung: $B_W(a,a)\ge0\Leftrightarrow$ RH; erst danach $\mathcal{H}_{\mathfrak{W}}:=\mathcal{A}_{\rm PW}/\ker B_W$.

---

## 11. Abhängigkeiten

| Referenz | SHA | Inhalt |
|---|---|---|
| NEU-220l | 1dc07b3 | Masterform $\mathfrak{W}(a)$; PD5a2a–f; Polarisation verfügbar; Positivitäts-Firewall |
| NEU-220k (Masterkontur) | 495544d | Vorzeichen, Faktor 2, Polbuchhaltung |
| NEU-220k (Konturtransport) | dc45cf8 | Konvergenz, Explizitformel |
| NEU-220c | a98a2e9 | Weil-Normierung, Gamma-Vorfaktor |
| NEU-220b | 01c6d23 | $T_\Gamma^{\rm raw}$ auf $\mathcal{S}(\mathbb{R})$; Involutionsverträglichkeit |
| NEU-250m | ecc1c3b | $g_{a,b}$ hermitesche Polarisation M2-Patch; $B_{\rm fin}$ |
| NEU-250r | bd1c0ab | $R_{\rm PW}$ surjektiv; $\mathcal{G}_{\rm ev}^{\mathbb{C}}$; Firewall aufgelöst |
| NEU-250p | 56ba1f7 | $J_{1/2}$-Kette; Weil-Selbstdualität |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07.*
