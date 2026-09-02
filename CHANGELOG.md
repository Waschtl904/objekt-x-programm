# Changelog

Sitzungsprotokoll des Objekt-X-Programms, neueste Einträge zuerst.

> **Operativer Forschungsstand: 2. September 2026 — P11 Strong Terminal / R43.**  
> Der nachfolgende NEU-Changelog bleibt als historisches Journalprotokoll erhalten; die neuen
> P11-Auditblöcke R38--R43 werden in diesem Addendum separat geführt.

Die Einträge ab NEU-162 sind aus der Commit-Historie des Arbeitsjournals rekonstruiert und
zu thematischen Blöcken zusammengefasst. Für Details siehe die jeweiligen Dokumente über
den [Gesamtindex](INDEX.md).


---

## [P11 R38–R43] — 2. September 2026: Strong Terminal auf einen Normal-Koeffizienten reduziert

Die Strong-Terminal-Front wurde in fünf unabhängig überprüften Auditblöcken stark verdichtet:

- **R38** — Modulus-/WOT-Clustergeometrie, formal frozen auf Commit `ab2aff076934f2b3d330a509f3aed7be4b504d10`.
- **R39** — Strong-Terminal-/Baseline-Firewall und exakter Cross-Terminal-Cauchy-Gate, frozen auf `0af33a6024d74e0e7a8f65bf8668c0d906d6cc86`.
- **R40** — Dualnormalen-Skala \(\|v_{X,U}\|\asymp U^{-1}\), frozen auf `4f93f314a58973328a5804c42202bedded8953a0`.
- **R41** — zweiter Hard-Constraint-Gamma-Layer und exakter Ratio-Limes, frozen auf `2ac1e5387f849321288bf64b3f8fc4d4008050ef`.
- **R42** — Dualnormalen-Richtung, strikte \(\gamma_R<\gamma_S\), tangentialer Polar-Collapse und echte Future-Transport-Konvergenz auf Kodimension eins; Freeze `7aff837d0a11a18dbf1818a936bd67bcda93bf54`, Ledger-Bereinigung `f495ce6d89dcb8facc8fa0d4e09dda279b24fb73`.

Governance für R38--R42:

\[
\boxed{\text{FROZEN — independently verified AI-GREEN}}
\]

aber **keine** kanonische \(\checkmark[M]\)-Promotion.

R42 reduziert für jedes feste \(0<R<S\) den gesamten verbleibenden Strong-Terminal-/C6-Gate auf

\[
\boxed{
\operatorname{Re}\langle
\varepsilon_R,K_{R,S}^{T,U}\varepsilon_R
\rangle
\longrightarrow1
\qquad(T,U\to\infty).
}
\]

Der echte Future-Transport konvergiert bereits stark auf
\[
H_R^0=\ker\beta_R^{(0)},
\]
also auf einem abgeschlossenen Unterraum von Kodimension eins.

### R43 Phase I — offen / exploratory

R43 wurde auf Commit `43a6762a55497f139e0f4b4f45a3865ddcf7cc28` eröffnet, mit
`973a25ec6f8e1bf5335898905cfb3ac5a8771684` um die reskalierte Edge-Form-Front ergänzt und
mit `5432ec1a9d845d63316a2eccc28662545a0c7619` um das Zwischenradius-/Gamma-Zyklizitätsgate erweitert.

Derzeitiger Hochrisikokandidat in R43 ist
\[
D_U(z_U,z_U)=O(U^{-1}),
\]
noch ohne externe Verifikation. Die Gamma-Zyklizitätsfrage ist ebenfalls offen.

**Firewalls:** Strong Terminal/C6 bleibt \(?[O]\). R37/G4c bleibt separat offen. Keine Aussage
R38--R43 darf R37 rückwirkend promovieren; kein Object-X- oder RH-Abschluss folgt.

---

## [NEU-228] — 26. Juli 2026: Der $u$-Regulator ist die Hebungswahl

$$[O\text{-}226\text{-}3] \equiv [O\text{-}153] \equiv [O\text{-}221\text{-}1c1a0]$$

**Die $u$-Summe ist kein Regulator.** NEU-153 definiert
$\Psi_p(\widehat\varepsilon_p)=\Pi_{W_{\mathrm{res}}}\widetilde\omega_2(\widehat\varepsilon_p,L_3^\circ)$.
Mit (43.1) und $\widehat\varepsilon_p=\sum_u a_{p,u}e_uV_p$ ist die Summe in (51.2) die
**Hebungsentwicklung**; NEU-51 schreibt sie mit $a_{p,u}\equiv1$. Der Regulator sitzt
eingangsseitig und ist auf die affine Faser $\mathcal L_p$ eingeschränkt — nicht frei, aber
auch nicht eindeutig.

**Option R2 widerlegt.** $\pi_{\mathrm{prim}}(e_0V_p)=\varepsilon_p$, $\pi_{\mathrm{prim}}(e_uV_p)=0$
für $u\neq0$ (153 Z.179). Der Projektor selektiert also $u=0$ — und der Kopplungsfaktor
$-us\log p$ verschwindet dort. $V_p^{\mathrm{can}}=0$. Eindeutigkeit und Nichtnullheit sind mit
$\pi_{\mathrm{prim}}$ **nicht** gleichzeitig erfüllbar; zulässig ist $\{u\neq0\}$. `✓[M]_neg`
Genau deshalb verlangt NEU-153 Z.188 $f_p\neq0$.

**Symmetrie-No-Go tritt nicht ein.** $\pi_{\mathrm{prim}}U_k\neq U_k\pi_{\mathrm{prim}}$ — der
$p$-Kanal bricht die Fouriertranslation geometrisch. Die Einzelmodenselektion scheitert nicht
an einer Symmetrie, sondern am Kopplungsfaktor. `✓[M]`

**`[O-226-4]` ebenfalls nicht neu.** Der Gramoperator $g^{(p)}_{uu}$, $g^{(p)}_{0u}$ steht in
NEU-153 §D.0.5 (Z.461/462) und ist dort seit 13. Juli 2026 offen, samt Positivität und
Vollständigkeit von $\mathcal H_p^{\mathrm{lift}}$.

