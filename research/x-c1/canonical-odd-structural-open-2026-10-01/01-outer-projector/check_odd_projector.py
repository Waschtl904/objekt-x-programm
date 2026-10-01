"""Exact tests of the measure, projector, physical metric and residual guard."""
from fractions import Fraction as F
from pathlib import Path
import tempfile
import completion_math as e
from verify_odd_projector import unpack,ARCHIVE

def pointbox(a): return [[[str(x),str(x)] for x in row] for row in a]
def norm2(a): return sum(x[0]**2 for x in a)
def trace(a): return sum(a[i][i] for i in range(len(a)))
def rayprojector(k,j):
    jk=e.mm(j,k);cov=e.mm(jk,e.trans(jk));d=trace(cov);assert d>0
    return e.scale(cov,1/d)
def residual_sin2_bound(residual_squared,vector_squared,mu_lower,lower_eigenvalue_upper):
    distance=mu_lower-lower_eigenvalue_upper
    if distance<=0:raise ValueError('upper eigenvalue not identified')
    return residual_squared/(vector_squared*distance**2)

def main():
    gp=[[F(4,5),F(1,10)],[F(1,10),F(3,4)]]
    lp=[[F(1,3),F(1,20)],[F(1,20),F(1,5)]];nu=F(3)
    assert e.mm(gp,lp)!=e.mm(lp,gp)
    h=e.sub(e.eye(2),gp);zp=e.mm(e.mm(gp,e.inv(lp)),gp)
    s=e.add(lp,e.scale(h,nu));t=e.add(zp,e.scale(h,1/nu))
    rebuilt=e.measure({'trial_resolvent_lower':pointbox(t),'trial_resolvent_upper':pointbox(t)},
                      {'physical_Ritz_matrix':pointbox(s),'physical_complement_gap_lower_exact':str(nu)})
    assert rebuilt['LP']==lp and rebuilt['GP']==gp and rebuilt['ZP']==zp

    c=[[F(2),F(0)],[F(1),F(3)]];cg=[[F(1),F(0)],[F(1,3),F(2)]]
    upper=[[F(3,5)],[F(4,5)]];pu=e.mm(upper,e.trans(upper))
    aw=e.add(e.scale(e.eye(2),F(2)),e.scale(pu,F(9)))
    m=e.mm(c,e.trans(c));r=e.mm(e.mm(c,aw),e.trans(c));t=e.mm(e.inv(m),r)
    k=e.sub(t,e.scale(e.eye(2),F(2)));pi=e.scale(k,F(1,9))
    assert e.mm(pi,pi)==pi and trace(pi)==1
    j=e.trans(cg);physical=e.mm(e.mm(j,e.trans(e.inv(c))),upper)
    expected=e.scale(e.mm(physical,e.trans(physical)),1/norm2(physical))
    pp=rayprojector(k,j);assert pp==expected and e.mm(pp,pp)==pp and trace(pp)==1
    lower=e.sub(e.scale(e.eye(2),F(11)),t)
    assert rayprojector(lower,j)!=pp

    y=[[F(3)],[F(4)]];mu=F(194,25);res=[[(F(2)-mu)*3],[(F(11)-mu)*4]]
    bound=residual_sin2_bound(norm2(res),norm2(y),mu,F(2))
    assert F(9,25)<=bound<1
    try:residual_sin2_bound(F(0),F(1),F(2),F(2))
    except ValueError:pass
    else:raise AssertionError('lower exact eigenvector mislabelled as upper')

    raw=(Path(__file__).resolve().parent/'inputs'/ARCHIVE).read_bytes()
    with tempfile.TemporaryDirectory(prefix='odd-projector-negative-') as tmp:
        try:unpack(raw+b' ',Path(tmp))
        except AssertionError as exc:assert 'hash mismatch' in str(exc)
        else:raise AssertionError('altered dependency accepted')
        assert not list(Path(tmp).iterdir())
    print('Noncommuting single measure, upper spectral projector, physical normalization, residual upper-mode guard and archive rejection: PASS')

if __name__=='__main__':main()
