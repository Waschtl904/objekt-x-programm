# P11 / Objekt X — AR(1), Weil-Tail und OX-GRAM: Konsolidierungsstand 2026-09-12

> **Rolle:** Forschungs-Konsolidierung auf `main`-Basis `77f47ec32787d5d8f2c8106c97b611650d44b9ff`.
> **Kein Registry-Eintrag, kein Freeze, kein RH-Resultat.**
> Dieses Dokument trennt exakte Algebra, externe/numerische Evidenz, offene Operatorfragen und ausdrücklich zurückgezogene Deutungen.

## 0. Warum diese Konsolidierung nötig ist

Seit dem Merge von PR #97 wurde die Prime-Power-/Hub-Struktur mehrfach neu interpretiert. Mehrere Deutungen wurden im Audit zurückgezogen, während einige algebraische Identitäten jeden Gegencheck überlebt haben. Ziel dieses Dokuments ist, die belastbaren Teile als neue operative Front festzuhalten und veraltete Zwischeninterpretationen zu sperren.

Die historische PR-#91-/PR-#96-/PR-#97-Provenienz bleibt erhalten. Dieses Dokument promotet keinen offenen Draft-PR und ersetzt keine Primärquelle.

---

## 1. Exaktes Prime-Power-Ledger

Für eine feste Primzahl `p` und Kanäle `j,k>=1` verwendet P11 den Hubfaktor

```math
\alpha_{p,k}=\sqrt{\log p}\,p^{-3k/4}.
```

Die Rest-Martingalmultiplizität ist

```math
1+\sum_{a=0}^{m-1}(p-1)p^a=p^m,
\qquad m=\min(j,k).
```

Daraus folgt die exakte kombinierte Koeffizientenmatrix

```math
\boxed{
C_{jk}^{(p)}=(\log p)\,p^{\min(j,k)}p^{-3(j+k)/4}.}
```

Auf der Diagonale

```math
\boxed{
C_{kk}^{(p)}=(\log p)p^{-k/2}=w_{p,k}}
```

mit dem Weil-Primzahlpotenzgewicht

```math
w_{p,k}=\frac{\Lambda(p^k)}{\sqrt{p^k}}=\frac{\log p}{p^{k/2}}.
```

Der Exponent `3/4` ist damit nicht eine frei gewählte Dämpfung. Wenn ein primitiver Faktor `p^{-\beta k}` unter der Martingalmultiplizität `p^k` die Weil-Diagonale ergeben soll, zwingt

```math
p^k p^{-2\beta k}=p^{-k/2}
```

exakt

```math
\boxed{\beta=3/4.}
```

**Status:** `✓[M]` elementare Algebra; zusätzlich extern/Arb an endlichen Ledgerblöcken gegengeprüft.

---

## 2. AR(1)-/Kac–Murdock–Szegő-Struktur

Setze

```math
q_p=p^{-1/2}.
```

Dann

```math
\boxed{
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}\,q_p^{|j-k|}.}
```

Nach Weil-Diagonalnormalisierung ist jeder Primast daher die stationäre AR(1)-Kovarianz

```math
R_q(j,k)=q^{|j-k|}.
```

Für verschiedene Primzahlen `p!=r` liefert der gemeinsame Hub die Root-Korrelation

```math
\boxed{R_{(p,j),(r,k)}=q_p^j q_r^k.}
```

Diese cross-prime Masse ist bereits fensterlos vorhanden und kein räumlicher Boundaryterm.

**Status:** `✓[M]` für die Koeffizientenalgebra; externe Arb-Kontrollen liegen vor. Kein Prioritätsanspruch gegenüber nicht vollständig geprüfter Literatur.

---

## 3. Tail-Transform und Hub als Root-Komponente

Für `0<q<1`, `s=sqrt(1-q^2)`, definiere auf dem Kanalraum

```math
(T_qX)_k=s\sum_{m\ge k}q^{m-k}X_m.
```

Dann gilt für `j,m>=1`

