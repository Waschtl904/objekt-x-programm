# NEU-254 — M4-A Direktaudit: Drei positive Hintergrundkandidaten

**Katalog-ID:** NEU-254  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07 (Patch: 2026-08-07)  
**Auftrag:** M4-A-Direktaudit — Vergleich von NEU-220e, NEU-220w, NEU-221 als Kandidaten für ein kanonisches positives Hintergrundskalarprodukt $\langle\cdot,\cdot\rangle_0$ auf $\mathcal{A}_{\rm PW}$ mit $B_W(a,b)=\langle a,A_Xb\rangle_0$.  
**Patch:** $R_{\rm PW}^{-1}$ $\times[M]$ (nicht definiert: $R_{\rm PW}$ surjektiv, nicht injektiv, großer Kern); kanonischer Rechtsinverser $S_{\rm PW}$ mit $R_{\rm PW}S_{\rm PW}=I$ eingeführt; Transport-Ergebnis $\langle S_{\rm PW}a,S_{\rm PW}b\rangle_{\rm Haar}=\langle a,b\rangle_{L^2(\mathbb{R},du)}$ vorläufig gebucht; Haar-Transport-Sektion überarbeitet.  
**Vorl. Status:** Rollenklassifikation $\checkmark[K/M]$; $H_0=L^2(\mathbb{R},du)$ vorläufig $?[O\to]$; Beschränktheit/Abschließbarkeit → NEU-255.  
**Vorgänger:** NEU-253 M4 (Patch), NEU-252 M3 (Patch), NEU-220e, NEU-220w, NEU-221

---

## 0. Ausgangslage

M4-A fragt (NEU-253 §3):
$$
\boxed{\text{Existiert aus der adelischen/arithmetischen Struktur kanonisch ein positives }\langle\cdot,\cdot\rangle_0\text{ mit }B_W(a,b)=\langle a,A_Xb\rangle_0\,?} \qquad (0\text{-Goal})
$$

Normierungs-Firewall (NEU-221 §0):
$$
\boxed{\mathcal{N}_X,\tau_X,T_X\text{ müssen quellseitig fixiert sein; kein Fitten auf }\mu_0,\mu_1.} \qquad (0\text{-Fire})
$$

---

## 1. Kandidat I: NEU-220e — Semifinite Spur

**Was NEU-220e liefert:**
$$
\mathcal{N}_\infty=L^\infty(\mathbb{R},dt),\qquad\tau_\infty(M_a)=\int a(t)\,dt,\qquad\Lambda_\Gamma(h)=\frac{1}{2\pi}\tau_\infty(M_{\gamma_\infty h}).
$$

$\tau_\infty$ realisiert nur den **Gamma-Block** $B_\Gamma$; die vollständige Form $B_W=B_{\rm pole}+B_\Gamma+B_{\rm fin}$ wird nicht getragen. Kein $\langle a,b\rangle_0$ auf $\mathcal{A}_{\rm PW}$ aus $\tau_\infty$ allein.

$$
\boxed{\text{NEU-220e: archimedischer Baustein; kein vollständiges M4-A-}\langle\cdot,\cdot\rangle_0.}\quad\checkmark[K/M] \qquad (1\text{-Verdict})
$$

| Kriterium | NEU-220e |
|---|---|
| RH-frei positiv? | $\checkmark$ (lokal, $B_\Gamma$) |
| Volles $B_W$? | $\times$ (nur $B_\Gamma$) |
| Kanonisch? | $\checkmark$ teilweise |
| Rolle | Archimedischer Baustein |

---

## 2. Kandidat II: NEU-220w — Moment-GNS

**Was NEU-220w liefert:**
$$
\mathcal{H}_\Xi^{\rm mom},\qquad J_\Xi,\qquad M_\Xi(w)=\langle\Omega_\Xi,(I-wJ_\Xi)^{-1}\Omega_\Xi\rangle.
$$

