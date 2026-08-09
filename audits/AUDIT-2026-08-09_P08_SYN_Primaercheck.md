# P08 SYN — Primärcheck Renormalized Prime Operators and Finite-Part Structures

**Datum:** 9. August 2026  
**SYN-Ziel:** `papers/P08_Renormalized_Prime_Operators_and_Finite_Part_Structures.md`  
**Geprüfter SYN-Stand:** Commit `29101001e79ab5418fd8dde0af30a1d27ca2e038`  
**Pass-A-Basis:** `audits/AUDIT-2026-08-09_P08_PassA_FINAL_SEAL.md`, Commit `964c602b`  
**Prüfart:** SYN-Direktaudit; kein erneuter Vollaudit der historischen NEU-121–150  

---

## 0. Prüfauftrag

Geprüft wurde ausschließlich, ob der P08-SYN-Draft den versiegelten Pass-A-Endstand ohne Hochstufung oder Typdrift destilliert. Kontrolliert wurden:

1. Jacobi-Typen und Selbstadjungiertheitsstatus;
2. Renormierungsbarrieren und ihre logische Reichweite;
3. P05-Scope der Rang-eins-Struktur;
4. Voraussetzungen der festen-$\beta$-$\mathcal S_1$-Aussage;
5. T2/Nichtentartung/Mangoldt-$R$;
6. Prime-only- versus Mangoldt-Mellin-Typisierung;
7. Finite-Part-Definition versus operatorielle Realisierung;
8. offene Root-Blocker und Routing nach P10/P11/P12.

Nicht durchgeführt wurde ein neuer mathematischer Gesamtaudit von 41 historischen Dateien.

---

## 1. H-T1 — Moment/KMS/Herglotz

Der Draft übernimmt korrekt:

$$
C_\xi
=1+\frac{\gamma_E}{2}-\frac12\log(4\pi)
\approx0.0230957,
$$

$$
\widehat\Omega=Z^{-1/2}\Omega_\tau,
\qquad
Z_{1,N}^{-1}\sim1/\log N.
$$

Die alten Formeln `C_xi≈-0.5493`, `Z^{+1/2}` und `R_N~log N` werden sichtbar als gesperrt/superseded geführt.

Die P07-Firewall

$$
m_{\rm arith}\text{ Herglotz}\iff RH
$$

wird nur als logische Grenzimplikation verwendet. P1/P2 und die konkrete Selbstadjungiertheit des historischen `A_N^{Jac,-}` bleiben offen.

**Ergebnis:** `OK`.

---

## 2. H-T2 — Jacobi-Renormierungsdiagnose

Der Draft trennt korrekt

$$
A_N^{\rm sym}=B_N^\Lambda
$$

von dem historischen antisymmetrischen P06/P07-Pfad. Er übernimmt streng

$$
b_{1,N}\asymp\gamma\sqrt{\log N/N}\to0
$$

und den Startvektor-Weylkanal

$$
\langle e_0,(A_N^{\rm sym}-z)^{-1}e_0\rangle\to-1/z.
$$

Nicht hochgestuft werden:

- globale Diagonalität aus `b1->0`;
- `b2/b1->infinity`;
- Existenz einer positiven nichtskalaren Prä-Lanczos-Metrik `W_N`.

Das abstrakte No-scalar-Lemma wird ausdrücklich nur conditional auf die Quotientendivergenz verwendet.

**Ergebnis:** `OK`.

---

## 3. H-T3 — Prä-Lanczos-/Grammetrik

Der Draft hält die P05-Firewall ein:

$$
\operatorname{rank}C_p^{\rm rel}\le1
$$

nur modellrelativ, und

$$
P_p=|c_p|^2\Pi_p^{(1)}
$$

wird nicht als orthogonaler Projektor bezeichnet.

Die NEU-128b-Typkorrektur wird richtig geschrieben:

$$
\Sigma_N(\beta)x
=\sum_p w_p\Psi_p\langle\Psi_p,x\rangle
$$

beziehungsweise als Quadratform.

Die beiden Paper-VII-Gegenbefunde bleiben `NO-GO`: falsche H3-Skalierung und unzulässiger Schluss von Phasencancellation auf absolute Schur-Zeilensummen. PSWF bleibt Methodenheuristik.

**Ergebnis:** `OK`.

---

## 4. H-T4 — Self-Energy, Spurklasse und Mangoldt-$R$

### 4.1 Algebraische Zerlegung

Der Draft übernimmt exakt nur die algebraische Identität

$$
\Sigma_{\rm rel}(\beta)
=\Sigma_{\rm rel}^{\infty}+\Sigma_{\rm rel}^{\rm ren}(\beta).
$$

Er behauptet weder Divergenz noch Nicht-Regularisierbarkeit des Rohanteils aus den vorhandenen Bounds.

Die PNT-Korrektur

$$
\sum_{p\le N}\frac{(\log p)^2}{p}
\sim\frac12(\log N)^2
$$

ist richtig migriert.

### 4.2 Feste-$\beta$-Spurklasse

