def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
# A = 65 Z = 90
    correct_kword = ''
    check = 0
    for ind in range(len(plaintext)):
        correct_kword += keyword[check]
        check += 1
        if check == len(keyword):
            check = 0

    for i in range(len(correct_kword)):
        if plaintext[i].isupper():
            check = True
        else:
            check = False
        if (ord(plaintext[i].upper()) > 64) and (ord(plaintext[i].upper()) < 91):
            num = ord(correct_kword[i].upper()) - 65
            if ord(plaintext[i].upper()) + num > 90:
                letter = chr(ord(plaintext[i].upper()) + num - 90 + 64)
            else:
                letter = chr(ord(plaintext[i].upper()) + num)
            if check:
                ciphertext += letter
            else:
                ciphertext += letter.lower()    
        else:
            ciphertext += plaintext[i]
    return ciphertext
print(encrypt_vigenere("pYTHON", "A"))

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    
    correct_kword = ''
    check = 0
    for ind in range(len(ciphertext)):
        correct_kword += keyword[check]
        check += 1
        if check == len(keyword):
            check = 0

    for i in range(len(correct_kword)):
        if ciphertext[i].isupper():
            check = True
        else:
            check = False
        if (ord(ciphertext[i].upper()) > 64) and (ord(ciphertext[i].upper()) < 91):
            num = ord(correct_kword[i].upper()) - 65
            if ord(ciphertext[i].upper()) - num <= 64:
                letter = chr(ord(ciphertext[i].upper()) - num + 90 - 64)
            else:
                letter = chr(ord(ciphertext[i].upper()) - num)
            if check:
                plaintext += letter
            else:
                plaintext += letter.lower()    
        else:
            plaintext += ciphertext[i]
    return plaintext
#print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))