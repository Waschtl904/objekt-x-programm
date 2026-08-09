# P06 — Jacobi–Feshbach and Divisor Graph

**Status:** SYN PRIMARY AUDITED — unabhängiger SYN-Zweitcheck ausständig  
**Datum:** 9. August 2026  
**Pass-A-Basis:** Gruppe G `P06 PASS A COMPLETE — doppelt geprüft`, `PASS-A-PROTOKOLL.md`, Commit `e32cfecb`; rein technischer Notationsfix `5bd6ff06`  
**Primärreconciliation:** `audits/AUDIT-2026-08-09_P06_PassA_Primaerreconciliation.md`, Commit `3e9b816d`  
**Targeted-Reaudits:** G-T1 `fbff73d9`, G-T2 `2b6cb2e8`, G-T3 `d8746ea1`, G-T4 `52197cdd`, G-T5 `dd0fd3a3`  
**Unabhängiger Pass-A-Zweitcheck:** `audits/AUDIT-2026-08-09_P06_PassA_Zweitcheck_Pfadgebunden.md`, Commit `b40af085`; Urteil `OHNE KONKRETEN GEGENBEFUND`  
**P06-SYN-Primärcheck:** `audits/AUDIT-2026-08-09_P06_SYN_Primaercheck.md`, Commit `b077a814`; zwei lokale Draft-Korrekturen angewendet, kein verbleibender Gegenbefund  

> Dieses SYN-Paper enthält ausschließlich den nach Gruppe G gültigen Endstand. Historische Jacobi-/Feshbach-Fehlversuche werden nur soweit erwähnt, wie sie eine heute verbindliche Firewall oder einen modellbezogenen No-Go-Befund begründen. `PASS A COMPLETE` ist eine Audit-/Migrationsaussage und löst keine offenen Lift-, Gram-, Schatten- oder Objekt-X-Probleme.

---

## Abstract

Wir konsolidieren die Jacobi–Feshbach- und Divisorgraph-Schicht des Objekt-X-Programms. Die robuste Struktur besteht aus endlichen Schur-/Feshbach-Identitäten, Weyl-/Stieltjes-Resolventenmatrixelementen, einer kollektiven Birman–Schwinger-Blockarchitektur und einer endlichen Trace-Geometrie geschlossener Divisorpfade. Die spätere Spektralanalyse ändert jedoch die Interpretation grundlegend: Der relative Generator $D_{\rm rel}$ ist in den auditierten Primfasern ein Transportgenerator mit rein absolutstetigem Spektrum, nicht der gesuchte diskrete Hilbert–Pólya-Endoperator. Diskrete historische Eigenbasisformeln werden daher durch projektionswertige Kreuzspektralmaße ersetzt. Primkanalbilder können generisch überlappen, ohne dass jedes Kreuzpaar nichtverschwindend sein muss. Endliche Feshbach-Identitäten liefern keine Schattennormkontrolle eines globalen Grenzoperators. Schließlich kollabiert die konkrete NEU-088–90-Mangoldt-/Orbit-/Resolvent-Skalierung auf der pathwise Skala: $T_N(z)\to0$, $\|C_N(z)\|_{HS}\to0$ und $D_N(z)\to1$. Dieser Befund widerlegt den historischen nichttrivialen Determinantenlimes, ist aber kein allgemeiner Feshbach-No-Go. Die intrinsische Lift-/Gramgeometrie und damit die globale Schatten-/Fredholmrealisierung bleiben nach P11 geroutet.

---

## §1 — Typisierte Feshbach- und Birman–Schwinger-Architektur

### Def. 1.1 — Kollektiver Transfer

Sei $D_{\rm rel}$ ein selbstadjungiert realisierter relativer Transportgenerator auf dem jeweils zugelassenen Hilbertraum und seien $V_p$ typisierte Primkanalabbildungen. Für endlichen Primcutoff $N$ bezeichnet

$$
\boxed{
V_N:=\sum_{p\le N}V_p
}
$$

