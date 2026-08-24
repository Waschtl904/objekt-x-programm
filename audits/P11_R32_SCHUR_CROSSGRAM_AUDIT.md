# P11/R32 — Schur-Cross-Gram-Transversalität nach P12

**Status:** Kandidat; keine Promotion.  
**Vorausgesetzte Rückbindung:** `audits/P11_P12_R32_RUECKBINDUNG_AUDIT.md` (selbst noch im unabhängigen Review).  
**P11:** FROZEN. R14 unverändert.  
**Ziel:** den nach P12 verbleibenden Schur-Annihilator-Kern in eine exakte nichtorthogonale Gram-/Transversalitätsfrage umschreiben.

---

## 1. Mediatorfaktor des festen Schurterms

Fixiere `T0` und schreibe
\[
H:=H_{T_0},
\qquad
B:=B_{T_0}=(I+R_{T_0}^*R_{T_0})^{-1}.
\]
Da `R_{T0}` beschränkt ist,
\[
0<(1+\|R_{T_0}\|^2)^{-1}I\le B\le I,
\]
also ist `B^{1/2}` beschränkt, positiv und beschränkt invertierbar.

Definiere den festen endlichen Mediator
\[
\boxed{
\mathscr M:=B^{1/2}H^*.
}
\tag{CG.1}
\]
Dann gilt exakt
\[
\boxed{
\Sigma_{T_0}=HBH^*=\mathscr M^*\mathscr M.
}
\tag{CG.2}
\]

Dies ist keine neue Positivitätsannahme, sondern die vorhandene Feshbach-Schur-Faktorisierung in Gramform.

---

## 2. Inneres und annulares Mediatorbild

Seien

- `E_I` die Nullfortsetzung des inneren Quellfensters `I=(-R,R)`;
- `E_A` die Nullfortsetzung des Annulus `A=(-S,-R) union (R,S)`.

Auf den jeweils relevanten Paritätssektoren setze
\[
\boxed{
\mathscr M_I:=\mathscr M E_I,
\qquad
\mathscr M_A:=\mathscr M E_{\mathcal A}.
}
\tag{CG.3}
\]

Der annularisierte Schur-Crossblock ist
\[
\mathcal T_{A,I}
:=E_{\mathcal A}^*\Sigma_{T_0}E_I.
\]
Mit (CG.2) folgt unmittelbar
\[
\boxed{
\mathcal T_{A,I}=\mathscr M_A^*\mathscr M_I,
\qquad
\mathcal T_{A,I}^*=\mathscr M_I^*\mathscr M_A.
}
\tag{CG.4}
\]

Damit ist der Schur-Crossblock exakt ein Cross-Gram-Operator der beiden Mediatorbilder.

---

## 3. Exakte Charakterisierung aller Schur-Annihilatoren

Setze
\[
\mathcal N_I:=\overline{\operatorname{Ran}\mathscr M_I}
\]
und sei `P_I` die orthogonale Projektion des Mediatorraums auf `N_I`.

Für einen Annulusvektor `w` gilt
\[
\begin{aligned}
\mathcal T_{A,I}^*w=0
&\iff \mathscr M_I^*\mathscr M_Aw=0\\
&\iff \mathscr M_Aw\perp\operatorname{Ran}\mathscr M_I\\
&\iff P_I\mathscr M_Aw=0.
\end{aligned}
\]
Also
\[
\boxed{
\ker\mathcal T_{A,I}^*
=
\{w:\mathscr M_Aw\in\mathcal N_I^\perp\}
=
\ker(P_I\mathscr M_A).
}
\tag{CG.5}
\]

Dies ist die exakte post-P12-Annihilatorfrage.

---

## 4. Was P12 zusätzlich für den Mediator liefert

Im P12-Drei-Shift-Fenster und auf einem **global bewiesenen** P12-Injektivitätsstratum gilt nach der Rückbindungsidentität
\[
\ker(H E_{\mathcal A}|_-)=0.
\]
Wegen
\[
H^*=-H
\]
und der Invertierbarkeit von `B^{1/2}` folgt
\[
\boxed{
\ker\mathscr M_A=0.
}
\tag{CG.6}
\]

Somit kann ein nichtzero Schur-Annihilator `w` nicht mehr dadurch entstehen, dass sein Mediatorbild verschwindet.  Er müsste notwendig ein **nichtzero** Mediatorbild besitzen, das exakt orthogonal zum gesamten inneren Mediatorbild steht:
\[
\boxed{
0\ne\mathscr M_Aw\in\mathcal N_I^\perp.
}
\tag{CG.7}
\]

Der post-P12-Engpass ist daher nicht „noch eine Hub-Injektivität“, sondern
\[
\boxed{
\operatorname{Ran}\mathscr M_A
\cap
\mathcal N_I^\perp
\stackrel?=\{0\}.
}
\tag{CG.8}
\]

Genauer ist wegen möglicher Nichtabgeschlossenheit von `Ran M_A` die punktweise Form (CG.5) die primäre Aussage; (CG.8) ist ihre Bildraumfassung.

---

## 5. Cross-Gram-Nichtentartung als richtiger nächster Satz

