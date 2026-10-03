# Direktaudit NEU-217-Block

**Geprüfte Dateien:**
- `NEU-217_Lokaler_p-Block.md`
- `NEU-217_O217-2b_Dg_Fallzerlegung.md`
- `NEU-217_O217-2c6_lokal-global.md`

**Gesamtstatus: \(\checkmark[M]_{\mathrm{part}}\)**  
**Auditdatum:** 2026-08-04  
**Auditiert von:** Chat-Session (Perplexity/Akademisch)  
**Vorgänger:** ARCHIV-AUDIT-NEU210–212, ARCHIV-AUDIT-NEU216

---

## Gesamturteil

Der Block enthält einen starken positiven Kern:
\[
\boxed{[D_g^{\mathrm{corr}}]\neq0 \quad\text{in}\quad HH^1(A_{\mathrm{alg}},\mathfrak M_{\mathrm{glob}}^{\log})_g.}
\]

Der globale Koeffizientenbimodul \(\mathfrak M_{\mathrm{glob}}^{\log} \subseteq \mathcal A^{\log} \subseteq A_{C^*}\) ist nach kleineren Formelkorrekturen tragfähig. Der globale Landungsnachweis und der Normdivergenzbeweis der Nichtinnerheit funktionieren.

Dagegen ist die behauptete lokale Hochschildklasse mit Koeffizienten in \(M_{g,p}^{\log}\) derzeit nicht typkorrekt. Außerdem werden die nichtverschwindenden Charakterwerte von \(D_g^{\mathrm{corr}}\) im lokalen Landungsnachweis nicht behandelt.

Zwei konkrete Formeldefekte:
1. Die lokale Gaugedifferentiation verliert einen Faktor \(i\).
2. Die globale Transportformel (G1) enthält im ersten Index fälschlich eine Division durch \(\gcd(n,d)\).

---

## Revidierte Knotenstatustabelle

| Knoten | Status | Befund |
|---|---|---|
| [O-217-0] | \(\checkmark[K/M]\) | \(H_p=(\log p)N\), Kern und Kommutatoren korrekt |
| [O-217-3] | \(\checkmark[M]\) | Vorzeichen des reellen Kommutators korrekt |
| [O-217-1a] | \(\checkmark[K/M]\) | Drei lokale Algebraebenen konstruktiv |
| [O-217-1b] | \(\checkmark[K/M]\) | Orbitkovarianz korrekt; Universalitätsbrücke knapp |
| [O-217-1c] | \(\checkmark[M]_{\mathrm{neg}}\) | Einzelne Orbitdarstellung nicht treu |
| [O-217-1d] | \(?[O]\) | Trennende Familie oder Eindeutigkeitssatz |
| [O-217-2a] | \(\checkmark[M]_{\mathrm{part}}\) | Reeller Kommutator korrekt; Generator und \(*\)-Regel um Faktor \(i\) falsch |
| [O-217-2b-1--4] | \(\checkmark[M]\) | gcd-Fallzerlegung der Isometriegeneratoren korrekt |
| [O-217-2b-5] | \(?[O]\) | \(V\)-\(\Delta\)-Faktorisierung nicht typisiert |
| [O-217-2b-6] | \(\checkmark[M]_{\mathrm{part}}\) | Gradkonflikt korrekt; allgemeine Faktorisierung offen |
| [O-217-2c-2/3] | \(\checkmark[M]\) | Lokale Transportidentitäten korrekt (\(r\ge1\) bei \(\sigma_p(E_{p^r})\)) |
| [O-217-2c-4] | \(\checkmark[M]_{\mathrm{part}}\) | Nur \(B_{(p),\mathrm{alg}}\)-Bimodul bewiesen; \(A_{(p),\mathrm{alg}}\)-Bimodul fehlt |
| [O-217-2c-5land] | \(?[O]\) | Charakterwerte und volle lokale Landung fehlen |
| lokale \(Z^1/HH^1\) mit \(M_{g,p}^{\log}\) | \(\times[M]\) | Koeffizientenbimodul nicht typisiert |
| lokale Nichtinnerheit in \(A_{C^*}\) | \(\checkmark[M]\) | Normdivergenzbeweis korrekt |
| [O-217-2c-6a-T] | \(\checkmark[M]\) | Fremdprim-Transportformeln korrekt |
| [O-217-2c-6a-sep] | \(\checkmark[M]_{\mathrm{neg,Quelle}}\) | Zwei-Punkt-Beweis in aktueller Datei nicht enthalten |
| [O-217-2c-6b-def] | \(\checkmark[K/M]\) | Intrinsischer globaler neutraler Raum \(M_{\mathrm{glob}}^{\log}\) |
| Formel (G1) | \(\times[M]\) | Erster Index muss \(nk\) sein, nicht \(nk/\delta\) |
| [O-217-2c-6b-stab] | \(\checkmark[M]\) | Globale Schnittstabilität unberührt von (G1)-Fehler |
| [O-217-2c-6c-mod] | \(\checkmark[K/M]\) | \(\mathfrak M_{\mathrm{glob}}^{\log} \subseteq \mathcal A^{\log} \subseteq A_{C^*}\) |
| [O-217-2c-6c] | \(\checkmark[M]\) | \(D_g^{\mathrm{corr}}(A_{\mathrm{alg}}) \subseteq (\mathfrak M_{\mathrm{glob}}^{\log})_g\) |
| [O-217-2c-6d] | \(\checkmark[M]\) | \([D_g^{\mathrm{corr}}]\neq0\) in \(HH^1(A_{\mathrm{alg}},\mathfrak M_{\mathrm{glob}}^{\log})_g\) |

