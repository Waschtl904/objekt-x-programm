# Offene Probleme — aktuelle POS-DIL-Priorität

> **Stand:** 13. September 2026.  
> Operative Quellen: [CURRENT-FRONT](CURRENT-FRONT.md), [AKTUELLER_STAND](00-uebersicht/AKTUELLER_STAND.md), [Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md), [DAG](00-uebersicht/DAG.md), [Registry](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md).
>
> Fixed-pair Strong Terminal/C6 ist im ausgewiesenen ungeraden P11-Scope verfügbar. OX-GEN-A ist geschlossen; POS-DIL-1 liefert einen positiven Prime-moment-Quotientenbaustein. Die operative Hauptfront ist jetzt **POS-DIL-2 / FEATURE-SHORTING**.

---

## Geschlossenes OX-GEN-A-Ergebnis

### `[OX-GEN-A]` Gemeinsamer Exponentialgenerator `✓[M]`

Mit

```math
E_\pm(v)=\int e^{\pm x/2}v(x)\,dx,
\qquad
\mathcal Ev=(E_+(v),E_-(v)),
```

```math
\rho(t)=\operatorname{diag}(e^{-t/2},e^{t/2})
```

und

```math
K_n=T_{\frac12\log n}-T_{-\frac12\log n},
\qquad
\lambda_n=n^{1/4}-n^{-1/4}
```

gilt

```math
\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\mathcal EK_n=\lambda_n\operatorname{diag}(-1,1)\mathcal E.
```

Suzukis elementarer archimedischer Anteil ist das negative Charakter derselben Darstellung:

```math
r_0''(t)=-\operatorname{tr}\rho(t),
\qquad
r_0(\log n)=-4\lambda_n^2.
```

Mit `P(E_+,E_-)=(E_-,E_+)`, `J=-P`:

```math
R_0(v,w)=\langle\mathcal Ev,J\mathcal Ew\rangle.
```

Kanonische Quelle: `audits/P11_OX_GEN_A_COMMON_EXPONENTIAL_GENERATOR_2026-09-13.md`.

---

## Geschlossener enger Prime-only-No-Go

### `[OX-GEN-A2-PRIME-ONLY]` Nur aus `{w_n,lambda_n}` `×[M]`

Die volle positive Prime-Gram-Form descendiert nicht durch `\mathcal E`, weil `ker \mathcal E` nicht in ihrem Radikal liegt. Die reine Quotientenkovarianz fixiert außerdem nur die off-diagonale Formklasse, nicht ihren absoluten Maßstab.

**Scope-Firewall:** Dies ist kein No-Go gegen Konstruktionen mit der vollständigen Translation-/Spiegelstruktur, Momentkompressionen oder zusätzlicher positiver Geometrie.

---

## POS-DIL-1 — geschlossen im dokumentierten Scope

Kanonische Quelle: `audits/P11_POS_DIL_1_PRIME_MOMENT_HILBERTIZATION_2026-09-13.md`.

### `[POS-DIL-1A]` Symmetrierigider positiver Begleiter `✓[M]`

Setze

```math
S=\operatorname{diag}(-1,1)=D_n/\lambda_n=2\rho'(0).
```

Die natürliche Companion-Klasse

```math
PMP=M,
\qquad SMS=M
```

zwingt

```math
M=tI.
```

Die zusätzliche Blockpositivität

```math
\begin{pmatrix}M&J\\J&M\end{pmatrix}\succeq0
```

ist genau für `t>=1` erfüllt. Damit ist der eindeutige minimale Begleiter in dieser Klasse

```math
\boxed{M_{\min}=I.}
```

### `[POS-DIL-1B]` Volle positive `rho`-Invarianz `×[M]`

Für `M>=0` gilt

```math
\rho(t)^*M\rho(t)=M\quad\forall t
\quad\Longrightarrow\quad M=0.
```

Ausgeschlossen ist damit die enge Klasse einer injektiven exakten unitären Hilbert-Intertwinerrealisierung der vollen Boost-Darstellung auf positivem Rang 2.

### `[POS-DIL-1C]` Prime-moment Hilbertisierung `✓[M]`

Für jede endliche nichtleere Prime-Power-Menge `N` setze

```math
\kappa_N=\sum_{n\in N}w_n\lambda_n^2,
```

```math
V_Nv=\kappa_N^{-1/2}
\bigl(\sqrt{w_n}\,\mathcal EK_nv\bigr)_{n\in N}.
```

Dann exakt

```math
\boxed{\|V_Nv\|^2=|E_+(v)|^2+|E_-(v)|^2,}
```

und mit `\mathbb P_N=\oplus P`

```math
\boxed{R_0(v,w)=\langle V_Nv,\mathbb P_NV_Nw\rangle.}
```

Für `n=p^k`, `q_p=p^{-1/2}` verbindet sich diese Momentabbildung mit der AR(1)-Root-Geometrie durch

```math
\boxed{\sqrt{w_{p,k}}D_{p^k}=\sqrt{\log p}(1-q_p^k)S.}
```

**Buchung:** `OX-GEN-A2'` insgesamt `✓[M]_part`: positiver gemeinsamer Quotientenbaustein konstruiert, volle kontraktive Einbettung noch offen.

---

## Priorität 0 — POS-DIL-2 / FEATURE-SHORTING

### `[POS-DIL-2]` Kontraktive Einbettung in die vorhandene positive Featuregeometrie `?[O]`

Frage:

