"""Exact finite polynomial geometry controls, not a whole model identification."""
from fractions import Fraction as Q
from math import comb

def coefficients(gamma, moments, *, inner):
    return [sum((Q(gamma[j]) * Q(comb(j, ell), 2**j) *
                 (1 + (-1)**(ell if inner else j-ell)) * Q(moments[j-ell])
                 for j in range(ell, len(gamma))), Q(0))
            for ell in range(len(gamma))]

def evaluate(co, x):
    return sum((a * Q(x)**k for k, a in enumerate(co)), Q(0))

def polynomial_circle_bound(coefficients, radius):
    radius = Q(radius)
    if radius <= 0:
        raise ValueError('Positive contour radius required')
    return sum((abs(Q(c)) * radius**k for k, c in enumerate(coefficients)), Q(0))

def controls():
    # Source f=1 on [1,2], Gamma(t)=-t/24, x=1/2.
    moments = [Q(1), Q(3, 2)]
    good = evaluate(coefficients([0, Q(-1, 24)], moments, inner=True), Q(1,2))
    old = evaluate(coefficients([0, Q(-1, 24)], moments, inner=False), Q(1,2))
    if (good, old, old-good) != (Q(-1,16), Q(-1,48), Q(1,24)):
        raise RuntimeError('Inner/outer signed kernel counterexample failed')
    # On the actual radius R=3, z^8 has sup 3^8, not 2^8.
    if polynomial_circle_bound([0]*8+[1],3) != 6561:
        raise RuntimeError('Contour radius regression')
    if polynomial_circle_bound([0]*8+[1],2) >= 6561:
        raise RuntimeError('Countercontrol no longer distinguishes the wrong radius')
    return {'inner_value':str(good),'old_inner_value':str(old),'signed_defect':str(old-good),
            'radius_3_degree_8_sup':'6561','radius_2_cannot_certify_radius_3':True}
