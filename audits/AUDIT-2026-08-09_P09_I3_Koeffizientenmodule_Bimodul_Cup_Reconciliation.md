# P09 / I3 — Koeffizientenmodule, Bimodul-No-go und geladener Cup-Aufstieg: Pass-A-Reconciliation

**Datum:** 9. August 2026  
**SYN-Ziel:** P09 — BC + Hochschild  
**Paket:** I3 — NEU-212–218  
**Prüfart:** `AUDIT-RECONCILED` / `AUDIT-REUSED` mit `TARGETED-REAUDIT` des NEU-218-Abschlussbeweises  
**Status:** **`I3 PASS A COMPLETE — GEGENCHECK AUSSTEHEND`**

---

## 0. Scope und autoritative Leserichtung

I3 umfasst pfadgebunden:

- `NEU-212_Zieltypbruecke_Intermediares_Koeffizientenmodul.md`,
- `NEU-213_Revisionsaudit_NEU212_Bimodul_Regularisierung.md`,
- `NEU-214_Bimodul_Rigiditaetslemma_Glattes_Potential.md`,
- `NEU-215_Zentralisator_Bimodul_No-go.md`,
- `NEU-216_Log_Koeffiziententyp_B-log.md`,
- die drei NEU-217-Dateien,
- die beiden NEU-218-Dateien.

Historische Direktaudit-Anker:

- `ARCHIV-AUDIT-NEU212.md`,
- `ARCHIV-AUDIT-NEU216.md`,
- `ARCHIV-AUDIT-NEU217.md`,
- `AUDITSTAND-2026-08-03.md`.

Spätere Reichweitenanker:

- `NEU-219_Finalaudit_Gesamtabschluss.md`,
- `OBJEKT-X-BESTANDSAUFNAHME.md`, Stand 5. August 2026,
- `NEU-222_Trassenaudit...` nur als lokaler Trassenbeleg, nicht als uneingeschränkter Superseder.

Verbindliche Präzedenz:

```text
August-Finalaudit / Bestandsaufnahme / Auditstand
    > node-spezifischer ARCHIV-AUDIT
    > Abschluss-/Revisionsdatei des Knotens
    > frühere Zwischenfassung.
```

Bei den Doppel-IDs NEU-217 und NEU-218 entscheidet der Pfad/Rollentyp, nicht die Nummer allein.

---

## 1. I3-Kernresultat

I3 repariert die in NEU-212 gescheiterte Schwartz-Regularisierung nicht durch einen nachträglichen Glättungsoperator, sondern durch einen direkt passenden logarithmischen Koeffiziententyp. Die Kette endet belastbar bei

\[
\boxed{
[D_g^{\rm corr}]\neq0
\in HH^1(A_{\rm alg},\mathfrak M_{\rm glob}^{\log})_g
}
\]

und, nach dem NEU-218-Abschluss,

\[
\boxed{
[D_g^{\rm corr}]\smile[\Theta^\wedge_{p_1,p_2,p_3}]
\neq0
\in HH^4(A_{\rm alg},\mathfrak M_{\rm glob}^{\log})_g.
}
\]

Dies ist ein **geladener nichttrivialer Hochschild-4-Cup mit Koeffizienten im globalen logarithmischen Bimodul**.

Es ist **nicht** die Aussage

\[
HH^4(A_{\rm alg},A_{\rm alg})_g\neq0
\]

und auch nicht automatisch eine zyklische, KMS-, Weil-, Hilbert- oder Operatorrealisierung.

---

## 2. NEU-212 — geschriebene Zieltypbrücke scheitert

### 2.1 Verbindlicher Status

Die geschriebene NEU-212-Fassung ist im zentralen Ziel `×[M]`.

Widerlegt sind:

1. `A_alg ⊂ A^infty` für die dort definierte absolute Schnellabfallbedingung: bereits `1` und `e(r)` liegen nicht darin;
2. die logarithmische Regularisierung `G/log(ν+2)` als Schwartz-Element: sie fällt nur wie `O(1/(j log j))`;
3. `\widetilde D_g(e(r))=0`: dies übernimmt den bereits in I2 widerlegten Charakterfehler und verletzt eine BC-Kreuzrelation;
4. daher die behauptete Klasse in `HH^1(A_alg,A^infty)_g`;
5. der angekündigte Cup-Aufstieg.

Belastbar bleiben nur:

