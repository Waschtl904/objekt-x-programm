# P11↔P12 Rückbindungs-Audit — R32 lokalisierter Hub

**Status:** Kandidat; noch nicht promotet.  
**Repo-Basis:** `Waschtl904/objekt-x-programm`, `main@3affcc6c29207814e9e7e0219746a77eff074409`.  
**P11:** FROZEN; keine Änderung am P11-Manuskript.  
**P12:** Round 29 formal promotet als A15.1b2n / R29-A `✓[M]_part`.  
**Ziel:** exakt entscheiden, was die P12-Injektivitätsarbeit für den in P11/R32-F(ii) ausdrücklich offenen Test
\[
\ker(H_{T_0}E_{\mathcal A})=\{0\}\ ?
\]
leistet, und den danach verbleibenden Engpass ohne Overclaim isolieren.

---

## 1. P11-Ausgangspunkt

Im aktuellen P11 wird die annular-fingerprint Strategie R32-F(ii) auf den konkreten Schurterm
\[
\Sigma_{T_0}=H_{T_0}B_{T_0}H_{T_0}^*,
\qquad
B_{T_0}=(I+R_{T_0}^*R_{T_0})^{-1}
\]
bezogen.  Nach dem No-Go für die naive unskalierte Neumann-Kontraktionsroute wird dort ausdrücklich festgehalten, dass vor dem Versuch, einen lokalisierten Annulus-Annihilator zu bauen, zuerst zu entscheiden ist,
\[
\boxed{\ker(H_{T_0}E_{\mathcal A})=\{0\}\ ?}
\tag{RB.1}
\]
mit Nullfortsetzung `E_A` vom symmetrischen Annulus
\[
\mathcal A_{R,S}=(-S,-R)\cup(R,S).
\]

P12 ist genau die seitdem entwickelte lokalisierte Hub-Injektivitätsbaustelle.  Dieser Audit prüft die exakte Operatoridentifikation, nicht nur eine thematische Ähnlichkeit.

---

## 2. Drei-Shift-Fenster und aktive Primzahlpotenzen

Setze wie in P12
\[
a=\frac12\log2,
\qquad
b=\frac12\log3,
\qquad
T=2a=\log2,
\qquad
c=\frac12\log5.
\]
Wir arbeiten im P12-Fenster
\[
\boxed{2a<T_0<c.}
\tag{RB.2}
\]
Dann
\[
4<e^{2T_0}<5.
\]
Für den P11-Hub
\[
H_{T_0}
=P_{T_0}\sum_{p^k\le e^{2T_0}}
\sqrt{\log p}\,p^{-3k/4}D_{k\log p}E_{T_0}
\]
sind daher **exakt** die drei Primzahlpotenzen
\[
\boxed{2,3,4}
\tag{RB.3}
\]
aktiv.

Ihre Halbverschiebungen sind
\[
\tau_{2,1}=a,
\qquad
\tau_{3,1}=b,
\qquad
\tau_{2,2}=T,
\]
und ihre Koeffizienten sind exakt
\[
p=\sqrt{\log2}\,2^{-3/4},
\qquad
r=\sqrt{\log3}\,3^{-3/4},
\qquad
q=\sqrt{\log2}\,2^{-3/2}.
\tag{RB.4}
\]
Dies sind genau die drei Shifts und Gewichte des kanonischen P12-Rohoperators.

---

## 3. Exakte Odd-Fold-Identifikation

Sei
\[
\mathcal H_{\mathcal A}^-
:=\{f\in L^2(\mathcal A_{R,S}): f(-u)=-f(u)\}
\]
der ungerade Annulussektor.

Definiere die unitäre Odd-Extension
\[
\mathcal O_{R,S}:L^2(R,S)\to\mathcal H_{\mathcal A}^-
\]
durch
\[
(\mathcal O_{R,S}h)(u)
=
\begin{cases}
2^{-1/2}h(u),&R<u<S,\\
-2^{-1/2}h(-u),&-S<u<-R.
\end{cases}
\tag{RB.5}
\]
und die normierte Positiv-Halbachsenrestriktion auf den geraden Zielsektor
\[
\mathcal R_+:L^2(-T_0,T_0)^+\to L^2(0,T_0),
\qquad
(\mathcal R_+g)(u)=\sqrt2\,g(u).
\tag{RB.6}
\]

Da jede Differenztranslation
\[
D_s=U_{s/2}-U_{-s/2}
\]
die Parität wechselt, bildet `H_{T0}` den ungeraden Annulussektor in den geraden Zielsektor ab.

