# NEU-223 — Quellenaudit: alternativer Vergleichsoperator, Schur, Konfinement und kompakter Resolvent

**Katalog-ID:** NEU-223
**Knoten:** `[O-223-1-alternative-comparison-operator-source-audit]`
**Stand:** 26. Juli 2026 · **Revision 2** (Graphnormklasse statt Operatorgleichheit; Vorzeichenkorrektur $(J^-)^2$)
**Typ:** Reines Quellenaudit von NEU-52 bis NEU-56 — **keine** Konstruktion eines $\tilde L$
**Zweck:** Den einzigen registrierten Pfad zu HP-2 so exakt typisieren, dass weder
Selbstadjungiertheit mit Konfinement noch Konfinement mit Kompaktheit verwechselt werden kann

---

## 0. Auditurteil

Zwei Befunde stehen bereits in den Quellen und ändern die Zielnormalform:

**(i) HP-2 ist für die RH-Hinrichtung nicht erforderlich.** NEU-56 §4 hält wörtlich fest:

> *„Für $\mathrm{Spec}(\lim A_N^{\mathrm{Jac},-})\subset\mathbb R$ genügt die **Selbstadjungiertheit** — ein
> diskretes Spektrum (Weg A) ist hierfür nicht notwendig. Der Engpass NEU-56 blockiert also
> **nicht** die RH-Hinrichtung; er entscheidet nur über den *Typ* des Spektrums."*

G3 betrifft damit ausschließlich das **HP-Profil** (XVI-C.1), nicht den Jacobi-Kanal.

**(ii) Die zulässige Klasse von $\tilde L$ ist quellenseitig auf eine *Graphnormklasse* reduziert.**
NEU-56 §1 zeigt, dass (N1) und (K) zusammen $L \simeq \lvert D_{\mathrm{rel}}\rvert$ erzwingen.
Das ist **keine Operatorgleichheit**: es können formal verschiedene $\tilde L$ in dieser Klasse
existieren. Für die Kompaktheitsfrage ist das unerheblich, weil graphnormäquivalente
Domäneneinbettungen gleichzeitig kompakt oder nicht kompakt sind. Der Suchraum kollabiert
also nicht auf einen Operator, wohl aber auf **eine einzige Kompaktheitsfrage** — und diese
wird kanonisch über $D_{\mathrm{rel}}$ selbst gestellt, nicht über $J^-$ (§6).

**(iii) Quellenfehler in NEU-56 §7 (Revision 2).** Der dort genannte Kandidat
$(1+(J^-)^2)^{1/2}$ ist typwidrig; korrekt ist $(1+D_{\mathrm{rel}}^2)^{1/2}$. Nachweis in §6.1.

$$
\boxed{\ [O\text{-}223\text{-}1] \quad \checkmark[M] \ \text{(Typisierung abgeschlossen; }\tilde L\text{-Klasse auf eine Graphnormklasse reduziert)}}
$$

---

## 1. `[O-223-1a]` — Domänen und Selbstadjungiertheit

### 1.1 Die Trennungsregel steht bereits in der Quelle

NEU-54 §0, Gleichung (54.SEP):

$$
\text{essentielle Selbstadjungiertheit} \;\neq\; \text{kompakte Resolvente} \;\neq\; \text{diskretes Spektrum}
\tag{54.SEP}
$$

> *„Selbstadjungiertheit zuerst. Konfinement danach. Spektralart zuletzt."*

### 1.2 Räume und Domänen

| Objekt | Definition | Quelle |
|---|---|---|
| Graphbasis | $\eta_a = \eta_{p;m;r,u}$, $a=(p,m,r,u)$ | 55.1 |
| $\mathcal D_0$ | $\operatorname{span}_{\mathrm{fin}}\{\eta_{p;m;r,u}\}$ | 54.1 |
| $\mathcal H_{\mathrm{rel}}^{\mathrm{eff}}$ | $\overline{\operatorname{Ran}(J^-)} = \ker(J^-)^\perp$ | 55.0 |
| $\mathcal D_0^{\mathrm{eff}}$ | $\mathcal D_0 \cap \mathcal H_{\mathrm{rel}}^{\mathrm{eff}}$, d.h. $r\neq 0$ und $m>1$ | 55.0 |
| $D_{\mathrm{rel}}$ | $\overline{iJ^-}$ auf $\mathcal H_{\mathrm{rel}}^{\mathrm{eff}}$ | 55.18 |
| $L$ | diagonal in der $\eta$-Basis, $L\eta_a = \ell(a)\eta_a$, $L\ge 1$ | 54.4 |
| $\ell(a)$ | $\sim 1 + \lvert r\rvert\log(2+m) + \lvert u\rvert\log p + \Omega(m)$ | 54.5 / 55.2 |

> **Warnung aus NEU-52 (Warnung 52.D0):** $\eta_{p;m;r,u}$ ist **Graphbasis, nicht
> Eigenbasis** von $D_{\mathrm{rel}}$. Die Spektralbasis existiert nicht explizit.

