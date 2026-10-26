"""Exact negative controls against promoting unrelated one-direction tests."""
from fractions import Fraction as Q
from pathlib import Path
import json
H=Path(__file__).resolve().parent
# Equal residual images: each diagonal test passes, their common direction fails.
n=Q(4,5);individual=n*n;trace=2*n*n
assert individual<1<trace
# Correlated finite metric, opposite residual images. Omitting inverse
# off-diagonal entries would conceal the exact negative joint direction.
C=[[Q(1),Q(9,10)],[Q(9,10),Q(1)]]
A=[[Q(100,19),Q(-90,19)],[Q(-90,19),Q(100,19)]]
n=Q(1,4)
diagonal_only=sum(A[i][i]*n*n for i in range(2))
complete=sum(abs(A[i][j])*n*n for i in range(2)for j in range(2))
assert diagonal_only<1<complete and complete==Q(5,4)
z=[Q(1),Q(-1)];gap=sum(z[i]*C[i][j]*z[j]for i in range(2)for j in range(2));residual=(2*n)**2
assert residual>gap
out={'status':'EXACT_NEGATIVE_CONTROLS_PASS','individual_success_joint_failure_detected':True,
 'inverse_metric_mixed_terms_required':True,'second_example_diagonal_only':str(diagonal_only),
 'second_example_complete_budget':str(complete),'scope':'Algebraic gate controls, not a replay of physical research data.'}
(H/'JOINT_REST_LEMMA_CONTROLS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out,indent=2))
