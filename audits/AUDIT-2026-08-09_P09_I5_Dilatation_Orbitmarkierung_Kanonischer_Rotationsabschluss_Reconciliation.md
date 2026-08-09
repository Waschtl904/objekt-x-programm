# P09 / I5 — Dilatation, Orbitmarkierung und kanonischer Rotationsabschluss: Pass-A-Reconciliation

**Datum:** 9. August 2026  
**SYN-Ziel:** P09 — BC + Hochschild  
**Paket:** I5 — `NEU-219h`–`NEU-219z` + `NEU-219_Finalaudit_Gesamtabschluss.md`  
**Prüfart:** `AUDIT-RECONCILED` / `AUDIT-REUSED` mit `TARGETED-REAUDIT` der Rollback-Kette und der Unit-Slot-Trennung  
**Status:** **`I5 PASS A COMPLETE — GEGENCHECK AUSSTEHEND`**

---

## 0. Präzedenz und Scope

Autoritativer Endanker ist `NEU-219_Finalaudit_Gesamtabschluss.md` mit Abschlusskorrektur vom 5. August 2026.

I5 liest die Zwischenfolge `h–z` ausschließlich unter dieser Präzedenz:

```text
Finalaudit / NEU-219y2 Unit-Slot-Abschluss
    > spätere Direktaudits v/w/x/y/z
    > r: Erstdefinition des kanonischen Basislifts
    > h–q: Dilatations-/Orbit-/Morita-Aufbau und Auditgerüst
    > s/t/u: historische Rotations-/No-go-Zwischenfassungen.
```

Insbesondere ist die Formel

\[
t\Phi_0=g^{-\beta}\Phi_0
\]

**nicht** Endstand. `s=-1` ist zurückgerollt.

---

## 1. NEU-219h/i — Dilatation: vom offenen Kandidaten zur adelischen Laca-Struktur

### NEU-219h

`NEU-219h` ist ein sauberer Strukturaudit: ein bloß formal adjungiertes `u_g` ist keine Reparatur. Die nichtunitalen BC-Endomorphismen `rho_n` benötigen zuerst eine echte automorphe Dilatation.

**Migration:** `AUDIT-ONLY / INCORPORATED_part` als Typfirewall.

### NEU-219i

Der Nachfolgeknoten ersetzt die drei offenen Kandidaten aus h durch die adelische Dilatationsarchitektur

\[
\widetilde B=C_0(\mathbb A_f),\qquad
(\gamma_rF)(a)=F(r^{-1}a),\qquad
\widetilde A=C_0(\mathbb A_f)\rtimes_\gamma\mathbb Q_+^\times.
\]

Mit `e=1_Zhat` wird die BC-Algebra als volle Ecke realisiert, und die Gruppenimplementierer erfüllen

\[
\deg(U_r)=r,\qquad
\widetilde\sigma_\beta(U_r)=r^\beta U_r.
\]

Der konjugierte Randtwist

\[
\boxed{\tau=\gamma_g\circ\widetilde\sigma_\beta}
\]

ist der richtige Typbefund für die spätere Modulrechnung.

**Migration:** `INCORPORATED` auf C*- und algebraisch-dynamischer Ebene. Kein Schluss auf einen bereits vollständigen logarithmischen analytischen Modul.

---

## 2. NEU-219j/k/l — algebraischer adelischer Kern, Ecke und Morita

### NEU-219j

Konstruiert werden

- der algebraische adelische Kern `A_tilde_alg`,
- der logarithmische Koeffizientenkern `A_tilde^log`,
- die Eckeneinbettung des bisherigen Moduls,
- ein abstrakter orbit-induzierter `tau`-äquivarianter Bimodul.

Die spätere globale Multiplikationsrealisierung ist hier **noch nicht** injektiv bewiesen.

**Migration:** `INCORPORATED_part`; die abstrakte Orbitsumme bleibt typkorrekt, die unmarkierte konkrete Gesamtrealisierung wird später negativ geschlossen.

### NEU-219k

Wichtiger Typfirewall:

\[
\widetilde L(\ldots)\in \widetilde M_{orb},
\]

