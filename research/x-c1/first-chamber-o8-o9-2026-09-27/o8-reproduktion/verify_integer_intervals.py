"""Standalone O8 certificate verifier using only the Python standard library.

No imports from the supplied generator/checkers or from Arb/FLINT. All
matrix arithmetic uses integer endpoints on a fixed decimal grid, with
outward rounding after multiplication and division. The full integral
model and its analytic interpretation remain inputs to this verifier.
"""
from pathlib import Path
from fractions import Fraction
from math import factorial,isqrt
from decimal import Decimal,localcontext
import argparse,gzip,hashlib,json,time


class Intervals:
    def __init__(self,digits):
        self.scale=10**digits
        self.zero=(0,0)
        self.one=(self.scale,self.scale)
    @staticmethod
    def ceildiv(n,d):return -((-n)//d)
    def fraction(self,x):
        x=Fraction(x)
        n=x.numerator*self.scale;d=x.denominator
        return n//d,self.ceildiv(n,d)
    def add(self,a,b):return a[0]+b[0],a[1]+b[1]
    def sub(self,a,b):return a[0]-b[1],a[1]-b[0]
    def mul(self,a,b):
        products=(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1])
        return min(products)//self.scale,self.ceildiv(max(products),self.scale)
    def square(self,a):
        lower=0 if a[0]<=0<=a[1] else min(a[0]*a[0],a[1]*a[1])
        return lower//self.scale,self.ceildiv(max(a[0]*a[0],a[1]*a[1]),self.scale)
    def div_positive(self,a,b):
        if b[0]<=0:raise ArithmeticError('Denominator interval is not strictly positive')
        pairs=((x*self.scale,y) for x in a for y in b)
        quotients=[(n//d,self.ceildiv(n,d)) for n,d in pairs]
        return min(x[0] for x in quotients),max(x[1] for x in quotients)
    def decode(self,pair,source_digits):
        lo,hi=map(int,pair)
        if lo>hi:raise ValueError('Reversed stored interval')
        factor=10**source_digits
        return (lo*self.scale)//factor,self.ceildiv(hi*self.scale,factor)


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def display(q):
    with localcontext() as context:
        context.prec=22
        return str(Decimal(q.numerator)/Decimal(q.denominator))


def gamma_residual_from_supplied_polynomial(data):
    """Validate the polynomial and its residual directly, without inversion code."""
    coefficients=[Fraction(x) for x in data['Gamma_polynomial_coefficients']]
    assert len(coefficients)==161
    # k_reg(2x)=(sech(x)+(1/(sinh(x)/x)-1)/x)/4.
    cosine_inverse=[4*coefficients[k] if k%2==0 else Fraction(0) for k in range(161)]
    sine_inverse=[Fraction(1)]+[4*coefficients[k-1] if k%2==0 else Fraction(0) for k in range(1,162)]
    denominators=[
        [Fraction(1,factorial(k)) if k%2==0 else Fraction(0) for k in range(257)],
        [Fraction(1,factorial(k+1)) if k%2==0 else Fraction(0) for k in range(257)]
    ]
    remainders=[]
    for numerator,denominator in zip((cosine_inverse,sine_inverse),denominators):
        terms={}
        for i,a in enumerate(numerator):
            if not a:continue
            for j,b in enumerate(denominator):
                if b:terms[i+j]=terms.get(i+j,Fraction(0))+a*b
        terms[0]-=1
        assert all(terms.get(k,0)==0 for k in range(len(numerator)))
        remainders.append({k:v for k,v in terms.items() if v})
    radius=Fraction(21,20)
    finite_cosine=sum((abs(v)*radius**k for k,v in remainders[0].items()),Fraction(0))
    finite_sine=sum((abs(v)*radius**(k-1) for k,v in remainders[1].items()),Fraction(0))
    cosine_size=sum((abs(v)*radius**k for k,v in enumerate(cosine_inverse)),Fraction(0))
    sine_size=sum((abs(v)*radius**k for k,v in enumerate(sine_inverse)),Fraction(0))
    cosine_tail=radius**258/Fraction(factorial(258))/(1-radius**2/Fraction(259*260))
    sine_tail_div_x=radius**257/Fraction(factorial(259))/(1-radius**2/Fraction(260*261))
    return (finite_cosine+finite_sine+cosine_size*cosine_tail+sine_size*sine_tail_div_x)/4


def check_rounding_operators():
    """Exercise signs, zero crossing, and directed rounding against Fractions."""
    arithmetic=Intervals(2)
    test_intervals=[(-319,-17),(-12,13),(0,0),(1,1),(17,329)]
    for a in test_intervals:
        for b in test_intervals:
            for operation,exact in (
                (arithmetic.add,lambda x,y:x+y),
                (arithmetic.sub,lambda x,y:x-y),
                (arithmetic.mul,lambda x,y:x*y)
            ):
                lo,hi=operation(a,b)
                for x in (Fraction(a[0],100),Fraction(a[1],100),Fraction(sum(a),200)):
                    for y in (Fraction(b[0],100),Fraction(b[1],100),Fraction(sum(b),200)):
                        assert Fraction(lo,100)<=exact(x,y)<=Fraction(hi,100)
            if b[0]>0:
                lo,hi=arithmetic.div_positive(a,b)
                for x in a:
                    for y in b:assert Fraction(lo,100)<=Fraction(x,y)<=Fraction(hi,100)
        lo,hi=arithmetic.square(a)
        for x in (*a,0) if a[0]<=0<=a[1] else a:
            assert Fraction(lo,100)<=Fraction(x,100)**2<=Fraction(hi,100)


def independent_ldl(matrix,arithmetic,progress):
    size=len(matrix)
    triangular=[[arithmetic.zero for _ in range(size)] for _ in range(size)]
    diagonal=[]
    for column in range(size):
        correction=arithmetic.zero
        for k in range(column):
            correction=arithmetic.add(correction,arithmetic.mul(arithmetic.square(triangular[column][k]),diagonal[k]))
        pivot=arithmetic.sub(matrix[column][column],correction)
        if pivot[0]<=0:raise ArithmeticError('Non-positive directed pivot '+str(column+1))
        diagonal.append(pivot)
        triangular[column][column]=arithmetic.one
        for row in range(column+1,size):
            correction=arithmetic.zero
            for k in range(column):
                product=arithmetic.mul(triangular[row][k],triangular[column][k])
                correction=arithmetic.add(correction,arithmetic.mul(product,diagonal[k]))
            triangular[row][column]=arithmetic.div_positive(arithmetic.sub(matrix[row][column],correction),pivot)
        if (column+1)%64==0 or column+1==size:progress(str(column+1)+' positive integer-interval pivots')
    inverse_trace=arithmetic.zero
    for column in range(size):
        vector=[arithmetic.zero]*size
        for row in range(column,size):
            acc=arithmetic.zero
            for k in range(column,row):
                acc=arithmetic.add(acc,arithmetic.mul(triangular[row][k],vector[k]))
            vector[row]=arithmetic.sub(arithmetic.one if row==column else arithmetic.zero,acc)
            inverse_trace=arithmetic.add(inverse_trace,arithmetic.div_positive(arithmetic.square(vector[row]),diagonal[row]))
    return diagonal,inverse_trace


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--package',type=Path,default=Path(__file__).resolve().parent.parent/'o8-rechenstand')
    parser.add_argument('--digits',type=int,default=120)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('integer_results.json'))
    args=parser.parse_args()
    if args.digits<110:raise ValueError('Use at least 110 decimal grid digits')
    arithmetic=Intervals(args.digits)
    folder=args.package.resolve()
    checks=[];log=[]
    def progress(message):
        log.append(message);print(message,flush=True)
    def check(label,condition):
        if not condition:raise AssertionError(label)
        checks.append(label)

    check_rounding_operators()
    check('signed interval primitives checked against exact rational endpoint and interior values',True)
    data=json.loads(gzip.decompress((folder/'a8_model.json.gz').read_bytes()))
    saved=json.loads(gzip.decompress((folder/'reserve_refined_lower_matrices.json.gz').read_bytes()))
    previous=json.loads((folder/'reserve_refined.json').read_bytes())
    tail=json.loads((folder/'refined_tail.json').read_bytes())
    common=json.loads((folder/'common_reserve.json').read_bytes())
    check('matrix model identity',sha(folder/'a8_model.json.gz')==previous['model_sha256'])
    check('generator identity',sha(folder/'generate_a8.py')==data['generator_sha256'])
    check('bound and checker identities',sha(folder/'rational_bounds.py')==data['bounds_source_sha256'] and sha(folder/'check_a8.py')==previous['checker_sha256'])
    check('tail and common result bindings',sha(folder/'refined_tail.json')==previous['refined_tail_binding_sha256'] and sha(folder/'refine_tail.py')==tail['source_sha256'] and sha(folder/'reserve_refined.json')==common['reserve_results_sha256'])
    check('endpoint and complete-model parameters',data['endpoint']=='3*log(2)/2' and data['exact_shift_relations']=={'d2':'2/3','d4':'4/3'} and data['Gamma_degree']==160 and data['cutoff']==383 and data['model_high_support_last_degree']==544)
    check('active family and integration cells',data['active_prime_powers']==[2,3,4,5,7] and len(data['positive_half_cells'])==5)
    check('100 decimal stored scales',data['scale_digits']==saved['scale_digits']==previous['scale_digits']==100)
    progress('Reconstructing the exact Gamma residual from the supplied polynomial')
    epsilon=gamma_residual_from_supplied_polynomial(data)
    check('Gamma residual independently recovered from polynomial',epsilon==Fraction(data['Gamma_kernel_error_exact']))
    gamma=Fraction(21,10)*epsilon
    eL=4*gamma
    check('low and Gamma operator errors reconstructed',gamma==Fraction(previous['Gamma_operator_error_exact']) and eL==Fraction(previous['low_form_error_exact']))
    raw=Fraction(6529,1000)-Fraction(491,200)-Fraction(858,3125)-Fraction(313,100)
    em_coarse=Fraction(1,10**6)
    margin=raw-16*em_coarse-12*em_coarse**2-Fraction(2,3)*(1+em_coarse**2)
    check('high-floor rational margin independently checked',raw==Fraction(2092,3125) and margin==Fraction(4135999981,1500000000000) and margin>0)
    check('sharper physical and T high floors',tail['high_physical_floor']=='2/3' and Fraction(2,3)/(Fraction(2,3)+Fraction(23,2))==Fraction(4,73))
    delta=Fraction(2,3)
    gram_coefficient=Fraction(3003,2000)
    common_physical=Fraction(12,10**30)
    common_defect=common_physical/(common_physical+Fraction(23,2))
    check('common reserve exact conversion',common_defect==Fraction(24,23*10**30+24) and common_defect>Fraction(1,10**30))
    results={
        'status':'INDEPENDENT_INTEGER_INTERVAL_CERTIFICATE_PASS',
        'arithmetic':'Python integers with exact outward rounding; standard library only',
        'grid_decimal_digits':args.digits,'checker_sha256':sha(Path(__file__)),
        'input_hashes':{name:sha(folder/name) for name in ('a8_model.json.gz','reserve_refined_lower_matrices.json.gz','reserve_refined.json','refined_tail.json','common_reserve.json')},
        'Gamma_residual_exact':str(epsilon),'high_floor_margin_exact':str(margin),
        'scope':'Independent certificate arithmetic on the delivered complete-model intervals; no independent reconstruction of the integral model or external analytic review',
        'imports_original_checker_or_generator':False,'uses_Arb_FLINT':False,
        'parities':{},'checks':checks,'github_writes':False
    }
    for parity,label in enumerate(('even','odd')):
        start=time.time();p=data['parities'][label]
        n=p['dimension']
        check(label+' dimension 191',n==191 and saved['parities'][label]['dimension']==191)
        first=384+parity;z=Fraction(21,40)
        em=z**first/factorial(first)/(1-z*z/Fraction((first+1)*(first+2)))
        if parity:em*=4
        eB=2*gamma+24*em
        check(label+' Mellin and coupling errors reconstructed',em==Fraction(previous['parities'][label]['high_mellin_correction_exact']) and eB==Fraction(previous['parities'][label]['coupling_operator_error_exact']))
        loss=eL+Fraction(3003,2)*eB**2
        loss_interval=arithmetic.fraction(loss)
        model_low=[[arithmetic.decode(v,100) for v in row] for row in p['A']]
        model_gram=[[arithmetic.decode(v,100) for v in row] for row in p['complete_model_raw_high_Gram']]
        matrix=[[arithmetic.decode(v,100) for v in row] for row in saved['parities'][label]['lower_matrix']]
        check(label+' matrix dimensions complete',all(len(m)==n and all(len(row)==n for row in m) for m in (model_low,model_gram,matrix)))
        check(label+' symmetric stored interval matrices',all(m[i][j]==m[j][i] for m in (model_low,model_gram,matrix) for i in range(n) for j in range(i)))
        contained=True
        for i in range(n):
            for j in range(n):
                formed=arithmetic.sub(model_low[i][j],arithmetic.mul(arithmetic.fraction(gram_coefficient),model_gram[i][j]))
                if i==j:formed=arithmetic.sub(formed,loss_interval)
                contained=contained and matrix[i][j][0]<=formed[0]<=formed[1]<=matrix[i][j][1]
        check(label+' every stored lower-matrix interval encloses the independently rebuilt sufficient matrix',contained)
        progress(label+': checking all stored matrix intervals with independent LDL')
        pivots,inverse_trace=independent_ldl(matrix,arithmetic,lambda message:progress(label+': '+message))
        check(label+' all 191 independently computed pivot intervals strictly positive',len(pivots)==191 and min(x[0] for x in pivots)>0)
        check(label+' inverse trace interval strictly positive',inverse_trace[0]>0)
        sigma=arithmetic.div_positive(arithmetic.one,inverse_trace)
        sigma_lower=Fraction(sigma[0],arithmetic.scale)
        # Only an upper coupling-norm bound is needed for the norm conversion.
        b2_upper=sum((Fraction(int(p['complete_model_raw_high_Gram'][i][i][1]),10**100) for i in range(n)),Fraction(0))*Fraction(1001,1000)+n*1001*eB**2
        check(label+' upper squared coupling bound positive',b2_upper>0)
        b2_interval=arithmetic.fraction(b2_upper)
        root=isqrt(b2_interval[1]*arithmetic.scale)
        if root*root<b2_interval[1]*arithmetic.scale:root+=1
        b_upper=Fraction(root,arithmetic.scale)
        check(label+' square root norm bound checked by exact squaring',b_upper*b_upper>=b2_upper)
        denominator=4*(1+b_upper/delta)**2
        physical=min(sigma_lower,delta)/denominator
        defect=physical/(physical+Fraction(23,2))
        check(label+' independently recovered common physical reserve',physical>common_physical)
        check(label+' independently recovered common defect reserve',defect>common_defect>Fraction(1,10**30))
        results['parities'][label]={
            'dimension':n,'positive_directed_pivots':len(pivots),
            'all_pivot_intervals_integer_grid':[[str(a),str(b)] for a,b in pivots],
            'inverse_trace_integer_grid':[str(x) for x in inverse_trace],
            'sigma_lower_exact':str(sigma_lower),'sigma_lower_display':display(sigma_lower),
            'coupling_norm_upper_exact':str(b_upper),
            'physical_lower_exact':str(physical),'physical_lower_display':display(physical),
            'defect_lower_exact':str(defect),'defect_lower_display':display(defect),
            'seconds':time.time()-start
        }
        progress(label+': lower bounds approximately '+display(physical)+' physical; '+display(defect)+' defect')
    results['checks_passed']=len(checks)
    results['both_parities_certified']=True
    results['common_physical_floor_exact']=str(common_physical)
    results['common_defect_floor_exact']=str(common_defect)
    args.output.write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
    progress(str(len(checks))+' grouped checks PASS; both complete 191D certificates independently reproduced')
    args.output.with_suffix('.log').write_text('\n'.join(log)+'\n',encoding='utf-8')


if __name__=='__main__':main()
