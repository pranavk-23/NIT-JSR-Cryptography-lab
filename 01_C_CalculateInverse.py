def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def mod_inverse(a, p):
    a %= p  # handle negatives or large a
    if a == 0:
        raise ValueError("0 has no multiplicative inverse modulo p.")
    g, x, _ = extended_gcd(a, p)
    if g != 1:
        # In GF(p) with prime p, this only happens if a == 0
        raise ValueError(f"{a} has no inverse modulo {p}.")
    return x % p  # make it a least nonnegative residue

# Example usage
p = 11
a = 3
inv = mod_inverse(a, p)
print(f"Inverse of {a} mod {p} is {inv}") 
