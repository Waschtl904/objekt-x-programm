# P11-C1k2 — Direkte BC-Rangeprojektions-Realisierung des GCD-Labelkerns

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1k2]` — Provenienzverstärkung von C1k  
**Vorgänger:** P11-C1k  
**Primärquelle:** `KONVENTIONEN.md` §4: `E_n=1_{n\widehat{\mathbb Z}}=\rho_n(1)`  

**Urteil:**

\[
\boxed{[P11-C1k2]\quad\checkmark[K/M]}
\]

Der in C1k konstruierte kanonische Label-Gramkern

\[
c(n,m)=\frac{\gcd(n,m)}{\sqrt{nm}}
\]

ist **direkt** als Gramkern normierter BC-Rangeprojektionen auf dem Haarraum `L^2(\widehat{\mathbb Z})` realisiert. Damit stammt die Labelgeometrie nicht nur aus einer neuen Common-Multiple-Darstellung, sondern bereits aus einem verbindlichen BC-Grundobjekt des Repos.

---

## 1. BC-Rangeprojektionen

Die verbindlichen Konventionen fixieren

\[
\boxed{
E_n:=\mu_n\mu_n^*=1_{n\widehat{\mathbb Z}}
=\rho_n(1).
}
\]

Sei `m_Haar` das normierte Haarmaß auf dem kompakten Ring `\widehat{\mathbb Z}`.

Für jedes `n\ge1` besitzt die offene/abgeschlossene Untergruppe

\[
n\widehat{\mathbb Z}
\]

Index `n`. Daher

\[
\boxed{m_{\rm Haar}(n\widehat{\mathbb Z})=\frac1n.}
\]

---

## 2. Normierte Rangeprojektionsvektoren

Definiere

\[
\boxed{
\zeta_n
:=
\sqrt n\,E_n
=\sqrt n\,1_{n\widehat{\mathbb Z}}
\in L^2(\widehat{\mathbb Z},m_{\rm Haar}).
}
\]

Dann

\[
\|\zeta_n\|_2^2
=n\,m_{\rm Haar}(n\widehat{\mathbb Z})
=1.
\]

Damit ist die Normierung **kanonisch durch den Index** bestimmt; kein freier Gewichtsfaktor wird gewählt.

Status: `✓[K/M]`.

---

## 3. Schnitt zweier BC-Rangebereiche

Für positive ganze Zahlen `n,m` gilt

\[
n\widehat{\mathbb Z}\cap m\widehat{\mathbb Z}
=\operatorname{lcm}(n,m)\widehat{\mathbb Z}.
\]

Daher

\[
\begin{aligned}
\langle\zeta_n,\zeta_m\rangle
&=
\sqrt{nm}\int_{\widehat{\mathbb Z}}E_n(x)E_m(x)\,dm_{\rm Haar}(x)\\
&=
\sqrt{nm}\;m_{\rm Haar}(\operatorname{lcm}(n,m)\widehat{\mathbb Z})\\
&=
\frac{\sqrt{nm}}{\operatorname{lcm}(n,m)}.
\end{aligned}
\]

Mit

\[
\gcd(n,m)\operatorname{lcm}(n,m)=nm
\]

folgt exakt

\[
\boxed{
\langle\zeta_n,\zeta_m\rangle
=
\frac{\gcd(n,m)}{\sqrt{nm}}.
}
\]

Dies ist genau der C1k-Kern.

Status: `✓[K/M]`.

---

## 4. Prime-Power-Spezialisierung

Für `n=p^k`, `m=q^\ell`:

### `p\neq q`

\[
\boxed{
\langle\zeta_{p^k},\zeta_{q^\ell}\rangle
=
\frac1{\sqrt{p^kq^\ell}}>0.
}
\]

### `p=q`

\[
\boxed{
\langle\zeta_{p^k},\zeta_{p^\ell}\rangle
=p^{-|k-\ell|/2}.
}
\]

### Diagonale

\[
\boxed{\|\zeta_{p^k}\|=1.}
\]

Damit ist die Rangeprojektionsgeometrie gleichzeitig

- vollständig Prime-Power-indiziert;
- nichtorthogonal über verschiedene Primlabels;
- markierungserhaltend auf endlichen Gramblöcken;
- RH-frei.

---

## 5. Direkter Zusammenhang mit BC-Endomorphismen

Da

\[
E_n=\rho_n(1),
\]

ist die Labelgeometrie direkt aus den Range-Endomorphismen der BC-Algebra aufgebaut.

Die Kreuzkopplung entsteht nicht aus einer frei gewählten Zahlentheorie-Matrix, sondern aus der tatsächlichen Überlappung der BC-Rangeprojektionen:

\[
\boxed{
E_nE_m
=1_{\operatorname{lcm}(n,m)\widehat{\mathbb Z}}.
}
\]

Die arithmetischen Operationen `gcd` und `lcm` erscheinen damit als **Schnittgeometrie der BC-Rangebereiche**.

---

## 6. Reconciliation mit der Traegertrennung

Für verschiedene Primlabels `p\neq q` ist

\[
E_{p^k}E_{q^\ell}
=E_{p^kq^\ell}.
\]

Der Schnittbereich gehört multiplikativ zum gemischten Sektor. Genau wie in C1j/NEU-250j gilt dort kein diagonales Mangoldtgewicht.

Das ist kein Problem, weil C1k2 den Mischbereich ausschließlich zur **Gramüberlappung der Labels** verwendet:

\[
\boxed{
\text{Mischsektor = Schnitt-/Mediatorgeometrie, nicht zusätzlicher Weil-Diagonalkanal.}
}
\]

Damit respektiert die Konstruktion die Trägertrennung vollständig.

---

## 7. Drei äquivalente Realisierungen desselben Kerns

P11 besitzt nun drei unabhängige Darstellungen:

### A. BC-Rangeprojektionen

\[
\zeta_n=\sqrt n\,1_{n\widehat{\mathbb Z}}.
\]

### B. Common-Multiple-/Dirichlet-Grenzkern aus C1k

\[
\lim_{\beta\downarrow1}
\langle\xi_n^{(\beta)},\xi_m^{(\beta)}\rangle
=
\frac{\gcd(n,m)}{\sqrt{nm}}.
\]

### C. Divisor-/Euler-`\varphi`-Inzidenz

\[
\xi_n^{\rm div}
=
\frac1{\sqrt n}
\sum_{d\mid n}\sqrt{\varphi(d)}e_d.
\]

Alle drei liefern denselben Gramkern.

Diese Dreifachrealisierung ist ein starker Kanonizitätsbefund: der Kern ist gleichzeitig

- Range-Schnittgeometrie;
- Common-Multiple-Geometrie;
- Common-Divisor-Geometrie.

---

## 8. Kein Konflikt mit P05-Wres-Überlappungen

Der C1k2-Kern ist **nicht** die historische `Wres`-Paarung der `\eta`-Graphbasis.

Er lebt auf dem abelschen BC-Rangeprojektionssektor `C(\widehat{\mathbb Z})\subset A_{C^*}`.

Daher muss P11 strikt unterscheiden:

\[
\boxed{
\text{BC-Range-Labelgram}
\neq
\text{Wres-Graphgram}.
}
\]

Die erste Struktur ist nun explizit und positiv; die zweite enthält zusätzliche dynamische/relative Informationen und ist nicht vollständig kanonisiert.

P11 darf sie später koppeln, aber nicht stillschweigend identifizieren.

---

## 9. Kombination mit analytischer Inzidenz

Mit dem C1c-Operator

\[
V_{p,k}^{an}
=
\sqrt{\frac{\log p}{p^{k/2}}}
D_{k\log p}
\]

kann unmittelbar

\[
\boxed{
\mathcal V_{p,k}a
:=
V_{p,k}^{an}a\otimes\zeta_{p^k}
}
\]

gebildet werden.

Dann

\[
\boxed{
\langle\mathcal V_{p,k}a,\mathcal V_{q,\ell}b\rangle
=
\frac{\gcd(p^k,q^\ell)}{\sqrt{p^kq^\ell}}
\sqrt{
\frac{\log p}{p^{k/2}}
\frac{\log q}{q^{\ell/2}}
}
\langle D_{k\log p}a,D_{\ell\log q}b\rangle.
}
\]

Diese Formel ist nun vollständig auf **zwei im Repo verankerten Quellen** aufgebaut:

1. P02/P11-C1c: logarithmischer Translationsfluss;
2. BC-Konventionen/P11-C1k2: Rangeprojektionsgeometrie.

Keine Primhebung wird benötigt.

---

## 10. Kanonizitätsstatus

| Kriterium | Status |
|---|---|
| aus verbindlichen BC-Grundobjekten gebaut | `PASS` |
| freie Kopplungsmatrix | `NEIN` |
| Prime-Power-Labels vollständig | `PASS` |
| Crossprime nichtorthogonal | `PASS` |
| Diagonalnorm 1 | `PASS` |
| cutoff-kompatibel | `PASS` |
| RH-/Nullstellendaten | `NEIN` |
| markierungserhaltender endlicher Gramraum | `PASS` |
| Gleichsetzung mit Wres-Graphgram | **nicht erlaubt** |
| exakte Weil-Kompression | `OPEN` |
| archimedische Labelerweiterung | `OPEN` |

---

## 11. Wichtigster Befund

C1k hatte einen mathematisch kanonischen GCD-Kern konstruiert.

C1k2 verbessert die Provenienz entscheidend:

\[
\boxed{
C_{nm}^{can}
=
\langle\sqrt n\,E_n,\sqrt m\,E_m\rangle_{L^2(\widehat{\mathbb Z})}.
}
\]

Damit ist die offene Labelmatrix aus C1g **nicht mehr nur ein Kandidat aus einer neuen Hilfskonstruktion**, sondern direkt in der vorhandenen BC-Rangegeometrie sichtbar.

---

## 12. Nächster Knoten

Der nächste Engpass bleibt:

\[
\boxed{[P11\text{-}C1l]\quad\text{Archimedische Erweiterung und exakte Source-Kompression}.}
\]

Besonders zu testen ist, ob die adelische gemeinsame Quelle eine kanonische Kopplung zwischen dem BC-Rangeprojektionsraum und dem kontinuierlichen Gamma-Inzidenzraum aus C1d vorgibt. Ohne eine solche Quelle darf kein Vektor für den archimedischen Platz in `L^2(\widehat{\mathbb Z})` frei gewählt werden.
