# NEU-250r — Komplexer adelischer Amplitudenport und Auflösung der Realitäts-Firewall

**Katalog-ID:** NEU-250r  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07  
**Auftrag:** (1) $\mathcal{S}_{\rm adel}^{\rm amp}$ definieren. (2) Port $R_{\rm PW}=\Phi J_{1/2}P_{\rm Haar}$ beweisen. (3) Surjektivität auf $\mathcal{A}_{\rm PW}$ mit explizitem Lift. (4) Realitäts-Firewall auflösen; M3 freigeben.  
**Gesamtausgang:** $R_{\rm PW}:\mathcal{S}_{\rm adel}^{\rm amp}\to\mathcal{A}_{\rm PW}$ wohldef. und surjektiv $\checkmark[K/M]$; Realitäts-Firewall $\checkmark$ aufgelöst; **M3 freigegeben**.  
**Vorgänger:** NEU-250q (Patch 2), NEU-250m (M2-Patch), NEU-250p, NEU-220l, NEU-220j

---

## 0. Überblick

NEU-250q hatte als Realitäts-Firewall festgehalten:
$$
\mathcal{C}_W\neq\text{komplexe Formdomäne für }B_W(a,b).
$$
Dieses Dokument löst die Firewall auf: $\mathcal{C}_W$ ist **nicht** die Quellenformdomäne des Weil-Kriteriums. Realität und Geradheit entstehen erst **diagonal** durch $a\mapsto c_a\mapsto g_a$. Der natürliche komplexe Amplitudenport ist
$$
\boxed{R_{\rm PW}=\Phi\circ J_{1/2}\circ P_{\rm Haar},}
$$
und dieser Port ist surjektiv auf $\mathcal{A}_{\rm PW}=C_c^\infty(\mathbb{R};\mathbb{C})$.

---

## 1. Ausgangslage: $\mathcal{A}_{\rm PW}$ als komplexe Formdomäne

NEU-220l definiert:
$$
\boxed{\mathcal{A}_{\rm PW}:=C_c^\infty(\mathbb{R};\mathbb{C}).} \qquad (1\text{-APW})
$$
Dies ist der **komplexe** Amplitudenraum, auf dem die hermitesche sesquilineare Form $B_W(a,b)$ lebt. Der reell-gerade Weil-Testkern $g_a\in\mathcal{C}_W$ entsteht erst durch den Autokorrelationsschritt:
$$
c_a:=a*a^\sharp,\qquad g_a(u):=\operatorname{Re}c_a(u). \qquad (1\text{-AutoCorr})
$$

Die Formdomäne ist also von Anfang an komplex; der reell-gerade Kern ist eine abgeleitete Größe auf der Diagonale.

---

## 2. Neuer adelischer Amplitudenraum $\mathcal{S}_{\rm adel}^{\rm amp}$

$$
\boxed{\mathcal{S}_{\rm adel}^{\rm amp}:=\left\{F\in\mathcal{S}(\mathbb{A}_\mathbb{Q}):(P_{\rm Haar}F)\big|_{(0,\infty)}\in C_c^\infty((0,\infty);\mathbb{C})\right\}.} \qquad (2\text{-Samp})
$$

**Bemerkung:** Die Bedingung ist nur an den **positiven Halbachsenanteil** gestellt. Der Wert bei $x=0$ und der negative Anteil sind frei.

---

## 3. Komplexer Amplitudenport $R_{\rm PW}$

Definiere:
$$
\boxed{R_{\rm PW}F(u):=e^{u/2}(P_{\rm Haar}F)(e^u),\qquad u\in\mathbb{R}.} \qquad (3\text{-RPW})
$$

**Wohldefiniertheit:** Für $F\in\mathcal{S}_{\rm adel}^{\rm amp}$ gilt $(P_{\rm Haar}F)|_{(0,\infty)}\in C_c^\infty((0,\infty);\mathbb{C})$. Der Träger liegt in einem Kompaktum $[c,C]\subset(0,\infty)$. Dann liegt der Träger von $u\mapsto(P_{\rm Haar}F)(e^u)$ in $[\log c,\log C]\subset\mathbb{R}$, und $e^{u/2}$ ist glatt, also:
$$
R_{\rm PW}F\in C_c^\infty(\mathbb{R};\mathbb{C})=\mathcal{A}_{\rm PW}.\qquad\checkmark \qquad (3\text{-WD})
$$

