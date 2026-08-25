# P11/R32 — FG-Exhaustivitätsabschluss: even zero-extension und expliziter Isomorphismus

**Status:** Kandidat; keine Promotion.  
**P11:** FROZEN. **P12:** unverändert. **R14:** unverändert.  
**Basis:** `audits/P11_R32_INVISIBLE_FIBER_GRAPH_RECONSTRUCTION_ADDENDUM.md`.  
**Ziel:** die im unabhängigen Review einzig verbliebene FGR-F-Lücke explizit schließen: die Rückrichtung von einer geglueten Kernel-Familie zu genau einem gesampelten geraden Element von `N_I`.

---

## 1. Setup

Es gelten die Notationen des Rekonstruktionsaddendums. Insbesondere

\[
\mathcal U_R=\bigcup_{\tau\in\{a,b,T\}}(\tau-R,\tau+R)\cap(0,T_0),
\]

\[
\mathcal Z_R^{\rm phys}=(0,T_0)\setminus\mathcal U_R,
\]

\[
J_R:L^2(\mathcal U_R)\xrightarrow{\sim}\mathfrak G_R,
\qquad R_R=J_R^{-1},
\]

und

\[
\Lambda_RJ_Rg=E_I^*H\,g_{\rm even}
\]

für die auf den gesampelten Bereich beschränkte gerade Fortsetzung.

Alle Mengengleichheiten zwischen Branchbildern und `U_R` sind im Folgenden **a.e.** zu verstehen. Dies ist die präzise Formulierung, weil offene Branchdomains isolierte Branchzentren bzw. Endpunkte auslassen können; diese bilden nur eine endliche Nullmenge.

---

## 2. Even-zero-extension

Definiere

\[
\operatorname{Ev}_R:L^2(\mathcal U_R)\longrightarrow L^2(-T_0,T_0)^+
\]

durch

\[
(\operatorname{Ev}_Rg)(t)
:=
\begin{cases}
 g(|t|),& |t|\in\mathcal U_R,\\
 0,& |t|\notin\mathcal U_R.
\end{cases}
\tag{EC.1}
\]

Dann ist `Ev_R` linear, injektiv und beschränkt mit

\[
\boxed{
\|\operatorname{Ev}_Rg\|_{L^2(-T_0,T_0)}^2
=2\|g\|_{L^2(\mathcal U_R)}^2.
}
\tag{EC.2}
\]

Umgekehrt ist jede gerade `L2`-Funktion, deren positiver wesentlicher Support in `U_R` liegt, a.e. eindeutig von der Form `Ev_R g`, nämlich mit

\[
g=y|_{\mathcal U_R}.
\tag{EC.3}
\]

Damit ist die zuvor verkürzt formulierte „gesampelte gerade Fortsetzung“ ein expliziter beschränkter Isomorphismus auf den geraden Sample-Unterraum.

---

## 3. Rückrichtung aus dem Gluing-Kernel

Sei

\[
F\in\mathfrak G_R\cap\ker\Lambda_R.
\]

Setze

\[
g:=R_RF\in L^2(\mathcal U_R),
\qquad
y_F:=\operatorname{Ev}_R g.
\tag{EC.4}
\]

Wegen `J_RR_R=I` auf `G_R` gilt

\[
J_Rg=F.
\tag{EC.5}
\]

Daher folgt exakt

\[
E_I^*Hy_F
=\Lambda_RJ_Rg
=\Lambda_RF
=0
\quad\text{a.e. auf }(0,R).
\tag{EC.6}
\]

Also

\[
\boxed{y_F\in\mathcal N_I.}
\tag{EC.7}
\]

Die Eindeutigkeit ist ebenso unmittelbar: Falls zwei gesampelte gerade Funktionen dieselbe Branchfamilie `F` besitzen, so haben ihre positiven Restriktionen wegen der Injektivität von `J_R` denselben Wert `R_RF` a.e.; durch Geradheit und Nullfortsetzung stimmen sie auf ganz `(-T_0,T_0)` a.e. überein.

Damit existiert **keine zusätzliche Klasse** gesampelter Lösungen, die außerhalb der Gluing-Darstellung liegen könnte.

---

## 4. Expliziter Gesamtisomorphismus

Sei

