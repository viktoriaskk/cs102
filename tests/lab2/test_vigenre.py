import unittest
from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere


class VigenreTestCase(unittest.TestCase):

    def test_encrypt(self):
        ans = {
            ('PYTHON', 'A'): 'PYTHON',
            ('python', 'a'): 'python',
            ('ATTACKATDAWN', 'LEMON'): 'LXFOPVEFRNHR',
        }
        for i in ans.keys():
            with self.subTest(i):
                self.assertEqual(encrypt_vigenere(*i), ans[i])

    def test_decrypt(self):
        ans = {
            ('PYTHON', 'A'): 'PYTHON',
            ('python', 'a'): 'python',
            ('LXFOPVEFRNHR', 'LEMON'): 'ATTACKATDAWN',
        }
        for i in ans.keys():
            with self.subTest(i):
                self.assertEqual(decrypt_vigenere(*i), ans[i])
