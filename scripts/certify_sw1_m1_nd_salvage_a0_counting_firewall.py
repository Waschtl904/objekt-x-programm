#!/usr/bin/env python3
"""SW1 M1-ND SALVAGE-A0 counting firewall certificate.

Purpose:
- certify the exact linear phase-count formula M_N=288N+144 already used by IMG3;
- certify that this count alone cannot imply an R-independent blind fraction
  once N is allowed to depend on R.

The script does NOT assert that the real phase locations cover the annulus.
It proves only that the cardinality/length estimate is compatible with full
coverage when N grows like 1/R, so actual phase geometry must be analyzed.
"""

import sympy as sp

print("SW1 M1-ND SALVAGE-A0 COUNTING FIREWALL")

N=sp.symbols("N", integer=True, nonnegative=True)
M=72*(4*N+2)
assert sp.expand(M)==288*N+144

# Abstract positive constants.
T,R,sigma=sp.symbols("T R sigma", positive=True)

# Restricted-tail condition sigma<R implies annulus length A=S-R<T.
S=T+sigma
A=sp.expand(S-R)
assert sp.simplify(T-A)==R-sigma

# If M*R >= T, then the raw count/length upper bound is already >= A.
# This makes the union bound non-informative: it cannot force beta>0.
margin=sp.expand(M*R-T)

# Explicit adaptive choice R_N=T/M. Then M*R_N=T exactly.
RN=sp.simplify(T/M)
assert sp.simplify(M*RN-T)==0

# Choosing sigma_N=R_N/2 gives an annulus shorter than T.
sigmaN=RN/2
AN=sp.simplify(T+sigmaN-RN)
assert sp.simplify(T-AN)==RN/2
assert (sp.simplify(T-AN)).is_positive is True

# For any fixed lower-chamber epsilon>0, RN<epsilon once
# M>T/epsilon.  The exact integer ceiling is an elementary Archimedean step
# and is intentionally kept outside the finite CAS certificate.
eps=sp.symbols("eps", positive=True)

print("M_N = 288*N + 144: PASS")
print("restricted tail sigma<R gives S-R<T: PASS")
print("adaptive R_N=T/M_N gives M_N*R_N=T exactly: PASS")
print("with sigma_N=R_N/2, annulus length is T-R_N/2<T: PASS")
print("CONCLUSION: count/length data alone are compatible with full coverage")
print("NECESSARY DEPTH ONLY: N=Omega(1/R)")
print("FIREWALL: actual A7/A8 phase locations and overlaps remain decisive")
print("SW1 M1-ND SALVAGE-A0 COUNTING FIREWALL: PASS")
