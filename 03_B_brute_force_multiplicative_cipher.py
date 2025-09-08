import math 

def modinv(a):
    for x in range(1, 26):
        if (a * x) % 26 == 1:
            return x
    return None

def multiplicative_decrypt(ciphertext):
    ciphertext = ciphertext.upper()
    for key in range(1, 26):
        if math.gcd(key, 26) == 1:
            inv = modinv(key)
            if inv:
                plaintext = ''
                for char in ciphertext:
                    if char.isalpha():
                        decrypted = (inv * (ord(char) - ord('A'))) % 26
                        plaintext += chr(decrypted + ord('A'))
                    else:
                        plaintext += char
                print(f'Key {key} (inv {inv}): {plaintext}')

ciphertext = "WNYJCLHAPPVSPWI" 
multiplicative_decrypt(ciphertext)
