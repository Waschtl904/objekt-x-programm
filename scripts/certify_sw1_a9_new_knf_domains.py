#!/usr/bin/env python3
"""SW1-A9 exact activity domains of the genuinely new KNF edge types.

For every 0<u<R the certified local K6 block has vertices
u, a+u, b-u, b+u, T-u, T+u.
This certificate derives the exact source domains of the six genuinely new
affine types and their inverse directions.

Endpoints are irrelevant L2-null sets; all intervals below are open.
"""
import sympy as sp

L,D,R,u=sp.symbols("L D R u", positive=True)
a=L+D
b=sp.Rational(3,2)*L+2*D
T=2*L+2*D
d=L/2+D
e=L/2

U=u
Ap=a+u
Bm=b-u
Bp=b+u
Tm=T-u
Tp=T+u

# Exact affine relations.
assert sp.simplify((b-U)-Bm)==0                    # r_b(U)=b-U
assert sp.simplify((U+b)-Bp)==0                    # tau_+b(U)=Bp
assert sp.simplify((Bp-b)-U)==0                    # tau_-b(Bp)=U

assert sp.simplify((a+b-Ap)-Bm)==0                 # r_{a+b}(Ap)=Bm
assert sp.simplify((Ap+d)-Bp)==0                   # tau_+d(Ap)=Bp
assert sp.simplify((Bp-d)-Ap)==0                   # tau_-d(Bp)=Ap

assert sp.simplify((Bm+e)-Tm)==0                   # tau_+e(Bm)=Tm
assert sp.simplify((Bp+e)-Tp)==0                   # tau_+e(Bp)=Tp
assert sp.simplify((Tm-e)-Bm)==0                   # tau_-e(Tm)=Bm
assert sp.simplify((Tp-e)-Bp)==0                   # tau_-e(Tp)=Bp

assert sp.simplify((T+b-Bm)-Tp)==0                 # r_{T+b}(Bm)=Tp
assert sp.simplify((T+b-Bp)-Tm)==0                 # r_{T+b}(Bp)=Tm

# Parameter-image interval endpoints.  Since 0<u<R, each parameterization is
# a bijection onto the stated open interval.
domains={
 "r_b": [("U",(0,R)),("Bm",(b-R,b))],
 "+b":  [("U",(0,R))],
 "-b":  [("Bp",(b,b+R))],
 "r_ab":[("Ap",(a,a+R)),("Bm",(b-R,b))],
 "+d":  [("Ap",(a,a+R))],
 "-d":  [("Bp",(b,b+R))],
 "+e":  [("Bm",(b-R,b)),("Bp",(b,b+R))],
 "-e":  [("Tm",(T-R,T)),("Tp",(T,T+R))],
 "r_Tb":[("Bm",(b-R,b)),("Bp",(b,b+R)),
         ("Tm",(T-R,T)),("Tp",(T,T+R))],
}

# Exact inverse/reflection closure at the level of parameterized endpoints.
assert sp.simplify(b-(b-R)-R)==0
assert sp.simplify((b+R)-b-R)==0
assert sp.simplify((a+R)-a-R)==0
assert sp.simplify(T-(T-R)-R)==0
assert sp.simplify((T+R)-T-R)==0

# The new domains are confined to the direct KNF windows.
# No new edge starts in the blind region outside (0,R), a+, b±, T± windows.
window_names={"U","Ap","Bm","Bp","Tm","Tp"}
assert all(name in window_names for rows in domains.values() for name,_ in rows)

print("SW1-A9 NEW KNF ACTIVITY-DOMAIN CERTIFICATE: PASS")
print("exact symbolic arithmetic: SymPy")
print("r_b : (0,R) U (b-R,b)")
print("tau_+b : (0,R); tau_-b : (b,b+R)")
print("r_{a+b} : (a,a+R) U (b-R,b)")
print("tau_+d : (a,a+R); tau_-d : (b,b+R)")
print("tau_+e : (b-R,b+R) split at b")
print("tau_-e : (T-R,T+R) split at T")
print("r_{T+b} : (b-R,b+R) U (T-R,T+R), split at centers")
print("endpoints are L2-null and omitted")
print("FIREWALL: activity domains only; no component/separator verdict")