formal den kollektiven Koppler beziehungsweise Zeilenoperator, sobald die beteiligten Quell- und Zieltypen eine solche Summe zulassen. Das Symbol bezeichnet **keine orthogonale Direktsumme der Zielbilder**. Für $z\in\mathbb C\setminus\mathbb R$ wird die Birman–Schwinger-/Feshbach-Blockarchitektur geschrieben als

$$
\boxed{
\mathcal K_N(z)
:=V_N^*(D_{\rm rel}-z)^{-1}V_N,
}
$$

mit Kreuzblöcken

$$
\boxed{
K_{pq}(z)
:=V_p^*(D_{\rm rel}-z)^{-1}V_q.
}
$$

Diese Formeln sind Operatorarchitektur unter den angegebenen Typ- und Domainvoraussetzungen; sie konstruieren noch keinen intrinsischen globalen Objekt-X-Koppler.  
[G-T1/GX1: `INCORPORATED_part / RECONCILED`]

### Satz 1.2 — Primblockdiagonalität ist nicht strukturell erzwungen

Aus der Primkanalgeometrie folgt nicht

$$
\mathcal K_N(z)=\bigoplus_{p\le N}K_{pp}(z).
$$

Verschiedene Primkanalbilder können im Zielraum überlappen, sodass Kreuzblöcke **generisch** auftreten können. Nicht bewiesen ist jedoch die stärkere Aussage

$$
K_{pq}(z)\neq0
\qquad\text{für jedes }p\neq q.
$$

Der Mechanismus ist Kanalbildüberlappung beziehungsweise ein nichttriviales Kreuzspektralmaß; eine Primmischung durch $D_{\rm rel}$ selbst ist dafür nicht erforderlich.  
[G-T1 / NEU-226–227: `✓[M]_{part}`]

### Firewall 1.3 — Festes $N$ bedeutet nicht endlichen Rang

Auch bei festem Primcutoff besitzen die Primkanäle unendliche interne Indizes. Daher ist eine pauschale Buchung

$$
\operatorname{rank}\mathcal K_N\le\pi(N)
$$

nicht zulässig.  
[NEU-226: `✓[M]_{neg}` gegen die historische Rangannahme]

---

## §2 — Spektralendstand des relativen Generators

### Satz 2.1 — Transportnatur in den auditierten Primfasern

Für die auditierten Primfasern gilt bis auf die verbindliche Transportnormalisierung

$$
\boxed{
D_{\rm rel}\big|_{\mathcal H_{p,a}}
\cong
2i\kappa_p^{\rm tr}\frac d{dt}
}
$$

auf $L^2(\mathbb R)$-Komponenten. Daraus folgen in diesem Primfaser-Scope:

- rein absolutstetiges Spektrum;
- kein Kern;
- kein kompakter reduzierter Resolvent.

Damit ist $D_{\rm rel}$ in dieser Rolle ein Transport-/Streugenerator und nicht der diskrete Hilbert–Pólya-Endoperator. Dies schließt einen anderen, erst später aus der globalen Objekt-X-Struktur hervorgehenden selbstadjungierten Endoperator nicht aus.  
[NEU-225; Gruppe G: `✓[M]` im Primfaser-Scope]

### Satz 2.2 — Projektionswertige Kreuzspektralmaßform

Sei $E_D$ das projektionswertige Spektralmaß von $D_{\rm rel}$. Für geeignete Kanalvektoren $a,b$ definiert man

$$
\mu_{pq}^{a,b}(B)
:=
\langle V_pa,E_D(B)V_qb\rangle.
$$

Dann gilt

$$
\boxed{
\langle a,K_{pq}(z)b\rangle
=
\int_{\mathbb R}
\frac{d\mu_{pq}^{a,b}(\lambda)}{\lambda-z}.
}
$$

Diese Stieltjesdarstellung ist die verbindliche Spektralsprache für die Kreuzblöcke.  
[NEU-227: `✓[K/M]`]

### Firewall 2.3 — Keine diskrete Eigenbasis aus NEU-051

