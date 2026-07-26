# NEU-224 — Kernbestimmung: flache Achsen, Antisymmetrisierung und der effektive Raum

**Katalog-ID:** NEU-224
**Knoten:** `[O-223-2a]` Kernbestimmung · `[O-223-2b]` reduzierender Spektralraum
**Stand:** 26. Juli 2026
**Vorgänger:** NEU-223 Rev. 2
**Typ:** Explizite Spaltenrechnung, danach Kernrekursion — quellenkritisch

---

## 0. Auditurteil

Die Rechnung war nicht durchführbar wie geplant, weil eine Voraussetzung nicht hält.

$$
\boxed{\ \text{Die Trägeraussage (55.3) beschreibt } \Theta_N, \ \textbf{nicht } J^-. \ \text{Sie ist mit } (J^-)^*=-J^- \ \text{(54.3) unverträglich.}\ }
$$

Daraus folgen drei Korrekturen und ein positives Ergebnis:

1. **Die flache Achse $r=0$ ist keine flache Achse von $J^-$.** NEU-54 §5 gilt nur für $\Theta_N$. `✓[M]_neg`
2. **Die Faser mit trivialer Teilermenge bleibt Kern** — sie ist gegen die Antisymmetrisierung robust und unendlichdimensional. `✓[M]`
3. **Damit ist `[O-223-2d]` auf dem vollen Raum bereits negativ entschieden.** `✓[M]`
4. **Der effektive Raum (55.0) ist nicht $(\ker D_{\mathrm{rel}})^\perp$**, sondern echt kleiner. `✓[M]_neg`

---

## 1. Drei Kernbegriffe, strikt getrennt

Sei $J_0^-$ der auf dem algebraischen Kern $\mathcal D_0$ (54.1) definierte Matrixoperator und
$D_{\mathrm{rel}} = \overline{iJ_0^-}$ (55.18, 56.9). Getrennt zu bestimmen sind:

$$
\ker_{\mathrm{alg}} J_0^- = \{x\in\mathcal D_0 : J_0^- x = 0\},
\qquad
\ker \overline{J_0^-},
\qquad
\ker D_{\mathrm{rel}} .
$$

Die letzten beiden stimmen überein, sobald die Abschlussidentität feststeht:
$\ker D_{\mathrm{rel}} = \ker\overline{J_0^-}$, da $D_{\mathrm{rel}} = i\,\overline{J_0^-}$.

> **Nicht automatisch.** $\ker\overline{J_0^-} = \overline{\ker_{\mathrm{alg}}J_0^-}$ ist **unbewiesen**.
> Der Abschluss kann zusätzliche Nullvektoren enthalten, die nur als Graphnormgrenzen
> algebraischer Folgen sichtbar werden. Behandelt in §6. `❓[O]`

Gesichert in dieser Richtung ist nur die Inklusion: ist $x\in\mathcal D_0$ mit $J_0^-x=0$, so
$x\in\ker\overline{J_0^-}$; und da der Kern eines abgeschlossenen Operators abgeschlossen ist,
gilt $\overline{\operatorname{span}}\,\ker_{\mathrm{alg}}J_0^- \subseteq \ker D_{\mathrm{rel}}$. `✓[M]`

---

## 2. Quellenkritik: $J^-$ ist antisymmetrisiert, $\Theta_N$ nicht

### 2.1 Die Ursprungsformel

$$
\Theta(e_rV_n) = r\log(n)\,e_{r+n}V_n
\tag{NEU-27 Z.165, NEU-31 Z.208, NEU-33 Z.164}
$$

bzw. mit Normierung $\Theta_N(e_rV_n) = -\gamma_N\,r\log(n)\,e_{r+n}V_n$ (NEU-55 Z.46, NEU-62 Z.98).

Das ist eine **reine Aufwärtsverschiebung**: $r \mapsto r+n$, mit $n$ **erhalten**.
Ein solcher einseitiger gewichteter Shift kann nicht schiefadjungiert sein.

