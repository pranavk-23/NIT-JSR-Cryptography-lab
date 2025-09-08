def poly_mul(a, b):
    res = 0
    while b:
        if b & 1:  # if lowest bit of b is set
            res ^= a
        a <<= 1
        b >>= 1
    return res

def poly_mod(a, m):
    deg_m = m.bit_length() - 1
    while a.bit_length() - 1 >= deg_m:
        shift = a.bit_length() - m.bit_length()
        a ^= m << shift
    return a

# Example with irreducible polynomial x^4 + x + 1 (0b10011)
p1 = 0b1011   # x^3 + x + 1
p2 = 0b1101   # x^3 + x^2 + 1
m  = 0b10011  # modulus
product = poly_mul(p1, p2)
print("Product:", bin(product))
print("Modulo result:", bin(poly_mod(product, m)))
