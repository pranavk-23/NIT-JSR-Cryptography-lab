# Advance Encryption Standard (AES)
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

def pad(data):
    block_size = AES.block_size
    padding = block_size - (len(data) % block_size)
    return data + bytes([padding] * padding)

def unpad(data):
    padding = data[-1]
    return data[:-padding]

def aes_encrypt(key, data):
    cipher = AES.new(key, AES.MODE_CBC)
    padded_data = pad(data)
    encrypted_data = cipher.encrypt(padded_data)
    return cipher.iv + encrypted_data

def aes_decrypt(key, encrypted_data):
    iv = encrypted_data[:AES.block_size]
    data = encrypted_data[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted_data = cipher.decrypt(data)
    unpadded_data = unpad(decrypted_data)
    return unpadded_data

if __name__ == "__main__":
    flag = True
    while(flag):
        key_size = input("Input Key Size (16, 24 and 32): ")
        try:
            key_size = int(key_size)
        except:
            print("Error: Only Integers are supported.")
            continue

        if key_size == 16 or key_size == 24 or key_size == 32:
            flag = False
        else:
            print("Error: Supported Key Size are 16, 24 and 32 only.")

    key = get_random_bytes(key_size)

    data = b"Hello, AES!"

    encrypted_data = aes_encrypt(key, data)

    decrypted_data = aes_decrypt(key, encrypted_data)

    print("Plaintext:", data, "\n")
    print("Key:", key, "\n")
    print("Encryption:")
    print("Ciphertext:", encrypted_data, "\n")
    print("Decryption:")
    print("Plaintext:", decrypted_data)