nicht automatisch in `A_tilde`. Daher ist eine unveränderte Algebra-KMS-Auswertung eines modulwertigen Ausdrucks nicht definiert.

Positiv bleiben algebraische Vollheit und lokale Einheiten.

**Migration:** aktueller Formeltyp `P09-CORE-NOGO`; algebraische Vollheit/lokale Einheiten `INCORPORATED`.

### NEU-219l

Autoritativer positiver Eckknoten:

\[
\boxed{e\widetilde A_{alg}e=j_A(A_{alg}).}
\]

Die exakte algebraische Eckidentität folgt nicht bloß aus dem C*-Full-Corner-Satz, sondern aus der expliziten Monomrechnung. Daraus entsteht ein konkreter algebraischer Morita-Kontext mit `Re` und `eR`.

**Migration:** `INCORPORATED`; die Behauptung „Laca allein beweist bereits die exakte algebraische Kerngleichheit“ ist `NO-GO,Quelle`.

---

## 3. NEU-219m/n — Orbitkollaps, Markierung und Modulgewicht

### NEU-219m: entscheidender Negativbefund

Die unmarkierte Orbitrealisierung kollabiert vollständig:

\[
\boxed{N_k=N_0\qquad\forall k\in\mathbb Z.}
\]

Daher ist die globale Summenabbildung

\[
\Pi:\bigoplus_k I_k\to \widetilde{\mathcal A}^{log}
\]

nicht injektiv, sofern das Modul nicht null ist. Die `R`-Sättigung entfernt die Orbitmarkierung.

Insbesondere sind verschachtelte adelische Ecken keine Orbitseparatoren.

**Migration:** `INCORPORATED`, `P09-CORE-NOGO` für Orbitdirektheit und globale unmarkierte `Pi`-Injektivität.

Die Reparatur ist die externe markierte Realisierung

\[
\mathcal N_{tag}=\bigoplus_k^{alg}N_0\delta_k.
\]

### NEU-219n

Auf `N_tag` wird ein typkorrektes KMS-Modulgewicht konstruiert:

\[
\varpi_{\beta,\chi}(x)
=\widetilde\omega_{\beta,\chi}(U_{g^{-1}}x),
\]

und die Eigenfamilie

\[
\Omega_\lambda\!\left(\sum_kx_k\delta_k\right)
=\sum_k\lambda^k\varpi_{\beta,\chi}(x_k)
\]

mit

\[
\Omega_\lambda(T\eta)=\lambda\Omega_\lambda(\eta).
\]

Gleichzeitig gilt negativ:

\[
\boxed{U_{g^{-1}}\neq T^{-1}\text{ auf }\mathcal N_{tag}.}
\]

Multiplikatorwirkung erhält den Orbitindex; nur der externe Shift ändert ihn.

**Migration:** markiertes Modulgewicht `INCORPORATED`; `U_{g^{-1}}=T^{-1}` `P09-CORE-NOGO`.

---

## 4. NEU-219o/p/q — Rotationsaudit als Gerüst, noch ohne Liftdefinition

Diese drei Dateien leisten nützliche Buchhaltung:

- direkter skalarer Rotationsweg statt untypisiertem modulwertigen Rotationsoperator,
- Trennung von Gamma-Ladung und Orbitindex,
- Formel
  \[
  \varepsilon=\kappa(a_0,a_1,a_2,a_3)-\kappa(a_1,a_2,a_3,a_4),
  \]
- Verbot, `kappa` aus dem Grad `g` zu raten.

Der entscheidende Auditbefund aus q lautet aber: **Ein konkretes `L_tilde` war bis dahin gar nicht definiert.**

Daher sind o–q kein eigenständiges Endresultat zur Rotation, sondern das Auditgerüst, das NEU-219r erzwingt.

**Migration:** `AUDIT-ONLY / SUPERSEDED-by-r` für offene Rotationsparameter; die Firewall `Grad != Orbitindex` bleibt `INCORPORATED`.

---

## 5. NEU-219r — kanonischer Basislift: positiver Endanker

NEU-219r führt erstmals den kanonischen Basislift ein:

\[
\boxed{
\widetilde L_0
=\eta_0\circ j_M\circ L^{cup}_{g;\mathbf p}
:A_{alg}^{\otimes4}\to I_0.
}
\]

