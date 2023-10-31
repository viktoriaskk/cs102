import unittest
from src.lab2.rsa import is_prime, gcd, multiplicative_inverse


class RsaTestCase(unittest.TestCase):

    def test_is_prime(self):
        ans = {
            2: True,
            11: True,
            8: False
        }
        for i in ans.keys():
            with self.subTest(i):
                self.assertEqual(is_prime(i), ans[i])

    def test_gcd(self):
        ans = {
            (12, 15): 3,
            (3, 7): 1
        }
        for i in ans.keys():
            with self.subTest(i):
                self.assertEqual(gcd(*i), ans[i])

    def test_multiplicative_inverse(self):
        ans = {
            (7, 40): 23
        }
        for i in ans.keys():
            with self.subTest(i):
                self.assertEqual(multiplicative_inverse(*i), ans[i])
