# Objekt X — kanonische Forschungsroadmap v2.6

> **Stand:** 13. September 2026; Registry unverändert.  
> **Rolle:** aktuelle Abhängigkeits- und Forschungsstrategiekarte.  
> **Keine Beweisautorität:** Diese Roadmap erzeugt keine `✓[M]`-Promotion, kein unabhängiges GREEN, keinen Freeze und keine Object-X-/RH-Folgerung.  
> **Operative Front:** [CURRENT-FRONT](../CURRENT-FRONT.md)  
> **Kurzstand:** [AKTUELLER_STAND](AKTUELLER_STAND.md)  
> **DAG:** [DAG](DAG.md)  
> **Registry:** [ACTIVE_THEOREM_REGISTRY](ACTIVE_THEOREM_REGISTRY.md)

---

## 1. Ausgangsbasis

Fixed-pair Strong Terminal/C6 ist im ungeraden P11-Graphraum verfügbar. Die Prime-Power-Seite besitzt die exakte AR(1)/Weil-Tail-Struktur

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}p^{-|j-k|/2},
\qquad T_q^*T_q+uu^*=R_q.
```

Für `a<=1` ist die lokalisierte Suzuki-/Weilform

```math
Q_{B_a}=G_a^+-N_a,
\qquad N_a=c_aI+C_a.
```

Die rückwärts aus bekannter Positivität definierte Kontraktorexistenz ist kein Object-X-Gate.

---

## 2. OX-GEN-A `✓[M]`

```math
\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\mathcal EK_n=D_n\mathcal E,
```

```math
r_0''(t)=-\operatorname{tr}\rho(t),
\qquad
R_0(v,w)=\langle\mathcal Ev,-P\mathcal Ew\rangle.
```

Prime-only-A2 aus `{w_n,lambda_n}` bleibt `×[M]` im engen Scope.

---

## 3. POS-DIL-1 — positive Rang-2-Hilbertumgebung

Die Companion-Symmetrien erzwingen `M=tI`; minimale Blockpositivität liefert `M=I`. Volle positive `rho`-Invarianz erzwingt `M=0`.

Die Prime-moment-Abbildung

```math
V_Nv=\kappa_N^{-1/2}(\sqrt{w_n}\,\mathcal EK_nv)_{n\in N}
```

liefert

```math
\|V_Nv\|^2=\|\mathcal Ev\|^2,
\qquad
R_0(v,w)=\langle V_Nv,\mathbb P_NV_Nw\rangle.
```

Für `n=p^k`:

```math
\sqrt{w_{p,k}}D_{p^k}=\sqrt{\log p}(1-p^{-k/2})S.
```

Buchung: `OX-GEN-A2'` insgesamt `✓[M]_part`.

---

## 4. POS-DIL-2A — bestehende lokale Featuremasse reicht nicht `×[M]`

Bei `a=1/2` verletzt eine explizite Plateaufolge die notwendige unit-gain-Bedingung

```math
\|\mathcal Ev\|^2\le G_{1/2}^+(v).
```

Der exakte Grenzdefekt ist

```math
\delta_0
=32\sinh^2\frac14-1-\sqrt2(\log2)^2
>\frac5{32}>0.
```

Damit sind unit-gain Shorting und kontraktive Target-observables innerhalb der unveränderten `G_{1/2}^+`-Norm ausgeschlossen.

---

## 5. POS-DIL-2B — erster äußerer Prime-Shift-Shell `✓[M]` bei a=1/2

Die nächste positive Klasse wird rein geometrisch definiert:

```math
\mathscr S_a^{\rm out}
=\{n=p^k:a<c_n\le2a\},
\qquad c_n=\frac12\log n.
```

```math
H_a^{\rm out}(v,w)
=\sum_{n\in\mathscr S_a^{\rm out}}
\frac{\Lambda(n)}{\sqrt n}
\langle K_nv,K_nw\rangle.
```

Für jeden äußeren Kanal (`c_n>a`) sind die beiden verschobenen Fenster disjunkt:

```math
\boxed{\|K_nv\|_2^2=2\|v\|_2^2.}
```

Folglich

```math
H_a^{\rm out}(v)=2B_a^{\rm out}\|v\|_2^2.
```

Diese Skalarmasse ist **kein gefittetes `tI`**, sondern die exakte lokale Form echter Prime-Kanäle mit ihren Weilgewichten.

Bei `a=1/2` enthält der Shell insbesondere `3,4,5`. Zusammen mit dem vorhandenen Log-Multiplikator:

```math
G_{1/2}^+(v)+H_{1/2}^{\rm out}(v)
>\frac83\|v\|_2^2.
```

