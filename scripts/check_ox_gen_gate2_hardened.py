# -*- coding: utf-8 -*-
"""Gate 2 (OX-GRAM) hardening checker, Arb prec 512.

This is a hardened version of the external Gate-2 checker. It keeps the same
Dirichlet-basis and Cholesky logic, but closes the interval-firewall gaps:

1. the Bernoulli truncation for r1'' gets an explicit rigorous tail ball;
2. the prime-power cutoff n < exp(2a) is decided only by Arb comparisons;
3. the logarithmic endpoint bound contains no float conversion;
4. Cholesky accepts a pivot only via the direct proof-oriented Arb test s>0.

Scope: a in {1/2, 4/5, 1}, hence exp(2a) < 8.
No Registry promotion and no RH/Object-X claim.
"""
import sys, time
from flint import ctx, arb, acb
import sympy as sp
from mpmath import mp, mpf, matrix as mpmat, eigsy

ctx.prec = 512
PI, C0 = arb.pi(), arb.const_euler()
TWOAP1 = (2*arb.pi()).log() + C0


def kk(m,a): return PI*m/(2*a)
def ph(m,a): return kk(m,a)*a


def vm_upto(X):
    """Prime powers n<X with every inclusion/exclusion decided in Arb.

    The present certificate is scoped to a<=1, so X=e^(2a)<e^2<8.
    We enumerate a safe finite superset n<=16 and use Arb comparisons only.
    """
    if not (X < arb(8)):
        raise RuntimeError("vm_upto hardening scope requires X<8 (a<=1)")
    primes=[]
    for p in range(2,17):
        if all(p % q for q in primes if q*q <= p):
            primes.append(p)
    out={}
    for p in primes:
        t=p
        while t<=16:
            tb=arb(t)
            if tb < X:
                out[t]=arb(p).log()
            elif tb > X:
                break
            else:
                raise RuntimeError(f"uncertified prime-power cutoff at n={t}, X={X}")
            t*=p
    return out


def _ic(m,c,lo,hi,z):  return (hi-lo)*c.cos() if z else ((m*hi+c).sin()-(m*lo+c).sin())/m
def _is(m,c,lo,hi,z):  return (hi-lo)*c.sin() if z else ((m*lo+c).cos()-(m*hi+c).cos())/m
def sinsin(ki,ci,kj,cj,lo,hi,same):
    return (_ic(ki-kj,ci-cj,lo,hi,same) - _ic(ki+kj,ci+cj,lo,hi,False))/2


def SHp(i,j,tau,a):
    ki,kj=acb(kk(i,a)),acb(kk(j,a))
    return sinsin(ki,acb(ph(i,a)),kj,kj*(acb(a)+tau),acb(-a),acb(a)-tau,i==j)


def SHm(i,j,tau,a):
    ki,kj=acb(kk(i,a)),acb(kk(j,a))
    return sinsin(ki,acb(ph(i,a)),kj,kj*(acb(a)-tau),acb(-a)+tau,acb(a),i==j)


def IP(i,j,a):
    return (arb(a) if i==j else arb(0))


def log_form(i,j,a):
    """The positive logarithmic difference form (log|D|-type geometry)."""
    ki,kj=acb(kk(i,a)),acb(kk(j,a)); pi_,pj_=acb(ph(i,a)),acb(ph(j,a)); same=(i==j)
    def f(u,_):
        lo,hi=acb(-a)+u,acb(a)
        t  = sinsin(ki,pi_,           kj,pj_,           lo,hi,same)
        t -= sinsin(ki,pi_,           kj,pj_-kj*u,      lo,hi,same)
        t -= sinsin(ki,pi_-ki*u,      kj,pj_,           lo,hi,same)
        t += sinsin(ki,pi_-ki*u,      kj,pj_-kj*u,      lo,hi,same)
        return t/u
    d=arb(2)**(-60)
    v=acb.integral(f,acb(d),acb(2*a),abs_tol=arb(2)**-300,rel_tol=arb(2)**-300,eval_limit=10**7,depth_limit=400).real
    err=kk(i,a)*kk(j,a)*2*a*d*d/2
    return (v+arb(0,err))/2


