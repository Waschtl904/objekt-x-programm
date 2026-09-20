# All-parity restart lemma and shrinking-step iteration

2026-09-19. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

Anchor: `a659047e00d024c0daa3991ea59fd21afd9f8793` on
`research/x-c1-inherited-resonance-shell-schur-2026-09-18`.

This package starts from the already proved local all-parity theorem at
\[
B={\log5\over2},\qquad 0<h\le10^{-20},
\]
and proves a new structural fact: the shell construction can be restarted
from a newly positive endpoint. The restart is uniform in the endpoint on a
fixed local band, but the explicit iteration produced here uses shrinking
step widths. It is therefore **not** a uniform-step transport theorem,
Connected Unit-Window Coercivity, Strong Terminal, full C1-GEOM, Object X,
global Weil positivity or RH.

No new Mellin condition and no A1 are introduced.

## 1. Input and exact zero-extension ceiling

Let `F_a` be the complete closed two-Mellin form space at window `a`, with
its even and odd invariant summands. Assume an endpoint `a` satisfies
\[
B\le a\le B+10^{-2}
\tag{1}
\]
and that on the complete all-parity form domain
\[
q_a[v]\ge\varepsilon\|v\|_2^2,
\qquad \varepsilon>0.
\tag{2}
\]
Exact physical zero extension preserves both Mellin functionals and the
connected form. Hence the variational gap is nonincreasing with the window.
The point of the restart lemma is not to contradict this monotonicity, but to
show that an arbitrarily slightly smaller target gap can be retained on a
new positive right shell.

Throughout the restart step write
\[
b=a+h,\qquad 0<h\le10^{-20},\qquad L=\log(2/h),
\tag{3}
\]
and require `b<=B+10^-2`.

## 2. The active set and disjoint input intervals remain uniform

On the band (1)-(3), no prime power beyond `5` is active. Indeed
\[
\log7-2b=\log(7/5)-2(a-B)-2h>0,
\]
because `log(1+x)>=x/(1+x)` gives `log(7/5)>=2/7`, while
`2(a-B)+2h<1/50+2*10^-20`.

For `x=a+r`, `0<r<h`, the four reflected positive-core input intervals are
\[
\begin{array}{c|c}
2&(a-\log2,\ a-\log2+h),\\
3&(\log3-a-h,\ \log3-a),\\
4&(\log4-a-h,\ \log4-a),\\
5&(\log5-a-h,\ \log5-a).
\end{array}
\tag{4}
\]
They stay inside `(0,a)` and are pairwise disjoint. The only moving nearest
pair is `2/3`, whose separation is
\[
\log6-2a-2h
=\log(6/5)-2(a-B)-2h
>1/6-1/50-2\,10^{-20}>0.
\tag{5}
\]
The `3/4` and `4/5` separations are at least `log(4/3)-h>1/4-h`
and `log(5/4)-h>1/5-h`.

Thus the same disjoint-input Cauchy-Schwarz estimate used at `a659047`
applies uniformly at every restart endpoint in this band:
\[
|q_{\rm prime}(Jv,S_s)|
\le \sqrt{2\sum_{q=2,3,4,5}w_q^2}\,\|v\|p,
\tag{6}
\]
with `w_q=Lambda(q)/sqrt(q)` and `p=||s||_(L2(a,b))`.

## 3. Uniform even and odd moment correctors

The restart uses full old-core plus profile coordinates, so no separate trace
coordinate is introduced.

### Even

On `0<=x<=a` put
\[
\rho_e(x)=1-x/a,
\qquad M_e(a)=\int_0^a\rho_e(x)\cosh(x/2)\,dx,
\qquad \chi_e=\rho_e/M_e,
\tag{7}
\]
and reflect `chi_e` evenly. Since `a>B>4/5` and `cosh>=1`,
\[
M_e(a)\ge a/2>2/5,
\]
so uniformly
\[
\|\chi_e\|_\infty<3,
\qquad \operatorname{Lip}(\chi_e)<4,
\qquad \|\chi_e\|_2^2<13.
\tag{8}
\]
It is in `H1_0((-a,a))` and has exact positive-half cosh moment one.

### Odd

Put
\[
\rho_o(x)={x\over a}(1-x/a),
\qquad M_o(a)=\int_0^a\rho_o(x)\sinh(x/2)\,dx,
\qquad \chi_o=\rho_o/M_o,
\tag{9}
\]
and reflect oddly. Since `sinh(x/2)>=x/2`,
\[
M_o(a)\ge a^2/24>2/75,
\]
therefore
\[
\|\chi_o\|_\infty<10,
\qquad \operatorname{Lip}(\chi_o)<47,
\qquad \|\chi_o\|_2^2<200.
\tag{10}
\]
Again the positive-half sinh moment is exactly one.

