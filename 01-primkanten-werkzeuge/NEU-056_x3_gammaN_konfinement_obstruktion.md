# NEU-56 — X.3.26: γ_N-Wahl, Konfinement-Obstruktion und Richtungsbefund Weg A/B

**Stand:** 29. Juni 2026
**Programm:** Objekt X / X.3
**Vorgänger:** NEU-55
**Ziel:** Exakte Auflösung der in NEU-54/55 identifizierten γ_N-Spannung (Konfinement vs. Schur-Test). Entscheidung kompakter Resolvent (Weg A) vs. Spektralmaß-Form (Weg B). Strenge Trennung: was die γ_N-Wahl für die **Selbstadjungiertheit** und was sie für den **Spektraltyp** bedeutet.

---

## 0. Kurzfazit (Marker vorangestellt)

\[
\boxed{
\begin{aligned}
&\textbf{(I)}\ \ \gamma_N = C/\log N \text{ löst die Spannung NICHT.} && \times\,[\mathrm{M}]\\
&\textbf{(II)}\ \ \text{Globaler Schur-Test und Konfinement sind mit \emph{einem} Skalar } \gamma_N \text{ unvereinbar.} && \times\,[\mathrm{M}]\\
&\textbf{(III)}\ \ \text{Die essentielle Selbstadjungiertheit (NEU-55) bleibt davon unberührt.} && \checkmark\,[\mathrm{M}]\\
&\textbf{(IV)}\ \ \text{Weg B (Spektralmaß-Form) ist der korrekte robuste Standard.} && \checkmark\,[\mathrm{M}]\\
&\textbf{(V)}\ \ \text{Weg A (kompakter Resolvent) über den Vergleichsoperator } L \text{ ist verschlossen.} && \times\,[\mathrm{M}]\\
&\textbf{(VI)}\ \ \text{Weg A bleibt offen über einen \emph{anderen} Vergleichsoperator.} && \mbox{❓}\,[\mathrm{O}]
\end{aligned}}
\tag{56.0}
\]

---

## 1. Präzisierung der zwei Bedingungen — sie leben auf verschiedenen Skalen

Aus NEU-55 (Setup 55.1–55.2):

\[
a=(p,m,r,u),\quad J^-\eta_a=\sum_b\Theta_{ba}\eta_b,\quad
L\eta_a=\ell(a)\eta_a,\quad
\ell(a)\sim 1+|r|\log(2+m)+|u|\log p+\Omega(m),
\tag{56.1}
\]
mit \(\Theta_{ba}\ne 0\) nur für \(b=(p',m,r+n,u')\), \(n\mid m\), und \(|\Theta_{ba}|\sim\gamma_N|r|\log n\).

**Nelson-Selbstadjungiertheit** (NEU-55, Satz 55.4) benötigt zwei Schranken, in denen \(L\) **Oberschranke** für \(J^-\) ist:

\[
\textbf{(N1)}\quad \|J^-x\|\le C\|Lx\|,\qquad
\textbf{(N2)}\quad |\langle J^-x,Lx\rangle-\langle Lx,J^-x\rangle|\le C\langle x,Lx\rangle.
\tag{56.2}
\]

**Konfinement / kompakter Resolvent** (Weg A) benötigt die **umgekehrte** Richtung — \(L\) ist **Unterschranke**, d.h. \(D_{\mathrm{rel}}\) dominiert \(L\):

\[
\textbf{(K)}\quad \|D_{\mathrm{rel}}x\|+\|x\|\ge c\,\|Lx\|,\qquad x\in\mathcal{D}_0^{\mathrm{eff}}.
\tag{56.3}
\]

> **Strukturelle Pointe:** (N1) verlangt \(J^-\lesssim L\), (K) verlangt \(L\lesssim |D_{\mathrm{rel}}|=|\overline{iJ^-}|\). Beide zusammen erzwingen \(L\simeq|D_{\mathrm{rel}}|\) bis auf Konstanten — eine sehr starke Forderung, die der weiter unten gezeigten γ_N-Asymptotik widerspricht.

---

## 2. Satz 56.1 — Widerlegung von \(\gamma_N=C/\log N\) \(\quad\times\,[\mathrm{M}]\)

