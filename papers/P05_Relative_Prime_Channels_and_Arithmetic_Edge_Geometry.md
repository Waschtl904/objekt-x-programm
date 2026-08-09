# P05 — Relative Prime Channels and Arithmetic Edge Geometry

**Status:** SYN FINAL AUDITED — kanonische Markdown-Quelle; LaTeX-Transfer freigegeben  
**Datum:** 9. August 2026  
**Pass-A-Basis:** Gruppe F `PASS A COMPLETE`, `PASS-A-PROTOKOLL.md`, Commit `9c23fc49`  
**F2-Primäraudit:** `audits/AUDIT-2026-08-09_F2_Primaeraudit_Fourier_Rohkopplung.md`, Commit `b6a97e27`; versiegelt `4c4c13e8`  
**F2-Zweitcheck:** `audits/AUDIT-2026-08-09_F2_Zweitcheck_Pfadgebunden.md`, Commit `27a5fe2e`  
**F3-Endstand:** Primäraudit-Patch `87b82b1a`  
**F4-Endstand:** Zweitcheck `20e7e07e`, Versiegelung `4d7ea3fc`  
**P05-SYN-Primärcheck:** `audits/AUDIT-2026-08-09_P05_SYN_Primaercheck.md`, Commit `54374bdf`  
**P05-SYN-Zweitcheck:** `audits/AUDIT-2026-08-09_P05_SYN_Zweitcheck_Pfadgebunden.md`, Commit `f50f3502`; Urteil `OHNE KONKRETEN GEGENBEFUND`  

> Dieses SYN-Paper enthält ausschließlich den nach F1–F4 gültigen Endstand. Historische Fehlversuche werden nur als Firewalls oder No-Go-Befunde erwähnt. `PASS A COMPLETE` bedeutet Migrationsabschluss, nicht Lösung der offenen mathematischen Probleme.

---

## Abstract

Wir konsolidieren die lokale Primkanal- und Primkantengeometrie des Objekt-X-Programms in einer typisierten Form. Die zentrale Struktur besteht aus drei strikt zu trennenden Ebenen: der Rohkopplung $T_p$, dem von einer gewählten Primhebung induzierten Kanaloperator $C_p^{[\widehat\varepsilon_p]}$ und seiner relativen Rang-eins-Realisierung $C_p^{\rm rel}[\widehat\varepsilon_p]$. Die exakte Liftzulässigkeit ist nicht linear, ein allgemeiner Nichtnullzeuge ist nicht konstruiert, und die Herkunft eines geladenen Repräsentanten $L_3^\circ$ bleibt blockiert. Zugleich sind mehrere robuste lokale Aussagen gesichert: die modale Rohkopplungsformel, die feste-$p$-Kollisions- und Restklassenzerlegung, die Transportnatur von $D_{\rm rel}$ in den auditierten Primsektoren, die projektionswertige Spektralmaßdarstellung, die Möglichkeit nichtorthogonaler Primkanalbilder sowie die arithmetische Trägertrennung zwischen direkten Kreuzprimkollisionen und dem von-Mangoldt-Träger. Die vollständige operatorische Primzahlpotenzrealisierung bleibt dagegen konditional.

---

## §1 — Typisierte Primkanalarchitektur

### Def. 1.1 — Drei verschiedene Operatorrollen

Für jede Primzahl $p$ werden drei Rollen strikt getrennt:

$$
\boxed{
T_p
\neq
C_p^{[\widehat\varepsilon_p]}
\neq
C_p^{\rm rel}[\widehat\varepsilon_p].
}
$$

- $T_p$ bezeichnet die Rohkopplung auf dem kontrollierten Fourier-/BC-Quellbereich.
- $C_p^{[\widehat\varepsilon_p]}$ ist der von einer gewählten Primhebung induzierte Primkanaloperator.
- $C_p^{\rm rel}[\widehat\varepsilon_p]$ ist die relative, im gewählten Modell eindimensional induzierte Realisierung.

