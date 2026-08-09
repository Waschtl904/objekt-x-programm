# P09 / I4 — KMS, getwistete Zyklizität und Hopf-SAYD: Pass-A-Reconciliation

**Datum:** 9. August 2026  
**SYN-Ziel:** P09 — BC + Hochschild  
**Paket:** I4 — `NEU-219_Zyklischer...` + `NEU-219a`–`NEU-219g`  
**Prüfart:** `AUDIT-RECONCILED` / `AUDIT-REUSED` mit gezieltem `TARGETED-REAUDIT` der Twist-, Zyklisierungs- und SAYD-Schritte  
**Status:** **`I4 PASS A COMPLETE — GEGENCHECK AUSSTEHEND`**

---

## 0. Scope und Präzedenz

I4 umfasst pfadgebunden:

- `NEU-219_Zyklischer_Koeffizient_KMS_Weil_Verfeinerung.md`,
- `NEU-219a_KMS_Typaudit_Negativbefund.md`,
- `NEU-219b_KMS_Neutralisierer_Aufspaltung.md`,
- `NEU-219c_KMS_Diagonalauswertung_positiv.md`,
- `NEU-219d_Getwisteter_Rand_Ladungsobstruktion.md`,
- `NEU-219e_Koeffizientenlinie_Typaudit.md`,
- `NEU-219f_Gewichtssektor_Zyklisierung_Pfadentscheidung.md`,
- `NEU-219g_Hopf_Typaudit_SAYD_Ausschluss.md`.

Bereits vorhandener Blockanker:

- `NEU-219_BLOCKAUDIT_I_KMS_Twist_Triage.md`.

Spätere Reichweitenanker:

- `NEU-219_Finalaudit_Gesamtabschluss.md` — autoritativ für die **kanonische Basislift-/Rotationsarchitektur** aus dem späteren I5-Strang;
- `OBJEKT-X-BESTANDSAUFNAHME.md` — Gesamtstand.

### Präzedenz-Firewall

Der spätere Finalaudit rollt die I5-Zwischenformel

\[
t\Phi_0=g^{-\beta}\Phi_0
\]

für den **kanonischen Basislift** zurück und beweist stärker

\[
t\Phi_0\neq C\Phi_0\qquad\forall C\in\mathbb C.
\]

Dies darf **nicht** mit dem I4-Befund

\[
T_{\sigma_\beta}\Phi_{\beta,\chi}=g^{-\beta}\Phi_{\beta,\chi}
\]

für die **direkt aus KMS-Zustand und HH4-Cup definierte skalare Kochain** identifiziert werden. Es sind verschiedene Objekte und verschiedene Rotationsarchitekturen. I4 migriert nur die rohe KMS-/Twist-Kette; I5 migriert den späteren Basislift-Rollback.

---

## 1. Eingang aus I3

Verbindliche Voraussetzung:

\[
[D_g^{\rm corr}]\smile[\Theta^\wedge]
\neq0
\in HH^4(A_{\rm alg},\mathfrak M_{\rm glob}^{\log})_g,
\qquad g\neq1.
\]

Setze

\[
A:=A_{\rm alg},\qquad M:=\mathfrak M_{\rm glob}^{\log}.
\]

I4 untersucht **nicht** erneut die Nichttrivialität dieser Hochschildklasse, sondern die Frage, ob und wie daraus skalare KMS-/zyklische Daten gewonnen werden können.

Die zentrale Firewall bleibt:

\[
\boxed{HH^4(A,M)_g\neq0\not\Rightarrow HC^4(A)\neq0.}
\]

---

## 2. Ursprungsknoten NEU-219 — Auditkorrekturen

Der Ursprungsknoten ist nur `✓[M]_part` zu lesen.

Belastbar:

1. Der volle gewöhnliche Kommutatorquotient
   \[
   \eta_{q,P}:=D_g^{\rm corr}(\mu_q)\mu_P
   \stackrel{?}{\notin}[A,M]
   \]
   bleibt `?[O]`.
2. Der partielle Quotient aus I3 entscheidet diesen Vollquotienten nicht.
3. Ein gewöhnlicher BC-KMS-Zustand ist wegen Nichtneutralität kein direkter Detektor von `eta`.
4. Ein KMS-getwisteter Pfad ist unabhängig vom gewöhnlichen Vollquotienten sinnvoll.