```math
(T_q^*T_q)_{jm}=q^{|j-m|}-q^{j+m}.
```

Mit `u_j=q^j` folgt

```math
\boxed{T_q^*T_q+uu^*=R_q.}
```

Der inverse Innovationsoperator ist exakt

```math
\boxed{D_q=T_q^{-1}=\frac{I-qS}{\sqrt{1-q^2}}.}
```

Er ist **nicht unitär**. Insbesondere ist `D_q^*D_q-I` nicht Rang 1. Die separat wahre Identität

```math
D_qD_q^*=R_q^{-1}+\frac1{p-1}e_1e_1^*
```

betrifft die andere Operatorreihenfolge und darf nicht als „Nichtunitarität = Hub“ umgedeutet werden.

Im fensterlosen Einzelprimast ist der Hubwert aus der ersten Tail-Koordinate rekonstruierbar:

```math
h_p=\frac{1}{\sqrt{p-1}}Y_{p,1}.
```

Das bedeutet koordinative Redundanz, nicht metrische Irrelevanz: P11 zählt Hub und Rest in getrennten Zielkomponenten; zusammen entsteht die stationäre AR(1)-Gramstruktur.

**Status:** `✓[M]` exakte Operatoralgebra auf dem Kanalraum.

---

## 4. Exakte Weil-Tail-Normalform der P11-Restseite

Mit dem nackten Weil-normalisierten Kanal

```math
X_{p,k,R}=\sqrt{w_{p,k}}\,K_{p,k}P_R
```

und

```math
Z_{p,k,R}v
=\sqrt{1-p^{-1}}\,P_{\Omega_{p,k-1,R}}
 \sum_{m\ge k}p^{-3(m-k)/4}K_{p,m}P_Rv
```

ist die P11-Restform sektorenweise exakt

```math
\boxed{
R_R^*R_R=\sum_{p,k}w_{p,k}Z_{p,k,R}^*Z_{p,k,R}.}
```

Dies ist eine Umparametrisierung der vorhandenen P11-Restform, kein neuer Positivitätssatz.

Fensterlos gilt nach Herausziehen der Weilgewichte die geometrische Tailratio `q=p^{-1/2}`; damit verbindet sich die P11-Martingalstruktur exakt mit der AR(1)-Algebra aus §2–3.

**Status:** `✓[M]` algebraisch; der spezielle PR-#91-Sektor `(2,0)` wurde extern mit Arb gegengeprüft.

---

## 5. PR-#91-Zeuge: was er wirklich zeigt

Am R=1-Prime-2-Zeugen trägt in der Restseite nur Sektor `(2,0)` bei. Im Codepfad sind die aktiven Paarungen

```text
(1,1), (3,1), (4,2)
```

mit den geschlossenen Werten

```math
-\frac{\log2}{2\sqrt2},\qquad
+\frac{\log2}{8},\qquad
+\frac{\log2}{16\sqrt2}.
```

Die zugehörige dünne Zeugenmatrix hat Rang 2, nicht Rang 1. Korrekt ist nur: die Beträge ihrer aktiven Einträge liegen auf der Rang-1-Amplitudenhülle

```math
(\log2)2^{-3(j+k)/4},
```

während die Trägermaske den Rang-1-Charakter zerstört.

Der naive einseitige Austausch

```math
K_k\mapsto (K_k-p^{-3/4}K_{k-1})/\sqrt{1-p^{-1}}
```

ist **nicht** die AR(1)-Whitening-Kongruenz des vollständigen Gramoperators. Sein FAIL am Zeugen falsifiziert diesen einseitigen Test, nicht die AR(1)-Struktur.

Der PR-#91-Zeuge bleibt nützlich als exakte gemischte Kalibration mit `\langle a,b\rangle=0`; für die globale lokale Identitätsmasse ist er gerade deshalb blind.

---

## 6. Nackte Translationkanäle und die lokale Identitätsmasse

Für

