# P11-C1g — Labelgeometrie: Common-Target-Synthese ist positiv, kollabiert aber Primmarkierungen

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1g]`  
**Vorgänger:** P11-C1c, P11-C1f  
**Ziel:** Prüfen, ob der liftfreie Gramkern allein bereits einen tragfähigen globalen Objekt-X-Träger liefert  

**Urteil:**

\[
\boxed{[P11-C1g]\quad\checkmark[M]_{\rm part}}
\]

Die kanonische additive Synthese der zentrierten Prime-Power-Inzidenzkanäle erzeugt ohne freie Parameter eine positive nichtorthogonale Gramform. Ihr minimaler Radikalquotient/Vervollständigungsraum kollabiert jedoch die Labelinformation und ist bereits bei einem einzelnen Kanal dicht in `L^2(\mathbb R)`. Daher ist diese Common-Target-Geometrie **allein** kein geeigneter Kandidat für die markierte globale Objekt-X-Kantengeometrie.

Der neue präzise Engpass ist eine intrinsische **positive Labelgeometrie**.

---

## 1. Source-induced endliche Labelmenge

Aus C1f:

\[
F_R
=
\{\alpha=(p,m):m\log p\le2R\}.
\]

Für jedes `\alpha\in F_R`:

\[
V_\alpha
:=
\sqrt{w_\alpha}D_{\ell_\alpha},
\qquad
D_s=U_{s/2}-U_{-s/2}.
\]

Alle `V_\alpha` bilden in denselben Hilbertraum

\[
H_0=L^2(\mathbb R,du)
\]

ab.

---

## 2. Kanonische additive Synthese

Auf dem algebraischen markierten Quellenraum

\[
\mathscr E_R^{\rm alg}
:=
\bigoplus_{\alpha\in F_R}^{\rm alg}\mathcal A_{\rm PW}^{(\alpha)}
\]

definiere

\[
\boxed{
S_R((a_\alpha)_\alpha)
:=
\sum_{\alpha\in F_R}V_\alpha a_\alpha.
}
\]

Die zugehörige Gramform ist

\[
\boxed{
\mathfrak G_R(x,y)
:=
\langle S_Rx,S_Ry\rangle_{L^2}.
}
\]

Explizit:

\[
\mathfrak G_R(x,y)
=
\sum_{\alpha,\beta\in F_R}
\sqrt{w_\alpha w_\beta}
\langle D_{\ell_\alpha}a_\alpha,
D_{\ell_\beta}b_\beta\rangle.
\]

Damit werden **ohne frei gewählte Kopplungsmatrix** exakt die C1c-Off-Diagonalblöcke aktiviert.

Für jedes `x`:

\[
\mathfrak G_R(x,x)=\|S_Rx\|_2^2\ge0.
\]

Status: `✓[K/M]`.

---

## 3. Radikal und minimaler Gramabschluss

Da

\[
\mathfrak G_R(x,x)=\|S_Rx\|^2,
\]

ist

\[
\boxed{
\operatorname{Rad}(\mathfrak G_R)=\ker S_R.
}
\]

Der Radikalquotient ist isometrisch mit dem Synthesebild:

\[
\mathscr E_R^{\rm alg}/\ker S_R
\cong
\operatorname{Ran}S_R.
\]

Nach Vervollständigung:

\[
\boxed{
\overline{\mathscr E_R^{\rm alg}/\ker S_R}^{\,\mathfrak G_R}
\cong
\overline{\operatorname{Ran}S_R}^{\,L^2}.
}
\]

Das ist das allgemeine Gram-/Syntheseprinzip.

---

## 4. Dichtes Bild schon eines einzigen Inzidenzkanals

Fixiere `s>0`. Unter der P02-Fourierkonvention gilt

\[
\widehat{D_sa}(t)
=
\left(e^{-its/2}-e^{its/2}\right)\widehat a(t)
=
-2i\sin(ts/2)\widehat a(t).
\]

Der Multiplikator

\[
m_s(t)=-2i\sin(ts/2)
\]

verschwindet nur auf der diskreten Menge

\[
\frac{2\pi}{s}\mathbb Z,
\]

die Lebesgue-Maß null besitzt.

Daher hat der Multiplikationsoperator auf `L^2(\mathbb R)` trivialen adjungierten Kern. Folglich

\[
\boxed{
\overline{\operatorname{Ran}D_s}=L^2(\mathbb R).
}
\]

Da `w_\alpha>0`, gilt dasselbe für `V_\alpha`.

Somit besitzt bereits jeder nichtleere Cutoff `F_R`:

\[
\boxed{
\overline{\operatorname{Ran}S_R}=L^2(\mathbb R).
}
\]

Status: `✓[M]`.

---

## 5. Konsequenz: Labelkollaps

Die markierten Prime-Power-Komponenten

\[
\alpha=(p,m)
\]

sind im algebraischen Quellraum verschieden. Nach Quotientierung durch `\ker S_R` zählt jedoch nur noch ihre **synthetisierte Summe im selben `L^2`-Zielraum**.

Unterschiedliche markierte Familien `x,y` mit

\[
S_Rx=S_Ry
\]

werden identifiziert.

Damit verliert die minimale Common-Target-Realisierung gerade die relative Markierungsinformation, die P05 als strukturell wichtig festhält.

\[
\boxed{
\text{gemeinsames }L^2\text{-Ziel allein}
\Longrightarrow
\text{zu starker Quotient / Labelkollaps}.
}
\]

---

## 6. Zweite Firewall: P03

Der minimale Abschluss der Common-Target-Synthese ist `L^2(\mathbb R)`.

P03 zeigt jedoch, dass die vollständige Weilform auf Haar-`L^2` selbst unter RH nicht closable ist. Daher kann die obige Common-Target-Synthese nicht einfach als finale positive Vervollständigung von `B_W` identifiziert werden.

Dies ist **kein** No-Go gegen `L^2` als Analyse- oder Zwischenraum; nur gegen die Gleichsetzung

\[
\boxed{
\text{minimaler Common-Target-Gramraum}=\mathcal K_X\text{ mit Weilformabschluss}.
}
\]

---

## 7. Warum der Gramkern trotzdem wichtig bleibt

Der Befund aus C1c bleibt vollständig gültig:

\[
G_{\alpha\beta}(a,b)
=
\langle V_\alpha a,V_\beta b\rangle
\]

ist ein kanonischer liftfreier positiver Überlappungskern.

C1g zeigt nur:

\[
\boxed{
G\text{ liefert die Überlappungsgeometrie, aber noch nicht die richtige Label-Hilbertisierung.}
}
\]

---

## 8. Allgemeine positive Labelgeometrie

Um Labels zu erhalten und zugleich nichtorthogonale Kreuzblöcke zuzulassen, führe abstrakt einen Label-Hilbertraum `K_R` mit Vektoren

\[
\xi_\alpha\in K_R,
\qquad\alpha\in F_R,
\]

ein.

Setze

\[
\boxed{
c_{\alpha\beta}:=\langle\xi_\alpha,\xi_\beta\rangle_{K_R}.}
\]

Dann ist

\[
C_R=(c_{\alpha\beta})_{\alpha,\beta\in F_R}\ge0.
\]

Erweiterte Kanäle:

\[
\boxed{
\widetilde V_\alpha a
:=
V_\alpha a\otimes\xi_\alpha
\in
L^2(\mathbb R)\otimes K_R.
}
\]

Kreuzblöcke:

\[
\boxed{
\widetilde G_{\alpha\beta}(a,b)
=
c_{\alpha\beta}
G_{\alpha\beta}(a,b).
}
\]

Für beliebige markierte Daten `(a_\alpha)` gilt automatisch

\[
\sum_{\alpha,\beta}
\widetilde G_{\alpha\beta}(a_\alpha,a_\beta)
=
\left\|
\sum_\alpha V_\alpha a_\alpha\otimes\xi_\alpha
\right\|^2
\ge0.
\]

Damit parametrisiert ein positiver Label-Gramkern `C_R` exakt eine Klasse positiver nichtorthogonaler markierungserhaltender Erweiterungen.

---

## 9. Zwei Grenzfälle

### Orthogonale Labels

\[
c_{\alpha\beta}=\delta_{\alpha\beta}.
\]

Dann bleiben alle Labels erhalten, aber es gibt keine echten Off-Diagonalblöcke.

### Vollständiger Labelkollaps

\[
c_{\alpha\beta}=1.
\]

Dann sind alle `\xi_\alpha` identisch; dies reproduziert die Common-Target-Synthese aus §2 und besitzt Rang eins in der Labelgeometrie.

Damit liegt der gesuchte Objekt-X-Typ strukturell **zwischen** diesen Extremen:

\[
\boxed{
I\neq C_R\neq\mathbf 1\mathbf 1^* 
}
\]

im qualitativen Sinn: nicht vollständig orthogonal, aber auch nicht vollständig identifiziert.

Dies ist keine Behauptung, dass jede Lösung diese endliche Matrixung exakt verwendet; es ist der finite Gram-Prototyp.

---

## 10. Der neue Kernengpass

Die Positivität von `C_R` allein ist trivial zu erzwingen und daher **kein** Kriterium für Kanonizität.

Gesucht ist eine arithmetisch/adelisch intrinsische Bestimmung

\[
\boxed{
C_R^{\rm can}
=(c_{\alpha\beta}^{\rm can})
}
\]

mit mindestens:

1. source-induced Cutoff-Kompatibilität `R<S`;
2. Involutionskompatibilität;
3. voller Prime-Power-Struktur;
4. Nichtorthogonalität ohne Labelkollaps;
5. keine Nullstellendaten/RH als Eingabe;
6. Kompatibilität mit P05-relativer Kantenmarkierung;
7. Kompatibilität mit der exakten Weilkompression/Restarchitektur.

---

## 11. Symmetrie allein selektiert `C_R` nicht

Alle `D_s` sind aus demselben abelschen Translationsfluss gebaut und kommutieren mit globalen Translationen in dem Sinn

\[
D_sU_r=U_rD_s.
\]

Daher bleibt jede feste Labelmatrix `C_R` mit der gemeinsamen Translationswirkung kompatibel.

\[
\boxed{
\text{Der Skalierungs-/Translationsfluss allein kann die Labelkopplung nicht kanonisieren.}
}
\]

Weitere arithmetische/korrespondenzielle Daten sind notwendig.

Status: `✓[M]` als Symmetrie-Firewall.

---

## 12. Statusmatrix

| Aussage | Status |
|---|---|
| additive Common-Target-Synthese `S_R` kanonisch definiert | `✓[K/M]` |
| ihre Gramform aktiviert C1c-Off-Diagonalblöcke | `✓[K/M]` |
| `Rad G_R=ker S_R` | `✓[M]` |
| `closure Ran D_s=L^2` für `s>0` | `✓[M]` |
| minimaler Common-Target-Gramabschluss bei `F_R\neq\emptyset` ist `L^2` | `✓[M]` |
| diese Minimalrealisierung erhält Prime-Power-Markierungen | `×[M]` |
| diese Minimalrealisierung allein ist finaler `K_X`-Weilabschluss | `×[M]` im P03/P05-Scope |
| positive markierungserhaltende Erweiterung via Label-Gramkern `C_R` | `✓[M]` abstrakt |
| `C_R=I` liefert echte Off-Diagonalität | `×[M]` |
| `C_R=11^*` erhält Labelinformation | `×[M]` |
| Translationssymmetrie selektiert `C_R` eindeutig | `×[M]` |
| kanonischer arithmetischer Label-Gramkern | `?[O]` |

---

## 13. Wichtigster P11-Befund nach C1g

Der gesuchte globale Mischblock ist jetzt auf drei Ebenen zerlegt:

\[
\boxed{
\underbrace{G_{\alpha\beta}}_{\text{analytische Überlappung: konstruiert}}
\times
\underbrace{c_{\alpha\beta}}_{\text{Labelgeometrie: offen}}
\longrightarrow
\underbrace{\widetilde G_{\alpha\beta}}_{\text{globale markierte Kreuzgeometrie}}.
}
\]

Die analytische Überlappung ist nicht länger der Hauptengpass. Der offene Kern ist die **arithmetische Gramgeometrie der Prime-Power-Labels**.

---

## 14. Nächster Knoten

\[
\boxed{[P11\text{-}C1h]\quad\text{Welche im Repo vorhandene arithmetische Struktur kann }C_R^{\rm can}\text{ erzeugen?}}
\]

Zu auditieren sind gezielt:

- relative Primkanten-/Korrespondenzstruktur aus P05;
- Wres-Paarung und ihre Provenienzfirewall;
- BC-Multiplikation/Prime-Power-Komposition aus P01/P09;
- gegebenenfalls Divisorgraph-/Feshbach-Inzidenz aus P06;

unter der strikten Regel: keine frei angepasste PSD-Matrix.
