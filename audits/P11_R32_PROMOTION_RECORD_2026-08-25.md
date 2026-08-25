# P11/R32 — Sammel-Promotion 2026-08-25

**Status:** kanonischer Promotionsrecord.  
**Freigabe:** explizite Projektfreigabe durch den Projektverantwortlichen am 2026-08-25: „promote die GREENen Resultate gesammelt“.  
**P11:** bleibt FROZEN. **P12:** unverändert. **R14:** unverändert.  
**Scope:** Nur die unten einzeln aufgeführten, zuvor unabhängig GREEN bestätigten Resultate werden formal gebucht. Keine weiteren Kandidaten werden implizit mitpromotet.

---

## 1. Promotete Resultate

### CTX-1 — horizon-adaptive zentrale Transversalität

\[
\boxed{\mathrm{CTX\!-\!1}:\checkmark[M]_{\rm part}}
\]

Für
\[
R\ge\max\{\varepsilon,d/2\},\qquad R<S<a,
\]
gilt
\[
\ker\mathcal K_{I,A}\cap
(\mathcal C_R^+\oplus\mathscr H_{\mathcal A}^-)=\{0\}.
\]
Äquivalent:
\[
\operatorname{Ran}(HE_{\mathcal A}|_-)
\cap(I+A)\mathcal C_R^+=\{0\}.
\]
Mechanismus: endliche `4x4`-/`6x6`-Orbitdeterminanten plus positiver Koeffizientenspalt.

Kanonischer Audit:
`audits/P11_R32_CENTRAL_TRANSVERSALITY_EXTENDED_AUDIT.md`.

---

### NS-1a — erste nichtzentrale Unsichtbarkeitsschale

\[
\boxed{\mathrm{NS\!-\!1a}:\checkmark[M]}
\]

Für
\[
d/2\le R<d
\]
ist die symmetrische erste nichtzentrale Schale \(\mathcal S_R^+\) ein unendlichdimensionaler Unterraum von
\[
\mathcal N_I=\ker(E_I^*H|_+).
\]

### NS-1 — Transversalität der ersten nichtzentralen Schale

\[
\boxed{\mathrm{NS\!-\!1}:\checkmark[M]_{\rm part}}
\]

Für
\[
d/2\le R<d,\qquad R<S<a,
\]
gilt
\[
\ker\mathcal K_{I,A}\cap
(\mathcal S_R^+\oplus\mathscr H_{\mathcal A}^-)=\{0\}.
\]
Äquivalent:
\[
\operatorname{Ran}(HE_{\mathcal A}|_-)
\cap(I+A)\mathcal S_R^+=\{0\}.
\]
Mechanismus: echter Full-Rest-Cross-Term `K1* M20 K2`, zentraler Echo und endliche \(\delta=d-e\)-Streifen-Elimination. Die vollständige 11-Wort-Bilanz wurde adversarial nachgezogen; global sind auf dieser Schale 4 von 11 Wörtern aktiv, an den beweiskritischen Punkten jeweils nur die explizit bilanzierten lokalen Beiträge.

Kanonische Audits:
- `audits/P11_R32_FIRST_NONCENTRAL_SHELL_TRANSVERSALITY_AUDIT.md`
- `audits/P11_R32_FIRST_NONCENTRAL_SHELL_11WORD_AUDIT.md` bzw. der zugehörige 11-Wort-Zusatzstand im Repo.

---

### SS-1a — zweite nichtzentrale Rand-Schale

\[
\boxed{\mathrm{SS\!-\!1a}:\checkmark[M]}
\]

Für
\[
d/2\le R<e
\]
mit \(\ell=e-R\) ist der durch
\[
y(b+u)=f(u),\qquad y(T-u)=\frac rq f(u),\qquad0<u<\ell,
\]
und Geradheit erzeugte Rand-Schalenraum \(\mathcal S_{R,2}^+\) unendlichdimensional und liegt in \(\mathcal N_I\).

### SS-L — exakte 10-von-11-Wortklassifikation

\[
\boxed{\mathrm{SS\!-\!L}:\checkmark[M]}
\]

Auf \(\mathcal S_{R,2}^+\) sind im Drei-Shift-Fenster exakt 10 von 11 Full-Rest-Wörtern als ambient Operatorwörter nicht identisch null. Nur
\[
W_{32}=K_3^*M_{20}K_2
\]
stirbt durch die Horizontgeometrie.

Kanonischer Audit:
`audits/P11_R32_SECOND_NONCENTRAL_SHELL_LEDGER_AUDIT.md`.

---

### SP-1 — skalare Profilkompression der zweiten Schale

\[
\boxed{\mathrm{SP\!-\!1}:\checkmark[M]_{\rm part}}
\]