Da `eta_0 o j_M` ein Bimodulhomomorphismus ist:

\[
\boxed{\widetilde L_0\in Z^4(A_{alg},I_0).}
\]

Weil die Definition ausschließlich im Nullsummanden lebt und weder `tau`- noch `T`-Shift verwendet:

\[
\boxed{\kappa=0,\qquad\varepsilon=0.}
\]

Folglich ist jedes Orbitgewicht `lambda` auf dem kanonischen Lift wirkungslos.

### Typkorrektur der Recovery-Identität

Die spätere Abschlussprüfung präzisiert:

\[
\Pi_0\circ\eta_0=\iota_{M_0\hookrightarrow N_0},
\]

nicht streng `id_{M_0}` bei Ziel `N_0`; äquivalent nach Eckkompression:

\[
(e\Pi_0e)\circ\eta_0=id_{M_0}.
\]

Die Injektivität von `eta_0` bleibt vollständig erhalten.

**Migration:** `INCORPORATED` mit dieser Typkorrektur.

---

## 6. NEU-219s/t und erstes NEU-219u — autoritativer Rollback

### Historische Behauptung

NEU-219s/t behaupteten schließlich

\[
t\Phi_0=g^{-\beta}\Phi_0,
\qquad s=-1.
\]

Diese Behauptung ist **nicht** zu migrieren.

### Warum sie fällt

NEU-219v schließt einen typwidrigen `U`-Eingaberotationskandidaten aus.

NEU-219w zeigt entscheidend:

- KMS permutiert Faktoren im Gewicht, aber ersetzt nicht
  `L(a_0,a_1,a_2,a_3)` durch `L(a_1,a_2,a_3,a_4)`;
- die in s verwendeten Regeln `(R1)–(R3)` enthalten die notwendige Rotationsrelation nicht;
- eine Grad-aussage über `L` ist keine Äquivarianzformel;
- der zentrale Übergang in s/t war nicht hergeleitet.

Damit:

\[
\boxed{s=-1\text{ unbewiesen und später vollständig zurückgerollt}.}
\]

Das erste `NEU-219u_Abschluss_O219_NoGo_Theorem.md` hängt an diesem falschen Beweis und ist als globaler Abschluss **SUPERSEDED**. Seine spätere Schlussrichtung „kanonischer Basislift nicht zyklisch“ wird zwar wieder wahr, aber durch einen anderen und stärkeren Beweis.

Zusätzlich darf die dortige Statusbuchung des vollen Quotienten nicht übernommen werden: `M/[A,M]` bleibt aus I4 offen.

**Migration:** s/t `SUPERSEDED`; erstes u `SUPERSEDED` als Beweis-/Statustabelle.

---

## 7. Zweites NEU-219u — nützliche Typkorrekturen, bedingter No-go später superseded

`NEU-219u_Abschlussaudit_Geladene_zyklische_Architektur.md` enthält zwei bleibende Präzisierungen:

1. die oben genannte Recovery-Typkorrektur;
2. das KMS-Regime muss im dort verwendeten Gibbs-Pfad als `beta>1` geführt werden.

Sein damaliger Rotations-No-go ist jedoch noch **bedingt** durch die später zurückgerollte Prämisse `(R): tPhi_0=g^{-beta}Phi_0`.

**Migration:** `INCORPORATED_part` für Typ-/Beta-Firewalls; bedingte Rotationsargumentation `SUPERSEDED`.

---

## 8. NEU-219x/y1 — Zieltypbrücke: isolierte Quelle negativ, Gesamt-DAG positiv

### NEU-219x — korrekter isolierter Quellenbefund

Bleibend korrekt ist nur die eng formulierte Aussage:

\[
\boxed{\text{NEU-211 allein beweist nicht }D_g(A_{alg})\subseteq\mathfrak M_{glob}^{log}.}
\]

Daher

`[O-219-5e1j-Dg-target-from-NEU211] = ✓[M]neg,Quelle`.

### Quellfehler in NEU-219x

Nicht migrieren:

- `D_g(e(r))=0`;
- globale Aussage `D_g(B_alg)=0`;
- „gleichmäßiger Grenzwert“ von `ad(Y_N)`.

