# Direktaudit NEU-216 — Logarithmischer Koeffiziententyp \(\mathcal B^{\log}\)

**Gesamtstatus der geschriebenen Fassung: \(\checkmark[M]_{\mathrm{part}}\)**  
**Auditdatum:** 2026-08-04  
**Auditiert von:** Chat-Session (Perplexity/Akademisch)  
**Vorgänger-Audits:** ARCHIV-AUDIT-NEU210.md, ARCHIV-AUDIT-NEU211.md, ARCHIV-AUDIT-NEU212.md

---

## Gesamturteil

NEU-216 erreicht einen echten konstruktiven Fortschritt. Der logarithmische Koeffiziententyp funktioniert im Kern:
\[
\mathcal B_{\mathrm{alg}} \subsetneq \mathcal B^{\log} \subsetneq C(\widehat{\mathbb Z})
\]
kann als unitaler Banach-\(*\)-Koeffiziententyp korrekt konstruiert werden. Die Transporte \(\sigma_k, \rho_k, T_a = \sigma_a\) erhalten \(\mathcal B^{\log}\), und die Transportdefekte erfüllen \(G_{a,d} \in \mathcal B^{\log}\). Die korrekte geladene Derivation erfüllt tatsächlich
\[
D_g^{\mathrm{corr}}(A_{\mathrm{alg}}) \subseteq \mathcal A^{\log},
\]
und es entsteht eine nichttriviale algebraische Hochschildklasse:
\[
\boxed{[D_g^{\mathrm{corr}}] \neq 0 \quad \text{in} \quad HH^1(A_{\mathrm{alg}}, \mathcal A^{\log})_g.}
\]

Nicht konstruiert sind:
- eine globale Banach- oder Fréchet-Vervollständigung der gesamten Gradsumme;
- ein kontinuierlicher Hochschildkomplex;
- ein Grad-3-Partner;
- ein Cup-Aufstieg nach \(HH^4\).

Die öffentliche rev.6 bezeichnet alle Knoten als geschlossen, lässt aber die zentralen Definitionen von \(\mathcal B^{\log}\), den Schalen und beiden Seminormen im Dateitext aus. Außerdem enthält sie eine falsche gcd-Relation und verweist beim Derivationsbild nicht eindeutig auf \(D_g^{\mathrm{corr}}\).

---

## Revidierte Knotenstatustabelle

| Knoten | Revidierter Status | Befund |
|---|---|---|
| [O-216-def] | \(\checkmark[K/M]\) | Fehlende Definitionen eindeutig ergänzbar |
| aktuelle Quelldefinition | \(\warning[M]\) | \(S_j, \nu, [\cdot]_{\tan}, [\cdot]_{\mathrm{rad}}, \mathcal B^{\log}\) fehlen in rev.6 |
| [O-216-0] | \(\checkmark[M]\) | BC-Konventionen korrekt |
| [O-216-2c] | \(\checkmark[M]\) | Band-Mittelwertlemma korrekt |
| [O-216-2a] | \(\checkmark[M]\) | Vorwärtsband; \(x\neq0\), \(C_\sigma(1)=0\) ergänzen |
| [O-216-2b] | \(\checkmark[M]\) | Rückwärtsband und \(\rho_k\)-Stabilität |
| [O-216-2d] | \(\checkmark[K/M]\) | \(T_a = \sigma_a\) als kanonische Wahl |
| [O-216-2] | \(\checkmark[M]\) | Gesamt: alle Transporte erhalten \(\mathcal B^{\log}\) |
| [O-216-3] | \(\checkmark[M]\) | \(G_{a,d} \in \mathcal B^{\log}\) |
| [O-216-1] | \(\checkmark[M]\) | Banach-\(*\)-Algebra nach Definitionsergänzung |
| gcd-Relation mit \(1/r\) | \(\times[M]\) | Korrekte Relation enthält keinen Skalarfaktor |
| [O-216-4a] | \(\checkmark[K/M]\) | Graduierte algebraische \(*\)-Algebra \(\mathcal A^{\log}\) |
| [O-216-4b] | \(\checkmark[M]\) | \(D_g^{\mathrm{corr}}(A_{\mathrm{alg}}) \subseteq \mathcal A^{\log}\) |
| [O-216-4c] | \(\checkmark[M]\) | \([D_g^{\mathrm{corr}}] \neq 0\) in \(HH^1(A_{\mathrm{alg}}, \mathcal A^{\log})_g\) |
| **[O-211-6a]** | **\(\checkmark[M]\)** | **Zieltypbrücke algebraisch positiv geschlossen** |
| [O-216-top] | \(?[O]\) | Globale Banach-/Fréchet-Vervollständigung |
| [O-216-cup] | \(?[O]\) | Grad-3-Partner, Cup-Kozykel und Nichtexaktheit |

