# CURRENT FRONT — Objekt X / POS-DIL

> **Operative Kopfschicht — zuerst lesen.**
> **Redaktioneller Stand:** 13. September 2026; keine Registry-Promotion.
> **Konsolidierungsquellen:** [AR(1)/Weil-Tail/OX-GRAM](audits/P11_OBJECT_X_AR1_OX_GRAM_CONSOLIDATION_2026-09-12.md), [Gate-2/OX-GEN](audits/P11_OX_GRAM_GATE2_AND_OX_GEN_2026-09-12.md), [OX-GEN-A gemeinsamer Exponentialgenerator](audits/P11_OX_GEN_A_COMMON_EXPONENTIAL_GENERATOR_2026-09-13.md), [POS-DIL-1 Prime-moment Hilbertization](audits/P11_POS_DIL_1_PRIME_MOMENT_HILBERTIZATION_2026-09-13.md).
> **Strategie:** [kanonische Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md).
> **Suchgegenstand:** [Objekt-X-Arbeitsdefinition](00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md).
> **Buchungen:** [Theorem-/Review-Registry](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md).

Diese Datei ordnet die Arbeit; sie beweist nichts. Der aktuelle `main`-Head und PR-Zustände werden live aus GitHub gelesen. Bei Konflikten ist die kanonische mathematische Quelle im benannten Scope maßgeblich.

## 1. Erreichter Meilenstein

Der integrierte positive Wurzelanker plus R42.51 liefert Strong Terminal/C6 für jedes **feste** `0<R<S` im **ungeraden P11-Graphraum**.

**Scope:** keine Radienuniformität, keine Operatornormkonvergenz, kein gerader Gesamtsektor, keine vollständige Objekt-X-Realisierung und keine RH-Folgerung.

## 2. Belastbare Prime-Power-Struktur

Seit PR #98 ist dokumentiert:

```math
C_{jk}^{(p)}=(\log p)p^{\min(j,k)}p^{-3(j+k)/4},
\qquad
C_{kk}^{(p)}=(\log p)p^{-k/2}.
```

