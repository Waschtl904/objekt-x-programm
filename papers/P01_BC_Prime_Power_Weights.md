# P01 — BC Prime-Power Weights and Local Arithmetic Structure

**Status:** SYN FINAL AUDITED — Dependency-Reconciled for P09  
**Datum:** 9. August 2026  
**Auditbasis:** `audits/AUDIT-2026-08-09_P01_Dependency_Reaudit_vor_P09.md` (`0bf1018e`)  
**Quellbasis:** doppelt gepruefter F4-Endstand der NEU-250f–r-Kette

---

## 1. Scope

P01 fixiert nur den heute gesicherten lokalen BC-/Primzahlpotenz-Endstand. Es behauptet **keine** vollstaendige globale Operatorrealisierung der von-Mangoldt-Funktion und keine Objekt-X-/Hilbert–Polya-Konstruktion.

---

## 2. Primitiver BC-p-Kanal

Im in NEU-250g explizit behandelten primitiven Kanal

\[
j_R=e_RV_p
\]

gilt algebraisch

\[
h_p^{\rm bal}=p^{-1/2}I,
\qquad
H_{\rm BC}j_R=(\log p)j_R.
\]

Damit entsteht im primitiven Kanal der Faktor

\[
\boxed{\frac{\log p}{\sqrt p}.}
\]

**Status:** `INCORPORATED_part`.  
**Offen:** Hilbert-Selbstadjungiertheit, Abschluss, Domaene und globaler Funktionalkalkuel von `H_BC`.

---

## 3. Arithmetische Primzahlpotenzidentitaet

Fuer jede Primzahl `p` und jedes `m>=1` gilt

\[
\boxed{
\frac{\Lambda(p^m)}{\sqrt{p^m}}
=
\frac{\log p}{p^{m/2}}.
}
\]

Dies ist eine rein arithmetische, RH-freie Identitaet.

**Status:** `✓[M]`.

### Firewall 3.1 — Arithmetik ist nicht Operatorrealisierung

Die allgemeine operatorische Formel

\[
h_n^{\rm bal}=n^{-1/2}I\qquad(n\ge1)
\]

ist im auditierten Quellenkegel **nicht bewiesen**. NEU-250g rechnet den primitiven `p`-Kanal; die all-`n`-Generalisierung in NEU-250i besitzt eine ungedeckte Rueckreferenz.

Daher bleibt die vollstaendige operatorische Primzahlpotenzrealisierung ueber `h_{p^m}^{bal}` bzw. `H_pr`:

\[
\boxed{\texttt{CONDITIONAL / ?[O]}.}
\]

Insbesondere wird keine globale Operatoridentitaet `H_pr = Lambda` behauptet.

---

## 4. Traegertrennung

Seien `p != q` Primzahlen und

\[
p m_p=q m_q=M.
\]

Dann besitzt `M` mindestens zwei verschiedene Primteiler. Folglich

\[
\Lambda(M)=0.
\]

Damit gilt fuer die in NEU-250j untersuchte direkte Kreuzprimkollision

\[
\boxed{
\operatorname{supp}\Lambda
\cap
\operatorname{supp}(\text{direkte Kreuzprimkollision})
=
\varnothing.
}
\]

**Status:** `✓[M]`.

### Firewall 4.1 — Traegertrennung ist keine Orthogonalitaet

Dieser Satz impliziert weder paarweise Orthogonalitaet noch Disjunktheit der Primkanalbilder als Hilbertraum-Unterraeume. Die generische nichtorthogonale Primkanalgeometrie aus P05 bleibt unberuehrt.

---

## 5. Statusmatrix

| Aussage | Status |
|---|---|
| primitiver Faktor `log p / sqrt(p)` | `INCORPORATED_part` |
| `Lambda(p^m)/sqrt(p^m)=log p/p^(m/2)` | `✓[M]` |
| all-`n`-Operatorrealisierung `h_n^bal=n^-1/2 I` | `?[O] / CONDITIONAL` |
| Hilbert-Fundierung von `H_BC` | `?[O]` |
| Mangoldt-Traeger vs. direkte Kreuzprimkollision | `✓[M]` |
| daraus globale Kanalorthogonalitaet | **nicht behauptet** |

---

## 6. Provenienz

Verbindliche Grundlage ist der F4-Endstand mit NEU-250f Patch 1, NEU-250g–l, NEU-250n und dem Superseding-Scan NEU-250m/o/p/q/r. Der pfadgebundene externe F4-Zweitcheck fand keinen Gegenbefund.

**P09-Nutzung:** P01 darf in P09 nur mit den oben explizit genannten Firewalls als BC-Lokalgrundlage verwendet werden.