def Mterm(i,j,a):
    ki,kj,pi_,pj_=kk(i,a),kk(j,a),ph(i,a),ph(j,a); e=arb(2)**(-50)
    f=lambda z,_:(acb(a*a)-z*z).log()*(acb(ki)*z+acb(pi_)).sin()*(acb(kj)*z+acb(pj_)).sin()
    v=acb.integral(f,acb(-a+e),acb(a-e),abs_tol=arb(2)**-300,rel_tol=arb(2)**-300,eval_limit=10**7,depth_limit=400).real
    B=2*ki*kj*e*e*(-(2*a*e).log()+1)
    return -(v+arb(0,B))/2


def R0(i,j,a):
    def mom(kind,m):
        k,p=acb(kk(m,a)),acb(ph(m,a))
        f=lambda z,_:((z/2).cosh() if kind=='ch' else (z/2).sinh())*(k*z+p).sin()
        return acb.integral(f,acb(-a),acb(a),abs_tol=arb(2)**-300,rel_tol=arb(2)**-300,eval_limit=10**7,depth_limit=400).real
    return -2*(mom('ch',i)*mom('ch',j)-mom('sh',i)*mom('sh',j))


NB=340; _B=[arb(0)]*(NB+1)
for n in range(1,NB+1):
    q=sp.Rational(sp.bernoulli(n,sp.Rational(1,4))); _B[n]=arb(int(q.p))/arb(int(q.q))
_C=[None]*(NB+1); f=arb(1); pw=arb(1)
for n in range(1,NB+1):
    f=f*n; pw=pw*(-2); _C[n]=_B[n]*pw/(2*f)

_RTAIL=(PI*PI/12)*(arb(2)/PI)**(NB+1)/(1-arb(2)/PI)


def r1pp_partial(u):
    tot=u*0; p=u**0
    for n in range(1,NB+1):
        tot=tot+acb(_C[n])*p; p=p*u
    return tot


def R1(i,j,a):
    f=lambda u,_: r1pp_partial(u)*(SHp(i,j,u,a)+SHm(i,j,u,a))
    v=acb.integral(f,acb(0),acb(2*a),abs_tol=arb(2)**-300,rel_tol=arb(2)**-300,eval_limit=10**7,depth_limit=400).real
    return v + arb(0, 4*a*a*_RTAIL)


def build(a,N,W,ca):
    G=[[arb(0)]*N for _ in range(N)]; Nm=[[arb(0)]*N for _ in range(N)]
    for i in range(1,N+1):
        for j in range(i,N+1):
            if (i%2)!=(j%2):
                continue
            ip=IP(i,j,a)
            P=arb(0)
            for n,lp in W.items():
                w=lp/arb(n).sqrt(); ln=acb(arb(n).log())
                P += w*(2*ip - SHp(i,j,ln,a).real - SHm(i,j,ln,a).real)
            g = log_form(i,j,a)+Mterm(i,j,a)+P
            nn= ca*ip + R0(i,j,a) + R1(i,j,a)
            G[i-1][j-1]=G[j-1][i-1]=g
            Nm[i-1][j-1]=Nm[j-1][i-1]=nn
    return G,Nm


def cholesky_certified(Q,idx):
    """PASS only when every pivot ball is rigorously contained in (0,infinity)."""
    n=len(idx); L=[[arb(0)]*n for _ in range(n)]; piv=[]
    for i in range(n):
        for j in range(i+1):
            s=Q[idx[i]][idx[j]]
            for k in range(j):
                s=s-L[i][k]*L[j][k]
            if i==j:
                if not (s > 0): return False,piv,i
                piv.append(s); L[i][i]=s.sqrt()
            else:
                L[i][j]=s/L[j][j]
    return True,piv,None


