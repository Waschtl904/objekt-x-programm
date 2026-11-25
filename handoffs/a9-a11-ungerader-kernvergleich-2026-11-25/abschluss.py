"""Exact rational full two-source endpoint from the directed field and finite prices."""
import argparse
import json
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path
from endpunkte import check, read

def sqrt_up(x):
    assert x >= 0
    scale=10**45
    n=isqrt(x.numerator*scale**2//x.denominator)
    n+=int(n*n*x.denominator<x.numerator*scale**2)
    result=Q(n,scale)
    assert result**2>=x
    return result

def decimal(x,places,upper):
    scaled=x*10**places
    n=-((-scaled.numerator)//scaled.denominator) if upper else scaled.numerator//scaled.denominator
    assert n>=0
    s=str(n).zfill(places+1)
    return s[:-places]+"."+s[-places:]

def certify(folder,old_s,old_e):
    check(folder,old_s,old_e)
    costs=read(folder/"ENERGIE.json")
    features=costs["residual_features"]
    P=Q(features["P_operator_upper"])
    beta=Q(20209999981781,182190000000000)
    c=Q(6967,10**6)
    assert 0<c<1 and beta>0
    def record(label,name):
        return read(folder/(label.upper()+"_"+name+".json"))
    err={}
    runs={}
    for key in ("e","s"):
        inside,left,right=[record(key,k) for k in ("interior","left","right")]
        assert len(inside["panels"])==11 and left["includes_endpoint"] and right["includes_endpoint"]
        assert {d["cache_sha256"] for d in (inside,left,right)}=={inside["cache_sha256"]}
        covered=max(Q(inside["interior_model_X_squared_upper"]),
                    sum(Q(row["upper"]) for row in inside["panels"]))
        X=covered+Q(left["X_squared_upper"])+Q(right["X_squared_upper"])
        physical=sqrt_up(Q(5,21)*X)+Q(record(key,"core")["dual_norm_upper"])+Q(record(key,"moment")["combined_dual"])+Q(record(key,"quelle")["low_solution_dual"])
        F,J=(Q(features[key][k]["norm_upper"]) for k in ("F","J"))
        # Eliminate F in the upper comparison inherited from Q_o.
        # L[J,J] <= 8 I, ||L^(-1/2) a* K_o^(-1/2)|| <= 5.
        w=physical+5*F
        z=J+sqrt_up(8*P)*5*F
        price=F**2+(w*w/beta+z*z+2*sqrt_up(c/beta)*w*z)/(1-c)
        runs[key]={"raw_model_norm_squared_upper":decimal(X,20,True),
                   "physical_T_dual_norm_upper":decimal(physical,15,True),
                   "whole_residual_energy_upper":decimal(price,20,True)}
        err[key]=price
    assert err["e"]<Q("6.680e-12") and err["s"]<Q("5.325e-7")
    k0,k1=map(Q,read(folder/"MISCHBUDGET.json")["mixed"])
    f0,f1=map(Q,costs["trial_mixed"]["price"])
    aa=Q(read(old_e)["K_P"][0])-Q(costs["trial_e"]["price"][1])-err["e"]
    bb=Q(read(old_s)["K_P_interval"][0])-Q(costs["trial_s"]["price"][1])-err["s"]
    zz=max(abs(k0-f1),abs(k1-f0))+sqrt_up(err["e"]*err["s"])
    det=aa*bb-zz**2
    assert aa>Q("9.7719e-8") and bb>Q(".00185697") and det>Q("3.16512e-11")
    he,hs=Q("3e-9"),Q("1e-4")
    future=(aa-he)*(bb-hs)-(zz+sqrt_up(he*hs))**2
    assert aa>he and bb>hs and future>Q("2.9004e-12")
    return dict(status="AUTHOR_DERIVED_CONDITIONAL_POSITIVE_FIXED_ODD_TWO_SPACE",residuals=runs,
                S_ee_lower=decimal(aa,18,False),S_ss_lower=decimal(bb,16,False),
                absolute_S_es_upper=decimal(zz,17,True),determinant_lower=decimal(det,22,False),
                additional_high_coupling_sufficient={"e_upper":"3e-9","s_upper":"1e-4","proved":False},
                high_block_inherited=True,two_space_plus_high_certified=False,
                full_quotient_certified=False,U11_constructed=False,point4_closed=False,external_review="OPEN")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("previous_s",type=Path)
    p.add_argument("previous_e",type=Path)
    p.add_argument("--data",type=Path,default=Path(__file__).parent)
    p.add_argument("--output",type=Path)
    args=p.parse_args()
    output=json.dumps(certify(args.data,args.previous_s,args.previous_e),indent=2)+"\n"
    if args.output:
        args.output.write_text(output,encoding="utf8")
    print(output)
