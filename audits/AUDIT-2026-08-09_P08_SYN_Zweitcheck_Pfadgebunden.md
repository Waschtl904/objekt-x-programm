# P08 SYN — Zweitcheck pfadgebunden

**Datum:** 9. August 2026  
**SYN-Ziel:** `papers/P08_Renormalized_Prime_Operators_and_Finite_Part_Structures.md`  
**Draft-Commit:** `29101001e79ab5418fd8dde0af30a1d27ca2e038`  
**Primärcheck:** `audits/AUDIT-2026-08-09_P08_SYN_Primaercheck.md`, Commit `f3330c2f`  
**Bindende Basis:** `audits/AUDIT-2026-08-09_P08_PassA_FINAL_SEAL.md`, Commit `964c602b`  
**Prüfart:** unabhängiger pfadgebundener Status-/Scope-Gegencheck; kein NEU-Vollaudit  

---

## 0. Leitfragen

Der Zweitcheck prüft fünf Hochrisikofragen:

1. Wird aus einer Renormierungsdiagnose versehentlich eine Konstruktion?
2. Werden Voraussetzungen der Spurklasse mit Voraussetzungen des Mangoldt-$R$ vermischt?
3. Wird ein modellrelativer Rang-eins-Befund globalisiert?
4. Wird der analytische Mellin-Kanal auf das falsche Prime-only-Objekt übertragen?
5. Wird `Tr_reg:=AC[-zeta'/zeta]` als operatorieller Satz gelesen?

---

## 1. Renormierungsdiagnose bleibt Diagnose

Der SYN-Draft schreibt streng

$$
b_{1,N}\to0
$$

und führt das Wachstum von $b_{2,N}/b_{1,N}$ nur als finite Evidenz mit offenem asymptotischem Grenzwert. Das abstrakte No-scalar-Lemma wird nur unter

$$
b_{2,N}/b_{1,N}\to\infty
$$

angewandt.

Die Existenz eines positiven nichtskalaren Prä-Lanczos-Operators $W_N$ wird ausdrücklich **nicht** daraus gefolgert.

**Pfadurteil:** kein Hochstufungsfehler.

---

## 2. Spurklasse und Mangoldt-$R$ bleiben logisch getrennt

Der Draft setzt für

$$
\Sigma_{\rm rel}^{\rm ren}(\beta)\in\mathcal S_1
$$

nur

- modellrelativ `rank C_p^rel<=1`,
- die quantitative Schranke `|c_p|^2=O((log p)^2/p)`

voraus.

T2 und `c_p!=0` werden erst beim primdiagonalen Operator

$$
R_p^{\rm Mang}=\log p/|c_p|^2
$$

verwendet. Damit ist die im eingereichten Pass-A-Gegencheck gefundene falsche Voraussetzungenverdrahtung im SYN nicht wieder aufgetaucht.

**Pfadurteil:** korrekt.

---

## 3. P05-Scope bleibt erhalten

Der Draft bezeichnet

$$
P_p=|c_p|^2\Pi_p^{(1)}
$$

nicht als orthogonalen Projektor und globalisiert `rank C_p^rel<=1` nicht. Liftunabhängigkeit, Nichtentartung und intrinsische Kanalnorm bleiben offen.

T2 wird nur conditional aus einer orthogonalen Edge-Label-Zerlegung abgeleitet; die intrinsische Herkunft dieser Zerlegung wird nicht behauptet.

**Pfadurteil:** kein Scope-Leak.

---

## 4. Mellin-Objekt ist korrekt typisiert

Der Draft trennt sichtbar

$$
S_{\varphi,X}(\beta)
=\sum_p\varphi(p/X)\frac{\log p\,p^{-\beta}}{1-p^{-\beta}}
$$

von

$$
\Psi_{\varphi,X}(\beta)
=\sum_n\Lambda(n)\varphi(n/X)n^{-\beta}.
$$

