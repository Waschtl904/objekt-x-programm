# NEU-226 — Quellenaudit NEU-51/77: globaler Feshbach-Transfer, Schattenklasse, Primkanalüberlappung

**Katalog-ID:** NEU-226
**Knoten:** `[O-225-2a]`–`[O-225-2f]`
**Stand:** 26. Juli 2026
**Vorgänger:** NEU-225
**Typ:** Quellenaudit von NEU-51 und NEU-77 — beide lagen der Bibliothekssuche nicht vor

---

## 0. Auditurteil

Drei Befunde, davon einer gegen ein eigenes Blatt.

1. **Der endliche-$N$-Befund gilt nicht.** $K_N(s)$ ist nach (51.2)/(51.3) **nicht**
   endlich-rangig; $\mathfrak p_N$ ist nicht $\bigoplus_{p\le N}\mathbb C\varepsilon_p$.
   $\mathcal S_2\setminus\mathcal S_1$ ist bei festem $N$ **nicht** ausgeschlossen. `✓[M]_neg`
2. **`[O-225-2c]` ist in der Quelle beantwortet.** Satz 51.3 (51.5): $\mathcal K_N\neq\bigoplus_p K_p$.
   Der Mechanismus ist die **Überlappung der Primkanäle** in der BC-Algebra. `✓[M]`
3. **Damit ist meine Konventionsfestlegung aus NEU-225 §1.2 falsch.** Die $\eta$-Familie ist
   **nicht** orthonormal über verschiedene Primkanäle. `✓[M]_neg` gegen NEU-225. Zurückgerollt.

Und ein Blocker:

4. **(51.3)/(51.4)/(51.7) setzen eine Eigenbasis von $D_{\mathrm{rel}}$ voraus**, die nach
   NEU-225 nicht existiert. Die Schattenklassenkriterien sind in ihrer jetzigen Form nicht
   auswertbar. `✓[M]_neg`

---

## 1. `[O-225-2b]` — Was die Quellen tatsächlich definieren

### 1.1 $V_p$ ist $C_p^{\mathrm{rel}}$ — die Identifikation steht in der Quelle

NEU-51 Kopfzeile: *„Explizite Basisformel für $K_{pq}(s)$ aus $V_p = C_p^{\mathrm{rel}}$."*
Die befürchtete stillschweigende Gleichsetzung findet also nicht statt; sie ist quellenseitig
gesetzt. `✓[M]`

$$
\mathcal K_N(s) = V_N^*(D_{\mathrm{rel}}-s)^{-1}V_N, \qquad V_N = \sum_{p\le N}V_p
\tag{51.0}
$$

$$
\mathcal K_N(s) = \sum_{p,q\le N}K_{pq}(s), \qquad K_{pq}(s) := V_p^*(D_{\mathrm{rel}}-s)^{-1}V_q
\tag{51.1}
$$

> **Typhinweis.** $V_N$ ist eine **Summe**, keine direkte Summe. Die Bilder $\operatorname{Ran}V_p$
> überlappen — genau daraus entstehen die Kreuzterme (§3).

### 1.2 Die Kopplungsform

Aus $\tilde\omega_2(e_uV_p, e_sV_m) = -u\,s\,\log(p)\,e_{u+ps}V_{pm}$ (NEU-43/44):

$$
\boxed{\ V_p(e_sV_m) = \sum_u (-u\,s\,\log p)\,\eta_{p;m;s,u}, \qquad \eta_{p;m;s,u}\sim e_{u+ps}V_{pm}\ }
\tag{51.2}
$$

### 1.3 Die entscheidende offene Wahl

NEU-51 §1 wörtlich: *„Die Summationsreichweite über $u$ ist noch nicht fixiert
(Regulierung)."* Zulässige Optionen: $u\in\mathbb Z$ mit Gewichtsabschneidung; $u$ durch den
$p$-Kanal-Projektor fixiert; endliche Fourierprojektion $\lvert u\rvert\le U_p$. Und:

$$
\boxed{\ \text{„Diese Wahl entscheidet später über } \mathcal S_1 \text{ vs. } \mathcal S_2\text{."} \ }
$$

Status dort: `✓/⚠[M]` — abhängig von der Regulierungswahl.

$$
\boxed{\ \text{`[O-225-2b]` ist damit \textbf{keine Definitionslücke, sondern ein Freiheitsgrad}: der } u\text{-Regulator.}\ }
$$

---

## 2. `[O-225-2a]` — Der endliche-$N$-Befund gilt nicht

### 2.1 Was vorausgesetzt war

Angenommen war $\mathfrak p_N = \bigoplus_{p\le N}\mathbb C\varepsilon_p$ mit
$\dim\mathfrak p_N = \pi(N)<\infty$, also $\operatorname{rank}K_N(z)\le\pi(N)$ und damit
$K_N(z)\in\mathcal S_1$.

### 2.2 Was die Quelle sagt

Nach (51.2) ist die Quelldomäne von $V_p$ von den $e_sV_m$ über **alle** $s,m$ aufgespannt —
unendlichdimensional. Entsprechend trägt die Matrix von $K_{pq}$ Doppelindizes:

$$
K_{pq}(s)_{(r,n),(t,m)}
= r\,t\,\log p\,\log q \sum_{u,v} u\,v\; R_{\mathrm{rel}}(s)\bigl[(p;n;r,u),(q;m;t,v)\bigr]
\tag{51.3}
$$

Jeder Primkanal trägt also einen vollen $(r,n)$-Index. Der Kanalraum ist **pro Primzahl**
unendlichdimensional.

Bestätigend: die explizite $\mathcal S_1$-Bedingung

$$
\sum_p (\log p)^2 \sum_{n,r,u}\frac{u^2r^2}{\lvert\lambda_{p;n;r,u}-s\rvert} < \infty
\tag{51.7}
$$

summiert **innerhalb** jedes Primkanals über $n,r,u$ und wird von NEU-51 als `?[O]` geführt
(*„Konvergenz von (51.7) ausständig"*). Bei endlichem Rang wäre sie trivial konvergent.

$$
\boxed{\ \operatorname{rank}K_N(z)\le\pi(N) \ \text{ist falsch.} \quad K_N(z)\in\mathcal S_1 \ \text{ist bei festem } N \ \textbf{nicht} \ \text{gesichert.} \quad \checkmark[M]_{\mathrm{neg}}\ }
$$

### 2.3 Konsequenz

$\mathcal S_2\setminus\mathcal S_1$ ist bei festem $N$ **nicht** ausgeschlossen. Die Trennung
zwischen endlicher Trunkierung und globalem Limes bleibt methodisch richtig und notwendig —
aber sie liefert hier **kein** No-Go, sondern nur eine offene Konvergenzfrage.

Ebenso: $\det\nolimits_2$ ist bei festem $N$ nicht durch einen gewöhnlichen endlichen
Determinanten ersetzbar. NEU-51 (51.8) führt $D_{\mathrm{scatt},N}(s)=\det_2(1-K_N(s))$
ausdrücklich **für endliches $N$**, mit der Spurkorrektur $\exp(\operatorname{Tr}K_N(s))$ in
(51.9), die zu $D_{\mathrm{Jac},N}$ gehört. `✓[M]`

---

## 3. `[O-225-2c]` — Der Mechanismus der Kreuzterme

### 3.1 Die Quellenaussage

$$
\boxed{\ \mathcal K_N \neq \bigoplus_{p\le N}K_p \ }
\tag{51.5}
$$

Satz 51.3 wörtlich: *„Für $p\neq q$ ist $K_{pq}(s)\neq 0$ generisch, weil $D_{\mathrm{rel}}$ auf
dem gemeinsamen Graphraum operiert und die $\eta_{p;n;r,u}$ **keine kanaldiagonale Basis
erzwingen**."*

Und die Gegenprobe, Z. 101: *„Ausnahme: Falls $D_{\mathrm{rel}}$ kantendiagonal ist, fallen
Off-Diagonale weg — aber dann wäre $R_{\mathrm{rel}}(s)[(p;n;r,u),(q;m;t,v)]=0$ für $p\neq q$,
was eine explizite Eigenschaft der Basis ist, nicht der allgemeinen Situation. ✗[M] als
Standardfall."*

### 3.2 Der Mechanismus ist explizit angebbar

Nach (51.2) gilt $\eta_{p;m;s,u}\sim e_{u+ps}V_{pm}$. Verschiedene Primkanäle landen auf
**demselben** BC-Element:

$$
\eta_{2;3;s,u} \sim e_{u+2s}V_{6}, \qquad \eta_{3;2;s',u'} \sim e_{u'+3s'}V_{6},
$$

und für $u+2s = u'+3s'$ fallen beide zusammen. Allgemein: $V_{pm}$ hängt nur vom Produkt ab,
und der Charakterindex $u+ps$ ist über $(u,s)$ mehrfach erreichbar.

$$
\boxed{\ \text{Der Kreuztermmechanismus ist die \textbf{Überlappung der Primkanalbilder} in der BC-Algebra, nicht eine Primmischung durch } D_{\mathrm{rel}}. \ }
$$

Das ist die Antwort auf `[O-225-2c]`: nicht „$D_{\mathrm{rel}}$ mischt Primkanten" und nicht
„$V$ ist nicht primdiagonal", sondern **die $\eta$-Familie ist über Primkanäle hinweg nicht
orthogonal**. `✓[M]`

### 3.3 Verträglich mit NEU-225

$D_{\mathrm{rel}}$ selbst bleibt kanalerhaltend — unter der BC-Identifikation (51.2) wirkt
$\Theta(e_rV_n)=r\log(n)e_{r+n}V_n$ mit $r=u+ps$, $n=pm$ als $s\mapsto s+m$ bei festem
$p,m,u$. Die Off-Diagonalität von $\mathcal K_N$ entsteht **nicht** im Operator, sondern in
der nichtorthogonalen Kopplung $V_p$. Beides ist widerspruchsfrei. `✓[M]`

---

## 4. Rückrollung: die $\eta$-Familie ist nicht orthonormal

NEU-225 §1.2 hatte verbindlich festgelegt:
$\langle\eta_{p;m;r,u},\eta_{p';m';r',u'}\rangle = \delta_{pp'}\delta_{mm'}\delta_{rr'}\delta_{uu'}$,
begründet über (55.4).

$$
\boxed{\ \text{Das ist falsch und wird zurückgerollt.} \quad \checkmark[M]_{\mathrm{neg}} \ \text{gegen NEU-225 §1.2.}\ }
$$

**Begründung.** (51.4) behandelt $\langle\eta_\alpha,\eta_{p;n;r,u}\rangle$ als generische
Überlappungen; Satz 51.3 beruht ausdrücklich darauf, dass die $\eta$ *keine kanaldiagonale
Basis erzwingen*; und (51.2) zeigt die Mehrfachbelegung explizit.

**Was bleibt.** (55.4) — $\lVert J^-\eta_a\rVert^2=\sum_b\lvert\Theta_{ba}\rvert^2$ — verlangt
Orthonormalität nur **innerhalb** eines festen $\Theta$-Orbits, also bei festem $(p,m,u)$
entlang $r$. Verbindlich ist daher nur noch:

$$
\boxed{\ \bigl\langle\eta_{p;m;r,u},\eta_{p;m;r',u}\bigr\rangle = \delta_{rr'} \qquad \text{(Orthonormalität \textbf{innerhalb} der Kette).} \ }
$$

Über verschiedene $(p,m,u)$ hinweg: **unbestimmt**, generisch $\neq 0$. `⚠[M]`

**Auswirkung auf NEU-225.** Die Primfaserdiagonalisierung benutzt nur die Kette bei festem
$(p,m,u)$ und ist damit **unberührt**. Zusätzlich robust: unter der NEU-51-Lesart lautet die
Kette $s\mapsto s+m$ mit Koeffizient $(u+ps)\log(pm)$ — wieder linear im Kettenindex, also
erneut von der Form $c(k+\delta)$ aus (225.2). Der Transportgeneratorbefund gilt in **beiden**
Indexlesarten. `✓[M]`

> **Wörterbuchkonflikt `⚠[M]`.** (55.3) liest den Shift als $r\to r+n$ mit $n\mid m$ und
> Koeffizient $\propto r\log n$; (51.2) liest ihn als $s\to s+m$ mit Koeffizient
> $(u+ps)\log(pm)$. Beide Lesarten stimmen strukturell überein (linearer Koeffizient,
> konstante Schrittweite), sind aber nicht identisch. Vor `[O-225-2d]` ist zu klären, welche
> gilt.

---

## 5. Der Blocker: (51.3)/(51.4)/(51.7) setzen eine Eigenbasis voraus

NEU-51 §2 beginnt: *„Sei $D_{\mathrm{rel}}\eta_\alpha = \lambda_\alpha\eta_\alpha$ eine
Spektralzerlegung."* Darauf beruhen

$$
R_{\mathrm{rel}}(s)[\cdots] = \sum_\alpha \frac{\overline{\langle\eta_\alpha,\eta_{p;n;r,u}\rangle}\langle\eta_\alpha,\eta_{q;m;t,v}\rangle}{\lambda_\alpha-s}
\tag{51.4}
$$

und die Bedingung (51.7) mit Eigenwerten $\lambda_{p;n;r,u}$.

$$
\boxed{\ \text{Nach NEU-225 hat } D_{\mathrm{rel}} \ \text{rein absolutstetiges Spektrum und \textbf{keine} Eigenwerte. Es gibt kein solches } \{\lambda_\alpha\}. \quad \checkmark[M]_{\mathrm{neg}}\ }
$$

Das war bereits durch NEU-52 (52.D0) verboten: *„$\eta_{p;m;r,u}$ darf nicht als Eigenbasis
von $D_{\mathrm{rel}}$ behandelt werden."* NEU-51 verletzt diese Warnung.

**Korrekte Form.** Das Resolventenmatrixelement muss als Spektralintegral gegen das
Spektralmaß geschrieben werden — genau die Weg-B-Form aus NEU-53/56 (56.12):

$$
R_{\mathrm{rel}}(s)[a,b] = \int_{\mathbb R}\frac{d\mu_{a,b}(\lambda)}{\lambda-s}.
$$

Solange (51.3)/(51.4)/(51.7) nicht in dieser Form neu geschrieben sind, sind
`[O-225-2d]` und `[O-225-2e]` **nicht auswertbar**.

$$
\boxed{\ \text{Neuer Vorschaltknoten: } [O\text{-}226\text{-}1] \ \text{— NEU-51 auf Spektralmaßform umschreiben.}\ }
$$

---

## 6. Die Schattenklassenkriterien — was quellenseitig steht

### 6.1 Hinreichend für Spurklasse

$$
(D_{\mathrm{rel}}-s)^{-1/2}V_N \in \mathcal S_2 \quad\Longrightarrow\quad K_N(s)\in\mathcal S_1
\tag{51.6}
$$

denn $K_N(s) = \bigl((D_{\mathrm{rel}}-s)^{-1/2}V_N\bigr)^*\bigl((D_{\mathrm{rel}}-s)^{-1/2}V_N\bigr)$.

Das ist die quellenseitige Fassung des Schatten-Hölder-Arguments — mit der **Resolventenwurzel**,
nicht mit $V$ allein. Die Variante „$V\in\mathcal S_2\Rightarrow K\in\mathcal S_1$" steht so
**nicht** in der Quelle und wäre auch nicht äquivalent, da $(D_{\mathrm{rel}}-s)^{-1}$ hier
unbeschränkt invertierbar bleibt (a.c. Spektrum $=\mathbb R$, kein Abfall der Resolvente in
Schattennormen). `⚠[M]`

### 6.2 Der Nicht-Spurklassen-Zeuge ist zulässig

Für $z=x+iy$, $y>0$: $\operatorname{Im}R(z) = y\bigl((D_{\mathrm{rel}}-x)^2+y^2\bigr)^{-1}\ge0$,
also $\operatorname{Im}K(z) = y\,V^*\bigl((D_{\mathrm{rel}}-x)^2+y^2\bigr)^{-1}V \ge 0$ und

$$
\operatorname{Tr}\operatorname{Im}K(z) = y\sum_p\lVert R(z)\Psi_p\rVert^2 .
$$

Divergenz dieser Summe beweist $\operatorname{Im}K(z)\notin\mathcal S_1$, also
$K(z)\notin\mathcal S_1$. Das ist ein echtes Kriterium, im Gegensatz zur Divergenz einer Summe
von Beträgen der Matrixeinträge.

**Voraussetzung, jetzt erfüllt.** Der Zeuge braucht die Selbstadjungiertheitsnormierung. NEU-51
§5 lässt beide offen: Option A ($D_{\mathrm{rel}}=J_N^-$ schiefadjungiert, (51.11)
$K_{pq}(s)^*=-K_{qp}(-\bar s)$) und Option B ($\mathcal D_{\mathrm{rel}}=iJ_N^-$
selbstadjungiert, (51.12)/(51.13) $K_{pq}(s)^*=K_{qp}(\bar s)$).

Nach NEU-225 §1.1 ist **Option B verbindlich**. Damit gilt $K(z)^*=K(\bar z)$ und
$\operatorname{Im}K(z)\ge0$ für $\operatorname{Im}z>0$. Der Zeuge ist zulässig. `✓[M]`

> **Aber:** Die Summe $\sum_p\lVert R(z)\Psi_p\rVert^2$ setzt eine orthonormale Primbasis
> voraus. Nach §4 ist genau das nicht gegeben. Die Spur muss basisfrei oder in einer
> tatsächlich orthonormalen Basis ausgewertet werden. `⚠[M]`

---

## 7. NEU-77 — der Grenzübergang ist nicht normkonvergent

NEU-77 zeigt für den getrunkierten Shift $V_n^{(N)}$ und
$J_N^- = \sum_{n\in S_N}\log(n)V_n^{(N)}R_N$ die **exakte** Identität ohne Fehlerterm

$$
\Pi_N S_N R_N D_{BC,N}\Pi_N^* = J_N^- \qquad \text{(endliches } N\text{)}. \quad \checkmark[M]
$$

Zwei Einschränkungen für den Limes:

| Punkt | Aussage | Status |
|---|---|---|
| (D) | Ohne Trunkierung entstehen Randterme; ihr Verschwinden ist **keine Operatornormaussage**, nur stark/punktweise für endlich getragene Vektoren | `⚠[M]` |
| (E) | Die normierte orthogonale Feshbach-Projektion $\tilde\Pi_N=\lvert S_N\rvert^{-1/2}\Pi_N$ liefert nur $\lvert S_N\rvert^{-1}J_N^-$; der fehlende Faktor muss mit der Jacobi-/Feshbach-Normierung (NEU-62) abgestimmt werden | `⚠[M]` |

NEU-77 hält ausdrücklich fest: *„Keine ‚starke Operatornormkonvergenz'… Der Ausdruck ‚starke
Operatornorm' ist kategorial inkonsistent. Randterme können im Operatornormsinn normgroß
bleiben."*

$$
\boxed{\ \text{Der Übergang } K_N(z)\to K(z) \ \text{ist quellenseitig \textbf{nicht} gesichert — nur punktweise auf endlich getragenen Vektoren.}\ }
$$

Da Schattenklassen **keine** punktweisen Invarianten sind, kann $\mathcal S_2\setminus\mathcal S_1$
für $K(z)$ nicht aus Eigenschaften der $K_N(z)$ erschlossen werden. `✓[M]`

---

## 8. Statusbilanz

| Aussage | Status |
|---|---|
| $V_p = C_p^{\mathrm{rel}}$ quellenseitig identifiziert | `✓[M]` (NEU-51 Kopf) |
| $V_N=\sum_{p\le N}V_p$ ist Summe, nicht direkte Summe | `✓[M]` (51.0) |
| $u$-Regulator offen; entscheidet $\mathcal S_1$ gegen $\mathcal S_2$ | `⚠[M]` (51.1) — **der Freiheitsgrad** |
| $\mathfrak p_N$ endlichdimensional, $\operatorname{rank}K_N\le\pi(N)$ | `✓[M]_neg` **widerlegt** |
| $\mathcal S_2\setminus\mathcal S_1$ bei festem $N$ ausgeschlossen | `✓[M]_neg` **widerlegt** |
| $\det_2$ bei festem $N$ nicht strukturell erzwungen | `✓[M]_neg` — (51.8)/(51.9) führen $\det_2$ für endliches $N$ |
| $\mathcal K_N\neq\bigoplus_p K_p$ | `✓[M]` (51.5) |
| Mechanismus: Überlappung der Primkanalbilder, nicht Primmischung durch $D_{\mathrm{rel}}$ | `✓[M]` (51.2) |
| $\eta$-Familie orthonormal über Primkanäle (NEU-225 §1.2) | `✓[M]_neg` **zurückgerollt** |
| Orthonormalität **innerhalb** der Kette bei festem $(p,m,u)$ | `✓[M]` |
| NEU-225-Primfaserbefund unberührt, in beiden Indexlesarten | `✓[M]` |
| Wörterbuchkonflikt (55.3) gegen (51.2) | `⚠[M]` |
| (51.3)/(51.4)/(51.7) setzen Eigenbasis von $D_{\mathrm{rel}}$ voraus | `✓[M]_neg` — verletzt 52.D0, widerspricht NEU-225 |
| (51.6) Spurklassekriterium mit Resolventenwurzel | `✓[M]` |
| $\operatorname{Im}K(z)\ge0$-Zeuge zulässig unter Option B (NEU-225 §1.1) | `✓[M]` |
| Spurauswertung $\sum_p\lVert R(z)\Psi_p\rVert^2$ setzt Orthonormalität voraus | `⚠[M]` |
| NEU-77: exakte Identität bei endlichem $N$ | `✓[M]` |
| NEU-77: Limes nur punktweise, **nicht** normkonvergent; Normierungsfaktor offen | `⚠[M]` (D),(E) |
| Schattenklasse von $K(z)$ aus $K_N(z)$ erschließbar | `✓[M]_neg` |

---

## 9. Revidierte Reihenfolge

| Knoten | Aufgabe | Priorität |
|---|---|---|
| `[O-226-1]` | **Vorschaltknoten.** (51.3)/(51.4)/(51.7) auf **Spektralmaßform** umschreiben. Ohne dies sind `[O-225-2d/e]` nicht auswertbar | **1** |
| `[O-226-2]` | Wörterbuchkonflikt (55.3) gegen (51.2) entscheiden | **2** |
| `[O-226-3]` | $u$-Regulator fixieren — die Wahl entscheidet $\mathcal S_1$ gegen $\mathcal S_2$ (51.1) | **3** |
| `[O-226-4]` | Orthonormale Basis des globalen Primkanalraums konstruieren (Gram–Schmidt über die überlappenden $\Psi_p$), damit Spuren auswertbar werden | **4** |
| `[O-225-2d/e]` | Hilbert-Schmidt-Summe und Nicht-$\mathcal S_1$-Zeuge | danach |
| `[O-225-3]` | Sektoren $m$ nicht prim | erst wenn sie $K_{pq}$ quantitativ beeinflussen |
| `[O-225-2f]` | $\det_2(I-K(z))$ gegen $D^{\mathrm{rel}}_{\mathrm{Spec}}$ | zuletzt |

---

## 10. Vorläufige Formulierung für Bestandsaufnahme und EINSTIEGSPROMPT

> **Schichtenverschiebung nach NEU-225/226.** Der relative Operator $D_{\mathrm{rel}}$ ist kein
> konfinierender Hilbert–Pólya-Kandidat. Bereits eine Primfaser besitzt absolutstetigen,
> translationsartigen Spektraltyp; auf dem vollen wie auf dem kernreduzierten Raum ist der
> Resolvent nicht kompakt. Seine Rolle wird neu eingeordnet: $D_{\mathrm{rel}}$ liefert die
> primarithmetische Transport- und Streugeometrie.
>
> Der neue Kandidat für eine kompakte bzw. Hilbert–Schmidt-spektrale Schicht ist der globale
> Feshbach-/Birman–Schwinger-Transfer $V^*(D_{\mathrm{rel}}-z)^{-1}V$. Anders als zunächst
> vermutet ist $K_N(z)$ auch bei festem $N$ **nicht** endlich-rangig: jeder Primkanal trägt
> einen vollen $(r,n)$-Index (51.2/51.3). $\mathcal S_2\setminus\mathcal S_1$ ist daher weder
> bei festem $N$ ausgeschlossen noch aus den Trunkierungen erschließbar, da der Limes nach
> NEU-77 nur punktweise und nicht normkonvergent ist.
>
> Die Off-Diagonalterme $K_{pq}$, $p\neq q$, sind quellenseitig gesichert (51.5). Ihr
> Mechanismus ist die **Überlappung der Primkanalbilder** in der BC-Algebra: verschiedene
> $(p,m)$ treffen dasselbe $V_{pm}$. $D_{\mathrm{rel}}$ selbst bleibt kanalerhaltend.
>
> Offen sind: die Umschreibung der Resolventenformeln auf Spektralmaßform, der $u$-Regulator,
> eine orthonormale Basis des globalen Primkanalraums, die Hilbert-Schmidt-Summe und ein
> unabhängiger Nicht-Spurklassen-Zeuge.
>
> **Neue Hauptlinie:** singuläre HH-Struktur $\to$ Primkanten-Transport $D_{\mathrm{rel}}$
> $\to$ globaler Feshbach-Transfer $K(z)$ $\to$ $\det_2$- und Weil-Schicht.
> Dies ist eine **Arbeitshypothese**. Kompaktheit, Schattenklasse, zyklischer Vektor und
> Determinantenidentität sind nicht bewiesen.

---

## Abhängigkeiten

| Referenz | Verwendet für |
|---|---|
| NEU-43/44 | $\tilde\omega_2(e_uV_p,e_sV_m) = -us\log(p)e_{u+ps}V_{pm}$ |
| NEU-50 | $\mathcal K_N(s)=V_N^*(D_{\mathrm{rel}}-s)^{-1}V_N$ |
| **NEU-51** | (51.0)–(51.13): Kopplungsform, $K_{pq}$, Off-Diagonalität, Schattenkriterien, Symmetrieoptionen |
| NEU-52 | 52.D0 — $\eta$ ist keine Eigenbasis |
| NEU-53, NEU-56 | Weg B, Spektralmaßform (56.12) |
| NEU-55 | (55.3) Trägeraussage, (55.4) |
| NEU-62 | Normierungsabstimmung für NEU-77 (E) |
| **NEU-77** | Feshbach-Kollaps, exakte Identität bei endlichem $N$, Punkte (D)/(E) |
| NEU-225 | Transportgenerator, Option B verbindlich, Primfaserdiagonalisierung |
