import math

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_decrypt(ciphertext):
    ciphertext = ciphertext.upper()
    valid_a = [a for a in range(1, 26) if math.gcd(a, 26) == 1]

    for a in valid_a:
        inv_a = modinv(a, 26)
        for b in range(26):
            plaintext = ''
            for char in ciphertext:
                if char.isalpha():
                    decrypted = (inv_a * ((ord(char) - ord('A')) - b)) % 26
                    plaintext += chr(decrypted + ord('A'))
                else:
                    plaintext += char
            print(f'a={a}, b={b}: {plaintext}')

ciphertext = "WVZCPSCFZQCUUIMC" 
affine_decrypt(ciphertext)
