# Direktaudit NEU-212 — Zieltypbrücke, Intermediäres Koeffizientenmodul \(\mathcal A^\infty\)

**Gesamtstatus der geschriebenen Fassung: ×[M]**  
**Auditdatum:** 2026-08-03  
**Auditiert von:** Chat-Session (Perplexity/Akademisch)  
**Vorgänger-Audits:** ARCHIV-AUDIT-NEU210.md, ARCHIV-AUDIT-NEU211.md

---

## Auditumfang

Geprüft wurden:
- `06-hochschild-bc-algebra/NEU-212_Zieltypbruecke_Intermediaeres_Koeffizientenmodul_A-infty.md` vollständig.
- Die behauptete faktorial-Sobolev-Algebra \(\mathcal B^\infty\) und die daraus abgeleitete geladene Algebra \(\mathcal A^\infty\).
- Die Regularisierungen der Transportdefekte \(G_{a,d}\).
- Die Definition \(\widetilde D_g(e(r)):=0\) auf BC-Kreuzrelationsverträglichkeit.
- Die behauptete HH\(^1\)-Klasse und die angekündigte Cup-Brücke.
- Den Revisionsknoten `NEU-213` hinsichtlich der Statusübernahme.

---

## Gesamturteil

NEU-212 konstruiert in der geschriebenen Form **weder** das behauptete intermediäre Koeffizientenmodul
\[
A_{\mathrm{alg}}\subsetneq \mathcal A^\infty \subsetneq A_{C^*},
\]
**noch** eine regularisierte geladene Derivation
\[
\widetilde D_g: A_{\mathrm{alg}}\to \mathcal A^\infty.
\]

Die drei zentralen positiven Behauptungen der Datei scheitern:
1. Die definierte schnelle Abfallbedingung enthält nicht einmal die Einheit und daher nicht \(A_{\mathrm{alg}}\).
2. Die logarithmische Regularisierung liefert nur Abfall der Größenordnung \(1/(j\log j)\), nicht schnellen Abfall.
3. Die Abbildung mit \(\widetilde D_g(e(r))=0\) verletzt eine BC-Kreuzrelation und ist daher **keine Derivation**.

Ein kleiner neutraler Kern bleibt verwertbar: Die Datei definiert im abelschen Sektor einen nichtunitalen Raum rasch gegen \(0\) verschwindender Funktionen. Außerdem liegt der korrigierte Charakterkoeffizient aus NEU-211 tatsächlich in diesem neutralen Raum. Daraus entsteht aber noch keine geladene Fréchet-Algebra und keine Hochschildklasse.

---

## Revidierte Knotenstatustabelle

| Knoten | Revidierter Status | Befund |
|---|---|---|
| [O-212-1] geschrieben | ×[M] | \(1,e(r)\notin\mathcal B^\infty\); keine Algebra zwischen \(A_{\mathrm{alg}}\) und \(A_{C^*}\) |
| [O-212-1a] | ✓[K/M] | Neutraler nichtunitaler Schnellabfallraum \(\mathcal S_0\) |
| [O-212-1b] | ×[M] | Geladene Fréchet-\(*\)-Algebra nicht konstruiert |
| [O-212-2a] | ×[M] | Tailabschneidung erhält \(1/j\)-Abfall |
| [O-212-2b] | ×[M] | Log-Regularisierung nur \(O(1/(j\log j))\), nicht Schwartz |
| [O-212-2] | ×[M] | Zentraler Regularisierungssatz widerlegt |
| [O-212-3] | ×[M] | Verletzt BC-Kreuzrelation; keine Derivation |
| [O-212-3HH] | ×[M] | Keine Klasse in \(HH^1(A_{\mathrm{alg}},\mathcal A^\infty)_g\) |
| [O-212-char] | ✓[M] | Korrigierter Charakterkoeffizient besitzt endlichen Schalenträger |
| [O-212-4a] | ✓[M]_neg | Divergenzbeweis ausgeschlossen; Quotient exakt \(1\) |
| [O-212-5] | ?[O] | Cup-Brücke offen und derzeit untypisiert |
| [O-211-6] | ?[O] | Durch NEU-212 **nicht** teilweise geschlossen |

---

## Kernbefunde

### 1. [O-212-1] geschrieben — ×[M]

Die definierte Bedingung misst **absoluten** Schnellabfall auf faktorialen Schalen, nicht „Schwingung“. Damit werden alle nichtverschwindenden konstanten Funktionen ausgeschlossen. Insbesondere gilt:
\[
1\notin \mathcal B^\infty, \qquad e(r)\notin \mathcal B^\infty.
\]

Da \(1,e(r)\in A_{\mathrm{alg}}\), ist die behauptete Inklusion
\[
A_{\mathrm{alg}}\subseteq \mathcal A^\infty
\]
mit dieser Koeffizientendefinition unmöglich.

### 2. [O-212-1a] — ✓[K/M]

