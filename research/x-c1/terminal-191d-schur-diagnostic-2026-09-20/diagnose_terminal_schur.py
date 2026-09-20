#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math, platform
from pathlib import Path
import numpy as np
from scipy.special import roots_legendre
import scipy

KAPPA=math.log(8*math.pi)+0.5772156649015328606+math.pi/2
WEIGHTS={2:math.log(2)/math.sqrt(2),3:math.log(3)/math.sqrt(3),4:math.log(2)/2,5:math.log(5)/math.sqrt(5),7:math.log(7)/math.sqrt(7)}
ELLS={q:math.log(q) for q in WEIGHTS}

def legendre_all(x,nmax):
    x=np.asarray(x);P=np.empty((x.size,nmax+1));P[:,0]=1.0
    if nmax:P[:,1]=x
    for n in range(1,nmax):P[:,n+1]=((2*n+1)*x*P[:,n]-n*P[:,n-1])/(n+1)
    P*=np.sqrt(2*np.arange(nmax+1)+1)[None,:];return P

def kfun(r):return np.exp(-r/2)/(-np.expm1(-2*r))
def tail_k(R,terms=500):return sum(math.exp(-(2*m+0.5)*R)/(2*m+0.5) for m in range(terms))

def build(a,parity,high_count,nx,nt):
    x,wx=roots_legendre(nx);z,wz=roots_legendre(nt);tmax=math.sqrt(2*a)
    t=.5*tmax*(z+1);wt=.5*tmax*wz;rnodes=t*t;wr=wt*2*t
    low=list(range(2+parity,384+parity,2));high=[384+parity+2*k for k in range(high_count)]
    degs=low+high;carrier=parity;nmax=max(degs);P=legendre_all(x,nmax);ec=P[:,carrier]
    moment=np.cosh(a*x/2) if parity==0 else np.sinh(a*x/2)
    denom=np.sum(wx*ec*moment)/2
    ratios=np.array([(np.sum(wx*P[:,n]*moment)/2)/denom for n in degs])
    Z=P[:,degs]-ec[:,None]*ratios[None,:];G=.5*Z.T@(wx[:,None]*Z);Gamma=np.zeros_like(G)
    for rr,ww in zip(rnodes,wr):
        d=rr/a;xs=x-d;mask=(xs>=-1)&(xs<=1);Ps=np.zeros((x.size,nmax+1))
        if np.any(mask):Ps[mask]=legendre_all(xs[mask],nmax)
        Zs=Ps[:,degs]-Ps[:,carrier,None]*ratios[None,:];C=.5*Z.T@(wx[:,None]*Zs)
        Gamma+=ww*kfun(rr)*(2*G-C-C.T)
    Gamma+=2*tail_k(2*a)*G;Q=Gamma-KAPPA*G
    for q,wq in WEIGHTS.items():
        ell=ELLS[q]
        if ell>=2*a:continue
        d=ell/a;xs=x-d;mask=(xs>=-1)&(xs<=1);Ps=np.zeros((x.size,nmax+1))
        if np.any(mask):Ps[mask]=legendre_all(xs[mask],nmax)
        Zs=Ps[:,degs]-Ps[:,carrier,None]*ratios[None,:];C=.5*Z.T@(wx[:,None]*Zs);Q-=wq*(C+C.T)
    Q=(Q+Q.T)/2;H=Q[191:,191:];Bmix=Q[191:,:191]
    S=Q[:191,:191]-Bmix.T@np.linalg.solve(H,Bmix);eig=np.linalg.eigvalsh((S+S.T)/2);heig=np.linalg.eigvalsh((H+H.T)/2)
    return {"parity":"even" if parity==0 else "odd","a":a,"low_dimension":191,"high_galerkin_dimension":high_count,
      "min_schur_eigenvalue":float(eig[0]),"second_schur_eigenvalue":float(eig[1]),"max_schur_eigenvalue":float(eig[-1]),
      "min_high_eigenvalue":float(heig[0]),"moment_max_abs_ratio":float(np.max(np.abs(ratios)))}

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--nx",type=int,default=900);ap.add_argument("--nt",type=int,default=300);ap.add_argument("--high",type=int,default=32);ap.add_argument("--json");args=ap.parse_args()
    rows=[];B=math.log(5)/2
    for a,name in [(B,"certified_B_calibration"),(1.0,"terminal_a1")]:
        for p in (0,1):
            row=build(a,p,args.high,args.nx,args.nt);row["case"]=name;rows.append(row)
            print(name,row["parity"],"minSchur=",format(row["min_schur_eigenvalue"],".17g"),"minHigh=",format(row["min_high_eigenvalue"],".17g"))
    calibration=[r for r in rows if r["case"]=="certified_B_calibration"];passed=all(r["min_schur_eigenvalue"]>=0 for r in calibration)
    report={"status":"DIAGNOSTIC_ONLY / NO_SIGN_CERTIFICATE","python":platform.python_version(),"numpy":np.__version__,"scipy":scipy.__version__,
      "nx":args.nx,"nt":args.nt,"high_galerkin_dimension":args.high,"rows":rows,"calibration_pass":passed,"sign_interpretation_allowed":passed,
      "verdict":"CALIBRATION_PASSED_DIAGNOSTIC_ONLY" if passed else "CALIBRATION_FAILED_DIRECT_QUADRATURE_NOT_SIGN_SAFE",
      "firewall":"If the B calibration is negative, terminal a=1 signs are raw diagnostics only and MUST NOT be promoted."}
    print("VERDICT",report["verdict"])
    if args.json:Path(args.json).write_text(json.dumps(report,indent=2,sort_keys=True)+"\n",encoding="utf-8")
if __name__=="__main__":main()
