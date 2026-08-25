# P11/R32 — exakte 11-Wort-Bilanz für die reparierte erste nichtzentrale Schale

**Status:** Zusatz-Audit; keine Promotion.  
**P11:** FROZEN. **P12:** unverändert. **R14:** unverändert.  
**Zweck:** Die einzige nach dem unabhängigen NS-Review verbliebene Unsicherheit wird isoliert geprüft: vollständige Bilanz aller elf Full-Rest-Wörter auf der Schale `S_R^+`.

## 1. Setup

Im Drei-Shift-Fenster
\[
2a<T_0<c=\tfrac12\log5,
\qquad a=\tfrac12\log2,
\quad b=\tfrac12\log3,
\]
setze
\[
d=b-a,
\qquad e=a-d,
\qquad \varepsilon=T_0-2a.
\]
Für
\[
\frac d2\le R<d,
\qquad h=d-R,
\]
sei `S_R^+` der gerade Schalenraum aus NS-1 mit positivem Träger
\[
J_R=(a-h,a+h)
\]
und Profil
\[
y(a-s)=y(a+s)=:f(s),\qquad |s|<h.
\]

Wir benutzen die SE-2-Zerlegung
\[
A=R_{T_0}^*R_{T_0}=A_{20}+A_{21}+A_{30},
\]
mit
\[
A_{20}=(\log2)\Phi_{20}^*M_{20}\Phi_{20},
\]
\[
\Phi_{20}=\alpha_1K_1+\alpha_2K_2+\alpha_3K_3,
\quad
\alpha_1=2^{-3/4},\ \alpha_2=2^{-3/2},\ \alpha_3=2^{-9/4},
\]
wo `K_j=K_{j log 2}^{tr}` den Halbshift `ja` besitzt,
\[
A_{21}=2(\log2)\alpha_2^2 K_2^*M_{21}K_2,
\]
und
\[
A_{30}=2(\log3)\beta^2 L^*M_{30}L,
\quad \beta=3^{-3/4},
\quad L=K_{\log3}^{tr}
\]
mit Halbshift `b`.

Damit bestehen exakt `9+1+1=11` geordnete Wörter.

## 2. Die beiden rechten Spalten k=1 und k=3 sterben vollständig

Auf `S_R^+` gilt exakt
\[
\boxed{M_{20}K_1y=0,\qquad M_{20}K_3y=0.}
\tag{WL.1}
\]

Für `K_1` hebt sich der zentrale Output durch die Profilsymmetrie auf. Seine äußeren Kopien liegen um `+-2a`; ihre kleinste Entfernung vom Ursprung ist
\[
2a-h.
\]
Die `M20`-Maske hat Radius
\[
a+\varepsilon.
\]
Da
\[
2a-h-(a+\varepsilon)=a-h-\varepsilon=e+R-\varepsilon>0
\]
wegen `epsilon<E<e`, werden alle äußeren Kopien abgeschnitten.

Für `K_3` liegen bereits die nächsten Outputs um `+-2a`, also gilt dieselbe strikte Maskentrennung.

Folglich verschwinden beim Anwenden von `A20` auf `y` alle sechs Wörter mit rechtem Index `k=1` oder `k=3`:
\[
\boxed{
W_{11}=W_{21}=W_{31}=W_{13}=W_{23}=W_{33}=0
\quad\text{auf }S_R^+,
}
\tag{WL.2}
\]
wo
\[
W_{\ell k}:=K_\ell^*M_{20}K_k.
\]

Wichtig: Dies ist eine Aussage über den **rechten** Faktor. Es erlaubt nicht, `K_1^*` oder `K_3^*` nach dem Rücktransport zu verwerfen.

## 3. Genau drei (2,0)-Wörter überleben

Setze
\[
g:=M_{20}K_2y.
\]
Dann
\[
A_{20}y
=(\log2)\alpha_2
\bigl(\alpha_1K_1^*+\alpha_2K_2^*+\alpha_3K_3^*\bigr)g.
\tag{WL.3}
\]

Somit überleben aus den neun Wörtern exakt
\[
\boxed{W_{12},\quad W_{22},\quad W_{32}.}
\tag{WL.4}
\]

Der maskierte Zwischenoutput `g` liegt nur auf den beiden (möglicherweise einseitig abgeschnittenen) Schalen um `+-a`. Daher liefert der Adjungiertentransport folgende möglichen Supportzentren:

| Wort | mögliche Zentren nach Rücktransport | Rolle im NS-Beweis |
|---|---|---|
| `W12=K1* M20 K2` | `0`, `+-2a` | zentraler Cross-Term-Echo; äußere `+-2a`-Kopien irrelevant für die Auswertungszonen |
| `W22=K2* M20 K2` | `+-a`, `+-3a` | lokaler `a`-Schalen-Selbstterm; `+-3a` liegt außerhalb des Horizonts |
| `W32=K3* M20 K2` | `+-2a`, `+-4a` | nur horizon-nahe äußere Kopien; kein zentraler oder `a`-Schalen-Beitrag |

Die Zentren folgen allein aus `supp(K_ell^*g) subset supp(g)+-{ell a}`.

## 4. Der zehnte Term (2,1) ist identisch null

Der einzige `(2,1)`-Term ist
\[
A_{21}=2(\log2)\alpha_2^2K_2^*M_{21}K_2.
\]
Der unmaskierte `K2 y`-Output liegt um `+-a`; seine minimale Entfernung vom Ursprung beträgt
\[
a-h=e+R.
\]
Die Maske `M21` hat Radius `epsilon`. Wegen
\[
e+R>e>\varepsilon
\]
gilt
\[
\boxed{M_{21}K_2y=0,\qquad A_{21}y=0.}
\tag{WL.5}
\]

