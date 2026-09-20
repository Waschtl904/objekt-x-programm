# Terminal 191D Schur diagnostic preflight at \`a=1\`

2026-09-20. **DIAGNOSTIC ONLY / NO SIGN CERTIFICATE**.

Verified mathematical input frontier: \`79988874cceeb01f17e0cda67485838c0b7c4f63\`.

This package starts the active \`TERMINAL-191D-DEFECT-SCHUR-A1\` computation
without changing theorem status. It tests a direct floating-point physical
quadrature against the rigorously positive calibration endpoint
\(B=\log(5)/2\) before allowing any interpretation at \`a=1\`.

The low coordinates are exactly those of the bridge theorem:
\(e_n=\sqrt{2n+1}P_n\), with even degrees \`2,4,...,382\` and odd degrees
\`3,5,...,383\`. The one nonautomatic Mellin moment is removed by the same
carrier correction
\[
M_{p,a}e_n=e_n-
\frac{\langle e_n,m_{p,a}\rangle}{\langle e_p,m_{p,a}\rangle}e_p.
\]

The diagnostic script evaluates the inherited physical nonpole form directly,
uses Gauss-Legendre quadrature plus the substitution \(r=t^2\) in the Gamma
integral, appends 32 high Galerkin modes, and forms an ordinary numerical
Schur complement.

At the certified positive endpoint \(B\), the run with \`nx=900\`, \`nt=300\`
returns
\[
\lambda_{\min}^{diag}(B,even)\approx-5.93\cdot10^{-3},\qquad
\lambda_{\min}^{diag}(B,odd)\approx-5.05\cdot10^{-3}.
\]
Therefore this direct quadrature pipeline **fails calibration**.

Consequently the raw \`a=1\` values stored in \`terminal_schur_diag.json\` have
no sign meaning. In particular,
\[
\lambda_{\min}^{diag}(1)<0
\not\Rightarrow S_1^p\not\succeq0.
\]

The only admissible conclusion is that direct physical floating-point
quadrature is not sign-safe at the precision required by this gate.

The rigorous route must instead extend the repository's existing analytic /
exact Legendre reference-operator engine to \`a=1\`, retain all five channels
\`2,3,4,5,7\`, construct the 191 moment-corrected Low columns, and enclose the
complete High response in
\[
S_1^p=I-\alpha_1^p-\beta_1^{p*}(I-K_1^p)^{-1}\beta_1^p.
\]
Only a directed rational/interval \`LDL*\` or a kernel-aware semidefinite
certificate may decide the terminal sign.

No negative Weil source, no C1c verdict, no Object-X claim and no RH claim
is made here.