Der kritische Kommutator-Schur-Quotient aus NEU-55 (55.16) ist
\[
Q(m):=\frac{|\ell(b)-\ell(a)|\,|\Theta_{ba}|}{\ell(a)}\sim \gamma_N\, m\log m.
\tag{56.4}
\]

**Behauptung (NEU-55 §6, Zeile 211):** Mit \(\gamma_N=C/\log N\) gelte \(Q\lesssim m/N\).

**Das ist falsch.** Einsetzen von \(\gamma_N=C/\log N\) liefert
\[
Q(m)=\frac{C\,m\log m}{\log N},\qquad
Q(m)\big|_{m=N}=\frac{C\,N\log N}{\log N}=C\,N\xrightarrow{N\to\infty}\infty.
\tag{56.5}
\]
Die Größe \(\dfrac{m\log m}{\log N}\) ist **nicht** \(m/N\); am oberen Rand \(m=N\) wächst sie wie \(N\). Der Schur-Quotient bleibt **unbeschränkt**. \(\quad\times\,[\mathrm{M}]\)

**Korrigierte Forderung für globalen Schur.** Damit \(\sup_{m\le N}Q(m)\le K\):
\[
\gamma_N\cdot N\log N\le K
\quad\Longleftrightarrow\quad
\boxed{\gamma_N\le \frac{K}{N\log N}.}
\tag{56.6}
\]
Es muss also \(\gamma_N=\mathcal{O}\!\big(1/(N\log N)\big)\) gelten — wesentlich schneller als \(1/\log N\).

---

## 3. Satz 56.2 — Konfinement-Obstruktion: globaler Schur \(\Rightarrow\) Verlust des Konfinements \(\quad\times\,[\mathrm{M}]\)

Setzt man die für globalen Schur **erzwungene** Rate \(\gamma_N=K/(N\log N)\) in den Konfinement-Term ein:
\[
\|J^-\eta_a\|\sim \gamma_N|r|\log n=\frac{K\,|r|\log n}{N\log N}\xrightarrow{N\to\infty}0
\qquad(\text{für festes }r,n).
\tag{56.7}
\]
Der gesamte schief-symmetrische Anteil \(J^-\) verschwindet im Grenzwert **relativ zu \(L\)**. Damit kann \(D_{\mathrm{rel}}=\overline{iJ^-}\) den Energieoperator \(L\) nicht von unten dominieren:
\[
\|D_{\mathrm{rel}}x\|\sim\gamma_N\,(\dots)\ll \|Lx\|
\quad\Longrightarrow\quad \textbf{(K) verletzt.}
\tag{56.8}
\]

**Schluss.** Mit *einem* skalaren \(\gamma_N\) sind (N1)/(N2) [verlangen \(\gamma_N\) klein] und (K) [verlangt \(\gamma_N\) nicht zu klein] **unvereinbar**. Die γ_N-Spannung ist real und nicht durch eine clevere skalare Wahl auflösbar. \(\quad\times\,[\mathrm{M}]\)

---

## 4. Satz 56.3 — Selbstadjungiertheit bleibt gültig \(\quad\checkmark\,[\mathrm{M}]\)

Die Obstruktion betrifft **nur** Richtung (K). Die Nelson-Bedingungen (N1)/(N2) werden durch kleines \(\gamma_N\) sogar **leichter** erfüllt (kleinere Matrixelemente \(|\Theta_{ba}|\sim\gamma_N|r|\log n\)):

- (N1): \(\sum_b|\Theta_{ba}|^2\lesssim \gamma_N^2\,\ell(a)^2\le C^2\ell(a)^2\) für jedes \(\gamma_N\le C\). \(\checkmark\)
- (N2): \(\sum_b|\ell(a)-\ell(b)|\,|\Theta_{ba}|\lesssim \gamma_N\,m\log m\cdot\ell(a)\), bei festem \(N\) endlich; mit \(\gamma_N\le K/(N\log N)\) auch gleichmäßig. \(\checkmark\)

