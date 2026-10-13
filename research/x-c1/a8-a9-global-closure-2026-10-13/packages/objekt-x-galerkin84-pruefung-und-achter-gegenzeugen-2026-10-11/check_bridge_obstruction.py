"""Exact audit of the proposed uniform Q8 multipliers; standard library only.

Usage: python check_bridge_obstruction.py --root EXTRACTED_GALERKIN_PACKAGE --out OUT
The original package's reproduce.py must have unpacked its bound predecessors.
All operator inequalities are inherited, not independently re-proved here.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse, hashlib, json

def mat(a): return [[F(x) for x in r] for r in a]
def tr(a): return [list(r) for r in zip(*a)]
def dot(x,y): return sum((a*b for a,b in zip(x,y)),F(0))
def mv(a,x): return [dot(r,x) for r in a]
def mm(a,b): return [[dot(r,c) for c in zip(*b)] for r in a]
def add(a,b,t=1): return [[x+t*y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(a,t): return [[t*x for x in r] for r in a]
def form(a,x): return dot(x,mv(a,x))
def block(a,i,j): return [[a[k][l] for l in j] for k in i]
def ident(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def inverse(a):
    n=len(a); w=[r[:]+e for r,e in zip(a,ident(n))]
    for j in range(n):
        assert w[j][j]
        d=w[j][j]; w[j]=[v/d for v in w[j]]
        for i in range(n):
            if i!=j:
                t=w[i][j];w[i]=[v-t*u for v,u in zip(w[i],w[j])]
    ans=[row[n:] for row in w];assert mm(a,ans)==ident(n)
    return ans
def sqrt_up(x,digits=60):
    assert x>=0
    den=10**digits; n=isqrt(x.numerator*den*den//x.denominator)
    if F(n*n,den*den)<x: n+=1
    ans=F(n,den); assert ans*ans>=x
    return ans
def upper_matrix(a):
    n=len(a); mid=[[sum(map(F,v))/2 for v in row] for row in a]
    out=[[(mid[i][j]+mid[j][i])/2 for j in range(n)] for i in range(n)]
    for i in range(n):
        out[i][i]+=sum((F(a[i][j][1])-F(a[i][j][0]))/2+abs(mid[i][j]-mid[j][i])/2 for j in range(n))
    return out
def lower_matrix(a): return scale(upper_matrix([[[-F(v[1]),-F(v[0])] for v in row] for row in a]),-1)
def positive(a):
    n=len(a); assert a==tr(a)
    l=ident(n); piv=[]
    for j in range(n):
        d=a[j][j]-sum(l[j][k]**2*piv[k] for k in range(j))
        assert d>0,(j,d)
        piv.append(d)
        for i in range(j+1,n): l[i][j]=(a[i][j]-sum(l[i][k]*l[j][k]*piv[k] for k in range(j)))/d
    return n
def serial(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,(tuple,list)): return [serial(v) for v in x]
    if isinstance(x,dict): return {k:serial(v) for k,v in x.items()}
    return x
def ceil_decimal(x,digits=9):
    d=10**digits
    return F(-((-x.numerator*d)//x.denominator),d)

def replay(data):
    cases=[]
    for c in data['cases']:
        N,P,Q,U,El,Dz,Dy,C,M=(mat(c[k]) for k in ['N','P','Q8','old_energy_upper','old_energy_lower','D_z_upper','D_Y_upper','C_U_centre','C_error_metric'])
        eps=F(c['C_error_norm_upper']); k=F(c['proposed_multiplier']); y=list(map(F,c['y']))
        x=[-v for v in mv(P,y)]; z=x+y
        assert [a+b for a,b in zip(x,mv(P,y))]==[0]*4
        assert dot(y,y)==1
        positive(Q);positive(M);positive(El);positive(add(U,El,-1))
        # B_direct = C_U + U_zY + error, ||M^(-1/2) error|| <= eps.
        B=add(C,block(U,range(4),range(4,12)))
        cross_error=2*eps*sqrt_up(form(M,x)*dot(y,y))
        actual_schur_upper=form(Dz,x)+2*dot(x,mv(B,y))+form(Dy,y)-form(El,z)+cross_error
        q=form(Q,y); target=k*q
        assert q>0 and actual_schur_upper<target
        # Independent regrouping at the common old-energy upper endpoint.
        Uzz=block(U,range(4),range(4)); Uyy=block(U,range(4,12),range(4,12))
        alt=form(add(Dz,Uzz,-1),x)+2*dot(x,mv(C,y))+form(add(Dy,Uyy,-1),y)+form(add(U,El,-1),z)+cross_error
        assert alt==actual_schur_upper
        # The old Young step has essentially no recoverable reserve.
        Kl=mat(c['K_lower']); Gamma=mat(c['Gamma_R_upper'])
        small=F(1,10**35)
        young_upper_pivots=positive(add(scale(Q,small),add(Kl,Q,-1),-1))
        remainder=add(add(Kl,scale(Gamma,2),-1),Q,-1)
        assert remainder==tr(remainder)
        assert all(remainder[i][i]>=sum(abs(remainder[i][j]) for j in range(8) if i!=j) for i in range(8))
        limit=ceil_decimal(actual_schur_upper/q)
        assert actual_schur_upper/q<=limit<k
        cases.append({'parity':c['parity'],'status':'PROPOSED_UNIFORM_ACTUAL_FINITE_BRIDGE_REFUTED_CONDITIONAL_ON_BOUND_INPUTS',
          'y':y,'x_equals_minus_P_y':x,'proposed_multiplier':k,
          'Q8_ray':q,'actual_finite_Schur_upper_on_ray':actual_schur_upper,
          'full_cross_error_charge':cross_error,'proposed_lower_value':target,
          'strict_contradiction_gap':target-actual_schur_upper,
          'upper_quotient':actual_schur_upper/q,'upper_quotient_display_rational':limit,
          'two_exact_regroupings_agree':True,
          'K_lower_minus_Q8_le_relative_Q8':small,'positive_pivots_for_Young_loss_upper':young_upper_pivots,
          'negative_actual_schur_witness':False,'full_remainder_certified':False})
    return serial({'status':'PASS_EXACT_UNIFORM_BRIDGE_OBSTRUCTION','cases':cases,
                   'new_operator_integrations':False,'inherited_operator_bounds_assumed':True,
                   'external_mathematical_review':False,'full_remainder_certified':False})

def build(root):
    fin=root/'work/inherited/Objekt-X-Endlicher-Schuranschluss-2026-10-09'
    paths={'schur':fin/'work/gamma-low-2026-10-09/SCHUR_SHELL_TIGHT_4096.json',
       'response':fin/'work/gamma-low-2026-10-09/RESPONSE_TIGHT_4096.json',
       'four':fin/'work/remainder-integration-check-v2/originals/eight-source/expected/4096/RESULT.json',
       'bridge':root/'work/inherited/Objekt-X-Unendlicher-Rest-Vergleich-2026-10-09/work/infinite-tail-2026-10-09/FINITE_BRIDGE.json'}
    d={k:json.loads(p.read_bytes()) for k,p in paths.items()}; cases=[]
    for p,(parity,j,k) in enumerate([('even',4,F(111,100)),('odd',1,F(129,100))]):
        s=d['schur']['cases'][p]; b=d['response']['blocks'][p]; br=d['bridge']['cases'][p+2]; four=d['four']['blocks'][p]
        U,El=mat(b['joint_upper_rational']),mat(b['joint_lower_rational'])
        assert add(U,El,-1)==mat(b['joint_difference_rational'])
        assert s['M_endpoint']==br['N'] and s['P_rational']==br['P']
        assert add(lower_matrix(four['D_lower']),block(U,range(4),range(4)),-1)==mat(br['N'])
        # Reconstruct the cross midpoint and its complete error, rather than trusting the Schur record.
        C0=[[sum(map(F,v))/2 for v in row] for row in b['C_signed_model_centre']]
        C=add(C0,scale(block(add(U,El,-1),range(4),range(4,12)),F(-1,2)))
        assert C==mat(s['C_endpoint_midpoint'])
        # Rebuild the additional interval rounding charge as in the inherited proof.
        eps=F(s['C_model_error_M_norm'])
        rad2=sum(((F(v[1])-F(v[0]))/2)**2 for row in b['C_signed_model_centre'] for v in row)
        Mi=inverse(mat(b['M_minus_lower_rational']))
        assert eps==F(b['C_centre_additional_model_error_norm_upper'])+sqrt_up(sum(Mi[i][i] for i in range(4))*rad2,45)
        cases.append({'parity':parity,'N':br['N'],'P':br['P'],'Q8':br['Q8'],
          'old_energy_upper':U,'old_energy_lower':El,'D_z_upper':upper_matrix(four['D_upper']),
          'D_Y_upper':s['D_Y_upper'],'C_U_centre':C,'C_error_metric':b['M_minus_lower_rational'],
          'C_error_norm_upper':eps,'K_lower':s['K_lower'],'Gamma_R_upper':s['Gamma_R_upper'],
          'proposed_multiplier':k,'y':[F(i==j) for i in range(8)]})
    return serial({'operator_hypotheses':['old_energy_lower <= E_old <= old_energy_upper',
       'D_zz <= D_z_upper','D_YY <= D_Y_upper',
       '||M^(-1/2)(D_zY-U_zY-C_U_centre)|| <= C_error_norm_upper'],
       'sources':{k:{'path':str(p.relative_to(root)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for k,p in paths.items()},'cases':cases})

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path);ap.add_argument('--out',type=Path,default=Path('.'));args=ap.parse_args()
    args.out.mkdir(parents=True,exist_ok=True); ip=args.out/'BRIDGE_OBSTRUCTION_INPUT.json'; op=args.out/'BRIDGE_OBSTRUCTION.json'
    if args.root:
        data=build(args.root.resolve());ip.write_text(json.dumps(data,indent=2)+'\n')
    else: data=json.loads(ip.read_bytes())
    result=replay(data)
    if not args.root and op.exists(): assert result==json.loads(op.read_bytes())
    else: op.write_text(json.dumps(result,indent=2)+'\n')
    for c in result['cases']:
        print(c['parity'], 'actual Schur / Q8 <=', c['upper_quotient_display_rational'], '<',c['proposed_multiplier'])
    print(result['status'])