```math
K_{p,k}=U_{k\log p/2}-U_{-k\log p/2}
```

gilt exakt

```math
\boxed{
K_{p,k}^*K_{p,k}=2I-U_{k\log p}-U_{-k\log p}.}
```

Die orthogonale Weil-gewichtete Kanalsumme erzeugt daher neben dem korrekten Primkamm eine lokale Masse

```math
\mathcal A_X I,
\qquad
\mathcal A_X=2\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}.
```

Bei einem festen kompakten Fenster `(-a,a)` ist nur `n<=e^{2a}` informationstragend; für `log n>2a` sind die verschobenen Träger disjunkt und

```math
\|K_nv\|^2=2\|v\|^2
```

exakt: zusätzliche Kanäle tragen nur die lokale Masse.

Die Größe

```math
A_L^{\rm Zhu}=\sum_{\log n<2L}\frac{2\Lambda(n)}{\sqrt n}
```

ist definitionsgleich mit dieser endlichen Primkammmassse bei `X=e^{2L}`. Die Identifikation ist wichtig; ein daraus künstlich definiertes `epsilon=e^{-A_L}` erzeugt jedoch keinen neuen Renormierungsmechanismus.

---

## 7. Suzuki-Fensterform: aktuelle OX-GRAM-Normalform

Für festes `a` wird Suzukis lokalisierte Weilform mit der Kanalidentität aus §6 zu

```math
\boxed{
Q_{B_a}(v)=G_a^+(v)-N_a(v)}
```

mit positiver Featureform

```math
G_a^+(v)
=\frac14\iint_{(-a,a)^2}\frac{|v(x)-v(y)|^2}{|x-y|}\,dx\,dy
 +\sum_{n\le e^{2a}}\frac{\Lambda(n)}{\sqrt n}\|K_nv\|^2
 -\frac12\int_{-a}^{a}\log(a^2-x^2)|v(x)|^2\,dx
```

für `a<=1`; alle drei angezeigten Summanden sind dann nichtnegativ.

**Terminologie-Firewall:** Der Kernel `1/|x-y|` ist in einer Dimension nicht die gewöhnliche `H^{1/2}`-Seminorm (`|x-y|^{-2}` wäre dafür maßgeblich). Die passende Bezeichnung ist hier logarithmische Douglas-/Dirichlet-Geometrie bzw. logarithmischer Sobolev-Formraum.

Der Defekt ist

```math
N_a(v)=\langle(c_aI+C_a)v,v\rangle,
```

wobei

```math
c_a=A_a^{\rm Zhu}+2A+1,
\qquad
2A+1=\log(2\pi)+\gamma,
```

und `C_a` der selbstadjungierte Kompakt-/Hilbert-Schmidt-Korrektor mit stetigem `r''`-Kern auf dem endlichen Fenster ist.

Diese Zerlegung ist eine endliche Identität; sie ist **keine** Objekt-X-Realisierung und beweist keine Positivität außerhalb bekannter Bereiche.

---

## 8. Normalisierungs-Gate: was bereits geprüft ist und was noch zu härten ist

Ein externer 256-Bit-Arb-Gegencheck verglich für `a in {0.5,0.8,1.0}` einen polarisierten 3x3-Testblock der Realraumzerlegung mit Suzukis Fourierdarstellung. Der Mehr-Radien-Test fing einen echten Implementierungsfehler `log n` statt `Lambda(n)=log p` am Primzahlpotenzkanal `n=4` ab; nach Korrektur lagen die getesteten Residuen in den Fehlerbällen.

**Noch offene Zertifikationshärtung vor Freeze:** Das übergebene Skript berechnet `r_1''` über eine Bernoulli-Partialsumme bis `N=300`, ohne den Rest `n>300` explizit in einen Arb-Restball einzuschließen. `acb.integral` zertifiziert damit die Partialsumme, nicht automatisch die vollständige Reihe. Dieser Rest ist wegen `|u|<=2<2pi` sehr klein, muss aber explizit gebucht werden; alternativ soll `r_1''` in geschlossener Form implementiert werden. Ebenso soll der Primzahlpotenz-Cutoff ohne Float-Grenzentscheidung gehärtet werden.

