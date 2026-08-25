# P11/R32 — unendlichdimensionaler zentraler Unsichtbarkeitsraum

**Status:** Kandidat; keine Promotion.  
**P11:** FROZEN. **P12:** unverändert. **R14:** unverändert.  
**Kontext:** Verstärkung von `P11_R32_INNER_DENSITY_NOGO_AUDIT.md`.

## 1. Setup

Im Drei-Shift-Fenster
\[
2a<T_0<c:=\frac12\log5,
\qquad
a=\frac12\log2,
\quad b=\frac12\log3>a,
\quad T=2a>a,
\]
ist der Hub
\[
H= pD_{2a}+rD_{2b}+qD_{2T}
\]
auf `L^2(-T0,T0)` mit Nullfortsetzung außerhalb des Horizonts.

Fixiere
\[
0<R<a,
\qquad I=(-R,R).
\]
Auf dem geraden Sektor setze
\[
\mathcal N_I:=\ker(E_I^*H|_{\mathscr H^+}).
\]

Definiere den zentralen geraden Unterraum
\[
\boxed{
\mathcal C_R^+
:=\{v\in L^2(-T_0,T_0)^+:
\operatorname{ess\,supp}v\subset[-(a-R),a-R]\}.
}
\tag{CI.1}
\]

Da `a-R>0`, ist `C_R^+` ein nichttrivialer geschlossener unendlichdimensionaler Hilbertraum.

## 2. Satz CI-1 — vollständige zentrale Unsichtbarkeit

\[
\boxed{
\mathcal C_R^+\subset\mathcal N_I.
}
\tag{CI.2}
\]

Insbesondere
\[
\boxed{
\dim\mathcal N_I=\infty.
}
\tag{CI.3}
\]

### Beweis

Sei `v in C_R^+`. Für fast jedes `u` mit `|u|<R` und jeden aktiven Halbshift
\[
\tau\in\{a,b,T\}
\]
gilt `tau>=a` und damit
\[
|u\pm\tau|\ge \tau-|u|>a-R.
\]
Bis auf die maßnulligen Randfälle liegen also beide Argumente außerhalb des wesentlichen Trägers von `v`. Daher
\[
v(u-\tau)=v(u+\tau)=0
\]
für fast jedes `|u|<R`, und folglich
\[
(D_{2\tau}v)(u)=0.
\]
Dies gilt für alle drei aktiven Shiftterme; somit
\[
(Hv)(u)=0
\quad\text{für fast jedes }|u|<R.
\]
Also
\[
E_I^*Hv=0,
\]
was (CI.2) beweist. Da `L^2(-(a-R),a-R)^+` unendlichdimensional ist, folgt (CI.3).

## 3. Konsequenz für die Cross-Gram-/SE-Transversalität

Die post-P12 inversefreie Transversalitätsfrage lautet auf globalen P12-Injektivitätsstrata
\[
\operatorname{Ran}(HE_{\mathcal A}|_-)
\cap
(I+R_{T_0}^*R_{T_0})\mathcal N_I
\stackrel?=\{0\}.
\]

CI-1 zeigt, dass der zweite Faktor bereits den großen Unterraum
\[
(I+R_{T_0}^*R_{T_0})\mathcal C_R^+
\]
enthält. Damit kann die verbleibende Aufgabe **nicht** als Kleinheit oder Endlichdimensionalität des inneren Unsichtbarkeitsraums formuliert werden.

Die korrekte Zielaussage bleibt qualitative Transversalität: selbst ein unendlichdimensionaler unsichtbarer Raum kann eine gegebene injektive Annulus-Hubrange trivial schneiden.

## 4. Coercivity-Firewall

CI-1 liefert ausdrücklich **keinen** Schur-Annihilator. Aus
\[
0\ne y\in\mathcal N_I
\]
folgt nicht
\[
(I+R^*R)y\in\operatorname{Ran}(HE_{\mathcal A}).
\]

Ebenso folgt aus CI-1 keine Aussage über
- closed range,
- bounded below / uniforme Winkel,
- Surjektivität,
- Polar Gauge,
- Strong Terminal Transport,
- Objekt X oder RH.

## 5. Kandidatenstatus

Bei unabhängiger GREEN-Prüfung wäre erlaubt:

- **CI-1:** `✓[M]` — unendlichdimensionaler zentraler Unterraum `C_R^+` liegt für jedes `0<R<a` im inneren Unsichtbarkeitsraum `N_I`.

Die eigentliche Transversalitätsfrage bleibt `?[O]`.
