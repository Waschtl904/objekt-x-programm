# Objekt X — NEXT GATE

**Stand:** 16. September 2026  
**Gate-ID:** `RELATIVE-COLLIGATION / CANCEL-FIRST`  
**Status:** `?[O]`  
**Branch:** `research/critical-half-green-tree-bridge-2026-09-13`  
**PR:** #116  
**Memory-layer parent:** `b3a74a7497d9c92c4dcb289d72a395b341deb727`  
**Canonical memory-layer commit:** see the Git commit that contains this file; do not replace by a floating branch assumption.

> Dies ist die einzige aktuelle Hauptfront dieses Forschungsastes. Keine neue Proxy-Suche, kein weiterer Methodenwechsel und keine Wiedereroeffnung gesperrter Klassen, solange dieser Gate nicht PASS oder FAIL erhalten hat.

---

## 0. Ziel in einem Satz

Konstruiere **vorwaerts**, coefficient-free und ohne Weil-Positivitaet/RH als Input eine positive bzw. konservative relative Kolligation, die Prime- und Continuum-Rootzustaende zuerst auf der sicheren `Lambda(n)/n`-Skala intern ausloescht und erst den endlichen relativen Boundary-Output durch den Critical-half-Port auf die Weil-Skala hebt.

Leitregel:

```text
RELATIVE CANCELLATION FIRST.
CRITICAL-HALF OUTPUT SECOND.
```

---

# 1. Fest vorgegebene Daten — nicht fitten

## 1.1 Lokale Euler-/Gamma-Zellen

Fuer `h>0`, `q=e^{-h/2}`:

```math
A_h
=\sum_{k\ge1}h e^{-kh/2}K_{kh}^*K_{kh},
```

```math
A_0
=\int_0^\infty e^{-t/2}K_t^*K_tdt
=4D^2(D^2+1/4)^{-1}.
```

Bereits bewiesen:

```math
0\preceq A_h\preceq A_0.
```

Daher existiert ein kanonischer lokaler Schur-Faktor

```math
b_h=\Phi_h b_0,
\qquad \|\Phi_h\|_{H^\infty(\Re s>0)}\le1.
```

Diese lokale Metrik ist fix.

## 1.2 Prime-Root-Massen

Prime-Power-Tiefen und sichere Root-Masse:

```math
h_j=\log n_j,
\qquad
a_j=\frac{\Lambda(n_j)}{n_j}.
```

## 1.3 Monotone Transportzellen

```math
s_0=\gamma,
\qquad
s_j=\gamma+\sum_{i\le j}a_i,
```

```math
I_0=[0,\gamma),
\qquad
I_j=[s_{j-1},s_j),
\qquad |I_j|=a_j.
```

Der Transport `a_j delta_{h_j} -> 1_{I_j}(L)dL` ist fix und positiv.

Bereits bewiesen:

```math
\sum_j a_j\sup_{L\in I_j}|L-h_j|<\infty.
```

## 1.4 Relative Root-Transferfunktion

Fuer `Re s>=0` konvergiert direkt und absolut:

```math
\gamma-\int_0^\gamma e^{-sL}dL
+
\sum_j\left[
 a_je^{-sh_j}-\int_{I_j}e^{-sL}dL
\right].
```

Dies ist die sichere, bereits konstruierte relative Stufe.

## 1.5 Critical-half Port

Der endliche relative Output ist mit

```math
J_\Delta(L)
=e^{L/2}\left(L-\gamma-\sum_{\log n<L}\frac{\Lambda(n)}n\right)
```

und

```math
D_+=\partial_x+1/2
```

gekoppelt.

Die beiden Seiten Prime/Continuum duerfen **nicht getrennt** durch `e^{L/2}` verstaerkt werden.

## 1.6 Hoehere Gamma-Reservoirs

```math
\mu_m=2m+1/2,\qquad m\ge1,
```

mit den bereits fixierten stabilen first-order Filterzustaenden. Diese sind positive Reservoirs, keine freien Fit-Parameter.

---

# 2. Minimale Kandidatenklasse

Der erste Kandidat soll bewusst eng sein.

Pro Transportzelle `I_j` verwende einen `2x2`-relativen Zustand

```text
[ discrete prime/root state ]
[ matched continuum cell   ]
```

mit folgenden Regeln:

1. Diagonalmetriken stammen ausschliesslich aus den bereits bewiesenen lokalen OU/Gamma-Zellen.
2. Die Prime-/Continuum-Massen sind exakt `a_j`; keine Gewichtsveraenderung.
3. Die Lagekopplung ist ausschliesslich durch `h_j` und `I_j` bestimmt.
4. Cross-Terme muessen aus der kanonischen overlap-cone / stopped-OU incidence folgen.
5. Kein Koeffizient darf anhand des Weil-Zielwertes, des Prime-2-Zeugen oder von Zeta-Nullstellen angepasst werden.
6. Vor Critical-half-Ausgabe muss der gemeinsame divergente Modus intern ausgeloescht sein.
7. Der ausgegebene relative Boundary-State muss in einen echten Hilbertraum fallen.