Korrekt laut Finalaudit:

\[
D_g^{corr}(e(r))=\mu_m C_{m,n;r}\mu_n^*,
\]

die Leibnizformel besitzt einen nichttrivialen mittleren Term, und es liegt nur **punktweise Normkonvergenz auf jedem festen** `a in A_alg` vor.

### NEU-219y1 — Gesamtzieltyp positiv

Die spätere Kette NEU-216/217 schließt die Zieltypbrücke:

\[
\boxed{
D_g^{corr}(A_{alg})\subseteq\mathfrak M_{glob}^{log},
\qquad
D_g^{corr}((A_{alg})_h)\subseteq M_{gh}.
}
\]

Das ist mit dem isolierten Negativbefund aus x kompatibel: x fragt „aus NEU-211 allein?“, y1 fragt „im Gesamt-DAG?“.

### Formelkorrektur y1

Nicht migrieren ist der falsche erste Index in der Transportformel. Korrekt:

\[
\boxed{
\sigma_n(G_{k,d})
=G_{nk,d/\delta}
-\rho_{d/\delta}G_{n/\delta,1}.
}
\]

**Migration:** x `INCORPORATED_part` nur als Quellen-No-go; y1 `INCORPORATED` mit Transport- und `D_g^{corr}`-Korrektur.

---

## 9. NEU-219z/y2 — stärkerer Unit-Slot-Abschluss

### NEU-219z: explizite Cup-Struktur

Für homogene Eingaben:

\[
\Theta^\wedge(a_i,a_j,a_k)
=\Delta_{\mathbf p}(h_i,h_j,h_k)a_i a_j a_k,
\]

und daher tragen `Phi_0` und `tPhi_0` im Allgemeinen unterschiedliche Determinantenfaktoren und unterschiedliche `D_g^{corr}`-Slots.

Besonders stark ist der Test `a_4=1`:

\[
\Phi_0(a_0,a_1,a_2,a_3,1)=0,
\]

weil `Theta^wedge(a_2,a_3,1)=0`.

### NEU-219y2: expliziter nichtverschwindender rotierten Zeuge

Der alte neutralisierende Zeuge `a_0^{neu}` verschwindet im Unit-Slot-Test und wird dort negativ geschlossen.

Der neue kleinste gradkorrekte Zeuge ist

\[
\boxed{a_0^\star=\mu_P^*.}
\]

Er liefert die Normalform

\[
D_g^{corr}(\mu_P^*)\mu_P=-\mu_m G_P\mu_n^*,
\]

und nach adelischer/KMS-Auswertung für `beta>1`:

\[
\boxed{
W(\mu_P^*)
=-n^{-\beta}\omega_{\beta,\chi}(G_P)<0
}
\]

für alle zulässigen extremalen `chi`.

Mit

\[
(a_0,a_1,a_2,a_3,a_4)
=(\mu_P^*,\mu_{p_1},\mu_{p_2},\mu_{p_3},1)
\]

gilt daher

\[
\boxed{\Phi_0(\mathbf a)=0,\qquad(t\Phi_0)(\mathbf a)\neq0.}
\]

Somit folgt unmittelbar und ohne jeden Exponentenansatz:

\[
\boxed{
t\Phi_0\neq C\Phi_0
\qquad\forall C\in\mathbb C.
}
\]

Dies ist stärker als `tPhi_0 != Phi_0` und macht eine Neuberechnung eines globalen `s` obsolet.

### Quellfehler-Firewall y2

Die Einleitung von y2 wiederholt historisch `D_g(e(r))=0`; das ist `×[M]`. Der Unit-Slot-Hauptbeweis benutzt für den positiven Zeugen jedoch `D_g^{corr}(mu_P^*)` und bleibt laut Finalaudit vollständig gültig.

**Migration:** z `INCORPORATED_part` als explizites Rotationsgerüst; y2 `INCORPORATED` als Hauptabschluss mit Einleitungs-Korrektur.

---

## 10. Autoritativer Endstand des Finalaudits

Die richtige Abschlusskette lautet

