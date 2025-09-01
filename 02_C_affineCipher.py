# Function to find modular inverse
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Encryption
def affine_encrypt(text, a, b):
    result = ""
    for char in text.upper():
        if char.isalpha():
            x = ord(char) - ord('A')
            result += chr(((a * x + b) % 26) + ord('A'))
        else:
            result += char  # keep spaces/punctuation
    return result

# Decryption
def affine_decrypt(cipher, a, b):
    result = ""
    a_inv = mod_inverse(a, 26)  # multiplicative inverse of a
    for char in cipher.upper():
        if char.isalpha():
            y = ord(char) - ord('A')
            result += chr(((a_inv * (y - b)) % 26) + ord('A'))
        else:
            result += char
    return result


# Example Usage
if __name__ == "__main__":
    text = "HELLO WORLD"
    a, b = 5, 8   # keys (must have gcd(a,26)=1)

    encrypted = affine_encrypt(text, a, b)
    decrypted = affine_decrypt(encrypted, a, b)

    print("Original:", text)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