- der neutrale nichtunitale Schnellabfallraum `S_0` (`✓[K/M]`),
- `C_{m,n;r}` besitzt endlichen Schalenträger und liegt insbesondere in `B_alg ∩ S_0` (`✓[M]`),
- der vorgeschlagene Offdiagonal-Divergenztest ist `✓[M]_neg`, weil exakt
  \[
  c_j/\log(j+2)=1.
  \]

### 2.2 Rolle in P09

NEU-212 wird **nicht** als positiver Zieltyp importiert. Es bleibt als dokumentierter Fehlschlag der zu starken Schwartz-Regularisierung und als Motivationsanker für den logarithmischen Ersatz.

---

## 3. NEU-213 — Revisionsknoten, aber durch den späteren Direktaudit überholt

NEU-213 identifiziert zwei zentrale Fehler korrekt:

- der Nichtinnerheits-Divergenztest kollabiert zu `1`,
- die punktweise Division durch `log(ν+2)` ist kein `A_alg`-Bimoduloperator und erhält daher die Leibnizregel nicht automatisch.

Seine Rückstufung von NEU-212 bleibt jedoch zu schwach. Der spätere `ARCHIV-AUDIT-NEU212` setzt die zentralen Aussagen `[O-212-2]` und `[O-212-3]` nicht nur auf `?[O]`, sondern auf `×[M]`.

**P09-Provenienz:**

```text
NEU-213: AUDIT-REUSED_part / SUPERSEDED_part
```

Die Fehlerdiagnose wird übernommen; seine zu milden Statuswerte nicht.

---

## 4. NEU-214/215 — globaler Bimodul-Glättungs-No-go

### 4.1 Rigiditätslemma

Für einen unitalen `A_alg`-Bimoduloperator

\[
R:A_{C^*}\to M
\]

gilt mit `r=R(1)` auf `A_alg` zwingend

\[
R(a)=ar=ra,
\]

also `r` liegt im Zentralisator.

### 4.2 Zentralisator

NEU-215 rev.4 schließt den Zentralisatorbeweis:

\[
\boxed{
\operatorname{Cent}_{A_{C^*}}(A_{\rm alg})
=Z(A_{C^*})
=\mathbb C1.
}
\]

Die tragende Kette ist:

1. `C(Zhat)` ist MASA im BC-`C^*`-System;
2. Kommutation mit `μ_k` erzwingt `σ_k(f)=f`, also `f(kx)=f(x)`;
3. `j!x→0` in `Zhat` und Stetigkeit erzwingen `f≡f(0)`.

### 4.3 No-go

Daraus folgt:

\[
\boxed{
R:A_{C^*}\to\mathcal A^\infty\subsetneq A_{C^*}
\text{ normstetig und global }A_{\rm alg}\text{-bimodular}
\Rightarrow R=0.
}
\]

Dies schließt `[O-213-4]` negativ.

### 4.4 Routing

Dieser No-go bleibt **P09-CORE-NOGO**. Er ist für die Architektur wichtig, weil er erklärt, warum NEU-216 nicht als nachträgliche Regularisierung `R∘D_g` konstruiert werden darf.

NEU-216 widerspricht dem No-go nicht: `B^log/A^log` wird direkt als Zieltyp definiert, und die bereits vorhandenen Werte von `D_g^corr` werden auf Zugehörigkeit geprüft.

---

## 5. NEU-216 — logarithmischer Koeffiziententyp repariert die Zieltypbrücke

### 5.1 Definitions-Firewall

Die öffentliche rev.6 verwendet `S_j`, `ν`, `[·]_tan`, `[·]_rad` und `B^log`, ohne diese Zentraldefinitionen im sichtbaren Dateikörper vollständig einzuführen. Für die SYN gilt deshalb die im Direktaudit/Auditstand kanonisierte Definition:

\[
L_j=(j+1)!,\qquad
S_j=L_j\widehat{\mathbb Z}\setminus L_{j+1}\widehat{\mathbb Z},
\]

\[
\nu(x)=\max\{j:(j+1)!\mid x\}\quad(x\neq0),
\]

\[
m_j(f)=\int_{S_j}f\,d\mu_j,
\]

\[
[f]_{\tan}=\sup_j (j+1)\operatorname{osc}_{S_j}(f),
\]

\[
[f]_{\rad}=\sup_j (j+1)|m_{j+1}(f)-m_j(f)|,
\]

