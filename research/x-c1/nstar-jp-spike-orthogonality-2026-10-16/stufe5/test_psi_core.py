"""Regression for the core lift against the independently stored stage-2 source.

Run: python3 stufe5/test_psi_core.py (requires mpmath).
Extract only the two pure functions from l00.py so its historical workspace
paths and expensive full integration are not evaluated. No scalar certificate.
"""
import ast
import importlib.util
import json
from pathlib import Path
import unittest

import mpmath as mp

HERE = Path(__file__).resolve().parent
PACKAGE = HERE.parent


def load_core():
    source = ast.parse((HERE / 'l00.py').read_text(encoding='utf-8'))
    selected = []
    for name in ('legendre_all', 'psi_core'):
        matches = [node for node in ast.walk(source)
                   if isinstance(node, ast.FunctionDef) and node.name == name]
        assert len(matches) == 1, name
        selected.append(matches[0])
    namespace = {'mp': mp}
    exec(compile(ast.Module(body=selected, type_ignores=[]), 'l00.py', 'exec'), namespace)
    return namespace


class PsiCoreRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mp.mp.dps = 80
        spec = importlib.util.spec_from_file_location('stage2_psi', PACKAGE / 'stufe2/qnp_psi.py')
        cls.reference = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.reference)
        cls.reference.PSI_PATH = PACKAGE / 'stufe1/PSI_DEFINITION.json'
        cls.data = json.loads(cls.reference.PSI_PATH.read_text(encoding='utf-8'))
        cls.g = cls.reference.setup(80)

    def core(self, parity, direction):
        ns = load_core()
        p = self.data[parity]
        d = p['directions'][direction]
        sigma = p['sigma']
        a8 = self.g['a8']
        m = (lambda x: mp.cosh(x/2)) if sigma == 0 else (lambda x: mp.sinh(x/2))
        ns.update(a=self.g['b9'], sigma=sigma, m=m,
                  mu8=(mp.sinh(a8) + (-1)**sigma*a8)/2,
                  mu=(mp.mpf(4)/3 + (-1)**sigma*self.g['b9'])/2,
                  zdeg=p['core_z_degrees'], ratios=list(map(mp.mpf, p['core_z_moment_ratios'])),
                  kz=list(map(mp.mpf, d['core_k_mid'])), lam_total=mp.mpf(d['lambda_total_mid']))
        return ns

    def test_agrees_with_stage2_source(self):
        for parity in ('even', 'odd'):
            for direction in ('upper_v', 'lower_Pv'):
                ns = self.core(parity, direction)
                reference = self.reference.Psi(self.g, parity, direction)
                for numerator in (0, 1, 2, 4, 6, 7):
                    with self.subTest(parity=parity, direction=direction, point=numerator):
                        x = self.g['a8']*numerator/8
                        self.assertLess(abs(ns['psi_core'](x)-reference.core(x)), mp.mpf('1e-45'))

    def test_unit_lift_cancels_unit_shell_moment(self):
        for parity in ('even', 'odd'):
            with self.subTest(parity=parity):
                ns = self.core(parity, 'lower_Pv')
                ns.update(lam_total=mp.mpf(1), kz=[mp.mpf(0)]*4)
                core_moment = mp.quad(lambda x: ns['m'](x)*ns['psi_core'](x), [0, self.g['a8']])
                self.assertLess(abs(core_moment+1), mp.mpf('1e-70'))


if __name__ == '__main__':
    unittest.main()