Zu migrierende Quellkorrekturen:

- die skalare Form mit fünf Argumenten hat **Kochaingrad 4**, nicht 5;
- `B:C^4→C^3` im Kozykelkomplex, nicht „höherer Grad“;
- die frühere Aussage `(1-lambda)Phi in im(b)` liefere automatisch einen zyklischen Korrekturterm ist `×[M]`;
- die Alternative „gewöhnlich versus KMS-getwistet“ ist nicht erschöpfend;
- durchgehend `D_g^{corr}` statt historischem `D_g`.

---

## 3. NEU-219a — direkter KMS-Detektor negativ

Für das homogene Zielelement

\[
\eta_{q,P}=D_g^{\rm corr}(\mu_q)\mu_P
\]

mit Grad

\[
H=gqP\neq1
\]

gilt bei jedem BC-KMS-Zustand und `beta>0`:

\[
\omega_\beta(\eta_{q,P})
=H^{-\beta}\omega_\beta(\eta_{q,P}),
\]

also

\[
\boxed{\omega_\beta(\eta_{q,P})=0.}
\]

Status:

\[
[O\text{-}219\text{-}1a\text{-KMS}]\quad\checkmark[M]_{\rm neg}.
\]

Zusätzlich ist ein KMS-Zustand keine gewöhnliche Spur auf `M`; er annihiliert im Allgemeinen nicht `[A,M]`, sondern den passend getwisteten Kommutatorraum.

Der gewöhnliche Vollquotient `[O-219-1]` bleibt deshalb offen.

---

## 4. NEU-219b/c — Gradneutralisierung und positive KMS-Auswertung

### 4.1 Expliziter Neutralisierer

Mit

\[
g=\frac mn,\qquad H=\frac{mqP}{n}
\]

ist

\[
\boxed{a_0^{\rm neu}:=\mu_n\mu_{mqP}^*}
\]

vom Grad `H^{-1}`.

Für den ausgezeichneten Cup-Wert gilt:

\[
a_0^{\rm neu}
L^{\rm cup}_{g;\mathbf p}(\mu_q,\mu_{p_1},\mu_{p_2},\mu_{p_3})
=
\left(\prod_{i=1}^3\log p_i\right)
\rho_n(\sigma_P(G_q)).
\]

Damit:

\[
\Phi_{\beta,\chi}(a_0^{\rm neu},\mu_q,\mu_{p_1},\mu_{p_2},\mu_{p_3})
=
n^{-\beta}
\left(\prod_i\log p_i\right)
\omega_{\beta,\chi}(\sigma_P(G_q)).
\]

### 4.2 `G_q` ist beschränkt

Wichtig: `G_q∈B^log⊂C(Zhat)` ist **beschränkt**. Unbeschränkt ist nur das rohe Hilfsprofil

\[
\mathscr X(x)=c_{\nu(x)}.
\]

Jede frühere Aussage, `G_q` selbst sei unbeschränkt, ist `SUPERSEDED/×[M]`.

### 4.3 Positivität für `beta>1`

Für extremale Gibbs-KMS-Zustände bei `beta>1`:

\[
\omega_{\beta,\chi}(F)=\frac1{\zeta(\beta)}
\sum_{k\ge1}k^{-\beta}F(k\chi).
\]

Da Einheiten `chi` die Faktorialtiefe nicht ändern, ist die Auswertung von `sigma_P(G_q)` unabhängig von `chi`. Weiter gilt

\[
G_q(x)\ge0
\]

und über

\[
k_J=\frac{L_J}{Pq}
\]

existiert für jedes hinreichend große `J` ein strikt positiver Gibbs-Summand. Daher:

\[
\boxed{
\omega_{\beta,\chi}(\sigma_P(G_q))>0
\quad\text{für alle }\beta>1
\text{ und alle extremalen }\chi.
}
\]

Somit ist die neutralisierte skalare Fünffachauswertung nicht identisch null.

### Beta-1-Firewall

Der Beweis benutzt die Gibbs-Normierung `1/zeta(beta)` und gilt **nur für `beta>1`**. Die Datei schließt `beta=1` ausdrücklich aus dieser Rechnung aus.

\[
\boxed{\beta=1\text{ wird durch I4 nicht positiv ausgewertet.}}
\]

---

## 5. NEU-219d — korrekte Twist-Orientierung und getwisteter Hochschildkozykel