Für die normierte Profilisometrie
\[
V_R=\frac{U_R}{\sqrt{2(1+\rho^2)}},\qquad \rho=r/q,
\]
gilt exakt
\[
\boxed{V_R^*AV_R=M_{\mu_R}},
\]
mit
\[
\mu_R(u)
=p^2+q^2+2r^2
+\frac{q^2(2+2^{-3/2})}{1+\rho^2}
\left(\rho^2 1_{\{u<\varepsilon\}}+1_{\{u>e-\varepsilon\}}\right)>0.
\]
Außerdem gilt die im Audit angegebene notwendige komprimierte Blockgleichung mit höchstens drei Annuluswerten.

**Firewall:** Dies ist eine Kompression. Es wird nicht behauptet,
\[
A\mathcal S_{R,2}^+\subset\mathcal S_{R,2}^+.
\]

Kanonischer Audit:
`audits/P11_R32_SECOND_SHELL_PROFILE_COMPRESSION_AUDIT.md`.

---

### ST-1 — Transversalität der zweiten nichtzentralen Schale

\[
\boxed{\mathrm{ST\!-\!1}:\checkmark[M]_{\rm part}}
\]

Für
\[
d/2\le R<e,\qquad R<S<a,
\]
gilt
\[
\boxed{
\ker\mathcal K_{I,A}\cap
(\mathcal S_{R,2}^+\oplus\mathscr H_{\mathcal A}^-)=\{0\}.
}
\]
Äquivalent auf dem hier globalen P12-Hub-Injektivitätsstratum:
\[
\operatorname{Ran}(HE_{\mathcal A}|_-)
\cap(I+A)\mathcal S_{R,2}^+=\{0\}.
\]
Mechanismus: zwei ambient Beobachtungspunkte
\[
x_1=e-u,\qquad x_2=a-u,
\]
sehen denselben Annuluswert \(w(d+u)\). Die lokalen 11-Wort-Ledger sind exakt
\[
x_1:\ W_{11},W_{13},
\qquad
x_2:\ W_{12},W_{23},
\]
und die beiden Restkoeffizienten besitzen entgegengesetztes Vorzeichen. Die lokale `2x2`-Determinante ist strikt positiv. Danach folgt aus \(y=0\) und der bereits global bewiesenen P12-Hub-Injektivität im Stratum \(S<T\), dass \(w=0\).

Kanonische Audits:
- `audits/P11_R32_SECOND_SHELL_TRANSVERSALITY_AUDIT.md`
- `audits/P11_R32_SECOND_SHELL_TRANSVERSALITY_LOCAL_LEDGER_AUDIT.md`.

---

## 2. Nicht mitpromotet

Die folgenden neueren Klassifikationskandidaten bleiben ausdrücklich offen:

\[
\boxed{\mathrm{FG\!-\!0}:?[O]}
\]
— automatisch blinder physischer Supportraum,

\[
\boxed{\mathrm{HT\!-\!1}:?[O]}
\]
— Horizontschwanz für \(R<\varepsilon\),

\[
\boxed{\mathrm{FG\!-\!1}:?[O]}
\]
— exhaustive Branch-/Gluing-Normalform von \(\mathcal N_I\),

\[
\boxed{\mathrm{FG\!-\!NG1}:?[O]}
\]
— arithmetische Firewall gegen den Fehlschluss „endlich viele Hub-Shifts implizieren endlich-periodische Overlap-Orbits“.

Kanonischer Kandidatenaudit:
`audits/P11_R32_INVISIBLE_FIBER_GRAPH_CLASSIFICATION_AUDIT.md`.

---

## 3. Harte Scope-Firewall der Sammel-Promotion

Die Promotion beweist **nicht**:

- \(\ker\mathcal K_{I,A}=0\) auf dem gesamten \(\mathcal N_I\);
- volle Injektivität des Schur-Crossblocks;
- Closed Range / bounded below / uniformen Winkel;
- vollständige Klassifikation von \(\mathcal N_I\);
- Polar Gauge oder Strong Terminal Transport;
- ein finales globales \(K_X\);
- Objekt X;
- RH.

Die promovierten Resultate sind sektorielle, aber echte mathematische Ausschlusssätze innerhalb der P11/R32-Schur-Geometrie.

---

## 4. Kanonischer Status nach Promotion

\[
\boxed{\mathrm{CTX\!-\!1}:\checkmark[M]_{\rm part}}
\]
\[
\boxed{\mathrm{NS\!-\!1a}:\checkmark[M]}
\]
\[
\boxed{\mathrm{NS\!-\!1}:\checkmark[M]_{\rm part}}
\]
\[
\boxed{\mathrm{SS\!-\!1a}:\checkmark[M]}
\]
\[
\boxed{\mathrm{SS\!-\!L}:\checkmark[M]}
\]
\[
\boxed{\mathrm{SP\!-\!1}:\checkmark[M]_{\rm part}}
\]
\[
\boxed{\mathrm{ST\!-\!1}:\checkmark[M]_{\rm part}}
\]

Dieser Record supersediert für diese Resultate ältere Auditkopfzeilen mit `Kandidat; keine Promotion` oder `?[O]`. Die mathematischen Inhalte und Firewalls der zugrundeliegenden Audits bleiben unverändert.