Nur für $\Psi$ wird die Identität

$$
\frac1{2\pi i}\int\widehat\varphi(s)X^s
\left(-\frac{\zeta'}{\zeta}(\beta+s)\right)ds
$$

als exakt geführt. Der Prime-only-Typfehler aus NEU-148 ist als No-Go erhalten.

Die korrigierte algebraische Differenz

$$
\Psi-S
=\sum_{k\ge2}\sum_p\log p
[\varphi(p^k/X)-\varphi(p/X)]p^{-k\beta}
$$

ist richtig eingebaut; eine neue quantitative Finite-Part-Hochstufung wird nicht vorgenommen.

**Pfadurteil:** korrekt.

---

## 5. Mellin-Pol, Kontur und Residuen

Der Draft führt bei `varphi=1` nahe 0

$$
\operatorname{Res}_{s=0}\widehat\varphi(s)=1
$$

und nicht `hat varphi(0)=1`. Das fixed-contour Restlemma bleibt `CONDITIONAL`; eine uniforme Kontur für variierendes kompaktes $K$ und die vollständige Residuenzählung bleiben `?[O]`.

Damit wird NEU-149 nicht stärker gelesen als im finalen Seal.

**Pfadurteil:** korrekt.

---

## 6. Finite-Part-Tautologie bleibt gesperrt

Der Draft unterscheidet explizit:

$$
\operatorname{Tr}_{\rm reg}:=\operatorname{AC}[-\zeta'/\zeta]
\qquad\text{(`✓[def]`)}
$$

von

$$
\operatorname{FP}\operatorname{Tr}(\cdots)
\stackrel?=-\zeta'/\zeta,
$$

was operatoriell offen bleibt.

Auch `[ZA] R_p\asymp p/log p` wird nicht als ausreichend für die Gleichheit von Finite Parts behandelt.

**Pfadurteil:** korrekt.

---

## 7. No-Go-Scope

Die negativen Aussagen des Drafts sind lokal begrenzt:

- `b1->0` sperrt den unrenormierten nichtdegenerierten Startvektorpfad, nicht jeden Grenzoperator;
- Paper-VII-Cancellation sperrt den konkreten absoluten Schur-Schluss, nicht jede operatorische Cancellation-Methode;
- NEU-148 sperrt den Mellin-Ansatz für den Cutoff `varphi(p/X)`, nicht die Mangoldt-Mellin-Methode;
- fehlendes T2 sperrt eine reine primweise Eigenwert-/Eulerproduktlesart, nicht globale nichtorthogonale Gramgeometrie.

**Pfadurteil:** keine Überdehnung der No-Gos.

---

## 8. Root-Blocker-Vollständigkeit

Der Draft hält sichtbar offen:

- KMS/GNS→Jacobi und Formkompatibilität;
- `b2/b1->infinity` streng;
- $W_N$;
- intrinsische Lift-/Kanalnormgeometrie;
- T2;
- `c_p!=0`;
- Mangoldt-$R$;
- uniforme Mellin-Kontur/Residuen;
- quantitativen/uniformen $\Psi/S$-Transfer;
- Primlabel-Finite-Part;
- operatorielle Realisierung von `Tr_reg`;
- $R$-Cutoff-Transfer;
- Grenzoperator-/Spektralmaßidentifikation NEU-124.

Kein Root-Blocker des FINAL-SEAL ist verschwunden.

---

## 9. Zweiturteil

Es wurde kein konkreter Status-, Scope-, Typ- oder Routinggegenbefund gefunden.

$$
\boxed{
\text{P08 SYN-ZWEITCHECK: OHNE KONKRETEN GEGENBEFUND.}
}
$$

Der Markdown-Inhalt ist damit `SYN FINAL AUDITED`-fähig. Nächster Schritt: Statusbuchung im Markdown und reine LaTeX-SYN-Übertragung mit Transferaudit.
