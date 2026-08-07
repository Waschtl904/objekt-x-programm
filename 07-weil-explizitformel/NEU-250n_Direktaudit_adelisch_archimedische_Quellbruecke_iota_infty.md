# NEU-250n — Direktaudit der adelisch-archimedischen Quellenbrücke $\iota_\infty$

**Katalog-ID:** NEU-250n  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07  
**Auftrag:** M1 aus NEU-250m gegen NEU-220a/220j auditieren — Typ, Konvergenz, Topologie, Involution, Normalisierung.  
**Gesamtausgang:** $\textbf{N-C}$ — Fehler präzise lokalisiert, minimal korrigierter Kandidat formuliert.  
**Vorgänger:** NEU-250m (M1 $?[O]$), NEU-220a (SHA 7964e36), NEU-220j (SHA 78165f9), NEU-220l, NEU-250h

---

## 0. Gesamtentscheidung

$$
\boxed{\text{Ausgang N-C.}} \qquad (0)
$$

Die in NEU-250m vorgeschlagene Abbildung
$$
\iota_\infty: \mathcal{S}_{\rm adel}\longrightarrow\mathcal{G}_W,
\qquad f\longmapsto\left[s\mapsto\int_0^\infty f_\infty(x)\,x^{s-\frac12}\,d^\times x\right]
$$
ist in dieser Form nicht typkorrekt konstruiert. Die Zentrierung $s-\tfrac12$ ist richtig; falsch bzw.
unscharfgesetzt sind Quelle, Extraktion $f\mapsto f_\infty$, Zielraumbezeichnung und Konvergenzbehauptung.

Die globale Brücke zerfällt sauber in zwei Teilprobleme:
$$
\boxed{\mathcal{S}_{\rm adel}\xrightarrow{\;r_{\infty,W}\;}\mathcal{S}_{\infty,W}\xrightarrow{\;\iota_\infty^{\rm loc}\;}\mathcal{W}.} \qquad (0\text{-DAG})
$$
Der zweite Pfeil ist vollständig typisiert ($\checkmark[K/M]$).
Der erste Pfeil ist die offene Forschungsfrage ($?[O]$).

---

## 1. Erster Quellenfehler: $\mathcal{S}_{\rm adel}$ ist kein konstruierter topologischer Raum

NEU-245b verwendet $\mathcal{S}_{\rm adel}$ als **Architekturbezeichnung** für einen noch zu konstruierenden gemeinsamen Quellenraum; eine vollständige topologische Definition $\mathcal{S}_{\rm adel}:=\mathcal{S}(\mathbb{A}_\mathbb{Q})$ wird dort nicht gegeben. NEU-245c führt die Konstruktion mit $?[O]$ als offene Aufgabe.

NEU-250k hat daraus eine bereits typisierte Quelle gemacht und auf NEU-245c als Nachweis verwiesen. Diese Rückreferenz trägt den stärkeren Befund nicht.

$$
\boxed{\mathcal{S}_{\rm adel}\text{ ist bislang Architekturplatzhalter, kein fertig konstruierter topologischer Quellenraum.}} \qquad (1)
$$

**Statuskorrektur NEU-250k K1:** Buchung „Existenz und Typ von $\mathcal{S}_{\rm adel}$: $\checkmark[M]$" wird auf $?[O]$ zurückgestuft. Die Architekturvorgabe selbst bleibt.

---

## 2. Zweiter Quellenfehler: NEU-220j definiert $\mathcal{W}$, nicht $\mathcal{G}_W$

NEU-220j definiert:

$$
\boxed{\mathcal{W}:=\{F_h: g\in C_c^\infty(\mathbb{R}),\,g\text{ reell und gerade}\},
\quad F_h(s):=h\!\left(\tfrac{s-\tfrac12}{i}\right),\quad h(z):=\int_{\mathbb{R}}g(u)e^{izu}\,du.} \qquad (2)
$$

Wegen des kompakten Trägers von $g$ sind $h$ und $F_h$ **ganz** (Paley-Wiener), nicht bloß auf einem Streifen holomorph. $\mathcal{W}$ trägt in NEU-220j **keine explizite Topologie**. Damit:
- $\mathcal{G}_W$ und $\mathcal{W}$ sind in NEU-250m nicht durch eine Definition identifiziert.
- Aussagen wie „$\iota_\infty$ stetig" oder „$\overline{\operatorname{ran}\iota_\infty}=\mathcal{W}$" sind nicht vollständig typisiert.

**Notwendige Ergänzung in NEU-220j:** Grundkörper und Topologie von $\mathcal{W}$ explizit festlegen.

---

## 3. Die autoritative archimedische Quelle: $\mathcal{S}_\infty$ aus NEU-220a