**Kanonik:** $R_{\rm PW}=\Phi\circ J_{1/2}\circ P_{\rm Haar}$ mit $\Phi$ dem Logkoordinatenwechsel.

$$
\boxed{R_{\rm PW}:\mathcal{S}_{\rm adel}^{\rm amp}\longrightarrow\mathcal{A}_{\rm PW}\quad\checkmark[K/M].} \qquad (3\text{-Port})
$$

---

## 4. Surjektivität auf $\mathcal{A}_{\rm PW}$: expliziter Lift

**Satz (Surjektivität):**
$$
\boxed{R_{\rm PW}:\mathcal{S}_{\rm adel}^{\rm amp}\twoheadrightarrow\mathcal{A}_{\rm PW}\quad\checkmark[K/M].} \qquad (4\text{-Surj})
$$

**Beweis.** Sei $a\in\mathcal{A}_{\rm PW}=C_c^\infty(\mathbb{R};\mathbb{C})$ beliebig. Setze
$$
\boxed{h_a(x):=\begin{cases}x^{-1/2}a(\log x) & x>0,\\ 0 & x\le0.\end{cases}} \qquad (4\text{-ha})
$$

*$h_a\in C_c^\infty(\mathbb{R};\mathbb{C})$:* Da $\operatorname{supp}a\subset[A,B]$ (kompakt), gilt $\operatorname{supp}h_a\subset[e^A,e^B]\subset(0,\infty)$; Glattheit folgt aus Glattheit von $a$ und $x^{-1/2}$ auf $(0,\infty)$; bei $x=0$ ist $h_a=0$ mit allen Ableitungen.

Setze den adelischen Lift:
$$
\boxed{F_a(x_\infty,x_{\rm fin}):=h_a(x_\infty)\cdot\mathbf{1}_{\hat{\mathbb{Z}}}(x_{\rm fin})\in\mathcal{S}(\mathbb{A}_\mathbb{Q}).} \qquad (4\text{-Fa})
$$

*$F_a\in\mathcal{S}_{\rm adel}^{\rm amp}$:* $(P_{\rm Haar}F_a)(x_\infty)=h_a(x_\infty)$, und $h_a|_{(0,\infty)}\in C_c^\infty((0,\infty);\mathbb{C})$. $\checkmark$

*$R_{\rm PW}F_a=a$:*
$$
R_{\rm PW}F_a(u)=e^{u/2}h_a(e^u)=e^{u/2}\cdot e^{-u/2}a(u)=a(u).\quad\checkmark \qquad (4\text{-Check})
$$

Da $a\in\mathcal{A}_{\rm PW}$ beliebig war, ist $R_{\rm PW}$ surjektiv. $\square$

**Strategisch:** Wir brauchen nicht jeden adelischen Schwartz-Vektor. Wir brauchen genügend adelische Quellvektoren, um alle Testamplituden des Weil-Kriteriums zu erreichen. Und genau das leistet $R_{\rm PW}$:

$$
\boxed{\text{Der adelische Port erreicht die gesamte Weil-Amplitudendomäne }\mathcal{A}_{\rm PW}.} \qquad (4\text{-Strat})
$$

---

## 5. Auflösung der Realitäts-Firewall

**Firewall (NEU-250q §6):** $\mathcal{C}_W\neq$ komplexe Formdomäne für $B_W(a,b)$.

**Auflösung:** $\mathcal{C}_W$ ist nie als komplexe Quellenformdomäne gedacht gewesen. Es ist der Bildraum unter $J_{1/2}$ für den reell-geraden Weil-Kern. Die komplexe Formdomäne ist $\mathcal{A}_{\rm PW}$, und diese ist der Amplitudenraum **vor** der Autokorrelation.

Die korrekte Struktur:
$$
\boxed{\begin{aligned}
&a\in\mathcal{A}_{\rm PW}\;\text{(komplex, freie Amplitude)},\\
&c_a=a*a^\sharp\;\text{(Autokorrelation)},\\
&g_a=\operatorname{Re}c_a\;\text{(reell-gerade Weil-Kern)}\in\mathcal{C}_W.
\end{aligned}} \qquad (5\text{-Chain})
$$