**Rücklauf.** Ohne 153.A (starke Vektorinvarianz) oder 153.B (schwache Norminvarianz) ist $V$
und damit die Schattenklasse von $K(z)$ **hebungsabhängig**. Zwei unabhängige Zugänge — die
Primkanalgewichte aus Strang 05 und der Feshbach-Transfer aus Strang 01 — enden am selben
Knoten. Keine Rückschritt, sondern Konvergenz: er ist die Wohldefiniertheitsbedingung der
gesamten Transferschicht.

**Leerfaser-Risiko `[O-228-2]`, neue Priorität 1.** NEU-153 Z.207: liegt $e_0V_p$ normiert und
$\perp\ker\pi_{\mathrm{prim}}$ bei positiv definiter verbundener Form, ist $\mathcal L_p$ leer
— dann existiert keine zulässige Kopplung und die Feshbach-Linie entfällt. Quellenseitig
nicht ausgeschlossen. Sperrvermerk: keine Schattenklassenrechnung davor.

**Reichweitenkorrektur.** $V\notin\mathcal S_2$ ist **notwendig** für den Nicht-$\mathcal S_1$-
Zeugen; $V\in\mathcal S_4$ ist **hinreichend**, nicht notwendig für $K(z)\in\mathcal S_2$ —
der Resolvent kann zusätzlich glätten.

Regulatoroptionen abschließend klassifiziert: R1 (freie Gewichte) `✓[M]_neg` Anti-Fitting,
R2 `✓[M]_neg`, R3 (freies $U_p$) `✓[M]_neg`, R4 (Hebungswahl) `❓[O]` — intrinsisch genau dann,
wenn 153.A/B gilt.

---

## [NEU-227] — 26. Juli 2026: Koordinatenwörterbuch und Spektralmaßform

**Beide Vorschaltknoten geschlossen.**

**`[O-226-2]` `✓[M]` — kein Entweder-oder.** (51.2) definiert die *Kopplung* $V_p$, (55.3) die
*Dynamik* von $J^-$; NEU-42 trennt beides bereits. Verbindliches Wörterbuch:
$\eta_{p;m;s,u}\leftrightarrow e_RV_M$, $M=pm$, $R=u+ps$. Wegen $u+ps+pm=u+p(s+m)$ ist
$R\mapsto R+M$ identisch mit $s\mapsto s+m$; auch das Gewicht stimmt,
$R\log M=(u+ps)\log(pm)$. Ein Sprung $R\mapsto R\pm d$ hält die $u$-Restklasse genau dann,
wenn $p\mid d$. **Rückwirkung:** Im Primsektor entfällt $d=1$ wegen $\log1=0$ und $d=p$
erfüllt $p\mid d$ — die Annahme „bei festem $u$" aus NEU-225 §3 ist damit **gerechtfertigt**,
nicht bloß gesetzt. Die alte Darstellung wird nicht negativ geschlossen; zurückgerollt ist nur
ihre Verwendung ohne Wörterbuch.

**`[O-226-1]` `✓[K/M]` — Spektralmaßform.** Kreuzspektralmaß
$\mu^{a,b}_{pq}(B)=\langle V_pa,E_D(B)V_qb\rangle$, komplexes endliches Borelmaß mit
$\lvert\mu\rvert(\mathbb R)\le\lVert V_pa\rVert\lVert V_qb\rVert$. Ersatz für (51.3):
$\langle a,K_{pq}(z)b\rangle=\int(\lambda-z)^{-1}d\mu^{a,b}_{pq}$. Ersatz für (51.4):
$M_{pq}(B)=V_p^*E_D(B)V_q$. Ersatz für (51.7):
$\lvert D-z\rvert^{-1/2}V\in\mathcal S_2$. Das Spurklassekriterium
$K_N(z)=B_z^*U_zB_z$, $B_z=\lvert D-z\rvert^{-1/2}V$, wurde nachgerechnet: $U_z$ und
$\lvert D-z\rvert^{-1/2}$ sind beide Borelfunktionen von $D$ und kommutieren.

**Abgeleitet.** Aus $\operatorname{Tr}\operatorname{Im}K_N(z)\le\lVert V\rVert_2^2/y$ folgt:
der Nicht-$\mathcal S_1$-Zeuge ist **nur möglich, wenn $V\notin\mathcal S_2$**. Das verschärft
die Vermutung $V\in\mathcal S_4\setminus\mathcal S_2$ zur Notwendigkeit — hinreichend ist es
nicht, da die Spektralmasse ins Unendliche entweichen kann. `[O-226-6]` hängt damit direkt an
`[O-226-3]`.

NEU-46s lokale Streudateninterpretation bleibt gültig, nur von der Eigenbasisannahme befreit.

**Der Einstiegspunkt ist verschoben:** nicht die Schattenklassensumme, sondern der
$u$-Regulator `[O-226-3]` und der Gramoperator des überlappenden Kopplungsraums `[O-226-4]`.
Regel: der Regulator darf nicht nachträglich an $\Xi$-Daten angepasst werden.

BESTANDSAUFNAHME (neuer §0) und EINSTIEGSPROMPT auf die neue Hauptlinie umgestellt;
KONVENTIONEN um Wörterbuch, Spektraldarstellung und Regulatorregel ergänzt.

---

## [NEU-226] — 26. Juli 2026: Quellenaudit NEU-51/77 — Feshbach-Transfer und Primkanalüberlappung

**Drei Befunde, davon einer gegen NEU-225 selbst.**

**Widerlegt: der endliche-$N$-Befund.** $K_N(z)$ ist bei festem $N$ **nicht** endlich-rangig.
Nach (51.2) ist die Quelldomäne von $V_p$ von allen $e_sV_m$ aufgespannt, und (51.3) trägt
Doppelindizes $K_{pq}(s)_{(r,n),(t,m)}$: jeder Primkanal ist für sich unendlichdimensional.
Die $\mathcal S_1$-Bedingung (51.7) summiert innerhalb jedes Primkanals über $n,r,u$ und ist
`?[O]`. $\mathcal S_2\setminus\mathcal S_1$ ist bei festem $N$ **nicht** ausgeschlossen, und
$\det_2$ wird von (51.8)/(51.9) ausdrücklich schon für endliches $N$ geführt. `✓[M]_neg`

