# NEU-220h — PD-5a1: Endlicher Weil-Port aus NEU-28

**Knoten:** `[O-220-1-PD5a1-finite-port]`  
**Stand:** 25. Juli 2026  
**Vorgänger:** NEU-220g (PD-5a-Struktur), NEU-28, NEU-29 (Primärdateien)  
**Ziel:** Vier Audit-Unterknoten aus Primärdateien bearbeiten; Entscheidungsgabel A/B/C ausgeben.

---

## 0. Gesamtbefund: Fall B

Der Audit ergibt eindeutig **Fall B**.

NEU-28 liefert die meromorphe Funktion $\lambda_\mathrm{mod}(s) = C_L/\zeta(s)$ und den
Abgeleiteten-Term $R_X^\xi(s) = C_L\cdot K_\xi(s)$ als meromorphe Funktion in $s$.
NEU-29 realisiert daraus über den Doppelresolvent-Kalkül eine Spurformel
$\sum_\rho m_\rho f(\rho)$.

**Weder NEU-28 noch NEU-29 konstruieren $\Lambda_\mathrm{fin}$ als typisiertes Weil-Funktional**
$\Lambda_\mathrm{fin}:\mathcal S_\mathrm{fin}^\mathrm{herm}\to\mathbb R$
mit festem $dt/(2\pi)$-Maß auf der kritischen Linie.

Die Entscheidungsgabel:

$$
\boxed{[O\text{-}220\text{-}1\text{-PD5a1-finite-port}]\quad\checkmark[M]_\mathrm{part}
\quad\text{(NEU-28 liefert nur }1/\zeta\text{, nicht typisiertes Weil-Funktional).}}
$$

Neuer offener Knoten:

$$
\boxed{[O\text{-}220\text{-}1\text{-PD5a1-logderivative-trace}]\quad?[O].}
$$

---

## 1. PD-5a1a — Exakter Eingabetyp aus NEU-28

### 1.1 Was NEU-28 tatsächlich definiert

Aus NEU-28 §3.2 (Primärtext):

$$
\mathrm{Tr}_{\varphi_s}(a\cdot\Delta_s^{-1})
= \sum_n n^{-s}/\zeta(s)\cdot n^s\cdot\langle e_{0,n},a\cdot e_{0,n}\rangle
= \frac{1}{\zeta(s)}\cdot\mathrm{Tr}_\mathrm{Hilbert}(a|_\mathrm{diag}).
$$

Für $a = L_3$:

$$
\lambda_\mathrm{mod}(s) = \frac{C_L}{\zeta(s)},
\qquad C_L = \mathrm{Tr}_\mathrm{Hilbert}(L_3|_\mathrm{diag})\in\mathbb C^\times.
$$

**Die Testvariable ist $s\in\mathbb C$, nicht eine Testfunktion $h$ oder $f_\mathrm{fin}$.**

$\lambda_\mathrm{mod}(s)$ ist eine skalare meromorphe Funktion auf $\{\Re(s)>1\}$,
analytisch fortgesetzt auf $\mathbb C$. Die Eingabe ist eine komplexe Zahl $s$,
kein Element eines Testfunktionsraums.

### 1.2 Der Eingabetyp in der vollständigen Kette

Die Abbildungskette aus NEU-28/29 lautet:

$$
\underbrace{s\in\mathbb C}_{\text{Eingabe}}
\xrightarrow{\lambda_\mathrm{mod}(s)=C_L/\zeta(s)}
\underbrace{\text{meromorphe Funktion}}_{\text{Wert}}
\xrightarrow{R_X^\xi = -\partial_s(\cdot)}
\underbrace{K_\xi(s) = \sum_\rho m_\rho/(s-\rho)^2}_{\text{Spektralfunktion}}
\xrightarrow{\text{Cauchy (NEU-29)}}
\underbrace{\sum_\rho m_\rho f(\rho)}_{\text{Spurwert}}
$$

wobei $f = F'$ aus einer **holomorphen Hilfsfunktion** $F$ (Primitive von $f$) stammt.

**Auditbefund 1a:** Der Eingabetyp von NEU-28 ist $s\in\mathbb C$ (meromorphe
Funktionsvariable), **nicht** ein Weil-Testfunktionselement. Ein Raum $\mathcal S_\mathrm{fin}$
im Sinne eines topologischen Testfunktionsraums ist in NEU-28 nicht errichtet.

$$
\boxed{\text{PD-5a1a}\quad\checkmark[M]_\mathrm{part}.}
$$

