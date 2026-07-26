# NEU-223 — Quellenaudit: alternativer Vergleichsoperator, Schur, Konfinement und kompakter Resolvent

**Katalog-ID:** NEU-223
**Knoten:** `[O-223-1-alternative-comparison-operator-source-audit]`
**Stand:** 26. Juli 2026
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

**(ii) Die zulässige Klasse von $\tilde L$ ist quellenseitig bereits auf einen Punkt reduziert.**
NEU-56 §1 zeigt, dass (N1) und (K) zusammen $L \simeq \lvert D_{\mathrm{rel}}\rvert$ erzwingen,
und NEU-56 §7 benennt den daraus folgenden kanonischen Kandidaten
$\tilde L = (1+(J^-)^2)^{1/2}$ samt der Feststellung, dass dann (K) **trivial** ist und
die gesamte Frage auf das Wachstum der Singulärwerte zusammenfällt.

$$
\boxed{\ [O\text{-}223\text{-}1] \quad \checkmark[M] \ \text{(Typisierung abgeschlossen; }\tilde L\text{-Klasse auf einen Kandidaten reduziert)}}
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
> weder äquivalente noch echt größere. Genau das ist der Inhalt der strukturellen Pointe
> $L\simeq\lvert D_{\mathrm{rel}}\rvert$ aus §1.

$$
\boxed{\ \text{Verboten sind sämtliche } \tilde L, \text{ die nicht } \asymp \lvert D_{\mathrm{rel}}\rvert \text{ sind — in beide Richtungen.}\ }
$$

### 5.2 Der kanonische Kandidat steht bereits in der Quelle

NEU-56 §7 nennt drei Anforderungen an $\tilde L$:

1. $\tilde L$ hat kompakten Resolventen (Eigenwerte $\to\infty$, endliche Multiplizität auf $\mathcal H_{\mathrm{rel}}^{\mathrm{eff}}$),
2. $\tilde L \lesssim \lvert D_{\mathrm{rel}}\rvert$ — echtes Konfinement, **nicht** über das skalare $\gamma_N$ erzwungen,
3. Verträglichkeit: $[J^-,\tilde L]$ Schur-kontrolliert.

und den daraus folgenden Kandidaten, wörtlich:

> *„$\tilde L$ als Funktion von $J^-$ selbst, z.B. $\tilde L = (1+(J^-)^2)^{1/2}$: dann ist
> (K) trivial ($\tilde L = \lvert D_{\mathrm{rel}}\rvert$), aber Kompaktheit des Resolventen
> wird zur Frage über das Wachstum der singulären Werte von $J^-$ auf
> $\mathcal H_{\mathrm{rel}}^{\mathrm{eff}}$ — das ist der eigentliche, bisher nicht
> adressierte Spektralpunkt."*

Mit dieser Wahl sind die Anforderungen 2 und 3 automatisch erfüllt: (K) gilt mit Gleichheit,
und $[J^-,\tilde L]$ entfällt als eigenständige Bedingung, da $\tilde L$ eine Funktion von
$J^-$ ist. **Übrig bleibt allein Anforderung 1.**

$$
\boxed{\ \text{Die } \tilde L\text{-Klasse ist quellenseitig auf einen Kandidaten reduziert. G3 ist damit keine Suchaufgabe mehr, sondern eine Spektralfrage.}\ }
$$

---

## 6. `[O-223-1d]` — Kompakte Einbettung: Typkorrektur

### 6.1 Die Formulierung in Ebene XVI war typwidrig

XVI-D/P5.2 fragt nach $s_k(J^-\vert_{\mathcal H_{\mathrm{rel}}^{\mathrm{eff}}})$. Für einen
**unbeschränkten** Operator sind gewöhnliche Singulärwerte nicht ohne Weiteres definiert.

Typkorrekte Objekte:

| Objekt | Bedeutung |
|---|---|
| $(\tilde L + i)^{-1} \in \mathcal K(\mathcal H_{\mathrm{rel}}^{\mathrm{eff}})$ | kompakter Resolvent von $\tilde L$ |
| $J^-(1+(J^-)^2)^{-1/2}$ | beschränkt, aber **nicht** kompakt (Betrag $\to 1$) — als Testobjekt ungeeignet |
| $(1+(J^-)^2)^{-1/2}$ | **das relevante Objekt**: kompakt $\iff$ $\tilde L$ hat kompakten Resolventen |
| $\operatorname{Dom}(\tilde L)\hookrightarrow \mathcal H_{\mathrm{rel}}^{\mathrm{eff}}$ mit $\tilde L$-Graphnorm | kompakt $\iff$ dasselbe |

