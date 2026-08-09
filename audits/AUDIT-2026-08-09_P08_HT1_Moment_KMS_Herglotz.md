# P08 Pass A — H-T1 Direktaudit / Reconciliation

## NEU-121 / NEU-121Cfix / NEU-122 — Moment, KMS/GNS, Herglotz

**Datum:** 9. August 2026  
**Paket:** H-T1  
**Prüfart:** `NEW-DIRECT-AUDIT` für die nicht separat auditierten Eingangsaussagen + `AUDIT-RECONCILED` gegen bindende spätere Korrekturen P06/P07  
**Live-Dateien:**

- `04-grenzoperator-renormierung/NEU-121_Renormierter_Moment_Hadamard_Abgleich.md`
- `04-grenzoperator-renormierung/NEU-121Cfix_Normalisierung_C_xi.md`
- `04-grenzoperator-renormierung/NEU-122_KMS_GNS_vs_Spektralnaehrung.md`

**Superseding Referenzen:**

- P06 §3: `J_N^- = (Theta_N-Theta_N^dagger)/2` schiefadjungiert; `S_N=(Theta_N-Theta_N^dagger)/(2i)=-iJ_N^-` selbstadjungiert.
- P07 §4/§5: `m_arith` Herglotz `iff` RH; Jacobi-/Herglotz-Realisierung nur konditional; Selbstadjungiertheit von `A_N^{Jac,-}` offen; kanonischer Grenzansatz verwendet Nevanlinna-normalisierte Maße/Approximanten.

---

## 1. `C_xi` — bindender Endstand

NEU-121 enthält in §121.2/§121.3 den historischen Zahlenwert `-0.5493`. Dieser ist rechnerisch falsch für die dort ausdrücklich verwendete Größe

