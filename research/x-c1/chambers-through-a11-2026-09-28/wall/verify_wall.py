"""Exact supporting checks for the general C1a wall lemma and its q9 instance.

Python standard library only. No frequency sampling, no new terminal
positivity calculation. Infinite-dimensional arguments remain in PROOF.md.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb,factorial
import argparse,hashlib,json,subprocess

DIM=8
def const(x):return {(0,)*DIM:F(x)} if x else {}
def var(j):return {tuple(int(k==j) for k in range(DIM)):F(1)}
def add(a,b):
    c=dict(a)
    for k,v in b.items():c[k]=c.get(k,F(0))+v
    return {k:v for k,v in c.items() if v}
def scale(a,s):return {k:v*s for k,v in a.items() if v*s}
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
    c={}
    for i,x in a.items():
        for j,y in b.items():
            k=tuple(v+w for v,w in zip(i,j));c[k]=c.get(k,F(0))+x*y
    return {k:v for k,v in c.items() if v}
def power(a,n):
    result=const(1)
    for _ in range(n):result=mul(result,a)
    return result
def product(*args):
    result=const(1)
    for p in args:result=mul(result,p)
    return result
def log_bounds(q,n=220):
    q=F(q);assert q>=1
    z=(q-1)/(q+1);term=z;s=F(0)
    for k in range(n):s+=term/(2*k+1);term*=z*z
    return 2*s,2*(s+term/((2*n+1)*(1-z*z)))
def prime_power(q):
    for p in range(2,q+1):
        if any(p%d==0 for d in range(2,p)):continue
        value=p;k=1
        while value<q:value*=p;k+=1
        if value==q:return p,k
    return None
def active(threshold):return {q for q in range(2,12) if q<threshold and prime_power(q)}

# Separate exact one-variable polynomial arithmetic for physical source probes.
def tidy(a):
    a=list(a)
    while a and not a[-1]:a.pop()
    return a
def uadd(a,b):return tidy([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def uscale(a,s):return tidy([x*s for x in a])
def deriv(a):return tidy([i*a[i] for i in range(1,len(a))])
def umul(a,b):
    c=[F(0)]*max(0,len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return tidy(c)
def evalp(a,x):return sum((v*x**i for i,v in enumerate(a)),F(0))
def shifted(a,shift):
    b=[F(0)]*len(a)
    for n,v in enumerate(a):
        for k in range(n+1):b[k]+=v*comb(n,k)*(-shift)**(n-k)
    return tidy(b)
def source(radius,k):
    phi=[F(0)]*(2*k+1)
    for j in range(k+1):phi[2*j]=(-1)**j*comb(k,j)*radius**(2*(k-j))
    return phi,uadd(deriv(deriv(phi)),uscale(phi,-F(1,4)))
def correlate(u,r,v,s,ell):
    lo=max(-r,ell-s);hi=min(r,ell+s)
    if lo>=hi:return F(0)
    p=umul(u,shifted(v,ell))
    return sum((a*(hi**(k+1)-lo**(k+1))/(k+1) for k,a in enumerate(p)),F(0))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--repository',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args();here=Path(__file__).resolve().parent;checks=[]
    def check(label,condition):
        if not condition:raise AssertionError(label)
        checks.append(label)

    # Formal identities are checked as polynomials, not at sampled frequencies.
    g,k,omega,c,v,z,v2,z2=[var(j) for j in range(DIM)];one=const(1)
    m=sub(add(g,omega),c);n=add(add(k,omega),c);h=add(g,add(k,scale(omega,2)))
    w=sub(sub(g,k),scale(c,2))
    dm=mul(v,sub(one,z));dn=mul(v,add(one,z))
    mp=add(m,dm);np=add(n,dn);hp=add(h,scale(v,2));wp=sub(w,scale(mul(v,z),2))
    check('old coupled sum m+n=h',add(m,n)==h)
    check('new coupled sum m+n=h',add(mp,np)==hp)
    check('old full Gram difference',sub(power(m,2),power(n,2))==mul(h,w))
    check('new full Gram difference',sub(power(mp,2),power(np,2))==mul(hp,wp))
    check('form increment is exactly -2v cos',sub(wp,w)==scale(mul(v,z),-2))
    check('T all mixed terms retained',power(mp,2)==add(add(power(m,2),scale(mul(m,dm),2)),power(dm,2)))
    check('D all mixed terms retained',power(np,2)==add(add(power(n,2),scale(mul(n,dn),2)),power(dn,2)))
    dm2=mul(v2,sub(one,z2));dn2=mul(v2,add(one,z2))
    mpp=add(mp,dm2);npp=add(np,dn2);hpp=add(hp,scale(v2,2))
    wpp=sub(wp,scale(mul(v2,z2),2))
    check('two-wall m update is order independent',mpp==add(add(m,dm2),dm))
    check('two-wall n update is order independent',npp==add(add(n,dn2),dn))
    check('two-wall coupled Gram difference',sub(power(mpp,2),power(npp,2))==mul(hpp,wpp))
    check('two-wall interaction term retained',power(mpp,2).get((0,0,0,0,1,1,1,1))==2)

    # Squared multiplier cocycle; strict positivity in PROOF.md fixes root signs.
    a,b,d,ha,hb,hd=[var(j) for j in range(6)]
    lhs=product(power(d,2),hb,power(b,2),ha,power(a,2),hd)
    rhs=product(power(d,2),ha,power(b,2),hd,power(a,2),hb)
    check('formal squared T/D ratio telescoping for three arbitrary terminals',lhs==rhs)
    na,nb,ma,mb=[var(j) for j in range(4)]
    check('formal R and separate T/D intertwining after clearing denominators',
          product(nb,mb,na,ma)==product(nb,na,mb,ma))

    # The all-frequency proof is two inequalities on whole regions.
    r=var(0)
    check('universal low-frequency case ell^2=16-r, r>=0',
          sub(const(8),scale(sub(const(16),r),F(1,2)))==scale(r,F(1,2)))
    check('universal low-frequency case ell^2=16+r, r>=0',
          sub(scale(add(const(16),r),F(8,16)),scale(add(const(16),r),F(1,2)))=={})
    check('g0 minus 8xi^2 has nonnegative numerator on xi^2<=1/4',
          sub(scale(r,4),product(scale(r,8),add(const(F(1,4)),r)))==product(scale(r,2),sub(one,scale(r,4))))
    check('g0 minus 2 has nonnegative numerator on xi^2>=1/4',
          sub(scale(r,4),scale(add(const(F(1,4)),r),2))==scale(sub(r,const(F(1,4))),2))
    for ell,expected in [(F(0),F(1)),(F(4),F(1)),(F(5),F(25,16)),(F(10),F(25,4))]:
        check('C_ell parameter regression '+str(ell),max(F(1),ell*ell/16)==expected)
    x,s=var(0),var(1)
    check('Jensen function identity supporting derivatives',
          power(x,2)==add(sub(mul(x,add(x,s)),mul(s,add(x,s))),power(s,2)))
    gg,ss,vv=var(0),var(1),var(2)
    check('h/(h+2v) >= s/(s+2v) has numerator 2vg',
          sub(mul(add(gg,ss),add(ss,scale(vv,2))),mul(ss,add(add(gg,ss),scale(vv,2))))==scale(mul(vv,gg),2))

    l2,u2=log_bounds(2);l3,u3=log_bounds(3);l11,u11=log_bounds(11)
    check('log2 < 7/10',u2<F(7,10))
    check('sqrt8 > 14/5',F(14,5)**2<8)
    check('q8 weight < 1/4',u2/F(14,5)<F(1,4))
    check('q8 shift < 21/10 < 4',3*u2<F(21,10)<4)
    check('log3 between 1 and 11/10',l3>1 and u3<F(11,10))
    check('A9 < A11 < 6/5',u3<l11/2 and u11/2<F(6,5))
    check('q9 has prime base3 and exponent2',prime_power(9)==(3,2))
    check('q9 denominator sqrt9 equals3',3**2==9)
    check('q9 weight bound11/30',u3/3<F(11,30))
    check('q9 shift bound11/5 gives C_ell=1',2*u3<F(11,5)<4)
    check('strict endpoint A8 active family',active(F(8))=={2,3,4,5,7})
    check('strict endpoint A9 active family',active(F(9))=={2,3,4,5,7,8})
    check('q9 becomes active strictly to the right',active(F(19,2))=={2,3,4,5,7,8,9})
    check('10 is not a prime power',prime_power(10) is None)
    check('strict endpoint A11 excludes11',active(F(11))=={2,3,4,5,7,8,9})
    thresholds=[F(15,2),F(8),F(17,2),F(9),F(19,2),F(11)]
    triples=0
    for i,a0 in enumerate(thresholds):
        for j in range(i,len(thresholds)):
            for t in range(j,len(thresholds)):
                qa,qb,qc=active(a0),active(thresholds[j]),active(thresholds[t])
                assert (qb-qa).isdisjoint(qc-qb) and (qb-qa)|(qc-qb)==qc-qa
                triples+=1
    check('all56 ordered endpoint and interior triples route both walls consistently',triples==56)

    check('q8 regression lower square20/21',F(10)/(10+F(1,2))==F(20,21))
    check('q8 regression T/D upper5/4,11/10',1+F(1,4)==F(5,4) and 1+F(1,2)/5==F(11,10))
    check('new envelope191/15 below13',12+2*F(11,30)==F(191,15)<13)
    check('q9 lower square150/161',F(10)/(10+F(11,15))==F(150,161))
    check('q9 T upper41/30',1+F(11,30)==F(41,30))
    check('q9 D upper86/75',1+F(11,15)/5==F(86,75))
    check('sqrt11 < 10/3',11<F(10,3)**2)
    check('Gamma floor6/5',4/F(10,3)==F(6,5))
    theta=F(6,5)**2/(F(6,5)+13)
    check('T floor36/355',theta==F(36,355))
    check('source/T equivalence6071/36',1+17/theta==F(6071,36))
    check('R bound squared4615/36',13/theta==F(4615,36)>1)
    check('source norm17 remains positive through A11',17-13==4 and 17+13==30)
    total=F(1,4)+F(11,30)
    check('two-wall total increment37/60',total==F(37,60))
    check('two-wall lower square300/337',F(10)/(10+2*total)==F(300,337))
    check('two-wall T upper97/60',1+total==F(97,60))
    check('two-wall D upper187/150',1+2*total/5==F(187,150))
    check('direct bound improves product T upper',F(97,60)<F(5,4)*F(41,30))
    check('q3 third-chamber chain inequalities',3**2==9<11<3**3)
    check('q2 third-chamber chain inequalities',2**3==8<9<11<2**4)
    check('all other active shifts exceed A11',all(q*q>11 for q in [4,5,7,8,9]))

    for radius in [F(1),F(9,8)]:
        for degree in [3,4]:
            phi,u=source(radius,degree)
            for sign in [-1,1]:
                factor=uadd(deriv(phi),uscale(phi,-F(sign,2)))
                check(f'exact Mellin-annulling derivative identity r={radius}, k={degree}, sign={sign}',
                      uadd(deriv(factor),uscale(factor,F(sign,2)))==u)
            check(f'vanishing source boundary r={radius}, k={degree}',
                  all(evalp(a,x)==0 for x in [-radius,radius] for a in [phi,deriv(phi),u]))
    _,u=source(F(1),3);_,vprobe=source(F(1),4)
    for ell in [F(-5,2),F(-2),F(2),F(5,2)]:
        check('exact old cross-source support probe ell='+str(ell),correlate(u,F(1),vprobe,F(1),ell)==0)
    _,larger=source(F(9,8),3)
    check('larger support permits a nonzero new correlation',correlate(larger,F(9,8),larger,F(9,8),F(2))>0)

    bindings=json.loads((here/'SOURCE_BINDINGS.json').read_bytes())
    for row in bindings['copied_inputs']:
        check('preserved input '+row['path'],sha(here/row['path'])==row['sha256'])
    common=json.loads((here/'inputs/a9/common_reserve.json').read_bytes())
    reserve=json.loads((here/'inputs/a9/reserve_results.json').read_bytes())
    integer=json.loads((here/'inputs/a9/integer_results.json').read_bytes())
    manifest=dict((name,digest) for digest,name in (line.split('  ',1) for line in (here/'inputs/a9/SHA256SUMS').read_text().splitlines()))
    check('A9 common reserve binds original Arb receipt',common['reserve_results_sha256']==sha(here/'inputs/a9/reserve_results.json'))
    check('A9 independent input hashes agree with verified original manifest',all(manifest[name]==value for name,value in integer['input_hashes'].items()))
    check('A9 prior both-parity verdicts agree',reserve['both_parities_strictly_certified'] and integer['both_parities_certified'] and all(r['positive_directed_pivots']==296 for r in integer['parities'].values()))
    c9=F(common['common_physical_floor_exact']);eta9=F(common['common_defect_floor_exact'])
    check('A9 imported exact reserve conversion',c9==F(1,10**35) and eta9==c9/(c9+12))
    image=1/F(41,30)**2*eta9;strong=c9/(c9+13)
    check('q9 multiplier image reserve900/1681',image==F(900,1681)*eta9)
    check('q9 physical image reserve1/(13*10^35+1)',strong==F(1,13*10**35+1)>image)
    embedding=[F(1),F(0)];new_defect=[[eta9,F(0)],[F(0),F(-1)]]
    compressed=sum((embedding[i]*new_defect[i][j]*embedding[j] for i in range(2) for j in range(2)),F(0))
    check('positive compression does not exclude a negative complement',compressed==eta9>0 and new_defect[1][1]<0)
    main_data=json.loads((here/'MAIN_CHECK.json').read_bytes())
    check('reviewed Main diff binding',main_data['reviewed_changes_sha256']==sha(here/'inputs/REVIEWED_MAIN_CHANGES.json') and main_data['bound_input_paths_unchanged'])
    source_state='COPIED_INPUTS_VERIFIED_REPOSITORY_PINS_NOT_RECHECKED'
    if args.repository:
        for row in bindings['repository_inputs']:
            content=subprocess.check_output(['git','show',row['commit']+':'+row['path']],cwd=args.repository)
            check('pinned Git input '+row['label'],hashlib.sha256(content).hexdigest()==row['sha256'])
        source_state='ALL_LOCAL_AND_REPOSITORY_INPUTS_VERIFIED'
    result={'status':'GENERAL_SINGLE_WALL_AND_Q9_EXACT_CHECKS_PASS',
            'checks_passed':len(checks),'checks':checks,'source_bindings':source_state,
            'analytical_review':'EXTERNAL_REVIEW_OPEN',
            'new_result':'General raw finite-wall continuation for the fixed C1a family, including q9',
            'raw_concrete_scope':'1<=A<=B<=C<=A11=log(11)/2',
            'third_chamber_full_positivity':'OPEN','new_terminal_matrix_computation':False,
            'new_Arb_replay':False,'new_A9_integer_replay':False,
            'q9':{'weight_upper':'11/30','shift_upper':'11/5','lower_multiplier_squared':'150/161',
                  'T_upper':'41/30','D_upper':'86/75','source_T_floor':'36/355',
                  'source_norm_equivalence':'6071/36','R_squared_upper':'4615/36',
                  'old_image_defect_floor_exact':str(strong)},
            'two_wall':{'lower_multiplier_squared':'300/337','T_upper':'97/60','D_upper':'187/150'},
            'file_sha256':{name:sha(here/name) for name in ['PROOF.md','Q9.md','verify_wall.py','SOURCE_BINDINGS.json','MAIN_CHECK.json']},
            'repository_writes':False}
    output=args.output or here/'CHECK_RESULTS.json'
    output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['status','checks_passed','source_bindings','third_chamber_full_positivity']}))

if __name__=='__main__':main()