Für `h in L^2(R,S)` und `u>0` liefert die direkte Substitution von (RB.3)–(RB.5)
\[
\begin{aligned}
(\mathcal R_+H_{T_0}E_{\mathcal A}\mathcal O_{R,S}h)(u)
={}&p\,[h(u-a)-h(u+a)]\\
&+r\,[h(u-b)-h(u+b)]\\
&+q\,[h(u-T)-h(u+T)],
\end{aligned}
\tag{RB.7}
\]
mit exakt derselben Odd-Reflection und denselben Support-/Source-Horizon-Cuts wie im P12-Rohoperator.

Damit gilt im gesamten Drei-Shift-Fenster die unitäre Operatoridentität
\[
\boxed{
\mathcal R_+H_{T_0}E_{\mathcal A}\mathcal O_{R,S}
=L_{R,S,T_0}^{\{a,b,2a\}}.
}
\tag{RB.8}
\]
Insbesondere
\[
\boxed{
\ker(H_{T_0}E_{\mathcal A}|_{\mathcal H_{\mathcal A}^-})=\{0\}
\iff
\ker L_{R,S,T_0}^{\{a,b,2a\}}=\{0\}.
}
\tag{RB.9}
\]

Die Normierungsfaktoren `sqrt(2)` dienen nur der Unitarität; ohne sie bleibt die Kernaussage identisch.

---

## 4. Was P12 für P11/R32 bereits entscheidet

Die konsolidierte P12-Injektivität liefert im Drei-Shift-Fenster volle Kerneltrivialität in den global bewiesenen Strata:

1. `S<T`;
2. `S=T`;
3. im Mixed Strip `T<S<T_0` für `rho<=R<T`, wobei
   \[
   \rho=\frac12\log\frac{10}{9};
   \]
4. im Mixed Strip für **alle** `0<R<T` unter der Restricted-Tail-Bedingung
   \[
   \sigma=S-T\le R.
   \]

Daher gilt dort durch (RB.9)
\[
\boxed{
\ker(H_{T_0}E_{\mathcal A}|_{\mathcal H_{\mathcal A}^-})=\{0\}.
}
\tag{RB.10}
\]

### Status RB-1

\[
\boxed{
\mathrm{RB\!-\!1}:\ \checkmark[M]
\quad\text{auf den globalen P12-Injektivitätsstrata.}
}
\]

Dies ist keine neue analytische Injektivitätsrechnung; es ist die exakte Rückbindung eines bereits bewiesenen P12-Satzes an den ausdrücklich offenen P11/R32-Hubtest.

---

## 5. Low-radius Firewall

Für
\[
0<R<\rho,
\qquad
R<\sigma,
\]
sind die Round-23–29-Resultate **lokale Faserzertifikate**, solange kein globaler Cover-/Descent-Satz bewiesen ist.

Insbesondere beweisen C42/C44/C26, M43, M68 und die Round-29-ε-Brücke an ihren jeweiligen Fasern lokale Aussagen wie
\[
h(x)=0
\quad\text{oder}\quad
h(x)=h(\delta-x)=0,
\]
aber nicht automatisch
\[
\ker L_{R,S,T_0}=\{0\}
\]
für den gesamten physikalischen Parameterpunkt.

Daher darf (RB.10) **nicht** aus den lokalen Round-23–29-Kammern auf den ganzen residualen Low-radius-Bereich erweitert werden.

### Status RB-1-low

\[
\boxed{
\mathrm{RB\!-\!1\!\text{-}low}:?[O]
}
\]
für den noch nicht global geschlossenen residualen Bereich.

Round 29 ändert diese Firewall nicht.

---

## 6. Funktionalanalytische Konsequenz: dichte Adjungiertenrange

Setze auf einem global geschlossenen P12-Stratum
\[
T_{\mathcal A}
:=H_{T_0}E_{\mathcal A}|_{\mathcal H_{\mathcal A}^-}
:\mathcal H_{\mathcal A}^-\to L^2(-T_0,T_0)^+.
\]
`T_A` ist beschränkt.  Aus (RB.10) und der elementaren Hilbertraumidentität
\[
\overline{\operatorname{Ran}T_{\mathcal A}^*}
=(\ker T_{\mathcal A})^\perp
\]
folgt
\[
\boxed{
\overline{\operatorname{Ran}T_{\mathcal A}^*}
=\mathcal H_{\mathcal A}^-.
}
\tag{RB.11}
\]
Wegen der in P11 bewiesenen Antisymmetrie
\[
H_{T_0}^*=-H_{T_0}
\]
gilt
\[
T_{\mathcal A}^*
=E_{\mathcal A}^*H_{T_0}^*|_{+}
=-E_{\mathcal A}^*H_{T_0}|_{+}.
\tag{RB.12}
\]
Somit sind die annularen Restriktionen von Hub-Ausgaben aus dem geraden Zielsektor dicht im ungeraden Annulussektor.

