# Objekt X — kanonische Forschungsroadmap v2.4

> **Stand:** 13. September 2026; Registry unverändert.  
> **Rolle:** aktuelle Abhängigkeits- und Forschungsstrategiekarte.  
> **Keine Beweisautorität:** Diese Roadmap erzeugt keine `✓[M]`-Promotion, kein unabhängiges GREEN, keinen Freeze und keine Object-X-/RH-Folgerung.  
> **Operative Front:** [CURRENT-FRONT](../CURRENT-FRONT.md)  
> **Kurzstand:** [AKTUELLER_STAND](AKTUELLER_STAND.md)  
> **DAG:** [DAG](DAG.md)  
> **Objekt-X-Definition:** [OBJEKT_X_AKTUELLE_ARBEITSDEFINITION](OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md)  
> **Registry:** [ACTIVE_THEOREM_REGISTRY](ACTIVE_THEOREM_REGISTRY.md)

---

## 0. Autorität und Konfliktregel

Bei Konflikten gilt nach Zuständigkeit:

1. Arbeitsdefinition für die Identität von Objekt X;
2. Registry für gebuchten Theorem-/Reviewstatus;
3. kanonische Audit-/Beweisquelle für Mathematik im benannten Scope;
4. `CURRENT-FRONT.md` für aktuelle Priorität;
5. diese Roadmap für Strategie;
6. `ACTIVE_FRONT.yaml` für historische Stack-/PR-Provenienz.

Der aktuelle `main`-Head wird live aus GitHub gelesen und nicht selbstreferenziell als SHA gespeichert.

---

## 1. Verfügbarer Meilenstein: fixed-pair Strong Terminal / C6

Der positive Wurzelanker plus R42.51 liefert für jedes feste `0<R<S`

```math
W_{R,S}^{[U]}\varepsilon_R\longrightarrow\varepsilon_S
```

im ungeraden P11-Graphraum.

Nicht enthalten: Radienuniformität, Operatornormkonvergenz, vollständiger gerader Sektor, Object-X-Realisierung oder RH.

---

## 2. Belastbare Prime-Power-Geometrie

```math
C_{jk}^{(p)}=(\log p)p^{\min(j,k)}p^{-3(j+k)/4},
\qquad C_{kk}^{(p)}=(\log p)p^{-k/2}.
```

