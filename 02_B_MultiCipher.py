from math import gcd

# Function to find modular inverse using Extended Euclidean Algorithm
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None  # if no inverse exists

def multiplicative_encrypt(plaintext, key):
    if gcd(key, 26) != 1:
        raise ValueError("Key must be coprime with 26 for decryption to work.")
    
    result = ""
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            P = ord(char) - base
            C = (P * key) % 26
            result += chr(C + base)
        else:
            result += char
    return result


def multiplicative_decrypt(ciphertext, key):
    if gcd(key, 26) != 1:
        raise ValueError("Key must be coprime with 26 for decryption to work.")
    
    inv_key = mod_inverse(key, 26)
    result = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            C = ord(char) - base
            P = (C * inv_key) % 26
            result += chr(P + base)
        else:
            result += char
    return result


# Example usage
plaintext = "HELLO"
key = 5 # valid since gcd(5, 26) = 1

ciphertext = multiplicative_encrypt(plaintext, key)
decrypted = multiplicative_decrypt(ciphertext, key)

print("Plaintext: ", plaintext)
print("Encrypted: ", ciphertext)
print("Decrypted: ", decrypted)