### 2.2 $J^-$ ist die Antisymmetrisierung

$$
\boxed{\ J_N^- := \tfrac12\bigl(\Theta_N - \Theta_N^\dagger\bigr) \ }
\tag{37.1}
$$

NEU-37 (Z. 124) nennt dies ausdrücklich *„die schiefadjungierte Kopplung aus NEU-35"*.
NEU-70 (Z. 39) bestätigt: *„A_N trägt Gewichte $\Theta_{ba}\sim r\log(n)$ und ist
antisymmetrisiert."*

Damit trägt $J^-$ **beide** Kantenrichtungen: $r\to r+n$ aus $\Theta_N$ und $r\to r-n$ aus
$\Theta_N^\dagger$. Erst so ergibt sich $(J^-)^*=-J^-$ (54.3) und die Symmetrie von $iJ^-$.

> **Normierungsdiskrepanz `⚠[M]`.** NEU-35 (Z. 220), NEU-62 (Z. 98) schreiben
> $J_N^- = \frac{1}{2i}(\Theta_N-\Theta_N^{Wres})$, NEU-37 (37.1) dagegen
> $J_N^-=\frac12(\Theta_N-\Theta_N^\dagger)$. Die Varianten unterscheiden sich um den Faktor
> $i$ und sind **nicht** beide schiefadjungiert: nur die NEU-37-Fassung erfüllt
> $(J^-)^*=-J^-$; die NEU-35-Fassung wäre selbstadjungiert, womit $D_{\mathrm{rel}}=\overline{iJ^-}$
> schiefadjungiert würde. NEU-54/55/56 verwenden implizit die NEU-37-Konvention. Der Kern ist
> von der Diskrepanz **nicht** betroffen (Faktor $i$ ändert ihn nicht); die Konvention sollte
> dennoch vereinheitlicht werden.

### 2.3 Der Defekt in (55.3)

NEU-55 setzt in (55.1) $J^-\eta_a = \sum_b \Theta_{ba}\eta_b$ und leitet in (55.3) ab:

