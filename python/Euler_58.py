import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

def euler_58():
    diagonales = 1 
    primos = 0
    n = 1 

    while True:
        n += 2  

        for i in range(1, 4):
            val = n**2 - i*(n - 1)
            if is_prime(val):
                primos += 1
        diagonales += 4
        proporcion = primos / diagonales
        if proporcion < 0.10:
            return n  

print(euler_58())