Die historischen Formeln NEU-051 (51.3), (51.4), (51.7), die eine diskrete Eigenbasis

$$
D_{\rm rel}\eta_\alpha=\lambda_\alpha\eta_\alpha
$$

voraussetzen, sind `SUPERSEDED`. Der Spektralsatz selbst ist davon nicht betroffen; ersetzt wird nur die unzulässige diskrete Darstellung durch Satz 2.2.

### Offen 2.4 — Zusammengesetzte Sektoren

Für nichtprime Sektoren können mehrere Teiler-Sprünge die $u$-Restklassen mischen. Die globale Spektralaussage aus Satz 2.1 darf daher nicht ohne Zusatzbeweis auf sämtliche zusammengesetzten Sektoren extrapoliert werden.  
[`[O-225-3]`: `?[O]`]

---

## §3 — Normalisierung des antisymmetrischen Jacobi-Anteils

### Def. 3.1 — Verbindliche Typtrennung

Für den historischen Jacobi-Operator $\Theta_N$ werden zwei verschiedene Operatoren unterschieden:

$$
\boxed{
J_N^-:=\frac12(\Theta_N-\Theta_N^\dagger),
}
$$

$$
\boxed{
S_N:=\frac1{2i}(\Theta_N-\Theta_N^\dagger)=-iJ_N^-.
}
$$

$J_N^-$ ist schiefadjungiert; $S_N$ ist die zugehörige selbstadjungierte Version. Insbesondere

$$
J_N^-\neq S_N.
$$

[G-T2: `✓[M]` als Typ-/Normierungskorrektur]

### Firewall 3.2 — Keine intrinsische $\gamma_N=1$-Rigidität

Die Wahl

$$
\gamma_N\equiv1
$$

ist zulässig, falls $\gamma_N$ tatsächlich ein freier Modellparameter ist. Der P06-Quellenstand beweist jedoch nicht, dass die intrinsische Objekt-X-Struktur diese Normalisierung erzwingt. Historische Aussagen, der entsprechende Weg sei „vollständig geschlossen“, werden nicht migriert.  
[G-T2: `SUPERSEDED_part / OPEN`]

---

## §4 — Divisorgraph und endliche Trace-Geometrie

### Def. 4.1 — Geschlossene Pfade

Für eine endliche gewichtete Matrix $A_N$ auf einem Divisor-/Kantengraphen besitzt

$$
\operatorname{Tr}(A_N^k)
$$

die übliche Interpretation als gewichtete Summe geschlossener Pfade der Länge $k$.

### Satz 4.2 — Erste zwei Spuren

Ist $A_N$ rein off-diagonal, so gilt

$$
\operatorname{Tr}(A_N)=0.
$$

Ist $A_N$ zusätzlich selbstadjungiert und endlich, dann

$$
\boxed{
\operatorname{Tr}(A_N^2)=\|A_N\|_{HS}^2.
}
$$

[G-T3: `✓[M]`]

### Satz 4.3 — Von-Mangoldt-Gewicht ist nicht logarithmische Weglänge

Für Primzahlpotenzen $p^k$ mit $k>1$ gilt

$$
\boxed{
\log(p^k)=k\log p
\neq
\Lambda(p^k)=\log p.
}
$$

Eine Graphgewichtung durch logarithmische Gesamtwegstrecke darf daher nicht mit der von-Mangoldt-Gewichtung identifiziert werden.  
[G-T3: `✓[M]`]

### Satz 4.4 — Ungerade Spuren: $r$-Gradierung reicht nicht

Eine bloße $r$-Gradierung impliziert nicht

$$
\operatorname{Tr}(A_N^{2j+1})=0
\qquad\forall j\ge0.
$$

Eine robuste strukturelle Zusatzbedingung, die ungerade geschlossene Pfade ausschließt und damit die entsprechenden ungeraden Spuren zum Verschwinden bringt, ist echte Bipartitheit des symmetrisierten Graphen.  
[G-T3: `✓[M]`]

### Firewall 4.5 — Historische konkrete Normalisierung nicht kanonisch

Eine alte konkrete Formel vom Typ

