# P11-C1c — Zentrierter Prime-Power-Inzidenz-Gramkern

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1c]` — liftfreier Gramkern direkt aus der gemeinsamen Quelle  
**Vorgänger:** P11-C1, P11-C1b  
**Primärbasis:** P02 (`\mathcal A_{PW}`, Translations-/Korrelationsstruktur, `B_{\rm fin}`), P05 (Prime-Power-Zeiten und Gewichte)  

**Urteil:**

\[
\boxed{[P11-C1c]\quad\checkmark[K/M]_{\rm part}}
\]

Es existiert RH-frei, liftfrei und vollständig prime-power-typisiert ein kanonischer positiver Gramkern aus **zentrierten Translationsdifferenzen**. Außerdem besitzt der endliche primarithmetische Weilblock eine exakte Darstellung als positive Dirichlet-/Inzidenzenergie minus einen skalaren Gegenblock. Die Identifikation dieser neuen Off-Diagonalgeometrie mit der vollständigen Objekt-X-Kopplung bleibt offen.

---

## 1. Bindende gemeinsame Quelle

P02 fixiert

\[
\mathcal A_{\rm PW}=C_c^\infty(\mathbb R;\mathbb C)
\subset L^2(\mathbb R,du)
\]

und den Translationsfluss

\[
(U_ta)(u):=a(u+t).
\]

Für `a,b\in\mathcal A_{PW}` gilt

\[
C_{a,b}(t)=\langle U_ta,b\rangle_{L^2}
\]

und

\[
g_{a,b}(t)
=\frac12\bigl(
\langle U_ta,b\rangle+
\langle U_{-t}a,b\rangle
\bigr).
\]

P05/P02 fixieren für jede Primzahlpotenz

\[
\ell_{p,m}:=m\log p,
\qquad
w_{p,m}:=\frac{\log p}{p^{m/2}}
=\frac{\Lambda(p^m)}{\sqrt{p^m}}>0.
\]

Keine Primhebung tritt in diesen Daten auf.

---

## 2. Definition des zentrierten Inzidenzoperators

Für jeden Prime-Power-Index

\[
\alpha=(p,m)
\]

definiere

\[
\ell_\alpha=m\log p,
\qquad
w_\alpha=\frac{\log p}{p^{m/2}}
\]

und

\[
\boxed{
D_\alpha
:=
U_{\ell_\alpha/2}-U_{-\ell_\alpha/2}.
}
\]

Der Operator vergleicht zwei um die Null symmetrisch gelegene logarithmische Positionen. Er ist daher die zentrierte Translationsversion einer orientierten Prime-Power-Kante.

Gewichtete Analyseabbildung:

\[
\boxed{
V_\alpha
:=
\sqrt{w_\alpha}\,D_\alpha.
}
\]

Für jeden einzelnen `\alpha` ist `V_\alpha` ein beschränkter Operator auf `L^2`, und er erhält `\mathcal A_{PW}`.

---

## 3. Exakte Dirichlet-Identität

Da `U_t` unitär ist,

\[
\begin{aligned}
\langle D_\alpha a,D_\alpha b\rangle
&=
\left\langle
(U_{\ell/2}-U_{-\ell/2})a,
(U_{\ell/2}-U_{-\ell/2})b
\right\rangle\\
&=
2\langle a,b\rangle
-\langle U_\ell a,b\rangle
-\langle U_{-\ell}a,b\rangle\\
&=
2\langle a,b\rangle-2g_{a,b}(\ell),
\end{aligned}
\]

mit `\ell=\ell_\alpha`.

Somit

\[
\boxed{
-2w_\alpha g_{a,b}(\ell_\alpha)
=
w_\alpha\langle D_\alpha a,D_\alpha b\rangle
-2w_\alpha\langle a,b\rangle.
}
\]

Dies ist eine exakte algebraische Identität.

---

## 4. Endlicher Primzahlpotenzblock als positive Energie minus Gegenblock

Für eine endliche Indexmenge `F` von Prime-Power-Labels setze

\[
B_{\rm fin}^{F}(a,b)
:=-2\sum_{\alpha\in F}
w_\alpha g_{a,b}(\ell_\alpha).
\]

Definiere

\[
\mathcal E_F(a,b)
:=
\sum_{\alpha\in F}
\langle V_\alpha a,V_\alpha b\rangle
=
\sum_{\alpha\in F}w_\alpha
\langle D_\alpha a,D_\alpha b\rangle
\]

und

\[
W_F:=\sum_{\alpha\in F}w_\alpha.
\]

Dann gilt exakt

\[
\boxed{
B_{\rm fin}^{F}(a,b)
=
\mathcal E_F(a,b)
-2W_F\langle a,b\rangle_{L^2}.
}
\]

Dabei ist

\[
\boxed{\mathcal E_F(a,a)\ge0}
\]

für jedes `a`.

Status: `✓[K/M]`.

---

## 5. Neuer liftfreier Prime–Prime-/Prime-Power-Gramkern

Da **alle** `V_\alpha` in denselben Hilbertraum `L^2(\mathbb R)` abbilden, definiere für beliebige Prime-Power-Labels

\[
\boxed{
G_{\alpha\beta}(a,b)
:=
\langle V_\alpha a,V_\beta b\rangle
=
\sqrt{w_\alpha w_\beta}
\langle D_\alpha a,D_\beta b\rangle.
}
\]

Für

\[
\alpha=(p,m),\qquad\beta=(q,n)
\]

ist dies eine explizite Formel für

\[
G_{(p,m),(q,n)}.
\]

Sie verwendet nur:

- die gemeinsame Testfunktionsebene `\mathcal A_{PW}`;
- den kanonischen Translationsfluss `U_t`;
- die arithmetischen Zeiten `m\log p`;
- die exakten positiven Halbgewichte `\sqrt{\log p/p^{m/2}}`.

Sie verwendet **keine** Primhebung, keine Nullstellen und keine RH-Annahme.

---

## 6. Positive Definitheit des vollständigen Labelkerns

Sei `F` eine endliche Menge von Prime-Power-Labels und seien `a_\alpha\in\mathcal A_{PW}` beliebig. Dann

\[
\begin{aligned}
\sum_{\alpha,\beta\in F}
G_{\alpha\beta}(a_\alpha,a_\beta)
&=
\sum_{\alpha,\beta\in F}
\langle V_\alpha a_\alpha,V_\beta a_\beta\rangle\\
&=
\left\|
\sum_{\alpha\in F}V_\alpha a_\alpha
\right\|_{L^2}^2\\
&\ge0.
\end{aligned}
\]

Also

\[
\boxed{G=(G_{\alpha\beta})\text{ ist ein positiver operatorwertiger Gramkern auf allen endlichen Prime-Power-Trunkierungen.}}
\]

Hermiteschkeit ist automatisch:

\[
G_{\beta\alpha}(b,a)
=
\overline{G_{\alpha\beta}(a,b)}.
\]

Status: `✓[K/M]`.

---

## 7. Explizite Kreuzblockformel

Aus

\[
D_\alpha^*=-D_\alpha
\]

(für die zentrierte Differenz) und direkter Expansion folgt als Formkern

\[
G_{\alpha\beta}(a,b)
=
\sqrt{w_\alpha w_\beta}
\bigl[
\langle U_{(\ell_\alpha-\ell_\beta)/2}a,b\rangle
-\langle U_{(\ell_\alpha+\ell_\beta)/2}a,b\rangle
\]
\[
\qquad
-\langle U_{-(\ell_\alpha+\ell_\beta)/2}a,b\rangle
+\langle U_{-(\ell_\alpha-\ell_\beta)/2}a,b\rangle
\bigr].
\]

Damit hängen Prime–Prime-Kreuzblöcke ausschließlich von den **Summen und Differenzen der logarithmischen Prime-Power-Zeiten** ab.

Für `p\neq q` ist dies eine echte arithmetisch bestimmte Off-Diagonalformel; Nichtnullheit für jedes einzelne Paar wird nicht behauptet.

---

## 8. Verhältnis zur P05-Kollisionsfirewall

P05 beweist, dass eine direkte algebraische Kreuzprimkollision

\[
pm_p=qm_q
\]

nicht auf dem Mangoldt-Träger liegt.

Der neue Gramkern benutzt jedoch keine solche Zielindexkollision. Seine Off-Diagonalität entsteht aus gemeinsamen Translationen im analytischen Quellraum:

\[
\ell_{p,m}\pm\ell_{q,n}
=
\log(p^m q^{\pm n}).
\]

Daher besteht kein Widerspruch zu P05 §9.

\[
\boxed{
\text{direkte Kreuzprimkollision}\neq\text{Translations-Gramüberlappung}.
}
\]

---

## 9. Verhältnis zu NEU-250 / P10

Der Kern `G_{\alpha\beta}` darf **nicht** als neuer vierter Summand zu `B_W` addiert werden.

Er ist vielmehr Kandidat für eine **nichtorthogonale Faktorisierungsgeometrie**.

Besonders wichtig:

- die Diagonalspur
  \[
  \sum_{\alpha\in F}G_{\alpha\alpha}(a,b)=\mathcal E_F(a,b)
  \]
  reproduziert nicht direkt `B_{\rm fin}^F`, sondern
  \[
  B_{\rm fin}^F=\mathcal E_F-2W_F\langle\cdot,\cdot\rangle;
  \]
- die echten Off-Diagonalblöcke `G_{\alpha\beta}`, `\alpha\neq\beta`, sind in der expliziten Weil-Zerlegung nicht als zusätzliche Terme sichtbar;
- sie dürfen daher nur innerhalb einer Umverteilung/Faktorisierung verwendet werden, deren Gesamtkompression exakt `B_W` erhält.

Dies respektiert das Additiv-Kreuzterm-No-Go aus NEU-250.

---

## 10. Globaler Summierbarkeits-Firewall

Für jedes feste `\alpha` ist `V_\alpha` beschränkt. Aber die naive direkte Summe

\[
a\longmapsto(V_\alpha a)_\alpha
\]

liegt im Allgemeinen **nicht** in

\[
\bigoplus_\alpha^{\ell^2}L^2,
\]

denn

\[
\sum_\alpha\|V_\alpha a\|_2^2
\]

ist ohne regulatorische Struktur im Allgemeinen nicht endlich.

Tatsächlich gilt für hinreichend große Verschiebung relativ zum kompakten Träger von `a`:

\[
\langle U_{\ell_\alpha}a,a\rangle=0,
\]

also

\[
\|D_\alpha a\|_2^2=2\|a\|_2^2.
\]

Da bereits der `m=1`-Anteil

\[
\sum_p\frac{\log p}{\sqrt p}
\]

divergiert, divergiert die naive direkte Energie.

\[
\boxed{
\text{Der positive Kern existiert auf endlichen Labelmengen; der naive }\ell^2\text{-Globalabschluss ist nicht zulässig.}
}
\]

Dies stimmt mit der NEU-250-Warnung gegen eine ungeprüfte primarithmetische `\ell^2`-Direktsumme überein.

---

## 11. Interpretation: Prime-Power-Kanten als zentrierte Differenzen

Der Operator

\[
D_{p,m}=U_{m\log p/2}-U_{-m\log p/2}
\]

ist eine analytische Inzidenzabbildung entlang einer logarithmischen Kante der Länge

\[
m\log p.
\]

Damit entsteht erstmals eine direkte Brücke zwischen

\[
\text{relativer Primkanten-Geometrie (P05)}
\]

und

\[
\text{gemeinsamer analytischer Amplituden-/Translationsgeometrie (P02)}.
\]

Diese Brücke ist RH-frei und benötigt keine Fourierhebung eines einzelnen Primkanals.

---

## 12. Statusmatrix

| Aussage | Status |
|---|---|
| `D_{p,m}=U_{m log p/2}-U_{-m log p/2}` kanonisch definiert | `✓[K/M]` |
| `V_{p,m}=sqrt(w_{p,m})D_{p,m}` liftfrei | `✓[K/M]` |
| Prime-Power-Gramkern `G_{alpha beta}=V_alpha^*V_beta` auf endlichen Trunkierungen PSD | `✓[K/M]` |
| vollständige `(p,m),(q,n)`-Verfeinerung | `✓[K/M]` auf endlichen Labelmengen |
| exakte Identität `B_fin^F=E_F-2W_F<.,.>` | `✓[K/M]` |
| naive unendliche `ell^2`-Direktsumme | `×[M]` als globaler Abschluss |
| `G_{alpha beta}` als zusätzlicher Weil-Summand | `×[M]` durch NEU-250-Firewall |
| Nutzung von `G` in einer exakten nichtorthogonalen Faktorisierung von `B_W` | `?[O]` |
| gemeinsamer positiver Grenzraum nach regulatorischer/renormierter Vervollständigung | `?[O]` |

---

## 13. Wichtigster neuer P11-Befund

Vor C1c war ein liftfreier Ursprung von Prime–Prime-Kreuzblöcken offen.

Nach C1c existiert ein expliziter Kandidat:

\[
\boxed{
G_{(p,m),(q,n)}
=
\sqrt{\frac{\log p}{p^{m/2}}\frac{\log q}{q^{n/2}}}
\,D_{p,m}^*D_{q,n}
}
\]

(im Form-Sinn auf `\mathcal A_{PW}`), wobei

\[
D_{p,m}=U_{m\log p/2}-U_{-m\log p/2}.
\]

Dies ist **noch nicht Objekt X**, aber erstmals im P11-Strang ein konkreter, liftfreier, RH-freier, vollständig prime-power-indizierter positiver Gramkern mit natürlichen Off-Diagonalblöcken.

---

## 14. Nächster Knoten

\[
\boxed{[P11\text{-}C1d]\quad\text{Kann der zentrierte Inzidenzkern mit Gamma-/Polgeometrie zu einer cutoff-kompatiblen Faktorisierung von }B_W\text{ gekoppelt werden?}}
\]

Erster Test:

\[
B_W^F
=
\underbrace{\mathcal E_F}_{\ge0}
+
\underbrace{\bigl(B_\Gamma+B_{\rm pole}-2W_F\langle\cdot,\cdot\rangle\bigr)}_{\text{Restblock}}
\]

und Prüfung, ob der Restblock eine **kanonische**, cutoff-kompatible archimedische Faktorisierung oder Umverteilung besitzt, ohne RH-Positivität vorauszusetzen.