Nach Weil-Diagonalnormalisierung:

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}p^{-|j-k|/2}.
```

Mit `q=p^{-1/2}`:

```math
T_q^*T_q=R_q-uu^*,
\qquad T_q^*T_q+uu^*=R_q.
```

Die P11-Restseite besitzt die exakte Weil-Tail-Normalform

```math
R_R^*R_R=\sum_{p,k}w_{p,k}Z_{p,k,R}^*Z_{p,k,R}.
```

Buchung: exakte Strukturinformation und theorem-ready Nebenprojekt; noch keine vollständige gemeinsame Prime-/Archimedean-Geometrie.

---

## 3. Endliche Suzuki-/OX-GRAM-Normalform

Für `a<=1`:

```math
Q_{B_a}=G_a^+-N_a,
\qquad N_a=c_aI+C_a.
```

`G_a^+` besteht aus positiven Prime-Kanal-, Log-Multiplikator- und logarithmischen `log|D|`-Formen.

Die Frage „existiert irgendein kontraktiver Faktor?“ ist kein Object-X-Gate: bei bereits bekannter lokaler Positivität kann ein solcher Faktor zirkulär aus `Q_{B_a}` konstruiert werden. Offen bleibt eine **vorwärts konstruierte kanonische** Geometrie.

---

## 4. Zertifikationsstand

PR #98 hat die endlichen Gate-1/Gate-2-Pfade gehärtet.

- Normalisierung: `a=0.5,0.8,1.0`, Realraum/Fourier, fail-closed Arb-Residualtests, explizite Bernoulli-/`sinc`-Restbälle, Arb-Cutoffs und Endpunktfehler.
- Gate 2: Arb 512 Bit, `N<=14`, drei Radien, beide Paritäten, **42/42** verschachtelte Blöcke mit strikt positiven Cholesky-Pivots.

Firewall: endliche Zertifikate, kein globaler Weil-Positivitäts- oder RH-Beweis.

---

## 5. OX-GEN-A — gemeinsamer Exponentialgenerator `✓[M]`

Definiere

```math
E_\pm(v)=\int e^{\pm x/2}v(x)\,dx,
\qquad \mathcal Ev=(E_+(v),E_-(v)).
```

Für

```math
\rho(t)=\operatorname{diag}(e^{-t/2},e^{t/2}),
\qquad
K_n=T_{\frac12\log n}-T_{-\frac12\log n},
\qquad
\lambda_n=n^{1/4}-n^{-1/4}
```

gilt

```math
\boxed{\mathcal ET_t=\rho(t)\mathcal E,}
\qquad
\boxed{\mathcal EK_n=\lambda_n\operatorname{diag}(-1,1)\mathcal E.}
```

Suzukis elementarer archimedischer Teil ist das negative Charakter derselben Darstellung:

```math
\boxed{r_0''(t)=-\operatorname{tr}\rho(t),}
\qquad
\boxed{r_0(\log n)=-4\lambda_n^2.}
```

Mit

```math
P=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad J=-P
```

gilt

```math
\boxed{R_0(v,w)=\langle\mathcal Ev,J\mathcal Ew\rangle.}
```

Prime-only-A2 aus `{w_n,lambda_n}` bleibt im dokumentierten engen Scope `×[M]`: die volle Prime-Gram-Form descendiert nicht durch `E`, und die Anti-Kovarianz fixiert den absoluten Maßstab nicht.

---

## 6. POS-DIL-1 — erste natürliche positive Companion-Klasse

Setze

```math
S=\operatorname{diag}(-1,1)=D_n/\lambda_n=2\rho'(0).
```

Dann `S^2=P^2=I`, `PSP=-S` und `rho(t)=e^{tS/2}`.

### 6.1 Symmetrierigidität `✓[M]`

Für eine positive Hermiteform `M` verlangen wir nur die beiden bereits vorhandenen involutiven Symmetrien

```math
PMP=M,
\qquad SMS=M.
```

Dann zwingt die Algebra

```math
\boxed{M=tI.}
```

Die Blockpositivität

```math
\begin{pmatrix}M&J\\J&M\end{pmatrix}\succeq0
```

ist genau für `t>=1` erfüllt. Der eindeutige minimale positive Begleiter in dieser Klasse ist daher

```math
\boxed{M_{\min}=I.}
```

### 6.2 Enger No-Go für volle positive `rho`-Invarianz `×[M]`

Fordert man dagegen

```math
\rho(t)^*M\rho(t)=M
```

für alle `t` und `M>=0`, folgt `M=0`. Eine injektive exakte unitäre Hilbert-Intertwinerrealisierung der Boost-Darstellung auf positivem Rang 2 ist damit ausgeschlossen.

### 6.3 Prime-moment Hilbertisierung `✓[M]`

Für eine endliche nichtleere Prime-Power-Menge `N` setze

```math
w_n=\frac{\Lambda(n)}{\sqrt n},
\qquad
\kappa_N=\sum_{n\in N}w_n\lambda_n^2,
```

und

```math
V_Nv=\kappa_N^{-1/2}
\bigl(\sqrt{w_n}\,\mathcal EK_nv\bigr)_{n\in N}
\in \bigoplus_{n\in N}\mathbb C^2.
```

Dann gilt exakt

```math
\boxed{\|V_Nv\|^2=|E_+(v)|^2+|E_-(v)|^2.}
```

Mit `\mathbb P_N=\oplus_{n\in N}P` gilt im **selben positiven Zielraum**

```math
\boxed{R_0(v,w)=\langle V_Nv,\mathbb P_NV_Nw\rangle.}
```

Die minimale positive Companion-Masse wird damit nicht post hoc als Diagonalblock eingesetzt, sondern als normierte Grammasse echter gewichteter Prime-Kanalausgänge erzeugt.

Für `n=p^k`, `q_p=p^{-1/2}` ist zusätzlich

```math
\boxed{\sqrt{w_{p,k}}D_{p^k}=\sqrt{\log p}(1-q_p^k)S.}
```

Die Kanalindex-Amplitude der neuen Momentabbildung ist exakt `flat minus AR(1)-root`.

**Buchung:** `OX-GEN-A2'` ist damit `✓[M]_part`, nicht vollständig geschlossen.

---

## 7. Aktuelle Default-Priorität: POS-DIL-2 / FEATURE-SHORTING

POS-DIL-1 liefert eine positive Hilbertisierung des **Rang-2-Momentquotienten**, aber noch keine kontraktive Einbettung dieses Quotienten in die vollständige positive Featuregeometrie `G_a^+`.

Der nächste echte Gate lautet:

> Ist die kanonische Prime-moment-Abbildung als kontraktive Postkompression bzw. als natürliches Shorting/Schur-Komplement der bereits vorhandenen positiven Prime-/`log|D|`-Featuregeometrie realisierbar?

Eine erste scharfe Form ist

```math
\boxed{\|\mathcal Ev\|^2\stackrel?\le G_a^+(v).}
```

oder typkorrekt, sobald die positive Featureabbildung `\mathcal F_a^+` fixiert ist, die Existenz eines **vorwärts definierten kontraktiven** Operators `C_a` mit

```math
C_a\mathcal F_a^+v=V_{N_a}v.
```

Beide Ausgänge bleiben logisch offen:

- **PASS:** die minimale positive Rang-2-Masse sitzt tatsächlich kontraktiv in der vorhandenen positiven Featuregeometrie;
- **FAIL:** POS-DIL-1 bleibt gültig, aber diese Shorting-Klasse fällt und muss mit Root/Hub-/`log|D|`-Struktur weiter verengt werden.

Keine fertige Weilform, kein RH und keine rückwärts definierte Positivitätswurzel dürfen als Input verwendet werden.

---

## 8. Danach: OX-GEN-B

Erst nach POS-DIL-2 werden die bislang offenen archimedischen Teile systematisch in dieselbe Geometrie einbezogen:

- `r_1` / regulärer archimedischer Korrektor;
- dominanter Skalarblock `c_aI`.

POS-DIL-1 erklärt diese Blöcke ausdrücklich noch nicht.

Parallel: Prime-Power-AR(1)/Martingal-Faktorisierung als eigenständigen RH-unabhängigen Satz verschriftlichen; nicht als Objekt X vermarkten.

---

## 9. Vollständiger Object-X-Pfad

Ein echter X-Kandidat muss mindestens spezifizieren:

- intrinsische gemeinsame Geometrie,
- Hilbert-/Mediatorraum,
- kanonische Abbildung `T_X`,
- Prime-Power-Kanal,
- archimedischen Kanal,
- gemeinsame nichtorthogonale Kopplung,
- Testklasse und Normalisierung,
- Nicht-Zirkularität.

```text
OX-GEN / POS-DIL partial geometry
        |
        | --candidate-input only-->
        v
GENUINE X CANDIDATE ?[O]
        |
        | --requires separate proof-->
        v
EXACT FULL WEIL-GRAM IDENTITY ?[O]
        |
        v
OBJECT-X REALIZATION ?[O]
        |
        v
WEIL-CRITERION-SCOPE ?[O]
        |
        v
RH
```

Keine `candidate-input`-Kante ist als logische Implikation zu lesen.

---

## 10. Separate Nebenfronten

- **R37/G4c:** separat offen; Beziehung zur OX-GEN-/X-Route unresolved.
- **Historische R43-COND-/FD23-/Flagfragen:** eigene offene Quantoren, nicht aktuelle Voraussetzung.
- **PR #91:** analytischer Source-descent/Weil-separation-Draft; kein unabhängiger Exact-Head-GREEN wird übertragen.
- **PR #49 / SW1 salvage:** Candidate-only Nebenfront; kein stiller Merge.

---

## 11. Gesperrte Interpretationen

Nicht reaktivieren:

- PR91-Zeugenmatrix Rang 1;
- `3/4` als bloße Dämpfung;
- Vier-Boundary-Erklärung;
- cross-prime als Fensterrand;
- „Nichtunitarität = Hub“;
- matched cutoff als Objekt-X-Mechanismus;
- OX-REN/OX-REN' als Hauptfront;
- klassische `H^{1/2}`-/Douglas-Terminologie für `1/|x-y|`;
- globaler Kollaps von `||I-W^*W||`;
- `0.603` als Konstante;
- reine OX-GRAM-Existenztests;
- Prime-only-Rang-2-Gram ohne zusätzliche Quotientenstruktur;
- Behauptung, POS-DIL-1 erkläre bereits `r_1` oder `c_aI`;
- Behauptung, `rho` sei für die neue positive Hilbertnorm unitär.

---

## 12. Falsifikations-/Rollback-Regeln

- **OX-GEN-A fällt:** darauf beruhende POS-DIL-Sätze neu auditieren; Prime-AR(1), C6 und Object-X-Ziel bleiben getrennt.
- **POS-DIL-1A-Klasse fällt:** nur Symmetrie-Companion-Buchung zurücknehmen.
- **Prime-moment-Identität fällt:** POS-DIL-1C und die Root-Amplitudenbrücke zurücknehmen; OX-GEN-A bleibt separat.
- **POS-DIL-2 fällt:** nur die kontraktive Feature-Shorting-Klasse ist ausgeschlossen; POS-DIL-1 bleibt bestehen.
- **Prime-AR(1)-Algebra fällt:** alle darauf gestützten Root/Hub-Interpretationen neu auditieren.
- **R37/G4c fällt:** keine automatische Wirkung auf OX-GEN/POS-DIL/C6.
- **PR91 fällt:** nur sein Kandidat fällt.
- **Ein X-Kandidat fällt an der vollen Weil-Gram-Identität:** kein universelles No-Go.

---

## 13. Explizit offen

```text
POS-DIL-2 / FEATURE-SHORTING
OX-GEN-B
r_1 / regular archimedean correction
scalar block c_a I in intrinsic geometry
genuine X candidate
exact full Weil-Gram identity
Object-X realization
Weil-criterion scope verification
RH
R37/G4c [separate]
```

Historische Nebenfragen bleiben über Audits, Git-Historie und Registry-/Problemprovenienz zugänglich; sie werden hier nicht zur Default-Priorität erhoben.