$$
\operatorname{Tr}(A_N^2)
=\sum r^2\log^2n
$$

wird nicht als kanonische P06-Normalisierung übernommen, solange sie nicht mit der verbindlichen $J_N^-/S_N$-Konvention neu eingesetzt ist.  
[G-T3: `NORMALIZATION-SUPERSEDED_part`]

---

## §5 — Endliche Feshbach-Identität und Grenzfirewall

### Satz 5.1 — Endliche Schur-/Feshbach-Grammatik

Die in NEU-077 verwendete endliche Schur-/Feshbach-Kollapsidentität bleibt im typisierten endlichen Matrixmodell algebraisch gültig. P06 übernimmt sie als endliche Identität, nicht als bereits vollzogenen globalen Operatorgrenzwert.  
[G3/GX1: `✓[M]`]

### Firewall 5.2 — Endlich bedeutet nicht Schattennormlimes

Der historische Grenzübergang ist nur punktweise beziehungsweise stark auf geeigneten endlich getragenen Vektoren kontrolliert. Daraus folgt keine Operatornorm-, Hilbert–Schmidt- oder Spurklassennormkonvergenz des globalen Transfers.

$$
\boxed{
\text{endliche Feshbachidentität}
\neq
\text{Schattennorm-kontrollierter Grenzoperator}.
}
$$

[NEU-077/226–227: `✓[M]` als Firewall]

### Def. 5.3 — Zwei Trunkierungsskalen

Die historische Skalierungsanalyse trennt die pathwise Skala

$$
M_N^{\rm path}\lesssim\frac{N}{\log N}
$$

von der strengeren Operatorstabilitätsskala

$$
M_N^{\rm op}
\lesssim
\sqrt{\frac{N}{\log N}}.
$$

Diese beiden Rollen dürfen nicht identifiziert werden.  
[NEU-084; Gruppe G: `INCORPORATED_part`]

### Befund 5.4 — Vorwärtsshift und Jacobi-Schließung

Ein reiner Vorwärtsshift ist nilpotent und für endliche Spur-/Determinantenfragen trivial. Erst die selbstadjungierte Jacobi-Schließung erzeugt Rückkanten und damit nichttriviale endliche Schleifen. Zugleich kollabiert der stark normierte Mangoldt-Vorwärtsshift auf festen Vektoren. Diese Befunde motivieren, aber beweisen keinen globalen Grenzoperator.

---

## §6 — Korrigierte relative Schleifenanalyse

### Def. 6.1 — Zweite Schleifenspur

Im konkreten NEU-088–90-Modell mit

$$
M_N=\frac{N}{\log N}
$$

tritt die zweite relative Schleifenspur in der Form

$$
T_N(z)
=
\frac{2\gamma^2}{N^2}
\sum_{r\le M_N}r^2
\sum_{n\le N-r}
\frac{\Lambda(n)^2}{(r-z)(r+n-z)}
$$

auf.

### Satz 6.2 — Der historische nichttriviale Grenzwert ist falsch

Die früher benutzte uniforme Asymptotik

$$
\sum_{n\le N-r}
\frac{\Lambda(n)^2}{r+n}
\sim
\frac12\log^2N
$$

ist nicht gleichmäßig bis $r=N/\log N$ zulässig. Mit

$$
A(x):=\sum_{n\le x}\Lambda(n)^2=O(x\log x)
$$

und der getrennten Summenabschätzung folgt für festes zulässiges $z$

$$
\boxed{
T_N(z)
=O_z\!\left(\frac{\log\log N}{\log N}\right)
\longrightarrow0.
}
$$

Damit ist der historische Grenzwert $\gamma^2/2$ `×[M]`.  
[G-T4: korrigierter Nullgrenzwert `✓[M]` im Modellscope]

### Def. 6.3 — Symmetrisierter Resolventenblock

Setze im selben endlichen Modell

$$
C_N(z)
:=
R_N(z)^{1/2}B_N^\Lambda R_N(z)^{1/2}.
$$