\[
\|f\|_{\mathcal B^{\log}}
=\|f\|_\infty+[f]_{\tan}+[f]_{\rad}.
\]

### 5.2 Belastbare Resultate

\[
\boxed{
\mathcal B_{\rm alg}\subsetneq\mathcal B^{\log}
\subsetneq C(\widehat{\mathbb Z})
}
\]

ist ein unitaler Banach-`*`-Koeffiziententyp.

Die BC-Transporte `σ_k`, `ρ_k` und die kanonische Wahl `T_a=σ_a` erhalten `B^log`; alle faktorialen Transportdefekte erfüllen

\[
G_{a,d}\in\mathcal B^{\log}.
\]

Definiert wird die algebraische graduierte `*`-Algebra

\[
\mathcal A^{\log}
=\bigoplus_h^{\rm alg}\mathcal A_h^{\log},
\qquad
\mathcal A_{m/n}^{\log}=\mu_m\mathcal B^{\log}\mu_n^*.
\]

Dann

\[
A_{\rm alg}\subsetneq\mathcal A^{\log}\subseteq A_{C^*},
\]

\[
D_g^{\rm corr}(A_{\rm alg})\subseteq\mathcal A^{\log},
\]

und

\[
\boxed{
[D_g^{\rm corr}]\neq0
\in HH^1(A_{\rm alg},\mathcal A^{\log})_g.
}
\]

Damit ist `[O-211-6a]` algebraisch positiv geschlossen.

### 5.3 Lokaler Formeldefekt

Die historische gcd-Relation mit einem Faktor `1/r` ist `×[M]`. Korrekt, für
`r=(n,p)`, `n=rn_1`, `p=rp_1`, ist

\[
\mu_n^*\mu_p=\mu_{p_1}\mu_{n_1}^*,
\]

ohne Skalarfaktor.

Dieser lokale Defekt zerstört die `B^log/A^log`-Konstruktion nicht.

### 5.4 Nicht bewiesen in NEU-216

- keine Banach-/Fréchet-Vervollständigung der vollen Gradsumme,
- kein kontinuierlicher Hochschildkomplex,
- noch kein Grad-3-Partner,
- noch kein Cup-Nichtverschwindensbeweis.

---

## 6. NEU-217 — lokal fehlerhaft, global tragfähig

I3 behandelt die drei NEU-217-Dateien als einen reconciliierten Block.

### 6.1 Lokale Punkte

Belastbar:

- lokale Bewertungs-/Gaugegeometrie im Kern,
- gcd-Fallzerlegung für `D_g^corr(μ_{p^r})` und Adjungierte,
- lokale Nichtinnerheit mit Ziel `A_{C^*}` über Normdivergenz.

Zu korrigieren/offen:

- der infinitesimale Gaugegenerator verliert historisch einen Faktor `i`; die reelle Ableitung `δ_p^(0)` ist `(1/i)∂_p` und erfüllt die Anti-`*`-Regel;
- eine einzelne Orbitdarstellung ist nicht treu; trennende Familie/Eindeutigkeit bleibt offen;
- der lokale Raum `M_{g,p}^{log}` ist nicht als vollständiger `A_(p),alg`-Bimodul typisiert;
- die nichtverschwindenden Charakterwerte `D_g^corr(e(r))` fehlen im lokalen Landungsnachweis;
- deshalb ist die lokale `HH^1`-Aussage mit genau diesem lokalen Koeffizientenmodul **nicht verwendbar**.

### 6.2 Globaler Bimodul

Der intrinsische neutrale Raum `M_glob^log` wird als Schnitt aller geeigneten `B_alg`-Bimodule in `B^log` definiert, die unter allen `σ_n,ρ_n` stabil sind und sämtliche `G_{k,d}` enthalten.

Der geladene globale Bimodul ist

\[
\mathfrak M_{\rm glob}^{\log}
=\overline{\operatorname{span}_{\rm fin}
\{a\xi b:a,b\in A_{\rm alg},\xi\in M_{\rm glob}^{\log}\}}
\subseteq\mathcal A^{\log}.
\]

Belastbar:

\[
D_g^{\rm corr}(A_{\rm alg})
\subseteq(\mathfrak M_{\rm glob}^{\log})_g,
\]

