# P11/R32 — SW1 Lemma: Irrationalität von \(\Delta/L\)

> **Stand:** 30. August 2026  
> **Scope:** elementares Konstantenlemma für A4/A5/A9/A10.  
> **Status:** AI-GREEN candidate + independent GREEN (certificate, algebraic reduction); keine Promotion.

---

## 1. Konstanten

Mit

\[
a=\frac12\log2,\qquad
b=\frac12\log3,
\]

\[
d=b-a,\qquad
e=2a-b
\]

gilt

\[
\Delta=d-e
=
\log3-\frac32\log2.
\]

Ferner

\[
L=a-\Delta
=
2\log2-\log3.
\]

Zu zeigen ist

\[
\boxed{\Delta/L\notin\mathbb Q.}
\]

---

## 2. Reduktion auf Primzahlbewertungen

Angenommen,

\[
\frac{\Delta}{L}=\frac mn
\]

mit

\[
m,n\in\mathbb Z,\qquad n\ne0.
\]

Dann

\[
n\Delta=mL,
\]

also

\[
n\left(\log3-\frac32\log2\right)
=
m(2\log2-\log3).
\]

Nach Multiplikation mit \(2\):

\[
\boxed{
2(n+m)\log3
=
(3n+4m)\log2.
}
\tag{IRR.1}
\]

Setze

\[
A:=2(n+m),
\qquad
B:=3n+4m.
\]

Aus

\[
A\log3=B\log2
\]

folgt durch Exponentiation in \(\mathbb Q_{>0}^{\times}\)

\[
3^A=2^B.
\]

Diese Gleichung ist auch für negative ganze Exponenten eine Gleichung in \(\mathbb Q^\times\).

Wende die Primzahlbewertungen \(v_2\) und \(v_3\) an:

\[
v_2(3^A)=0,
\qquad
v_2(2^B)=B,
\]

also

\[
B=0.
\]

Ebenso

\[
v_3(3^A)=A,
\qquad
v_3(2^B)=0,
\]

also

\[
A=0.
\]

Daher

\[
2n+2m=0,
\qquad
3n+4m=0.
\]

Die Koeffizientenmatrix ist

\[
\begin{pmatrix}
2&2\\
3&4
\end{pmatrix}
\]

mit Determinante

\[
8-6=2\ne0.
\]

Folglich

\[
n=m=0,
\]

im Widerspruch zu \(n\ne0\).

Damit

\[
\boxed{
\Delta/L\notin\mathbb Q.
}
\]

---

## 3. Zertifikat

Zertifikat:

scripts/certify_sw1_delta_over_L_irrationality.py

Commit:

02044e3d236289869a0de5e6b276a00f23ab0a9c

Committed Script-Blob:

201c87e795011681778dfac03e7aa2e5cff54a59

Der exakt gleiche Dateiinhalt wurde vor dem Commit lokal ausgeführt und ergab bereits denselben Git-Blob-SHA.

Ergebnis:

SW1 DELTA-OVER-L IRRATIONALITY ALGEBRA CERTIFICATE: PASS

Das Zertifikat prüft:

- die exakten \((\log2,\log3)\)-Koeffizienten von \(\Delta\) und \(L\);
- die Reduktion von \(n\Delta=mL\) auf IRR.1;
- die Integer-Matrix;
- \(\det=2\).

Der Primzahlbewertungs-Schritt ist der oben vollständig ausgeschriebene mathematische Beweis und keine CAS-Behauptung.

---

## 4. Firewall

Dieses Lemma beweist ausschließlich

\[
\Delta/L\notin\mathbb Q.
\]

Es beweist keine Orbit-Endlichkeit oder -Unendlichkeit ohne zusätzliche Graph-/Transferaussage und insbesondere keine Schur-, Cross-Gram-, Objekt-X- oder RH-Folgerung.
