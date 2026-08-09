# P08 — Renormalized Prime Operators and Finite-Part Structures

**Status:** SYN DRAFT — Pass-A migriert; SYN-Direktaudit ausständig  
**Datum:** 9. August 2026  
**Pass-A-Basis:** `audits/AUDIT-2026-08-09_P08_PassA_FINAL_SEAL.md`  
**Scope:** Live-Block `04-grenzoperator-renormierung/`, NEU-121–150 gemäß P08-Inventar  

> Dieses SYN-Paper enthält ausschließlich den am 9. August 2026 versiegelten P08-Endstand. Historische Hochstufungen, die im Pass-A-Audit gesperrt wurden, werden nicht als positive Resultate übernommen. `?[O]`, `CONDITIONAL`, `×[M]` und modellrelative Aussagen bleiben sichtbar.

---

## Abstract

P08 konsolidiert zwei logisch getrennte Stränge des Grenzoperator- und Renormierungsprogramms. Der erste Strang ist eine **Renormierungsdiagnose** für endliche Jacobi-Modelle: die erste Lanczos-Kante kollabiert streng, der Startvektor-Weylkanal degeneriert unrenormiert, und eine mögliche Divergenz des Quotienten $b_{2,N}/b_{1,N}$ würde eine skalare Renormierung ausschließen. Daraus folgt jedoch keine Konstruktion einer nichtskalaren Prä-Lanczos-Metrik.

Der zweite Strang untersucht **renormalisierte Primoperatoren, Mangoldt-Spuren und Finite-Part-Strukturen**. Eine feste-$\beta$-Spurklasse ist im relativen Rang-eins-Modell unter einer quantitativen Kanalnormschranke konditional verfügbar; Primorthogonalität und Nichtentartung werden erst für eine primdiagonale Mangoldt-Observable benötigt. Analytisch ist der exakte Mellin-Kanal nicht die Prime-only-Summe mit Cutoff $\varphi(p/X)$, sondern die geglättete Mangoldt-Summe

$$
\Psi_{\varphi,X}(\beta)=\sum_{n\ge1}\Lambda(n)\varphi(n/X)n^{-\beta}.
$$

Für sie gilt die korrekte Mellin-Darstellung über $-\zeta'/\zeta(\beta+s)$. Die operatorielle Identifikation eines Finite-Part-Grenzwerts mit der analytischen Fortsetzung von $-\zeta'/\zeta$ bleibt offen. P08 konstruiert weder Objekt X noch einen Hilbert–Pólya-Endoperator und enthält keinen RH-Beweis.

---

## §1 — Bindende Typ- und Statusfirewalls

### 1.1 P05-Firewall: relative Primkanäle

Für P08 gilt bindend:

$$
\operatorname{rank} C_p^{\rm rel}\le 1
$$

nur in der induzierten relativen Modellrealisierung. Der gewichtete Rang-eins-Operator wird als

$$
P_p=|c_p|^2\Pi_p^{(1)}
$$

geschrieben; $P_p$ ist im Allgemeinen **kein orthogonaler Projektor**. Nichtentartung

$$
c_p\neq0
$$

für alle Primkanäle, Liftunabhängigkeit von $|c_p|^2$ und eine intrinsische termweise Asymptotik bleiben offen.  
[P05; H-T3/H-T4]

### 1.2 P06/P07-Firewall: zwei Jacobi-Typen

Die endliche direkt symmetrische Schließung

$$
A_N^{\rm sym}=B_N^\Lambda=J_N^\Lambda+(J_N^\Lambda)^*
$$

ist selbstadjungiert. Davon zu unterscheiden ist der historische antisymmetrische Pfad mit

$$
J_N^-:=\frac12(\Theta_N-\Theta_N^\dagger),
\qquad
S_N:=\frac1{2i}(\Theta_N-\Theta_N^\dagger)=-iJ_N^-.
$$

$J_N^-$ ist schiefadjungiert, $S_N$ selbstadjungiert. Die Selbstadjungiertheit eines historischen konkreten $A_N^{\rm Jac,-}$ bleibt `?[O]`; Herglotz-/Spektralmaßaussagen über diesen Kandidaten sind deshalb konditional.  
[P06/P07; H-T1/H-T2]

### 1.3 Finite-Part-Firewall

Die Definition