\[
\boxed{
\widetilde L_0
\longrightarrow\kappa=0
\longrightarrow\varepsilon=0
\longrightarrow\text{kein globales }s
\longrightarrow\text{kein }\lambda^*.
}
\]

und der zentrale Satz ist

\[
\boxed{t\Phi_0\neq C\Phi_0\quad\forall C\in\mathbb C.}
\]

### Exakte Reichweite

Ausgeschlossen ist die **globale konstante Rotationseigenrelation des kanonischen skalaren Basislifts**. Daraus folgt insbesondere: dieser konkrete kanonische Repräsentant ist nicht gewöhnlich zyklisch.

Nicht ausgeschlossen sind:

- ein anderer zyklischer oder getwistet-zyklischer Repräsentant derselben Hochschildklasse;
- ein genuin orbitverschiebender, wesentlich nichtkanonischer Lift;
- nichtstandardmäßige parazyklische/SAYD-/relative Koeffizientenarchitekturen;
- die Weil-/Gammafaktorpaarung.

Daher bleiben/exportieren:

\[
[O\text{-}219\text{-cyclic-representative}]\quad ?[O],
\]

\[
[O\text{-}219\text{-5e2-genuine-orbit-shifting-lift}]\quad ?[O],
\]

\[
[O\text{-}219\text{-6}]\to O\text{-}220\text{ archimedischer/Weil-Gamma-Pfad}.
\]

Der volle gewöhnliche Modulquotient `M/[A,M]` bleibt ebenfalls offen und wird durch I5 nicht entschieden.

---

## 11. Klassifikation der I5-Dateien

| Quelle | P09-Klassifikation |
|---|---|
| NEU-219h | `AUDIT-ONLY / INCORPORATED_part` |
| NEU-219i | `INCORPORATED` — adelische Dilatation / Full Corner / Dynamik |
| NEU-219j | `INCORPORATED_part` — abstrakter Orbitlift, konkrete Gesamtinjektivität später negativ |
| NEU-219k | `INCORPORATED_part` + `P09-CORE-NOGO` für untypisierte aktuelle Gewichtsformel |
| NEU-219l | `INCORPORATED` — exakte algebraische Ecke / Morita |
| NEU-219m | `INCORPORATED` — Orbitdirektheit negativ, Markierung positiv |
| NEU-219n | `INCORPORATED` — markiertes Modulgewicht; `U=T^-1` negativ |
| NEU-219o–q | `AUDIT-ONLY / SUPERSEDED-by-r` für offene Rotationsparameter; `Grad != Orbitindex` bleibt |
| NEU-219r | `INCORPORATED` mit Recovery-Typkorrektur |
| NEU-219s | `SUPERSEDED` |
| NEU-219t | `SUPERSEDED` — `s=-1` / globale Eigenrelation nicht migrieren |
| NEU-219u `Abschluss_O219_NoGo_Theorem` | `SUPERSEDED` als Abschluss-/Beweisstatus |
| NEU-219u `Abschlussaudit_Geladene...` | `INCORPORATED_part` für Typ-/Beta-Korrekturen; bedingter No-go `SUPERSEDED` |
| NEU-219v | `INCORPORATED` — typwidrige U-Eingaberotation `NO-GO` |
| NEU-219w | `INCORPORATED` — R1–R3-Rotationsbeweis `NO-GO,Quelle` |
| NEU-219x | `INCORPORATED_part` — NEU-211-isolierter Zieltyp-No-go; interne Quellfehler `×[M]` |
| NEU-219y1 | `INCORPORATED` mit Transport-/Dg-Korrektur |
| NEU-219z | `INCORPORATED_part` — explizite Cup-Rotationsstruktur |
| NEU-219y2 | `INCORPORATED` — Hauptabschluss, Einleitungsfehler ausgenommen |
| NEU-219 Finalaudit | **`AUTHORITATIVE / INCORPORATED`** |

---

## 12. P09-CORE-NOGOs aus I5

