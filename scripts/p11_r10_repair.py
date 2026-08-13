from pathlib import Path

path = Path("papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex")
text = path.read_text()

old1 = r'''\[
 \boxed{
 (R_Rf)(u)
 =\sum_{p^k\le e^{2R}}
 \sqrt{\log p}\,p^{-k/4}
 D_{k\log p}E_Rf(u)\otimes\mathsf Q_R(u)\eta_{p,k}.
 }
\tag{2.6}\label{eq:rest-operator}
\]
For fixed $R$ these are bounded finite-window operators.'''

new1 = r'''\[
 \boxed{
 (R_Rf)(u)
 =\sum_p\sum_{k\ge1}
 \sqrt{\log p}\,p^{-k/4}
 D_{k\log p}E_Rf(u)\otimes\mathsf Q_R(u)\eta_{p,k}.
 }
\tag{2.6}\label{eq:rest-operator}
\]
This sum is nevertheless effectively finite for every fixed $R$.  Indeed, a nonzero
summand at $u\in(-R,R)$ requires $\mathsf Q_R(u)\eta_{p,k}\ne0$, hence
$J_{p,R}(u)\ge1$ and therefore $p\le e^{2R}$.  It also requires
$D_{k\log p}E_Rf(u)\ne0$, so at least one of $u\pm\frac{k}{2}\log p$ lies in
$[-R,R]$.  Consequently
\[
 \frac{k}{2}\log p\le R+|u|\le2R,
 \qquad\text{hence}\qquad p^k\le e^{4R}.
\]
Thus only finitely many $(p,k)$ can contribute at a fixed source level, and both $H_R$
and $R_R$ are bounded finite-window operators.'''

old2 = r'''At fixed $R$ the effectively active sums are finite.  Then
\[
 \mathfrak R_R(f,g)
 =\sum_p(\log p)(p-1)\sum_{a\ge0}p^a
 \int_{\Omega_{p,a,R}}
 \Phi_{p,a,R}[f](u)\overline{\Phi_{p,a,R}[g](u)}\,du.
\tag{3.4}\label{eq:rest-gram}
\]
Define the canonical analysis target
\[
 \mathscr Z_R:=\bigoplus_p\bigoplus_{a\ge0}L^2(\Omega_{p,a,R})
\]
and
\[
 (\widetilde R_Rf)_{p,a}(u)
 :=\sqrt{(\log p)(p-1)p^a}\,
 1_{\Omega_{p,a,R}}(u)\Phi_{p,a,R}[f](u).
\]
Polarization of~\eqref{eq:rest-gram} gives
\[
 \boxed{\widetilde R_R^*\widetilde R_R=R_R^*R_R.}
\tag{3.5}\label{eq:full-rest-gram}
\]'''

new2 = r'''At fixed $R$ the effectively active sums are finite.  The coefficient of
$\psi_{p,a}$ in the $p$-sector of $R_Rf$ is, by~\eqref{eq:projected-mark}, exactly
\[
 \sqrt{(\log p)(p-1)p^a}\,
 1_{\Omega_{p,a,R}}(u)\Phi_{p,a,R}[f](u).
\]
Since the martingale coordinates $\psi_{p,a}$ are orthonormal and different prime
sectors are orthogonal, one obtains directly
\[
 \mathfrak R_R(f,g):=\langle R_Rf,R_Rg\rangle
 =\sum_p(\log p)(p-1)\sum_{a\ge0}p^a
 \int_{\Omega_{p,a,R}}
 \Phi_{p,a,R}[f](u)\overline{\Phi_{p,a,R}[g](u)}\,du.
\tag{3.4}\label{eq:rest-gram}
\]
Define the canonical analysis target
\[
 \mathscr Z_R:=\bigoplus_p\bigoplus_{a\ge0}L^2(\Omega_{p,a,R})
\]
and
\[
 (\widetilde R_Rf)_{p,a}(u)
 :=\sqrt{(\log p)(p-1)p^a}\,
 1_{\Omega_{p,a,R}}(u)\Phi_{p,a,R}[f](u).
\]
Thus the preceding coordinate identity gives, for all $f,g$,
\[
 \langle\widetilde R_Rf,\widetilde R_Rg\rangle_{\mathscr Z_R}
 =\langle R_Rf,R_Rg\rangle,
\]
and hence
\[
 \boxed{\widetilde R_R^*\widetilde R_R=R_R^*R_R.}
\tag{3.5}\label{eq:full-rest-gram}
\]'''

c1 = text.count(old1)
c2 = text.count(old2)
if c1 != 1 or c2 != 1:
    raise SystemExit(f"Refusing repair: expected unique blocks, got definition={c1}, full_rest={c2}")

path.write_text(text.replace(old1, new1).replace(old2, new2))
print("Applied exactly two guarded R10 replacements.")