Die historische Bezeichnung

\[
\theta_\beta:=\alpha_{i\beta},
\qquad \theta_\beta(a_h)=h^{-\beta}a_h
\]

passt zur KMS-Gleichung

\[
\omega(xy)=\omega(y\theta_\beta(x)).
\]

In der Standardkonvention für den getwisteten **Letztrand** muss dagegen der inverse Twist verwendet werden:

\[
\boxed{
\sigma_\beta:=\theta_\beta^{-1}=\alpha_{-i\beta},
\qquad \sigma_\beta(a_h)=h^\beta a_h.
}
\]

Für

\[
\Phi_{\beta,\chi}(a_0,\ldots,a_4)
:=\omega_{\beta,\chi}(a_0L(a_1,a_2,a_3,a_4))
\]

liefert `bL=0` zusammen mit

\[
\omega(xy)=\omega(\sigma_\beta(y)x)
\]

direkt:

\[
\boxed{b^{\sigma_\beta}\Phi_{\beta,\chi}=0.}
\]

Die alternative Behauptung `b^{theta_beta}Phi=0` in derselben Standard-Letztrandkonvention ist `✓[M]_neg`.

Damit ist für `beta>1` ein **nichtverschwindender getwisteter Hochschild-4-Kozykel** vorhanden:

\[
\boxed{
0\neq\Phi_{\beta,\chi}
\in Z^4_{\sigma_\beta,\mathrm{Hoch}}(A).
}
\]

---

## 6. Ladungsobstruktion gegen standardmäßige getwistete Zyklizität

Da `L` homogenen Grad `g` besitzt, gilt für homogene Eingaben:

\[
L(\sigma_\beta(a_1),\ldots,\sigma_\beta(a_4))
=
g^{-\beta}\sigma_\beta(L(a_1,\ldots,a_4)).
\]

Daraus folgt für die rohe skalare I4-Kochain:

\[
\boxed{
T_{\sigma_\beta}\Phi_{\beta,\chi}
=
g^{-\beta}\Phi_{\beta,\chi}.
}
\]

Für `g!=1`, `beta>0` ist `g^{-beta}!=1`. Im parazyklischen Komplex gilt in Grad 4

\[
\lambda_{\sigma_\beta}^{5}=T_{\sigma_\beta}.
\]

Daher kann

\[
\lambda_{\sigma_\beta}\Phi=\Phi
\]

nicht gelten.

\[
\boxed{
\Phi_{\beta,\chi}
\notin Z^4_{\sigma_\beta,\lambda}(A)
\qquad(g\neq1).
}
\]

Status: `✓[M]_neg` für **diesen standardmäßigen getwisteten zyklischen Kandidaten**.

### Reichweiten-Firewall gegen I5-Verwechslung

Diese I4-Gleichung betrifft die rohe KMS-Kochain `Phi_{beta,chi}`. Der spätere Finalaudit rollt eine formal ähnliche Eigenwertbehauptung für den **kanonischen Basislift `Phi_0`** zurück. Daraus folgt kein Widerspruch; die Objekte sind verschieden.

---

## 7. NEU-219e — externe Eigenlinie versus echter Koeffizient

Eine externe `Z`-Eigenlinie

\[
E_{g,\beta}=\mathbb C e_{g,\beta},
\qquad S(e)=g^\beta e
\]

kann formal den `T`-Eigenwert kompensieren:

\[
(S\otimes T)(e\otimes\Phi)=e\otimes\Phi.
\]

Status: `✓[K]` als Buchhaltungsobjekt.

Aber:

\[
T\Psi=\Psi\not\Rightarrow\lambda\Psi=\Psi.
\]

Die bloße Eigenlinie liefert keine para-/zyklische Koeffiziententheorie.

Zusätzlich existiert für `beta>0` **kein** eindimensionales unitales `sigma_beta`-äquivariantes `A_alg`-Bimodul. Aus

\[
\mu_k^*\mu_k=1
\]

muss ein Algebracharakter `chi(mu_k)!=0` erfüllen; `sigma_beta(mu_k)=k^beta mu_k` und Äquivarianz würden dann `k^beta=1` für `k>=2` erzwingen.

\[
\boxed{
\text{1-dim. unitales }\sigma_\beta\text{-äquivariantes }A\text{-Bimodul}
\quad\checkmark[M]_{\rm neg}.
}
\]

