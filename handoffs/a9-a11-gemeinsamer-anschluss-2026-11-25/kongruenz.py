"""Interval certificate for a real symmetric matrix via a point preconditioner."""
from fractions import Fraction
from math import isqrt
from flint import arb, arb_mat, fmpz_mat


def positivity(A,high,gram_trace):
    n=A.nrows()
    candidate=A.mid()
    factor=arb_mat(n,n)
    pivots=[]
    for k in range(n):
        pivot=candidate[k,k].mid()
        if not pivot>0:
            return dict(positive=False,proved_pivots=0,candidate_pivots=k,
                        failed_candidate_pivot=pivot.str(16))
        root=pivot.sqrt().mid()
        factor[k,k]=root
        pivots.append(pivot)
        for i in range(k+1,n):
            factor[i,k]=(candidate[i,k]/root).mid()
        for i in range(k+1,n):
            for j in range(k+1,i+1):
                candidate[i,j]=(candidate[i,j]-factor[i,k]*factor[j,k]).mid()
    # The directed verdict only depends on this point matrix and the original balls.
    X=factor.inv().mid()
    assert all(X[i,i]>0 for i in range(n))
    for i in range(n):
        for j in range(i+1,n):
            X[i,j]=0
    B=X*A*X.transpose()
    diagonal_floor=min((B[i,i]-sum((abs(B[i,j]) for j in range(n) if j!=i),arb(0))).lower() for i in range(n))
    assert diagonal_floor>0
    inverse_norm_sq=sum((X[i,j]**2 for i in range(n) for j in range(i+1)),arb(0))
    floor=diagonal_floor/inverse_norm_sq
    assert floor>0
    joint=min(high.lower(),floor.lower())/(4*(1+gram_trace.sqrt()/high)**2)
    assert joint>0
    # Second verdict: point-integer simultaneous congruence and an exact
    # Gershgorin margin for a common rational Loewner minorant.
    scale=10**85
    F=fmpz_mat(n,n)
    S=fmpz_mat(n,n)
    for i in range(n):
        for j in range(i+1):
            scaled=A[i,j]*scale
            v=scaled.mid().floor().unique_fmpz()
            assert abs(scaled-arb(v))<2
            assert abs(A[j,i]*scale-arb(v))<2
            F[i,j]=F[j,i]=v
            S[i,j]=(X[i,j]*scale).mid().floor().unique_fmpz()
        assert S[i,i]>0
        F[i,i]-=2*n
    C=S*F*S.transpose()
    numerator=min(int(C[i,i])-sum(abs(int(C[i,j])) for j in range(n) if j!=i) for i in range(n))
    assert numerator>0
    s_squared=sum(int(S[i,j])**2 for i in range(n) for j in range(i+1))
    exact_floor=Fraction(numerator,scale*s_squared)
    norm_upper=isqrt(int(gram_trace.upper().ceil().unique_fmpz()))+1
    assert gram_trace<norm_upper**2
    rational_joint=min(Fraction(161,100),exact_floor)/(4*(1+norm_upper/Fraction(161,100))**2)
    assert rational_joint>Fraction("1e-55")
    def floor_decimal(q):
        return str((q.numerator*10**55)//q.denominator)+"e-55"
    return dict(positive=True,dimension=n,gershgorin_lower=diagonal_floor.str(15),
                finite_schur_floor_lower=floor.lower().str(15),
                gram_trace=gram_trace.str(15),joint_floor_display=joint.lower().str(15),
                exact_finite_lower=floor_decimal(exact_floor),
                exact_physical_lower=floor_decimal(rational_joint),
                exact_physical_above_1e_45=bool(rational_joint>Fraction("1e-45")),
                joint_above_1e_45=bool(joint>arb("1e-45")),
                joint_above_1e_55=bool(joint>arb("1e-55")))
