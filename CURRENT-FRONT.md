# CURRENT FRONT — Objekt X / NULLPOL-CORE

> **Operative Kopfschicht — zuerst lesen.**  
> **Redaktioneller Stand:** 13. September 2026; keine Registry-Promotion.  
> **Kanonischer neuer Audit:** [Nullpol-Reklassifikation](audits/P11_NULLPOLE_STRATEGIC_RECLASSIFICATION_2026-09-13.md).  
> Die OX-GEN-A-/POS-DIL-Audits bleiben mathematisch gültige Quellen, sind aber strategisch zur auxiliary full-class pole-layer route zurückgestuft.

Diese Datei ordnet die Arbeit; sie beweist nichts. Registry und Arbeitsdefinition werden nicht automatisch durch Merge/CI promoviert.

---

## 1. Gesicherte Basis

Fixed-pair Strong Terminal/C6 liegt für jedes feste `0<R<S` im ungeraden P11-Graphraum vor. Die Prime-Power-Seite besitzt die exakte AR(1)/Weil-Tail-Struktur

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}p^{-|j-k|/2},
\qquad T_q^*T_q+uu^*=R_q.
```

Für `0<a<=1` gilt im kanonischen Suzuki-Cutoff-Gauge

```math
Q_{B_a}=G_a^+-c_aI-R_0-R_1.
```

---

## 2. Neuer Schlüsselfund — `E_±` sind die Polfunktionale `✓[M]`

Mit

```math
M(v)(s)=\int_{\mathbb R}v(x)e^{(s-1/2)x}\,dx
```

gilt exakt

```math
\boxed{E_-(v)=M(v)(0),\qquad E_+(v)=M(v)(1).}
```

Damit ist die OX-GEN-A-Rang-2-Ebene nicht irgendein archimedischer Defekt, sondern exakt die Ebene der beiden Polwerte `s=0,1` der expliziten Formel.

Definiere

```math
\mathscr D_{NP}
=\{v\in C_c^\infty(\mathbb R):M(v)(0)=M(v)(1)=0\}.
```

Dann

```math
\boxed{E_+=E_-=0\quad\text{auf }\mathscr D_{NP},}
```

also

```math
\boxed{R_0|_{\mathscr D_{NP}}=0,
\qquad \|\mathcal Ev\|^2=0.}
```

Für komplexe `v` gilt allgemein

```math
R_0(v,v)
=-2\operatorname{Re}\bigl(E_+(v)\overline{E_-(v)}\bigr).
```

---

## 3. Globaler Weil-Scope: Nullpol ist RH-äquivalent `✓[K/M]`

Connes–Consani, Proposition C.1, liefert für jede endliche Menge

```math
F\supset\{0,1\},\qquad F\cap Z=\varnothing
```

eine RH-äquivalente Weil-Vorzeichenbedingung auf kompakt getragenen Testfunktionen mit

```math
\widetilde g(z)=0\qquad(z\in F).
```

Insbesondere ist `F={0,1}` zulässig.

**Folge:** Das Entfernen der beiden Polfunktionale ist auf der **globalen** Weil-Testklasse logisch kostenlos für die RH-Äquivalenz.

### Firewall

Nicht behaupten: Für jedes einzelne feste Fenster `a` sei die Nullpol-Unterklasse bereits für sich RH-äquivalent. Proposition C.1 ist eine globale Testklassenaussage.

---

## 4. Konsequenz für die lokale Normalform

Auf der lokalen Nullpol-Unterklasse gilt im kanonischen Suzuki-Gauge exakt

```math
\boxed{
Q_{B_a}(v)
=G_a^+(v)-c_a\|v\|_2^2-R_1(v,v),
\qquad M(v)(0)=M(v)(1)=0.
}
```

Der gesamte `R_0`-Layer und seine POS-DIL-Begleitmasse verschwinden.

Die PR-#105-Normalform

```math
Q_{B_a}=P_a^{(0)}-c_a^{out}I-R_1
```

bleibt exakt und nützlich auf der vollen lokalen Testklasse, ist für die Nullpol-Hauptroute aber optional.

---

## 5. Strategische Reklassifikation von OX-GEN-A

OX-GEN-A bleibt mathematisch `✓[M]`:

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

**Neue strategische Buchung:**

```text
OX-GEN-A = exakter Pole-layer-X-Kandidatenbaustein,
           auxiliary auf der Nullpol-Hauptroute.