Der vollständige Eingabetyp nach Cauchy-Kalkul (NEU-29) ist:
$f$ holomorph auf einer Umgebung der Nullstellen, aus der Testklasse
$\mathcal A_\xi = \{f:\mathbb C\to\mathbb C\text{ hol.}\mid\sum_\rho m_\rho|f(\rho)|<\infty\}$.
Dieser Raum ist jedoch ein globaler holomorpher Funktionenraum, kein
hermitescher $L^2$-artiger Schwartzraum auf $\mathbb R$.

---

## 2. PD-5a1b — Typ von $\Lambda_\mathrm{fin}$

### 2.1 Was in NEU-28 wirklich vorliegt

NEU-28 liefert:

1. **KMS-Spur:** $\lambda_\mathrm{mod}(s) = \mathrm{Tr}_{\varphi_s}(L_3\cdot\Delta_s^{-1})$
   auf dem GNS-Hilbertraum $H_s$ des Zustands $\varphi_s$. Das ist eine
   **KMS-Spurauswertung** bei festem Parameter $s$.

2. **Meromorphe Funktion:** Das Ergebnis $C_L/\zeta(s)$ ist eine skalare
   meromorphe Funktion von $s$.

3. **Cauchy-Spurformel (NEU-29):** 
   $\mathrm{Tr}_\mathrm{Wres}(f(D_X^\mathrm{BC})\cdot L_3^\circ) = \sum_\rho m_\rho f(\rho)$
   für $f\in\mathcal A_\xi$. Das ist eine **Residuensumme**, keine Spurform
   auf einem Testfunktionsraum in Weil-Normierung.

**Was NEU-28/29 nicht liefert:**
Eine Abbildung $\Lambda_\mathrm{fin}:\mathcal S_\mathrm{fin}\to\mathbb C$ in der Form

