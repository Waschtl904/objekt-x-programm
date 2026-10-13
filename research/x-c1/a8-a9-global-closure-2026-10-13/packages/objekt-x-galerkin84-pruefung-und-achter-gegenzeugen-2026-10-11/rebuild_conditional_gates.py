"""Rebuild R84 from C84 and the metric, then certify the conditional gates.

Requires python-flint 0.9.0. Does not evaluate new operator integrals.
The conditional matrices are constructed here; the saved diagnostic matrices
are used only for interval consistency checks.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json,sys

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True)
    ap.add_argument('--out',type=Path,default=Path('CONDITIONAL_GATE_REBUILD.json'))
    ap.add_argument('--deps',type=Path);args=ap.parse_args()
    if args.deps:sys.path.insert(0,str(args.deps.resolve()))
    from flint import arb,arb_mat,fmpq,ctx
    ctx.prec=512
    def af(x):
        q=F(x);return arb(fmpq(q.numerator,q.denominator))
    def box(v):return af(v[0]).union(af(v[1]))
    def mat(a):return arb_mat([[box(v) for v in r] for r in a])
    def rat(a):return arb_mat([[af(v) for v in r] for r in a])
    def eye(n):return arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
    def gram(c,g):return c.transpose()*g*c
    def subrows(a,l,h):return arb_mat([[a[i,j] for j in range(a.ncols())] for i in range(l,h)])
    def symmetric(a):return (a+a.transpose())/2
    def positive(a):
        a=symmetric(a);n=a.nrows();l=[[arb(0) for _ in range(n)] for _ in range(n)];ds=[]
        for j in range(n):
            d=a[j,j]-sum((l[j][k]**2*ds[k] for k in range(j)),arb(0))
            assert d>0,('positive pivot unproved',j,str(d))
            ds.append(d);l[j][j]=arb(1)
            for i in range(j+1,n):l[i][j]=(a[i,j]-sum((l[i][k]*l[j][k]*ds[k] for k in range(j)),arb(0)))/d
        return {'positive_pivots':n}
    def check_overlap(a,b):
        assert a.nrows()==b.nrows() and a.ncols()==b.ncols()
        for i in range(a.nrows()):
            for j in range(a.ncols()):assert a[i,j].overlaps(b[i,j]),(i,j)
        return a.nrows()*a.ncols()
    def read(p):return json.loads(p.read_bytes())
    root=args.root.resolve();task=root/'work/galerkin84-2026-10-10'
    bp=root/'work/inherited/Objekt-X-Unendlicher-Rest-Vergleich-2026-10-09/work/infinite-tail-2026-10-09/FINITE_BRIDGE.json'
    bridge=read(bp);diag=read(task/'BRIDGE_DIAGNOSTIC.json');cases=[]
    for p,label in enumerate(['EVEN','ODD']):
        gp=task/f'GALERKIN_{label}_3072.json';d=read(gp);c=mat(d['C84_model']);br=bridge['cases'][2+p]
        cp=root/f'work/inherited/Objekt-X-Endlicher-Schuranschluss-2026-10-09/work/gamma-low-2026-10-09/CERTIFICATE_{label}_gamma224_tight_4096.json'
        assert d['bindings']['inverse']==hashlib.sha256(cp.read_bytes()).hexdigest()
        assert d['bindings']['bridge']==hashlib.sha256(bp.read_bytes()).hexdigest()
        rho=af(read(cp)['rho']);cl=subrows(c,0,191);cz=subrows(c,191,195);cy=subrows(c,195,203)
        base=cl.transpose()*cl/(1-rho)+2*gram(cz,rat(br['N']).inv())
        r8=gram(cy,rat(br['Q8']).inv());r=base+r8
        checks={'R84_entries_rebuilt':check_overlap(r,mat(d['R84_model']))}
        b=af(F(9999999999,10**10))*rat(d['E84_centre_rational'])-mat(d['H84_model'])
        checks['B84_entries_rebuilt']=check_overlap(b,mat(d['B84_model']))
        opt=d['optional_positive_potential_comparison'];bplus=b+af(F(9999999999,10**10))*mat(opt['potential84_model'])
        proposal=diag['cases'][p];k=F(proposal['proposed_Q8_multiplier']);newr=base+r8/af(k)
        checks['conditional_R84_entries_rebuilt']=check_overlap(newr,mat(proposal['conditional_R84_model']))
        ep=box(opt['Bplus_operator_error_scalar']);er=box(d['R84_operator_error_scalar']);ell=F(proposal['finite_generalized_eigenvalue_upper'])
        checks['conditional_gate']=positive(bplus-newr-eye(84)*(ep+er))
        checks['conditional_eigenvalue_upper']=positive(af(ell)*bplus-newr-eye(84)*(af(ell)*ep+er))
        cases.append({'parity':label.lower(),'galerkin_sha256':hashlib.sha256(gp.read_bytes()).hexdigest(),
                      'proposed_multiplier':str(k),'conditional_eigenvalue_upper':str(ell),'checks':checks,
                      'stronger_bridge_proved':False,'full_remainder_certified':False})
        print(label,checks,flush=True)
    out={'status':'PASS_REBUILT_CONDITIONAL_FINITE_GATES','bits':ctx.prec,'cases':cases,
         'new_operator_integrations':False,'conditional_gate_does_not_prove_bridge':True,'full_remainder_certified':False}
    args.out.write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