### 1.3 Flache Achsen

Aus $\lVert\Theta_N(e_rV_n)\rVert = \gamma_N\lvert r\rvert\log(n)\,\lVert e_{r+n}V_n\rVert$ (54.12):
$r=0$ und $n=1$ liefern verschwindende Kopplung. NEU-54 §5:

> *„Sie sind nicht automatisch problematisch für Selbstadjungiertheit … aber für Konfinement
> sind sie problematisch."*

Gewählt wird Option 3: $\mathcal H_{\mathrm{rel}} = \ker(J^-)\oplus\ker(J^-)^\perp$,
$D_{\mathrm{rel}} = 0 \oplus D_{\mathrm{rel}}\vert_{\ker(J^-)^\perp}$ (54.13), Status `⚠[M]`.

Und NEU-55 (55.PRE), für die Kompaktheitsfrage entscheidend:

$$
\boxed{\ \ker(J^-)\ \text{mit unendlicher Multiplizität verhindert kompakten Resolventen.}\ }
\tag{55.PRE}
$$

### 1.4 Was bewiesen ist

| Aussage | Status | Quelle |
|---|---|---|
| $(J^-)_{ab} = -\overline{(J^-)_{ba}}$, also $iJ^-$ symmetrisch auf $\mathcal D_0$ | `✓[M]` | Satz 54.1 |
| $[J^-,L]_{ba} = (\ell(a)-\ell(b))\Theta_{ba}$ | `✓[M]` | 55.10 |
| $iJ^-$ wesentlich selbstadjungiert auf $\mathcal D_0^{\mathrm{eff}}$ | `✓[M]` **unter** (N1),(N2) | 55.17 |
| $D_{\mathrm{rel}}$ kanonisch selbstadjungiert; Resolvente für $s\notin\mathbb R$ | `✓[M]` | 55.18, 56.9 |
| Essentielle Selbstadjungiertheit bleibt von der Obstruktion unberührt | `✓[M]` | Satz 56.3 |

> **Keine Übertragung.** Aus 55.17/55.18 folgt **nichts** über kompakte Resolventen.

---

## 2. `[O-223-1b]` — Die Vergleichsoperatorabschätzung (N1)/(N2)

### 2.1 Exakte Form

$$
\textbf{(N1)}\quad \lVert J^-x\rVert \le C\lVert Lx\rVert, \qquad x\in\mathcal D_0
\tag{54.6}
$$

$$
\textbf{(N2)}\quad \bigl\lvert\langle J^-x,Lx\rangle - \langle Lx,J^-x\rangle\bigr\rvert \le C\langle x,Lx\rangle, \qquad x\in\mathcal D_0
\tag{54.7}
$$

Es wird **keine** Kato-Rellich-Form $a\lVert Lx\rVert + b\lVert x\rVert$ mit $a<1$ verwendet.
NEU-54 §4 verwirft Kato-Rellich ausdrücklich: $J^-$ ist *„primär ein gewichteter
Off-Diagonal-Graphoperator ohne klaren dominanten diagonalen Teil"*, Status `⚠[M]`, nur als
letzte Rückfalloption.

### 2.2 Hinreichende Matrixkriterien

$$
\text{zu (N1):}\quad \sum_b \lvert\Theta_{ba}\rvert^2 \le C^2\ell(a)^2
\tag{55.5}
$$

$$
\text{Schur-Variante:}\quad \sup_a \sum_b \frac{\lvert\Theta_{ba}\rvert}{\ell(a)} < \infty, \qquad \sup_b \sum_a \frac{\lvert\Theta_{ba}\rvert}{\ell(a)} < \infty
\tag{55.9}
$$

Daraus $J^-L^{-1}\in\mathcal B(\mathcal H)$, also (N1).

$$
\text{zu (N2), zeilenweise:}\quad \sum_b \lvert\ell(a)-\ell(b)\rvert\,\lvert\Theta_{ba}\rvert \le C\ell(a)
\tag{55.12}
$$

### 2.3 Kopplungsstruktur und Konstanten

$$
\Theta_N(e_rV_n) = -\gamma_N\,r\log(n)\,e_{r+n}V_n, \qquad
\Theta_{ba}\neq 0 \ \text{nur für}\ b=(p',m,r+n,u'),\ n\mid m
\tag{55.3}
$$

$$
\lvert\Theta_{ba}\rvert \sim \gamma_N\lvert r\rvert\log n, \qquad
\lvert\Theta_{ba}\rvert \lesssim \gamma_N\,\ell(a)
\tag{55.6/55.7}
$$

$$
\lvert\ell(b)-\ell(a)\rvert \sim n\log(2+m) \lesssim m\log(2+m)
\tag{55.14}
$$

$$
\frac{\lvert\ell(b)-\ell(a)\rvert\,\lvert\Theta_{ba}\rvert}{\ell(a)} \lesssim \gamma_N\,m\log m
\tag{55.16}
$$