Definiere die bilineare/sesquilineare Cross-Gram-Paarung
\[
\boxed{
\mathfrak G_{A,I}(w,f)
:=\langle\mathscr M_Aw,\mathscr M_If\rangle.
}
\tag{CG.9}
\]
Dann
\[
\mathfrak G_{A,I}(w,f)
=\langle w,\mathcal T_{A,I}f\rangle.
\]

Für festes `w` ist
\[
\boxed{
\mathfrak G_{A,I}(w,f)=0\ \forall f
\iff
w\in\ker\mathcal T_{A,I}^*.
}
\tag{CG.10}
\]

Auf den P12-Injektivitätsstrata ist daher die gewünschte Schur-Annihilatorfreiheit exakt die Forderung:

> Jeder nichtzero ungerade Annulusvektor besitzt mindestens einen inneren Testvektor, mit dem seine preconditionierte Hub-Amplitude eine nichtzero Cross-Gram-Paarung hat.

Das ist eine **nichtorthogonale Transversalitätsbedingung**, nicht eine lokale Support- oder reine Positivitätsbedingung.

---

## 6. Quantitative Version und Firewall

Für `w` mit `M_A w != 0` definiere formal den relativen Überlapp
\[
\alpha(w)
:=
\frac{\|P_I\mathscr M_Aw\|}
     {\|\mathscr M_Aw\|}
\in[0,1].
\tag{CG.11}
\]
Dann auf den P12-Injektivitätsstrata
\[
\boxed{
\mathcal T_{A,I}^*w=0
\iff
\alpha(w)=0.
}
\tag{CG.12}
\]

Ein **uniformer** Winkel
\[
\inf_{w\ne0}\alpha(w)>0
\tag{CG.13}
\]
wäre eine starke quantitative Transversalität.  Sie würde jedoch allein noch keinen bounded-below-Satz in der ursprünglichen `w`-Norm liefern, solange keine quantitative untere Schranke für `M_A` vorliegt.

Daher:

- P12-Injektivität gibt `M_A w != 0` für `w != 0`;
- sie gibt **keine** uniforme Untergrenze für `||M_A w||/||w||`;
- Cross-Gram-Nichtentartung (CG.10) ist schwächer als ein uniformer Winkel;
- Closed Range / Observability bleibt separat offen.

---

## 7. Ein starker, aber nicht notwendiger Suffizienztest

Falls
\[
\boxed{
\overline{\operatorname{Ran}\mathscr M_I}
=\mathcal K_{\rm med}^{+}
}
\tag{CG.14}
\]
im relevanten Mediator-Paritätssektor gilt, dann `N_I^perp=0` und damit sofort
\[
\ker\mathcal T_{A,I}^*=0.
\]

Da `B^{1/2}` beschränkt invertierbar ist,
\[
\overline{\operatorname{Ran}(B^{1/2}H^*E_I)}
=\mathcal K_{\rm med}^{+}
\]
ist äquivalent zur Dichtheit von `Ran(H^*E_I)`; durch Hilbertraumdualität wiederum zur Injektivität von
\[
E_I^*H
\]
auf dem entsprechenden Zielsektor.

Somit ist
\[
\boxed{
\ker(E_I^*H)=0
}
\tag{CG.15}
\]
ein **hinreichender**, aber nicht notwendiger Test für Schur-Annihilatorfreiheit.

Dieser Test ist logisch verschieden von P12s
\[
\ker(H E_{\mathcal A})=0.
\]
Er darf nicht mit P12 identifiziert werden.

---

## 8. Strategische Konsequenz

Nach der P12-Rückbindung besitzt R32-F(ii) nun drei sauber getrennte Ebenen:

1. **äußerer Annulus-Hubkernel**
   \[
   \ker(H E_{\mathcal A})
   \]
   — durch P12 auf den globalen P12-Strata trivial;

2. **Schur-Cross-Gram-Transversalität**
   \[
   \ker(\mathscr M_I^*\mathscr M_A)
   \]
   — echter post-P12 Kern, offen;

3. **quantitative Transversalität / Closed Range**
   — nochmals stärker und ebenfalls offen.

Der entscheidende strukturelle Wechsel ist
\[
\boxed{
\text{Kernelproblem}
\longrightarrow
\text{Cross-Gram-Winkelproblem zwischen zwei nichtorthogonalen Mediatorbildern.}
}
\tag{CG.16}
\]

Das ist bemerkenswert kompatibel mit dem langfristigen Objekt-X-Fahndungsbild einer gemeinsamen nichtorthogonalen Quelle/Mediator-Geometrie, wird hier aber **nicht** zu einer Objekt-X-Aussage promotet.

---

## 9. Status vor unabhängigem Review

\[
\boxed{
\mathrm{CG\!-\!1}:?[O]
}
\]
für die exakte Faktorisierungs-/Transversalitätsbuchung bis zur unabhängigen Prüfung.

Der mathematisch neue offene Test bleibt
\[
\boxed{
\ker(\mathscr M_I^*\mathscr M_A)=\{0\}\ ?
}
\]
beziehungsweise punktweise
\[
\boxed{
P_I\mathscr M_Aw\ne0
\quad\forall\,w\ne0.
}
\]

Keine Aussage über `Delta`, Polar Gauge, Cross-Polar-Asymptotik, Strong Terminal Transport, Objekt X oder RH folgt allein aus diesem Reduktionssatz.
