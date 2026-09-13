# Offene Probleme — aktuelle OX-GEN-Priorität

> **Stand:** 13. September 2026.  
> Operative Quellen: [CURRENT-FRONT](CURRENT-FRONT.md), [AKTUELLER_STAND](00-uebersicht/AKTUELLER_STAND.md), [Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md), [DAG](00-uebersicht/DAG.md), [Registry](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md).
>
> Fixed-pair Strong Terminal/C6 ist im ausgewiesenen ungeraden P11-Scope verfügbar. OX-GEN-A ist seit dem 13. September positiv geschlossen; die operative Front liegt jetzt bei einer **positiven Dilatation/Einbettung** der gemeinsamen Rang-2-Generatorgeometrie.

---

## Geschlossenes OX-GEN-A-Ergebnis

### `[OX-GEN-A]` Gemeinsamer Exponentialgenerator `✓[M]`

Mit

```math
E_\pm(v)=\int e^{\pm x/2}v(x)\,dx,
\qquad
\mathcal Ev=(E_+(v),E_-(v))
```

und

```math
\rho(t)=\operatorname{diag}(e^{-t/2},e^{t/2})
```

gilt

```math
\mathcal ET_t=\rho(t)\mathcal E,
```

sowie für

```math
K_n=T_{\frac12\log n}-T_{-\frac12\log n},
\qquad
\lambda_n=n^{1/4}-n^{-1/4}
```

```math
\mathcal EK_n=\lambda_n\operatorname{diag}(-1,1)\mathcal E.
```

Suzukis elementarer archimedischer Anteil ist das negative Charakter derselben Darstellung:

```math
r_0''(t)=-\operatorname{tr}\rho(t),
\qquad
r_0(\log n)=-4\lambda_n^2.
```

Mit Austauschoperator

```math
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}
```

gilt

```math
R_0(v,w)=\langle\mathcal Ev,-P\mathcal Ew\rangle.
```

Die Struktur ist fensterunabhängig; für Nullfortsetzungen aus `H_0^1(-a,a)` tritt in `E_\pm(K_nv)` kein Randterm auf.

Kanonische Quelle: `audits/P11_OX_GEN_A_COMMON_EXPONENTIAL_GENERATOR_2026-09-13.md`.

---

## Geschlossener enger No-Go

### `[OX-GEN-A2-PRIME-ONLY]` Nur aus `{w_n,lambda_n}` `×[M]`

Die volle positive Prime-Gram-Form descendiert nicht durch `\mathcal E`, weil `ker \mathcal E` nicht in ihrem Radikal liegt.

Die reine Quotientenkovarianz

```math
D_n^*HD_n=-\lambda_n^2H
```

fixiert nur eine off-diagonale Hermiteform

```math
H=\begin{pmatrix}0&b\\\bar b&0\end{pmatrix};
```

der Maßstab `b` bleibt frei. Die diskreten Daten `{w_n,lambda_n}` allein können daher den absoluten `R_0`-Koeffizienten nicht kanonisch bestimmen.

**Scope-Firewall:** Dies ist kein No-Go gegen eine Konstruktion, die die vollständige Translation-/Spiegelstruktur oder zusätzliche positive Geometrie benutzt.

---

## Priorität 0 — POSITIVE-DILATION-CLASS

### `[POSITIVE-DILATION-CLASS]` Natürliche zulässige Klasse definieren `?[O]`

Vor jedem No-Go eine enge, mathematisch natürliche Klasse positiver Erweiterungen/Intertwiner festschreiben, die aus

```text
(C^2, rho, P, E), Prime channels K_n, Prime AR(1), log|D|-geometry
```

gebaut werden darf.

Die Klasse darf nicht post hoc auf ein gewünschtes Ergebnis zugeschnitten werden.

**Gate-Regel:** Positive Konstruktion und negativer Ausgang müssen beide vorab logisch möglich sein.

---

## Priorität 1 — OX-GEN-A2' / POSITIVE-DILATION

### `[OX-GEN-A2']` Positive Einbettung des Rang-2-Generators `?[O]`

Frage:

> Lässt sich die kanonische indefinite Translation-/Reflexions-Geometrie
> 
> ```math
> (\mathbb C^2,\rho,P,\mathcal E)
> ```
> 
> intrinsisch in die positive Prime-/`log|D|`-Featuregeometrie einbetten oder als Schur-/Defektterm einer positiven Erweiterung realisieren — ohne die fertige Weilform, RH oder eine rückwärts definierte Positivitätswurzel zu verwenden?

Positive Antwort: erster expliziter gemeinsamer Prime-/Archimedean-Baustein **mit positiver Umgebung**.

Negative Antwort: Klassen-No-Go nur für die vorher definierte `POSITIVE-DILATION-CLASS`.

---

## Priorität 2 — OX-GEN-B

### `[OX-GEN-B]` Verbleibende archimedische Teile `?[O]`

Erst nach A2' sollen die bislang unberührten Teile in dieselbe Geometrie einbezogen werden:

- `[OX-R1]` regulärer `r_1''`-Korrektor;
- `[OX-SCALAR]` dominanter Skalarblock `c_aI`.

Die gemeinsame Rang-2-Generatorstruktur erklärt diese Teile **noch nicht**.

---

## Priorität 3 — vollständiger Objekt-X-Pfad

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

### R37/G4c `?[O]`

Separat offen. Beziehung zur OX-GEN-/X-Route unresolved.

### Historische R43-COND-/FD23-/Flagfragen

Einzelne quantitative Fragen bleiben in ihren eigenen Quantoren offen, sind aber keine Voraussetzungen des fixed-pair-C6-Pfads und derzeit nicht Default-Priorität.

### PR #91

Analytischer Draft; kein unabhängiger Exact-Head-GREEN wird durch die aktuelle Front übertragen.

### PR #49 / SW1 salvage

Candidate-only Nebenfront. Kein stiller Merge.

---

## Geschlossen / nicht erneut öffnen ohne neuen Widerspruch

- fixed-pair Strong Terminal/C6 im dokumentierten ungeraden Scope;
- OX-GRAM-Existenzfrage als zirkuläres/vakuantes X-Gate;
- CERT-HARDEN im dokumentierten endlichen Scope;
- OX-GEN-A gemeinsamer Translation-/Reflexionsgenerator;
- Prime-only-A2 aus `{w_n,lambda_n}` im exakt definierten engen Scope.

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
- Behauptung, der Rang-2-Generator erkläre bereits `r_1` oder `c_aI`.

Historische NEU-/Wres-/HH-Probleme bleiben über Git, INDEX, STATUS und ursprüngliche Dokumente als Provenienz verfügbar.