### Status RB-2

\[
\boxed{
\mathrm{RB\!-\!2}:\ \checkmark[M]
\quad\text{auf den globalen P12-Injektivitätsstrata.}
}
\]

**Firewall:** Injektivität impliziert hier nur dichte Adjungiertenrange.  Ohne eine zusätzliche Closed-Range-/Bounded-below-Abschätzung folgt **keine** Surjektivität und keine quantitative Observabilitätskonstante.

---

## 7. Der einfache Kernel-Annihilator-Pfad ist dort negativ geschlossen

Für die konkrete annularisierte Schur-Abbildung definiere
\[
\mathcal T_{R,S,T_0}
:=E_{\mathcal A}^*\Sigma_{T_0}E_I,
\qquad
\Sigma_{T_0}=H_{T_0}B_{T_0}H_{T_0}^*,
\tag{RB.13}
\]
wobei `E_I` die Nullfortsetzung des inneren Quellfensters bezeichnet.

Wenn ein ungerader Annulusvektor `w` die stärkere Bedingung
\[
H_{T_0}E_{\mathcal A}w=0
\tag{RB.14}
\]
erfüllt, dann ist wegen `H*=-H`
\[
H_{T_0}^*E_{\mathcal A}w=0
\]
und damit für jedes innere `f`
\[
\langle\mathcal T_{R,S,T_0}f,w\rangle
=
\langle B_{T_0}H_{T_0}^*E_If,
       H_{T_0}^*E_{\mathcal A}w\rangle
=0.
\tag{RB.15}
\]
Ein nichttrivialer Kernelvektor aus (RB.14) wäre also tatsächlich ein unmittelbarer Schur-Range-Annihilator.

Aber auf den globalen P12-Strata gilt (RB.10).  Daher existiert dort **kein** nichttrivialer Annihilator dieses einfachen Typs.

### Status RB-3

\[
\boxed{
\mathrm{RB\!-\!3}:\ \checkmark[M]_{\rm neg}
}
\]
für den **einfachen Kernel-Annihilator-Pfad** auf den global geschlossenen P12-Strata.

Das ist ein Route-No-Go, kein No-Go gegen Schur-Annihilatoren allgemein.

---

## 8. Der echte post-P12 Engpass

Der Annulusvektor `w` annihiliert die konkrete Schur-Range genau dann, wenn
\[
\mathcal T_{R,S,T_0}^*w=0.
\]
Da `Sigma_{T0}` selbstadjungiert ist,
\[
\boxed{
\mathcal T_{R,S,T_0}^*
=E_I^*\Sigma_{T_0}E_{\mathcal A}
=E_I^*H_{T_0}B_{T_0}H_{T_0}^*E_{\mathcal A}.
}
\tag{RB.16}
\]
Der richtige nächste Kerneltest lautet daher
\[
\boxed{
\ker\bigl(E_I^*H_{T_0}B_{T_0}H_{T_0}^*E_{\mathcal A}\bigr)
\stackrel?=\{0\}.
}
\tag{RB.17}
\]

P12 entscheidet nur die strengere Vorbedingung
\[
\ker(H_{T_0}E_{\mathcal A})=\{0\}.
\]
Ein möglicher **indirekter Schur-Annihilator** müsste daher notwendigerweise
\[
H_{T_0}^*E_{\mathcal A}w\ne0
\]
erfüllen, aber nach Anwendung des positiven invertierbaren `B_{T0}`, des zweiten Hubs und der inneren Restriktion verschwinden:
\[
E_I^*H_{T_0}B_{T_0}H_{T_0}^*E_{\mathcal A}w=0.
\tag{RB.18}
\]

### Status RB-4

\[
\boxed{
\mathrm{RB\!-\!4}:?[O].
}
\]

Dies ist der präzisere Nachfolger des in P11/R32-F(ii) zunächst genannten äußeren Hub-Kerntests.

---

## 9. Verbindung zur annularen Cancellation-Frage

