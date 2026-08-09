# P11-C1n — Neutraler BC-Hub: exakte Sternzerlegung der Prime-Power-Labelgeometrie und archimedischer Ankerpilot

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1n]`  
**Vorgänger:** P11-C1k2, P11-C1m  
**Status:**

\[
\boxed{[P11-C1n]\quad\checkmark[K/M]_{\rm part}}
\]

Der kanonische BC-GCD-Labelraum der Prime-Power-Kanäle besitzt eine exakte orthogonale **Sternzerlegung**:

\[
\boxed{
K_{\mathcal P^*}
=
\mathbb C\zeta_1
\oplus
\bigoplus_p K_p^0.
}
\]

Alle Kreuzprimüberlappungen laufen ausschließlich über den neutralen BC-Vektor

\[
\zeta_1=E_1=1_{\widehat{\mathbb Z}}.
\]

Die primspezifischen Restanteile sind über verschiedene Primzahlen orthogonal. Damit entsteht eine kanonische globale Hub-Geometrie, die weder vollständig blockdiagonal noch ein Labelkollaps ist.

Relativ zum neutralen finite-adischen Anker liefert sie außerdem einen natürlichen **latenten** Archimedes–Prime-Kreuzblock. Die Intrinsizität dieses archimedischen Ankers auf dem vollen adelischen Quellenraum bleibt wegen C1l offen.

---

## 1. BC-GCD-Labelvektoren

Aus C1k2:

\[
\zeta_n
=
\sqrt n\,E_n
\in L^2(\widehat{\mathbb Z}),
\]

mit

\[
\boxed{
\langle\zeta_n,\zeta_m\rangle
=
\frac{\gcd(n,m)}{\sqrt{nm}}.
}
\]

Insbesondere

\[
\zeta_1=E_1
\]

und

\[
\boxed{
\langle\zeta_1,\zeta_n\rangle
=\frac1{\sqrt n}.}
\]

---

## 2. Zentrierte primspezifische Labelvektoren

Für jede Primzahlpotenz `p^k`, `k\ge1`, definiere

\[
\boxed{
\eta_{p,k}
:=
\zeta_{p^k}-p^{-k/2}\zeta_1.
}
\]

Dann

\[
\langle\eta_{p,k},\zeta_1\rangle
=
p^{-k/2}-p^{-k/2}=0.
\]

Also

\[
\boxed{\eta_{p,k}\perp\zeta_1.}
\]

---

## 3. Kreuzprimorthogonalität der zentrierten Reste

Seien `p\neq q`. Dann

\[
\gcd(p^k,q^\ell)=1,
\]

also

\[
\langle\zeta_{p^k},\zeta_{q^\ell}\rangle
=p^{-k/2}q^{-\ell/2}.
\]

Daher

\[
\begin{aligned}
\langle\eta_{p,k},\eta_{q,\ell}\rangle
={}&
\langle\zeta_{p^k},\zeta_{q^\ell}\rangle
-p^{-k/2}\langle\zeta_1,\zeta_{q^\ell}\rangle\\
&-q^{-\ell/2}\langle\zeta_{p^k},\zeta_1\rangle
+p^{-k/2}q^{-\ell/2}\langle\zeta_1,\zeta_1\rangle\\
={}&0.
\end{aligned}
\]

Somit

\[
\boxed{
\eta_{p,k}\perp\eta_{q,\ell}
\qquad(p\neq q).
}
\]

Status: `✓[K/M]`.

---

## 4. Gleicher Primkanal

Für dieselbe Primzahl gilt

\[
\langle\zeta_{p^k},\zeta_{p^\ell}\rangle
=p^{-|k-\ell|/2}.
\]

Daher

\[
\boxed{
\langle\eta_{p,k},\eta_{p,\ell}\rangle
=
p^{-|k-\ell|/2}-p^{-(k+\ell)/2}.
}
\]

Insbesondere

\[
\boxed{
\|\eta_{p,k}\|^2
=1-p^{-k}>0.
}
\]

Die primspezifischen Restvektoren sind also nicht trivial.

---

## 5. Exakte Sternzerlegung

Definiere

\[
K_p^0
:=
\overline{\operatorname{span}\{\eta_{p,k}:k\ge1\}}.
\]

Aus §§2–3:

\[
K_p^0\perp\zeta_1,
\qquad
K_p^0\perp K_q^0\quad(p\neq q).
\]

Da

\[
\zeta_{p^k}
=p^{-k/2}\zeta_1+\eta_{p,k},
\]

folgt für den von allen Prime-Power-Labelvektoren erzeugten Abschluss

\[
\boxed{
K_{\mathcal P^*}
=
\mathbb C\zeta_1
\oplus
\bigoplus_p K_p^0.
}
\]

Status: `✓[K/M]`.

---

## 6. Bedeutung: alle Kreuzprimblöcke laufen durch den neutralen Hub

Für `p\neq q`:

\[
\begin{aligned}
\langle\zeta_{p^k},\zeta_{q^\ell}\rangle
&=
\left\langle
p^{-k/2}\zeta_1+\eta_{p,k},
q^{-\ell/2}\zeta_1+\eta_{q,\ell}
\right\rangle\\
&=
\boxed{p^{-k/2}q^{-\ell/2}}.
\end{aligned}
\]

Die primspezifischen Restanteile tragen dazu nichts bei.

Damit besitzt die BC-Labelgeometrie die Form eines Sterns:

```text
           K_2^0
             \