---

## 8. NEU-219f — parazyklischer Gewichtssektor und Zyklisierungsannihilation

Setze

\[
w=g^{-\beta}\neq1.
\]

Der `w`-Eigenraum von `T` bildet wegen `b^sigma T = T b^sigma` einen wohldefinierten getwisteten Hochschild-Unterkomplex:

\[
C^\bullet_{\sigma,w}(A).
\]

Damit ist die Ladung als **parazyklische Buchhaltung** mathematisch typisiert:

\[
\boxed{[O\text{-}219\text{-}5c1c\text{-para}]\quad\checkmark[K/M].}
\]

Aber gewöhnliche Zyklisierung annihiliert diesen Sektor. Auf dem `w`-Eigenraum:

\[
1-T=(1-w)\operatorname{id}
\]

ist invertierbar. Im Koinvariantenquotienten gilt daher

\[
\Phi=\frac1{1-w}(1-T)\Phi,
\]

also

\[
\boxed{[\Phi]_{\rm zyklisiert}=0.}
\]

Status:

\[
[O\text{-}219\text{-}5c1c\text{-cyc}]\quad\checkmark[M]_{\rm neg}.
\]

Firewall: Ein neu definierter „geladener parazyklischer“ Kohomologietyp wäre **neue Modellstruktur** und darf nicht als gewöhnliches `HC^4` etikettiert werden.

---

## 9. NEU-219g — Hopf-/SAYD-Typaudit

### 9.1 Gradierung gibt Koaktion, nicht kanonische Aktion

Für

\[
\Gamma=\mathbb Q_+^\times,
\qquad \mathcal H_\Gamma=\mathbb C[\Gamma]
\]

liefert die Gradierung kanonisch

\[
\delta_A(a_h)=a_h\otimes u_h.
\]

Das ist eine `H_Gamma`-**Komodulalgebra**.

Die Gradierung allein bestimmt keine kanonische `H_Gamma`-Modulalgebra-Wirkung.

\[
\boxed{[O\text{-}219\text{-}5d1b]\quad\checkmark[M]_{\rm neg}.}
\]

Nicht ausgeschlossen sind künstlich zusätzlich gewählte Wirkungen mit Zusatzstruktur.

### 9.2 Minimaler reparierter Hopf-Typ

Für den tatsächlich benötigten einzelnen KMS-Twist genügt

\[
\boxed{\mathcal H_\beta=\mathbb C[t,t^{-1}]\cong\mathbb C[\mathbb Z]}
\]

mit

\[
t^k\triangleright a_h=h^{k\beta}a_h=\sigma_\beta^k(a_h).
\]

Dies ist eine typkorrekte Modulalgebra: `✓[K/M]`.

### 9.3 SAYD-Kollision

Für eine eindimensionale SAYD-Linie mit

\[
e\cdot t^k=c^ke,
\qquad \lambda(e)=t^r\otimes e
\]

fordert Stabilität

\[
c^r=1.
\]

Damit der letzte Randterm genau den bereits bewiesenen KMS-Twist `sigma_beta=t` enthält, muss

\[
r=-1.
\]

Damit die nichttriviale Ladung kompensiert wird, muss zugleich

\[
c=g^{-\beta}.
\]

Stabilität mit `r=-1` erzwingt jedoch `c=1`. Für `g!=1`, `beta>0` widerspricht dies `c=g^{-beta}`.

\[
\boxed{
\text{Kein standardmäßiger homogener SAYD-Koeffizient über }\mathcal H_\beta
\text{ kann zugleich den einzelnen KMS-Twist und die Ladung }g\neq1\text{ kompensieren.}
}
\]

Status: `✓[M]_neg` im **standardmäßigen `H_beta`-SAYD-Setup**.

### SAYD-Reichweiten-Firewall

Nicht migrieren als „alle Hopf-zyklischen Reparaturen unmöglich“.

Offen bleibt ausdrücklich:

\[
[O\text{-}219\text{-}5d3]
\quad\text{nichtstandardmäßiger }A\text{-relativer Hopf-Koeffizient}
\quad ?[O].
\]

---

## 10. I4-Endmatrix