For a parity profile `s`, let `S_s^e` or `S_s^o` be its reflected shell
extension and put
\[
Y_s^e=-m_s^e\chi_e+S_s^e,
\qquad
Y_s^o=-m_s^o\chi_o+S_s^o.
\tag{11}
\]
As `b<1`, the elementary series bounds
`cosh(1/2)<6/5` and `sinh(1/2)<3/5` give
\[
|m_s^e|\le{6\over5}\sqrt h\,p,
\qquad
|m_s^o|\le{3\over5}\sqrt h\,p.
\tag{12}
\]
Thus each profile satisfies exactly its parity component of the original
two Mellin conditions. Together the two parity conditions are exactly the
original pair, not two new conditions.

## 4. Uniform complete core/profile coupling below four

The singular Gamma core/shell pairing obeys uniformly
\[
|\mathcal E(Jv,S_s)|\le
\left({\pi\over\sqrt2}+{5\sqrt2\over4}\sqrt{ah}\right)\|v\|p.
\tag{13}
\]
The pinned disjoint-prime certificate gives
\[
\sqrt{2\sum_{q=2,3,4,5}w_q^2}<1.601.
\tag{14}
\]

For the even corrector, the same kernel estimate as in the full-width even
proof gives Gamma-action norm `<155`; the bounded non-Gamma remainder has
norm at most `14`, hence
\[
|q_a(v,\chi_e)|<215\|v\|.
\tag{15}
\]
For the odd corrector, the proof at `a659047` gives uniformly
\[
|q_a(v,\chi_o)|<1200\|v\|.
\tag{16}
\]
The active set is the same `2,3,4,5`; changing the endpoint inside (1) does
not change the operator-norm bound used in (15)-(16).

Using `pi<22/7`, `1/sqrt(2)<5/7`, `sqrt(2)<3/2`, (12)-(16), and
`sqrt(h)<=10^-10`, both parities satisfy the complete bound
\[
\boxed{|q_b(Jv,Y_s)|<4\|v\|p.}
\tag{17}
\]
No finite core expansion is used here.

## 5. Uniform profile floor

For both reflection signs the pure shell satisfies
\[
q_b[S_s]\ge2(L-8)p^2.
\tag{18}
\]
The same-side leakage is endpoint-independent. The opposite-shell distance
is at least `2B` and only increases. Arithmetic shell self-correlations for
`q=2,3,4,5` vanish on (1)-(3): same-side widths are smaller than `log2`,
and an opposite-side overlap would require `2a-log q+r+r'=0`, which is
impossible except the null endpoint contact `q=5,a=B,r=r'=0`.

For a bounded core function the uniform shell bound is
\[
|q_b(Jf,S_s)|\le\|f\|_\infty\sqrt h\,(L+11)p.
\tag{19}
\]
Expanding the exact moment correction gives, in the even case,
\[
d_e[s]\ge
\left[2(L-8)-{36\over5}h(L+11)-{6552\over25}h\right]p^2,
\tag{20}
\]
and in the odd case the already proved estimate
\[
d_o[s]\ge[2(L-8)-h(12L+1140)]p^2.
\tag{21}
\]
For `0<h<=10^-20`, each displayed loss is `<1`. Hence uniformly in both
parities
\[
\boxed{d_{e/o}[s]>(2L-17)p^2.}
\tag{22}
\]

## 6. Complete profile coordinates at a restarted endpoint

Let `K_a^e,K_a^o` be the even/odd physical L2 Mellin kernels and let
`F_a^e,F_a^o` be the corresponding closed form spaces. Define the profile
form space by pullback,
\[
F_{p,a,h}^{e/o}=\{s:Y_s^{e/o}\in F_b^{e/o}\}.
\tag{23}
\]
Then
\[
\Psi_{e/o}:F_a^{e/o}\oplus F_{p,a,h}^{e/o}\to F_b^{e/o},
\qquad \Psi(v,s)=Jv+Y_s,
\tag{24}
\]
is a form-space isomorphism.

At Hilbert level its inverse is exactly
\[
s=u|_{(a,b)},\qquad v=u_{\rm core}+m_s\chi_{e/o}.
\tag{25}
\]
The profile moment cancels the shell moment, so there is no kernel and no
trace duplication. Exact zero extension places `F_a` inside `F_b`; the
profile image is in `F_b` by (23). The bounds (2), (17), (22) make the
product graph norm complete and the image form-closed. Actual H1 sources
belong to the image by the same boundary-strip cutoff and moment-restoration
argument already used in the odd package. Their exact preimage satisfies
\[
v(a)=s(a),\qquad s(b)=0,
\tag{26}
\]
with the appropriate parity reflection. Thus no separate core zero trace
or extra Mellin condition is imposed.

This section is analytic; the checker only verifies its constant ledger.

## 7. Restart lemma