Daher gilt **unverändert** (NEU-55 Satz 55.4):
\[
\boxed{iJ^-\ \text{ist wesentlich selbstadjungiert auf } \mathcal{D}_0^{\mathrm{eff}},\quad
D_{\mathrm{rel}}=\overline{iJ^-}\ \text{kanonisch selbstadjungiert.}}
\tag{56.9}
\]
Die Resolvente \((D_{\mathrm{rel}}-s)^{-1}\) existiert für \(s\notin\mathbb{R}\). \(\quad\checkmark\,[\mathrm{M}]\)

> Wichtige Konsequenz für die RH-Äquivalenz: Für \(\mathrm{Spec}(\lim A_N^{\mathrm{Jac},-})\subset\mathbb{R}\) genügt die **Selbstadjungiertheit** — ein diskretes Spektrum (Weg A) ist hierfür nicht notwendig. Der Engpass NEU-56 blockiert also **nicht** die RH-Hinrichtung; er entscheidet nur über den *Typ* des Spektrums.

---

## 5. Option B — alternative Skalierungen (geprüft, beide scheitern an (K))

### 5.1 B1: separables m-Gewicht \(\Theta\mapsto \Theta\cdot w(m)\)

Schur verlangt \(w(m)\,m\log m\le K\), also \(w(m)\le K/(m\log m)\). Der Konfinement-Term wird dann
\[
w(m)\,\gamma_N|r|\log n\sim \frac{\gamma_N|r|\log n}{m\log m}.
\]
Entlang \(|r|\to\infty\) bei festem \(m\): \(\to\infty\) (Konfinement hält in \(r\)). Entlang \(m\to\infty\) bei festem \(r\): \(\to 0\) (Konfinement bricht in \(m\)-Richtung). Ergebnis: **partielles Konfinement nur in der \(r\)-Achse**, nicht global. \(\quad\times/\mbox{❓}\,[\mathrm{M}]\)

### 5.2 B2: L-Rekalibrierung \(\ell(a)\to\ell(a)+m\log m\)

Mit dem stärkeren Energiegewicht wird der Schur-Quotient
\[
Q_{B2}(m)\sim\frac{\gamma_N\,m(\log m)^2 r}{r\,m\log m}=\gamma_N\log m
\le \frac{C\log m}{\log N}\le C\quad(m\le N).
\tag{56.10}
\]
Der Schur-Test ist nun **beschränkt** (Wachstum von \(m\) auf \(\log m\) reduziert). **Aber:** \(\|Lx\|\) wächst jetzt wie \(m\log m\), während \(\|D_{\mathrm{rel}}x\|\) weiterhin nur wie \(\gamma_N|r|\log n\) wächst. Die Konfinement-Ungleichung (K) verschlechtert sich dadurch noch:
\[
\|D_{\mathrm{rel}}x\|+\|x\|\ \ll\ \|Lx\|\sim m\log m.
\tag{56.11}
\]
B2 rettet also Selbstadjungiertheit/Schur, macht Weg A aber **erst recht** unmöglich. \(\quad\times\,[\mathrm{M}]\)

**Befund Option B:** Keine getestete Reskalierung (skalar, separabel, oder L-Rekalibrierung) erfüllt (N1)/(N2) **und** (K) zugleich mit dem Vergleichsoperator \(L\). Die Obstruktion ist robust gegenüber dieser Klasse von Modifikationen.

---

## 6. Satz 56.4 — Entscheidung Weg A vs. Weg B

\[
\boxed{
\begin{aligned}
\text{Weg B (Spektralmaß-Form):}\ &
R_{\mathrm{rel}}(s)[a,b]=\int_{\mathbb{R}}\frac{1}{\lambda-s}\,d\mu_{a,b}(\lambda)
\quad\text{gilt allein aus (56.9).} && \checkmark\,[\mathrm{M}]\\[4pt]
\text{Weg A (kompakter Resolvent):}\ &
\text{über Vergleichsoperator } L \text{ verschlossen (Satz 56.2).} && \times\,[\mathrm{M}]\\[4pt]
\text{Weg A offen:}\ &
\text{nur über einen anderen, mit } J^- \text{ verträglichen Vergleichsoperator } \tilde L. && \mbox{❓}\,[\mathrm{O}]
\end{aligned}}
\tag{56.12}
\]

Damit ist **Weg B (NEU-53)** der getragene Standard. Die robuste Einheitsform aus NEU-53 (Resolventen-Matrixelement, \(K_{pq}\)) bleibt der Arbeitsrahmen.

