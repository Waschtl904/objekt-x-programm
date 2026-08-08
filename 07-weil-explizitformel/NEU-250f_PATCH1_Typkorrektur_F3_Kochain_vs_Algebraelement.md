# NEU-250f Patch 1 — Typkorrektur: $F^3$-Kochain versus Algebraelement

**Datum:** 8. August 2026  
**Bezug:** NEU-250f, Commit `ada2f955`  
**Prüfart:** `TARGETED-REAUDIT` aufgrund eines konkreten Typkonflikts im P05/Pass-A-Reconciliation  
**Status:** Der unbedingte Filtrations-No-Go aus NEU-250f wird **SUPERSEDED**; die filtrationsmäßige Implikation bleibt als konditionaler Satz gültig.

---

## 1. Anlass

NEU-250f schließt aus dem Quellenbeleg aus NEU-019

\[
L_3\in C^4\!\left(F^3A_{\rm BC}^{\rm an},F^3A_{\rm BC}^{\rm an}\right)
\]

auf

\[
L_3^\circ\in F^3A_{\rm BC}^{\rm an},
\]

und verwendet anschließend eine Fourier-Monoidentwicklung

\[
L_3^\circ=\sum_{s,m}\ell_{s,m}e_sV_m.
\]

Dieser Schluss ist ohne zusätzliche Auswertungs- oder Realisierungsabbildung typologisch nicht zulässig.

Ein Element von

\[
C^4(A,A)
\]

ist ein Hochschild-Kochain (eine mehrlineare Abbildung mit Werten in $A$), nicht selbst ein Element von $A$. Aus der Wertebereichsangabe folgt nur:

\[
L_3(a_1,\dots,a_4)\in F^3A_{\rm BC}^{\rm an}
\]

für typzulässige Eingaben. Sie liefert keinen kanonischen standalone-Vektor $L_3^\circ\in F^3A$.

Status:

\[
\boxed{L_3\in C^4(F^3A,F^3A)\Longrightarrow L_3^\circ\in F^3A}
\qquad \times[M]\ \text{ohne zusätzliche Typbrücke.}
\]

---

## 2. Abgleich mit dem bereits auditierten Typfundament

NEU-170d und NEU-173 hatten den betreffenden Typkegel bereits bereinigt:

- Im auditierten Quellenkegel ist kein vollständiges Tupel
  \((B_3,M,C^\bullet,b,L_3,\rho_{\rm op})\) konstruiert.
- Insbesondere fehlt eine Realisierungsabbildung

\[
\rho_{\rm op}:Z^4(B_3,M)\longrightarrow A_{\rm BC}^{\rm an}
\quad\text{oder}\quad
\rho_{\rm op}:Z^4(B_3,M)\longrightarrow\operatorname{End}(\mathcal H),
\]

welche den Kochain-/Klassenrepräsentanten in den in NEU-41 ff. verwendeten Algebra-/Operatorraum überführt.
- Die Substitution eines abstrakten $L_3$ als Algebraelement war deshalb bereits als Typblockade erkannt.

NEU-250f darf diese Firewall nicht durch die bloße Wertebereichsangabe $C^4(F^3A,F^3A)$ umgehen.

---

## 3. Was aus der Filtration tatsächlich folgt

Die Filtrationsrechnung in NEU-250f ist **nach erfolgter Typisierung** korrekt.

Nach NEU-025 gilt

\[
F^3A_{\rm BC}^{\rm an}
=\overline{\operatorname{span}}\{e_rV_n:\Omega(n)\ge3\}.
\]

Daher gilt für jedes konkret gegebene Algebraelement

\[
X\in F^3A_{\rm BC}^{\rm an},
\qquad
X=\sum_{s,m}x_{s,m}e_sV_m,
\]

notwendig

\[
x_{s,1}=0\qquad\forall s,
\]

weil $\Omega(1)=0<3$.

Damit ist der korrekte Satz:

> **Konditionaler Filtrationssatz.** Ist ein konkreter, für die Rohkopplung verwendeter Repräsentant bzw. eine konkrete Auswertung $L_{3,\rm alg}^\circ$ typkorrekt als Element von $F^3A_{\rm BC}^{\rm an}$ konstruiert, dann gilt
> \[
> \ell_{s,1}=0\quad\forall s,
> \]
> und folglich verschwindet der primitive $m=1$-Anteil der darauf aufgebauten Rohkopplung.

Status:

\[
\boxed{L_{3,\rm alg}^\circ\in F^3A\Longrightarrow \ell_{s,1}=0\Longrightarrow P_{m=1}\widetilde T_p^{\rm raw}=0}
\qquad \checkmark[M].
\]

Die Prämisse ist im bisherigen Quellenkegel jedoch nicht konstruiert.

---

## 4. Revidierte Statusbuchung für NEU-250f

| Aussage | Alter Status in NEU-250f | Korrigierter Status |
|---|---:|---:|
| $L_3\in C^4(F^3A,F^3A)$ als Quellenbeleg aus NEU-019 | $\checkmark[M]$ | $\checkmark[M]$ als Quellenbefund |
| Aus diesem Beleg folgt ein standalone $L_3^\circ\in F^3A$ | implizit $\checkmark[M]$ | $\times[M]$ Typfehler |
| $\ell_{s,1}=0$ für den in NEU-41 verwendeten abstrakten $L_3^\circ$ | $\checkmark[M]$ | $?[O]$ / derzeit nicht wohldefiniert ohne Realisierung |
| $L_{3,\rm alg}^\circ\in F^3A\Rightarrow \ell_{s,1}=0$ | nicht getrennt | $\checkmark[M]$ |
| $L_{3,\rm alg}^\circ\in F^3A\Rightarrow P_{m=1}\widetilde T_p^{\rm raw}=0$ | nicht getrennt | $\checkmark[M]$ |
| Unbedingter Filtrations-No-Go für den historischen $L_3^\circ$-Kopplungspfad | $\checkmark[M]_{\rm neg,Quelle}$ | **SUPERSEDED / nicht bewiesen** |

Damit wird der Knoten

\[
[O\text{-}221\text{-}1c1a0\text{-C1a/10a}]
\]

nicht positiv entschieden. Seine typkorrekte Form lautet zunächst:

\[
\boxed{?[O]:\ \text{Existiert eine konkrete Algebra-/Operatorrealisierung des relevanten }L_3\text{-Datums, und liegt sie in }F^3A?}
\]

Erst bei positiver Beantwortung greift der filtrationsmäßige $m=1$-No-Go.

---

## 5. Rückwirkung auf NEU-41/42 und P05

Für die SYN-Migration nach P05 gilt verbindlich:

1. Die explizite bilineare Basisformel
   \[
   \widetilde\omega_2(e_uV_p,e_sV_m)
   =-us\log(p)e_{u+ps}V_{pm}
   \]
   bleibt unberührt.
2. Die daraus entwickelte Rohkopplung mit einem **frei gegebenen Algebraelement** als zweitem Argument ist typkorrekt.
3. Die Spezialisierung dieses zweiten Arguments auf den abstrakten/normalisierten $L_3^\circ$ bleibt dagegen an der in NEU-170d/173 festgestellten Realisierungsbrücke hängen.
4. Daher darf P05 weder die historische $L_3^\circ$-Rohkopplung als unbedingte Konstruktion noch den NEU-250f-$m=1$-No-Go als unbedingten Satz übernehmen.

---

## 6. Rückwirkung auf NEU-250g

NEU-250g verwendet NEU-250f in seiner Motivation mit der Aussage, der alte $L_3$-Kopplungspfad sei für den primitiven $m=1$-Sektor endgültig geschlossen.

Diese Motivationsaussage ist durch Patch 1 zu NEU-250f zu schwächen:

\[
\boxed{\text{Der }m=1\text{-No-Go gilt konditional, sobald eine konkrete }F^3\text{-Algebrarealisierung des relevanten }L_3\text{-Datums vorliegt.}}
\]

Die eigenständige algebraische Konstruktion in NEU-250g (modulare Halbgewichtung / primitiver Weilfaktor) wird durch diesen Typbefund **nicht** widerlegt; sie ist in Paket F4 separat zu auditieren.

---

## 7. Pass-A-Urteil

**Prüfart:** `TARGETED-REAUDIT`  
**Auslöser:** konkrete Kollision NEU-250f ↔ NEU-170d/173  
**Urteil:**

\[
\boxed{\text{NEU-250f ursprünglicher unbedingter No-Go: SUPERSEDED.}}
\]

\[
\boxed{L_{3,\rm alg}^\circ\in F^3A\Rightarrow P_{m=1}\widetilde T_p^{\rm raw}=0\quad\checkmark[M]\text{ (konditionaler Anwendungssatz).}}
\]

Keine Aussage über die Existenz einer solchen Realisierung wird hochgestuft.