NEU-220a (SHA 7964e36) liefert:

$$
\boxed{\mathcal{S}_\infty:=\left\{f:\mathbb{R}_+^\times\to\mathbb{C}:\,y\mapsto f(e^y)\in\mathcal{S}(\mathbb{R})\right\},\quad
\Phi f(y):=f(e^y),\quad\Phi:\mathcal{S}_\infty\overset{\sim}{\longrightarrow}\mathcal{S}(\mathbb{R}).} \qquad (3)
$$

Involution (NEU-220a \S1):
$$
f^\sharp(x):=\overline{f(x^{-1})}. \qquad (3\text{-Inv})
$$

Mellin-Port (autoritativ, PD-2):
$$
\boxed{\mathcal{M}_\infty f(t):=\int_0^\infty f(x)\,x^{it}\,\frac{dx}{x}.} \qquad (3\text{-Mellin})
$$

Spektralverkettung (NEU-220b):
$$
\mathcal{S}_\infty\xrightarrow{\mathcal{M}_\infty}\mathcal{S}(\mathbb{R})\xrightarrow{T_\Gamma^{\rm raw}}\mathbb{C}. \qquad (3\text{-Chain})
$$

Das ist bereits eine typkorrekte archimedische Verbindung zum $W_\infty$-/Gamma-Funktional.

---

## 4. Normierungskorrektur in NEU-220a

NEU-220a \S2 schreibt gleichzeitig $\mathcal{M}_\infty f(t)=\int_0^\infty f(x)\,x^{it}\,dx/x$ und $\mathcal{M}_\infty f=\widehat{\Phi f}\cdot 2\pi$ (mit $\hat{g}(t)=\int g(y)e^{ity}\,dy$).

Nachrechnen durch Substitution $x=e^y$:
$$
\mathcal{M}_\infty f(t)=\int_{\mathbb{R}}(\Phi f)(y)\,e^{ity}\,dy=\widehat{\Phi f}(t).
$$

$$
\boxed{\text{Korrektur NEU-220a: }\mathcal{M}_\infty f=\widehat{\Phi f}\text{ (kein }2\pi\text{-Faktor) unter der Konvention }\hat{g}(t)=\int g(y)e^{ity}\,dy.} \qquad (4\text{-Fix})
$$

Dieser Normierungskonflikt ist vor allen weiteren Normalisierungsargumenten zu bereinigen.

---

## 5. Scheitern der holomorphen Mellinabbildung auf ganz $\mathcal{S}_\infty$

Für $f\in\mathcal{S}_\infty$ ist der NEU-250m-Kandidat
$$
M_f(s):=\int_0^\infty f(x)\,x^{s-\frac12}\,d^\times x
=\int_{\mathbb{R}}(\Phi f)(y)\,e^{(s-\frac12)y}\,dy.
$$

Auf der kritischen Geraden $s=\tfrac12+it$:
$$
\boxed{M_f\!\left(\tfrac12+it\right)=\mathcal{M}_\infty f(t).} \qquad (5\text{-CL})
$$

**Die Zentrierung ist richtig.** Für $\Re s\neq\tfrac12$ tritt der exponentielle Faktor $e^{(\Re s-\frac12)y}$ auf. Ein allgemeines $\Phi f\in\mathcal{S}(\mathbb{R})$ hat polynomialen, nicht exponentiellen Abfall. Damit konvergiert das Integral im Allgemeinen **in keinem offenen Streifen** um die kritische Gerade.

$$
\boxed{\mathcal{S}_\infty\longrightarrow\{\text{holomorphe Funktionen in einem Streifen}\}\text{ ist durch diese Formel nicht definiert.}} \qquad (5\text{-NoGo})
$$

---

## 6. Minimal korrigierter lokaler Kandidat

$$
\boxed{\mathcal{S}_{\infty,W}:=\Phi^{-1}\!\left(C_c^\infty(\mathbb{R};\mathbb{R})_{\rm even}\right)
=\left\{f\in\mathcal{S}_\infty:\Phi f\in C_c^\infty(\mathbb{R};\mathbb{R}),\,\Phi f\text{ gerade}\right\}.} \qquad (6\text{-Src})
$$

Für $f\in\mathcal{S}_{\infty,W}$ ist
$$
\boxed{\iota_\infty^{\rm loc}(f)(s):=\int_0^\infty f(x)\,x^{s-\frac12}\,d^\times x} \qquad (6\text{-Map})
$$
für alle $s\in\mathbb{C}$ wohldefiniert und **ganz**.

**Identität mit NEU-220j:** Setze $g:=\Phi f$. Dann:
$$
\iota_\infty^{\rm loc}(f)(s)
=\int_{\mathbb{R}}g(u)\,e^{(s-\frac12)u}\,du
=h\!\left(\frac{s-\tfrac12}{i}\right)=F_h(s).
$$

