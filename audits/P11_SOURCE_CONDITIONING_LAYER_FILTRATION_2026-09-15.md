# P11 Audit — source-conditioning layer filtration and exact activation radii

**Datum:** 15. September 2026  
**Basis:** P11 source-dependent martingale projection and the typed COMMON-JUMP/Tree bridge.  
**Rolle:** exakte Radiusfiltration der P11-Innovationsschichten.  
**Registry:** unveraendert.  
**Nonclaim:** kein globales Object X, kein NP-GAP-/RH-Beweis, keine Publikationsneuheit.

---

## 0. Kurzurteil

Die source-dependent finite-adische Konditionierung besitzt eine exakte, bislang nicht ausgeschriebene Radiusfiltration.

Fixiere einen Prime-Power-Kanal `p^k` und eine Martingalinnovation `ell` mit `1<=ell<=k`. Dann ist die `ell`-te Innovationskomponente des P11-Restoperators genau dann als nichttrivialer `L^2`-Operator vorhanden, wenn

```math
\boxed{
R>\frac{k+\ell}{4}\log p.
}
```

Die Innovationen eines festen `p^k`-Kanals schalten sich daher nacheinander bei

```math
\frac{k+1}{4}\log p,
\frac{k+2}{4}\log p,
\ldots,
\frac{2k}{4}\log p
```

ein.

Der letzte Aktivierungsradius

```math
R=\frac{k}{2}\log p
```

ist zugleich

1. der Beginn eines positiven-massigen Quellbereichs, auf dem der vollstaendige `p^k`-Mark erhalten bleibt;
2. der Beginn echter zweiseitiger Shiftueberlappung;
3. exakt der P11-Hubcutoff `p^k<=e^{2R}`;
4. exakt der kanonische COMMON-JUMP-Prime-Power-Cutoff `log(p^k)<=2R`.

Somit werden partielle same-prime Boundary-Innovationen **vor** der globalen Root-/Cross-prime-Kopplung sichtbar; der Root wird erst bei voller Interaktionsreife des Kanals zugeschaltet.

Status:

```text
nested source projections Q_R(u)                         ✓[M]
rank-one positive increments per new innovation level     ✓[M]
exact ell-layer activation radius                         ✓[M]
hub cutoff = final innovation/full-overlap cutoff         ✓[M]
hub cutoff = COMMON-JUMP prime-power cutoff               ✓[M]
source conditioning implements a canonical radius filter   ✓[M]
this filtration alone yields Weil positivity               ?[O]
Feshbach transport preserves the needed direct system      ?[O]
```

---

# 1. Verschachtelte Radiusprojektionen

P11 definiert fuer `u in (-R,R)`

```math
J_{p,R}(u)
=\max\left\{0,
\left\lfloor\frac{2(R-|u|)_+}{\log p}\right\rfloor
\right\}
```

und

```math
Q_R(u)\psi_{p,j}
=1_{\{j<J_{p,R}(u)\}}\psi_{p,j}.
```

Sei `0<R<S` und `|u|<R`. Dann

```math
J_{p,S}(u)\ge J_{p,R}(u).
```

Da beide Operatoren Koordinatenprojektionen auf Anfangsabschnitte derselben Martingalbasis sind,

```math
\boxed{
Q_R(u)Q_S(u)=Q_S(u)Q_R(u)=Q_R(u).
}
```

Also

```math
\boxed{Q_R(u)\preceq Q_S(u).}
```

Die finite-adische source conditioning bildet auf jedem alten Quellpunkt ein kanonisch verschachteltes System orthogonaler Projektionen.

---

# 2. Jeder neue Martingallevel ist ein positiver Rang-eins-Gramzuwachs

Die normalisierten Prime-Power-Marks sind

```math
\eta_{p,k}
=\sqrt{p-1}\sum_{a=0}^{k-1}p^{(a-k)/2}\psi_{p,a}.
```

Wenn beim Radiuswachstum genau der Level `ell` neu freigeschaltet wird, also die Basisrichtung `psi_{p,ell-1}`, dann ist ihr Koeffizient im Kanal `k`

```math
(v_{p,\ell})_k
=\sqrt{p-1}\,p^{(\ell-1-k)/2}1_{\{k\ge\ell\}}.
```

Damit ist der Zuwachs der same-prime Mark-Grammatrix exakt

