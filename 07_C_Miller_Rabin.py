import random

def negative_mod(x, n):
    reminder = x % n
    return reminder-n

def step1(n):
    n = n-1

    k = 1
    while (n % pow(2, k) != 0):
        k += 1
    
    # print("k:", k, "m:", n//pow(2, k))
    return k, n//pow(2, k)

def step2(n):
    # return random.randint(1, n-1)
    return 2

def step3(n, m, a, k):
    T = pow(a, m) % n
    T_negative = negative_mod(pow(a, m), n)

    if T == 1 or T_negative == -1:
        return True
    
    for i in range(0, k):
        x = T 
        T = pow(x, 2) % n
        T_negative = negative_mod(pow(x, 2), n)

        if T == 1:
            return False
        
        if T_negative == -1:
            return True
        
    return False

def miller_rabin(n):
    k, m = step1(n)
    a = step2(n)
    x = step3(n, m, a, k)
    return x

if __name__ == "__main__":
    flag = True
    while flag:
        n = input("Input n: ")
        try:
            n = int(n)
            flag = False
        except:
            print("Error: Please input a number.")

    x = miller_rabin(n)
    if x :
        print("Prime")
    else :
        print("Composite")
