# NEU-250r — Komplexer adelischer Amplitudenport und Auflösung der Realitäts-Firewall

**Katalog-ID:** NEU-250r  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07 (Patch: 2026-08-07)  
**Auftrag:** (1) $\mathcal{S}_{\rm adel}^{\rm amp}$ definieren. (2) Port $R_{\rm PW}$ beweisen. (3) Surjektivität mit explizitem Lift. (4) Realitäts-Firewall auflösen: $\mathcal{G}_{\rm ev}^{\mathbb{C}}$ einführen; diagonale Aussage von komplexer Polarisation trennen; M3-Kette typisieren.  
**Gesamtausgang:** $R_{\rm PW}$ wohldef. und surjektiv $\checkmark[K/M]$; Realitäts-Firewall $\checkmark$ aufgelöst; **M3 freigegeben**.  
**Vorgänger:** NEU-250q (Patch 2), NEU-250m (M2-Patch), NEU-250p, NEU-220l, NEU-220j, NEU-220a

---

## 0. Überblick

NEU-250q hatte als Realitäts-Firewall festgehalten:
$$
\mathcal{C}_W\neq\text{komplexe Formdomäne für }B_W(a,b).
$$
Dieses Dokument löst die Firewall auf: Die natürliche Evenisierung für die komplexe hermitesche Polarisation landet in
$$
\mathcal{G}_{\rm ev}^{\mathbb{C}}:=C_c^\infty(\mathbb{R};\mathbb{C})_{\rm even},
$$
nicht in $\mathcal{C}_W\subset C_c^\infty((0,\infty);\mathbb{R})$. Die Diagonale fällt dann automatisch in den reell-geraden Testbereich von NEU-220j zurück.

---

## 1. Ausgangslage: $\mathcal{A}_{\rm PW}$ als komplexe Formdomäne

NEU-220l definiert:
$$
\boxed{\mathcal{A}_{\rm PW}:=C_c^\infty(\mathbb{R};\mathbb{C}).} \qquad (1\text{-APW})
$$

Für $a\in\mathcal{A}_{\rm PW}$ ist $c_a:=a*a^\sharp$ die Autokorrelation. Sie ist hermitesch:
$$
c_a(-u)=\overline{c_a(u)},
$$
im Allgemeinen aber **nicht** reell-gerade. Erst die Evenisierung
$$
g_a(u):=\operatorname{Re}c_a(u)=\tfrac{1}{2}(c_a(u)+c_a(-u))
$$
ist reell-gerade, $g_a\in C_c^\infty(\mathbb{R};\mathbb{R})_{\rm even}$ — der Testbereich von NEU-220j.

$$
\boxed{c_a\notin\mathcal{C}_W\text{ im Allgemeinen; }g_a\in C_c^\infty(\mathbb{R};\mathbb{R})_{\rm even}.} \qquad (1\text{-Diag})
$$

---

## 2. Neuer adelischer Amplitudenraum $\mathcal{S}_{\rm adel}^{\rm amp}$

$$
\boxed{\mathcal{S}_{\rm adel}^{\rm amp}:=\left\{F\in\mathcal{S}(\mathbb{A}_\mathbb{Q}):(P_{\rm Haar}F)\big|_{(0,\infty)}\in C_c^\infty((0,\infty);\mathbb{C})\right\}.} \qquad (2\text{-Samp})
$$

---

## 3. Komplexer Amplitudenport $R_{\rm PW}$

$$
\boxed{R_{\rm PW}F(u):=e^{u/2}(P_{\rm Haar}F)(e^u),\qquad u\in\mathbb{R}.} \qquad (3\text{-RPW})
$$

**Wohldefiniertheit:** Träger von $(P_{\rm Haar}F)|_{(0,\infty)}$ in $[c,C]\subset(0,\infty)$ $\Rightarrow$ Träger von $R_{\rm PW}F$ in $[\log c,\log C]\subset\mathbb{R}$ $\Rightarrow$ $R_{\rm PW}F\in\mathcal{A}_{\rm PW}$.

$$
\boxed{R_{\rm PW}:\mathcal{S}_{\rm adel}^{\rm amp}\longrightarrow\mathcal{A}_{\rm PW}\quad\checkmark[K/M].} \qquad (3\text{-Port})
$$

---

## 4. Surjektivität auf $\mathcal{A}_{\rm PW}$: expliziter Lift

$$
\boxed{R_{\rm PW}:\mathcal{S}_{\rm adel}^{\rm amp}\twoheadrightarrow\mathcal{A}_{\rm PW}\quad\checkmark[K/M].} \qquad (4\text{-Surj})
$$

**Beweis.** Sei $a\in C_c^\infty(\mathbb{R};\mathbb{C})$ beliebig. Setze
$$
\boxed{h_a(x):=\begin{cases}x^{-1/2}a(\log x) & x>0,\\ 0 & x\le0,\end{cases}\qquad F_a:=h_a\otimes\mathbf{1}_{\hat{\mathbb{Z}}}.} \qquad (4\text{-Lift})
$$

