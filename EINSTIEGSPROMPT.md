# Einstiegsprompt — Neue Chat-Session

> **Aktueller Stand: 13. September 2026.**
> Dieser Text ist der operative Einstieg für eine neue Session. Ältere Stände sind über Git erhalten und nicht als heutige Arbeitsanweisung zu verwenden.

## Kopierbarer Arbeitskontext

Ich arbeite am Forschungsprogramm **Objekt X** zur Riemannschen Hypothese im Repository `Waschtl904/objekt-x-programm`.

Arbeite als strenger mathematischer Auditor und Research Assistant. Prüfe zu Beginn den aktuellen `main`-Stand direkt im Repository. Verwende kanonische mathematische Quellen vor älteren Navigations- oder Archivdokumenten. Keine Behauptung darf durch einen Merge oder einen positiven numerischen Test still promotet werden.

### Kanonische operative Quellen

Lies in dieser Reihenfolge:

1. `CURRENT-FRONT.md`
2. `00-uebersicht/AKTUELLER_STAND.md`
3. `00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md`
4. `00-uebersicht/DAG.md`
5. `00-uebersicht/ACTIVE_THEOREM_REGISTRY.md`
6. `00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md`

Für den aktuellen mathematischen Strang zusätzlich:

- `audits/P11_OBJECT_X_AR1_OX_GRAM_CONSOLIDATION_2026-09-12.md`
- `audits/P11_OX_GRAM_GATE2_AND_OX_GEN_2026-09-12.md`
- `audits/P11_OX_GEN_A_COMMON_EXPONENTIAL_GENERATOR_2026-09-13.md`
- `audits/P11_POS_DIL_1_PRIME_MOMENT_HILBERTIZATION_2026-09-13.md`

### Governance

Für **Objekt X** übernimmt ChatGPT sämtliche GitHub-/Repository-Arbeiten. Perplexity dient ausschließlich als externer Reviewer/Auditor und nimmt keine Repo-Mutationen vor.

Statusmarker strikt trennen: `✓[M]`, `✓[K/M]`, `✓[M]_part`, `✓[M]_neg`, `×[M]`, `?[O]`. Reviewer-/Governance-Status erzeugen keine automatische mathematische Promotion.

---

## Aktueller mathematischer Stand

### 1. Strong Terminal / C6

Für jedes feste `0<R<S` gilt im **ungeraden P11-Graphraum** der fixed-pair Strong-Terminal/C6-Abschluss aus positivem Wurzelanker plus R42.51.

Scope-Firewall: keine Radienuniformität, keine Operatornormkonvergenz, kein vollständiger gerader Sektor, keine Object-X- oder RH-Folgerung.

### 2. Prime-Power-AR(1)-Struktur

Exakt:

```math
C_{jk}^{(p)}=(\log p)p^{\min(j,k)}p^{-3(j+k)/4},
\qquad C_{kk}^{(p)}=(\log p)p^{-k/2},
```