---

## Kernbefunde

### 1. Fehlende Zentraldefinitionen — \(\warning[M]\)

Rev.6 verwendet \(S_j, \nu(x), [f]_{\tan}, [f]_{\mathrm{rad}}, \mathcal B^{\log}\) ohne innere Definition. Kanonische Ergänzung:
\[
L_j = (j+1)!, \quad P_j = 1_{L_j\widehat{\mathbb Z}}, \quad S_j = L_j\widehat{\mathbb Z}\setminus L_{j+1}\widehat{\mathbb Z},
\]
\[
\nu(x) = \max\{j : (j+1)! \mid x\} \quad (x\neq0),
\]
\[
m_j(f) = \int_{S_j} f\,d\mu_j, \qquad [f]_{\tan} = \sup_{j\ge0}(j+1)\operatorname{osc}_{S_j}(f),
\]
\[
[f]_{\mathrm{rad}} = \sup_{j\ge0}(j+1)|m_{j+1}(f)-m_j(f)|,
\]
\[
\mathcal B^{\log} = \{f\in C(\widehat{\mathbb Z}) : |f|_{\mathcal B^{\log}} := |f|_\infty + [f]_{\tan} + [f]_{\mathrm{rad}} < \infty\}.
\]

Echte Inklusionen:
\[
\mathcal B_{\mathrm{alg}} \subsetneq \mathcal B^{\log} \subsetneq C(\widehat{\mathbb Z}).
\]

### 2. [O-216-2] — \(\checkmark[M]\): Transporte erhalten \(\mathcal B^{\log}\)

**Vorwärtsband \(\sigma_k\):** Für \(x\neq0\) gilt \(0 \le \nu(kx)-\nu(x) \le C_\sigma(k)\), wobei \(C_\sigma(k) = \sum_{p\mid k} p \cdot v_p(k)\) und \(C_\sigma(1)=0\). Damit \(\sigma_k(\mathcal B^{\log}) \subseteq \mathcal B^{\log}\).

**Rückwärtsband \(\rho_k\):** \(\rho_k f(x) = 1_{k\widehat{\mathbb Z}}(x)f(x/k)\); für \(j\ge J(k)\) gilt \(S_j\subseteq k\widehat{\mathbb Z}\) und \(\nu(x)-C_\sigma(k) \le \nu(x/k) \le \nu(x)\). Damit \(\rho_k(\mathcal B^{\log}) \subseteq \mathcal B^{\log}\). Hinweis: \(\rho_k\) ist nicht unital (\(\rho_k(1)=E_k \neq 1\) für \(k>1\)).

**Kanonischer Transport \(T_a = \sigma_a\):** Durch BC-Kovarianz \(f\mu_a = \mu_a\sigma_a(f)\) kanonisch bestimmt.

### 3. [O-216-3] — \(\checkmark[M]\): Transportdefekte \(G_{a,d} \in \mathcal B^{\log}\)

Für \(x \in d\widehat{\mathbb Z}\):
\[
G_{a,d}(x) = \log\frac{\nu(adx/d)+2}{\nu(x/d)+2},
\]
wobei \(0 \le \nu(ady/y) - \nu(y) \le C_\sigma(ad)\). Auf tiefen Schalen:
\[
(j+1)\operatorname{osc}_{S_j}(G_{a,d}) = O(1), \qquad (j+1)|m_{j+1}(G_{a,d})-m_j(G_{a,d})| = O(1).
\]
Dies löst exakt das Problem, an dem NEU-212 scheiterte: Die Defekte fallen nur wie \(1/j\), und \(\mathcal B^{\log}\) verlangt logarithmische, nicht beliebig schnelle Kontrolle.

### 4. [O-216-1] — \(\checkmark[M]\): Banach-\(*\)-Algebra