## 5. Der elfte Term (3,0) überlebt, aber erzeugt keinen zentralen Echo

Der `(3,0)`-Block besitzt nur das eine Wort
\[
\boxed{A_{30}=2(\log3)\beta^2L^*M_{30}L.}
\tag{WL.6}
\]

`Ly` erzeugt nach der Maske nur Schalen um `+-d`; der Rücktransport mit Halbshift `b=a+d` erzeugt daher mögliche Zentren
\[
\boxed{+-a,\qquad +-(a+2d).}
\tag{WL.7}
\]

Insbesondere liegt kein Supportzentrum bei `0`. Der `(3,0)`-Term kann den zentralen Echo (NS.9) daher nicht verändern.

## 6. Vollständige 11-Wort-Tabelle

| Nr. | Block/Wort | Status auf `S_R^+` |
|---:|---|---|
| 1 | `(2,0) W11` | `0` |
| 2 | `(2,0) W21` | `0` |
| 3 | `(2,0) W31` | `0` |
| 4 | `(2,0) W12` | **aktiv** — zentral `0` + äußere `+-2a` |
| 5 | `(2,0) W22` | **aktiv** — `+-a` (+ `+-3a` außerhalb Horizont) |
| 6 | `(2,0) W32` | **aktiv** — äußere `+-2a` (+ `+-4a` außerhalb) |
| 7 | `(2,0) W13` | `0` |
| 8 | `(2,0) W23` | `0` |
| 9 | `(2,0) W33` | `0` |
| 10 | `(2,1)` | `0` |
| 11 | `(3,0)` | **aktiv** — `+-a`, `+-(a+2d)` |

Damit wirken global auf `S_R^+` exakt
\[
\boxed{4\text{ von }11\text{ Wörtern}.}
\tag{WL.8}
\]

## 7. Vollständigkeit der beiden NS-Auswertungsformeln

### 7.1 Zentralbereich `0<t<h`

Da `R>=d/2`, gilt
\[
h=d-R\le d/2,
\]
also
\[
2h\le d<a.
\]
Daher
\[
a-h>h,
\qquad
2a-h>a+h.
\tag{WL.9}
\]

Somit kann im Zentralbereich `0<t<h` von den vier aktiven Wörtern **nur `W12`** beitragen. Folglich ist NS.9 vollständig:
\[
\boxed{
(Ay)(t)
=(\log2)\alpha_1\alpha_2
\bigl(1+1_{t<\varepsilon}\bigr)f(t)
=(\log2)2^{-9/4}
\bigl(1+1_{t<\varepsilon}\bigr)f(t).
}
\tag{WL.10}
\]

Es existiert kein weiterer verdeckter Full-Rest-Term am zentralen Output.

### 7.2 Lokaler Schalenpunkt `a+t`, `0<t<h`

Die `+-2a`-Outputs von `W12` und `W32` beginnen frühestens bei `2a-h`, und wegen (WL.9)
\[
2a-h>a+h.
\]
Sie können daher `a+t` nicht erreichen. Der äußere `(3,0)`-Output beginnt bei
\[
a+2d-h>a+h
\]
weil `d>h`.

Somit tragen an `a+t` exakt nur

- `W22` mit Koeffizient
  \[
  (\log2)\alpha_2^2=(\log2)2^{-3}=q^2,
  \]
- der lokale `(3,0)`-Selbstterm mit Koeffizient `2r^2` unter der Maskenbedingung
  \[
  t\ge\delta-\varepsilon.
  \]

Damit ist auch NS.10/NS.11 vollständig:
\[
\boxed{
((I+A)y)(a+t)
=\bigl(1+q^2+2r^2 1_{t\ge\delta-\varepsilon}\bigr)f(t).
}
\tag{WL.11}
\]

## 8. Sauberer Zentralbereich

Im NS-Beweis tritt für `x<=R+e` der Punkt
\[
t=a-x\ge h
\]
auf, gleichzeitig wegen `x>R`
\[
t<a-R.
\]
Aus `h<=R` folgt
\[
a-R\le a-h.
\]
Der zentrale `W12`-Echo endet bei `|t|<h`, während alle übrigen aktiven Wörter frühestens an der ursprünglichen `a`-Schale `a-h` oder weiter außen beginnen. Daher gilt auf diesem gesamten Beweisbereich exakt
\[
\boxed{y(t)=(Ay)(t)=0.}
\tag{WL.12}
\]

Damit ist auch die saubere `d`-Gleichung NS.13 gegen alle elf Wörter abgesichert.

## 9. Verdict-Kandidat

Die Wort-für-Wort-Bilanz liefert:

- sechs `(2,0)`-Wörter identisch null;
- drei `(2,0)`-Wörter global aktiv;
- `(2,1)` identisch null;
- `(3,0)` global aktiv;
- nur `W12` am zentralen Echo;
- nur `W22` plus `(3,0)` an der lokalen `a`-Schale;
- kein aktives Wort im sauberen zentralen Beweisbereich.

Damit ist die von der unabhängigen Prüfung markierte Restunsicherheit **intern geschlossen**. Eine Promotion von NS-1 erfolgt daraus noch nicht; dafür bleibt die unabhängige GREEN-Bestätigung dieses Ledgers abzuwarten.

Bei unabhängigem GREEN wäre die zuvor vorgesehene Buchung zulässig:

- **NS-1a:** `✓[M]`;
- **NS-1:** `✓[M]_part`.

Keine Aussage über den vollständigen inneren Unsichtbarkeitsraum, den vollen Schur-Crossblock, Polar Gauge, Strong Terminal, Objekt X oder RH.