\[
\mathcal Z_R^+
:=\{z\in L^2(-T_0,T_0)^+:
\operatorname{ess\,supp}(z|_{(0,T_0)})\subset\mathcal Z_R^{\rm phys}\}.
\]

Definiere

\[
\Phi_R:
\mathcal Z_R^+\oplus
(\mathfrak G_R\cap\ker\Lambda_R)
\longrightarrow\mathcal N_I
\]

durch

\[
\boxed{
\Phi_R(z,F):=z+\operatorname{Ev}_R(R_RF).
}
\tag{EC.8}
\]

### Injektivität

Die beiden Summanden besitzen disjunkten positiven physischen Support a.e. Daher ist ihre Summe orthogonal. Aus `Phi_R(z,F)=0` folgen `z=0` und `Ev_R(R_RF)=0`; anschließend `R_RF=0` und wegen `J_RR_RF=F` auch `F=0`.

### Surjektivität

Sei `y in N_I`. Zerlege orthogonal nach positivem Support

\[
y=y_{\rm blind}+y_{\rm samp},
\]

mit `y_blind in Z_R^+` und `y_samp` auf der geraden Fortsetzung von `U_R` getragen. Setze

\[
g:=y_{\rm samp}|_{\mathcal U_R},
\qquad F:=J_Rg.
\]

Dann ist `F in G_R`. Weil der blinde Anteil von `E_I^*H` nicht gesehen wird,

\[
0=E_I^*Hy=E_I^*Hy_{\rm samp}=\Lambda_RF,
\]

also `F in ker Lambda_R`, und nach (EC.3)

\[
y_{\rm samp}=\operatorname{Ev}_R(R_RF).
\]

Somit `y=Phi_R(y_blind,F)`.

### Beschränktheit

`Ev_R`, `J_R` und `R_R` sind beschränkt; die physische Blind-/Sample-Projektion ist eine orthogonale Supportprojektion. Daher sind `Phi_R` und `Phi_R^{-1}` beschränkt.

Folglich

\[
\boxed{
\mathcal N_I
\xrightarrow[\Phi_R^{-1}]{\ \sim\ }
\mathcal Z_R^+\oplus(\mathfrak G_R\cap\ker\Lambda_R)
}
\tag{EC.9}
\]

als Hilberträume über einen kanonischen beschränkten Isomorphismus. Es wird weiterhin **keine Unitarität** bezüglich der ungegewichteten Branch-Direktproduktnorm behauptet.

---

## 5. Adversarialer Exhaustivitätscheck

Ein hypothetisches `y in N_I`, das von (EC.9) nicht erfasst würde, müsste einen positiven physischen Supportpunkt entweder

1. außerhalb `U_R` besitzen — dieser Anteil liegt definitionsgemäß in `Z_R^+`; oder
2. innerhalb `U_R` besitzen — dieser Anteil besitzt über `J_R` zwingend eine eindeutige Branchfamilie in `G_R`, und die Kernelgleichung ist exakt `Lambda_R F=0`.

Diese beiden Fälle zerlegen `(0,T_0)` a.e. vollständig. Ein dritter Supporttyp existiert nicht. Nullmengen an Branchzentren oder Endpunkten erzeugen in `L2` keine zusätzliche Klasse.

---

## 6. Review-Folge

Mit (EC.1)–(EC.9) ist genau der im unabhängigen Review als noch zu knapp bezeichnete FGR-F-Rückschritt explizit ausformuliert.

**Kandidatenverdict dieses Closure-Audits:**

```text
FGR-F EXHAUSTIVE NORMAL FORM: CANDIDATE GREEN
FG-1 OVERALL:                CANDIDATE GREEN
```

Dies ist **keine Promotion**. Eine formale Statusänderung erfolgt nur nach unabhängiger Gegenprüfung und ausdrücklicher Projektfreigabe.

---

## 7. Firewall

Aus (EC.9) folgt nicht:

- Trivialität von `N_I`;
- Trivialität des augmentierten Blockkerns;
- Injektivität des vollen Schur-Crossblocks;
- Closed Range / bounded below / uniforme Winkel;
- Strong Terminal Transport;
- Objekt X oder RH.

Das Resultat klassifiziert ausschließlich den inneren Unsichtbarkeitsraum für die hier betrachtete lokale Drei-Shift-Geometrie.
