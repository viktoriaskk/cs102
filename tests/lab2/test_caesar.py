import unittest
from src.lab2.caesar import encrypt_caesar, decrypt_caesar


class CaesarTestCase(unittest.TestCase):

    def test_encrypt(self):
        ans = {
            'PYTHON': 'SBWKRQ',
            'python': 'sbwkrq',
            'Python3.6': 'Sbwkrq3.6',
            '': ''
        }
        for i in ans.keys():
            with self.subTest(i):
                self.assertEqual(encrypt_caesar(i), ans[i])

    def test_decrypt(self):
        ans = {
            'SBWKRQ': 'PYTHON',
            'sbwkrq': 'python',
            'Sbwkrq3.6': 'Python3.6',
            '': ''
        }
        for i in ans.keys():
            with self.subTest(i):
                self.assertEqual(decrypt_caesar(i), ans[i])
