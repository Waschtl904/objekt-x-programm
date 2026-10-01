"""Exact finite constructions and transported moment constraints."""
from fractions import Fraction as F
import completion_math as e

def rotation_data(o,weights):
    n=e.annihilator(o);v=[[row[1]] for row in n];u=e.trans(e.mm([weights],o))
    assert e.mm(e.trans(u),v)==[[0]]
    k=e.sub(e.mm(u,e.trans(v)),e.mm(v,e.trans(u)))
    s=e.mm(e.trans(u),u)[0][0]*e.mm(e.trans(v),v)[0][0]
    assert k==e.scale(e.trans(k),-1)
    return k,e.mm(k,k),s

def cayley(data,t):
    k,k2,s=data;den=1+t*t*s/4;assert den>0
    q=e.add(e.add(e.eye(len(k)),e.scale(k,t/den)),e.scale(k2,t*t/(2*den)))
    assert e.mm(q,e.trans(q))==e.eye(len(k))
    return q

def transported_moments(y,ga,la,gb,lb,nu):
    ba=e.add(ga,e.scale(la,F(1,17)));bb=e.add(gb,e.scale(lb,F(1,17)))
    z=e.mm(y,e.inv(bb))
    low_mass=e.mm(e.mm(z,gb),e.trans(z))
    low_energy=e.mm(e.mm(z,lb),e.trans(z))
    mass=e.sub(ga,low_mass);energy=e.sub(la,low_energy)
    bdef=e.sub(ba,e.mm(z,e.trans(y)))
    assert e.add(energy,e.scale(mass,17))==e.scale(bdef,17)
    return {'mass':mass,'energy':energy,'b_defect':bdef,'support_defect':e.sub(energy,e.scale(mass,nu))}

def negative_vector(a,index=4):
    # A proposal obtained from a Schur pivot. The final quadratic form itself
    # is verified exactly, so no inferred sign of an interval pivot is used.
    left=[row[:index] for row in a[:index]];b=[[row[index]] for row in a[:index]]
    top=e.scale(e.mm(e.inv(left),b),-1)
    scale=10**12
    w=[[F((x[0]*scale).numerator//(x[0]*scale).denominator,scale)] for x in top]+[[F(1)]]+[[F(0)] for _ in range(len(a)-index-1)]
    value=e.compressed(w,a)[0][0];assert value<0
    return w,value
