# P11 / Objekt X — Nullpol-Reklassifikation von OX-GEN-A und POS-DIL

> **Stand:** 13. September 2026  
> **Basis:** `main@1d56684221c5877100157001f75008104abcc800` (PR #105).  
> **Rolle:** theorem-level strategischer Audit; keine Registry-Promotion, kein RH-Resultat.  
> **Quellenstatus:** OX-GEN-/POS-DIL-Identitäten aus dem Repository; externe Gegenprüfung vom 13.09.2026; klassische Nullpol-Reduktion nach Connes–Consani, Proposition C.1.  
> **Kernaussage:** Die OX-GEN-A-/POS-DIL-Mathematik bleibt gültig, ist aber auf einer global RH-äquivalenten Nullpol-Testklasse annihilierbar und daher **kein notwendiger Object-X-Hauptengpass**.

---

## 0. Kurzurteil

Die folgenden Aussagen bleiben unverändert mathematisch gültig:

- OX-GEN-A: gemeinsame zweidimensionale Translation-/Reflexionsstruktur für Prime-Kanäle und `R_0`;
- POS-DIL-1: Prime-moment Hilbertization der Rang-2-Momentmasse;
- POS-DIL-2A: enger unit-gain No-Go auf der vollen lokalen Testklasse;
- POS-DIL-2B/2C: Außen-Prime-Shell, voller Radius `0<a<=1`, exakte cutoff-gauge und positive `R_0`-Absorption.

Neu ist die **zahlentheoretische Identifikation des Rang-2-Quotienten**:

```math
E_-(v)=M(v)(0),
\qquad
E_+(v)=M(v)(1),
```

wobei

```math
M(v)(s)=\int_{\mathbb R}v(x)e^{(s-1/2)x}\,dx.
```

Damit liegt die gesamte `R_0`-/POS-DIL-Rang-2-Struktur auf den beiden Polfunktionalen der expliziten Formel.

Auf der Nullpolklasse

```math
\mathscr D_{\rm NP}
:=\{v\in C_c^\infty(\mathbb R):M(v)(0)=M(v)(1)=0\}
```

gilt exakt

```math
\boxed{E_-(v)=E_+(v)=0,}
```

und daher

```math
\boxed{R_0(v,w)=0,\qquad \|\mathcal Ev\|^2=0
\quad(v,w\in\mathscr D_{\rm NP}).}
```

Connes–Consani, Proposition C.1, zeigt zugleich, dass die **globale** Weil-Vorzeichenbedingung auf einer solchen Nullstellenklasse RH-äquivalent bleibt; sogar jede endliche Zusatzmenge `F superset {0,1}` ist zulässig, sofern `F` keine nichttriviale Zeta-Nullstelle trifft.

**Strategische Konsequenz:** `R_0` muss für einen RH-äquivalenten Object-X-Pfad nicht positiv dilatiert oder absorbiert werden. Es kann durch eine zulässige Testklassenwahl exakt entfernt werden.

---

## 1. Exakte Identifikation der Polfunktionale `✓[M]`

In der additiven Logarithmuskoordinate ist der Mellintransform

```math
M(v)(s)=\int_{\mathbb R}v(x)e^{(s-1/2)x}\,dx.
```

Daher unmittelbar

```math
M(v)(0)=\int v(x)e^{-x/2}\,dx=E_-(v),
```

```math
M(v)(1)=\int v(x)e^{x/2}\,dx=E_+(v).
```

Die Funktionale `E_±` sind also nicht bloß formal verwandte exponentielle Generatoren, sondern exakt die zwei ausgezeichneten Mellinwerte an den Polstellen `s=0,1` der expliziten Formel.

### 1.1 Quellenabgleich

- Yoshidas additive Mellin-Normierung gibt exakt die obigen Werte bei `s=0,1`.
- Bombieris Konturverschiebung isoliert die Beiträge an `s=0,1` als die entsprechenden Mellinwerte.
- Connes–Consani schreiben die globale explizite Formel mit den beiden Polwerten `\tilde f(0),\tilde f(1)` und verwenden ausdrücklich Testfunktionen, die dort verschwinden.

Diese Identifikation ist unabhängig von den POS-DIL-Numeriken.

---

## 2. Nullpol-Annihilation von `R_0` `✓[M]`

OX-GEN-A liefert polarisiert

```math
R_0(v,w)
=-E_+(v)\overline{E_-(w)}
-E_-(v)\overline{E_+(w)}.
```

Somit gilt auf `\mathscr D_{\rm NP}` identisch

```math
\boxed{R_0|_{\mathscr D_{\rm NP}\times\mathscr D_{\rm NP}}=0.}
```

Ebenso verschwindet die POS-DIL-Begleitmasse

```math
\boxed{
\|\mathcal Ev\|^2
=|E_+(v)|^2+|E_-(v)|^2
=0.
}
```

Damit ist nicht nur der indefinite Kreuzterm, sondern auch sein minimaler positiver Companion auf dieser Testklasse exakt Null.

### 2.1 Präzisierung für komplexe Testfunktionen

Für komplexe `v` lautet die quadratische Kurzform

```math
\boxed{
R_0(v,v)
=-2\operatorname{Re}\bigl(E_+(v)\overline{E_-(v)}\bigr).
}
```

Die Kurzschrift `-2E_+(v)E_-(v)` ist nur für reellwertige `v` ohne weitere Konjugationskonvention zulässig.

---

## 3. Importierter Nullpol-Scope des Weil-Kriteriums `✓[K/M]`

Connes–Consani formulieren für jede endliche Menge

```math
F\supset\{0,1\},
\qquad
F\cap Z=\varnothing,
```

eine RH-äquivalente Weil-Vorzeichenbedingung auf

```math
g\in C_c^\infty(\mathbb R_+^*),
\qquad
\widetilde g(z)=0\quad(z\in F).
```

Insbesondere darf man `F={0,1}` wählen.

Damit ist die Nullpolbedingung **global kostenlos im logischen RH-Scope**: Sie entfernt keine notwendige nichttriviale Zeta-Nullstelle und zerstört die RH-Äquivalenz des globalen Weil-Kriteriums nicht.

### 3.1 Wichtige Firewall: global versus fixes Fenster

Aus Proposition C.1 folgt **nicht** automatisch:

```text
für jedes einzelne feste a ist Weil-Positivität auf
D_NP ∩ C_c^∞(-a,a) bereits RH-äquivalent.
```

Die importierte Aussage betrifft die globale kompakt getragene Nullpolklasse. Lokale Fenster bleiben Bausteine/Approximationen dieser globalen Front; eine fixed-`a`-Äquivalenz wird hier nicht behauptet.

---

## 4. Konsequenz für die aktuelle OX-GRAM-Normalform

Vor der optionalen Außen-Shell-Gauge gilt für `0<a<=1`

```math
Q_{B_a}=G_a^+-c_aI-R_0-R_1.
```

Auf der lokalen Nullpol-Unterklasse folgt daher exakt

```math
\boxed{
Q_{B_a}(v)
=G_a^+(v)-c_a\|v\|_2^2-R_1(v,v),
\qquad E_+(v)=E_-(v)=0.
}
```

Die Rang-2-Schicht ist vollständig verschwunden.

Die PR-#105-Normalform

```math
Q_{B_a}=P_a^{(0)}-c_a^{out}I-R_1
```

bleibt ebenfalls exakt, ist für die Nullpolroute aber **optional**: Ihr positiver `R_0`-Absorptionsmechanismus löst einen Term, der auf `\mathscr D_{\rm NP}` bereits identisch Null ist.

---

## 5. Strategische Reklassifikation von OX-GEN-A

### 5.1 Was unverändert bleibt

OX-GEN-A bleibt `✓[M]`:

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

Das ist eine echte gemeinsame Prime-/archimedische Generatoridentität.

### 5.2 Was zurückgestuft wird

Die bisherige strategische Deutung

```text
OX-GEN-A/POS-DIL liefert einen notwendigen Klassenschnitt
auf dem Weg zu Object X
```

wird zurückgezogen.

Begründung: Auf einer global RH-äquivalenten Testklasse ist der gesamte Zielterm annihiliert. Eine Architekturentscheidung, die nur `R_0` erklärt, verkleinert daher die zulässige Object-X-Klasse auf diesem Scope nicht.

**Neue Buchung:**

```text
OX-GEN-A = exakter X-Kandidatenbaustein / Pole-layer identity,
strategisch auxiliary auf der Nullpol-Hauptroute.
```

Kein mathematischer Satz wird widerrufen.

---

## 6. Strategische Reklassifikation von POS-DIL

Die PRs #101--#105 bleiben als korrekte Mathematik bestehen:

```text
POS-DIL-1        Prime-moment Hilbertization
POS-DIL-2A       enger full-class unit-gain No-Go
POS-DIL-2B       erster äußerer Prime-Shell
POS-DIL-2C-R     Radiusdomination 0<a<=1
POS-DIL-2C-B     exakte Shell-Gauge und positive R_0-Absorption
```

Sie bilden künftig eine **auxiliary full-class pole-layer route**.

Sie sind nützlich für:

- Verständnis der vollen unbeschränkten Testklasse;
- exakte Prime-cutoff-Gauges;
- Modellierung positiver Erweiterungen;
- mögliche spätere Rekonstruktion einer vollständigen Geometrie ohne Nullpolrestriktion.

Sie sind aber **nicht mehr Default-Hauptfront**, weil der von ihnen behandelte Rang-2-Term auf `\mathscr D_{\rm NP}` verschwindet.

---

## 7. Numerische POS-DIL-Befunde — präziser Scope

Der externe Arb-Rayleighlauf auf der Dirichletbasis bis `N=14` reproduziert

```text
a=0.5   C_14 = 1.1688940156130010...
a=0.8   C_14 = 1.3185442177485860...
a=1.0   C_14 = 0.92691807750030217...
```

Damit ist die ursprüngliche enge Domination durch `G_a^+` bei `a=0.5` und `a=0.8` bereits endlichdimensional ausgeschlossen; `a=1` bleibt aus diesem Test global offen.

Eine unabhängige Sektorauswertung lokalisiert die Obstruktion numerisch vollständig im **geraden Sektor**; der ungerade Sektor liegt mit großem Abstand unter der Schwelle.

Diese Numerik ist konsistent mit der Struktur von `R_0`, wird aber **nicht** für den Nullpol-Schluss benötigt.

### 7.1 Präzisierungen der POS-DIL-Algebra

- Für
  ```math
  \begin{pmatrix}tI&J\\J&tI\end{pmatrix}
  ```
  gilt Semidefinitheit genau für `t>=1`, strikte Positivität genau für `t>1`; `t=1` ist der entartete Randfall.
- Aus
  ```math
  D_n^*HD_n=-\lambda_n^2H
  ```
  folgt
  ```math
  H=\begin{pmatrix}0&b\\\bar b&0\end{pmatrix},
  \qquad b\in\mathbb C.
  ```
  Es bleiben also ohne zusätzliche reelle Struktur zwei reelle Freiheitsgrade.

---

## 8. Neue Default-Hauptfront: NULLPOL-CORE

Definiere als strategischen Filter:

> **NULLPOL-CORE-Regel.** Ein neuer Object-X-Hauptfront-Schritt zählt nur dann als Klassenschnitt oder Konstruktionsfortschritt, wenn sein Mechanismus nach Einschränkung auf die global RH-äquivalente Nullpolklasse `\mathscr D_{\rm NP}` noch nichttrivial ist.

Ein Mechanismus, der ausschließlich einen auf `\mathscr D_{\rm NP}` verschwindenden Term erklärt, ist theorematisch interessant, aber strategisch auxiliary.

### 8.1 Aktiver Rest

Im kanonischen Suzuki-Cutoff-Gauge lautet der lokale Rest auf Nullpol:

```math
\boxed{
Q_{B_a}|_{\rm NP}
=G_a^+|_{\rm NP}
-c_aI
-R_1|_{\rm NP}.
}
```

Damit sind die Default-Gates:

1. **NP-R1:** exakte Generator-/Kernel-/Paritätsstruktur von `R_1` auf Nullpol bestimmen;
2. **NP-SCALAR:** den Skalarledger `c_aI` in einem festgelegten Gauge bzw. eine gaugeinvariante Restgröße isolieren;
3. **NP-COMMON:** prüfen, ob `R_1` und Skalarrest aus einem gemeinsamen Prime-/archimedischen Mechanismus entstehen;
4. nur Mechanismen weiterverfolgen, die auf `\mathscr D_{\rm NP}` tatsächlich wirken;
5. danach Rückbindung an den globalen Nullpol-Weil-Scope und erst dann an Object X/RH.

---

## 9. Gauge-Firewall für den Skalar

PR #105 hat korrekt gezeigt, dass ein isolierter Skalarwert unter Außen-Prime-cutoff-Gauge verschoben werden kann:

```math
c_a\mapsto c_a+b_J.
```

Daher darf die neue Front nicht einfach behaupten, der nackte Zahlenwert `c_a` sei ohne Gaugewahl ein kanonisches Objekt.

Operativ gibt es zwei zulässige Wege:

- **canonical-Suzuki gauge:** den ursprünglichen lokalen Cutoff explizit fixieren und dort `c_a` untersuchen;
- **gauge-invariant route:** eine Kombination aus Skalarledger und Featureenergie konstruieren, die unter den exakten Prime-cutoff-Gauges invariant ist.

Die Nullpolreduktion entfernt `R_0`, aber **nicht** diese Gaugefrage.

---

## 10. Status nach Reklassifikation

```text
E_-=M(v)(0), E_+=M(v)(1)                              ✓[M]
R_0 and ||Ev||^2 vanish on null-pole class             ✓[M]
global RH-equivalence on finite-null class             ✓[K/M] imported (Connes–Consani Prop. C.1)
OX-GEN-A algebra                                        ✓[M]
OX-GEN-A as necessary Object-X class cut               withdrawn
POS-DIL #101-#105 mathematics                           preserved
POS-DIL as default Object-X main front                 withdrawn
NULLPOL-CORE gate discipline                            active
R_1 on null-pole                                        ?[O]
gauge-fixed/invariant scalar remainder                  ?[O]
full Weil-Gram identity / Object X / RH                 ?[O]
```

---

## 11. Governance / Provenienz

- Der externe Reviewerbericht prüfte zunächst den älteren Snapshot `main@48d1656c`; seine algebraischen/source-level Aussagen wurden gegen die aktuelle Mathematik und Primärquellen gegengeprüft.
- Die Rayleigh-Skripte dienen als numerische Zusatzprovenienz, **nicht** als current-head `independent GREEN (certificate)`.
- Keine Registry-Promotion aus diesem Audit.
- Keine Aussage dieses Audits widerruft PR #101--#105 mathematisch.
- Keine RH-Folgerung wird aus einer lokalen fixed-`a`-Nullpolklasse behauptet.

---

## 12. Endurteil

Der neue Befund ist eine **strategische Korrektur, kein mathematischer Rückschritt**:

```text
R_0/OX-GEN-A/POS-DIL
    = exakte und wertvolle Pole-layer geometry
    = auf global RH-äquivalenter Nullpolklasse annihilierbar
    => auxiliary, nicht Default-Hauptengpass.
```

Die belastbare Hauptfront lautet jetzt:

```math
\boxed{
\text{NULLPOL-CORE: positive Prime/log|D| geometry}
\; - \; \text{scalar ledger}
\; - \; R_1.
}
```

Der nächste Gate muss vorab die Frage bestehen:

> **Wirkt und schneidet dieser Mechanismus die zulässige Geometrie auch nach `M(v)(0)=M(v)(1)=0`?**

Falls nein, ist er Nebenstruktur und kein Object-X-Hauptfront-Fortschritt.