\[
\boxed{
[D_g^{\rm corr}]\neq0
\in HH^1(A_{\rm alg},\mathfrak M_{\rm glob}^{\log})_g.
}
\]

### 6.3 Formelkorrektur

In der historischen globalen Transportformel `(G1)` muss der erste Index `nk` lauten, nicht `nk/δ`. Die globale Schnittstabilität und der Landungs-/Nichtinnerheitsbeweis bleiben davon unberührt.

---

## 7. NEU-218, erste Datei — Kozykelbau positiv, Nichtverschwindensroute zunächst offen

Die erste NEU-218-Datei konstruiert korrekt die neutralen Bewertungsableitungen

\[
\delta_p^{(0)}(a_h)=v_p(h)\log p\,a_h
\]

und deren dreifach alternierten Cup

\[
\Theta^\wedge_{p_1,p_2,p_3}
=\sum_{\sigma\in S_3}\operatorname{sgn}(\sigma)
\delta_{p_{\sigma(1)}}^{(0)}\smile
\delta_{p_{\sigma(2)}}^{(0)}\smile
\delta_{p_{\sigma(3)}}^{(0)}.
\]

Belastbar:

\[
b\Theta^\wedge=0,
\qquad
[\Theta^\wedge]\neq0,
\]

mit Paarungswert

\[
6\prod_{i=1}^3\log p_i\neq0.
\]

Mit der Modulmultiplikation entsteht

\[
L^{\rm cup}_{g;\mathbf p}
:=D_g^{\rm corr}\smile\Theta^\wedge
\in Z^4(A_{\rm alg},\mathfrak M_{\rm glob}^{\log})_g.
\]

Die alte augmentationsbasierte Nichtverschwindensroute scheitert; ebenso der zwischenzeitlich vorgeschlagene Baker-/`log q`-Koeffiziententrennungsschritt. Diese Zwischenwege sind `SUPERSEDED/NO-GO`.

---

## 8. NEU-218 Abschluss — Følnerbeweis des nichttrivialen geladenen Cup-Produkts

Die zweite NEU-218-Datei ist der autoritative I3-Endanker.

### 8.1 Normalform

Wähle paarweise verschiedene Primzahlen `q,p_1,p_2,p_3`, alle teilerfremd zu `mn`, und setze

\[
P=p_1p_2p_3,
\qquad
R=\{q,p_1,p_2,p_3\}.
\]

Im teilerfremden Sektor:

\[
D_g^{\rm corr}(\mu_q)=\mu_{mq}G_q\mu_n^*,
\qquad G_q=G_{q,1}\in B^{\log},
\]

also

\[
\boxed{
D_g^{\rm corr}(\mu_q)\mu_P
=\mu_{mqP}\sigma_P(G_q)\mu_n^*.
}
\]

### 8.2 Dynamischer Koinvariantenknoten

Zu zeigen ist

\[
\sigma_P(G_q)
otin
\sum_{r\in R}(1-\sigma_r)B^{\log}.
\]

Da `σ_P(G_q)-G_q` bereits in der Summe der drei `p_i`-Koränder liegt, genügt die Aussage für `G_q`.

### 8.3 Targeted re-audit des Følnerarguments

Definiere

\[
S_{r,N}=\sum_{k=0}^{N-1}\sigma_r^k,
\qquad
\mathcal F_N=\prod_{r\in R}S_{r,N}.
\]

Für einen einzelnen Korand gilt wegen
`S_{r,N}(1-σ_r)=1-σ_r^N` und `||σ_r||_{∞→∞}≤1`:

\[
\|\mathcal F_N((1-\sigma_r)F)\|_\infty
\le2N^3\|F\|_\infty.
\]

Eine Darstellung von `G_q` als Summe der vier Koränder würde daher
`N^{-3}||F_N(G_q)||_∞=O(1)` erzwingen.

Sei `J_N` minimal mit `v_q(L_{J_N})≥N` und

\[
x_N=L_{J_N}/q^N.
\]

Mit

\[
d_N=v_q(L_{J_N})-N,
\qquad K_N=q(d_N+1)
\]

folgt aus der Minimalität

\[
K_N=O(\log J_N),
\qquad K_N/J_N\to0.
\]

Für
`s=p_1^{k_1}p_2^{k_2}p_3^{k_3}`, `0≤k_i<N`, gilt gleichmäßig

\[
\nu(sx_N)\le K_N,
\qquad
\nu(q^Nsx_N)\ge J_N.
\]

