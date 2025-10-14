def power(base, expo, mod):
    result = 1
    base = base % mod
    while expo > 0:
        if expo % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        expo = expo // 2
    return result

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Brute-force modular inverse
def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1

# Generate RSA key pair (public and private)
def generate_keys():
    p = 7919
    q = 1009
    n = p * q
    phi = (p - 1) * (q - 1)

    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break

    d = mod_inverse(e, phi)
    return e, d, n

# "Signing" is encrypting hash/message with private key
def sign(message, private_key, n):
    return power(message, private_key, n)

# "Verification" is decrypting signature with public key
def verify(signature, public_key, n):
    return power(signature, public_key, n)

# Main authentication example
def main():
    # Sender generates RSA keys
    sender_public_key, sender_private_key, n = generate_keys()

    print(f"Sender's Public Key (e, n): ({sender_public_key}, {n})")
    print(f"Sender's Private Key (d, n): ({sender_private_key}, {n})")

    # Message to be sent
    message = 123  # Can be a hash of a real message
    print(f"\nOriginal Message: {message}")

    # Sender signs the message using their private key
    signature = sign(message, sender_private_key, n)
    print(f"Digital Signature (signed message): {signature}")

    # Receiver verifies using the sender's public key
    verified_message = verify(signature, sender_public_key, n)
    print(f"Verified Message: {verified_message}")

    # Check if verified message matches original
    if verified_message == message:
        print(" Signature is valid. Message is authenticated.")
    else:
        print(" Signature is invalid. Message is NOT authenticated.")

if __name__ == "__main__":
    main()