Diese Typtrennung ist verbindlich. Rang- oder Normaussagen über $C_p^{\rm rel}$ dürfen nicht auf $T_p$ übertragen werden.  
[F1/F2: `✓[K/M]` als Typfirewall]

### Satz 1.2 — Nullmodusobstruktion auf der kontrollierten Formel

Auf der kontrollierten modalen Rohkopplungsformel gilt

$$
T_p(e_0V_p)=0.
$$

Der ungechargte Fouriermodus erzeugt daher in diesem lokalen Modell keine Rohkopplung.  
[NEU-041/155; F1/F2: `✓[M]` auf dem kontrollierten Definitionsbereich]

### Notationskonvention 1.3 — Rang-eins-Projektion

Historisch wurde für die orthogonale Rang-eins-Projektion teilweise $\pi_p$ verwendet. Da NEU-158/160 $\pi_p$ zugleich für eine Symmetriedarstellung benutzen, schreibt P05

$$
\boxed{\Pi_p^{(1)}:=|e_1^{(p)}\rangle\langle e_1^{(p)}|.}
$$

### Satz 1.4 — Rang-eins-Aussage nur für die induzierte Ebene

Im eindimensional induzierten relativen Modell gilt

$$
\operatorname{rank} C_p^{\rm rel}[\widehat\varepsilon_p]\le 1.
$$

Für den zugehörigen gewichteten positiven Rang-eins-Operator

$$
P_p=|c_p|^2\Pi_p^{(1)},
\qquad
(\Pi_p^{(1)})^2=\Pi_p^{(1)},
$$

gilt

$$
P_p^2=|c_p|^2P_p.
$$

Insbesondere ist $P_p$ im Allgemeinen kein orthogonaler Projektor.  
[F1/F2: `✓[M]` modellrelativ]

### Firewall 1.5 — Kein intrinsisches Primgewicht aus dem Rang-eins-Modell

Aus den obigen Identitäten folgt nicht unbedingtes

$$
c_p\neq0,
$$

keine Hebungsunabhängigkeit von $|c_p|^2$ und keine termweise Asymptotik

$$
|c_p|^2\asymp \frac{(\log p)^2}{p}.
$$

Nichtentartung und Hebungsunabhängigkeit bleiben offen.  
[NEU-151–153; F2: `?[O]`]

---

## §2 — Liftgeometrie und exakte Zulässigkeit

### Notationskonvention 2.0 — Liftkern und verbundene Liftform

Die historischen F2-Blätter verwenden $K_p$ für den Kern der primitiven Projektion. Da F3 dieselbe Buchstabenfamilie $K_p,K_{pq}$ für Prim-/Feshbachblöcke verwendet, schreibt P05 für den Liftkern eindeutig

$$
\boxed{\mathscr K_p^{\rm lift}:=\ker\pi_{\rm prim}.}
$$

Ebenso wird die im Liftstrang verwendete verbundene Form zur Abgrenzung vom späteren BC-Halbgewicht $h_p^{\rm bal}$ als

$$
\boxed{h_p^{\rm conn}}
$$

notiert. Beide Änderungen sind reine SYN-Disambiguierungen.

### Def. 2.1 — Primitive Liftfaser

Die Fourier-geladenen Richtungen

$$
E_p^{\rm ch}:=\operatorname{span}\{e_uV_p:u\neq0\}
$$

liegen algebraisch in $\mathscr K_p^{\rm lift}$.

### Satz 2.2 — Die Normierungsbedingung ist quadratisch

Für eine Liftänderung $k$ relativ zu einem Basispunkt $\widehat\varepsilon_p^{\,0}$ besitzt die exakte Normierungsbedingung die Form

$$
2\operatorname{Re}h_p^{\rm conn}(\widehat\varepsilon_p^{\,0},k)
+h_p^{\rm conn}(k,k)=0.
$$

Sie ist daher keine homogene lineare Kerngleichung.  
[NEU-157 rev.3 / 165b: `✓[M]`]