Mit der punktweisen Hilfsfunktion `Xscr(x)=c_{ν(x)}` auf `x≠0` teleskopiert die `q`-Richtung:

\[
\sum_{k=0}^{N-1}G_q(q^ksx_N)
=\mathscr X(q^Nsx_N)-\mathscr X(sx_N)
\ge c_{J_N}-c_{K_N}.
\]

Nach Summation über die `N^3` drei übrigen Primrichtungen:

\[
\mathcal F_N(G_q)(x_N)
\ge N^3(c_{J_N}-c_{K_N}),
\]

wobei

\[
c_{J_N}-c_{K_N}
=\log\frac{J_N+2}{K_N+2}\to+\infty.
\]

Also

\[
N^{-3}\|\mathcal F_N(G_q)\|_\infty\to\infty,
\]

Widerspruch.

**Targeted-Reaudit-Urteil:** Der Følner-Schritt ist in der angegebenen Modellarchitektur konsistent; kein konkreter Gegenbefund gefunden.

Damit:

\[
\boxed{
G_q\notin\sum_{r\in R}(1-\sigma_r)B^{\log}.
}
\]

### 8.4 Partieller Modulkommutatorquotient

Für `H=gqP` setze

\[
C_{H;R}=\sum_{r\in R}[\mu_r,M_{H/r}]\subseteq M_H,
\qquad M=\mathfrak M_{\rm glob}^{\log}.
\]

Die homogenen Komponenten von `M⊂A^log` besitzen im gewählten teilerfremden Sektor die eindeutige Normalform mit festem reduzierten linken/rechten Isometrieindex und einem `B^log`-Koeffizienten. Daher überträgt sich der Koinvariantenbefund auf

\[
\boxed{
D_g^{\rm corr}(\mu_q)\mu_P\notin C_{H;R}.
}
\]

Der stärkere Vollquotient

\[
D_g^{\rm corr}(\mu_q)\mu_P\stackrel?\notin[A,M]
\]

bleibt offen und wird **nicht** benötigt.

### 8.5 Dualzyklus und Paarung

Ein algebraisches Funktional auf `M_H/C_{H;R}`, das die nichtverschwindende Klasse trennt, liefert `φ∈M^∨` mit

\[
\varphi(D_g^{\rm corr}(\mu_q)\mu_P)\neq0
\]

und den vier benötigten partiellen Zentralitätsrelationen

\[
\varphi(\mu_r m)=\varphi(m\mu_r),
\qquad r\in R.
\]

Daraus wird der explizite duale Vierzyklus

\[
z_\varphi
=\sum_{\pi\in S_4}\operatorname{sgn}(\pi)
\varphi\otimes\mu_{r_{\pi(1)}}\otimes\cdots\otimes\mu_{r_{\pi(4)}}
\]

mit

\[
\partial z_\varphi=0.
\]

Die Paarung ist

\[
\boxed{
\langle L^{\rm cup}_{g;\mathbf p},z_\varphi\rangle
=6\Bigl(\prod_{i=1}^3\log p_i\Bigr)
\varphi(D_g^{\rm corr}(\mu_q)\mu_P)
eq0.
}
\]

Folglich

\[
\boxed{
[L^{\rm cup}_{g;\mathbf p}]
eq0
\in HH^4(A_{\rm alg},\mathfrak M_{\rm glob}^{\log})_g.
}
\]

**Endstatus:** `✓[K/M]` — Konstruktion + mathematischer Nachweis innerhalb des explizit gebauten Koeffizientenmodells.

---

## 9. Spätere Reichweitenkontrolle

### 9.1 NEU-219-Finalaudit

Der spätere kanonische Rotations-/Zyklizitäts-No-go hebt den Hochschildbefund nicht auf. Er zeigt vielmehr, dass für den kanonischen Basislift

\[
t\Phi_0\neq C\Phi_0\quad\forall C\in\mathbb C,
\]

und rollt den früheren skalaren Exponenten `s=-1` zurück.

Der offene Knoten eines zyklischen oder getwistet-zyklischen Ersatzrepräsentanten wird ausdrücklich exportiert. Daher:

```text
geladenes HH4 mit Koeffizientenmodul: positiv;
kanonische gewöhnliche zyklische/Rotationsverfeinerung: negativ;
anderer zyklischer/getwisteter Repräsentant: offen.
```

