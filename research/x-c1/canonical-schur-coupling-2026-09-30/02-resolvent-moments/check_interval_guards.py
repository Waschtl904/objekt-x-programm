"""Regression checks for interval edge cases encountered during development."""
from flint import arb,arb_mat
from resolvent_moments import dotcol,nonnegative_upper,square_bounds,gupper

def rejected(function,arg):
 try:function(arg)
 except AssertionError:return
 raise AssertionError('A nonfinite or invalid interval was accepted')

x=arb(0,arb('1e-80'))
assert dotcol(arb_mat([[x]]),0).is_finite()
lo,hi=square_bounds(x)
assert lo==0 and hi>0
rejected(nonnegative_upper,arb('nan'))
rejected(nonnegative_upper,arb(-1))
rejected(gupper,arb_mat([[arb(1),arb('nan')],[arb('nan'),arb(1)]]))
print('Five interval edge-case checks PASS')