P11/R31–R33 definieren
\[
\Delta_{R,S}^{[T_0]}
=\phi_S-A_S^{[T_0]}j_{R,S}
\]
und beweisen exakt
\[
\Delta_{R,S}^{[T_0]}=0
\iff
s_{R,S,T_0}=0.
\]
Die Gamma-Seite ist durch den inzwischen geschlossenen P02→P11-Symbolbridge exakt anti-lokal; offen ist eine mögliche konkrete Cancellation durch den Schurterm.

RB-3 zeigt: Auf den global geschlossenen P12-Strata kann diese Cancellation-Frage **nicht** durch einen nichttrivialen Vektor aus `ker(H E_A)` separiert werden.  Jede erfolgreiche Annihilatorstrategie muss die engere konkrete Schur-Komposition (RB.16) ausnutzen.

Dies ist eine echte strategische Rückbindung:

\[
\boxed{
\text{P12 schließt den P11/R32-Vorfilter}
\;\Longrightarrow\;
\text{die Forschung muss auf die Schur-Komposition oder direkt auf Polar/Cross-Polar wechseln.}
}
\tag{RB.19}
\]

---

## 10. Rückbindungskette mit Status

| Übergang | Status nach diesem Audit | Bedeutung |
|---|---|---|
| P12 lokalisierte Hub-Injektivität → P11/R32 äußerer Hub-Kerntest | `✓[M]` auf globalen P12-Strata | exakte unitäre Operatoridentifikation |
| lokale Round-23–29 Faserzertifikate → voller Low-radius Hub-Kerntest | `?[O]` | Projection-/Fiber-Firewall |
| Hub-Injektivität → dichte Adjungiertenrange | `✓[M]` | Hilbertraumdualität |
| Hub-Injektivität → quantitative bounded-below / Closed Range | `?[O]` | nicht aus Injektivität ableitbar |
| einfacher `ker(H E_A)`-Annihilator → Schur-Annihilator | `✓[M]` als Implikation, aber Quellkernel dort trivial | Route `✓[M]_neg` |
| indirekter Schur-Annihilator `ker(E_I^* Σ E_A)` | `?[O]` | echter post-P12 Annular-Range-Kern |
| annularer Schur-Range-Test → `Delta != 0` / volle Normal-Mismatch-Klassifikation | `?[O]` | zusätzliche Separation nötig |
| Modulus/inverse-root → relative Polar Gauge | `?[O]` | R14-Firewall |
| relative Polar Gauge / Cross-Polar → Strong Terminal Transport | `?[O]` | direkte Cauchy-Kette bleibt offen |
| Strong Terminal Transport → globale Gram/Mediator-Geometrie | `?[O]` | P11 Open Problem |
| globale Geometrie → adelische + Fredholm/Schatten-Schicht → Objekt X | `?[O]` | separate höhere Verpflichtungen |

---

## 11. Nichtbehauptungen / Firewall

Dieser Audit behauptet **nicht**:

- globale P12-Injektivität im gesamten residualen Low-radius-Bereich;
- einen bounded-below-Satz für `H_{T0}E_A`;
- Closed Range oder Surjektivität des adjungierten lokalisierten Hubs;
- Nichtexistenz sämtlicher Schur-Range-Annihilatoren;
- `Delta_{R,S}^{[T0]} != 0` für alle Tripel;
- Verschwinden oder Nichtverschwinden des tangentialen Gamma-Crossblocks;
- Polar-Gauge-Konvergenz oder -Nichtkonvergenz;
- Strong Terminal Transport;
- globale Gram-/Mediator-Geometrie;
- Objekt X oder RH.

P11 bleibt FROZEN.  R14 bleibt unverändert.

---

## 12. Kandidatenverdict

Vor unabhängigem Review:

\[
\boxed{
\begin{aligned}
\mathrm{RB\!-\!1}&:\ ?[O]\ \text{(Promotion ausstehend; mathematische Herleitung oben)},\\
\mathrm{RB\!-\!2}&:\ ?[O]\ \text{(Promotion ausstehend)},\\
\mathrm{RB\!-\!3}&:\ ?[O]\ \text{(Promotion ausstehend)},\\
\mathrm{RB\!-\!4}&:\ ?[O]\ \text{(echter offener Folgeengpass)}.
\end{aligned}
}
\]

Bei unabhängigem GREEN dürfen RB-1 und RB-2 als `✓[M]` auf den global geschlossenen P12-Strata und RB-3 als `✓[M]_neg` Route-No-Go gebucht werden.  RB-4 bleibt offen.
