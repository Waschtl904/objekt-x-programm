"""Outward rational serialization, including exact decimal-grid boundaries."""
from fractions import Fraction as F
from flint import arb,arb_mat

def serial(v,digits=70):
    if isinstance(v,arb):
        s=10**digits
        # Multiplication by s is itself rounded. Take its directed endpoint
        # before applying floor/ceil, avoiding an ambiguous integer interval.
        lo=(v.lower()*s).lower().floor().unique_fmpz()
        hi=(v.upper()*s).upper().ceil().unique_fmpz()
        assert lo is not None and hi is not None,('non-finite scalar',str(v))
        return [str(F(int(lo),s)),str(F(int(hi),s))]
    if isinstance(v,arb_mat):return [[serial(v[i,j],digits) for j in range(v.ncols())] for i in range(v.nrows())]
    if isinstance(v,F):return str(v)
    if isinstance(v,dict):return {k:serial(x,digits) for k,x in v.items()}
    if isinstance(v,(tuple,list)):return [serial(x,digits) for x in v]
    return v