```math
\boxed{
\Delta G_{p,\ell}
=v_{p,\ell}v_{p,\ell}^*\succeq0.
}
```

Fuer einen Sprung von Tiefe `J_1` auf `J_2` folgt

```math
\boxed{
G_{p,J_2}-G_{p,J_1}
=\sum_{\ell=J_1+1}^{J_2}v_{p,\ell}v_{p,\ell}^*\succeq0.
}
```

Die source-conditioned Innovationsgeometrie waechst somit radiusweise in expliziten positiven Rang-eins-Schichten.

---

# 3. Wann ist die ell-te Innovation eines p^k-Kanals wirklich raeumlich aktiv?

Setze

```math
h=\log p,
\qquad
t=kh.
```

Die `ell`-te Innovationsrichtung `psi_{p,ell-1}` wird von `Q_R(u)` genau dann behalten, wenn

```math
\ell\le J_{p,R}(u),
```

also

```math
\boxed{|u|\le R-\frac{\ell h}{2}.}
```

Der raeumliche Jump

```math
D_{kh}E_Rf(u)
=E_Rf(u+kh/2)-E_Rf(u-kh/2)
```

kann an einem solchen `u` nur dann nichttrivial sein, wenn mindestens einer der beiden verschobenen Punkte im Quellfenster `(-R,R)` liegt.

Wir fragen daher, wann die Intervalle

```math
[-R+\ell h/2,\ R-\ell h/2]
```

und

```math
(-R-kh/2,\ R-kh/2)
```

(bzw. symmetrisch der andere Shift) positive Ueberlappungslaenge besitzen.

Die Summe der Halbbreiten ist

```math
R+(R-\ell h/2)=2R-\ell h/2,
```

waehrend der Abstand der Mittelpunkte `kh/2` ist. Positive Ueberlappung ist daher aequivalent zu

```math
\frac{kh}{2}<2R-\frac{\ell h}{2}.
```

Also

```math
\boxed{
R>\frac{k+\ell}{4}h
=\frac{k+\ell}{4}\log p.
}
```

Bei Gleichheit beruehren sich die Intervalle nur in einem Randpunkt; als `L^2`-Operator entsteht dort noch kein positiver-massiger Beitrag. Fuer Cutoff-Formeln ist die Unterscheidung an diesem Nullmengenrand unschaedlich, fuer den Aktivierungssatz wird deshalb strikt `>` verwendet.

---

# 4. Exakte Aktivierungsleiter eines festen Prime-Power-Kanals

Fuer `ell=1,...,k` entstehen die Schwellen

```math
R_{k,\ell}
=\frac{k+\ell}{4}\log p.
```

Damit

```text
ell=1:     (k+1) log p / 4     erste finite-adische Innovation sichtbar
ell=2:     (k+2) log p / 4
...
ell=k:      k log p / 2        letzte Innovation / voller Mark moeglich
```

Zwischen zwei aufeinanderfolgenden Schwellen ist die maximale source-conditioned Innovationstiefe des `p^k`-Kanals konstant.

### Verfeinerung der groben P11-Supportschranke

Die bisherige notwendige Grobschranke fuer einen Restkanal war

```math
p^k\le e^{4R}.
```

Fuer einen **tatsaechlich nichttrivialen** Restbeitrag wird mindestens `ell=1` benoetigt. Daher gilt strenger (bis auf den Nullmengenrand)

```math
\boxed{
p^{k+1}<e^{4R}.}
```

Dies ist eine Verfeinerung der effektiven Restkanal-Supportbedingung, keine Aenderung der P11-Definition.

---

# 5. Der letzte Innovationseinschub ist genau der Full-overlap-Cutoff

Fuer `ell=k` lautet die Schwelle

```math
R>\frac{k}{2}\log p.
```

Dies ist exakt die Bedingung, dass es einen positiven-massigen zentralen Quellbereich gibt mit

```math
|u|+\frac{k}{2}\log p<R,
```

also beide Shiftpunkte

```math
u\pm\frac{k}{2}\log p
```

gleichzeitig im Fenster liegen.

Auf diesem zentralen Bereich ist der vollstaendige Mark `eta_{p,k}` erhalten.

Damit fallen zusammen:

```math
\boxed{
\text{letzte Innovation}
\Longleftrightarrow
\text{full overlap}
\Longleftrightarrow
k\log p<2R.
}
```