$$
\operatorname{Tr}_{\rm reg}(R\Sigma)(\beta)
:=\operatorname{AC}\!\left[-\frac{\zeta'}{\zeta}\right](\beta)
$$

ist zulässig und hat Status `✓[def]`. Sie ist **keine** operatorielle Herleitung eines Cutoff-Grenzwerts. Die Gleichheit eines konkret konstruierten Finite Parts mit dieser analytischen Fortsetzung bleibt ein Beweisziel.  
[NEU-145; H-T4/H-T5]

---

## §2 — Moment-/KMS-Eingang und Herglotz-Grenze

### Satz 2.1 — Korrigierte $\xi$-Konstante

Für die in NEU-121 verwendete Größe gilt bindend

$$
\boxed{
C_\xi=-\frac{\xi'(0)}{\xi(0)}
=1+\frac{\gamma_E}{2}-\frac12\log(4\pi)
\approx0.0230957.
}
$$

Der historische Zahlenwert $-0.5493$ ist `×[M]` und `SUPERSEDED`.  
[NEU-121Cfix: `✓[M]`]

### Satz 2.2 — KMS/GNS-Normalisierung

Für

$$
\tau_{\beta,N}(T)=\sum_{n\le N}n^{-\beta}\langle e_n,Te_n\rangle,
\qquad
Z_{\beta,N}=\tau_{\beta,N}(1),
$$

und $\varphi_{\beta,N}=Z_{\beta,N}^{-1}\tau_{\beta,N}$ besitzt der GNS-Vektor des normalisierten Zustands die Form

$$
\boxed{\widehat\Omega=Z^{-1/2}\Omega_\tau.}
$$

Für $\beta=1$ gilt

$$
Z_{1,N}^{-1}\sim\frac1{\log N}.
$$

Die historischen Formeln $\widehat\Omega=Z^{+1/2}\Omega_\tau$ und $R_N\sim\log N$ sind `×[M]`.  
[NEU-121/122; H-T1]

### Satz 2.3 — Herglotz-Firewall

P07 fixiert

$$
\boxed{m_{\rm arith}\text{ ist Herglotz}\iff\mathrm{RH}.}
$$

Daher gilt als reine logische Implikation:

$$
\widetilde m_N^{\rm ren}
\xrightarrow{\rm loc.unif.}
m_{\rm arith}
\quad\Longrightarrow\quad
m_{\rm arith}\text{ Herglotz}
\quad\Longrightarrow\quad
\mathrm{RH},
$$

sofern die Approximanten echte Herglotzfunktionen sind. Die Existenz und kanonische Wahl einer solchen Folge ist `?[O]`.

### Offen 2.4 — KMS/GNS–Jacobi-Brücke

Offen bleiben insbesondere:

1. eine vorab fixierte selbstadjungierte GNS-Observable, deren Lanczos-Darstellung den gewünschten Jacobioperator erzeugt (`P1 ?[O]`);
2. die Formkompatibilität mit der Bombieri-/Weil-Geometrie (`P2 ?[O]`);
3. eine konkrete selbstadjungierte Realisierung des historischen $A_N^{\rm Jac,-}$;
4. die kanonische Nevanlinna-Normalisierung und Tail-Kontrolle.

---

## §3 — Renormierungsdiagnose des symmetrischen Jacobi-Pfads

### Satz 3.1 — Kollaps der ersten Lanczos-Kante

Für den direkt symmetrisierten endlichen Kandidaten und den Startvektor $q_0=e_1$ gilt

$$
a_{0,N}=0,
$$

und

$$
\boxed{
b_{1,N}
=\frac{\gamma}{N}
\sqrt{\sum_{n=2}^{N-1}\Lambda(n)^2}
\asymp
\gamma\sqrt{\frac{\log N}{N}}
\longrightarrow0.
}
$$

Damit scheitert die unrenormierte nichtdegenerierte Eintrittsbedingung $b_{1,N}\to b_1>0$.  
[NEU-123A; H-T2: `✓[M]_{neg}`]

### Korollar 3.2 — Startvektor-Weylkanal

Aus

$$
A_N^{\rm sym}e_0=b_{1,N}e_1
$$

folgt für $z\in\mathbb C\setminus\mathbb R$

$$
\boxed{
\langle e_0,(A_N^{\rm sym}-z)^{-1}e_0\rangle
\longrightarrow -\frac1z.
}
$$

Der unrenormierte Startvektor-Kanal kann daher nicht $m_{\rm arith}$ liefern.  
[H-T2: `✓[M]_{neg}`]

### Firewall 3.3 — Keine globale Diagonalität

Aus $b_{1,N}\to0$ folgt **nicht**, dass alle höheren Offdiagonalparameter verschwinden oder ein Grenzoperator insgesamt diagonal wird. Die historische globale Diagonalitätsbehauptung ist `×[M]`.

### Satz 3.4 — Skalare Lanczos-Kovarianz

Für $c_N>0$ gilt

$$
A_N\mapsto c_NA_N
\quad\Longrightarrow\quad
a_{j,N}\mapsto c_Na_{j,N},
\qquad
b_{j,N}\mapsto c_Nb_{j,N}.
$$

Insbesondere ist

$$
\frac{b_{2,N}}{b_{1,N}}
$$

unter positiver skalarer Prä-Lanczos-Skalierung invariant.  
[NEU-125: `✓[M]`]

### Satz 3.5 — Abstraktes No-scalar-Lemma

Falls

$$
\frac{b_{2,N}}{b_{1,N}}\longrightarrow\infty,
$$

kann keine positive skalare Folge $\kappa_N$ beide Größen $b_{1,N}/\kappa_N$ und $b_{2,N}/\kappa_N$ gegen endliche positive Grenzwerte schicken.  
[NEU-123H: `✓[M]` als bedingtes abstraktes Lemma]

### Offen 3.6 — Zweite Kante und nichtskalare Geometrie

Die endlichen Daten zeigen starkes Wachstum von $b_{2,N}/b_{1,N}$, beweisen aber weder

$$
\frac{b_{2,N}}{b_{1,N}}\to\infty
$$

noch eine spezifische Asymptotik. Der strenge Grenzwert bleibt `?[O]`.

Eine positive nichtskalare Prä-Lanczos-Geometrie $W_N$ bleibt ebenfalls `?[O]`. Die Doppelbarriere **diagnostiziert einen möglichen Bedarf**, konstruiert $W_N$ aber nicht.

---

## §4 — Prä-Lanczos-/Grammetrik: zulässiger Scope und No-Gos

### Satz 4.1 — Ebenentrennung

Eine Jacobi-seitige Self-Energy ist noch keine intrinsische Prä-Lanczos-Metrik. Ein echter Kandidat $W_N$ müsste vor dem Lanczos-Schritt auf der Quell-/Feshbach-Ebene konstruiert und seine Positivität, Nichtskalarität, Intrinsizität und Grenzverträglichkeit separat bewiesen werden.  
[NEU-127/128b: `✓[M]` als Typdiagnose]

### Firewall 4.2 — Rang-eins-Form nur modellrelativ

Im historischen Rang-eins-Modell kann formal

$$
\Sigma_N(\beta)x
=\sum_p w_p(\beta)\Psi_p\langle\Psi_p,x\rangle
$$

beziehungsweise

$$
\langle x,\Sigma_N(\beta)x\rangle
=\sum_p w_p(\beta)|\langle\Psi_p,x\rangle|^2
$$

geschrieben werden. Die historische Formel, die einen Vektor mit der skalaren Summe $\sum_p w_p|\langle\Psi_p,x\rangle|^2$ identifiziert, ist `×[M]`.  
[NEU-128b]

### No-Go 4.3 — Paper-VII-Skalierung

Aus einer Schranke

$$
P_{kl}\le C_2c^{1/2}
$$

und der Definition $A_{kl}=P_{kl}c^{1/2}$ folgt

$$
A_{kl}=O(c),
$$

nicht $O(1)$. Die historische H3-Verifikation mit dieser Skalierung ist `×[M]`.

### No-Go 4.4 — Phasencancellation kontrolliert keine absolute Schur-Summe

Aus signierter dyadischer Cancellation folgt nicht

$$
\sup_i\sum_{j\ne i}|T_{ij}|=O(1).
$$

Das Modell

$$
T_{ij}=\frac{e^{i\alpha(i-j)}}{|i-j|}
$$

zeigt trotz Cancellation

$$
\sum_{j\ne i}|T_{ij}|\asymp\log N.
$$

Damit bleibt eine korrekte Nelson-/Schur-Brücke über Operatornormen, Quadratsummen, $TT^*$, Cotlar-Strukturen oder echte Orthogonalität offen.  
[NEU-131/Paper VII: `×[M]`]

### Bemerkung 4.5 — PSWF-Route

Die PSWF-/Edge-Koerzivitätsidee bleibt eine **Methodenheuristik**. Sie liefert keine bewiesene Operatoridentifikation $D_{\rm rel}=\overline{iJ^-}$ und keine konstruierte Prä-Lanczos-Metrik.  
[NEU-130]

---

## §5 — Renormalisierte Selbstenergie und feste-$\beta$-Spurklasse

### Definition 5.1 — Algebraische $\beta$-Zerlegung

Aus

$$
\frac1{1-p^{-\beta}}
=1+\frac{p^{-\beta}}{1-p^{-\beta}}
$$

folgt formal die Zerlegung

$$
\boxed{
\Sigma_{\rm rel}(\beta)
=\Sigma_{\rm rel}^{\infty}
+\Sigma_{\rm rel}^{\rm ren}(\beta),
}
$$

mit dem renormalisierten Anteil

$$
\Sigma_{\rm rel}^{\rm ren}(\beta)
:=\sum_p\frac{p^{-\beta}}{1-p^{-\beta}}P_p.
$$

[NEU-136: `✓[M]` algebraisch]

### Firewall 5.2 — Rohanteil

Aus den vorhandenen Upper Bounds folgt weder die Divergenz noch die Nicht-Regularisierbarkeit von $\Sigma_{\rm rel}^{\infty}$. Insbesondere beweist eine Obergrenze für $|c_p|^2$ keine Untergrenze für die tatsächliche Rohsumme.

Die korrekte PNT-Vergleichsasymptotik lautet

$$
\sum_{p\le N}\frac{(\log p)^2}{p}
\sim\frac12(\log N)^2,
$$

nicht $\frac13(\log N)^3$.  
[NEU-136: historische log-kubische Formel `×[M]`]

### Proposition 5.3 — Konditionale feste-$\beta$-Spurklasse

Unter den beiden Voraussetzungen

1. modellrelativ $\operatorname{rank}C_p^{\rm rel}\le1$;
2. quantitativ
   $$
   |c_p|^2=O\!\left(\frac{(\log p)^2}{p}\right),
   $$

folgt für jedes feste reelle $\beta>0$

$$
\boxed{
\Sigma_{\rm rel}^{\rm ren}(\beta)\in\mathcal S_1.
}
$$

Die Konvergenz ist uniform für $\beta\ge\beta_0>0$.  
[NEU-137/H-T4: `CONDITIONAL ✓[M]_{model}`]

**Wichtig:** T2 und $c_p\neq0$ sind **keine** Voraussetzungen dieses reinen $\mathcal S_1$-Schritts.

### Offen 5.4 — Quantitative Kanalnorm

Die Schätzung

$$
|c_p|^2=O\!\left(\frac{(\log p)^2}{p}\right)
$$

ist im gegenwärtigen Endstand nicht intrinsisch bewiesen. Ihr Modellursprung benutzt insbesondere einen offenen Schritt $B_p=O(1/p)$. Status: `?[O] / CONDITIONAL`.

### Proposition 5.5 — Fredholm-Basistheorie

Sobald $\Sigma_{\rm rel}^{\rm ren}(\beta)\in\mathcal S_1$ vorliegt, sind die gewöhnliche Fredholm-Determinante und die Potenzspuren im Standard-Schattenrahmen definiert.  
[NEU-137/138: `CONDITIONAL ✓[M]`]

Ohne T2 sind die primweisen Gewichte jedoch nicht automatisch Eigenwerte der Gesamtsumme. Ein reines Primfaktor-/Euler-/Ihara-Produkt folgt daher nicht aus der Spurklasse allein.

### Satz 5.6 — Korrekte zweite Spur

Im endlichen beziehungsweise spurklassigen Scope gilt formal

$$
\boxed{
\operatorname{Tr}(\Sigma^2)
=\sum_{p,q}w_pw_q\operatorname{Tr}(P_pP_q).
}
$$

Die historische Formel mit einem zusätzlichen Gesamtfaktor ist `×[M]`.  
[NEU-139]

---

## §6 — T2, Nichtentartung und Mangoldt-Observable

### Lemma 6.1 — Konditionale Edge-Label-Orthogonalität

Falls eine intrinsisch gerechtfertigte orthogonale Zerlegung

$$
W_{\rm res,rel}
=\bigoplus_{(m,p)}^\perp H_{m\to pm}
$$

vorliegt, sind verschiedene Primlabelkanäle orthogonal. Das abstrakte Lemma ist korrekt; die Herleitung dieser orthogonalen Summe aus der ursprünglichen BC-Geometrie ist jedoch nicht geschlossen.  
[NEU-142/143: `✓[M]` conditional; intrinsisches T2 `?[O]`]

### Offen 6.2 — Nichtentartung

Ein allgemeiner Beweis

$$
\boxed{c_p\neq0\quad\text{für alle relevanten Primzahlen}}
$$

liegt nicht vor. Status: `?[O]`.

### Definition 6.3 — Primdiagonale Mangoldt-Observable (conditional)

Unter T2, $c_p\neq0$ und einer sauber abgeschlossenen primdiagonalen Hilbertraumrealisierung kann formal

$$
R_p^{\rm Mang}:=\frac{\log p}{|c_p|^2}
$$

definiert werden. Im modellrelativen Rang-eins-Scope gilt dann

$$
\operatorname{Tr}(RP_p)=\log p.
$$

Die konkrete selbstadjungierte Operatorrealisierung von $R$ bleibt `?[O]/CONDITIONAL`.  
[NEU-140–144]

Unter der zusätzlichen **konditionalen** Kanalnormschranke aus §5 folgt lediglich

$$
R_p^{\rm Mang}\gtrsim\frac{p}{\log p};
$$

eine Asymptotik $R_p\sim p/\log p$ ist nicht bewiesen.

### Proposition 6.4 — Gewöhnliche Mangoldt-Spur im absoluten Konvergenzgebiet

Im primdiagonalen Modell gilt für $\Re\beta>1$ formal

$$
\operatorname{Tr}\bigl(R\Sigma_{\rm rel}^{\rm ren}(\beta)\bigr)
=\sum_p\frac{\log p\,p^{-\beta}}{1-p^{-\beta}}
=-\frac{\zeta'}{\zeta}(\beta).
$$

Status: `CONDITIONAL ✓[M]_{model}`. Diese Gleichheit im gewöhnlichen Konvergenzgebiet ist von jeder späteren Finite-Part-Fortsetzung strikt zu unterscheiden.

---

## §7 — Scharfer Primcutoff und Grenze der Prime-only-Explizitformel

### Definition 7.1 — Prime-only-Cutoff

$$
S_X(\beta)
:=\sum_{p\le X}\frac{\log p\,p^{-\beta}}{1-p^{-\beta}}
=\sum_{k\ge1}T_k(X,\beta),
$$

$$
T_k(X,\beta):=\sum_{p\le X}\log p\,p^{-k\beta}.
$$

Die Schichtzerlegung ist exakt.  
[NEU-146: `✓[M]`]

### Satz 7.2 — PNT-Hauptterm

Für festes $k\beta$ mit $\Re(k\beta)<1$ liefert partielle Summation aus $\vartheta(X)\sim X$

$$
T_k(X,\beta)
\sim\frac{X^{1-k\beta}}{1-k\beta}.
$$

Für $k\beta=1$ tritt der logarithmische Hauptterm $\log X$ auf. Am Rand $\Re(k\beta)=1$, $k\beta\neq1$, ist der entsprechende Hauptterm beschränkt oszillierend und besitzt im Allgemeinen keinen Grenzwert.  
[NEU-146/147: `✓[M]` nach Korrektur]

### Firewall 7.3 — $\vartheta$ ist nicht $\psi$

Die Prime-only-Summe $T_k$ läuft über

$$
\vartheta(X)=\sum_{p\le X}\log p,
$$

während die klassische explizite Formel direkt die Mangoldt-Summe

$$
\psi(X)=\sum_{p^j\le X}\log p
$$

beschreibt. Ein direkter Import der $\psi$-Nullstellenterme in $T_k$ ohne Primpotenz-/Möbiuskorrektur ist `×[M]`.  
[NEU-147]

Die RH-Verbindung der zusätzlichen Nullstellenbeiträge bleibt als **Richtungsstruktur** `✓[M]_{part}` erhalten; ein vollständiger Prime-only-Äquivalenzsatz ist `?[O]`.

---

## §8 — Der korrekte Mellin-Kanal: geglättete Mangoldt-Summe

### Definition 8.1 — Testfunktion und Mellintransformierte

Sei $\varphi\in C_c^\infty([0,\infty))$ mit $\varphi(x)=1$ für $x$ nahe $0$. Für $\Re s>0$ sei

$$
\widehat\varphi(s)
:=\int_0^\infty\varphi(x)x^{s-1}\,dx.
$$

Die Mellintransformierte besitzt eine meromorphe Fortsetzung mit einfachem Pol bei $s=0$ und

$$
\boxed{\operatorname{Res}_{s=0}\widehat\varphi(s)=1.}
$$

Die historischen Aussagen „$\widehat\varphi$ ist ganz“ und „$\widehat\varphi(0)=1$“ sind `×[M]`.  
[NEU-148; Korrektur NEU-149]

### Definition 8.2 — Geglättete Mangoldt-Summe

$$
\boxed{
\Psi_{\varphi,X}(\beta)
:=\sum_{n\ge1}\Lambda(n)\varphi(n/X)n^{-\beta}
=\sum_{p,k\ge1}\log p\,\varphi(p^k/X)p^{-k\beta}.
}
$$

### Satz 8.3 — Exakte Mellin-Darstellung

Für eine direkte Mellin-Inversion auf einer Linie

$$
c>\max(0,1-\Re\beta)
$$

gilt

$$
\boxed{
\Psi_{\varphi,X}(\beta)
=\frac1{2\pi i}
\int_{(c)}
\widehat\varphi(s)X^s
\left(-\frac{\zeta'}{\zeta}(\beta+s)\right)ds.
}
$$

[H-T5: `✓[M]`]

### No-Go 8.4 — Prime-only-Mellin-Typfehler

Für

$$
S_{\varphi,X}(\beta)
=\sum_p\varphi(p/X)
\frac{\log p\,p^{-\beta}}{1-p^{-\beta}}
$$

liefert Mellin-Inversion den inneren Ausdruck

$$
\sum_{p,k\ge1}\log p\,p^{-k\beta-s},
$$

nicht

$$
-\frac{\zeta'}{\zeta}(\beta+s)
=\sum_{p,k\ge1}\log p\,p^{-k\beta-ks}.
$$

Die Live-Identität NEU-148.A für $S_{\varphi,X}$ ist deshalb `×[M]`.

### Satz 8.5 — Korrekte $\Psi/S$-Differenz

Algebraisch gilt

$$
\boxed{
\Psi_{\varphi,X}(\beta)-S_{\varphi,X}(\beta)
=\sum_{k\ge2}\sum_p\log p
\,[\varphi(p^k/X)-\varphi(p/X)]p^{-k\beta}.
}
$$

Die historische Differenzformel aus NEU-148.6 ist `×[M]`.

**Statusfirewall:** Für $\Re\beta>1/2$ ist die höhere-Primpotenzreihe absolut summierbar und liefert die natürliche Route für einen $\Psi/S$-Transfer. Der für die Finite-Part-Anwendung benötigte quantitative/uniforme Transfer bleibt im versiegelten P08-Endstand `?[O]`; P08 beansprucht hier keine neue Hochstufung.

---

## §9 — Konturrest und analytischer Finite Part

### Proposition 9.1 — Mellin-Pol bei $s=0$

Ist $\beta$ keine Polstelle von $-\zeta'/\zeta$, dann liefert der Pol von $\widehat\varphi$ bei $s=0$ im korrigierten $\Psi$-Strang den Residuenbeitrag

$$
\operatorname{Res}_{s=0}
\left[
\widehat\varphi(s)X^s
\left(-\frac{\zeta'}{\zeta}(\beta+s)\right)
\right]
=-\frac{\zeta'}{\zeta}(\beta).
$$

[NEU-149: `✓[M]`]

### Proposition 9.2 — Fixed-contour Restlemma (conditional)

Auf einer fest gewählten linken Kontur $\Gamma_{-M}$ mit

$$
\Re s\le -M<0
$$

und einem quantitativ positiven Abstand von allen relevanten Polen gilt

$$
|X^s|\le X^{-M}.
$$

Zusammen mit geeignetem vertikalem Mellin-Abfall und einer polynomialen beziehungsweise logarithmischen Kontrolle von $\zeta'/\zeta$ ergibt dies conditional

$$
R_{\varphi,X}(\beta)=O(X^{-M}).
$$

Status: `CONDITIONAL ✓[M]` für den korrigierten $\Psi$-Strang.

### Offen 9.3 — Uniforme Kontur und vollständige Residuenzählung

Nicht bewiesen ist eine einheitliche nullstellenvermeidende Kontur mit ausreichendem Abstand für einen variierenden kompakten $\beta$-Bereich sowie die vollständige uniforme Residuenzählung beim Konturgrenzübergang. Insbesondere ist die Menge

$$
\{\omega-\beta:\beta\in K\}
$$

für kontinuierliches $K$ nicht diskret.  
[NEU-149/H-T5: `?[O]`]

### Definition 9.4 — Analytischer Finite-Part-Zielwert

Nach Abzug aller nichtverschwindenden Residuenbeiträge ist das Ziel

$$
\operatorname{FP}^{\varphi}_{X\to\infty}\Psi_{\varphi,X}(\beta)
\stackrel{?}{=}
-\frac{\zeta'}{\zeta}(\beta).
$$

Der fixed-contour Baustein ist vorhanden; der vollständige uniforme Abschluss bleibt `?[O]`.

---

## §10 — Operatorielle Primlabel-Brücke und Cutoff-Hierarchie

### Definition 10.1 — Primlabel-Observable (conditional)

Unter einer intrinsisch gerechtfertigten orthogonalen Primzerlegung und Nichtentartung kann formal

$$
N_{\mathbb P}\Psi_p=p\Psi_p
$$

definiert werden. Für eine orthogonale, nicht notwendig normierte Familie ist die natürliche maximale Multiplikationsdomäne durch

$$
\sum_p p^2|\xi_p|^2\|\Psi_p\|^2<\infty
$$

zu typisieren; außerdem ist das orthogonale Komplement festzulegen.  
[NEU-150/H-T5: `CONDITIONAL`]

### Proposition 10.2 — Formale Primlabel-Spuridentität

Im primdiagonalen Modell gilt algebraisch

$$
\operatorname{Tr}\!\left(
\varphi(N_{\mathbb P}/X)\,R\,
\Sigma_{\rm rel}^{\rm ren}(\beta)
\right)
=S_{\varphi,X}(\beta).
$$

Status: `CONDITIONAL ✓[M]_{model}`.

### Offen 10.3 — Primlabel-Finite-Part

Die Aussage

$$
\operatorname{FP}_{X\to\infty}^{N_{\mathbb P}}
\operatorname{Tr}\!\left(
\varphi(N_{\mathbb P}/X)R\Sigma_{\rm rel}^{\rm ren}(\beta)
\right)
=-\frac{\zeta'}{\zeta}(\beta)
$$

ist `?[O]`. Sie benötigt mindestens den korrigierten $\Psi/S$-Transfer sowie die analytische Rest-/Residuenkontrolle.

### Offen 10.4 — $R$-Cutoff

Ein Operatorcutoff

$$
\varphi(R/\Lambda)
$$

ist nicht automatisch äquivalent zum Primlabel-Cutoff. Selbst die Zusatzannahme

$$
[ZA]:\qquad R_p\asymp\frac{p}{\log p}
$$

würde nur die grobe Skalenvergleichbarkeit liefern. Für die Identifikation von **Finite Parts** ist eine quantitativ stärkere Asymptotik samt Fehlerkontrolle nötig.  
[NEU-146/150: `?[O]`]

---

## §11 — Zwei getrennte P08-Stränge

### Strang A — Renormierungsdiagnose

Der gesicherte Anfang ist

$$
\boxed{b_{1,N}\to0.}
$$

Dazu gibt es starke finite Evidenz für Wachstum von $b_{2,N}/b_{1,N}$, aber

$$
\frac{b_{2,N}}{b_{1,N}}\to\infty
$$

bleibt `?[O]`. Falls dieser Grenzwert bewiesen wird, greift das abstrakte No-scalar-Lemma. Eine positive nichtskalare Prä-Lanczos-Geometrie $W_N$ bleibt danach weiterhin ein eigener Konstruktionsknoten `?[O]`.

### Strang B — Mangoldt/Mellin-Operatorbrücke

Die korrekte Abhängigkeitsordnung lautet:

1. **Self-Energy:** modellrelative Rangstruktur + quantitative $c_p$-Obergrenze $\Rightarrow$ feste-$\beta$-$\mathcal S_1$ `CONDITIONAL`;
2. **Mangoldt-R:** T2 + Nichtentartung + abgeschlossene Primzerlegung $\Rightarrow$ primdiagonales $R$ `CONDITIONAL`;
3. **Analytik:** exakte $\Psi_{\varphi,X}$-Mellin-Darstellung;
4. **Kontur:** uniforme Rest-/Residuenzählung `?[O]`;
5. **Prime-only-Transfer:** $\Psi/S$-Transfer in der für Finite Parts nötigen Stärke `?[O]`;
6. **Operatorbrücke:** Primlabel-Finite-Part `?[O]`;
7. **Cutoffvergleich:** Primlabel $\to R$-Cutoff `?[O]`.

Keine dieser Stufen darf durch

$$
\operatorname{Tr}_{\rm reg}:=\operatorname{AC}[-\zeta'/\zeta]
$$

ersetzt werden.

---

## §12 — Statusmatrix

| Aussage | SYN-Status | Quelle |
|---|---|---|
| korrigiertes $C_\xi\approx0.0230957$ | `PROVED` | NEU-121Cfix |
| alter $C_\xi$-Wert $-0.5493$ | `NO-GO / SUPERSEDED` | NEU-121 |
| $\widehat\Omega=Z^{-1/2}\Omega_\tau$ | `PROVED` | NEU-122, H-T1 |
| $Z_{1,N}^{-1}\sim1/\log N$ | `PROVED` | NEU-121/122 |
| historisches $A_N^{\rm Jac,-}$ selbstadjungiert | `OPEN` | H-T1/P07 |
| KMS/GNS $\to$ Jacobi | `OPEN` | NEU-122 P1 |
| KMS-Formkompatibilität | `OPEN` | NEU-122 P2 |
| $A_N^{\rm sym}$ endlich selbstadjungiert | `PROVED` | NEU-123A |
| $b_{1,N}\asymp\gamma\sqrt{\log N/N}\to0$ | `PROVED_NEG` | NEU-123A |
| Startvektor-Resolvente $\to-1/z$ | `PROVED_NEG` | H-T2 |
| $b_1\to0\Rightarrow$ gesamter Limes diagonal | `NO-GO` | NEU-123A |
| $b_{2,N}/b_{1,N}\to\infty$ | `OPEN` | NEU-123F/G |
| abstraktes No-scalar-Lemma unter Quotientendivergenz | `PROVED_CONDITIONAL` | NEU-123H |
| intrinsisches positives nichtskalares $W_N$ | `OPEN` | H-T3 |
| gewichteter Rang-eins-Operator ist orthogonaler Projektor | `NO-GO` | NEU-128A/P05 |
| NEU-128b Operator/Skalar-Formel | `NO-GO` | NEU-128b |
| PSWF $\Rightarrow$ konkrete Prä-Lanczos-Metrik | `HEURISTIC / OPEN` | NEU-130 |
| Paper-VII-H3-Skalierung | `NO-GO` | NEU-131 |
| Cancellation $\Rightarrow$ absolute Schur-Zeilensumme | `NO-GO` | NEU-131 |
| algebraische $\beta$-Zerlegung | `PROVED` | NEU-136 |
| $\sum_{p\le N}(\log p)^2/p\sim\frac12(\log N)^2$ | `PROVED` | H-T4/PNT |
| Rohdivergenz aus $c_p$-Upper-Bound | `NO-GO` | NEU-136 |
| $|c_p|^2=O((\log p)^2/p)$ intrinsisch | `OPEN / CONDITIONAL` | NEU-134–135D |
| feste-$\beta$ $\Sigma_{\rm rel}^{\rm ren}\in\mathcal S_1$ | `CONDITIONAL_MODEL` | NEU-137 |
| Fredholm-Basistheorie aus $\mathcal S_1$ | `CONDITIONAL` | NEU-137/138 |
| primeweise Eigenwert-/Eulerproduktlesart ohne T2 | `NO-GO` | NEU-138 |
| korrekte zweite Spur $\sum_{p,q}w_pw_q\operatorname{Tr}(P_pP_q)$ | `PROVED` | NEU-139 |
| intrinsisches T2 | `OPEN` | NEU-142/143 |
| $c_p\neq0$ für alle Primkanäle | `OPEN` | P05/H-T4 |
| primdiagonales Mangoldt-$R$ | `CONDITIONAL / OPEN` | NEU-140–144 |
| gewöhnliche Mangoldt-Spur $=-\zeta'/\zeta$ für $\Re\beta>1$ | `CONDITIONAL_MODEL` | NEU-141/144 |
| $\operatorname{Tr}_{\rm reg}:=\operatorname{AC}[-\zeta'/\zeta]$ | `DEFINITION` | NEU-145 |
| Schichtzerlegung des scharfen Primcutoffs | `PROVED` | NEU-146 |
| Prime-only-Explizitformel ohne $\vartheta/\psi$-Korrektur | `NO-GO` | NEU-147 |
| RH-Verbindung des Prime-only-Defekts | `PROVED_PART / OPEN` | NEU-147 |
| Mellin-Identität für $S_{\varphi,X}$ mit $-\zeta'/\zeta(\beta+s)$ | `NO-GO` | NEU-148 |
| Mellin-Identität für $\Psi_{\varphi,X}$ | `PROVED` | H-T5 |
| $\widehat\varphi$ ganz / $\widehat\varphi(0)=1$ | `NO-GO` | NEU-148 |
| $\operatorname{Res}_{0}\widehat\varphi=1$ | `PROVED` | NEU-149 |
| historische $\Psi-S$-Differenzformel | `NO-GO` | NEU-148.6 |
| quantitativer/uniformer $\Psi/S$-Transfer | `OPEN` | H-T5 |
| fixed-contour Restlemma für $\Psi$ | `CONDITIONAL` | NEU-149 |
| uniforme Kontur + vollständige Residuen | `OPEN` | NEU-149 |
| Primlabel-Observable $N_{\mathbb P}$ | `CONDITIONAL` | NEU-150 |
| Primlabel-Spuridentität | `CONDITIONAL_MODEL` | NEU-150 |
| Primlabel-Finite-Part $=-\zeta'/\zeta$ | `OPEN` | NEU-150 |
| operatorielle Realisierung von $\operatorname{Tr}_{\rm reg}$ | `OPEN` | NEU-145/150 |
| $R$-Cutoff-Transfer | `OPEN` | NEU-146/150 |

---

## §13 — Knotenprovenienz des P08-Blocks

| Live-Knoten | Rolle im SYN | Provenienzstatus |
|---|---|---|
| NEU-121 | $C_\xi$, Renormierungseingang; Altwerte gesperrt | `INCORPORATED` bereinigt |
| NEU-121Cfix | korrigiertes $C_\xi$ | `INCORPORATED` |
| NEU-122 | KMS/GNS, P1/P2/P3; lokale Normierung korrigiert | `INCORPORATED` bereinigt |
| NEU-123 | abstraktes Jacobi/Core/Carleman-Schema | `INCORPORATED` |
| NEU-123A | konkrete erste Lanczos-Kante; globale Diagonalität gesperrt | `INCORPORATED` bereinigt |
| NEU-123B | erste skalare Renormierungsdiagnose | `INCORPORATED` |
| NEU-123C | exakte Diagonaldrift-Reduktion | `INCORPORATED` |
| NEU-123D | Paritätskorrektur / konditionale HL-Heuristik | `INCORPORATED` conditional |
| NEU-123E | sparse Primpaarkorrelations-Lücke | `OPEN` |
| NEU-123F_Numerische_Diagnose | finite numerische Evidenz | `INCORPORATED` numerisch |
| NEU-123F_Ergebnisse | finite numerische Evidenz / Zusammenfassung | `INCORPORATED` numerisch |
| NEU-123G | zweite Offdiagonale, asymptotischer Grenzwert offen | `INCORPORATED` numerisch |
| NEU-123H | abstraktes No-scalar-Lemma | `INCORPORATED` conditional |
| NEU-123I | gradierte Renormierung, Selbstadjungiertheitsfirewall | `INCORPORATED` |
| NEU-124 | Spektrum/Spektralmaß erst nach Grenzoperator | `OPEN` |
| NEU-125 | skalare Lanczos-Kovarianz; Skalenprovenienz bereinigt | `INCORPORATED` bereinigt |
| NEU-127 | Prä-Lanczos-Triage | `INCORPORATED` |
| NEU-128A | Self-Energy-Modell; Projektorlesart gesperrt | `INCORPORATED` modellrelativ |
| NEU-128b | Ebenentrennung; Operator/Skalar-Formel gesperrt | `INCORPORATED` bereinigt |
| NEU-130 | PSWF-/Koerzivitätsidee | `INCORPORATED` heuristic |
| NEU-131 | historische Schur-/Nelson-Brücke scheitert | `NO-GO`; Ersatzroute `OPEN` |
| NEU-132 | Primschalenmethodik; ungewichtete H1-Schranke gesperrt | `INCORPORATED` bereinigt |
| NEU-133 | historischer Abel/H1-Kern gesperrt | `NO-GO`; gewichteter Ersatz `OPEN` |
| NEU-134 | Kanalgewichtsextraktion, quantitativ offen | `INCORPORATED` conditional |
| NEU-135 | Normkonvention im Modell | `INCORPORATED` modellrelativ |
| NEU-135D | Welt-2-Modellentscheidung; $B_p$-Abfall offen | `INCORPORATED` modellrelativ |
| NEU-136 | algebraische Zerlegung; Divergenz-/Asymptotikfehler gesperrt | `INCORPORATED` bereinigt |
| NEU-137 | feste-$\beta$ Spurklasse | `INCORPORATED` conditional |
| NEU-138 | Fredholm-Basis; reine Primfaktorlesart gesperrt | `INCORPORATED` bereinigt |
| NEU-139 | T1/T2-Diagnose; zweite Spur korrigiert | `INCORPORATED` bereinigt |
| NEU-140 | Normierungsbruch / Mangoldt-$R$ conditional | `INCORPORATED` conditional |
| NEU-141 | unbeschränkte Mangoldt-Renormierung / Konvergenzgebiete | `INCORPORATED` conditional |
| NEU-142 | T2-Bifurkationslemma | `INCORPORATED` |
| NEU-143 | Edge-Label-T2 unter Modellannahme | `INCORPORATED` conditional |
| NEU-144 | primdiagonales $R$ nur conditional | `INCORPORATED` bereinigt |
| NEU-145 | analytische Fortsetzungsdefinition | `INCORPORATED` als `DEFINITION` |
| NEU-146 | scharfer Primcutoff / [ZA] | `INCORPORATED` bereinigt |
| NEU-147 | Randfall erhalten; direkte Prime-only-Explizitformel gesperrt | `INCORPORATED` bereinigt |
| NEU-148 | falscher $S$-Mellin-Pfad gesperrt; korrekter $\Psi$-Kanal extrahiert | `NO-GO` + korrigierter SYN-Ersatz |
| NEU-149 | Mellin-Polkorrektur und conditional Restlemma | `INCORPORATED` conditional |
| NEU-150 | Primlabel-Operatorbrücke nur conditional/open | `INCORPORATED` conditional |

---

## §14 — Offene Kernfragen nach P08

P08 friert keine der folgenden Fragen als gelöst ein:

1. **KMS/GNS–Jacobi:** konkrete selbstadjungierte GNS-Observable und Formkompatibilität.
2. **Zweite Lanczos-Kante:** strenger Nachweis $b_{2,N}/b_{1,N}\to\infty$.
3. **Prä-Lanczos-Geometrie:** Konstruktion eines intrinsischen positiven nichtskalaren $W_N$.
4. **Lift-/Kanalnorm:** intrinsische Definition und quantitative Kontrolle von $|c_p|^2$.
5. **Primorthogonalität:** intrinsisches T2 statt definitorischer Edge-Direktsumme.
6. **Nichtentartung:** $c_p\neq0$ für alle relevanten Primkanäle.
7. **Mangoldt-$R$:** selbstadjungierte primdiagonale Operatorrealisierung.
8. **Mellin-Kontur:** uniforme nullstellenvermeidende Kontur und vollständige Residuenzählung.
9. **$\Psi/S$-Transfer:** quantitative/uniforme Kontrolle in der für Finite Parts benötigten Stärke.
10. **Operatorielle Regularisierung:** Primlabel-Finite-Part und Gleichheit mit der analytischen Fortsetzung.
11. **$R$-Cutoff:** quantitativer Vergleich mit dem Primlabel-Cutoff; `[ZA]` allein reicht nicht.
12. **Grenzoperator/Spektralmaß:** NEU-124 bleibt bis zu einer kanonischen Grenzoperatorrealisierung gesperrt.

---

## §15 — Routing und SYN-Endurteil

### → P10 — No-Go-Sammlung

Nach P10 werden die gesicherten negativen Resultate geroutet, insbesondere:

- Kollaps der unrenormierten ersten Jacobi-Kante;
- falsche globale Diagonalitätsfolge;
- Paper-VII-Skalierungs- und Cancellationfehler;
- Primeclock-H1/Abel-No-Go;
- log-kubische Primzahlsummen-Asymptotik;
- Prime-only-Mellin-Typfehler;
- falsche $\Psi/S$-Differenzformel.

### → P11 — globale Objekt-X-Geometrie

Nach P11 gehören:

- intrinsische Lift-/Quell-/Gramgeometrie;
- Nichtentartung und T2 als globale Geometriefragen;
- globale nichtorthogonale Primkopplung;
- globale Fredholm-/Schattenrealisierung jenseits des modellrelativen P08-Scope.

### → P12 — Finite-to-Infinite Weil

Analytische Grenzübergänge, die eine vollständige Weil-Geometrie mit endlichen/renormalisierten Modellen verbinden sollen, bleiben dort beziehungsweise in späteren Grenzblöcken zu behandeln.

### SYN-Endurteil

Der belastbare P08-Kern ist schmaler als die historischen Renormierungsblätter, aber klar typisiert:

$$
\boxed{
\text{Jacobi-Kollapsdiagnose}
\;\oplus\;
\text{conditional feste-}\beta\text{-Spurklasse}
\;\oplus\;
\text{exakter Mangoldt-Mellin-Kanal}
}
$$

mit strikt offenen Operator- und Cutoff-Brücken.

Der zentrale Schutzsatz lautet:

$$
\boxed{
\text{analytische Fortsetzung von }-\zeta'/\zeta
\neq
\text{bereits konstruierter operatorieller Finite Part}
\neq
\text{Hilbert--Pólya-/Objekt-X-Operator}.
}
$$

**Aktueller Status:** `SYN DRAFT`. Vor Freeze sind SYN-Primärcheck, pfadgebundener SYN-Zweitcheck, LaTeX-Übertragung und LaTeX-Transferaudit erforderlich.
