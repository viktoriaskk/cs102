import unittest
from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere
import random 
import string

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

    def test_randomized(self):
        kwlen = random.randint(4, 24)
        keyword = ''.join(random.choice(string.ascii_letters) for _ in range(kwlen))
        plaintext = ''.join(random.choice(string.ascii_letters + ' -,')for _ in range(64))
        ciphertext = encrypt_vigenere(plaintext, keyword)
        self.assertEqual(plaintext, decrypt_vigenere(ciphertext, keyword))