# -*- coding: utf-8 -*-
"""Run the hardened finite-window Suzuki normalization gate on one radius.

Usage:
  python scripts/run_ox_gen_normalization_hardened.py 2000 a
  python scripts/run_ox_gen_normalization_hardened.py 2000 b
  python scripts/run_ox_gen_normalization_hardened.py 2000 c

where a=1/2, b=4/5, c=1.
"""
import sys, time
from flint import arb
import ox_gen_gate_norm_hardened as g

Z=float(sys.argv[1]) if len(sys.argv)>1 else 2000.0
PAIRS=[(0,0),(0,2),(2,2),(1,1)]
MIX=[(0,1),(1,2)]
key=sys.argv[2] if len(sys.argv)>2 else 'a'
AL={'a':[arb(1)/2],'b':[arb(8)/10],'c':[arb(1)]}[key]

print(f"### Hardened normalization gate, Arb prec {g.ctx.prec} Bit, Z={Z}")
print(f"### 2A+1 = log(2pi)+C0 = {g.fmt(g.TWOAP1)}")
print(f"### uniform r1pp tail |u|<=2 after NB={g.NB}: <= {g._RTAIL.str(8,radius=False)}")

for a in AL:
    W=g.vm_upto((2*a).exp())
    Aa=2*sum((lp/arb(n).sqrt() for n,lp in W.items()),arb(0))
    print('='*104)
    print(f"a={g.fmt(a)}  n<e^(2a): {sorted(W)}  A_a^Zhu={g.fmt(Aa)}  c_a={g.fmt(Aa+g.TWOAP1)}")
    Wp=g.mk_Wprime(W)
    for i,j in PAIRS+MIX:
        t0=time.time()
        ip=g.IP(i,j,a); Lr=g.L_real(i,j,a); Tr,_,P=g.prime_blocks(i,j,a,W)
        r0=g.R0(i,j,a); r1=g.R1(i,j,a)
        ipF=g.fint(g.W_one,i,j,a,Z,g.mk_tail('one'))
        LF=g.fint(g.W_log,i,j,a,Z,g.mk_tail('log'),logw=True)
        TrF=g.fint(Wp,i,j,a,Z,g.mk_tail('bnd',Aa))
        r0F=g.fint(lambda z:g.W_r0(z,a),i,j,a,Z,g.mk_tail('loglike'),logw=True)
        r1F=g.fint(g.W_r1,i,j,a,Z,g.mk_tail('loglike'),logw=True)
        psF=g.fint(g.W_psi,i,j,a,Z,g.mk_tail('loglike'),logw=True)
        Qr=Lr+P-(Aa+g.TWOAP1)*ip-r0-r1
        Qf=psF-TrF-r0F
        tag='MIX' if (i,j) in MIX else 'same parity'
        print(f"--- (i,j)=({i+1},{j+1}) {tag} [{time.time()-t0:.0f}s]")
        print(f"  A  <v,w>  d {g.fmt(ip-ipF)}")
        print(f"  B  L_a    d {g.fmt(Lr-LF)}")
        print(f"  C  Tr     d {g.fmt(Tr-TrF)}")
        print(f"  C2 P_a    d {g.fmt(P-(Aa*ip-Tr))}")
        print(f"  D  R0     d {g.fmt(r0-r0F)}")
        print(f"  E  R1     d {g.fmt(r1-r1F)}")
        print(f"  F  Q      RESID {g.fmt(Qr-Qf)}")
        sys.stdout.flush()