K_3^0  ----  zeta_1  ---- K_5^0
             /
           K_7^0   ...
```

**Aber:** Die Prime-Power-Labels kollabieren nicht auf den Hub, weil jedes `K_p^0` nichttrivial bleibt und die endlichen GCD-Grammatrizen strikt positiv definit sind.

---

## 7. Kein Widerspruch zur P10-Rang-/Kopplungsfirewall

Der gemeinsame **Labelhub** `\mathbb C\zeta_1` ist eindimensional.

Nach Tensorierung mit dem analytischen Amplitudenraum wird daraus jedoch

\[
L^2(\mathbb R)\otimes\mathbb C\zeta_1
\cong L^2(\mathbb R),
\]

ein unendlichdimensionaler gemeinsamer Kanal.

Daher darf aus der eindimensionalen Labelkomponente **nicht** geschlossen werden, die gesamte globale Kopplung sei endlich-rangig.

Ebenso wird kein historischer Rang-eins-Projektor `P_p=|c_p|^2\Pi_p` wieder eingeführt; C1n beschreibt einen anderen Tensorfaktor.

---

## 8. Kombination mit der analytischen Prime-Power-Inzidenz

Aus C1c/C1k2:

\[
\mathcal V_{p,k}a
:=
\sqrt{w_{p,k}}\,D_{k\log p}a
\otimes\zeta_{p^k},
\qquad
w_{p,k}=\frac{\log p}{p^{k/2}}.
\]

Mit der Sternzerlegung:

\[
\boxed{
\mathcal V_{p,k}a
=
\underbrace{
\sqrt{w_{p,k}}p^{-k/2}D_{k\log p}a\otimes\zeta_1
}_{\text{globaler neutraler Hubanteil}}
+
\underbrace{
\sqrt{w_{p,k}}D_{k\log p}a\otimes\eta_{p,k}
}_{\text{primspezifischer Anteil}}.
}
\]

Für verschiedene Primzahlen entsteht ihr Kreuzblock **ausschließlich** aus dem ersten Term.

---

## 9. Expliziter Kreuzprimblock in Hubform

Für `p\neq q`:

\[
\boxed{
\begin{aligned}
\langle\mathcal V_{p,k}a,\mathcal V_{q,\ell}b\rangle
={}&
\sqrt{w_{p,k}w_{q,\ell}}
\,p^{-k/2}q^{-\ell/2}\\
&\times
\langle D_{k\log p}a,D_{\ell\log q}b\rangle.
\end{aligned}
}
\]

Dies ist exakt dieselbe C1k2-Kreuzform, nun strukturell als **gemeinsame neutrale BC-Hubüberlappung** erklärt.

---

## 10. Archimedischer neutraler Anker — Pilot

Der archimedische Gamma-Inzidenzkanal aus C1d besitzt keinen Prime-Power-Labelindex. Auf dem Tensorproduktpilot ist daher der finite-adisch **neutrale** Vektor

\[
\boxed{\zeta_\infty^{(0)}:=\zeta_1=E_1}
\]

der minimale ausgezeichnete Kandidat.

Er wird zusätzlich durch den P02-Standardlift

\[
F_a^{(0)}(x,y)=h_a(x)E_1(y)
\]

motiviert.

Dann gilt für jedes Prime-Power-Label

\[
\boxed{
\langle\zeta_\infty^{(0)},\zeta_{p^k}\rangle
=p^{-k/2}.}
\]

Damit entsteht ein natürlicher Archimedes–Prime-Labelkoeffizient.

**Firewall aus C1l:** Der volle Haar-Port selektiert diese finite-adische Richtung nicht liftunabhängig. Daher ist `\zeta_\infty=\zeta_1` als **Tensorprodukt-/Standardsektionspilot** kanonisch, aber noch nicht als intrinsischer Deszent auf dem gesamten `R_PW`-Quotienten bewiesen.

---

## 11. Latenter Archimedes–Prime-Gramblock

Für eine archimedische Kantenlänge `s>0` setze formal im Pilot

\[
\mathcal V_{\infty,s}a
:=
\sqrt{\omega_\infty(s)}D_sa\otimes\zeta_1.
\]

Dann für ein Prime-Power-Label `(p,k)`:

\[
\boxed{
\begin{aligned}
\langle\mathcal V_{\infty,s}a,\mathcal V_{p,k}b\rangle
={}&
p^{-k/2}
\sqrt{\omega_\infty(s)w_{p,k}}\\
&\times
\langle D_sa,D_{k\log p}b\rangle.
\end{aligned}
}
\]

Für jede **endliche** Menge archimedischer Kantenlängen und Prime-Power-Labels ist die gesamte Blockmatrix automatisch PSD, weil sie ein gewöhnlicher Tensorprodukt-Gramkern ist.

Status: `✓[M]` als endlicher Tensorproduktpilot; kontinuierlicher globaler Synthese-/Integrationsabschluss `?[O]`.

---

## 12. Warum dies noch keine additive Weil-Kopplung ist

Die in §§8–11 auftretenden Kreuzblöcke sind **latente Gramwerte** einer größeren positiven Vorstruktur.

Sie dürfen nicht als zusätzliche Terme zu

\[
B_W=B_\Gamma+B_{\rm fin}+B_{\rm pole}
\]

addiert werden.

Die weiterhin offene Aufgabe lautet, einen gemeinsamen Quellen-/Kompressionsoperator zu konstruieren, dessen positiver Gramraum diese Hubgeometrie trägt und dessen komprimierte Form exakt den eingefrorenen Weilblock bzw. eine kontrollierte Approximation reproduziert.

NEU-250/P10 bleiben unverändert bindend.

---

## 13. Statusmatrix

| Aussage | Status |
|---|---|
| `eta_{p,k}=zeta_{p^k}-p^{-k/2}zeta_1` | `✓[K/M]` |
| `eta_{p,k}\perp zeta_1` | `✓[K/M]` |
| `K_p^0\perp K_q^0` für `p\neq q` | `✓[K/M]` |
| Sternzerlegung `K_P*=C zeta_1 ⊕ ⊕_p K_p^0` | `✓[K/M]` |
| alle Crossprime-GCD-Blöcke durch neutralen Hub | `✓[K/M]` |
| Labelhub eindimensional => Gesamtoperator endlich-rangig | `×[M]` als Schluss |
| analytisch getensorierter Prime-Hub | `✓[K/M]` |
| neutraler archimedischer Anker `zeta_infty=zeta_1` relativ zum Tensor-/Standardsektionspilot | `✓[M]` |
| derselbe Anker intrinsisch auf vollem `R_PW`-Quotienten | `?[O]` |
| endliche gemischte Archimedes–Prime-Grammatrizen PSD | `✓[M]` |
| kontinuierlicher globaler Hub-Syntheseabschluss | `?[O]` |
| exakte Weil-Kompression | `?[O]` |

---

## 14. Wichtigster P11-Befund

Die globale Prime-Power-Kopplung besitzt nun eine sehr konkrete Quellengeometrie:

\[
\boxed{
\text{gemeinsamer neutraler BC-Hub}
\oplus
\text{primspezifische orthogonale Restgeometrien}.
}
\]

Dies vereinigt zwei zuvor getrennte Anforderungen:

1. **Markierungserhalt:** die `K_p^0` bleiben verschieden;
2. **Nichtorthogonalität:** alle Primkanäle teilen den neutralen Hub.

Der archimedische Kanal besitzt im natürlichen Tensorproduktpilot denselben neutralen finite-adischen Anker.

Damit ist eine erste echte **globale Kandidatengeometrie** sichtbar — weiterhin ohne Behauptung, dass ihre Source-Kompression bereits `B_W` positiv realisiert.

---

## 15. Nächster Knoten

\[
\boxed{[P11\text{-}C1o]\quad\text{Source-Kompressionsaudit der neutralen Hubgeometrie}.}
\]

Zu prüfen ist:

1. welche positive Form auf dem verfeinerten adelischen Port `(P_Haar,M_R)` natürlich von der Hubzerlegung induziert wird;
2. wie ihre Kompression auf den skalaren P02-Testkern aussieht;
3. ob der Unterschied zur exakten endlichen Weilform als expliziter Restoperator `R_R` geschrieben werden kann;
4. ob irgendein Teil dieses Rests entlang `R\to\infty` strukturell verschwindet, ohne RH/Nullstellen als Input.