**RH-Problem:** Die benötigte Positivität $\mathcal{L}_\Xi(p^*p)\ge0$, $\mathcal{L}_\Xi(xp^*p)\ge0$ ist laut NEU-220w RH-äquivalent.
$$
\langle p,q\rangle_0:=\mathcal{L}_\Xi(q^*p)\quad\times[M]\text{ als RH-freie Konstruktionsquelle.} \qquad (2\text{-Err})
$$

**Rolle:** NEU-220w ist das Ziel- und Kontrollmodell: Was M4-A konstruiert, muss am Ende denselben Typ wie $\mathcal{H}_\Xi^{\rm mom}$ reproduzieren.

$$
\boxed{\text{NEU-220w: Kontroll-/Zielmodell; Konstruktionsquelle }\times[M]\text{ (RH-äquiv.)}}\quad\checkmark[K/M] \qquad (2\text{-Verdict})
$$

| Kriterium | NEU-220w |
|---|---|
| RH-frei positiv? | $\times$ (RH-äquivalent) |
| Volles $B_W$? | indirekt $\checkmark$ |
| Kanonisch? | $\checkmark$ nach Momentdaten |
| Rolle | Kontroll-/Zielmodell |

---

## 3. Kandidat III: NEU-221 — Adelische Momentquelle

**Strukturprinzip (übernommen):** $T_X=B_X^{-1}\ge0$; Momente $\mu_0,\mu_1,\mu_2$ als Frühtests; keine freien Skalierungsparameter. Stärkster Kandidat in NEU-221 war:
$$
\boxed{D_{\rm Spec,N}^{\rm rel}=D_{\rm Jac}\cdot D_{\rm scatt},\quad\text{Euler+Feshbach/Weyl+archimedisch (gemeinsame Determinante, keine direkte Summe)}.} \qquad (3\text{-NEU221})
$$

**Technischer Stand seit NEU-221:**

| Baustein | Status |
|---|---|
| Normierungs-Firewall | $\checkmark$ |
| $T_X=B_X^{-1}$ als Arbeitsvariable | $\checkmark$ |
| $\mu_0,\mu_1,\mu_2$ als Frühtests | $\checkmark$ |
| $D_{\rm scatt,N}$ als Operator | $\times[M]$ (NEU-250l untypisiert) |
| Feshbach/Weyl-Quellregion (Richtung) | $\checkmark$ Re-Audit nötig |
| Archimedische Kopplung separat | $\times$ (muss integriert, nicht direkte Summe) |

$$
\boxed{\text{NEU-221: konzeptionell stärkster Pfad; technisch Re-Audit gegen NEU-250ff nötig.}}\quad\checkmark[K/M] \qquad (3\text{-Verdict})
$$

| Kriterium | NEU-221 |
|---|---|
| RH-frei positiv? | Ziel $\checkmark$; noch nicht konstruiert |
| Volles $B_W$? | Ziel $\checkmark$ |
| Kanonisch? | Ziel $\checkmark$; teilweise offen |
| Rolle | Hauptpfad, Re-Audit fällig |

---

## 4. Vergleichsmatrix

| Kandidat | RH-frei positiv? | Volles $B_W$? | Kanonisch? | Heutiger Status |
|---|---|---|---|---|
| NEU-220e semifinite Spur | $\checkmark$ ($B_\Gamma$) | $\times$ | $\checkmark$ teilw. | Archimedischer Baustein |
| NEU-220w Moment-GNS | $\times$ (RH-äquiv.) | indirekt $\checkmark$ | $\checkmark$ nach Momente | Kontroll-/Zielmodell |
| NEU-221 adelische Quelle | Ziel $\checkmark$ | Ziel $\checkmark$ | Ziel $\checkmark$ | Hauptpfad, Re-Audit nötig |

---

## 5. Haar-Transport: Reparatur und Befund

### 5.1 Typfehler $R_{\rm PW}^{-1}$ $\times[M]$

Die erste Fassung schrieb:
$$
\langle a,b\rangle_0:=\langle R_{\rm PW}^{-1}a,R_{\rm PW}^{-1}b\rangle_{\rm Haar}\quad\times[M]. \qquad (5\text{-OldErr})
$$