---

## 7. Was Weg A noch retten könnte (Forschungsagenda, ❓ [O])

Ein **kompakter Resolvent** erfordert einen Vergleichsoperator \(\tilde L\) mit:
1. \(\tilde L\) hat kompakten Resolventen (Eigenwerte \(\to\infty\), endliche Multiplizität auf \(\mathcal{H}_{\mathrm{rel}}^{\mathrm{eff}}\)),
2. \(\tilde L\lesssim |D_{\mathrm{rel}}|\) (echtes Konfinement, **nicht** über das skalare \(\gamma_N\) erzwungen),
3. Verträglichkeit \([\,J^-,\tilde L\,]\) Schur-kontrolliert.

Kandidaten:
- **\(\tilde L\) als Funktion von \(J^-\) selbst**, z.B. \(\tilde L=(1+(J^-)^2)^{1/2}\): dann ist (K) trivial (\(\tilde L=|D_{\mathrm{rel}}|\)), aber Kompaktheit des Resolventen wird zur Frage über das Wachstum der singulären Werte von \(J^-\) auf \(\mathcal{H}_{\mathrm{rel}}^{\mathrm{eff}}\) — das ist der eigentliche, bisher nicht adressierte Spektralpunkt.
- **Spurklasse-Kriterium** über \(K_{pq}\) (NEU-51): falls \(\sum_p \mathrm{Tr}\,|M_p(z)|<\infty\) gleichmäßig, ergäbe sich diskretes Spektrum — zu prüfen.

> Damit verschiebt sich die *eigentliche* Weg-A-Frage weg von der γ_N-Wahl hin zum **Wachstum der singulären Werte von \(J^-\)** auf \(\mathcal{H}_{\mathrm{rel}}^{\mathrm{eff}}\). Das ist der präzise Nachfolge-Engpass.

---

## 8. Statusmatrix

| Aussage | Status |
|---|---|
| \(\gamma_N=C/\log N\) löst Spannung (NEU-55 §6) | \(\times\) [M] **widerlegt** |
| Korrekte globale Schur-Rate \(\gamma_N\le K/(N\log N)\) (56.6) | \(\checkmark\) [M] |
| Globaler Schur \(\Rightarrow\) Konfinement bricht (56.7–56.8) | \(\times\) [M] **Obstruktion** |
| (N1)/(N2) und (K) skalar unvereinbar (Satz 56.2) | \(\times\) [M] |
| Essentielle Selbstadjungiertheit bleibt gültig (Satz 56.3) | \(\checkmark\) [M] |
| Option B1 (separables \(w(m)\)) | \(\times\)/❓ [M] partiell |
| Option B2 (L-Rekalibrierung) | \(\times\) [M] |
| Weg B (Spektralmaß) robuster Standard | \(\checkmark\) [M] |
| Weg A über \(L\) | \(\times\) [M] verschlossen |
| Weg A über \(\tilde L\) (sing. Werte von \(J^-\)) | ❓ [O] **neuer Engpass** |
| RH-Hinrichtung braucht nur SA, nicht Weg A | \(\checkmark\) [M] |

---

## 9. Nächster Schritt

\[
\boxed{
\text{NEU-57: Wachstum der singulären Werte von } J^- \text{ auf } \mathcal{H}_{\mathrm{rel}}^{\mathrm{eff}};
\ \text{Spurklasse-Kriterium via } K_{pq} \text{ (NEU-51) für kompakten Resolventen.}
}
\]

Teilfragen:
1. Singulärwert-Asymptotik \(s_k(J^-|_{\mathcal{H}_{\mathrm{rel}}^{\mathrm{eff}}})\) — divergiert sie (Weg A möglich) oder akkumuliert sie (nur Weg B)?
2. Gilt \(\sum_p\mathrm{Tr}\,|M_p(z)|<\infty\) gleichmäßig in \(z\) auf Kompakta?
3. Ist die RH-Hinrichtung mit reiner Spektralmaß-Form (Weg B) vollständig formulierbar, ohne Weg A?

---

*Erstellt 29. Juni 2026 — NEU-56. Lakatosianische Epistemik: alle Aussagen markiert. Symbolische Asymptotik unabhängig nachgerechnet (sympy).*