$$
\boxed{\iota_\infty^{\rm loc}(f)=F_h.} \qquad (6\text{-Id})
$$

Das ist eine Identität, keine Analogie. Der korrigierte lokale Port reproduziert wortwörtlich den NEU-220j-Kern.

$$
\boxed{\mathcal{S}_{\infty,W}\xrightarrow{\;\iota_\infty^{\rm loc}\;}\mathcal{W}} \quad\checkmark[K/M] \qquad (6\text{-Arrow})
$$

---

## 7. Involution: korrigierter Port ist kompatibel

Für $f\in\mathcal{S}_{\infty,W}$ gilt allgemein:
$$
\iota_\infty^{\rm loc}(f^\sharp)(s)=\overline{\iota_\infty^{\rm loc}(f)(1-\bar{s})}. \qquad (7\text{-Gen})
$$

Für die reell-gerade Unterklasse $\mathcal{S}_{\infty,W}$ gilt $f^\sharp=f$, also:
$$
\boxed{\iota_\infty^{\rm loc}(f)(s)=\overline{\iota_\infty^{\rm loc}(f)(1-\bar{s})},} \qquad (7\text{-Sym})
$$
genau die Weil-Symmetriestruktur $F_h(1-s)=F_h(s)$. Der lokale Kandidat ist durch die vorhandenen Konventionen praktisch erzwungen.

---

## 8. Der eigentliche adelische Typfehler: $f_\infty$ existiert nicht kanonisch

Selbst mit $\mathcal{S}_{\rm adel}:=\mathcal{S}(\mathbb{A}_\mathbb{Q})$ hat ein allgemeines $f\in\mathcal{S}(\mathbb{A}_\mathbb{Q})$ **keine kanonisch ausgezeichnete Tensorzerlegung** $f=f_\infty\otimes f_{\rm fin}$; diese existiert nur bei reinen Tensoren.

Die erzwungene Zerlegung der Brücke:

$$
\boxed{\mathcal{S}_{\rm adel}
\xrightarrow{\;r_{\infty,W}\;}
\mathcal{S}_{\infty,W}
\xrightarrow{\;\iota_\infty^{\rm loc}\;}
\mathcal{W}.} \qquad (8\text{-Split})
$$

Zweiter Pfeil: $\checkmark[K/M]$ (dieses Audit).  
Erster Pfeil: $?[O]$ — **NEU-250o**.

Ein Kandidat für $r_{\infty,W}$: Paarung des endlichen adelischen Anteils mit einem ausgezeichneten Vektor $\phi_{\rm fin}^0\in\mathcal{S}(\mathbb{A}_{\mathbb{Q},\rm fin})$,
$$
r_{\infty,W}(f):=\left[x_\infty\mapsto\int_{\mathbb{A}_{\mathbb{Q},\rm fin}}f(x_\infty,x_{\rm fin})\,\phi_{\rm fin}^0(x_{\rm fin})\,dx_{\rm fin}\right],
$$
aber Kanonizität und Abbildungseigenschaft nach $\mathcal{S}_{\infty,W}$ sind nicht im Repository vorhanden.

---

## 9. Kompatibilität mit $g_a$ (NEU-220l): strukturell gut, aber quadratisch

NEU-220l setzt $g_a:=\operatorname{Re}(a*a^\sharp)\in C_c^\infty(\mathbb{R};\mathbb{R})$, gerade. Mit $f_a(x):=g_a(\log x)$ gilt $f_a\in\mathcal{S}_{\infty,W}$ und
$$
\iota_\infty^{\rm loc}(f_a)=F_{h_a}\in\mathcal{W}. \qquad (9\text{-Compat})
$$

Positiver M1-Kompatibilitätsbefund. **Aber:** $a\mapsto g_a$ ist quadratisch, nicht linear. Die Abbildung $a\mapsto f_a\mapsto F_{h_a}$ ist noch keine lineare Quellenabbildung $\mathcal{T}:\mathcal{S}_{\rm adel}\to\mathcal{K}_X$ — das ist M3/Polarisation und wird hier nicht weiter verfolgt.

---

## 10. Auditmatrix

