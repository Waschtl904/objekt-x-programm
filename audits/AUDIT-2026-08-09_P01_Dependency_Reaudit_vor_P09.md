# P01 Dependency-Reaudit vor P09

**Datum:** 9. August 2026  
**Ziel:** `papers/P01_BC_Prime_Power_Weights.*` als belastbare Voraussetzung fuer P09 typisieren  
**Pruefart:** `AUDIT-RECONCILED` + `TARGETED-REAUDIT`  
**Primärbasis:** F4-Primäraudit `audits/AUDIT-2026-08-08_F4_Primaeraudit_Mangoldt_Primzahlpotenz_Mediator.md` + gueltiger pfadgebundener Zweitcheck `AUDIT-2026-08-09_F4_Zweitcheck_Pfadgebunden.md`

---

## 1. Ausgangsbefund

Die bisherige P01-LaTeX-Fassung war ein frueher `SYN, Entwurf` und enthielt drei zu starke Aussagen:

1. die BC/Frobenius/Nakayama-Energie-Realisierung von
   \[\Lambda(p^k)/\sqrt{p^k}\]
   sei fuer alle Primzahlpotenzen bereits vollstaendig kanonisch hergeleitet;
2. `All results are unconditional (RH-free)`;
3. NEU-250j liefere eine pauschale Disjunktheit/Orthogonalitaet aller Primzahlpotenzkanaele.

Diese Fassung ist gegen den spaeter doppelt geprueften F4-Endstand zu reconciliieren.

---

## 2. Verbindlicher F4-Endstand

### 2.1 Primitiver p-Kanal

Auf dem in NEU-250g explizit behandelten primitiven Kanal `j_R=e_RV_p` gilt algebraisch

\[
h_p^{\rm bal}=p^{-1/2}I,
\qquad
H_{\rm BC}j_R=(\log p)j_R,
\]

und damit der lokale Faktor

\[
\boxed{\frac{\log p}{\sqrt p}.}
\]

**Status fuer P01:** `INCORPORATED_part`.  
**Firewall:** Hilbert-Selbstadjungiertheit, Abschluss, Domaene und globaler Funktionalkalkuel von `H_BC` bleiben offen.

### 2.2 Arithmetische Primzahlpotenzidentitaet

Fuer jedes `m>=1` gilt zahlentheoretisch

\[
\boxed{
\frac{\Lambda(p^m)}{\sqrt{p^m}}
=
\frac{\log p}{p^{m/2}}.
}
\]

**Status:** `✓[M]`, RH-frei.

### 2.3 Operatorische all-n-Realisierung

Die starke operatorische Aussage

\[
h_n^{\rm bal}=n^{-1/2}I
\qquad (n\ge1)
\]

ist im auditierten Quellenkegel **nicht bewiesen**. NEU-250i schreibt diese Generalisierung NEU-250g zu, waehrend NEU-250g nur den primitiven `p`-Kanal rechnet.

Daher ist die operatorische Primzahlpotenzrealisierung ueber `h_{p^m}^{bal}` / `H_pr` weiterhin

\[
\boxed{\texttt{CONDITIONAL / ?[O]}.}
\]

### 2.4 Traegertrennung

Der gesicherte Satz aus NEU-250j lautet:

Wenn `p != q` und eine direkte Kreuzprimkollision `p m_p = q m_q = M` vorliegt, dann besitzt `M` mindestens zwei verschiedene Primteiler und daher

\[
\Lambda(M)=0.
\]

Also

\[
\boxed{
\operatorname{supp}\Lambda
\cap
\operatorname{supp}(\text{direkte Kreuzprimkollision})
=
\varnothing.
}
\]

Dies ist **keine** Aussage, dass die Primkanalbilder als Hilbertraum-Unterraeume orthogonal oder generell disjunkt seien. Die in P05/F3 gesicherte generische Nichtorthogonalitaet bleibt bestehen.

---

## 3. Urteil ueber die alte P01-Fassung

| Alte Aussage | Urteil | Ersatz |
|---|---|---|
| vollstaendig kanonische all-prime-power Operatorrealisierung | `SUPERSEDED` | primitive p-Realisierung `INCORPORATED_part`; all-n-Realisierung `CONDITIONAL/?[O]` |
| `All results are unconditional` | `SUPERSEDED` | nur arithmetische Identitaet und Traegerlemma unbedingt/RH-frei |
| pauschale Kanaldisjunktheit | `SUPERSEDED` | nur Traegertrennung Mangoldt vs. direkte Kreuzprimkollision |
| `H_pr = Lambda` als Operatoridentitaet | gesperrt | insbesondere auf Zahlen mit mehreren verschiedenen Primteilern falsch typisiert |

---

## 4. P01-Endstatus fuer P09

P01 darf als Voraussetzung fuer P09 verwendet werden **nur** in folgender Form:

1. BC-Zeitentwicklung liefert im primitiven p-Sektor algebraisch den Faktor `log p / sqrt(p)`;
2. `Lambda(p^m)/sqrt(p^m)=log p/p^(m/2)` ist eine arithmetische Identitaet;
3. die all-n-/Hilbert-Operatorrealisierung bleibt offen/konditional;
4. Traegertrennung ist kein Orthogonalitaetssatz.

Nach Synchronisierung von Markdown und LaTeX gilt:

\[
\boxed{\text{P01 DEPENDENCY RECONCILED fuer P09 — keine all-n-Hochstufung.}}
\]

Kein RH-Beweis, keine Objekt-X-Konstruktion, keine globale Hilbert-Pólya-Realisierung folgt hieraus.