### 2.4 Abhängigkeiten der Konstanten — Antwort auf die Auditfragen

| Frage | Quellenbefund |
|---|---|
| Uniform in $N$? | **Nein.** NEU-55 §4 Warnung: *„Bei festem $N$ und endlichen $m\le N$ ist (55.16) beschränkt. Im Grenzübergang $N\to\infty$ muss die Konvergenzrate $\gamma_N\to 0$ schnell genug gewählt werden."* |
| Welche Normierung tritt ein? | Skalares $\gamma_N$, eingeführt über $\Theta_N$ (55.3). Erzwungene globale Schur-Rate: $\gamma_N \le K/(N\log N)$ (56.6) `✓[M]` |
| Auf welchem Kern? | $\mathcal D_0^{\mathrm{eff}}$, also $r\neq 0$, $m>1$ (55.0) |
| Abhängigkeit von Primzahlgrenzen/Orbitparametern? | über $m\le N$ und $\Omega(m)$ in $\ell(a)$ (54.5); (55.16) wächst mit $m$ |
| Relative Beschränktheit oder Kommutatorabschätzung? | **Beides getrennt**: (N1) relative Beschränktheit, (N2) Kommutatorabschätzung. Nelsons Kommutatortheorem verlangt beide |

### 2.5 Statuspräzisierung

| Bedingung | Status | Quelle |
|---|---|---|
| (55.5) Nelson-Bed. 1 | `✓/⚠[M]` **heuristisch** | 55.7 Statusmatrix |
| (55.9) Schur-Test exakt | **`?[O]`** | 55.7 Statusmatrix |
| (55.10) Kommutatorformel | `✓[M]` | 55.7 |
| (55.12) Kommutator-Schur | `✓[M]` für endliches $N$; `⚠[M]` im Grenzfall | 55.7 |

---

## 3. `[O-223-1c]` — Konfinement, logisch getrennt

### 3.1 Die Bedingung

$$
\textbf{(K)}\quad \lVert D_{\mathrm{rel}}x\rVert + \lVert x\rVert \ \ge\ c\,\lVert Lx\rVert, \qquad x\in\mathcal D_0
\tag{54.16 / 56.3}
$$

Sie kontrolliert die $L$-Graphnorm durch die Operatorgraphnorm und ist **kein** Bestandteil
des Nelson-Kriteriums.

### 3.2 Die Richtungsspannung — wörtlich

NEU-56 §1:

> **Strukturelle Pointe.** *(N1) verlangt $J^-\lesssim L$, (K) verlangt
> $L\lesssim \lvert D_{\mathrm{rel}}\rvert = \lvert\overline{iJ^-}\rvert$. Beide zusammen
> erzwingen $L\simeq\lvert D_{\mathrm{rel}}\rvert$ bis auf Konstanten — eine sehr starke
> Forderung, die der weiter unten gezeigten $\gamma_N$-Asymptotik widerspricht.*

$$
\boxed{\ \textbf{(N1)} \ \text{will } L \text{ groß.} \qquad \textbf{(K)} \ \text{will } L \text{ klein.} \qquad \text{Zusammen:} \ L \simeq \lvert D_{\mathrm{rel}}\rvert. \ }
$$

### 3.3 Die Doppelrolle von $\gamma_N$ (NEU-55 §6)

| Rolle | Anforderung |
|---|---|
| Konfinement: $\lVert J^-\eta_a\rVert \sim \gamma_N\lvert r\rvert\log n \to\infty$ | $\gamma_N$ **nicht zu schnell** $\to 0$ |
| Kommutator-Schur: $\gamma_N\,m\log m$ beschränkt | $\gamma_N$ **schnell genug** $\to 0$ |

---

## 4. Das No-Go von NEU-56 als Implikationsdiagramm

### 4.1 Was bewiesen ist

$$
\underbrace{\text{Schur-/Nelsonkontrolle über } L}_{\Rightarrow\ \gamma_N \le K/(N\log N)\ (56.6)}
\;+\;
\underbrace{\text{Konfinement über denselben } L}_{\text{(K), } 56.3}
\;+\;
\underbrace{\text{skalare Normierung } \gamma_N}_{\text{eine Zahl pro } N}
\;\Longrightarrow\;
\text{inkompatible Asymptotik}
$$

Der Mechanismus (Satz 56.2, `✗[M]`): Einsetzen der erzwungenen Rate liefert
$$\lVert J^-\eta_a\rVert \sim \gamma_N\lvert r\rvert\log n = \frac{K\lvert r\rvert\log n}{N\log N} \xrightarrow{N\to\infty} 0 \quad (\text{festes } r,n),
\tag{56.7}$$
also $\lVert D_{\mathrm{rel}}x\rVert \ll \lVert Lx\rVert$ und damit **(K) verletzt** (56.8).

### 4.2 Was ausgeschlossen ist und was nicht

$$
\boxed{\ \text{ausgeschlossen: derselbe Mechanismus mit diesem } L \text{ und skalarem } \gamma_N \ }
$$