Bis dahin lautet der Status:

```text
Normalisierungs-Gate: numerisch/Arb stark GREEN, vollständige Repo-Zertifikationshärtung OPEN.
```

Keine Registry-Promotion.

---

## 9. OX-GRAM-Erstmessung

Auf der extern geprüften 3-dimensionalen trigonometrischen Basis wurde das generalisierte Eigenproblem

```math
N_av=\mu\,G_a^+v
```

für `a=0.5,0.8,1.0` gemessen. In beiden Paritätssektoren blieb `mu_max<1`; die einfache Kontraktionsform ist auf diesem kleinen Unterraum daher nicht falsifiziert.

Diese Ritzwerte sind nur Untergrenzen für die oberste relative Eigenzahl des vollständigen Problems. `mu_max<1` auf einem Unterraum ist dort äquivalent zu Weil-Positivität auf diesem Unterraum und kein unabhängiger Beleg für einen kanonischen Intertwiner.

Die kleine Zahl `1-mu_max` ist eine **untere Spektrallücke**, nicht die Operatornorm von `I-W_a^*W_a`.

---

## 10. Neue operative Hauptfrage: OX-GRAM / relativer Defekt

Definiere den positiven Formraum

```math
\mathscr H_a^+
=\overline{H_0^1(-a,a)}^{\,G_a^+}
```

und die natürliche Einbettung

```math
J_a:\mathscr H_a^+\to L^2(-a,a).
```

Da die logarithmische Fourierenergie hohe Frequenzen zunehmend bestraft, ist als nächster analytischer Gate zu beweisen, dass `J_a` kompakt ist. Dann ist

```math
\boxed{A_a^{\rm rel}=J_a^*(c_aI+C_a)J_a}
```

kompakt und selbstadjungiert auf `\mathscr H_a^+`, und

```math
\boxed{
Q_{B_a}(v)=\langle(I-A_a^{\rm rel})v,v\rangle_{\mathscr H_a^+}.}
```

Damit wird die lokale Objekt-X-Frage zu einem diskreten relativen Spektralproblem:

```math
Q_{B_a}\ge0
\quad\Longleftrightarrow\quad
\lambda_{\max}(A_a^{\rm rel})\le1.
```

**Wichtig:** Diese Äquivalenz ist nur eine Reformulierung, kein Positivitätsbeweis. Objekt X wäre erst erreicht, wenn der Defekt aus der bereits vorhandenen Prime-/Douglas-Geometrie durch einen expliziten, nichtzirkulären Mechanismus erklärt bzw. faktorisiert wird.

Ein möglicher starker Zieltyp wäre ein explizit aus den Feature-Daten gebauter Kontraktor `W_a`, ohne Verwendung von RH, `B_a^{1/2}` oder des unbekannten Forminfimums, mit

```math
c_aI+C_a=\mathcal F_a^*W_a^*W_a\mathcal F_a.
```

Das ist derzeit `?[O]`.

---

## 11. Nächste Gates

In dieser Reihenfolge:

1. **CERT-HARDEN:** Bernoulli-Rest bzw. geschlossene `r_1''`-Form und Arb-sicherer Prime-Power-Cutoff im Normalisierungs-Gate.
2. **OX-COMPACT:** Kompaktheit der Einbettung `J_a` und damit des relativen Defekts `A_a^{rel}` beweisen.
3. **OX-RITZ:** verschachtelte Paritätsbasen `N=3,4,6,8,12,16,20`; oberste mehrere Ritz-Eigenwerte und zugehörige Eigenvektoren speichern, nicht nur `mu_max`.
4. **MODE-DECOMP:** den beinahe-kritischen Ritzvektor blockweise nach logarithmischer Douglas-Geometrie, Prime-Gram, Skalar `c_aI`, `r_0''`, `r_1''` zerlegen.
5. Nur falls eine robuste einzelne dominante Mode sichtbar wird: Zusammenhang mit dem AR(1)-Root/Hub untersuchen.
6. Erst danach einen kanonischen `W_a` konstruieren.

