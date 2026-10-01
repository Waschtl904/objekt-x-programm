"""Independent exact finite-operator controls for the transport identity."""
from pathlib import Path
from tempfile import TemporaryDirectory
from fractions import Fraction as F
import completion_math as e
import transport_math as tm
from verify_transport_gate import unpack,BASE,ARCHIVE

def positive2(a):assert a==e.trans(a) and a[0][0]>0 and a[0][0]*a[1][1]-a[0][1]**2>0
def main():
    # Genuine common operator, spectral projection and simultaneous q/L2 isometry.
    qb=[[F(x) if i==j else F(0) for j in range(4)] for i,x in enumerate([F(1,1000),F(1,2000),2,3])]
    p=F(39999,40001);s=F(400,40001);assert p*p+s*s==1
    j=[[p,0],[0,p],[s,0],[0,s]];qa=e.compressed(j,qb);ga=e.eye(2)
    assert qa[0][1]==0 and max(qa[i][i] for i in range(2))<F(17,9999)
    mix=[[F(3,5),F(-4,5)],[F(4,5),F(3,5)]]
    lowtrial=e.mm(mix,[[F(3,5),0],[0,F(5,13)]])
    ub=e.mm(lowtrial+[[F(4,5),0],[0,F(12,13)]],mix)
    assert e.compressed(j,e.eye(4))==e.eye(2) and e.compressed(ub,e.eye(4))==e.eye(2)
    vb=[row[:] if i<2 else [F(0),F(0)] for i,row in enumerate(ub)]
    gb=e.compressed(vb,e.eye(4));lb=e.compressed(vb,qb)
    assert e.mm(gb,lb)!=e.mm(lb,gb)
    y=e.mm(e.mm(e.trans(j),e.add(e.eye(4),e.scale(qb,F(1,17)))),vb)
    out=tm.transported_moments(y,ga,qa,gb,lb,F(1))
    high=[row[:] if i>=2 else [F(0),F(0)] for i,row in enumerate(j)]
    assert out['mass']==e.compressed(high,e.eye(4)) and out['energy']==e.compressed(high,qb)
    positive2(out['support_defect']);positive2(out['b_defect'])
    bb=e.add(gb,e.scale(lb,F(1,17)))
    low=e.mm(vb,e.mm(e.inv(bb),e.trans(y)))
    assert low==[row[:] if i<2 else [F(0),F(0)] for i,row in enumerate(j)]
    # Separate positivity and the b-Gram do not imply the high support condition.
    bad=tm.transported_moments([[F(9,10)]],[[F(1)]],[[F(1,100)]],[[F(1)]],[[F(1,1000)]],F(1))
    assert all(bad[k][0][0]>0 for k in ('mass','energy','b_defect'))
    assert bad['support_defect'][0][0]<0
    # All-positive diagonals can still violate the matrix inequality.
    test=[[F(1),F(2)],[F(2),F(1)]];w,val=tm.negative_vector(test,1)
    assert val<0 and all(test[i][i]>0 for i in range(2))
    raw=(BASE/'inputs'/ARCHIVE).read_bytes()
    with TemporaryDirectory() as temp:
        try:unpack(raw+b' ',Path(temp))
        except AssertionError as exc:assert 'hash mismatch' in str(exc)
        else:raise AssertionError('Tampered archive accepted')
    print('Exact noncommuting common operator, projection identities, separate-Gram negative control, off-diagonal witness and tamper rejection: PASS')
if __name__=='__main__':main()