Was NEU-55/56 tatsächlich kontrollieren:

- **NEU-55 (55.9):** $J^-L^{-1} \in \mathcal B(\mathcal H)$ — **Beschränktheit**, nicht Kompaktheit.
- **NEU-54 (54.16/54.17):** $L^{-1}$ kompakt, *„da $\ell(p,m,r,u)\to\infty$ entlang der Basis"*; zusammen mit (K) folgt $(D_{\mathrm{rel}}-i)^{-1}\in\mathcal K$.

> **Konsequenz.** Die Kompaktheit von $L^{-1}$ ist gesichert (Diagonaloperator mit
> divergierenden Einträgen). Verloren geht nicht die Kompaktheit von $L$, sondern die
> Brücke (K) zwischen $L$ und $D_{\mathrm{rel}}$. Bei $\tilde L = \lvert D_{\mathrm{rel}}\rvert$
> ist die Brücke trivial — dafür ist die Kompaktheit nicht mehr geschenkt.

### 6.2 Die korrekt gestellte Frage

$$
\boxed{\ \text{Ist } \bigl(1+(J^-)^2\bigr)^{-1/2} \ \text{kompakt auf } \mathcal H_{\mathrm{rel}}^{\mathrm{eff}}\,? \ }
$$

Äquivalent: Divergiert die Eigenwertfolge von $\lvert D_{\mathrm{rel}}\rvert$ auf
$\mathcal H_{\mathrm{rel}}^{\mathrm{eff}}$, oder akkumuliert sie?

Notwendige Vorbedingung aus (55.PRE): $\ker(J^-)$ darf nicht mit unendlicher Multiplizität
in den betrachteten Raum eingehen — deshalb die Restriktion auf
$\mathcal H_{\mathrm{rel}}^{\mathrm{eff}} = \ker(J^-)^\perp$.

Zweites Kriterium aus NEU-56 §7: *„Spurklasse-Kriterium über $K_{pq}$ (NEU-51): falls
$\sum_p \operatorname{Tr}\lvert M_p(z)\rvert < \infty$ gleichmäßig, ergäbe sich diskretes
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

> **Sperrvermerk.** Ein endlicher Jacobi- oder Graphoperator besitzt trivialerweise
> kompakten Resolventen. HP-2 betrifft **nicht** die endlichen Trunkierungen, sondern die
> unendliche bzw. renormierte Realisierung. Der Schluss
> $$D_N \text{ hat diskretes Spektrum} \;\Longrightarrow\; D_\infty \text{ hat kompakten Resolventen}$$
> ist **unzulässig** und in keiner Quelle behauptet.

---

## 8. Zielnormalform — revidiert

Der im Auftrag vorgeschlagene Zielzustand lautete: $\exists\,\tilde L\ge 1$ mit
$\lVert J^-x\rVert \le a\lVert\tilde Lx\rVert + b\lVert x\rVert$,
$\lVert\tilde Lx\rVert \le C(\lVert D_{\mathrm{rel}}x\rVert + \lVert x\rVert)$ und
$(\tilde L+i)^{-1}\in\mathcal K(\mathcal H_{\mathrm{rel}})$.

Nach §5.2 kollabiert das: Mit $\tilde L = (1+(J^-)^2)^{1/2}$ sind die ersten beiden
Bedingungen automatisch erfüllt. Die Zielnormalform reduziert sich auf

$$
\boxed{\
\bigl(1+(J^-)^2\bigr)^{-1/2} \in \mathcal K\bigl(\mathcal H_{\mathrm{rel}}^{\mathrm{eff}}\bigr)
\quad\text{auf } \mathcal D_0^{\mathrm{eff}},
\ }
$$

zuzüglich der noch offenen Grundlagen: exakter Schur-Test (55.9) und Nelson-Bed. 1 (55.5)
für die Selbstadjungiertheit, auf der alles aufbaut.