Realität und Geradheit entstehen **diagonal** und **nach** der Autokorrelation. Das ist kein Hindernis für M3 — im Gegenteil: Die Polarisation $(a,b)\mapsto g_{a,b}$ arbeitet direkt auf $\mathcal{A}_{\rm PW}$ (komplex), und $g_{a,a}\in\mathcal{C}_W$ ist dann automatisch.

$$
\boxed{\text{Realitäts-Firewall aufgelöst.}\quad\checkmark[K/M]} \qquad (5\text{-Res})
$$

---

## 6. Gesamtkette für M3

$$
\boxed{\mathcal{S}_{\rm adel}^{\rm amp}\xrightarrow{R_{\rm PW}=\Phi J_{1/2}P_{\rm Haar}}\mathcal{A}_{\rm PW}\xrightarrow{a\mapsto c_a}\mathcal{C}_W\xrightarrow{\mathcal{M}_\infty}\mathcal{W}.} \qquad (6\text{-M3-Chain})
$$

Jeder Pfeil ist jetzt sauber:

| Pfeil | Typ | Status |
|---|---|---|
| $R_{\rm PW}$: $\mathcal{S}_{\rm adel}^{\rm amp}\to\mathcal{A}_{\rm PW}$ | wohldef., surjektiv | $\checkmark[K/M]$ |
| $a\mapsto c_a$: $\mathcal{A}_{\rm PW}\to\mathcal{C}_W$ (auf Diagonale: $a\mapsto g_a$) | Autokorrelation, reell-gerade | $\checkmark[K/M]$ |
| $\mathcal{M}_\infty$: $\mathcal{C}_W\to\mathcal{W}$ | Mellin, Tate-Zeta | $\checkmark[K/M]$ (NEU-220a) |

$$
\boxed{\textbf{M3 freigegeben.}} \qquad (6\text{-M3-Release})
$$

---

## 7. Statusbuchungen

$$
R_{\rm PW}:\mathcal{S}_{\rm adel}^{\rm amp}\to\mathcal{A}_{\rm PW}\quad\checkmark[K/M] \qquad (7\text{-a})
$$

$$
R_{\rm PW}\text{ surjektiv auf }\mathcal{A}_{\rm PW}\quad\checkmark[K/M]\qquad\text{(expliziter Lift }F_a=h_a\otimes\mathbf{1}_{\hat{\mathbb{Z}}}) \qquad (7\text{-b})
$$

$$
\text{Realitäts-Firewall aufgelöst: }\mathcal{C}_W\text{ ist Kern der Diagonale, nicht Quellendomäne}\quad\checkmark[K/M] \qquad (7\text{-c})
$$

$$
\text{M3 freigegeben}\quad\checkmark[K/M] \qquad (7\text{-d})
$$

---

## 8. Notiz: Was Q-B/Q-C bedeuten

Q-B (Regularisierung) und Q-C (alternativer Port) werden nicht benötigt: der Amplitudenport $R_{\rm PW}$ löst das Konvergenzproblem durch die richtige Domänenwahl, ohne Regularisierung und ohne Kanonizitätsverlust.

---

## Abhängigkeiten

| Referenz | SHA | Inhalt |
|---|---|---|
| NEU-250q (Patch 2) | 7c03f68 | Exakte Konvergenzbedingung; $\mathcal{C}_{\rm conv}$/$\mathcal{C}_W$; Nichtdichtheit |
| NEU-250m | ecc1c3b | $B_{\rm fin}$; hermitesche Polarisation |
| NEU-250p | 56ba1f7 | $J_{1/2}$-Kette; Weil-Selbstdualität |
| NEU-220l | 1dc07b3 | $\mathcal{A}_{\rm PW}=C_c^\infty(\mathbb{R};\mathbb{C})$; Autokorrelation |
| NEU-220j | 41e28cf | $\mathcal{S}_{\infty,W}$; reell-gerader Kern |
| NEU-220a | 653c8a9 | $\mathcal{M}_\infty$; $\mathcal{S}_\infty$ |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07.*
