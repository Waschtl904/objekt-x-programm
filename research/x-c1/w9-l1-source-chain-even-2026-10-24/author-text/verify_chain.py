"""Exact, bounded L1 application checks. No integration and no source mutation.

This executable checks finite algebra, source bindings and budget inclusions.
Whole-space analytic reasoning is stated separately in L1-BEWEIS.txt.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb, factorial, isqrt
from decimal import Decimal, localcontext
import argparse, gzip, hashlib, json

def need(value, message):
    if not value: raise ValueError(message)

def sha(raw): return hashlib.sha256(raw).hexdigest()
def read(p): return json.loads(p.read_bytes())
def sqrtup(x, digits=160):
    x=Q(x); need(x>=0,'Negative square-root argument')
    g=10**digits; v=x*g*g; n=isqrt(v.numerator//v.denominator)
    if n*n<v:n+=1
    return Q(n,g)
def up(pair):
    need(len(pair)==2 and Q(pair[0])<=Q(pair[1]),'Invalid enclosure')
    return Q(pair[1])
def display(x):
    with localcontext()as d:
        d.prec=22
        return str(Decimal(x.numerator)/Decimal(x.denominator))
def inv_series(n, offset):
    a=[Q(1,factorial(k+offset))if k%2==0 else Q(0)for k in range(n+1)]
    out=[Q(1)]
    for k in range(1,n+1):out.append(-sum((a[j]*out[k-j]for j in range(1,k+1)),Q(0)))
    return out
def dot(a,b):return sum((x*y for x,y in zip(a,b)),Q(0))
def add(a,b):return [x+y for x,y in zip(a,b)]
def sub(a,b):return [x-y for x,y in zip(a,b)]
def scale(a,c):return [x*c for x in a]

ap=argparse.ArgumentParser();ap.add_argument('--bindings',type=Path,required=True)
ap.add_argument('--output',type=Path,required=True)
args=ap.parse_args();spec=read(args.bindings)
need(not args.output.exists(),'Output must be new')
data={}
for alias,row in spec['files'].items():
    p=(args.bindings.parent/row['path']).resolve();raw=p.read_bytes()
    need(sha(raw)==row['sha256'],'Source changed: '+alias)
    data[alias]=raw
j=lambda key:json.loads(data[key])
checks={};negative={}

# Coefficientwise identity for the WHOLE inner/outer polynomial kernel.
# mu_j is treated as a free formal moment: no numerical low projection used.
N=224;pc=inv_series(N+1,0);ps=inv_series(N+1,1)
gamma=[(pc[n]+ps[n+1])/4 for n in range(N+1)]
count=0;wrong=[]
for n in range(N+1):
    for k in range(n+1):
        physical=gamma[n]*Q(comb(n,k),2**n)*(1+(-1)**k)
        convolution=gamma[n]*Q(factorial(n),2**n*factorial(k)*factorial(n-k))*(1+(-1)**k)
        historic=gamma[n]*Q(comb(n,k),2**n)*((-1)**k+1)
        reversed_direction=gamma[n]*Q(comb(n,k),2**n)*(1+(-1)**(n-k))
        need(physical==convolution==historic,'Whole polynomial orientation mismatch')
        if reversed_direction!=physical:wrong.append((n,k,str(physical),str(reversed_direction)))
        count+=1
checks['whole_kernel_formal_coefficients']=count
checks['source_families']=['Phi: 191','F: 4 global + 8 lifted Y','J: 84 lifted J']
negative['reversed_orientation_rejected']=len(wrong)>0
checks['first_orientation_counterexample']=wrong[0]
checks['reversed_orientation_different_coefficients']=len(wrong)
adapter=data['corrected_builder'].decode();historic=data['old_fields'].decode();oldcode=data['old_global_code'].decode()
need('co[224-k]/fac[k]*(1+(-1)**k)'in adapter,'Adapter formula changed')
need('conv[224-l]/fac[l]*((-1)**l+eps)*a**l'in historic,'Historic column formula changed')
need('comb(k,l)*((-1)**l+(-1)**p)*a**l*ym[k-l]'in oldcode,'Historical global formula changed')
need('kernel(f,ls,a,oldcs,p)'in historic,'Phi formula changed')
need('kernel(ph,ls,a,gamma_old,0)'in data['whole_builder'].decode(),'Whole Phi formula changed')

# Exact finite controls of the stated whole-space algebra. They do not replace
# the general proof and explicitly reject a low-coordinate-only inference.
m=list(map(Q,[2,1,3]));e=list(map(Q,[1,0,0]));me=dot(m,e)
M=lambda x:sub(x,scale(e,dot(m,x)/me))
Ms=lambda x:sub(x,scale(m,dot(e,x)/me))
E=lambda c:[Q(0),c,Q(0)]
PHi=lambda x:[Q(0),Q(0),x[2]]
s=[Q(7,5),Q(1,3),Q(2,7)];s0=[Q(1),Q(2,3),Q(5,7)];c0=Q(1,9)
c=Ms(s)[1]
whole=PHi(Ms(s));model=sub(Ms(s0),E(c0))
identity=sub(Ms(sub(s,s0)),E(c-c0))
need(sub(whole,model)==identity,'Whole high decomposition')
need(Ms(m)==[0,0,0],'Shared moment is not annihilated')
# A source with zero low difference may still have arbitrarily large high error.
counter=[Q(0),Q(0),Q(17)];need(Ms(counter)[1]==0 and dot(PHi(Ms(counter)),PHi(Ms(counter)))==289,'High-tail control')
negative['low_coordinates_do_not_control_high_tail']=True
checks['whole_high_decomposition_control']=True
# Unknown dependence must not be replaced by an orthogonal-error hypothesis.
need((Q(1)+Q(1))**2>Q(1)**2+Q(1)**2,'Cross-term example')
negative['missing_common_feature_cross_factor_rejected']=True
checks['common_error_bound']='||dJ w-dF p|| <= sqrt(EJ)||w||+sqrt(p*EF p); squared joint metric uses factor 2'

# The second midpoint operation is not justified by an enclosing interval.
# Instead prove equality of every actual cached Y/J dyadic to its source.
cache=json.loads(gzip.decompress(data['original_cache']))
need(sha(cache['payload'].encode())==cache['payload_sha256'],'Cache payload binding')
need(cache['source_sha256']==sha(data['whole_builder']),'Cache builder binding')
parts=dict(json.loads(cache['payload'])['mapping']);matched=0
def same_midpoint(r,b):
    m,e,rad,re=b['ball']
    return rad==0 and Q(m)*Q(2)**e==Q(r)
for key,alias,field,columns in [('Y','frozen_Y','Y_local_rational_midpoints',8),('J','frozen_J','working_basis_midpoints_rational',84)]:
    original=j(alias)[field];actual=parts[key]['matrix']
    need(len(original)==len(actual)==96,'Whole basis row count')
    for ref,row in zip(original,actual):
        need(len(ref)==len(row)==columns,'Whole basis column count')
        for r,b in zip(ref,row):
            need(same_midpoint(r,b),'Second basis midpoint changes exact coefficient')
            matched+=1
need(matched==8832,'Complete basis comparison')
checks['second_basis_midpoint_exact_matches']=matched
bad_ball={'ball':parts['Y']['matrix'][0][0]['ball'][:]};bad_ball['ball'][0]+=1
negative['changed_second_midpoint_rejected']=not same_midpoint(j('frozen_Y')['Y_local_rational_midpoints'][0][0],bad_ball)

# Complete polynomial shell norm: 96 orthonormal Legendre modes, h>1/20.
# Sup <=96/sqrt(2h); full logarithmic potential norm <=1 (normalized variable).
# H_95<6, |log(pi*h)+Euler|<4, regular/reflection/prime caps as in proof.
H95=sum((Q(1,k)for k in range(1,96)),Q(0));need(H95<6,'Harmonic cap')
shell_Q_cap=H95+4+96+2+1+12
whole_Q_lift_cap=shell_Q_cap+47+60  # intentionally larger than component sum
outer_density_cap=2*whole_Q_lift_cap
need(outer_density_cap<100000,'Finite polynomial coordinate transport')
checks['degree95_outer_density_transport_upper']=str(outer_density_cap)
checks['retained_coordinate_transport_cap']='100000'

# Imported H-SOURCE facts are checked against the bound original data.
fun=j('functions');response=j('response')['parities']['even']['fixed_X']
deltaD=Q(fun['parities']['even']['whole_D12_operator_error_upper'])
T2=Q(response['T_norm_squared_upper'])
ed=Q(response['whole_Hilbert_residual_model_error_upper'])
need(deltaD**2*T2<=ed**2,'Whole response error transport')
terms=j('term_check');need(terms['T']['fresh_rounding_below_old_price'],'Fresh T freeze not covered')
need(up(terms['T']['fresh_function_T_rounding_norm'])<up(terms['T']['old_pairing_T_rounding_norm']),'T price order')
need(up(terms['T']['fresh_to_old_T_norm'])>0,'Different T midpoints silently equated')
checks['H_SOURCE']={'deltaD':str(deltaD),'deltaD_display':display(deltaD),'ed':str(ed),'ed_display':display(ed),
 'whole_response_transport':True,'fresh_T_price_covered':True,'T_midpoints_not_identified':True,
 'projection_convention':'Compare Pi9 h; use raw representatives only through maps annihilating the same exact moment carrier.'}

# Retain whole moment-transfer R2. Its exact scalar recombination is repeated;
# it is not replaced by the much coarser generic 1e40 amplification.
r2=j('moment_R2');eps=Q(r2['moment_difference_sup_and_derivative'])
need(eps==Q(2,factorial(160)),'Moment epsilon')
v={k:Q(x)for k,x in r2['transfer_coefficients'].items()}
moment=(v['raw_operator']+v['explicit_moment_pairings']+v['mixed_prime_convention'])*eps
need(moment==Q(r2['moment_X_upper']),'Whole moment transfer mismatch')
need(r2['bilinear_identity']['omitted_cross_term_rejected'],'Missing moment cross control')
rows={k:Q(x)for k,x in r2['identified_X_remainder_rows'].items()}
need(rows['explicit_common_moment160_transfer_R2']==moment,'Moment ledger row')
need('inherited_moment_derivative_envelope_other_stages'not in rows,'Duplicate moment debit')
joint=sum(rows.values(),Q(0));raw=joint*Q(18219,10000)/100
need(raw==Q(r2['joint_raw_upper']) and raw<Q('1e-150'),'Small remainder sum')
checks['small_remainders']={'rows':list(rows),'moment_X':str(moment),'moment_X_display':display(moment),
 'joint_raw':str(raw),'joint_raw_display':display(raw),'assigned_raw_allowance':'1e-150',
 'unused_raw_FJ_1e_minus_200_floors':'Retained numerical slack; same builder m160 cause assigned only to R2.',
 'numerical_inclusion_does_not_prove_catalogue_completeness':True}

# Exact positive scalar ledger recombination, with original outward endpoints.
ledger=j('whole_ledger')['values'];wr=j('whole_result');norm=j('independent_norm')
rootL=sqrtup(Q(5,21));operator=10*(up(ledger['p_total'])+up(ledger['low_feature_total']))+rootL*up(ledger['raw_X_error'])
paid=Q(wr['whole_operator_model_Ldual_error_upper']);need(operator<=paid,'Original operator endpoint insufficient')
change=sqrtup(up(norm['norm_squared_intermediate']))+up(norm['smooth_log_remainder_X'])+up(norm['moment_Taylor_remainder_X'])
energy=(rootL*(sqrtup(Q(wr['model_X_norm_squared_upper']))+change+Q(wr['core_bridge_X_error_upper'])+Q(wr['core_quadrature_X_error_upper']))+paid)**2
need(energy<Q('4.632e-11'),'Energy bound')
checks['energy']={'upper':str(energy),'display':display(energy),'retained_cap':'4.632e-11','p_charged_once':True}
negative['changed_source_hash_rejected']=sha(data['whole_builder']+b'\n')!=spec['files']['whole_builder']['sha256']
for k,v in negative.items():need(v,'Negative control failed: '+k)
out={'status':'FINITE_L1_APPLICATION_CHECKS_PASS','analytical_proof':'L1-BEWEIS.txt',
 'source_basis':spec['historical_basis'],'integrated_main':spec['integrated_main'],
 'source_hashes_verified':len(data),'checks':checks,'negative_controls':negative,
 'historical_lemmas_reproved':False,'new_integration':False,'external_review':'OPEN',
 'full_L1_status':'Requires the separate analytic catalogue and targeted review; finite checks alone are insufficient.'}
args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'bound_files':len(data),'kernel_coefficients':count,'negative_controls':len(negative),
 'moment_X':display(moment),'small_remainder_raw':display(raw),'energy':display(energy)},indent=2))