1. Bloßes formales `u_g` ohne echte Dilatation.
2. Aktuelle algebraische KMS-Auswertung eines abstrakt modulwertigen Ausdrucks ohne typisierte Paarung.
3. Orbitdirektheit der gesättigten `N_k`; tatsächlich `N_k=N_0`.
4. Globale unmarkierte `Pi`-Injektivität.
5. Eckkompressionen als Orbitseparatoren.
6. `U_{g^{-1}}=T^{-1}` auf der markierten Orbitsumme.
7. Typwidrige U-Eingaberotation aus NEU-219v.
8. Rotationsbeweis allein aus `(R1)–(R3)` aus NEU-219s/t.
9. Globale konstante Rotationseigenrelation des kanonischen Basislifts:
   \[
   t\Phi_0=C\Phi_0.
   \]

Die Punkte 1–8 typisieren die Sucharchitektur. Punkt 9 ist das autoritative starke End-No-go.

---

## 13. Was I5 ausdrücklich **nicht** beweist

- Kein No-go für die I3-Hochschildklasse selbst.
- Kein Beweis oder Widerlegung von `HH^4(A_alg,A_alg)_g != 0`.
- Kein vollständiger Ausschluss aller zyklischen/getwistet-zyklischen Repräsentanten.
- Kein Ausschluss eines genuin orbitverschiebenden nichtkanonischen Lifts.
- Kein Schluss auf einen Hilbert–Pólya-Operator.
- Keine Weil-/Gammafaktor-Realisierung; dieser Teil ist exportiert.
- Keine Entscheidung des vollen Quotienten `M/[A,M]`.

---

## 14. Fünf atomare Gegencheckfragen

1. **Dilatation/Morita:** Ist die I5-Lesart korrekt, dass NEU-219i/l die adelische C*-Dilatation, Full-Corner-Struktur und exakte algebraische Ecke positiv liefern, ohne daraus einen vollständig analytisch vervollständigten logarithmischen Koeffizientenmodul zu folgern?

2. **Orbitmarkierung:** Ist korrekt, dass NEU-219m die unmarkierte Orbitrealisierung strukturell widerlegt (`N_k=N_0`, globale `Pi` nicht injektiv), während die markierte Ersatzrealisierung und das Modulgewicht aus NEU-219n typkorrekt bleiben; insbesondere `U_{g^{-1}}` erhält den Orbitindex und ist nicht `T^{-1}`?

3. **Kanonischer Lift:** Ist NEU-219r korrekt als autoritativer positiver Knoten zu lesen: `L_tilde0=eta_0 o j_M o L_cup in Z^4(A_alg,I_0)`, `kappa=epsilon=0`, `lambda` wirkungslos; mit der späteren Typkorrektur `Pi_0 o eta_0 = inclusion_{M_0->N_0}` bzw. nach Eckkompression `id_{M_0}`?

4. **Rollback und End-No-go:** Ist korrekt, dass `s=-1` und `tPhi_0=g^{-beta}Phi_0` aus s/t zurückgerollt sind, dass v/w nur die falschen Beweiswege schließen, und dass y2 stattdessen mit dem Unit-Slot-Tupel `(mu_P^*,mu_p1,mu_p2,mu_p3,1)` stärker `Phi_0=0`, `tPhi_0!=0` und damit `tPhi_0!=C Phi_0` für jedes konstante `C` beweist?

5. **Quellfehler/Reichweite:** Bleibt der y2-Hauptbeweis trotz der historischen Fehler `D_g(e(r))=0` in x/y2, `D_g(B_alg)=0`, „uniformer Grenzwert“ und des falschen ersten Indexes in y1 gültig, wenn konsequent `D_g^corr` und die korrigierte Transportformel verwendet werden; und ist zugleich korrekt, dass nur der kanonische konstante Rotationsrepräsentant ausgeschlossen ist, während `[O-219-cyclic-representative]`, ein genuin orbitverschiebender Lift, der volle Quotient `M/[A,M]` und der Weil-/Gamma-Pfad offen/exportiert bleiben?

---

## 15. Pass-A-Endstand I5

\[
\boxed{
\text{I5 PASS A COMPLETE — kanonische Rotationsarchitektur reconciliert; Gegencheck ausstehend.}
}
\]

Nach Gegencheck ohne konkreten Befund kann I5 versiegelt und I6 (`NEU-222`) als letzter P09-Superseding-/Routing-Scan durchgeführt werden.