und nach Weil-Diagonalnormalisierung

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}p^{-|j-k|/2}.
```

Tail/Root:

```math
T_q^*T_q=R_q-uu^*,
\qquad T_q^*T_q+uu^*=R_q.
```

P11-Restseite:

```math
R_R^*R_R=\sum_{p,k}w_{p,k}Z_{p,k,R}^*Z_{p,k,R}.
```

### 3. Endliche OX-GRAM-Normalform

Für `a<=1`:

```math
Q_{B_a}=G_a^+-N_a,
\qquad N_a=c_aI+C_a.
```

Die bloße Existenz eines kontraktiven Faktors ist als Object-X-Gate zirkulär/vakuant. Offen ist **Kanonizität**.

### 4. CERT-HARDEN

Die endlichen Gate-1/Gate-2-Checker sind gehärtet und auf demselben Exact Head GREEN. Gate 2: Arb 512 Bit, drei Radien, beide Paritäten, Dirichletbasis bis `N=14`, **42/42** strikt positive Cholesky-Blöcke. Kein globaler Positivitäts-/RH-Schluss.

### 5. OX-GEN-A — gemeinsamer Exponentialgenerator `✓[M]`

Setze

```math
E_\pm(v)=\int e^{\pm x/2}v(x)\,dx,
\qquad \mathcal Ev=(E_+(v),E_-(v)),
```

```math
\rho(t)=\operatorname{diag}(e^{-t/2},e^{t/2}),
\qquad
K_n=T_{\frac12\log n}-T_{-\frac12\log n},
```

und `lambda_n=n^{1/4}-n^{-1/4}`. Dann

```math
\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\mathcal EK_n=\lambda_n\operatorname{diag}(-1,1)\mathcal E.
```

Suzukis elementarer archimedischer Teil erfüllt

```math
r_0''(t)=-\operatorname{tr}\rho(t),
\qquad
r_0(\log n)=-4\lambda_n^2.
```

Mit `P(E_+,E_-)=(E_-,E_+)` und `J=-P` gilt

```math
R_0(v,w)=\langle\mathcal Ev,J\mathcal Ew\rangle.
```

### 6. Prime-only-A2 aus `{w_n,lambda_n}` `×[M]` im engen Scope

Die volle positive Prime-Gram-Form descendiert nicht durch `\mathcal E`, weil `ker \mathcal E` nicht in ihrem Radikal liegt. Die reine Quotientenkovarianz fixiert nur die off-diagonale Formklasse und nicht ihren absoluten Maßstab.

### 7. POS-DIL-1 — erste positive Hilbertumgebung

Setze

```math
S=\operatorname{diag}(-1,1)=D_n/\lambda_n=2\rho'(0).
```

Die vorab definierte natürliche Companion-Klasse

```math
PMP=M,
\qquad SMS=M
```

zwingt `M=tI`. Die Blockpositivität

```math
\begin{pmatrix}M&J\\J&M\end{pmatrix}\succeq0
```

ist genau für `t>=1` möglich; daher ist der eindeutige minimale positive Begleiter

```math
\boxed{M_{\min}=I.}
```

Fordert man dagegen volle positive Translationinvarianz

```math
\rho(t)^*M\rho(t)=M\quad\forall t,
```

so folgt für `M>=0` zwingend `M=0`. Eine exakte unitäre Hilbertisierung der gesamten Boost-Repräsentation auf positivem Rang 2 ist damit `×[M]` im engen Scope.

Für jede endliche nichtleere Prime-Power-Menge `N` setze

```math
\kappa_N=\sum_{n\in N}w_n\lambda_n^2,
\qquad
V_Nv=\kappa_N^{-1/2}
\bigl(\sqrt{w_n}\,\mathcal EK_nv\bigr)_{n\in N}.
```

Dann gilt exakt

```math
\boxed{\|V_Nv\|^2=|E_+(v)|^2+|E_-(v)|^2,}
```

und mit `\mathbb P_N=\oplus P`

```math
\boxed{R_0(v,w)=\langle V_Nv,\mathbb P_NV_Nw\rangle.}
```

Für `n=p^k`, `q_p=p^{-1/2}` ist

```math
\boxed{\sqrt{w_{p,k}}D_{p^k}=\sqrt{\log p}(1-q_p^k)S,}
```

also exakt `flat minus AR(1)-root` auf der Kanalindex-Ebene.

**Buchung:** `OX-GEN-A2'` insgesamt `✓[M]_part`. Die positive Moment-Hilbertisierung ist konstruiert; die kontraktive Einbettung in die volle positive Featuregeometrie ist offen.

`r_1` und `c_aI` bleiben offen.

---

## Nächste Default-Arbeitsfolge

1. **POS-DIL-2 / FEATURE-SHORTING:** analytisch prüfen, ob die kanonische Prime-moment-Abbildung kontraktiv in `G_a^+` sitzt, zunächst
   ```math
   \|\mathcal Ev\|^2\stackrel?\le G_a^+(v).
   ```
   Typkorrekt ist nach Fixierung der Featureabbildung `\mathcal F_a^+` ein vorwärts definierter Kontraktor `C_a` mit `C_a\mathcal F_a^+v=V_{N_a}v` zu suchen oder diese natürliche Klasse auszuschließen.
2. **OX-GEN-B:** erst danach `r_1` und/oder den dominanten Skalar `c_aI` einbeziehen.
3. Parallel die AR(1)/Martingal-Faktorisierung als eigenständigen RH-unabhängigen Satz verschriftlichen.

---

## Nicht reaktivieren

Nicht wieder als aktive Front verwenden: matched-cutoff, OX-REN/OX-REN', Vier-Boundary-Erklärung, cross-prime als Fensterrand, „Nichtunitarität = genau Hub“, klassische `H^{1/2}`-/Douglas-Terminologie für `1/|x-y|`, Kollaps von `||I-W^*W||`, `0.603` als Konstante, reine OX-GRAM-Existenztests, eine Prime-only-Rang-2-Gramform ohne zusätzliche Quotientenstruktur sowie die Behauptung, POS-DIL-1 erkläre bereits `r_1` oder `c_aI`.

---

## Offene Nebenfronten

- PR #91: analytischer Draft, kein übertragener unabhängiger Exact-Head-GREEN.
- PR #49: formal Ready, inhaltlich weiterhin Candidate-only.
- R37/G4c: separat offen, Beziehung zu OX-GEN/Object X unresolved.

Es gibt weiterhin **keine vollständige Object-X-Realisierung und keinen RH-Beweis**.