\[
C_\xi=-\frac{\xi'(0)}{\xi(0)}.
\]

NEU-121Cfix korrigiert bindend:

\[
\boxed{
C_\xi
=1+\frac{\gamma_E}{2}-\frac12\log(4\pi)
\approx0.0230957.
}
\]

Die symmetrische Nullstellensummenform ist nur in der kanonisch gepaarten/symmetrisierten Bedeutung zu verwenden. Nicht zu migrieren ist eine Lesart als rohe absolute Konvergenz von `sum_rho |1/rho|`.

### Status

- Formel und Zahlenwert aus `NEU-121Cfix`: `✓[M]`.
- historischer Wert `-0.5493`: `×[M]`, `SUPERSEDED`.
- die uneinheitliche historische Herleitung in NEU-121 §121.2 wird nicht wörtlich nach P08 übernommen; maßgeblich ist Cfix.

---

## 2. KMS-/GNS-Normalisierung — lokaler Fehler in NEU-122

NEU-122 definiert für den Dirichlet-Cutoff

\[
\tau_{\beta,N}(T)=\sum_{n\le N}n^{-\beta}\langle e_n,Te_n\rangle,
\qquad
Z_{\beta,N}=\tau_{\beta,N}(1),
\]

und den normalisierten Zustand

\[
\varphi_{\beta,N}=Z_{\beta,N}^{-1}\tau_{\beta,N}.
\]

Für `beta=1` gilt korrekt

\[
Z_{1,N}=\sum_{n\le N}\frac1n
=\log N+\gamma_E+o(1),
\qquad
Z_{1,N}^{-1}\sim\frac1{\log N}.
\]

### 2.1 GNS-Vektornorm

Sei `Omega_tau` der GNS-Vektor des **unnormalisierten** positiven Funktionals `tau`. Dann

\[
\|\Omega_\tau\|^2=\tau(1)=Z.
\]

Der Vektor des normalisierten Zustands ist daher

\[
\boxed{
\widehat\Omega=Z^{-1/2}\Omega_\tau,
}
\]

und nicht `Z^{+1/2} Omega_tau` wie in NEU-122 §122.1.

Denn

\[
\langle\widehat\Omega,\pi(T)\widehat\Omega\rangle
=Z^{-1}\tau(T)=\varphi(T).
\]

### Status

- NEU-122-Formel `\widehat\Omega=Z^{1/2}\Omega`: `×[M]`.
- korrigierte Formel `\widehat\Omega=Z^{-1/2}\Omega`: `✓[M]`.
- der skalare Normalisierungsfaktor
  \[
  R_N=Z_{1,N}^{-1}\sim1/\log N
  \]
  ist korrekt.

### 2.2 Lokaler Widerspruch bereits in NEU-121

NEU-121 §121.5.3 schreibt nach `Z_1^{-1}->0` zunächst, eine Renormierung `R_N ~ log N` sei nötig, verwendet unmittelbar danach aber den Kandidaten mit Faktor `1/log N`.

Der erste Satz ist falsch/verkehrt herum. Bindend ist:

\[
\boxed{R_N\sim Z_{1,N}^{-1}\sim1/\log N.}
\]

Dieser Punkt wird durch die korrigierte Lesart von NEU-122 §122.4 reconciliiert.

### 2.3 Was konzeptionell erhalten bleibt

Nach der Vorzeichen-/Potenzkorrektur bleibt die wichtige Anti-Fitting-Idee tragfähig:

Der Faktor `1/log N` kann im ausdrücklich definierten Dirichlet-Cutoff aus der Normalisierung des positiven Funktionals stammen und muss nicht nachträglich an `C_xi` angepasst werden.

Das beweist jedoch **nicht**, dass dieses endliche Dirichlet-Gewicht bereits der kanonische BC-KMS/GNS-Eingang des Objekt-X-Programms ist. Die eigentliche Brücke P1 bleibt offen.

---

## 3. Typ von `A_N^{Jac,-}` — Herglotz nur konditional

NEU-121 und NEU-122 verwenden wiederholt Aussagen der Form

\[
m_{\Omega,N}(z)
=\langle\Omega,(A_N^{\rm Jac,-}-z)^{-1}\Omega\rangle
\]

und behandeln `A_N^{Jac,-}` dabei als selbstadjungiert.

Dies darf nicht unbesehen migriert werden.

P06 fixiert:

\[
J_N^-:=\frac12(\Theta_N-\Theta_N^\dagger)
\quad\text{ist schiefadjungiert},
\]

\[
S_N:=\frac1{2i}(\Theta_N-\Theta_N^\dagger)=-iJ_N^-
\quad\text{ist selbstadjungiert}.
\]

P07 hält ausdrücklich fest:

\[
A_N^{\rm Jac,-}\text{ selbstadjungiert}: ?[O].
\]

Daher gilt für P08:

> Jede Spektralmaß-/Herglotz-Aussage über `A_N^{Jac,-}` ist **konditional auf eine sauber typisierte selbstadjungierte Realisierung**.

Insbesondere ist eine historische Formel vom Typ

\[
A_N^{\rm Jac,-}=H_N+\beta_NJ_N^-
\]

bei selbstadjungiertem `H_N` und reellem `beta_N` nicht automatisch selbstadjungiert. Eine zulässige selbstadjungierte Variante müsste den Faktor/Typ explizit korrigieren, etwa über `S_N=-iJ_N^-` oder einen entsprechend imaginären Koeffizienten.

### Status

- abstrakte Resolventen-/Spektralmaßform für einen **gegebenen selbstadjungierten** endlichen Operator: `✓[M]`.
- Selbstadjungiertheit des historischen konkreten `A_N^{Jac,-}`: `?[O]` / `SUPERSEDED_part` durch P06/P07-Typisierung.
- Aussagen, die sie in NEU-121/122 ohne Kondition voraussetzen: nicht nach P08 migrieren.

---

## 4. Herglotz/RH-Logik — korrekt, aber P07 ist die kanonische Form

P07 friert ein:

\[
\boxed{m_{\rm arith}\text{ ist Herglotz}\iff\mathrm{RH}.}
\]

Für jeden selbstadjungierten endlichen Operator und positiven Spektralvektor ist seine Stieltjes-Resolventenfunktion Herglotz. Daher ist die logische Firewall korrekt:

\[
\text{Herglotz-Approximanten}
\xrightarrow{\text{lokal gleichmäßig}}
m_{\rm arith}
\Longrightarrow
m_{\rm arith}\text{ Herglotz}
\Longrightarrow
\mathrm{RH}.
\]

Der Grenzübergang ist also selbst Teil des harten RH-Kerns, kein bloßer Approximationstrick.

### 4.1 Superseding Normalisierung aus P07

NEU-122.W formuliert dies noch mit dem rohen `m_{Omega,N}`. P07 §5 ist präziser und deshalb für P08 verbindlich:

Da die endlichen Spektralmaße Masse 1 haben, das arithmetische Nullstellenmaß aber unendliche Gesamtmasse, wird der kanonische Kandidat als Nevanlinna-normalisierte Folge geschrieben:

\[
\widetilde\mu_N=c_N\mu_{\Omega,N},
\]

\[
\widetilde m_N^{\rm ren}(z)
=a_N+\int_{\mathbb R}
\left(\frac1{t-z}-\frac{t}{1+t^2}\right)d\widetilde\mu_N(t),
\qquad c_N>0,\ a_N\in\mathbb R.
\]

Damit ist der rohe Satz `m_{Omega,N}->m_arith` nur eine stärkere Spezialform, nicht die kanonische P08-Grenzarchitektur.

### Status

- `m_arith` Herglotz `iff` RH: `✓[M]` gemäß eingefrorenem P07.
- lokale gleichmäßige Konvergenz geeigneter Herglotz-Approximanten `=> RH`: `✓[M]` als logische Implikation.
- Existenz/kanonische Wahl einer solchen Approximantenfolge: `?[O]`.
- bloße Spektralnäherung der Ordinaten `sigma(A_N)->{Im rho}`: kein RH-Beweis; diagnostisch בלבד, wie NEU-122 selbst korrekt warnt.

---

## 5. P1/P2/P3-Endstatus von NEU-122

### P1 — KMS/GNS -> Jacobi

Gesucht ist eine vorab fixierte selbstadjungierte GNS-Observable `A_N^-`, deren zyklische/Lanczos-Darstellung den gewünschten Jacobioperator erzeugt.

**Status:** `?[O]`.

### P2 — KMS-Form gegen Bombieri-/Weil-Form

Die vorgeschlagene Form-Konvergenz ist nur ein Prüfziel; keine Herleitung liegt vor.

**Status:** `?[O]`.

### P3 — Dirichlet-Normalisierung

Für das ausdrücklich definierte endliche Dirichlet-Gewicht gilt

\[
Z_{1,N}^{-1}\sim1/\log N.
\]

**Status:** `✓[M]` als skalare Normalisierungsrechnung; **nicht** als Beweis der P1-/P2-Brücke.

Damit bleibt die KMS-Route insgesamt offen:

\[
\boxed{P1?[O]+P2?[O]+P3\checkmark[M].}
\]

---

## 6. H-T1 Statusmatrix

| Punkt | Historischer Stand | H-T1-Endstand |
|---|---|---|
| `C_xi=-xi'(0)/xi(0)` | Formel richtig, Zahl in NEU-121 falsch | `✓[M]` via 121Cfix; `-0.5493` `×[M]` |
| GNS-Vektor | `Z^{+1/2} Omega` in NEU-122 | `×[M]`; korrekt `Z^{-1/2} Omega` |
| Dirichlet-Skala | `Z^{-1}~1/log N` | `✓[M]` |
| NEU-121 Satz `R_N~log N` | widerspricht Folgerechnung | `×[M]`; korrekt `1/log N` |
| Selbstadjungiertheit `A_N^{Jac,-}` | mehrfach vorausgesetzt | `?[O]`; Herglotz nur konditional |
| `J_N^-` vs `S_N` | historisch vermischt | P06-Typtrennung bindend `✓[M]` |
| `m_arith` Herglotz `iff` RH | Warnsatz | `✓[M]` gemäß P07 |
| rohe Jacobi-m-Konvergenz | als Ziel formuliert | nur Spezialfall; P07-Nevanlinna-Normalisierung bindend |
| P1 KMS/GNS-Jacobi-Brücke | offen | `?[O]` |
| P2 Formkompatibilität | offen | `?[O]` |
| P3 Normalisierung | positiv | `✓[M]` nur für definierten Dirichlet-Cutoff |

---

## 7. Endurteil H-T1

\[
\boxed{\text{H-T1 COMPLETE — zwei lokale Korrekturen, keine neue globale Obstruktion.}}
\]

Die zwei bindenden lokalen Korrekturen sind:

1. `C_xi`: historischer Zahlenwert `-0.5493` gesperrt; Cfix `≈0.0230957` bindend.
2. GNS-Normalisierung: `Z^{+1/2}` ist falsch; korrekt `Z^{-1/2}` und damit `R_N=Z^{-1}~1/log N`.

Zusätzlich wird die bereits von P06/P07 erzwungene Firewall festgeschrieben:

> **Keine Herglotz-/Spektralmaßaussage aus NEU-121/122 wird ohne eine typisierte selbstadjungierte Realisierung von `A_N^{Jac,-}` migriert.**

H-T2 kann auf dieser Basis den eigentlichen Jacobi-Grenzoperator-/Carleman-Strang prüfen.