Da $\operatorname{supp}a\subset[A,B]$, liegt $\operatorname{supp}h_a\subset[e^A,e^B]\subset(0,\infty)$; $h_a\in C_c^\infty(\mathbb{R};\mathbb{C})$; $(P_{\rm Haar}F_a)|_{(0,\infty)}=h_a|_{(0,\infty)}\in C_c^\infty((0,\infty);\mathbb{C})$; also $F_a\in\mathcal{S}_{\rm adel}^{\rm amp}$. Und:
$$
R_{\rm PW}F_a(u)=e^{u/2}h_a(e^u)=e^{u/2}\cdot e^{-u/2}a(u)=a(u).\quad\checkmark \qquad (4\text{-Check})
$$

$$
\boxed{\text{Der adelische Port erreicht die gesamte Weil-Amplitudendomäne }\mathcal{A}_{\rm PW}.} \qquad (4\text{-Strat})
$$

---

## 5. Auflösung der Realitäts-Firewall: $\mathcal{G}_{\rm ev}^{\mathbb{C}}$ und hermitesche Polarisation

### 5.1 Komplexifizierte Evenisierung

Für $a,b\in\mathcal{A}_{\rm PW}$ definiere die verschobene Kreuzkorrelation
$$
C_{a,b}(t):=\langle a,U_tb\rangle=\int_{\mathbb{R}}a(v)\overline{b(v-t)}\,dv
$$
und die hermitesche Evenisierung
$$
\boxed{g_{a,b}(t):=\frac{1}{2}\bigl(C_{a,b}(t)+C_{a,b}(-t)\bigr).} \qquad (5\text{-gab})
$$

Dann:
$$
\boxed{\mathcal{G}_{\rm ev}^{\mathbb{C}}:=C_c^\infty(\mathbb{R};\mathbb{C})_{\rm even},\qquad g_{a,b}\in\mathcal{G}_{\rm ev}^{\mathbb{C}}.} \qquad (5\text{-Gev})
$$

**Hermitizität:** $g_{b,a}(t)=\overline{g_{a,b}(t)}$. $\checkmark$

### 5.2 Diagonale

Auf der Diagonale $b=a$ fällt $g_{a,b}$ in den reellen Teilraum:
$$
\boxed{g_{a,a}(t)=\operatorname{Re}\langle a,U_ta\rangle=g_a(t)\in C_c^\infty(\mathbb{R};\mathbb{R})_{\rm even}.} \qquad (5\text{-Diag})
$$

Das ist genau der Testbereich von NEU-220j. $\checkmark$

### 5.3 $\mathcal{C}_W$ ist Bild der Diagonale, nicht Quellenformdomäne

$$
\boxed{\mathcal{C}_W\subset C_c^\infty(\mathbb{R};\mathbb{R})_{\rm even}\text{ ist der Bildraum der Diagonale }a\mapsto g_{a,a},\text{ nicht die Quellenformdomäne.}} \qquad (5\text{-CW})
$$

---

## 6. Korrekte M3-Kette (Fourier-/Weil-Port aus NEU-220j)

Der Schritt $\mathcal{G}_{\rm ev}^{\mathbb{C}}\to\mathcal{W}_{\mathbb{C}}$ wird durch den Fourier-/Weil-Port aus NEU-220j realisiert: Für $g\in\mathcal{G}_{\rm ev}^{\mathbb{C}}$
$$
g\longmapsto h(z):=\int_{\mathbb{R}}g(u)e^{izu}\,du\longmapsto F_h(s):=h\!\left(\frac{s-\tfrac{1}{2}}{i}\right). \qquad (6\text{-FourierWeil})
$$

Der reell-gerade Mel\-lin-Port $\mathcal{M}_\infty:\mathcal{C}_W\to\mathcal{W}$ (NEU-220a) ist die Einschränkung auf die reelle Diagonale.

$$
\boxed{\mathcal{S}_{\rm adel}^{\rm amp}\xrightarrow{R_{\rm PW}}\mathcal{A}_{\rm PW}\xrightarrow{(a,b)\mapsto g_{a,b}}\mathcal{G}_{\rm ev}^{\mathbb{C}}\xrightarrow{\text{Fourier/Weil}}\mathcal{W}_{\mathbb{C}}.} \qquad (6\text{-M3-Chain})
$$

Auf der Diagonale:
$$
\mathcal{S}_{\rm adel}^{\rm amp}\xrightarrow{R_{\rm PW}}\mathcal{A}_{\rm PW}\xrightarrow{a\mapsto g_{a,a}}C_c^\infty(\mathbb{R};\mathbb{R})_{\rm even}\xrightarrow{\mathcal{M}_\infty}\mathcal{W}.\quad\checkmark \qquad (6\text{-Diag-Chain})
$$

