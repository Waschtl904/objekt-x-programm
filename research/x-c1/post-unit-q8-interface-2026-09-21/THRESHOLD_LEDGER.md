# THRESHOLD_LEDGER - post-unit C1 and the q=8 wall

Status: **FIRST CLOSED CHAMBER O1–O7 AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN; O8+ OPEN**. No positivity beyond terminal horizon 1.

## Activation rule

A prime-power channel q=p^k is active on source horizon a exactly when
\[
\log q<2a.
\]
The inequality is strict. At A_q=(1/2)log q the channel is still excluded.
Endpoint contact has measure zero in the inherited compact-source translation
pairing.

The weight is
\[
w_q=\frac{\Lambda(q)}{\sqrt q},
\]
so \Lambda(p^k)=\log p.

| q | exact threshold | decimal guide | status at a=1 |
|---|---:|---:|---|
| 2 | log(2)/2 | 0.3465735902799726 | active |
| 3 | log(3)/2 | 0.5493061443340549 | active |
| 4 | log(4)/2 = log(2) | 0.6931471805599453 | active |
| 5 | log(5)/2 | 0.8047189562170501 | active |
| 7 | log(7)/2 | 0.9729550745276566 | active |
| 8 | log(8)/2 | 1.0397207708399179 | inactive |
| 9 | log(9)/2 = log(3) | 1.0986122886681098 | inactive |

Define
\[
A_8=\frac12\log8,\qquad A_9=\frac12\log9=\log3.
\]

Then
\[
\boxed{1\le a\le A_8\Longrightarrow
\mathcal Q_-=\{2,3,4,5,7\}.}
\]
At a=A_8, q=8 is still inactive.

Immediately right of the wall,
\[
A_8<a\le A_9
\]
the family is
\[
\boxed{\mathcal Q_+=\{2,3,4,5,7,8\}.}
\]
At a=A_9, q=9 is still excluded.

For q=8=2^3,
\[
\boxed{w_8=\frac{\Lambda(8)}{\sqrt8}
=\frac{\log2}{\sqrt8}.}
\]
It is not log(8)/sqrt(8).

## Terminal convention

For terminal horizon A use
\[
\mathcal Q_A=\{q=p^k:\log q<2A\}
\]
as one fixed channel family for every source window a\le A.

Thus
\[
1\le A\le A_8\Rightarrow\mathcal Q_A=\mathcal Q_-,
\]
and
\[
A_8<A\le A_9\Rightarrow\mathcal Q_A=\mathcal Q_+.
\]

A_9 is only the next-wall sentinel. This package does not attempt the q=9
wall and proves no positivity, new Schur dimension, wall crossing, Object X,
global Weil positivity, or RH.