**Submultiplikativität:**
\[
[fg]_{\tan} \le |f|_\infty[g]_{\tan} + |g|_\infty[f]_{\tan},
\]
\[
[fg]_{\mathrm{rad}} \le |f|_\infty[g]_{\mathrm{rad}} + |g|_\infty[f]_{\mathrm{rad}} + [f]_{\tan}[g]_{\tan}.
\]
Damit \(|fg|_{\mathcal B^{\log}} \le |f|_{\mathcal B^{\log}}|g|_{\mathcal B^{\log}}\).

**Vollständigkeit:** Cauchyfolgen sind uniform Cauchy, Limes liegt in \(C(\widehat{\mathbb Z})\); beide Zusatzseminormen sind unterhalbstetig.

### 5. Fehler in der gcd-Relation — \(\times[M]\)

Die geschriebene Relation \(\mu_{n_1}^*\mu_{p_1} = \mu_{p_1}\mu_{n_1}^*/r\) ist falsch. Korrekt mit \(r=(n,p), n=rn_1, p=rp_1, (n_1,p_1)=1\):
\[
\mu_n^*\mu_p = \mu_{p_1}\mu_{n_1}^*.
\]
Kein Skalarfaktor \(1/r\). Der falsche Faktor wird in der Produktformel nicht weiter verwendet; es handelt sich um einen lokalen Formeldefekt, nicht um einen Zusammenbruch der Konstruktion.

### 6. [O-216-4a/4b/4c] — \(\checkmark[M]\): Geladener Koeffiziententyp und HH\(^1\)-Klasse

**Graduierte Algebra:** \(\mathcal A^{\log} = \bigoplus_h^{\mathrm{alg}} \mathcal A_h^{\log}\) mit \(\mathcal A_h^{\log} = \mu_m\mathcal B^{\log}\mu_n^*\) (\(h=m/n\) gekürzt) ist graduierte algebraische \(*\)-Algebra.

**Korrekte Produktformel:** Mit \(s=(mp_1,qn_1), M=mp_1/s, N=qn_1/s\):
\[
(\mu_mf\mu_n^*)(\mu_pg\mu_q^*) = \mu_M\rho_s(\sigma_{p_1}(f)\sigma_{n_1}(g))\mu_N^*.
\]

**Enthalt von \(A_{\mathrm{alg}}\):** Da \(\rho_s(\mathcal B_{\mathrm{alg}}) \subseteq \mathcal B_{\mathrm{alg}} \subseteq \mathcal B^{\log}\), gilt \(A_{\mathrm{alg}} \subsetneq \mathcal A^{\log} \subseteq A_{C^*}\).

**Derivationsbild:** Da \(G_{a,d} \in \mathcal B^{\log}\) und \(C_{m,n;r} \in \mathcal B_{\mathrm{alg}} \subseteq \mathcal B^{\log}\), gilt \(D_g^{\mathrm{corr}}(A_{\mathrm{alg}}) \subseteq \mathcal A^{\log}\).

**Nichttrivialität:** Da \([D_g^{\mathrm{corr}}] \neq 0\) in \(HH^1(A_{\mathrm{alg}}, A_{C^*})_g\) (verbindliches Kontrollblatt) und \(\mathcal A^{\log} \subseteq A_{C^*}\), kann \(D_g^{\mathrm{corr}}\) auch in \(\mathcal A^{\log}\) keinen Implementierer besitzen:
\[
\boxed{[D_g^{\mathrm{corr}}] \neq 0 \quad \text{in} \quad HH^1(A_{\mathrm{alg}}, \mathcal A^{\log})_g.}
\]

**Folgerung:** Der intermediare Zieltypknoten ist algebraisch positiv geschlossen: \([O\text{-}211\text{-}6\mathrm{a}]\) \(\checkmark[M]\).

### 7. Was NEU-216 nicht beweist

- **[O-216-top] ?[O]:** Keine Norm auf der Gradsumme; \(\mathcal A^{\log}\) ist nur als algebraische Summe definiert.
- **[O-216-cup] ?[O]:** Kein Grad-3-Partner \(\Theta \in HH^3(A_{\mathrm{alg}}, \mathcal A^{\log})\), kein Cup-Produkt \(D_g^{\mathrm{corr}} \smile \Theta\), keine Nichtexaktheit geprüft.

---

## Korrigierter DAG

