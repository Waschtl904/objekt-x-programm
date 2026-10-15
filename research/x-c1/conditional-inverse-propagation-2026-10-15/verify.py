"""Exact finite controls of PROOF.md; no arithmetic horizon certificate."""
from fractions import Fraction as F
import json


def mat(rows):
    return [[F(x) for x in row] for row in rows]


def eye(n):
    return mat([[int(i == j) for j in range(n)] for i in range(n)])


def tr(a):
    return list(map(list, zip(*a)))


def add(a, b, sign=1):
    return [[x + sign*y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def mul(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in tr(b)] for row in a]


def inv(a):
    n = len(a)
    b = [row[:] + unit for row, unit in zip(a, eye(n))]
    for k in range(n):
        j = next(j for j in range(k, n) if b[j][k])
        b[j], b[k] = b[k], b[j]
        d = b[k][k]
        b[k] = [v/d for v in b[k]]
        for j in range(n):
            if j != k:
                d = b[j][k]
                b[j] = [x-d*y for x, y in zip(b[j], b[k])]
    return [r[n:] for r in b]


def block(a, c, d):
    return [x+y for x, y in zip(a, c)] + [x+y for x, y in zip(tr(c), d)]


def psd(a, strict=False):
    if a != tr(a):
        return False
    b = [r[:] for r in a]
    for k in range(len(b)):
        pivot = b[k][k]
        if pivot < 0 or (strict and pivot == 0):
            return False
        if pivot == 0:
            if any(b[j][k] for j in range(k+1, len(b))):
                return False
            continue
        for i in range(k+1, len(b)):
            for j in range(k+1, len(b)):
                b[i][j] -= b[i][k]*b[k][j]/pivot
    return True


def majorant(u, h, v):
    hv = mul(h, v)
    return block(add(u, mul(hv, tr(h))), [[-x for x in row] for row in hv], v)


def successful(name, a, c, p, b, ugap, vgap, slack):
    a, c, p, b, ugap, vgap, slack = map(mat, (a, c, p, b, ugap, vgap, slack))
    ai, bi = inv(a), inv(b)
    u, v = add(ai, ugap), add(bi, vgap)
    assert psd(a, True) and psd(b, True)
    assert all(psd(x) for x in (ugap, vgap, slack))
    r = add(c, mul(a, p), -1)
    k = add(add(b, mul(tr(r), mul(u, r))), slack)
    d = add(add(add(k, mul(tr(p), c)), mul(tr(c), p)), mul(tr(p), mul(a, p)), -1)
    q = block(a, c, d)
    h = add(p, mul(u, r))
    exact_lower_inverse = majorant(u, h, bi)
    upper = majorant(u, h, v)
    assert psd(q, True)
    assert psd(add(upper, inv(q), -1))
    assert psd(add(upper, exact_lower_inverse, -1))
    lower = inv(exact_lower_inverse)
    assert psd(add(q, lower, -1))
    # Independently expand the completed square and the residual shear.
    ui = inv(u)
    assert lower == block(ui, mul(ui, h), add(b, mul(tr(h), mul(ui, h))))
    n, m = len(a), len(b)
    shear = [row + [-v for v in pr] for row, pr in zip(eye(n), p)]
    shear += [[F(0)]*n + row for row in eye(m)]
    assert mul(tr(shear), mul(q, shear)) == block(a, r, k)
    # Nonunitary physical coordinates: inverse must transform by congruence.
    j = eye(n+m)
    j[0][0], j[0][-1] = F(2), F(1, 3)
    ji = inv(j)
    qphys = mul(tr(ji), mul(q, ji))
    uphys = mul(j, mul(upper, tr(j)))
    assert psd(add(uphys, inv(qphys), -1))
    return {'name': name, 'result': 'ALGEBRA_CONTROL_PASS', 'dimension': n+m}


def main():
    cases = []
    for i, (a, c, p, b, ug, vg, sl) in enumerate([
        ([[2]], [[1]], [[F(1,3)]], [[3]], [[1]], [[2]], [[F(1,4)]]),
        ([[2,1],[1,3]], [[1,2],[3,-1]], [[1,0],[F(1,3),1]], [[3,1],[1,2]], [[1,1],[1,1]], [[1,0],[0,2]], [[0,0],[0,0]]),
        ([[2,1],[1,4]], [[1,2,3],[4,0,-2]], [[0,1,0],[1,0,1]], [[2,0,0],[0,3,1],[0,1,2]], [[1,0],[0,0]], [[0,0,0],[0,1,1],[0,1,1]], [[1,0,0],[0,0,0],[0,0,2]]),
        ([[2,1],[1,3]], [[2,1],[1,3]], [[1,0],[0,1]], [[2,1],[1,2]], [[1,0],[0,1]], [[0,0],[0,0]], [[0,0],[0,0]]),
        ([[3,1],[1,2]], [[1],[-1]], [[0],[0]], [[2]], [[0,0],[0,0]], [[1]], [[0]]),
        ([[2,0],[0,5]], [[1,1],[2,2]], [[0,0],[0,0]], [[1,0],[0,1]], [[1,1],[1,1]], [[1,1],[1,1]], [[0,0],[0,0]]),
        ([[F(1,10**30)]], [[F(1,10**15)]], [[10**15]], [[F(1,10**20)]], [[1]], [[1]], [[0]]),
        ([[1]], [[1]], [[1]], [[F(1,2)]], [[1]], [[0]], [[0]]),
    ]):
        cases.append(successful(['scalar','noncommuting','rectangular','exact_response',
                                'zero_response','rank_one_gaps','ill_conditioned','repaired_certificate'][i],
                               a,c,p,b,ug,vg,sl))
    q = mat([[1,1],[1,F(3,2)]])
    assert psd(q, True) and F(3,2)-2 < 0
    cases.append({'name':'comparison_failure_with_positive_form','result':'CERTIFICATE_FAIL'})
    qneg = mat([[1,1],[1,F(1,2)]])
    witness = mat([[-1],[1]])
    assert mul(tr(witness), mul(qneg,witness))[0][0] == -F(1,2)
    cases.append({'name':'actual_negative_witness','result':'MATHEMATICAL_FAIL'})
    u_bad = mat([[F(1,2)]])
    assert not psd(add(u_bad, mat([[1]]), -1))
    cases.append({'name':'underestimated_old_inverse','result':'INVALID_HYPOTHESIS_DETECTED'})
    correct = inv(q)
    wrong = [row[:] for row in correct]
    wrong[0][1] *= -1
    wrong[1][0] *= -1
    assert not psd(add(wrong, correct, -1))
    cases.append({'name':'wrong_inverse_cross_sign','result':'WRONG_FORMULA_DETECTED'})
    assert len(cases) == 12
    print(json.dumps({'scope':'finite rational algebra only', 'controls':cases,
                      'all_controls_passed':True, 'arithmetic_renewal_certified':False}, indent=2))


if __name__ == '__main__':
    main()