Mathematisch sinnvoll bleibt der neutrale Raum
\[
\mathcal S_0 := \{f\in C(\hat{\mathbb Z}) : p_k(f)<\infty \ \forall k\},
\]
mit
\[
p_k(f)=\sup_{j\ge 0}(j+1)^k\sup_{x\in S_j}|f(x)|,
\qquad S_j=L_j\hat{\mathbb Z}\setminus L_{j+1}\hat{\mathbb Z}.
\]

Für jedes \(f\in\mathcal S_0\) gilt \(f(0)=0\). Unter punktweiser Multiplikation, Konjugation sowie den festen Transporten \(T_a,\rho_d\) bleibt dieser Raum stabil.

### 3. [O-212-1b] — ×[M]

Die „volle“ geladene Algebra
\[
\overline{\operatorname{span}}^{\mathcal B^\infty\text{-koeff.}}\{\mu_k b\mu_{k'}^*\}
\]
ist nicht präzise definiert: Es fehlen Topologie, Gradkontrolle, Produktabschluss unter den BC-Relationen und Stetigkeit der Adjunktion. Damit ist **keine** geladene Fréchet-\(*\)-Algebra konstruiert.

### 4. [O-212-2a]/[O-212-2b]/[O-212-2] — ×[M]

Die Tailabschneidung beseitigt das asymptotische Verhalten \(G_{a,d}(x)=O(1/j)\) auf der Schale \(\nu(x)=j\) nicht. Auch die logarithmische Regularisierung
\[
\widetilde G_{a,d}(x)=\frac{G_{a,d}(x)}{\log(\nu(x)+2)}
\]
führt nur zu
\[
\widetilde G_{a,d}(x)=O\!\left(\frac{1}{j\log j}\right),
\]
nicht zu schnellem Abfall.

**Explizites Gegenbeispiel:** Für \(a=2,d=1\) ist \(G_{2,1}=B_2\). Mit \(x_j=(j+2)!/2\) für gerade \(j\) gilt
\[
\nu(x_j)=j,\qquad \nu(2x_j)=j+1,
\]
und damit
\[
\widetilde G_{2,1}(x_j)
=\frac{\log((j+3)/(j+2))}{\log(j+2)}
\sim \frac{1}{j\log j}.
\]
Folglich divergiert bereits die Halbnorm \(k=2\):
\[
(j+1)^2|\widetilde G_{2,1}(x_j)|\sim \frac{j}{\log j}\to\infty.
\]
Also \(\widetilde G_{2,1}\notin \mathcal B^\infty\).

### 5. [O-212-3] — ×[M]

NEU-212 setzt erneut
\[
\widetilde D_g(e(r))=0,
\]
obwohl nach dem Audit von NEU-211 verbindlich ist:
\[
D_g^{\mathrm{corr}}(e(r))=\mu_m C_{m,n;r}\mu_n^*.
\]

**Explizite Relationsverletzung:** Wähle \(g=2\), also \(m=2,n=1\), und den Generator \(\mu_2\). Die BC-Relation
\[
e(1/4)\mu_2=\mu_2 e(1/2)
\]
würde für eine Derivation mit trivialer Charakterwirkung erzwingen:
\[
e(1/4)\widetilde D_2(\mu_2)=\widetilde D_2(\mu_2)e(1/2).
\]
Mit \(\widetilde D_2(\mu_2)=\mu_4\widetilde G_{2,1}\) ist die Differenz aber
\[
\mu_4\widetilde G_{2,1}(1-e(1/2)),
\]
und am Punkt \(x=1\) gilt
\[
\widetilde G_{2,1}(1)=\frac{\log(3/2)}{\log 2}\neq 0,
\qquad e(1/2)(1)=-1.
\]
Daraus folgt ein nichtverschwindender Wert
\[
2\frac{\log(3/2)}{\log 2}\neq 0.
\]
Also respektiert \(\widetilde D_2\) die BC-Kreuzrelation nicht.

### 6. [O-212-3HH] — ×[M]

Da \(\widetilde D_g\) keine Derivation ist, definiert diese Abbildung **keinen** Hochschild-1-Kozykel. Aussagen wie
\[
[\widetilde D_g]\in HH^1(A_{\mathrm{alg}},\mathcal A^\infty)_g
\]
sind in der geschriebenen Fassung bedeutungslos.

### 7. [O-212-char] — ✓[M]

Der **korrigierte** Charakterkoeffizient
\[
C_{m,n;r}=\sum_{j=0}^{J(r)-1} c_j M_{m,n;r}q_j
\]
hat endlichen Schalenträger und erfüllt daher jede Schnellabfallbedingung. Somit gilt:
\[
C_{m,n;r}\in B_{\mathrm{alg}}\cap \mathcal S_0.
\]

Der Charakterfehler ist also für die Derivation fatal, aber der korrigierte Charakterwert selbst bildet **keine** Schnellabfallobstruktion.

### 8. [O-212-4a] — ✓[M]_neg

Der vorgeschlagene Offdiagonaltest liefert nicht divergende Matrixelemente, denn mit \(c_j=\log(j+2)\) gilt exakt
\[
\frac{c_j}{\log(j+2)}=1.
\]
Damit ist gerade dieser Nichtinnerheitsbeweis ausgeschlossen.

### 9. [O-212-5] — ?[O]

Die genannte Cup-Formel ist nur ein Zielbild. Es fehlen:
- eine präzise Koeffizientenmultiplikation
\(\mathcal A^\infty\otimes_{A_{\mathrm{alg}}}\mathcal A^\infty\to\mathcal A^\infty\),
- ein typisierter HH\(^3\)-Partner,
- und eine Nichtexaktheitsanalyse.

Damit bleibt die Zieltyp-/Cup-Brücke vollständig offen.

---

## Bewertung von NEU-213

NEU-213 erkennt zwei Fehler korrekt:
- \(c_j/\log(j+2)=1\), also kein divergierender Offdiagonaltest;
- die punktweise Regularisierung ist kein \(A_{\mathrm{alg}}\)-Bimoduloperator.

Die Statuskorrektur bleibt aber **zu schwach**. Insbesondere müssen nun gelten:
- `[O-212-2]` : `?[O] → ×[M]`
- `[O-212-3]` : `?[O] → ×[M]`

NEU-213 sollte daher zusammen mit NEU-212 in einem späteren Korrekturcommit nachgezogen werden.

---

## Korrigierter DAG

```text
[O-211-6] intermediäres Koeffizientenmodul / Cup-Brücke ?[O]
      |
      +--> [O-212-1] ×[M]
      |    behauptete A_alg-enthaltende Fréchet-Algebra existiert so nicht
      |
      +--> [O-212-1a] ✓[K/M]
      |    neutraler nichtunitaler Schnellabfallraum S_0
      |
      +--> [O-212-char] ✓[M]
      |    C_{m,n;r} hat endlichen Schalenträger und liegt in S_0
      |
      +--> [O-212-2a] ×[M]
      |    Tailabschneidung regularisiert nicht schnell genug
      |
      +--> [O-212-2b] ×[M]
      |    G/log(ν+2) nur O(1/(j log j))
      |
      +--> [O-212-3] ×[M]
      |    D~_g(e(r))=0 verletzt BC-Kreuzrelation
      |
      +--> [O-212-4a] ✓[M]_neg
      |    Offdiagonal-Divergenzroute ausgeschlossen
      |
      +--> [O-212-5] ?[O]
           typkorrekte Koeffizientenmultiplikation,
           HH³-Partner und Cup-Nichtexaktheit fehlen
```

---

## Erforderlicher Korrekturblock für NEU-212

```markdown
AUDITKORREKTUR 2026-08-03

Gesamtstatus der geschriebenen Fassung: ×[M].

1. Die Definition von B^∞ misst absoluten Schnellabfall und enthält weder 1
   noch die Charaktere e(r). Daher gilt A_alg ⊄ A^∞.

2. Die Abschätzung
   (j+1)^k / ((j+2) log(j+2)) → 0
   ist für k ≥ 2 falsch. Der Kandidat G~/log(ν+2) liegt im Allgemeinen
   nicht in B^∞.

3. Die Definition D~_g(e(r)) = 0 übernimmt den widerlegten Charakterfehler
   aus NEU-211 und verletzt eine BC-Kreuzrelation. D~_g ist keine Derivation.

4. Es entsteht keine Klasse in HH¹(A_alg,A^∞)_g und noch kein Cup-Pfeil
   nach HH⁴.

Verbindlich bleiben:
- der neutrale nichtunitale Schnellabfallraum;
- C_{m,n;r} besitzt endlichen Schalenträger;
- der Cup-/Zieltypknoten bleibt offen.
```

---

## Nächster Auditknoten

NEU-212 schließt **keine** Zieltypbrücke; `[O-211-6]` bleibt vollständig offen. Der nächste verbindliche Direktaudit ist daher:

\[
\boxed{\texttt{NEU-216_Log_Koeffiziententyp_B-log.md}}
\]

Zu prüfen ist dort insbesondere, ob \(\mathcal B^{\log}\)
- wirklich ein \(A_{\mathrm{alg}}\)-Bimodul ist,
- alle korrigierten Charakterwerte \(\mu_mC_{m,n;r}\mu_n^*\) enthält,
- sämtliche Transportdefekte \(G_{a,d}\) enthält,
- unter linken und rechten BC-Wirkungen stabil ist,
- eine typkorrekte Hochschild-Koeffizientenstruktur trägt,
- und ob es nur Zielraum oder bereits cup-fähige Algebra liefert.

*Wichtigster neuer Befund gegenüber NEU-213:*  
\[
\boxed{[O\text{-}212\text{-}2]\text{ und }[O\text{-}212\text{-}3]\text{ sind direkt widerlegt, nicht nur ungeklärt.}}
\]
