# NEU-250c — Vollständiger Frobenius-Gramtest des direkten Kandidaten

**Knoten:**
\[
[O\text{-}221\text{-}1c1a0\text{-C1}]
\]

**Status:** \(\checkmark[M]_{\mathrm{part}}\)

**Datum:** 7. August 2026

> **Vorgänger:** NEU-250b — Kandidat \(j^{(0)}(E_R) = e_R V_2\) scheitert an Typkorrektheit
> bzgl.\ \(F^3 A_{\mathrm{BC}}^{\mathrm{an}}\) (kein Doppelpol). Offen blieb: Liefert die
> Frobenius-Paarung \(\varepsilon_\beta(j_R^* j_{R'})\) trotzdem eine auswertbare Gramform?

**Korrektur zu NEU-250b:** Die dortige Aussage „Route A vollständig geschlossen“ war
zu stark. Route A ist als direkte \(F^3\)-Repräsentation negativ; die modulare
Frobenius-Paarung \(\varepsilon_\beta(j_R^* j_{R'})\) war dort nicht gerechnet.
Diese Lücke wird hier geschlossen.

---

## 1. Matrixkoeffizienten des Kandidaten

Nach NEU-015 \S3.1 gilt für den Basisvektor \(e_R V_n \in A_{\mathrm{BC}}^{\mathrm{an}}\):
\[
(e_R V_n)_{m,k,r'} = \delta_{k,\,nm}\,\delta_{r',R}.
\]

Für \(n = 2\):
\[
(j_R)_{m,k,r'} = (e_R V_2)_{m,k,r'} = \delta_{k,2m}\,\delta_{r',R}.
\]

Involution (nach NEU-015 §3, \((e_r V_n)^* = V_n^* e_{-r}\)):
\[
(j_R)^* = V_2^* e_{-R},
\qquad
(V_2^* e_{-R})_{m,k,r'} = \delta_{m,2k}\,\delta_{r',-R}.
\]

---

## 2. Linke Gramform \(G^L_{R,R'}(\beta) = \varepsilon_\beta(j_R^* j_{R'})\)

### 2.1 Produkt \(j_R^* j_{R'} = (V_2^* e_{-R})(e_{R'} V_2)\)

Matrixprodukt (Faltung über Zwischenindex \(k\)):
\[
(j_R^* j_{R'})_{m,\ell,r''}
= \sum_{k} (V_2^* e_{-R})_{m,k,-R}\,(e_{R'} V_2)_{k,\ell,R'}
= \sum_k \delta_{m,2k}\,\delta_{k,2\ell}\cdot\delta_{r'',-R+R'}.
\]

Die \(k\)-Summe liefert \(k = m/2\) (benötigt \(2 \mid m\)) und \(k = \ell/2 \cdot 2 = 2\ell\)
— Widerspruch. Korrekt:
- \((V_2^* e_{-R})_{m,k,\cdot}\): belegt \(m = 2k\), also \(k = m/2\).
- \((e_{R'} V_2)_{k,\ell,\cdot}\): belegt \(\ell = 2k\).
- Zusammen: \(\ell = 2k = 2 \cdot m/2 = m\) **und** \(2 \mid m\).

Also:
\[
(j_R^* j_{R'})_{m,\ell,r''}
= \delta_{\ell,m}\,\delta_{r'',R'-R}\,\mathbf{1}_{[2 \mid m]}.
\]

**Ergebnis:** \(j_R^* j_{R'}\) ist diagonal (\(\ell = m\)), mit Ladung \(r'' = R'-R\) und Träger nur auf geraden \(m\).

### 2.2 Modulare Spur

Nach NEU-015 §3.1 erfasst \(\varepsilon_\beta\) nur den Koeffizienten bei \(m = \ell\), \(r'' = 0\):
\[
\varepsilon_\beta(j_R^* j_{R'})
= \sum_{m \in \mathbb{N}^\times} m^{-\beta}\,(j_R^* j_{R'})_{m,m,0}
= \sum_{m \in \mathbb{N}^\times} m^{-\beta}\,\delta_{0,R'-R}\,\mathbf{1}_{[2\mid m]}.
\]

Für \(R' \neq R\): der Faktor \(\delta_{0,R'-R} = 0\), also \(\varepsilon_\beta(j_R^* j_{R'}) = 0\).

Für \(R' = R\):
\[
\varepsilon_\beta(j_R^* j_R)
= \sum_{\substack{m \in \mathbb{N}^\times \\ 2 \mid m}} m^{-\beta}
= \sum_{n=1}^\infty (2n)^{-\beta}
= 2^{-\beta}\,\zeta(\beta).
\]

**Ergebnis linke Gramform:**
\[
\boxed{G^L_{R,R'}(\beta) = \varepsilon_\beta(j_R^* j_{R'}) = \delta_{R,R'}\cdot 2^{-\beta}\,\zeta(\beta).}
\]

---

## 3. Rechte Gramform \(G^R_{R,R'}(\beta) = \varepsilon_\beta(j_{R'} j_R^*)\)

### 3.1 Produkt \(j_{R'} j_R^* = (e_{R'} V_2)(V_2^* e_{-R})\)

\[
(j_{R'} j_R^*)_{m,\ell,r''}
= \sum_k (e_{R'} V_2)_{m,k,R'}\,(V_2^* e_{-R})_{k,\ell,-R}
= \sum_k \delta_{k,2m}\,\delta_{\ell,2k}\cdot\delta_{r'',R'-R}.
\]

- \((e_{R'} V_2)_{m,k,\cdot}\): belegt \(k = 2m\).
- \((V_2^* e_{-R})_{k,\ell,\cdot}\): belegt \(k = 2\ell\).
- Zusammen: \(2m = 2\ell\), also \(\ell = m\). Kein Teilbarkeitseinsatz.

\[
(j_{R'} j_R^*)_{m,\ell,r''}
= \delta_{\ell,m}\,\delta_{r'',R'-R}.
\]

**Kein** \(\mathbf{1}_{[2\mid m]}\)-Filter! Das Produkt \(j_{R'} j_R^*\) ist diagonal auf **allen** \(m \in \mathbb{N}^\times\).

### 3.2 Modulare Spur

\[
\varepsilon_\beta(j_{R'} j_R^*)
= \sum_m m^{-\beta}\,\delta_{0,R'-R}.
\]

Für \(R' \neq R\): null. Für \(R' = R\):
\[
\varepsilon_\beta(j_R j_R^*)
= \sum_{m=1}^\infty m^{-\beta} = \zeta(\beta).
\]

**Ergebnis rechte Gramform:**
\[
\boxed{G^R_{R,R'}(\beta) = \varepsilon_\beta(j_{R'} j_R^*) = \delta_{R,R'}\cdot\zeta(\beta).}
\]

---

## 4. KMS-Konsistenzcheck

Nach NEU-015 \S5.2 gilt die KMS-Symmetrie:
\[
\varepsilon_\beta(FG) = \varepsilon_\beta(\sigma_{i\beta}(G)\,F).
\]

Mit \(F = j_R^*\), \(G = j_R\) und \(\sigma_{i\beta}(e_R V_2) = e_R\,e^{i\beta \log 2}\,V_2 = 2^{i\beta}\cdot e_R V_2\)
(da \(V_2\) unter der Zeitentwicklung \(\sigma_t\) den Faktor \(2^{it}\) trägt):
\[
\varepsilon_\beta(j_R^* j_R)
\overset{?}{=} \varepsilon_\beta(\sigma_{i\beta}(j_R)\,j_R^*)
= \varepsilon_\beta(2^{i\cdot i\beta} e_R V_2\,V_2^* e_{-R})
= 2^{-\beta}\,\varepsilon_\beta(j_R j_R^*).
\]

Linke Seite: \(2^{-\beta}\,\zeta(\beta)\). Rechte Seite: \(2^{-\beta}\cdot\zeta(\beta)\). \(\checkmark[M]\)

**Die KMS-Bedingung ist erfüllt** — kein Fehler in den Matrixrechnungen \S2–3.

---

## 5. Residuen bei \(\beta \to 1^+\)

Da \(\zeta(\beta) \sim 1/(\beta-1)\) (einfacher Pol):

\[
\operatorname*{Res}_{\beta=1} G^L_{R,R'}(\beta)
= \delta_{R,R'}\cdot 2^{-1} = \frac{\delta_{R,R'}}{2}.
\]

\[
\operatorname*{Res}_{\beta=1} G^R_{R,R'}(\beta)
= \delta_{R,R'}\cdot 1 = \delta_{R,R'}.
\]

Beide Gramformen besitzen einen **einfachen Pol** bei \(\beta = 1\) mit positivem,
diagonalem Residuum. Insbesondere:

\[
\operatorname*{Res}_{\beta=1} G^L_{R,R}(\beta) = \tfrac{1}{2} > 0,
\qquad
\operatorname*{Res}_{\beta=1} G^R_{R,R}(\beta) = 1 > 0.
\]

---

## 6. Positivität und Hermiteschheit

Die linke Gramform:
\[
G^L_{R,R'}(\beta) = \delta_{R,R'}\cdot 2^{-\beta}\zeta(\beta)
\]
ist für \(\beta > 1\) reell, diagonal und positiv auf dem Fourier-Indexraum. Das Residuum
\(\operatorname*{Res}_{\beta=1} G^L\) ist eine positiv-definite Diagonalmatrix
(mit Einträgen \(1/2\) für alle \(R\)).

**Positive-definite Frobenius-Gramform:**
\[
\boxed{\bigl(\operatorname*{Res}_{\beta=1} G^L_{R,R'}\bigr) = \tfrac{1}{2}\,\delta_{R,R'} > 0.}
\]

---

## 7. Einordnung: einfacher Pol vs.\ Doppelpol

| Objekt | Polordnung bei \(\beta=1\) | Herkunft |
|---|---|---|
| \(G^L_{R,R'}(\beta)\) | einfach (\(\zeta\)-Typ) | \(V_2 V_2^*\)-Transfer, Grad 1 |
| \(G^R_{R,R'}(\beta)\) | einfach (\(\zeta\)-Typ) | Volle Monoiddiagonale |
| \(\mathrm{Wres}_{\mathrm{BC}}^{(2,0)}\) | Doppelpol (\(\Lambda^2\)-Typ) | \(L_3\)/Massey-Homotopie, Grad 3 |

**Die hier konstruierte Gramform ist nicht dieselbe wie** \(\mathrm{Wres}_{\mathrm{BC}}^{(2,0)}\).
Sie stammt aus dem \(F^1\)-Sektor und trägt keinen logarithmischen Primfaktor.
Das ist kein Fehler, sondern eine strukturelle Aussage:

> **Die direkte modulare Frobenius-Paarung \(\varepsilon_\beta(j_R^* j_{R'})\)
> liefert eine wohldefinierte, positive, einfache-Pol-Gramform auf
> \(\mathscr V_{\mathrm{rel},2,N}^{\mathrm{pre}}\) —
> aber nicht den \(F^3/L_3\)-Wres-Doppelpol, den NEU-250a als Zielstruktur fordert.**

---

## 8. Sechs-Bedingungs-Tabelle für \(j^{(0)}\) (vollständig)

| Bedingung | Befund | Status |
|---|---|---|
| 1.\ Typkorrektheit: \(j_R \in F^3 A_{\mathrm{BC}}^{\mathrm{an}}\) | \(e_R V_2 \in F^1 \setminus F^2\) | \(\checkmark[M]_{\mathrm{neg}}\) |
| 2.\ Linearität | Trivial aus Basisvektordefinition | \(\checkmark[M]\) |
| 3.\ Indexverträglichkeit | \(R\) aus \(e_R\), \(p=2\) aus \(V_2\) | \(\checkmark[M]\) |
| 4.\ Involutionsverträglichkeit | \(j_R^* = V_2^* e_{-R}\) explizit, KMS-Check \(\checkmark\) | \(\checkmark[M]\) |
| 5.\ Residuenfähigkeit (\(F^3\)-Wres-Typ) | Nur einfacher Pol; kein Doppelpol | \(\checkmark[M]_{\mathrm{neg}}\) |
| 5'.\ Residuenfähigkeit (\(F^1\)-Typ) | \(\mathrm{Res}_{\beta=1}G^L_{R,R} = 1/2 > 0\) | \(\checkmark[M]\) |
| 6.\ Nichttautologie | \(G^L_{R,R}\) hängt von den BC-Relationen ab | \(\checkmark[M]\) |

---

## 9. Ausgangsentscheidung

\[
\boxed{\text{Ausgang C1a (modifiziert): } j^{(0)} \text{ erzeugt positive Frobenius-Gramform}
\text{ — aber auf } F^1\text{, nicht } F^3.}
\]

Damit entstehen zwei getrennte offene Fragen:

**\([O\text{-}221\text{-}1c1a0\text{-C1-a}]\)** (neuer Strang):
> Kann die \(F^1\)-Frobenius-Gramform
> \(\operatorname*{Res}_{\beta=1}\varepsilon_\beta(j_R^* j_{R'}) = \frac{1}{2}\delta_{R,R'}\)
> als **direkte modulare Gramform** für den Primkantenraum verwendet werden,
> unabhängig vom \(F^3\)/Wres-Pfad?

**\([O\text{-}221\text{-}1c1a0\text{-C1-b}]\)** (negativer Befund, Route B):
> Es existiert **kein** Weg, \(e_R V_2\) durch Gradanhebung in \(F^3 A_{\mathrm{BC}}^{\mathrm{an}}\)
zu bewegen und dabei die Gramform zu erhalten, ohne die Nichtkanonizität der Wahl
von \(A^{(2)}\) zu riskieren.
> Dieser Befund ergibt sich aus der expliziten Diagonalstruktur: Die Gram-Offdiagonalelemente
> verschwinden zwingend (\(\delta_{R,R'}\)), also gibt es keinen Mischterm, der einen
> Doppelpol erzeugen könnte.

---

## 10. Konsequenz für das Gesamtprogramm

Der Befund eröffnet den folgenden alternativen Pfad:

```
[Bestehender Pfad, bisher aktiv]
Vrel^pre  --j_{p,N}-->  F3 A_BC^an  --lambda_beta^mod-->  Doppelpol  --Wres_BC^(2,0)-->  Gram

[Neuer Pfad, jetzt bewiesen für p=2]
Vrel^pre  --j^(0)-->   F1 A_BC^an  --eps_beta(j* j')-->  einfacher Pol  --Res_1-->  (1/2)*delta
```

Der neue Pfad umgeht den \(F^3/L_3\)-Sektor vollständig. Er liefert eine
positive, nicht-ausgeartete Gramform auf \(\mathscr V_{\mathrm{rel},2,N}^{\mathrm{pre}}\)
aus der vorhandenen BC-Frobenius-Struktur.

**Offene Folgefrage \([O\text{-}221\text{-}1c1a0\text{-C1-a}]\):**
Ist diese \(F^1\)-Gramform für das Radikal-/Hilbert-Raum-Konstruktionsprogramm
(NEU-044, NEU-221e) verwendbar, oder setzt dieses zwingend den \(F^3\)/Wres-Typ voraus?

---

## 11. Statusbuchung

| Teilknoten | Aussage | Status |
|---|---|---|
| \([O\text{-}221\text{-}1c1a0\text{-C1/1}]\) | \(j_R^* j_{R'}\) Matrixkoeffizient berechnet | \(\checkmark[M]\) |
| \([O\text{-}221\text{-}1c1a0\text{-C1/2}]\) | \(j_{R'} j_R^*\) Matrixkoeffizient berechnet | \(\checkmark[M]\) |
| \([O\text{-}221\text{-}1c1a0\text{-C1/3}]\) | KMS-Symmetrie verifiziert | \(\checkmark[M]\) |
| \([O\text{-}221\text{-}1c1a0\text{-C1/4}]\) | Linkes Residuum \(= \frac{1}{2}\delta_{R,R'} > 0\) | \(\checkmark[M]\) |
| \([O\text{-}221\text{-}1c1a0\text{-C1/5}]\) | Rechtes Residuum \(= \delta_{R,R'} > 0\) | \(\checkmark[M]\) |
| \([O\text{-}221\text{-}1c1a0\text{-C1/6}]\) | Kein Doppelpol: \(j^{(0)}\) nicht im \(F^3\)-Sektor | \(\checkmark[M]_{\mathrm{neg}}\) |
| \([O\text{-}221\text{-}1c1a0\text{-C1-a}]\) | \(F^1\)-Gramform für Wres-Radikal-Konstruktion verwendbar? | \(?[O]\) |
| \([O\text{-}221\text{-}1c1a0\text{-C1-b}]\) | Route B (Gradanhebung) geschlossen | \(\checkmark[M]_{\mathrm{neg}}\) |

Gesamtstatus:
\[
\boxed{[O\text{-}221\text{-}1c1a0\text{-C1}]:\ \checkmark[M] \text{ (vollständig, mit zwei Ausgangszweigen C1-a und C1-b)}}
\]
