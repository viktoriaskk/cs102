def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    # A = 65 Z = 90
    check = False
    letter = ''
    for symbol in plaintext:
 #       symbol = symbol.upper()
        if symbol.isupper():
            check = True
        else:
            check = False
        if (ord(symbol.upper()) > 64) and (ord(symbol.upper()) < 91):
            if ord(symbol.upper()) + 3 < 91:
                letter = chr(ord(symbol.upper()) + 3)
            else:
                letter = chr((ord(symbol.upper()) + 3)- 90 + 64)
            if check:
                ciphertext += letter
            else:
                ciphertext += letter.lower() 
        else:
            ciphertext += symbol
        
    return ciphertext
#print(encrypt_caesar("PYTHON"))

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    
    check = False
    letter = ''
    for symbol in ciphertext:
        if symbol.isupper():
            check = True
        else:
            check = False
        if (ord(symbol.upper()) > 64) and (ord(symbol.upper()) < 91):
            if ord(symbol.upper()) - 3 > 64:
                letter = chr(ord(symbol.upper()) - 3)
            else:
                letter = chr((ord(symbol.upper()) - 3)+ 90 - 64)
            if check:
                plaintext += letter
            else:
                plaintext += letter.lower() 
        else:
            plaintext += symbol

    return plaintext
#print(decrypt_caesar("Sbwkrq3.6"))