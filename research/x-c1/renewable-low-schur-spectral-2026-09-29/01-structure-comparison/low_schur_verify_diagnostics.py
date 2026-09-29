"""Verify exact sign witnesses and interval evaluations of explicit directions.

The physical form evaluation is conditional on the already published model
error inequalities. It supplies no inter-chamber renewal theorem.
"""
from pathlib import Path
from fractions import Fraction
import argparse,gzip,hashlib,json,sys
from flint import arb,arb_mat,fmpq,ctx
sys.set_int_max_str_digits(100000)
p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--diagnostics',type=Path,required=True)
p.add_argument('--vectors',type=Path,required=True);p.add_argument('--precision-check',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
a=p.parse_args();ctx.prec=768;scale=10**100
d=json.loads(a.diagnostics.read_bytes());vs=json.loads(a.vectors.read_bytes());other=json.loads(a.precision_check.read_bytes())
for path,digest in d['input_sha256'].items():assert hashlib.sha256((a.repo/path).read_bytes()).hexdigest()==digest,path
def ball(pair):
    lo,hi=map(int,pair);assert lo<=hi
    return arb(fmpq(lo+hi,2*scale))+arb(0,arb(fmpq(hi-lo,2*scale)))
def dot(x,y):return (x.transpose()*y)[0,0]
def decimal_ball(value):
    q=Fraction(value);return arb(fmpq(q.numerator,q.denominator))
def upper_fraction(v,digits=85):
    s=10**digits;num=int((v.upper()*s).ceil().unique_fmpz());return str(Fraction(num,s))
evaluations={};lower_matrices={}
for name,relative,receipt in [
 ('A8','first-chamber-o8-o9-2026-09-27/o8-rechenstand','reserve_refined'),
 ('A9','chambers-through-a11-2026-09-28/a9','reserve_results'),
 ('A11','chambers-through-a11-2026-09-28/a11','preconditioned_results')]:
    folder=a.repo/'research/x-c1'/relative
    model=json.loads(gzip.decompress((folder/(name.lower()+'_model.json.gz')).read_bytes()))
    result=json.loads((folder/(receipt+'.json')).read_bytes());eL=arb(fmpq(result['low_form_error_exact']))
    lower_stem='reserve_refined' if name=='A8' else 'reserve_results'
    lower=json.loads(gzip.decompress((folder/(lower_stem+'_lower_matrices.json.gz')).read_bytes()))
    for parity in ('even','odd'):
        key=name+'-'+parity;vdata=vs[key+'-1'];v=arb_mat([[decimal_ball(c)] for c in vdata['coefficients']])
        lower_matrices[key]=lower['parities'][parity]['lower_matrix']
        L=arb_mat([[ball(x) for x in row] for row in model['parities'][parity]['A']])
        vnorm=dot(v,v);lq=dot(v,L*v);actual=lq+arb(0,(eL*vnorm).upper())
        pi=int(parity=='odd')
        carrier=-sum((v[i,0]*arb(2*k+1).sqrt()*ball(model['raw_low_moments'][k])
                     for i,k in enumerate(vdata['degrees'])),arb(0))/(arb(2*pi+1).sqrt()*ball(model['raw_low_moments'][pi]))
        normsq=vnorm+carrier*carrier;assert normsq>0
        physical=actual/normsq
        assert physical>0
        evaluations[key]={'direction':'explicit rational decimal coefficient vector in critical_vectors.json',
          'status':'DIRECTED_EVALUATION_CONDITIONAL_ON_PUBLISHED_MODEL_ERROR_BOUND',
          'physical_form_rayleigh_interval':physical.str(25),'physical_form_rayleigh_upper_exact':upper_fraction(physical),
          'low_model_rayleigh_interval':(lq/vnorm).str(25),'source_norm_squared_interval':normsq.str(25)}
signs={}
for key,cmp in d['reference_comparisons'].items():
    rows=cmp['diagonal_witnesses'];negative=rows[0];positive=rows[1]
    left,right=key.split('->');aa,bb=lower_matrices[left],lower_matrices[right]
    for witness in rows:
        index=(witness['degree']-2-int(left.endswith('odd')))//2
        actual=[int(bb[index][index][0])-int(aa[index][index][1]),
                int(bb[index][index][1])-int(aa[index][index][0])]
        assert actual==list(map(int,witness['interval_numerators']))
        assert int(witness['denominator'])==scale
    assert int(negative['interval_numerators'][1])<0
    assert int(positive['interval_numerators'][0])>0
    signs[key]={'conclusion':'INDEFINITE_DIFFERENCE_IN_REFERENCE_COEFFICIENTS',
                'negative_degree':negative['degree'],'positive_degree':positive['degree']}
stability=[]
for j in range(3):
    x=Fraction(d['cases']['A11-even']['modes'][j]['midpoint_eigenvalue_approx'])
    y=Fraction(other['cases']['A11-even']['modes'][j]['midpoint_eigenvalue_approx'])
    relative=abs(x-y)/abs(x);assert relative<Fraction(1,10**60)
    stability.append(float(relative))
report={'status':'DIAGNOSTIC_VERIFICATION_PASS','source_commit':d['source_commit'],
  'source_input_hashes_verified':len(d['input_sha256']),'physical_direction_evaluations':evaluations,
  'exact_interval_sign_checks':signs,'768_vs_1024_bit_A11_even_relative_differences':stability,
  'does_not_prove':['General renewable low positivity','Physical-transport Loewner monotonicity','New global status']}
a.out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