### Die drei möglichen Ausgänge

| Ausgang | Bedeutung |
|---|---|
| **kompakt** | HP-2 erfüllt; HP-3 bis HP-6 werden anschließend prüfbar; Weg A wieder offen |
| **nicht kompakt** | HP-2 für diesen Kandidaten `✗[M]`. Da die $\tilde L$-Klasse auf einen Punkt reduziert ist, wäre das eine **erheblich stärkere No-Go-Klasse** als NEU-56 — nicht mehr „dieser Mechanismus", sondern „jeder Vergleichsoperator in der erzwungenen Ordnungsklasse" |
| **unentschieden** | Knoten bleibt offen, aber mit typkorrekt gestellter Frage statt der bisherigen typwidrigen Singulärwertformulierung |

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
| No-Go betrifft nur diesen $L$ mit skalarem $\gamma_N$; A′, B1, B2 verbraucht | `✓[M]` |
| Rekalibrierungen scheitern in **beiden** Ordnungsrichtungen | `✓[M]` abgeleitet (§5.1) |
| $\tilde L$-Klasse auf $(1+(J^-)^2)^{1/2}$ reduziert | `✓[M]` (56 §7) |
| Typkorrektur: relevantes Objekt ist $(1+(J^-)^2)^{-1/2}$, nicht $s_k(J^-)$ | `✓[M]` |
| Kompaktheit von $(1+(J^-)^2)^{-1/2}$ auf $\mathcal H_{\mathrm{rel}}^{\mathrm{eff}}$ | **`❓[O]`** — der Knoten |
| Spurklassekriterium $\sum_p\operatorname{Tr}\lvert M_p(z)\rvert<\infty$ | `❓[O]` (NEU-51) |
| Exakter Schur-Test (55.9), Nelson-Bed. 1 (55.5) | `❓[O]` / `✓/⚠[M]` heuristisch |
| **Gesamtstatus `[O-223-1]`** | **`✓[M]`** (Typisierung), Folgeknoten offen |

---

## 10. Nächster atomarer Knoten

$$
\boxed{\ [O\text{-}223\text{-}2\text{-compactness-of-inverse-modulus-on-effective-space}] \ }
$$

Zu klären, in dieser Reihenfolge:

1. **Kerngröße.** Ist $\dim\ker(J^-) = \infty$? Falls ja, ist die Restriktion auf
   $\mathcal H_{\mathrm{rel}}^{\mathrm{eff}}$ zwingend (55.PRE) — und die Wohldefiniertheit
   der Projektion zu belegen.
2. **Eigenwertdivergenz.** Divergiert das Spektrum von $\lvert D_{\mathrm{rel}}\rvert$ auf
   $\mathcal H_{\mathrm{rel}}^{\mathrm{eff}}$ mit endlicher Multiplizität?
3. **Alternativkriterium.** Trägt $\sum_p\operatorname{Tr}\lvert M_p(z)\rvert<\infty$
   gleichmäßig auf Kompakta (NEU-51)?
4. **Grundlagen nachziehen.** Exakter Beweis von (55.9) und (55.5) — sie tragen die
   Selbstadjungiertheit, auf der die gesamte Frage beruht.

---

## Abhängigkeiten

| Referenz | Verwendet für |
|---|---|
| NEU-52 | Graphbasis $\eta_a$; Warnung 52.D0 (Graphbasis $\neq$ Eigenbasis) |
| NEU-53 | Operatorstatus $D_{\mathrm{rel}}$, Weg A / Weg B |
| NEU-54 | (54.SEP), $\mathcal D_0$, $L$ und $\ell(a)$, (N1)/(N2), flache Achsen, (K), (54.17) |
| NEU-55 | $\mathcal H^{\mathrm{eff}}_{\mathrm{rel}}$, (55.PRE), Matrixkriterien, Kommutatorformel, $\gamma_N$-Doppelrolle |
| NEU-56 | Rate $\gamma_N\le K/(N\log N)$, Satz 56.1/56.2/56.3, Optionen B1/B2, (56.12), $\tilde L$-Agenda §7 |
| NEU-51 | Spurklassekriterium via $K_{pq}$ |
| NEU-220u | HP-1–HP-7, insbesondere HP-2/HP-3 |
