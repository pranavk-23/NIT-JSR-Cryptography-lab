def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():  # only shift alphabets
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char  # keep spaces/punctuation unchanged
    return result


plaintext = "NIT JSR"
key = 3

ciphertext = caesar_encrypt(plaintext, key)

print("Plaintext: ", plaintext)
print("Encrypted: ", ciphertext)
