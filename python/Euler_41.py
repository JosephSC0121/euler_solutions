from itertools import permutations
import math
def pandigital():
    digits = "123456789"  # Dígitos del 1 al 9
    pandigitl_number = []

    for i in range(1, 10):  # Longitud del número pandigital
        for perm in permutations(digits, i):
            numero = int("".join(perm))
            pandigitl_number.append(numero)
    return pandigitl_number[-100:]
def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primes():
    pandigitals = pandigital()
    for i in range(9876543220,0,-1):
        if i in pandigitals and prime(i):
            return i

if __name__ == "__main__":
    print(primes())