| Prüfpunkt | Befund |
|---|---|
| $\mathcal{S}_{\rm adel}$ exakt definiert? | Nein — Architekturplatzhalter |
| $\mathcal{S}_{\rm adel}=\mathcal{S}(\mathbb{A}_\mathbb{Q})$ aus NEU-245b/c? | Nein — unbelegte Verschärfung in NEU-250m |
| $\mathcal{G}_W$ exakt in NEU-220j? | Nein — der Raum heißt $\mathcal{W}$ |
| $f\mapsto f_\infty$ für allgemeines adelisches $f$? | Nicht kanonisch |
| Zentrierung $x^{s-1/2}$? | **Richtig** — auf $s=\tfrac12+it$ exakt $\mathcal{M}_\infty f(t)$ |
| Konvergenz auf ganz $\mathcal{S}_\infty$? | Nur auf krit. Geraden gesichert; kein allgem. Streifen |
| Abbildung nach $\mathcal{W}$? | Nur auf $\mathcal{S}_{\infty,W}$ |
| Involution? | $\iota_\infty^{\rm loc}(f^\sharp)(s)=\overline{\iota_\infty^{\rm loc}(f)(1-\bar{s})}$ |
| Stetigkeit $\mathcal{S}_{\rm adel}\to\mathcal{W}$? | Nicht formulierbar — Topologien fehlen |
| Kompatibilität mit $W_\infty$/Gamma? | Ja via $\mathcal{S}_\infty\to\mathcal{S}(\mathbb{R})\to\mathbb{C}$ (NEU-220b) |
| Kompatibilität mit $g_a$? | Ja über $f_a(x)=g_a(\log x)$; aber $a\mapsto g_a$ quadratisch |
| $2\pi$-Faktor in NEU-220a? | **Normierungskonflikt** — kein $2\pi$ unter der dortigen Fourierkonvention |

---

## 11. Statusbuchungen

$$
[O\text{-}250m/1]:\quad\checkmark[M]_{\rm neg,Quelle} \qquad (11\text{-a})
$$

$$
\iota_\infty:\mathcal{S}_{\rm adel}\to\mathcal{G}_W\text{ in der Form von NEU-250m}:\quad\times[M] \qquad (11\text{-b})
$$

$$
\boxed{\iota_\infty^{\rm loc}:\mathcal{S}_{\infty,W}\to\mathcal{W}\quad\checkmark[K/M]} \qquad (11\text{-c})
$$

$$
r_{\infty,W}:\mathcal{S}_{\rm adel}\to\mathcal{S}_{\infty,W}\quad?[O]\qquad\to\text{NEU-250o} \qquad (11\text{-d})
$$

---

## 12. Notwendige Repo-Korrekturen

1. **NEU-250m \S0/M1:** $f_\infty$ entfernen; $\mathcal{G}_W$ durch $\mathcal{W}$ ersetzen; Identität $\iota_\infty^{\rm loc}(f)=F_h$ eintragen.
2. **NEU-250k K1:** $\mathcal{S}_{\rm adel}$ Existenz/Typ: $\checkmark[M]\to ?[O]$.
3. **NEU-220a \S2:** $2\pi$-Faktor streichen: korrekt $\mathcal{M}_\infty f=\widehat{\Phi f}$.
4. **NEU-220j:** Topologie von $\mathcal{W}$ explizit festlegen.

---

## 13. Nächster atomarer Schritt

$$
\boxed{\text{NEU-250o — Konstruktion des adelisch-archimedischen Restriktionsports }r_{\infty,W}:\mathcal{S}_{\rm adel}\to\mathcal{S}_{\infty,W}.}
$$

Auftrag ausschließlich: $\mathcal{S}_{\rm adel}$ samt Topologie definieren oder als offen buchen; Kanonizität eines Paarungsvektors $\phi_{\rm fin}^0$ prüfen; Abbildungseigenschaft nach $\mathcal{S}_{\infty,W}$ (reell-gerade, log-kompakt getragen) nachweisen. Erst dann ist M1 geschlossen und M3 freigeschaltet.

---

## Abhängigkeiten

| Referenz | SHA | Inhalt |
|---|---|---|
| NEU-220a | 7964e36 | $\mathcal{S}_\infty$, $\mathcal{M}_\infty$, Involution, Normierungskorrektur |
| NEU-220j | 78165f9 | $\mathcal{W}$-Raum, $F_h$, Konturtransport |
| NEU-220b | — | $T_\Gamma^{\rm raw}$, Spektralverkettung |
| NEU-220l | 1dc07b3 | Weil-Quadratik, $g_a$, Autokorrelation |
| NEU-245b | 79ecf25 | $\mathcal{S}_{\rm adel}$ als Architekturvorgabe |
| NEU-245c | 1ef32ab | M3 $?[O]$: gemeinsame adelische Quelle offen |
| NEU-250h | 0abda0b | $g_a$-Struktur im primitiven Weilkanal |
| NEU-250k | dbd892a | K1 zurückgestuft; K3-Firewall bleibt |
| NEU-250m | ce1a7af | M1 $\times[M]$; M2 $\checkmark[M]$; M3/M4 $?[O]$ |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07.*