### 9.2 Bestandsaufnahme 5. August

Die spätere Bestandsaufnahme führt

\[
[D_g^{\rm corr}]\smile[\Theta^\wedge]\neq0
\]

explizit als neues verbindliches Resultat und formuliert zugleich, dass die singuläre Route bis `HH^4` trägt und erst an der Zyklizität blockiert.

Damit existiert **kein späterer Rollback des I3-HH4-Endbefunds**.

### 9.3 NEU-222

NEU-222 unterstützt die Trassenaussage „singuläre Route trägt bis HH4“, ist aber bei mehreren Detailstatus älter/stärker als die späteren August-Audits. Es wird deshalb nur als `AUDIT-REUSED_part` verwendet.

---

## 10. Reconciliation-Matrix I3

| Quelle/Knoten | P09-Status | Verbindlicher Befund |
|---|---|---|
| NEU-212 geschriebene `A^infty`-Brücke | `SUPERSEDED / ×[M]` | zu starke Schwartz-Regularisierung scheitert |
| NEU-212 `S_0`, Charakterkoeffizient | `INCORPORATED_part` | neutraler Schnellabfallraum; `C_{m,n;r}` endlicher Schalenträger |
| NEU-213 | `AUDIT-REUSED_part / SUPERSEDED_part` | richtige Fehlerdiagnose, zu milde Statuskorrektur |
| NEU-214-1 | `INCORPORATED` | Bimodul-Rigidität `R(a)=aR(1)=R(1)a` |
| NEU-215 Zentralisator | `INCORPORATED` | `Cent(A_alg)=C1` im `A_C*`-Ziel |
| globaler Bimodul-Glätter | `P09-CORE-NOGO` | normstetiger echter globaler Bimodul-Glätter ist null |
| NEU-216 `B^log` | `INCORPORATED` | unitaler logarithmischer Banach-`*`-Koeffiziententyp |
| NEU-216 gcd `1/r` | `×[M]` | kein Skalarfaktor |
| `A^log`, Zieltyp | `INCORPORATED` | `D_g^corr(A_alg)⊂A^log`, nichttriviales HH1 |
| NEU-217 lokale `M_{g,p}^log`-HH1 | `NO-GO / UNTYPED` | lokales Koeffizientenbimodul nicht vollständig typisiert |
| NEU-217 globale `M_glob^log`-Route | `INCORPORATED` | globaler Bimodul und nichttriviales geladenes HH1 |
| NEU-217 Formel G1 alter Index | `×[M]` | erster Index `nk`, nicht `nk/δ` |
| NEU-218 erste Datei | `INCORPORATED_part / SUPERSEDED_part` | `Theta^wedge`, Cup-Kozykel; alte Nichtverschwindenswege nicht final |
| Baker-/`log q`-Trennung | `NO-GO` | über komplexem Koeffizientenraum unzulässig |
| NEU-218 Abschluss Følner | `INCORPORATED` | dynamischer Koinvarianten-No-go |
| partieller Modulquotient | `INCORPORATED` | genügt für Dualzyklus/Paarung |
| Vollquotient `[A,M]` | `OPEN` | nicht benötigt, nicht geschlossen |
| geladener Cup | `INCORPORATED_model` | nichttrivial in `HH^4(A_alg,M_glob^log)_g` |
| zyklische/KMS-Verfeinerung | `OPEN/NO-GO canonical` | kanonischer Rotationspfad später negativ; Ersatzrepräsentant offen |

---

## 11. SYN-Firewalls nach I3

### Firewall A — Koeffiziententyp

Zulässig:

\[
[D_g^{\rm corr}]\smile[\Theta^\wedge]
eq0
\in HH^4(A_{\rm alg},\mathfrak M_{\rm glob}^{\log})_g.
\]

Nicht zulässig ohne neuen Beweis:

\[
HH^4(A_{\rm alg},A_{\rm alg})_g\neq0.
\]

### Firewall B — Hochschild versus zyklisch

Nichttrivialität in geladenem Hochschild-Grad 4 impliziert **keine** gewöhnliche zyklische Klasse, KMS-Paarung oder Weil-Klasse.

### Firewall C — algebraisch versus topologisch

`A^log` und `M_glob^log` liefern den algebraischen Koeffizientenapparat; eine globale Banach-/Fréchet-Vervollständigung der vollen Gradsumme und ein kontinuierlicher Hochschildkomplex sind nicht Teil des bewiesenen Resultats.