**Beantwortet: der Kreuztermmechanismus.** Satz 51.3 (51.5): $\mathcal K_N\neq\bigoplus_pK_p$,
*„weil die $\eta_{p;n;r,u}$ keine kanaldiagonale Basis erzwingen"*. Der Mechanismus ist die
**Überlappung der Primkanalbilder**: nach (51.2) gilt $\eta_{p;m;s,u}\sim e_{u+ps}V_{pm}$, und
verschiedene $(p,m)$ treffen dasselbe $V_{pm}$. $D_{\mathrm{rel}}$ selbst bleibt
kanalerhaltend — die Off-Diagonalität sitzt in der Kopplung, nicht im Operator. `✓[M]`

**Zurückgerollt: NEU-225 §1.2.** Die dortige Festlegung, die $\eta$-Familie sei global
orthonormal, ist damit falsch. Verbindlich bleibt nur Orthonormalität **innerhalb** einer
Kette bei festem $(p,m,u)$. `✓[M]_neg` Die Primfaserdiagonalisierung aus NEU-225 ist
unberührt und gilt in beiden Indexlesarten.

**Blocker.** (51.3)/(51.4)/(51.7) setzen $D_{\mathrm{rel}}\eta_\alpha=\lambda_\alpha\eta_\alpha$
voraus. Nach NEU-225 hat $D_{\mathrm{rel}}$ rein absolutstetiges Spektrum und keine
Eigenwerte; NEU-52 (52.D0) hatte das bereits verboten. Die Schattenklassenkriterien sind in
dieser Form nicht auswertbar. Vorschaltknoten `[O-226-1]`: auf Spektralmaßform umschreiben.

**NEU-77.** Die Feshbach-Identität $\Pi_NS_NR_ND_{BC,N}\Pi_N^*=J_N^-$ ist bei endlichem $N$
exakt ohne Fehlerterm `✓[M]`. Der Limes ist jedoch nur punktweise auf endlich getragenen
Vektoren, **nicht** normkonvergent (Punkt D), und der Normierungsfaktor $\lvert S_N\rvert^{-1}$
ist offen (Punkt E). Schattenklassen sind keine punktweisen Invarianten — die Klasse von
$K(z)$ ist daher aus den $K_N(z)$ **nicht** erschließbar.

**Bestätigt.** $V_p=C_p^{\mathrm{rel}}$ steht quellenseitig fest. Der $\operatorname{Im}K(z)\ge0$-
Zeuge ist zulässig, da NEU-225 §1.1 Option B (selbstadjungiert) verbindlich gemacht hat.
Freiheitsgrad ist der $u$-Regulator (51.1): *„Diese Wahl entscheidet später über
$\mathcal S_1$ vs. $\mathcal S_2$."*

Revidierte Reihenfolge: `[O-226-1]` Spektralmaßform, `[O-226-2]` Wörterbuchkonflikt
(55.3) gegen (51.2), `[O-226-3]` $u$-Regulator, `[O-226-4]` orthonormale Primkanalbasis —
danach erst die Schattenklassensummen.

---

## [NEU-225] — 26. Juli 2026: Primfaserdiagonalisierung — $D_{\mathrm{rel}}$ ist ein Transportgenerator

**Der reduzierte kompakte Resolvent ist ausgeschlossen. HP-2 ist die falsche Forderung an diese Schicht.**

**Konventionsbereinigung.** $J_N^-=\frac12(\Theta_N-\Theta_N^\dagger)$ (37.1) ist verbindlich;
$\frac{1}{2i}(\cdots)$ aus NEU-35/62 heißt ab sofort $S_N$ und ist ein anderer,
selbstadjungierter Operator. $\{\eta_{p;m;r,u\}}$ orthonormal (quellenintern über 55.4).
Wörterbuch $(r,n)\leftrightarrow(p,m,r,u)$ festgeschrieben. Siehe KONVENTIONEN.md.

**Reaudit NEU-56.** Der Widerspruch in Satz 56.1/56.2 benutzt ausschließlich Testvektoren,
keine Invarianz und keine Spektralrestriktion. **Satz 56.2 bleibt gültig**; nur die
Raumbezeichnung wird korrigiert.

**Rechnung.** Auf der Primfaser $m=p$ ist der einzige Teiler $>1$ gleich $p$, also
$J^-\eta_r=\frac{\alpha_p}{2}(r\eta_{r+p}-(r-p)\eta_{r-p})$. Zerlegung nach $r\bmod p$ liefert
Ketten $J^-e_k=c_p((k+\delta)e_{k+1}-(k-1+\delta)e_{k-1})$ mit $c_p=\frac12\gamma_N p\log p$ —
ein **Dilatationsgenerator**, keine konfinierende Jacobi-Matrix. Fourier:
$\mathcal FD_{\mathrm{rel}}\mathcal F^{-1}=ic_p[2\sin\theta\,\partial_\theta+\cos\theta]-c_p(2\delta-1)\sin\theta$.
Logarithmische Koordinate $t=\log\tan(\theta/2)$ und beschränkte Eichung entfernen den
$\operatorname{sech}$-Term:

$$D_{\mathrm{rel}}\big|_{\mathcal H_{p,a}}\cong 2ic_p\,d/dt \ \text{ auf } L^2(\mathbb R)^{\oplus2}.$$

Rein absolutstetiges Spektrum $\mathbb R$, keine Eigenwerte, also kein Kern in den
Primsektoren und $\mathcal H_p\subseteq(\ker D_{\mathrm{rel}})^\perp$. Explizite
graphnormbeschränkte Orthonormalfolge (verschobene Buckel) — realisierungsunabhängig.

$$\text{Auch der reduzierte kompakte Resolvent ist ausgeschlossen.} \quad \times[M]$$

Numerisch kontrolliert: Schiefsymmetrie exakt, Fourierform auf $6{,}9\cdot10^{-7}$, Buckel
orthonormal bei konstanter Graphnorm.

**Offener Vorbehalt:** Ist $\mathcal D_0$ ein Kern der selbstadjungierten Realisierung?
Das ist derselbe Vorbehalt wie in (55.17) und trägt nicht das Ergebnis. `[O-225-1]`

**Schichtenverschiebung.** $D_{\mathrm{rel}}$ ist ein Streu-/Transportgenerator, kein
Hilbert–Pólya-Operator. Konfinement scheiterte in NEU-56 strukturell, nicht an der Wahl von
$\gamma_N$ oder $L$. Das kompakte Objekt sollte eine Ebene später entstehen, als
Feshbach-/Birman–Schwinger-Transfer $K_N(z)=V_N^*(D_{\mathrm{rel}}-z)^{-1}V_N$ — dort könnten
HP-2, HP-3, HP-5 und die zyklische Weyl-Funktion zusammentreffen. **Arbeitshypothese**,
kein Ergebnis: `[O-225-2]`, neue Hauptlinie.