Für komplexes $z$ ist $C_N(z)$ im Allgemeinen **nicht** selbstadjungiert. Daher gilt nicht allgemein

$$
\|C_N(z)\|_{HS}^2
=
\operatorname{Tr}(C_N(z)^2).
$$

Korrekt ist

$$
\boxed{
\|C_N(z)\|_{HS}^2
=
\operatorname{Tr}(C_N(z)^*C_N(z)).
}
$$

[G-T5: historische Selbstadjungiertheits-/HS-Gleichsetzung `×[M]`]

### Satz 6.4 — Hilbert–Schmidt-Kollaps

Die betragspositive Matrixabschätzung liefert

$$
\boxed{
\|C_N(z)\|_{HS}^2
=O_z\!\left(\frac{\log\log N}{\log N}\right)
\longrightarrow0.
}
$$

Somit auch

$$
\|C_N(z)\|\to0.
$$

Für jedes feste $k\ge3$ gilt

$$
|\operatorname{Tr}(C_N(z)^k)|
\le
\|C_N(z)\|^{k-2}\|C_N(z)\|_{HS}^2
\longrightarrow0.
$$

Auch der zweite Schleifenterm verschwindet.  
[G-T5: `✓[M]` im Modellscope]

### Korollar 6.5 — Kollaps der konkreten relativen Determinante

Da der lineare Term wegen der off-diagonalen Struktur verschwindet,

$$
\operatorname{Tr}(B_NR_N(z))=0,
$$

folgt im konkreten endlichen NEU-088–90-Modell

$$
\boxed{
\log D_N(z)\to0,
\qquad
D_N(z)\to1.
}
$$

Damit erzeugt diese konkrete Mangoldt-/Orbit-/Resolvent-Skalierung keinen nichttrivialen $C\xi(z)$-Grenzwert.  
[G-T5: `✓[M]` im Modellscope]

### Firewall 6.6 — Kein allgemeiner Feshbach-No-Go

Korollar 6.5 ist **kein** No-Go gegen

- anders skalierte oder renormierte relative Determinanten;
- einen globalen Transfer $V^*(D_{\rm rel}-z)^{-1}V$ nach intrinsischer Quellkonstruktion;
- eine $\det_2$-/Weil-Schicht in anderer Hilbertisierung.

Der Befund ist modell- und skalenspezifisch.

---

## §7 — Weyl-/Stieltjes- und Determinanteninterface

### Satzschema 7.1 — Weyl-/Herglotz-Sprache

Resolventenmatrixelemente und die Stieltjesdarstellung aus Satz 2.2 liefern die korrekte analytische Sprache für die P06-Kreuzblöcke. Endliche Weyl- und Determinantenquotienten bleiben unter ihren Typ-, Selbstadjungiertheits- und Holomorphievoraussetzungen gültige Bausteine.  
[NEU-063/064, NEU-046/049: `INCORPORATED_part`]

### Offen 7.2 — Arithmetische Divisoridentifikation

Eine globale Identifikation des resultierenden Weyl-/Determinantenobjekts mit der Riemannschen $\xi$-Funktion ist nicht bewiesen. Insbesondere bleiben Aussagen vom Typ

$$
Z_N(z)\longrightarrow C\,\xi(z)
$$

`?[O]` beziehungsweise `CONDITIONAL`.  
[NEU-065; Gruppe G Firewall 11]

### Befund 7.3 — Primitive Orbit- und Divisorgraph-Schicht

Die endliche Divisorgraph-Grammatik, primitive Orbit-/Möbiusmechanismen und primitive Zykluszerlegungen aus NEU-067–069 bleiben als endliche kombinatorische Bausteine erhalten. Die naiven Ihara-/Periodisierungsrouten NEU-070/071 liefern dagegen keinen kanonischen Zeta-Anschluss und werden nur als negative Richtungsdiagnose erinnert.

---

## §8 — Schattenkriterien und P06/P11-Grenze

### Firewall 8.1 — Keine Schattenrechnung vor intrinsischer Quelle