`3/4` ist durch Weil-Diagonale plus Martingalmultiplizität erzwungen. Nach Weil-Diagonalnormalisierung:

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}\,p^{-|j-k|/2},
\qquad q_p=p^{-1/2}.
```

Tail/Root:

```math
T_q^*T_q=R_q-uu^*,
\qquad
T_q^*T_q+uu^*=R_q.
```

P11-Restseite:

```math
R_R^*R_R=\sum_{p,k}w_{p,k}Z_{p,k,R}^*Z_{p,k,R}.
```

Cross-prime Root-Gram ist fensterloser Bulk, kein Boundaryterm.

**Spur B:** theorem-ready, RH-unabhängig, ausdrücklich noch nicht Objekt X.

## 3. Endliche Suzuki-/OX-GRAM-Normalform

Für `a<=1`:

```math
Q_{B_a}(v)=G_a^+(v)-N_a(v),
\qquad
N_a=c_aI+C_a.
```

`G_a^+` besteht aus positiven Prime-Kanal-, Log-Multiplikator- und logarithmischen `log|D|`-Formen. Die reine Existenzfrage `N_a<=G_a^+?` ist als Objekt-X-Gate geschlossen: bei bereits bekannter lokaler Weil-Positivität kann ein Kontraktor rückwärts aus `Q` gebaut werden. Das ist zirkulär.

**Übrig bleibt Kanonizität.**

## 4. CERT-HARDEN — geschlossen im dokumentierten endlichen Scope

PR #98 enthält gehärtete read-only Zertifikatswege.

- Gate 1: Realraum/Fourier-Normalisierung bei `a in {0.5,0.8,1.0}`, mit Bernoulli-Tailball, Arb-Cutoff, Arb-Endpunktfehler, `sinc`-Rest und fail-closed Null-Einschluss.
- Gate 2: Arb 512 Bit, Dirichletbasis bis `N=14`, drei Radien, beide Paritäten, **42/42** strikt positive Arb-Cholesky-Blöcke.

**Firewall:** endlichdimensionales Zertifikat, kein globaler Weil-Positivitäts- oder RH-Beweis.

## 5. OX-GEN-A — gemeinsamer Exponentialgenerator geschlossen `✓[M]`

Für kompakt getragene Testfunktionen setze

```math
E_\pm(v)=\int e^{\pm x/2}v(x)\,dx,
\qquad
\mathcal Ev=(E_+(v),E_-(v)).
```

Für Translationen `(T_t v)(x)=v(x+t)` gilt exakt

```math
\boxed{\mathcal ET_t=\rho(t)\mathcal E,\qquad
\rho(t)=\operatorname{diag}(e^{-t/2},e^{t/2}).}
```

Mit

```math
K_n=T_{\frac12\log n}-T_{-\frac12\log n},
\qquad
\lambda_n=n^{1/4}-n^{-1/4}
```

folgt

```math
\boxed{\mathcal EK_n
=\lambda_n\operatorname{diag}(-1,1)\mathcal E.}
```

Suzukis elementarer Anteil erfüllt zugleich

```math
\boxed{r_0''(t)=-\operatorname{tr}\rho(t)=-2\cosh(t/2),}
```

sogar

```math
\boxed{r_0(t)=-4\bigl(\operatorname{tr}\rho(t)-2\bigr),
\qquad r_0(\log n)=-4\lambda_n^2.}
```

Mit

```math
P=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad J=-P
```

gilt

```math
\boxed{R_0(v,w)=\langle\mathcal Ev,J\mathcal Ew\rangle_{\mathbb C^2}.}
```

Unter jedem Kanal:

```math
\boxed{R_0(K_nv,K_nw)=-\lambda_n^2R_0(v,w).}
```

## 6. Prime-only-A2 aus `{w_n,lambda_n}` geschlossen `×[M]`

Der zunächst vorgeschlagene Test „Prime-Gram direkt auf dem Rang-2-Quotienten“ ist nicht wohldefiniert:

- `ker \mathcal E` ist zwar unter jedem `K_n` invariant;
- die positive Form `\sum w_n||K_n v||^2` verschwindet dort aber nicht;
- sie descendiert daher ohne zusätzliche Quotientennorm/Schur-Komplement/Komplementwahl nicht auf `v -> (E_+,E_-)`.

Auch die reine Quotienten-Kovarianz fixiert den Maßstab nicht. Für eine Hermiteform `H` mit

```math
D_n^*HD_n=-\lambda_n^2H
```

folgt nur eine off-diagonale Formklasse; der absolute Maßstab bleibt frei.

## 7. POS-DIL-1 — natürliche Rang-2-Companion-Klasse geschlossen

Setze

```math
S=\operatorname{diag}(-1,1)=D_n/\lambda_n=2\rho'(0).
```

Dann

```math
S^2=P^2=I,
\qquad PSP=-S,
\qquad \rho(t)=e^{tS/2}.
```

### 7.1 Symmetrierigidität `✓[M]`

Für eine positive Hermiteform `M` auf `C^2` verlangen wir als erste minimale natürliche Companion-Klasse nur

```math
PMP=M,
\qquad SMS=M.
```

Dann ist zwingend

```math
\boxed{M=tI.}
```

Die Schur-Bedingung

```math
\begin{pmatrix}M&J\\J&M\end{pmatrix}\succeq0
```

ist damit genau für `t>=1` erfüllt. Der eindeutige minimale Begleiter in dieser Klasse ist

```math
\boxed{M_{\min}=I.}
```

### 7.2 Vollständige positive `rho`-Invarianz ist unmöglich `×[M]`

Fordert man stattdessen

```math
\rho(t)^*M\rho(t)=M
```

für alle `t` und `M>=0`, folgt bereits aus der Ableitung bei `t=0`

```math
SM+MS=0,
```

und Positivität erzwingt

```math
\boxed{M=0.}
```

Damit gibt es insbesondere keine injektive exakte unitäre Hilbert-Intertwinerrealisierung von `rho` auf positivem Rang 2.

## 8. POS-DIL-1 — Prime-moment Hilbertization `✓[M]`

Sei `N` eine endliche nichtleere Prime-Power-Menge und

```math
w_n=\frac{\Lambda(n)}{\sqrt n},
\qquad
\kappa_N=\sum_{n\in N}w_n\lambda_n^2>0.
```

Auf

```math
\mathcal H_N=\bigoplus_{n\in N}\mathbb C^2
```

definiere

```math
\iota_Nz
=\kappa_N^{-1/2}
\bigl(\sqrt{w_n}D_nz\bigr)_{n\in N}.
```

Dann

```math
\boxed{\iota_N^*\iota_N=I.}
```

Mit `\mathbb P_N=\oplus_{n\in N}P` gilt sogar

```math
\boxed{\mathbb P_N\iota_N=\iota_NJ,
\qquad
\iota_N^*\mathbb P_N\iota_N=J.}
```

Für Testfunktionen ist

```math
V_Nv=\iota_N\mathcal Ev
=\kappa_N^{-1/2}
\bigl(\sqrt{w_n}\,\mathcal EK_nv\bigr)_{n\in N}.
```

Also exakt

```math
\boxed{\|V_Nv\|^2=|E_+(v)|^2+|E_-(v)|^2,}
```

und mit derselben positiven Featureabbildung

```math
\boxed{R_0(v,w)=\langle V_Nv,\mathbb P_NV_Nw\rangle.}
```

Damit taucht die minimale positive Rang-2-Masse in der vorab definierten **Prime-moment-Klasse** kanonisch als Gramnorm echter gewichteter Prime-Kanalausgänge auf.

### 8.1 AR(1)-Root-Brücke

Für `n=p^k`, `q_p=p^{-1/2}` gilt

```math
\boxed{
\sqrt{w_{p,k}}\,D_{p^k}
=\sqrt{\log p}\,(1-q_p^k)S.
}
```

Die Kanalindex-Amplitude ist damit exakt `flat minus AR(1)-root`, weil der Root-Vektor des Primasts `u_k=q_p^k` ist.

**Firewall:** Das identifiziert nicht den P11-Huboperator mit `E_±`; bewiesen ist die Amplitudenrelation in der Momentkompression.

## 9. Status von OX-GEN-A2'

Die Prime-moment-Konstruktion ist der erste positive gemeinsame **Quotientenbaustein**:

```text
OX-GEN-A common generator plane                 ✓[M]
POS-DIL-1 symmetry-rigid minimal companion      ✓[M]
POS-DIL-1 full-rho same-space Hilbertization    ×[M] [enger Scope]
POS-DIL-1 prime-moment positive embedding       ✓[M]
OX-GEN-A2' overall                              ✓[M]_part
```

Warum nur `✓[M]_part` für A2' insgesamt:

- der volle positive Prime-Gramoperator descendiert weiterhin nicht durch `E`;
- der Zielbereich von `iota_N` bleibt zweidimensional;
- noch nicht bewiesen ist, dass die Momentabbildung **kontraktiv** in der vorhandenen `G_a^+`-Featuregeometrie sitzt;
- `log|D|`, `r_1` und `c_aI` sind noch nicht integriert.

## 10. Neue operative Hauptfrage: POS-DIL-2 / FEATURE-SHORTING

Für die vollständige positive Featureform `G_a^+` ist jetzt der schärfere, weiterhin nichtzirkuläre Gate:

> **Ist die kanonische Prime-moment-Abbildung als kontraktive Postkompression bzw. als natürliches Shorting/Schur-Komplement der vorhandenen positiven Prime-/`log|D|`-Featuregeometrie realisierbar?**

Eine erste scharfe Form lautet

```math
\boxed{\|\mathcal Ev\|^2\stackrel?\le G_a^+(v).}
```

bzw. typkorrekt nach Fixierung der Featureabbildung `\mathcal F_a^+` die Existenz eines **vorwärts definierten kontraktiven** Operators `C_a` mit

```math
C_a\mathcal F_a^+v=V_{N_a}v.
```

Beide Ausgänge sind logisch offen.

- **PASS:** die minimale positive Rang-2-Masse sitzt tatsächlich kontraktiv in der bestehenden positiven Featuregeometrie.
- **FAIL:** POS-DIL-1 bleibt gültig, aber nicht als kontraktiver Schur-/Defektbaustein von `G_a^+`; dann ist die Klasse mit Root/Hub-/`log|D|`-Struktur weiter zu verengen.

## 11. Nächste Gates

1. **POS-DIL-2 / FEATURE-SHORTING** — analytisch zuerst; Numerik nur als Gegenvektorsuche/Orientierung.
2. **OX-GEN-B** — erst nach Klärung des positiven Feature-Gates `r_1` und/oder `c_aI` einbeziehen.
3. **Spur B parallel:** AR(1)/Martingal-Faktorisierung theorem-ready verschriftlichen.

## 12. Gesperrte Deutungen

Nicht wieder aktivieren:

- Rang-1-PR91-Zeugenmatrix;
- Vier-Boundary-Erklärung;
- cross-prime als Fensterrand;
- „Nichtunitarität = genau Hub“;
- matched-cutoff als Mechanismus;
- OX-REN/OX-REN' als Hauptfront;
- `H^{1/2}`-/klassische Douglas-Terminologie für `1/|x-y|`;
- Kollaps von `||I-W^*W||`;
- `0.603` als Konstante;
- Prime-only-Rang-2-Gram ohne zusätzliche Quotientenstruktur;
- Behauptung, POS-DIL-1 erkläre bereits `r_1` oder `c_aI`;
- Behauptung, `rho` sei für die neue positive Hilbertnorm unitär.

## 13. Governance

- PR #91 bleibt analytischer Draft ohne übertragenes unabhängiges Exact-Head-GREEN.
- PR #49 ist formal Ready, inhaltlich aber weiterhin `candidate only; no merge requested yet`.
- Registry, `ACTIVE_FRONT.yaml` und Arbeitsdefinition werden durch diese Front nicht automatisch geändert.
- Kein Object-X- oder RH-Abschluss.
