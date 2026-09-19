# X-C0 — Correction: Critical-half amplitude normalization in the endpoint colligation

**Datum:** 16. September 2026  
**Korrigiert:** `X_C0_OU_ENDPOINT_COLLIGATION_AND_COMPACT_CRITICAL_RELATIVE_OUTPUT_2026-09-16.md`  
**Registry:** unverändert.  
**Nonclaim:** keine neue Weil-Identitaet; dies ist eine Normalisierungs-/Scope-Korrektur.

---

## 0. Korrektur

Im vorangehenden Endpoint-Colligation-Audit wurde der Faktor

```math
e^{L/2}
```

faelschlich als **Critical-half-Amplitudenfaktor** bezeichnet.

Das sichere Root-Quadratgewicht ist

```math
a\sim e^{-L},
```

waehrend das Weilgewicht

```math
w\sim e^{-L/2}
```

ist. Daher ist der Critical-half-Lift

```math
\boxed{e^{L/2}\text{ auf Energie-/Masssebene}}
```

aber nur

```math
\boxed{e^{L/4}\text{ auf Amplitudenebene}.}
```

Die **korrekte** Critical-half-Amplitudenabbildung fuer die vor der Verstaerkung gebildete OU-Endpunktdifferenz lautet somit

```math
\boxed{
C^{crit}_{p,L}
:=e^{L/4}(e^{-Ph_p}-e^{-PL}).
}
```

Auf dem Grundmodus `P=1/2`:

```math
\boxed{
e^{L/4}(e^{-h/2}-e^{-L/2})
=e^{-L/4}(e^{-(h-L)/2}-1).}
```

Der im frueheren Audit untersuchte Operator

```math
e^{L/2}(e^{-Ph_p}-e^{-PL})
```

ist daher ein **staerker uebergewichteter Stress-Test**, nicht die physikalisch erforderliche Critical-half-Amplitudennormierung.

Da sogar dieser staerkere Stress-Test auf den dort verwendeten sicheren Root-Massenzellen beschraenkt/kompakt ist, bleibt die korrekte `e^(L/4)`-Aussage erst recht gueltig.

---

# 1. Korrekte ground-mode compactness

Fuer `L in I_p`, `h_p=log p`, setze

```math
\chi_{crit}(h_p,L)
:=e^{L/4}(e^{-h_p/2}-e^{-L/2}).
```

Dann

```math
\chi_{crit}(h,L)
=e^{-L/4}(e^{-(h-L)/2}-1),
```

also fuer

```math
\delta_p=\sup_{L\in I_p}|L-h_p|
```

```math
\boxed{
|\chi_{crit}(h_p,L)|
\le e^{-L/4}(e^{\delta_p/2}-1).
}
```

Insbesondere geht der Zelloperator noch schneller gegen null als der im vorangehenden Audit verwendete Overlift.

Damit ist die korrekte Abbildung

```math
\mathcal C_0^{crit}:\ell^2(a_p)\to L^2(dL)
```

beschraenkt und kompakt.

---

# 2. Korrekte RP2-operatorwertige Version

Setze

```math
\boxed{
C_{p,L}^{crit}
=e^{L/4}(e^{-Ph_p}-e^{-PL}),
\qquad P\ge1/2.
}
```

Fuer ein Spektralgewicht `mu>=1/2`, `m=min(L,h_p)` und `delta=|L-h_p|` gilt

```math
|e^{-\mu h_p}-e^{-\mu L}|
\le\mu\delta e^{-\mu m}.
```

Daher

```math
\begin{aligned}
e^{L/4}|e^{-\mu h_p}-e^{-\mu L}|
&\le
\mu\delta
 e^{-(\mu-1/4)m}
 e^{\delta/4}.
\end{aligned}
```

Fuer grosse Zellen ist die rechte Seite gleichmaessig in `mu>=1/2` durch `C delta_p e^{-m/4}` beschraenkt und geht gegen null.

Folglich bleibt

```math
\boxed{
\mathcal C_{RP2}^{crit}:
\ell^2(a_p;L^2(RP^2))
\to L^2(dL;L^2(RP^2))
}
```

beschraenkt und kompakt.

---

# 3. Positive Shorting energy

Die coefficient-free positive relative OU-Energie

```math
R_P(h,L)
=
2P[2-e^{-2Ph}-e^{-2PL}]^{-1}(e^{-Ph}-e^{-PL})^2
\succeq0
```

bleibt unveraendert.

Auf **Energieebene** ist der korrekte Critical-half-Lift daher

```math
\boxed{e^{L/2}R_P(h,L),}
```

bzw. fuer einen square-root output

```math
\boxed{e^{L/4}R_P(h,L)^{1/2}.}
```

Die fruehere Aussage mit `e^(L/2) R_P^(1/2)` war over-weighted und darf nicht als exakte Weil-Normalisierung zitiert werden.

---

# 4. Zusaetzliche Scope-Firewall: sichere Root-Masse vs. voller Prime-Readout

Die Compactness-Aussagen leben auf

```math
\ell^2(a_p),
\qquad
a_p=\frac{\log p}{p-1},
```

also auf der **sicheren Root-Quadratmassenskala**.

Sie beweisen noch **nicht**, dass der fertige X-C0 Prime-/Euler-Readout mit seiner vollstaendigen Weil-Normalisierung durch denselben Operator kontrolliert wird.

Insbesondere:

```text
bounded/compact Critical lift AFTER root-mass cancellation       ✓[K/M]
identification with complete Prime-cell sampling norm            ?[O]
identity with J_Delta / Gamma_a / centered Weil                  ?[O]
```

Ein spaeterer C1-Kandidat muss diese Typ-/Massfrage explizit loesen; die Kompaktheit allein darf nicht als Weil-Identitaet hochgestuft werden.

---

# 5. Status der vorangehenden Resultate

Unveraendert korrekt:

```text
OU Root/stop-endpoint 2-port precision             ✓[M]
positive common-endpoint Shorting                  ✓[M]
relative energy R_P(h,L)                           ✓[M]
```

Korrigiert:

```text
Critical-half AMPLITUDE factor                     e^(L/4), not e^(L/2)
e^(L/2) amplitude map                              stronger stress-test only
```

Weiter offen:

```text
exact coefficient identity with X-C0 / Weil       ?[O]
Prime-2 quartet for final C1 readout               ?[O]
Object X / NP-GAP / RH                             ?[O]
```

No Registry change.