```text
NEU-212 ×[M]
  zu starke Schwartz-Regularisierung
        |
        v
[O-216-def] ✓[K/M]
  logarithmische Schalen-Seminormen
        |
        +--> [O-216-1] ✓[M]
        |    B_alg ⊊ B^log ⊊ C(Zhat)
        |    unitaler Banach-*-Koeffiziententyp
        |
        +--> [O-216-2] ✓[M]
        |    sigma_k, rho_k und T_a erhalten B^log
        |
        +--> [O-216-3] ✓[M]
        |    G_{a,d} ∈ B^log
        |
        +--> gcd-Relation mit 1/r ×[M]
        |          |
        |          v
        |    korrigierte Produktformel (kein 1/r)
        |
        +--> [O-216-4a] ✓[K/M]
        |    A^log = span_fin{mu_m B^log mu_n*}
        |    graduierte algebraische *-Algebra
        |
        +--> [O-216-4b] ✓[M]
        |    D_g^corr(A_alg) ⊂ A^log
        |
        +--> [O-216-4c] ✓[M]
        |    [D_g^corr] ≠ 0 in HH¹(A_alg,A^log)_g
        |    ==> [O-211-6a] ✓[M]
        |
        +--> [O-216-top] ?[O]
        |    globale topologische Vervollständigung
        |
        +--> [O-216-cup] ?[O]
             Grad-3-Partner und Cup-Aufstieg
```

---

## Erforderlicher Korrekturblock für NEU-216

```
AUDITKORREKTUR 2026-08-04

Gesamtstatus: ✓[M]_part.

1. In der aktuellen rev.6 fehlen die Definitionen von S_j, ν,
   [·]_tan, [·]_rad und B^log. Sie müssen vor Abschnitt 216.A
   vollständig eingefügt werden.

2. „Normiertes Haarmaß auf S_j“ ist durch „normalisierte Einschränkung
   des Haarmaßes auf S_j“ zu ersetzen.

3. C_sigma(1) := 0 und alle ν-Transportformeln sind für x ≠ 0 zu lesen.

4. Die Relation
      μ_{n1}* μ_{p1} = μ_{p1} μ_{n1}* / r
   ist falsch. Korrekt ist
      μ_n* μ_p = μ_{p1} μ_{n1}*.
   Es tritt kein Faktor 1/r auf.

5. In der Produktreduktion sind
      s = (mp1, qn1),  M = mp1/s,  N = qn1/s
   explizit zu definieren.

6. Die Zieltypaussage gilt ausschließlich für die korrigierte Derivation:
      D_g^corr(e(r)) = μ_m C_{m,n;r} μ_n*.

7. Korrekt und neu zu verbuchen:
      [D_g^corr] ≠ 0  in  HH¹(A_alg, A^log)_g.

8. Offen bleiben:
   - globale Banach-/Fréchet-Topologie der Gradsumme;
   - kontinuierlicher Hochschildkomplex;
   - Grad-3-Partner;
   - Cup-Aufstieg nach HH⁴.
```

---

## Nächster Auditknoten

NEU-216 repariert die **Zieltypbrücke** erfolgreich, aber noch nicht die **Cup-Brücke**.

Der nächste verbindliche Direktaudit folgt der Reihenfolge:
\[
\text{NEU-217\_Lokaler\_p-Block} \longrightarrow \text{NEU-217\_O217-2b} \longrightarrow \text{NEU-217\_O217-2c6}
\]

Dort zu prüfen:
- Welcher lokale \(p\)-Koeffizientenraum wird definiert?
- Ist er ein \(A_{\mathrm{alg}}\)-Bimodul oder nur ein lokaler Funktionsraum?
- Wird \(D_g^{\mathrm{corr}}(e(r)) = \mu_m C_{m,n;r}\mu_n^*\) korrekt verwendet?
- Ist die lokale Fallzerlegung für alle gcd-Fälle typkorrekt?
- Existiert eine echte lokal-globale Klebeabbildung?
- Wird bereits ein Grad-3-Partner oder Cup-Produkt behauptet?

*Wichtigster neuer Buchungsposten:*
\[
\boxed{[D_g^{\mathrm{corr}}] \neq 0 \quad \text{in} \quad HH^1(A_{\mathrm{alg}}, \mathcal A^{\log})_g.}
\]
Diese Aussage ist algebraisch vollständig gesichert; topologische und Cup-fähige Verfeinerung bleiben offen.