Ein robust zertifiziertes `mu>1` bei korrekter Normalisierung wäre keine gewöhnliche Architektur-Negativprobe, sondern würde einen expliziten negativen Weil-Vektor liefern und erfordert sofort einen unabhängigen zweiten Checker.

---

## 12. Ausdrücklich zurückgezogene / gesperrte Deutungen

Nicht wieder als aktive Front verwenden:

- „3/4 kauft nur Beschränktheit“ — falsch; `3/4` wird durch Weil-Diagonale + Martingalmultiplizität erzwungen.
- „PR91-Zeugenmatrix ist Rang 1“ — falsch; Rang 2 mit Rang-1-Amplitudenhülle auf sparsamer Trägermaske.
- „X_req ist fehlende Hub-Normierung“ — falsch.
- „Vier Boundary-Blöcke erklären Interior minus Baseline“ — falsch; `D_q` ist nicht unitär und cross-prime ist fensterloser Bulk/Root-Gram.
- „Cross-prime ist Boundary“ — falsch.
- „Nichtunitarität von D_q ist genau der Hub“ — zu stark/falsch; nur die passende Rang-1-Differenz stationäre vs. Dirichlet-AR-Kovarianz ist mit dem Hub verknüpft.
- „Suzuki-Basispunkt-Vierterm entfernt die lokale 2I-Masse“ — falsch auf der Nullmittelklasse.
- „Suzukis L_a ist primär ein Hadamard-Endlichteil, an den Prime-Masse gekoppelt werden soll“ — zurückgezogen; Suzuki definiert die endliche logarithmische Douglasform direkt.
- matched cutoff `epsilon=e^{-A_L}` als Objekt-X-Mechanismus — verworfen; nach Definition nur Umparametrisierung und falsche Buchungsrichtung für die Weilform.
- OX-REN/OX-REN' als aktuelle Hauptfront — entfällt zugunsten der endlichen OX-GRAM-Form.
- R-Invarianztest durch bloßes Ersetzen von `R=1` im PR97-Checker — methodisch ungültig, da aktive Primzahlen/Sektoren mit dem Radius wechseln.
- neuer R=1-Zeuge für einen 3x3-Interiorblock — ungeeignet; `k=3` ist bei `p=2,R=1` nicht Interior.

---

## 13. Verhältnis zu offenen PRs und Registry

- PR #91 bleibt ein eigener analytischer Draft und wird durch diese Konsolidierung weder reviewt noch promotet.
- Die gemergten PR #96/#97 bleiben gültige lokale Negativresultate für ihre ausdrücklich getesteten Mediator-/Feshbach-Routen; ihre Interpretation als globale Objekt-X-Hürde wird nicht erweitert.
- `ACTIVE_THEOREM_REGISTRY.md` bleibt unverändert.
- Keine Aussage dieses Dokuments ist ein RH-Beweis oder eine vollständige Objekt-X-Realisierung.

## 14. Forschungsregel ab jetzt

Ein Schritt zählt auf der Objekt-X-Hauptfront nur noch, wenn er mindestens eine der folgenden Bedingungen erfüllt:

1. konstruiert einen expliziten Teil einer gemeinsamen Gramgeometrie;
2. verkleinert die zulässige Architekturklasse durch einen echten Klassen-No-Go;
3. beweist eine notwendige Struktur des relativen Defektoperators;
4. schließt eine Normalisierungs-/Domain-/Konvergenzlücke, die für OX-GRAM tatsächlich benötigt wird.

Bloße Umschreibungen, speziell angepasste Witness-Werte oder neue Proxy-Runden ohne Bezug auf einen dieser Gates sind Nebenarbeit, nicht Hauptfront-Fortschritt.
