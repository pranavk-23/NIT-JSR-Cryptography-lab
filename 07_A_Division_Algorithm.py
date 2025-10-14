def is_prime(n):
    if n <= 1:
        return False
    
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":
    flag = True
    while flag:
        num = input("input a number: ")
        try:
            num = int(num)
            flag = False
        except:
            print("Error: Only integers allowed.")

    if is_prime(num):
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")