$$
\boxed{\ \text{NICHT ausgeschlossen: jeder Vergleichsoperator oder jeder kompakte Resolvent} \ }
$$

NEU-56 (56.12) hält Punkt (VI) ausdrücklich offen: *„Weg A offen: nur über einen anderen,
mit $J^-$ verträglichen Vergleichsoperator $\tilde L$."* `❓[O]`

### 4.3 Verbrauchte Freiheitsgrade — die getesteten Varianten

| Variante | Zusatzannahme | Ergebnis | Status |
|---|---|---|---|
| **A** | skalares $\gamma_N = C/\log N$ | widerlegt (Satz 56.1) | `✗[M]` |
| **A′** | skalares $\gamma_N$ beliebig | globaler Schur erzwingt $\gamma_N\le K/(N\log N)$, damit (K) verletzt (Satz 56.2) | `✗[M]` |
| **B1** | separables $m$-Gewicht $\Theta\mapsto\Theta\cdot w(m)$; Schur verlangt $w(m)\le K/(m\log m)$ | Konfinement hält **nur** in der $r$-Achse ($\lvert r\rvert\to\infty$ bei festem $m$), bricht in $m$-Richtung ($m\to\infty$ bei festem $r$): **partielles Konfinement** | `✗/❓[M]` |
| **B2** | $L$-Rekalibrierung $\ell(a)\to\ell(a)+m\log m$ | Schur-Quotient wird beschränkt ($Q_{B2}\sim\gamma_N\log m \le C$, 56.10), aber $\lVert Lx\rVert \sim m\log m$ wächst, während $\lVert D_{\mathrm{rel}}x\rVert$ nur wie $\gamma_N\lvert r\rvert\log n$ wächst: (K) **verschlechtert sich** (56.11) | `✗[M]` |

**Befund Option B (56.5, wörtlich):** *„Keine getestete Reskalierung (skalar, separabel,
oder $L$-Rekalibrierung) erfüllt (N1)/(N2) und (K) zugleich mit dem Vergleichsoperator $L$.
Die Obstruktion ist robust gegenüber dieser Klasse von Modifikationen."*

---

## 5. `[O-223-1e]` — Die verbleibende zulässige Klasse von $\tilde L$

### 5.1 Was B2 über bloße Rekalibrierungen zeigt

Der Auditauftrag vermutete, dass $\lVert\tilde Lx\rVert \asymp \lVert Lx\rVert$ den Widerspruch
nur umschreibt. Die Quellen belegen mehr — und zwar in beide Richtungen der Ordnung:

> **Abgeleitete Beobachtung (nicht Quellenaussage, aus 56.10/56.11 und §1 hergeleitet).**
> B2 ist gerade **nicht** graphnormäquivalent zu $L$: $\ell + m\log m \gg \ell$. Es
> scheitert trotzdem — und zwar an (K), also am *anderen* Ende als die skalaren Varianten,
> die an Schur scheitern. Vergrößern von $L$ hilft (N1)/(N2) und schadet (K); Verkleinern
> umgekehrt. Damit ist keine Rekalibrierung in der von $L$ erzeugten Ordnungsklasse frei —
> weder äquivalente noch echt größere.

### 5.2 Die Reduktion ist eine Graphnormklasse, keine Operatorgleichheit

Aus $J^-\lesssim\tilde L$ und $\tilde L\lesssim\lvert D_{\mathrm{rel}}\rvert$ zusammen mit der
in NEU-56 §1 verwendeten Gegenrichtung folgt für jeden zulässigen Vergleichsoperator:

$$
\boxed{\ \lVert\tilde Lx\rVert + \lVert x\rVert \ \asymp\ \bigl\lVert\lvert D_{\mathrm{rel}}\rvert x\bigr\rVert + \lVert x\rVert \ }
$$

> **Präzisierung (Revision 2).** In dieser Klasse können formal verschiedene Operatoren
> liegen. Der Suchraum kollabiert daher **nicht** notwendig auf einen einzigen Operator.
> Für die Kompaktheit ist das jedoch unerheblich: graphnormäquivalente Domäneneinbettungen
> sind gleichzeitig kompakt oder nicht kompakt. Der Suchraum kollabiert also auf **eine
> einzige Kompaktheitsfrage**.

$$
\boxed{\ \text{G3 ist keine Suchaufgabe nach einem Vergleichsoperator mehr, sondern eine Spektralfrage über } D_{\mathrm{rel}}. \ }
$$

### 5.3 Die drei Anforderungen aus NEU-56 §7

NEU-56 §7 verlangt von $\tilde L$: (1) kompakter Resolvent auf $\mathcal H_{\mathrm{rel}}^{\mathrm{eff}}$,
(2) $\tilde L\lesssim\lvert D_{\mathrm{rel}}\rvert$ ohne Erzwingung über skalares $\gamma_N$,
(3) $[J^-,\tilde L]$ Schur-kontrolliert. Wählt man $\tilde L$ als Funktion von
$\lvert D_{\mathrm{rel}}\rvert$, sind (2) und (3) automatisch erfüllt. **Übrig bleibt allein (1).**