### Satz 2.3 — Keine zusätzliche lineare Kernfamilie im auditierten Quellenkegel

Im explizit auditierten Quellenkegel liefern NEU-157 und NEU-44 keine zusätzlichen nichttrivialen Operatoren

$$
L_{p,a}:\mathscr K_p^{\rm lift}\to Y_{p,a}
$$

mit exakter Zulässigkeitsbedingung $L_{p,a}(k)=0$. In diesem Quellenkegel gilt daher für die postulierte homogene Kernfamilie

$$
\mathscr K_p^{\rm hom}=\mathscr K_p^{\rm lift}.
$$

Dies ist ein negativer Quellenbefund, kein globaler mathematischer Unmöglichkeitssatz.  
[NEU-167b: `✓[M]_{neg}` als Quellenbefund]

### Offen 2.4 — Exakt zulässiger Nichtnullzeuge

Ein vollständiger Beweis der Existenz eines exakt zulässigen $k$ mit

$$
T_p(k)\neq0
$$

liegt im auditierten Quellenstand nicht vor. Präprojektive und infinitesimale Satzschemata sind gültig, die Integration in die exakte nichtlineare Zulässigkeitsmenge bleibt offen.  
[NEU-157/168: `?[O]`]

---

## §3 — Rohkopplung und feste-$p$-Kollisionsgeometrie

### Def. 3.1 — Modale Rohkopplung

Für $u\neq0$ lautet die kontrollierte präprojektive Formel

$$
T_p^{\rm pre}(e_uV_p)
= -\sum_{s,m}\ell_{s,m}\,u\,s\log p\;e_{u+ps}V_{pm}.
$$

Die Formel ist nur auf dem explizit kontrollierten modalen Quellbereich zu verwenden; sie liefert keine automatische globale Operatorverlängerung.

### Satz 3.2 — Injektivität für einen festen Eingangsmodus

Für festes $p$ und festes $u$ ist

$$
(s,m)\longmapsto (u+ps,pm)
$$

injektiv. Verschiedene Summanden eines einzelnen Eingangsmodus kollidieren daher nicht in derselben algebraischen Zielkoordinate.  
[NEU-169: `✓[M]`]

### Korollar 3.3 — Bedingte Einzelmoden-Nichtverschwindung

Definiere

$$
\operatorname{supp}^{\times}(L_3^\circ)
:=\{(s,m):s\ell_{s,m}\neq0\}.
$$

Dann gilt auf dem kontrollierten modalen Bereich

$$
\operatorname{supp}^{\times}(L_3^\circ)\neq\varnothing
\Longrightarrow
T_p^{\rm pre}(e_uV_p)\neq0
\qquad (u\neq0).
$$

Die Voraussetzung ist im alten Quellenpfad nicht hergeleitet.  
[NEU-169: `✓[M]` konditional; NEU-170d: Provenienz `?[O]`]

### Satz 3.4 — Restklassen-/Faltungszerlegung

Für eine Zielkollision innerhalb eines festen Primkanals gilt

