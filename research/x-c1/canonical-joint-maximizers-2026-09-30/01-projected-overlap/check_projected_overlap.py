"""Small exact operator example and rejection checks for the new certificate."""
from verify_projected_overlap import *

def point_matrix(a): return [[point(x) for x in row] for row in a]
def exact_product(a,b): return [[sum(x*y for x,y in zip(row,col)) for col in tr(b)] for row in a]
def contains_matrix(enclosure,exact):
    assert all(enclosure[i][j][0]<=x<=enclosure[i][j][1] for i,row in enumerate(exact) for j,x in enumerate(row))
def diagonal(xs): return [[x if i==j else F(0) for j in range(len(xs))] for i,x in enumerate(xs)]
def compress(u,d): return exact_product(exact_product(tr(u),diagonal(d)),u)
def must_reject(action):
    try: action()
    except (AssertionError,ValueError,ZeroDivisionError): return
    raise AssertionError('invalid input was accepted')

def main():
    a=[[F(2),F(1)],[F(1),F(3)]]
    ai=[[F(3,5),F(-1,5)],[F(-1,5),F(2,5)]]
    contains_matrix(inverse(point_matrix(a),positive_pivots=True),ai)
    print('Exact non-diagonal inverse: PASS')
    must_reject(lambda: div(point(1),(F(-1),F(1))))
    must_reject(lambda: sqrt_upper(F(-1)))
    must_reject(lambda: interval(['2','1']))
    must_reject(lambda: inverse(point_matrix([[F(1),F(1)],[F(1),F(1)]]),positive_pivots=True))
    print('Zero divisor, negative root, reversed interval, singular matrix rejected: PASS')
    # A real spectral measure with two critical and two complementary modes.
    # Low and high contributions do not commute in the two trial coordinates.
    p,t=F(99,101),F(20,101)
    u=[[p,F(0)],[F(0),p],[t*F(3,5),t*F(-4,5)],[t*F(4,5),t*F(3,5)]]
    q=[F(1,1000),F(1,500),F(2),F(3)]
    s=compress(u,q);ti=compress(u,[1/x for x in q])
    assert exact_product(s,ti)!=exact_product(ti,s)
    assert exact_product(tr(u),u)==[[F(1),F(0)],[F(0),F(1)]]
    hi=[[ti[i][j]+F(i==j,100) for j in range(2)] for i in range(2)]
    source={'trial_resolvent_lower':rational(point_matrix(ti)),
            'trial_resolvent_upper':rational(point_matrix(hi))}
    trial={'physical_Ritz_matrix':rational(point_matrix(s)),
           'physical_complement_gap_lower_exact':'2',
           'physical_trial_max_Rayleigh_upper_exact':str(norm_upper(point_matrix(s)))}
    result=moment_bound(source,trial)
    gp=compress(u,[F(1),F(1),F(0),F(0)])
    lp=compress(u,[q[0],q[1],F(0),F(0)])
    zp=compress(u,[1/q[0],1/q[1],F(0),F(0)])
    for key,value in [('projected_Gram',gp),('projected_energy',lp),('projected_inverse',zp)]:
        contains_matrix(result[key],value)
    dh=compress(u,[F(0),F(0),q[2],q[3]])
    for i in range(2):
        assert result['eta'][i]>=t
        assert result['high_energy_diagonal_upper'][i]>=dh[i][i]
    print('Noncommuting joint spectral measure: all projected moments and leakage bounds PASS')
    bad=dict(trial);bad['physical_complement_gap_lower_exact']='1/1000'
    must_reject(lambda:moment_bound(source,bad))
    print('Missing spectral separation rejected: PASS')
    print('ALL PROJECTED OVERLAP CHECKS PASS')

if __name__=='__main__':main()