Die spätere Liftanalyse zeigt, dass der globale Quellhilbertraum, die Liftunabhängigkeit und die Gramgeometrie noch nicht intrinsisch abgeschlossen sind. Deshalb darf P06 zwar konditionale Schattenkriterien für

$$
K(z)=V^*(D_{\rm rel}-z)^{-1}V
$$

formulieren, aber keine globale Schattenklasse als bereits konstruierten Objekt-X-Satz ausgeben.

### Befund 8.2 — $\mathcal S_2/\mathcal S_4$-Firewall

Der Quellenstand sichert lediglich: Für den vorgeschlagenen Nicht-$\mathcal S_1$-Zeugenmechanismus muss $V\notin\mathcal S_2$ gelten. Die stärkere Arbeitshypothese

$$
V\in\mathcal S_4\setminus\mathcal S_2
$$

ist durch den P06-Quellenkegel nicht bewiesen.  
[NEU-227: `✓[M]` für die Notwendigkeit im Zeugenmechanismus; $\mathcal S_4$-Teil `?[O]`]

### Satz 8.3 — Bedeutung des $u$-Parameters

Der historische sogenannte $u$-Regulator ist keine freie Regularisierungszahl. Verbindlich ist

$$
\boxed{
u\text{-Parameter}=\text{Hebungswahl innerhalb der Primfaser}.
}
$$

Die kanonische Wahl $u=0$ kann gerade die Kopplung vernichten. Schattenverhalten darf daher nicht durch freies Tuning von $u$ postuliert werden.  
[NEU-228: `✓[M]` als Typ-/Rollenklärung]

### Sperrvermerk 8.4 — Routing nach P11

Folgende Punkte gehören nicht als gelöste P06-Konstruktionen in dieses Paper:

- intrinsische Liftunabhängigkeit;
- Quellhilbertisierung;
- Gramoperator der überlappenden Kanalbilder;
- intrinsischer Mischblock $\beta_p$;
- globale nichtorthogonale Kopplungsgeometrie;
- daraus abgeleitete globale Fredholm-/Schattenrealisierung.

Sie werden nach P11 geroutet. NEU-228b/229 dürfen in P06 nur als Blocker/Interface zitiert werden.  
[Gruppe G / P06-P11-Firewall]

---

## §9 — Kanonische P06-Firewall-Liste

Für die weitere SYN-Migration gelten verbindlich:

1. $J_N^-\neq S_N$; $J_N^-=\frac12(\Theta_N-\Theta_N^\dagger)$ und $S_N=-iJ_N^-$.
2. $D_{\rm rel}$ ist in den auditierten Primfasern Transportgenerator, nicht der diskrete HP-Endoperator.
3. Diskrete NEU-051-Eigenbasisformeln sind `SUPERSEDED`; Kreuzspektralmaße sind verbindlich.
4. Primblockdiagonalität ist nicht strukturell erzwungen; universelles $K_{pq}\neq0$ ist nicht bewiesen.
5. Kreuzblöcke entstehen aus Kanalbildüberlappung, nicht notwendigerweise aus Primmischung durch $D_{\rm rel}$.
6. Festes $N$ impliziert keinen endlichen Rang von $\mathcal K_N$.
7. Endliche Feshbachidentität impliziert keine Schattennormkonvergenz.
8. $u$ ist Liftkoordinate/Hebungswahl, kein freier Regulator.
9. Globale Schatten-/Fredholmrealisierung bleibt bis zur intrinsischen Lift-/Gramgeometrie blockiert.
10. Zusammengesetzte Sektoren bleiben `[O-225-3]` offen.
11. $Z_N\to C\xi$ und entsprechende Divisoridentifikationen bleiben `?[O]` / `CONDITIONAL`.
12. Endliche Graphtrace-Geometrie ist keine diskrete Spektralzerlegung von $D_{\rm rel}$.
13. Selbstadjungiertheit von $C_N(z)$ für komplexes $z$ ist im Allgemeinen falsch.
14. Im konkreten NEU-088–90-Scaling gilt $T_N(z)\to0$ und $D_N(z)\to1$.
15. Dieser Determinantenkollaps ist kein globaler Feshbach-No-Go.

