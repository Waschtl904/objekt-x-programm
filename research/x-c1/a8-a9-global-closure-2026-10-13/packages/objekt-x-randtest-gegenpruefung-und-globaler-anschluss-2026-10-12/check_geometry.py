"""Independent exact geometry check: endpoint recurrence, not monomial integration."""
from fractions import Fraction as F
from pathlib import Path
import argparse, json

def log_atanh(z, count=160):
    lo = 2 * sum((z**(2*k+1)/F(2*k+1) for k in range(count)), F(0))
    return lo, lo + 2*z**(2*count+1)/((2*count+1)*(1-z*z))

def geometry(power=14, ncut=104):
    q=F(1,2**power); t=2*q-1
    vals=[F(1),t]
    for n in range(1,ncut):
        vals.append(((2*n+1)*t*vals[n]-n*vals[n-1])/(n+1))
    # (2n+1) integral P_n = P_(n+1)-P_(n-1); endpoint -1 cancels.
    integrals=[2*q]+[(vals[n+1]-vals[n-1])/(2*n+1) for n in range(1,ncut)]
    squares=[F(2*n+1,4)/q*v*v for n,v in enumerate(integrals)]
    mass=1-sum(squares)
    H=F(0); low=F(0)
    for n,v in enumerate(squares):
        if n: H+=F(1,n)
        low+=(H+F(11,10))*v
    ln2=log_atanh(F(1,3))
    minus_log_one_minus_q=log_atanh(q/(2-q))
    entropy=[power*x/2+(1-q)*y/(2*q) for x,y in zip(ln2,minus_log_one_minus_q)]
    energy=[F(11,10)+v-low for v in entropy]
    return integrals,squares,mass,energy

def rounded(x, up=False):
    scale=10**100
    v=x*scale
    floor=v.numerator//v.denominator
    return F(floor+(int(v.denominator!=1) if up else 0),scale)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    integrals,squares,mass,energy=geometry()
    assert F('0.522048329797')<mass<F('0.522048329799')
    assert F('3.71232003276')<energy[0]<energy[1]<F('3.71232003278')
    comparisons=0
    for path in sorted(args.input.glob('ENDPOINT_*_14_*.json')):
        d=json.loads(path.read_bytes())
        assert F(d['mass_outside'][0])<=mass<=F(d['mass_outside'][1])
        assert max(energy[0],F(d['L_outside_exact_model'][0]))<=min(energy[1],F(d['L_outside_exact_model'][1]))
        for n,interval in enumerate(d['step_projection_coefficients']):
            a,b=map(F,interval); assert a<=b
            assert a*b>0 and (a>0)==(integrals[n]>0)
            assert min(a*a,b*b)<=squares[n]<=max(a*a,b*b)
            comparisons+=1
    assert comparisons==416
    # Exact bound for a family of narrower steps. These are geometry only;
    # no new residual values or global upper bounds are asserted.
    family=[]
    for k in [14,18,22,26]:
        _,sq,m,e=geometry(k)
        q=F(1,2**k)
        assert sum(sq)<=104**2*q
        assert e[0]>= (sum((F(1,n) for n in range(1,105)),F(0))+F(11,10))*m
        family.append({'cut_power':k,'outside_mass_lower':str(rounded(m)),'outside_mass_upper':str(rounded(m,True)),'energy_lower':str(rounded(e[0])),'energy_upper':str(rounded(e[1],True)),'new_residual_integration':False})
    out={'status':'PASS_INDEPENDENT_ENDPOINT_RECURRENCE_AND_ENERGY',
         'coefficient_square_checks':comparisons,'mass_exact':str(mass),
         'energy_lower':str(rounded(energy[0])),'energy_upper':str(rounded(energy[1],True)),
         'family_geometry':family,'full_tail_upper_computed':False,
         'full_remainder_certified':False}
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(out['status']); print('mass',float(mass),'energy',float(energy[0]))
    for row in family:print('q=2^-'+str(row['cut_power']), 'mass',float(F(row['outside_mass_lower'])),'Eplus',float(F(row['energy_lower'])))

if __name__=='__main__':main()
