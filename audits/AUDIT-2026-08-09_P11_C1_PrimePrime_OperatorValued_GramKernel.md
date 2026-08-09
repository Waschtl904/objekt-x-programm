# P11-C1 — Prime–Prime Operator-Valued Gram Kernel

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1]` — Prime–Prime-Überlappungsoperator  
**Vorgänger:** `AUDIT-2026-08-09_P11_PassA_Opening_SourceFirst_Global_Coupling.md`  
**Primärquelle:** P05 §6–§7, insbesondere die gemeinsame Spektralmaßform

\[
\mu_{pq}^{a,b}(B):=\langle V_pa,E_D(B)V_qb\rangle.
\]

**Urteil:**

\[
\boxed{[P11-C1]\quad\checkmark[M]_{\rm part}}
\]

Für jede **fest gewählte** Familie von Primkanalabbildungen `V_p` in denselben Hilbertraum mit gemeinsamer PVM `E_D` ist die Matrix der Überlappungsmaße ein positiver operatorwertiger/maßwertiger Gramkern. Die intrinsische Kanonizität dieser Familie und die Identifikation mit der globalen Weil-Kopplung bleiben offen.

---

## 1. Typisierte Ausgangslage

P05 liefert für Primkanalabbildungen `V_p,V_q` und die projektionswertige Spektralauflösung `E_D` eines gemeinsamen selbstadjungierten Transportoperators die Maße

\[
\mu_{pq}^{a,b}(B)
:=
\langle V_pa,E_D(B)V_qb\rangle.
\]

Außerdem

\[
\langle a,K_{pq}(z)b\rangle
=
\int_{\mathbb R}\frac{d\mu_{pq}^{a,b}(\lambda)}{\lambda-z}.
\]

P05 verwendet diese Formel als Ersatz für die historisch falsche diskrete Eigenbasislesart und hält ausdrücklich fest, dass verschiedene Primkanalbilder nicht orthogonal sein müssen.

---

## 2. Hermitesche Symmetrie

Da `E_D(B)=E_D(B)^*` für jede borelsche Menge `B`, gilt

\[
\begin{aligned}
\mu_{qp}^{b,a}(B)
&=\langle V_qb,E_D(B)V_pa\rangle\\
&=\overline{\langle V_pa,E_D(B)V_qb\rangle}\\
&=\overline{\mu_{pq}^{a,b}(B)}.
\end{aligned}
\]

Damit ist die Primblockmatrix

\[
\bigl(\mu_{pq}^{a_p,a_q}(B)\bigr)_{p,q\in S}
\]

für jedes endliche `S` hermitesch.

\[
\boxed{\mu_{qp}^{b,a}=\overline{\mu_{pq}^{a,b}}.}
\]

Status: `✓[M]`.

---

## 3. Positive Definitheit endlicher Primblockmatrizen

Sei `S` eine endliche Primmenge und seien `a_p` beliebige zulässige Kanalvektoren. Dann

\[
\begin{aligned}
\sum_{p,q\in S}\mu_{pq}^{a_p,a_q}(B)
&=
\sum_{p,q\in S}
\langle V_pa_p,E_D(B)V_qa_q\rangle\\
&=
\left\langle
\sum_{p\in S}V_pa_p,
E_D(B)\sum_{q\in S}V_qa_q
\right\rangle.
\end{aligned}
\]

Da `E_D(B)` eine orthogonale Projektion ist,

\[
\left\langle x,E_D(B)x\right\rangle
=
\|E_D(B)x\|^2\ge0.
\]

Somit

\[
\boxed{
\sum_{p,q\in S}\mu_{pq}^{a_p,a_q}(B)
=
\left\|E_D(B)\sum_{p\in S}V_pa_p\right\|^2
\ge0.
}
\]

Äquivalent ist für jedes `B` die Matrix

\[
\boxed{
\bigl(\mu_{pq}^{a_p,a_q}(B)\bigr)_{p,q\in S}\ge0.
}
\]

Status: `✓[M]`.

Dies ist keine RH-Annahme und keine Positivitätsannahme über die Weilform; es ist reine Hilbertraum-/PVM-Grampositivität auf der bereits von P05 typisierten gemeinsamen Zielstruktur.

---

## 4. Der ungespektralisierte Gramkern

Setzt man `B=\mathbb R`, so ist `E_D(\mathbb R)=I`. Daher

\[
\mu_{pq}^{a,b}(\mathbb R)
=
\langle V_pa,V_qb\rangle.
\]

Damit existiert relativ zur gewählten Familie `V_p` der natürliche Kreuzblock

\[
\boxed{
G_{pq}(a,b):=\langle V_pa,V_qb\rangle.
}
\]

Falls die `V_p` als beschränkte Operatoren zwischen festgelegten Hilberträumen vorliegen, ist formal

\[
\boxed{G_{pq}=V_p^*V_q.}
\]

Ohne eine solche globale Beschränktheit wird `G_{pq}` nur als sesquilineare Form auf dem gemeinsamen Kern gebucht.

Für jede endliche Primmenge `S`:

\[
\sum_{p,q\in S}G_{pq}(a_p,a_q)
=
\left\|\sum_{p\in S}V_pa_p\right\|^2\ge0.
\]

Damit ist `G=(G_{pq})` ein positiver Gramkern.

---

## 5. Nichtorthogonalität bekommt eine exakte Bedeutung

Für ein Paar `p\neq q` gilt

\[
G_{pq}\equiv0
\]

exactly dann, wenn die betreffenden Kanalbilder auf dem betrachteten Kern orthogonal sind.

P05 beweist nur:

\[
\text{Primblockdiagonalität ist nicht strukturell erzwungen.}
\]

Daraus darf **nicht** gefolgert werden

\[
G_{pq}\neq0\quad\forall p\neq q.
\]

Die C1-Konstruktion respektiert diese Firewall: sie erzeugt den Kreuzblock aus der Überlappung, ohne Nichtnullheit künstlich vorzugeben.

---

## 6. Spektralisierte positive Kerne

Allgemeiner: Für jede beschränkte nichtnegative borelsche Funktion `\varphi\ge0` ist

\[
\int\varphi(\lambda)\,d\mu_{pq}^{a,b}(\lambda)
=
\langle V_pa,\varphi(D)V_qb\rangle.
\]

Daher

\[
\sum_{p,q\in S}
\int\varphi(\lambda)\,d\mu_{pq}^{a_p,a_q}(\lambda)
=
\left\|\varphi(D)^{1/2}\sum_{p\in S}V_pa_p\right\|^2\ge0.
\]

Das liefert eine ganze Familie positiver Primblock-Gramkerne.

**Firewall:** Der Resolventenkern `(D-z)^{-1}` ist für allgemeines komplexes `z` kein positiver Funktionalkalkül. Aus der Positivität der Maße folgt daher **nicht**, dass `K_{pq}(z)` eine positive Blockmatrix ist.

---

## 7. Was damit tatsächlich gewonnen ist

Der P11-Eröffnungsverdacht wird bestätigt:

\[
\boxed{
B_{pq}\text{-artige Off-Diagonalität muss nicht ad hoc erfunden werden.}
}
\]

Innerhalb einer gemeinsamen Hilbertraumrealisierung entsteht sie automatisch als Gramüberlappung

\[
V_p^*V_q
\]

bzw. als spektral verfeinerter maßwertiger Kern

\[
V_p^*E_D(\cdot)V_q.
\]

Damit existiert ein **mathematisch natürlicher Ursprung** von Prime–Prime-Kreuzblöcken.

---

## 8. Warum C1 nur partiell geschlossen ist

Vier zentrale Punkte bleiben offen.

### C1-a — Kanonizität der `V_p`

P05 trennt Rohkopplung, hebungsinduzierten Kanal und relative Rang-eins-Realisierung. Nichtentartung und Hebungsunabhängigkeit der Kanalgewichte sind offen. Daher ist noch nicht bewiesen, dass die konkrete Familie `V_p` selbst kanonisch aus den Objekt-X-Daten folgt.

### C1-b — Liftunabhängigkeit des Gramkerns

Zu prüfen ist

\[
G_{pq}^{[\widehat\varepsilon_p,\widehat\varepsilon_q]}
\stackrel{?}{=}
G_{pq}^{\rm intrinsic}
\]

oder wenigstens eine kanonische Äquivalenzklasse nach Quotientenbildung.

### C1-c — Prime-Power-Verfeinerung

Objekt X benötigt vollständige Labels `(p,m)`, nicht nur Primlabels. Offen ist die kanonische Erweiterung

\[
G_{(p,m),(q,n)}.
\]

### C1-d — Weil-Identifikation

Die Grampositivität von `G_{pq}` beweist **nicht**

\[
B_W(f,g)=\left\langle\mathcal T_Xf,\mathcal T_Xg\right\rangle_X.
\]

Sie liefert nur einen positiven Überlappungsmechanismus. Die exakte arithmetische Gewichtung, der archimedische Kanal und die Kompression auf die vollständige Weilform bleiben zu beweisen.

---

## 9. Statusreconciliation

| Teilfrage | Status |
|---|---|
| Hermiteschkeit von `\mu_{pq}` | `✓[M]` |
| PSD endlicher Primblockmatrizen für jedes PVM-Ereignis `B` | `✓[M]` |
| ungespektralisierter Gramkern `G_{pq}(a,b)=<V_pa,V_qb>` | `✓[M]` relativ zu fixer `V_p`-Familie |
| positiver Funktionalkalkül `\varphi(D)`, `\varphi\ge0` | `✓[M]` |
| Positivität des komplexen Resolventenkerns | **nicht behauptet** |
| kanonische/liftunabhängige `V_p` | `?[O]` |
| liftunabhängiger intrinsischer `G_{pq}` | `?[O]` |
| Prime-Power-Kern `G_{(p,m),(q,n)}` | `?[O]` |
| Identifikation dieses Gramkerns mit der vollständigen Objekt-X-/Weil-Kopplung | `?[O]` |

---

## 10. Strategischer Befund

Vor C1 lautete der Engpass grob:

\[
\text{„Woher kommt }B_{pq}\text{?“}
\]

Nach C1 lautet er präziser:

\[
\boxed{
\text{„Woher kommt die kanonische gemeinsame Familie }V_p\text{, deren Gramkern }V_p^*V_q\text{ die Kreuzblöcke liefert?“}
}
\]

Das ist ein echter Fortschritt der Problemtypisierung: **die Off-Diagonalform selbst ist nicht mehr das primäre unbekannte Objekt; die Kanonisierung der gemeinsamen Primkanal-Einbettung ist es.**

---

## 11. Nächster Knoten

\[
\boxed{[P11\text{-}C1b]\quad\text{Lift-/Quotienteninvarianz des Gramkerns }G_{pq}.}
\]

Zu prüfen ist zuerst, ob die bereits in P05 vorhandene Nullraum-/Quotientenarchitektur genügt, um Änderungen der Primhebung in radikale Richtungen zu absorbieren und dadurch `G_{pq}` auf eine kanonische Quotientenebene absteigen zu lassen.
