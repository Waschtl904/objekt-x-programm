# NEU-249 — Polare Kollisionsfaktorisierung und Wres-Gramabstieg

**Kennung:** NEU-249  
**Ordner:** `07-weil-explizitformel/`  
**Datum:** 2026-08-06  
**Knoten:** `[O-246/0corr-1]`  
**Vorgänger:** NEU-248 — Direktaudit `[O-246/0]`, Kollisionsoperator und kanonisches Rechtsinverses  
**Korrekturen an:** NEU-248 §5 (Rechtsinversenbeschränktheit), §3 (Gewichtskanonizität)  
**Nachfolger:** `[O-246/0corr-2]` — Wres-Gramabstieg und Hebungsunabhängigkeit von J_{p,b}

---

## 0 — Auditbasis und Drei-Objekte-Trennung

Geprüft wird der neue Knoten `[O-246/0corr]` aus NEU-248. Der Auditstandard verlangt Typkorrektheit, Quotientenabstieg, Domänenprüfung und strikte Trennung zwischen Beweis und konditionalem Modell.

Drei quellenseitig verschiedene Objekte sind durchgehend auseinanderzuhalten:

1. **Transporthilbertraum:** \(\overline{\operatorname{span}}\{\eta_{p;p;s,u}\}\) — nach NEU-225 orthonormal; der \(u\)-Index ist ein von der Primtransportdynamik nicht bewegter eigenständiger Index.
2. **Algebraischer relativer Rohzielraum:** \(\operatorname{span}\{E^{\mathrm{rel}}_{R;1\to p}\}\) — nur mit relativer sesquilinearer Wres-Form; Primkantendiagonalität und positive Hilbertrealisierung sind nicht bewiesen.
3. **Wres-Quotient:** positiver Hilbertraum erst nach zusätzlicher Konstruktion; nicht verfügbar.

---

## 1 — Gesamturteil

\[
\boxed{[O\text{-}246/0\mathrm{corr}]:\;\checkmark[M]_{\mathrm{part}}}
\]

Der gewichtete Kollisionsoperator lässt sich im abstrakten orthonormalen Koeffizientenmodell vollständig analysieren. Dort erhält man ein exaktes Beschränktheitskriterium und eine explizite Moore–Penrose-Inverse.

Diese Modellrechnung steigt nicht automatisch auf den tatsächlichen Wres-Zielraum ab.

**Zentrales neues Resultat:**

\[
\boxed{
\text{Bei natürlichen quadratsummierbaren Gewichten existiert global kein beschränktes Rechtsinverses.}
}
\]

Der stabile kanonische Kandidat ist nicht das Rechtsinverse, sondern die partielle Isometrie der Polardarstellung. Sie verwendet den Faktor \(B_R^{-1/2}\), ist aber gerade **kein** Rechtsinverses.

---

## 2 — Wo sitzen die Gewichte wirklich?

NEU-221e gibt für die Rohkopplung an:

\[
-\sum_{s,m} \ell_{s,m,u,s\log p}\; E^{\mathrm{rel}}_{u+ps;\,m\to pm}.
\]

Für eine Hebung \(\sum_u a_{p,u} e_u V_p\) entsteht im Primzielsektor \(m=1\):

\[
-\sum_{s,u} a_{p,u}\,\ell_{s,1,u,s\log p}\; E^{\mathrm{rel}}_{u+ps;\,1\to p}.
\]

Auf der fein indizierten \(\eta\)-Ebene:

\[
\sum_{s,u} a_{p,u}\,\ell_{s,1}(-us\log p)\;\eta_{p;p;s,u}.
\]

NEU-228 hält ausdrücklich fest, dass die \(u\)-Koeffizienten \(a_{p,u}\) die gewählte Fourierhebung darstellen und **keinen** unabhängigen Zielraumregulator bilden.

### 2.1 — Konsequenz: Kanonizität der Gewichte ist offen

Der zunächst natürliche Kollaps ist ungewichtet: \(\eta_{p;p;s,u} \mapsto E^{\mathrm{rel}}_{u+ps;1\to p}\). Die Faktoren \(-a_{p,u}\ell_{s,1}us\log p\) sind ursprünglich Koeffizienten des Kopplungsvektors. Sie nachträglich als Operatorgewichte \(b_{s,u}\) in \(\kappa_{p,b}\) einzubauen, ist eine mögliche Faktorisierung, aber nicht automatisch eine kanonische quellenseitige Zerlegung. Für beliebige \(d_{s,u}\neq 0\) gilt formal:

\[
c_{s,u} = (b_{s,u}d_{s,u})(d_{s,u}^{-1}c_{s,u}).
\]

\[
\boxed{\text{Kanonizität der Gewichte }b_{s,u}:\;?[O]}
\]

\[
\boxed{\text{Ein eigenständiger kanonischer gewichteter Kollisionsoperator folgt nicht allein aus der Rohkopplungsformel.}}
\]

---

## 3 — Abstrakter Faseroperator: vollständige Analyse

Setze \(I_p = \mathbb{Z}^2\), \(\pi_p(s,u) = u+ps\). Betrachte

\[
A_{p,b}: \ell^2(I_p) \longrightarrow \ell^2(\mathbb{Z}),
\qquad
(A_{p,b}x)_R = \sum_{u+ps=R} b_{s,u}\,x_{s,u}.
\]

Definiere die **Fasergewichte**

\[
B_R := \sum_{u+ps=R} |b_{s,u}|^2.
\]

Durch Cauchy–Schwarz und Summation:

\[
|(A_{p,b}x)_R|^2 \le B_R \sum_{u+ps=R}|x_{s,u}|^2,
\qquad
\|A_{p,b}x\|^2 \le \Bigl(\sup_R B_R\Bigr)\|x\|^2.
\]

Die Schranke wird durch einen auf einer Faser proportional zu \(\overline{b}_{s,u}\) gewählten Vektor erreicht.

\[
\boxed{A_{p,b}\text{ ist beschränkt} \iff \sup_R B_R < \infty,\qquad \|A_{p,b}\|^2 = \sup_R B_R.}
\]

**Status:** \(\checkmark[M]\) — betrifft ausschließlich den Operator zwischen zwei \(\ell^2\)-Räumen.

---

## 4 — Einschränkung: kein direkter Wres-Satz

Der tatsächliche Zielraum besitzt keine nachgewiesene orthonormale Basis \(\{E_R\}\). Sei formal \(S_E:(c_R)_R \mapsto \sum_R c_R E_R\) der Syntheseoperator. Dann ist der wirkliche Kollisionsoperator:

\[
K_{p,b} = S_E A_{p,b},
\qquad
K_{p,b}^* K_{p,b} = A_{p,b}^* G_E A_{p,b},
\quad
G_E = ({\langle E_R, E_{R'}\rangle_{\mathrm{Wres,rel}}})_{R,R'}.
\]

Das einfache Kriterium \(\sup_R B_R < \infty\) ist für \(K_{p,b}\) nur dann unmittelbar exakt, wenn \(S_E\) eine isometrische Einbettung ist. Das ist nicht bewiesen.

\[
\boxed{\sup_R B_R < \infty\text{ als Kriterium für den tatsächlichen Wres-Operator: }\checkmark[K/M].}
\]

---

## 5 — Beschränktes Rechtsinverses: exaktes Kriterium

Angenommen \(0 < B_R < \infty\) für jedes \(R\). Dann ist auf endlich getragenen Zielvektoren formal:

\[
A_{p,b}^\dagger e_R = \frac{1}{B_R}\sum_{u+ps=R}\overline{b}_{s,u}\,e_{s,u},
\qquad
A_{p,b} A_{p,b}^\dagger e_R = e_R.
\]

Die Norm dieses Urbildes ist \(\|A_{p,b}^\dagger e_R\|^2 = B_R^{-1}\).

**Vollständiges Beschränktheitskriterium:**

\[
\boxed{A_{p,b}^\dagger\text{ ist genau dann beschränkt, wenn }\inf_R B_R > 0.
\qquad
\|A_{p,b}^\dagger\|^2 = \frac{1}{\inf_R B_R}.}
\]

**Korrektur gegenüber NEU-248 §5:** Die dort angegebene Bedingung \(0 < B_R < \infty\) punktweise genügt nur für das algebraische Rechtsinverse auf endlich getragenen Folgen. Sie reicht nicht für Beschränktheit auf \(\ell^2(\mathbb{Z})\).

---

## 6 — No-Go: natürliche endliche Gewichte und Kompaktheit

Motiviert durch die Rohkopplungsformel:

\[
b_{s,u} = -a_{p,u}\,\ell_{s,1}\,us\log p.
\]

Unter natürlichen gewichteten Energiebedingungen:

\[
\sum_u |u\,a_{p,u}|^2 < \infty,
\qquad
\sum_s |s\,\ell_{s,1}|^2 < \infty.
\]

Dann ist \(A_{p,b}\) sogar **Hilbert–Schmidt**:

\[
\sum_{s,u}|b_{s,u}|^2 = (\log p)^2 \Bigl(\sum_u |u\,a_{p,u}|^2\Bigr)\Bigl(\sum_s |s\,\ell_{s,1}|^2\Bigr) < \infty
\implies A_{p,b}\in\mathcal{S}_2.
\]

Da \((B_R)_R \in \ell^1(\mathbb{Z})\), gilt:

\[
B_R \longrightarrow 0 \quad (|R|\to\infty),
\qquad \inf_R B_R = 0.
\]

Damit:

\[
\boxed{A_{p,b}^\dagger\text{ ist unbeschränkt.}}
\]

**Alternativer Kompaktheitsschluss:** Ein kompakter Operator \(\ell^2(I_p)\to\ell^2(\mathbb{Z})\) auf einen unendlichdimensionalen Hilbertraum kann kein beschränktes Rechtsinverses besitzen, da sonst \(I = A_{p,b}A_{p,b}^\dagger\) kompakt wäre.

\[
\boxed{
\begin{array}{c}
\textbf{No-Go-Satz.}\\[2pt]
\text{Sind die natürlichen Kopplungsgewichte quadratsummierbar,}\\
\text{ist }A_{p,b}\text{ kompakt und besitzt global kein beschränktes Rechtsinverses.}
\end{array}
}
\]

**Status:** \(\checkmark[M]\) im orthonormalen Koeffizientenmodell. Ob die \(\ell^2\)-Bedingungen aus den Quellen folgen, bleibt \(?[O]\).

---

## 7 — Stabile Architektur: partielle Isometrie der Polardarstellung

Die Moore–Penrose-Inverse verwendet \(B_R^{-1}\) und ist unbeschränkt wenn \(B_R\to 0\). Dagegen definiert

\[
J_{p,b}:\ell^2(\{R: B_R>0\})\longrightarrow\ell^2(I_p),
\qquad
J_{p,b}\,e_R = \frac{1}{\sqrt{B_R}}\sum_{u+ps=R}\overline{b}_{s,u}\,e_{s,u},
\]

eine **Isometrie**, denn verschiedene \(R\)-Fasern sind disjunkt:

\[
\langle J_{p,b}\,e_R,\,J_{p,b}\,e_{R'}\rangle = \delta_{RR'}.
\]

Aber:

\[
A_{p,b}\,J_{p,b}\,e_R = \sqrt{B_R}\,e_R \neq e_R.
\]

Damit ist \(J_{p,b}\) **kein Rechtsinverses**, sondern es gilt die **Polardarstellung**:

\[
\boxed{A_{p,b} = D_{\sqrt{B}}\,J_{p,b}^*,}
\]

wobei \(D_{\sqrt{B}}\,e_R = \sqrt{B_R}\,e_R\).

### 7.1 — Saubere Trennung

| Faktor | Eigenschaft |
|---|---|
| \(J_{p,b}\) | Isometrisch, stabil, geometrische Brücke |
| \(D_{\sqrt{B}}\) | Diagonal, trägt die Kopplungsstärken, darf gegen null gehen |

Die Kompaktheit liegt vollständig in \(D_{\sqrt{B}}\), nicht in \(J_{p,b}\).

---

## 8 — Vergleich der Kandidaten

| Kandidat | Formel | Eigenschaft |
|---|---|---|
| Rechtsinverses \(A^\dagger\) | \(B_R^{-1}\sum\overline{b}\,e_{s,u}\) | \(AA^\dagger=I\), aber beschränkt nur wenn \(\inf B_R>0\) |
| Isometrische Brücke \(J_{p,b}\) | \(B_R^{-1/2}\sum\overline{b}\,e_{s,u}\) | immer isometrisch auf \(B_R>0\), aber \(AJ=D_{\sqrt{B}}\neq I\) |
| Einzelmodensektion | \(e_R\mapsto e_{s(R),u(R)}\) | beschränkt, aber willkürlich, nicht gewichtsbestimmt |

Dieselbe Normierungsalternative wie in NEU-246 taucht hier auf höherer Ebene wieder auf: \(B_R^{-1}\) gibt das echte Rechtsinverse, analytisch meist unbeschränkt; \(B_R^{-1/2}\) gibt die stabile Brücke, aber kein Rechtsinverses.

---

## 9 — Kanonizität bleibt hebungsabhängig

Auch \(J_{p,b}\) ist nur dann intrinsisch, wenn die normierten Faserprofile

\[
\frac{b_{s,u}}{\sqrt{B_R}}
\]

unabhängig von der gewählten zulässigen Hebung sind. Die Koeffizienten \(a_{p,u}\) sind aber gerade die Hebungswahl. NEU-228 führt starke Vektorinvarianz, Norminvarianz und Geometrie der Hebungsfaser als offen. NEU-221e formuliert das exakte Abstiegsproblem als

\[
\widetilde{T}_p^{\mathrm{raw}}\bigl(\Delta_p^{\mathrm{adm}}\bigr) \subseteq \mathcal{N}_{\mathrm{Wres,rel}},
\]

und hält fest, dass diese Inklusion weder für die zulässige Differenzmenge noch für den gesamten algebraischen Kern bewiesen ist.

\[
\boxed{\text{Kanonizität von }J_{p,b}:\;?[O]}
\]

mit direktem Rücklauf zu \([O\text{-}221\text{-}1c1a]\) und \([O\text{-}153\text{-A/B}]\).

---

## 10 — Statusbuchung für [O-246/0corr]

| Teilknoten | Aussage | Status |
|---|---|---|
| \([O\text{-}246/0\mathrm{corr}\text{-a}]\) | abstrakter Faseroperator \(A_{p,b}\) | \(\checkmark[M]\) |
| \([O\text{-}246/0\mathrm{corr}\text{-b}]\) | \(\|A_{p,b}\|^2=\sup_R B_R\) | \(\checkmark[M]\) |
| \([O\text{-}246/0\mathrm{corr}\text{-c}]\) | dasselbe Kriterium für den Wres-Zielraum | \(\checkmark[K/M]\) |
| \([O\text{-}246/0\mathrm{corr}\text{-d}]\) | algebraisches minimales Rechtsinverses | \(\checkmark[M]\) |
| \([O\text{-}246/0\mathrm{corr}\text{-e}]\) | punktweise \(B_R>0\) genügt für beschränktes Rechtsinverses | \(\checkmark[M]_{\mathrm{neg}}\) |
| \([O\text{-}246/0\mathrm{corr}\text{-f}]\) | beschränktes Rechtsinverses iff \(\inf_R B_R>0\) | \(\checkmark[M]\) |
| \([O\text{-}246/0\mathrm{corr}\text{-g}]\) | bei \(b\in\ell^2(I_p)\): beschränktes globales Rechtsinverses | \(\checkmark[M]_{\mathrm{neg}}\) |
| \([O\text{-}246/0\mathrm{corr}\text{-h}]\) | partielle Isometrie \(J_{p,b}\) | \(\checkmark[M]\) |
| \([O\text{-}246/0\mathrm{corr}\text{-i}]\) | quellenseitig kanonische Wahl von \(b\) | \(?[O]\) |
| \([O\text{-}246/0\mathrm{corr}\text{-j}]\) | Abstieg von \(J_{p,b}\) auf den Wres-Hilbertraum | \(?[O]\) |
| \([O\text{-}246/0\mathrm{corr}\text{-k}]\) | Hebungsunabhängigkeit | \(?[O]\) |

---

## 11 — Repository-Korrekturen für NEU-248

**Korrektur 1 — Rechtsinversenbeschränktheit (§5):**  
\(0 < B_R < \infty\) genügt nur für das algebraische Rechtsinverse auf endlich getragenen Zielvektoren. Für Beschränktheit auf \(\ell^2(\mathbb{Z})\) ist notwendig und hinreichend \(\inf_R B_R > 0\).

**Korrektur 2 — Wres-Zielraumeinschränkung (§3):**  
Das Kriterium \(\sup_R B_R < \infty\) ist als exakter Satz nur für den abstrakten Koeffizientenoperator \(A_{p,b}:\ell^2(\mathbb{Z}^2)\to\ell^2(\mathbb{Z})\) zu buchen. Für den Wres-Zielraum ist zusätzlich der Gramoperator \(G_E = S_E^* S_E\) erforderlich.

**Korrektur 3 — Gewichtskanonizität (§2):**  
Die Gewichte \(b_{s,u}\) dürfen nicht ohne Weiteres als „von der Rohkopplung erzwungene Operatorgewichte" bezeichnet werden. Die Rohkopplung erzwingt Gesamtkoeffizienten; ihre Aufteilung zwischen Operator und Quellvektor ist eine Faktorisierungswahl.

**Korrektur 4 — Partiell isometrischer Kandidat:**  
\(J_{p,b}\,e_R = B_R^{-1/2}\sum_{u+ps=R}\overline{b}_{s,u}\,e_{s,u}\) ist als eigener Kandidat aufzunehmen: stabile polar-dekompositorische Brücke, kein Rechtsinverses.

**Korrektur 5 — No-Go-Satz:**

\[
b\in\ell^2(\mathbb{Z}^2)
\implies A_{p,b}\in\mathcal{S}_2
\implies A_{p,b}\text{ besitzt kein beschränktes Rechtsinverses auf }\ell^2(\mathbb{Z}).
\]

---

## 12 — Endurteil und nächster atomarer Knoten

\[
\boxed{
\text{Der gewichtete Kollisionsoperator kann die Brücke nicht über ein beschränktes globales Rechtsinverses liefern.}
}
\]

Im orthonormalen Koeffizientenmodell gilt die klare Alternative:

\[
\begin{array}{ll}
\text{ungewichteter Kollaps:} & \text{unbeschränkt wegen unendlicher Fasern,}\\[2pt]
\text{quadratsummierbar gewichteter Kollaps:} & \text{kompakt, daher kein beschränktes Rechtsinverses.}
\end{array}
\]

Die richtige stabile Architektur ist:

\[
\boxed{A_{p,b} = D_{\sqrt{B}}\,J_{p,b}^*,}
\]

also partielle Isometrie \(+\) diagonaler Kopplungsstärkenoperator. Die partielle Isometrie ist konditional kanonisch, sobald die Gewichte kanonisch sind. Genau diese Kanonizität bleibt an die Hebungs- und Wres-Grambarriere gebunden.

**Nächster atomarer Forschungsauftrag:**

\[
\boxed{[O\text{-}246/0\mathrm{corr}\text{-}2]:\;\text{Wres-Gramabstieg und Hebungsunabhängigkeit von }J_{p,b}}
\]

Konkret:

1. Trenne \(A_{p,b}\) von \(S_E\); definiere die tatsächliche Form \(K_{p,b} = S_E A_{p,b}\).
2. Berechne oder definiere die Zielgrammatrix \(G_E = S_E^* S_E\).
3. Prüfe, ob \(J_{p,b}\) nach Änderung der zulässigen Hebung invariant ist.
4. Prüfe nicht mehr die Existenz eines beschränkten Rechtsinversen — dieses ist unter natürlichen endlichen Energiebedingungen negativ ausgeschlossen.

---

## 13 — Repository-Korrekturblock

```text
AUDIT [O-246/0corr] (NEU-249, Stand 2026-08-06)

Gesamturteil:              checkmark[M]_part

No-Go-Satz (neu):
  b in ell^2(Z^2) => A_{p,b} in S_2 => kein beschraenktes Rechtsinverses.

Stabile Architektur:
  A_{p,b} = D_sqrt(B) J_{p,b}^*

Teilknoten:
  [O-246/0corr-a]  abstrakter Faseroperator                checkmark[M]
  [O-246/0corr-b]  ||A||^2 = sup B_R                       checkmark[M]
  [O-246/0corr-c]  Wres-Zielraumversion                    checkmark[K/M]
  [O-246/0corr-d]  algebraisches Rechtsinverses             checkmark[M]
  [O-246/0corr-e]  punktweise B_R>0 genuegt                checkmark[M]_neg
  [O-246/0corr-f]  beschraenkt iff inf B_R > 0             checkmark[M]
  [O-246/0corr-g]  b in ell^2: kein beschraenktes Rechts.  checkmark[M]_neg
  [O-246/0corr-h]  partielle Isometrie J_{p,b}             checkmark[M]
  [O-246/0corr-i]  kanonische Gewichtswahl                 ?[O]
  [O-246/0corr-j]  Wres-Abstieg von J_{p,b}                ?[O]
  [O-246/0corr-k]  Hebungsunabhaengigkeit                  ?[O]

Korrekturen an NEU-248:
  §5: 0 < B_R < infty genuegt nicht fuer Hilbertraum-Rechtsinverses;
      notw. und hinr.: inf_R B_R > 0.
  §3: Gewichte nicht als kanonisch erzwungen bezeichnen.
  Neu: J_{p,b} als eigener Kandidat (partiell isometrisch, kein RI).
  Neu: No-Go-Satz fuer b in ell^2.

Naechster Knoten:
  [O-246/0corr-2]: Wres-Gramabstieg und Hebungsunabhaengigkeit von J_{p,b}.
  Ruecklauf zu [O-221-1c1a] und [O-153-A/B].
```

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung des RH-Forschungsjournals*