> Ist die kanonische Prime-moment-Abbildung als kontraktive Postkompression bzw. als natürliches Shorting/Schur-Komplement der bereits vorhandenen positiven Prime-/`log|D|`-Featuregeometrie realisierbar — ohne fertige Weilform, RH oder rückwärts definierte Positivitätswurzel?

Eine erste scharfe Form ist

```math
\boxed{\|\mathcal Ev\|^2\stackrel?\le G_a^+(v).}
```

Typkorrekt soll nach Fixierung einer positiven Featureabbildung `\mathcal F_a^+` ein **vorwärts definierter** Operator `C_a` gesucht werden mit

```math
C_a\mathcal F_a^+v=V_{N_a}v,
\qquad \|C_a\|\le1.
```

Beide Ausgänge sind vorab logisch möglich:

- **PASS:** die minimale positive Rang-2-Masse sitzt kontraktiv in der bestehenden positiven Featuregeometrie;
- **FAIL:** nur diese natürliche Shorting-Klasse ist ausgeschlossen; POS-DIL-1 bleibt gültig und die Klasse muss mit Root/Hub-/`log|D|`-Struktur verfeinert werden.

Keine weiteren bloßen `mu_max`-Sweeps als Hauptfront. Zuerst algebraisch/analytisch; Numerik nur als Gegenvektorsuche oder Orientierung.

---

## Priorität 1 — OX-GEN-B

### `[OX-GEN-B]` Verbleibende archimedische Teile `?[O]`

Erst nach POS-DIL-2 sollen die bislang unberührten Teile in dieselbe Geometrie einbezogen werden:

- `[OX-R1]` regulärer `r_1''`-Korrektor;
- `[OX-SCALAR]` dominanter Skalarblock `c_aI`.

POS-DIL-1 erklärt diese Teile **noch nicht**.

---

## Priorität 2 — vollständiger Objekt-X-Pfad

### `[OX-CANDIDATE]` Genuine X candidate `?[O]`

Gesucht wird eine intrinsische gemeinsame Geometrie mit Hilbert-/Mediatorraum, kanonischer Abbildung, Prime-Power- und archimedischem Kanal, gemeinsamer nichtorthogonaler Kopplung, Testklasse, Normalisierung und Nicht-Zirkularität.

### `[OX-WEIL-GRAM]` Exakte volle Weil-Gram-Identität `?[O]`

```math
Q_W(f,g)=\langle T_Xf,T_Xg\rangle_{\mathcal K_X}
```

auf der richtigen vollständig normalisierten Testklasse.

### `[OX-REALIZATION]` Object-X-Realisierung `?[O]`

Erst gemeinsame intrinsische Geometrie plus exakte volle Weil-Gram-Identität bilden eine Realisierung.

### `[OX-WEIL-SCOPE]` Weil-Kriterium-Scope `?[O]`

Nach einer Realisierung separat prüfen, ob Form und Testklasse exakt den benötigten klassischen Weil-Kriterium-Scope erfüllen.

### `RH` `?[O]`

Unverändert offen.

---

## Spur B — eigenständige Mathematik

### `[AR1-WRITEUP]` Prime-Power-AR(1)/Martingal-Faktorisierung

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}p^{-|j-k|/2},
\qquad
T_q^*T_q+uu^*=R_q.
```

Theorem-ready, RH-unabhängig und **nicht als Objekt X** verschriftlichen.

---

## Separate / geparkte Probleme

- **R37/G4c `?[O]`:** separat offen; Beziehung zur OX-GEN-/X-Route unresolved.
- **Historische R43-COND-/FD23-/Flagfragen:** eigene Quantoren, nicht Voraussetzung des fixed-pair-C6-Pfads.
- **PR #91:** analytischer Draft; kein unabhängiger Exact-Head-GREEN wird durch die aktuelle Front übertragen.
- **PR #49 / SW1 salvage:** Candidate-only Nebenfront; kein stiller Merge.

---

## Geschlossen / nicht erneut öffnen ohne neuen Widerspruch

- fixed-pair Strong Terminal/C6 im dokumentierten ungeraden Scope;
- OX-GRAM-Existenzfrage als zirkuläres/vakuantes X-Gate;
- CERT-HARDEN im dokumentierten endlichen Scope;
- OX-GEN-A gemeinsamer Translation-/Reflexionsgenerator;
- Prime-only-A2 aus `{w_n,lambda_n}` im exakt definierten engen Scope;
- POS-DIL-1A Symmetrierigidität/minimaler Companion;
- POS-DIL-1B voller `rho`-unitärer Same-space-Weg als enger No-Go;
- POS-DIL-1C Prime-moment Hilbertisierung.

---

## Gesperrte Altdeutungen

Nicht als neue offene Probleme wieder einführen:

- PR91-Zeugenmatrix Rang 1;
- `3/4` als freie Dämpfung;
- Vier-Boundary-Erklärung;
- cross-prime als Boundary;
- „Nichtunitarität = Hub“;
- matched cutoff / OX-REN;
- klassische `H^{1/2}`-/Douglas-Deutung von `1/|x-y|`;
- globaler Defektnorm-Kollaps;
- `0.603` als Konstante;
- reine OX-GRAM-Existenzsweeps;
- Prime-Gram auf dem Rang-2-Quotienten ohne zusätzliche Quotientenstruktur;
- Behauptung, POS-DIL-1 erkläre bereits `r_1` oder `c_aI`;
- Behauptung, `rho` sei für die neue positive Hilbertnorm unitär.

Historische NEU-/Wres-/HH-Probleme bleiben über Git, INDEX, STATUS und ursprüngliche Dokumente als Provenienz verfügbar.