---

## §10 — Status- und Provenienzmatrix

| Baustein | Status für P06-SYN | Herkunft |
|---|---|---|
| endliche Schur-/Feshbach-Identität | `✓[M]` im endlichen typisierten Modell | NEU-040/045/077, GX1/G3 |
| Weyl-/Stieltjes-Resolventensprache | `INCORPORATED_part` | NEU-046/063/064/227 |
| kollektive Blockarchitektur $K_{pq}$ | `INCORPORATED_part / RECONCILED` | NEU-050, G-T1 |
| generische Kanalbildüberlappung | `✓[M]_{part}` | NEU-226/227, G-T1 |
| universelles $K_{pq}\ne0$ für alle $p\ne q$ | nicht bewiesen | G-T1 |
| Transportnatur von $D_{\rm rel}$ in Primfasern | `✓[M]` | NEU-225 |
| projektionswertige Kreuzspektralmaßform | `✓[K/M]` | NEU-227 |
| diskrete Eigenbasisform NEU-051 | `SUPERSEDED` | NEU-225/227 |
| $J_N^- / S_N$-Typtrennung | `✓[M]` | G-T2 |
| endliche Divisorpfad-/Trace-Geometrie | `✓[M]` | G-T3 |
| $\log(p^k)\ne\Lambda(p^k)$, $k>1$ | `✓[M]` | G-T3 |
| endliche Feshbachidentität $\Rightarrow$ globaler Schattenlimes | nicht zulässig | NEU-077/226/227 |
| $T_N(z)\to\gamma^2/2$ | `×[M]` | G-T4 |
| $T_N(z)\to0$ auf $N/\log N$ | `✓[M]` im NEU-088–90-Modell | G-T4 |
| $C_N(z)$ selbstadjungiert für komplexes $z$ | `×[M]` | G-T5 |
| $\|C_N(z)\|_{HS}\to0$ | `✓[M]` im NEU-088–90-Modell | G-T5 |
| $D_N(z)\to1$ | `✓[M]` im NEU-088–90-Modell | G-T5 |
| allgemeiner Feshbach-No-Go | nicht bewiesen / ausdrücklich nicht behauptet | G-T5 |
| zusammengesetzte Sektoren | `?[O]` | `[O-225-3]` |
| $V\in\mathcal S_4\setminus\mathcal S_2$ | strukturelle Arbeitshypothese / `?[O]` | NEU-227 |
| intrinsische globale Lift-/Gram-/Mischblockgeometrie | nach P11; offen/Quellenblocker | NEU-228b/229 |
| $Z_N\to C\xi$ | `?[O] / CONDITIONAL` | NEU-065 |

---

## §11 — Schlussbild

Der P06-Endstand ist weder ein Jacobi-Beweis der Riemannschen Vermutung noch ein Feshbach-No-Go. Er liefert vielmehr ein präzises Operator- und Kombinatorik-Interface:

$$
\boxed{
\text{endliche Divisorpfade}
\;\longleftrightarrow\;
\text{Schur/Feshbach}
\;\longleftrightarrow\;
\text{Weyl/Stieltjes-Kreuzspektralmaße},
}
$$

unter drei entscheidenden Grenzen:

$$
\boxed{
\text{Transport} \neq \text{HP-Endoperator},
\qquad
\text{endlich} \neq \text{Schattenlimes},
\qquad
\text{P06} \neq \text{intrinsische globale Gramgeometrie}.
}
$$

Die konkrete historische Schleifenskalierung ist nach G-T4/G-T5 vollständig diagnostiziert und kollabiert auf $D_N(z)\to1$. Der nächste mathematische Anschluss liegt daher nicht in einer Wiederbelebung dieses Determinantenlimits, sondern in der späteren intrinsischen Quell-/Gramkonstruktion und einer gegebenenfalls neu skalierten globalen Feshbach-/Fredholmarchitektur.

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, 2026-08-09.*