Andererseits

```math
\|\mathcal Ev\|^2
\le4\sinh\frac12\|v\|_2^2
<\frac83\|v\|_2^2.
```

Damit

```math
\boxed{
\|\mathcal Ev\|^2
\le G_{1/2}^+(v)+H_{1/2}^{\rm out}(v)
}
```

auf der ganzen Testklasse.

Mit `A_{1/2}^{out}=G_{1/2}^++H_{1/2}^{out}` folgt

```math
\boxed{
\begin{pmatrix}
A_{1/2}^{\rm out}&R_0\\
R_0&A_{1/2}^{\rm out}
\end{pmatrix}\succeq0.
}
```

Dies ist der erste nach dem POS-DIL-2A-No-Go konstruierte positive gemeinsame Prime-/`r_0`-Schurbaustein.

---

## 6. Warum der Fortschritt noch partiell ist

Die äußeren Kanäle `c_n>a` wurden in der lokalisierten Suzuki-Normalform nicht als Teil des endlichen `G_a^+`-Blocks behalten. Ihre positive Restriktion auf das Fenster ist mathematisch echt, aber eine **vollständige Weil-Identität darf diese Energie nicht einfach zusätzlich erfinden**.

Daher bleiben zwei Fragen offen:

1. **Radius:** Für welche `a` trägt derselbe geometrische Shell die Momentmasse?
2. **Buchung:** Welche kanonische Gegenbuchung/Teleskopierung/Root-Hub-Struktur erlaubt den Shell in einer exakten gemeinsamen Geometrie, ohne die Weilform zu verändern?

Die zweite Frage hat strategisch Vorrang vor weiteren bloßen Positivitätssweeps.

---

## 7. Aktuelle Default-Priorität: POS-DIL-2C / SHELL-BOOKING-AND-RADIUS

### Gate 2C-B — exakte Shell-Buchung `?[O]`

Untersuche zuerst die Provenienz der reinen Außenkanalmasse:

- Wo erscheint sie vor der lokalen Cutoff-/Normalform-Umschreibung?
- Lässt sie sich durch Shell-Differenzen oder eine telescopische Prime-Zerlegung bilanzieren?
- Gibt die AR(1)-Root/Hub-Zerlegung `T_q^*T_q+uu^*=R_q` eine natürliche Gegenkomponente?
- Gibt es eine Beziehung der POS-DIL-1-Amplitude `1-u_k` zu dieser Gegenbuchung?

Erfolg nur, wenn die volle Form unverändert bleibt und die Konstruktion vorwärts aus vorhandenen Daten kommt.

### Gate 2C-R — Radiusfortsetzung `?[O]`

Bestimme den maximalen Radiusbereich, auf dem

```math
\|\mathcal Ev\|^2
\le G_a^+(v)+H_a^{\rm out}(v)
```

gilt. Algebraische Intervallanalyse an Prime-Power-Shellwechseln ist numerischen Sweeps vorzuziehen.

---

## 8. Danach: OX-GEN-B

`r_1` und `c_aI` erst dann einbeziehen, wenn ihre Rolle aus der gemeinsamen Geometrie vorwärts motiviert ist. Der Außenshell darf nicht still mit `c_aI` identifiziert werden.

Parallel: Prime-Power-AR(1)/Martingal-Faktorisierung als eigenständige RH-unabhängige Mathematik verschriftlichen.

---

## 9. Vollständiger Object-X-Pfad

```text
OX-GEN / POS-DIL partial geometry
        |
        | --candidate-input only-->
        v
GENUINE X CANDIDATE ?[O]
        |
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

Keine candidate-input-Kante ist eine Theoremimplikation.

---

## 10. Firewalls

Nicht reaktivieren oder überdehnen:

- arbitrary contractor aus fertiger Weil-Positivität;
- Prime-only Rang-2-Gram ohne Zusatzstruktur;
- matched cutoff/OX-REN;
- cross-prime als Boundary;
- klassische `H^{1/2}`-Deutung des `1/|x-y|`-Kerns;
- POS-DIL-2A als globaler No-Go gegen positive Erweiterungen;
- Außenshellmasse als bereits identifizierter `c_aI`-Block;
- Shell-Positivität als volle Weil-Buchung.

---

## 11. Explizit offen

```text
POS-DIL-2C exact shell booking / renormalization
POS-DIL-2C radius extension
OX-GEN-B
r_1
c_a I in intrinsic geometry
genuine X candidate
exact full Weil-Gram identity
Object-X realization
Weil-criterion scope
RH
R37/G4c [separate]
```