> *„$\Theta_{ba}\neq 0$ nur für $b=(p',m',r+n,u')$ mit $m'=m$, $n\mid m$."*

$$
\boxed{\ \text{Das ist der Träger von } \Theta_N, \ \text{nicht der von } J^- = \tfrac12(\Theta_N-\Theta_N^\dagger). \ }
$$

Der Träger von $J^-$ ist symmetrisch: $r\to r\pm n$. `✓[M]_neg` gegen (55.1)/(55.3).

> **Reichweite dieser Korrektur.** Betroffen ist die **Kernbestimmung** und die Definition des
> effektiven Raums. **Nicht betroffen** sind die Schätzungen (55.5)/(55.9)/(55.12): sie sind
> Betragsabschätzungen, und die Rückwärtskanten haben denselben Betrag wie die Vorwärtskanten.
> Sie ändern nur Konstanten (Faktor $\le 2$). Die Obstruktion aus NEU-56 bleibt unberührt.

---

## 3. `[O-223-2a.1]` — Explizite Spaltenrechnung für die flachen Achsen

Geprüft wird die vollständige Spalte, nicht nur einzelne verschwindende Koeffizienten.

### 3.1 Achse $r=0$ — **kein Kernvektor** `✓[M]_neg`

NEU-54 §5 behauptet: *„$r = 0$: Kopplung verschwindet, $\Theta_N(e_0V_n) = 0$"*, und schließt
daraus, $J^-$ wirke dort wie $0$ (Z. 147).

Die erste Aussage ist richtig, die Folgerung nicht. Die Adjungiertenkomponente liefert

$$
\bigl(\Theta_N^\dagger\bigr)_{ba} = \overline{(\Theta_N)_{ab}} ,
$$

also für $a=(\dots,r=0,\dots)$ die eingehenden Kanten aus $r=-n$ mit Gewicht

$$
(\Theta_N)_{a,(\dots,-n,\dots)} = -\gamma_N\,(-n)\log n = +\gamma_N\,n\log n \ \neq\ 0 \qquad (n>1).
$$

Folglich

$$
\boxed{\ J^-\eta_{(p;m;0,u)} = -\tfrac12\,\Theta_N^\dagger\eta_{(p;m;0,u)} \ \neq\ 0 \qquad\text{sobald } m \text{ einen Teiler } n>1 \text{ besitzt.} \ }
$$

Die Spalte ist **nicht** null. Die $r=0$-Achse ist eine flache Achse von $\Theta_N$, aber
nicht von $J^-$.

### 3.2 Achse mit trivialer Teilermenge — **echter Kernvektor** `✓[M]`

NEU-54 §5 zweiter Fall: *„$n=1$: $\log(1)=0$, Kopplung verschwindet."*

Hier verschwindet **beides**: die Vorwärtskante $r\to r+1$ hat Gewicht $r\log 1 = 0$, und die
Rückwärtskante aus $r-1$ hat Gewicht $(r-1)\log 1 = 0$. Da $\Theta$ die Faser $n$ erhält
($e_rV_n\mapsto e_{r+n}V_n$), ist die gesamte Faser $n=1$ invariant und

$$
\boxed{\ J^-\big|_{\{n=1\}} = 0 . \ }
$$

In der $(p,m,r,u)$-Indizierung entspricht das $m=1$: die einzige Teilerbedingung $n\mid 1$
erzwingt $n=1$, also $\log n = 0$ in beiden Richtungen.

$$
\boxed{\ \mathcal K_{\mathrm{flat}} := \overline{\operatorname{span}}\{\eta_{p;1;r,u}\} \ \subseteq\ \ker D_{\mathrm{rel}} \ }
$$

Die drei vom Auditauftrag geforderten Einzelpunkte:

| Punkt | Befund |
|---|---|
| Basisvektoren in der Kerndomäne | `✓[M]` — $\eta_a\in\mathcal D_0$ nach (54.1) |
| Vollständige Spalte verschwindet | `✓[M]` — beide Kantenrichtungen tragen $\log 1 = 0$ |
| Lineare Unabhängigkeit / Orthonormalität | `✓[M]` **quellenintern**: (55.4) setzt $\lVert J^-\eta_a\rVert^2=\sum_b\lvert\Theta_{ba}\rvert^2$ an, was genau dann gilt, wenn $\{\eta_b\}$ orthonormal ist. Eine explizite Definition der $\eta$-Familie samt Skalarprodukt fehlt in den Quellen — `⚠[M]` |

### 3.3 Unendliche Dimension

Die Faser $\{\eta_{p;1;r,u}\}$ läuft über alle $r$ (und alle $p,u$). Sie ist damit
unendlichdimensional:

$$
\boxed{\ \dim\ker D_{\mathrm{rel}} = \infty . \ }
$$

**$N$-Unabhängigkeit:** Das Verschwinden beruht auf $\log 1 = 0$, nicht auf $\gamma_N$. Es
überlebt daher jeden Grenzübergang $N\to\infty$ und jede Wahl von $\gamma_N$. `✓[M]`

---

## 4. Folgerung: `[O-223-2d]` auf dem vollen Raum negativ

Auf $\ker D_{\mathrm{rel}}$ wirkt $(1+D_{\mathrm{rel}}^2)^{-1/2}$ als **Identität**. Ein
Operator, der auf einem unendlichdimensionalen Teilraum die Identität ist, ist nicht kompakt.

$$
\boxed{\ \bigl(1+D_{\mathrm{rel}}^2\bigr)^{-1/2} \notin \mathcal K(\mathcal H_{\mathrm{rel}}), \qquad (D_{\mathrm{rel}}-i)^{-1} \notin \mathcal K(\mathcal H_{\mathrm{rel}}). \ }
$$

$$
\boxed{\ D_{\mathrm{rel}} \ \text{besitzt auf dem vollen relativen Hilbertraum keinen kompakten Resolventen.} \quad \times[M] \ }
$$

**Umfang.** Ausgeschlossen ist HP-2 für die **unreduzierte** Realisierung. **Nicht
ausgeschlossen** ist HP-2 für $D_{\mathrm{rel}}\vert_{(\ker D_{\mathrm{rel}})^\perp}$ — das
bleibt die eigentliche Frage. Ebenfalls **nicht ausgeschlossen** ist, dass eine anders
konstruierte Realisierung $H_X$ von Objekt X HP-2 erfüllt.

---

## 5. `[O-223-2b]` — Zerlegt in eine triviale und eine offene Hälfte

### 5.1 Die reduzierende Eigenschaft ist automatisch `✓[M]`

Da $D_{\mathrm{rel}}$ selbstadjungiert ist (56.9), gilt nach dem Spektralsatz

$$
\ker D_{\mathrm{rel}} = E_{D_{\mathrm{rel}}}(\{0\})\,\mathcal H_{\mathrm{rel}},
\qquad\text{also}\qquad
\bigl(\ker D_{\mathrm{rel}}\bigr)^{\perp} = E_{D_{\mathrm{rel}}}\bigl(\mathbb R\setminus\{0\}\bigr)\,\mathcal H_{\mathrm{rel}} .
$$

Der Raum $(\ker D_{\mathrm{rel}})^\perp$ reduziert $D_{\mathrm{rel}}$ also **unmittelbar**.
NEU-223 Rev. 2 hatte das zu Unrecht als eigenen schweren Knoten geführt — korrigiert.

### 5.2 Offen bleibt allein die Identifikation mit der Quelldefinition

NEU-55 (55.0) definiert $\mathcal H^{\mathrm{eff}}_{\mathrm{rel}} := \overline{\operatorname{Ran}(J^-)} = \ker(J^-)^\perp$.
Für dicht definierte abgeschlossene $T$ gilt $\overline{\operatorname{Ran}T} = (\ker T^*)^\perp$;
bei schiefadjungiertem $\overline{J_0^-}$ folgt
$\overline{\operatorname{Ran}\overline{J_0^-}} = (\ker\overline{J_0^-})^\perp$. Zu auditieren
bleibt die Gleichheit mit dem **Präabschluss**-Bild:

$$
\overline{\operatorname{Ran}(J_0^-)} \;\overset{?}{=}\; \overline{\operatorname{Ran}\overline{J_0^-}} \;=\; \bigl(\ker D_{\mathrm{rel}}\bigr)^{\perp} .
\qquad \text{`❓[O]`}
$$

### 5.3 Der Defekt in (55.0) `✓[M]_neg`

NEU-55 (55.0) präzisiert $\mathcal D_0^{\mathrm{eff}}$ als *„$r\neq 0$ **und** $m>1$"*.

Nach §3.1 gehört die $r=0$-Achse jedoch **nicht** zum Kern. Die Bedingung $r\neq0$ entfernt
also Vektoren, die im effektiven Raum verbleiben müssten:

$$
\boxed{\ \mathcal H^{\mathrm{eff}}_{\mathrm{rel}} \ \text{im Sinne von (55.0)} \ \subsetneq\ \bigl(\ker D_{\mathrm{rel}}\bigr)^{\perp} . \ }
$$

Der so definierte Raum ist **echt kleiner** als der Spektralraum und — da die $r=0$-Vektoren
über die Rückwärtskanten an $r=\pm n$ koppeln — **nicht invariant** unter $J^-$. Er reduziert
$D_{\mathrm{rel}}$ daher nicht. Die korrekte Restriktion ist
$\{m>1\}$ allein, nicht $\{r\neq0\}\cap\{m>1\}$.

---

## 6. `[O-223-2a.3/4]` — Restkern und Abschlusskontrolle: offen

### 6.1 Warum der Träger den Kern nicht bestimmt

Aus $\Theta_{ba}\neq 0 \Rightarrow n\mid m$ kennt man nur den Träger. Ein Graph ohne isolierte
Knoten kann dennoch nichttrivialen Kern haben, durch linear abhängige Zeilen, symmetrische
oder antisymmetrische Auslöschungen, mehrere Pfade mit entgegengesetzten Koeffizienten oder
unendliche $\ell^2$-Lösungen von $\sum_a\Theta_{ba}x_a=0$. Der Restkern

$$
\mathcal K_{\mathrm{res}} := \ker D_{\mathrm{rel}} \ominus \mathcal K_{\mathrm{flat}}
$$

muss daher über die **gewichteten Gleichungen** bestimmt werden, nicht über den
Teilbarkeitsgraphen. `❓[O]`

### 6.2 Vorhandene Gradierung

Aus (55.3) und $\Theta(e_rV_n)=r\log(n)e_{r+n}V_n$ ist $m$ (bzw. $n$) **erhalten**. Damit

$$
\mathcal H_{\mathrm{rel}} = \bigoplus_{m} \mathcal H_m, \qquad \ker D_{\mathrm{rel}} = \bigoplus_m \ker\bigl(D_{\mathrm{rel}}\vert_{\mathcal H_m}\bigr),
$$

und die Kernfrage zerfällt sektorweise. Sektor $m=1$: vollständig Kern (§3.2). Sektoren
$m>1$: offen. `❓[O]`

Innerhalb eines Sektors $m>1$ ist $J^-\vert_{\mathcal H_m}$ eine schiefsymmetrische
Bandmatrix in $r$ mit Sprüngen $\pm n$ über die Teiler $n\mid m$, $n>1$, und Gewichten
$\propto \gamma_N r\log n$. Die Rekursion nach §223-2a.3 ist auf diese Sektoren anzusetzen.

### 6.3 Abschlusskontrolle

Zu prüfen bleibt, ob aus $x_k\in\mathcal D_0$, $x_k\to x$, $J_0^-x_k\to 0$ notwendig
$x\in\overline{\mathcal K_{\mathrm{flat}}}$ folgt. Hinreichend wäre eine coercive Abschätzung

$$
\lVert x\rVert \le C\lVert J_0^-x\rVert, \qquad x\in\mathcal D_0\cap\mathcal K_{\mathrm{flat}}^{\perp} .
$$

Eine solche uniforme Schranke schlösse nicht nur zusätzliche Abschlusskerne aus, sondern
lieferte eine **Spektrallücke bei $0$** auf dem reduzierten Raum. `❓[O]`

> **Warnung.** Eine Spektrallücke bei $0$ ist **nicht** dasselbe wie kompakter Resolvent.
> Auch mit Lücke kann wesentliches Spektrum bei $\lambda\neq0$ oder eine beschränkte Folge
> nichtverschwindender Eigenwerte unendlicher Multiplizität vorliegen.

---

## 7. Statusbilanz

| Aussage | Status |
|---|---|
| $J_N^- = \frac12(\Theta_N-\Theta_N^\dagger)$, antisymmetrisiert | `✓[M]` (37.1, NEU-35, NEU-70) |
| Normierungsdiskrepanz $\frac12$ (NEU-37) gegen $\frac{1}{2i}$ (NEU-35/62) | `⚠[M]` — nur NEU-37 ist schiefadjungiert |
| (55.1)/(55.3) beschreiben den Träger von $\Theta_N$, nicht von $J^-$ | `✓[M]_neg` |
| Betragsabschätzungen (55.5)/(55.9)/(55.12) davon **unberührt** | `✓[M]` |
| NEU-54 §5: $r=0$ ist flache Achse von $J^-$ | `✓[M]_neg` **widerlegt** |
| Faser $m=1$ (bzw. $n=1$) vollständig im Kern, beide Kantenrichtungen | `✓[M]` |
| $\dim\ker D_{\mathrm{rel}} = \infty$, unabhängig von $\gamma_N$ und $N$ | `✓[M]` |
| $(1+D_{\mathrm{rel}}^2)^{-1/2}\notin\mathcal K(\mathcal H_{\mathrm{rel}})$ — voller Raum | **`✗[M]`** |
| $(\ker D_{\mathrm{rel}})^\perp$ reduziert $D_{\mathrm{rel}}$ automatisch | `✓[M]` (Spektralsatz) |
| $\overline{\operatorname{Ran}(J_0^-)} = (\ker D_{\mathrm{rel}})^\perp$ (Präabschluss) | `❓[O]` |
| (55.0) $\mathcal D_0^{\mathrm{eff}}$ mit $r\neq0$: echt zu klein, nicht invariant | `✓[M]_neg` |
| Orthonormalität der $\eta$-Familie explizit definiert | `⚠[M]` — nur implizit über (55.4) |
| $(r,n)$- gegen $(p,m,r,u)$-Indexübersetzung explizit | `⚠[M]` — in keiner Quelle ausgeführt; beide Lesarten führen hier zum selben Ergebnis |
| Restkern in den Sektoren $m>1$ | `❓[O]` `[O-223-2a.3]` |
| Abschlusskontrolle / coercive Schranke auf $\mathcal K_{\mathrm{flat}}^\perp$ | `❓[O]` `[O-223-2a.4]` |

---

## 8. Nachfolgeknoten

$$
\boxed{\ [O\text{-}224\text{-}1\text{-reduced-spectral-type-on-the-corrected-effective-space}] \ }
$$

| Teilknoten | Aufgabe |
|---|---|
| `[O-224-1a]` | Effektiven Raum **neu definieren** als $\{m>1\}$-Anteil statt (55.0); Invarianz und Reduktion nachweisen |
| `[O-224-1b]` | Restkern sektorweise: schiefsymmetrische Bandmatrix in $r$ mit Sprüngen $\pm n$, $n\mid m$, $n>1$ |
| `[O-224-1c]` | Coercive Schranke $\lVert x\rVert\le C\lVert J_0^-x\rVert$ auf $\mathcal K_{\mathrm{flat}}^\perp$ — Spektrallücke bei $0$? |
| `[O-224-1d]` | Graphnormbeschränkte Orthonormalfolge im reduzierten Raum konstruieren oder ausschließen (negativer Zeuge bzw. Weyl-Folge) |

**Vorab zu bereinigen (Redaktionsschulden):** Normierungskonvention für $J_N^-$ vereinheitlichen;
explizite Definition der $\eta$-Familie samt Skalarprodukt; $(r,n)\leftrightarrow(p,m,r,u)$-Übersetzung.

---

## Abhängigkeiten

| Referenz | Verwendet für |
|---|---|
| NEU-27 (Z.165), NEU-31 (Z.208), NEU-33 (Z.164) | $\Theta(e_rV_n)=r\log(n)e_{r+n}V_n$ |
| NEU-35 (Z.220), NEU-62 (Z.98) | $J_N^-=\frac{1}{2i}(\Theta_N-\Theta_N^{Wres})$ — abweichende Normierung |
| NEU-37 (37.1) | $J_N^-=\frac12(\Theta_N-\Theta_N^\dagger)$, schiefadjungiert |
| NEU-70 (Z.39) | Antisymmetrisierung bestätigt |
| NEU-53, NEU-54 | $\mathcal D_0$, (54.3) Schiefadjungiertheit, (54.12) flache Achsen, (54.SEP) |
| NEU-55 | (55.0) effektiver Raum, (55.1)/(55.3) Träger, (55.4) Orthonormalität implizit, (55.PRE) |
| NEU-56 | (56.9) Selbstadjungiertheit, §4 RH braucht nur SA |
| NEU-223 Rev. 2 | Zielnormalform, Knotenstruktur `[O-223-2a–d]` |
