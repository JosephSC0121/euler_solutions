import time, math

def Erastotenes_crib(n): # Criba de Erastótenes

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(math.sqrt(n)) + 1):
        if is_prime[p]:
            for i in range(p * p, len(is_prime), p):
                is_prime[i] = False
    return is_prime

def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n: 
            if n > 1: 
                factors.append(n)
            break
    return list(set(factors))

def phi(n):
    total = n
    prime_factor = prime_factors(n)
    
    for p in prime_factor:
        total *= (1-1/p)
        
    return total

def maxprimefactors(limit):
    total = 1
    primes = [i for (i, isprime) in enumerate(Erastotenes_crib(int(math.sqrt(limit)))) if isprime]
    for i in primes:
        if total * i > limit:
            break
        else:
            total *= i
    return total

if __name__ == "__main__":
    print(maxprimefactors(1000000))
