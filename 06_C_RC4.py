def ksa(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def prga(S, length):
    i = j = 0
    keystream = []

    for _ in range(length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        keystream.append(k)
    
    return keystream

def rc4_encrypt(key, plaintext):
    S = ksa(key)
    keystream = prga(S, len(plaintext))
    encrypted = bytes([keystream[i] ^ plaintext[i] for i in range(len(plaintext))])
    return encrypted

def rc4_decrypt(key, ciphertext):
    return rc4_encrypt(key, ciphertext)

if __name__ == "__main__":
    # Example usage
    key = b"SecretKey" # Key should be bytes
    plaintext = b"Hello, RC4!"
    print("Plaintext:", plaintext, "\nKey:", key, "\n")

    # Encrypt the data
    encrypted = rc4_encrypt(key, plaintext)
    print("Encryption:\nCiphertext:", encrypted.hex(), "\n")

    # Decrypt the data
    decrypted = rc4_decrypt(key, encrypted)
    print("Decryption:\nPlaintext:", decrypted.decode('utf-8'))