---

# 6. Der P11-Hub schaltet genau am COMMON-JUMP-Cutoff

Der originale P11-Hub lautet

```math
H_R
=P_R\sum_{p^k\le e^{2R}}
\sqrt{\log p}\,p^{-3k/4}D_{k\log p}E_R.
```

Sein Kanal `p^k` ist somit genau dann vorhanden, wenn

```math
\boxed{k\log p\le2R.}
```

Dies ist derselbe Prime-Power-Cutoff wie im kanonischen finite-window COMMON-JUMP-Ledger.

Bis auf den Nullmengen-Grenzfall ist es zugleich exakt die letzte Schwelle `R_{k,k}` aus §5.

Interpretation:

> Die gemeinsame Root-/Cross-prime-Kopplung wird nicht beim ersten einseitigen Auftauchen eines tiefen Prime-Power-Kanals zugeschaltet. Sie erscheint erst dann, wenn derselbe Kanal erstmals einen echten zweiseitigen Innenbereich und seine volle Innovationskette besitzen kann.

---

# 7. Vor dem Hub: partial same-prime boundary geometry

Fuer `k>=2` koennen die ersten Innovationslevel bereits bei

```math
R>\frac{k+1}{4}\log p
```

auftreten, waehrend

```math
R<\frac{k}{2}\log p
```

noch keinen Hubterm fuer `p^k` erlaubt.

In diesem Regime ist der Kanal nur ueber source-conditioned same-prime Innovationsdaten gekoppelt; eine Cross-prime Root-Korrelation des `p^k`-Kanals existiert noch nicht.

Fuer `k=1` fallen erste Innovation und Hubaktivierung zusammen:

```math
R>\frac12\log p.
```

Damit besitzt nur eine echte hoehere Prime-Power (`k>=2`) ein nichtleeres **pre-hub boundary regime**.

---

# 8. Radiuswachstum auf einem alten Quellfenster ist manifest positiv

Fixiere `R<S` und betrachte nur alte Quellpunkte `|u|<R` sowie eine feste alte Kanalmenge.

Die Hubkoeffizienten bereits aktiver Kanaele aendern sich nicht. Die Restprojektionen erfuellen

```math
Q_R(u)\preceq Q_S(u).
```

Daher ist der Zuwachs des finite-adischen Mark-Grams auf dem alten Kanalraum eine Summe positiver Rang-eins-Terme aus §2.

Also

```math
\boxed{
G^{rest}_{S,u}-G^{rest}_{R,u}\succeq0.
}
```

und fuer eine feste bereits Hub-aktive Kanalmenge ebenso

```math
\boxed{
G^{hub+rest}_{S,u}-G^{hub+rest}_{R,u}\succeq0.
}
```

Dies ist eine echte forward-definierte positive Radiusinkrement-Struktur **vor** jedem Feshbach-/Schur-Schritt.

---

# 9. Was damit geloest ist — und was nicht

Geloest / typkorrekt:

```text
- dieselben raeumlichen Jumpfeatures tragen COMMON-JUMP und P11;
- source conditioning ist eine exakte Overlap-Tiefenfiltration;
- die Projektoren sind unter Radiuswachstum verschachtelt;
- jeder neue Innovationslevel ist ein positiver Rang-eins-Zuwachs;
- der Hubcutoff stimmt exakt mit dem COMMON-JUMP Prime-Power-Cutoff ueberein;
- Cross-prime coupling beginnt erst am Full-overlap-Gate.
```

Noch offen:

```text
- ob Sigma_R=H_R(I+R_R^*R_R)^{-1}H_R^* diese positiven Inkremente radius-kompatibel transportiert;
- ob die tieferen pre-hub Restkanaele exakt die COMMON-JUMP Exterior-/Gauge-Masse realisieren;
- wie die Gamma-/L_{1/2}-Boundary-Geometrie in denselben Direct System eingebaut wird;
- ob daraus eine vorwaerts definierte positive Gramform mit Schur-Komplement Q_W entsteht.
```

Der naechste Gate ist daher nicht mehr die Existenz einer radius-abhaengigen positiven Geometrie. Eine solche Geometrie liegt bereits vor. Der Gate ist ihre **Feshbach-/finite-part-Kompatibilitaet mit der Weilform**.