| Rolle | Endstand | Provenienz |
|---|---|---|
| Voller gewöhnlicher Quotient `eta notin [A,M]` | `?[O]` | OPEN |
| Direkter KMS-Detektor von `eta` | `✓[M]_neg` | P09-CORE-NOGO |
| Neutralisierer `a0^neu` | `✓[K/M]` | INCORPORATED |
| `omega_{beta,chi}(sigma_P(G_q))>0` | `✓[M]` für `beta>1` | INCORPORATED |
| `beta=1`-KMS-Auswertung | `?[O]` / nicht durch I4 bewiesen | OPEN/FIREWALL |
| `b^{sigma_beta}Phi=0` | `✓[K/M]` | INCORPORATED |
| `b^{theta_beta}Phi=0` in Standard-Letztrandkonvention | `✓[M]_neg` | P09-CORE-NOGO / convention correction |
| `Phi != 0` als `sigma_beta`-getwisteter Hochschild-4-Kozykel | `✓[K/M]` | INCORPORATED |
| Standard-getwistete Zyklizität derselben `Phi` | `✓[M]_neg` | P09-CORE-NOGO |
| Externe modulare Eigenlinie | `✓[K]`, nur formal | AUDIT-ONLY / bookkeeping |
| 1-dim. unitales `sigma_beta`-äquivariantes A-Bimodul | `✓[M]_neg` | P09-CORE-NOGO |
| `w=g^{-beta}`-Hochschild-/parazyklischer Gewichtssektor | `✓[K/M]` | INCORPORATED_part |
| gewöhnliche Zyklisierung des `w!=1`-Sektors | `✓[M]_neg` | P09-CORE-NOGO |
| `H_Gamma`-Koaktion aus Gradierung | `✓[K/M]` | INCORPORATED |
| kanonische `H_Gamma`-Aktion allein aus Gradierung | `✓[M]_neg` | P09-CORE-NOGO |
| `H_beta=C[Z]`-Modulalgebra via `sigma_beta` | `✓[K/M]` | INCORPORATED |
| abstrakte SAYD-Linien über `H_beta` | `✓[K/M]` | INCORPORATED |
| standard-SAYD: KMS-Twist + Ladung zugleich | `✓[M]_neg` | P09-CORE-NOGO |
| nichtstandardmäßiger A-relativer Hopf-Koeffizient | `?[O]` | OPEN |
| Dilatationsalgebra / invertierbares `u_g` | `?[O]`, an I5 | OPEN / ROUTED |

---

## 11. Was I4 positiv liefert

Für `beta>1` und extremale KMS-Zustände ist eine explizite, nichtverschwindende skalare Form konstruiert, die mit korrekter Standardorientierung ein getwisteter Hochschild-4-Kozykel ist:

\[
\boxed{
0\neq\Phi_{\beta,\chi}
\in Z^4_{\sigma_\beta,\mathrm{Hoch}}(A_{\rm alg}),
\qquad
b^{\sigma_\beta}\Phi_{\beta,\chi}=0.
}
\]

Dies ist ein echter positiver I4-Befund.

Gleichzeitig gilt für genau diese rohe Kochain:

\[
\boxed{
T_{\sigma_\beta}\Phi_{\beta,\chi}
=g^{-\beta}\Phi_{\beta,\chi}
eq\Phi_{\beta,\chi},
}
\]

also keine standardmäßige getwistete zyklische Klasse desselben Repräsentanten.

---

## 12. Reichweiten-Firewalls für SYN

I4 beweist **nicht**:

1. dass die I3-Hochschildklasse verschwindet — sie bleibt bestehen;
2. dass **jeder** zyklische oder getwistet-zyklische Repräsentant derselben Hochschildklasse unmöglich ist;
3. dass der volle gewöhnliche Quotient `M/[A,M]` entschieden ist;
4. dass `beta=1` durch die Gibbs-Auswertung behandelt ist;
5. dass nichtstandardmäßige A-relative Hopf-Koeffizienten ausgeschlossen sind;
6. dass die Dilatations-/Crossed-Product-Route ausgeschlossen ist;
7. dass bereits eine Weil-/Gamma-/Operatorrealisierung existiert.

Der spätere Finalaudit bestätigt ausdrücklich, dass

\[
[O\text{-}219\text{-cyclic-representative}]\quad ?[O]
\]

als nichtkanonischer Reparaturknoten offen/exportiert bleibt.

---

## 13. Routing nach I4

### Bleibt in P09

