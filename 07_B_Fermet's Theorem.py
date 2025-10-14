import random

def power_mod(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result

def fermat_primality_test(n, k):
    if n <= 1:
        return False

    for _ in range(k):
        a = random.randint(2, n - 1)
        if power_mod(a, n - 1, n) != 1:
            return False
    return True

if __name__ == "__main__":
    p = 5
    a = 2
    print(fermat_primality_test(p, a))
