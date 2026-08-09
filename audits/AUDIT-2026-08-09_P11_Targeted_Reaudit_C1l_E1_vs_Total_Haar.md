# P11 — Targeted Reaudit C1l: `E_1`-Moment versus totale Haarprojektion

**Datum:** 9. August 2026  
**Betroffener Knoten:** P11-C1l  
**Auslöser:** Typcheck vor P11-C1m  

**Urteil:**

\[
\boxed{\text{C1l bleibt im Haupt-No-Go gültig; nur }M_1=P_{Haar}\text{ wird SUPERSEDED.}}
\]

---

## 1. Zwei verschiedene Integrationen

P02 definiert

\[
(P_{Haar}F)(x)
=
\int_{\mathbb A_{\mathbb Q,f}}F(x,y)\,dy.
\]

Die BC-Rangeprojektion

\[
E_1=1_{\widehat{\mathbb Z}}
\]

ist dagegen nur die charakteristische Funktion des kompakten Unterrings `\widehat{\mathbb Z}\subset\mathbb A_f`.

Daher ist der in C1l definierte Momentkanal

\[
M_1F(x)
=
\int_{\mathbb A_f}F(x,y)E_1(y)\,dy
=
\int_{\widehat{\mathbb Z}}F(x,y)\,dy
\]

im Allgemeinen **nicht** gleich `P_Haar F`.

\[
\boxed{M_1\neq P_{Haar}\quad\text{auf }\mathcal S(\mathbb A_\mathbb Q)\text{ allgemein}.}
\]

---

## 2. Warum der Hauptbeweis aus C1l erhalten bleibt

Für

\[
\phi_n=E_n-\frac1nE_1
\]

gilt weiterhin

\[
\int_{\mathbb A_f}\phi_n(y)\,dy=0,
\]

weil beide Funktionen in `\widehat{\mathbb Z}` getragen sind und

\[
\operatorname{vol}(n\widehat{\mathbb Z})=1/n,
\qquad
\operatorname{vol}(\widehat{\mathbb Z})=1.
\]

Ebenso bleibt

\[
\int\phi_nE_n
=
\frac{n-1}{n^2}\neq0.
\]

Damit existieren weiterhin adelische Haar-Nullrichtungen, welche die BC-Rangeprojektionsmomente verändern.

Der zentrale Schluss

\[
\boxed{\text{BC-Labelmomente faktorieren nicht durch }R_{PW}}
\]

bleibt vollständig erhalten.

---

## 3. P02-Standardsektion

Für den expliziten P02-Surjektivitätslift

\[
F_a^{(0)}(x,y)=h_a(x)E_1(y)
\]

gilt wegen des Supports in `\widehat{\mathbb Z}` tatsächlich

\[
M_1F_a^{(0)}=P_{Haar}F_a^{(0)}=h_a.
\]

Diese Gleichheit ist also **sektionrelativ**, nicht global auf dem adelischen Amplitudenraum.

---

## 4. Korrigierter verfeinerter Porttyp

Ein künftiger BC-wertiger adelischer Port darf die totale Haarprojektion nicht durch die `E_n`-Momente ersetzen.

Der minimale Typ ist vielmehr

\[
\boxed{
F\longmapsto
\left(
P_{Haar}F,
(M_nF)_{n\in\mathcal P^*}
\right).
}
\]

Die erste Komponente erhält exakt den bisherigen P02-Port; die weiteren Komponenten speichern finite BC-Labelinformation.

Optional kann auch `M_1` separat mitgeführt werden, aber es ist redundant nur auf speziellen Quellunterräumen wie der P02-Standardsektion.

---

## 5. Präzedenzvermerk

```text
P11 Targeted Reaudit C1l E1-vs-Haar (dieses Dokument)
    > C1l §9 Formulierung M1=P_Haar.
```

Alle übrigen C1l-Befunde bleiben bindend.

---

## 6. Nächster Knoten

P11-C1m verwendet daher den korrigierten Porttyp

\[
\mathcal R_R F
=
\left(
P_{Haar}F,
(\langle F(x,\cdot),\zeta_n\rangle)_{n\in F_R}
\right),
\]

und prüft dessen endliche Gram-/Redundanzstruktur.