NEU-250r beweist $R_{\rm PW}:\mathcal{S}_{\rm adel}^{\rm amp}\twoheadrightarrow\mathcal{A}_{\rm PW}$ als **surjektiv**, nicht injektiv. $R_{\rm PW}$ hat einen großen Kern; für ein $a\in\mathcal{A}_{\rm PW}$ gibt es viele adelische Urbilder. Das Symbol $R_{\rm PW}^{-1}a$ ist ohne weitere Wahl nicht eindeutig.

### 5.2 Kanonischer Lift $S_{\rm PW}$ (NEU-250r)

Aus NEU-250r existiert der explizite kanonische Rechtsinverse:
$$
\boxed{S_{\rm PW}a=h_a\otimes\mathbf{1}_{\widehat{\mathbb{Z}}},\qquad h_a(x)=\begin{cases}x^{-1/2}a(\log x),&x>0,\\0,&x\le0,\end{cases}\qquad R_{\rm PW}S_{\rm PW}=I.} \qquad (5\text{-Lift})
$$

### 5.3 Transport-Satz

Mit $\operatorname{vol}(\widehat{\mathbb{Z}})=1$:
$$
\langle S_{\rm PW}a,S_{\rm PW}b\rangle_{L^2(\mathbb{A})}=\int_0^\infty x^{-1}\overline{a(\log x)}b(\log x)\,dx=\int_{\mathbb{R}}\overline{a(u)}b(u)\,du.
$$
$$
\boxed{\langle S_{\rm PW}a,S_{\rm PW}b\rangle_{\rm Haar}=\langle a,b\rangle_{L^2(\mathbb{R},du)}.} \qquad (5\text{-Transport})
$$

### 5.4 Hilbertraumformulierung

Der Haar-Port auf Hilbertraumebene:
$$
\overline{R}_{\rm PW}:L^2(\mathbb{A}_{\mathbb{Q}})\longrightarrow L^2(\mathbb{R},du):
$$
Endliche Variablen mit $\mathbf{1}_{\widehat{\mathbb{Z}}}$ paaren, auf $x>0$ beschränken, dann $J_{1/2}$ anwenden. $J_{1/2}:L^2(\mathbb{R}_+,dx)\to L^2(\mathbb{R},du)$ ist **unitär**:
$$
\int_{\mathbb{R}}|e^{u/2}h(e^u)|^2\,du=\int_0^\infty|h(x)|^2\,dx. \qquad (5\text{-Unit})
$$

$S_{\rm PW}$ ist der adjungierte isometrische Lift; $\overline{R}_{\rm PW}S_{\rm PW}=I$. Damit:
$$
\boxed{L^2(\mathbb{A}_{\mathbb{Q}})/\ker\overline{R}_{\rm PW}\cong L^2(\mathbb{R},du).} \qquad (5\text{-Quot})
$$

### 5.5 Strategische Einordnung

Der kanonische Haar-Majorant ist nach Transport schlicht $L^2(\mathbb{R},du)$. Die Primzahlarithmetik steckt nach dem Quotienten nicht mehr sichtbar in $H_0$, sondern muss vollständig im Realisierungsoperator $A_X$ bzw. seiner Domäne und Spektralstruktur sitzen. Das ist **nicht** ein Problem, sondern ein plausibler Befund: einfacher Hilbertraum, hochgradig arithmetischer Operator.

Was noch nicht behauptet wird:
$$
\boxed{\text{"Adelische positive Geometrie gefunden" — noch nicht. Beschränktheit/Abschließbarkeit von }A_X\text{ offen.}} \qquad (5\text{-Caveat})
$$

### 5.6 Status

$$
R_{\rm PW}^{-1}\text{ als Konstruktion}\quad\times[M]\;(\text{nicht definiert; }R_{\rm PW}\text{ surjektiv, großer Kern}) \qquad (5\text{-a})
$$
$$
\langle S_{\rm PW}a,S_{\rm PW}b\rangle_{\rm Haar}=\langle a,b\rangle_{L^2(\mathbb{R},du)}\quad\checkmark[K/M] \qquad (5\text{-b})
$$
$$
L^2(\mathbb{A}_{\mathbb{Q}})/\ker\overline{R}_{\rm PW}\cong L^2(\mathbb{R},du)\quad\checkmark[K/M] \qquad (5\text{-c})
$$
$$
H_0=L^2(\mathbb{R},du)\text{ als M4-A-Majorante vorläufig }?[O\to]\text{ (Vollbeweis in NEU-255)} \qquad (5\text{-d})
$$