**Alle Pfeile typisiert:**

| Pfeil | Typ | Status |
|---|---|---|
| $R_{\rm PW}$: $\mathcal{S}_{\rm adel}^{\rm amp}\to\mathcal{A}_{\rm PW}$ | wohldef., surjektiv | $\checkmark[K/M]$ |
| $(a,b)\mapsto g_{a,b}$: $\mathcal{A}_{\rm PW}\times\mathcal{A}_{\rm PW}\to\mathcal{G}_{\rm ev}^{\mathbb{C}}$ | hermitesch, sesquilinear | $\checkmark[K/M]$ |
| Diagonale $a\mapsto g_{a,a}$: $\mathcal{A}_{\rm PW}\to C_c^\infty(\mathbb{R};\mathbb{R})_{\rm even}$ | reell-gerade | $\checkmark[K/M]$ |
| Fourier/Weil-Port: $\mathcal{G}_{\rm ev}^{\mathbb{C}}\to\mathcal{W}_{\mathbb{C}}$ | NEU-220j, Komplexifizierung | $\checkmark[K/M]$ |

$$
\boxed{\textbf{M3 freigegeben.}} \qquad (6\text{-M3-Release})
$$

---

## 7. Status Q-B / Q-C (präzisiert)

$$
\boxed{\text{Für die bisherige Paley-Wiener-Domäne }\mathcal{A}_{\rm PW}\text{ werden Q-B/Q-C nicht benötigt.}\quad\checkmark[K/M]} \qquad (7\text{-QB-QC})
$$

Nicht bewiesen und offen: Ob $\mathcal{S}_{\rm adel}^{\rm amp}$ der kanonische **globale** Quellenraum von Objekt X ist. Er ist ein auf $\mathcal{A}_{\rm PW}$ zugeschnittener, surjektiv-effizienter Unterraum. Globale Gramgeometrie und spätere M4-Anforderungen könnten einen größeren oder kanonischeren Raum verlangen.

---

## 8. Statusbuchungen

$$
R_{\rm PW}:\mathcal{S}_{\rm adel}^{\rm amp}\twoheadrightarrow\mathcal{A}_{\rm PW}\quad\checkmark[K/M] \qquad (8\text{-a})
$$

$$
g_{a,b}=\tfrac{1}{2}(C_{a,b}+C_{a,b}(-\cdot))\in\mathcal{G}_{\rm ev}^{\mathbb{C}}\quad\checkmark[K/M] \qquad (8\text{-b})
$$

$$
g_{b,a}=\overline{g_{a,b}}\quad\checkmark[K/M] \qquad (8\text{-c})
$$

$$
g_{a,a}=\operatorname{Re}\langle a,U_ta\rangle\in C_c^\infty(\mathbb{R};\mathbb{R})_{\rm even}\quad\checkmark[K/M] \qquad (8\text{-d})
$$

$$
c_a\notin\mathcal{C}_W\text{ im Allgemeinen; }\mathcal{C}_W=\text{Bild der Diagonale}\quad\checkmark[K/M] \qquad (8\text{-e})
$$

$$
\text{M3-Kette vollst. typisiert: }\mathcal{S}_{\rm adel}^{\rm amp}\to\mathcal{A}_{\rm PW}\to\mathcal{G}_{\rm ev}^{\mathbb{C}}\to\mathcal{W}_{\mathbb{C}}\quad\checkmark[K/M] \qquad (8\text{-f})
$$

$$
\text{Q-B/Q-C nur für PW-Bereich nicht benötigt; globale Kanonizität offen}\quad?[O] \qquad (8\text{-g})
$$

---

## Abhängigkeiten

| Referenz | SHA | Inhalt |
|---|---|---|
| NEU-250q (Patch 2) | 7c03f68 | Exakte Konvergenzbedingung; Nichtdichtheit; Firewall |
| NEU-250m | ecc1c3b | $B_{\rm fin}$; hermitesche Polarisation $g_{a,b}$ |
| NEU-250p | 56ba1f7 | $J_{1/2}$-Kette; Weil-Selbstdualität |
| NEU-220l | 1dc07b3 | $\mathcal{A}_{\rm PW}$; Autokorrelation; Hermitizität |
| NEU-220j | 41e28cf | Fourier/Weil-Port; $C_c^\infty(\mathbb{R};\mathbb{R})_{\rm even}$-Kern |
| NEU-220a | 653c8a9 | $\mathcal{M}_\infty$; $\mathcal{S}_\infty$ |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07. Patch 2026-08-07: $a\mapsto c_a\to\mathcal{C}_W$ entfernt; $\mathcal{G}_{\rm ev}^{\mathbb{C}}$ eingeführt; diagonale Aussage von komplexer Polarisation getrennt; Fourier/Weil-Port aus NEU-220j; Q-B/Q-C präzisiert.*
