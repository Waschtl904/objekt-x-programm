# P11/R32 — SW1-A10 C1C1-AN Hilbert-Space Blind Review Packet

> **Stand:** 30. August 2026  
> **Ziel:** unabhängiger Review der korrigierten analytischen Mehrblatt-Fiberisierung.  
> **Status vor Review:** A10-C1C1-AN = AI-GREEN candidate.  
> **Wichtig:** Der erste analytische Entwurf war falsch normiert; dieses Paket bezieht sich ausschließlich auf die reparierte Fassung.

---

## A. Ursprüngliche Hilberträume

Horizont:

\[
\mathscr H_+
=
L^2(-T_0,T_0)^+.
\]

Annulus:

\[
\mathscr W
=
L^2((-S,-R)\cup(R,S))^-.
\]

Innerer Kernel:

\[
K
=
\ker(E_I^*H|_{\mathscr H_+}).
\]

A2 beweist, dass \(K\) abgeschlossen ist.

---

## B. Korrigierte unitäre Paritätsfaltungen

Für gerades \(y\):

\[
\boxed{
F_+y
=
\sqrt2\,y|_{(0,T_0)}.
}
\]

Dann

\[
\|F_+y\|_{L^2(0,T_0)}
=
\|y\|_{\mathscr H_+}.
\]

Für ungerades \(w\):

\[
\boxed{
F_-w
=
\sqrt2\,w|_{(R,S)}.
}
\]

Dann

\[
\|F_-w\|_{L^2(R,S)}
=
\|w\|_{\mathscr W}.
\]

---

## C. Vierblatt-Horizontcover

Auf \(\mathbb T_L\):

\[
\phi_{P,0}(\theta)=\theta,
\qquad
\phi_{P,1}(\theta)=\theta+\frac L2,
\]

\[
\phi_{\bar Q,0}(\theta)=4\Delta-\theta,
\qquad
\phi_{\bar Q,1}(\theta)=4\Delta-\theta+\frac L2.
\]

Die vier Maps bilden eine Klein-Vierergruppe modulo \(L\) und erhalten das Kreismaß.

Für \(f\in L^2(0,T_0)\) definiert der positive Cover

\[
(V_Hf)_{g,k}(\theta)
=
\frac12\,
m_{g,k}(\theta)\,
f(\rho_g(\theta)+kL),
\qquad
k=0,1,2.
\]

Für jedes feste \(g\) partitionieren die drei Lifts den Horizont, also

\[
\|V_Hf\|=\|f\|.
\]

Der tatsächliche Horizont-Embeddingoperator ist

\[
\boxed{
U_H=V_HF_+.
}
\]

Direkt in ursprünglichen \(y\)-Werten:

\[
\boxed{
(U_Hy)_{g,k}(\theta)
=
\frac1{\sqrt2}\,
m_{g,k}(\theta)\,
y(\rho_g(\theta)+kL).
}
\]

---

## D. Annuluscover

Für \(u\in L^2(R,S)\):

\[
(V_Wu)_k(\theta)
=
n_k(\theta)u(\theta+kL),
\qquad k=0,1,2.
\]

Wegen \(S<T_0<3L\) ist \(V_W\) isometrisch.

Der tatsächliche Annulus-Embeddingoperator ist

\[
\boxed{
U_W=V_WF_-.
}
\]

Direkt in ursprünglichen \(w\)-Werten:

\[
\boxed{
(U_Ww)_k(\theta)
=
\sqrt2\,
n_k(\theta)\,
w(\theta+kL).
}
\]

---

## E. Drei gezielte Reviewfragen

### E1. Fixpunkte / Mehrfachauswertung

Ist die Isometrie von \(U_H\) korrekt, obwohl zwei der vier Kreistransformationen an einzelnen \(\theta\)-Werten denselben physischen Punkt auswerten können?

Zu prüfen:

- Die vier \(g\)-Werte sind verschiedene direkte-Summen-Komponenten.
- Punktweise Verschiedenheit der vier \(\phi_g(\theta)\) ist für die Normsumme nicht erforderlich.
- Opposite-slope-Kollisionen lösen nur
  \[
  2\theta\equiv4\Delta
  \quad\text{oder}\quad
  2\theta\equiv4\Delta+\frac L2
  \pmod L,
  \]
  also höchstens vier Kreispunkte.

### E2. Abgeschlossenheit von \(U_H(K)\)

A2 gibt:

\[
K\subset\mathscr H_+
\quad\text{abgeschlossen}.
\]

Da \(U_H\) isometrisch ist, soll folgen:

\[
\boxed{
U_H(K)
\text{ ist abgeschlossen}.
}
\]

Damit wäre

\[
(U_H|_K)^{-1}:U_H(K)\to K
\]

beschränkt und wohldefiniert.

### E3. Intertwining / Kopplung der beiden Cover

Der inversefreie physische Operator ist

\[
\widetilde{\mathscr C}_R(y,w)
=
(I+A)y+HE_{\mathcal A}w,
\qquad y\in K,\ w\in\mathscr W.
\]

Definiere

\[
\boxed{
\widehat{\mathscr C}_R
=
U_H\widetilde{\mathscr C}_R
\bigl(
(U_H|_K)^{-1}\oplus U_W^{-1}
\bigr).
}
\]

Zu prüfen:

1. Ist diese Konjugationsdefinition auf
   \[
   U_H(K)\oplus U_W(\mathscr W)
   \]
   wohldefiniert?
2. Benötigt ihre Existenz irgendeine zusätzliche punktweise Rand-Matching-Bedingung zwischen dem 12er Horizont- und dem 3er Annuluscover?
3. Oder ist eine solche Matchingfrage erst bei der expliziten C2-Matrixdarstellung relevant?
4. Sind Gate-/Liftgrenzen als \(L^2\)-Nullmengen für die abstrakte Operatorgleichheit unschädlich?

---

## F. Kernelkette

Wenn E1–E3 halten, soll gelten:

\[
\ker\widehat{\mathscr C}_R
\cong
\ker\widetilde{\mathscr C}_R
\cong
\ker\mathscr C_R
\cong
\ker\Gamma_I.
\]

Bitte insbesondere prüfen, ob irgendwo still eine Surjektivität auf den vollen Ambient-Raum behauptet wird. Behauptet wird nur Isometrie auf geschlossene Bildunterräume.

---

## G. Zertifizierte finite Inputs

1. Mehrblatt-Algebra: scripts/certify_sw1_a10_c1c1_multisheet_cover.py
2. Korrigierte Faltungsnormierung: scripts/certify_sw1_a10_c1c1_parity_fold_normalization.py

Die unendlichdimensionale \(L^2\)-Aussage selbst ist **nicht** durch diese Skripte zertifiziert.

---

## H. Gewünschtes Verdict

Bitte getrennt urteilen:

- Fixpunkt-/Direktsummenfrage: PASS / FAIL
- \(U_H(K)\)-Closure: PASS / FAIL
- abstraktes Intertwining: PASS / FAIL
- Gesamt C1C1-AN: PASS / FAIL

Keine Aussage zu C2 oder \(\ker\Gamma_I=\{0\}\) ist Teil dieses Reviews.