$$
\Lambda_\mathrm{fin}(h) = \frac1{2\pi}\int_{\mathbb R}\frac{\zeta'}{\zeta}\!\left(\tfrac12+it\right)h(t)\,dt
$$

oder ein äquivalentes semifinites Spurintegral
$\tau_\mathrm{fin}(M_{\zeta'/\zeta}\cdot h(H_\mathrm{fin}))$
ist in den Primärdateien nicht ausgeschrieben.

**Auditbefund 1b:** $\Lambda_\mathrm{fin}$ ist in NEU-28/29 **keine** der vier
kanonischen Typen: weder semifinit typisiert, noch als Weil-Distribution auf
$\mathcal S^\mathrm{herm}(\mathbb R)$ realisiert. Sie ist eine KMS-Spur
bei festem $s$ (Typ III) und ein Cauchy-Residuenfunktional (Typ: meromorph).

$$
\boxed{\text{PD-5a1b}\quad\checkmark[M]_\mathrm{part}.}
$$

---

## 3. PD-5a1c — Übergang von $1/\zeta$ zu $\zeta'/\zeta$: Typisierungsschritt

### 3.1 Was NEU-28 leistet (Primärtext §3.4, §7.2)

NEU-28 liefert den Ableitungsschritt in $s$:

$$
R_X(s) = -\partial_s\lambda_\mathrm{mod}(s) = -\partial_s\frac{C_L}{\zeta(s)} = C_L\cdot\frac{\zeta'(s)}{\zeta(s)^2}.
$$

Und nach Gamma-Korrektur (§7.2, explizit):

$$
R_X^\xi(s) = C_L\cdot K_\xi(s),
\qquad
K_\xi(s) = -\partial_s(\xi'/\xi)(s) = \sum_\rho \frac{m_\rho}{(s-\rho)^2}.
$$

Dieser Schritt ist eine **Ableitung der meromorphen Funktion** in der Variablen $s$,
nicht eine Auswertung auf einer Testfunktion $h(t)$.

### 3.2 Der fehlende Typisierungsschritt

Der benötigte Ausdruck für das endliche Weil-Funktional ist:

$$
\Lambda_\mathrm{fin}(h) = \frac1{2\pi}\int_{\mathbb R}\frac{\zeta'}{\zeta}\!\left(\tfrac12+it\right)h(t)\,dt
\quad\text{(Weil-Zielform)},
$$

oder äquivalent in Primzahlpotenzform:

$$
\Lambda_\mathrm{fin}(h) = \sum_{p^k}\Lambda(p^k)\,\hat h(\log p^k)
\quad\text{(distributionell)},
$$

mit $\hat h(u) = \int_\mathbb R h(t)e^{(1/2+it)u}\,dt$ (Mellin-Fourier auf der kritischen Linie).

Um diesen Ausdruck aus $\lambda_\mathrm{mod}(s) = C_L/\zeta(s)$ zu gewinnen,
bräuchte man einen der folgenden Mechanismen (alle noch nicht ausgeschrieben):

| Mechanismus | Status |
|---|---|
| $-\partial_s\log\lambda_\mathrm{mod}(s)\big|_{s=1/2+it}$ als Randwert | ?[O] |
| $\tau_\mathrm{fin}(M_{\zeta'/\zeta}\cdot h(H_\mathrm{fin}))$ semifinit | ?[O] |
| Mellin-Inversion: $\lambda_\mathrm{mod}\leftrightarrow\Lambda_\mathrm{fin}$ über $\mathcal M_\mathrm{fin}$ | ?[O] |
| Relative Determinante: $\partial_s\log\det_\mathrm{rel}(s)\sim\zeta'/\zeta$ | ?[O] |

**Das ist der zentrale Engpass:** Die algebraisch verfügbare Funktion ist
$1/\zeta(s)$ (ein Spektraldeterminant), das Weil-Funktional braucht $\zeta'/\zeta$
(einen logarithmischen Ableitung). Der Schritt zwischen beiden ist in den
Primärdateien zwar **algebraisch** vollzogen ($-\partial_s C_L/\zeta = C_L\zeta'/\zeta^2$),
aber **nicht als typisierte Abbildungskette** auf einem Testfunktionsraum
$\mathcal S_\mathrm{fin}^\mathrm{herm}\to\mathbb R$ realisiert.

**Auditbefund 1c:** Dies ist der zentrale Typunterschied.

$$
\boxed{[O\text{-}220\text{-}1\text{-PD5a1-logderivative-trace}]\quad?[O].}
$$

$$
\boxed{\text{PD-5a1c}\quad\checkmark[M]_\mathrm{part}.}
$$

### 3.3 Ausgeschriebene typisierte Ableitungskette (Zielform)

Die zu konstruierende Kette lautet:

$$
\mathcal S_\mathrm{fin}^\mathrm{herm}
\xrightarrow{h\mapsto M_{(\zeta'/\zeta)\circ\sigma}}
L^1(\mathcal N_\mathrm{fin},\tau_\mathrm{fin})
\xrightarrow{\tau_\mathrm{fin}}
\mathbb R,
$$

mit $\sigma(t) = \frac12+it$ (Parametrisierung der kritischen Linie) und
$\tau_\mathrm{fin}(M_a) = \frac1{2\pi}\int_\mathbb R a(t)\,dt$.

Das hätte dann exakt die Parallelstruktur zu $\Lambda_\Gamma$ aus PD-4c3:

$$
\mathcal S_{\infty,\mathrm{even}}^{\mathbb R}
\xrightarrow{h\mapsto M_{\gamma_\infty^\mathrm{sym}\cdot h}}
L^1(\mathcal N_\infty,\tau_\infty)
\xrightarrow{\tau_\infty}
\mathbb R.
$$

Die Analogie macht die Konstruktionsaufgabe präzise: $\gamma_\infty^\mathrm{sym}$
entspricht $(-\zeta'/\zeta)|_{1/2+it}$ auf der endlichen Seite.

---

## 4. PD-5a1d — Realität, Involution und Maßnormierung

### 4.1 Realität von $\zeta'/\zeta$ auf der kritischen Linie

Auf $s = \tfrac12+it$ gilt wegen der Schwarz-Reflexion $\zeta(\overline s) = \overline{\zeta(s)}$:

$$
\overline{\frac{\zeta'}{\zeta}\!\left(\tfrac12+it\right)}
= \frac{\overline{\zeta'(\tfrac12+it)}}{\overline{\zeta(\tfrac12+it)}}
= \frac{\zeta'(\tfrac12-it)}{\zeta(\tfrac12-it)}
= \frac{\zeta'}{\zeta}\!\left(\tfrac12-it\right).
$$

Also: Für reelles gerades $h(-t) = h(t)\in\mathbb R$:

$$
\overline{\Lambda_\mathrm{fin}(h)}
= \frac1{2\pi}\int_\mathbb R\overline{\frac{\zeta'}{\zeta}\!\left(\tfrac12+it\right)}h(t)\,dt
= \frac1{2\pi}\int_\mathbb R\frac{\zeta'}{\zeta}\!\left(\tfrac12-it\right)h(t)\,dt
= \frac1{2\pi}\int_\mathbb R\frac{\zeta'}{\zeta}\!\left(\tfrac12+it\right)h(t)\,dt
= \Lambda_\mathrm{fin}(h).
$$

(Im letzten Schritt: Substitution $t\mapsto-t$ und Geradheit von $h$.)

Also ist $\Lambda_\mathrm{fin}(h)\in\mathbb R$ für reelles gerades $h$ —
**falls** der Ausdruck konvergiert (dazu unten).

### 4.2 Konvergenz und Maßnormierung

**Problem:** $\zeta'/\zeta(\tfrac12+it)$ ist für $t\in\mathbb R$ nicht absolut integrierbar.
Die Weil-Formel erfordert einen Regularisierungsschritt:

$$
\Lambda_\mathrm{fin}(h)
= \sum_{p^k}\Lambda(p^k)\hat h(\log p^k)
$$

als regulierte Summe über Primzahlpotenzen, mit Fourier-Mellin-Koeffizient
$\hat h(u) = \int_\mathbb R h(t)e^{(1/2+it)u}\,dt$ für $h\in\mathcal S(\mathbb R)$ reell-gerade.
Diese Summe konvergiert für $h$ mit schnell abfallendem $\hat h$.

Der Zusammenhang mit dem kritischen-Linien-Integral ist formal:

$$
\frac1{2\pi}\int_\mathbb R\frac{\zeta'}{\zeta}\!\left(\tfrac12+it\right)h(t)\,dt
\overset{?}{=} \sum_{p^k}\Lambda(p^k)\hat h(\log p^k)
$$

nur im Sinne der regulierten Auswertung (Konturverschiebung von $\Re(s)=\tfrac12$
nach $\Re(s)>1$), nicht als absolut konvergentes Integral.

**Auditbefund 1d:** Der Vorfaktor $1/(2\pi)$ in $\Lambda_\mathrm{fin}$ ist mit dem
archimedischen $1/(4\pi)$ in $\Lambda_\Gamma$ **nicht automatisch kompatibel**.
Der Faktor $2$ kommt daher, dass $\Lambda_\Gamma$ die symmetrisierte Gamma-Form
$\gamma_\infty^\mathrm{sym} = \gamma_\infty(t)+\gamma_\infty(-t)$ trägt (ein Geradenintegral
über $2\mathrm{Re}(\gamma_\infty)$), während $\Lambda_\mathrm{fin}$ direkt das
Linienintegral trägt. Beide haben als gemeinsamen Nenner $2\pi$, wenn
$\Lambda_\Gamma$ in der Form $\frac1{2\pi}\int\gamma_\infty(t)h(t)\,dt$
(PD-4b, nicht PD-4c3) geschrieben wird.

$$
\boxed{\text{PD-5a1d}\quad\checkmark[M]_\mathrm{part}.}
$$

Der korrekte Übereinstimmungspunkt:

$$
\Lambda_\mathrm{fin}(h) = \frac1{2\pi}\int_\mathbb R\frac{\zeta'}{\zeta}\!\left(\tfrac12+it\right)h(t)\,dt
\quad\text{und}\quad
\Lambda_\Gamma(h) = \frac1{2\pi}\int_\mathbb R\gamma_\infty(t)h(t)\,dt
$$

tragen beide den Vorfaktor $1/(2\pi)$ — aber PD-4c3 hat den Vorfaktor $1/(4\pi)$
wegen der Symmetrisierung. Für reelles gerades $h$ gilt:

$$
\frac1{2\pi}\int\gamma_\infty(t)h(t)\,dt
= \frac1{4\pi}\int\gamma_\infty^\mathrm{sym}(t)h(t)\,dt
\quad\text{(wegen }\gamma_\infty^\mathrm{sym} = \gamma_\infty(t)+\gamma_\infty(-t)\text{ und Geradheit von }h\text{).}
$$

Damit sind beide Vorfaktoren **konsistent**, sofern $h$ reell-gerade ist.

---

## 5. Gesamtbefund und neuer Knoten

### 5.1 Zusammenfassung der vier Unterknoten

| Unterknoten | Befund | Status |
|---|---|---|
| PD-5a1a: Eingabetyp | Testvariable ist $s\in\mathbb C$, kein Weil-Raum | ✓[M]_part |
| PD-5a1b: Typ von $\Lambda_\mathrm{fin}$ | KMS-Spur + Cauchy-Residuum; kein Weil-Funktional | ✓[M]_part |
| PD-5a1c: $1/\zeta\to\zeta'/\zeta$ | Algebraisch vollzogen, nicht typisiert | ✓[M]_part |
| PD-5a1d: Realität und Normierung | Konsistenz bei $1/(2\pi)$ gezeigt; Regularisierung offen | ✓[M]_part |

### 5.2 Der zentrale neue Knoten

**Was konstruiert werden muss:**

$$
\boxed{
[O\text{-}220\text{-}1\text{-PD5a1-logderivative-trace}]\quad?[O].
}
$$

Konkret: Konstruiere einen Operator

$$
H_\mathrm{fin}\text{ auf }L^2(\mathbb R,dt)
\quad\text{mit}\quad
\gamma_\mathrm{fin}(t) := -\frac{\zeta'}{\zeta}\!\left(\tfrac12+it\right)
$$

und eine semifinite Von-Neumann-Algebra
$\mathcal N_\mathrm{fin}\supset M_{\gamma_\mathrm{fin}}$
mit Spur $\tau_\mathrm{fin}(M_a)=\frac1{2\pi}\int_\mathbb R a(t)\,dt$, sodass

$$
\Lambda_\mathrm{fin}(h)
= \frac1{2\pi}\tau_\mathrm{fin}\bigl(M_{\gamma_\mathrm{fin}}\cdot h(H_\mathrm{fin})\bigr)
$$

für reelles gerades $h$. Das wäre die exakte Parallelkonstruktion zu $\Lambda_\Gamma$
aus PD-4b/c3.

**Schlüsselfrage:** Ist $\gamma_\mathrm{fin}(t) = -\zeta'/\zeta(\tfrac12+it)$ im selben
Sinne semifinit-integrierbar wie $\gamma_\infty^\mathrm{sym}$? Das ist nicht
apriorisch klar: $\gamma_\infty^\mathrm{sym}$ wächst logarithmisch (Stirling),
während $\zeta'/\zeta$ auf der kritischen Linie im Mittel logarithmisch wächst,
aber mit Nullstellen-Singularitäten (unter RH durch
$\sum_\rho 1/(\rho-\tfrac12-it)$ beschrieben).

### 5.3 Struktureller Vergleich archimedisch vs. endlich

| Aspekt | Archimedisch ($X_\infty$) | Endlich ($X_\mathrm{fin}$) |
|---|---|---|
| Symbol | $\gamma_\infty^\mathrm{sym}(t)$ | $-\zeta'/\zeta(\tfrac12+it)$ |
| Herkunft | $\log$-Ableitung von $S_\infty$ (unitär) | $\log$-Ableitung von... ? |
| Regularität | $\in L^\infty_\mathrm{loc}$, log. Wachstum | Singularitäten bei $\Im(\rho)$ |
| Spurtyp | $\tau_\infty$-semifinit (PD-4b) | $\tau_\mathrm{fin}$-semifinit: ?[O] |
| Von-Neumann-Alg. | $\mathcal N_\infty = L^\infty(\mathbb R)$ | $\mathcal N_\mathrm{fin}=L^\infty(\mathbb R)$: formal analog |
| Unitärer Streufaktor | $S_\infty=\Gamma_\mathbb R(\tfrac12-it)/\Gamma_\mathbb R(\tfrac12+it)$ | $S_\mathrm{fin}(t) = ?$ |
| Zeitverzögerung | $Q_\infty = M_{\gamma_\infty^\mathrm{sym}}$ | $Q_\mathrm{fin} = M_{\gamma_\mathrm{fin}}$: formal analog |

Die Analogie macht den Konstruktionsweg klar: $S_\mathrm{fin}(t)$ müsste ein
unitärer Operator sein, dessen logarithmische Ableitung $-\zeta'/\zeta(\tfrac12+it)$
erzeugt. Ein naheliegender Kandidat ist ein Euler-Produkt:

$$
S_\mathrm{fin}(t) = \prod_p\frac{1-p^{-(1/2-it)}}{1-p^{-(1/2+it)}}
= \frac{\overline{\zeta(\tfrac12+it)}}{\zeta(\tfrac12+it)}
\cdot(\text{Konvergenzfaktor}),
$$

aber die Konvergenz und Unitarität dieses Produkts auf der kritischen Linie
ist nicht trivial (Nullstellen von $\zeta(\tfrac12+it)$ würden Singularitäten
erzeugen). Das bleibt als Kandidat für `[O-220-1-PD5a1-logderivative-trace]`.

---

## 6. Endliche Objekt-$X_\mathrm{fin}$-Schablone nach NEU-220h

Nach dem Audit kann $X_\mathrm{fin}$ präziser als Ziel-Schablone formuliert werden:

$$
\boxed{
X_\mathrm{fin} = \bigl(L^2(\mathbb R,dt),\,\mathcal N_\mathrm{fin}=L^\infty(\mathbb R),\,
\tau_\mathrm{fin},\,M_{\gamma_\mathrm{fin}},\,\Lambda_\mathrm{fin}\bigr)
}
$$

mit $\gamma_\mathrm{fin}(t) = -\zeta'/\zeta(\tfrac12+it)$ (nach Regularisierung)
und $\Lambda_\mathrm{fin}(h) = \frac1{2\pi}\tau_\mathrm{fin}(M_{\gamma_\mathrm{fin}}h(H_\mathrm{fin}))$.

Das ist eine Schablone, kein konstruiertes Objekt. Die fehlende Konstruktion ist:

$$
\boxed{[O\text{-}220\text{-}1\text{-PD5a1-logderivative-trace}]\quad?[O].}
$$

---

## 7. Konsequenz für $X_\mathrm{weak}$ und PD-5a2

Nach diesem Audit ist die Situation:

- **$X_\infty$ vollständig konstruiert** (NEU-220f, PD-4b/c1–c3)
- **$X_\mathrm{fin}$ als Schablone präzisiert** (NEU-220h)
- **$X_\mathrm{weak} = X_\mathrm{fin}\oplus X_\infty$ bedingt offen**:
  gesperrt bis `[O-220-1-PD5a1-logderivative-trace]` $\geq$ ✓[M]

Sobald die Konstruktion in §5.2 gelingt, kann PD-5a2 sofort
(mit vollständiger Typkorrektur) abgeschlossen werden:

$$
\Lambda_{\mathbb A}^\mathrm{weak}(h) = \Lambda_\mathrm{fin}(h) + \Lambda_\Gamma(h)
= \frac1{2\pi}\tau_\mathrm{fin}(M_{\gamma_\mathrm{fin}}h(H_\mathrm{fin}))
+ \frac1{2\pi}\tau_\infty(M_{\gamma_\infty}h(H_\infty))
$$

für reelles gerades $h\in\mathcal S(\mathbb R)$, mit **identischer Typstruktur** auf
beiden Seiten.

$$
\boxed{\text{PD-5a2: freigegeben sobald PD-5a1-logderivative-trace}\geq\checkmark[M].}
$$

---

## 8. Aktualisierter DAG-Stand (nach NEU-220h)

```
PD-4   checkmark[K/M]_part
  ├── ...(c1–c3 checkmark, c4 ?[O])
PD-5a1  checkmark[M]_part
  ├── PD-5a1a  checkmark[M]_part  (Eingabetyp: s in C, kein S_fin)
  ├── PD-5a1b  checkmark[M]_part  (Typ: KMS+Cauchy, kein Weil-Funktional)
  ├── PD-5a1c  checkmark[M]_part  (1/zeta -> zeta'/zeta algebraisch, nicht typisiert)
  ├── PD-5a1d  checkmark[M]_part  (Normierung 1/(2pi) konsistent, Regularisierung offen)
  └── [PD5a1-logderivative-trace]  ?[O]  <- ZENTRAL
           Ziel: M_{gamma_fin} semifinit typisieren
           Kandidat: S_fin(t) = zeta(1/2-it)/zeta(1/2+it) (unitaer?)
PD-5a2  GESPERRT bis PD5a1-logderivative-trace >= checkmark[M]
X_infty  vollstaendig: (H_inf, S_inf, Q_inf, tau_inf, Lambda_Gamma)  checkmark
X_fin    Schablone: (L2, N_fin, tau_fin, M_gamma_fin, Lambda_fin)   checkmark[M]_part
X_weak = X_fin oplus X_inf  GESPERRT bis X_fin >= checkmark[M]
```

---

*Datei: `katalog/NEU-220h_Endlicher_Weil-Port_aus_NEU-28.md` | 25. Juli 2026*  
*Kernresultat: Fall B bestätigt; vier PD-5a1-Unterknoten ✓[M]_part; zentraler Engpass [PD5a1-logderivative-trace] ?[O]*  
*Quellen: NEU-28 (§3.2, §7.2), NEU-29 (§2–3)*