---

## 6. `[O-223-1d]` — Kompaktheit: Typkorrektur in zwei Stufen

### 6.1 Erste Stufe: Vorzeichenkorrektur am Quellenkandidaten

NEU-56 §7 nennt wörtlich $\tilde L = (1+(J^-)^2)^{1/2}$. Dieser Ausdruck ist **typwidrig**.

Aus NEU-54 (54.3) und Z. 47 sowie NEU-53 §2 gilt in den Quellen ausdrücklich

$$
(J^-)_{ab} = -\overline{(J^-)_{ba}}, \qquad (J_N^-)^* = -J_N^- ,
\tag{54.3}
$$

also ist $J^-$ **schiefadjungiert** — genau deshalb wird $iJ^-$ symmetrisch und
$D_{\mathrm{rel}} = \overline{iJ^-}$ selbstadjungiert (55.18, 56.9). Daraus folgt

$$
D_{\mathrm{rel}}^2 = (iJ^-)^2 = -(J^-)^2, \qquad\text{also}\qquad
1+(J^-)^2 = 1 - D_{\mathrm{rel}}^2 .
$$

Der Ausdruck $1+(J^-)^2$ ist damit **nicht** $\ge 1$, sondern $\le 1$, und seine Wurzel
existiert im Allgemeinen nicht. Gemeint — und im Weiteren verwendet — ist

$$
\boxed{\ \tilde L \;=\; \bigl(1+\lvert J^-\rvert^2\bigr)^{1/2} \;=\; \bigl(1+D_{\mathrm{rel}}^2\bigr)^{1/2} \;\ \text{mit}\ \; \lvert J^-\rvert = \bigl((J^-)^*J^-\bigr)^{1/2} = \lvert D_{\mathrm{rel}}\rvert . \ }
$$

> **Status.** `✓[M]_neg` gegen die Schreibweise in NEU-56 §7. Die *Absicht* der Quelle —
> $\tilde L$ als Funktion von $J^-$, sodass (K) trivial wird — bleibt unberührt und korrekt;
> korrigiert wird allein die Symbolform. Die Identität mit $\lvert D_{\mathrm{rel}}\rvert$ ist
> hier aus der Quelldefinition $D_{\mathrm{rel}}=\overline{iJ^-}$ und (54.3) belegt, nicht aus
> formaler Symbolrechnung übernommen.

### 6.2 Zweite Stufe: die kanonische Formulierung läuft über $D_{\mathrm{rel}}$

Da $D_{\mathrm{rel}}$ selbstadjungiert ist (56.9), sind äquivalent:

$$
(D_{\mathrm{rel}} - i)^{-1} \in \mathcal K
\quad\Longleftrightarrow\quad
\bigl(1+D_{\mathrm{rel}}^2\bigr)^{-1/2} \in \mathcal K
\quad\Longleftrightarrow\quad
\operatorname{Dom}(D_{\mathrm{rel}}) \hookrightarrow \mathcal H_{\mathrm{rel}} \ \text{kompakt (Graphnorm).}
$$

Diese Form ist typologisch sicherer als jede über $J^-$, weil $J^-$ erst nach Multiplikation
mit $i$ und Abschluss selbstadjungiert wird.

Was NEU-55/56 demgegenüber tatsächlich kontrollieren:

- **NEU-55 (55.9):** $J^-L^{-1}\in\mathcal B(\mathcal H)$ — **Beschränktheit**, nicht Kompaktheit.
- **NEU-54 (54.16/54.17):** $L^{-1}$ kompakt, *„da $\ell(p,m,r,u)\to\infty$ entlang der Basis"*; zusammen mit (K) folgt $(D_{\mathrm{rel}}-i)^{-1}\in\mathcal K$.

> **Konsequenz.** Die Kompaktheit von $L^{-1}$ war nie das Problem. Verloren geht nicht sie,
> sondern die Brücke (K) zwischen $L$ und $D_{\mathrm{rel}}$. Bei
> $\tilde L\asymp\lvert D_{\mathrm{rel}}\rvert$ ist die Brücke trivial — dafür ist die
> Kompaktheit nicht mehr geschenkt.

### 6.3 Der Kernschritt und was er *nicht* leistet

Ist $\dim\ker D_{\mathrm{rel}} = \infty$, so wirkt $(1+D_{\mathrm{rel}}^2)^{-1/2}$ auf dem Kern
als **Identität**; der volle Operator kann dann nicht kompakt sein. Die Restriktion auf

$$
\mathcal H_{\mathrm{rel}}^{\mathrm{eff}} := \bigl(\ker D_{\mathrm{rel}}\bigr)^{\perp}
$$

