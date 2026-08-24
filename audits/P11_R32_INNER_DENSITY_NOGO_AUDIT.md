# P11/R32 — No-Go für den dichten inneren Mediatorweg bei R<a

**Status:** Kandidat; keine Promotion.  
**Kontext:** Folgeaudit zu `P11_R32_SCHUR_CROSSGRAM_AUDIT.md`.  
**P11:** FROZEN. R14 unverändert.

---

## 1. Motivation

Der Schur-Cross-Gram-Audit identifiziert als starken hinreichenden Test für Annihilatorfreiheit die Dichtheit des inneren Mediatorbildes
\[
\overline{\operatorname{Ran}\mathscr M_I}
=\mathcal K_{\rm med}^{+},
\qquad
\mathscr M_I=B_{T_0}^{1/2}H_{T_0}^*E_I.
\]

Dieser Test ist absichtlich stärker als nötig.  Hier wird geprüft, ob er im P12-Drei-Shift-Fenster überhaupt plausibel ist.

---

## 2. Drei aktive Halbshifts

Im Fenster
\[
2a<T_0<\frac12\log5,
\qquad
 a=\frac12\log2,
\]
sind im Hub exakt die drei Halbshifts
\[
\tau\in\{a,b,T\},
\qquad
b=\frac12\log3>a,
\qquad
T=\log2>a.
\]
Insbesondere
\[
\boxed{\tau\ge a\quad\text{für jeden aktiven Hubshift}.}
\tag{DN.1}
\]

---

## 3. Expliziter unsichtbarer Zentralvektor

Fixiere
\[
\boxed{0<R<a.}
\tag{DN.2}
\]
Wähle
\[
0<\varepsilon<a-R
\]
und einen nichtzero geraden Vektor
\[
v\in C_c^\infty(-\varepsilon,\varepsilon)^+.
\]

Für jedes `u in (-R,R)` und jeden aktiven Halbshift `tau >= a` gilt
\[
|u\pm\tau|
\ge \tau-|u|
>a-R
>\varepsilon.
\]
Daher
\[
v(u-\tau)=v(u+\tau)=0.
\]
Jeder einzelne Differenzshift verschwindet auf dem inneren Fenster:
\[
(D_{2\tau}v)(u)=0
\qquad(|u|<R).
\]
Nach Summation über die drei aktiven Primzahlpotenzen folgt exakt
\[
\boxed{
E_I^*H_{T_0}v=0.
}
\tag{DN.3}
\]
Da `v != 0`, ist
\[
\boxed{
\ker(E_I^*H_{T_0}|_+)\ne\{0\}
\qquad(0<R<a).
}
\tag{DN.4}
\]

---

## 4. Konsequenz für das preconditionierte innere Mediatorbild

Setze
\[
B=(I+R_{T_0}^*R_{T_0})^{-1}>0.
\]
P11s Paritätssymmetrie impliziert, dass `B^{1/2}` den geraden Sektor erhält, und `B^{1/2}` ist beschränkt invertierbar.

Definiere
\[
y:=B^{-1/2}v\ne0.
\]
Dann ist `y` gerade und
\[
E_I^*H B^{1/2}y
=E_I^*Hv
=0.
\]
Aber
\[
\mathscr M_I^*
=E_I^*H B^{1/2}.
\]
Somit
\[
\boxed{
\ker\mathscr M_I^*\ne\{0\}
\qquad(0<R<a).
}
\tag{DN.5}
\]
und Hilbertraumdualität liefert
\[
\boxed{
\overline{\operatorname{Ran}\mathscr M_I}
\ne\mathcal K_{\rm med}^{+}.
}
\tag{DN.6}
\]

---

## 5. Status des starken Dichtheitspfads

Damit ist der in CG.14 formulierte starke Suffizienzweg
\[
\overline{\operatorname{Ran}\mathscr M_I}
=\mathcal K_{\rm med}^{+}
\]
für jeden
\[
0<R<a
\]
**exakt ausgeschlossen**.

### Kandidatenstatus DN-1

Vor unabhängigem Review:
\[
\boxed{\mathrm{DN\!-\!1}:?[O].}
\]

Bei unabhängigem GREEN darf gebucht werden:
\[
\boxed{
\mathrm{DN\!-\!1}:\checkmark[M]_{\rm neg}
\quad\text{für den dichten inneren Mediator-Suffizienzweg bei }0<R<a.
}
\]

---

## 6. Was dieser No-Go NICHT sagt

Aus der Nichtdichtheit des inneren Mediatorbildes folgt **nicht** automatisch ein Schur-Annihilator.

Der echte Cross-Gram-Kern ist
\[
\ker(\mathscr M_I^*\mathscr M_A).
\]
DN-1 zeigt lediglich, dass
\[
\ker\mathscr M_I^*\ne0.
\]
Für einen tatsächlichen Annulus-Annihilator müsste zusätzlich ein nichtzero `w` existieren mit
\[
\mathscr M_Aw\in\ker\mathscr M_I^*.
\]
P12-Injektivität liefert auf den global geschlossenen Strata sogar
\[
\mathscr M_Aw\ne0\qquad(w\ne0),
\]
entscheidet aber nicht, ob dieses nichtzero Bild in den unsichtbaren inneren Mediatorrichtungen liegen kann.

Somit bleibt die echte Frage
\[
\boxed{
\operatorname{Ran}\mathscr M_A
\cap
\ker\mathscr M_I^*
\stackrel?=\{0\}
}
\tag{DN.7}
\]
offen.

DN-1 schließt daher **nur** den zu starken Dichtheits-Suffizienzweg und schärft die Forschungsfront auf relative Transversalität.

Keine Aussage über annular cancellation, Polar Gauge, Strong Terminal Transport, Objekt X oder RH folgt.
