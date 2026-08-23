# P12 Runde 22 — Restricted-tail descent with no lower-radius threshold

**Status:** theorem candidate; not promoted; independent raw/scope review required.  
**Repo basis:** current P12 after Round 21 promotion.  
**Firewall:** P11 FROZEN; R14 unchanged; no Polar Gauge, Strong/Terminal Transport, Objekt X, or RH claim.

## 1. Statement

Let
\[
T=2a,\qquad 2a<T_0<c,\qquad
\sigma:=S-T,\qquad \varepsilon:=T_0-T,
\]
so
\[
0<\sigma<\varepsilon<\varepsilon_{\max}.
\]

The candidate theorem is

\[
\boxed{
0<R<T,\qquad 0<\sigma\le R
\Longrightarrow
\ker L_{R,T+\sigma,T_0}^{\{a,b,2a\}}=\{0\}.
}
\tag{R22}
\]

Thus the entire restricted-tail regime has no positive lower-radius
threshold.

For \(R\ge e/2\), this is already contained in committed Round 14.
It remains only to prove \(0<R<e/2\).

---

## 2. Lower-half kill for arbitrary \(0<R<e/2\)

Assume
\[
0<R<e/2,\qquad 0<\sigma\le R.
\]

For every \(x\in(R,a)\),
\[
x>R\ge\sigma
\]
implies
\[
T+x>S=T+\sigma.
\]

Hence the only mixed-tail contamination of the endpoint E-equation is absent.
The canonical lower E-equation is exactly the endpoint/A14.3a equation.

Therefore the repaired A14.3a lower-circle unique-continuation argument applies
with no use of \(R\ge\rho\), and gives

\[
\boxed{h=0\quad\text{a.e. on }(R,a).}
\tag{2.1}
\]

---

## 3. Horizon source creates a right null strip

For \(0<t<\varepsilon\), the source \(u=T+t\) is horizon-legal and gives

\[
p\,h(a+t)+r\,h(e+t)+q\,h(t)=0.
\tag{3.1}
\]

Because
\[
\varepsilon<e,\qquad e+\varepsilon<2e<a,
\]
both \(t\) and \(e+t\) lie either below \(R\) (support-zero) or inside the
already-killed interval \((R,a)\). Hence

\[
\boxed{h(a+t)=0\quad(0<t<\varepsilon)\ {\rm a.e.}}
\tag{3.2}
\]

and, with \(l(z)=h(T-z)\),

\[
l(z)=0,\qquad a-\varepsilon<z<a.
\tag{3.3}
\]

---

## 4. High reflection is tail-free on the seed strip

Since
\[
a-\varepsilon>a-\varepsilon_{\max}>d,
\]
the whole strip (3.3) lies in the committed high-reflection domain.

The possible mixed tail offsets are \(z\) and \(z-e\).
On this strip,

\[
z>a-\varepsilon>d>e/2>R\ge\sigma,
\]

and

\[
z-e>d-\varepsilon>d-\varepsilon_{\max}>e/2>R\ge\sigma.
\]

Thus all mixed-tail contaminants are above \(S\), and the old
high-reflection identity is unchanged:

\[
q\,l(z)+p\,l(a-z)=0.
\tag{4.1}
\]

Using (3.3), with \(w=a-z\), gives

\[
\boxed{l(w)=0\quad(0<w<\varepsilon)\ {\rm a.e.}}
\tag{4.2}
\]

No \(\rho\)-bound has been used.

---

## 5. P1 kills the entire tail

The committed unconditional identity P1 is

\[
H(t)+l(t)+\frac{2r}{p}H(d-t)=0,
\qquad 0<t<\varepsilon.
\tag{5.1}
\]

For \(0<t<\sigma\), (4.2) gives \(l(t)=0\).

Also, because \(\sigma\le R<e/2\),

\[
d-t>d-\sigma\ge d-R>d-e/2>e/2>\sigma.
\]

Hence
\[
H(d-t)=0
\]
by tail support. Therefore (5.1) gives

\[
\boxed{H(t)=0\quad(0<t<\sigma)\ {\rm a.e.}}
\tag{5.2}
\]

so the entire mixed tail \((T,T+\sigma)\) vanishes.

---

## 6. Reduction to b1

After (5.2), the same kernel vector is supported in \((R,T)\), while the
source horizon \(T_0\) is unchanged.

Committed b1 applies for every
\[
2a<T_0<c,\qquad 0<R<T,\qquad S_{\rm eff}=T,
\]
and yields
\[
\boxed{h=0.}
\]

Thus (R22) follows.

---

## 7. Exact inequalities used

The proof requires only

\[
0<R<e/2,\qquad \sigma\le R,
\]
together with the fixed P12 chamber
\[
0<\sigma<\varepsilon<\varepsilon_{\max}<e,
\]
and the elementary constant comparisons
\[
a-\varepsilon_{\max}>d,\qquad
d-\varepsilon_{\max}>e/2,\qquad
d-e/2>e/2.
\]

No step uses \(R\ge\rho\).

---

## 8. Booking

Before independent review:

\[
\boxed{\text{restricted-tail all-}R\text{ theorem: review candidate}.}
\]

If GREEN, this removes the entire sector \(\sigma\le R\) from every future
low-radius descent problem.  The only remaining low-radius geometry is the
genuine overlap \(\sigma>R\).