Unberührt: HP-2 ist für Objekt X nicht widerlegt, nur für $H_X=D_{\mathrm{rel}}$. Die
RH-Hinrichtung braucht nur Selbstadjungiertheit (NEU-56 §4).

---

## [NEU-224] — 26. Juli 2026: Kernbestimmung, Antisymmetrisierung und effektiver Raum

**`[O-223-2a]` ergab ein Ergebnis und drei Quellenkorrekturen.**

**Quellenkritik.** NEU-27/31/33 definieren $\Theta(e_rV_n)=r\log(n)e_{r+n}V_n$ als reine
Aufwärtsverschiebung. NEU-37 (37.1) und NEU-35/70 definieren $J_N^-$ als **Antisymmetrisierung**
$\frac12(\Theta_N-\Theta_N^\dagger)$. Der Träger (55.1)/(55.3) beschreibt daher $\Theta_N$,
**nicht** $J^-$, und ist mit $(J^-)^*=-J^-$ (54.3) unverträglich. `✓[M]_neg`
Die Betragsabschätzungen (55.5)/(55.9)/(55.12) sind davon **unberührt** (Faktor $\le2$);
die Obstruktion aus NEU-56 bleibt gültig.

**Widerlegt.** Die flache Achse $r=0$ (NEU-54 §5) ist flache Achse von $\Theta_N$, nicht von
$J^-$: die Rückwärtskanten aus $r=-n$ tragen $\gamma_N n\log n\neq0$. `✓[M]_neg`

**Ergebnis.** Die Faser $m=1$ (bzw. $n=1$) liegt vollständig im Kern — beide Kantenrichtungen
tragen $\log 1=0$ — und ist unendlichdimensional, unabhängig von $\gamma_N$ und $N$. Also
$\dim\ker D_{\mathrm{rel}}=\infty$, und $(1+D_{\mathrm{rel}}^2)^{-1/2}$ wirkt dort als
Identität:

$$D_{\mathrm{rel}} \text{ besitzt auf } \mathcal H_{\mathrm{rel}} \text{ keinen kompakten Resolventen.} \quad \times[M]$$

**Weitere Korrektur.** $\mathcal D_0^{\mathrm{eff}}$ nach (55.0) verlangt $r\neq0$ **und**
$m>1$ und ist damit echt kleiner als $(\ker D_{\mathrm{rel}})^\perp$ sowie nicht invariant
unter $J^-$. Korrekt ist $\{m>1\}$ allein. `✓[M]_neg`

**Vereinfachung.** $(\ker D_{\mathrm{rel}})^\perp$ reduziert $D_{\mathrm{rel}}$ automatisch
(Spektralsatz); NEU-223 Rev. 2 hatte das zu Unrecht als schweren Knoten geführt. Offen bleibt
nur die Identifikation mit dem Präabschlussbild $\overline{\operatorname{Ran}(J_0^-)}$.

**Redaktionsschulden:** Normierung $\frac12$ (NEU-37) gegen $\frac{1}{2i}$ (NEU-35/62) — nur
erstere ist schiefadjungiert; explizite $\eta$-Definition samt Skalarprodukt fehlt;
$(r,n)\leftrightarrow(p,m,r,u)$-Übersetzung fehlt.

Nachfolgeknoten `[O-224-1a–d]`. XVI-D/P5 entsprechend korrigiert.

---

## [NEU-223] — 26. Juli 2026: Vergleichsoperator, Schur, Konfinement, kompakter Resolvent

**Quellenaudit NEU-52–56. Zwei Befunde ändern die Zielnormalform.**

1. **HP-2 ist für die RH-Hinrichtung nicht erforderlich.** NEU-56 §4: Für
   $\mathrm{Spec}\subset\mathbb R$ genügt Selbstadjungiertheit; der Engpass entscheidet nur
   über den Spektraltyp. G3 betrifft ausschließlich das HP-Profil.
2. **Die $\tilde L$-Klasse ist quellenseitig auf einen Kandidaten reduziert.** (N1) verlangt
   $L$ groß, (K) verlangt $L$ klein, zusammen $L\simeq\lvert D_{\mathrm{rel}}\rvert$
   (NEU-56 §1). NEU-56 §7 nennt $\tilde L=(1+(J^-)^2)^{1/2}$: (K) wird trivial, die
   Verträglichkeitsbedingung entfällt.

Vier Aussagen strikt getrennt: Selbstadjungiertheit (N1)/(N2), Vergleichsoperatorabschätzung,
Konfinement (K), kompakte Einbettung. Die Trennungsregel (54.SEP) stand bereits in NEU-54.
Konstanten sind **nicht** uniform in $N$; (55.16) wächst wie $\gamma_N m\log m$.

Verbrauchte Freiheitsgrade: skalares $\gamma_N$ (A, A′), separables $m$-Gewicht (B1 —
partielles Konfinement nur in der $r$-Achse), $L$-Rekalibrierung (B2 — rettet Schur, ruiniert
(K)). Abgeleitet: Rekalibrierungen scheitern in **beiden** Ordnungsrichtungen.

Typkorrektur: $s_k(J^-)$ ist für unbeschränktes $J^-$ nicht definiert. Relevantes Objekt ist
$(1+(J^-)^2)^{-1/2}$; die Zielnormalform kollabiert auf dessen Kompaktheit auf
$\mathcal H^{\mathrm{eff}}_{\mathrm{rel}}$. Ein negativer Ausgang wäre eine erheblich
stärkere No-Go-Klasse als NEU-56.

Sperrvermerk: „$D_N$ diskret $\Rightarrow$ $D_\infty$ kompakt resolvent" ist unzulässig.

