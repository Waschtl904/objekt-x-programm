# Aktueller Stand — Objekt X / NULLPOL-CORE

> **Stand:** 13. September 2026; Registry unverändert.  
> Details: [CURRENT-FRONT](../CURRENT-FRONT.md), [Nullpol-Audit](../audits/P11_NULLPOLE_STRATEGIC_RECLASSIFICATION_2026-09-13.md), [Roadmap](FORSCHUNGS_ROADMAP_AKTUELL.md), [DAG](DAG.md).

## 1. Basis

Prime-Power-AR(1), fixed-pair Strong Terminal/C6 und die lokale Normalform bleiben verfügbar. Für `0<a<=1` im kanonischen Suzuki-Gauge:

```math
Q_{B_a}=G_a^+-c_aI-R_0-R_1.
```

## 2. Nullpol-Schlüsselidentität `✓[M]`

Mit

```math
M(v)(s)=\int_{\mathbb R}v(x)e^{(s-1/2)x}\,dx
```

gilt

```math
\boxed{E_-(v)=M(v)(0),\qquad E_+(v)=M(v)(1).}
```

Auf

```math
\mathscr D_{NP}=\{v:M(v)(0)=M(v)(1)=0\}
```

verschwinden daher exakt

```math
R_0(v,w),\qquad \|\mathcal Ev\|^2.
```

Connes–Consani, Proposition C.1, liefert eine **globale RH-äquivalente** Weil-Testklasse mit diesen Nullbedingungen; keine fixed-`a`-Äquivalenz wird daraus behauptet.

## 3. Strategische Korrektur

OX-GEN-A bleibt `✓[M]`, wird aber als exakte **Pole-layer geometry** reklassifiziert. Die frühere Deutung als notwendiger Object-X-Klassenschnitt ist zurückgezogen.

Die mathematischen Resultate PR #101--#105 bleiben vollständig gültig und bilden nun die auxiliary full-class POS-DIL-Route. Sie sind nicht mehr Default-Hauptfront.

## 4. Nullpol-Normalform

Auf der lokalen Nullpol-Unterklasse gilt exakt

```math
\boxed{
Q_{B_a}(v)
=G_a^+(v)-c_a\|v\|_2^2-R_1(v,v).
}
```

Damit verbleiben als aktive nichtannihilierbare Blöcke:

```text
positive Prime/log|D| geometry
minus scalar ledger
minus R_1.
```

## 5. Neue Default-Hauptfrage

**NULLPOL-CORE / `R_1` + Skalarledger `?[O]`.**

Nächste Schritte:

1. exakten polarisierten `R_1`-Kernel rekonstruieren;
2. `R_1`-Parität und Generator-/Translationsstruktur auf Nullpol bestimmen;
3. canonical-Suzuki-Gauge und gaugeinvariante Skalarformulierung parallel prüfen;
4. nur Mechanismen als Hauptfortschritt zählen, die nach `M(v)(0)=M(v)(1)=0` nichttrivial bleiben.

## 6. POS-DIL-Präzisierungen

- Für komplexe `v`: `R_0(v,v)=-2 Re(E_+(v) overline(E_-(v)))`.
- Der minimale Companion-Block ist bei `t=1` semidefinit/entartet; strikt positiv erst für `t>1`.
- Im Anti-Kovarianz-No-Go bleibt `b in C`, also zwei reelle Parameter.
- Die externe Rayleigh-Diagnostik lokalisiert die alte Domination-Obstruktion numerisch im geraden Sektor.

## 7. Offen

```text
NP-R1
NP-SCALAR / gauge-invariant scalar remainder
NP-COMMON
genuine X candidate
exact full Weil-Gram identity
Object-X realization
Weil-criterion scope
RH
```