---

## 6. M4-A Hauptpfad

$$
\boxed{\text{Hauptpfad M4-A: NEU-221-Strukturprinzip + Haar-Transport + Koisometriebeweis (NEU-255).}} \qquad (6\text{-Main})
$$

1. NEU-221-Normierungs-Firewall, $T_X=B_X^{-1}\ge0$, Momente $\mu_0,\mu_1,\mu_2$ übernehmen.
2. Koisometriebeweis $\overline{R}_{\rm PW}$ vollständig in NEU-255.
3. $\langle a,b\rangle_0=\langle a,b\rangle_{L^2(\mathbb{R})}$ kanonisch buchen.
4. $|B_W(a,b)|\le C\|a\|_2\|b\|_2$ testen (Beschränktheit erwartet zu scheitern).
5. Falls Scheitern: Abschließbarkeits-/Selbstadjungiertheitskette (NEU-253 §3-Chain).
6. NEU-220w als Kontrollmodell am Ende.

---

## 7. Statusbuchungen

$$\text{NEU-220e: Gamma-Baustein, kein vollständiges }\langle\cdot,\cdot\rangle_0\quad\checkmark[K/M] \qquad (7\text{-a})$$
$$\text{NEU-220w: Zielmodell; Konstruktionsquelle }\times[M]\quad\checkmark[K/M] \qquad (7\text{-b})$$
$$\text{NEU-221: stärkster Pfad; }D_{\rm scatt,N}\;\times[M]\text{; Firewall }\checkmark\quad\checkmark[K/M] \qquad (7\text{-c})$$
$$R_{\rm PW}^{-1}\text{ als Konstruktion}\quad\times[M] \qquad (7\text{-d})$$
$$\langle S_{\rm PW}a,S_{\rm PW}b\rangle_{\rm Haar}=\langle a,b\rangle_{L^2(\mathbb{R})}\quad\checkmark[K/M] \qquad (7\text{-e})$$
$$L^2(\mathbb{A})/\ker\overline{R}_{\rm PW}\cong L^2(\mathbb{R})\quad\checkmark[K/M] \qquad (7\text{-f})$$
$$\text{M4-A Hauptpfad identifiziert}\quad\checkmark[K/M] \qquad (7\text{-g})$$
$$\text{Beschränktheit/Abschließbarkeit }A_X\quad?[O]\text{ → NEU-255} \qquad (7\text{-h})$$

---

## 8. Abhängigkeiten

| Referenz | SHA | Inhalt |
|---|---|---|
| NEU-253 | a95d3b5 | M4 Rahmen; Rad; Signatur-Firewall; M4-A Zwei-Fälle |
| NEU-252 (Patch) | 4ee78ed | $B_W$ hermitesch; $B_W^{\rm adel}$ |
| NEU-220e | 9a1f3c2 | Semifinite Spur $\tau_\infty$; $\Lambda_\Gamma$ |
| NEU-220w | f1bce0f | Moment-GNS; $\mathcal{H}_\Xi^{\rm mom}$; Kontrollmodell |
| NEU-221 | f678057 | Normierungs-Firewall; $T_X=B_X^{-1}$; Feshbach-Quellregion |
| NEU-250r (Patch) | bd1c0ab | $S_{\rm PW}$; $R_{\rm PW}S_{\rm PW}=I$; $\mathcal{S}_{\rm adel}^{\rm amp}$ |
| NEU-220l | 1dc07b3 | $B_W\ge0\Leftrightarrow$ RH |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07. Patch 2026-08-07: $R_{\rm PW}^{-1}$ $\times[M]$ → $S_{\rm PW}$; Transport-Satz $\checkmark$; Haar-Koisometrie vorläufig $\checkmark$.*