**Revision 2 (Gegenlese).** Zwei Präzisierungen: (a) Die Reduktion ist eine
**Graphnormklasse** $\lVert\tilde Lx\rVert+\lVert x\rVert\asymp\lVert\lvert D_{\mathrm{rel}}\rvert x\rVert+\lVert x\rVert$,
keine Operatorgleichheit — der Suchraum kollabiert auf eine Kompaktheitsfrage, nicht auf
einen Operator. (b) **Vorzeichenkorrektur:** $(1+(J^-)^2)^{1/2}$ aus NEU-56 §7 ist typwidrig,
da $(J^-)^*=-J^-$ (54.3) und damit $1+(J^-)^2=1-D_{\mathrm{rel}}^2\not\ge1$; korrekt ist
$(1+D_{\mathrm{rel}}^2)^{1/2}$. `✓[M]_neg` Ferner: der reduzierende Spektralraum
$E_{D_{\mathrm{rel}}}(\mathbb R\setminus\{0\})\mathcal H=\mathcal H^{\mathrm{eff}}$ ist eine
eigene offene Bedingung, in 55.0 nicht belegt; Kernabspaltung allein genügt nicht.
Binärer Test mit negativem Zeugen und Weyl-Folge aufgenommen.

Nachfolgeknoten `[O-223-2]` mit Teilknoten a–d. XVI-D/P5 entsprechend korrigiert.

---

## [NEU-222] — 26. Juli 2026: Trassenaudit der singulären Route — Statuskorrektur

**Reines Quellenaudit. Ergebnis: Die als offen geführte Entscheidungsfrage war überholt.**

`[O-209-5]` und `[O-209-6]` sind seit dem 20. Juli durch NEU-210 geschlossen
($Z_g=\{0\}$ exakt via Pontrjagin; faktoriales Ursprungspotential mit
$\operatorname{Sing}(X)=\{0\}$). `[O-207-5b]` gehört zur verlassenen mehrdimensionalen
Gitterroute; die faktoriale Kette erreicht Normkonvergenz direkt über das Transportband
$P_j \le E_{L_j/k} \le P_{j-k}$ und fällt damit in die von NEU-207 ausdrücklich
offengelassene Klasse der approximativen Ketten.

**Die singuläre Route trägt bis $HH^4$:** NEU-210 → 211 ($D_g$, Nichtinnerheit) →
212/216 (Zieltyp) → 217 (globale Nichtinnerheit) → 218 (Cup-Aufstieg). Sie endet an der
**Zyklizität** (NEU-219u), nicht an der Konstruktion.