Die Kandidatenklasse darf spaeter vergroessert werden, aber nur nach einem expliziten FAIL dieser minimalen Klasse.

---

# 3. Was als PASS zaehlt

Ein PASS benoetigt **alle** folgenden Punkte:

### P1 — Positiver Parent

Expliziter Hilbert-/Storage-Raum `H_rel` und positive Energie

```math
E(z)=\langle Pz,z\rangle,\qquad P\succeq0,
```

vor jeder Verwendung von RH/Weil-Positivitaet.

### P2 — Coefficient-free coupling

Alle Kopplungen folgen aus P11-/OU-/Transport-/Gamma-Daten; keine nachtraegliche Kalibration.

### P3 — Relative cancellation is internal

Der unbeschraenkte gemeinsame Critical-half-Hauptteil darf nicht als Differenz zweier separat divergenter Outputnormen definiert werden. Die Ausloeschung muss als interner State-/Boundary-Mechanismus vor der Outputverstarkung stattfinden.

### P4 — Exact Prime-2 mixed calibration

Auf dem bereits fixierten `R=1` PR-#91-Zeugen muss exakt die bekannte gemischte Weil-Korrektur reproduziert werden:

```math
B_W(a,b)-c_\Gamma(a,b)=-\frac{\log2}{\sqrt2}.
```

Kein numerischer Naeherungstreffer genuegt.

### P5 — Full local identities preserved

Der Kandidat darf S1–S13 aus `HARD_AUDIT_SURVIVOR_STATE.md` nicht verletzen.

### P6 — Noncircular right-half-plane storage

Erst wenn P1–P5 vorwaerts stehen, darf untersucht werden, ob die resultierende Transferfunktion die bekannte Lagarias-/`xi'/xi`-Positive-Real-Struktur liefert.

Ein PASS waere der erste substanzielle Object-X-Mechanismus dieses Astes.

---

# 4. Was als FAIL zaehlt

Die minimale Klasse ist FAIL, sobald einer dieser Punkte rigoros gezeigt wird:

1. Positivitaet des Parent-Blocks erzwingt eine Prime-2-Kalibration, die vom exakten Ziel getrennt ist.
2. Die interne relative Ausloeschung laesst notwendigerweise einen unbeschraenkten Critical-half-Output zurueck.
3. Der kanonische Cross-Block ist auf dem Root-Transportraum nicht closable/beschraenkt in der benoetigten Energy-Topologie.
4. Ein Rang-/Totalitaetsargument reduziert den relativen Output auf null oder auf eine bereits gesperrte Klasse.
5. Die Konstruktion ist algebraisch nur eine Rueckdefinition aus der Weilform/`xi'/xi` und daher zirkulaer.

Bei FAIL:

```text
close RELATIVE-COLLIGATION minimal class;
keep all survivor identities;
do not immediately invent fitted coefficients.
```

---

# 5. Erster konkreter Arbeitszug

Nicht global starten. Zuerst `R=1`, Prime-2-Witness.

### Schritt A — Transportzellen im endlichen Witness-Scope

Bestimme exakt, welche `I_j` und Prime-Power-Tiefen durch den Witness ueberhaupt aktiv werden.

### Schritt B — Kanonischen 2x2 Cross-Block ableiten

Nur aus:

```text
- equal-mass transport I_j,
- local Schur factor Phi_h,
- stopped OU boundary mode,
- overlap-cone incidence,
- fixed D_+=partial+1/2 port.
```

Keine freien Skalare.

### Schritt C — Mixed pairing symbolisch ausrechnen

Berechne die induced pairing `Q_rel(a,b)` exakt.

### Schritt D — Destruktiver Vergleich

Vergleiche mit

```math
-\log2/\sqrt2.
```

- exakt gleich -> Kandidatenklasse ueberlebt und wird auf weitere Witnesses/radii erweitert;
- exakt getrennt -> Class No-Go dokumentieren;
- Ausdruck nicht wohldefiniert/unbeschraenkt -> Functional-analytic No-Go dokumentieren.

---

# 6. Governance

- PR #116 bleibt Draft.
- Keine Registry-Promotion durch einen einzelnen lokalen PASS.
- Jede neue Identitaet bekommt Primaeraudit + Scope + Nonclaim.
- Jeder No-Go wird in `WHAT_NOT_TO_REOPEN.md` aufgenommen.
- `RESEARCH_STATE.yaml` muss bei Frontverschiebung aktualisiert werden.
- `HARD_AUDIT_SURVIVOR_STATE.md` bleibt die menschliche kanonische Einstiegsebene.

---

# 7. Erfolgskriterium fuer den naechsten Agenten

Ein neuer Agent soll nach Lesen dieser Datei **nicht** fragen: „Welche Methode probieren wir als Naechstes?“

Er soll genau eine Frage bearbeiten:

```text
Can the canonical equal-mass Prime/continuum transport cells support a
positive 2x2 relative colligation which cancels before the Critical-half lift
and reproduces the exact R=1 Prime-2 mixed Weil pairing without fitted data?
```

Alles andere ist vorerst Nebenfront.