- direkter KMS-Gewichtsausschluss;
- korrekte Twistorientierung;
- nichtverschwindender getwisteter Hochschildkozykel für `beta>1`;
- standardmäßige Ladungsobstruktion gegen Zyklizität;
- parazyklischer Gewichtssektor und Zyklisierungsannihilation;
- Hopf-Typtrennung: Koaktion vs. Aktion;
- Standard-SAYD-No-go.

### Geht in I5

\[
[O\text{-}219\text{-}5e1]
\quad\text{Dilatationsalgebra / invertierbarer Ladungsträger}
\]

sowie die daraus entwickelte adelische/Morita-/Basislift-/Rotationsarchitektur `NEU-219h–z`.

### Bleibt offen/exportiert

- voller Quotient `[O-219-1]`;
- `beta=1`-KMS-Auswertung;
- nichtstandardmäßiger A-relativer Hopf-Koeffizient `[O-219-5d3]`;
- nichtkanonischer zyklischer/getwistet-zyklischer Ersatzrepräsentant;
- Weil-/Gamma-/Operatorrealisierung.

---

## 14. Fünf atomare Gegencheckfragen

### Frage 1 — KMS-Auswertung und Beta-Reichweite

Ist die Trennung korrekt, dass `omega_beta(eta_{q,P})=0` für `beta>0`, nach Gradneutralisierung aber

\[
\omega_{\beta,\chi}(\sigma_P(G_q))>0
\]

für alle extremalen `chi` und **nur im hier bewiesenen Bereich `beta>1`** gilt, während `beta=1` in I4 offen bleibt?

### Frage 2 — Twist und standardmäßige Zyklizität

Ist die Standardorientierung

\[
\sigma_\beta=\alpha_{-i\beta}=\theta_\beta^{-1}
\]

korrekt, sodass `b^{sigma_beta}Phi=0` aus `bL=0` + KMS folgt, während

\[
T_{\sigma_\beta}\Phi=g^{-\beta}\Phi\neq\Phi
\]

für `g!=1` die standardmäßige getwistete Zyklizität **dieses Repräsentanten** ausschließt?

### Frage 3 — Eigenlinie und parazyklischer Gewichtssektor

Ist korrekt, dass eine externe `g^beta`-Eigenlinie nur `T` formal kompensiert, aber keine zyklische Koeffiziententheorie liefert; dass kein 1-dim. unitales `sigma_beta`-äquivariantes `A_alg`-Bimodul existiert; und dass der `w=g^{-beta}!=1`-Gewichtssektor zwar ein `b^sigma`-Unterkomplex ist, bei gewöhnlicher Invarianten-/Koinvarianten-Zyklisierung aber annihiliert wird?

### Frage 4 — Hopf/SAYD-Reichweite

Ist die Typtrennung korrekt: die `Q_+^x`-Gradierung liefert kanonisch eine `H_Gamma`-Koaktion, nicht eine kanonische `H_Gamma`-Aktion; `H_beta=C[Z]` wirkt dagegen durch `sigma_beta`; und im standardmäßigen `H_beta`-SAYD-Setup kollidieren KMS-Twist (`r=-1`) und Ladungskompensation (`c=g^{-beta}`) mit Stabilität (`c^r=1`), ohne den nichtstandardmäßigen A-relativen Hopf-Knoten auszuschließen?

### Frage 5 — Gesamtfirewall / späterer Finalaudit

Ist korrekt eingefroren, dass I4 den I3-HH4-Cup nicht zurückrollt, den vollen Quotienten `M/[A,M]` nicht entscheidet und **nicht alle** möglichen zyklischen/getwistet-zyklischen Repräsentanten ausschließt; dass die Dilatationsroute erst I5 betrifft; und dass der spätere Rollback von `t Phi_0=g^{-beta}Phi_0` nur den kanonischen Basislift `Phi_0` betrifft, nicht die rohe I4-Kochain `Phi_{beta,chi}`?

---

## 15. Pass-A-Urteil

Kein interner Gegenbefund zur reconciliierten I4-Kette.

\[
\boxed{
\text{P09 / I4 PASS A COMPLETE — GEGENCHECK AUSSTEHEND}
}
\]

Bei Gegencheck ohne Befund: I4 versiegeln und I5 (`NEU-219h–z` + Finalaudit) aktivieren.