Die Voraussetzungen sind korrekt verdrahtet:

1. modellrelativ `rank C_p^rel<=1`;
2. `|c_p|^2=O((log p)^2/p)`.

Daraus wird nur

$$
\Sigma_{\rm rel}^{\rm ren}(\beta)\in\mathcal S_1
$$

für festes reelles `beta>0` als `CONDITIONAL ✓[M]_{model}` abgeleitet.

Der Draft sagt ausdrücklich, dass T2 und `c_p!=0` **nicht** Voraussetzungen dieses Schritts sind.

### 4.3 T2 und Mangoldt-$R$

T2 sowie `c_p!=0` werden erst für die primdiagonale Definition

$$
R_p^{\rm Mang}=\frac{\log p}{|c_p|^2}
$$

verwendet. Beide bleiben offen/conditional. Die gewöhnliche Spuridentität mit `-zeta'/zeta` wird nur für `Re beta>1` und nur im primdiagonalen Modell behauptet.

**Ergebnis:** `OK`.

---

## 5. H-T5 — Mellin- und Finite-Part-Typisierung

### 5.1 Prime-only-No-Go

Der Draft übernimmt nicht die falsche NEU-148.A-Identität. Er zeigt korrekt den Typunterschied

$$
\sum_{p,k}\log p\,p^{-k\beta-s}
\neq
\sum_{p,k}\log p\,p^{-k\beta-ks}.
$$

### 5.2 Korrektes Mangoldt-Objekt

Als exaktes Mellin-Objekt wird ausschließlich

$$
\Psi_{\varphi,X}(\beta)
=\sum_n\Lambda(n)\varphi(n/X)n^{-\beta}
$$

verwendet, mit

$$
\Psi_{\varphi,X}(\beta)
=\frac1{2\pi i}\int_{(c)}\widehat\varphi(s)X^s
\left(-\frac{\zeta'}{\zeta}(\beta+s)\right)ds.
$$

Die Mellin-Polkorrektur

$$
\operatorname{Res}_{s=0}\widehat\varphi(s)=1
$$

ist sichtbar; `hat phi` wird nicht als ganz bezeichnet.

### 5.3 $\Psi/S$-Transfer

Die korrekte algebraische Differenz

$$
\Psi_{\varphi,X}-S_{\varphi,X}
=\sum_{k\ge2}\sum_p\log p
[\varphi(p^k/X)-\varphi(p/X)]p^{-k\beta}
$$

ist übernommen. Trotz der naheliegenden absoluten Summierbarkeit für `Re beta>1/2` wird im SYN keine neue quantitative/uniforme Hochstufung vorgenommen; der für die Finite-Part-Anwendung benötigte Transfer bleibt gemäß Seal `?[O]`.

### 5.4 Kontur und operatorielle Brücke

Das fixed-contour Restlemma wird nur `CONDITIONAL` geführt. Uniforme Kontur/Residuenzählung bleibt `?[O]`.

`N_P` wird nur conditional eingeführt und die Domäne trägt den fehlenden Normfaktor

$$
\sum_pp^2|\xi_p|^2\|\Psi_p\|^2<\infty.
$$

Primlabel-Finite-Part, operatorielle Realisierung von `Tr_reg` und der $R$-Cutoff-Transfer bleiben offen.

**Ergebnis:** `OK`.

---

## 6. Finite-Part-Tautologie

Der Draft hält die wichtigste logische Firewall ein:

$$
\operatorname{Tr}_{\rm reg}:=\operatorname{AC}[-\zeta'/\zeta]
$$

bleibt `DEFINITION / ✓[def]` und wird nicht als Beweis eines operatoriellen Grenzwerts verwendet.

**Ergebnis:** `OK`.

---

## 7. Provenienz und Routing

Die Knotenprovenienz führt alle 41 Live-Dokumente des Inventars einschließlich der beiden NEU-123F-Dateien. Gemischte historische Knoten werden als `INCORPORATED bereinigt` beziehungsweise `NO-GO + Ersatzroute` typisiert; offene Zielknoten bleiben `OPEN`.

Routing ist korrekt:

- gesicherte Negativbefunde → P10;
- intrinsische Lift-/Gram-/T2-/Nichtentartungsfragen und globale Schatten/Fredholm-Geometrie → P11;
- Finite-to-Infinite-Weil-Grenzfragen → P12.

Keine Objekt-X- oder Hilbert–Pólya-Konstruktion wird behauptet.

**Ergebnis:** `OK`.

---

## 8. Primärurteil

Es wurde **kein Status-, Typ-, Formel- oder Routingkonflikt** zwischen dem P08-SYN-Draft und dem versiegelten Pass-A-Endstand gefunden.

$$
\boxed{
\text{P08 SYN-PRIMÄRCHECK: OHNE KONKRETEN GEGENBEFUND.}
}
$$

Der Markdown-Draft kann zum pfadgebundenen SYN-Zweitcheck weitergegeben werden. Ein `SYN FINAL AUDITED`-Status wird erst nach diesem Zweitcheck gebucht.
