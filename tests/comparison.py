import unittest
import sys
sys.path.insert(1, '../src/gui')


from mem_dixy.tag.comparison import *


class check_comparison(unittest.TestCase):
    @classmethod
    def _add_token(cls, array):  # !<>=
        index = 0
        index |= EXCLAMATION_MARK in array
        index <<= 1
        index |= LESS_THAN_SIGN in array
        index <<= 1
        index |= GREATER_THAN_SIGN in array
        index <<= 1
        index |= EQUALS_SIGN in array
        return cls.all_encoding.get(index)

    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.all_encoding = {
            0x0: nu,  # ____
            0x1: eq,  # ___=
            0x2: gt,  # __>_
            0x3: ge,  # __>=
            0x4: lt,  # _<__
            0x5: le,  # _<_=
            0x6: ne,  # _<>_
            0x7: nu,  # _<>=
            0x8: nn,  # !___
            0x9: ne,  # !__=
            0xA: le,  # !_>_
            0xB: lt,  # !_>=
            0xC: ge,  # !<__
            0xD: gt,  # !<_=
            0xE: eq,  # !<>_
            0xF: nn   # !<>=
        }

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.all_encoding = {}

    def test__EMPTY(self):
        t = []
        self.assertIs(self._add_token(t), nu)

    def test__EQUALS_SIGN(self):
        t = [EQUALS_SIGN]
        self.assertIs(self._add_token(t), eq)

    def test__EQUALS_SIGN__EXCLAMATION_MARK(self):
        t = [EQUALS_SIGN, EXCLAMATION_MARK]
        self.assertIs(self._add_token(t), ne)

    def test__EQUALS_SIGN__EXCLAMATION_MARK__GREATER_THAN_SIGN(self):
        t = [EQUALS_SIGN, EXCLAMATION_MARK, GREATER_THAN_SIGN]
        self.assertIs(self._add_token(t), lt)

    def test__EQUALS_SIGN__EXCLAMATION_MARK__GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [EQUALS_SIGN, EXCLAMATION_MARK, GREATER_THAN_SIGN, LESS_THAN_SIGN]
        self.assertIs(self._add_token(t), nn)

    def test__EQUALS_SIGN__EXCLAMATION_MARK__LESS_THAN_SIGN(self):
        t = [EQUALS_SIGN, EXCLAMATION_MARK, LESS_THAN_SIGN]
        self.assertIs(self._add_token(t), gt)

    def test__EQUALS_SIGN__GREATER_THAN_SIGN(self):
        t = [EQUALS_SIGN, GREATER_THAN_SIGN]
        self.assertIs(self._add_token(t), ge)

    def test__EQUALS_SIGN__GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [EQUALS_SIGN, GREATER_THAN_SIGN, LESS_THAN_SIGN]
        self.assertIs(self._add_token(t), nu)

    def test__EQUALS_SIGN__LESS_THAN_SIGN(self):
        t = [EQUALS_SIGN, LESS_THAN_SIGN]
        self.assertIs(self._add_token(t), le)

    def test__EXCLAMATION_MARK(self):
        t = [EXCLAMATION_MARK]
        self.assertIs(self._add_token(t), nn)

    def test__EXCLAMATION_MARK__GREATER_THAN_SIGN(self):
        t = [EXCLAMATION_MARK, GREATER_THAN_SIGN]
        self.assertIs(self._add_token(t), le)

    def test__EXCLAMATION_MARK__GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [EXCLAMATION_MARK, GREATER_THAN_SIGN, LESS_THAN_SIGN]
        self.assertIs(self._add_token(t), eq)

    def test__EXCLAMATION_MARK__LESS_THAN_SIGN(self):
        t = [EXCLAMATION_MARK, LESS_THAN_SIGN]
        self.assertIs(self._add_token(t), ge)

    def test__GREATER_THAN_SIGN(self):
        t = [GREATER_THAN_SIGN]
        self.assertIs(self._add_token(t), gt)

    def test__GREATER_THAN_SIGN__LESS_THAN_SIGN(self):
        t = [GREATER_THAN_SIGN, LESS_THAN_SIGN]
        self.assertIs(self._add_token(t), ne)

    def test__LESS_THAN_SIGN(self):
        t = [LESS_THAN_SIGN]
        self.assertIs(self._add_token(t), lt)



if __name__ == '__main__':
    unittest.main()