```

Zurückgezogen ist nur die frühere Deutung, dies sei bereits ein notwendiger Object-X-Klassenschnitt. Auf `\mathscr D_{NP}` ist der gesamte Zielterm annihiliert.

---

## 6. Strategische Reklassifikation von POS-DIL

PR #101--#105 bleiben gültig:

```text
#101  Prime-moment Hilbertization
#102  full-class unit-gain No-Go
#103  first exterior Prime shell
#104  shell domination for 0<a<=1
#105  exact cutoff-gauge and positive R_0 absorption
```

Sie bilden künftig die

```text
AUX-POS-DIL / full-class pole-layer route.
```

Sie werden **nicht** als Default-Hauptfront geführt, weil ihr Rang-2-Gegenstand auf der global RH-äquivalenten Nullpolklasse verschwindet.

### Präzisierungen

- Der Block `[[tI,J],[J,tI]]` ist semidefinit genau für `t>=1`, strikt positiv erst für `t>1`; `t=1` ist der entartete Randfall.
- Im Anti-Kovarianz-No-Go bleibt
  ```math
  H=\begin{pmatrix}0&b\\\bar b&0\end{pmatrix},\qquad b\in\mathbb C,
  ```
  also ohne zusätzliche reelle Struktur zwei reelle Freiheitsgrade.
- Die externe Rayleigh-Rechnung lokalisiert die alte Domination-Obstruktion numerisch ausschließlich im geraden Sektor; das ist Zusatzdiagnostik, kein Input für die Nullpolreduktion.

---

## 7. Neue Default-Hauptfront — NULLPOL-CORE / `R_1` + Skalarledger

### Verbindliche Gate-Regel

> Ein neuer Object-X-Hauptfront-Schritt zählt nur, wenn sein Mechanismus nach Einschränkung auf `M(v)(0)=M(v)(1)=0` noch nichttrivial ist.

Ein Satz über einen dort identisch verschwindenden Term kann theorematisch wertvoll sein, zählt aber nur als Nebenstruktur.

### Aktiver Rest

```math
\boxed{
Q_{B_a}|_{NP}
=G_a^+|_{NP}-c_aI-R_1|_{NP}.
}
```

Die nächste Prüfreihenfolge lautet:

1. **NP-R1:** exakten polarisierten Kernel von `R_1` rekonstruieren;
2. Parität, Translation-/Reflexionssymmetrien und Spektral-/Generatorstruktur von `R_1` **auf Nullpol** bestimmen;
3. **NP-SCALAR:** im kanonischen Suzuki-Gauge den Skalarledger analysieren und parallel eine gaugeinvariante Formulierung suchen;
4. **NP-COMMON:** nur vorab definierte Mechanismen testen, die `R_1` und/oder Skalarrest auf `\mathscr D_{NP}` tatsächlich einschränken;
5. erst danach einen genuinen X-Kandidaten formulieren.

---

## 8. Gauge-Firewall

PR #105 zeigt exakt, dass Außen-Prime-Kanäle

```math
c_a\mapsto c_a+b_J
```

gegenbuchen können. Daher ist der nackte Skalarwert ohne Gaugewahl nicht invariant.

Zulässig sind zwei Arbeitsmodi:

- **canonical-Suzuki gauge:** den ursprünglichen Cutoff explizit fixieren und dort `c_aI+R_1` untersuchen;
- **gauge-invariant route:** eine unter den exakten Prime-cutoff-Gauges invariante Reststruktur konstruieren.

Die Nullpolreduktion tötet `R_0`, nicht diese Skalar-/Gaugefrage.

---

## 9. Firewalls

Nicht behaupten:

- OX-GEN-A oder POS-DIL seien mathematisch widerlegt;
- die full-class POS-DIL-Sätze seien nutzlos;
- fixed-`a`-Nullpolpositivität sei bereits RH-äquivalent;
- `c_a` sei ohne Gauge-Fixierung ein intrinsischer Object-X-Skalar;
- `R_1` sei erklärt;
- Object X oder RH seien gelöst.

---

## 10. Status

```text
E_-=M(v)(0), E_+=M(v)(1)                              ✓[M]
R_0 and ||Ev||^2 vanish on null-pole class             ✓[M]
global finite-null Weil criterion                     ✓[K/M] imported
OX-GEN-A mathematics                                   ✓[M]
OX-GEN-A as necessary Object-X class cut               withdrawn
POS-DIL #101-#105 mathematics                          preserved
POS-DIL as default main front                          withdrawn
NULLPOL-CORE gate discipline                           active
R_1 on null-pole                                       ?[O]
gauge-fixed/invariant scalar remainder                 ?[O]
genuine X candidate / full Weil-Gram / Object X / RH   ?[O]
```

PR #91, PR #49 und R37/G4c bleiben separate Nebenfronten. Registry unverändert.