Assume (2), choose any target
\[
0<\gamma<\varepsilon,
\qquad m=\varepsilon-\gamma,
\qquad \delta=m/2,
\qquad \eta={m\over4\gamma}.
\tag{27}
\]
By (17), (22) and Young's inequality,
\[
q_b[\Psi(v,s)]
\ge(\varepsilon-\delta)\|v\|^2
 +\left(2L-17-{16\over\delta}\right)p^2
\]
\[
=(\gamma+m/2)\|v\|^2
 +\left(2L-17-{32\over m}\right)p^2.
\tag{28}
\]
Moreover (8), (10), (12) give the common physical norm estimate
\[
\|\Psi(v,s)\|^2
\le(1+\eta)\|v\|^2+
\left[2+72(1+\eta^{-1})h\right]p^2.
\tag{29}
\]
Since
\[
\gamma(1+\eta)=\gamma+m/4<\gamma+m/2,
\tag{30}
\]
it is sufficient that
\[
72\left(1+{4\gamma\over m}\right)h\le1,
\tag{31}
\]
\[
2\log(2/h)-17-{32\over m}\ge3\gamma.
\tag{32}
\]
Under (1), (3), (31), (32) the complete restarted endpoint obeys
\[
\boxed{q_{a+h}[u]\ge\gamma\|u\|^2}
\tag{33}
\]
on both parity form spaces and therefore on the complete two-Mellin form
space. In particular every actual nonzero H1_0 source has strictly positive
energy.

Equivalently, one may take any
\[
0<h\le\min\left\{10^{-20},\ B+10^{-2}-a,
{1\over72(1+4\gamma/m)},
2\exp\left[-{17+32/m+3\gamma\over2}\right]\right\}.
\tag{34}
\]
This is an explicit **restart lemma**. The constants in the analytic shell
construction are uniform in the endpoint `a`; only the allowed width depends
on the certified gap budget `m=epsilon-gamma`.

## 8. Explicit infinite shrinking-step iteration from a659047

The local all-parity theorem at the anchor gives at
\[
b_0=B+10^{-20}
\]
the certified gap
\[
\varepsilon_0=3\cdot10^{-15}.
\tag{35}
\]
For `n>=0` define
\[
\varepsilon_n=10^{-15}\left(1+2^{1-n}\right),
\qquad
m_n=\varepsilon_n-\varepsilon_{n+1}=10^{-15}2^{-n},
\tag{36}
\]
\[
N_n=4\cdot10^{16}\,2^n,
\qquad h_n=2^{-N_n},
\qquad b_{n+1}=b_n+h_n.
\tag{37}
\]
Then every restart hypothesis is satisfied.

First `log2=2 atanh(1/3)>2/3`, so
\[
2\log(2/h_n)=2(N_n+1)\log2>{4\over3}N_n.
\]
Therefore
\[
2\log(2/h_n)-17-{32\over m_n}
>
{64\over3}10^{15}2^n-17
>3\varepsilon_{n+1}.
\tag{38}
\]

Second
\[
\eta_n={m_n\over4\varepsilon_{n+1}}
={1\over4(2^n+1)}.
\]
Since `N_n>=n+20`,
\[
72(1+\eta_n^{-1})h_n
\le {648\over2^{20}}<1.
\tag{39}
\]
Also `N_n>=80` and `2^80>10^20`, so `h_n<10^-20`.

Finally `N_n>=N_0+n`, hence
\[
\sum_{n\ge0}h_n\le2^{-N_0+1}<10^{-20}.
\tag{40}
\]
Thus every endpoint remains below `B+2*10^-20`, far inside the uniform band
(1). Induction with the restart lemma proves
\[
\boxed{
q_{b_n}[u]\ge\varepsilon_n\|u\|^2
\quad\text{for every }n\ge0,
\qquad
\varepsilon_n>10^{-15}.
}
\tag{41}
\]
for the complete all-parity two-Mellin form space.

This is a genuine infinite **strictly increasing endpoint chain** with a
positive uniform gap floor. It proves restartability/iterability of the local
transport mechanism.

## 9. What is and is not closed

Closed here:

- a parity-complete restart lemma from any already positive endpoint in the
  local band `B<=a<=B+10^-2`;
- uniform corrector, active-set, coupling and profile constants on that band;
- an explicit infinite strictly increasing sequence of endpoints starting
  from `B+10^-20`;
- a certified lower gap `>10^-15` at every finite endpoint of that sequence.

Still open:

- a **uniform positive lower bound on the step width** independent of the
  iteration number;
- a quantitatively useful Window Amplification beyond the tiny local band;
- crossing the `q=7` activation threshold `log(7)/2` by this restart lemma;
- a non-summable step mechanism reaching a prescribed macroscopic endpoint;
- Connected Unit-Window Coercivity, Strong Terminal, full C1-GEOM, Object X,
  global Weil positivity and RH.

The exact gap monotonicity explains why the shrinking-gap budget is not a
cosmetic issue: every guaranteed new-direction Schur loss must be paid from
an already nonincreasing variational gap. This package proves that the loss
can be made summable by shrinking the shell, but it does not prove that it
can be made zero or uniformly harmless at a fixed positive width.