ist dann zwingend (vgl. 55.PRE). Sie ist aber **nur zulässig, wenn dieser Raum den Operator
reduziert**, d.h. wenn er mit dem Spektralprojektor übereinstimmt:

$$
\boxed{\ E_{D_{\mathrm{rel}}}\bigl(\mathbb R\setminus\{0\}\bigr)\,\mathcal H_{\mathrm{rel}} \;=\; \mathcal H_{\mathrm{rel}}^{\mathrm{eff}} \ }
$$

Bei Selbstadjungiertheit ist das kanonisch formulierbar und **muss belegt werden**, nicht
vorausgesetzt. NEU-55 (55.0) definiert $\mathcal H^{\mathrm{eff}}_{\mathrm{rel}}$ über
$\overline{\operatorname{Ran}(J^-)}=\ker(J^-)^\perp$ ohne diesen Nachweis.

> **Sperrvermerk (Revision 2).** Das Entfernen eines unendlichdimensionalen Nullraums
> **genügt nicht**. Auch danach kann wesentliches Spektrum bei einem $\lambda\neq 0$ oder
> eine beschränkte Folge nichtverschwindender Eigenwerte unendlicher Multiplizität vorliegen.
> Der Schluss „Kern abgespalten $\Rightarrow$ kompakter reduzierter Resolvent" ist unzulässig.

### 6.4 Der binäre Test

**Negativer Zeuge.** Es genügt, eine orthonormale Folge
$x_n \in \operatorname{Dom}(D_{\mathrm{rel}}) \cap \mathcal H_{\mathrm{rel}}^{\mathrm{eff}}$
zu konstruieren mit

$$
\sup_n \bigl(\lVert x_n\rVert + \lVert D_{\mathrm{rel}}x_n\rVert\bigr) < \infty .
$$

Dann ist die Graphnormeinbettung nicht kompakt, also
$(1+D_{\mathrm{rel}}^2)^{-1/2}\vert_{\mathcal H_{\mathrm{rel}}^{\mathrm{eff}}} \notin \mathcal K$.

Stärkere Variante — **Weyl-Folge**:
$\lVert x_n\rVert = 1$, $x_n \rightharpoonup 0$, $\lVert(D_{\mathrm{rel}}-\lambda)x_n\rVert \to 0$.
Dann liegt $\lambda$ im wesentlichen Spektrum.

**Positiver Beweis.** Für jedes $R<\infty$ muss der Graphnormball

$$
\bigl\{x \in \mathcal H_{\mathrm{rel}}^{\mathrm{eff}} : \lVert x\rVert^2 + \lVert D_{\mathrm{rel}}x\rVert^2 \le R\bigr\}
$$

in $\mathcal H_{\mathrm{rel}}^{\mathrm{eff}}$ präkompakt sein. Spektral äquivalent:

$$
\dim E_{\lvert D_{\mathrm{rel}}\rvert}\bigl([0,T]\bigr)\,\mathcal H_{\mathrm{rel}}^{\mathrm{eff}} < \infty \quad \forall\, T<\infty,
$$

und die nichtverschwindenden Eigenwerte müssen betragsmäßig gegen unendlich laufen.

Zweites, unabhängiges Kriterium aus NEU-56 §7: *„Spurklasse-Kriterium über $K_{pq}$ (NEU-51):
falls $\sum_p \operatorname{Tr}\lvert M_p(z)\rvert < \infty$ gleichmäßig, ergäbe sich diskretes
Spektrum — zu prüfen."* `❓[O]`

---

## 7. Endliches $N$ gegen Grenzoperator

Für jede zentrale Aussage getrennt geführt.