### Firewall D — partieller versus voller Kommutatorquotient

NEU-218 benötigt nur

\[
D_g(\mu_q)\mu_P\notin C_{H;R}.
\]

Der Vollquotient gegen `[A,M]` bleibt offen.

### Firewall E — keine Operatorbrücke

Aus dem positiven Cup folgt kein Hilbert-Pólya-Operator und keine positive Weil-Form-Realisierung.

---

## 12. P09/P10-Routing

**P09-CORE-NOGO:**

- Schwartz-Regularisierung aus NEU-212 scheitert;
- globaler normstetiger Bimodul-Glätter ist durch NEU-215 ausgeschlossen;
- lokale NEU-217-Koeffizientenklasse ist untypisiert;
- Baker-/komplexe `log q`-Trennung ist kein zulässiger Quotientendetektor.

Diese Befunde bleiben in P09, weil sie die positive `B^log → M_glob^log → HH4`-Architektur erzwingen/typisieren.

Kandidatenspezifische Nebenwege dürfen später in P10 gespiegelt werden.

---

## 13. Endurteil I3

\[
\boxed{
\text{P09 / I3 PASS A COMPLETE — Gegencheck ausstehend}
}
\]

Der I3-Endstand ist **stärker** als I2:

\[
\boxed{
[D_g^{\rm corr}]\smile[\Theta^\wedge]
eq0
\in HH^4(A_{\rm alg},\mathfrak M_{\rm glob}^{\log})_g.
}
\]

Er bleibt jedoch strikt ein geladener Hochschildbefund **mit Koeffizientenmodul**.

---

## 14. Fünf atomare Gegencheckfragen

### Frage 1 — NEU-212 → NEU-216

Ist die Leserichtung korrekt, dass NEU-212s `A^infty`-/Schwartz-Regularisierung zentral `×[M]` ist, während NEU-216 sie **nicht repariert durch einen Bimoduloperator**, sondern durch direkte Definition des logarithmischen Zieltyps `B^log/A^log`; und dass damit `[D_g^corr] != 0 in HH^1(A_alg,A^log)_g` belastbar ist?

### Frage 2 — NEU-214/215-No-go

Ist der globale No-go korrekt begrenzt auf normstetige globale `A_alg`-Bimoduloperatoren `R:A_C*→A^infty⊊A_C*`, so dass er NEU-216 nicht widerspricht und als `P09-CORE-NOGO` erhalten bleiben muss?

### Frage 3 — NEU-217 lokal/global

Ist die Trennung korrekt: lokale `HH^1`-Aussage mit `M_{g,p}^log` nicht typisiert, aber der globale Bimodul `M_glob^log`/`mathfrak M_glob^log` trägt `D_g^corr` und die Klasse bleibt dort nichttrivial; Formel `(G1)` nur mit erstem Index `nk`?

### Frage 4 — NEU-218 Følner/Cup

Ist der Abschlussbeweis korrekt, dass der Mehrparameter-Følner-Test

\[
G_q\notin\sum_{r\in R}(1-\sigma_r)B^{\log}
\]

liefert, daraus der partielle Quotient `M_H/C_{H;R}` einen nichtaugmentativen Dualzeugen erzeugt und damit

\[
[D_g^{\rm corr}]\smile[\Theta^\wedge]\neq0
\in HH^4(A_{\rm alg},\mathfrak M_{\rm glob}^{\log})_g
\]

folgt, **ohne** den vollen Quotienten `M/[A,M]` entscheiden zu müssen?

### Frage 5 — Reichweite und späterer NEU-219-No-go

Ist die Firewall korrekt, dass dieser I3-Befund weder `HH^4(A_alg,A_alg)_g != 0` noch eine zyklische/KMS-/Weil- oder Operatorrealisierung beweist; und dass NEU-219s späterer kanonischer Rotations-No-go den Hochschild-Cup nicht zurückrollt, sondern erst die kanonische zyklische Verfeinerung blockiert?

---

## 15. Seal-Regel

Bei Gegencheck ohne konkreten mathematischen Befund:

```text
I3 → PASS A COMPLETE / SEALED
I4 → ACTIVE
```

Bei Gegenbefund wird ausschließlich der betroffene atomare Punkt wieder geöffnet.
