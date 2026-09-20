#!/usr/bin/env python3
from fractions import Fraction

EPS=Fraction(1,10**26)
S_UP=Fraction(23,2)
ETA=EPS/(S_UP+EPS)

checks=[]
def check(name,cond):
    if not cond:
        raise SystemExit("FAIL "+name)
    checks.append(name)

check("physical epsilon positive", EPS>0)
check("mediator envelope positive", S_UP>0)
check("eta identity", ETA*(S_UP+EPS)==EPS)
check("strict terminal reserve exceeds 1e-28", ETA>Fraction(1,10**28))
check("terminal reserve below one", ETA<1)

factor=1+S_UP/EPS
check("coercivity conversion identity", ETA*factor==1)

print("PASS",len(checks),"C1d quantitative consistency checks")
for x in checks:
    print("PASS",x)
print("ETA =",ETA)
print("No local square-root intertwining is used.")
