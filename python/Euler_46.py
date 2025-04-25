import math

def Erastotenes_crib(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(math.sqrt(n) + 1)):
        if is_prime[p]:
            for i in range(p*p, len(is_prime), p):
                is_prime[i] = False
    primes = [x for x in range(len(is_prime)) if is_prime[x]]
    return primes

def prime_number(n):
    for i in range(2,int(math.sqrt(n)) + 1 ):
        if n % i == 0:
            return False
    return True

def goldbach_conjeture():
    primes = Erastotenes_crib(10000)
    for i in range(10000):
        if i % 2 != 0 and not prime_number(i):
            found = False
            for num in primes:
                for mult in range(1, 100):
                    goldbach_num = num + 2 * mult**2
                    if i == goldbach_num:
                        found = True
                        break
                if found:
                    break
            if not found:
                return print(i)
                        
goldbach_conjeture()
