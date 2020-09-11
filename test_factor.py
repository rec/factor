import unittest

import factor


class FactorTest(unittest.TestCase):
    def test_trivial(self):
        assert set(factor.factor(1)) == set()
        assert set(factor.factor(2)) == {2}
        assert set(factor.factor(3)) == {3}

    def test_two_way(self):
        for n in range(1, 1024):
            fl = factor.to_factor_list(n)
            n2 = factor.from_factor_list(fl)
            assert n == n2