Korrigiert: Ebene XVI XVI-D/P4 (führte geschlossene Knoten als offen und P4 als
Entscheidungsknoten), Bestandsaufnahme §4.1 („kohomologische Schicht steuert auf Leere
zu" — zurückgenommen) und die G4-Priorisierung (entfällt; G3 rückt auf Rang eins).

Verbleibend offen auf der Trasse: `[O-212-5]`, `[O-213-3/5]`, `[O-214-4b]`, `[O-217-1d]` —
technische Restknoten, keine Existenzentscheidungen.

---

## [NEU-221e] — 26. Juli 2026: Hebungsfaser, Wres-Quotient, Spektralmaßabstieg

**Typaudit des Kopplungsvektors. Das exakte Abstiegskriterium ist bewiesen, seine
Verifikation gesperrt. `[O-221-1c1a]` steigt von `?[O]` auf `✓[M]_part`.**

Die Kernkorrektur: Weil NEU-46 den relativen Vektor als **zyklischen** Vektor einer
Weyl-Funktion verwendet, ist die Hebungsfrage **nicht** durch Normgleichheit entschieden.
Verschieden gewählte, gleich normierte Hebungen können verschiedene Resolventenmatrixstellen,
Spektralmaße und inverse Momente erzeugen.

Drei Ebenen werden getrennt: algebraische affine Liftfaser $\widehat\varepsilon_p^{\,0}+K_p$ ·
exakt zulässige normierte Liftmenge $\widehat{\mathcal E}_p^{\mathrm{adm}}$ ·
Wres-Quotientbildung im **relativen** Zielraum.

| Ergebnis | Status |
|---|---|
| Exaktes Abstiegskriterium $\widetilde T_p^{\mathrm{raw}}(\Delta_p^{\mathrm{adm}}) \subseteq \mathcal N_{\mathrm{Wres,rel}}$ | `✓[M]` |
| Roh- und quotientierte Kopplung typologisch getrennt: $T_p^{\mathrm{rel}} = Q_{\mathrm{Wres,rel}}\circ\widetilde T_p^{\mathrm{raw}}$ | `✓[K]_part` |
| $\Delta_p^{\mathrm{adm}} = \mathcal A_p^{\mathrm{adm}} - \mathcal A_p^{\mathrm{adm}}$ ist die **Differenzmenge**, im Allgemeinen echt größer als $\mathcal A_p^{\mathrm{adm}}$ (157.2) | `✓[M]` |
| Ungeladener Rohkandidat $e_0V_p$ ausgeschlossen — $\widetilde T_p^{\mathrm{raw}}(e_0V_p)=0$ | `✓[M]_neg` |
| Rang-eins-Bildstabilisator ist $U(1)$ — nur im **positiven** Hilbertraumfall | `✓[M]` konditional |
| Verifikation des Abstiegs auf $\Delta_p^{\mathrm{adm}}$ | **gesperrt** |
| Beschränktheit/Rang von $T_p^{\mathrm{rel}}$ auf ganz $B_{3,p}^{\mathrm{lift}}$ | `?[O]` |
| Spektralmaßinvarianz, Liftstabilisator, intrinsische Sektion | `?[O]` |

Vier Typkorrekturen gegenüber dem Vorentwurf: das Wres-Radikal muss **vor** dem Quotienten
formuliert werden; $K_p$ ist nicht die Menge zulässiger Hebungsänderungen; der Zielraum muss
der **kantenmarkierte** relative Raum sein; Rang eins und Beschränktheit von
$C_p[\widehat\varepsilon_p]$ folgen aus dem eindimensionalen Definitionsraum und sagen nichts
über die Rohabbildung.

Typwarnungen: Bei indefiniter Form ist das Radikal **nicht** die Menge isotroper Vektoren.
Der Schluss $C_pC_p^{\#}=C_p'C_p'^{\#} \Rightarrow \Psi_p'=e^{i\theta}\Psi_p$ setzt die positive
Hilbertrealisierung voraus.

Nächster atomarer Knoten: `[O-221-1c1a0-admissible-difference-locus-and-raw-relative-coupling]`.

Parallel: **Ebene XVI Revision 2** — das Axiomenregister wurde von Stand NEU-114 auf NEU-221e
nachgezogen und in ein Kontrollblatt mit drei logischen Ebenen umgebaut.
Siehe [`00-grundlegung/ebene-XVI-objekt-x.md`](00-grundlegung/ebene-XVI-objekt-x.md).

---

## [NEU-221 – NEU-221d] — 26. Juli 2026: Adelische Momentquelle

**Ziel: eine adelische Quelle für die positive Momentfolge des Hankel-Kriteriums.
Zwischenstand — die Quelle ist noch nicht konstruiert, aber die fehlenden Bestandteile sind
exakt benannt.**

| Eintrag | Ergebnis | Status |
|---|---|---|
| NEU-221 | Sichtung vorhandener BC-/KMS-Quellen; erster normalisierter positiver Weil-Momentkandidat | `✓ [K]` |
| NEU-221c | Zyklischer Feshbach-Weyl-Kandidat, quadratische Resolvente, Normierungs-Firewall für den Quellvektor | `✓ [K]` |
| NEU-221d | Direktextraktion aus NEU-46: $D_N^{\mathrm{rel}}$ ist selbstadjungiert, aber $(\mathcal H_N^{\mathrm{rel}}, D_N^{\mathrm{rel}}, \Psi_N)$ ist **noch kein vollständig typisiertes zyklisches Tripel** | `✓ [M]_part` |

Offen nach NEU-221d: Typisierung von $\varepsilon_p, \Psi_p$ als konkrete Hilbertvektoren,
quellseitige Fixierung von $\lVert\Psi_N\rVert$, Nullmodusfreiheit $E_{D_N^{\mathrm{rel}}}(\{0\})\Psi_N = 0$,
Endlichkeit der inversen Momente $\int\lvert\lambda\rvert^{-2k-2}d\mu_{\Psi_N}$ für $k=0,1,2$
sowie die vollständig gekoppelte endlich-archimedische Geometrie.

---

## [NEU-220 – NEU-220w] — 25.–26. Juli 2026: Weil-Explizitformel bis Hankelpositivität

**Der bislang stärkste Strang. Endet mit einer unkonditionalen RH-Äquivalenz.**

### Archimedischer Faktor (NEU-220 – 220g)

| Eintrag | Ergebnis |
|---|---|
| NEU-220 / 220a | Quelltyp und Zielraum des Gammafaktors; zentrierte Mellin-Koordinate, Involutionskompatibilität |
| NEU-220b | Gamma-Symbol als temperierte Distribution konstruiert |
| NEU-220c / 220d | Repository-Audit der Weil-Normierung; Trennung von Pol- und Gammaanteil, Korrektur des rohen Polterms auf der kritischen Linie |
| NEU-220e | **No-Go:** gewöhnliche Hilbertspur unzureichend — $\Lambda_\Gamma$ verlangt eine semifinite Spur |
| NEU-220f / 220g | Gamma-Symbol als archimedische Streuphasenableitung; typkorrekte Zusammenführung endlicher und archimedischer Spurformen |

### Konturtransport und Weil-Form (NEU-220h – 220m)

| Eintrag | Ergebnis |
|---|---|
| NEU-220h / 220i | Endlicher Weil-Port aus NEU-28; Zeta-Quotient als endlicher Streufaktor ausgeschlossen |
| NEU-220j / 220k | Holomorpher Weil-Testkern, Konvergenz der Nullstellensumme, Horizontalabschätzung; Xi-Masterkontur mit exakten Vorzeichen, Faktor 2 und Polbuchhaltung ohne Doppelzählung trivialer Nullstellen |
| NEU-220l | Weil-Quadratform über zentrierte Autokorrelation typisiert; RH-Positivität von der Spektralrealisierung getrennt |
| NEU-220m rev.2 | Gesamt-Weilform auf der Testfunktions-Rigging; Korrektur von Pol- und Primpolarisierung, Gammadomänen, indefiniter Abschließbarkeit |

### Grenztyp und Krein-Raum (NEU-220n – 220t)

| Eintrag | Ergebnis |
|---|---|
| NEU-220n – 220p | Endliche Fensteroperatoren selbstadjungiert; Randflucht bewiesen; globale Spur nicht abschließbar; erweiterter Graphenraum konstruiert |
| NEU-220q | Prim-Pol-Renormierung; RH-äquivalentes Temperiertheitskriterium |
| NEU-220r | Fourier-Nullstellenmaß identifiziert; Lebesgue-$L^2$-Multiplikator ausgeschlossen; bedingtes Spektralmodell |
| NEU-220s rev.2 | Unkonditionales Nullstellenpaar-Kreinmodell; RH als Kollaps zur positiven Metrik; Korrektur der Multiplizitäts-Doppelzählung |
| NEU-220t | Vollständige Klassifikation der Metrikblöcke; **Off-Axis-Trägheit, Positivitäts-No-Go, Similarity-No-Go**; beschränkte Similarity zu positiver Metrik ist RH-äquivalent |

### Hankel-Kriterium (NEU-220u – 220w)

| Eintrag | Ergebnis |
|---|---|
| NEU-220u | Spektraldeterminantenklasse von $\Xi$ fixiert; **gewöhnliche Spurklassen-Determinante ausgeschlossen**; Resolventenspur als Ziel |
| NEU-220v rev.2 | Xi-Determinante als Stieltjes-Resolventenspur; Hankel-Positivitätshierarchie; Korrektur der Quadratnullstellen-Implikation |
| **NEU-220w** | **Vollständige Hankel-Hierarchie ist RH-äquivalent** — beide Richtungen bewiesen; Moment-GNS-Weyl-Modell; Quantisierung des semifiniten Spektralmaßes |

$$\mathrm{RH} \iff H_N^{(0)}\succeq 0 \ \text{ und }\ H_N^{(1)}\succeq 0 \quad \forall N\ge 0, \qquad \mu_k = -\frac{k+1}{(2k+2)!}(\log\Xi)^{(2k+2)}(0).$$

---

## [NEU-219 – NEU-219z] — 22.–25. Juli 2026: O-219-Strang und No-Go-Theorem

**Der längste geschlossene Strang des Programms. Ergebnis: ein starkes negatives
Strukturresultat, das die Zyklizitätsobstruktion exakt lokalisiert.**

| Block | Ergebnis |
|---|---|
| NEU-219 – 219d | KMS-Typaudit: $\omega_\beta(\eta_{q,P})=0$ negativ; getwisteter Quotient; expliziter Neutralisierer; $\omega_{\beta,\chi}(\sigma_P(G_q))>0$ für $\beta>1$; Ladungseigenkochain $T_\sigma\Phi = g^{-\beta}\Phi$ |
| NEU-219e – 219g | Externe Eigenlinie; unitales Bimodul negativ; parazyklisches Koeffizientenobjekt offen; Hopf-Typbruch Komodul vs. Modul; SAYD-Stabilität vs. Ladung negativ — Dilatationspfad wird primär |
| NEU-219h – 219l | Automorphe Dilatation der $\rho_n$; Laca-Dilatation mit $\tau = \gamma_g\circ\sigma_\beta$; adelischer Lift des Koeffizientenmoduls; Multiplikator-, Paarungs- und Morita-Audit; exakter algebraischer Eckkern |
| NEU-219m – 219q | Orbit-Direktheit negativ; orbit-markierte Ersatzrealisierung und KMS-Modulgewicht; Multiplikator-Shift ausgeschlossen; dreiparametriger Auditrahmen $C(g,\beta,\lambda) = \lambda^\varepsilon g^{s\beta}$; Orbitindexfunktion $\kappa$ |
| NEU-219r – 219t | Kanonischer Basislift $\tilde L_0$: Erstdefinition, Kozykelerhalt, $\kappa = 0$, $\varepsilon = 0$; vollständige $U_{g^{-1}}$-Buchführung; **$s = -1$ global bewiesen** |
| **NEU-219u** | **No-Go-Theorem O-219:** $\tilde L_0 \in Z^4(A_{\mathrm{alg}}, I_0)$ typkorrekt, aber $t\Phi_0 = g^{-\beta}\Phi_0$ mit $g^{-\beta}\neq 1$ — keine gewöhnliche zyklische Klasse in $HC^4$ |
| NEU-219v – 219z | Nachaudits: typwidrige $U$-Eingaberotation ausgeschlossen; (R1)–(R3) als unzureichend erkannt (Fall D); $D_g$-Primärformel und Zieltypbrücke über NEU-211/216/217; Unit-Slot-Zeuge $\mu_P^*$; Finalaudit mit DAG-Export und Rollback-Vermerk |

Konsequenz: Der Pfad `[O-219-6]` — Weil-/Gammafaktorpaarung — wird zum neuen Hauptpfad
und eröffnet den Strang NEU-220.

---

## [NEU-216 – NEU-218] — 21.–22. Juli 2026: Koeffiziententyp und Cup-Aufstieg

| Eintrag | Ergebnis | Status |
|---|---|---|
| NEU-216 rev.1–6 | Logarithmischer Koeffiziententyp $\mathcal B^{\log}$ vollständig auditiert: kanonisches Schalenmittel $m_j$, radiale Seminorm, Faktorialband $C_\sigma(k)$, Supportschwelle $J(k)$, Band-Mittelwertlemma mit scharfen Konstanten, submultiplikative Norm **ohne Renormierung**, $T_a := \sigma_a$ kanonisch, $\mathcal A^{\log}$ konstruiert, $D_g(A_{\mathrm{alg}})\subseteq\mathcal A^{\log}$ | `✓ [M]` |
| NEU-217 rev.1–3 | Lokaler $p$-Block: Typisierung $N/S/H_p$, Gradkonflikt $\delta_p$ vs. $D_g$ fixiert, Faithfulness-Negativresultat, koordinatenfreie $\delta_p^{(0)}$ via Gaugewirkung | `✓ [K/M]` |
| NEU-217 `[O-217-2b/2c]` | gcd-Fallzerlegung, lokale Defekträume, Bimodulstabilität, lokale Nichtinnerheit via Normdivergenzbeweis (Gradpaarargument gestrichen) | `✓ [M]` |
| NEU-217 `[O-217-2c-6]` | Lokal-globaler Klebeknoten: Zwei-Punkt-Trennungszeuge für $\sigma_q$ und $\rho_q$, intrinsische Konstruktion, **globale Nichtinnerheit** — Grad-1-Pfad geschlossen | `✓ [K/M]` |
| NEU-218 | Grad-3-Partner und geladener Cup-Aufstieg; Eingabealternierung widerlegt; Korrekturaudit rollt die Baker-Gewichtstrennung zurück, schließt die Nica-Formel positiv; `[SO-Q_sigma]` via Følner-Wachstumsargument geschlossen — **Cup-Aufstieg $HH^4$ vollständig** | `✓ [M]` |

Zusätzlich: `KONVENTIONEN.md` angelegt und die $\rho_k$-Fourierform verbindlich fixiert.

---

## [NEU-195 – NEU-215] — 19.–21. Juli 2026: Derivationen, Potentiale, Bimodul-No-go

| Eintrag | Ergebnis | Status |
|---|---|---|
| NEU-195 | Bewertungsderivationen; Reduktion auf eine atomare $HH^1$-Frage; Routen A/B | `✓ [M]` / `✓ [M]_neg` |
| NEU-196 / 200 | Augmentationsblindheit: reguläre Potentiale sind im Kommutatorquotienten unsichtbar | `✓ [M]_neg` |
| NEU-197 / 199 | Universeller Dualdetektor, Kommutatorquotient $Q_{h,p}$; Generatorformel $D_g^H(\mu_k)$, Obstruktionspfeil-Quotiententest | `✓ [M]` |
| NEU-201 – 203 | Singuläres Potential $H_{\mathrm{sing}}$ als Testkandidat; **Revisionsaudit: alle drei Beweisschritte negativ** — $H_{\mathrm{sing}}$ nicht wohldefiniert, KMS-Test unzulässig; korrigiertes Singularitätskriterium über Projektionsdifferenzen | `✗ [M]` |
| NEU-204 / 205 | Dyadische Schalen: neutrale unbeschränkte äußere Derivation $A_{\mathrm{alg}}\to A_{C^*}$; geladener/algebraischer Zieltyp negativ; geladener dyadischer Twist, naive Linksverschiebung ausgeschlossen | `✓ [M]` / `✓ [M]_neg` |
| NEU-206 – 210 | Biorthogonale geladene Partialisometrieschalen; Bewertungsgitter und **Ketten-No-go**; separierbare Primpotentiale und Refinementstabilität; **Charakterkern-No-go**; faktoriale Ursprungssingularität und Charakterabsorption | `✓ [K/M]` / `✗ [M]` |
| NEU-211 – 213 | Nichtteilerfremder Faktorialaudit und geladene äußere Derivation; Zieltypbrücke über das intermediäre Koeffizientenmodul $\mathcal A^\infty$; Revisionsaudit korrigiert Rechen- und Leibniz-Typfehler | `✓ [M]` |
| NEU-214 rev.2 / 215 rev.4 | Bimodul-Rigiditätslemma und glattes Potential $X_N^\infty$; Zentralisatorbeweis, MASA via topologisch freier $\mathbb Q_+^\times$-Wirkung, $Z(A_{C^*}) = \mathbb C 1$ — **globaler Bimodul-No-go, verschärft zu $R=0$** | `✗ [M]` |

---

## [NEU-174 – NEU-194] — 18.–19. Juli 2026: Hochschild-Komplex und geladene HH⁴-Klasse

| Eintrag | Ergebnis |
|---|---|
| NEU-174 / 175 | Minimaler Hochschild-Komplex mit induzierter BC-Zeitwirkung; Gewichtraumkomplex und geladener Kettenprojektor; Korrekturen: Modellwahl $B_3^{\mathrm{mod}}$, reguläres Bimodul, $\alpha_t\circ\sigma = \sigma\circ\alpha_t$ |
| NEU-176 / 177 | Konstruktion einer nichttrivialen geladenen 4-Kohomologieklasse; direkter Kozykeltest und gewichteter Dualzyklus für $L_{3,\lambda}$; Statuskorrektur zu NEU-176 |
| NEU-178 | **Vier-Prim-Polynommodell:** explizite geladene $HH^4$-Klasse und Dualzyklus; schließt `[O-177-1..7]` im lokalen Modell, eröffnet den Transferknoten zu $A_{\mathbb Q}$ |
| NEU-179 – 181 | Transfertriage; $\mathbb Q_+^\times$-Gradierung und Primvaluationsderivationen; Homogenitätsaudit und algebraischer Modular-Twist $\sigma_\beta$; typisierte Cup-Route mit Leibnizregel |
| NEU-182 / 183 | **Nullkozykel-No-go:** $Z(A_{\mathbb Q})_g = 0$ für $g\neq 1_\Gamma$ (regulär) und $Z^0(A,{}_{\mathrm{id}}A_{\sigma_\beta}) = 0$ für $\Re\beta>0$ (verdreht); Zentrumstest, Strukturbruch, $\Omega_{\mathbf p}$-Auswertung |
| NEU-184 – 187 | Koeffizientenaudit für $Z(A_{\mathbb Q})_g$; Augmentationscharakter und Dualzyklus; geladener Sektor von $HH^4$; **Restriktionssatz** für geladene äußere Derivationen mit Gruppenalgebra-Reduktion, $H^1(G,B_\rho)\neq 0$ |
| NEU-188 | Erweiterungsobstruktion punktierter Gruppenkozykel; vollständiges Relationssystem (E3)/(E7); `[O-188-4]` **konditional** aufgelöst |
| AUDIT 2026-07-19 | Fortschrittsbilanz-Korrektur: Trennung von regulärer und verdrehter Nullkozykelroute, Äußerlichkeit nur konditional, Operatorbrücke als nächste Pflichtdisziplin |
| NEU-189 / 190 | Typaudit der Operatorrealisierung von $[\Omega_{\mathbf p}]$; vollständiger Audit NEU-1–188 nach typisierter Operatorbrücke — negativer Quellenbefund bestätigt |
| NEU-192 – 194 | Zeugenarchitektur, Separationssatz und Warnlemma für invariante Spuren; geladener Dualzyklus $z_{-\lambda}$ konstruiert, Randtest geschlossen; Paarung $\neq 0$; determinantisches Modell als Kozykel ausgeschlossen |

---

## [NEU-162 – NEU-173] — 15.–18. Juli 2026: Zeugenroute L₃° und Typfundament

**Ergebnis des Stranges: Die Zeugenroute über $L_3^\circ$ ließ sich nicht schließen. Die
Quellenkegel-Audits legten offen, dass die Fourierladung nie konstruktiv fixiert wurde —
ein negativer, aber präziser Befund, der den Übergang zur kohomologischen Route auslöste.**

| Eintrag | Ergebnis |
|---|---|
| NEU-162 – 164 | Quantoren- und Zulässigkeitstest für $L_3^\circ = e_1V_1$; Einmodenzeuge, Liftmitgliedschaft, Nichtnullkante; $R_{p,j}$-Test mit drei Ausgängen A/B/C und $U_p^{\mathrm{adm}}$ |
| NEU-165 / 165a / 165b | Import der $R_{p,j}$-Wirkung, Matrixstruktur, Basisnullmengen, gemeinsamer Kern; Quellenregister; **Konsistenzaudit: $R_{p,j}$ in NEU-157 nur postuliert (Klasse 4)** — führt zu NEU-157 rev.3 |
| NEU-166 / 166a / 166b | Ein- und Zweimoden-Test; Typ-, Domänen- und Deszentaudit von $\tilde T_p$; Rollen- und Provenienzentscheidung mit Stop-Regel $u = 1-p$, vier Endbefunden und Sperrmarken |
| NEU-167 / 167b | Lineare Kernbedingungen vs. offene Fourierladungsbedingung; `[O-167-2]` **negativ geschlossen** — $A_p = \emptyset$ im auditierten Quellenkegel |
| NEU-168 / 169 | Nichtverschwindensgeometrie der exakt zulässigen Liftmenge; Kollisionssystem und Einzelmoden-Nichtverschwindung von $B_p$ |
| NEU-170 / 170a – 170c | Gewichteter Träger von $L_3^\circ$; Klassen- und Repräsentantenaudit — **negativer Quellenbefund**; NEU-28 ist Spur-/Normierungsquelle, **kein Fourierimport** |
| NEU-170d | Vollständiger bereinigter DAG-Stand nach Direktaudit NEU-20/26/28/29/161/162/170a–c |
| NEU-171 – 173 | Typfundament der $L_3$-Klasse und ihres Fouriergrades; Direktaudit NEU-72/170b; Delta-Audit NEU-20/28 und Abschluss des Typfundament-Quellenkegels |

---

## Frühere Einträge (bis NEU-161 rev.5)

Das ursprüngliche Sitzungsprotokoll bis zum 15. Juli 2026 ist unverändert erhalten:
[CHANGELOG_alt.md](CHANGELOG_alt.md).
