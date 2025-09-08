def poly_add(a, b):
    return a ^ b   # XOR = addition mod 2


p1 = 0b1011   # x^3 + x + 1
p2 = 0b1101   # x^3 + x^2 + 1
print(bin(poly_add(p1, p2)))  # Result: 0b1110 (x^3 + x^2 + x)