$$
(u,s,m)\sim_p(u',s',m')
\iff
m=m',\qquad u-u'=p(s'-s).
$$

Nach Zerlegung in Restklassen $c\in\mathbb Z/p\mathbb Z$ wird das Mehrmoden-Kernproblem zu einem Faltungsannihilator:

$$
x^{(c)}*b^{(m)}=0.
$$

Dies ist die kanonische lokale Kollisionsbeschreibung für P05.  
[NEU-169: `✓[M]`]

### Firewall 3.5 — Feste-$p$-Kollision ist keine Kreuzprimkollision

Die obige Relation betrifft einen festen Primkanal $p$. Sie ist typologisch verschieden von einer Kreuzprimkollision $p\neq q$ der Form

$$
pm_p=qm_q.
$$

Beide Kollisionsbegriffe dürfen nicht identifiziert werden.  
[F2/F4: `✓[K/M]` Scope-Firewall]

---

## §4 — Herkunftsblockade des geladenen $L_3^\circ$

### Satz 4.1 — Rechenzulässig ist nicht herkunftszulässig

Die Modellwahl

$$
L_3^\circ=e_1V_1
$$

ist innerhalb des historischen Testmodells rechenzulässig und liefert beispielsweise den nichtverschwindenden Skalar

$$
(p-1)\log p\neq0.
$$

Daraus folgt jedoch nicht, dass $e_1V_1$ ein aus dem gegebenen abstrakten Datum $[L_3]$ hergeleiteter oder kanonisch gewählter Repräsentant ist.  
[NEU-162, korrigiert durch NEU-170d: `CONDITIONAL`]

### Satz 4.2 — Typ- und Ladungsblockade sind unabhängig

Der Endanker NEU-170d trennt:

$$
[L_3]\not\longmapsto L_3^\circ=e_1V_1
\qquad\text{(Herkunftsblockade)},
$$

und

$$
(p-1)\log p\neq0
\not\Longrightarrow
C_p(e_{1-p}V_p)\neq0
\qquad\text{(Zielkantenblockade)}.
$$

Ein positiver Skalarfaktor allein konstruiert weder einen typisierten Repräsentanten noch die benötigte nichtverschwindende relative Zielkante.

### Satz 4.3 — Endstatus des alten Typquellenpfads

Im auditierten Quellenkegel ist kein vollständiges Tupel

$$
(B_3,M,C^\bullet,b,L_3,\rho_{\rm op})
$$

konstruiert. Dies ist

- `✓[M]_{neg}` als Quellenbefund,
- `?[O]` als mathematische Neukonstruktionsfrage.

Außerdem ist

$$
\delta_{\rm BC}:A_Q\to A_Q
$$

eine Algebraableitung und nicht das Hochschild-Kodifferential

$$
b:C^n(B_3,M)\to C^{n+1}(B_3,M).
$$

[NEU-173]

---

## §5 — Quotienten- und Symmetriearchitektur

### Notationskonvention 5.0 — Quotientenraum und Symmetriedarstellung

NEU-159/160 verwenden $Q_p$ für den Rohkopplungsquotienten. Im globalen Objekt-X-Programm ist $Q_p$ zugleich für den lokalen Weil-Beitrag reserviert. P05 schreibt deshalb für den F2-Quotientenraum

$$
\boxed{\mathscr Q_p^{\rm quot}:=Q_p^{(\mathrm{NEU\text{-}159/160)}.}
$$

Die historische Darstellung $\pi_p:G_p\to\mathcal U(Q_p)$ wird entsprechend als

$$
\boxed{\pi_p^{\rm sym}:G_p\to\mathcal U(\mathscr Q_p^{\rm quot})}
$$

geschrieben, um sie von der früheren Rang-eins-Projektion zu unterscheiden.

### Satz 5.1 — Abstrakte Quotientenstruktur

Auf der abstrakten Ebene sind folgende Aussagen gültig:

- die wohldefinierte positive Quotientenform nach Nullraumfaktorisierung,
- die skaliert-isometrische Identifikation mit dem abgeschlossenen Bildraum,
- das allgemeine Nullraumabstiegslemma,
- das Intertwining-zu-Unitärität-Lemma.

[NEU-160: `✓[M]`]

### Satz 5.2 — Abstrakter Kommutantensatz

Für eine konkrete unitäre Darstellung $\pi_p^{\rm sym}$ auf $\mathscr Q_p^{\rm quot}$ gilt: Beschränkte positive semidefinite $G_p$-invariante Formen sind genau dann skalare Vielfache einer Referenzform, wenn

$$
\pi_p^{\rm sym}(G_p)'=\mathbb C I.
$$

Dies ist der abstrakte Schur-/Kommutantenmechanismus.  
[NEU-158: `✓[M]`]

### Offen 5.3 — Konkrete Realisierung

Nicht automatisch mitbewiesen sind:

$$
\mathscr Q_p^{\rm quot}\neq\{0\},
$$

eine konkrete unitäre Wirkung $\pi_p^{\rm sym}$, deren Irreduzibilität und damit die konkrete Eindeutigkeit der verbundenen Form.  
[NEU-158–160: `?[O]` / `CONDITIONAL`]

### Firewall 5.4 — Kein globaler Deszent aus der lokalen Formel

NEU-166a/166b liefern keine unbedingte globale Erweiterung von $T_p^{\rm pre}$, keinen vollständigen Definitionsbereich, keinen Quotientendeszent und keinen kanonischen transversalen Detektor. Fall 3a ist nur lokal/modenweise formelmäßig bestätigt; die globale Fallentscheidung bleibt offen.  
[F2: `?[O]`]

---

## §6 — Transportgeometrie der auditierten Primsektoren

### Notationskonvention 6.0 — Transportkoeffizient

NEU-225 verwendet historisch ebenfalls das Symbol $c_p$ für den Transportkoeffizienten $\frac12\gamma_Np\log p$. Dieses Symbol ist in §§1–2 bereits für die hebungsabhängige Primkanal-Amplitude belegt. P05 disambiguiert daher rein redaktionell:

$$
\boxed{\kappa_p^{\rm tr}:=\frac12\gamma_Np\log p.}
$$

Diese Umbenennung verändert keine mathematische Aussage aus NEU-225.

### Satz 6.1 — Transportnormalform

Auf einer auditierten Primfaser $\mathcal H_{p,a}$ gilt die unitäre Transportnormalform

$$
D_{\rm rel}\big|_{\mathcal H_{p,a}}
\cong
2i\kappa_p^{\rm tr}\frac{d}{dt}
\quad\text{auf}\quad
L^2(\mathbb R)\oplus L^2(\mathbb R).
$$

[NEU-225; F3: `✓[M]`]

### Korollar 6.2 — Spektraltyp im Primsektor

In den auditierten Primsektoren besitzt $D_{\rm rel}$ rein absolutstetiges Spektrum und keinen Kern; ein kompakter Resolvent ist ausgeschlossen. Damit ist $D_{\rm rel}$ dort ein Transportgenerator und kein bereits gefundener Hilbert–Pólya-Operator.  
[F3: `✓[M]`]

### Offen 6.3 — Zusammengesetzte Sektoren

Für nichtprimitive beziehungsweise zusammengesetzte $m$-Sektoren können Mehrfachsprünge Restklassen mischen. Eine globale Spektralaussage über sämtliche Mischsektoren ist nicht bewiesen.  
[`[O-225-3]`: `?[O]`]

### Satz 6.4 — Spektralmaß statt diskreter Eigenbasis

Die historische diskrete Eigenbasisdarstellung für $D_{\rm rel}$ ist zu ersetzen durch die projektionswertige Spektralmaßform. Für Primkanalabbildungen $V_p,V_q$ definiere

$$
\mu_{pq}^{a,b}(B)
:=\langle V_pa,E_D(B)V_qb\rangle,
$$

und damit

$$
\langle a,K_{pq}(z)b\rangle
=
\int_{\mathbb R}\frac{d\mu_{pq}^{a,b}(\lambda)}{\lambda-z}.
$$

Diese Form ist die verbindliche spektrale Schreibweise.  
[NEU-227: `✓[K/M]`]

---

## §7 — Nichtorthogonale Primkanalgeometrie

### Def. 7.1 — Koordinatenwörterbuch

Das verbindliche Wörterbuch lautet

$$
\eta_{p;m;s,u}
\longleftrightarrow
e_RV_M,
\qquad
M=pm,
\quad
R=u+ps.
$$

Es identifiziert die Primkantenkoordinaten mit den BC-Koordinaten und ist insbesondere im Primsektor vollständig kontrolliert.  
[NEU-227: `✓[M]`]

### Satz 7.2 — Primkanalbilder müssen nicht orthogonal sein

Verschiedene Primkanalbilder können nichttrivial überlappen. Daher ist eine globale Primblockdiagonalität

$$
\mathcal K_N\stackrel?=\bigoplus_p K_p
$$

nicht strukturell erzwungen. Kreuzblöcke $K_{pq}$ können generisch nichtverschwinden; dies ist keine Aussage, dass sie für jedes $p\neq q$ zwingend ungleich null sind.  
[NEU-226/227; F3: `✓[M]`]

### Firewall 7.3 — Nichtorthogonalität ist nicht Primmischung von $D_{\rm rel}$

Die Off-Diagonalität kann aus überlappenden Kanalbildern

$$
\operatorname{Ran}V_p\not\perp\operatorname{Ran}V_q
$$

entstehen, ohne dass $D_{\rm rel}$ selbst Primlabels mischen muss.

---

## §8 — Arithmetische Primzahlpotenzgewichte

### Satz 8.1 — Primitiver algebraischer Halbgewichtsfaktor

Im primitiven $p$-Kanal wird algebraisch der Halbgewichtsfaktor

$$
h_p^{\rm bal}=p^{-1/2}I
$$

und damit der lokale Faktor

$$
\frac{\log p}{\sqrt p}
$$

erhalten. Dies ist ein partielles algebraisches Resultat; eine vollständige Hilbert-Selbstadjungiertheit, Abschließbarkeit, Domäne und ein globaler Funktionalkalkül des zugrundeliegenden BC-Operators sind damit nicht bewiesen.  
[NEU-250g; F4: `✓[M]_{part}`]

### Satz 8.2 — Testfunktionswert als Matrixkoeffizient

Für die Autokorrelation gilt

$$
g_a(x)=\operatorname{Re}\langle a,U_xa\rangle_{L^2(\mathbb R)},
$$

insbesondere

$$
\boxed{
g_a(\log p)=\operatorname{Re}\langle a,U_{\log p}a\rangle.
}
$$

Dieser Ausdruck ist ein unitärer Matrixkoeffizient und kein Normquadrat; er kann null oder negativ sein.  
[NEU-250h: `✓[M]`]

### Satz 8.3 — Arithmetische Primzahlpotenzidentität

Für jede Primzahlpotenz $p^m$ gilt

$$
\boxed{
\frac{\Lambda(p^m)}{\sqrt{p^m}}
=
\frac{\log p}{p^{m/2}}.
}
$$

Dies ist eine arithmetische Identität.  
[F4: `✓[M]`]

### Firewall 8.4 — Arithmetische Identität ist keine vollständige Operatorrealisierung

Im gegenwärtigen Quellenstand ist kein vollständiger Beweis

$$
h_n^{\rm bal}=n^{-1/2}I
\qquad\text{für alle }n\ge1
$$

gefunden. Die Rückreferenz in NEU-250i auf eine solche allgemeine Rechnung ist durch NEU-250g nicht gedeckt. Daher bleibt die starke form-/operatorische Primzahlpotenzrealisierung

$$
h_{p^m}^{\rm bal}
\bigl(H_{\rm pr}^{1/2}E_R,H_{\rm pr}^{1/2}E_{R'}\bigr)
=
\frac{\log p}{p^{m/2}}\delta_{RR'}
$$

`CONDITIONAL`.

### Firewall 8.5 — $H_{\rm pr}$ ist nicht die von-Mangoldt-Funktion auf gemischten Zahlen

Die formal gradnormierte BC-Energie darf nicht mit der arithmetischen Funktion $\Lambda$ auf allen natürlichen Zahlen identifiziert werden. Für eine Zahl mit mehreren verschiedenen Primteilern, etwa $6$, gilt arithmetisch

$$
\Lambda(6)=0,
$$

während die gradnormierte Energie nicht automatisch verschwindet.  
[F4]

---

## §9 — Trägertrennung: direkte Kreuzprimkollision versus Mangoldt-Träger

### Satz 9.1 — Kreuzprimkollision erzeugt keinen Mangoldt-Trägerpunkt

Seien $p\neq q$ Primzahlen und

$$
pm_p=qm_q=M.
$$

Dann besitzt $M$ mindestens zwei verschiedene Primteiler. Daher

$$
\Lambda(M)=0.
$$

Folglich

$$
\boxed{
\operatorname{supp}\Lambda
\cap
\operatorname{supp}(\text{direkte Kreuzprimkollision})
=
\varnothing.
}
$$

[NEU-250j; F4: `✓[M]`]

### Firewall 9.2 — Trägertrennung ist kein Orthogonalitäts-No-Go

Satz 9.1 widerspricht nicht Satz 7.2. Die generische nichtorthogonale Primkanalgeometrie kann bestehen, obwohl direkte Kreuzprimkollisionen nicht auf dem Mangoldt-Träger liegen. Der Satz trennt arithmetischen Träger und Kollisionssupport; er beweist keine globale Orthogonalität der Primkanäle.

---

## §10 — Schnittstellen zu den Folgesynthesen

### → P06 — Jacobi–Feshbach und Spektralmaß

Nach P06 werden weitergereicht:

- Schur-/Feshbach-Komplementfragen,
- globale Quotienten- und Deszentfragen,
- Spektralmaß-/Schattenklassenkriterien,
- $u$-Regulator und Quellhilbertisierung,
- die offenen zusammengesetzten Sektoren `[O-225-3]`.

### → P09 — BC/Hochschild-Typfundament

Nach P09 werden weitergereicht:

$$
(B_3,M,C^\bullet,b,L_3,\rho_{\rm op}),
$$

die Konstruktion eines typkorrekten Repräsentanten von $[L_3]$ sowie die strikte Trennung von $\delta_{\rm BC}$ und Hochschild-$b$.

### → P11 — Globale nichtorthogonale Kopplung

Nach P11 werden weitergereicht:

- gemeinsame globale Quellenräume,
- Gramoperatoren der überlappenden Primkanalbilder,
- globale Off-Diagonalblöcke,
- der Mediatorstatus J-A/J-B,
- die Verbindung zwischen arithmetischer Trägerstruktur und globaler Weil-Geometrie.

P05 behauptet keine dieser globalen Konstruktionen bereits gelöst zu haben.

---

## §11 — Statusmatrix

| Aussage | Status | Quelle / Paket |
|---|---|---|
| $T_p\neq C_p^{[\widehat\varepsilon_p]}\neq C_p^{\rm rel}[\widehat\varepsilon_p]$ | `✓[K/M]` Typfirewall | F1/F2 |
| $T_p(e_0V_p)=0$ auf kontrollierter modaler Formel | `✓[M]` | F1/F2 |
| $\operatorname{rank}C_p^{\rm rel}\le1$ im eindimensional induzierten Modell | `✓[M]` modellrelativ | F1/F2 |
| intrinsisches $c_p\neq0$ / Nichtentartung | `?[O]` | F1/F2 |
| starke oder schwache Hebungsunabhängigkeit | `?[O]` | F2 |
| Normierungsbedingung mit $h_p^{\rm conn}$ ist quadratisch | `✓[M]` | F2 |
| zusätzliche lineare $L_{p,a}$-Kernfamilie im auditierten Quellenkegel | `✓[M]_{neg}` Quellenbefund | F2 |
| exakt zulässiger Nichtnullzeuge | `?[O]` | F2 |
| feste-$p$-Injektivität $(s,m)\mapsto(u+ps,pm)$ | `✓[M]` | F2 |
| feste-$p$-Restklassen-/Faltungskollision | `✓[M]` | F2 |
| geladener $L_3^\circ$ aus $[L_3]$ hergeleitet | `?[O]` | NEU-170d/173 |
| abstrakte Quotienten-/Intertwining-Lemmata | `✓[M]` | F2 |
| konkrete $\mathscr Q_p^{\rm quot}\neq0$, unitäre Wirkung, Irreduzibilität | `?[O]` / `CONDITIONAL` | F2 |
| Transportnormalform $D_{\rm rel}\cong2i\kappa_p^{\rm tr}d/dt$ in Primsektoren | `✓[M]` | F3 |
| reines a.c.-Spektrum / kein Kern in auditierten Primsektoren | `✓[M]` | F3 |
| globale Spektralaussage in zusammengesetzten Sektoren | `?[O]` | `[O-225-3]` |
| projektionswertige Spektralmaßform | `✓[K/M]` | F3 |
| Primkanalbilder können nichttrivial überlappen | `✓[M]` | F3 |
| Primblockdiagonalität ist nicht strukturell erzwungen | `✓[M]` | F3 |
| primitiver Faktor $\log p/\sqrt p$ | `✓[M]_{part}` | F4 |
| $g_a(\log p)=\operatorname{Re}\langle a,U_{\log p}a\rangle$ | `✓[M]` | F4 |
| $\Lambda(p^m)/\sqrt{p^m}=\log p/p^{m/2}$ | `✓[M]` | F4 |
| $h_n^{\rm bal}=n^{-1/2}I$ für alle $n$ | `CONDITIONAL` / Beweis nicht gefunden | F4 |
| vollständige operatorische Primzahlpotenzrealisierung | `CONDITIONAL` | F4 |
| Kreuzprimkollision $\cap\operatorname{supp}\Lambda=\varnothing$ | `✓[M]` | F4 |
| Kreuzprim-Trägertrennung impliziert keine Primorthogonalität | `✓[M]` | F3/F4 |

---

## §12 — Offene Kernfragen nach P05

P05 schließt den lokalen Syntheseblock, lässt aber insbesondere folgende Fragen offen:

1. **Liftintrinsik:** Konstruktion einer hebungsunabhängigen, nichtentarteten Primkanalgröße $|c_p|^2$.
2. **Exakte Zulässigkeit:** Konstruktion eines exakt zulässigen geladenen Lifts mit nichtverschwindender Rohkopplung.
3. **$L_3$-Herkunft:** typisierte Repräsentantenbrücke von $[L_3]$ zu einem tatsächlich verwendbaren geladenen Operator-/Algebraelement.
4. **Globale Deszendenz:** vollständiger Definitionsbereich und Quotientendeszent der Rohkopplung.
5. **Zusammengesetzte Sektoren:** Spektral- und Restklassengeometrie jenseits der auditierten Primfasern.
6. **Primzahlpotenzoperator:** Beweis einer allgemeinen BC-Halbgewichtung und Hilbert-Fundierung des gradnormierten Operators.
7. **Globale Gramgeometrie:** Konstruktion der nichtorthogonalen globalen Kopplung, die lokale Primkanalbilder und den archimedischen Kanal in einer gemeinsamen positiven Geometrie organisiert.

---

## §13 — SYN-Endurteil

Die lokale Primkanalgeometrie ist nach Gruppe F deutlich schärfer typisiert als in den historischen Knoten:

$$
\boxed{
\text{lokale Rohkopplung}
+\text{nichtlineare Liftgeometrie}
+\text{Transportprimfasern}
+\text{nichtorthogonale Kanalbilder}
+\text{arithmetische Trägertrennung}
}
$$

sind miteinander kompatibel, aber noch keine globale Objekt-X-Realisierung.

Der zentrale Schutzsatz für die weitere Migration lautet:

$$
\boxed{
\text{lokale Primkanalstruktur}
\neq
\text{globale positive Gramkopplung}
\neq
\text{Hilbert--Pólya-Operator}.
}
$$

**Aktueller Status:** `SYN FINAL AUDITED`. Der unabhängige P05-SYN-Gegencheck ergab keinen konkreten Gegenbefund. Die Markdown-Inhaltsstufe ist abgeschlossen; als nächster Schritt folgt die reine LaTeX-SYN-Übertragung mit anschließendem Transferaudit.