def gen_spec(Q,G,idx,dps=80):
    """Midpoint diagnostic only; Cholesky above is the interval certificate."""
    mp.dps=dps; n=len(idx)
    Qm=mpmat(n,n); Gm=mpmat(n,n)
    for p in range(n):
        for q in range(n):
            Qm[p,q]=mpf(Q[idx[p]][idx[q]].mid().str(40,radius=False))
            Gm[p,q]=mpf(G[idx[p]][idx[q]].mid().str(40,radius=False))
    Ev,Vg=eigsy(Gm, eigvals_only=False)
    Hi=mpmat(n,n)
    for p in range(n):
        for q in range(n):
            s=mpf(0)
            for r in range(n): s+=Vg[p,r]*Vg[q,r]/mp.sqrt(Ev[r])
            Hi[p,q]=s
    Mm=Hi*Qm*Hi
    w,V=eigsy(Mm, eigvals_only=False)
    k=min(range(n), key=lambda t: w[t])
    vec=[V[p,k] for p in range(n)]
    coord=[sum(Hi[p,q]*vec[q] for q in range(n)) for p in range(n)]
    nrm=mp.sqrt(sum(c*c for c in coord)) or mpf(1)
    return w[k], max(w), [c/nrm for c in coord], Ev


if __name__=="__main__":
    Nmax=int(sys.argv[1]) if len(sys.argv)>1 else 14
    which=sys.argv[2] if len(sys.argv)>2 else 'all'
    rad={'a':[arb(1)/2],'b':[arb(8)/10],'c':[arb(1)],'all':[arb(1)/2,arb(8)/10,arb(1)]}[which]
    print(f"### GATE 2 HARDENED -- Arb prec {ctx.prec}, Dirichletbasis N<={Nmax}")
    print(f"### 2A+1 = {TWOAP1.str(16,radius=False)}")
    print(f"### uniform r1pp tail |u|<=2 after NB={NB}: <= {_RTAIL.str(8,radius=False)}")
    for a in rad:
        W=vm_upto((2*a).exp()); Aa=2*sum((lp/arb(n).sqrt() for n,lp in W.items()),arb(0))
        ca=Aa+TWOAP1
        print("="*104); print(f"a = {a.str(6,radius=False)}   n<e^(2a): {sorted(W)}   A_a = {Aa.str(16,radius=False)}   c_a = {ca.str(16,radius=False)}")
        t0=time.time(); G,Nm=build(a,Nmax,W,ca); print(f"  [Matrizen {Nmax}x{Nmax} in {time.time()-t0:.0f}s]")
        Q=[[G[i][j]-Nm[i][j] for j in range(Nmax)] for i in range(Nmax)]
        maxrad=max(float(Q[i][j].rad()) for i in range(Nmax) for j in range(Nmax))
        print(f"  max Ballradius der Q-Eintraege: {maxrad:.2e}")
        for nm,par in (("gerade (m ungerade)",1),("ungerade (m gerade)",0)):
            full=[m-1 for m in range(1,Nmax+1) if m%2==par]
            print(f"  --- Sektor {nm}, dim {len(full)}")
            for d in range(1,len(full)+1):
                idx=full[:d]
                ok,piv,fail=cholesky_certified(Q,idx)
                nu,numax,vec,Gev=gen_spec(Q,G,idx)
                tag="Q>0 ZERTIFIZIERT" if ok else f"Cholesky-FAIL @ Pivot {fail}"
                print(f"    dim {2*d-1+(1-par):>3} (d={d}): nu_min={float(nu):+.6e}  mu_max={float(1-nu):.18f}  {tag}")
                if d==len(full):
                    print(f"      Extremalrichtung (Koeff. phi_m, m={[f for f in range(1,Nmax+1) if f%2==par]}):")
                    print("        "+"  ".join(f"{float(c):+.4f}" for c in vec))
        sys.stdout.flush()