| Aussage | festes $N$ | uniform in $N$ | Grenzoperator |
|---|---|---|---|
| Lokale Endlichkeit von $\Theta_N$ (55.3) | `✓[M]` | — | Nachbarzahl nach oben unbegrenzt |
| Nelson-Bed. 1 (55.5) | `✓/⚠[M]` heuristisch | `?[O]` | `?[O]` |
| Schur-Test (55.9) | — | `?[O]` | `?[O]` |
| Kommutator-Schur (55.12) via (55.16) | `✓[M]`, da $m\le N$ | **nein** | `⚠[M]`, abhängig von $\gamma_N$ |
| Erzwungene Rate $\gamma_N \le K/(N\log N)$ | — | `✓[M]` (56.6) | — |
| Konfinement (K) | — | — | `✗[M]` verletzt (56.7/56.8) |
| Essentielle Selbstadjungiertheit | — | — | `✓[M]` (56.9) |
| $\sigma(D_{\mathrm{rel},N})$ diskret | `✓[M]` (NEU-53 §2, *„Harmlos"*) | — | **kein Übertrag** |

> **Sperrvermerk.** Ein endlicher Jacobi- oder Graphoperator besitzt trivialerweise
> kompakten Resolventen; NEU-53 §2 hält das für $D_{\mathrm{rel},N}$ ausdrücklich fest und
> nennt es *„harmlos"*. HP-2 betrifft **nicht** die endlichen Trunkierungen, sondern die
> unendliche bzw. renormierte Realisierung. Der Schluss
> $$D_N \text{ hat diskretes Spektrum} \;\Longrightarrow\; D_\infty \text{ hat kompakten Resolventen}$$
> ist **unzulässig** und in keiner Quelle behauptet.

---

## 8. Zielnormalform — revidiert (Revision 2)

Der im Auftrag vorgeschlagene Zielzustand lautete: $\exists\,\tilde L\ge 1$ mit
$\lVert J^-x\rVert \le a\lVert\tilde Lx\rVert + b\lVert x\rVert$,
$\lVert\tilde Lx\rVert \le C(\lVert D_{\mathrm{rel}}x\rVert + \lVert x\rVert)$ und
$(\tilde L+i)^{-1}\in\mathcal K(\mathcal H_{\mathrm{rel}})$.

Nach §5.2 kollabiert das auf eine Graphnormklasse, und nach §6.2 ist deren kanonischer
Repräsentant $D_{\mathrm{rel}}$ selbst. Die Zielnormalform lautet damit:

$$
\boxed{\
\bigl(1+D_{\mathrm{rel}}^2\bigr)^{-1/2}\Big\vert_{\mathcal H_{\mathrm{rel}}^{\mathrm{eff}}} \in \mathcal K\bigl(\mathcal H_{\mathrm{rel}}^{\mathrm{eff}}\bigr),
\quad\text{mit}\quad E_{D_{\mathrm{rel}}}(\mathbb R\setminus\{0\})\,\mathcal H_{\mathrm{rel}} = \mathcal H_{\mathrm{rel}}^{\mathrm{eff}}
\ }
$$

zuzüglich der noch offenen Grundlagen: exakter Schur-Test (55.9) und Nelson-Bed. 1 (55.5)
für die Selbstadjungiertheit, auf der alles aufbaut.

### Die drei möglichen Ausgänge

| Ausgang | Bedeutung |
|---|---|
| **kompakt** | HP-2 erfüllt; HP-3 bis HP-6 werden anschließend prüfbar; Weg A wieder offen |
| **nicht kompakt** | Erheblich stärker als NEU-56: nicht nur $L$ und seine Rekalibrierungen scheitern, sondern die **kanonische $D_{\mathrm{rel}}$-Realisierung besitzt keinen kompakten reduzierten Resolventen** |
| **unentschieden** | Knoten bleibt offen, aber mit typkorrekt gestellter Frage |

### Reichweite eines negativen Ergebnisses — Umfangsklausel

$$
\boxed{\ \text{Ausgeschlossen wäre die gesamte erzwungene Vergleichsoperatorklasse des gegenwärtigen relativen Jacobi-/Feshbachmodells.} \ }
$$

**Nicht ausgeschlossen wäre**, dass eine anders konstruierte Realisierung $H_X$ von Objekt X
HP-2 erfüllt. Ein negatives Ergebnis wäre ein No-Go über *dieses Modell*, nicht über X.

**Ebenso nicht betroffen:**

$$
\boxed{\ \text{HP-2 entscheidet über den Spektraltyp, nicht über die RH-Hinrichtung durch Selbstadjungiertheit.} \ }
$$

`[O-223-2]` ist ein scharfer, binärer Strukturtest des **HP-Profils** (XVI-C.1), aber
**keine Sperre** für den schwächeren Jacobi- oder Stieltjeskanal (XVI-C.2).

---

## 9. Statusbilanz

| Aussage | Status |
|---|---|
| HP-2 ist für die RH-Hinrichtung nicht erforderlich (NEU-56 §4) | `✓[M]` |
| (54.SEP): SA $\neq$ kompakte Resolvente $\neq$ diskretes Spektrum | `✓[M]` |
| (N1)/(N2) exakt extrahiert; keine Kato-Rellich-Form | `✓[M]` |
| Konstanten nicht uniform in $N$ | `✓[M]` |
| (K) ist kein Bestandteil des Nelson-Kriteriums | `✓[M]` |
| (N1)+(K) erzwingen $L\simeq\lvert D_{\mathrm{rel}}\rvert$ | `✓[M]` (56 §1) |
| Reduktion ist **Graphnormklasse**, keine Operatorgleichheit | `✓[M]` abgeleitet (§5.2) |
| No-Go betrifft nur diesen $L$ mit skalarem $\gamma_N$; A′, B1, B2 verbraucht | `✓[M]` |
| Rekalibrierungen scheitern in **beiden** Ordnungsrichtungen | `✓[M]` abgeleitet (§5.1) |
| **$(1+(J^-)^2)^{1/2}$ in NEU-56 §7 ist typwidrig; korrekt $(1+D_{\mathrm{rel}}^2)^{1/2}$** | **`✓[M]_neg`** (§6.1) |
| Kanonische Formulierung über $D_{\mathrm{rel}}$, drei äquivalente Formen | `✓[M]` (§6.2) |
| Reduzierende Eigenschaft $E_{D_{\mathrm{rel}}}(\mathbb R\setminus\{0\})\mathcal H=\mathcal H^{\mathrm{eff}}$ | **`❓[O]`** — in 55.0 nicht belegt |
| Kernabspaltung genügt nicht (wesentliches Spektrum bei $\lambda\neq0$ möglich) | `✓[M]` (§6.3) |
| Kompaktheit von $(1+D_{\mathrm{rel}}^2)^{-1/2}$ auf $\mathcal H^{\mathrm{eff}}_{\mathrm{rel}}$ | **`❓[O]`** — der Knoten |
| Spurklassekriterium $\sum_p\operatorname{Tr}\lvert M_p(z)\rvert<\infty$ | `❓[O]` (NEU-51) |
| Exakter Schur-Test (55.9) / Nelson-Bed. 1 (55.5) | `❓[O]` / `✓/⚠[M]` heuristisch |
| **Gesamtstatus `[O-223-1]`** | **`✓[M]`** (Typisierung), Folgeknoten offen |

---

## 10. Nachfolgeknoten `[O-223-2]` — vier Teilschritte

$$
\boxed{\ [O\text{-}223\text{-}2\text{-spectral-type-of-the-forced-operator}] \ }
$$

| Teilknoten | Aufgabe | Status |
|---|---|---|
| `[O-223-2a]` | $\dim\ker D_{\mathrm{rel}}$ und **exakte Beschreibung** des Kerns. Die flachen Achsen $r=0$, $n=1$ (54.12) sind Kandidaten, aber kein Beweis der Gleichheit $\ker(J^-)=\operatorname{span}\{\ldots\}$ | `❓[O]` |
| `[O-223-2b]` | $\mathcal H^{\mathrm{eff}}_{\mathrm{rel}} = (\ker D_{\mathrm{rel}})^\perp$ als **reduzierender** Spektralraum: $E_{D_{\mathrm{rel}}}(\mathbb R\setminus\{0\})\mathcal H_{\mathrm{rel}} = \mathcal H^{\mathrm{eff}}_{\mathrm{rel}}$ | `❓[O]` |
| `[O-223-2c]` | Konstruktion einer graphnormbeschränkten Orthonormalfolge in $\operatorname{Dom}(D_{\mathrm{rel}})\cap\mathcal H^{\mathrm{eff}}_{\mathrm{rel}}$ — **oder** Ausschluss einer solchen | `❓[O]` |
| `[O-223-2d]` | $(1+D_{\mathrm{rel}}^2)^{-1/2}\vert_{\mathcal H^{\mathrm{eff}}_{\mathrm{rel}}} \in\mathcal K$? | `❓[O]` |

Parallel nachzuziehen (tragen die Selbstadjungiertheit, auf der alles beruht): exakter
Beweis von (55.9) und (55.5).

---

## Abhängigkeiten

| Referenz | Verwendet für |
|---|---|
| NEU-51 | Spurklassekriterium via $K_{pq}$ |
| NEU-52 | Graphbasis $\eta_a$; Warnung 52.D0 (Graphbasis $\neq$ Eigenbasis) |
| NEU-53 | Operatorstatus $D_{\mathrm{rel}}$, Weg A / Weg B, $J_N^{-*}=-J_N^-$ (§2) |
| NEU-54 | (54.SEP), $\mathcal D_0$, $L$ und $\ell(a)$, (N1)/(N2), (54.3) Schiefadjungiertheit, flache Achsen, (K), (54.17) |
| NEU-55 | $\mathcal H^{\mathrm{eff}}_{\mathrm{rel}}$, (55.PRE), Matrixkriterien, Kommutatorformel, $\gamma_N$-Doppelrolle |
| NEU-56 | Rate $\gamma_N\le K/(N\log N)$, Satz 56.1/56.2/56.3, §4 (RH braucht nur SA), Optionen B1/B2, (56.12), $\tilde L$-Agenda §7 |
| NEU-220u | HP-1–HP-7, insbesondere HP-2/HP-3 |

---

## Revisionsverlauf

| Rev. | Datum | Änderung |
|---|---|---|
| 1 | 26. Juli 2026 | Erstfassung des Quellenaudits NEU-52–56 |
| **2** | 26. Juli 2026 | §5.2 Reduktion als **Graphnormklasse** statt Operatorgleichheit. §6.1 **Vorzeichenkorrektur**: $(1+(J^-)^2)^{1/2}$ in NEU-56 §7 typwidrig wegen $(J^-)^*=-J^-$; korrekt $(1+D_{\mathrm{rel}}^2)^{1/2}$. §6.2 kanonische Formulierung über $D_{\mathrm{rel}}$. §6.3 reduzierender Spektralraum als eigene offene Bedingung; Kernabspaltung genügt nicht. §6.4 binärer Test mit negativem Zeugen und Weyl-Folge. §8 Umfangsklausel. §10 vier Teilknoten `[O-223-2a–d]`. |
