# Project Euler Problem #5
import math

def prime_number(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n% i == 0:
             return False
    return True

def prime_number_list(num):
    lista = []
    for i in range(2, num):
        if prime_number(i) == True:
            lista.append(i)
    return lista

def smallest(num):
    primes = prime_number_list(num)
    result = 1
    for p in primes:
        i = 1
        # Encuentra la potencia maxima de cada numero primo para MCM
        while p**i < num:
            i += 1
        # Multiplica todas las potencias maximas
        result *= p**(i-1)
    return result

if __name__ == "__main__":
    print(smallest(20))