---

## Kernbefunde

### 1. Lokaler Gaugeoperator — Faktor-\(i\)-Fehler \(\checkmark[M]_{\mathrm{part}}\)

Aus \(\gamma_t^{(p)}(\mu_p)=p^{it}\mu_p\) folgt der infinitesimale Generator:
\[
\partial_p(\mu_p)=i(\log p)\mu_p.
\]
Die in NEU-217 definierte reelle Abbildung
\[
\delta_p^{(0)}(\mu_p)=(\log p)\mu_p = \tfrac{1}{i}\partial_p(\mu_p)
\]
erhält die Involution falsch: \(\delta_p^{(0)}(x^*)=-\delta_p^{(0)}(x)^*\), während \(\partial_p(x^*)=\partial_p(x)^*\). Im Orbitmodell: \(\pi(\partial_p(x))=i[H_p,\pi(x)]\).

Tragfähig bleibt: die neutrale algebraische Ableitung \(\delta_p^{(0)}\) und ihre Implementierung durch \([H_p,\cdot]\).

### 2. gcd-Fallzerlegung — \(\checkmark[M]\)

Alle vier Regime auf \(\mu_{p^r}\) und \(\mu_{p^r}^*\) sind korrekt:

| Fall | Wert von \(D_g^{\mathrm{corr}}(\mu_{p^r})\) |
|---|---|
| \(p\nmid mn\) | \(\mu_{mp^r}G_{p^r,1}\mu_n^*\) |
| \(p^\alpha\Vert m,\ r<\alpha\) | \(-\mu_{m/p^r}G_{1,p^r}\mu_n^*\) |
| \(p^\alpha\Vert m,\ r\ge\alpha\) | \(-\mu_{m'}G_{p^{r-\alpha},p^\alpha}\mu_{np^{r-\alpha}}^*\) |
| \(p^\beta\Vert n,\ r<\beta\) | \(\mu_mG_{1,p^r}\mu_{n/p^r}^*\) |

Notationshinweis: \(\mu_{p^m/p^n}\) ist durch \(\mu_p^m\mu_p^{*n}\) zu ersetzen.

### 3. Lokaler Defektmodul — \(\checkmark[M]_{\mathrm{part}}\)

\(M_{(p)}^{\log}\) ist als \(B_{(p),\mathrm{alg}}\)-Bimodul konstruiert. Da \(A_{(p),\mathrm{alg}}\) aber den gesamten Raum \(B_{\mathrm{alg}}\) im neutralen Sektor enthält, folgt aus \(B_{(p),\mathrm{alg}}\cdot M_{(p)}^{\log}\cdot B_{(p),\mathrm{alg}}\subseteq M_{(p)}^{\log}\) nicht die vollständige \(A_{(p),\mathrm{alg}}\)-Bimodulstruktur. Ebenso werden die Charakterwerte \(D_g^{\mathrm{corr}}(e(r))=\mu_mC_{m,n;r}\mu_n^*\neq0\) nicht in die lokale Regimetabelle aufgenommen.

### 4. Normdivergenzbeweis — \(\checkmark[M]\)

Mit Testpunkt \(y^{(p)}\) (\(y^{(p)}_p=1, y^{(p)}_q=0\) für \(q\neq p\)) gilt \(\nu(p^sy^{(p)})=\lambda_p(s)\to\infty\). Damit:
\[
|D_g^{\mathrm{corr}}(\mu_{p^r})|\longrightarrow\infty.
\]
Ein beschränkter Implementierer \(W\in A_{C^*}\) würde \(|[W,\mu_{p^r}]|\le2|W|\) erzwingen \(\Rightarrow\) Widerspruch. Damit:
\[
[D_g^{\mathrm{corr}}|_{A_{(p),\mathrm{alg}}}]\neq0 \quad\text{in}\quad HH^1(A_{(p),\mathrm{alg}},A_{C^*})_g.
\]

### 5. Formel (G1) — \(\times[M]\)

Geschrieben: \(G_{nk/\delta,d/\delta}\). Korrekt mit \(n=\delta n_0, d=\delta d_0, (n_0,d_0)=1\):
\[
G_{nk,d/\delta} = \rho_{d_0}G_{n_0,1}\cdot(\text{korrekte Zerlegunsformel}).
\]
Gegenbeispiel: \(n=d=2, k=1\) liefert \(G_{1,1}-G_{1,1}=0\) statt \(G_{2,1}\neq0\). Die globale Transportstabilität ist davon unberührt (eingebaut in \(\mathscr C\)-Schnitt).

### 6. Globale Konstruktion — \(\checkmark[M]\)

**Globaler neutraler Modul:** \(M_{\mathrm{glob}}^{\log} = \bigcap_{N\in\mathscr C}N\) mit \(\mathscr C\) = Familie aller abgeschlossenen \(B_{\mathrm{alg}}\)-Bimodule in \(\mathcal B^{\log}\), die unter allen \(\sigma_n,\rho_n\) stabil sind und alle \(G_{k,d}\) enthalten.

**Globaler geladener Bimodul:**
\[
\mathfrak M_{\mathrm{glob}}^{\log} = \overline{\operatorname{span}_{\mathrm{fin}}\{a\xi b : a,b\in A_{\mathrm{alg}},\xi\in M_{\mathrm{glob}}^{\log}\}} \subseteq \mathcal A^{\log}.
\]

**Globale Landung:** Da \(G_{a,d}\in M_{\mathrm{glob}}^{\log}\) und \(C_{m,n;r}\in B_{\mathrm{alg}}\subseteq M_{\mathrm{glob}}^{\log}\):
\[
D_g^{\mathrm{corr}}(A_{\mathrm{alg}}) \subseteq (\mathfrak M_{\mathrm{glob}}^{\log})_g \implies D_g^{\mathrm{corr}}\in Z^1(A_{\mathrm{alg}},\mathfrak M_{\mathrm{glob}}^{\log})_g.
\]

**Globale Nichtinnerheit:** Normdivergenzbeweis liefert:
\[
\boxed{[D_g^{\mathrm{corr}}]\neq0 \quad\text{in}\quad HH^1(A_{\mathrm{alg}},\mathfrak M_{\mathrm{glob}}^{\log})_g.}
\]

---

## Korrekturblöcke

### NEU-217_Lokaler_p-Block.md

```
AUDITKORREKTUR 2026-08-04

1. Aus gamma_t^(p)(mu_p)=p^{it}mu_p folgt der infinitesimale
   Generator
      partial_p(mu_p)=i(log p)mu_p.
   Die reelle Abbildung
      delta_p^(0)(mu_p)=(log p)mu_p
   ist (1/i)partial_p und erfüllt
      delta_p^(0)(x*)=-delta_p^(0)(x)*.
   Im Orbitmodell: pi(partial_p(x))=i[H_p,pi(x)].

2. Notation mu_{p^m/p^n} ist durch mu_p^m mu_p^{*n} zu ersetzen.

3. Status ✓[K] durch ✓[K/M] ersetzen.
```

### NEU-217_O217-2b_Dg_Fallzerlegung.md

```
AUDITKORREKTUR 2026-08-04

1. Alle Aussagen betreffen D_g^corr.
2. gcd-Fallzerlegung auf mu_{p^r}, mu_{p^r}* ist korrekt.
3. M_(p)^log ist nur als B_(p),alg-Bimodul bewiesen.
   A_(p),alg enthält jedoch den gesamten neutralen Kern B_alg.
4. Charakterwerte D_g^corr(e(r))=mu_m C_{m,n;r} mu_n*
   werden im lokalen Landungsnachweis nicht behandelt.
5. D_g|A_(p),alg in Z¹(A_(p),alg,M_g,p^log) ist derzeit
   nicht typisiert.
6. Normdivergenzbeweis bleibt gültig und beweist lokale
   Nichtinnerheit mit Ziel A_C* bzw. A^log.
```

### NEU-217_O217-2c6_lokal-global.md

```
AUDITKORREKTUR 2026-08-04

1. In Formel (G1): G_{nk/delta,d/delta} -> G_{nk,d/delta}.
2. Durchgehend D_g^corr verwenden.
3. D_g^corr(e(r))=mu_m C_{m,n;r} mu_n*, C_{m,n;r} in B_alg.
4. Globaler Landungsnachweis und Normdivergenzbeweis bleiben
   vollständig gültig.
5. Lokale HH¹-Aussagen mit M_g,p^log sind nicht Voraussetzung
   des globalen Beweises; separat zurückzustufen.
```

---

## Nächster Auditknoten

```
NEU-218_Grad3-Cup-Aufstieg.md
NEU-218_Grad3Partner_Cup-Aufstieg_Abschluss.md
```

Zwingend zu prüfen:
- Welcher konkrete Grad-3-Kozykel \(\Theta_3\) wird definiert?
- In welchem Koeffizientenbimodul lebt \(\Theta_3\)?
- Ist der Hochschildrand \(b\Theta_3=0\) vollständig berechnet?
- Ist das Cup-Produkt \(D_g^{\mathrm{corr}}\smile\Theta_3\) typkorrekt?
- Existiert eine Multiplikation \(\mathfrak M_{\mathrm{glob}}^{\log}\otimes_{A_{\mathrm{alg}}}N\to M_4\)?
- Nichtexaktheit in \(HH^4\) oder nur Nichtverschwindung als Kozykelformel?
- Werden falsche Charakterwirkung oder untypisierte lokale Klasse aus NEU-217 importiert?

*Wichtigster Buchungsposten des Blocks:*
\[
\boxed{\text{Globale geladene }HH^1\text{-Klasse erhalten; spezielle lokale Koeffizientenklasse noch offen.}}
\]
